#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / ".qa").glob("l3-ch26-generator-part-*.txt"))
EXPECTED = [
    (6000, "b869749131e7551754de0f46296601b941741329"),
    (6000, "1de8698e30dc0ac70c03bf04ace43e050f9d9b80"),
    (6000, "e55b2d1fb52f57f43036f743c943bcdfaaacaecb"),
    (6000, "aee54775771fee1502862bda504c6a66b9ede882"),
    (6000, "f129d58eb5bb35ad6bd8ab4ac42accfd0f47ef3f"),
    (6000, "35859118f276f1ff3c24b81ff89031d47c4e0bb5"),
    (6000, "066af475c75ed5c6a0e10ddbfc5f88878e61e03e"),
    (6000, "2edefe06a2e35b9bdda91e10a631057dda12dc49"),
    (1516, "41fda277e6ca3cc9b47a988e4744cb378791b7e0"),
]
lines: list[str] = []
clean_parts: list[str] = []
for index, path in enumerate(PARTS):
    raw = path.read_text(encoding="utf-8")
    clean = "".join(raw.split())
    clean_parts.append(clean)
    actual = (len(clean), hashlib.sha1(clean.encode("ascii")).hexdigest())
    expected = EXPECTED[index] if index < len(EXPECTED) else None
    lines.append(f"{path.name}: actual={actual}; expected={expected}; match={actual == expected}")
encoded = "".join(clean_parts)
lines.append(f"combined-length={len(encoded)}")
try:
    compressed = base64.b64decode(encoded, validate=True)
    lines.append(f"combined-sha256={hashlib.sha256(compressed).hexdigest()}")
except Exception as exc:
    lines.append(f"decode-error={type(exc).__name__}: {exc}")
(ROOT / ".qa/l3-ch26-diagnostic.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
