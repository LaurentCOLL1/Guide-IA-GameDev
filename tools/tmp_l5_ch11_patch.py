#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Livre-V/CHAPITRE-11-Reference-GDScript.md"
text = path.read_text(encoding="utf-8")
old = "#19-classes-héritage-et-class_name"
new = "#19-classes-héritage-et-classname"
count = text.count(old)
if count not in {0, 2}:
    raise RuntimeError(f"Nombre inattendu d’ancres class_name : {count}")
if count:
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")
print(f"ancres corrigées : {count}")
