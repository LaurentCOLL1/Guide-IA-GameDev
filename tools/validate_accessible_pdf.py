#!/usr/bin/env python3
"""Validate the tagged PDF candidate and separate machine checks from human review."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "publications"
PDF = DIST / "Guide-IA-GameDev-accessible.pdf"
MANIFEST = DIST / "accessible-pdf-manifest.json"
DEFAULT_REPORT = DIST / "accessible-pdf-validation.json"
DEFAULT_VERAPDF_IMAGE = "verapdf/cli:v1.30.2"
CONTAINER_ROOT = Path("/data")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def command(*args: str, timeout: int = 300) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    return completed.stdout


def recursive_values(node: Any, key_names: set[str]) -> list[Any]:
    values: list[Any] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key.lower() in key_names:
                values.append(value)
            values.extend(recursive_values(value, key_names))
    elif isinstance(node, list):
        for value in node:
            values.extend(recursive_values(value, key_names))
    return values


def source_audit() -> dict[str, Any]:
    errors: list[str] = []
    image_count = 0
    raw_image_count = 0
    contents = ROOT / "contents.txt"
    metadata = ROOT / "metadata-accessible-pdf.yaml"
    sources: list[Path] = []

    for raw in contents.read_text(encoding="utf-8").splitlines():
        item = raw.strip()
        if item and not item.startswith("#"):
            sources.append(ROOT / item)

    markdown_image = re.compile(r"!\[([^\]]*)\]\([^\n)]+\)")
    raw_img = re.compile(r"<img\b([^>]*)>", re.IGNORECASE)
    alt_attr = re.compile(r"\balt\s*=\s*([\"'])(.*?)\1", re.IGNORECASE | re.DOTALL)

    for path in sources:
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in markdown_image.finditer(text):
            image_count += 1
            if not match.group(1).strip():
                errors.append(f"source:image-alt-empty:{path.relative_to(ROOT)}")
        for match in raw_img.finditer(text):
            raw_image_count += 1
            alt = alt_attr.search(match.group(1))
            if alt is None or not alt.group(2).strip():
                errors.append(f"source:raw-image-alt-empty:{path.relative_to(ROOT)}")

    metadata_text = metadata.read_text(encoding="utf-8") if metadata.is_file() else ""
    for needle in ("lang: fr-FR", "pdfstandard: ua-2", "title:", "author:"):
        if needle not in metadata_text:
            errors.append(f"metadata:missing:{needle}")

    return {
        "source_count": len(sources),
        "markdown_images": image_count,
        "raw_html_images": raw_image_count,
        "errors": errors,
    }


def run_verapdf(image: str, pdf: Path) -> tuple[dict[str, Any] | None, str, list[str]]:
    errors: list[str] = []
    if shutil.which("docker") is None:
        return None, "", ["verapdf:docker-missing"]

    relative = pdf.relative_to(ROOT)
    docker_command = [
        "docker",
        "run",
        "--rm",
        "--network=none",
        "--security-opt",
        "no-new-privileges",
        "--volume",
        f"{ROOT}:{CONTAINER_ROOT}:ro",
        image,
        "--format",
        "json",
        "--maxfailuresdisplayed",
        "100",
        "-f",
        "ua2",
        str(CONTAINER_ROOT / relative),
    ]
    completed = subprocess.run(
        docker_command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=900,
    )
    raw = completed.stdout.strip()
    if not raw:
        errors.append("verapdf:empty-report")
        if completed.stderr.strip():
            errors.append(f"verapdf:stderr:{completed.stderr.strip()[:400]}")
        return None, raw, errors

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        errors.append("verapdf:invalid-json")
        return None, raw, errors

    compliance_values = recursive_values(payload, {"compliant", "iscompliant"})
    boolean_values = [value for value in compliance_values if isinstance(value, bool)]
    if not boolean_values:
        errors.append("verapdf:missing-compliance-result")
    elif any(value is False for value in boolean_values):
        errors.append("verapdf:pdfua2-non-compliant")
    elif not any(value is True for value in boolean_values):
        errors.append("verapdf:pdfua2-not-confirmed")

    if completed.returncode not in (0, 1):
        errors.append(f"verapdf:exit:{completed.returncode}")
    return payload, raw, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, default=PDF)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--verapdf-image", default=os.environ.get("VERAPDF_IMAGE", DEFAULT_VERAPDF_IMAGE))
    args = parser.parse_args()

    errors: list[str] = []
    result: dict[str, Any] = {
        "schema_version": 1,
        "status": "failure",
        "standard": "PDF/UA-2",
        "machine_validation": {},
        "source_audit": {},
        "human_validation": {
            "status": "required-before-accessibility-conformance-claim",
            "checks": [
                "ordre de lecture complet avec technologies d'assistance",
                "qualité contextuelle des alternatives textuelles",
                "navigation par titres, listes, tableaux, liens et notes",
                "prononciation et compréhension du contenu français",
                "essais avec au moins un lecteur d'écran et un lecteur PDF cible",
            ],
        },
        "reservations": [
            "veraPDF couvre uniquement les exigences PDF/UA vérifiables par machine",
            "aucune certification d'accessibilité ni conformité utilisateur exhaustive n'est revendiquée",
            "aucune release publique n'est produite",
        ],
    }

    pdf = args.pdf.resolve()
    if not pdf.is_file() or pdf.stat().st_size < 1000:
        errors.append("pdf:missing-or-small")
    if not args.manifest.is_file():
        errors.append("manifest:missing")

    source_result = source_audit()
    result["source_audit"] = source_result
    errors.extend(source_result["errors"])

    if pdf.is_file():
        result["pdf"] = {"file": pdf.name, "bytes": pdf.stat().st_size, "sha256": sha256(pdf)}
        try:
            info = command("pdfinfo", str(pdf))
            tagged = re.search(r"^Tagged:\s+yes\s*$", info, re.MULTILINE | re.IGNORECASE) is not None
            pages_match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.MULTILINE)
            pages = int(pages_match.group(1)) if pages_match else 0
            title_match = re.search(r"^Title:\s+(.+)$", info, re.MULTILINE)
            result["machine_validation"]["pdfinfo"] = {
                "tagged": tagged,
                "pages": pages,
                "title": title_match.group(1).strip() if title_match else None,
            }
            if not tagged:
                errors.append("pdfinfo:not-tagged")
            if pages < 100:
                errors.append("pdfinfo:unexpected-page-count")
            if title_match is None or "Guide" not in title_match.group(1):
                errors.append("pdfinfo:missing-title")
        except Exception as exc:
            errors.append(f"pdfinfo:{type(exc).__name__}")

        try:
            text = command("pdftotext", "-f", "1", "-l", "8", str(pdf), "-")
            if "Guide" not in text or "Laurent" not in text:
                errors.append("pdftotext:missing-title-or-author")
            result["machine_validation"]["text_sample_chars"] = len(text)
        except Exception as exc:
            errors.append(f"pdftotext:{type(exc).__name__}")

        try:
            command("qpdf", "--check", str(pdf))
            with tempfile.TemporaryDirectory() as temp_dir:
                qdf = Path(temp_dir) / "accessible.qdf.pdf"
                command("qpdf", "--qdf", "--object-streams=disable", str(pdf), str(qdf), timeout=600)
                qdf_text = qdf.read_bytes().decode("latin-1", errors="ignore")
            structural_checks = {
                "struct_tree_root": "/StructTreeRoot" in qdf_text,
                "mark_info": "/MarkInfo" in qdf_text,
                "marked_true": re.search(r"/Marked\s+true", qdf_text) is not None,
                "document_language": re.search(r"/Lang\s*(?:\(fr-FR\)|<FEFF00660072002D00460052>)", qdf_text) is not None,
                "display_document_title": re.search(r"/DisplayDocTitle\s+true", qdf_text) is not None,
                "pdfua_identifier": "pdfuaid:part" in qdf_text or "pdfuaid" in qdf_text,
            }
            result["machine_validation"]["pdf_structure"] = structural_checks
            for key, passed in structural_checks.items():
                if not passed:
                    errors.append(f"structure:{key}")
        except Exception as exc:
            errors.append(f"qpdf:{type(exc).__name__}")

        try:
            verapdf_payload, verapdf_raw, verapdf_errors = run_verapdf(args.verapdf_image, pdf)
            errors.extend(verapdf_errors)
            raw_path = args.report.parent / "verapdf-ua2-report.json"
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(verapdf_raw + ("\n" if verapdf_raw else ""), encoding="utf-8")
            result["machine_validation"]["verapdf"] = {
                "image": args.verapdf_image,
                "report": raw_path.name,
                "parsed": verapdf_payload is not None,
                "compliant": not verapdf_errors,
            }
        except Exception as exc:
            errors.append(f"verapdf:{type(exc).__name__}")

    if args.manifest.is_file() and pdf.is_file():
        try:
            manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
            if manifest.get("standard_candidate") != "PDF/UA-2":
                errors.append("manifest:standard-candidate")
            if manifest.get("language") != "fr-FR":
                errors.append("manifest:language")
            if manifest.get("output", {}).get("sha256") != sha256(pdf):
                errors.append("manifest:sha256")
            if manifest.get("source_count") != source_result["source_count"]:
                errors.append("manifest:source-count")
        except Exception as exc:
            errors.append(f"manifest:{type(exc).__name__}")

    result["errors"] = sorted(set(errors))
    result["status"] = "success" if not result["errors"] else "failure"
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "success" else 1


if __name__ == "__main__":
    sys.exit(main())
