from pathlib import Path
import re

VALIDATED_HEAD = '9054fc3fea652d4d7200450253c05b6d88f6ad2e'
CHAPTERS_RUN = 29710815665
CONTEXTS_RUN = 29710815628
ARTIFACT_ID = 8448923780
ARTIFACT_DIGEST = 'sha256:ac9b609aec007ac37e1946765111574c1ab33813dcfa7de9a152062ce651951d'

for chapter in (15, 16):
    path = Path(f'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-{chapter}.yaml')
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(?m)^status: pending-ci$', 'status: complete', text, count=1)
    text = re.sub(r'(?m)^validated-head-commit: pending-ci$', f'validated-head-commit: {VALIDATED_HEAD}', text, count=1)
    text = re.sub(
        r'(?m)^  ci-status: pending$',
        '  ci-status: success\n'
        f'  validated-head-commit: {VALIDATED_HEAD}\n'
        f'  validate-chapters-without-pdf-run-id: {CHAPTERS_RUN}\n'
        f'  validate-usage-contexts-run-id: {CONTEXTS_RUN}\n'
        f'  artifact-id: {ARTIFACT_ID}\n'
        f'  artifact-digest: {ARTIFACT_DIGEST}',
        text,
        count=1,
    )
    if 'status: pending-ci' in text or 'validated-head-commit: pending-ci' in text or '  ci-status: pending' in text:
        raise RuntimeError(f'chapter {chapter}: pending evidence remains')
    path.write_text(text, encoding='utf-8')
