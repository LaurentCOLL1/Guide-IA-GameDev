from pathlib import Path

path = Path("Livre-III/CHAPITRE-07-Creation-des-humanoides.md")
text = path.read_text(encoding="utf-8")

faulty = "**Exemple fautif :**"
corrected = "**Exemple corrigé :**"
faulty_marker = "> **[LECTURE] Exemple fautif — Ne pas saisir.**"
corrected_marker = "> **[LECTURE] Exemple corrigé — Ne pas saisir.**"

if text.count(faulty) != 10:
    raise RuntimeError(f"Libellés fautifs attendus : 10 ; trouvés : {text.count(faulty)}")
if text.count(corrected) != 10:
    raise RuntimeError(f"Libellés corrigés attendus : 10 ; trouvés : {text.count(corrected)}")
if faulty_marker in text or corrected_marker in text:
    raise RuntimeError("Les repères corrigés existent déjà partiellement.")

text = text.replace(faulty, faulty_marker)
text = text.replace(corrected, corrected_marker)
path.write_text(text, encoding="utf-8")

print("20 repères de diagnostic corrigés sans modifier le nombre de lignes.")
