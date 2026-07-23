#!/usr/bin/env python3
import hashlib
from pathlib import Path

CHAPTER_PATH = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
AUDIT_PATH = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
PROOF_PATH = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-13.yaml")
GOVERNANCE_PATH = Path(".qa/ch13-governance.py")
CLOSE_PATH = Path(".qa/ch13-close.py")
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "48defcdb19887a51643c87d3ad2aa02d37792c5d42409d1d9508b511d255af0e"

for path in (CHAPTER_PATH, AUDIT_PATH, PROOF_PATH, GOVERNANCE_PATH, CLOSE_PATH):
    if not path.is_file():
        raise RuntimeError(f"Fichier requis absent : {path}")

chapter_sha = hashlib.sha256(CHAPTER_PATH.read_bytes()).hexdigest()
audit_sha = hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest()
if chapter_sha != EXPECTED_CHAPTER_SHA:
    raise RuntimeError(f"Empreinte du chapitre 13 invalide : {chapter_sha}")
if audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError(f"Empreinte de l'audit du chapitre 13 invalide : {audit_sha}")

Path(".qa/ch13-analysis.json").unlink(missing_ok=True)
Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
print("Chapitre 13 et audit vérifiés ; gouvernance autorisée.")
