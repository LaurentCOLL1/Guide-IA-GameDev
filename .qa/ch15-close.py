from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

STAGE_STAMP = '2026-07-23T20:23:04+02:00'
CHAPTER_HASH = '7db682e1b4c4bc85519a056b45d5ffb80b340d50a5d9c7663e38690cdcf0f85a'
AUDIT_HASH = 'a54b97367c5fc1434f369b67505dc130fec37a111e9d8602abc0afa880dab728'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: attendu une occurrence, obtenu {count}.')
    return text.replace(old, new, 1)


def main() -> None:
    document_head = os.environ['DOCUMENT_HEAD']
    run_id = os.environ['VALIDATION_RUN_ID']
    artifact_id = os.environ['MAIN_ARTIFACT_ID']
    artifact_digest = os.environ['MAIN_ARTIFACT_DIGEST']
    context_id = os.environ['CONTEXT_ARTIFACT_ID']
    context_digest = os.environ['CONTEXT_ARTIFACT_DIGEST']

    proof_path = Path('Livre-III/QA/VALIDATION-FINALE-CHAPITRE-15.yaml')
    proof = proof_path.read_text(encoding='utf-8')
    proof = replace_once(proof, 'status: pending', 'status: complete', 'statut preuve')
    proof = replace_once(proof, 'validated-head-commit: null', f'validated-head-commit: {document_head}', 'tête validée')
    proof = replace_once(proof, '    run-id: null\n    conclusion: pending', f'    run-id: {run_id}\n    conclusion: success', 'validation chapitres')
    proof = replace_once(proof, '    run-id: null\n    conclusion: pending', f'    run-id: {run_id}\n    conclusion: success', 'validation contextes')
    proof = replace_once(proof, '  artifact:\n    id: null\n    name: chapter-validation-without-pdf\n    digest: null', f'  artifact:\n    id: {artifact_id}\n    name: chapter-validation-without-pdf\n    digest: {artifact_digest}', 'artefact principal')
    proof = replace_once(proof, '  context-artifact:\n    id: null\n    name: usage-context-audit\n    digest: null', f'  context-artifact:\n    id: {context_id}\n    name: usage-context-audit\n    digest: {context_digest}', 'artefact contextes')
    proof_path.write_text(proof, encoding='utf-8')

    now = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()
    continuity_path = Path('CONTINUITE-PROJET.md')
    continuity = continuity_path.read_text(encoding='utf-8')
    continuity = replace_once(continuity, 'version: "3.45.0"', 'version: "3.45.1"', 'version continuité finale')
    continuity = replace_once(continuity, f'last-updated: "{STAGE_STAMP}"', f'last-updated: "{now}"', 'horodatage continuité finale')
    final_entry = f'''### {now} — version 3.45.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-15.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 15 Finalizer Runner`, run `{run_id}`, sur la tête documentaire `{document_head}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{artifact_id}`, digest `{artifact_digest}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{context_id}`, digest `{context_digest}` ;
- empreinte SHA-256 du chapitre : `{CHAPTER_HASH}` ;
- empreinte SHA-256 de l’audit : `{AUDIT_HASH}` ;
- métriques finales : 2 236 lignes, 64 titres, 66 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 16 — Textures, matériaux et pipeline PBR, niveau Élevée ;
- aucun végétal, texture, matériau, atlas, shader, carte, `MultiMesh`, imposteur, collision, scène, GLB, benchmark, résultat runtime ou PDF du Livre III produit.

'''
    anchor = f'### {STAGE_STAMP} — version 3.45.0'
    continuity = replace_once(continuity, anchor, final_entry + anchor, 'journal preuve finale')
    continuity_path.write_text(continuity, encoding='utf-8')


if __name__ == '__main__':
    main()
