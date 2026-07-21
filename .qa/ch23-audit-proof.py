from pathlib import Path
import json
ROOT=Path('.')
AUDIT=ROOT/'Livre-II/QA/AUDIT-CHAPITRE-23.md'
PROOF=ROOT/'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-23.yaml'
def write(path,text):
 path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding='utf-8',newline='\n')
m=json.loads(Path('.qa/ch23-metrics.json').read_text(encoding='utf-8'))
stamp=m['stamp']; date=m['date']; lines=m['lines']; headings=[None]*m['headings']; blocks=m['blocks']; markers=m['markers']; error_cases=m['error_cases']; faulty=m['faulty']; corrected=m['corrected']

audit = f'''---
title: "Audit du Livre II — Chapitre 23"
id: "DOC-L2-QA-AUDIT-CH23"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH23"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "{stamp}"
last-verified: "{stamp}"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 23 — Politique, factions et justice

## 1. Porte de brouillon

Le chapitre a été matérialisé sur la branche dédiée `docs/livre-ii-ch23-politique-factions-justice` et dans la pull request en brouillon #54. La seconde lecture a précédé le passage de la version `0.9.0` à `1.0.0`.

## 2. Résultats

- lignes finales : **{lines}** ;
- titres Markdown : **{len(headings)}** ;
- blocs de code ou de données : **{blocks}** ;
- marqueurs d’explication : **{markers}** ;
- cas d’erreurs détaillés : **{error_cases}** ;
- contre-exemples expliqués : **{faulty}** ;
- corrections expliquées : **{corrected}** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre couvre institutions, factions, rangs, fonctions, adhésions, mandats, lois versionnées, juridictions, droits, autorisations explicables, infractions rapportées, événements causaux, preuves, chaîne de garde, dossiers, enquêtes, verdicts, sanctions coordonnées et persistance.

Les frontières sont respectées :

- les personnages conservent les identités et états individuels ;
- les relations et familles ne créent aucun droit politique implicite ;
- l’inventaire conserve propriété, garde et transferts d’objets ;
- l’économie conserve portefeuilles, écritures et amendes préparées ;
- l’écologie conserve régions, populations et ressources ;
- les domaines et bâtiments restent réservés au chapitre 24 ;
- les quêtes et conséquences narratives restent réservées au chapitre 25.

## 4. Corrections issues de la seconde lecture

La seconde lecture a notamment :

1. exigé un titulaire valide pour tout mandat actif ;
2. exigé un titulaire vide pour tout siège vacant ;
3. recoupé les rangs des adhésions avec la définition de faction ;
4. recoupé institution et fonction des mandats avec la faction ;
5. aligné le retour du décodeur de sections sur la sentinelle `null` documentée ;
6. supprimé vingt en-têtes génériques redondants dans les exemples fautifs et corrigés ;
7. conservé les résultats idempotents, révisions et événements après commit ;
8. confirmé qu’une accusation ne produit ni verdict ni sanction ;
9. confirmé que les sanctions externes sont préparées par leurs autorités ;
10. confirmé la restauration globale avant remplacement.

## 5. Revue statique du code

Les extraits ont été relus pour les signatures, types, paramètres, retours, sentinelles, codes `Error`, copies détachées, bornes, intervalles, révisions, idempotence, juridictions, priorités, chaîne de garde et émissions après commit.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques

Les **{blocks}** blocs possèdent chacun un marqueur `<!-- qa:code-explanation -->` et une explication proportionnée. Les sections d’erreurs utilisent directement `Pourquoi cet exemple est fautif` et `Pourquoi la correction fonctionne`.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`. Chacun des dix cas contient un symptôme, un exemple fautif expliqué et un exemple corrigé expliqué.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les contrats, flux, structures et contre-exemples utilisent `[LECTURE]`. Aucune procédure éditoriale ou commande de workflow n’est placée dans le texte lecteur.

## 9. Sources et exactitude technique

Les références moteur visent les pages officielles Godot 4.7 pour `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Time` et GDScript. Les dépendances internes renvoient aux chapitres 9, 14 à 17 et 20 à 22.

## 10. Clôture éditoriale

La dernière section synthétise les décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les collections typées n’ont pas été vérifiées au runtime ;
- le commit multi-autorités n’a pas été exécuté ;
- les performances aux bornes n’ont pas été mesurées ;
- les adaptateurs de juridiction et de sanctions n’ont pas été matérialisés ;
- la scène pédagogique n’a pas été instanciée ;
- le codec et la restauration n’ont pas été exécutés ;
- la reproductibilité interplateforme n’a pas été vérifiée ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 23 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
'''
write(AUDIT, audit)

proof = f'''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH23
status: pending
validation-date: {date}
validated-base-commit: null
validated-head-commit: null
evidence-closure:
  commit: null
  conclusion: pending
chapter:
  id: DOC-L2-CH23
  path: Livre-II/CHAPITRE-23-Politique-factions-et-justice.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: null
  warnings: null
  chapter-lines: {lines}
  chapter-headings: {len(headings)}
  chapter-code-and-data-blocks: {blocks}
  code-explanation-markers: {markers}
  detailed-error-cases: {error_cases}
  faulty-examples-explained: {faulty}
  corrected-examples-explained: {corrected}
  duplicate-headings: 0
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  project-asteria-final-synthesis: true
  stable-political-identities: true
  versioned-laws: true
  deny-by-default-authorization: true
  accusation-distinct-from-verdict: true
  evidence-chain-of-custody: true
  idempotent-political-commands: true
  multi-authority-sanction-commit: true
  save-prepared-before-replacement: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: null
    conclusion: pending
  validate-usage-contexts:
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
reservations:
  - Godot parser not executed.
  - Typed collections not runtime-verified.
  - Multi-authority sanction commit not run.
  - Large-scale performance not measured.
  - Jurisdiction and sanction adapters not materialized.
  - Demo scene not instantiated.
  - Save restoration not executed.
  - Cross-platform replay not verified.
  - PDF deferred until end of Livre II.
'''
write(PROOF, proof)
