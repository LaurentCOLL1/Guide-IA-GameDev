#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md"
PROOF = ROOT / "Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-16.yaml"
EXPECTED_PERMANENT = {
    "CONTINUITE-PROJET.md",
    "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md",
    "Livre-IV/QA/AUDIT-CHAPITRE-16.md",
    "Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-16.yaml",
    "Livre-IV/index.md",
    "ROADMAP.md",
    "contents.txt",
    "plans/LIVRE-IV-PLAN-MAITRE.md",
}


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"remplacement attendu une fois, obtenu {count}: {old!r}")
    return text.replace(old, new, 1)


def main() -> None:
    chapter = CHAPTER.read_text(encoding="utf-8")
    chapter = replace_once(
        chapter,
        "> **[LECTURE] Contrôler signature et bundle sur un Mac de qualification.**",
        "> **[WSL] Contrôler signature et bundle dans un terminal macOS de qualification.**",
    )
    chapter = replace_once(
        chapter,
        "> **[WEB] Exemple fautif — Ne pas appliquer.**\n\n```text\nfile:///C:/build/web/index.html",
        "> **[LECTURE] Exemple fautif — Ne pas appliquer.**\n\n```text\nfile:///C:/build/web/index.html",
    )
    chapter = replace_once(
        chapter,
        "> **[WEB] Exemple corrigé — Adapter au projet réel.**\n\n```text\nhttps://localhost.example.test/asteria/",
        "> **[LECTURE] Exemple corrigé — Adapter au projet réel.**\n\n```text\nhttps://localhost.example.test/asteria/",
    )
    CHAPTER.write_text(chapter, encoding="utf-8", newline="\n")

    proof = PROOF.read_text(encoding="utf-8")
    old_hash = "432ff27f555b35c474a91f3a5d2a951973eda34f36a86127735be85568c36ff8"
    new_hash = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
    proof = replace_once(proof, f"chapter-sha256: {old_hash}", f"chapter-sha256: {new_hash}")
    PROOF.write_text(proof, encoding="utf-8", newline="\n")

    for path in [
        ROOT / "tools/temporary/fix_l4_ch16_markers.py",
        ROOT / ".github/workflows/livre-iv-ch16-marker-fix.yml",
    ]:
        path.unlink(missing_ok=True)

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    changed = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "origin/main"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    if set(changed) != EXPECTED_PERMANENT:
        raise RuntimeError(f"diff permanent inattendu: {changed}")


if __name__ == "__main__":
    main()
