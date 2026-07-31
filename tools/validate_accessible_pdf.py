#!/usr/bin/env python3
"""Validate the machine-checkable structure of the tagged technical PDF."""
from __future__ import annotations

import argparse
import hashlib
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
    result = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def catalog_text() -> str:
    """Read only the PDF trailer and catalog, never page-content streams."""
    trailer = command(["qpdf", "--show-object=trailer", str(PDF)])
    root_match = re.search(r"/Root\s+(\d+)\s+(\d+)\s+R", trailer)
    if not root_match:
        return trailer
    object_id = f"{root_match.group(1)},{root_match.group(2)}"
    catalog = command(["qpdf", f"--show-object={object_id}", str(PDF)])
    return trailer + "\n" + catalog


def parse_verapdf(report: Path | None) -> tuple[dict[str, object], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    result: dict[str, object] = {
        "executed": False,
        "profile": "ua1",
        "report_parsed": False,
        "machine_compliant": None,
        "failed_checks": None,
        "note": "veraPDF covers machine-verifiable PDF/UA checks only",
    }
    if report is None:
        errors.append("verapdf_report_not_requested")
        return result, errors, warnings
    if not report.is_file() or report.stat().st_size == 0:
        errors.append("verapdf_report_absent_or_empty")
        return result, errors, warnings

    result["executed"] = True
    text = report.read_text(encoding="utf-8", errors="replace")
    compliant_true = bool(
        re.search(r'(?:isCompliant|compliant)="(?:true|1)"', text, re.IGNORECASE)
    )
    compliant_false = bool(
        re.search(r'(?:isCompliant|compliant)="(?:false|0)"', text, re.IGNORECASE)
    )
    if compliant_true == compliant_false:
        errors.append("verapdf_result_unparseable")
        return result, errors, warnings

    result["report_parsed"] = True
    result["machine_compliant"] = compliant_true
    failed = re.search(r'failedChecks="(\d+)"', text)
    result["failed_checks"] = int(failed.group(1)) if failed else None
    if not compliant_true:
        warnings.append("verapdf_ua1_noncompliance_requires_correction_or_reservation")
    return result, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DIST / "validation.json")
    parser.add_argument("--verapdf-report", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
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
    pdf_hash = sha256(PDF)
    qpdf_check = command(["qpdf", "--check", str(PDF)])
    info = command(["pdfinfo", str(PDF)])
    catalog = catalog_text()
    first_text = command(["pdftotext", "-f", "1", "-l", "3", str(PDF), "-"])

    pages_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
    pages = int(pages_match.group(1)) if pages_match else 0
    normalized_catalog = re.sub(r"\s+", " ", catalog)
    checks = {
        "qpdf_integrity": "No syntax or stream encoding errors found" in qpdf_check,
        "pdfinfo_tagged": bool(re.search(r"^Tagged:\s+yes$", info, re.MULTILINE | re.IGNORECASE)),
        "markinfo_marked": bool(
            re.search(r"/MarkInfo\s*<<.*?/Marked\s+true.*?>>", normalized_catalog)
        ),
        "structure_tree": bool(re.search(r"/StructTreeRoot\s+\d+\s+\d+\s+R", catalog)),
        "document_language": bool(
            re.search(r"/Lang\s*\(fr-FR\)", catalog)
            or re.search(r"/Lang\s*<66722[dD]4652>", catalog)
            or re.search(r"/Lang\s*<feff00660072002[dD]00460052>", catalog)
        ),
        "title_metadata": "Guide réaliste" in info or "Guide réaliste" in first_text,
        "author_metadata": "Laurent Collin" in info or "Laurent Collin" in first_text,
        "page_count_plausible": pages >= 4000,
        "manifest_claim_bounded": manifest.get("claim")
        == "tagged-pdf-machine-checked-not-full-pdfua-conformance",
        "manifest_standard_target": manifest.get("standard_target") == "PDF/UA-1",
        "source_count": manifest.get("source_count") == 162,
        "manifest_bytes_match": manifest.get("bytes") == PDF.stat().st_size,
        "manifest_sha256_match": manifest.get("sha256") == pdf_hash,
    }
    for name, passed in checks.items():
        if not passed:
            errors.append(name)

    verapdf, verapdf_errors, verapdf_warnings = parse_verapdf(args.verapdf_report)
    errors.extend(verapdf_errors)
    warnings.extend(verapdf_warnings)

    if errors:
        status = "failure"
    elif warnings:
        status = "success-with-reservations"
    else:
        status = "success"

    report = {
        "schema_version": 2,
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "pages": pages,
        "bytes": PDF.stat().st_size,
        "sha256": pdf_hash,
        "claim": manifest.get("claim"),
        "verapdf": verapdf,
        "human_checks_required": [
            "reading-order",
            "alternative-text-quality",
            "heading-hierarchy",
            "list-and-table-semantics",
            "links-notes-code-and-formulas",
            "screen-reader-behaviour",
        ],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
