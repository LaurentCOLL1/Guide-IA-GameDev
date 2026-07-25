---
title: "Livre IV — Chapitre 2 : Stratégie générale d’assurance qualité"
id: "DOC-L4-CH02"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 2
last-verified: "2026-07-25T21:06:09+02:00"
audit-status: "complete"
audit-date: "2026-07-25T21:06:09+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-02.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Stratégie générale d’assurance qualité

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L4-CH02`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence héritées :** Godot `4.7.1-stable`, CPython `3.14.6` avec repli `3.13.14`, GDScript, Forward+

## 1. Rôle du chapitre

L’assurance qualité ne se résume pas à chercher des anomalies juste avant une livraison. Elle organise la manière dont une équipe prévient les défauts, détecte les écarts, décide quoi corriger, conserve les preuves et accepte consciemment les risques résiduels.

Ce chapitre définit la stratégie générale de `Project Asteria`. Il répond à six questions :

1. quelles qualités le produit doit-il préserver ;
2. quels risques menacent ces qualités ;
3. quelles activités réduisent chaque risque ;
4. qui possède la décision ;
5. quelles preuves sont exigées avant de franchir une porte ;
6. quelles conditions imposent un arrêt, un report, une dérogation ou un retour arrière.

La stratégie ne remplace pas les cas de test. Elle fournit le cadre dans lequel les cas fonctionnels, les suites de régression, les diagnostics, les revues artistiques, les contrôles de sécurité et les validations produit seront créés dans les chapitres suivants.

> **[LECTURE] Boucle générale d’assurance qualité — Ne pas saisir.**

```text
intention produit
    ↓
risques explicites
    ↓
prévention
    ↓
détection
    ↓
preuves et écarts
    ↓
correction ou acceptation documentée
    ↓
porte qualité
    ├── PASS
    ├── PASS_WITH_RESERVATIONS
    ├── HOLD
    └── REJECT
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** l’intention produit précède le choix des contrôles.
- **Risque :** chaque activité QA doit réduire un risque nommé ou vérifier une exigence.
- **Décision :** la porte ne dépend pas d’un score unique ; elle consomme des preuves et des réserves.
- **Sorties :** les quatre statuts distinguent acceptation, acceptation conditionnelle, attente et refus.
- **Invariant :** aucun outil automatique ne s’attribue seul l’autorité de publier le produit.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer qualité, assurance qualité, contrôle qualité et test ;
- relier les qualités du produit aux risques et aux preuves ;
- séparer prévention, détection et correction ;
- définir des niveaux de test sans écrire prématurément les cas détaillés ;
- construire une matrice risques/contrôles ;
- définir des critères d’entrée et de sortie vérifiables ;
- créer des portes qualité avec statuts, propriétaires et règles d’escalade ;
- organiser les responsabilités en modes Solo et Studio ;
- distinguer sévérité, priorité, probabilité, impact et détectabilité ;
- encadrer les dérogations, réserves et dates d’expiration ;
- produire un calendrier QA proportionné au projet ;
- conserver une chaîne de preuve traçable sans transformer les indicateurs en objectifs artificiels.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les chartes, matrices, schémas, commandes et scripts sont des modèles pédagogiques. Aucune campagne produit, revue artistique, analyse de sécurité, session d’accessibilité, répétition de restauration, test de charge ou décision de publication de `Project Asteria` n’est revendiquée comme exécutée.

> **[LECTURE] État de preuve du chapitre — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  qa_charter_materialized: false
  risk_register_materialized: false
  gate_policy_executed: false
  functional_campaign_executed: false
  artistic_review_executed: false
  security_review_executed: false
  accessibility_review_executed: false
  recovery_drill_executed: false
  release_decision_approved: false
  runtime_claims: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `static_review` atteste une revue documentaire et technique des modèles.
- **Séparation :** chaque famille de validation possède son propre indicateur de matérialisation.
- **Décision :** aucune publication n’est présentée comme approuvée.
- **Réserves :** les valeurs `false` empêchent de confondre stratégie écrite et campagne réellement conduite.
- **Limite :** une future preuve d’exécution devra citer l’environnement, la version, les résultats et le responsable.

## 4. Prérequis et frontières

Le lecteur doit connaître :

- l’architecture feature-first et les frontières d’autorité du Livre II ;
- les événements typés, les services injectés et les données versionnées ;
- les tests unitaires, d’intégration et simulations du Livre II, chapitre 27 ;
- la journalisation et la reproductibilité du Livre II, chapitre 28 ;
- l’automatisation Python du Livre II, chapitre 29 ;
- l’équilibrage et la télémétrie locale du Livre IV, chapitre 1.

Le chapitre couvre :

- le modèle de qualité ;
- les risques ;
- les responsabilités ;
- les niveaux et familles de validation ;
- les portes qualité ;
- les critères d’entrée et de sortie ;
- les dérogations ;
- le calendrier ;
- les rapports de synthèse et de décision.

Il ne couvre pas :

- le catalogue de métriques d’équilibrage du chapitre 1 ;
- les cas de test, fixtures, scènes et suites de régression du chapitre 3 ;
- la reproduction détaillée des anomalies du chapitre 4 ;
- la politique complète de logs, métriques et traces du chapitre 5 ;
- le profilage CPU, GPU, mémoire ou chargement des chapitres 6 à 9 ;
- la sécurité réseau détaillée du chapitre 13 ;
- les procédures de déploiement du chapitre 14 ;
- les contrôles propres à une plateforme de distribution du chapitre 17.

> **Frontière essentielle :** ce chapitre décide **quels risques doivent être couverts, par qui et avant quelle porte**. Les chapitres suivants décident **comment exécuter les validations spécialisées**.

## 5. Vocabulaire opérationnel

La **qualité** est l’aptitude du produit à satisfaire des besoins explicites et implicites dans un contexte donné.

L’**assurance qualité** organise les activités qui donnent confiance dans le processus et le produit : standards, revues, critères, contrôles, responsabilités et preuves.

Le **contrôle qualité** examine un résultat pour détecter un écart : build, scène, asset, rapport, configuration ou comportement.

Un **test** exécute ou évalue un objet selon des entrées et des attentes définies.

Une **revue** examine un artefact sans nécessairement exécuter le produit.

Un **risque qualité** relie une cause possible à une conséquence sur le joueur, l’équipe, le produit, les données, la sécurité ou la réputation.

Une **porte qualité** est une décision formelle entre deux phases. Elle ne se réduit pas à un voyant de pipeline.

Un **critère d’entrée** doit être vrai avant de commencer une phase. Un **critère de sortie** doit être démontré avant de la fermer.

Une **preuve** est un artefact consultable : rapport, journal, capture, manifeste, résultat signé, empreinte, décision ou lien vers une exécution.

Une **réserve** décrit une limite connue qui n’empêche pas nécessairement l’usage prévu.

Une **dérogation** autorise temporairement un écart à une règle, avec propriétaire, justification, portée et expiration.

La **sévérité** décrit l’effet d’un défaut. La **priorité** décrit l’ordre choisi pour le traiter. Elles peuvent différer.

## 6. Charte QA de Project Asteria

La charte transforme les intentions générales en engagements stables. Elle ne contient pas de cas de test : elle décrit les qualités, autorités et règles de décision.

> **[VSC] Visual Studio Code — Créer `config/qa/qa-charter.v1.yaml`.**

```yaml
qa_charter:
  schema_version: 1
  charter_id: AST-QA-CHARTER-001
  product: Project Asteria
  principles:
    - risk_based
    - evidence_before_decision
    - prevention_before_rework
    - reproducibility
    - least_privilege
    - accessibility_by_design
    - rollback_preserved
  decision_authority:
    release: product_owner
    security_exception: security_owner
    accessibility_exception: accessibility_owner
    technical_gate: technical_lead
    artistic_gate: art_direction
  forbidden_shortcuts:
    - automatic_release_from_single_score
    - undocumented_waiver
    - mutable_approved_evidence
    - production_data_as_default_fixture
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la charte possède un identifiant et une version de schéma.
- **Principes :** chaque valeur décrit une règle durable, pas un résultat de campagne.
- **Autorités :** les décisions sont attribuées à des rôles distincts.
- **Interdictions :** les raccourcis empêchent une promotion automatique ou une preuve modifiée après approbation.
- **Effet de bord :** le fichier ne lance aucun contrôle ; il configure la gouvernance.

## 7. Construire un modèle de qualité

Un modèle de qualité transforme « le jeu doit être bon » en dimensions observables. `Project Asteria` retient neuf dimensions :

| Dimension | Question directrice | Exemple de risque |
|---|---|---|
| adéquation fonctionnelle | le produit réalise-t-il les fonctions attendues ? | progression bloquée |
| fiabilité | reste-t-il cohérent dans le temps ? | sauvegarde corrompue |
| performance | respecte-t-il les budgets définis ? | saccades dans une zone critique |
| utilisabilité | les actions sont-elles compréhensibles ? | objectif illisible |
| accessibilité | l’expérience reste-t-elle praticable avec des besoins variés ? | information transmise uniquement par couleur |
| sécurité | les actifs, services et données sont-ils protégés ? | autorité réseau contournée |
| compatibilité | les configurations prises en charge restent-elles fonctionnelles ? | contrôleur non reconnu |
| maintenabilité | une modification peut-elle être comprise et vérifiée ? | dépendance cachée |
| récupérabilité | le produit et ses données peuvent-ils revenir à un état sûr ? | migration irréversible |

Le modèle ne promet pas une perfection uniforme. Il aide à déclarer les qualités critiques par fonctionnalité et par phase.

> **[LECTURE] Profil de qualité du produit — Ne pas saisir.**

```yaml
quality_profile:
  id: AST-QUALITY-PROFILE-001
  dimensions:
    functional_suitability:
      criticality: critical
      owner: product_design
    reliability:
      criticality: critical
      owner: technical_lead
    performance:
      criticality: high
      owner: performance_owner
    usability:
      criticality: high
      owner: ux_owner
    accessibility:
      criticality: high
      owner: accessibility_owner
    security:
      criticality: critical
      owner: security_owner
    compatibility:
      criticality: medium
      owner: platform_owner
    maintainability:
      criticality: high
      owner: technical_lead
    recoverability:
      criticality: critical
      owner: operations_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clés :** les dimensions utilisent des identifiants stables indépendants des libellés d’interface.
- **Criticité :** elle représente l’importance stratégique, pas le résultat d’un test.
- **Propriété :** chaque dimension possède un rôle responsable de sa couverture.
- **Usage :** les risques et portes référencent ce profil au lieu de recréer leurs propres catégories.
- **Limite :** la criticité peut varier selon un mode de jeu ou une plateforme ; une nouvelle version du profil documente ce changement.

## 8. Séparer prévention, détection et correction

Trois activités peuvent viser le même risque sans être interchangeables.

- **Prévention :** architecture, conventions, validation de données, revue de conception, budgets et permissions minimales.
- **Détection :** tests, analyses statiques, revues, instrumentation, playtests et inspections.
- **Correction :** patch, migration, retour arrière, désactivation, restauration et communication.

Une stratégie qui ne prévoit que la détection découvre les défauts tard. Une stratégie qui ne prévoit que la prévention suppose à tort que les règles seront toujours respectées.

> **[LECTURE] Couverture en trois couches — Ne pas saisir.**

```yaml
risk_control_layers:
  risk_id: AST-RISK-SAVE-CORRUPTION-001
  prevention:
    - versioned_save_schema
    - atomic_write
    - migration_review
  detection:
    - compatibility_campaign
    - corrupted_fixture_campaign
    - restore_verification
  correction:
    - backup_restore
    - migration_rollback
    - affected_build_withdrawal
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Risque :** les trois listes répondent à une même identité.
- **Prévention :** les contrôles réduisent la probabilité avant exécution.
- **Détection :** les campagnes cherchent les écarts résiduels.
- **Correction :** les actions limitent l’impact après découverte.
- **Invariant :** une couche vide sur un risque critique exige une justification explicite.

## 9. Définir les niveaux de validation

Les niveaux décrivent l’échelle à laquelle une preuve est recherchée. Ils ne prescrivent pas encore les cas précis.

| Niveau | Objet principal | Décision préparée |
|---|---|---|
| composant | fonction, classe, ressource isolée | le contrat local tient-il ? |
| intégration | collaboration entre systèmes | les frontières et formats sont-ils compatibles ? |
| système | build jouable complet | les parcours et qualités globales tiennent-ils ? |
| acceptation | besoin produit et public visé | le résultat est-il acceptable pour l’usage prévu ? |
| exploitation | installation, mise à jour, restauration | le produit peut-il être opéré et récupéré ? |

Les tests unitaires du Livre II restent au niveau composant. Le chapitre 3 organisera les cas fonctionnels et les suites de non-régression à travers ces niveaux.

> **[LECTURE] Politique des niveaux — Ne pas saisir.**

```yaml
validation_levels:
  component:
    default_owner: feature_owner
    evidence_kind: automated_result
  integration:
    default_owner: technical_qa
    evidence_kind: integration_report
  system:
    default_owner: product_qa
    evidence_kind: campaign_report
  acceptance:
    default_owner: product_owner
    evidence_kind: signed_decision
  operations:
    default_owner: operations_owner
    evidence_kind: recovery_report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** chaque clé représente une échelle de validation.
- **Propriétaire :** le rôle par défaut peut être remplacé dans un plan de campagne versionné.
- **Preuve :** `evidence_kind` annonce la forme attendue sans inventer un résultat.
- **Séparation :** une réussite au niveau composant ne remplace pas l’acceptation produit.
- **Extension :** un projet multijoueur peut ajouter des validations d’infrastructure sans modifier la signification des niveaux existants.

## 10. Organiser les familles de contrôle

Une même porte peut consommer plusieurs familles :

- revue documentaire ;
- analyse statique ;
- test automatisé ;
- test manuel reproductible ;
- simulation ;
- playtest ;
- revue artistique ;
- revue d’accessibilité ;
- revue de sécurité ;
- contrôle de compatibilité ;
- exercice de restauration ;
- inspection de conformité de distribution.

La famille décrit la méthode générale. Le cas précis, ses entrées et ses résultats appartiennent aux campagnes spécialisées.

> **[LECTURE] Catalogue des familles — Ne pas saisir.**

```yaml
control_families:
  documentary_review:
    executes_product: false
    human_judgment: true
  static_analysis:
    executes_product: false
    human_judgment: false
  automated_test:
    executes_product: true
    human_judgment: false
  manual_test:
    executes_product: true
    human_judgment: true
  artistic_review:
    executes_product: true
    human_judgment: true
  security_review:
    executes_product: variable
    human_judgment: true
  recovery_drill:
    executes_product: true
    human_judgment: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exécution :** `executes_product` distingue revue de texte et comportement runtime.
- **Jugement :** certaines familles produisent une mesure, d’autres exigent une appréciation humaine.
- **Variable :** une revue de sécurité peut combiner analyse statique, inspection et exécution contrôlée.
- **Usage :** le registre des risques choisit une ou plusieurs familles appropriées.
- **Limite :** la présence d’un humain ne dispense pas de critères ni de preuves.

## 11. Décrire un risque qualité

Un risque utile décrit un événement redouté, une cause, une conséquence, une population affectée et un propriétaire. « La sauvegarde » n’est pas un risque ; « une migration rend une sauvegarde antérieure illisible sans restauration possible » en est un.

> **[VSC] Visual Studio Code — Créer `config/qa/risk-register.v1.yaml`.**

```yaml
risk_register:
  schema_version: 1
  register_id: AST-QA-RISKS-001
  risks:
    - id: AST-RISK-SAVE-MIGRATION-001
      quality_dimension: recoverability
      statement: "Une migration rend une sauvegarde prise en charge illisible."
      causes:
        - unversioned_schema_change
        - partial_migration
      consequences:
        - player_progress_loss
        - support_incident
      affected_population:
        - returning_players
      likelihood: possible
      impact: catastrophic
      detectability: difficult
      owner: save_system_owner
      status: open
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Énoncé :** le risque décrit un événement et non un thème.
- **Causes :** elles orientent les mesures de prévention.
- **Conséquences :** elles justifient l’impact attribué.
- **Population :** elle empêche d’oublier un groupe affecté.
- **Statuts :** `open` signifie que la couverture et le risque résiduel doivent encore être décidés.

## 12. Évaluer probabilité, impact et détectabilité

Une multiplication brute de notes ordinales donne une apparence de précision. Le chapitre utilise plutôt une grille déclarée :

- probabilité : `rare`, `unlikely`, `possible`, `likely`, `almost_certain` ;
- impact : `minor`, `moderate`, `major`, `critical`, `catastrophic` ;
- détectabilité avant dommage : `easy`, `moderate`, `difficult`, `very_difficult`.

Le classement final est dérivé par une table versionnée. Un impact catastrophique ne devient jamais faible uniquement parce que la probabilité paraît rare.

> **[LECTURE] Politique de classement — Ne pas saisir.**

```yaml
risk_policy:
  id: AST-QA-RISK-POLICY-001
  rules:
    - when:
        impact: catastrophic
      classification: critical
    - when:
        impact: critical
        likelihood_in: [possible, likely, almost_certain]
      classification: critical
    - when:
        impact: major
        detectability_in: [difficult, very_difficult]
      classification: high
    - default: medium
  manual_override:
    allowed: true
    requires:
      - rationale
      - owner
      - review_date
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** la première règle applicable détermine la classification.
- **Conservatisme :** un impact catastrophique reste critique.
- **Détectabilité :** un défaut difficile à voir avant dommage augmente la priorité de couverture.
- **Dérogation :** un classement manuel est permis, mais il laisse une justification et une date de revue.
- **Limite :** la politique priorise l’attention ; elle ne calcule pas une probabilité scientifique.

## 13. Prioriser sans confondre risque et effort

La priorité de traitement dépend :

- de la classification du risque ;
- de l’échéance de la porte ;
- de la disponibilité d’une mesure de réduction ;
- du coût de retard ;
- des dépendances ;
- du risque créé par la correction elle-même.

Un contrôle peu coûteux sur un risque moyen peut être réalisé avant une campagne chère sur un risque élevé, sans que le risque moyen devienne plus important.

> **[LECTURE] File de travail QA — Ne pas saisir.**

```yaml
qa_work_item:
  id: AST-QA-WORK-017
  risk_id: AST-RISK-SAVE-MIGRATION-001
  risk_classification: critical
  control_kind: recovery_drill
  estimated_effort_days: 2
  gate_deadline: G3_RELEASE_CANDIDATE
  dependencies:
    - save_migration_fixture_ready
  priority: P0
  priority_rationale: "Risque critique et preuve exigée avant le candidat."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** l’élément de travail référence le risque, il ne le remplace pas.
- **Effort :** l’estimation aide à planifier sans réduire la criticité.
- **Porte :** l’échéance explique quand la preuve doit exister.
- **Dépendances :** elles rendent les blocages visibles.
- **Justification :** `priority_rationale` évite une priorité arbitraire.

## 14. Construire une matrice risques/contrôles

La matrice répond à la question de validation du chapitre : chaque risque critique possède-t-il une couverture explicite ?

> **[VSC] Visual Studio Code — Créer `config/qa/risk-control-matrix.v1.yaml`.**

```yaml
risk_control_matrix:
  schema_version: 1
  matrix_id: AST-QA-RISK-CONTROLS-001
  rows:
    - risk_id: AST-RISK-SAVE-MIGRATION-001
      classification: critical
      prevention_controls:
        - AST-CTRL-SAVE-SCHEMA-REVIEW-001
      detection_controls:
        - AST-CTRL-SAVE-COMPATIBILITY-CAMPAIGN-001
        - AST-CTRL-SAVE-RESTORE-DRILL-001
      correction_controls:
        - AST-CTRL-SAVE-ROLLBACK-001
      gate_ids:
        - G2_INTEGRATION
        - G3_RELEASE_CANDIDATE
      owner: save_system_owner
      residual_risk_decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ligne :** une ligne rassemble les couches de contrôle d’un risque.
- **Identifiants :** les contrôles sont référencés sans détailler encore leurs cas.
- **Portes :** elles indiquent quand la couverture est consommée.
- **Propriété :** un rôle répond de la complétude et du risque résiduel.
- **Décision :** `pending` interdit de présenter le risque comme accepté.

## 15. Définir le cycle de vie des portes

`Project Asteria` utilise six portes :

| Porte | Transition | Objet |
|---|---|---|
| `G0_SCOPE` | idée → travail autorisé | besoin, risques initiaux, propriétaire |
| `G1_CHANGE_READY` | implémentation → revue | code, données, assets et documentation prêts à examiner |
| `G2_INTEGRATION` | branche → intégration | compatibilité avec la base commune |
| `G3_RELEASE_CANDIDATE` | intégration → candidat | couverture des risques critiques et stabilité |
| `G4_RELEASE` | candidat → publication | décision produit, risques résiduels, retour arrière |
| `G5_POST_RELEASE` | publication → exploitation | santé, incidents, apprentissages et actions |

Les noms sont stables. Les critères peuvent évoluer par version de politique.

> **[LECTURE] Catalogue des portes — Ne pas saisir.**

```yaml
quality_gates:
  policy_id: AST-QA-GATES-001
  gates:
    G0_SCOPE:
      decision_owner: product_owner
    G1_CHANGE_READY:
      decision_owner: feature_owner
    G2_INTEGRATION:
      decision_owner: technical_lead
    G3_RELEASE_CANDIDATE:
      decision_owner: product_qa
    G4_RELEASE:
      decision_owner: product_owner
    G5_POST_RELEASE:
      decision_owner: operations_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catalogue :** la politique centralise les identités des portes.
- **Autorité :** chaque transition possède un décideur.
- **Séparation :** le propriétaire de la porte peut consulter plusieurs spécialistes.
- **Version :** modifier un propriétaire crée une nouvelle révision de politique.
- **Limite :** ce catalogue ne contient pas encore les critères détaillés.


## 16. Écrire des critères d’entrée

Un critère d’entrée doit être observable avant la phase. « Le projet est prêt » est inutilisable. « Le build candidat porte un identifiant immuable et son manifeste est disponible » est vérifiable.

> **[LECTURE] Critères d’entrée de `G3_RELEASE_CANDIDATE` — Ne pas saisir.**

```yaml
gate_entry_criteria:
  gate_id: G3_RELEASE_CANDIDATE
  criteria:
    - id: AST-G3-ENTRY-BUILD-001
      statement: "Un build candidat immuable et identifié est disponible."
      evidence_kind: build_manifest
    - id: AST-G3-ENTRY-RISKS-001
      statement: "Le registre des risques est à jour."
      evidence_kind: signed_risk_register
    - id: AST-G3-ENTRY-SCOPE-001
      statement: "La portée fonctionnelle est gelée ou chaque exception est approuvée."
      evidence_kind: scope_decision
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque critère peut être référencé dans un rapport.
- **Phrase :** le verbe et l’objet rendent l’état vérifiable.
- **Preuve :** `evidence_kind` annonce ce qui doit être consultable.
- **Gel :** une exception de portée reste possible, mais elle exige une décision.
- **Invariant :** la phase ne commence pas lorsqu’un critère obligatoire est inconnu.

## 17. Écrire des critères de sortie

Un critère de sortie décrit ce qui doit être démontré. Il ne doit pas dépendre d’une impression générale.

> **[LECTURE] Critères de sortie de `G3_RELEASE_CANDIDATE` — Ne pas saisir.**

```yaml
gate_exit_criteria:
  gate_id: G3_RELEASE_CANDIDATE
  criteria:
    - id: AST-G3-EXIT-CRITICAL-RISKS-001
      statement: "Chaque risque critique possède prévention, détection, correction et décision résiduelle."
      evidence_kind: risk_control_matrix
    - id: AST-G3-EXIT-STOP-SHIP-001
      statement: "Aucun défaut stop-ship ouvert ne cible le build candidat."
      evidence_kind: defect_snapshot
    - id: AST-G3-EXIT-RECOVERY-001
      statement: "Le chemin de retour arrière prévu est documenté et vérifiable."
      evidence_kind: rollback_plan
    - id: AST-G3-EXIT-REPORT-001
      statement: "Le rapport de porte cite toutes les réserves ouvertes."
      evidence_kind: gate_report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** le premier critère exige les trois couches et une décision résiduelle.
- **Blocage :** la photographie des défauts est liée au build.
- **Récupération :** le retour arrière est exigé avant la promotion.
- **Transparence :** les réserves ne disparaissent pas du rapport.
- **Limite :** les preuves détaillées seront produites par les campagnes concernées.

## 18. Représenter le statut d’une porte

Les statuts sont :

- `PASS` : tous les critères obligatoires sont satisfaits ;
- `PASS_WITH_RESERVATIONS` : les écarts autorisés sont couverts par des dérogations valides ;
- `HOLD` : une preuve manque ou une dépendance empêche la décision ;
- `REJECT` : un critère bloquant échoue ou le risque résiduel est inacceptable.

> **[LECTURE] Décision de porte — Ne pas saisir.**

```yaml
gate_decision:
  id: AST-GATE-DECISION-G3-004
  gate_id: G3_RELEASE_CANDIDATE
  subject_build: AST-BUILD-0.8.0-RC4
  status: HOLD
  decided_at: "<timestamp>"
  decision_owner: product_qa
  satisfied_criteria:
    - AST-G3-ENTRY-BUILD-001
    - AST-G3-ENTRY-RISKS-001
  missing_evidence:
    - AST-CTRL-SAVE-RESTORE-DRILL-001
  active_waivers: []
  rationale: "La preuve de restauration du build candidat manque."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sujet :** la décision vise un build précis.
- **Temps :** l’horodatage empêche de réutiliser silencieusement une décision ancienne.
- **État :** `HOLD` distingue l’attente d’un refus définitif.
- **Preuve manquante :** l’identité permet de retrouver le contrôle attendu.
- **Autorité :** le propriétaire signe la décision et sa justification.

## 19. Conserver une chaîne de preuve

Une chaîne de preuve relie :

1. besoin ou risque ;
2. contrôle ;
3. exécution ou revue ;
4. résultat ;
5. défaut éventuel ;
6. décision ;
7. version du produit.

Une capture isolée sans build, scénario ni auteur est une illustration, pas une preuve suffisante.

> **[LECTURE] Manifeste de preuve — Ne pas saisir.**

```yaml
evidence_manifest:
  id: AST-QA-EVIDENCE-G3-004
  subject_build: AST-BUILD-0.8.0-RC4
  source_revision: "<git-commit>"
  environment_profile: AST-ENV-WINDOWS-DX12-001
  items:
    - control_id: AST-CTRL-SAVE-RESTORE-DRILL-001
      execution_id: AST-QA-RUN-RESTORE-042
      result: FAIL
      artifact_sha256: "<sha256>"
      defect_ids:
        - AST-DEFECT-184
  immutable_after_approval: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sujet :** build et révision lient la preuve au produit.
- **Environnement :** le profil évite une généralisation hors configuration.
- **Résultat :** `FAIL` est conservé avec le défaut correspondant.
- **Intégrité :** l’empreinte permet de détecter une modification de l’artefact.
- **Immutabilité :** une correction crée une nouvelle exécution, elle ne réécrit pas l’historique approuvé.

## 20. Gérer la traçabilité

La traçabilité doit être suffisante pour répondre à trois questions :

- pourquoi ce contrôle existe-t-il ;
- sur quelle version a-t-il été appliqué ;
- quelle décision a-t-il influencée ?

Elle n’exige pas de relier chaque ligne de code à chaque test. La granularité suit le risque.

> **[LECTURE] Lien de traçabilité — Ne pas saisir.**

```yaml
trace_link:
  requirement_id: AST-REQ-SAVE-COMPATIBILITY-001
  risk_ids:
    - AST-RISK-SAVE-MIGRATION-001
  control_ids:
    - AST-CTRL-SAVE-COMPATIBILITY-CAMPAIGN-001
    - AST-CTRL-SAVE-RESTORE-DRILL-001
  evidence_ids:
    - AST-QA-EVIDENCE-G3-004
  gate_decision_ids:
    - AST-GATE-DECISION-G3-004
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exigence :** elle explique le besoin produit.
- **Risques :** ils justifient la profondeur de couverture.
- **Contrôles :** ils décrivent les moyens choisis.
- **Preuves :** elles montrent les résultats obtenus.
- **Décisions :** elles enregistrent l’effet réel sur la progression du produit.

## 21. Définir les rôles en mode Solo

En Solo, une seule personne peut cumuler les rôles, mais elle ne doit pas fusionner mentalement leurs décisions.

Le développeur Solo utilise des changements de posture :

1. **auteur** : produit le changement ;
2. **relecteur** : vérifie critères et risques après une pause ;
3. **opérateur** : exécute les contrôles sans modifier les attentes ;
4. **décideur** : relit les preuves et accepte le risque résiduel ;
5. **archiviste** : conserve les manifestes et réserves.

Un délai ou une session séparée réduit le biais de confirmation.

> **[LECTURE] Séparation temporelle en Solo — Ne pas saisir.**

```yaml
solo_qa_roles:
  change_id: AST-CHANGE-042
  author_session: 2026-07-20
  review_session: 2026-07-21
  evidence_session: 2026-07-22
  decision_session: 2026-07-22
  same_person: true
  expectations_frozen_before_evidence: true
  unresolved_risks_relisted_before_decision: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sessions :** les dates matérialisent les changements de posture.
- **Identité :** `same_person` ne prétend pas à une indépendance organisationnelle.
- **Gel :** les attentes sont figées avant de voir les résultats.
- **Rappel :** les risques non résolus sont relus au moment de décider.
- **Limite :** un risque de sécurité ou juridique élevé peut exiger une revue externe malgré le mode Solo.

## 22. Définir les rôles en mode Studio

En Studio, les responsabilités principales sont :

- propriétaire produit ;
- responsable QA produit ;
- responsable technique ;
- propriétaires de fonctionnalités ;
- QA technique ;
- direction artistique ;
- responsable accessibilité ;
- responsable sécurité ;
- responsable plateformes ;
- responsable exploitation ;
- gestionnaire de publication.

Une matrice RACI aide à distinguer :

- `R` : réalise ;
- `A` : répond de la décision ;
- `C` : est consulté ;
- `I` : est informé.

> **[LECTURE] Extrait de matrice RACI — Ne pas saisir.**

```yaml
raci:
  activity: G3_RELEASE_CANDIDATE
  roles:
    product_qa: A
    technical_qa: R
    technical_lead: C
    art_direction: C
    accessibility_owner: C
    security_owner: C
    product_owner: I
    operations_owner: I
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unicité :** une activité possède idéalement un seul rôle `A`.
- **Réalisation :** plusieurs rôles peuvent être `R` lorsque les contrôles sont répartis.
- **Consultation :** les spécialistes évaluent leurs domaines.
- **Information :** les rôles concernés reçoivent la décision sans la signer.
- **Limite :** la matrice ne remplace pas les compétences ni les disponibilités réelles.

## 23. Choisir le niveau d’indépendance

L’indépendance réduit le biais, mais augmente le coût de coordination. Le niveau dépend du risque :

| Risque | Indépendance minimale suggérée |
|---|---|
| faible et local | auteur avec checklist |
| moyen | relecture par un pair |
| élevé | spécialiste distinct |
| critique | spécialiste distinct et décideur séparé |

Une personne indépendante n’est pas automatiquement compétente. La stratégie exige les deux : distance suffisante et expertise adaptée.

## 24. Construire un calendrier QA

Le calendrier ne repousse pas toute validation à la fin. Il place les activités au moment où elles coûtent le moins cher et produisent une décision utile.

> **[VSC] Visual Studio Code — Créer `config/qa/qa-calendar.v1.yaml`.**

```yaml
qa_calendar:
  calendar_id: AST-QA-CALENDAR-001
  cadences:
    per_change:
      - scope_risk_review
      - static_checks
      - focused_validation
    daily_integration:
      - integration_smoke
      - defect_triage
    weekly:
      - risk_register_review
      - artistic_consistency_review
      - accessibility_backlog_review
    per_milestone:
      - system_campaign
      - recovery_drill
      - compatibility_matrix
    per_release_candidate:
      - critical_risk_coverage_review
      - gate_G3
    per_release:
      - gate_G4
      - rollback_readiness_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cadences :** elles lient une fréquence à des familles d’activité.
- **Changement :** les contrôles ciblés restent proches de la modification.
- **Hebdomadaire :** les registres et cohérences transversales sont revus régulièrement.
- **Jalon :** les campagnes coûteuses sont planifiées avant le candidat.
- **Release :** la décision finale exige la capacité de revenir en arrière.

## 25. Planifier par coût de retour

Le coût de correction augmente généralement lorsque le défaut traverse davantage de phases. La stratégie place donc :

- les ambiguïtés de besoin avant l’implémentation ;
- les erreurs de contrat au niveau composant ;
- les incompatibilités aux frontières lors de l’intégration ;
- les parcours complets au niveau système ;
- les décisions de valeur lors de l’acceptation ;
- les procédures de restauration avant publication.

Cette règle n’interdit pas les validations tardives ; elle évite qu’elles soient les premières.

## 26. Définir les environnements pris en charge

Un résultat n’est valable que pour les environnements couverts. La matrice décrit les configurations promises, représentatives ou exploratoires.

> **[LECTURE] Profils d’environnement — Ne pas saisir.**

```yaml
environment_matrix:
  id: AST-QA-ENVIRONMENTS-001
  profiles:
    - id: AST-ENV-WINDOWS-DX12-001
      tier: supported
      os: Windows
      renderer: Forward+
      graphics_api: Direct3D_12
      input: keyboard_mouse
    - id: AST-ENV-LINUX-VULKAN-001
      tier: supported
      os: Linux
      renderer: Forward+
      graphics_api: Vulkan
      input: keyboard_mouse
    - id: AST-ENV-LOW-SPEC-EXPLORATORY-001
      tier: exploratory
      os: Windows
      renderer: Compatibility
      input: gamepad
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** chaque environnement possède une identité réutilisable.
- **Tier :** `supported` crée une obligation supérieure à `exploratory`.
- **Rendu :** le renderer et l’API graphique font partie du contexte.
- **Entrée :** le périphérique peut modifier les parcours et l’accessibilité.
- **Limite :** les versions matérielles détaillées seront définies par les campagnes de compatibilité.

## 27. Geler une baseline de configuration

Une campagne compare des résultats seulement si la configuration est identifiée. La baseline contient :

- build ;
- données ;
- paramètres ;
- addons ;
- versions de moteur et d’outils ;
- environnement ;
- options de difficulté ;
- langue ;
- périphériques ;
- statut des fonctionnalités expérimentales.

> **[LECTURE] Baseline de validation — Ne pas saisir.**

```yaml
validation_baseline:
  id: AST-QA-BASELINE-RC4-001
  build_id: AST-BUILD-0.8.0-RC4
  source_revision: "<git-commit>"
  godot_version: 4.7.1-stable
  data_catalog_version: 12
  balance_profile_id: AST-BAL-PROFILE-RELAY-REF-001
  locale: fr-FR
  environment_profile: AST-ENV-WINDOWS-DX12-001
  experimental_features: []
  approved: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Build :** l’identité du candidat est distincte de la révision source.
- **Données :** le catalogue possède sa propre version.
- **Équilibrage :** le profil est référencé sans recopier ses paramètres.
- **Locale :** les textes et formats peuvent modifier l’expérience.
- **Approbation :** `false` interdit de présenter la baseline comme retenue.

## 28. Distinguer sévérité et priorité

Sévérité proposée :

- `S0_CATASTROPHIC` : perte irréversible, compromission grave, impossibilité générale d’usage ;
- `S1_CRITICAL` : fonctionnalité majeure bloquée sans contournement acceptable ;
- `S2_MAJOR` : dégradation importante avec contournement limité ;
- `S3_MODERATE` : gêne réelle sans blocage majeur ;
- `S4_MINOR` : défaut cosmétique ou faible impact.

Priorité proposée :

- `P0_NOW` ;
- `P1_BEFORE_GATE` ;
- `P2_PLANNED` ;
- `P3_BACKLOG`.

Un défaut visuel mineur sur l’écran de lancement peut recevoir une priorité élevée avant une démonstration. Un défaut sévère dans une fonctionnalité désactivée peut être planifié après sécurisation de la désactivation.

> **[LECTURE] Classification d’un défaut — Ne pas saisir.**

```yaml
defect:
  id: AST-DEFECT-184
  title: "La restauration échoue après une migration interrompue."
  affected_build: AST-BUILD-0.8.0-RC4
  severity: S0_CATASTROPHIC
  priority: P0_NOW
  risk_ids:
    - AST-RISK-SAVE-MIGRATION-001
  reproducibility: consistent
  workaround: none
  owner: save_system_owner
  status: open
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sévérité :** la perte potentielle justifie `S0_CATASTROPHIC`.
- **Priorité :** le défaut est traité immédiatement avant la porte.
- **Risque :** le lien remonte au registre.
- **Reproductibilité :** elle décrit la fréquence observée, pas l’impact.
- **Contournement :** `none` augmente la pression de traitement sans modifier la sévérité.

## 29. Organiser le triage

Le triage vérifie :

1. identité du build et environnement ;
2. symptôme observable ;
3. étendue ;
4. sévérité ;
5. priorité ;
6. propriétaire ;
7. lien avec un risque ;
8. besoin de reproduction supplémentaire ;
9. effet sur les portes ;
10. communication requise.

Le triage ne cherche pas d’abord un coupable. Il choisit une action et un niveau d’urgence.

> **[LECTURE] Décision de triage — Ne pas saisir.**

```yaml
triage_decision:
  defect_id: AST-DEFECT-184
  classification_confirmed: true
  assigned_owner: save_system_owner
  blocks_gates:
    - G3_RELEASE_CANDIDATE
    - G4_RELEASE
  required_actions:
    - preserve_failing_fixture
    - implement_atomic_rollback
    - rerun_recovery_drill
  communication:
    stakeholders:
      - product_owner
      - support_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Confirmation :** le triage peut réviser une classification initiale.
- **Portes :** le défaut bloque deux transitions précises.
- **Actions :** la fixture fautive est conservée avant correction.
- **Revalidation :** la campagne de restauration doit être rejouée.
- **Communication :** les rôles affectés sont informés sans exposer de données inutiles.

## 30. Définir les règles stop-ship

Une règle `stop-ship` interdit la publication tant que sa condition est vraie. Exemples :

- perte ou corruption non récupérable de données prises en charge ;
- exécution de code non autorisée ;
- contournement d’autorité réseau critique ;
- impossibilité de lancer ou terminer le parcours principal ;
- défaut d’accessibilité rendant une fonction essentielle impraticable pour un mode officiellement pris en charge ;
- absence de retour arrière pour une migration irréversible ;
- dépendance ou licence incompatible avec la distribution prévue.

> **[VSC] Visual Studio Code — Créer `config/qa/stop-ship-policy.v1.yaml`.**

```yaml
stop_ship_policy:
  id: AST-QA-STOP-SHIP-001
  conditions:
    - id: AST-STOP-DATA-LOSS-001
      statement: "Perte non récupérable de données prises en charge."
      waiver_allowed: false
    - id: AST-STOP-RCE-001
      statement: "Exécution de code non autorisée confirmée."
      waiver_allowed: false
    - id: AST-STOP-MAIN-PATH-001
      statement: "Parcours principal impossible sans contournement pris en charge."
      waiver_allowed: false
    - id: AST-STOP-LICENSE-001
      statement: "Distribution incompatible avec une obligation de licence."
      waiver_allowed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conditions :** chaque blocage possède une identité et une phrase vérifiable.
- **Dérogation :** `false` interdit une acceptation locale du risque.
- **Portée :** la condition vise les données et parcours officiellement pris en charge.
- **Licence :** un problème juridique de distribution est traité comme un blocage produit.
- **Extension :** de nouvelles conditions créent une nouvelle version de politique.

## 31. Encadrer une dérogation

Une dérogation ne transforme pas un échec en réussite. Elle documente qu’une autorité accepte temporairement un écart.

Elle contient :

- critère concerné ;
- portée ;
- justification ;
- risque résiduel ;
- mesures compensatoires ;
- propriétaire ;
- approbateur ;
- date d’expiration ;
- condition de révocation.

> **[LECTURE] Dérogation bornée — Ne pas saisir.**

```yaml
waiver:
  id: AST-QA-WAIVER-012
  criterion_id: AST-G3-EXIT-COMPATIBILITY-004
  applies_to_builds:
    - AST-BUILD-0.8.0-RC4
  rationale: "Le périphérique exploratoire n’est pas dans le périmètre pris en charge."
  residual_risk: "Fonctionnement inconnu sur ce périphérique."
  compensating_controls:
    - release_notes_disclosure
    - telemetry_disabled_for_unknown_device
  owner: platform_owner
  approved_by: product_owner
  expires_at: 2026-08-15
  revocation_condition: "Le périphérique passe au niveau supported."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** la dérogation vise un build et un critère précis.
- **Risque :** l’incertitude reste visible.
- **Compensation :** les mesures réduisent l’exposition sans prétendre résoudre le défaut.
- **Expiration :** la date empêche une exception permanente.
- **Révocation :** un changement de périmètre invalide l’autorisation.

## 32. Relier QA documentaire, technique, artistique et produit

Quatre axes collaborent :

- **documentaire :** exigences, métadonnées, références, procédures et décisions ;
- **technique :** code, données, performances, sécurité, compatibilité et récupération ;
- **artistique :** cohérence visuelle, lisibilité, animation, audio et intégration ;
- **produit :** valeur, parcours, accessibilité, difficulté, attentes du public et risques de publication.

Un axe ne remplace pas les autres. Un build stable peut rester illisible ; une scène magnifique peut casser les budgets ; une fonctionnalité correcte peut ne pas répondre au besoin.

> **[LECTURE] Couverture multidisciplinaire d’une porte — Ne pas saisir.**

```yaml
gate_domain_reviews:
  gate_id: G3_RELEASE_CANDIDATE
  domains:
    documentary:
      owner: documentation_owner
      status: pending
    technical:
      owner: technical_qa
      status: pending
    artistic:
      owner: art_direction
      status: pending
    product:
      owner: product_qa
      status: pending
  aggregate_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaines :** les quatre revues sont séparées.
- **Propriété :** chaque axe possède un rôle compétent.
- **Statut global :** il reste en attente tant que les règles de combinaison ne sont pas appliquées.
- **Transparence :** une réussite technique ne masque pas un échec artistique ou produit.
- **Limite :** les critères propres à chaque domaine sont définis dans leurs plans spécialisés.

## 33. Encadrer la QA artistique

La QA artistique vérifie notamment :

- conformité au brief ;
- cohérence des échelles et silhouettes ;
- lisibilité du gameplay ;
- continuité des animations ;
- absence de défauts de matériaux ;
- cohérence des niveaux sonores ;
- respect des budgets ;
- provenance et droits ;
- intégration dans les scènes prises en charge.

Elle ne demande pas que tous les goûts convergent. Elle transforme les décisions artistiques approuvées en critères observables.

> **[LECTURE] Fiche de revue artistique — Ne pas saisir.**

```yaml
art_review:
  asset_id: AST-ASSET-RELAY-GATE-001
  asset_revision: 7
  brief_id: AST-ART-BRIEF-RELAY-001
  review_contexts:
    - gameplay_camera
    - low_light
    - accessibility_high_contrast
  criteria:
    silhouette_readability: pending
    material_consistency: pending
    animation_continuity: pending
    budget_compliance: pending
    rights_verified: pending
  decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Révisions :** l’asset et son brief sont identifiés séparément.
- **Contextes :** la revue ne se limite pas à une vue de présentation.
- **Critères :** lisibilité, cohérence, animation, budget et droits restent distincts.
- **Accessibilité :** le mode à contraste renforcé fait partie des contextes.
- **Décision :** aucune valeur n’est préremplie comme réussie.

## 34. Encadrer l’accessibilité

L’accessibilité est intégrée dès la conception. La stratégie demande :

- alternatives aux informations uniquement colorées ou sonores ;
- tailles et contrastes lisibles ;
- remappage des commandes lorsque pertinent ;
- sous-titres et réglages audio ;
- rythme et délais adaptables ;
- prévention des effets visuels problématiques ;
- navigation cohérente ;
- tests avec les modes pris en charge.

La conformité à une liste ne garantit pas une expérience utilisable. Les contrôles combinent exigences, inspection et retours de personnes concernées lorsque le protocole le permet.

## 35. Encadrer la sécurité

La stratégie de sécurité suit les risques :

- surfaces d’entrée ;
- autorité ;
- secrets ;
- données personnelles ;
- dépendances ;
- formats importés ;
- réseau ;
- mises à jour ;
- sauvegardes ;
- journalisation sensible.

Les contrôles détaillés viendront avec les chapitres réseau, DevOps et publication. Ici, la porte exige que les risques critiques aient un propriétaire et une décision explicite.

> **[LECTURE] Revue de sécurité de porte — Ne pas saisir.**

```yaml
security_gate_review:
  gate_id: G3_RELEASE_CANDIDATE
  threat_model_version: AST-THREAT-MODEL-003
  critical_findings_open: "<measured-value>"
  dependency_review_id: "<evidence-id>"
  secret_scan_id: "<evidence-id>"
  network_authority_review_id: "<evidence-id>"
  residual_risk_decision: pending
  owner: security_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Modèle :** la revue cite une version de menaces.
- **Mesure :** le nombre de constats doit provenir d’une preuve réelle.
- **Dépendances :** les contrôles restent référencés séparément.
- **Risque :** la décision résiduelle n’est pas déduite automatiquement du nombre.
- **Autorité :** le responsable sécurité signe son domaine.


## 36. Encadrer les données et l’IA

Lorsqu’un outil IA intervient, la QA documente :

- source de l’entrée ;
- version du modèle ou service ;
- paramètres importants ;
- droits et restrictions ;
- données sensibles interdites ;
- validation humaine ;
- transformation après génération ;
- provenance de l’asset final ;
- critères de rejet ;
- possibilité de régénérer ou remplacer.

Un résultat généré n’est pas accepté parce qu’il « ressemble au brief ». Il suit les mêmes portes artistiques, techniques, juridiques et produit que les autres assets.

> **[LECTURE] Provenance d’un asset assisté — Ne pas saisir.**

```yaml
assisted_asset_provenance:
  asset_id: AST-ASSET-RELAY-CONCEPT-014
  generation_tool: "<tool-and-version>"
  source_inputs:
    - AST-BRIEF-RELAY-001
  sensitive_data_included: false
  human_review:
    art_direction: pending
    technical_integration: pending
    rights_review: pending
  final_asset_revision: pending
  replacement_possible: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outil :** son identité et sa version doivent être renseignées avant usage comme preuve.
- **Entrées :** le brief est référencé sans stocker de contenu sensible inutile.
- **Revue :** art, technique et droits sont des décisions séparées.
- **Révision finale :** elle reste en attente tant que l’asset n’est pas matérialisé.
- **Remplacement :** la stratégie évite une dépendance irréversible à un résultat non reproductible.

## 37. Préparer la récupérabilité

La récupérabilité couvre :

- retour à une version précédente ;
- restauration de sauvegardes ;
- reprise d’une migration interrompue ;
- réinstallation ;
- reconstruction d’un build ;
- récupération des configurations ;
- retrait d’un contenu fautif ;
- conservation des preuves d’incident.

La présence d’une sauvegarde ne prouve pas qu’elle peut être restaurée. La porte consomme une preuve de restauration adaptée au risque.

> **[LECTURE] Plan de retour arrière — Ne pas saisir.**

```yaml
rollback_plan:
  id: AST-ROLLBACK-PLAN-RC4-001
  subject_build: AST-BUILD-0.8.0-RC4
  previous_supported_build: AST-BUILD-0.7.6
  data_migration:
    reversible: false
    restore_path: AST-RESTORE-PATH-SAVE-012
  triggers:
    - stop_ship_condition_confirmed
    - crash_rate_threshold_exceeded
    - save_corruption_confirmed
  decision_owner: operations_owner
  verification_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Versions :** le candidat et la version de repli sont explicites.
- **Migration :** une migration irréversible exige un chemin de restauration.
- **Déclencheurs :** les événements de retour arrière sont déclarés avant publication.
- **Autorité :** l’exploitation possède la décision opérationnelle.
- **Preuve :** `pending` interdit de supposer que le plan fonctionne.

## 38. Choisir des indicateurs QA sans les détourner

Des indicateurs utiles :

- temps entre détection et triage ;
- âge des défauts par sévérité ;
- taux de réouverture ;
- part des risques critiques couverts ;
- stabilité des campagnes ;
- défauts échappés par phase ;
- durée des portes ;
- dérogations expirées ;
- restaurations réussies sur tentatives ;
- proportion de contrôles non déterministes.

Aucun indicateur ne doit devenir un objectif isolé. Fermer rapidement un défaut en le reclassant ne réduit pas le risque.

> **[LECTURE] Tableau de bord avec dénominateurs — Ne pas saisir.**

```yaml
qa_metrics:
  reporting_period: "<period>"
  critical_risk_coverage:
    covered: "<measured-value>"
    total: "<measured-value>"
  reopened_defects:
    reopened: "<measured-value>"
    closed: "<measured-value>"
  recovery_drills:
    successful: "<measured-value>"
    attempted: "<measured-value>"
  expired_waivers:
    count: "<measured-value>"
  interpretation_owner: product_qa
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Période :** les valeurs sont bornées dans le temps.
- **Dénominateurs :** couverture, réouverture et restauration restent recalculables.
- **Placeholders :** aucune mesure n’est inventée.
- **Dérogations :** leur expiration devient visible.
- **Interprétation :** un rôle analyse les nombres au lieu d’appliquer un seuil universel.

## 39. Produire un rapport de porte

Le rapport résume :

- sujet ;
- politique appliquée ;
- critères ;
- preuves ;
- défauts ;
- risques résiduels ;
- dérogations ;
- décision ;
- signataires ;
- actions.

> **[VSC] Visual Studio Code — Créer `work/qa/gates/AST-GATE-G3-RC4.yaml`.**

```yaml
gate_report:
  id: AST-GATE-G3-RC4
  gate_id: G3_RELEASE_CANDIDATE
  policy_version: AST-QA-GATES-001
  subject_build: AST-BUILD-0.8.0-RC4
  evidence_manifest_id: AST-QA-EVIDENCE-G3-004
  criteria:
    satisfied: []
    failed: []
    unknown: []
  open_defects: []
  residual_risks: []
  active_waivers: []
  decision:
    status: HOLD
    rationale: "Rapport modèle : preuves non matérialisées."
  signatories:
    product_qa: pending
    technical_lead: pending
    product_owner: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Politique :** le rapport cite les règles utilisées.
- **Trois listes :** satisfait, échoué et inconnu ne sont pas confondus.
- **Risques :** ils restent visibles même sans défaut ouvert.
- **Décision :** le modèle est `HOLD` puisqu’aucune preuve réelle n’est fournie.
- **Signatures :** les approbations ne sont pas préremplies.

## 40. Produire un rapport de synthèse

Un rapport de synthèse n’énumère pas tous les résultats. Il montre :

- décision proposée ;
- risques critiques ;
- blocages ;
- tendances ;
- réserves ;
- changements depuis la précédente porte ;
- actions et propriétaires.

> **[LECTURE] Synthèse pour décision — Ne pas saisir.**

```yaml
qa_summary:
  subject_build: AST-BUILD-0.8.0-RC4
  proposed_gate_status: HOLD
  critical_risks:
    covered: "<measured-value>"
    total: "<measured-value>"
  stop_ship_defects_open: "<measured-value>"
  changed_since_previous_review:
    - "<change>"
  reservations:
    - "<reservation>"
  required_actions:
    - action: "<action>"
      owner: "<role>"
      due_gate: "<gate-id>"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Proposition :** le statut reste une recommandation jusqu’à signature.
- **Criticité :** les risques utilisent un numérateur et un total.
- **Blocages :** les défauts stop-ship sont séparés des autres.
- **Évolution :** la différence depuis la revue précédente évite une photographie sans contexte.
- **Actions :** chaque action possède un rôle et une échéance de porte.

## 41. Valider la structure de la stratégie

Un validateur léger peut vérifier les contrats documentaires : identifiants, risques critiques, propriétaires, couches de contrôle et dates de dérogation. Il ne prétend pas exécuter les campagnes.

> **[VSC] Visual Studio Code — Créer `automation/src/asteria_tools/qa/validate_strategy.py`.**

```python
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable


@dataclass(frozen=True)
class RiskCoverage:
    risk_id: str
    classification: str
    owner: str
    prevention_count: int
    detection_count: int
    correction_count: int
    residual_decision: str


def validate_critical_risk(coverage: RiskCoverage) -> list[str]:
    issues: list[str] = []
    if not coverage.risk_id.strip():
        issues.append("QA_RISK_ID_MISSING")
    if coverage.classification == "critical":
        if not coverage.owner.strip():
            issues.append("QA_CRITICAL_RISK_OWNER_MISSING")
        if coverage.prevention_count < 1:
            issues.append("QA_CRITICAL_RISK_PREVENTION_MISSING")
        if coverage.detection_count < 1:
            issues.append("QA_CRITICAL_RISK_DETECTION_MISSING")
        if coverage.correction_count < 1:
            issues.append("QA_CRITICAL_RISK_CORRECTION_MISSING")
        if coverage.residual_decision not in {"accepted", "rejected", "pending"}:
            issues.append("QA_RESIDUAL_DECISION_INVALID")
    return issues


def expired_waiver_ids(
    waivers: Iterable[tuple[str, date]],
    today: date,
) -> list[str]:
    return sorted(
        waiver_id
        for waiver_id, expiration in waivers
        if expiration < today
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dataclass :** `frozen=True` rend l’objet de couverture immuable après création.
- **Paramètre :** `coverage` regroupe les champs nécessaires à la règle critique.
- **Retour :** la fonction renvoie tous les codes de non-conformité au lieu de s’arrêter au premier.
- **Comptages :** chaque couche exige au moins un contrôle pour un risque critique.
- **Dérogations :** `expired_waiver_ids()` reçoit la date explicitement, ce qui rend le contrôle déterministe et testable.

## 42. Lancer le contrôle structurel

> **[PS] PowerShell 7 — Vérifier les contrats de stratégie QA.**

```powershell
.\.venv\Scripts\python.exe -m asteria_tools.qa.validate_strategy `
  --charter config\qa\qa-charter.v1.yaml `
  --risks config\qa\risk-register.v1.yaml `
  --matrix config\qa\risk-control-matrix.v1.yaml `
  --gates config\qa\quality-gates.v1.yaml

if ($LASTEXITCODE -ne 0) {
  throw "La stratégie QA contient une non-conformité structurelle."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interpréteur :** l’environnement virtuel du projet est utilisé.
- **Entrées :** charte, risques, matrice et portes sont fournis explicitement.
- **Continuation :** l’accent grave prolonge la commande PowerShell.
- **Code de retour :** toute valeur différente de zéro bloque le lot documentaire.
- **Limite :** la commande valide la structure, pas les comportements du jeu.

## 43. Lire la sortie du validateur

> **[SORTIE] Exemple de sortie structurelle — Ne pas saisir.**

```text
QA strategy validation
charter: OK
risk register: 12 risks
critical risks: 4
critical risks fully covered: 3
expired waivers: 1

ERROR QA_CRITICAL_RISK_CORRECTION_MISSING AST-RISK-SAVE-MIGRATION-001
ERROR QA_WAIVER_EXPIRED AST-QA-WAIVER-004
result: FAILED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Comptages :** les risques totaux et critiques rendent le périmètre visible.
- **Couverture :** trois risques sur quatre ont les trois couches requises.
- **Codes :** chaque ligne associe une règle à une identité.
- **Résultat :** `FAILED` signifie que la stratégie est incomplète, pas que le produit runtime a échoué.
- **Action :** le propriétaire ajoute une correction ou renouvelle explicitement la décision de dérogation.

## 44. Mode Solo

En Solo :

- limiter le registre aux risques qui influencent réellement une décision ;
- commencer par trois à sept risques critiques ou élevés ;
- définir les portes `G0`, `G2`, `G3` et `G4` avant d’ajouter des variantes ;
- séparer les sessions d’écriture, d’exécution et de décision ;
- automatiser les contrôles structurels répétitifs ;
- garder les preuves sous des chemins stables ;
- dater les dérogations ;
- refuser les critères impossibles à vérifier seul ;
- demander une revue externe pour sécurité, accessibilité ou droits lorsque le risque l’exige.

Une stratégie courte et appliquée vaut mieux qu’un classeur exhaustif jamais relu.

## 45. Mode Studio

En Studio :

- attribuer un propriétaire à chaque dimension de qualité ;
- définir les services et équipes consultés par porte ;
- publier les politiques de classement et stop-ship ;
- rendre les environnements et baselines immuables ;
- synchroniser les calendriers technique, artistique et produit ;
- séparer les rapports détaillés des synthèses de décision ;
- mesurer les dérogations et leur expiration ;
- conserver les résultats négatifs ;
- organiser une escalade pour désaccord de sévérité ou risque résiduel ;
- réviser la stratégie après chaque incident significatif.

La QA n’est pas un service placé à la fin de la chaîne. Chaque propriétaire de système reste responsable de la qualité de son domaine.

## 46. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants appliquent la règle sémantique complète : symptôme, exemple fautif, correction et explication de la différence.

### 46.1 Tester uniquement à la fin

**Symptôme ou risque :** les besoins ambigus, contrats incompatibles et assets non conformes sont découverts lorsque la correction coûte le plus cher.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
qa_plan:
  activities:
    - final_test_week
  earlier_reviews: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une unique semaine finale concentre toutes les détections et ne prévoit aucune prévention ni validation intermédiaire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
qa_plan:
  per_change:
    - scope_risk_review
    - static_checks
  per_integration:
    - boundary_validation
  per_candidate:
    - system_campaign
    - gate_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les activités sont placées près des décisions qu’elles doivent éclairer, tout en conservant une campagne système avant le candidat.

### 46.2 Confondre sévérité et priorité

**Symptôme ou risque :** un défaut cosmétique urgent est classé catastrophique, ou une perte de données est minimisée parce que sa correction est coûteuse.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
defect:
  severity: urgent
  priority: catastrophic
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les deux champs mélangent impact et ordre de traitement, ce qui empêche une comparaison cohérente.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
defect:
  severity: S0_CATASTROPHIC
  priority: P0_NOW
  severity_rationale: "Perte non récupérable de progression."
  priority_rationale: "Bloque G3 et G4."
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’impact et l’ordre sont évalués séparément puis justifiés par des faits distincts.

### 46.3 Promouvoir parce que le pipeline est vert

**Symptôme ou risque :** la publication est autorisée alors que les revues artistique, accessibilité ou produit restent inconnues.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
release_rule:
  when_ci_green: publish
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un résultat technique unique reçoit une autorité produit et masque les domaines non couverts.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
release_rule:
  requires:
    - technical_gate_passed
    - artistic_gate_passed
    - accessibility_gate_decided
    - residual_risks_signed
    - rollback_ready
  decision_owner: product_owner
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La décision combine plusieurs domaines et reste signée par l’autorité produit.

### 46.4 Enregistrer un risque sans propriétaire

**Symptôme ou risque :** le registre grandit, mais personne ne construit la couverture ni ne décide du risque résiduel.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
risk:
  id: AST-RISK-NETWORK-AUTHORITY-001
  owner: null
  status: open
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’identité du risque ne suffit pas à déclencher une action ou une décision.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
risk:
  id: AST-RISK-NETWORK-AUTHORITY-001
  owner: network_owner
  review_gate: G2_INTEGRATION
  residual_decision_owner: security_owner
  status: open
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La couverture, l’échéance et l’autorité résiduelle sont attribuées à des rôles identifiés.

### 46.5 Accorder une dérogation sans expiration

**Symptôme ou risque :** une exception temporaire devient une règle permanente et continue de s’appliquer à de nouveaux builds.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
waiver:
  criterion_id: AST-G3-EXIT-COMPATIBILITY-004
  applies_forever: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La portée, le responsable, le risque et la date de revue sont absents.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
waiver:
  id: AST-QA-WAIVER-012
  criterion_id: AST-G3-EXIT-COMPATIBILITY-004
  applies_to_builds:
    - AST-BUILD-0.8.0-RC4
  owner: platform_owner
  approved_by: product_owner
  expires_at: 2026-08-15
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’exception est limitée à un build, possédée, approuvée et automatiquement réexaminée à l’expiration.

### 46.6 Utiliser un pourcentage de couverture comme preuve de qualité

**Symptôme ou risque :** l’équipe cherche à augmenter un nombre sans vérifier que les risques critiques sont réellement couverts.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
quality_decision:
  code_coverage_percent: 90
  conclusion: release_ready
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le pourcentage ne décrit ni les comportements couverts, ni les risques, ni les assertions, ni les domaines non techniques.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
quality_decision:
  critical_risks:
    covered: 4
    total: 5
  uncovered_risk_ids:
    - AST-RISK-SAVE-MIGRATION-001
  conclusion: HOLD
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le dénominateur et le risque manquant rendent la décision vérifiable et empêchent une promotion prématurée.

### 46.7 Modifier les critères après avoir vu les résultats

**Symptôme ou risque :** un seuil est abaissé pour faire passer un candidat déjà produit.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
criterion:
  id: AST-PERF-BUDGET-001
  threshold: "modifié après le run"
  rationale: "Le build doit passer."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La décision adapte la règle au résultat et détruit la valeur comparative de la campagne.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
criterion:
  id: AST-PERF-BUDGET-001
  version: 2
  effective_from_build: AST-BUILD-0.9.0
  previous_version_preserved: true
  rationale: "Nouveau périmètre matériel approuvé."
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La nouvelle règle possède une version, une date d’effet et ne réécrit pas l’évaluation du build précédent.

### 46.8 Utiliser des données de production comme fixtures par défaut

**Symptôme ou risque :** une campagne locale copie des sauvegardes ou identifiants réels sans nécessité ni gouvernance.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
test_data:
  source: production_export
  anonymized: false
  approval: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les données réelles sont utilisées sans minimisation, base, contrôle d’accès ni justification.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
test_data:
  source: synthetic_fixture
  fixture_id: AST-FIXTURE-SAVE-MIGRATION-001
  personal_data: prohibited
  generated_from_schema_version: 11
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Une fixture synthétique versionnée répond au besoin de migration sans exposer de personne ni de sauvegarde réelle.

### 46.9 Fermer un défaut sans preuve de correction

**Symptôme ou risque :** le ticket est marqué résolu après modification du code, mais le scénario fautif n’est pas rejoué.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
defect:
  id: AST-DEFECT-184
  status: closed
  reason: "Le correctif a été committé."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un commit prouve une modification, pas la disparition du symptôme ni l’absence de régression.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
defect:
  id: AST-DEFECT-184
  status: verified
  fix_revision: "<git-commit>"
  verification_execution_id: AST-QA-RUN-RESTORE-043
  regression_control_id: AST-CTRL-SAVE-COMPATIBILITY-CAMPAIGN-001
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La fermeture cite la révision, l’exécution de vérification et le contrôle de non-régression associé.

### 46.10 Traiter tous les défauts comme bloquants

**Symptôme ou risque :** la porte devient impraticable, les équipes cachent les défauts mineurs et les risques critiques perdent leur visibilité.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
gate_policy:
  any_open_defect: REJECT
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le statut ignore sévérité, périmètre, contournement, risque résiduel et dérogations bornées.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
gate_policy:
  reject_when:
    - stop_ship_condition_open
    - critical_risk_without_decision
  allow_reservation_when:
    - non_blocking_defect_documented
    - valid_waiver_present
  decision_owner: product_owner
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les blocages sont réservés aux conditions inacceptables, tandis que les écarts non bloquants restent visibles et gouvernés.

## 47. Checklist de production et d’acceptation

- [ ] charte QA versionnée ;
- [ ] modèle de qualité et propriétaires définis ;
- [ ] registre des risques à jour ;
- [ ] chaque risque critique possède un propriétaire ;
- [ ] prévention, détection et correction définies pour chaque risque critique ;
- [ ] risque résiduel décidé ou explicitement en attente ;
- [ ] niveaux et familles de validation séparés ;
- [ ] environnements et baselines identifiés ;
- [ ] critères d’entrée et de sortie observables ;
- [ ] propriétaires des portes désignés ;
- [ ] règles stop-ship publiées ;
- [ ] dérogations bornées par portée et expiration ;
- [ ] sévérité et priorité séparées ;
- [ ] calendrier proportionné au projet ;
- [ ] QA documentaire, technique, artistique et produit reliées ;
- [ ] sécurité, accessibilité et récupérabilité représentées ;
- [ ] rapports et manifestes de preuve versionnés ;
- [ ] indicateurs accompagnés de leurs dénominateurs ;
- [ ] aucune donnée réelle utilisée comme fixture par défaut ;
- [ ] aucune décision automatique issue d’un score unique ;
- [ ] aucune instruction de pilotage éditorial dans le texte lecteur.

## 48. Critère d’acceptation de la stratégie

La stratégie de `Project Asteria` pourra être déclarée matérialisée lorsque :

- la charte QA existe dans le projet ;
- le modèle de qualité est approuvé ;
- le registre des risques contient les risques critiques connus ;
- la matrice relie chaque risque critique à prévention, détection et correction ;
- chaque porte possède des critères vérifiables et un propriétaire ;
- les environnements pris en charge sont identifiés ;
- les règles stop-ship sont approuvées ;
- les dérogations possèdent une expiration ;
- les modèles de preuve et de rapport sont utilisables ;
- le validateur structurel réussit ;
- une revue Solo ou Studio confirme la couverture explicite des risques critiques.

Le présent chapitre ne revendique aucune de ces matérialisations ni exécutions.

## 49. Références techniques officielles

- [Godot 4.7 — Utilisation en ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Python 3.14 — `dataclasses`](https://docs.python.org/3.14/library/dataclasses.html)
- [Python 3.14 — `datetime`](https://docs.python.org/3.14/library/datetime.html)
- [Python 3.14 — `typing`](https://docs.python.org/3.14/library/typing.html)
- [GitHub Actions — Environnements et approbations](https://docs.github.com/actions/deployment/targeting-different-environments/managing-environments-for-deployment)
- [OWASP — Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [W3C — Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [Livre II — Chapitre 27 : Tests unitaires, tests d’intégration et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Livre II — Chapitre 28 : Journalisation, diagnostic et reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md)
- [Livre II — Chapitre 29 : Automatisation Python et génération de données](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md)
- [Livre IV — Chapitre 1 : Équilibrage et télémétrie locale](CHAPITRE-01-Equilibrage-et-telemetrie-locale.md)

## 50. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient les décisions suivantes :

- la QA commence par les risques et non par une liste d’outils ;
- la prévention, la détection et la correction restent trois responsabilités distinctes ;
- les niveaux de validation décrivent l’échelle, tandis que les familles décrivent la méthode ;
- les cas détaillés restent réservés aux campagnes des chapitres spécialisés ;
- chaque risque critique possède un propriétaire et une décision résiduelle ;
- aucune porte ne dépend d’un score ou d’un pipeline unique ;
- les critères d’entrée et de sortie sont observables ;
- les statuts `PASS`, `PASS_WITH_RESERVATIONS`, `HOLD` et `REJECT` restent distincts ;
- les preuves citent build, environnement, contrôle, résultat et décision ;
- les défauts conservent sévérité et priorité séparées ;
- les règles stop-ship couvrent notamment perte de données, compromission, parcours principal et incompatibilité de licence ;
- les dérogations ont une portée, un approbateur et une expiration ;
- les modes Solo et Studio appliquent une séparation adaptée des rôles ;
- les axes documentaire, technique, artistique et produit participent aux portes ;
- accessibilité, sécurité et récupérabilité sont intégrées à la stratégie ;
- les données synthétiques sont préférées aux données réelles pour les fixtures ;
- une correction n’est close qu’après vérification ;
- le retour arrière est préparé avant la décision de publication ;
- les résultats négatifs et risques résiduels restent consultables ;
- aucun résultat runtime n’est revendiqué sans exécution conservée.

> **[LECTURE] Décisions de la stratégie QA — Ne pas saisir.**

```yaml
asteria_qa_strategy:
  charter_id: AST-QA-CHARTER-001
  quality_profile_id: AST-QUALITY-PROFILE-001
  risk_policy_id: AST-QA-RISK-POLICY-001
  gate_policy_id: AST-QA-GATES-001
  stop_ship_policy_id: AST-QA-STOP-SHIP-001
  risk_based: true
  prevention_detection_correction_required: true
  critical_risk_owner_required: true
  critical_risk_residual_decision_required: true
  single_score_release_authority: prohibited
  evidence_before_decision: required
  waiver_expiration: required
  synthetic_test_data_default: true
  rollback_before_release: required
  detailed_test_cases_owned_by_chapter_3: true
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Politiques :** les cinq identifiants relient la charte, le modèle de qualité, les risques, les portes et les blocages.
- **Risques critiques :** propriétaire et décision résiduelle sont obligatoires.
- **Autorité :** un score unique ne peut pas publier le produit.
- **Données :** les fixtures synthétiques sont le choix par défaut.
- **Frontière :** les cas détaillés appartiennent au chapitre 3, et `not_started` interdit toute revendication d’exécution.
