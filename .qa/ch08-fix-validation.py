from pathlib import Path

path = Path("Livre-III/CHAPITRE-08-Creation-des-animaux.md")
text = path.read_text(encoding="utf-8")

faulty = "> **[LECTURE] Exemple fautif — Ne pas saisir.**"
corrected = "> **[LECTURE] Correction — Ne pas saisir.**"

if text.count(faulty) != 10:
    raise RuntimeError(f"Exemples fautifs attendus : 10, trouvés : {text.count(faulty)}")
if text.count(corrected) != 10:
    raise RuntimeError(f"Corrections attendues : 10, trouvées : {text.count(corrected)}")

text = text.replace(faulty, "**Exemple fautif :**")
text = text.replace(corrected, "**Exemple corrigé :**")
path.write_text(text, encoding="utf-8")

print("Les dix diagnostics utilisent les libellés pédagogiques normalisés.")
