from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MAPPING = [
    (
        "Livre-I/CHAPITRE-06-Audio-IA-local-voix-transcription-musique-et-effets.md",
        "Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md",
        6,
        9,
    ),
    (
        "Livre-I/CHAPITRE-05-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md",
        "Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md",
        5,
        8,
    ),
    (
        "Livre-I/CHAPITRE-04-ComfyUI-et-workflows-graphiques.md",
        "Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md",
        4,
        7,
    ),
    (
        "Livre-I/CHAPITRE-03-Open-WebUI-Open-Terminal-et-Vane.md",
        "Livre-I/CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md",
        3,
        6,
    ),
    (
        "Livre-I/CHAPITRE-02-Docker-et-Docker-Compose.md",
        "Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md",
        2,
        5,
    ),
]


def update_front_matter(path: Path, old_number: int, new_number: int) -> None:
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        f'title: "Livre I — Chapitre {old_number} :',
        f'title: "Livre I — Chapitre {new_number} :',
        1,
    )
    text = re.sub(
        rf"(?m)^chapter:\s*{old_number}\s*$",
        f"chapter: {new_number}\nlegacy-chapter: {old_number}\ncanonical-order: {new_number}",
        text,
        count=1,
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_links(old_rel: str, new_rel: str) -> None:
    old_name = Path(old_rel).name
    new_name = Path(new_rel).name
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or path.suffix.lower() not in {".md", ".txt", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        changed = text.replace(old_rel, new_rel).replace(old_name, new_name)
        if changed != text:
            path.write_text(changed, encoding="utf-8", newline="\n")


def main() -> None:
    for old_rel, new_rel, old_number, new_number in MAPPING:
        old_path = ROOT / old_rel
        new_path = ROOT / new_rel
        if new_path.exists() and not old_path.exists():
            update_front_matter(new_path, old_number, new_number)
            replace_links(old_rel, new_rel)
            continue
        if not old_path.exists():
            raise FileNotFoundError(f"Fichier source absent : {old_rel}")
        if new_path.exists():
            raise FileExistsError(f"Destination déjà présente : {new_rel}")
        old_path.rename(new_path)
        update_front_matter(new_path, old_number, new_number)
        replace_links(old_rel, new_rel)


if __name__ == "__main__":
    main()
