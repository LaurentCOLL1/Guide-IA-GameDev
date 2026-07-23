#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
import os
import subprocess
from pathlib import Path

EXPECTED_PACKAGE_SHA = "2d70d119a36bf61e6cdb6bb38b24abb79adc5cee48806149083ce5393e6fc494"
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "1eaa54f65360d61d2268e6037892b0be671a4f1cdc49957c6f9c31263f17b6dc"
DIAGNOSTIC_PATH = Path(".qa/ch13-diagnostic.json")

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
report = {"fragment_count": len(parts), "original_lengths": [len(part) for part in parts]}
if len(parts) == 14 and len(parts[12]) == 6263 and len(parts[13]) == 20:
    parts[13] = parts[12][4000:] + parts[13]
    parts[12] = parts[12][:4000]
if len("".join(parts)) % 4 == 3:
    parts[-1] += "="
report["corrected_lengths"] = [len(part) for part in parts]
report["encoded_length"] = len("".join(parts))

try:
    compressed = base64.b64decode("".join(parts), validate=True)
    report["base64_valid"] = True
    actual_package_sha = hashlib.sha256(compressed).hexdigest()
    report["actual_package_sha256"] = actual_package_sha
    report["package_sha_matches"] = actual_package_sha == EXPECTED_PACKAGE_SHA
    report["compressed_length"] = len(compressed)
    raw = gzip.decompress(compressed)
    report["gzip_valid"] = True
    report["uncompressed_length"] = len(raw)
    payload = json.loads(raw.decode("utf-8"))
    report["json_valid"] = True
    report["schema"] = payload.get("schema")
    files = payload.get("files") if isinstance(payload, dict) else None
    report["payload_paths"] = sorted(files) if isinstance(files, dict) else []
    if isinstance(files, dict):
        chapter_key = "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md"
        audit_key = "Livre-III/QA/AUDIT-CHAPITRE-13.md"
        chapter = files.get(chapter_key)
        audit = files.get(audit_key)
        report["governance_present"] = ".qa/ch13-governance.py" in files
        report["close_present"] = ".qa/ch13-close.py" in files
        if isinstance(chapter, str):
            chapter_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
            report["actual_chapter_sha256"] = chapter_sha
            report["chapter_sha_matches"] = chapter_sha == EXPECTED_CHAPTER_SHA
            report["chapter_lines"] = len(chapter.splitlines())
        if isinstance(audit, str):
            audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()
            report["actual_audit_sha256"] = audit_sha
            report["audit_sha_matches"] = audit_sha == EXPECTED_AUDIT_SHA
            report["audit_lines"] = len(audit.splitlines())
except Exception as exc:
    report["error"] = f"{type(exc).__name__}: {exc}"

DIAGNOSTIC_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", str(DIAGNOSTIC_PATH)], check=True)
if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
    subprocess.run(["git", "commit", "-m", "chore(ch13): mesurer le paquet réparé"], check=True)
    subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)
raise RuntimeError("Diagnostic du paquet réparé enregistré ; matérialisation interrompue.")
