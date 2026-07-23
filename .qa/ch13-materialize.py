#!/usr/bin/env python3
import base64
import hashlib
import json
import os
import subprocess
import zlib
from pathlib import Path

EXPECTED = {
    "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md": "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9",
    "Livre-III/QA/AUDIT-CHAPITRE-13.md": "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc",
}
DIAGNOSTIC_PATH = Path(".qa/ch13-diagnostic.json")

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
encoded = "".join(parts[:12]) + parts[12][:4000] + parts[12][4000:] + parts[13] + "="
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

deflate = compressed[position:-8]
decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
output = bytearray()
error = None
consumed = 0
for offset in range(0, len(deflate), 128):
    chunk = deflate[offset:offset + 128]
    try:
        output.extend(decompressor.decompress(chunk))
        consumed = offset + len(chunk)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        consumed = offset
        break
if error is None:
    try:
        output.extend(decompressor.flush())
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"

text = output.decode("utf-8", errors="ignore")
report = {
    "compressed_length": len(compressed),
    "deflate_start": position,
    "deflate_length": len(deflate),
    "deflate_consumed_before_error": consumed,
    "partial_output_bytes": len(output),
    "decompression_error": error,
    "recovered": {},
    "partial_tail": text[-500:],
}

decoder = json.JSONDecoder()
for path, expected_sha in EXPECTED.items():
    key = json.dumps(path, ensure_ascii=False)
    index = text.find(key)
    item = {"key_found": index >= 0}
    if index >= 0:
        colon = text.find(":", index + len(key))
        if colon >= 0:
            value_start = colon + 1
            while value_start < len(text) and text[value_start].isspace():
                value_start += 1
            try:
                value, end = decoder.raw_decode(text, value_start)
                item["value_decoded"] = isinstance(value, str)
                item["value_end"] = end
                if isinstance(value, str):
                    actual_sha = hashlib.sha256(value.encode("utf-8")).hexdigest()
                    item["sha256"] = actual_sha
                    item["sha_matches"] = actual_sha == expected_sha
                    item["lines"] = len(value.splitlines())
                    item["characters"] = len(value)
            except Exception as exc:
                item["decode_error"] = f"{type(exc).__name__}: {exc}"
    report["recovered"][path] = item

DIAGNOSTIC_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", str(DIAGNOSTIC_PATH)], check=True)
if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
    subprocess.run(["git", "commit", "-m", "chore(ch13): analyser la sortie DEFLATE partielle"], check=True)
    subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)
raise RuntimeError("Diagnostic DEFLATE partiel enregistré ; matérialisation interrompue.")
