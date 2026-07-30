#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "publications"
REQUIRED = {
    "pdf": DIST / "Guide-IA-GameDev.pdf",
    "html": DIST / "Guide-IA-GameDev.html",
    "epub": DIST / "Guide-IA-GameDev.epub",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(*args: str) -> str:
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DIST / "validation.json")
    args = parser.parse_args()
    errors: list[str] = []
    result: dict[str, object] = {"schema_version": 1, "status": "failure", "formats": {}}

    for fmt, path in REQUIRED.items():
        if not path.is_file() or path.stat().st_size < 1000:
            errors.append(f"missing-or-small:{fmt}")
        else:
            result["formats"][fmt] = {"bytes": path.stat().st_size, "sha256": sha256(path)}

    pdf = REQUIRED["pdf"]
    if pdf.is_file():
        try:
            info = command("pdfinfo", str(pdf))
            match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
            if match is None:
                errors.append("pdf:missing-page-count")
            else:
                pages = int(match.group(1))
                if pages < 100:
                    errors.append("pdf:unexpected-page-count")
                result["formats"]["pdf"]["pages"] = pages
            text = command("pdftotext", "-f", "1", "-l", "5", str(pdf), "-")
            if "Guide" not in text or "Laurent" not in text:
                errors.append("pdf:missing-title-or-author")
        except Exception as exc:
            errors.append(f"pdf:inspection:{type(exc).__name__}")

    html = REQUIRED["html"]
    if html.is_file():
        text = html.read_text(encoding="utf-8", errors="replace")
        for needle in ("<!DOCTYPE html", "Guide IA GameDev", "CC-BY-SA-4.0"):
            if needle not in text:
                errors.append(f"html:missing:{needle}")
        toc_patterns = (
            r'id=["\']TOC["\']',
            r'id=["\']table-of-contents["\']',
            r'role=["\']doc-toc["\']',
        )
        if not any(re.search(pattern, text, re.IGNORECASE) for pattern in toc_patterns):
            errors.append("html:missing:toc")
        if re.search(r'(?:src|href)=["\'](?:/|file:)', text):
            errors.append("html:absolute-local-resource")

    epub = REQUIRED["epub"]
    if epub.is_file():
        try:
            with zipfile.ZipFile(epub) as archive:
                names = archive.namelist()
                if not names or names[0] != "mimetype":
                    errors.append("epub:mimetype-not-first")
                mimetype = archive.read("mimetype").decode("ascii")
                if mimetype != "application/epub+zip":
                    errors.append("epub:bad-mimetype")
                container = archive.read("META-INF/container.xml").decode("utf-8")
                if "rootfile" not in container:
                    errors.append("epub:missing-rootfile")
                joined = "\n".join(
                    archive.read(name).decode("utf-8", errors="ignore")
                    for name in names if name.endswith((".opf", ".xhtml", ".html"))
                )
                if "CC BY-SA 4.0" not in joined and "CC-BY-SA-4.0" not in joined:
                    errors.append("epub:missing-license")
                result["formats"]["epub"]["entries"] = len(names)
        except Exception as exc:
            errors.append(f"epub:inspection:{type(exc).__name__}")

    manifest_path = DIST / "publication-manifest.json"
    if not manifest_path.is_file():
        errors.append("manifest:missing")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("publication_status") != "technical-build-not-official-release":
            errors.append("manifest:publication-status")
        for fmt, path in REQUIRED.items():
            if path.is_file() and manifest.get("outputs", {}).get(fmt, {}).get("sha256") != sha256(path):
                errors.append(f"manifest:sha256:{fmt}")
        result["source_count"] = manifest.get("source_count")

    result["errors"] = errors
    result["status"] = "success" if not errors else "failure"
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
