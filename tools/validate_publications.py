#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

EXPECTED_LICENSE = "CC BY-SA 4.0"


def run_text(command: list[str]) -> str:
    result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class PublicationHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.fragments: list[str] = []
        self.file_urls: list[str] = []
        self.lang = ""
        self.title_parts: list[str] = []
        self.in_title = False
        self.has_toc = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.lang = values.get("lang", "")
        identifier = values.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicate_ids.add(identifier)
            self.ids.add(identifier)
            if identifier == "TOC":
                self.has_toc = True
        href = values.get("href", "")
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(href[1:])
        if href.startswith("file://"):
            self.file_urls.append(href)
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def validate_pdf(path: Path, work: Path) -> dict[str, object]:
    qpdf = run_text(["qpdf", "--check", str(path)])
    info = run_text(["pdfinfo", str(path)])
    fonts = run_text(["pdffonts", str(path)])
    text_path = work / "publication.txt"
    subprocess.run(["pdftotext", str(path), str(text_path)], check=True)
    text = text_path.read_text(encoding="utf-8", errors="replace")
    pages_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
    page_size_match = re.search(r"^Page size:\s+(.+)$", info, re.MULTILINE)
    pages = int(pages_match.group(1)) if pages_match else 0
    errors: list[str] = []
    if pages < 4000:
        errors.append(f"pdf-pages:{pages}")
    if "A4" not in (page_size_match.group(1) if page_size_match else ""):
        errors.append("pdf-not-a4")
    if EXPECTED_LICENSE not in text or "Guide IA GameDev" not in text:
        errors.append("pdf-license-or-title-missing")
    font_lines = [line for line in fonts.splitlines()[2:] if line.strip()]
    if not font_lines:
        errors.append("pdf-fonts-empty")
    for line in font_lines:
        if (
            "Type 3" in line
            or "unknown" in line.lower()
            or re.search(r"\sno\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$", line)
        ):
            errors.append("pdf-font-not-embedded")
            break
    return {
        "pages": pages,
        "page_size": page_size_match.group(1) if page_size_match else None,
        "text_bytes": text_path.stat().st_size,
        "qpdf": "No syntax or stream encoding errors found" in qpdf,
        "font_rows": len(font_lines),
        "errors": errors,
    }


def validate_html(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    parser = PublicationHTMLParser()
    parser.feed(raw)
    errors: list[str] = []
    missing_fragments = sorted(set(parser.fragments) - parser.ids)
    if parser.lang.lower() not in {"fr", "fr-fr"}:
        errors.append(f"html-lang:{parser.lang}")
    if not parser.has_toc:
        errors.append("html-toc-missing")
    if parser.duplicate_ids:
        errors.append(f"html-duplicate-ids:{len(parser.duplicate_ids)}")
    if missing_fragments:
        errors.append(f"html-missing-fragments:{len(missing_fragments)}")
    title = "".join(parser.title_parts).strip()
    if "Guide réaliste" not in title:
        errors.append("html-title-missing")
    if EXPECTED_LICENSE not in raw or "Guide IA GameDev" not in raw:
        errors.append("html-license-or-project-missing")
    if parser.file_urls:
        errors.append(f"html-file-urls:{len(parser.file_urls)}")
    return {
        "lang": parser.lang,
        "title": title,
        "ids": len(parser.ids),
        "internal_fragments": len(parser.fragments),
        "missing_fragments": len(missing_fragments),
        "missing_fragment_sample": missing_fragments[:50],
        "duplicate_id_sample": sorted(parser.duplicate_ids)[:50],
        "file_url_sample": parser.file_urls[:20],
        "errors": errors,
    }


def validate_epub(path: Path, epubcheck_jar: Path) -> dict[str, object]:
    errors: list[str] = []
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            errors.append("epub-mimetype-not-first")
        if archive.read("mimetype") != b"application/epub+zip":
            errors.append("epub-mimetype-invalid")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            errors.append("epub-mimetype-compressed")
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find("{urn:oasis:names:tc:opendocument:xmlns:container}rootfiles/{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
        package_path = rootfile.attrib["full-path"] if rootfile is not None else ""
        if not package_path or package_path not in names:
            errors.append("epub-package-missing")
        text = "\n".join(
            archive.read(name).decode("utf-8", errors="replace")
            for name in names
            if name.lower().endswith((".xhtml", ".html", ".opf", ".xml"))
        )
        if EXPECTED_LICENSE not in text or "Guide IA GameDev" not in text:
            errors.append("epub-license-or-project-missing")
    result = subprocess.run(
        ["java", "-Xss4m", "-Xmx2g", "-jar", str(epubcheck_jar.resolve()), str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    epubcheck_output = result.stdout
    if result.returncode != 0:
        errors.append(f"epubcheck-exit:{result.returncode}")
        print(epubcheck_output, file=sys.stderr)
    return {
        "entries": len(names),
        "package_path": package_path,
        "epubcheck_exit": result.returncode,
        "epubcheck_summary": epubcheck_output[-8000:],
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated PDF, HTML and EPUB publications")
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--epubcheck-jar", type=Path, required=True)
    args = parser.parse_args()

    dist = args.dist.resolve()
    files = {
        "pdf": dist / "Guide-IA-GameDev.pdf",
        "html": dist / "Guide-IA-GameDev.html",
        "epub": dist / "Guide-IA-GameDev.epub",
    }
    missing = [str(path) for path in files.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("Artefacts absents : " + ", ".join(missing))
    if not args.epubcheck_jar.is_file():
        raise FileNotFoundError(f"EPUBCheck absent : {args.epubcheck_jar}")

    with tempfile.TemporaryDirectory(prefix="validate-publications-") as temporary:
        work = Path(temporary)
        results = {
            "pdf": validate_pdf(files["pdf"], work),
            "html": validate_html(files["html"]),
            "epub": validate_epub(files["epub"], args.epubcheck_jar),
        }
    errors = [f"{fmt}:{error}" for fmt, result in results.items() for error in result["errors"]]
    report = {
        "schema_version": 1,
        "status": "success" if not errors else "failure",
        "artifacts": {
            fmt: {"file": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for fmt, path in files.items()
        },
        "results": results,
        "errors": errors,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "errors": errors, "artifacts": report["artifacts"]}, ensure_ascii=False, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, subprocess.CalledProcessError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"publication-validation-error: {exc}", file=sys.stderr)
        raise SystemExit(1)
