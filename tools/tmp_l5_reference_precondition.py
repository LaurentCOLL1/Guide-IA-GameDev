#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "ROADMAP.md"
text = path.read_text(encoding="utf-8")
current = """## M6 — Livre V : Encyclopédie technique

- [x] Chapitre 1 — Carte générale de la collection — rédigé, repéré et audité au niveau `static-review`.
- [ ] Fiches universelles — 1 chapitre sur 26.
- [ ] Arbres de décision et matrices.
- [ ] Bibliothèques techniques et index croisés.
"""
expected = """## M6 — Livre V : Encyclopédie technique

- [ ] Fiches universelles.
- [ ] Arbres de décision et matrices.
- [ ] Bibliothèques techniques et index croisés.
"""
if current not in text:
    raise RuntimeError("Le bloc M6 courant attendu est absent.")
path.write_text(text.replace(current, expected, 1), encoding="utf-8", newline="\n")
