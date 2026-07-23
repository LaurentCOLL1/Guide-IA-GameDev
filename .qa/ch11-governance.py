#!/usr/bin/env python3
from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Motif introuvable dans {path}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


old_chapter_sha = "70862593df9ea757123d6285f1cecd12e621ed02ce48111723af6632c1e0a874"
new_chapter_sha = "bcc38ce80457fc3b765d9d818f8a8d82c102bd9387d9eb11af57f94c5f8e73ee"
old_audit_sha = "939e775c3bfdb1c46398426ee14aa48262f3fe673a65433b1caa34571582a4af"
new_audit_sha = "afc04b0d138f789788f3a16144281b8c060c1f0bb8a13bf8ce7b3d06fc722288"

replace_once(
    "Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md",
    "## 38. Erreurs fréquentes et corrections\n\n### 38.1 Autoriser toutes les combinaisons par défaut",
    "## 38. Erreurs fréquentes et corrections\n\n<!-- qa:error-correction-section -->\n\n### 38.1 Autoriser toutes les combinaisons par défaut",
)

replace_once(
    "Livre-III/QA/AUDIT-CHAPITRE-11.md",
    "- lignes : 1 973 ;",
    "- lignes : 1 975 ;",
)

proof_path = "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-11.yaml"
replace_once(proof_path, "  chapter-lines: 1973", "  chapter-lines: 1975")
replace_once(proof_path, f"  chapter-sha256: {old_chapter_sha}", f"  chapter-sha256: {new_chapter_sha}")
replace_once(proof_path, f"  audit-sha256: {old_audit_sha}", f"  audit-sha256: {new_audit_sha}")

close_path = ".qa/ch11-close.py"
replace_once(close_path, old_chapter_sha, new_chapter_sha)
replace_once(close_path, old_audit_sha, new_audit_sha)
replace_once(close_path, "1 973 lignes", "1 975 lignes")

print("Chapter 11 QA marker correction applied.")
