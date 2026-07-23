#!/usr/bin/env python3
import base64
import hashlib
import json
import os
import subprocess
import zlib
from pathlib import Path

EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
CHAPTER_KEY = "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md"

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
if len(parts) != 14 or [len(part) for part in parts[:12]] != [4000] * 12:
    raise RuntimeError("Fragments initiaux du chapitre 13 invalides.")
if len(parts[12]) != 6263 or len(parts[13]) != 20:
    raise RuntimeError(f"Forme finale inattendue : {[len(part) for part in parts]}")

encoded = "".join(parts[:12]) + parts[12] + parts[13] + "="
compressed = base64.b64decode(encoded, validate=True)
position = 10
flags = compressed[3]
if flags & 0x04:
    xlen = int.from_bytes(compressed[position:position + 2], "little")
    position += 2 + xlen
if flags & 0x08:
    while compressed[position] != 0:
        position += 1
    position += 1
if flags & 0x10:
    while compressed[position] != 0:
        position += 1
    position += 1
if flags & 0x02:
    position += 2

decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
raw = decompressor.decompress(compressed[position:-8]) + decompressor.flush()
text = raw.decode("utf-8", errors="ignore")
key = json.dumps(CHAPTER_KEY, ensure_ascii=False)
index = text.find(key)
if index < 0:
    raise RuntimeError("Clé du chapitre 13 introuvable dans la sortie récupérée.")
colon = text.find(":", index + len(key))
value_start = colon + 1
while text[value_start].isspace():
    value_start += 1
chapter, _ = json.JSONDecoder().raw_decode(text, value_start)
if not isinstance(chapter, str):
    raise RuntimeError("Valeur du chapitre 13 non textuelle.")
actual_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_sha != EXPECTED_CHAPTER_SHA:
    raise RuntimeError(f"Empreinte récupérée invalide : {actual_sha}.")

target = Path(CHAPTER_KEY)
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(chapter, encoding="utf-8")
Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)

subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", str(target), ".qa/ch13-diagnostic.json"], check=False)
if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
    subprocess.run(["git", "commit", "-m", "docs(ch13): récupérer le chapitre original vérifié"], check=True)
    subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)
raise RuntimeError("Chapitre original récupéré et poussé ; reconstruction QA volontairement différée.")
