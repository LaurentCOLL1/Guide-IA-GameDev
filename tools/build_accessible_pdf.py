#!/usr/bin/env python3
"""Build a separate tagged PDF/UA-2 candidate through a pinned Pandoc image."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
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
BUILD_LOG = DIST / "accessible-build.log"
DEFAULT_IMAGE = "pandoc/latex:3.10.0.0-ubuntu@sha256:568ae5d3dc4cf9266753c9c78e7d073c1472f6540e0cf02de6a330143df8bdb7"
CONTAINER_ROOT = Path("/data")
CONTAINER_TEXMF = Path("/texmf-cache")
DIAGNOSTIC_PATTERN = re.compile(
    r"(^!|LaTeX Error|Package .* Error|Fatal error|Emergency stop|"
    r"Undefined control sequence|not set up for use|Error producing PDF|"
    r"^l\.\d+|^\./[^:]+:\d+:)",
    re.IGNORECASE,
)


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
        text=True,
        capture_output=True,
    )
    if completed.stdout:
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n", flush=True)
    if completed.stderr:
        print(completed.stderr, end="" if completed.stderr.endswith("\n") else "\n", file=sys.stderr, flush=True)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(
            completed.returncode,
            command,
            output=completed.stdout,
            stderr=completed.stderr,
        )
    return completed.stdout.strip() if capture else ""


def print_build_diagnostics(log_path: Path) -> None:
    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    matches: list[str] = []
    for index, line in enumerate(lines):
        if DIAGNOSTIC_PATTERN.search(line):
            start = max(0, index - 2)
            end = min(len(lines), index + 5)
            matches.extend(lines[start:end])
            matches.append("---")
    print("\n=== Diagnostic LuaLaTeX borné ===", file=sys.stderr)
    if matches:
        for line in matches[-160:]:
            print(line, file=sys.stderr)
    else:
        print("Aucun motif fatal standard détecté ; fin du journal :", file=sys.stderr)
        for line in lines[-120:]:
            print(line, file=sys.stderr)
    print(f"Journal complet : {log_path.relative_to(ROOT)}", file=sys.stderr)


def run_build(command: list[str], source_count: int) -> None:
    visible = command[: command.index("--output=" + container_path(OUTPUT)) + 1]
    print("+", " ".join(visible), f"… [{source_count} sources]", flush=True)
    BUILD_LOG.parent.mkdir(parents=True, exist_ok=True)
    with BUILD_LOG.open("w", encoding="utf-8") as stream:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=stream,
            stderr=subprocess.STDOUT,
        )
    if completed.returncode != 0:
        print_build_diagnostics(BUILD_LOG)
        raise subprocess.CalledProcessError(completed.returncode, command)
    tail = BUILD_LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-20:]
    print("\n=== Fin du journal de construction ===")
    for line in tail:
        print(line)
    print(f"Journal complet : {BUILD_LOG.relative_to(ROOT)}")


def image_digest(image: str) -> str:
    inspected = run(
        ["docker", "image", "inspect", "--format", "{{join .RepoDigests \"\\n\"}}", image],
        capture=True,
    )
    return next((line for line in inspected.splitlines() if "@sha256:" in line), image)


def container_path(path: Path) -> str:
    return str(CONTAINER_ROOT / path.relative_to(ROOT))


def texmf_cache_root() -> Path:
    parent = Path(os.environ.get("RUNNER_TEMP", str(DIST))).resolve()
    return parent / "guide-ia-gamedev-texmf"


def prepare_texmf_cache() -> Path:
    cache_root = texmf_cache_root()
    shutil.rmtree(cache_root, ignore_errors=True)
    for child in ("var", "config", "cache"):
        (cache_root / child).mkdir(parents=True, exist_ok=True)
    return cache_root


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
        for path in (OUTPUT, MANIFEST, BUILD_LOG):
            path.unlink(missing_ok=True)

    if args.pull:
        run(["docker", "pull", args.image])

    cache_root = prepare_texmf_cache()
    command = [
        "docker",
        "run",
        "--rm",
        "--network=none",
        "--security-opt",
        "no-new-privileges",
        "--volume",
        f"{ROOT}:{CONTAINER_ROOT}",
        "--volume",
        f"{cache_root}:{CONTAINER_TEXMF}",
        "--workdir",
        str(CONTAINER_ROOT),
        "--env",
        f"SOURCE_DATE_EPOCH={os.environ.get('SOURCE_DATE_EPOCH', '1785452640')}",
        "--env",
        "HOME=/tmp",
        "--env",
        f"TEXMFVAR={CONTAINER_TEXMF / 'var'}",
        "--env",
        f"TEXMFCONFIG={CONTAINER_TEXMF / 'config'}",
        "--env",
        f"TEXMFCACHE={CONTAINER_TEXMF / 'cache'}",
    ]

    if os.name != "nt" and hasattr(os, "getuid") and hasattr(os, "getgid"):
        command.extend(["--user", f"{os.getuid()}:{os.getgid()}"])
    host_fonts = Path("/usr/share/fonts")
    if host_fonts.is_dir():
        command.extend(["--volume", f"{host_fonts}:/usr/share/fonts:ro"])

    command.extend(
        [
            args.image,
            "--verbose",
            f"--metadata-file={container_path(METADATA)}",
            "--from=markdown+yaml_metadata_block",
            f"--resource-path={CONTAINER_ROOT}",
            "--toc",
            "--number-sections",
            f"--lua-filter={container_path(PDF_FILTER)}",
            "--pdf-engine=lualatex",
            "--pdf-engine-opt=-file-line-error",
            "--pdf-engine-opt=-interaction=nonstopmode",
            "--pdf-engine-opt=-halt-on-error",
            "--variable=pdfstandard:ua-2",
            "--metadata=license:CC-BY-SA-4.0",
            f"--output={container_path(OUTPUT)}",
        ]
    )
    command.extend(container_path(path) for path in sources)

    try:
        run_build(command, len(sources))
    finally:
        shutil.rmtree(cache_root, ignore_errors=True)

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
