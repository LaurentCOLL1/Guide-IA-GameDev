from pathlib import Path
import os

def repl(text, old, new, label):
    count=text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, got {count}')
    return text.replace(old,new,1)

p=Path('Livre-III/QA/VALIDATION-FINALE-CHAPITRE-19.yaml'); t=p.read_text(encoding='utf-8')
t=repl(t,'status: pending','status: complete','proof status')
t=repl(t,'validated-head-commit: pending',f"validated-head-commit: {os.environ['DOCUMENT_HEAD']}",'proof head')
t=repl(t,'  blocking-errors: pending','  blocking-errors: 0','proof errors')
old1='''  validate-chapters-without-pdf:
    workflow-name: Chapter 19 Finalizer Runner
    execution: embedded-command
    run-id: pending
    conclusion: pending'''
new1=f'''  validate-chapters-without-pdf:
    workflow-name: Chapter 19 Finalizer Runner
    execution: embedded-command
    run-id: {os.environ['VALIDATION_RUN_ID']}
    conclusion: success'''
t=repl(t,old1,new1,'proof validation workflow')
old2='''  validate-usage-contexts:
    workflow-name: Chapter 19 Finalizer Runner
    execution: embedded-command
    run-id: pending
    conclusion: pending'''
new2=f'''  validate-usage-contexts:
    workflow-name: Chapter 19 Finalizer Runner
    execution: embedded-command
    run-id: {os.environ['VALIDATION_RUN_ID']}
    conclusion: success'''
t=repl(t,old2,new2,'proof context workflow')
old3='''  artifact:
    id: pending
    name: chapter-validation-without-pdf
    digest: pending'''
new3=f'''  artifact:
    id: {os.environ['MAIN_ARTIFACT_ID']}
    name: chapter-validation-without-pdf
    digest: {os.environ['MAIN_ARTIFACT_DIGEST'].removeprefix('sha256:')}'''
t=repl(t,old3,new3,'proof artifact')
old4='''  context-artifact:
    id: pending
    name: usage-context-audit
    digest: pending'''
new4=f'''  context-artifact:
    id: {os.environ['CONTEXT_ARTIFACT_ID']}
    name: usage-context-audit
    digest: {os.environ['CONTEXT_ARTIFACT_DIGEST'].removeprefix('sha256:')}'''
t=repl(t,old4,new4,'proof context artifact')
p.write_text(t,encoding='utf-8')

p=Path('CONTINUITE-PROJET.md'); t=p.read_text(encoding='utf-8')
t=repl(t,'version: "3.49.0"','version: "3.49.1"','continuity version close')
t=repl(t,'last-updated: "2026-07-24T04:10:00+02:00"','last-updated: "2026-07-24T04:30:00+02:00"','continuity timestamp close')
journal=f'''### 2026-07-24T04:30:00+02:00 — version 3.49.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-19.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 19 Finalizer Runner`, run `{os.environ['VALIDATION_RUN_ID']}`, sur la tête documentaire `{os.environ['DOCUMENT_HEAD']}` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `{os.environ['MAIN_ARTIFACT_ID']}`, digest `{os.environ['MAIN_ARTIFACT_DIGEST'].removeprefix('sha256:')}` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `{os.environ['CONTEXT_ARTIFACT_ID']}`, digest `{os.environ['CONTEXT_ARTIFACT_DIGEST'].removeprefix('sha256:')}` ;
- empreinte SHA-256 du chapitre : `57b09954e53bd85507cc283e373ba5b6a66981100dac277db36041851e241e7b` ;
- empreinte SHA-256 de l’audit : `6b04f3a29668933df08e4a8ccc88c81373545baaa3297b87c92bdd6afd781c67` ;
- métriques finales : 2 255 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 20 — Animation procédurale et animation par keyframes, niveau Élevée ;
- aucun rig, poids, correctif, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

'''
t=repl(t,'## 27. Journal\n\n','## 27. Journal\n\n'+journal,'continuity close journal')
p.write_text(t,encoding='utf-8')
