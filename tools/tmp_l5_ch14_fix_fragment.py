#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Livre-V/CHAPITRE-14-Schemas-SQLite-et-migrations.md"
text = path.read_text(encoding="utf-8")
old = "#141-foreign_keys-avant-louverture"
new = "#141-foreignkeys-avant-louverture"
if new not in text:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Fragment attendu une fois, trouvé {count}.")
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
