#!/usr/bin/env python3
"""Build a separate tagged PDF/UA-2 candidate through a pinned Pandoc image."""
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
METADATA = ROOT / "metadata-accessible-pdf.yaml"
PDF_FILTER = ROOT / "filters" / "pdf-normalize.lua"
OUTPUT = DIST / "Guide-IA-GameDev-accessible.pdf"
MANIFEST = DIST / "accessible-pdf-manifest.json"
DEFAULT_IMAGE = "pandoc/latex:3.10.0.0-ubuntu"
CONTAINER_ROOT = Path("/data")


def fail(message: str) -> None:
    raise SystemExit(f"Erreur : {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_files() -> list[Path]:
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


def run(command: list[str], *, capture: bool = False) -> str:
    print("+", " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=capture,
    )
    return completed.stdout.strip() if capture else ""


def image_digest(image: str) -> str:
    inspected = run(
        ["docker", "image", "inspect", "--format", "{{join .RepoDigests \"\\n\"}}", image],
        capture=True,
    )
    return next((line for line in inspected.splitlines() if "@sha256:" in line), image)


def container_path(path: Path) -> str:
    return str(CONTAINER_ROOT / path.relative_to(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", default=os.environ.get("PANDOC_LATEX_IMAGE", DEFAULT_IMAGE))
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--pull", action="store_true", help="Télécharger explicitement l'image avant le build")
    args = parser.parse_args()

    if shutil.which("docker") is None:
        fail("Docker est introuvable")
    for path in (METADATA, PDF_FILTER):
        if not path.is_file():
            fail(f"fichier absent : {path.relative_to(ROOT)}")

    sources = source_files()
    DIST.mkdir(parents=True, exist_ok=True)
    if args.clean:
        for path in (OUTPUT, MANIFEST):
            path.unlink(missing_ok=True)

    if args.pull:
        run(["docker", "pull", args.image])

    command = [
        "docker",
        "run",
        "--rm",
        "--network=none",
        "--security-opt",
        "no-new-privileges",
        "--volume",
        f"{ROOT}:{CONTAINER_ROOT}",
        "--workdir",
        str(CONTAINER_ROOT),
        "--env",
        f"SOURCE_DATE_EPOCH={os.environ.get('SOURCE_DATE_EPOCH', '1785452640')}",
        "--env",
        "HOME=/tmp",
        "--env",
        "TEXMFVAR=/tmp/texmf-var",
        "--env",
        "TEXMFCONFIG=/tmp/texmf-config",
        "--env",
        "TEXMFCACHE=/tmp/texmf-cache",
    ]

    if os.name != "nt" and hasattr(os, "getuid") and hasattr(os, "getgid"):
        command.extend(["--user", f"{os.getuid()}:{os.getgid()}"])
    host_fonts = Path("/usr/share/fonts")
    if host_fonts.is_dir():
        command.extend(["--volume", f"{host_fonts}:/usr/share/fonts:ro"])

    command.extend(
        [
            args.image,
            f"--metadata-file={container_path(METADATA)}",
            "--from=markdown+yaml_metadata_block",
            f"--resource-path={CONTAINER_ROOT}",
            "--toc",
            "--number-sections",
            f"--lua-filter={container_path(PDF_FILTER)}",
            "--pdf-engine=lualatex",
            "--variable=pdfstandard:ua-2",
            "--metadata=license:CC-BY-SA-4.0",
            f"--output={container_path(OUTPUT)}",
        ]
    )
    command.extend(container_path(path) for path in sources)
    run(command)

    if not OUTPUT.is_file() or OUTPUT.stat().st_size < 1000:
        fail(f"sortie vide ou absente : {OUTPUT}")

    manifest = {
        "schema_version": 1,
        "collection": "Guide-IA-GameDev",
        "publication_status": "technical-accessibility-candidate-not-official-release",
        "standard_candidate": "PDF/UA-2",
        "validation_scope": "build-only-machine-validation-pending",
        "license": "CC-BY-SA-4.0",
        "language": "fr-FR",
        "source_count": len(sources),
        "source_order": str(CONTENTS.relative_to(ROOT)),
        "toolchain": {
            "pandoc_latex_image": args.image,
            "pandoc_latex_image_digest": image_digest(args.image),
        },
        "output": {
            "file": OUTPUT.name,
            "bytes": OUTPUT.stat().st_size,
            "sha256": sha256(OUTPUT),
        },
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
