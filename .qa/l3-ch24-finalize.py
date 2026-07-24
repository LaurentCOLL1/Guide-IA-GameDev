#!/usr/bin/env python3
from pathlib import Path
import base64
import hashlib
import zlib

ROOT = Path(__file__).resolve().parent
PART_COUNT = 13
EXPECTED_PAYLOAD_LENGTH = 44084
EXPECTED_PAYLOAD_SHA256 = "be64d1385d216414eab88044f549eca7f3de8dbc2c36924c834f512570d6a64e"
EXPECTED_SOURCE_SHA256 = "0a95481aa77d00d53e19d41565e6eb3f0750d7c3b50e3ed1f53600cd987049b0"

payload = "".join(
    (ROOT / f"l3-ch24-generator-part-{index:02d}.txt").read_text(encoding="utf-8")
    for index in range(1, PART_COUNT + 1)
)
if len(payload) != EXPECTED_PAYLOAD_LENGTH:
    raise RuntimeError(f"Longueur du payload invalide: {len(payload)}")
if hashlib.sha256(payload.encode("utf-8")).hexdigest() != EXPECTED_PAYLOAD_SHA256:
    raise RuntimeError("Empreinte du payload invalide")

source = zlib.decompress(base64.b64decode(payload)).decode("utf-8")
if hashlib.sha256(source.encode("utf-8")).hexdigest() != EXPECTED_SOURCE_SHA256:
    raise RuntimeError("Empreinte du générateur invalide")

compiled = compile(source, "<l3-ch24-finalizer>", "exec")
exec(compiled)
