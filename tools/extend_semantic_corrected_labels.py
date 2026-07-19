#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
validator = root / "tools/validate_chapters.py"
text = validator.read_text(encoding="utf-8")
old = r'''r"(?:exemple|structure|organisation|chemin|dépendances?|arbre|lot)[^\n]{0,100}corrig(?:é|ée|és|ées)"'''
new = r'''r"(?:exemple|structure|organisation|architecture|flux|chemin|dépendances?|arbre|lot)[^\n]{0,100}corrig(?:é|ée|és|ées)"'''
if text.count(old) != 1:
    raise SystemExit(f"Validator pattern count: {text.count(old)}")
validator.write_text(text.replace(old, new, 1), encoding="utf-8")

continuity = root / "CONTINUITE-PROJET.md"
text = continuity.read_text(encoding="utf-8")
old = "- contrôles `quick_check` et `foreign_key_check` ;\n"
new = (
    "- contrôles `quick_check` et `foreign_key_check` ;\n"
    "- validateur sémantique étendu aux libellés « Architecture corrigée » et « Flux corrigé » ;\n"
)
if text.count(old) != 1:
    raise SystemExit(f"Continuity insertion count: {text.count(old)}")
continuity.write_text(text.replace(old, new, 1), encoding="utf-8")

for rel in (
    "tools/extend_semantic_corrected_labels.py",
    ".github/workflows/extend-semantic-corrected-labels.yml",
):
    file_path = root / rel
    if file_path.exists():
        file_path.unlink()

print("Semantic corrected labels extended.")
