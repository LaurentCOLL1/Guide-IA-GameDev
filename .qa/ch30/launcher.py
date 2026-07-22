#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import io
import re
import runpy
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PARTS = [Path(__file__).with_name(f"prefix-{index:02d}.txt") for index in range(3)]
BROKEN = Path(__file__).with_name("bootstrap.py")

source = BROKEN.read_text(encoding="utf-8")
match = re.search(r'PAYLOAD = """(.*?)"""', source, re.DOTALL)
if match is None:
    raise RuntimeError("suffixe du payload introuvable")

payload = "".join(path.read_text(encoding="utf-8") for path in PARTS) + match.group(1)
if len(payload) != 37828:
    raise RuntimeError(f"longueur du payload inattendue: {len(payload)}")
if hashlib.sha256(payload.encode("ascii")).hexdigest() != "a026dfd5c9200ea094bc93dfd735ecf5c29796ac8e2c8ddd0dfe3cbb34f4ba49":
    raise RuntimeError("empreinte textuelle du payload invalide")

archive_bytes = base64.b64decode(payload, validate=True)
if hashlib.sha256(archive_bytes).hexdigest() != "f3e4706964c523cec4ab30df8e75b44d6ed1d7a9bfb67c8e86342abbfc7571c2":
    raise RuntimeError("empreinte de l’archive invalide")

with tempfile.TemporaryDirectory(prefix="ch30-") as tmp:
    extracted = Path(tmp)
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as archive:
        archive.extractall(extracted)
    runpy.run_path(str(extracted / "apply.py"), run_name="__main__")

chapter_path = ROOT / "Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md"
chapter = chapter_path.read_text(encoding="utf-8")
faulty_labels = (
    "Architecture fautive", "Configuration fautive", "Dépendances fautives",
    "Organisation fautive", "Flux fautif", "Arbre fautif",
    "Formulation fautive", "Commande fautive", "Approche fautive",
)
corrected_labels = (
    "Architecture corrigée", "Configuration corrigée", "Dépendances corrigées",
    "Organisation corrigée", "Flux corrigé", "Arbre corrigé",
    "Formulation corrigée", "Commande corrigée", "Approche corrigée",
)
for label in faulty_labels:
    chapter = chapter.replace(f"**{label} :**", "**Exemple fautif :**")
for label in corrected_labels:
    chapter = chapter.replace(f"**{label} :**", "**Exemple corrigé :**")
chapter_path.write_text(chapter, encoding="utf-8")
