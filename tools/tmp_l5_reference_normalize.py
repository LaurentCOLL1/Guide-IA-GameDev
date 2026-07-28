#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "CONTINUITE-PROJET.md",
    "ROADMAP.md",
    "plans/LIVRE-V-PLAN-MAITRE.md",
    "Livre-V/index.md",
    "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md",
    "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md",
    "Livre-V/QA/AUDIT-CHAPITRE-01.md",
    "tools/validate_chapters.py",
    "tools/check_code_explanation_structure.py",
    "tools/check_context_markers.py",
    "tools/audit_contextes_utilisation.py",
    "tools/audit_contextes_semantiques.py",
    "tools/report_contextes_utilisation.py",
)


def normalize(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8", newline="\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for rel in FILES:
        normalize(ROOT / rel)

    proof_path = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml"
    proof = yaml.safe_load(proof_path.read_text(encoding="utf-8"))
    proof["integrity"]["chapter-sha256"] = sha256(
        ROOT / "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"
    )
    proof["integrity"]["audit-sha256"] = sha256(
        ROOT / "Livre-V/QA/AUDIT-CHAPITRE-01.md"
    )
    proof_path.write_text(
        yaml.safe_dump(proof, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
