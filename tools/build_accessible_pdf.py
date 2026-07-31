#!/usr/bin/env python3
"""Build a tagged technical PDF with the LaTeX tagging prototype."""
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
DIST = ROOT / "dist" / "accessible-pdf"
CONTENTS = ROOT / "contents.txt"
METADATA = ROOT / "metadata.yaml"
PDF_FILTER = ROOT / "filters" / "pdf-normalize.lua"
OUTPUT = DIST / "Guide-IA-GameDev-tagged.pdf"
TEMPLATE = DIST / "tagged-pandoc-template.tex"


def fail(message: str) -> None:
    raise SystemExit(f"Erreur : {message}")


def run(command: list[str], env: dict[str, str], *, capture: bool = False) -> str:
    print("+", " ".join(command), flush=True)
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
    )
    return result.stdout if capture else ""


def source_files() -> list[Path]:
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
        fail("aucune source déclarée")
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def make_template(env: dict[str, str]) -> None:
    default = run(["pandoc", "--print-default-template=latex"], env, capture=True)
    if "\\documentclass" not in default:
        fail("modèle LaTeX Pandoc sans documentclass")
    metadata = r"""\DocumentMetadata{
  lang=fr-FR,
  pdfversion=1.7,
  pdfstandard=ua-1,
  testphase=latest
}
"""
    TEMPLATE.write_text(metadata + default, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    for executable in ("pandoc", "lualatex"):
        if shutil.which(executable) is None:
            fail(f"{executable} est introuvable")
    for required in (CONTENTS, METADATA, PDF_FILTER):
        if not required.is_file():
            fail(f"fichier absent : {required}")

    if args.clean and DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", "1785452640")
    make_template(env)
    sources = source_files()

    command = [
        "pandoc",
        f"--metadata-file={METADATA}",
        "--from=markdown+yaml_metadata_block",
        f"--resource-path={ROOT}",
        "--toc",
        "--number-sections",
        f"--lua-filter={PDF_FILTER}",
        "--pdf-engine=lualatex",
        f"--template={TEMPLATE}",
        "--metadata=license:CC-BY-SA-4.0",
        "--metadata=title-meta:Guide réaliste de création de jeux vidéo 3D avec IA locale",
        "--metadata=author-meta:Laurent Collin",
        f"--output={OUTPUT}",
    ]
    command.extend(str(path) for path in sources)
    run(command, env)

    if not OUTPUT.is_file() or OUTPUT.stat().st_size < 100_000:
        fail("PDF balisé absent ou anormalement petit")

    manifest = {
        "schema_version": 1,
        "status": "technical-tagged-pdf-not-official-release",
        "standard_target": "PDF/UA-1",
        "claim": "tagged-pdf-machine-checked-not-full-pdfua-conformance",
        "engine": "lualatex",
        "source_count": len(sources),
        "file": OUTPUT.name,
        "bytes": OUTPUT.stat().st_size,
        "sha256": sha256(OUTPUT),
        "license": "CC-BY-SA-4.0",
    }
    (DIST / "accessible-pdf-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
