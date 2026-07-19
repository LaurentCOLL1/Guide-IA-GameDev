from pathlib import Path

validator_path = Path("tools/validate_chapters.py")
text = validator_path.read_text(encoding="utf-8")
old = r'''r"(?:exemple|structure|organisation|architecture|flux|chemin|dépendances?|arbre|lot)[^\n]{0,100}corrig(?:é|ée|és|ées)",'''
new = r'''r"(?:exemple|structure|organisation|architecture|flux|formulation|ordre|historique|chemin|dépendances?|arbre|lot)[^\n]{0,100}corrig(?:é|ée|és|ées)",'''
if old not in text:
    raise SystemExit("Semantic corrected-label regex not found")
validator_path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
Path("tools/patch_ch09_validator.py").unlink()
Path(".github/workflows/patch-ch09-validator.yml").unlink()
