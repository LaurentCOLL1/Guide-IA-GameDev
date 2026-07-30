#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = PROJECT_ROOT.parent

REQUIRED_PROJECT_FILES = (
    "project.godot",
    ".gitignore",
    ".gitattributes",
    "README.md",
    "src/core/bootstrap_report.gd",
    "src/features/bootstrap/main.gd",
    "src/features/bootstrap/main.tscn",
    "tests/run_tests.gd",
    "docs/.gdignore",
    "docs/environment/godot-reference.json",
)

REQUIRED_PACK_FILES = (
    "README.md",
    "CHANGELOG.md",
    "VERSION",
    "LICENSE-STATUS.md",
    "PROVENANCE.json",
    "DEPENDENCIES.json",
    "manifest.json",
    "environments/solo/profile.json",
    "environments/studio/profile.json",
)

FORBIDDEN_NAMES = {".env", "credentials.json", "secrets.json"}
FORBIDDEN_SUFFIXES = {
    ".db", ".sqlite", ".sqlite3", ".gguf", ".ckpt", ".safetensors",
    ".pck", ".exe", ".dll",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path, errors: list[str]) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"JSON invalide ou illisible : {path.relative_to(PACK_ROOT)} — {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"Objet JSON attendu : {path.relative_to(PACK_ROOT)}")
        return {}
    return value


def validate_profile(path: Path, expected_id: str, errors: list[str]) -> dict[str, object]:
    profile = load_json(path, errors)
    if profile.get("schema_version") != 1:
        errors.append(f"schema_version invalide : {path.relative_to(PACK_ROOT)}")
    if profile.get("profile_id") != expected_id:
        errors.append(f"profile_id invalide : {path.relative_to(PACK_ROOT)}")
    if profile.get("local_ai_required") is not False:
        errors.append(f"local_ai_required doit rester faux : {path.relative_to(PACK_ROOT)}")
    platforms = profile.get("required_platforms")
    if not isinstance(platforms, list) or not platforms:
        errors.append(f"required_platforms doit être une liste non vide : {path.relative_to(PACK_ROOT)}")
    return profile


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_PROJECT_FILES:
        if not (PROJECT_ROOT / relative).is_file():
            errors.append(f"Fichier projet absent : {relative}")
    for relative in REQUIRED_PACK_FILES:
        if not (PACK_ROOT / relative).is_file():
            errors.append(f"Fichier pack absent : {relative}")

    project_text = (PROJECT_ROOT / "project.godot").read_text(encoding="utf-8")
    for fragment in (
        'config/name="Project Asteria Starter Kit"',
        'run/main_scene="res://src/features/bootstrap/main.tscn"',
        'PackedStringArray("4.7", "Forward Plus")',
    ):
        if fragment not in project_text:
            errors.append(f"project.godot ne contient pas : {fragment}")

    scene_text = (PROJECT_ROOT / "src/features/bootstrap/main.tscn").read_text(encoding="utf-8")
    for fragment in (
        'path="res://src/features/bootstrap/main.gd"',
        '[node name="Main" type="Node3D"]',
        '[node name="Marker" type="MeshInstance3D" parent="."]',
    ):
        if fragment not in scene_text:
            errors.append(f"Scène de bootstrap incomplète : {fragment}")

    main_script = (PROJECT_ROOT / "src/features/bootstrap/main.gd").read_text(encoding="utf-8")
    report_script = (PROJECT_ROOT / "src/core/bootstrap_report.gd").read_text(encoding="utf-8")
    tests_script = (PROJECT_ROOT / "tests/run_tests.gd").read_text(encoding="utf-8")
    for fragment in ("CP-SK-BOOTSTRAP-001", "get_bootstrap_report", "local_ai_optional"):
        if fragment not in main_script:
            errors.append(f"Contrat bootstrap absent du script principal : {fragment}")
    for fragment in ("class_name BootstrapReport", "to_dictionary", "is_valid"):
        if fragment not in report_script:
            errors.append(f"Contrat BootstrapReport absent : {fragment}")
    if "STARTER_KIT_TESTS: PASS" not in tests_script:
        errors.append("Le runner GDScript ne publie pas son marqueur de succès.")

    solo = validate_profile(PACK_ROOT / "environments/solo/profile.json", "solo", errors)
    studio = validate_profile(PACK_ROOT / "environments/studio/profile.json", "studio", errors)
    if solo.get("required_reviewers") != 0:
        errors.append("Le profil Solo doit commencer avec required_reviewers=0.")
    if studio.get("required_reviewers") != 1:
        errors.append("Le profil Studio doit commencer avec required_reviewers=1.")
    if "linux-x86_64" not in studio.get("required_platforms", []):
        errors.append("Le profil Studio doit déclarer linux-x86_64.")

    dependencies = load_json(PACK_ROOT / "DEPENDENCIES.json", errors)
    dependency_items = dependencies.get("dependencies", [])
    if not isinstance(dependency_items, list) or not any(
        isinstance(item, dict)
        and item.get("id") == "godot-engine"
        and item.get("version") == "4.7.1-stable"
        for item in dependency_items
    ):
        errors.append("La dépendance Godot 4.7.1-stable doit être déclarée.")
    if dependencies.get("godot_addons") != []:
        errors.append("Le lot initial ne doit contenir aucun addon Godot.")

    provenance = load_json(PACK_ROOT / "PROVENANCE.json", errors)
    if provenance.get("third_party_files") != [] or provenance.get("binary_files") != []:
        errors.append("Le lot initial ne doit contenir ni fichier tiers ni binaire.")
    if provenance.get("personal_data") is not False or provenance.get("secrets") is not False:
        errors.append("La provenance doit confirmer l'absence de données personnelles et de secrets.")

    for path in PACK_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"Fichier interdit : {path.relative_to(PACK_ROOT)}")
        if ".godot" in path.parts or ".import" in path.parts:
            errors.append(f"Cache Godot versionné : {path.relative_to(PACK_ROOT)}")

    tracked_files = sorted(
        path.relative_to(PACK_ROOT).as_posix()
        for path in PACK_ROOT.rglob("*")
        if path.is_file()
        and not path.name.endswith(".uid")
        and path.name not in {"validation-static.json", "validation-runtime.json"}
    )
    hashes = {relative: sha256(PACK_ROOT / relative) for relative in tracked_files}
    report = {
        "schema_version": 1,
        "validator": "starter-kit-static",
        "python_version": sys.version.split()[0],
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "file_count": len(tracked_files),
        "files": hashes,
    }
    if args.report:
        report_path = Path(args.report)
        if not report_path.is_absolute():
            report_path = PROJECT_ROOT / report_path
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Starter Kit static validation: PASS ({len(tracked_files)} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
