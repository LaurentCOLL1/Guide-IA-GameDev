from pathlib import Path
import re

HEAD = "22446295f0e0c839a9732923dcd902a85a39d149"
BASE = "b603dcee25bdef01b9d6e47f4eddf441672a905c"
RUN_CHAPTERS = "29707351671"
RUN_CONTEXTS = "29707351667"
ARTIFACT_ID = "8448308094"
DIGEST = "sha256:97eeb31fd5a7db8a0f11a7212d7ca128a54239bbfd8c18bd8eaa683b1d3c6a27"

CONFIG = {
    15: {
        "path": Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml"),
        "lines": 2883,
        "headings": 69,
        "significant": 29,
        "code_data": 66,
        "gdscript": 55,
        "explanations": 56,
        "refined": 44,
        "missing": 12,
    },
    16: {
        "path": Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-16.yaml"),
        "lines": 3141,
        "headings": 89,
        "significant": 36,
        "code_data": 69,
        "gdscript": 66,
        "explanations": 67,
        "refined": 43,
        "missing": 24,
    },
}

for chapter, cfg in CONFIG.items():
    path = cfg["path"]
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^status: pending-ci$", "status: complete", text, count=1)
    text = re.sub(r"(?m)^validation-date: .+$", "validation-date: 2026-07-20", text, count=1)
    text = re.sub(r"(?m)^validated-head-commit: .+$", f"validated-head-commit: {HEAD}", text, count=1)
    if "validated-head-commit:" not in text:
        text = re.sub(
            r"(?m)^(validated-base-commit: .+)$",
            rf"\1\nenrichment-base-commit: {BASE}\nvalidated-head-commit: {HEAD}",
            text,
            count=1,
        )
    elif "enrichment-base-commit:" not in text:
        text = re.sub(
            r"(?m)^(validated-base-commit: .+)$",
            rf"\1\nenrichment-base-commit: {BASE}",
            text,
            count=1,
        )
    replacements = {
        "sources": 75,
        "unique-identifiers": 71,
        "livre-ii-chapters": 16,
        "chapter-lines": cfg["lines"],
        "chapter-headings": cfg["headings"],
        "chapter-significant-code-blocks": cfg["significant"],
        "chapter-code-and-data-blocks": cfg["code_data"],
        "total-context-blocks": 1642,
        "marked-context-blocks": 1642,
        "gdscript-code-blocks": cfg["gdscript"],
    }
    for key, value in replacements.items():
        text = re.sub(rf"(?m)^  {re.escape(key)}: .+$", f"  {key}: {value}", text, count=1)
    text = re.sub(r"(?m)^    run-id: \d+$", f"    run-id: {RUN_CHAPTERS}", text, count=1)
    first_position = text.find(f"    run-id: {RUN_CHAPTERS}")
    second_match = re.search(r"(?m)^    run-id: \d+$", text[first_position + 1:])
    if second_match:
        start = first_position + 1 + second_match.start()
        end = first_position + 1 + second_match.end()
        text = text[:start] + f"    run-id: {RUN_CONTEXTS}" + text[end:]
    text = re.sub(r"(?m)^    id: \d+$", f"    id: {ARTIFACT_ID}", text, count=1)
    text = re.sub(r"(?m)^    digest: .+$", f"    digest: {DIGEST}", text, count=1)
    text = re.sub(r"(?m)^  significant-code-or-data-blocks: \d+$", f"  significant-code-or-data-blocks: {cfg['explanations']}", text, count=1)
    text = re.sub(r"(?m)^  explanations-added: \d+$", f"  explanations-added: {cfg['explanations']}", text, count=1)
    text = re.sub(r"(?m)^  explanations-refined-after-second-review: \d+$", f"  explanations-refined-after-second-review: {cfg['refined']}", text, count=1)
    text = re.sub(r"(?m)^  previously-missing-explanations-added: \d+$", f"  previously-missing-explanations-added: {cfg['missing']}", text, count=1)
    text = re.sub(r"(?m)^  ci-status: pending$", "  ci-status: success", text, count=1)
    correction = "  - Enrichissement pédagogique de tous les blocs GDScript et données significatifs selon QA Q1.1.\n"
    if correction.strip() not in text:
        text = text.replace("ci:\n", correction + "ci:\n", 1)
    path.write_text(text, encoding="utf-8")
