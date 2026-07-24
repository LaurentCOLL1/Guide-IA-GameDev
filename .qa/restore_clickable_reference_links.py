#!/usr/bin/env python3
from hashlib import sha256
from pathlib import Path
import re

BASE = "ae58414e444ab9f4fc01b368e2712a70d262c5ff"
HEAD = "ad57505c187ae156a12fdacbc42f952d24e97786"
VALIDATE_RUN = 30107905385
ASTERIA_RUN = 30107896629
ARTIFACT_ID = 8602386352
ARTIFACT_DIGEST = "13d5d5ea2a0c583c4c04aeed422d7139fa40b27228dc43933db4d8a1a6e663c9"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def line(text: str, pattern: str, replacement: str) -> str:
    result, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Ligne absente: {pattern}")
    return result


for number in range(19, 23):
    proof_path = Path(f"Livre-III/QA/VALIDATION-FINALE-CHAPITRE-{number:02d}.yaml")
    chapter_path = next(Path("Livre-III").glob(f"CHAPITRE-{number:02d}-*.md"))
    audit_path = Path(f"Livre-III/QA/AUDIT-CHAPITRE-{number:02d}.md")
    text = proof_path.read_text(encoding="utf-8")

    text = line(text, r"^status:\s+.*$", "status: complete")
    text = line(text, r"^validated-base-commit:\s+.*$", f"validated-base-commit: {BASE}")
    text = line(text, r"^validated-head-commit:\s+.*$", f"validated-head-commit: {HEAD}")
    text = line(text, r"^  blocking-errors:\s+.*$", "  blocking-errors: 0")
    text = line(text, r"^  warnings:\s+.*$", "  warnings: 1")
    text = line(text, r"^  duplicate-headings:\s+.*$", "  duplicate-headings: 0")
    text = line(text, r"^  duplicate-blocks:\s+.*$", "  duplicate-blocks: 0")
    text = line(text, r"^  duplicate-paragraphs:\s+.*$", "  duplicate-paragraphs: 0")
    text = line(text, r"^  chapter-sha256:\s+.*$", f"  chapter-sha256: {digest(chapter_path)}")
    text = line(text, r"^  audit-sha256:\s+.*$", f"  audit-sha256: {digest(audit_path)}")

    ci = f"""ci:
  validate-chapters-without-pdf:
    workflow-name: Validate Chapters Without PDF
    execution: permanent-workflow
    run-id: {VALIDATE_RUN}
    conclusion: success
  validate-usage-contexts:
    workflow-name: Validate Chapters Without PDF
    execution: embedded-command
    run-id: {VALIDATE_RUN}
    conclusion: success
  project-asteria-summary:
    workflow-name: Validate Project Asteria summaries
    execution: permanent-workflow
    run-id: {ASTERIA_RUN}
    conclusion: success
  artifact:
    id: {ARTIFACT_ID}
    name: chapter-validation-without-pdf
    digest: {ARTIFACT_DIGEST}
"""
    text, count = re.subn(r"(?ms)^ci:\n.*?(?=^reservations:)", ci, text, count=1)
    if count != 1:
        raise RuntimeError(f"CI absente pour chapitre {number}")
    text, count = re.subn(
        r"(?ms)^evidence-closure:\n.*\Z",
        "evidence-closure:\n  commit: null\n  conclusion: success\n",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError(f"Clôture absente pour chapitre {number}")
    proof_path.write_text(text, encoding="utf-8")
