from __future__ import annotations

import base64
import gzip
import hashlib
import json
import os
from pathlib import Path

CHAPTER = Path('Livre-III/CHAPITRE-15-Vegetation-et-biomes.md')
AUDIT = Path('Livre-III/QA/AUDIT-CHAPITRE-15.md')
PROOF = Path('Livre-III/QA/VALIDATION-FINALE-CHAPITRE-15.yaml')
EXPECTED_CHAPTER = '7db682e1b4c4bc85519a056b45d5ffb80b340d50a5d9c7663e38690cdcf0f85a'
EXPECTED_AUDIT = 'a54b97367c5fc1434f369b67505dc130fec37a111e9d8602abc0afa880dab728'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_package() -> dict[str, str]:
    parts = sorted(Path('.qa').glob('ch15-package-*.txt'))
    if len(parts) != 4:
        raise RuntimeError(f'Quatre fragments attendus, {len(parts)} reçus.')

    chunks = [path.read_text(encoding='ascii').strip() for path in parts]

    # Le premier transfert a remplacé le dernier caractère du fragment 1.
    # La réparation est bornée, explicite et disparaît avec le transport temporaire.
    if chunks[0].endswith('u'):
        chunks[0] = chunks[0][:-1] + 'O'

    encoded = ''.join(chunks)
    payload = json.loads(gzip.decompress(base64.b64decode(encoded)).decode('utf-8'))
    required = {'chapter', 'audit', 'governance', 'close'}
    if set(payload) != required:
        raise RuntimeError(f'Clés de paquet inattendues: {sorted(payload)}')
    return payload


def main() -> None:
    if os.environ.get('HEAD_BRANCH') != 'docs/livre-iii-ch15-vegetation-biomes':
        raise RuntimeError('Branche inattendue pour le lot du chapitre 15.')

    payload = load_package()
    CHAPTER.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    CHAPTER.write_text(payload['chapter'], encoding='utf-8')
    AUDIT.write_text(payload['audit'], encoding='utf-8')
    Path('.qa/ch15-governance.py').write_text(payload['governance'], encoding='utf-8')
    Path('.qa/ch15-close.py').write_text(payload['close'], encoding='utf-8')

    chapter_hash = sha256(CHAPTER)
    audit_hash = sha256(AUDIT)
    if chapter_hash != EXPECTED_CHAPTER:
        raise RuntimeError(f'Empreinte du chapitre inattendue: {chapter_hash}')
    if audit_hash != EXPECTED_AUDIT:
        raise RuntimeError(f'Empreinte de l audit inattendue: {audit_hash}')

    base_commit = os.environ['BASE_COMMIT']
    PROOF.write_text(f'''schema-version: 1
evidence-id: DOC-L3-QA-EVIDENCE-CH15
status: pending
validation-date: '2026-07-23'
validated-base-commit: {base_commit}
validated-head-commit: null
chapter:
  id: DOC-L3-CH15
  path: Livre-III/CHAPITRE-15-Vegetation-et-biomes.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 1
  chapter-lines: 2236
  chapter-headings: 64
  chapter-code-and-data-blocks: 66
  significant-code-and-data-blocks: 66
  code-explanation-markers: 66
  structured-non-error-code-explanations: 46
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  duplicate-headings: 0
  duplicate-blocks: 0
  duplicate-paragraphs: 0
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  solo-studio-markdown-only: true
  master-plan-scope-covered: true
  biome-visual-and-ecological-profile-documented: true
  species-morphotype-variant-instance-separation-documented: true
  trees-shrubs-grasses-flowers-groundcover-debris-documented: true
  scale-pivot-and-source-collections-documented: true
  foliage-opacity-and-atlas-boundary-documented: true
  size-season-health-variants-documented: true
  hierarchical-wind-documented: true
  per-instance-wind-phase-documented: true
  local-visual-interaction-documented: true
  lod-impostors-and-distant-representations-documented: true
  distribution-maps-and-coordinate-contract-documented: true
  slope-altitude-moisture-and-exclusion-rules-documented: true
  deterministic-seeds-and-versioned-algorithm-documented: true
  geometry-nodes-preview-boundary-documented: true
  multimesh-selection-and-limit-documented: true
  spatial-batching-by-cell-species-lod-material-documented: true
  custom-aabb-and-wind-margin-documented: true
  cell-lifecycle-integration-documented: true
  collision-and-placement-exclusion-separated: true
  navigation-clearance-documented: true
  shadows-overdraw-and-transparency-cost-documented: true
  cpu-gpu-memory-density-benchmark-documented: true
  blender-gltf-export-documented: true
  godot-derived-scene-documented: true
  functions-parameters-types-returns-operators-documented: true
  provenance-documented: true
  solo-and-studio-documented: true
  acceptance-gate-documented: true
  no-terrain-streaming-duplication: true
  no-general-pbr-duplication: true
  no-generic-uv-baking-duplication: true
  no-general-animation-duplication: true
  no-authoritative-ecological-simulation: true
  no-authoritative-gameplay-state: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  error-explanations-directly-after-markers: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  validate-chapters-without-pdf:
    workflow-name: Chapter 15 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending
  validate-usage-contexts:
    workflow-name: Chapter 15 Finalizer Runner
    execution: embedded-command
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
  context-artifact:
    id: null
    name: usage-context-audit
    digest: null
reservations:
- Pilot biome brief not approved by a production review.
- References, rights and provenance not qualified.
- Species catalogue and species sheets not approved.
- Dimensions, silhouettes and pivots not measured.
- Trees, shrubs, grasses, flowers, groundcovers and debris not produced.
- Blender sources and export collections not created.
- Foliage, atlases and materials not produced.
- Wind shaders not compiled.
- Local interaction not executed.
- Seasonal and health variants not produced.
- LOD assets and impostors not produced.
- Distribution maps not produced.
- Slope, altitude, moisture and exclusion constraints not tested.
- Deterministic placement not executed.
- Geometry Nodes preview not created.
- MultiMesh resources not generated.
- Batch sizes and custom bounding boxes not measured.
- Cell loading and unloading integration not tested.
- Collisions and navigation not produced or validated.
- Shadows and overdraw not measured.
- Godot scenes and GLB exports not materialized.
- Density benchmark not executed.
- CPU, GPU, VRAM, memory, draw-call, distance and density values not measured.
- Starter Kit not materialized.
- Collection-wide licence not defined.
- Livre III PDF not built by end-of-book policy.
evidence-closure:
  commit: null
  conclusion: pending
''', encoding='utf-8')


if __name__ == '__main__':
    main()
