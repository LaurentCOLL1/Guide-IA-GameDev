#!/usr/bin/env python3
from pathlib import Path

required = [
    Path("Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md"),
    Path("Livre-III/QA/AUDIT-CHAPITRE-21.md"),
    Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-21.yaml"),
]
for path in required:
    if not path.is_file():
        raise RuntimeError(f"Fichier permanent absent : {path}")
audit = required[1].read_text(encoding="utf-8")
if 'last-verified: "2026-07-24T13:38:11+02:00"' not in audit:
    raise RuntimeError("Horodatage last-verified absent de l’audit du chapitre 21.")
print("Lot permanent du chapitre 21 présent ; reprise ciblée de la validation.")
