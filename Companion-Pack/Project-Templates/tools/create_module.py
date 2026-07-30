#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = PACK_ROOT / "module-template"
MODULE_ID_RE = re.compile(r"^[a-z][a-z0-9_]{2,47}$")
TOKEN_RE = re.compile(r"__[A-Z0-9_]+__")
UID_ALPHABET = "abcdefghijklmnopqrstuvwxyz23456789"

def pascal_case(value: str) -> str:
    return "".join(part.capitalize() for part in value.split("_") if part)

def uid_for(label: str) -> str:
    number = int.from_bytes(hashlib.sha256(label.encode("utf-8")).digest()[:8], "big")
    chars: list[str] = []
    for _ in range(13):
        chars.append(UID_ALPHABET[number % len(UID_ALPHABET)])
        number //= len(UID_ALPHABET)
    return "uid://" + "".join(chars)

def render(value: str, tokens: dict[str, str]) -> str:
    for key, replacement in tokens.items():
        value = value.replace(key, replacement)
    return value

def main() -> int:
    parser = argparse.ArgumentParser(description="Create a layered Godot module.")
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--module-id", required=True)
    parser.add_argument("--display-name", required=True)
    args = parser.parse_args()

    project = args.project.resolve()
    if not (project / "project.godot").is_file():
        parser.error("--project must point to a generated Godot project")
    if not MODULE_ID_RE.fullmatch(args.module_id):
        parser.error("--module-id must be snake_case, 3 to 48 characters")

    project_manifest = json.loads((project / "project-template.json").read_text(encoding="utf-8"))
    project_id = str(project_manifest["project_id"])
    module_class = pascal_case(args.module_id)
    if not module_class:
        parser.error("--module-id does not produce a class prefix")

    target_root = project / "src" / "features" / args.module_id
    if target_root.exists():
        parser.error(f"module already exists: {target_root}")

    tokens = {
        "__MODULE_ID__": args.module_id,
        "__MODULE_CLASS__": module_class,
        "__MODULE_DISPLAY_NAME__": args.display_name.strip(),
    }

    source_root = MODULE_ROOT / "__MODULE_ID__"
    created: list[str] = []
    for source in sorted(source_root.rglob("*.tmpl")):
        relative = source.relative_to(source_root)
        rendered_relative = render(relative.as_posix(), tokens)
        if not rendered_relative.endswith(".tmpl"):
            raise RuntimeError(f"unexpected module template name: {relative}")
        rendered_relative = rendered_relative[:-5]
        target = target_root / rendered_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        text = render(source.read_text(encoding="utf-8"), tokens)
        unresolved = TOKEN_RE.search(text)
        if unresolved:
            raise RuntimeError(f"unresolved token {unresolved.group(0)} in {source}")
        target.write_text(text, encoding="utf-8")
        created.append(target.relative_to(project).as_posix())
        if target.suffix == ".gd":
            uid_path = target.with_suffix(target.suffix + ".uid")
            uid_path.write_text(
                uid_for(f"{project_id}:{target.relative_to(project).as_posix()}") + "\n",
                encoding="utf-8",
            )
            created.append(uid_path.relative_to(project).as_posix())

    modules_path = project / "modules.json"
    modules = json.loads(modules_path.read_text(encoding="utf-8"))
    modules["modules"].append({
        "module_id": args.module_id,
        "display_name": args.display_name.strip(),
        "source": "CP-PACK-02 module-template",
        "test_script": f"res://src/features/{args.module_id}/tests/test_{args.module_id}.gd",
    })
    modules["modules"] = sorted(modules["modules"], key=lambda item: item["module_id"])
    modules_path.write_text(
        json.dumps(modules, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": "success",
        "module_id": args.module_id,
        "created": sorted(created),
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
