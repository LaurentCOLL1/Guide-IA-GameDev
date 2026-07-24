#!/usr/bin/env python3
from pathlib import Path

checks = {
    "Livre-III/index.md": "21. [Capture de mouvement et retargeting]",
    "contents.txt": "Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md",
    "ROADMAP.md": "21 chapitres rédigés, repérés et audités sur 30",
    "plans/LIVRE-III-PLAN-MAITRE.md": "chapitres 1 à 21 rédigés",
    "CONTINUITE-PROJET.md": "Livre-III/CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md",
}
for path_text, marker in checks.items():
    path = Path(path_text)
    if not path.is_file() or marker not in path.read_text(encoding="utf-8"):
        raise RuntimeError(f"État de gouvernance attendu absent : {path_text} / {marker}")
print("Gouvernance du chapitre 21 déjà matérialisée et vérifiée.")
