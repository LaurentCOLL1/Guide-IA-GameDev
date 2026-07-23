from pathlib import Path

proof = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-16.yaml").read_text(encoding="utf-8")
continuity = Path("CONTINUITE-PROJET.md").read_text(encoding="utf-8")

if "status: pending" not in proof or "validated-head-commit: null" not in proof:
    raise RuntimeError("La preuve provisoire du chapitre 16 n'est pas dans l'état attendu.")
if 'version: "3.46.0"' not in continuity:
    raise RuntimeError("La gouvernance provisoire du chapitre 16 n'est pas dans l'état attendu.")
