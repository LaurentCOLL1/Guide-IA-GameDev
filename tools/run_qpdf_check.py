#!/usr/bin/env python3
"""Run qpdf preflight while preserving warnings as structured evidence."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

INTEGRITY_MESSAGE = "No syntax or stream encoding errors found"
WARNING_SUCCESS_MESSAGE = "qpdf: operation succeeded with warnings"


def classify_qpdf_result(return_code: int, output: str) -> dict[str, object]:
    warning_lines = [
        line.strip()
        for line in output.splitlines()
        if "WARNING:" in line or WARNING_SUCCESS_MESSAGE in line.lower()
    ]
    clean_integrity = INTEGRITY_MESSAGE in output
    warning_success = WARNING_SUCCESS_MESSAGE in output.lower()
    if return_code == 0:
        completion_marker = clean_integrity
    elif return_code == 3:
        completion_marker = warning_success
    else:
        completion_marker = False

    errors: list[str] = []
    warnings: list[str] = []
    if return_code not in {0, 3}:
        errors.append(f"qpdf_exit_code:{return_code}")
    if not completion_marker:
        errors.append("qpdf_completion_marker_absent")
    if return_code == 3:
        warnings.append("qpdf_completed_with_warnings")
    if warning_lines:
        warnings.append("qpdf_reported_warnings")

    if errors:
        status = "failure"
    elif warnings:
        status = "success-with-reservations"
    else:
        status = "success"

    return {
        "schema_version": 2,
        "status": status,
        "exit_code": return_code,
        "completion_marker_present": completion_marker,
        "clean_integrity_message_present": clean_integrity,
        "warning_success_message_present": warning_success,
        "errors": errors,
        "warnings": warnings,
        "warning_lines": warning_lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--text", type=Path, required=True)
    args = parser.parse_args()

    qpdf = shutil.which("qpdf")
    if qpdf is None:
        raise SystemExit("qpdf absent")
    if not args.pdf.is_file():
        raise SystemExit(f"PDF absent : {args.pdf}")

    result = subprocess.run(
        [qpdf, "--check", str(args.pdf)],
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    output = result.stdout
    report = classify_qpdf_result(result.returncode, output)
    report["pdf"] = args.pdf.as_posix()

    args.text.parent.mkdir(parents=True, exist_ok=True)
    args.text.write_text(output, encoding="utf-8")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
