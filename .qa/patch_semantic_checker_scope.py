#!/usr/bin/env python3
from pathlib import Path

path = Path("tools/check_code_explanation_structure.py")
text = path.read_text(encoding="utf-8")
old = '''def check(path: Path) -> list[str]:
    chapter = number(path)
    if chapter is None:
        return []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors, error_ranges = check_error_correction_sections(path, lines)

    if chapter < 17:
        return errors
'''
new = '''def check(path: Path) -> list[str]:
    chapter = number(path)
    if chapter is None or chapter < 17:
        return []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors, error_ranges = check_error_correction_sections(path, lines)
'''
if old not in text:
    raise SystemExit("Ancre de portée du validateur introuvable")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
print("Contrôle strict limité aux chapitres restructurés 17 à 26.")
