#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
validator = root / "tools/validate_chapters.py"
text = validator.read_text(encoding="utf-8")
old = '''            if "Exemple corrigé" not in child_body:
                missing.append("exemple corrigé")
            has_labeled_difference = "**Différence :**" in child_body
            trailing_prose = ""
            if "Exemple corrigé" in child_body:
                corrected_part = child_body.split("Exemple corrigé", 1)[1]
'''
new = '''            corrected_match = re.search(
                r"(?:exemple|structure|organisation|chemin|dépendances?|arbre|lot)[^\\n]{0,100}corrig(?:é|ée|és|ées)",
                child_body,
                re.IGNORECASE,
            )
            if corrected_match is None:
                missing.append("exemple corrigé")
            has_labeled_difference = "**Différence :**" in child_body
            trailing_prose = ""
            if corrected_match is not None:
                corrected_part = child_body[corrected_match.end():]
'''
if old not in text:
    raise SystemExit("Corrected example validator block not found")
text = text.replace(old, new, 1)
validator.write_text(text, encoding="utf-8")

for rel in (
    "tools/generalize_corrected_example_marker.py",
    ".github/workflows/generalize-corrected-example-marker.yml",
):
    path = root / rel
    if path.exists():
        path.unlink()

print("Corrected-example marker generalized.")
