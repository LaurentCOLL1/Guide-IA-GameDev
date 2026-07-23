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
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
DIAGNOSTIC_PATH = Path(".qa/ch13-diagnostic.json")

fragment_paths = sorted(Path(".qa").glob("ch13-package-*.txt"))
parts = [path.read_text(encoding="utf-8").strip() for path in fragment_paths]
report = {"fragment_lengths": [len(part) for part in parts], "candidates": []}

if len(parts) != 14 or len(parts[12]) != 6263 or len(parts[13]) != 20:
    report["error"] = "Forme du paquet inattendue."
else:
    fragment_13 = parts[12][:4000]
    prefix_14 = parts[12][4000:]
    suffix_14 = parts[13]
    for character in BASE64_ALPHABET:
        candidate_14 = prefix_14 + character + suffix_14
        encoded = "".join(parts[:12] + [fragment_13, candidate_14])
        item = {"character": character}
        try:
            compressed = base64.b64decode(encoded, validate=True)
            item["package_sha256"] = hashlib.sha256(compressed).hexdigest()
            item["package_sha_matches"] = item["package_sha256"] == EXPECTED_PACKAGE_SHA
            raw = gzip.decompress(compressed)
            item["gzip_valid"] = True
            payload = json.loads(raw.decode("utf-8"))
            item["json_valid"] = True
            files = payload.get("files") if isinstance(payload, dict) else None
            if isinstance(files, dict):
                chapter = files.get("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
                audit = files.get("Livre-III/QA/AUDIT-CHAPITRE-13.md")
                if isinstance(chapter, str):
                    item["chapter_sha256"] = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
                    item["chapter_sha_matches"] = item["chapter_sha256"] == EXPECTED_CHAPTER_SHA
                    item["chapter_lines"] = len(chapter.splitlines())
                if isinstance(audit, str):
                    item["audit_sha256"] = hashlib.sha256(audit.encode("utf-8")).hexdigest()
                    item["audit_sha_matches"] = item["audit_sha256"] == EXPECTED_AUDIT_SHA
                    item["audit_lines"] = len(audit.splitlines())
                item["governance_present"] = ".qa/ch13-governance.py" in files
                item["close_present"] = ".qa/ch13-close.py" in files
        except Exception as exc:
            item["error"] = f"{type(exc).__name__}: {exc}"
        if item.get("gzip_valid") or item.get("package_sha_matches"):
            report["candidates"].append(item)

DIAGNOSTIC_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", str(DIAGNOSTIC_PATH)], check=True)
if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
    subprocess.run(["git", "commit", "-m", "chore(ch13): tester les candidats du paquet"], check=True)
    subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)
raise RuntimeError("Diagnostic des candidats enregistré ; matérialisation interrompue.")
