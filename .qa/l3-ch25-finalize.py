#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha1
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / ".qa").glob("l3-ch25-generator-part-*.txt"))
EXPECTED = [
    (9000, "259fbc34a50f0db871e0f572e02ce9851b49578e"),
    (9000, "61e4a706304902cfd395d1fe17446ab705d4aa94"),
    (9000, "22662579ac053852c637112c75f9607ba92b1187"),
    (9000, "2d7d535724f67c1bc223de85ec089e843a908982"),
    (9000, "34a65c5fdb25f3939365b96c4c6c0559654a9904"),
    (3376, "b1c4727df6498de84a9ff2bbf25c4a498590bc47"),
]
lines = []
for index, path in enumerate(PARTS):
    content = path.read_text(encoding="utf-8").strip()
    actual = (len(content), sha1(content.encode("utf-8")).hexdigest())
    padding = [position for position, char in enumerate(content) if char == "="]
    expected = EXPECTED[index] if index < len(EXPECTED) else None
    lines.append(
        f"{path.name}: actual={actual}; expected={expected}; padding={padding}; match={actual == expected}"
    )
combined = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
lines.append(f"combined-length={len(combined)}")
lines.append(f"combined-padding={[position for position, char in enumerate(combined) if char == '=']}")
(ROOT / ".qa/l3-ch25-error.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
