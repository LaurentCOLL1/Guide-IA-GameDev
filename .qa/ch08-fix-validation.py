from pathlib import Path

path = Path("Livre-III/CHAPITRE-08-Creation-des-animaux.md")
lines = path.read_text(encoding="utf-8").splitlines()

malformed = 0
for index, line in enumerate(lines):
    if line.startswith("> ****[") and line.endswith("****"):
        lines[index] = line.replace("> ****[", "> **[", 1)[:-4] + "**"
        malformed += 1

faulty = 0
corrected = 0
for index, line in enumerate(lines):
    if line == "**Exemple fautif :**":
        lines[index] = "> **[LECTURE] Exemple fautif — Ne pas saisir.**"
        faulty += 1
    elif line == "**Exemple corrigé :**":
        lines[index] = "> **[LECTURE] Exemple corrigé — Ne pas saisir.**"
        corrected += 1

if malformed != 23:
    raise RuntimeError(f"Repères mal formés attendus : 23, trouvés : {malformed}")
if faulty != 10:
    raise RuntimeError(f"Exemples fautifs attendus : 10, trouvés : {faulty}")
if corrected != 10:
    raise RuntimeError(f"Exemples corrigés attendus : 10, trouvés : {corrected}")

path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Les 43 blocs possèdent désormais un repère d'utilisation normalisé.")
