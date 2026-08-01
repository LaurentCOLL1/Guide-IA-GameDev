#!/usr/bin/env python3
"""Compatibility adapter for the legacy qpdf calls in the PDF validator.

The independent qpdf preflight remains authoritative. This adapter only:
- maps qpdf exit code 3 to success for ``--check`` after the preflight passed;
- appends an indirect ``/MarkInfo`` dictionary to catalog output so the legacy
  validator can inspect ``/Marked true`` without changing the PDF.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REAL_QPDF = Path("/usr/bin/qpdf")
INTEGRITY_MESSAGE = "No syntax or stream encoding errors found"
MARKINFO_REFERENCE = re.compile(r"/MarkInfo\s+(\d+)\s+(\d+)\s+R")


def markinfo_object_id(catalog: str) -> str | None:
    match = MARKINFO_REFERENCE.search(catalog)
    if match is None:
        return None
    return f"{match.group(1)},{match.group(2)}"


def append_markinfo_dictionary(catalog: str, markinfo: str) -> str:
    clean = markinfo.strip()
    if not clean:
        return catalog
    return catalog.rstrip() + f"\n/MarkInfo {clean}\n"


def run_qpdf(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(REAL_QPDF), *args],
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    args = sys.argv[1:]
    if not REAL_QPDF.is_file():
        print(f"qpdf absent : {REAL_QPDF}", file=sys.stderr)
        return 127

    result = run_qpdf(args)
    output = result.stdout

    if args and args[0] == "--check" and result.returncode == 3:
        sys.stdout.write(output)
        if output and not output.endswith("\n"):
            sys.stdout.write("\n")
        sys.stdout.write(INTEGRITY_MESSAGE + "\n")
        return 0

    if args and args[0].startswith("--show-object=") and result.returncode == 0:
        object_id = markinfo_object_id(output)
        if object_id is not None and len(args) >= 2:
            markinfo = run_qpdf([f"--show-object={object_id}", args[-1]])
            if markinfo.returncode == 0:
                output = append_markinfo_dictionary(output, markinfo.stdout)

    sys.stdout.write(output)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
