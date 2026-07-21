from __future__ import annotations

import base64
import gzip
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = [HERE / f"refine_payload_{index}.txt" for index in range(1, 4)]
payload = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
source_bytes = gzip.decompress(base64.b64decode(payload))
expected = "2236fdd3c995a3e89260fd7c91c659ca446f75bad80a61f3eb9254bf840a6cec"
actual = hashlib.sha256(source_bytes).hexdigest()
if actual != expected:
    raise RuntimeError(f"empreinte du script invalide: {actual}")
for path in PARTS:
    path.unlink()
SOURCE = source_bytes.decode("utf-8")

validator_boundary = '''def end_of_explanation(lines: list[str], start: int) -> int:
    structured_seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == STRUCTURED:
            structured_seen = True
            continue
        if structured_seen and (line.startswith("- **") or line.startswith("  ")):
            continue
        if structured_seen:
            return index
    return len(lines)
'''
SOURCE, count = re.subn(
    r'def end_of_explanation\(lines: list\[str\], start: int\) -> int:\n.*?\n\ndef check\(',
    validator_boundary + '\n\ndef check(',
    SOURCE,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("fonction de frontière du validateur introuvable")

refinement_boundary = '''def explanation_end(lines: list[str], start: int) -> int:
    wrapper_seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == WRAPPER:
            wrapper_seen = True
            continue
        if wrapper_seen and (line.startswith("- **") or line.startswith("  ")):
            continue
        if wrapper_seen:
            return index
    return len(lines)
'''
SOURCE, count = re.subn(
    r'def explanation_end\(lines: list\[str\], start: int\) -> int:\n.*?\n\ndef parse_bullets\(',
    refinement_boundary + '\n\ndef parse_bullets(',
    SOURCE,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("fonction de frontière du raffinement introuvable")

exec(compile(SOURCE, __file__, "exec"))
