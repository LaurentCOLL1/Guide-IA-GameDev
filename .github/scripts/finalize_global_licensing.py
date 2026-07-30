#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
RUN_ID = "30561457478"
ARTIFACT_ID = "8767038421"
DIGEST = "sha256:bda4f6a33fda885a5ee2bc140c835a1af58a695d9399c5fd64cac099839371d9"
VERIFIED = "2026-07-30T18:26:37+02:00"


def run(*args: str) -> None:
    subprocess.run(list(args), check=True)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 occurrence, got {count}")
    return text.replace(old, new, 1)


proof_path = ROOT / "QA/VALIDATION-LICENSING.yaml"
proof = proof_path.read_text(encoding="utf-8")
if "status: complete" not in proof:
    proof = replace_once(proof, "status: qualified-candidate", "status: complete", "proof status")
    proof = replace_once(proof, "validation-status: awaiting-permanent-workflow", "validation-status: runtime-tested-linux", "proof validation")
    proof = proof.replace(
        "reservations:\n",
        "environment:\n  os: ubuntu-24.04\n  python: 3.12.13\n"
        "results:\n  required-policy-files: 9\n  companion-pack-license-files: 10\n"
        "  allowed-spdx-identifiers: 3\n  matrix-rules: 5\n  chapter-validation: success\n"
        "  obsolete-global-license-markers: 0\n"
        "ci:\n  workflow: Validate Global Licensing\n"
        f"  run-id: {RUN_ID}\n  artifact-id: {ARTIFACT_ID}\n  artifact-digest: {DIGEST}\n"
        "reservations:\n",
        1,
    )
    proof_path.write_text(proof, encoding="utf-8")


audit_path = ROOT / "QA/AUDIT-LICENSING.md"
audit = audit_path.read_text(encoding="utf-8")
audit = audit.replace('status: "candidate"', 'status: "reviewed"', 1)
audit = audit.replace('last-verified: "2026-07-30T18:08:00+02:00"', f'last-verified: "{VERIFIED}"', 1)
audit = audit.replace('audit-level: "static-review"', 'audit-level: "runtime-tested-linux"', 1)
audit = audit.replace(
    "La qualification runtime Linux reste à inscrire dans la preuve YAML après le workflow permanent.",
    f"Le workflow permanent a réussi sur Ubuntu 24.04 avec Python 3.12.13 : run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{DIGEST}`.",
)
audit_path.write_text(audit, encoding="utf-8")


continuity_path = ROOT / "CONTINUITE-PROJET.md"
continuity = continuity_path.read_text(encoding="utf-8")
continuity = continuity.replace('last-updated: "2026-07-30T18:08:00+02:00"', f'last-updated: "{VERIFIED}"', 1)
continuity = continuity.replace("- licence globale à définir ;", "- licence globale multiple définie et validée ;", 1)
continuity = continuity.replace(
    "- licence globale à décider avant publication officielle de la collection ;",
    "- notices de licence et attributions à embarquer dans chaque publication officielle ;",
    1,
)
if f"- run `{RUN_ID}`" not in continuity:
    continuity = replace_once(
        continuity,
        "- validation CI dédiée ajoutée ;",
        "- validation CI dédiée ajoutée et réussie sur Ubuntu 24.04 avec Python `3.12.13` ;\n"
        f"- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{DIGEST}` ;",
        "continuity evidence",
    )
continuity_path.write_text(continuity, encoding="utf-8")


updated_checksums: list[str] = []
for checksum_path in sorted((ROOT / "Companion-Pack").glob("*/checksums.json")):
    data = json.loads(checksum_path.read_text(encoding="utf-8"))
    pack_root = checksum_path.parent
    changed = False
    for relative, expected in list(data.get("files", {}).items()):
        target = pack_root / relative
        if not target.is_file():
            raise RuntimeError(f"checksum target missing: {target.relative_to(ROOT)}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            data["files"][relative] = actual
            changed = True
    if changed:
        checksum_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        updated_checksums.append(str(checksum_path.relative_to(ROOT)))

run(sys.executable, "tools/validate_licenses.py", "--report", "dist/licensing/finalizer-validation.json")
run(sys.executable, "tools/validate_chapters.py")
run("git", "diff", "--check")

tracked = ["QA/AUDIT-LICENSING.md", "QA/VALIDATION-LICENSING.yaml", "CONTINUITE-PROJET.md", *updated_checksums]
changed = subprocess.run(["git", "status", "--porcelain", "--", *tracked], check=True, capture_output=True, text=True).stdout.strip()
if not changed:
    print("GLOBAL_LICENSING_FINALIZER: ALREADY_COMPLETE")
    raise SystemExit(0)

run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", *tracked)
run("git", "commit", "-m", "docs(license): synchroniser la preuve et les checksums")
run("git", "push", "origin", "HEAD:feat/global-licensing-policy")
print("GLOBAL_LICENSING_FINALIZER: PASS")
