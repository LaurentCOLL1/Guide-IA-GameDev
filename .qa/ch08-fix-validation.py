from pathlib import Path

path = Path("Livre-III/CHAPITRE-08-Creation-des-animaux.md")
text = path.read_text(encoding="utf-8")

old_grid = "> **[APP] Blender — Grille de poses de déformation — Ne pas saisir.**"
new_grid = "> **[LECTURE] Grille de poses de déformation — Ne pas saisir.**"
old_report = "> **[APP] Blender — Rapport d’influences attendu — Ne pas saisir.**"
new_report = "> **[SORTIE] Blender — Rapport d’influences attendu — Ne pas saisir.**"

if text.count(old_grid) != 1:
    raise RuntimeError(f"Repère de grille attendu une fois, trouvé {text.count(old_grid)}")
if text.count(old_report) != 1:
    raise RuntimeError(f"Repère de rapport attendu une fois, trouvé {text.count(old_report)}")

text = text.replace(old_grid, new_grid, 1)
text = text.replace(old_report, new_report, 1)
path.write_text(text, encoding="utf-8")
print("Les deux repères sémantiques du chapitre 8 sont corrigés.")
