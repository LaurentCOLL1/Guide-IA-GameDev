from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

FORBIDDEN_DIRS = {".godot", "__pycache__", ".venv", "venv", "node_modules"}
FORBIDDEN_SUFFIXES = {
    ".exe", ".dll", ".so", ".dylib", ".bin", ".zip", ".7z", ".tar",
    ".gz", ".sqlite", ".sqlite3", ".db", ".pck",
}
SECRET_PATTERNS = [
    r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY",
    r"ghp_[A-Za-z0-9]{20,}",
    r"sk-[A-Za-z0-9]{20,}",
]
PERSONAL_DATA_PATTERNS = [
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    r"\b(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}\b",
]
REQUIRED = [
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "manifest.json",
    "catalog.json",
    "DEPENDENCIES.json",
    "LICENSE-STATUS.md",
    "PROVENANCE.json",
    "sql/migrations/manifest.json",
    "sql/migrations/001_create_beacon_state.sql",
    "sql/migrations/002_add_beacon_activation_event.sql",
    "sql/migrations/003_add_content_documents.sql",
    "sql/migrations/004_add_derived_cache.sql",
    "data/synthetic/asteria-fixture.json",
    "python/src/asteria_database/__init__.py",
    "python/tests/test_migrations.py",
    "python/tests/test_repositories.py",
    "python/tests/test_backup_restore.py",
    "python/tests/test_validation_synthetic.py",
    "tools/init_database.py",
    "tools/backup_database.py",
    "tools/restore_database.py",
    "tools/validate_database.py",
    "docs/API.md",
    "docs/SCHEMA.md",
    "docs/INTEGRATION.md",
    "docs/BOUNDARIES.md",
    "qa/AUDIT-DATABASE-LIBRARY.md",
    "qa/VALIDATION-DATABASE-LIBRARY.yaml",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_python(path: Path, errors: list[str]) -> None:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        errors.append(f"python-syntax:{path}:{exc.lineno}:{exc.msg}")


def validate_migrations(root: Path, errors: list[str]) -> dict[str, int]:
    manifest = load_json(root / "sql/migrations/manifest.json")
    migrations = manifest.get("migrations", [])
    versions = [int(item.get("version", -1)) for item in migrations]
    if versions != list(range(1, len(migrations) + 1)):
        errors.append(f"migration-sequence:{versions}")
    if int(manifest.get("latest_version", -1)) != len(migrations):
        errors.append("migration-latest-version-mismatch")
    names: set[str] = set()
    for item in migrations:
        name = str(item.get("name", ""))
        rel = str(item.get("path", ""))
        if not name or name in names:
            errors.append(f"migration-name:{name}")
        names.add(name)
        path = root / rel
        if not path.is_file():
            errors.append(f"missing-migration:{rel}")
            continue
        payload = path.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != str(item.get("sha256", "")):
            errors.append(f"migration-checksum:{rel}")
        text = payload.decode("utf-8")
        if re.search(r"\b(BEGIN|COMMIT|ROLLBACK)\b", text, re.IGNORECASE):
            errors.append(f"transaction-control-inside-migration:{rel}")
        if not sqlite3.complete_statement(text):
            errors.append(f"incomplete-sql:{rel}")
    return {
        "migration_count": len(migrations),
        "latest_version": int(manifest.get("latest_version", -1)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing:{rel}")

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    package_manifest = load_json(root / "manifest.json")
    catalog = load_json(root / "catalog.json")
    if package_manifest.get("version") != version:
        errors.append("manifest-version-mismatch")
    if catalog.get("pack_version") != version:
        errors.append("catalog-version-mismatch")

    migration_stats = validate_migrations(root, errors)

    fixture = load_json(root / "data/synthetic/asteria-fixture.json")
    if fixture.get("schema_version") != 1:
        errors.append("synthetic-schema-version")
    if "No personal data" not in str(fixture.get("notice", "")):
        errors.append("synthetic-notice")

    source_files: list[str] = []
    python_files = 0
    sql_files = 0
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in FORBIDDEN_DIRS for part in rel.parts):
            errors.append(f"forbidden-directory:{rel}")
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden-binary-or-database:{rel}")
        source_files.append(str(rel))
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-utf8:{rel}")
            continue
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text):
                errors.append(f"possible-secret:{rel}")
        if "synthetic" not in str(rel).lower():
            for pattern in PERSONAL_DATA_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    warnings.append(f"possible-personal-data-review:{rel}")
        if path.suffix == ".py":
            python_files += 1
            parse_python(path, errors)
        if path.suffix == ".sql":
            sql_files += 1

    report = {
        "status": "success" if not errors else "failure",
        "pack_version": version,
        "source_files": len(source_files),
        "python_files": python_files,
        "sql_files": sql_files,
        "migration_count": migration_stats["migration_count"],
        "latest_schema_version": migration_stats["latest_version"],
        "errors": errors,
        "warnings": warnings,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        return 1
    print(
        "DATABASE_LIBRARY_STATIC: PASS "
        f"({len(source_files)} files, "
        f"{migration_stats['migration_count']} migrations)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
