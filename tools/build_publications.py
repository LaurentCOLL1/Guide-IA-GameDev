#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

FORMATS = ("pdf", "html", "epub")
OUTPUT_NAMES = {
    "pdf": "Guide-IA-GameDev.pdf",
    "html": "Guide-IA-GameDev.html",
    "epub": "Guide-IA-GameDev.epub",
}


def run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, check=True, env=env)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_sources(root: Path, contents_file: Path) -> list[Path]:
    sources: list[Path] = []
    for raw in contents_file.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        source = root / value
        if not source.is_file():
            raise FileNotFoundError(f"Source absente : {value}")
        sources.append(source)
    if not sources:
        raise RuntimeError("Aucune source de publication déclarée")
    return sources


def main() -> int:
    parser = argparse.ArgumentParser(description="Build PDF, HTML and EPUB publications from contents.txt")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dist", type=Path)
    parser.add_argument("--formats", nargs="+", choices=FORMATS, default=list(FORMATS))
    args = parser.parse_args()

    root = args.root.resolve()
    dist = (args.dist or root / "dist" / "publication").resolve()
    contents_file = root / "contents.txt"
    metadata_files = [root / "metadata.yaml", root / "publication" / "metadata.yaml"]
    filter_file = root / "filters" / "pdf-normalize.lua"
    css_file = root / "publication" / "style.css"

    if shutil.which("pandoc") is None:
        raise RuntimeError("Pandoc est introuvable")
    for required in [contents_file, filter_file, css_file, *metadata_files]:
        if not required.is_file():
            raise FileNotFoundError(f"Fichier de construction absent : {required.relative_to(root)}")

    sources = read_sources(root, contents_file)
    dist.mkdir(parents=True, exist_ok=True)

    common = [
        "pandoc",
        f"--metadata-file={metadata_files[0]}",
        f"--metadata-file={metadata_files[1]}",
        "--from=markdown+yaml_metadata_block",
        f"--lua-filter={filter_file}",
        "--toc",
        "--number-sections",
        f"--resource-path={root}",
    ]
    source_args = [str(path) for path in sources]
    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", "1785440400")
    outputs: dict[str, dict[str, object]] = {}

    for fmt in args.formats:
        output = dist / OUTPUT_NAMES[fmt]
        if fmt == "pdf":
            command = common + ["--pdf-engine=xelatex", f"--output={output}"] + source_args
        elif fmt == "html":
            command = common + [
                "--to=html5",
                "--standalone",
                "--embed-resources",
                "--mathml",
                f"--css={css_file}",
                f"--output={output}",
            ] + source_args
        else:
            command = common + [
                "--to=epub3",
                "--epub-chapter-level=1",
                f"--css={css_file}",
                f"--output={output}",
            ] + source_args
        run(command, env=env)
        outputs[fmt] = {
            "file": output.name,
            "bytes": output.stat().st_size,
            "sha256": sha256(output),
        }

    source_manifest = [
        {
            "path": str(path.relative_to(root)).replace("\\", "/"),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sources
    ]
    manifest = {
        "schema_version": 1,
        "status": "technical-artifacts-not-release",
        "source_count": len(sources),
        "source_date_epoch": env["SOURCE_DATE_EPOCH"],
        "formats": outputs,
        "sources": source_manifest,
    }
    (dist / "publication-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    checksums = "".join(f"{entry['sha256']}  {entry['file']}\n" for entry in outputs.values())
    (dist / "SHA256SUMS").write_text(checksums, encoding="utf-8")
    print(json.dumps({"source_count": len(sources), "formats": outputs}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"publication-build-error: {exc}", file=sys.stderr)
        raise SystemExit(1)
