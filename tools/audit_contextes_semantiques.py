#!/usr/bin/env python3
"""Validate semantic consistency of usage-context markers."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER_RE = re.compile(
    r"^> \*\*\[(?P<code>PS|CMD|WSL|DCT|DCK|VSC|WEB|APP|SORTIE|LECTURE)\](?P<rest>.*)$"
)
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>[^`]*)$")
PATH_RE = re.compile(
    r"`([^`\n]*(?:[\\/]|\.(?:json|ya?ml|toml|ini|cfg|conf|env|md|txt|py|ps1|sh|bat|cmd|sql|gd|tscn|tres|godot|dockerfile|gitignore|gitattributes))[^`\n]*)`",
    re.IGNORECASE,
)
FILE_LANGS = {
    "json", "yaml", "yml", "toml", "ini", "cfg", "conf", "dockerfile", "dotenv", "env",
    "gitignore", "gitattributes", "python", "py", "gdscript", "sql", "markdown", "md", "xml",
    "csv", "javascript", "js", "typescript", "ts",
}


def files() -> list[Path]:
    result: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III"):
        result.extend(sorted(base.rglob("*.md")))
    result.append(ROOT / "STYLE_GUIDE.md")
    return [path for path in result if path.is_file()]


def previous_nonempty(lines: list[str], index: int) -> int | None:
    index -= 1
    while index >= 0:
        if lines[index].strip():
            return index
        index -= 1
    return None


def context(lines: list[str], marker_index: int, count: int = 8) -> str:
    values = [lines[marker_index].strip()]
    index = marker_index - 1
    while index >= 0 and len(values) < count + 1:
        value = lines[index].strip()
        if value:
            if len(values) > 1 and value.startswith(("#", "```", "~~~")):
                break
            values.append(value)
        index -= 1
    return " ".join(reversed(values)).lower()


def allowed_markers(lang: str, marker_line: str, semantic_context: str) -> set[str] | None:
    lang = lang.lower()
    paths = PATH_RE.findall(marker_line)
    target = paths[-1].lower() if paths else ""

    if lang in {"powershell", "pwsh"}:
        if target.endswith((".ps1", ".psm1", ".psd1")):
            return {"PS", "VSC"}
        return {"PS"}

    if lang in {"cmd", "bat", "batch"}:
        if target.endswith((".bat", ".cmd")):
            return {"CMD", "VSC"}
        return {"CMD"}

    if lang in {"bash", "sh", "shell", "zsh"}:
        if target.endswith(".sh"):
            return {"VSC", "WSL", "DCT"}
        if any(word in semantic_context for word in (
            "terminal du conteneur", "dans le conteneur", "shell du conteneur", "docker exec",
        )):
            return {"DCT"}
        return {"WSL"}

    if lang in FILE_LANGS:
        return {"VSC", "LECTURE", "SORTIE"}

    if lang in {"text", "", "plaintext", "console", "output"}:
        return {"APP", "DCK", "VSC", "SORTIE", "LECTURE"}

    if lang == "mermaid":
        return {"VSC", "LECTURE"}

    return None


def process(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    inside = False
    fence_char = ""
    fence_len = 0

    for index, line in enumerate(lines):
        match = FENCE_RE.match(line.strip())
        if not match:
            continue
        fence = match.group("fence")
        lang = match.group("lang").strip().split()[0].lower() if match.group("lang").strip() else ""
        if inside:
            if fence[0] == fence_char and len(fence) >= fence_len and not lang:
                inside = False
            continue

        inside = True
        fence_char = fence[0]
        fence_len = len(fence)
        marker_index = previous_nonempty(lines, index)
        if marker_index is None:
            continue
        marker_match = MARKER_RE.match(lines[marker_index].strip())
        if not marker_match:
            continue

        marker = marker_match.group("code")
        semantic_context = context(lines, marker_index)
        allowed = allowed_markers(lang, lines[marker_index].strip(), semantic_context)
        if allowed is not None and marker not in allowed:
            rendered = ", ".join(f"[{value}]" for value in sorted(allowed))
            errors.append(
                f"{path.relative_to(ROOT).as_posix()}:{index + 1}: "
                f"bloc `{lang or 'text'}` marqué [{marker}], attendu parmi {rendered}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", required=True)
    _args = parser.parse_args()

    all_errors: list[str] = []
    controlled = files()
    for path in controlled:
        all_errors.extend(process(path))

    print(f"Fichiers contrôlés : {len(controlled)}")
    print(f"Incohérences sémantiques détectées : {len(all_errors)}")
    for error in all_errors:
        print(f"- {error}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
