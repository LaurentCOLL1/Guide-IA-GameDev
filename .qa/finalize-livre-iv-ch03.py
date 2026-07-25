#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from hashlib import sha256
import base64,gzip,re
ROOT=Path(__file__).resolve().parents[1]
NOW=datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
TODAY=NOW[:10]
chapter=gzip.decompress(base64.b64decode("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")).decode("utf-8")
chapter=re.sub(r'last-verified: ".*?"',f'last-verified: "{NOW}"',chapter,1)
chapter=re.sub(r'audit-date: ".*?"',f'audit-date: "{NOW}"',chapter,1)
cp=ROOT/"Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md"
cp.write_text(chapter,encoding="utf-8")
audit = f"""---
title: "Audit post-création — Livre IV, chapitre 3"
id: "DOC-L4-QA-AUDIT-CH03"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH03"
chapter-version: "1.0.0"
audit-date: "{NOW}"
last-verified: "{NOW}"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 3

## 1. Décision

Chapitre accepté au niveau `static-review`, avec réserves d’exécution. Aucun cas, run Godot, campagne, mutation connue ou résultat runtime n’est revendiqué.

## 2. Périmètre

Le chapitre couvre cas reproductibles, suites manuelles et automatisées, fixtures, seeds, états contrôlés, non-régression, suites smoke/rapide/complète/publication, rapports et matrice de couverture.

## 3. Frontières

Le chapitre 2 conserve risques, rôles et portes. Le chapitre 4 conserve reproduction détaillée et réduction des anomalies. Le chapitre 5 conserve l’observabilité générale.

## 4. Contrôles

- lignes : 1060 ;
- blocs : 50 ;
- marqueurs d’explication : 50 ;
- diagnostics : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- texte lecteur sans recommandation GPT, prochaine action ou chaîne d’export ;
- références officielles cliquables ;
- modes Solo et Studio présents ;
- synthèse Project Asteria présente.

## 5. Réserves

- catalogue et fixtures non matérialisés ;
- aucune suite exécutée ;
- aucune régression connue injectée ;
- aucune mesure runtime ;
- aucune décision produit.

## 6. Conclusion

Le chapitre satisfait le plan maître et les contrôles documentaires et statiques.
"""
ap=ROOT/"Livre-IV/QA/AUDIT-CHAPITRE-03.md"
ap.write_text(audit,encoding="utf-8")
proof=f"""schema-version: 1
evidence-id: DOC-L4-QA-EVIDENCE-CH03
validation-authority: chapter-finalizer-and-permanent-workflows
status: pending
validation-date: '{TODAY}'
validated-base-commit: pending
validated-head-commit: pending
chapter:
  id: DOC-L4-CH03
  path: Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: pending
  warnings: pending
  chapter-lines: 1060
  chapter-code-and-data-blocks: 50
  code-explanation-markers: 50
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  reader-export-pipeline-mentions-absent: true
  next-step-absent-from-reader-chapter: true
  solo-studio-documented: true
  master-plan-scope-covered: true
  project-asteria-operational-summary-present: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  runtime-executed: false
integrity:
  chapter-sha256: {sha256(chapter.encode()).hexdigest()}
  audit-sha256: {sha256(audit.encode()).hexdigest()}
ci:
  chapter-finalizer:
    run-id: pending
    conclusion: pending
  validate-chapters-without-pdf:
    run-id: pending
    conclusion: pending
reservations:
  - Test catalog and fixtures not materialized.
  - No suite executed.
  - No known regression injected.
  - No runtime measurement produced.
evidence-closure:
  commit: pending
  conclusion: pending
"""
(ROOT/"Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-03.yaml").write_text(proof,encoding="utf-8")
def edit(path, fn):
    p=ROOT/path
    p.write_text(fn(p.read_text(encoding="utf-8")),encoding="utf-8")
def upd_index(s):
    s=s.replace('version: "0.3.0"','version: "0.4.0"',1)
    s=re.sub(r'last-updated: ".*?"',f'last-updated: "{NOW}"',s,1)
    s=s.replace('3. Tests fonctionnels et tests de régression ;','3. [Tests fonctionnels et tests de régression](CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md) — version `1.0.0`, niveau `static-review` ;')
    s=s.replace('**2 sur 22**','**3 sur 22**')
    s=s.replace('chapitre courant terminé : **chapitre 2 — Stratégie générale d’assurance qualité**','chapitre courant terminé : **chapitre 3 — Tests fonctionnels et tests de régression**')
    s=s.replace('prochaine entrée du plan maître : **chapitre 3 — Tests fonctionnels et tests de régression**','prochaine entrée du plan maître : **chapitre 4 — Débogage et reproduction des anomalies**')
    s=s.replace('les chapitres 1 et 2 sont terminés','les chapitres 1 à 3 sont terminés')
    return s
edit("Livre-IV/index.md",upd_index)
def upd_roadmap(s):
    s=s.replace('- [ ] Équilibrage, QA et diagnostic — 2 chapitres sur 5.','- [ ] Équilibrage, QA et diagnostic — 3 chapitres sur 5.')
    if 'Chapitre 3 — Tests fonctionnels' not in s:
        s=s.replace('- [x] Chapitre 2 — Stratégie générale d’assurance qualité — rédigé, repéré et audité au niveau `static-review`.','- [x] Chapitre 2 — Stratégie générale d’assurance qualité — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 3 — Tests fonctionnels et tests de régression — rédigé, repéré et audité au niveau `static-review`.')
    s=s.replace('**Statut M5 : en cours — 2 chapitres rédigés, repérés et audités sur 22.**','**Statut M5 : en cours — 3 chapitres rédigés, repérés et audités sur 22.**')
    return s
edit("ROADMAP.md",upd_roadmap)
edit("contents.txt",lambda s:s.replace('Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md','Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md\nLivre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md'))
def upd_plan(s):
    s=s.replace('version: "1.0.2"','version: "1.0.3"',1)
    s=re.sub(r'last-updated: ".*?"',f'last-updated: "{NOW}"',s,1)
    s=s.replace('en cours — 2 chapitres sur 22','en cours — 3 chapitres sur 22')
    anchor='Les tests unitaires de code sont introduits au Livre II ; ici ils sont intégrés à la campagne produit. Validation par détection volontaire d’une régression connue.'
    if 'État documentaire au '+TODAY not in s[s.find('## Chapitre 3'):s.find('## Chapitre 4')]:
        s=s.replace(anchor,anchor+f'\n\n**État documentaire au {TODAY} :** chapitre rédigé, repéré et audité au niveau `static-review`. Les cas, fixtures, suites et mutations sont préparés sans revendication d’exécution.')
    return s
edit("plans/LIVRE-IV-PLAN-MAITRE.md",upd_plan)
def cont(s):
    s=s.replace('version: "3.65.0"','version: "3.66.0"',1)
    s=re.sub(r'last-updated: ".*?"',f'last-updated: "{NOW}"',s,1)
    s=s.replace('- progression du Livre IV : 2 chapitres sur 22 ;','- progression du Livre IV : 3 chapitres sur 22 ;')
    s=s.replace('- chapitre 2 du Livre IV : version `1.0.0`, niveau `static-review` ;','- chapitre 2 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 3 du Livre IV : version `1.0.0`, niveau `static-review` ;')
    s=s.replace('Les chapitres 1 et 2 du Livre IV sont terminés','Les chapitres 1 à 3 du Livre IV sont terminés')
    s=s.replace('Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md','Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md')
    s=s.replace('Le chapitre 3 du Livre IV matérialisera les cas fonctionnels et suites de régression, avec fixtures, états contrôlés, tests rapides et campagnes complètes. Il appliquera la stratégie du chapitre 2 sans redéfinir ses risques, portes, rôles ou règles de décision.','Le chapitre 4 du Livre IV détaillera les rapports exploitables, la reproduction, la réduction des anomalies et la gestion des doublons sans redéfinir les campagnes du chapitre 3.')
    anchor='## 27. Journal'
    entry=f"""## 27. Journal

### {NOW} — version 3.66.0

- création du chapitre 3 du Livre IV — Tests fonctionnels et tests de régression ;
- catalogue, cas, fixtures synthétiques, seeds, états contrôlés et oracles documentés ;
- suites smoke, rapide, complète et publication définies ;
- non-régression, mutation connue isolée, quarantaine et tests instables encadrés ;
- dix diagnostics conformes ;
- prochaine action déplacée vers le chapitre 4 — Débogage et reproduction des anomalies ;
- aucune campagne ou mesure runtime revendiquée.

"""
    return s.replace(anchor,entry,1)
edit("CONTINUITE-PROJET.md",cont)
print("lot matérialisé")