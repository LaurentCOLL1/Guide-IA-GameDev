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
report = {
    "fragment_count": len(fragment_paths),
    "expected_fragment_count": 14,
    "expected_package_sha256": EXPECTED_PACKAGE_SHA,
    "expected_chapter_sha256": EXPECTED_CHAPTER_SHA,
    "expected_audit_sha256": EXPECTED_AUDIT_SHA,
    "fragments": [],
}
encoded_parts = []
for path in fragment_paths:
    text = path.read_text(encoding="utf-8").strip()
    encoded_parts.append(text)
    report["fragments"].append({
        "path": str(path),
        "length": len(text),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    })

encoded = "".join(encoded_parts)
report["encoded_length"] = len(encoded)
try:
    compressed = base64.b64decode(encoded, validate=True)
    report["base64_valid"] = True
    report["actual_package_sha256"] = hashlib.sha256(compressed).hexdigest()
    report["package_sha_matches"] = report["actual_package_sha256"] == EXPECTED_PACKAGE_SHA
    try:
        raw = gzip.decompress(compressed)
        report["gzip_valid"] = True
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
            if isinstance(chapter, str):
                report["actual_chapter_sha256"] = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
                report["chapter_sha_matches"] = report["actual_chapter_sha256"] == EXPECTED_CHAPTER_SHA
                report["chapter_lines"] = len(chapter.splitlines())
            if isinstance(audit, str):
                report["actual_audit_sha256"] = hashlib.sha256(audit.encode("utf-8")).hexdigest()
                report["audit_sha_matches"] = report["actual_audit_sha256"] == EXPECTED_AUDIT_SHA
                report["audit_lines"] = len(audit.splitlines())
    except Exception as exc:
        report["gzip_or_json_error"] = f"{type(exc).__name__}: {exc}"
except Exception as exc:
    report["base64_valid"] = False
    report["base64_error"] = f"{type(exc).__name__}: {exc}"

DIAGNOSTIC_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if os.environ.get("HEAD_BRANCH") and not os.environ.get("CH13_DIAGNOSTIC_ALREADY_PUSHED"):
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
    subprocess.run(["git", "add", str(DIAGNOSTIC_PATH)], check=True)
    status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if status.returncode != 0:
        subprocess.run(["git", "commit", "-m", "chore(ch13): enregistrer le diagnostic du paquet"], check=True)
        subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)

raise RuntimeError("Diagnostic du paquet chapitre 13 enregistré ; matérialisation volontairement interrompue.")
