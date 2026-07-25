---
title: "Livre III — Chapitre 28 : Importation et intégration dans Godot"
id: "DOC-L3-CH28"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 28
last-verified: "2026-07-25T06:23:53+02:00"
audit-status: "complete"
audit-date: "2026-07-25T06:23:53+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-28.md"
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

# Importation et intégration dans Godot

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH28`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Importer un asset ne signifie pas seulement le rendre visible dans l’éditeur. La chaîne transforme une livraison externe en ressources Godot reproductibles, puis l’encapsule dans une scène d’intégration qui protège les réglages propres au jeu.

Le chapitre définit les contrats de format, de preset, de remapping, de post-traitement et de réimportation. Il ne modifie ni la direction artistique, ni les règles de gameplay, ni les sources canoniques produites dans les chapitres précédents.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: approved_asset_delivery_and_manifest
  transformation: deterministic_import_remap_postprocess_and_integration
  output: imported_resources_integration_scenes_and_reimport_evidence
  authority: presentation_and_tooling_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la livraison doit être approuvée, identifiée et accompagnée de ses dépendances.
- **Transformation :** les réglages d’import et les scripts dérivent des ressources reproductibles.
- **Sortie :** les scènes d’intégration portent les personnalisations Godot sans éditer la scène importée.
- **Autorité :** aucun importeur, socket ou suffixe de nom ne décide une règle métier.
- **Preuve :** aucun import réel ni test runtime n’est revendiqué.

## 2. Résultats d’apprentissage

Le lecteur saura choisir un format d’échange, définir des profils d’import par famille d’asset, séparer scène importée et scène d’intégration, puis conserver les personnalisations lors d’une réimportation.

Il saura aussi externaliser ou remapper les matériaux, gérer animations, collisions et sockets, écrire un post-import idempotent, comparer les changements et préparer des contrôles Solo ou Studio.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  formats: [glb, gltf_separate, blend_direct, fbx_ufbx, obj_limited]
  import: [defaults, presets, advanced_settings, suffixes]
  integration: [inherited_scene, composition_scene, external_resources]
  automation: [post_import, metadata, idempotence, bounded_validation]
  reimport: [dependency_diff, customization_protection, rollback_plan]
  validation: [structure, materials, animations, collisions, sockets, runtime_budget]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Formats :** le choix dépend du type d’asset et du besoin de revue ou de portabilité.
- **Import :** les réglages répétitifs deviennent des profils explicites.
- **Intégration :** les ajouts Godot vivent hors de la scène régénérée.
- **Automatisation :** le post-import reste déterministe, borné et inspectable.
- **Validation :** les preuves statiques et runtime restent séparées.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les arborescences, presets et scripts sont des contrats pédagogiques ; ils ne prouvent pas qu’un GLB, un matériau, une animation ou une collision a été importé correctement.

Les budgets de durée d’import, taille de cache, mémoire, draw calls et temps de chargement sont des candidats. Ils doivent être mesurés avec les assets et plateformes réellement retenus.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  import_profile_created: false
  glb_imported: false
  inherited_scene_created: false
  material_remap_executed: false
  post_import_script_executed: false
  reimport_campaign_executed: false
  runtime_budget_recorded: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est relue sans annoncer une intégration terminée.
- **Imports :** aucun fichier externe n’est déclaré traité par Godot.
- **Scripts :** aucun callback de post-import n’est présenté comme exécuté.
- **Mesures :** aucun coût ni résultat de réimportation n’est inventé.
- **Publication :** le PDF reste différé jusqu’à la fin du Livre III.

## 4. Frontières avec les chapitres voisins

Les chapitres 4 à 27 conservent les sources, conventions, matériaux, rigs, animations, VFX, UI, audio et timings faciaux. Le chapitre 28 consolide leur arrivée dans Godot sans les redéfinir.

Le chapitre 29 possédera la porte de validation technique et artistique ; le chapitre 30 automatisera les lots. Le Livre II conserve toute autorité métier et les outils d’édition génériques.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapters_04_to_27: canonical_sources_artistic_rules_and_asset_deliveries
  chapter_28: import_profiles_remaps_integration_scenes_and_reimport_contract
  chapter_29: final_asset_quality_gate
  chapter_30: batch_orchestration_and_ci
  book_ii: runtime_domain_authority_and_generic_editor_architecture
  invariant: imported_assets_never_create_business_rules
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** les livraisons approuvées sont consommées sans modifier leur intention artistique.
- **Chapitre 28 :** les ressources dérivées et scènes d’intégration deviennent reproductibles.
- **Aval :** la validation finale et les lots restent réservés aux chapitres suivants.
- **Invariant :** l’import ne transforme jamais un nom de nœud en décision gameplay.

## 5. Pilote d’intégration de Project Asteria

Le pilote `AST-IMPORT-PILOT-SCOUT-RELAY-001` combine un éclaireur animé, un module de relais statique, leurs matériaux, collisions, sockets et une bibliothèque d’animations. Il réutilise les pilotes déjà décrits sans prétendre que leurs fichiers existent.

Ce lot expose les principaux risques : squelettes, blendshapes, animations, matériaux externes, collisions simples, points d’attache, LOD et réimportation après changement de source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_import_pilot:
  id: AST-IMPORT-PILOT-SCOUT-RELAY-001
  character_source: AST-FACE-PILOT-RELAY-DIALOGUE-001
  environment_source: AST-CINE-PILOT-SCOUT-RELAY-001
  vfx_dependency: AST-VFX-PILOT-RELAY-STORM-001
  audio_dependency: AST-AUDIO-PILOT-RELAY-STORM-001
  profiles: [character_hero, static_prop, animation_library]
  integration_scenes:
    - scout_integrated.tscn
    - relay_module_integrated.tscn
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** un lot réduit couvre plusieurs familles sans devenir une production complète.
- **Personnage :** le profil vérifie squelette, skin, blendshapes et animations.
- **Décor :** le module statique vérifie matériaux, collisions, sockets et LOD.
- **Dépendances :** VFX et audio sont référencés mais restent produits par leurs chapitres.
- **Réserve :** aucune scène ou ressource n’est déclarée créée.

## 6. Modèle mental de la chaîne d’import

La source canonique, la livraison, le fichier `.import`, le cache `.godot/imported` et la scène d’intégration n’ont pas le même statut. Les confondre rend les réimportations imprévisibles.

La source est modifiée dans l’outil auteur ; la livraison est versionnée ; le fichier `.import` conserve la configuration ; le cache est régénérable ; la scène d’intégration appartient au projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_states:
  canonical_source: outside_or_source_workspace
  delivery: res://assets/source_delivery/
  import_config: <delivery>.import
  generated_cache: res://.godot/imported/
  imported_scene: generated_read_only_surface
  integration_scene: res://assets/integration/
  version_control:
    commit: [delivery, import_config, integration_scene]
    ignore: [res://.godot/]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** elle conserve l’autorité d’auteur et ne doit pas être remplacée par le cache.
- **Configuration :** le sidecar `.import` doit être versionné avec la livraison.
- **Cache :** le dossier `.godot` est dérivé et peut être reconstruit.
- **Intégration :** les personnalisations Godot vivent dans une scène possédée par le projet.

## 7. Arborescence des livraisons et intégrations

Une arborescence sépare les fichiers entrants, les ressources externes, les scènes d’intégration et les rapports. Cette séparation évite qu’un artiste écrase un fichier possédé par Godot.

Les chemins sont des conventions de dépôt, pas des identités métier. Chaque manifeste conserve un identifiant stable indépendant du nom de fichier.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
res://assets/
  source_delivery/
    characters/scout/
    environment/relay/
  materials/
    shared/
    overrides/
  animations/
    libraries/
  integration/
    characters/
    environment/
  import_profiles/
  reports/import/
  test_scenes/import/
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Livraisons :** les fichiers reçus sont regroupés par asset et version.
- **Matériaux :** les ressources partagées et overrides sont externes aux imports régénérés.
- **Intégration :** les scènes locales référencent les scènes importées.
- **Rapports :** les diffs et contrôles ne sont pas mélangés aux assets runtime.

## 8. Matrice format-usage

Aucun format n’est universel. GLB est la livraison 3D par défaut, glTF séparé facilite certaines revues, `.blend` direct accélère un parcours Solo dépendant de Blender, FBX utilise l’importeur ufbx et OBJ reste limité.

La matrice doit décrire capacités, dépendances, inspectabilité, risques et politique de repli avant le premier import.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
format_usage:
  glb:
    use: default_3d_delivery
    strengths: [portable, single_file, gltf_2]
  gltf_separate:
    use: reviewable_scene_and_external_textures
    strengths: [text_scene, separate_dependencies]
  blend:
    use: solo_iteration_candidate
    dependency: qualified_blender_installation
  fbx:
    use: supplier_constraint_only
    importer: ufbx
  obj:
    use: simple_static_mesh_only
    limits: [no_skeleton, no_animation, limited_materials]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **GLB :** le conteneur binaire réduit le nombre de dépendances visibles.
- **glTF séparé :** le texte et les fichiers externes facilitent certains diffs.
- **Blend :** l’import direct ajoute une dépendance d’outil sur chaque poste.
- **Formats hérités :** FBX et OBJ exigent des limites explicites.

## 9. Choix entre GLB et glTF séparé

GLB simplifie la livraison atomique. Le glTF séparé rend la description textuelle inspectable et permet de gérer les textures comme fichiers indépendants.

La décision se prend par famille d’asset et ne change pas silencieusement au milieu d’une production.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gltf_delivery_policy:
  character_hero:
    container: glb
    embedded_textures: false
    reason: stable_single_scene_with_external_material_library
  modular_environment:
    container: gltf_separate
    embedded_textures: false
    reason: dependency_review_and_shared_textures
  policy_change:
    requires: [decision_record, dependency_migration, reimport_campaign]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Personnage :** un conteneur stable peut réduire les erreurs de livraison.
- **Environnement :** des dépendances externes peuvent mieux servir la mutualisation.
- **Textures :** leur stratégie reste explicite et cohérente avec le chapitre 16.
- **Changement :** une migration de format invalide les preuves d’import précédentes.

## 10. Import direct des fichiers Blender

Godot peut appeler Blender pour convertir un `.blend` vers glTF avant l’import. Cette voie facilite l’itération locale mais impose une version de Blender disponible et qualifiée sur chaque poste concerné.

Le parcours Studio privilégie une livraison glTF ou GLB reproductible afin de ne pas rendre l’import dépendant d’installations divergentes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blend_import_profile:
  enabled_for: solo_iteration_only
  blender_version: qualified_per_project
  executable_path: editor_setting
  source_control: blend_source_or_export_not_both_without_policy
  studio_default: exported_glb
  web_and_android_editor: unsupported_for_external_blender_call
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendance :** l’éditeur doit pouvoir lancer une version compatible de Blender.
- **Solo :** la conversion transparente peut accélérer une boucle locale.
- **Studio :** une livraison exportée réduit la variabilité des postes.
- **Plateformes :** les éditeurs incapables de lancer Blender utilisent un export intermédiaire.

## 11. Import FBX avec ufbx

FBX peut être imposé par un fournisseur. Godot 4.7 dispose d’une voie ufbx ; le projet doit enregistrer l’importeur choisi et éviter de mélanger silencieusement les anciens chemins FBX2glTF.

Un asset reçu en FBX est comparé à une référence GLB lorsque les matériaux, animations ou axes semblent ambigus.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
fbx_policy:
  accepted_when: supplier_constraint_documented
  importer: ufbx
  importer_change: explicit_requalification
  comparison_asset: optional_glb_reference
  checks: [scale, axes, skeleton, animation_names, materials, blendshapes]
  fallback: request_gltf_2_delivery
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrainte :** FBX n’est pas choisi par habitude mais par besoin documenté.
- **Importeur :** le chemin ufbx est épinglé dans le profil.
- **Comparaison :** une référence réduit les ambiguïtés de conversion.
- **Repli :** glTF 2.0 reste la demande privilégiée lorsque possible.

## 12. Limites de OBJ et DAE

OBJ convient à une géométrie statique simple mais ne transporte pas les contrats modernes d’un personnage ou d’une scène animée. DAE reste une voie héritée à qualifier au cas par cas.

Le projet refuse de corriger en aval un format incapable de porter les informations nécessaires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
legacy_format_gate:
  obj:
    allowed_for: [simple_static_mesh, reference_geometry]
    forbidden_for: [rig, animation, pivots_complex, pbr_contract]
  dae:
    status: legacy_candidate
    requires: dedicated_comparison
  rejection_code: IMPORT_FORMAT_CAPABILITY_MISMATCH
  remediation: request_glb_or_gltf
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **OBJ :** sa simplicité devient une limite pour les assets complexes.
- **DAE :** la compatibilité historique ne vaut pas validation.
- **Refus :** le code stable permet un diagnostic automatisable.
- **Correction :** le fournisseur reçoit une demande de format adaptée.

## 13. Contrat de livraison 3D

Chaque livraison 3D possède un manifeste indiquant identité, version, unité, axes, collection exportée, format, dépendances, empreintes et autorité de publication.

Le fichier binaire seul ne suffit pas à expliquer comment il a été produit ni quelles personnalisations doivent survivre.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
delivery_manifest:
  schema: asteria-asset-delivery-v1
  asset_id: AST-CHAR-SCOUT-001
  version: 1.0.0
  format: glb
  source_revision: blender-source-revision
  unit_meters: 1.0
  exported_collection: __EXPORT
  dependencies: [AST-MAT-SCOUT-001]
  sha256: pending_until_materialized
  publication_authority: named_role
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** l’asset ne dépend pas du chemin ou du nom affiché.
- **Version :** une livraison approuvée est immuable.
- **Conventions :** unités, axes et collection proviennent du chapitre 4.
- **Empreinte :** elle vérifie l’intégrité sans prouver l’auteur ou la qualité.

## 14. Processus d’import Godot

Lorsqu’un fichier source entre dans le projet, Godot crée une configuration `<asset>.import` et des ressources internes sous `.godot/imported`. Le code charge l’asset par son chemin source avec `ResourceLoader` ou `load`.

Accéder directement au cache avec `FileAccess` crée une dépendance fragile et peut échouer dans un export.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_import_process:
  source_path: res://assets/source_delivery/environment/relay.glb
  config_path: res://assets/source_delivery/environment/relay.glb.import
  cache_root: res://.godot/imported/
  runtime_reference: res://assets/source_delivery/environment/relay.glb
  loader: ResourceLoader
  direct_cache_access: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sidecar :** la configuration d’import est versionnée avec la source.
- **Cache :** le nom interne est dérivé et non stable pour le code.
- **Chargement :** le chemin source laisse Godot résoudre la ressource importée.
- **Export :** la résolution fonctionne dans l’éditeur comme dans le build.

## 15. Dock Import et valeurs par défaut

Le dock Import règle un fichier ou une sélection. Les valeurs par défaut de projet réduisent les écarts, mais une exception par asset reste possible et doit être documentée.

Un preset n’est pas une preuve de résultat : il décrit une intention reproductible à vérifier après réimportation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_defaults:
  scene:
    generate_lods: profile_defined
    create_shadow_meshes: profile_defined
    use_named_skin_binds: rig_profile_defined
  texture:
    detect_3d: true
    mipmaps: per_usage
    compression_mode: per_platform_profile
  audio:
    mode: per_duration_and_latency
  override_record:
    required_for_non_default: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défauts :** ils évitent de répéter des clics sur chaque asset.
- **Exceptions :** elles restent localisées et justifiées.
- **Familles :** scènes, textures et audio n’emploient pas les mêmes critères.
- **Preuve :** le résultat doit encore être inspecté et mesuré.

## 16. Profils d’import versionnés

Les réglages d’import sont décrits dans un catalogue lisible en plus des sidecars générés par Godot. Ce catalogue facilite la revue et la reconstruction après changement d’outil.

Le sidecar reste la configuration appliquée ; le catalogue explique l’intention et les différences par famille.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_profile_catalog:
  AST-IMPORT-PROFILE-STATIC-001:
    family: static_prop
    scene_root_type: Node3D
    materials: external_remap
    collisions: authored_suffix_or_explicit_scene
  AST-IMPORT-PROFILE-CHARACTER-001:
    family: skinned_character
    skeleton: preserve
    animations: external_library
    blendshapes: required
  AST-IMPORT-PROFILE-ANIM-001:
    family: animation_library
    meshes: disabled
    library_output: external
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catalogue :** les identifiants de profil sont stables.
- **Statique :** le profil privilégie géométrie, matériaux et collisions.
- **Personnage :** le squelette et les blendshapes sont obligatoires.
- **Animation :** la bibliothèque peut être importée séparément du mesh.

## 17. Preset pour les assets statiques

Un asset statique doit conserver échelle, pivot, matériaux, LOD et collisions attendues. Les options coûteuses ou destructrices ne sont pas activées par défaut sans comparaison.

Le preset sert de point de départ, puis le pilote vérifie les résultats dans une scène neutre.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
static_prop_profile:
  id: AST-IMPORT-PROFILE-STATIC-001
  root: Node3D
  mesh:
    generate_lods: candidate
    create_shadow_meshes: candidate
    ensure_tangents: required_when_normal_map
  materials: external_remap
  collisions: explicit_contract
  navigation: separate_asset
  test_scene: res://assets/test_scenes/import/static_prop_lab.tscn
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** le nœud conserve un transform éditable dans la scène d’intégration.
- **Mesh :** LOD et shadow mesh restent des candidats à comparer.
- **Matériaux :** les ressources partagées sont remappées hors de l’import.
- **Collision :** elle ne dérive pas automatiquement du mesh visuel sans contrat.

## 18. Preset pour les personnages squelettés

Le profil personnage vérifie hiérarchie, peau, influences, blendshapes, animations et sockets. Il refuse une livraison qui perd les canaux exigés par le rig approuvé.

Les contrôleurs et règles gameplay ne sont jamais ajoutés dans la scène importée ; ils appartiennent à la scène d’intégration.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
character_profile:
  id: AST-IMPORT-PROFILE-CHARACTER-001
  root: Node3D
  skeleton:
    required: true
    named_skin_binds: profile_decision
    rest_pose_hash: manifest_reference
  blendshapes:
    required_channels: manifest_list
  animations:
    destination: external_library
  gameplay_scripts_in_import: forbidden
  integration_scene: res://assets/integration/characters/scout_integrated.tscn
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Squelette :** la rest pose et les binds sont comparés au manifeste.
- **Blendshapes :** les canaux manquants bloquent le profil facial.
- **Animations :** elles peuvent être externalisées pour survivre aux réimports.
- **Gameplay :** les scripts métier restent dans les scènes possédées par le projet.

## 19. Preset pour les bibliothèques d’animation

Les animations peuvent être livrées dans un fichier séparé et importées comme bibliothèque. Cette séparation réduit les doublons de mesh et permet de versionner les clips indépendamment.

Les noms, boucles, pistes, root motion et filtres restent des décisions explicites issues des chapitres 20, 21 et 27.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_library_profile:
  id: AST-IMPORT-PROFILE-ANIM-001
  import_mode: animation_library
  mesh_import: disabled
  skeleton_contract: AST-RIG-PROFILE-SCOUT-001
  clips:
    - id: AST-ANIM-SCOUT-IDLE-001
      loop: true
    - id: AST-FACE-ANIM-RELAY-SCOUT-001
      loop: false
  track_filter: explicit_allowlist
  root_motion: presentation_contract_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode :** la livraison devient une bibliothèque plutôt qu’une scène complète.
- **Contrat :** le squelette cible est identifié avant import.
- **Clips :** chaque animation possède un identifiant distinct du nom affiché.
- **Pistes :** une allowlist évite d’importer des canaux inattendus.

## 20. Preset pour les textures

Les textures utilisent les règles du chapitre 16 : espace colorimétrique, mipmaps, compression, normal maps, données linéaires et plateformes sont séparés.

Le détecteur automatique peut aider, mais une texture critique conserve un profil explicite afin d’éviter les changements silencieux de contexte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
texture_profiles:
  base_color:
    color_space: srgb
    mipmaps: true
    compression: platform_candidate
  normal:
    color_space: linear_data
    normal_map: true
    mipmaps: true
  orm:
    color_space: linear_data
    channels: [occlusion, roughness, metallic]
  ui_icon:
    color_space: srgb
    mipmaps: context_dependent
  evidence: measured_after_import
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base color :** les couleurs sont interprétées en sRGB.
- **Normal :** la texture est traitée comme donnée et non comme couleur.
- **ORM :** les canaux restent documentés et cohérents.
- **Mesure :** la compression retenue est vérifiée sur les plateformes cibles.

## 21. Preset pour l’audio

Le chapitre 26 définit les masters et exports runtime ; le chapitre 28 applique seulement des choix d’import cohérents avec durée, latence, boucle et mémoire.

Les réglages ne changent ni le loudness approuvé ni le montage source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_import_profiles:
  ui_short:
    source_family: wav
    priority: low_latency
    looping: false
  ambience_loop:
    source_family: ogg_vorbis
    priority: streaming_memory_balance
    looping: true
  voice_line:
    source_family: ogg_vorbis
    priority: intelligibility
    looping: false
  loudness_authority: chapter_26_master
  runtime_measurement: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **UI :** les sons courts privilégient une réponse immédiate.
- **Ambiance :** la durée et la boucle influencent le mode de lecture.
- **Voix :** l’intelligibilité reste le critère principal.
- **Frontière :** l’import ne remixe pas le master.

## 22. Scène importée comme surface régénérée

Une scène importée est reconstruite quand la source ou sa configuration change. L’éditer comme si elle était une scène locale crée des modifications fragiles.

Le projet l’utilise comme base en lecture seule et déplace les scripts, nœuds complémentaires et réglages locaux vers une scène d’intégration.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
scene_ownership:
  imported_scene:
    path: res://assets/source_delivery/characters/scout.glb
    owner: importer
    manual_edits: forbidden
  integration_scene:
    path: res://assets/integration/characters/scout_integrated.tscn
    owner: project
    additions: [controllers, audio_players, vfx_sockets, gameplay_adapters]
  source_change:
    regenerates: imported_scene
    preserves: integration_scene_when_contract_stable
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** la ressource générée appartient à l’importeur.
- **Intégration :** le projet possède les ajouts et références locales.
- **Réimport :** la base peut changer sans effacer automatiquement la scène locale.
- **Contrat :** les chemins de nœuds et sockets doivent rester stables ou être migrés.

## 23. Scène héritée

L’héritage de scène permet d’ajouter des nœuds et de modifier des propriétés autorisées au-dessus d’une scène importée. Les nœuds de la base ne peuvent pas être supprimés et les sous-ressources doivent être externalisées pour être éditées durablement.

Cette approche convient à une adaptation légère lorsque la hiérarchie amont reste stable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
inherited_scene_policy:
  use_when: light_customization_and_stable_hierarchy
  base: res://assets/source_delivery/environment/relay.glb
  derived: res://assets/integration/environment/relay_inherited.tscn
  allowed:
    - add_nodes
    - override_exposed_properties
  limitations:
    - cannot_remove_base_nodes
    - imported_subresources_not_directly_editable
  mitigation: externalize_shared_resources
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** la scène importée reste la source héritée.
- **Ajouts :** les nœuds locaux peuvent être placés dans la dérivée.
- **Limites :** la suppression des nœuds de base n’est pas le bon mécanisme.
- **Ressources :** les matériaux éditables sont sauvegardés à l’extérieur.

## 24. Scène d’intégration par composition

La composition instancie la scène importée sous une racine locale. Elle offre une frontière claire pour les scripts, collisions gameplay, audio, VFX et adaptateurs.

Cette voie est privilégiée lorsque la hiérarchie importée peut changer ou lorsque plusieurs variantes partagent le même visuel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
composition_scene:
  root: ScoutIntegrated
  children:
    Visual:
      instance: res://assets/source_delivery/characters/scout.glb
    RuntimeAdapters:
      script: res://src/features/characters/presentation/scout_visual_adapter.gd
    Audio:
      scene: res://assets/integration/audio/scout_audio.tscn
    Vfx:
      scene: res://assets/integration/vfx/scout_vfx.tscn
  identity_source: character_definition_id
  visual_path_as_identity: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** la scène locale possède le cycle de vie d’intégration.
- **Visual :** l’instance importée reste remplaçable.
- **Adaptateurs :** la présentation traduit des états déjà décidés.
- **Identité :** le chemin du mesh ne devient jamais un identifiant métier.

## 25. Externalisation des sous-ressources

Un matériau, une animation ou une ressource générée dans la scène importée peut être sauvegardé comme ressource externe lorsque le projet doit l’éditer ou la partager.

L’externalisation doit conserver une relation traçable avec la livraison et éviter de créer une copie orpheline.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
external_resource_record:
  source_asset: AST-CHAR-SCOUT-001
  imported_subresource: Material_Armor
  external_path: res://assets/materials/overrides/scout_armor.tres
  role: project_owned_override
  base_delivery_version: 1.0.0
  remap_profile: AST-MAT-REMAP-SCOUT-001
  review_on_reimport: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la ressource d’origine est identifiée.
- **Chemin :** l’override possède un emplacement stable.
- **Version :** la dépendance à la livraison est enregistrée.
- **Réimport :** le remap est contrôlé après chaque changement de source.

## 26. Remapping des matériaux

Le remapping associe un matériau importé à une ressource Godot externe. Il évite de refaire les mêmes réglages après chaque réimport et permet de partager un matériau maître.

La clé de correspondance doit être stable et les matériaux manquants doivent produire un rapport, pas une substitution silencieuse.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
material_remap:
  profile_id: AST-MAT-REMAP-SCOUT-001
  source_asset: AST-CHAR-SCOUT-001
  mappings:
    Armor_Main: res://assets/materials/overrides/scout_armor.tres
    Skin_Main: res://assets/materials/overrides/scout_skin.tres
  missing_source_material: blocking
  unknown_source_material: report_and_review
  fallback_material: diagnostic_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le remap est versionné indépendamment du fichier binaire.
- **Mappings :** les noms sources sont contrôlés contre une liste attendue.
- **Manquant :** une dépendance absente bloque la publication.
- **Fallback :** le matériau de diagnostic n’est jamais promu comme résultat final.

## 27. Textures extraites et dépendances externes

Extraire les textures d’un glTF peut améliorer le contrôle des options d’import et le partage, mais ajoute des fichiers et des relations à maintenir.

La politique choisit soit des textures embarquées, soit des dépendances externes traçables ; elle évite les mélanges non documentés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
texture_dependency_policy:
  embedded:
    allowed_for: self_contained_delivery
    extraction: optional_reviewed_step
  external:
    allowed_for: shared_material_library
    manifest_required: true
    relative_paths_only: true
  missing_texture:
    status: blocked
    diagnostic_material: magenta_check_only
  absolute_paths: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Embarqué :** le conteneur simplifie la livraison.
- **Externe :** les dépendances peuvent être mutualisées et configurées séparément.
- **Manquant :** le défaut reste visible et bloquant.
- **Chemins :** les références absolues personnelles sont refusées.

## 28. Suffixes de nom et personnalisation des nœuds

Godot peut interpréter certains suffixes de noms pour personnaliser le type ou le traitement de nœuds lors de l’import. Cette convention doit être centralisée et compatible avec le chapitre 4.

Un suffixe est une instruction d’import, pas une identité durable ni une règle gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
name_suffix_policy:
  enabled: true
  source_of_truth: docs/assets/import-name-suffixes.md
  examples:
    - Mesh-collision
    - Socket_Weapon
    - Helper-noimp
  validation:
    duplicate_socket_names: blocking
    unsupported_suffix: warning_or_blocking_by_profile
  gameplay_identity_from_name: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Convention :** la liste des suffixes autorisés est versionnée.
- **Auteur :** les noms sont préparés dans le DCC avant export.
- **Validation :** les collisions de noms et suffixes inconnus sont signalés.
- **Frontière :** la logique métier utilise des identifiants explicites.

## 29. Collisions importées

Les collisions peuvent être décrites par géométries dédiées, suffixes ou scènes locales. Le mesh visuel haute résolution n’est pas automatiquement une collision acceptable.

La collision physique gameplay reste sous l’autorité des systèmes du Livre II, même si sa forme provient d’un asset importé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
collision_import_contract:
  visual_asset: AST-PROP-RELAY-001
  collision_source: authored_simple_mesh
  shape_family: concave_static_candidate
  dynamic_body_requires: convex_or_primitive_profile
  generated_from_render_mesh: prohibited_without_measurement
  gameplay_layer_mask: integration_scene_owned
  validation: [scale, origin, coverage, complexity, separation_from_triggers]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** une géométrie simple est préparée pour son usage physique.
- **Dynamique :** les contraintes diffèrent des décors statiques.
- **Couches :** les masques sont réglés dans la scène d’intégration.
- **Validation :** la couverture et le coût doivent être mesurés.

## 30. Sockets et points d’attache

Les sockets transportent une intention spatiale : main droite, bouche, arme, VFX ou caméra. Leur nom, transform et parent sont vérifiés à l’import.

Un socket ne possède aucune autorité sur l’objet équipé ; il ne fait que fournir une pose d’attache à une décision déjà validée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
socket_contract:
  profile: AST-SOCKET-PROFILE-SCOUT-001
  required:
    - id: socket_weapon_r
      parent_bone: hand_r
    - id: socket_radio
      parent_bone: hand_l
    - id: socket_voice
      parent_bone: head
  missing_required: blocking
  transform_tolerance: measured_candidate
  authority: presentation_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** les sockets attendus sont listés par identifiant.
- **Parent :** le lien au bone est contrôlé après import.
- **Transform :** la tolérance reste une valeur à mesurer.
- **Autorité :** l’inventaire décide l’équipement avant l’attache visuelle.

## 31. Animations, pistes et boucles

L’import des animations conserve un inventaire de clips, durées, boucles, pistes et dépendances. Les marqueurs ou pistes de méthode ne doivent pas appliquer directement des conséquences gameplay.

Les boucles et découpages sont comparés aux décisions du chapitre 20 et non déduits aveuglément du nom.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_import_inventory:
  source: scout_animation_library.glb
  clips:
    Idle:
      expected_loop: true
      track_policy: allowlisted
    RelayDialogue:
      expected_loop: false
      facial_profile: AST-FACE-LANG-FR-001
  method_tracks:
    allowed: presentation_notifications_only
    domain_mutation: forbidden
  unknown_clip: report_and_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Inventaire :** les clips attendus sont comparés aux clips importés.
- **Boucle :** le comportement provient d’un contrat explicite.
- **Pistes :** une allowlist évite les canaux indésirables.
- **Frontière :** les événements gameplay sont committés ailleurs.

## 32. Squelettes, skins et rest pose

Un import réussi doit conserver la hiérarchie, la rest pose, les binds, les influences et les noms fonctionnels nécessaires au retargeting et à la synchronisation faciale.

Une comparaison structurelle détecte les os ajoutés, supprimés ou déplacés avant qu’une réimportation casse les animations locales.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skeleton_import_check:
  profile: AST-RIG-PROFILE-SCOUT-001
  expected_root: Skeleton3D
  required_bones: manifest_reference
  rest_pose_digest: pending_until_materialized
  skin_count: expected_one_or_profile
  max_influences: renderer_profile
  missing_bone: blocking
  hierarchy_change: migration_required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le rig attendu est versionné en amont.
- **Empreinte :** la rest pose peut être résumée par des données canoniques.
- **Influences :** la limite dépend du renderer et du profil.
- **Migration :** une hiérarchie modifiée invalide les dépendances.

## 33. Blendshapes et canaux faciaux

Les morph targets glTF deviennent des blendshapes Godot lorsque la chaîne d’export et d’import les conserve. Le profil facial vérifie la présence et l’orthographe des canaux requis.

Un canal absent n’est pas recréé automatiquement par le post-import : la source doit être corrigée ou le profil explicitement migré.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blendshape_import_check:
  viseme_set: AST-FACE-VISEME-SET-001
  required:
    - viseme_A
    - viseme_E
    - viseme_MBP
    - blink_L
    - blink_R
  unknown_channels: report
  missing_required: blocking
  automatic_channel_fabrication: forbidden
  language_profile_review: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Jeu de formes :** la liste provient du chapitre 27.
- **Canaux :** les noms importés sont comparés sans approximation silencieuse.
- **Manquant :** le problème remonte à la source ou à une migration.
- **Langue :** la présence technique ne prouve pas la qualité linguistique.

## 34. LOD, ombres et visibilité

Les LOD importés ou générés doivent conserver pivot, matériaux, AABB et seuils cohérents avec le chapitre 18. Les options d’import ne remplacent pas une campagne visuelle.

Les shadow meshes et niveaux générés restent des variantes candidates tant que silhouette, coût et transitions ne sont pas mesurés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
lod_import_contract:
  source_asset: AST-LOD-PILOT-SIGNAL-TOWER-001
  levels: [LOD0, LOD1, LOD2]
  pivot_match: required
  material_slot_match: required
  aabb_consistency: required
  generated_lods:
    status: candidate
    human_review: required
  visibility_ranges: integration_scene_owned
  runtime_measurement: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** les livraisons manuelles conservent des identités cohérentes.
- **Génération :** un résultat automatique n’est pas approuvé par défaut.
- **Visibilité :** les seuils appartiennent à la scène d’intégration.
- **Mesure :** les transitions et coûts restent à vérifier.

## 35. Métadonnées importées

Les métadonnées peuvent transporter une catégorie, un identifiant d’asset ou une information de traitement. Elles doivent être validées par une liste fermée et ne jamais contenir une commande à exécuter.

Le post-import copie seulement les clés autorisées vers les nœuds ou ressources concernés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
metadata_policy:
  allowed_keys:
    - asteria_asset_id
    - asteria_role
    - asteria_socket_id
    - asteria_import_profile
  forbidden_values:
    - executable_method_name
    - absolute_path
    - secret
    - gameplay_rule
  unknown_key: ignored_and_reported
  max_string_length: bounded_candidate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Allowlist :** les clés reconnues sont limitées.
- **Valeurs :** les métadonnées ne deviennent pas du code.
- **Inconnues :** elles sont signalées sans mutation arbitraire.
- **Limite :** la taille des chaînes est bornée avant utilisation.

## 36. Manifeste d’import

Le manifeste d’import relie livraison, profil, sidecar, ressources externes, scène d’intégration et rapport de validation. Il permet de reconstruire pourquoi un asset a cette forme dans Godot.

Les empreintes sont calculées sur les fichiers matérialisés et restent absentes tant que le pilote n’existe pas.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_manifest:
  schema: asteria-import-manifest-v1
  import_id: AST-IMPORT-SCOUT-001
  asset_id: AST-CHAR-SCOUT-001
  delivery_version: 1.0.0
  profile_id: AST-IMPORT-PROFILE-CHARACTER-001
  source_path: res://assets/source_delivery/characters/scout.glb
  integration_scene: res://assets/integration/characters/scout_integrated.tscn
  external_resources: [AST-MAT-REMAP-SCOUT-001]
  hashes: pending_until_materialized
  status: draft
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** l’identité du traitement est distincte de celle de l’asset.
- **Profil :** les options attendues sont référencées.
- **Dépendances :** les ressources externes et scène locale sont listées.
- **Statut :** le manifeste reste brouillon avant preuves et approbation.

## 37. Post-import avec `EditorScenePostImport`

Un script `@tool` dérivé de `EditorScenePostImport` reçoit la racine importée, peut la valider ou la modifier, puis doit retourner la scène. Il s’exécute dans l’éditeur, pas comme logique gameplay.

Le script du pilote ajoute uniquement des métadonnées normalisées et vérifie les sockets requis ; il ne crée pas de règles métier.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
@tool
extends EditorScenePostImport

const REQUIRED_SOCKETS := {
    "socket_weapon_r": true,
    "socket_radio": true,
    "socket_voice": true,
}

func _post_import(scene: Node) -> Object:
    var found := {}
    _scan(scene, found)
    for socket_id: String in REQUIRED_SOCKETS:
        if not found.has(socket_id):
            push_error("IMPORT_SOCKET_MISSING: %s" % socket_id)
    scene.set_meta("asteria_import_profile", "AST-IMPORT-PROFILE-CHARACTER-001")
    return scene

func _scan(node: Node, found: Dictionary) -> void:
    if node.name.to_snake_case().begins_with("socket_"):
        found[node.name.to_snake_case()] = true
    for child: Node in node.get_children():
        _scan(child, found)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Annotation :** `@tool` autorise l’exécution dans l’éditeur.
- **Entrée :** `scene` est la racine générée par l’importeur.
- **Scan :** la récursion collecte des noms de sockets sans exécuter de méthode issue des données.
- **Retour :** la scène doit être renvoyée après traitement.
- **Limite :** le script signale un problème mais ne décide pas la qualité finale.

## 38. Idempotence du post-import

Un post-import peut être relancé plusieurs fois. Il doit produire le même résultat pour la même entrée et éviter d’ajouter à chaque passage des nœuds, suffixes ou ressources supplémentaires.

Les transformations utilisent des identifiants, remplacent une sortie dérivée connue ou vérifient sa présence avant création.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
post_import_idempotence:
  same_input_same_profile: same_scene_structure
  generated_node_name: __ASTERIA_IMPORT_METADATA
  creation_rule: create_only_if_absent
  replacement_rule: replace_owned_generated_content_only
  user_nodes: never_delete
  ordering: stable_sorted_by_node_path
  random_seed: none
  timestamp_in_output: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Répétition :** la réimportation ne doit pas accumuler des modifications.
- **Propriété :** seul le contenu généré et identifié peut être remplacé.
- **Ordre :** les parcours et sorties sont triés de façon stable.
- **Déterminisme :** l’heure et le hasard global sont exclus.

## 39. Refus de la réimportation récursive

Un script post-import ne doit pas lancer une nouvelle réimportation du fichier qu’il traite. Cette boucle peut saturer l’éditeur ou produire des résultats dépendants de l’ordre.

Les dépendances sont déclarées et les changements demandant un nouvel import sont planifiés après la fin du cycle courant.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reimport_guard:
  inside_post_import:
    call_scan_sources: false
    call_reimport_files: false
    mutate_source_file: false
  allowed:
    - validate_current_scene
    - modify_generated_scene_in_memory
    - emit_bounded_diagnostics
  deferred_reimport:
    owner: explicit_editor_tool
    condition: outside_import_callback
    max_attempts: 1
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Callback :** il traite uniquement la scène courante.
- **Interdits :** source et file d’import ne sont pas modifiées récursivement.
- **Diagnostics :** les messages restent bornés et structurés.
- **Reprise :** un outil séparé peut demander un import contrôlé.

## 40. Post-import ou plugin d’import personnalisé

`EditorScenePostImport` convient à la transformation d’une scène déjà comprise par Godot. `EditorImportPlugin` ou un importeur de format répond à un nouveau type de fichier ou à une ressource métier spécifique.

Le projet choisit la surface la plus petite et évite de créer un importeur personnalisé lorsque des presets et un post-import suffisent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
extension_choice:
  editor_scene_post_import:
    use_when: supported_scene_format_needs_validation_or_adjustment
  editor_import_plugin:
    use_when: custom_resource_format_requires_first_class_import
  scene_format_importer:
    use_when: unsupported_3d_scene_format_is_strategic
  default_choice: built_in_importer_plus_profile
  custom_code_requires: [tests, versioning, license_review, removal_plan]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Post-import :** il agit après la conversion d’une scène prise en charge.
- **Plugin :** il introduit un format ou type de ressource supplémentaire.
- **Format 3D :** la complexité n’est justifiée que par un besoin stratégique.
- **Gouvernance :** tout code d’import possède tests et plan de retrait.

## 41. Validateur structurel d’une scène importée

Un validateur statique peut parcourir la scène, compter les nœuds attendus, vérifier les types, sockets, matériaux et métadonnées, puis produire un rapport sans modifier l’asset.

Les résultats utilisent des codes stables et distinguent blocage, avertissement et information.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
@tool
extends RefCounted

func validate_scene(root: Node, required_paths: PackedStringArray) -> Array[Dictionary]:
    var findings: Array[Dictionary] = []
    for required_path: String in required_paths:
        if root.get_node_or_null(NodePath(required_path)) == null:
            findings.append({
                "code": "IMPORT_NODE_MISSING",
                "severity": "blocking",
                "path": required_path,
            })
    return findings
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type de retour :** le tableau contient des dictionnaires de diagnostic.
- **Chemins :** chaque `NodePath` attendu vient du profil versionné.
- **Refus :** un nœud absent produit un finding sans mutation.
- **Consommation :** l’appelant écrit le rapport et décide la suite selon la porte QA.

## 42. Diff de réimportation

La réimportation compare au minimum structure de nœuds, types, transforms, matériaux, surfaces, os, animations, blendshapes, collisions, sockets et métadonnées.

Le diff doit être stable, lisible et relié aux versions de livraison ; un simple constat visuel dans l’éditeur ne suffit pas.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reimport_diff:
  baseline_delivery: 1.0.0
  candidate_delivery: 1.1.0
  compare:
    - node_paths_and_types
    - transforms
    - mesh_surface_counts
    - material_slot_names
    - skeleton_hierarchy
    - animation_inventory
    - blendshape_channels
    - collision_shapes
    - socket_transforms
    - approved_metadata
  output: res://assets/reports/import/AST-IMPORT-SCOUT-001-diff.yaml
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Versions :** la baseline et la candidate sont explicites.
- **Structure :** le diff couvre plus que le nombre de fichiers.
- **Sortie :** le rapport est conservé hors des ressources runtime.
- **Décision :** les changements attendus et inattendus sont revus séparément.

## 43. Protection des personnalisations Godot

Chaque personnalisation est classée : override externe, nœud de scène d’intégration, configuration d’import ou donnée runtime. Cette classification indique ce qui doit survivre à une réimportation.

Une modification non classée est considérée à risque jusqu’à migration vers une surface possédée par le projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
customization_registry:
  - id: AST-CUSTOM-SCOUT-MATERIALS
    surface: external_resources
    survives_reimport: true
  - id: AST-CUSTOM-SCOUT-AUDIO
    surface: integration_scene
    survives_reimport: true
  - id: AST-CUSTOM-SCOUT-LOOP-FLAGS
    surface: import_configuration
    survives_reimport: expected
  - id: AST-CUSTOM-SCOUT-GAMEPLAY
    surface: domain_and_presentation_code
    imported_scene_storage: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Registre :** chaque personnalisation possède une surface autorisée.
- **Ressources :** les overrides externes restent indépendants du sous-resource importé.
- **Scène :** les nœuds locaux ne sont pas écrits dans la base régénérée.
- **Gameplay :** la logique ne réside jamais dans l’asset importé.

## 44. Dépendances, déplacements et renommages

Déplacer un fichier dans le dock FileSystem aide Godot à mettre à jour les références connues. Les déplacements externes massifs, renommages de matériaux ou changements de sockets exigent une campagne de dépendances.

Les identifiants d’asset restent stables même si le chemin change ; le manifeste enregistre la migration.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_move_plan:
  asset_id: AST-PROP-RELAY-001
  old_path: res://assets/source_delivery/relay/relay.glb
  new_path: res://assets/source_delivery/environment/relay/relay.glb
  operation_surface: Godot_FileSystem_dock
  impacted:
    - integration_scenes
    - import_manifest
    - material_remaps
    - test_scenes
  stable_identity_unchanged: true
  validation_required: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le déplacement ne crée pas un nouvel asset.
- **Outil :** le dock FileSystem conserve mieux les références Godot.
- **Impact :** les manifestes et remaps sont vérifiés.
- **Validation :** une ouverture et réimportation contrôlées suivent la migration.

## 45. Versionnement de `.import` et exclusion de `.godot`

Les fichiers `<asset>.import` contiennent les options et métadonnées importantes et doivent être commités. Le dossier `.godot` contient des caches régénérables et reste exclu du contrôle de version.

Supprimer `.godot` peut forcer une reconstruction locale ; supprimer un sidecar `.import` peut perdre la configuration partagée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
version_control_policy:
  commit:
    - "*.import"
    - source_deliveries
    - integration_scenes
    - external_resources
    - import_manifests
  ignore:
    - ".godot/"
    - generated_import_cache
  git_lfs_candidates:
    - "*.glb"
    - "*.blend"
    - large_audio_and_textures
  lfs_adoption: repository_policy_required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sidecars :** ils représentent une partie de la configuration reproductible.
- **Cache :** il est reconstruit par l’éditeur.
- **LFS :** les gros binaires peuvent utiliser une politique dédiée.
- **Gouvernance :** le suivi LFS est décidé au niveau du dépôt, pas par un utilisateur isolé.

## 46. Import headless et environnement propre

Une campagne automatisée peut ouvrir l’éditeur en mode headless pour reconstruire les imports dans un workspace propre, puis exécuter les validateurs. La commande exacte doit être qualifiée avec le binaire Godot retenu.

Le succès du processus prouve seulement que l’import et les contrôles ont terminé ; il ne prouve pas la qualité visuelle ou la performance en jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
headless_import_campaign:
  environment: clean_checkout
  godot_binary: qualified_4_7_1_standard
  steps:
    - restore_large_files
    - open_project_headless_editor
    - wait_for_import_completion
    - run_structure_validators
    - collect_import_logs
    - compare_expected_manifests
  visual_approval: separate_human_review
  runtime_benchmark: separate_campaign
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Workspace :** un checkout propre détecte les dépendances cachées.
- **Binaire :** la version et l’édition sont épinglées.
- **Logs :** les avertissements et échecs sont conservés.
- **Limite :** une exécution headless ne remplace pas la revue visuelle.

## 47. Profils de plateforme

Les formats sources restent communs, mais compression de texture, audio, influences de skin et budgets peuvent varier selon la plateforme ou le renderer.

Un profil de plateforme dérive des options autorisées sans modifier la source canonique ni prétendre qu’un réglage unique convient partout.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
platform_import_profiles:
  desktop_forward_plus:
    texture_compression: measured_candidate
    skin_influences: project_profile
    audio_streaming: per_asset
  mobile:
    texture_compression: device_family_candidate
    skin_influences: compatible_profile
    mesh_budget: reduced_candidate
  compatibility:
    feature_limits: explicit
  qualification:
    required_on_real_target: true
    inherited_from_desktop_without_test: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Desktop :** le profil de référence reste à mesurer.
- **Mobile :** les influences et budgets peuvent être plus contraints.
- **Compatibility :** les limites du renderer sont explicites.
- **Qualification :** aucune cible n’hérite d’une garantie sans test réel.

## 48. Budgets d’import et d’intégration

Le chapitre prépare des mesures de durée d’import, taille des caches, taille des ressources exportées, mémoire, temps de chargement, surfaces, matériaux et animations actives.

Les cibles initiales sont des bornes candidates ; elles deviennent des budgets seulement après baseline et répétitions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_budget_plan:
  metrics:
    - cold_import_duration_ms
    - warm_reimport_duration_ms
    - generated_cache_bytes
    - exported_resource_bytes
    - scene_load_duration_ms
    - resident_memory_bytes
    - mesh_surfaces
    - material_instances
    - animation_tracks
  repetitions: candidate
  baseline_machine: project_reference_hardware
  status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Froid :** l’import initial inclut la reconstruction des caches.
- **Chaud :** la réimportation mesure un changement contrôlé.
- **Runtime :** chargement et mémoire sont évalués séparément de l’éditeur.
- **Statut :** aucune valeur n’est enregistrée avant exécution.

## 49. Scène de test d’import

Une scène neutre instancie l’asset intégré avec éclairages, caméra, repères d’échelle et contrôles d’animation. Elle ne remplace ni la scène de validation finale du chapitre 29 ni le gameplay.

Le test isole les variables d’import afin de diagnostiquer un matériau, un pivot, une collision ou un socket.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_test_scene:
  path: res://assets/test_scenes/import/AST-IMPORT-PILOT-SCOUT-RELAY-001.tscn
  fixtures:
    - one_meter_reference
    - neutral_lighting
    - material_spheres
    - collision_debug_toggle
    - skeleton_and_socket_markers
    - animation_selector
    - lod_distance_markers
  domain_services: absent
  capture_plan: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fixture :** les repères rendent les défauts comparables.
- **Isolation :** aucun service métier n’est nécessaire.
- **Contrôles :** les sous-systèmes peuvent être activés séparément.
- **Captures :** les vues de référence restent à produire.

## 50. Matrice de tests

La campagne couvre import propre, réimportation sans changement, changement de mesh, matériau, squelette, animation, socket et chemin. Chaque scénario déclare résultat attendu et surface protégée.

Un test qui ne modifie aucune variable ne prouve pas que les personnalisations survivent à un changement réel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reimport_test_matrix:
  - case: clean_import
    expected: all_required_resources_present
  - case: identical_reimport
    expected: deterministic_no_unowned_changes
  - case: material_added
    expected: unknown_material_reported
  - case: socket_removed
    expected: blocking_finding
  - case: skeleton_hierarchy_changed
    expected: migration_required
  - case: source_path_moved
    expected: references_migrated_and_verified
  - case: integration_scene_custom_node
    expected: custom_node_preserved
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propre :** la baseline est reconstruite sans cache préexistant.
- **Identique :** la répétition vérifie l’idempotence.
- **Changements :** chaque cas cible une dépendance différente.
- **Protection :** les nœuds locaux doivent rester présents.

## 51. Workflow Solo

En Solo, un petit nombre de profils, des scènes d’intégration simples et une checklist de réimport réduisent les clics sans créer une plateforme complexe.

La personne conserve un journal de changements et exécute une revue différée avant d’accepter une nouvelle livraison.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
solo_workflow:
  profiles:
    - AST-IMPORT-PROFILE-STATIC-001
    - AST-IMPORT-PROFILE-CHARACTER-001
    - AST-IMPORT-PROFILE-ANIM-001
  integration_style: composition_first
  post_import_scripts: minimal
  reimport_check:
    - inspect_diff
    - open_test_scene
    - verify_materials
    - verify_animation
    - verify_collisions_and_sockets
  approval: manual_deferred_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Réduction :** trois profils couvrent le pilote sans surarchitecture.
- **Composition :** la scène locale protège les personnalisations.
- **Automatisation :** le script ne fait que les tâches répétitives sûres.
- **Revue :** une pause réduit le biais d’acceptation immédiate.

## 52. Workflow Studio

En Studio, les responsabilités de source, livraison, import, intégration et validation sont séparées. Les profils, scripts et manifestes passent par revue de code et les réimports importants possèdent une demande de changement.

La branche d’intégration conserve les rapports et ne fusionne pas une livraison dont les changements inattendus restent ouverts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
studio_workflow:
  roles:
    source_owner: art_department
    delivery_owner: technical_art
    import_profile_owner: technical_art
    integration_owner: gameplay_presentation
    final_validator: chapter_29_quality_gate
  controls:
    - reviewed_manifest
    - clean_import_ci
    - deterministic_post_import
    - dependency_diff
    - artistic_review
    - runtime_measurement
  unresolved_blocking_findings: prevent_merge
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôles :** chaque surface possède une autorité identifiable.
- **CI :** l’import propre détecte les dépendances locales cachées.
- **Diff :** les changements inattendus sont résolus avant fusion.
- **Validation :** le chapitre 29 prononce l’acceptation finale.

## 53. Provenance et licences à l’import

L’import ne transforme pas un asset juridiquement bloqué en ressource publiable. Le manifeste de provenance et les restrictions suivent la livraison et ses dérivés.

Les scripts post-import ne suppriment ni attribution, ni références de consentement, ni statut de retrait.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_provenance:
  asset_id: AST-CHAR-SCOUT-001
  publication_status: blocked_until_proof_bundle
  source_license_reference: LicenseRef-Asteria-Character-Source
  derived_resources:
    - imported_scene
    - external_material_overrides
    - animation_library
    - integration_scene
  attribution_required: manifest_value
  withdrawal_propagation: required
  legal_decision_by_automation: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** un asset bloqué reste bloqué après conversion.
- **Dérivés :** toutes les ressources conservent la relation de provenance.
- **Attribution :** les obligations ne sont pas effacées par l’import.
- **Autorité :** un script ne prononce aucune conclusion juridique.

## 54. Sécurité des scripts d’import

Un script d’import s’exécute dans l’éditeur avec accès au projet. Il traite les métadonnées et fichiers entrants comme non fiables, limite les chemins et n’exécute jamais un nom de méthode fourni par l’asset.

Les dépendances externes, plugins et convertisseurs sont qualifiés comme du code.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_security:
  input_trust: untrusted_until_validated
  allowed_roots:
    - res://assets/source_delivery/
    - res://assets/materials/
    - res://assets/reports/import/
  path_escape: blocking
  shell_execution: forbidden
  dynamic_method_dispatch_from_metadata: forbidden
  maximum_nodes: bounded_candidate
  maximum_metadata_bytes: bounded_candidate
  third_party_importer: license_and_security_review_required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Confiance :** un fichier artistique peut contenir des données inattendues.
- **Chemins :** les écritures restent sous des racines fermées.
- **Exécution :** les métadonnées ne construisent ni commande ni appel dynamique.
- **Dépendances :** un importeur tiers suit la politique de sécurité du dépôt.

## 55. Checklist de réimportation

La checklist commence avant de remplacer la livraison et se termine après les contrôles dans la scène d’intégration. Elle conserve baseline, candidate, rapport et décision.

Aucune case n’est cochée dans ce chapitre tant que le pilote n’est pas matérialisé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reimport_checklist:
  before:
    - freeze_baseline_delivery_and_manifest
    - record_expected_changes
    - verify_working_tree_clean
  import:
    - replace_candidate_delivery
    - inspect_import_configuration_diff
    - run_clean_reimport
  after:
    - compare_structure_and_dependencies
    - open_integration_scene
    - verify_materials_animations_collisions_sockets
    - execute_runtime_campaign
    - archive_report_and_decision
  current_status: all_open
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Avant :** la baseline et les changements attendus sont écrits.
- **Import :** la configuration est revue avant exécution.
- **Après :** les personnalisations et dépendances sont contrôlées.
- **Décision :** le rapport reste lié à la version candidate.

## 56. Porte d’acceptation du chapitre

La porte documentaire exige un périmètre complet, des contrats cohérents, des références cliquables, dix diagnostics et une synthèse Asteria. La porte runtime restera ouverte jusqu’à matérialisation.

Une future acceptation d’asset combinera import reproductible, personnalisations préservées, dépendances résolues, résultat visuel et budgets mesurés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_acceptance:
  static_review:
    scope_complete: true
    clickable_references: true
    diagnostics: 10
    duplicate_content: none
    runtime_claims: none
  future_runtime:
    clean_import: required
    identical_reimport: deterministic
    customizations_preserved: required
    dependencies_resolved: required
    visual_review: required
    performance_budget: measured
  current: static_review_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statique :** la documentation peut être acceptée sans simuler une exécution.
- **Runtime :** les critères futurs restent explicitement ouverts.
- **Personnalisations :** aucune scène locale ne doit être perdue.
- **Décision :** la porte du chapitre 29 restera l’autorité finale.

## 57. Diagnostics et corrections
<!-- qa:error-correction-section -->

Les cas suivants décrivent des défauts reproductibles. Chaque correction protège une frontière précise de la chaîne d’import.

### 57.1 Éditer directement la scène importée

**Symptôme ou risque :** La scène régénérée reçoit des personnalisations qui peuvent disparaître au prochain import.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
scene:
  path: res://assets/source_delivery/characters/scout.glb
  manual_changes:
    - attach_gameplay_script
    - edit_embedded_material
    - add_audio_player
  reimport_plan: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la scène régénérée reçoit des personnalisations qui peuvent disparaître au prochain import.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
scene:
  imported_base: res://assets/source_delivery/characters/scout.glb
  integration_scene: res://assets/integration/characters/scout_integrated.tscn
  local_changes:
    - gameplay_presentation_adapter
    - external_material_remap
    - audio_scene
  reimport_plan: compare_base_then_open_integration
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la scène locale possède les ajouts et référence seulement la base importée.

### 57.2 Distribuer uniquement un `.blend` à toute l’équipe

**Symptôme ou risque :** L’import dépend d’installations et versions non maîtrisées sur les postes et agents.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
delivery:
  format: blend
  blender_version: any
  team_requirement: implicit
  build_agents: no_blender
  fallback: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’import dépend d’installations et versions non maîtrisées sur les postes et agents.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
delivery:
  studio_default: glb
  blend_source: retained_in_authoring_workspace
  blender_version: qualified
  build_agents: import_glb_without_external_blender
  solo_direct_blend: optional_profile
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la livraison GLB est portable tandis que la voie `.blend` reste une option Solo qualifiée.

### 57.3 Utiliser OBJ pour un personnage animé

**Symptôme ou risque :** OBJ ne transporte pas les contrats nécessaires au rig, aux animations et aux morph targets.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
character_delivery:
  format: obj
  expected:
    - skeleton
    - skin
    - animations
    - blendshapes
  validation: visual_only
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** OBJ ne transporte pas les contrats nécessaires au rig, aux animations et aux morph targets.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
character_delivery:
  format: glb
  expected:
    - skeleton
    - skin
    - animations
    - blendshapes
  profile: AST-IMPORT-PROFILE-CHARACTER-001
  validation: structural_plus_visual
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** GLB porte la scène glTF 2.0 et le profil vérifie explicitement les canaux attendus.

### 57.4 Faire appliquer une règle gameplay par le post-import

**Symptôme ou risque :** Le fichier artistique devient une source de règles métier et contourne les autorités du Livre II.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
post_import:
  metadata: damage=25
  action: attach_damage_script
  authority: imported_node_name
  review: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le fichier artistique devient une source de règles métier et contourne les autorités du Livre II.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
post_import:
  metadata_allowlist: [asteria_asset_id, asteria_role]
  action: validate_and_tag_presentation
  gameplay_definition: separate_domain_resource
  authority: book_ii_systems
  review: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le post-import reste limité à la validation et la présentation ; les données métier sont séparées.

### 57.5 Ajouter des nœuds à chaque réimportation

**Symptôme ou risque :** La structure grossit à chaque exécution et le résultat dépend du nombre de réimports.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
post_import:
  every_run:
    - add_child: ImportMarker
    - append_suffix: _processed
  ownership_marker: absent
  deterministic: false
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la structure grossit à chaque exécution et le résultat dépend du nombre de réimports.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
post_import:
  generated_node: __ASTERIA_IMPORT_METADATA
  if_absent: create
  if_present: replace_owned_content
  ordering: stable
  timestamp: absent
  deterministic: true
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un nœud généré identifié est créé ou remplacé de manière idempotente.

### 57.6 Modifier un matériau embarqué sans l’externaliser

**Symptôme ou risque :** Le sous-resource appartient à la scène régénérée et peut être remplacé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
material:
  location: imported_scene_subresource
  edit: roughness_and_shader
  external_copy: none
  remap: none
  reimport_expectation: preserved
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le sous-resource appartient à la scène régénérée et peut être remplacé.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
material:
  imported_name: Armor_Main
  external_resource: res://assets/materials/overrides/scout_armor.tres
  remap_profile: AST-MAT-REMAP-SCOUT-001
  reimport_review: required
  ownership: project
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la ressource externe est possédée par le projet et réappliquée par un remap versionné.

### 57.7 Générer la collision depuis le mesh visuel sans contrat

**Symptôme ou risque :** La géométrie de rendu peut être trop complexe ou incompatible avec un corps dynamique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
collision:
  source: highest_resolution_render_mesh
  body: dynamic
  complexity: unbounded
  layers: imported_defaults
  measurement: assumed
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la géométrie de rendu peut être trop complexe ou incompatible avec un corps dynamique.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
collision:
  source: authored_simple_collision_mesh
  body_profile: explicit
  shape_family: convex_or_primitive_for_dynamic
  layers: integration_scene_owned
  measurement: pending_campaign
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une forme dédiée et un profil physique explicite séparent lisibilité visuelle et coût de collision.

### 57.8 Utiliser le nom d’un socket comme identité métier

**Symptôme ou risque :** La présence d’un nœud visuel crée implicitement un objet ou un droit d’équipement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
equipment:
  item_identity: Socket_Weapon
  attach_if_node_exists: true
  inventory_commit: absent
  missing_socket: create_item_anyway
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la présence d’un nœud visuel crée implicitement un objet ou un droit d’équipement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
equipment:
  item_identity: inventory_item_id
  inventory_commit: required_before_visual_attach
  socket_profile: AST-SOCKET-PROFILE-SCOUT-001
  visual_attach: presentation_after_commit
  missing_socket: diagnostic_and_visual_fallback
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’inventaire décide l’état, puis la présentation utilise le socket comme transform seulement.

### 57.9 Committer `.godot` et supprimer les sidecars `.import`

**Symptôme ou risque :** Le dépôt conserve un cache volumineux mais perd les options d’import partageables.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
version_control:
  commit: [.godot/]
  ignore: ["*.import"]
  result: cache_shared_configuration_lost
  clean_checkout: inconsistent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le dépôt conserve un cache volumineux mais perd les options d’import partageables.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
version_control:
  commit: ["*.import", source_deliveries, integration_scenes]
  ignore: [.godot/]
  clean_checkout: rebuild_import_cache
  expected: reproducible_configuration
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les sidecars versionnés reconstruisent le cache local ignoré dans un checkout propre.

### 57.10 Réimporter sans baseline ni diff

**Symptôme ou risque :** Les pertes de personnalisations et changements de dépendances ne sont pas détectés de façon reproductible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reimport:
  replace_source: true
  expected_changes: undocumented
  diff: none
  integration_scene_check: skipped
  approval: visual_glance
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les pertes de personnalisations et changements de dépendances ne sont pas détectés de façon reproductible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reimport:
  baseline_delivery: frozen
  candidate_delivery: versioned
  expected_changes: listed
  diff: structure_materials_rig_animation_collision_socket
  integration_scene_check: required
  approval: technical_plus_artistic_plus_runtime
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la baseline, le diff et la scène d’intégration rendent les écarts visibles avant acceptation.

## 58. Checklist de production et validation

La checklist reste ouverte tant que les livraisons, profils, scènes et mesures n’existent pas. Une revue statique ne coche aucune étape d’exécution.

- [ ] livraison et manifeste approuvés ;
- [ ] format choisi selon la matrice format-usage ;
- [ ] sidecar `.import` versionné ;
- [ ] dossier `.godot` exclu du dépôt ;
- [ ] profil d’import identifié ;
- [ ] scène importée laissée sans personnalisation locale fragile ;
- [ ] scène d’intégration créée par héritage ou composition ;
- [ ] matériaux externes et remaps contrôlés ;
- [ ] textures et audio conformes à leurs profils ;
- [ ] squelette, skin et blendshapes comparés au manifeste ;
- [ ] inventaire d’animations et boucles contrôlé ;
- [ ] collisions et sockets validés ;
- [ ] métadonnées limitées à l’allowlist ;
- [ ] post-import idempotent et sans réimportation récursive ;
- [ ] import propre exécuté dans un workspace neuf ;
- [ ] réimportation identique déterministe ;
- [ ] diff de livraison examiné ;
- [ ] personnalisations Godot préservées ;
- [ ] scène de test ouverte et capturée ;
- [ ] budgets éditeur et runtime mesurés ;
- [ ] provenance et droits toujours publiables ;
- [ ] rapport et décision archivés.

> **[LECTURE] État de la checklist — Ne pas saisir.**

```yaml
checklist_status:
  pilot: AST-IMPORT-PILOT-SCOUT-RELAY-001
  completed_items: 0
  open_items: 22
  evidence_level: static_review
  runtime_gate: open
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** la checklist s’applique au lot éclaireur-relais.
- **État :** aucune étape matérielle n’est déclarée accomplie.
- **Preuve :** la revue statique valide seulement la méthode.
- **Porte :** l’import et les mesures restent à exécuter.

## 59. Références techniques officielles

Les pages suivantes documentent les mécanismes utilisés. Elles ne remplacent ni la qualification d’un asset, ni la revue artistique, ni les tests de réimportation.

- [Godot 4.7 — Processus d’importation](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html)
- [Godot 4.7 — Pipeline des assets](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/index.html)
- [Godot 4.7 — Importer des scènes 3D](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html)
- [Godot 4.7 — Formats 3D disponibles](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)
- [Godot 4.7 — Configuration de l’import 3D](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html)
- [Godot 4.7 — Personnalisation des types par suffixes](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/node_type_customization.html)
- [Godot 4.7 — Paramètres avancés d’importation](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/using_the_advanced_import_settings_dialog.html)
- [Godot 4.7 — `ResourceImporterScene`](https://docs.godotengine.org/en/4.7/classes/class_resourceimporterscene.html)
- [Godot 4.7 — `EditorScenePostImport`](https://docs.godotengine.org/en/4.7/classes/class_editorscenepostimport.html)
- [Godot 4.7 — `EditorImportPlugin`](https://docs.godotengine.org/en/4.7/classes/class_editorimportplugin.html)
- [Godot 4.7 — Plugins d’import](https://docs.godotengine.org/en/4.7/tutorials/plugins/editor/import_plugins.html)
- [Godot 4.7 — Importer des images](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_images.html)
- [Godot 4.7 — Importer des échantillons audio](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_audio_samples.html)
- [Godot 4.7 — Organisation du projet](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html)
- [Godot — Contrôle de version](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html)
- [Khronos — Spécification glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- [Blender Manual — Export glTF 2.0](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html)
- [Livre III — Chapitre 4 : Pipeline Blender et organisation des fichiers](CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)
- [Livre III — Chapitre 16 : Textures, matériaux et pipeline PBR](CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md)
- [Livre III — Chapitre 18 : LOD, imposteurs et optimisation géométrique](CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md)
- [Livre III — Chapitre 19 : Rigging et skinning](CHAPITRE-19-Rigging-et-skinning.md)
- [Livre III — Chapitre 20 : Animation procédurale et animation par keyframes](CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md)
- [Livre III — Chapitre 27 : Synchronisation labiale et animation faciale](CHAPITRE-27-Synchronisation-labiale-et-animation-faciale.md)

> **[LECTURE] Portée des sources — Ne pas saisir.**

```yaml
reference_scope:
  godot_version: 4.7
  primary_topics:
    - import_process
    - 3d_scene_import
    - scene_inheritance
    - post_import
    - version_control
  external_standards:
    - gltf_2_0
    - blender_gltf_export
  runtime_evidence: separate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** les pages Godot 4.7 sont privilégiées pour les API du chapitre.
- **Sujets :** les sources couvrent import, héritage, post-traitement et versionnement.
- **Standards :** glTF et Blender complètent le contrat d’échange.
- **Limite :** la documentation ne constitue pas une preuve d’exécution du pilote.

## 60. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-IMPORT-PILOT-SCOUT-RELAY-001` comme pilote du chapitre. GLB constitue la livraison 3D par défaut ; glTF séparé, `.blend`, FBX et OBJ restent des variantes encadrées par la matrice format-usage.

Les fichiers `.import` sont versionnés et `.godot/` reste un cache exclu. Les personnalisations vivent dans des ressources externes et scènes d’intégration. Les post-imports sont idempotents, bornés, sans autorité métier et sans réimportation récursive.

> **[LECTURE] Décisions permanentes — Ne pas saisir.**

```yaml
asteria_import_decisions:
  pilot_id: AST-IMPORT-PILOT-SCOUT-RELAY-001
  import_manifest_id: AST-IMPORT-SCOUT-001
  static_profile_id: AST-IMPORT-PROFILE-STATIC-001
  character_profile_id: AST-IMPORT-PROFILE-CHARACTER-001
  animation_profile_id: AST-IMPORT-PROFILE-ANIM-001
  material_remap_id: AST-MAT-REMAP-SCOUT-001
  socket_profile_id: AST-SOCKET-PROFILE-SCOUT-001
  default_3d_delivery: glb
  imported_scene_rule: generated_read_only_surface
  customization_rule: external_resource_or_integration_scene
  version_control_rule: commit_import_sidecars_ignore_godot_cache
  automation_rule: idempotent_bounded_no_recursive_reimport
  authority_rule: import_never_commits_domain_state
  acceptance: clean_import_plus_diff_plus_visual_plus_runtime_plus_rights
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** profils, remap et manifeste restent stables et versionnés.
- **Format :** GLB est la voie par défaut, sans interdire les variantes qualifiées.
- **Personnalisations :** elles sont sorties de la scène régénérée.
- **Automatisation :** les scripts restent déterministes et limités.
- **Porte :** l’acceptation exige encore import propre, diff, revue, mesures et droits.
- **Réserve :** aucun asset, preset, script exécuté, scène ou benchmark n’est déclaré matérialisé.
