#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_PACKAGE_SHA = "2d70d119a36bf61e6cdb6bb38b24abb79adc5cee48806149083ce5393e6fc494"
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
if len(fragment_paths) != 14:
    raise RuntimeError(f"Nombre de fragments invalide : {len(fragment_paths)} au lieu de 14.")

parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
if len(parts[12]) != 6263 or len(parts[13]) != 20:
    raise RuntimeError(f"Forme du paquet inattendue : {[len(part) for part in parts]}")

fragment_13 = parts[12][:4000]
fragment_14_prefix = parts[12][4000:]
fragment_14_suffix = parts[13]
recovered = None
compressed = None

for character in BASE64_ALPHABET:
    candidate_14 = fragment_14_prefix + character + fragment_14_suffix
    candidate_parts = parts[:12] + [fragment_13, candidate_14]
    encoded = "".join(candidate_parts)
    try:
        candidate_compressed = base64.b64decode(encoded, validate=True)
    except Exception:
        continue
    if hashlib.sha256(candidate_compressed).hexdigest() == EXPECTED_PACKAGE_SHA:
        recovered = character
        compressed = candidate_compressed
        parts = candidate_parts
        break

if recovered is None or compressed is None:
    raise RuntimeError("Caractère Base64 manquant introuvable par l’empreinte attendue.")

if [len(part) for part in parts[:13]] != [4000] * 13 or len(parts[13]) != 2284:
    raise RuntimeError("Découpage final du paquet invalide.")

payload = json.loads(gzip.decompress(compressed).decode("utf-8"))
if payload.get("schema") != 1 or not isinstance(payload.get("files"), dict):
    raise RuntimeError("Schéma du paquet chapitre 13 invalide.")

for raw_path, content in payload["files"].items():
    target = Path(raw_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

chapter = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
audit = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
actual_chapter_sha = hashlib.sha256(chapter.read_bytes()).hexdigest()
actual_audit_sha = hashlib.sha256(audit.read_bytes()).hexdigest()
if actual_chapter_sha != EXPECTED_CHAPTER_SHA:
    raise RuntimeError(f"Empreinte du chapitre 13 invalide : {actual_chapter_sha}.")
if actual_audit_sha != EXPECTED_AUDIT_SHA:
    raise RuntimeError(f"Empreinte de l’audit du chapitre 13 invalide : {actual_audit_sha}.")

Path(".qa/ch13-diagnostic.json").unlink(missing_ok=True)
print(f"Caractère Base64 restauré avec preuve cryptographique : {recovered}")
