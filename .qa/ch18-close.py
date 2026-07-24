from pathlib import Path
import os

def repl(t,o,n,label):
    if t.count(o)!=1: raise RuntimeError(f'{label}: {t.count(o)}')
    return t.replace(o,n,1)

p=Path('Livre-III/QA/VALIDATION-FINALE-CHAPITRE-18.yaml'); t=p.read_text(encoding='utf-8')
t=repl(t,'status: pending','status: complete','status')
t=repl(t,'validated-head-commit: pending',f"validated-head-commit: {os.environ['DOCUMENT_HEAD']}",'head')
t=repl(t,'  blocking-errors: pending','  blocking-errors: 0','errors')
old_chapters='''  validate-chapters-without-pdf:
    workflow-name: Chapter 18 Finalizer Runner
    execution: embedded-command
    run-id: pending
    conclusion: pending'''
new_chapters=f'''  validate-chapters-without-pdf:
    workflow-name: Chapter 18 Finalizer Runner
    execution: embedded-command
    run-id: {os.environ['VALIDATION_RUN_ID']}
    conclusion: success'''
t=repl(t,old_chapters,new_chapters,'run chapters')
old_contexts='''  validate-usage-contexts:
    workflow-name: Chapter 18 Finalizer Runner
    execution: embedded-command
    run-id: pending
    conclusion: pending'''
new_contexts=f'''  validate-usage-contexts:
    workflow-name: Chapter 18 Finalizer Runner
    execution: embedded-command
    run-id: {os.environ['VALIDATION_RUN_ID']}
    conclusion: success'''
t=repl(t,old_contexts,new_contexts,'run contexts')
t=repl(t,'    id: pending\n    name: chapter-validation-without-pdf\n    digest: pending',f"    id: {os.environ['MAIN_ARTIFACT_ID']}\n    name: chapter-validation-without-pdf\n    digest: {os.environ['MAIN_ARTIFACT_DIGEST'].removeprefix('sha256:')}",'artifact')
t=repl(t,'    id: pending\n    name: usage-context-audit\n    digest: pending',f"    id: {os.environ['CONTEXT_ARTIFACT_ID']}\n    name: usage-context-audit\n    digest: {os.environ['CONTEXT_ARTIFACT_DIGEST'].removeprefix('sha256:')}",'context artifact')
p.write_text(t,encoding='utf-8')

p=Path('CONTINUITE-PROJET.md'); t=p.read_text(encoding='utf-8')
t=repl(t,'version: "3.48.0"','version: "3.48.1"','continuity version')
t=repl(t,'last-updated: "2026-07-24T02:35:00+02:00"','last-updated: "2026-07-24T02:55:00+02:00"','continuity time')
j=f'''### 2026-07-24T02:55:00+02:00 — version 3.48.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-18.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 18 Finalizer Runner`, run `{os.environ['VALIDATION_RUN_ID']}`, sur la tête documentaire `{os.environ['DOCUMENT_HEAD']}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{os.environ['MAIN_ARTIFACT_ID']}`, digest `{os.environ['MAIN_ARTIFACT_DIGEST'].removeprefix('sha256:')}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{os.environ['CONTEXT_ARTIFACT_ID']}`, digest `{os.environ['CONTEXT_ARTIFACT_DIGEST'].removeprefix('sha256:')}` ;
- empreinte SHA-256 du chapitre : `e3a68e7826741d7f09136777108c370e5678bf5c5e4707c337164b1f88092697` ;
- empreinte SHA-256 de l’audit : `7a1740697d1a8aeefad7ee2c6ca32b73aaa8d601988e223fcc3c43eaf6c935d1` ;
- métriques finales : 3 904 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 19 — Rigging et skinning, niveau Élevée ;
- aucun mesh LOD, proxy, atlas, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

'''
t=repl(t,'## 27. Journal\n\n','## 27. Journal\n\n'+j,'journal close')
p.write_text(t,encoding='utf-8')
