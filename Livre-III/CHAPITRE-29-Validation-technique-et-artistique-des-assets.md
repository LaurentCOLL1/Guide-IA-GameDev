---
title: "Livre III — Chapitre 29 : Validation technique et artistique des assets"
id: "DOC-L3-CH29"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 29
last-verified: "2026-07-25T07:39:11+02:00"
audit-status: "complete"
audit-date: "2026-07-25T07:39:11+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-29.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Validation technique et artistique des assets

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH29`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Une porte qualité transforme un avis dispersé en décision reproductible. Elle reçoit un asset identifié, ses sources, son manifeste, ses résultats d’import et ses preuves, puis sépare clairement les constats techniques, la revue artistique et la décision de publication.

Le chapitre ne promet pas qu’un asset est bon parce qu’un script ne trouve aucune anomalie. Les contrôles automatiques peuvent bloquer un contrat mesurable ; la conformité artistique, la lisibilité et l’adéquation au projet restent revues par une personne responsable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: versioned_asset_candidate_with_manifest_and_import_evidence
  technical_review: deterministic_checks_against_family_profile
  artistic_review: human_comparison_against_visual_bible_and_usage
  decision: accepted_rejected_or_changes_requested
  authority: content_quality_gate_only
  runtime_claims: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le candidat doit être versionné et relié à ses sources, dépendances et preuves.
- **Contrôle technique :** les règles mesurables utilisent des profils explicites et des codes stables.
- **Contrôle artistique :** une personne compare intention, usage, lisibilité et cohérence à la bible.
- **Décision :** le rapport conserve les écarts, responsables, actions et réserves.
- **Limite :** aucun contrôle d’asset ne crée ou ne modifie une règle gameplay.

## 2. Résultats d’apprentissage

Le lecteur saura construire une checklist universelle, l’étendre par famille d’asset, attribuer des responsabilités et transformer chaque anomalie en constat vérifiable. Il saura aussi distinguer un blocage automatique d’une demande artistique et d’une dérogation limitée.

À la fin du chapitre, il pourra préparer une scène Godot de validation, un schéma de rapport, un protocole de mesure et une boucle de correction utilisables en Solo comme en Studio.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  universal_gate: [identity, provenance, integrity, budget, godot_test]
  family_extensions:
    - static_mesh
    - character
    - animation
    - material_texture
    - vfx
    - ui
    - audio
  evidence: [manifest, machine_report, captures, measurements, review_notes]
  decisions: [changes_requested, rejected, accepted_with_waiver, accepted]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Socle :** toutes les familles partagent identité, droits, version, dépendances et preuve Godot.
- **Extensions :** chaque famille ajoute uniquement ses contrôles propres.
- **Preuves :** les sorties automatiques et les observations humaines restent séparées.
- **Décisions :** chaque statut possède des préconditions et un responsable explicites.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les profils, scripts, scènes et rapports sont des contrats pédagogiques ; ils ne prouvent pas qu’un asset réel a traversé la porte.

Les seuils numériques présentés sont des exemples candidats ou des champs de profil. Ils doivent être remplacés par les budgets approuvés du projet et mesurés sur les plateformes cibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  pilot_assets_materialized: false
  godot_validation_scene_created: false
  automated_checks_executed: false
  artistic_review_performed: false
  runtime_measurements_recorded: false
  final_asset_acceptance_issued: false
  pdf_produced: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode et les extraits sont relus sans annoncer une campagne exécutée.
- **Scène :** aucune scène de validation Godot n’est déclarée créée.
- **Mesures :** aucune valeur de temps, mémoire, draw calls ou qualité n’est inventée.
- **Décision :** aucun asset de Project Asteria n’est déclaré accepté.
- **Publication :** le PDF reste différé jusqu’à la fin du Livre III.

## 4. Frontières avec les chapitres voisins

Les chapitres 1 à 27 restent propriétaires des intentions, sources, conventions artistiques et livraisons. Le chapitre 28 reste propriétaire des formats, presets, remaps, scènes d’intégration et procédures de réimportation.

Le chapitre 29 possède la porte d’acceptation d’un candidat individuel. Le chapitre 30 orchestrera les lots, la reprise et la CI, sans pouvoir déclarer seul la qualité artistique. La QA du jeu complet demeure au Livre IV.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapters_01_to_27: artistic_rules_sources_and_family_contracts
  chapter_28: import_profiles_reimport_and_integration
  chapter_29: individual_asset_quality_gate_and_final_decision
  chapter_30: batch_orchestration_ci_and_sampling
  book_iv: complete_game_qa_and_platform_release
  invariant: asset_validation_never_commits_gameplay_state
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** les critères propriétaires sont consommés sans être redéfinis.
- **Chapitre 28 :** la reproductibilité d’import reste une dépendance obligatoire.
- **Chapitre 29 :** les constats sont consolidés en décision d’asset.
- **Aval :** le lot et la QA du jeu possèdent leurs propres responsabilités.
- **Invariant :** un statut d’asset ne devient jamais un état de simulation.

## 5. Pilote de validation de Project Asteria

Le pilote `AST-ASSET-GATE-SCOUT-RELAY-001` reprend l’éclaireur animé et le module de relais du chapitre 28. Il permet de tester une même porte sur un personnage, un prop statique et leurs dépendances visibles.

Le pilote reste un contrat de validation : il nomme les profils, scènes et rapports attendus sans prétendre que les fichiers, captures ou mesures existent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_asset_gate_pilot:
  id: AST-ASSET-GATE-SCOUT-RELAY-001
  candidates:
    - AST-CHAR-SCOUT-001
    - AST-PROP-RELAY-MODULE-001
  import_dependency: AST-IMPORT-PILOT-SCOUT-RELAY-001
  checklist: AST-ASSET-QA-CHECKLIST-001
  validation_scene: AST-ASSET-QA-SCENE-001
  report_schema: AST-ASSET-QA-REPORT-001
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** deux familles suffisent à éprouver la checklist commune et ses extensions.
- **Dépendance :** la scène d’intégration du chapitre 28 constitue l’entrée Godot.
- **Checklist :** les critères universels et familiaux portent des identifiants stables.
- **Rapport :** les résultats techniques, artistiques et juridiques restent traçables.
- **Réserve :** aucune acceptation n’est déclarée.

## 6. Modèle mental de la porte qualité

Une porte qualité n’est ni une simple checklist ni un bouton vert. Elle combine un profil versionné, un candidat figé, une exécution déterministe, une revue humaine, une décision signée et une possibilité de reprise.

La décision ne porte jamais sur un fichier mutable sans identité. Elle porte sur une révision précise, reliée à ses sources et à son empreinte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
quality_gate:
  profile: immutable_versioned_rules
  candidate: frozen_asset_revision
  machine_pass: reproducible_findings
  human_pass: documented_artistic_judgment
  decision: scoped_and_signed
  rework: new_candidate_revision
  audit_trail: append_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** les règles utilisées sont conservées avec leur version.
- **Candidat :** l’empreinte empêche de confondre deux révisions.
- **Passes :** la machine collecte des faits ; la personne évalue les qualités non réductibles.
- **Reprise :** une correction produit un nouveau candidat et une nouvelle exécution.
- **Historique :** les décisions antérieures ne sont pas réécrites.

## 7. Machine d’états d’un asset

Les états décrivent le parcours de revue, pas la qualité intrinsèque du contenu. Un asset peut être techniquement valide mais attendre une revue artistique, ou être artistiquement approuvé tout en restant bloqué par ses droits.

Les transitions sont explicites afin qu’une interface, un script ou un tableau de production ne déduise pas un statut depuis la couleur d’une cellule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_states:
  - DRAFT
  - READY_FOR_REVIEW
  - TECHNICAL_BLOCKED
  - ART_REVIEW_REQUIRED
  - CHANGES_REQUESTED
  - RIGHTS_BLOCKED
  - ACCEPTED_WITH_WAIVER
  - ACCEPTED
  - RETIRED
terminal_for_release: [ACCEPTED, ACCEPTED_WITH_WAIVER]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Brouillon :** le contenu reste modifiable et n’entre pas dans une build de publication.
- **Blocages :** technique et droits restent distincts pour orienter la correction.
- **Revue :** un passage technique ne remplace pas l’avis artistique.
- **Acceptation :** la dérogation doit être bornée et visible.
- **Retrait :** un asset accepté peut être retiré sans effacer son historique.

## 8. Transitions autorisées et refus contrôlés

Une transition vérifie les préconditions du statut cible. Par exemple, `ACCEPTED` exige une révision inchangée, aucun blocage ouvert, une provenance qualifiée et deux décisions présentes lorsque le profil Studio l’impose.

Un refus de transition est un résultat normal du contrat. Il doit renvoyer un code stable et la liste des préconditions manquantes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transition_policy:
  READY_FOR_REVIEW:
    requires: [candidate_frozen, manifest_valid]
  ART_REVIEW_REQUIRED:
    requires: [technical_blockers_zero, rights_blockers_zero]
  ACCEPTED:
    requires:
      - candidate_hash_unchanged
      - technical_decision_approved
      - artistic_decision_approved
      - rights_decision_approved
      - waivers_valid
  refusal_code: ASSET_GATE_PRECONDITION_MISSING
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préconditions :** chaque cible déclare les preuves nécessaires.
- **Empreinte :** la décision est annulée si le candidat a changé.
- **Décisions :** les responsabilités ne sont pas fusionnées dans un booléen unique.
- **Refus contrôlé :** le code et les champs manquants permettent une correction déterministe.

## 9. Responsabilités et séparation des rôles

Le propriétaire de l’asset prépare le candidat et répond aux demandes de correction. Le valideur technique contrôle les contrats mesurables ; le valideur artistique juge la conformité à la bible et à l’usage ; le responsable des droits confirme le statut juridique.

Dans un petit projet, une même personne peut porter plusieurs rôles, mais elle exécute des passes séparées et conserve la date, le rôle assumé et les preuves consultées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
roles:
  asset_owner:
    can: [submit_candidate, answer_findings, publish_new_revision]
  technical_reviewer:
    can: [run_checks, classify_technical_findings]
  artistic_reviewer:
    can: [compare_bible, request_visual_changes, approve_art]
  rights_reviewer:
    can: [approve_provenance, block_distribution]
  release_owner:
    can: [issue_final_decision]
separation_rule: role_context_recorded_even_when_person_is_same
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaire :** il ne peut pas supprimer un constat pour obtenir l’acceptation.
- **Technique :** il ne transforme pas un goût en règle automatique.
- **Artistique :** il motive les écarts avec des références et le contexte d’usage.
- **Droits :** il peut bloquer une distribution techniquement parfaite.
- **Solo :** la séparation temporelle réduit l’auto-validation impulsive.

## 10. Identité, version et empreinte du candidat

Le rapport doit viser une révision immuable. L’identifiant stable nomme l’asset à travers le temps ; la version et l’empreinte nomment le candidat exact soumis à la porte.

Les chemins sont utiles pour retrouver les fichiers, mais ils ne constituent pas une identité durable. Un déplacement ne doit pas créer un nouvel asset, et un remplacement de contenu au même chemin doit créer une nouvelle révision.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_candidate:
  asset_id: AST-CHAR-SCOUT-001
  candidate_version: 0.7.0-rc.2
  source_revision: scout_blend_r184
  delivery_path: res://assets/source_delivery/characters/scout.glb
  delivery_sha256: <sha256>
  integration_scene: res://assets/integration/characters/scout_integrated.tscn
  profile_id: AST-ASSET-QA-PROFILE-CHARACTER-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** il reste stable même si le fichier ou le nom affiché change.
- **Version :** elle ordonne les révisions candidates.
- **Empreinte :** elle lie les résultats au contenu binaire exact.
- **Chemins :** ils localisent les dépendances sans devenir l’identité.
- **Profil :** la version des règles doit être enregistrée dans le rapport.

## 11. Contrat d’entrée de la validation

La porte refuse un candidat incomplet avant d’exécuter des contrôles coûteux. Le manifeste doit indiquer la famille, les dépendances, le profil, le contexte d’usage et les preuves disponibles.

Cette prévalidation distingue l’absence de donnée d’un contrôle négatif. Un champ manquant ne doit jamais devenir silencieusement une valeur par défaut favorable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
submission_contract:
  required:
    - asset_id
    - candidate_version
    - family
    - source_revision
    - delivery_sha256
    - integration_scene
    - import_profile_id
    - qa_profile_id
    - provenance_record_id
    - intended_usage
  unknown_field_policy: reject
  missing_field_policy: technical_blocker
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs requis :** ils garantissent que le candidat peut être reproduit et interprété.
- **Famille :** elle sélectionne l’extension de checklist appropriée.
- **Usage :** un même contenu peut être acceptable en foule et refusé en gros plan.
- **Politique stricte :** les champs inconnus ou manquants ne sont pas ignorés.
- **Résultat :** la porte échoue avant toute prétendue revue complète.

## 12. Provenance, licence et consentement comme précondition

Le chapitre 5 reste l’autorité du modèle juridique. La porte du chapitre 29 ne réécrit pas ce modèle : elle vérifie que l’enregistrement attendu existe, vise la bonne révision et autorise l’usage et la redistribution prévus.

Une provenance inconnue, une licence ambiguë ou un consentement insuffisant bloque l’acceptation finale, même lorsque l’asset est visuellement et techniquement irréprochable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rights_gate:
  provenance_record_id: AST-PROV-CHAR-SCOUT-001
  source_identity_complete: true
  licence_expression_resolved: true
  redistribution_allowed: true
  modification_allowed: true
  attribution_requirements_recorded: true
  consent_scope_sufficient: true
  unresolved_rights: []
decision_when_unresolved: RIGHTS_BLOCKED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le rapport pointe vers le registre de provenance plutôt que recopier ses données.
- **Portée :** l’usage prévu et la redistribution sont vérifiés séparément.
- **Attribution :** les obligations de crédit restent conservées avec l’asset.
- **Consentement :** les droits personnels ne sont pas déduits d’une simple disponibilité du fichier.
- **Blocage :** l’acceptation finale reste impossible tant qu’un point juridique est ouvert.

## 13. Intégrité des sources, livraisons et dépendances

Les empreintes ne prouvent pas la qualité, mais elles prouvent que les preuves se rapportent aux mêmes octets. Le rapport conserve les empreintes du candidat, du manifeste, du profil et des dépendances critiques.

La liste de dépendances Godot complète les dépendances déclarées. Toute différence doit être expliquée : une dépendance cachée ou manquante peut casser un checkout propre ou un export.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
integrity:
  candidate_sha256: <sha256>
  manifest_sha256: <sha256>
  qa_profile_sha256: <sha256>
  declared_dependencies:
    - res://assets/materials/scout_body.tres
    - res://assets/textures/scout_body_base_color.webp
  discovered_dependencies:
    - res://assets/materials/scout_body.tres
    - res://assets/textures/scout_body_base_color.webp
  dependency_diff: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Empreintes :** elles relient le rapport à des fichiers précis.
- **Déclaré :** le manifeste exprime l’intention de dépendance.
- **Découvert :** `ResourceLoader.get_dependencies()` peut compléter la vue après import.
- **Différence :** un écart est un constat à classifier, pas un détail ignoré.
- **Checkout propre :** la reproductibilité doit être vérifiée hors du cache local.

## 14. Checklist universelle et extensions par famille

La checklist universelle couvre les invariants communs : identité, droits, intégrité, dimensions, import, dépendances, budget, preuve Godot et décision. Une extension ajoute les contrôles propres à une famille sans dupliquer le socle.

Cette composition empêche une liste monolithique dans laquelle des critères audio, UI et rig deviennent des cases « non applicables » difficiles à auditer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
checklist_composition:
  universal_profile: AST-ASSET-QA-CHECKLIST-001
  family_profile: AST-ASSET-QA-PROFILE-CHARACTER-001
  optional_modules:
    - AST-ASSET-QA-MODULE-FACIAL-001
    - AST-ASSET-QA-MODULE-LOD-001
  merged_rule_order:
    - universal
    - family
    - optional_modules
  duplicate_rule_policy: reject
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Socle :** il garantit une acceptation cohérente entre toutes les familles.
- **Famille :** elle porte les règles spécifiques et les budgets associés.
- **Modules :** ils s’activent uniquement lorsqu’une capacité est réellement présente.
- **Ordre :** la fusion déterministe facilite la comparaison des rapports.
- **Doublon :** deux règles portant le même identifiant indiquent un conflit de gouvernance.

## 15. Profil de contrôle et identifiants de règles

Chaque règle possède un identifiant stable, une version, un niveau par défaut, des paramètres et une méthode de preuve. Le texte affiché peut évoluer sans casser les historiques.

Un profil ne contient pas seulement des seuils : il décrit aussi les conditions d’applicabilité, la source du budget et la manière de traiter une mesure indisponible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rule:
  id: AST-QA-GEO-TRIANGLES-001
  version: 1.2.0
  applies_when: family_in_character_or_creature
  default_severity: BLOCKER
  parameters:
    max_triangles_lod0: candidate_from_budget_registry
  evidence:
    kind: measured_integer
    source: imported_mesh_statistics
  unavailable_measurement: INDETERMINATE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** il reste comparable entre deux versions de rapport.
- **Applicabilité :** une règle non pertinente n’est pas artificiellement validée.
- **Paramètres :** les budgets proviennent d’un registre approuvé.
- **Preuve :** le type de valeur et sa source sont explicites.
- **Indéterminé :** une mesure absente n’est jamais convertie en succès.

## 16. Unités, échelle, axes et pivot

La validation compare les dimensions attendues, la transform de racine et le pivot à l’usage réel. Une dimension plausible ne suffit pas : un personnage peut avoir la bonne hauteur tout en portant une échelle négative ou un pivot inutilisable.

Les tolérances sont définies par famille et usage. Elles ne sont ni universelles ni dérivées d’un seul asset.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
spatial_contract:
  expected_unit: metre
  root_scale: [1.0, 1.0, 1.0]
  negative_scale_allowed: false
  expected_up_axis_in_godot: y
  expected_forward_axis_in_godot: minus_z
  bounds_m:
    min: [-0.6, 0.0, -0.4]
    max: [0.6, 1.9, 0.4]
  pivot_profile: character_feet_origin
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** les dimensions sont interprétées dans l’espace Godot final.
- **Échelle :** la racine normalisée évite des surprises de physique et d’animation.
- **Axes :** le rapport vérifie le résultat importé, pas seulement les réglages de l’outil auteur.
- **Bornes :** elles constituent une enveloppe candidate liée à la famille.
- **Pivot :** son profil décrit l’usage attendu, par exemple pieds, centre ou charnière.

## 17. Transforms appliquées et échelles négatives

Une hiérarchie peut sembler correcte dans une vue statique tout en contenant des transforms non appliquées, des inversions ou des cisaillements qui perturbent le skinning, les collisions et les sockets.

La porte distingue les transforms autorisées sur la scène d’intégration des transforms interdites dans la livraison importée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transform_checks:
  imported_root:
    translation_allowed: false
    rotation_allowed: false
    non_uniform_scale_allowed: false
    negative_determinant_allowed: false
  integration_root:
    translation_allowed: true
    rotation_allowed: true
    scale_policy: uniform_only
  child_exceptions:
    - rule_id: AST-QA-SOCKET-TRANSFORM-001
      scope: socket_nodes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine importée :** elle reste neutre pour préserver la reproductibilité.
- **Scène d’intégration :** elle peut placer l’asset sans modifier la livraison.
- **Déterminant négatif :** il signale une inversion susceptible de retourner normales et repères.
- **Exceptions :** elles sont ciblées par règle et non par tolérance implicite.

## 18. Géométrie, surfaces et topologie

Les contrôles techniques recensent sommets, indices, surfaces, matériaux et géométries vides. Les défauts de topologie nécessitant l’outil auteur restent signalés par un rapport Blender ou un validateur de format, puis liés au rapport Godot.

Une scène Godot ne doit pas prétendre détecter ce que son API ne mesure pas. La source de chaque constat est indiquée afin de distinguer inspection du format, inspection DCC et inspection runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
geometry_evidence:
  godot_import:
    mesh_count: 3
    surface_count: 5
    empty_surfaces: 0
    material_slots: 5
  gltf_validator:
    errors: 0
    warnings: candidate_to_review
  blender_source_report:
    non_manifold_edges: candidate_to_measure
    zero_area_faces: candidate_to_measure
evidence_sources_are_not_interchangeable: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Godot :** les statistiques portent sur les ressources réellement importées.
- **Validateur glTF :** il contrôle la conformité du conteneur et de la spécification.
- **Blender :** il peut produire des constats propres à la topologie source.
- **Séparation :** un résultat absent d’une source n’est pas inventé depuis une autre.
- **Décision :** les constats sont consolidés avec leur origine.

## 19. Budgets de sommets, triangles, surfaces et matériaux

Les budgets sont liés à une famille, un niveau de détail, une distance et une plateforme. Le nombre de primitives rendu par Godot peut dépasser le nombre de triangles du mesh à cause des passes de profondeur et d’ombre ; ces mesures ne sont donc pas interchangeables.

Le profil conserve à la fois les statistiques de contenu et les mesures de scène afin d’expliquer les écarts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
geometry_budget:
  profile_id: AST-BUDGET-CHAR-HERO-PC-001
  content:
    lod0_triangles_max: 90000
    lod0_surfaces_max: 8
    material_slots_max: 8
  scene_measurement:
    render_primitives_monitor: record_not_compare_to_mesh_triangles_directly
    draw_calls_max: candidate_to_measure
  platform: windows_forward_plus_reference
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le budget porte un identifiant et une plateforme.
- **Contenu :** les limites de maillage sont vérifiées avant la mesure runtime.
- **Primitives rendues :** elles incluent les passes et ne remplacent pas le compteur de triangles source.
- **Draw calls :** la valeur cible reste candidate jusqu’à mesure du pilote.
- **Révision :** un dépassement peut conduire à une correction ou à une dérogation documentée.

## 20. UV, densité de texels et chevauchements

La porte ne refait pas le dépliage du chapitre 17. Elle vérifie que les jeux UV attendus existent, que leur rôle est déclaré et que la densité observée se situe dans la plage du profil.

Les chevauchements sont parfois volontaires. Ils doivent alors être explicitement autorisés pour le canal concerné, faute de quoi ils restent un constat à corriger.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
uv_contract:
  channels:
    uv0:
      purpose: material_textures
      texel_density_px_per_m: candidate_from_family_profile
      overlap_policy: declared_only
    uv1:
      purpose: lightmap_or_secondary_data
      required: false
      overlap_policy: forbidden_when_used_for_lightmap
  missing_channel_severity: BLOCKER_when_required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canal :** chaque UV reçoit un usage compréhensible.
- **Densité :** la cible dépend de la distance et de la famille.
- **Chevauchement :** une superposition intentionnelle est déclarée plutôt que devinée.
- **UV secondaire :** son obligation dépend du pipeline réellement retenu.
- **Sévérité :** l’absence bloque uniquement lorsqu’un contrat l’exige.

## 21. Matériaux, slots et contrat PBR

La validation compare les slots attendus au manifeste et vérifie que les matériaux externes ou remappés du chapitre 28 sont utilisés. Un slot vide, un doublon involontaire ou un matériau embarqué non durable devient un constat explicite.

La conformité PBR porte sur les canaux et espaces colorimétriques attendus, pas sur une apparence isolée sous un seul éclairage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
material_contract:
  expected_slots:
    - body
    - eyes
    - hair
  external_materials_required: true
  embedded_materials_allowed: false
  pbr_channels:
    base_color: srgb
    normal: linear
    roughness: linear
    metallic: linear
    ambient_occlusion: linear
  empty_slot_policy: blocker
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Slots :** leurs identifiants sont comparés au manifeste de livraison.
- **Ressources externes :** elles préservent les remaps à travers la réimportation.
- **Espaces :** les cartes de données ne sont pas interprétées comme des couleurs.
- **Slot vide :** il peut produire une apparence différente selon la scène.
- **Revue :** la plausibilité matérielle reste contrôlée sous plusieurs éclairages.

## 22. Textures, dimensions, canaux et import

Chaque texture est contrôlée selon son usage : dimensions, ratio, alpha, espace colorimétrique, compression, répétition et dépendances. Une résolution élevée n’est pas automatiquement un gage de qualité.

Les paramètres importés sont comparés au profil du chapitre 28. Le chapitre 29 constate les écarts et leur effet ; il ne modifie pas silencieusement les sidecars.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
texture_checks:
  base_color:
    dimensions_power_of_two_required: false
    max_dimension: candidate_from_platform_profile
    color_space: srgb
    alpha_expected: false
  normal:
    color_space: linear
    normal_map_import: true
  masks:
    color_space: linear
    packed_channels_manifested: true
  import_changes_during_review: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Usage :** le rôle de la texture sélectionne les règles pertinentes.
- **Dimensions :** les limites viennent du budget de plateforme.
- **Normal map :** le profil d’import doit reconnaître la carte comme donnée normale.
- **Canaux empaquetés :** leur signification est conservée dans le manifeste.
- **Immutabilité :** un changement d’import exige une nouvelle révision du candidat.

## 23. Transparence, découpe et risque d’overdraw

La transparence augmente souvent le coût et peut compliquer le tri. La porte recense les matériaux transparents, leur couverture écran prévue et la possibilité d’utiliser une découpe alpha ou une solution opaque.

Le nombre de matériaux transparents est un indicateur, pas une mesure d’overdraw. La scène de validation doit conserver des vues représentatives avant toute conclusion de performance.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transparency_review:
  materials:
    - id: scout_hair
      mode: alpha_scissor
      expected_screen_coverage: bounded
    - id: relay_hologram
      mode: alpha_blend
      expected_screen_coverage: scene_specific
  checks:
    - transparent_surface_count
    - sorting_artifacts
    - silhouette_quality
    - representative_camera_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Modes :** la découpe et le mélange possèdent des compromis différents.
- **Couverture :** le coût dépend de la portion d’écran et des couches superposées.
- **Artefacts :** le tri et les intersections sont revus visuellement.
- **Mesure :** une vue représentative est nécessaire pour interpréter les coûts.
- **Décision :** la solution la plus simple compatible avec l’intention est privilégiée.

## 24. Squelette, hiérarchie et pose de repos

Pour un personnage, la porte compare la liste d’os, la hiérarchie, la racine, la pose de repos et les conventions de nommage au manifeste du rig. Un simple chargement réussi ne prouve pas la compatibilité avec les animations.

Les os supplémentaires sont autorisés uniquement lorsqu’ils sont déclarés et compatibles avec le profil de retargeting.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skeleton_contract:
  root_bone: Root
  deformation_root: Hips
  required_bones_manifest: AST-RIG-SCOUT-001
  unexpected_bone_policy: review
  duplicate_bone_names: blocker
  rest_pose_hash: <canonical_pose_hash>
  negative_bone_scale: forbidden
  retarget_profile: AST-RETARGET-HUMANOID-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racines :** la racine de scène et la racine de déformation restent distinguées.
- **Manifeste :** les os requis proviennent du rig approuvé.
- **Pose de repos :** son empreinte aide à détecter un export incohérent.
- **Échelle :** les inversions sur les os peuvent produire des déformations instables.
- **Retargeting :** la compatibilité est vérifiée contre un profil explicite.

## 25. Skinning, influences et déformations

Les statistiques de poids contrôlent les sommets non pondérés, les influences excessives et les poids non normalisés. Elles doivent être complétées par des poses de test, car une distribution mathématiquement valide peut rester visuellement mauvaise.

Les poses extrêmes sont choisies selon les zones à risque : épaules, hanches, genoux, poignets, mâchoire et accessoires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skinning_gate:
  max_influences_per_vertex: candidate_from_renderer_profile
  unweighted_vertices_max: 0
  normalized_weights_required: true
  test_poses:
    - arms_up
    - deep_crouch
    - wrist_twist
    - jaw_open
  visual_checks:
    - volume_preservation
    - collapsing
    - candy_wrapper_twist
    - accessory_intersection
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Influences :** la limite doit correspondre au pipeline d’export et de rendu.
- **Sommets non pondérés :** ils constituent un blocage pour un mesh déformé.
- **Normalisation :** la somme des poids doit être cohérente.
- **Poses :** elles exposent les défauts absents de la pose neutre.
- **Visuel :** la revue humaine reste nécessaire pour juger les volumes.

## 26. Blendshapes et canaux faciaux

La porte vérifie les noms, le nombre, la pose neutre, les amplitudes et les correctifs attendus par le profil facial. Elle ne recrée pas le jeu de visèmes du chapitre 27.

Un canal présent mais inutilisable, inversé ou saturé est distingué d’un canal absent. Les tests utilisent des valeurs bornées et des combinaisons représentatives.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_gate:
  viseme_set: AST-FACE-VISEME-SET-001
  required_shapes:
    - neutral
    - jaw_open
    - lips_closed
    - lips_round
    - lips_wide
  duplicate_names: blocker
  neutral_nonzero_channels: blocker
  test_values: [0.0, 0.5, 1.0]
  combination_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Jeu :** le chapitre 27 reste l’autorité des formes et mappings.
- **Neutre :** aucun canal résiduel ne doit déformer la pose de référence.
- **Amplitude :** plusieurs valeurs révèlent les non-linéarités et saturations.
- **Combinaisons :** parole et expression sont testées ensemble.
- **Résultat :** les écarts sont rapportés sans modifier le rig pendant la revue.

## 27. Inventaire d’animations, durées et boucles

L’inventaire compare les clips attendus, leurs durées, plages, boucles et pistes au manifeste d’animation. Une animation supplémentaire ou manquante n’est pas ignorée.

La porte contrôle aussi les ressources externes ou bibliothèques retenues après import, afin que le rapport vise ce que Godot jouera réellement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_inventory:
  expected:
    idle:
      loop: true
      duration_s: candidate_range
    walk:
      loop: true
      duration_s: candidate_range
    interact_relay:
      loop: false
      duration_s: candidate_range
  unexpected_clip_policy: review
  missing_clip_policy: blocker
  source_library: AST-ANIM-LIB-SCOUT-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clips :** les noms stables sont comparés à la livraison approuvée.
- **Boucle :** son statut est une propriété du contrat, pas une déduction par durée.
- **Durée :** les plages candidates détectent des exports tronqués ou étirés.
- **Bibliothèque :** le rapport pointe vers la ressource réellement intégrée.
- **Écart :** tout clip inattendu doit être expliqué ou retiré.

## 28. Root motion, pistes et événements

Le root motion est comparé au profil de déplacement et aux conventions du chapitre 20. Les événements d’animation restent des signaux de présentation ou des repères ; ils ne deviennent pas une autorité métier.

Les pistes visant des chemins absents, des propriétés inattendues ou des nœuds de gameplay constituent des blocages.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_track_gate:
  root_motion:
    enabled_for: [walk, run]
    source_bone: Root
    drift_tolerance: candidate_from_animation_profile
  forbidden_targets:
    - gameplay_state
    - inventory
    - quest_progress
  missing_node_track: blocker
  event_tracks:
    allowed: [footstep_marker, vfx_marker, audio_marker]
    authority: presentation_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Root motion :** sa source et ses clips autorisés sont explicités.
- **Dérive :** la tolérance dépend du profil et doit être mesurée.
- **Cibles interdites :** une piste ne peut pas modifier un système métier.
- **Repères :** les événements déclenchent des présentations après décision autoritaire.
- **Chemins manquants :** ils révèlent une incompatibilité d’intégration.

## 29. Collisions et profils physiques

La validation compare le type de collision à l’usage : statique, dynamique, zone, navigation ou simple sélection. Le mesh de rendu ne doit pas devenir automatiquement une collision dynamique complexe.

Les couches, masques, transforms et matériaux physiques sont inspectés dans la scène d’intégration, car ils appartiennent au contexte Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
collision_gate:
  relay_module:
    body_type: StaticBody3D
    shape_policy: compound_primitives_or_simplified_convex
    render_mesh_as_shape: forbidden
    layers: [environment]
    masks: [player, projectile]
  scout:
    body_type: CharacterBody3D
    shape_policy: capsule
    bone_attached_hitboxes: separate_profile
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** le corps correspond à la mobilité et à l’autorité physique.
- **Forme :** la collision reste plus simple que le mesh de rendu.
- **Couches :** elles sont comparées au contrat du projet.
- **Personnage :** la capsule de locomotion reste distincte des hitboxes éventuelles.
- **Scène :** les réglages sont validés après intégration, pas seulement dans la livraison.

## 30. Sockets, marqueurs et métadonnées

Les sockets sont des transforms de présentation. La porte vérifie leur nom, parent, transform local et profil d’usage, mais ne les traite jamais comme identité d’objet ou permission d’équipement.

Les métadonnées sont limitées à une liste autorisée. Une clé inconnue peut révéler une donnée d’outil oubliée ou une tentative de contourner les contrats du projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
socket_gate:
  profile: AST-SOCKET-PROFILE-SCOUT-001
  required:
    hand_r:
      parent_bone: Hand.R
      usage: visual_attachment
    back:
      parent_bone: Spine.03
      usage: visual_attachment
  metadata_allowlist:
    - asset_id
    - source_revision
    - profile_id
  unknown_metadata: blocker
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Socket :** il localise un attachement visuel après décision métier.
- **Parent :** la hiérarchie est comparée au rig approuvé.
- **Transform :** les écarts sont mesurés dans l’espace local attendu.
- **Métadonnées :** la liste fermée empêche les conventions parallèles.
- **Autorité :** l’existence d’un socket ne crée aucun objet équipé.

## 31. Chaîne LOD, monotonie et cohérence

Une chaîne LOD est validée comme un ensemble ordonné. Les coûts doivent diminuer avec la distance, les matériaux et collisions doivent suivre le profil, et l’identité visuelle doit rester reconnaissable.

La porte distingue la monotonie technique de l’acceptabilité perceptuelle : une réduction régulière des triangles ne garantit pas une silhouette satisfaisante.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
lod_gate:
  levels:
    - id: LOD0
      triangles: candidate_measure
      materials: candidate_measure
    - id: LOD1
      triangles: candidate_measure
      materials: candidate_measure
    - id: LOD2
      triangles: candidate_measure
      materials: candidate_measure
  monotonic_requirements:
    triangles: strictly_decreasing
    materials: non_increasing
  silhouette_review: required
  distance_profile: AST-LOD-PROFILE-SCOUT-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** les niveaux sont comparés selon leur usage à distance.
- **Monotonie :** triangles et matériaux ne doivent pas remonter sans justification.
- **Profil :** les seuils de distance proviennent du chapitre 18.
- **Silhouette :** une capture par caméra de référence conserve la preuve perceptuelle.
- **Décision :** un LOD peut passer la technique et échouer la revue artistique.

## 32. VFX, particules et effets dépendants

Les VFX sont validés selon leur fonction, leur profil de qualité, leur population bornée et leur lisibilité. Le chapitre 23 reste propriétaire des techniques de particules et de shaders.

La porte du chapitre 29 vérifie la présence des profils attendus, la conservation de l’information critique et les preuves de mesure dans les vues prévues.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
vfx_gate:
  effect_id: AST-VFX-IMPACT-METAL-001
  required_profiles: [low, reference, high]
  critical_information_preserved: review_required
  population_limits_manifested: true
  visibility_bounds_reviewed: candidate
  overdraw_capture_required: true
  gameplay_authority: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** les variantes conservent la fonction malgré la réduction du coût.
- **Limites :** population et durée de vie sont des contrats vérifiables.
- **Bornes :** la visibilité doit être qualifiée dans la scène réelle.
- **Capture :** la couverture écran et l’overdraw nécessitent des vues représentatives.
- **Autorité :** l’effet ne décide jamais l’impact ou le dégât.

## 33. UI, icônes et assets d’interface

Les assets UI sont contrôlés avec les règles des chapitres 24 et 25 : dimensions, marges, états, lisibilité, contraste, focus, localisation et codages redondants.

Une icône ne peut pas être acceptée uniquement à sa taille source. La porte exige des captures aux échelles et ratios prévus, avec les textes et états réels.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ui_asset_gate:
  icon_set: AST-UI-ICON-CORE-001
  required_states: [default, hover, pressed, disabled, focused]
  scales: [1.0, 1.25, 1.5, 2.0]
  ratios: ["16:9", "16:10", "21:9", "4:3"]
  color_only_meaning: forbidden
  long_text_fixture: required
  pseudo_localization_fixture: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** les variantes interactives appartiennent au contrat de composant.
- **Échelles :** les contours et détails sont revus à plusieurs tailles.
- **Ratios :** la validation inclut les zones sûres et le reflow.
- **Redondance :** la couleur ne porte jamais seule une information critique.
- **Texte :** la pseudo-localisation révèle les assets trop dépendants d’un libellé court.

## 34. Audio, voix et livrables sonores

Les assets audio sont contrôlés avec le manifeste du chapitre 26 : format, canaux, durée, boucle, loudness mesuré, crête vraie, provenance et stratégie de lecture.

La porte ne fixe pas une cible universelle. Elle vérifie que la mesure a été réalisée selon le profil, que les variations sont cohérentes et que les limites de voix simultanées sont documentées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_asset_gate:
  stream_id: AST-AUDIO-RELAY-WIND-001
  format_profile: AST-AUDIO-PROFILE-AMBIENCE-001
  channels_expected: stereo
  loop_points_samples: required
  loudness_report: required
  true_peak_report: required
  licence_record: required
  concurrency_profile: AST-AUDIO-CONCURRENCY-AMBIENCE-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** le profil décrit la compression et les canaux attendus.
- **Boucle :** les points en échantillons sont conservés avec la source.
- **Mesures :** loudness et crête vraie sont lues depuis un rapport réel.
- **Droits :** la provenance reste une précondition de publication.
- **Concurrence :** la validation d’un fichier ne remplace pas le test de mix en scène.

## 35. Architecture de la scène Godot de validation

La scène `AST-ASSET-QA-SCENE-001` fournit un environnement stable : éclairage neutre, repère d’échelle, caméras nommées, surfaces de référence et emplacements dédiés aux tests. Elle charge la scène d’intégration, jamais la source brute.

Les fixtures sont composées pour être réutilisables. Le pilote ne doit pas devenir une scène de gameplay ni dépendre d’Autoloads inutiles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
validation_scene:
  id: AST-ASSET-QA-SCENE-001
  path: res://scenes/validation/assets/asset_quality_gate.tscn
  root: Node3D
  fixtures:
    - neutral_lighting
    - scale_reference
    - material_reference
    - animation_rig
    - collision_socket
    - lod_distance
  candidate_mount: CandidateRoot
  gameplay_dependencies: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scène :** elle possède un identifiant et un chemin stable.
- **Fixtures :** chaque module isole une famille de constats.
- **Montage :** le candidat est instancié sous un nœud connu.
- **Dépendances :** la scène reste autonome et reproductible.
- **Limite :** elle n’exécute aucune logique métier du jeu.

## 36. Éclairage neutre, surfaces et caméras de référence

L’éclairage de contrôle doit rendre visibles les défauts sans fabriquer une apparence cinématique. Plusieurs configurations révèlent les normales, la rugosité, les silhouettes et les transparences.

Les caméras portent des transforms versionnées. Une capture n’est comparable que si la caméra, l’éclairage, le renderer, la résolution et le profil sont enregistrés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
visual_fixture:
  environments:
    - neutral_soft
    - grazing_light
    - high_contrast
    - flat_color_debug
  cameras:
    - full_body_front
    - full_body_side
    - close_face
    - material_detail
    - gameplay_distance
  capture_metadata:
    - renderer
    - resolution
    - camera_transform
    - environment_id
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Éclairages :** les variantes exposent des défauts différents.
- **Caméras :** elles couvrent inspection rapprochée et usage réel.
- **Métadonnées :** elles rendent la capture reproductible.
- **Comparaison :** une différence de fixture ne doit pas être interprétée comme une différence d’asset.
- **Artistique :** la scène neutre complète, sans remplacer, les scènes d’ambiance.

## 37. Fixture d’échelle, pivot et orientation

La fixture affiche une grille métrique, une silhouette humaine de référence et des axes visibles. Elle permet de vérifier rapidement dimensions, origine, orientation et comportement lors d’une rotation.

Les valeurs observées sont également consignées dans le rapport ; la capture seule ne suffit pas pour une porte automatisable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
scale_fixture:
  grid_spacing_m: 1.0
  reference_objects:
    - human_1_80m
    - cube_1m
  axis_gizmo: true
  turntable_angles_deg: [0, 90, 180, 270]
  measurements:
    - aabb_size
    - root_transform
    - pivot_world_position
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Grille :** elle donne un repère visuel immédiatement compréhensible.
- **Références :** plusieurs formes réduisent les erreurs d’interprétation.
- **Rotation :** elle expose les axes inversés et pivots excentrés.
- **Mesures :** les données numériques complètent la preuve visuelle.
- **Tolérance :** le profil de famille décide de l’acceptabilité.

## 38. Fixture de matériaux et de textures

La fixture de lookdev alterne fonds clairs, sombres et colorés, puis éclaire le candidat sous plusieurs angles. Elle révèle coutures, normal maps inversées, roughness extrême et problèmes de transparence.

Les matériaux de la fixture sont des références du banc de test, pas des remplacements des matériaux du candidat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
material_fixture:
  backdrops: [middle_gray, near_black, near_white, saturated_blue]
  light_angles_deg: [15, 45, 80]
  debug_modes:
    - albedo_only
    - normals
    - roughness
    - metallic
    - uv_checker
  candidate_material_override: forbidden_in_acceptance_capture
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonds :** ils révèlent halos, franges et pertes de contraste.
- **Angles :** la lumière rasante montre les défauts de normales.
- **Modes :** les vues de données facilitent le diagnostic.
- **Override :** une capture d’acceptation conserve les matériaux réellement livrés.
- **Correction :** les modifications se font dans une nouvelle révision de source.

## 39. Fixture d’animation, de rig et de visage

La fixture exécute une liste fermée de clips et poses, à vitesse contrôlée. Elle compare les os, blendshapes et pistes à leurs manifestes avant la lecture.

La lecture sert à observer la déformation et les transitions ; elle ne déclenche aucun événement gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_fixture:
  clips:
    - idle
    - walk
    - interact_relay
  test_poses:
    - arms_up
    - deep_crouch
    - wrist_twist
  facial_tests:
    - viseme_sequence
    - blink
    - brow_asymmetry
  playback_speed: 1.0
  gameplay_signals_connected: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liste fermée :** les clips testés sont connus et versionnés.
- **Poses :** elles ciblent les zones de déformation à risque.
- **Visage :** les canaux sont testés seuls puis combinés.
- **Vitesse :** la comparaison évite des lectures accélérées ou ralenties.
- **Isolation :** la scène de validation ne connecte aucun signal métier.

## 40. Fixture de collisions, sockets et interactions visuelles

La fixture affiche les formes de collision, teste des raycasts de diagnostic et instancie des marqueurs visuels sur les sockets. Elle ne simule pas l’inventaire ou les permissions.

Les résultats portent sur présence, type, transform et intersection. Un test de collision réussi ne valide pas automatiquement le ressenti ou l’équilibrage du jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
collision_socket_fixture:
  collision_debug_visible: true
  probes:
    - floor_contact
    - doorway_clearance
    - projectile_line
  socket_markers:
    - hand_r
    - back
  attachment_assets: diagnostic_primitives_only
  domain_actions: disabled
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Debug :** les formes sont visibles sans modifier leur configuration.
- **Sondes :** des trajectoires connues exposent les volumes incohérents.
- **Marqueurs :** des primitives simples montrent position et orientation des sockets.
- **Isolation :** aucun objet d’inventaire réel n’est créé.
- **Portée :** la fixture valide le contrat d’asset, pas le gameplay complet.

## 41. Fixture de distance et de transition LOD

La fixture LOD place des caméras à des distances contrôlées et enregistre le niveau attendu, la taille écran et les différences visibles. Les transitions sont observées en approche et en éloignement afin de contrôler l’hystérésis.

Le banc de test ne change pas les seuils pour obtenir une capture favorable. Toute modification du profil produit une nouvelle version et une nouvelle campagne.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
lod_fixture:
  camera_distances_m: [2, 5, 10, 20, 40]
  directions: [approach, retreat]
  record:
    - active_lod
    - screen_coverage
    - transition_frame
    - silhouette_capture
  profile_changes_during_run: forbidden
  hysteresis_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distances :** elles correspondent aux usages prévus du profil.
- **Directions :** l’approche et le recul révèlent l’hystérésis.
- **Enregistrement :** niveau, couverture et capture sont corrélés.
- **Immutabilité :** le profil reste figé pendant la campagne.
- **Revue :** le popping reste une appréciation visuelle documentée.

## 42. Collecte de moniteurs avec Godot

Godot expose des moniteurs de performance pour le temps de frame, les objets, les ressources, les primitives, les draw calls et certaines mémoires. Ces valeurs décrivent la scène complète au moment de la mesure.

Le script ci-dessous prépare un échantillon minimal. Il ne soustrait pas automatiquement le coût de la fixture et ne prétend pas isoler parfaitement l’asset.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
extends Node

func capture_render_sample() -> Dictionary:
    return {
        "fps": Performance.get_monitor(Performance.TIME_FPS),
        "frame_time_s": Performance.get_monitor(Performance.TIME_PROCESS),
        "objects": Performance.get_monitor(Performance.RENDER_TOTAL_OBJECTS_IN_FRAME),
        "primitives": Performance.get_monitor(
            Performance.RENDER_TOTAL_PRIMITIVES_IN_FRAME
        ),
        "draw_calls": Performance.get_monitor(
            Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME
        ),
        "video_mem_bytes": Performance.get_monitor(
            Performance.RENDER_VIDEO_MEM_USED
        ),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Retour :** la fonction produit un `Dictionary` sérialisable pour un échantillon.
- **Moniteurs :** les constantes visent les valeurs de la dernière frame rendue ou de la dernière seconde selon le cas.
- **Primitives :** la valeur inclut les passes de rendu et ne correspond pas directement aux triangles source.
- **Mémoire :** la mesure inclut des allocations de la scène et du moteur.
- **Limite :** une campagne contrôlée doit établir la baseline de la fixture.

## 43. Protocole de mesure, chauffe et répétitions

Une mesure exploitable fixe le binaire, le renderer, la résolution, la caméra, la fixture et la durée. Elle sépare la chauffe, la collecte et la synthèse.

Les répétitions servent à estimer la variabilité. La médiane est souvent plus robuste qu’un unique minimum favorable, mais le choix statistique doit être documenté.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
measurement_protocol:
  engine: Godot_4.7.1_standard
  renderer: forward_plus
  resolution: [1920, 1080]
  warmup_frames: candidate_to_measure
  sample_frames: candidate_to_measure
  repetitions: candidate_to_measure
  aggregation:
    frame_time: median_and_percentiles
    draw_calls: median_and_max
    memory: stabilized_range
  fixture_baseline: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** les paramètres rendent deux campagnes comparables.
- **Chauffe :** elle limite l’effet des imports, caches et compilations initiales.
- **Répétitions :** elles montrent la variabilité au lieu de cacher un pic.
- **Agrégation :** chaque métrique utilise une synthèse adaptée.
- **Baseline :** le coût du banc de test est enregistré séparément.

## 44. Baseline, tolérances et comparaison

Une baseline est une campagne acceptée, liée à une révision, un profil et un environnement. Elle n’est pas un fichier magique à mettre à jour dès qu’un test échoue.

Les tolérances distinguent bruit de mesure, amélioration et régression. Leur justification est conservée avec la règle et révisée lorsque le matériel ou le renderer change.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
baseline:
  id: AST-ASSET-QA-BASELINE-SCOUT-001
  candidate_version: 0.6.0
  environment_profile: AST-PC-REF-FORWARDPLUS-001
  metrics:
    draw_calls: measured_value
    primitives: measured_value
    frame_time_ms: measured_distribution
  tolerances:
    draw_calls_delta_max: candidate
    frame_time_relative_delta_max: candidate
  update_requires: explicit_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la baseline est reliée à un candidat et un environnement précis.
- **Distribution :** le temps de frame conserve davantage qu’une moyenne.
- **Tolérances :** elles sont des paramètres approuvés, pas des ajustements opportunistes.
- **Mise à jour :** une personne examine la cause avant de remplacer la référence.
- **Historique :** les baselines précédentes restent consultables.

## 45. Captures visuelles et nomenclature

Les captures sont des preuves comparatives. Leur nom et leur manifeste doivent indiquer candidat, caméra, environnement, profil, résolution et frame.

Une image recadrée ou retouchée peut servir à expliquer un défaut, mais elle ne remplace pas la capture brute d’acceptation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
capture_record:
  asset_id: AST-CHAR-SCOUT-001
  candidate_version: 0.7.0-rc.2
  camera_id: full_body_front
  environment_id: neutral_soft
  resolution: [1920, 1080]
  renderer: forward_plus
  file: captures/scout/0.7.0-rc.2/full_body_front_neutral_soft.png
  raw_capture: true
  annotations_file: optional_separate_overlay
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** les éléments essentiels sont aussi stockés dans le manifeste.
- **Brut :** l’image d’acceptation reste non retouchée.
- **Annotation :** les commentaires vivent dans un calque ou fichier séparé.
- **Comparabilité :** caméra et environnement identiques permettent une revue avant/après.
- **Droits :** les captures suivent les restrictions de l’asset représenté.

## 46. Grille de revue artistique

La revue artistique transforme la bible visuelle en questions observables : silhouette, proportions, langage de formes, matériaux, palette, lisibilité, finition et adéquation au contexte.

La grille ne réduit pas l’art à une somme mécanique. Elle structure les observations et exige une justification reliée à une référence, une règle ou un usage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
art_review_rubric:
  silhouette:
    question: readable_at_gameplay_distance
    evidence: gameplay_distance_capture
  proportions:
    question: consistent_with_species_and_role
    evidence: scale_fixture_capture
  materials:
    question: coherent_with_asteria_material_language
    evidence: material_fixture_set
  palette:
    question: functional_and_region_consistent
    evidence: bible_reference_ids
  finish:
    question: appropriate_for_target_maturity
    evidence: closeup_review
rating_scale: [conform, minor_deviation, major_deviation, indeterminate]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Questions :** elles décrivent un fait à observer plutôt qu’un goût vague.
- **Preuves :** chaque jugement renvoie à une capture ou une référence.
- **Échelle :** elle distingue conformité, écart et manque de preuve.
- **Maturité :** un prototype n’est pas jugé comme un asset de livraison.
- **Décision :** les écarts majeurs deviennent des demandes de correction.

## 47. Comparer à la bible et aux références approuvées

La comparaison cite des identifiants de planches, palettes et exemples approuvés. Une référence externe non qualifiée ne peut pas devenir silencieusement la norme d’acceptation.

Les écarts autorisés sont documentés. Une variation culturelle, régionale ou narrative peut être conforme si elle respecte le cadre de dérogation défini par la bible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reference_comparison:
  visual_bible_version: 1.0.0
  reference_ids:
    - AST-BIBLE-SILHOUETTE-SCOUT-001
    - AST-BIBLE-PALETTE-RELAY-001
    - AST-BIBLE-MATERIAL-WEATHERED-METAL-001
  approved_deviations:
    - id: AST-ART-DEVIATION-STORM-WETNESS-001
      scope: relay_storm_scene
      rationale: narrative_weather_condition
  untracked_reference_policy: reject
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** la revue indique quelle bible a servi de norme.
- **Identifiants :** les planches et palettes sont retrouvables.
- **Dérogation :** elle possède un périmètre et une justification.
- **Référence externe :** elle doit d’abord entrer dans le registre de provenance.
- **Résultat :** la comparaison reste reproductible par une autre personne.

## 48. Dérogations et acceptation avec réserve

Une dérogation accepte temporairement un écart connu lorsque le risque est compris et limité. Elle ne transforme pas un défaut en conformité générale.

La dérogation possède un propriétaire, une portée, une échéance ou condition de retrait, ainsi qu’un plan de correction. Une dérogation sans limite est un changement de règle qui doit être traité comme tel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
waiver:
  id: AST-WAIVER-SCOUT-LOD1-001
  finding_id: AST-FINDING-LOD-SILHOUETTE-014
  scope:
    asset_id: AST-CHAR-SCOUT-001
    candidate_version: 0.7.0-rc.2
    platform: windows_reference
  owner: art_lead
  rationale: vertical_slice_schedule
  expires_on: next_candidate_revision
  correction_plan: simplify_cape_preserving_outer_contour
  status: approved
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** la dérogation vise un constat précis.
- **Portée :** elle ne s’étend pas à d’autres assets ou plateformes.
- **Propriétaire :** une personne assume le risque et le suivi.
- **Expiration :** la prochaine révision réouvre automatiquement le point.
- **Plan :** l’écart possède une voie de résolution.

## 49. Constats, sévérités et codes stables

Un constat décrit une observation, la règle concernée, les preuves, la sévérité et l’action attendue. La sévérité n’est pas une émotion : elle dépend de l’effet sur publication, usage, coût ou droits.

Les codes stables permettent d’agréger les rapports sans dépendre du texte traduit.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
finding:
  id: AST-FINDING-SCOUT-00042
  rule_id: AST-QA-RIG-RESTPOSE-001
  code: RIG_REST_POSE_MISMATCH
  severity: BLOCKER
  observation: imported_rest_pose_hash_differs_from_manifest
  evidence:
    - report://skeleton_manifest_diff.json
    - capture://scout/arms_up.png
  expected_action: reexport_from_approved_rest_pose
  status: OPEN
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le constat peut être suivi à travers les échanges.
- **Règle :** elle explique le critère appliqué.
- **Code :** il reste stable même si le message évolue.
- **Preuves :** elles permettent de reproduire et comprendre l’observation.
- **Action :** la correction attendue reste distincte de la décision finale.

## 50. Schéma du rapport d’asset

Le rapport consolide les résultats sans écraser leurs sources. Il conserve le candidat, les profils, l’environnement, les constats, les décisions, les dérogations et les empreintes.

Les sections absentes sont explicites. Un rapport ne doit pas afficher `0` lorsqu’une campagne n’a pas été exécutée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_report:
  schema: project-asteria-asset-qa-report
  schema_version: 1
  report_id: AST-ASSET-QA-REPORT-SCOUT-0007
  candidate:
    asset_id: AST-CHAR-SCOUT-001
    version: 0.7.0-rc.2
    sha256: <sha256>
  profiles:
    checklist: AST-ASSET-QA-CHECKLIST-001
    family: AST-ASSET-QA-PROFILE-CHARACTER-001
  executions:
    technical: not_executed
    runtime: not_executed
    artistic: not_performed
  findings: []
  waivers: []
  decisions: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** le nom et la version permettent des migrations futures.
- **Candidat :** le rapport vise une révision immuable.
- **Profils :** les règles utilisées sont conservées.
- **Exécutions :** les statuts distinguent absence de campagne et succès.
- **Listes :** constats, dérogations et décisions restent append-only.

## 51. Boucle de correction et nouvelle révision

Une correction ne modifie pas le candidat en place. Le propriétaire produit une nouvelle révision, cite les constats visés et explique les changements attendus.

La porte relance les contrôles affectés et un ensemble de non-régression. Fermer un constat sans nouvelle preuve ou parce que le fichier a été remplacé détruit la traçabilité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rework_submission:
  previous_candidate: 0.7.0-rc.2
  new_candidate: 0.7.0-rc.3
  addressed_findings:
    - AST-FINDING-SCOUT-00042
    - AST-FINDING-SCOUT-00047
  expected_changes:
    - restore_approved_rest_pose
    - reduce_lod1_cape_popping
  rerun:
    targeted_rules: [rig_rest_pose, lod_silhouette]
    regression_modules: [universal, character_core]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Révision :** le candidat précédent reste consultable.
- **Constats :** la soumission indique ce qu’elle prétend corriger.
- **Changements :** les attentes préparent le diff et la revue.
- **Relance ciblée :** les contrôles coûteux peuvent être limités sans supprimer le socle.
- **Non-régression :** la correction ne doit pas casser un contrat déjà validé.

## 52. Décisions, signatures et acceptation finale

La décision finale porte sur un candidat, un rapport et une version de profil. Elle indique qui accepte, dans quel rôle, à quelle date et pour quel périmètre.

Une acceptation devient invalide lorsque l’empreinte du candidat, les droits, le profil obligatoire ou une dépendance critique change.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
final_decision:
  candidate:
    asset_id: AST-CHAR-SCOUT-001
    version: 0.7.0-rc.3
    sha256: <sha256>
  report_id: AST-ASSET-QA-REPORT-SCOUT-0008
  status: ACCEPTED
  approvals:
    technical: reviewer_id
    artistic: reviewer_id
    rights: reviewer_id
    release_owner: reviewer_id
  valid_for:
    platform_profiles: [windows_reference]
    usage: [gameplay_mid, cinematic_closeup]
  invalidation_on: [candidate_change, rights_change, required_profile_change]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Candidat :** la signature vise des octets précis.
- **Rapport :** les preuves et constats restent accessibles.
- **Approbations :** les rôles sont enregistrés même si certaines personnes se répètent.
- **Périmètre :** l’acceptation n’est pas universelle par défaut.
- **Invalidation :** les changements significatifs rouvrent la porte.

## 53. Parcours Mode Solo

En Solo, une seule personne peut préparer, contrôler et accepter l’asset. Pour réduire le biais, elle fige le candidat, exécute la checklist, attend une session distincte avant la revue artistique et relit le rapport comme si elle recevait le travail d’un tiers.

Le parcours conserve peu de statuts, mais ne supprime ni les droits, ni les mesures, ni la preuve Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
solo_workflow:
  steps:
    - freeze_candidate
    - run_universal_and_family_checks
    - capture_validation_scene
    - wait_for_separate_art_review_session
    - classify_findings
    - correct_or_document_waiver
    - issue_final_decision
  minimum_roles_recorded:
    - asset_owner
    - technical_reviewer
    - artistic_reviewer
    - release_owner
  same_person_allowed: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gel :** la revue porte sur une révision stable.
- **Séparation temporelle :** elle limite l’auto-justification immédiate.
- **Rôles :** le contexte de décision reste visible.
- **Dérogation :** elle suit les mêmes exigences qu’en Studio.
- **Porte :** l’absence d’équipe ne réduit pas les préconditions d’acceptation.

## 54. Parcours Mode Studio

En Studio, les propriétaires, valideurs et responsables de publication sont identifiés par famille. La double validation technique et artistique évite qu’un seul tableau mélange conformité de format, opinion artistique et décision de livraison.

Les délais de correction sont des objectifs de service internes. Ils ne modifient ni la sévérité d’un constat ni les critères d’acceptation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
studio_workflow:
  owners:
    asset: character_team
    technical_review: tech_art
    artistic_review: art_direction
    rights_review: production_legal
    release_decision: content_release_owner
  review_policy:
    technical_and_artistic_independent: true
    blocker_requires_rejection: true
    waiver_requires_owner_and_expiry: true
  correction_sla:
    blocker: project_policy
    major: project_policy
    minor: project_policy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaires :** chaque étape possède un interlocuteur responsable.
- **Indépendance :** les revues conservent leurs critères propres.
- **Blocage :** un délai court ne transforme pas un blocker en acceptation.
- **SLA :** les durées viennent de la politique de production.
- **Publication :** le responsable final vérifie la complétude des décisions.

## 55. Historique, conservation et confidentialité

Les rapports, captures, mesures et décisions sont conservés selon leur utilité et leurs droits. Les fichiers sensibles, identités personnelles ou sources non redistribuables ne sont pas publiés dans un dépôt public.

Le rapport public peut conserver des identifiants, empreintes et statuts tout en pointant vers une archive interne contrôlée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
retention_policy:
  public_repository:
    allowed:
      - redacted_report
      - rule_ids
      - candidate_hashes_when_non_sensitive
      - decision_status
    forbidden:
      - personal_data
      - confidential_source_files
      - restricted_reference_images
      - private_licence_documents
  internal_archive:
    access: role_based
    retention: project_policy
    deletion_events: logged
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Public :** seules les preuves redistribuables sont versionnées.
- **Interne :** les documents restreints restent sous contrôle d’accès.
- **Rédaction :** les identités ou informations sensibles sont supprimées des exports.
- **Conservation :** la durée dépend du risque, des droits et de la politique du projet.
- **Suppression :** un retrait est journalisé sans réécrire les décisions historiques.

## 56. Préparer l’automatisation du chapitre 30

La porte du chapitre 29 expose des entrées, sorties et codes stables afin que le chapitre 30 puisse orchestrer plusieurs candidats. Elle ne définit pas encore les files, retries, checkpoints ou quotas de lot.

L’automatisation pourra collecter les constats techniques, produire des artefacts et sélectionner des échantillons. Elle ne pourra ni inventer une preuve manquante ni approuver seule la qualité artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
batch_contract_for_chapter_30:
  input:
    - candidate_manifest
    - qa_profile
    - frozen_workspace
  output:
    - machine_report
    - artifacts_manifest
    - exit_code
  stable_exit_codes:
    0: checks_completed_without_blocker
    10: technical_blockers_found
    20: input_contract_invalid
    30: execution_incomplete
  human_gate_required: true
  batch_policy_owned_by: chapter_30
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** le lot reçoit des candidats déjà figés.
- **Sorties :** rapport et artefacts restent exploitables sans lire les journaux bruts.
- **Codes :** ils distinguent constats, entrée invalide et exécution incomplète.
- **Humain :** le code `0` n’équivaut pas à une acceptation artistique.
- **Frontière :** l’orchestration et la reprise restent au chapitre 30.

## 57. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Ces cas détaillés montrent comment une porte apparemment rigoureuse peut produire une acceptation non reproductible. Chaque correction rétablit l’identité du candidat, la séparation des responsabilités ou la qualité des preuves.

### 57.1 Accepter parce que l’asset « paraît bon »

**Symptôme ou risque :** La décision dépend d’une impression non reliée à une révision, une scène ou des critères.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
review:
  asset: scout.glb
  comment: looks_good
  technical_checks: skipped
  rights_check: assumed
  decision: ACCEPTED
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le commentaire ne vise ni version ni empreinte, ignore les préconditions techniques et juridiques et ne permet aucune reproduction.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
review:
  candidate:
    asset_id: AST-CHAR-SCOUT-001
    version: 0.7.0-rc.3
    sha256: <sha256>
  technical_report: AST-ASSET-QA-REPORT-SCOUT-0008
  art_references: [AST-BIBLE-SILHOUETTE-SCOUT-001]
  rights_decision: approved
  decision: ACCEPTED
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la décision vise un candidat immuable et relie les preuves techniques, artistiques et juridiques.

### 57.2 Laisser le script approuver la qualité artistique

**Symptôme ou risque :** Un passage automatique sans blocker devient directement une acceptation finale.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func decide(report: Dictionary) -> String:
    if report["blockers"] == 0:
        return "ACCEPTED"
    return "REJECTED"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’absence de blocker technique ne prouve ni la conformité à la bible, ni la lisibilité, ni l’adéquation à l’usage.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func technical_outcome(report: Dictionary) -> String:
    if int(report["blockers"]) > 0:
        return "TECHNICAL_BLOCKED"
    return "ART_REVIEW_REQUIRED"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le script peut bloquer ou transmettre à la revue artistique, mais il ne signe pas l’acceptation finale.

### 57.3 Valider uniquement dans Blender

**Symptôme ou risque :** L’asset est déclaré terminé sans vérifier son import, ses remaps et sa scène d’intégration Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
validation:
  blender_file_opens: true
  viewport_looks_correct: true
  godot_import: skipped
  integration_scene: skipped
  decision: ACCEPTED
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la source DCC ne prouve pas le résultat importé, les dépendances, les collisions, les animations ou les coûts dans le moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
validation:
  source_report: required
  gltf_validation: required
  godot_clean_import: required
  integration_scene_test: required
  runtime_measurements: required_for_release_profile
  decision_after_all_gates: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les preuves suivent toute la chaîne jusqu’à la représentation réellement utilisée dans Godot.

### 57.4 Utiliser un budget universel pour toutes les familles

**Symptôme ou risque :** La même limite de triangles ou de textures est appliquée à un prop lointain, un héros et un décor modulaire.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
budget:
  max_triangles: 50000
  max_texture: 2048
  applies_to: all_assets_all_platforms
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le coût acceptable dépend de la famille, de la distance, de la fréquence d’apparition, du renderer et de la plateforme.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
budgets:
  character_hero_pc:
    profile_id: AST-BUDGET-CHAR-HERO-PC-001
  prop_background_pc:
    profile_id: AST-BUDGET-PROP-BG-PC-001
  mobile_profiles:
    status: not_qualified
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque usage référence un profil versionné et les plateformes non qualifiées restent explicitement ouvertes.

### 57.5 Mesurer une seule frame froide

**Symptôme ou risque :** La première frame après chargement est comparée à une limite comme si elle représentait le coût stable.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
measurement:
  warmup_frames: 0
  sample_frames: 1
  repetitions: 1
  selected_value: first_frame
  fixture_baseline: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la mesure mélange chargement, compilation, cache, fixture et variabilité sans permettre une interprétation fiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
measurement:
  warmup_frames: candidate_profile_value
  sample_frames: candidate_profile_value
  repetitions: candidate_profile_value
  aggregation: median_and_percentiles
  fixture_baseline: required
  environment_manifest: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la campagne sépare chauffe, collecte, variabilité et coût du banc de test dans un environnement documenté.

### 57.6 Créer une dérogation sans portée ni expiration

**Symptôme ou risque :** Un écart accepté pour un jalon devient implicitement acceptable pour toutes les futures versions.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
waiver:
  finding: cape_popping
  rationale: no_time
  status: approved_forever
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la dérogation ne vise ni candidat, ni plateforme, ni propriétaire et ne possède aucun déclencheur de réexamen.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
waiver:
  id: AST-WAIVER-SCOUT-LOD1-001
  finding_id: AST-FINDING-LOD-SILHOUETTE-014
  candidate_version: 0.7.0-rc.2
  platform: windows_reference
  owner: art_lead
  expires_on: next_candidate_revision
  correction_plan: preserve_cape_outer_contour
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’écart est limité, assumé et automatiquement rouvert lors de la prochaine révision.

### 57.7 Modifier le candidat pendant la revue

**Symptôme ou risque :** Un valideur ajuste un matériau ou un preset puis conserve le rapport de la révision précédente.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
review_session:
  candidate_hash_before: abc
  tweak_material_in_editor: true
  candidate_hash_after: def
  report_candidate_hash: abc
  continue_review: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les captures et mesures ne portent plus sur le candidat identifié, ce qui invalide la décision.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
review_session:
  candidate_hash_before: abc
  candidate_mutation: forbidden
  requested_change: create_new_candidate_revision
  current_report_status: invalidated
  next_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** toute modification produit une nouvelle révision et une nouvelle campagne liée à sa propre empreinte.

### 57.8 Fusionner tous les résultats dans un booléen

**Symptôme ou risque :** Les droits, la technique, l’art et l’exécution incomplète sont réduits à `passed: false`.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
result:
  passed: false
  message: asset_failed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le propriétaire ne sait pas si le problème vient d’un blocker, d’une preuve absente, d’un avis artistique ou des droits.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
result:
  execution: completed
  technical_status: TECHNICAL_BLOCKED
  artistic_status: NOT_STARTED
  rights_status: APPROVED
  findings:
    blockers: 2
    major: 1
  next_action: correct_technical_findings
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les dimensions restent séparées et conduisent à une action de correction précise.

### 57.9 Produire un constat sans preuve ni reproduction

**Symptôme ou risque :** Le rapport contient une phrase vague qu’une autre personne ne peut pas vérifier.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
finding:
  code: MATERIAL_BAD
  message: texture looks wrong
  evidence: none
  reproduction: none
  severity: BLOCKER
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le code est imprécis, la sévérité non justifiée et aucune fixture ou capture ne permet de reproduire l’observation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
finding:
  code: NORMAL_MAP_GREEN_CHANNEL_INVERTED
  rule_id: AST-QA-MAT-NORMAL-003
  severity: MAJOR
  observation: grazing_light_reveals_inverted_relief
  evidence:
    - capture://scout/material_detail_grazing.png
    - import://scout_normal.webp.import
  reproduction:
    scene: AST-ASSET-QA-SCENE-001
    camera: material_detail
    environment: grazing_light
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le constat cite une règle, une observation, des preuves et une procédure reproductible.

### 57.10 Accepter avec une provenance incomplète

**Symptôme ou risque :** La qualité visuelle et les performances sont utilisées pour contourner une licence ou un consentement non résolu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
gate:
  technical: approved
  artistic: approved
  provenance: unknown
  redistribution: assumed
  final_decision: ACCEPTED
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la publication peut violer des droits même si l’asset fonctionne parfaitement dans le moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
gate:
  technical: approved
  artistic: approved
  provenance: unresolved
  rights_status: RIGHTS_BLOCKED
  final_decision: prohibited
  required_action: qualify_source_licence_and_consent
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la porte maintient un blocage indépendant jusqu’à qualification explicite des droits.

## 58. Checklist de production et d’acceptation

Cette checklist reste ouverte tant que le pilote et ses preuves n’existent pas. La revue statique valide la méthode, pas l’exécution.

Une case n’est cochée que si le rapport cite la révision, la preuve et la personne ou le processus responsable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
checklist_status:
  pilot: AST-ASSET-GATE-SCOUT-RELAY-001
  universal_rules_defined: true
  family_profiles_materialized: false
  validation_scene_materialized: false
  clean_import_executed: false
  technical_campaign_executed: false
  artistic_review_performed: false
  rights_review_performed: false
  final_acceptance_issued: false
  evidence_level: static_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** la checklist vise le lot éclaireur-relais.
- **Règles :** les contrats pédagogiques sont définis dans le chapitre.
- **Matérialisation :** profils, scène et scripts restent à créer.
- **Campagnes :** aucune exécution technique, artistique ou juridique n’est revendiquée.
- **Porte :** l’acceptation finale demeure ouverte.

- [ ] candidat figé avec identifiant, version et empreinte ;
- [ ] manifeste complet et profil de famille sélectionné ;
- [ ] provenance, licence, redistribution et consentement qualifiés ;
- [ ] source, livraison, sidecars et dépendances cohérents ;
- [ ] import propre Godot exécuté ;
- [ ] dimensions, unités, axes, pivot et transforms contrôlés ;
- [ ] géométrie, surfaces, matériaux, UV et textures contrôlés ;
- [ ] rig, skinning, blendshapes et animations contrôlés lorsque applicables ;
- [ ] collisions, sockets, métadonnées et LOD contrôlés ;
- [ ] scène de validation ouverte avec fixtures versionnées ;
- [ ] captures brutes produites sous les caméras de référence ;
- [ ] protocole de mesure exécuté avec baseline et répétitions ;
- [ ] grille artistique renseignée contre la bible approuvée ;
- [ ] constats classifiés avec preuves et reproduction ;
- [ ] corrections soumises comme nouvelles révisions ;
- [ ] dérogations bornées, signées et expirables ;
- [ ] approbations technique, artistique et droits présentes ;
- [ ] décision finale liée au candidat exact ;
- [ ] rapport, artefacts et historique archivés ;
- [ ] aucune logique gameplay créée par l’asset ou sa validation.

## 59. Références techniques officielles

Les pages suivantes documentent les API et outils utilisés. Elles ne remplacent ni les profils du projet, ni la revue artistique, ni les mesures du pilote.

Les références du chapitre 28 restent applicables pour l’import et la réimportation ; cette section ajoute les sources nécessaires à la validation, aux dépendances et aux mesures.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reference_scope:
  godot_version: 4.7
  primary_topics:
    - command_line_import
    - resource_dependencies
    - performance_monitors
    - profiler
    - import_and_integration
  external_validation:
    - khronos_gltf_validator
    - blender_scene_statistics
  project_authorities:
    - visual_bible
    - provenance_registry
    - family_budgets
  runtime_evidence: separate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Godot :** les pages 4.7 sont utilisées pour les commandes et API du chapitre.
- **Khronos :** le validateur glTF complète le contrôle de conformité du format.
- **Blender :** les statistiques source complètent ce que Godot observe après import.
- **Projet :** la bible, les budgets et les droits restent les autorités d’acceptation.
- **Limite :** la documentation ne constitue pas une campagne exécutée.

- [Godot 4.7 — Tutoriel de ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Godot 4.7 — Classe `Performance`](https://docs.godotengine.org/en/4.7/classes/class_performance.html)
- [Godot 4.7 — Le profiler](https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/the_profiler.html)
- [Godot 4.7 — Moniteurs de performance personnalisés](https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/custom_performance_monitors.html)
- [Godot 4.7 — Classe `ResourceLoader`](https://docs.godotengine.org/en/4.7/classes/class_resourceloader.html)
- [Godot 4.7 — Processus d’importation](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html)
- [Godot 4.7 — Importer des scènes 3D](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html)
- [Godot 4.7 — Paramètres avancés d’importation](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/using_the_advanced_import_settings_dialog.html)
- [Khronos Group — glTF Validator](https://github.com/KhronosGroup/glTF-Validator)
- [Khronos Group — Spécification glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- [Blender Manual — Barre d’état et statistiques de scène](https://docs.blender.org/manual/en/latest/interface/window_system/status_bar.html)
- [Blender Manual — Overlays et statistiques du viewport](https://docs.blender.org/manual/en/latest/editors/3dview/display/overlays.html)
- [Livre III — Chapitre 2 : Direction artistique et bible visuelle](CHAPITRE-02-Direction-artistique-et-bible-visuelle.md)
- [Livre III — Chapitre 5 : Provenance, licences et validation des assets](CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)
- [Livre III — Chapitre 18 : LOD, imposteurs et optimisation géométrique](CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md)
- [Livre III — Chapitre 19 : Rigging et skinning](CHAPITRE-19-Rigging-et-skinning.md)
- [Livre III — Chapitre 23 : Effets visuels, particules et simulations](CHAPITRE-23-Effets-visuels-particules-et-simulations.md)
- [Livre III — Chapitre 24 : Interface utilisateur](CHAPITRE-24-Interface-utilisateur.md)
- [Livre III — Chapitre 26 : Voix, bruitages, ambiances et musique](CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md)
- [Livre III — Chapitre 28 : Importation et intégration dans Godot](CHAPITRE-28-Importation-et-integration-dans-Godot.md)

## 60. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-ASSET-GATE-SCOUT-RELAY-001` comme pilote de la porte qualité. L’éclaireur et le module de relais seront soumis comme révisions figées, reliées au manifeste d’import du chapitre 28, à la bible visuelle, au registre de provenance et aux budgets de famille.

La validation finale exigera une campagne technique reproductible, une revue artistique documentée, une décision de droits et des mesures Godot sur le profil de référence. Un passage automatique sans blocker conduira seulement à `ART_REVIEW_REQUIRED`, jamais à une acceptation artistique.

Les livrables attendus sont la checklist universelle, les profils personnage et prop, la scène de validation, le schéma de rapport, les captures, mesures, constats, dérogations et décisions. Leur matérialisation et leur exécution restent ouvertes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_asset_gate_decisions:
  pilot_id: AST-ASSET-GATE-SCOUT-RELAY-001
  checklist_id: AST-ASSET-QA-CHECKLIST-001
  validation_scene_id: AST-ASSET-QA-SCENE-001
  report_schema_id: AST-ASSET-QA-REPORT-001
  character_profile_id: AST-ASSET-QA-PROFILE-CHARACTER-001
  prop_profile_id: AST-ASSET-QA-PROFILE-STATIC-001
  acceptance_requires:
    - candidate_identity_and_hash
    - rights_approved
    - technical_blockers_zero
    - godot_evidence_complete
    - artistic_approval
    - valid_waivers_only
  automation_outcome_without_blocker: ART_REVIEW_REQUIRED
  gameplay_authority: none
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** les profils, la scène et le rapport possèdent des noms stables.
- **Entrée :** le candidat provient de la chaîne d’import approuvée du chapitre 28.
- **Porte :** droits, technique, preuve Godot et art restent nécessaires.
- **Automatisation :** elle collecte et bloque, mais n’approuve pas seule l’art.
- **Autorité :** la validation de contenu ne modifie aucun état gameplay.
- **Réserve :** aucun asset, rapport, capture ou benchmark n’est déclaré matérialisé.
