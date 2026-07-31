#!/usr/bin/env python3
"""Validate the machine-checkable structure of the tagged technical PDF."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "accessible-pdf"
PDF = DIST / "Guide-IA-GameDev-tagged.pdf"
MANIFEST = DIST / "accessible-pdf-manifest.json"


def command(args: list[str]) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE)
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DIST / "validation.json")
    parser.add_argument("--verapdf-report", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    if not PDF.is_file():
        errors.append("PDF absent")
    if not MANIFEST.is_file():
        errors.append("manifeste absent")
    for executable in ("pdfinfo", "qpdf", "pdftotext"):
        if shutil.which(executable) is None:
            errors.append(f"outil absent : {executable}")
    if errors:
        raise SystemExit("; ".join(errors))

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    info = command(["pdfinfo", str(PDF)])
    qpdf_json = command(["qpdf", "--json", str(PDF)])
    first_text = command(["pdftotext", "-f", "1", "-l", "3", str(PDF), "-"])

    pages_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
    pages = int(pages_match.group(1)) if pages_match else 0
    checks = {
        "markinfo_marked": '"/MarkInfo"' in qpdf_json and '"/Marked": true' in qpdf_json,
        "structure_tree": '"/StructTreeRoot"' in qpdf_json,
        "document_language": '"/Lang": "u:fr-FR"' in qpdf_json or '"/Lang": "fr-FR"' in qpdf_json,
        "title_metadata": "Guide réaliste" in info or "Guide réaliste" in first_text,
        "author_metadata": "Laurent Collin" in info or "Laurent Collin" in first_text,
        "page_count_plausible": pages >= 4000,
        "manifest_claim_bounded": manifest.get("claim") == "tagged-pdf-machine-checked-not-full-pdfua-conformance",
        "source_count": manifest.get("source_count") == 162,
    }
    for name, passed in checks.items():
        if not passed:
            errors.append(name)

    verapdf = {
        "executed": False,
        "profile": "ua1",
        "machine_compliant": None,
        "failed_checks": None,
        "note": "veraPDF covers machine-verifiable PDF/UA checks only",
    }
    if args.verapdf_report and args.verapdf_report.is_file():
        verapdf["executed"] = True
        text = args.verapdf_report.read_text(encoding="utf-8", errors="replace")
        verapdf["machine_compliant"] = 'isCompliant="true"' in text or 'compliant="1"' in text
        failed = re.search(r"failedChecks=\"(\d+)\"", text)
        verapdf["failed_checks"] = int(failed.group(1)) if failed else None

    report = {
        "schema_version": 1,
        "status": "success" if not errors else "failure",
        "errors": errors,
        "checks": checks,
        "pages": pages,
        "bytes": PDF.stat().st_size,
        "claim": manifest.get("claim"),
        "verapdf": verapdf,
        "human_checks_required": [
            "reading-order",
            "alternative-text-quality",
            "heading-hierarchy",
            "table-semantics",
            "screen-reader-behaviour",
        ],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
