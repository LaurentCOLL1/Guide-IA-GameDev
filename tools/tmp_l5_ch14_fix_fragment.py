#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md"
text = path.read_text(encoding="utf-8")

replacements = (
    ("#141-foreign_keys-avant-louverture", "#141-foreignkeys-avant-louverture"),
    ("> **Repère :** **[LECTURE]**", "> **Repères d’utilisation :** **[LECTURE]**"),
)

for old, new in replacements:
    if new in text:
        continue
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Remplacement attendu une fois, trouvé {count}: {old!r}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
