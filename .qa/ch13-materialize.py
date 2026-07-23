#!/usr/bin/env python3
import base64
import hashlib
import json
import zlib
from pathlib import Path

EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"
CHAPTER_KEY = "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md"
AUDIT_KEY = "Livre-III/QA/AUDIT-CHAPITRE-13.md"

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
if len(fragment_paths) != 14:
    raise RuntimeError(f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14.")

parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
if [len(part) for part in parts[:12]] != [4000] * 12:
    raise RuntimeError("Les douze premiers fragments sont invalides.")
if len(parts[12]) != 6263 or len(parts[13]) != 20:
    raise RuntimeError(f"Forme finale inattendue : {[len(part) for part in parts]}")

prefix = "".join(parts[:12]) + parts[12][:4000]
tail = parts[12][4000:] + parts[13] + "="
encoded = prefix + tail
compressed = base64.b64decode(encoded, validate=True)

if compressed[:3] != b"\x1f\x8b\x08":
    raise RuntimeError("En-tête gzip absent.")
flags = compressed[3]
position = 10
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
if position >= len(compressed) - 8:
    raise RuntimeError("Bornes DEFLATE invalides.")

raw = zlib.decompress(compressed[position:-8], -zlib.MAX_WBITS)
payload = json.loads(raw.decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 13 invalide.")

files = payload["files"]
chapter = files.get(CHAPTER_KEY)
audit = files.get(AUDIT_KEY)
if not isinstance(chapter, str) or not isinstance(audit, str):
    raise RuntimeError("Chapitre ou audit absent du paquet restauré.")
chapter_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()
if chapter_sha != EXPECTED_CHAPTER_SHA or audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError(
        f"Empreintes permanentes invalides : chapitre={chapter_sha}, audit={audit_sha}."
    )
if ".qa/ch13-governance.py" not in files or ".qa/ch13-close.py" not in files:
    raise RuntimeError("Scripts de gouvernance ou de clôture absents.")

for raw_path, content in files.items():
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
print("Paquet chapitre 13 restauré depuis le flux DEFLATE avec empreintes permanentes exactes.")
