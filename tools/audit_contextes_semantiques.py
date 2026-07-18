#!/usr/bin/env python3
"""Validate and correct semantic consistency of usage-context markers."""

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
    "json", "yaml", "yml", "toml", "ini", "cfg", "conf", "dockerfile",
    "dotenv",
    "env",
    "gitignore", "gitattributes", "python", "py", "gdscript", "sql",
    "markdown", "md", "xml", "csv", "javascript", "js", "typescript", "ts",
}


def files() -> list[Path]:
    result: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I"):
        result.extend(sorted(base.rglob("*.md")))
    result.append(ROOT / "STYLE_GUIDE.md")
    return [p for p in result if p.is_file()]


def previous_nonempty(lines: list[str], index: int) -> int | None:
    i = index - 1
    while i >= 0:
        if lines[i].strip():
            return i
        i -= 1
    return None


def context(lines: list[str], index: int, count: int = 8) -> str:
    values: list[str] = []
    i = index - 1
    while i >= 0 and len(values) < count:
        value = lines[i].strip()
        if not value:
            i -= 1
            continue
        if values and (value.startswith("#") or value.startswith("```") or value.startswith("~~~")):
            break
        values.append(value)
        i -= 1
    return " ".join(reversed(values)).lower()


def expected_marker(lang: str, marker: str, marker_line: str, ctx: str) -> tuple[str, str] | None:
    lang = lang.lower()
    path_values = PATH_RE.findall(marker_line)
    target = path_values[-1] if path_values else ""
    target_lower = target.lower()

    if lang in {"powershell", "pwsh"}:
        is_script_file = marker == "VSC" and target_lower.endswith((".ps1", ".psm1", ".psd1"))
        if is_script_file:
            return None
        if "fermer et rouvrir powershell" in ctx or "après réouverture" in ctx:
            return (
                "PS",
                "> **[PS] PowerShell 7 - Vérifier après réouverture :** fermer PowerShell, ouvrir une nouvelle fenêtre, puis exécuter les commandes.",
            )
        return (
            "PS",
            "> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.",
        )

    if lang in {"cmd", "bat", "batch"}:
        if marker == "VSC" and target_lower.endswith((".bat", ".cmd")):
            return None
        return (
            "CMD",
            "> **[CMD] Invite de commandes Windows - Exécuter :** utiliser `cmd.exe`.",
        )

    if lang in {"bash", "sh", "shell", "zsh"}:
        if marker == "VSC" and target_lower.endswith(".sh"):
            return None
        if any(word in ctx for word in ("dans le conteneur", "terminal du conteneur", "docker exec", "shell du conteneur")):
            return (
                "DCT",
                "> **[DCT] Terminal du conteneur - Exécuter :** utiliser le shell du conteneur concerné.",
            )
        return (
            "WSL",
            "> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée.",
        )

    if lang in FILE_LANGS:
        context_paths = PATH_RE.findall(ctx)
        context_target = context_paths[-1] if context_paths else ""
        file_action = any(word in ctx for word in (
            "créer", "creer", "modifier", "contenu du fichier",
            "enregistrer dans", "copier le fichier", "fichier :",
        ))
        if marker == "LECTURE" and file_action:
            chosen = context_target or target or "fichier indiqué dans l’étape"
            return (
                "VSC",
                f"> **[VSC] Visual Studio Code - Créer ou modifier :** `{chosen}`.",
            )
        if marker in {"VSC", "LECTURE", "SORTIE"}:
            if lang == "json" and target_lower == ".vscode/settings.json":
                return (
                    "VSC",
                    "> **[VSC] Visual Studio Code - Créer :** `.vscode/settings.json` à la racine du projet. Ouvrir le dossier du projet dans VS Code, créer le dossier `.vscode` s’il n’existe pas, puis créer `settings.json`.",
                )
            return None
        if target:
            return (
                "VSC",
                f"> **[VSC] Visual Studio Code - Créer ou modifier :** `{target}`.",
            )
        return (
            "LECTURE",
            "> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.",
        )

    if lang in {"text", "", "plaintext", "console", "output"}:
        output_words = ("résultat attendu", "sortie attendue", "doit afficher", "exemple de sortie")
        if any(word in ctx for word in output_words):
            return (
                "SORTIE",
                "> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.",
            )
        return (
            "LECTURE",
            "> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**",
        )

    if lang == "mermaid":
        if marker in {"VSC", "LECTURE"}:
            return None
        return (
            "LECTURE",
            "> **[LECTURE] Diagramme de référence - Ne pas exécuter :** lire le flux représenté.",
        )

    return None


def process(path: Path, apply: bool) -> tuple[int, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    changes = 0
    errors: list[str] = []
    inside = False
    fence_char = ""
    fence_len = 0

    for i, line in enumerate(lines):
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

        marker_index = previous_nonempty(lines, i)
        if marker_index is None:
            continue
        marker_match = MARKER_RE.match(lines[marker_index].strip())
        if not marker_match:
            continue
        marker = marker_match.group("code")
        expectation = expected_marker(
            lang,
            marker,
            lines[marker_index].strip(),
            context(lines, marker_index),
        )
        if expectation is None:
            continue
        expected_code, replacement = expectation
        if marker == expected_code:
            continue
        message = (
            f"{path.relative_to(ROOT).as_posix()}:{i + 1}: "
            f"bloc `{lang or 'text'}` marqué [{marker}], attendu [{expected_code}]"
        )
        errors.append(message)
        if apply:
            lines[marker_index] = replacement
            changes += 1

    if apply and changes:
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return changes, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--apply", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()

    total_changes = 0
    all_errors: list[str] = []
    for path in files():
        changes, errors = process(path, apply=args.apply)
        total_changes += changes
        all_errors.extend(errors)

    print(f"Fichiers contrôlés : {len(files())}")
    print(f"Incohérences sémantiques détectées : {len(all_errors)}")
    if args.apply:
        print(f"Repères corrigés : {total_changes}")
    for error in all_errors:
        print(f"- {error}")

    return 0 if args.apply or not all_errors else 1


if __name__ == "__main__":
    sys.exit(main())
