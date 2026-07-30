#!/usr/bin/env python3
"""Static validator for the Documentation Library."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
ID_RE = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)+$")
SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
BINARY_SUFFIXES = {".pdf", ".docx", ".epub", ".zip", ".7z", ".rar", ".exe", ".dll"}


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected object")
    return data


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated YAML front matter")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError(f"{path}: front matter must be an object")
    return data


def validate_markdown(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if "\ufeff" in text:
        errors.append(f"{path}: BOM forbidden")
    if TOKEN_RE.search(text):
        errors.append(f"{path}: unresolved placeholder")
    if text.count("\n# ") + (1 if text.startswith("# ") else 0) != 1:
        errors.append(f"{path}: exactly one H1 required")
    if "Repères d’utilisation" not in text:
        errors.append(f"{path}: usage markers missing")
    if "à compléter" in text.lower() or "tbd" in text.lower():
        errors.append(f"{path}: unfinished marker")
    try:
        meta = front_matter(path)
    except Exception as exc:
        errors.append(str(exc))
        return
    for key in ("title", "id", "status", "version", "lang", "usage-context-standard"):
        if key not in meta:
            errors.append(f"{path}: missing {key}")
    if "id" in meta and not ID_RE.fullmatch(str(meta["id"])):
        errors.append(f"{path}: invalid id")
    if "version" in meta and not SEMVER_RE.fullmatch(str(meta["version"])):
        errors.append(f"{path}: invalid version")
    if meta.get("usage-context-standard") != "DOC-V0-ANN-CONTEXTES":
        errors.append(f"{path}: wrong usage context standard")


def validate_schema_shape(schema: dict, data: dict, path: Path, errors: list[str]) -> None:
    for key in schema.get("required", []):
        if key not in data:
            errors.append(f"{path}: missing required key {key}")
    props = schema.get("properties", {})
    for key, rule in props.items():
        if key not in data:
            continue
        value = data[key]
        if "const" in rule and value != rule["const"]:
            errors.append(f"{path}: {key} must equal {rule['const']}")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{path}: {key} not allowed")
        if "pattern" in rule and not re.fullmatch(rule["pattern"], str(value)):
            errors.append(f"{path}: {key} does not match pattern")


def validate(root: Path) -> dict:
    errors: list[str] = []
    required = [
        "README.md", "VERSION", "manifest.json", "catalog.json",
        "schemas/front-matter.schema.json", "schemas/qa-proof.schema.json",
        "examples/generation-plan.json", "scripts/generate_document.py",
        "scripts/validate_documentation_library.py", "qa/AUDIT-DOCUMENTATION-LIBRARY.md",
        "qa/VALIDATION-DOCUMENTATION-LIBRARY.yaml",
    ]
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    manifest = load_json(root / "manifest.json")
    catalog = load_json(root / "catalog.json")
    if manifest.get("version") != "1.0.0":
        errors.append("manifest version mismatch")
    entries = catalog.get("entries")
    if not isinstance(entries, list) or len(entries) < 12:
        errors.append("catalog must contain at least 12 entries")
        entries = []
    for entry in entries:
        path = root / str(entry.get("path", ""))
        if not path.is_file():
            errors.append(f"catalog path missing: {path}")
    if len({entry.get("id") for entry in entries}) != len(entries):
        errors.append("catalog ids must be unique")

    templates = sorted((root / "templates").rglob("*"))
    templates = [p for p in templates if p.is_file()]
    examples = sorted((root / "examples/filled").rglob("*"))
    examples = [p for p in examples if p.is_file()]
    if len(templates) != 13:
        errors.append(f"expected 13 templates, found {len(templates)}")
    if len(examples) != 10:
        errors.append(f"expected 10 filled examples, found {len(examples)}")

    for path in templates:
        text = path.read_text(encoding="utf-8")
        if not TOKEN_RE.search(text):
            errors.append(f"{path}: template has no placeholder")
        if path.suffix == ".md" and "Repères d’utilisation" not in text:
            errors.append(f"{path}: template usage markers missing")

    front_schema = load_json(root / "schemas/front-matter.schema.json")
    qa_schema = load_json(root / "schemas/qa-proof.schema.json")
    for path in examples:
        if path.suffix == ".md":
            validate_markdown(path, errors)
            try:
                validate_schema_shape(front_schema, front_matter(path), path, errors)
            except Exception:
                pass
        elif path.suffix in {".yaml", ".yml"}:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                errors.append(f"{path}: YAML object required")
            else:
                validate_schema_shape(qa_schema, data, path, errors)
            if TOKEN_RE.search(path.read_text(encoding="utf-8")):
                errors.append(f"{path}: unresolved placeholder")

    checksums = load_json(root / "checksums.json")
    for rel, expected in checksums.get("files", {}).items():
        path = root / rel
        if not path.is_file():
            errors.append(f"checksum path missing: {rel}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"checksum mismatch: {rel}")

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in BINARY_SUFFIXES:
            errors.append(f"forbidden binary artifact: {path}")
        if path.is_file() and path.stat().st_size > 500_000:
            errors.append(f"oversized file: {path}")

    return {
        "status": "success" if not errors else "failure",
        "pack_version": manifest.get("version"),
        "source_files": sum(1 for p in root.rglob("*") if p.is_file()),
        "template_count": len(templates),
        "filled_example_count": len(examples),
        "catalog_entries": len(entries),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text + "\n", encoding="utf-8")
    print(text)
    if result["status"] == "success":
        print(f"DOCUMENTATION_LIBRARY_STATIC: PASS ({result['source_files']} files)")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
