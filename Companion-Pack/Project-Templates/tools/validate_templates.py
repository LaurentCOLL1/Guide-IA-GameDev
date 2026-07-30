#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TOKENS = {
    "__PROJECT_NAME__",
    "__PROJECT_ID__",
    "__PROJECT_SLUG__",
    "__PROFILE_ID__",
    "__OWNER_HANDLE__",
    "__REVIEW_MODE__",
    "__REQUIRED_REVIEWERS__",
    "__RELEASE_APPROVAL__",
    "__MODULE_ID__",
    "__MODULE_CLASS__",
    "__MODULE_DISPLAY_NAME__",
}
TOKEN_RE = re.compile(r"__[A-Z0-9_]+__")
FORBIDDEN_PARTS = {".godot", "__pycache__", ".venv", "secrets", "credentials"}
FORBIDDEN_SUFFIXES = {".exe", ".dll", ".so", ".dylib", ".zip", ".7z", ".png", ".jpg", ".jpeg", ".ogg", ".wav"}

REQUIRED_PACK_FILES = [
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "manifest.json",
    "DEPENDENCIES.json",
    "PROVENANCE.json",
    "LICENSE-STATUS.md",
    "template-schema.json",
    "tools/instantiate_project.py",
    "tools/instantiate_project.ps1",
    "tools/create_module.py",
    "tools/validate_templates.py",
    "templates/common/project.godot",
    "templates/common/src/features/bootstrap/main.tscn",
    "templates/profiles/solo/config/profile.json",
    "templates/profiles/studio/config/profile.json",
    "templates/profiles/studio/.github/CODEOWNERS",
    "module-template/__MODULE_ID__/module.json.tmpl",
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".godot" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()

def run(*args: str) -> None:
    subprocess.run(args, check=True, text=True)

def inspect_sources(errors: list[str]) -> dict[str, int]:
    files = 0
    text_files = 0
    for path in sorted(PACK_ROOT.rglob("*")):
        if not path.is_file():
            continue
        files += 1
        relative = path.relative_to(PACK_ROOT)
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            errors.append(f"forbidden path part: {relative}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden bundled binary or media: {relative}")
            continue
        text_files += 1
        text = path.read_text(encoding="utf-8")
        if "\r\n" in text:
            errors.append(f"CRLF line endings: {relative}")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"trailing whitespace: {relative}:{line_number}")
        residual = text
        for allowed in ALLOWED_TOKENS:
            residual = residual.replace(allowed, "")
        for token in TOKEN_RE.findall(residual):
            errors.append(f"unknown template token {token}: {relative}")
    return {"files": files, "text_files": text_files}

def validate_generated(project: Path, profile: str, errors: list[str]) -> None:
    run(sys.executable, str(project / "tools" / "validate_project.py"))
    manifest = json.loads((project / "project-template.json").read_text(encoding="utf-8"))
    profile_data = json.loads((project / "config" / "profile.json").read_text(encoding="utf-8"))
    if manifest.get("profile") != profile:
        errors.append(f"{profile}: project-template profile mismatch")
    if profile_data.get("profile_id") != profile:
        errors.append(f"{profile}: profile.json mismatch")
    codeowners = project / ".github" / "CODEOWNERS"
    if profile == "studio" and not codeowners.is_file():
        errors.append("studio: CODEOWNERS missing")
    if profile == "solo" and codeowners.exists():
        errors.append("solo: CODEOWNERS should not be materialized")
    if profile_data.get("hidden_dependencies"):
        errors.append(f"{profile}: hidden dependencies declared")
    if profile_data.get("local_ai_required") is not False:
        errors.append(f"{profile}: local AI must remain optional")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    for rel in REQUIRED_PACK_FILES:
        if not (PACK_ROOT / rel).is_file():
            errors.append(f"missing pack file: {rel}")

    stats = inspect_sources(errors)
    generated: dict[str, dict[str, str]] = {}

    with tempfile.TemporaryDirectory(prefix="project-templates-") as temp:
        temp_root = Path(temp)
        for profile in ("solo", "studio"):
            first = temp_root / f"{profile}-first"
            second = temp_root / f"{profile}-second"
            command = [
                sys.executable,
                str(PACK_ROOT / "tools" / "instantiate_project.py"),
                "--profile", profile,
                "--project-name", f"Asteria {profile.title()} Sample",
                "--project-id", f"asteria_{profile}_sample",
                "--owner-handle", "example-owner",
            ]
            run(*command, "--output", str(first))
            run(*command, "--output", str(second))
            validate_generated(first, profile, errors)
            validate_generated(second, profile, errors)
            first_digest = tree_digest(first)
            second_digest = tree_digest(second)
            if first_digest != second_digest:
                errors.append(f"{profile}: generation is not deterministic")

            run(
                sys.executable,
                str(PACK_ROOT / "tools" / "create_module.py"),
                "--project", str(first),
                "--module-id", "inventory_demo",
                "--display-name", "Inventaire de démonstration",
            )
            module_root = first / "src" / "features" / "inventory_demo"
            if not (module_root / "module.json").is_file():
                errors.append(f"{profile}: module manifest missing")
            module_uids = list(module_root.rglob("*.gd.uid"))
            if len(module_uids) != 5:
                errors.append(f"{profile}: expected 5 generated module UIDs, got {len(module_uids)}")
            validate_generated(first, profile, errors)
            generated[profile] = {
                "project_tree_sha256": first_digest,
                "module_tree_sha256": tree_digest(module_root),
            }

    report = {
        "schema_version": 1,
        "pack_id": "CP-PACK-02-PROJECT-TEMPLATES",
        "status": "success" if not errors else "failure",
        "source_files": stats["files"],
        "text_files": stats["text_files"],
        "profiles": generated,
        "errors": errors,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if errors:
        print("\n".join(errors))
        return 1
    print(
        "PROJECT_TEMPLATES_STATIC: PASS "
        f"({stats['files']} files, Solo and Studio deterministic)"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
