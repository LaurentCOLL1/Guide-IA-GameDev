#!/usr/bin/env python3
"""Build the reader collection as PDF, standalone HTML and EPUB 3."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "publications"
CONTENTS = ROOT / "contents.txt"
METADATA = ROOT / "metadata.yaml"
PDF_FILTER = ROOT / "filters" / "pdf-normalize.lua"
BASENAME = "Guide-IA-GameDev"
FORMATS = ("pdf", "html", "epub")


def fail(message: str) -> None:
    raise SystemExit(f"Erreur : {message}")


def sources() -> list[Path]:
    if not CONTENTS.is_file():
        fail(f"fichier absent : {CONTENTS}")
    result: list[Path] = []
    for raw in CONTENTS.read_text(encoding="utf-8").splitlines():
        item = raw.strip()
        if not item or item.startswith("#"):
            continue
        path = ROOT / item
        if not path.is_file():
            fail(f"source absente : {item}")
        result.append(path)
    if not result:
        fail("contents.txt ne contient aucune source")
    return result


def run(command: list[str], env: dict[str, str]) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build(fmt: str, source_files: list[Path], env: dict[str, str]) -> Path:
    extension = "epub" if fmt == "epub" else fmt
    output = DIST / f"{BASENAME}.{extension}"
    common = [
        "pandoc",
        f"--metadata-file={METADATA}",
        "--from=markdown+yaml_metadata_block",
        f"--resource-path={ROOT}",
        "--toc",
        "--number-sections",
    ]
    if fmt == "pdf":
        command = common + [
            f"--lua-filter={PDF_FILTER}",
            "--pdf-engine=xelatex",
            "--metadata=license:CC-BY-SA-4.0",
            f"--output={output}",
        ]
    elif fmt == "html":
        command = common + [
            "--standalone",
            "--embed-resources",
            "--section-divs",
            "--metadata=license:CC-BY-SA-4.0",
            f"--output={output}",
        ]
    elif fmt == "epub":
        command = common + [
            "--to=epub3",
            "--epub-chapter-level=1",
            "--metadata=rights:CC BY-SA 4.0 - Laurent Collin",
            "--metadata=license:CC-BY-SA-4.0",
            f"--output={output}",
        ]
    else:
        fail(f"format inconnu : {fmt}")
    command.extend(str(path) for path in source_files)
    run(command, env)
    if not output.is_file() or output.stat().st_size == 0:
        fail(f"sortie vide ou absente : {output}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--formats", nargs="+", choices=FORMATS, default=list(FORMATS))
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    if shutil.which("pandoc") is None:
        fail("Pandoc est introuvable")
    if not METADATA.is_file() or not PDF_FILTER.is_file():
        fail("metadata.yaml ou filtre PDF absent")
    if "pdf" in args.formats and shutil.which("xelatex") is None:
        fail("XeLaTeX est introuvable")

    if args.clean and DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", "1785452640")
    source_files = sources()
    outputs = [build(fmt, source_files, env) for fmt in args.formats]

    manifest = {
        "schema_version": 1,
        "collection": BASENAME,
        "publication_status": "technical-build-not-official-release",
        "license": "CC-BY-SA-4.0",
        "source_count": len(source_files),
        "source_order": str(CONTENTS.relative_to(ROOT)),
        "outputs": {
            path.suffix.lstrip("."): {
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in outputs
        },
    }
    manifest_path = DIST / "publication-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
