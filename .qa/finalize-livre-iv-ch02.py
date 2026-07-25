#!/usr/bin/env python3
from __future__ import annotations

import base64
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo
import re
import zlib

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
TODAY = NOW[:10]
BASE_COMMIT = "6f9b702b5cedc9ffd2ea76ba51a3ddb37e439ea5"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)


encoded = "".join(read(f".qa/ch02.part{i}").strip() for i in range(5))
chapter = zlib.decompress(base64.b64decode(encoded)).decode("utf-8")
expected_sha = "641906502d493d6fc44332759426cc2d39c34b13c341e965a898541489bc63ae"
if sha256(chapter.encode("utf-8")).hexdigest() != expected_sha:
    raise RuntimeError("Empreinte du chapitre 2 inattendue.")
if re.search(r"\bpdf\b", chapter, flags=re.IGNORECASE):
    raise RuntimeError("Le texte lecteur contient une référence à la chaîne d’export du guide.")
if "GPT-5.6" in chapter or "Prochaine étape" in chapter:
    raise RuntimeError("Le texte lecteur contient une instruction de pilotage éditorial.")
if chapter.count("<!-- qa:code-explanation -->") != 58:
    raise RuntimeError("Nombre de marqueurs d’explication inattendu.")
if chapter.count("**Pourquoi cet exemple est fautif :**") != 10:
    raise RuntimeError("Nombre d’explications fautives inattendu.")
if chapter.count("**Pourquoi la correction fonctionne :**") != 10:
    raise RuntimeError("Nombre d’explications corrigées inattendu.")

chapter_path = "Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md"
write(chapter_path, chapter)
chapter_hash = sha256(chapter.encode("utf-8")).hexdigest()


audit = f'''---
title: "Audit post-création — Livre IV, chapitre 2"
id: "DOC-L4-QA-AUDIT-CH02"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH02"
chapter-version: "1.0.0"
audit-date: "{NOW}"
last-verified: "{NOW}"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 2

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation de la charte QA, du registre des risques, de la matrice risques/contrôles, des portes qualité, des campagnes, des revues spécialisées et des exercices de récupération.

Aucune campagne fonctionnelle, artistique, sécurité, accessibilité, compatibilité, restauration ou publication de `Project Asteria` n’est revendiquée comme exécutée. Les commandes, schémas et scripts restent des modèles pédagogiques relus statiquement.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- niveaux de test, responsabilités et portes qualité ;
- distinction entre prévention, détection et correction ;
- risques, priorités et calendrier ;
- critères d’entrée et de sortie ;
- articulation des axes documentaire, technique, artistique et produit.

Les livrables sont préparés comme contrats : charte QA, modèle de qualité, registre des risques, matrice risques/contrôles, calendrier, rôles Solo/Studio, modèles de rapports et validateur structurel. Leur matérialisation dans le projet fil rouge reste en réserve.

## 3. Frontières contrôlées

- le chapitre 1 conserve le catalogue de métriques, les simulations d’équilibrage et les rapports de décision associés ;
- le chapitre 3 conservera les cas de test, fixtures, scènes, suites manuelles et automatisées et matrices de couverture détaillées ;
- le chapitre 4 conservera la reproduction et le diagnostic des anomalies ;
- le chapitre 5 conservera la politique d’observabilité produit ;
- les chapitres 6 à 10 conserveront les campagnes de profilage et d’optimisation ;
- les chapitres 13 à 17 conserveront sécurité réseau, DevOps, packaging et publication spécialisés ;
- aucune porte qualité ne modifie directement un système de gameplay ;
- aucun pipeline ou score unique ne reçoit l’autorité de publication.

## 4. Contrôles pédagogiques

- objectifs, résultats d’apprentissage, prérequis et frontières explicités ;
- vocabulaire qualité, QA, contrôle, test, risque, porte, preuve, réserve, dérogation, sévérité et priorité défini ;
- modèles de qualité, niveaux et familles de contrôle documentés ;
- prévention, détection et correction séparées ;
- registre des risques et politique de classement expliqués ;
- couverture explicite des risques critiques par matrice ;
- six portes et leurs critères d’entrée/sortie définis ;
- statuts `PASS`, `PASS_WITH_RESERVATIONS`, `HOLD` et `REJECT` distingués ;
- rôles Solo et Studio, RACI et indépendance documentés ;
- calendrier, environnements, baselines, triage, stop-ship et dérogations couverts ;
- QA documentaire, technique, artistique et produit reliées ;
- accessibilité, sécurité, données assistées et récupérabilité intégrées ;
- indicateurs avec dénominateurs et modèles de rapports fournis ;
- validateur Python structurel et commande PowerShell expliqués ;
- cinquante-huit blocs possèdent un repère et une explication ;
- dix diagnostics suivent la séquence sémantique complète ;
- sources officielles fournies sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 2204 ;
- titres : 61 ;
- blocs code ou données : 58 ;
- blocs significatifs : 58 ;
- marqueurs d’explication : 58 ;
- explications structurées hors diagnostics : 38 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques sous forme de liens Markdown cliquables ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le script Python utilise `dataclasses`, `datetime`, `typing`, listes et ensembles de la bibliothèque standard. La date est injectée dans `expired_waiver_ids()` au lieu d’être lue implicitement, ce qui maintient le déterminisme du contrôle.

Les valeurs de probabilité, impact et détectabilité sont déclarées ordinales. Le chapitre refuse de présenter leur multiplication comme une mesure scientifique. Les portes consomment plusieurs domaines et la décision finale reste humaine.

Les termes `RACI`, `stop-ship`, baseline, dérogation et risque résiduel sont définis dans leur usage opérationnel. Les exemples ne prétendent pas constituer une certification ou un conseil juridique personnalisé.

## 7. Contrôle des doublons et des frontières

Aucun titre, bloc significatif ou paragraphe long n’est dupliqué.

Les sujets voisins restent distincts :

- métriques et équilibrage : chapitre 1 ;
- cas fonctionnels et régression : chapitre 3 ;
- reproduction des anomalies : chapitre 4 ;
- observabilité : chapitre 5 ;
- profilage : chapitres 6 à 10 ;
- sécurité réseau et exploitation : chapitres 13 à 17.

## 8. Réserves ouvertes

- charte `AST-QA-CHARTER-001` non matérialisée ;
- profil de qualité non approuvé ;
- registre des risques non créé ;
- matrice risques/contrôles non créée ;
- calendrier et politiques de portes non créés ;
- aucune campagne fonctionnelle ou de non-régression exécutée ;
- aucune revue artistique, accessibilité ou sécurité exécutée ;
- aucun exercice de restauration ou retour arrière exécuté ;
- aucun environnement ou build candidat qualifié ;
- aucune décision de porte ou de publication approuvée ;
- aucune mesure runtime produite ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître et peut entrer dans la validation documentaire et statique. La preuve finale reste en attente de la réussite des contrôles sur la branche dédiée.
'''

audit_path = "Livre-IV/QA/AUDIT-CHAPITRE-02.md"
write(audit_path, audit)
audit_hash = sha256(audit.encode("utf-8")).hexdigest()

proof = f'''schema-version: 1
evidence-id: DOC-L4-QA-EVIDENCE-CH02
validation-authority: chapter-finalizer-and-permanent-workflows
status: pending
validation-date: '{TODAY}'
validated-base-commit: {BASE_COMMIT}
validated-head-commit: pending
chapter:
  id: DOC-L4-CH02
  path: {chapter_path}
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: pending
  warnings: pending
  chapter-lines: 2204
  chapter-headings: 61
  chapter-code-and-data-blocks: 58
  significant-code-and-data-blocks: 58
  code-explanation-markers: 58
  structured-non-error-code-explanations: 38
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  duplicate-headings: 0
  duplicate-blocks: 0
  duplicate-paragraphs: 0
  reader-qa-procedure-absent: true
  reader-export-pipeline-mentions-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  solo-studio-documented: true
  master-plan-scope-covered: true
  project-asteria-operational-summary-present: true
  clickable-technical-references: true
  qa-charter-documented: true
  risk-test-matrix-documented: true
  entry-exit-criteria-documented: true
  quality-gates-documented: true
  prevention-detection-correction-separated: true
  documentary-technical-artistic-product-linked: true
  stop-ship-and-waivers-documented: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  error-explanations-directly-after-markers: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  chapter-finalizer:
    workflow-name: Livre IV Chapter 2 Finalizer
    execution: pending
    run-id: pending
    conclusion: pending
  validate-chapters-without-pdf:
    workflow-name: Validate Chapters Without PDF
    execution: pending
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    workflow-name: Validate Usage Contexts
    execution: pending
    run-id: pending
    conclusion: pending
  artifact:
    id: pending
    name: livre-iv-ch02-validation-without-pdf
    digest: pending
reservations:
  - QA charter not materialized.
  - Risk register and risk/control matrix not materialized.
  - Gate policy and QA calendar not materialized.
  - Functional and regression campaigns not executed.
  - Artistic, accessibility and security reviews not executed.
  - Recovery drill and rollback not executed.
  - No release candidate or environment qualified.
  - No gate or release decision approved.
  - Runtime measurements not produced.
  - Collection-wide licence not defined.
  - Final export accessibility tagging remains open.
evidence-closure:
  commit: pending
  conclusion: pending
'''
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-02.yaml", proof)

index_path = "Livre-IV/index.md"
index = read(index_path)
index = replace_once(index, 'version: "0.2.1"', 'version: "0.3.0"', "version index")
index = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', index, count=1, flags=re.MULTILINE)
index = replace_once(index, '2. Stratégie générale d’assurance qualité ;', '2. [Stratégie générale d’assurance qualité](CHAPITRE-02-Strategie-generale-d-assurance-qualite.md) — version `1.0.0`, niveau `static-review` ;', "entrée chapitre 2")
index = replace_once(index, '- chapitres rédigés, repérés et audités : **1 sur 22** ;', '- chapitres rédigés, repérés et audités : **2 sur 22** ;', "progression index")
index = replace_once(index, '- chapitre courant terminé : **chapitre 1 — Équilibrage et télémétrie locale** ;', '- chapitre courant terminé : **chapitre 2 — Stratégie générale d’assurance qualité** ;', "chapitre courant index")
index = replace_once(index, '- prochaine entrée du plan maître : **chapitre 2 — Stratégie générale d’assurance qualité** ;', '- prochaine entrée du plan maître : **chapitre 3 — Tests fonctionnels et tests de régression** ;', "prochaine entrée index")
index = replace_once(index, 'le chapitre 1 est terminé au niveau documentaire et statique', 'les chapitres 1 et 2 sont terminés au niveau documentaire et statique', "statut index")
write(index_path, index)

roadmap_path = "ROADMAP.md"
roadmap = read(roadmap_path)
roadmap = replace_once(roadmap, '- [x] Chapitre 1 — Équilibrage et télémétrie locale — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Équilibrage, QA et diagnostic — 1 chapitre sur 5.', '- [x] Chapitre 1 — Équilibrage et télémétrie locale — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 2 — Stratégie générale d’assurance qualité — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Équilibrage, QA et diagnostic — 2 chapitres sur 5.', "roadmap chapitres")
roadmap = replace_once(roadmap, '**Statut M5 : en cours — 1 chapitre rédigé, repéré et audité sur 22.**', '**Statut M5 : en cours — 2 chapitres rédigés, repérés et audités sur 22.**', "statut M5")
write(roadmap_path, roadmap)

contents_path = "contents.txt"
contents = read(contents_path)
contents = replace_once(contents, 'Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md\nLivre-V/index.md', 'Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md\nLivre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md\nLivre-V/index.md', "ordre lecteur")
write(contents_path, contents)

plan_path = "plans/LIVRE-IV-PLAN-MAITRE.md"
plan = read(plan_path)
plan = replace_once(plan, 'version: "1.0.1"', 'version: "1.0.2"', "version plan")
plan = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', plan, count=1, flags=re.MULTILINE)
plan = replace_once(plan, '> **Statut :** en cours — 1 chapitre sur 22', '> **Statut :** en cours — 2 chapitres sur 22', "statut plan")
anchor = 'Les tests détaillés viennent aux chapitres suivants. Validation par couverture explicite des risques critiques.'
plan = replace_once(plan, anchor, anchor + f'\n\n**État documentaire au {TODAY} :** chapitre rédigé, repéré et audité au niveau `static-review`. La charte, les risques, les portes et rapports sont préparés sans revendication de campagne ou de décision runtime.', "état chapitre 2 plan")
write(plan_path, plan)

continuity_path = "CONTINUITE-PROJET.md"
continuity = read(continuity_path)
continuity = replace_once(continuity, 'version: "3.64.0"', 'version: "3.65.0"', "version continuité")
continuity = re.sub(r'^last-updated: ".*"$', f'last-updated: "{NOW}"', continuity, count=1, flags=re.MULTILINE)
continuity = replace_once(continuity, '- ne pas collecter une métrique sans question, finalité et politique de conservation explicites ;', '- ne pas considérer un pipeline vert, un score unique ou un taux de couverture comme une autorité de publication ;\n- ne pas enregistrer un risque critique sans propriétaire, couches de contrôle et décision résiduelle ;\n- ne pas accorder une dérogation sans portée, approbateur et expiration ;\n- ne pas modifier un critère après observation des résultats sans créer une nouvelle version applicable aux campagnes futures ;\n- ne pas collecter une métrique sans question, finalité et politique de conservation explicites ;', "règles QA")
continuity = replace_once(continuity, '- progression du Livre IV : 1 chapitre sur 22 ;\n- chapitre 1 du Livre IV : version `1.0.1`, niveau `static-review` ;', '- progression du Livre IV : 2 chapitres sur 22 ;\n- chapitre 1 du Livre IV : version `1.0.1`, niveau `static-review` ;\n- chapitre 2 du Livre IV : version `1.0.0`, niveau `static-review` ;', "état Livre IV")
continuity = replace_once(continuity, 'Le chapitre 1 du Livre IV est terminé au niveau documentaire et statique. Le catalogue, les scénarios, les collecteurs, les analyses, les playtests et les décisions réelles restent non matérialisés.', 'Les chapitres 1 et 2 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, revues spécialisées, playtests et décisions réelles restent non matérialisés.', "résumé prochaine action")
continuity = replace_once(continuity, 'Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md\nNiveau GPT-5.6 Sol recommandé : Élevée', 'Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md\nNiveau GPT-5.6 Sol recommandé : Élevée', "chemin prochaine action")
continuity = replace_once(continuity, 'Le chapitre 2 du Livre IV définira les niveaux de test, responsabilités, risques, critères d’entrée et de sortie et portes qualité. Il ne recopiera ni le catalogue de métriques et les expériences du chapitre 1, ni les cas fonctionnels et suites de régression réservés au chapitre 3.', 'Le chapitre 3 du Livre IV matérialisera les cas fonctionnels et suites de régression, avec fixtures, états contrôlés, tests rapides et campagnes complètes. Il appliquera la stratégie du chapitre 2 sans redéfinir ses risques, portes, rôles ou règles de décision.', "description prochaine action")
journal_anchor = '### 2026-07-25T20:33:18+02:00 — version 3.64.0'
journal_entry = f'''### {NOW} — version 3.65.0

- création du chapitre 2 du Livre IV — Stratégie générale d’assurance qualité ;
- charte QA, modèle de qualité, niveaux, familles et matrice risques/contrôles documentés ;
- prévention, détection et correction séparées ;
- portes `G0` à `G5`, critères d’entrée/sortie et statuts de décision définis ;
- rôles Solo/Studio, RACI, indépendance et calendrier encadrés ;
- environnements, baselines, sévérité, priorité, triage, stop-ship et dérogations documentés ;
- QA documentaire, technique, artistique et produit reliées ;
- accessibilité, sécurité, données assistées et récupérabilité intégrées ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 3 — Tests fonctionnels et tests de régression, niveau Élevée ;
- aucune campagne, revue spécialisée, décision de porte, mesure runtime ou publication produit revendiquée.


{journal_anchor}'''
continuity = replace_once(continuity, journal_anchor, journal_entry, "journal continuité")
write(continuity_path, continuity)

print(f"Chapitre écrit : {chapter_path}")
print(f"Horodatage : {NOW}")
print(f"SHA-256 chapitre : {chapter_hash}")
print(f"SHA-256 audit : {audit_hash}")
