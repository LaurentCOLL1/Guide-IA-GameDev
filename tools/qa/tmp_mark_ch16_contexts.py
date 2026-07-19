from pathlib import Path

path = Path("Livre-II/CHAPITRE-16-Famille-et-generations.md")
lines = path.read_text(encoding="utf-8").splitlines()
result: list[str] = []
added = 0

for line in lines:
    if line.startswith("```gdscript"):
        previous = ""
        for candidate in reversed(result):
            if candidate.strip():
                previous = candidate.strip()
                break

        if not previous.startswith("> **["):
            if previous == "**Exemple fautif :**":
                marker = "> **[LECTURE] Exemple fautif — Ne pas utiliser.**"
            elif previous == "**Exemple corrigé :**":
                marker = "> **[LECTURE] Exemple corrigé — Structure de référence.**"
            else:
                marker = "> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**"

            if result and result[-1] != "":
                result.append("")
            result.append(marker)
            result.append("")
            added += 1

    result.append(line)

if added != 49:
    raise RuntimeError(f"Expected 49 context markers, added {added}")

path.write_text("\n".join(result) + "\n", encoding="utf-8", newline="\n")
print(f"Added {added} context markers to {path}")
