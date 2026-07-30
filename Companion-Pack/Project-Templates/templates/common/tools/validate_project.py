#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "project.godot",
    "project-template.json",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "src/core/bootstrap_report.gd",
    "src/features/bootstrap/main.gd",
    "src/features/bootstrap/main.tscn",
    "src/features/example_feature/README.md",
    "src/composition/project_composition.gd",
    "tests/run_tests.gd",
    "docs/adr/0000-template.md",
    "docs/adr/0001-project-profile.md",
    "docs/governance/branch-policy.md",
    "docs/governance/responsibilities.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
]
TOKEN_RE = re.compile(r"__(?:PROJECT|PROFILE|OWNER|REVIEW|REQUIRED|RELEASE)_[A-Z_]+__")

def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".godot" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".ogg", ".wav"}:
            continue
        text = path.read_text(encoding="utf-8")
        if TOKEN_RE.search(text):
            errors.append(f"unresolved token: {path.relative_to(ROOT)}")
        if "\r\n" in text:
            errors.append(f"CRLF line endings: {path.relative_to(ROOT)}")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"trailing whitespace: {path.relative_to(ROOT)}:{line_number}")
    manifest_path = ROOT / "project-template.json"
    if manifest_path.is_file():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if data.get("profile") not in {"solo", "studio"}:
            errors.append("invalid profile in project-template.json")
        if data.get("hidden_dependencies") != []:
            errors.append("hidden_dependencies must be empty")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PROJECT_TEMPLATE_STATIC: PASS ({len(REQUIRED)} required files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
