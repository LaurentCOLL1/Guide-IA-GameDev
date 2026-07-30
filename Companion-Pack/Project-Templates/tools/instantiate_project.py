#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
COMMON_ROOT = PACK_ROOT / "templates" / "common"
PROFILE_ROOT = PACK_ROOT / "templates" / "profiles"
PACK_VERSION = (PACK_ROOT / "VERSION").read_text(encoding="utf-8").strip()

PROJECT_ID_RE = re.compile(r"^[a-z][a-z0-9_]{2,63}$")
OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,38})$")
TOKEN_RE = re.compile(r"__[A-Z0-9_]+__")

PROFILES = {
    "solo": {
        "review_mode": "delayed_self_review",
        "required_reviewers": 0,
        "release_approval": "self_review",
    },
    "studio": {
        "review_mode": "independent_review",
        "required_reviewers": 1,
        "release_approval": "independent_approver",
    },
}

def slugify(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = normalized.strip("-")
    if not normalized:
        raise ValueError("project name does not produce a usable slug")
    return normalized[:64]

def iter_source_files(source_root: Path):
    for path in sorted(source_root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink is forbidden in templates: {path}")
        if path.is_file():
            yield path

def render_text(text: str, tokens: dict[str, str]) -> str:
    for key, value in tokens.items():
        text = text.replace(key, value)
    return text

def copy_overlay(source_root: Path, output_root: Path, tokens: dict[str, str]) -> None:
    for source in iter_source_files(source_root):
        relative = source.relative_to(source_root)
        rendered_relative = Path(render_text(relative.as_posix(), tokens))
        target = output_root / rendered_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        target.write_text(render_text(text, tokens), encoding="utf-8")

def assert_no_unresolved_tokens(output_root: Path) -> None:
    errors: list[str] = []
    for path in sorted(output_root.rglob("*")):
        if not path.is_file() or ".godot" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        match = TOKEN_RE.search(text)
        if match:
            errors.append(f"{path.relative_to(output_root)}: {match.group(0)}")
    if errors:
        raise ValueError("unresolved tokens:\n" + "\n".join(errors))

def main() -> int:
    parser = argparse.ArgumentParser(description="Instantiate a Solo or Studio Godot project.")
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--owner-handle", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not PROJECT_ID_RE.fullmatch(args.project_id):
        parser.error("--project-id must be snake_case, 3 to 64 characters")
    if not OWNER_RE.fullmatch(args.owner_handle):
        parser.error("--owner-handle must be a Git-compatible account or organization name")

    output = args.output.resolve()
    if output.exists():
        if not args.force:
            parser.error(f"output already exists: {output}")
        shutil.rmtree(output)
    output.mkdir(parents=True)

    profile = PROFILES[args.profile]
    project_slug = slugify(args.project_name)
    tokens = {
        "__PROJECT_NAME__": args.project_name.strip(),
        "__PROJECT_ID__": args.project_id,
        "__PROJECT_SLUG__": project_slug,
        "__PROFILE_ID__": args.profile,
        "__OWNER_HANDLE__": args.owner_handle,
        "__REVIEW_MODE__": profile["review_mode"],
        "__REQUIRED_REVIEWERS__": str(profile["required_reviewers"]),
        "__RELEASE_APPROVAL__": profile["release_approval"],
    }

    copy_overlay(COMMON_ROOT, output, tokens)
    copy_overlay(PROFILE_ROOT / args.profile, output, tokens)

    manifest_path = output / "project-template.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["template_pack_version"] = PACK_VERSION
    manifest["required_reviewers"] = profile["required_reviewers"]
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    assert_no_unresolved_tokens(output)
    print(json.dumps({
        "status": "success",
        "profile": args.profile,
        "project_id": args.project_id,
        "output": str(output),
        "template_pack_version": PACK_VERSION,
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
