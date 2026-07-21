#!/usr/bin/env python3
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(".")
PARTS_DIR = ROOT / ".qa/ch23-payload"
TARGET = ROOT / "Livre-II/CHAPITRE-23-Politique-factions-et-justice.md"
SOURCE_SHA256 = "ba9d44672b060ba23b285b7ffca23a4bdf7cd7910a2bdcc4b91337119e553c10"
FINAL_SHA256 = "3b06c4888743957f4a4804eda53183ff235378511d841a5fe5b45d197fa5d4d8"

parts = sorted(PARTS_DIR.glob("part-*.txt"))
if len(parts) != 4:
    raise SystemExit(f"expected 4 payload parts, found {len(parts)}")

encoded = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
source = gzip.decompress(base64.b64decode(encoded))
if len(source) != 148646:
    raise SystemExit(f"unexpected source size: {len(source)}")
if hashlib.sha256(source).hexdigest() != SOURCE_SHA256:
    raise SystemExit("source SHA-256 mismatch")

text = source.decode("utf-8")
old_decision = "if outcome == Outcome.DENY and not StableId.is_valid(denied_reason_id):\n\t\treturn ERR_INVALID_DATA"
new_decision = "if outcome in [Outcome.DENY, Outcome.INDETERMINATE]:\n\t\tif not StableId.is_valid(denied_reason_id):\n\t\t\treturn ERR_INVALID_DATA"
if text.count(old_decision) != 1:
    raise SystemExit(f"authorization replacement count: {text.count(old_decision)}")
text = text.replace(old_decision, new_decision, 1)
text = text.replace(
    "- Un refus exige une raison stable.",
    "- Un refus ou une impossibilité d’évaluer exige une raison stable.",
    1,
)
if text.count("var all_lists: Array[Array] = [") != 1:
    raise SystemExit("nested typed array replacement count mismatch")
text = text.replace("var all_lists: Array[Array] = [", "var all_lists: Array = [", 1)

final = text.encode("utf-8")
if len(final) != 148702:
    raise SystemExit(f"unexpected final size: {len(final)}")
if hashlib.sha256(final).hexdigest() != FINAL_SHA256:
    raise SystemExit("final SHA-256 mismatch")
TARGET.write_bytes(final)
print(f"reconstructed {TARGET} ({len(final)} bytes, sha256={FINAL_SHA256})")
