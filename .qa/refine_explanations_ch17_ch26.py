from __future__ import annotations

import base64
import gzip
import hashlib
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
SOURCE = SOURCE.replace(
    'or line.startswith("**Symptôme")\n            ):',
    'or line.startswith("**Symptôme")\n                or line.startswith("<a id=")\n            ):',
    1,
)
SOURCE = SOURCE.replace(
    'or line.startswith("**Symptôme")\n    )',
    'or line.startswith("**Symptôme")\n        or line.startswith("<a id=")\n    )',
    1,
)
exec(compile(SOURCE, __file__, "exec"))
