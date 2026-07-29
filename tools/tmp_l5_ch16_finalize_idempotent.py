#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

CHAPTER = Path("Livre-V/CHAPITRE-16-Patrons-d-architecture.md")
AUDIT = Path("Livre-V/QA/AUDIT-CHAPITRE-16.md")
PROOF = Path("Livre-V/QA/VALIDATION-FINALE-CHAPITRE-16.yaml")
CHAPTER_SHA = "23d740ea8746baf7aee5480536b0c89448d5e150e56bb0e543d8f74903fe0e38"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_text(path: str, expected: str) -> None:
    text = Path(path).read_text(encoding="utf-8")
    if expected not in text:
        raise RuntimeError(f"Expected governance marker missing in {path}: {expected}")


def main() -> int:
    if digest(CHAPTER) != CHAPTER_SHA:
        raise RuntimeError("Chapter SHA-256 mismatch")

    audit_text = AUDIT.read_text(encoding="utf-8")
    if 'last-verified: "2026-07-29T06:49:56+02:00"' not in audit_text:
        raise RuntimeError("Audit last-verified metadata missing")
    audit_sha = digest(AUDIT)

    metrics = json.loads(Path("dist/QA-LIVRE-V-CH16-CHAPTER.json").read_text(encoding="utf-8"))
    expected = {
        "lines": 409,
        "headings": 19,
        "cards": 13,
        "matrices": 3,
        "markdown_links": 65,
        "source_book_links": 34,
        "fragment_links": 21,
        "official_links": 13,
        "fenced_blocks": 0,
        "compact_diagrams": 7,
        "chapter_sha256": CHAPTER_SHA,
    }
    if metrics != expected:
        raise RuntimeError(f"Chapter metrics mismatch: {metrics!r}")

    require_text("Livre-V/index.md", 'version: "1.8.0"')
    require_text("Livre-V/index.md", "Progression : **16 chapitres sur 26**")
    require_text("ROADMAP.md", "Patrons d’architecture — fiche 16 rédigée et auditée")
    require_text("ROADMAP.md", "16 chapitres rédigés, repérés et audités sur 26")
    require_text("contents.txt", "Livre-V/CHAPITRE-16-Patrons-d-architecture.md")
    require_text("plans/LIVRE-V-PLAN-MAITRE.md", 'version: "1.16.0"')
    require_text("plans/LIVRE-V-PLAN-MAITRE.md", "16 chapitres sur 26 rédigés et audités")
    require_text("CONTINUITE-PROJET.md", 'version: "4.03.0"')
    require_text("CONTINUITE-PROJET.md", "Livre-V/CHAPITRE-17-Patrons-de-gameplay.md")

    proof_text = PROOF.read_text(encoding="utf-8")
    pattern = r"(?m)^  audit-sha256: [0-9a-f]{64}$"
    replacement = f"  audit-sha256: {audit_sha}"
    proof_text, count = re.subn(pattern, replacement, proof_text)
    if count != 1:
        raise RuntimeError(f"Expected one audit hash line in proof, found {count}")
    PROOF.write_text(proof_text, encoding="utf-8")

    print(f"Governance verified; proof audit SHA-256={audit_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
