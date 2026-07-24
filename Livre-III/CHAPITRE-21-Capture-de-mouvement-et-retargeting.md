---
title: "Livre III — Chapitre 21 : Capture de mouvement et retargeting"
id: "DOC-L3-CH21"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre III"
chapter: 21
last-verified: "2026-07-24T18:01:38+02:00"
audit-status: "complete"
audit-date: "2026-07-24T18:01:38+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-21.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
reference-tools:
  blender:
    version: "5.2.0"
    channel: "Stable"
    qualification: "documentation-reviewed-against-5.0-manual"
  exchange:
    format: "glTF 2.0"
    default-container: "GLB"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Capture de mouvement et retargeting

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH21`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Transformer des mouvements capturés ou acquis légalement en animations dirigées, nettoyées, retargetées et intégrables dans la bibliothèque du projet, sans confondre fidélité au signal et qualité d’animation.

Le fil rouge utilise `AST-MOCAP-PILOT-SCOUT-001`, dérivé du rig humanoïde du chapitre 19 et du contrat d’animation du chapitre 20. Aucune session réelle, aucun clip, aucun GLB et aucune scène Godot ne sont présentés comme produits.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Rig validé et bibliothèque du chapitre 20
    ↓
Besoin d'animation et choix de capture
    ↓
Consentement, droits et préparation de session
    ↓
Acquisition, ingestion et gel de la source brute
    ↓
Nettoyage des trajectoires et des contacts
    ↓
Mapping, pose de référence et retargeting
    ↓
Corrections artistiques et fonctionnelles
    ↓
Export, import Godot et tests multi-rigs
    ↓
Porte d'acceptation et archivage des preuves
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** le squelette, la rest pose et les conventions du rig sont déjà approuvés.

- **Chaîne :** les données brutes restent séparées des prises sélectionnées et des animations publiées.

- **Aval :** le résultat alimente la bibliothèque du chapitre 20 et peut être mis en scène au chapitre 22.

- **Réserve :** le chapitre décrit la méthode sans revendiquer d’acquisition ou d’exécution réelle.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura choisir une famille de capture, préparer une session traçable, qualifier les droits, nettoyer bruit et glissements, construire un mapping et corriger un retargeting.

Il saura également comparer plusieurs morphologies, conserver le rythme utile, intégrer les clips dans Godot et distinguer une preuve statique d’un test runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  acquisition: [method_selection, calibration, take_review]
  governance: [consent, provenance, rights, restricted_storage]
  cleanup: [noise, gaps, contacts, root_path, collisions]
  retargeting: [bone_map, reference_pose, proportions, custom_profiles]
  correction: [hands, feet, center_of_mass, art_direction]
  integration: [gltf, animation_library, multi_rig_test]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Acquisition :** la méthode est choisie selon le mouvement, le budget et les contraintes du lieu.

- **Gouvernance :** les autorisations sont vérifiées avant la publication d’un dérivé.

- **Technique :** mapping, poses et proportions sont traités comme des contrats explicites.

- **Validation :** les contacts, le rythme, les morphologies et les droits possèdent chacun une porte.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les manifestes, scripts, profils et scènes montrés sont des exemples documentaires non exécutés.

Aucun seuil de filtrage, taux d’erreur de contact, temps CPU ou gain de production n’est déclaré mesuré. Ces valeurs seront établies seulement sur les données et machines réelles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static-review
  performer_recorded: false
  raw_session_materialized: false
  cleanup_executed: false
  retargeting_executed: false
  gltf_exported: false
  godot_imported: false
  multi_rig_tested: false
  runtime_measurements: false
  pdf_produced: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la cohérence de la procédure est relue, pas la qualité d’un mouvement inexistant.

- **Données :** aucune information personnelle de performeur n’est créée dans le dépôt public.

- **Mesures :** les tolérances demeurent des champs à renseigner après essais.

- **Publication :** le PDF reste différé à la fin du Livre III.

## 4. Frontières avec les chapitres voisins

Le chapitre 19 reste propriétaire du squelette, des poids, des axes, du roll et de la rest pose. Le chapitre 20 reste propriétaire des principes de keyframes, des cycles, du root motion, des événements et de l’`AnimationTree`.

Le présent chapitre transforme des sources capturées en clips compatibles. Le chapitre 22 décide ensuite cadrages, plans, rythmes narratifs et synchronisation cinématique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapter_19: rig_skeleton_skinning_rest_pose
  chapter_20: authored_animation_library_and_runtime_graph
  chapter_21: capture_cleanup_mapping_and_retargeting
  chapter_22: cinematics_cameras_and_staging
  chapter_28: global_asset_integration
  book_iv: whole_game_runtime_optimization
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rig :** une incompatibilité de squelette remonte au chapitre 19 et n’est pas masquée ici.

- **Animation :** les corrections artistiques utilisent les principes déjà établis au chapitre 20.

- **Cinématique :** le clip n’impose ni focale, ni découpage, ni intention dramatique.

- **Intégration :** la chaîne globale de publication reste réservée au chapitre 28.

## 5. Asset pilote et scénario de validation

Le pilote représente un éclaireur qui marche, s’arrête, se baisse, saisit une radio puis se redresse. Cette séquence combine locomotion, transfert de poids, contacts de mains et changements de hauteur.

Trois cibles utilisent le même mouvement : le rig de référence, une morphologie courte et robuste, puis une morphologie grande et fine. Le test révèle les défauts de proportion qu’un seul personnage masquerait.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pilot:
  asset_id: AST-MOCAP-PILOT-SCOUT-001
  source_rig_profile: MOCAP-HUMANOID-SOURCE-V1
  target_rigs:
    - HUMANOID-ASTERIA-V1
    - HUMANOID-ASTERIA-SHORT-V1
    - HUMANOID-ASTERIA-TALL-V1
  action: walk_crouch_radio_stand
  validation_scene: MOCAP_RETARGET_BENCH_001
  status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** la séquence sollicite pieds, bassin, colonne, épaules et mains.

- **Variation :** les trois morphologies partagent un profil fonctionnel sans partager leurs longueurs.

- **Scène :** le banc de test est un livrable prévu et non une scène déclarée existante.

- **Décision :** le statut reste candidat jusqu’aux revues juridique, artistique et technique.

## 6. Vocabulaire de la chaîne mocap

Une session regroupe un contexte d’acquisition. Une prise est un enregistrement continu. Un clip est un extrait sélectionné. Une animation publiée est un dérivé nettoyé, retargeté et approuvé.

Ces mots ne sont pas interchangeables : une prise brute peut contenir plusieurs actions, des répétitions, des données de calibration et des passages refusés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
terminology:
  session: acquisition_context_and_participants
  take: continuous_recording
  selected_clip: bounded_excerpt_from_take
  cleaned_clip: corrected_source_skeleton_motion
  retargeted_clip: motion_transformed_for_target_rig
  published_animation: approved_library_asset
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Session :** elle possède lieu, méthode, personnes, autorisations et calibration.

- **Prise :** elle conserve le signal continu sans prétendre être un asset final.

- **Clip :** ses bornes et sa raison de sélection sont tracées.

- **Publication :** seul le dérivé approuvé rejoint la bibliothèque consommable.

## 7. Hiérarchie des sources et dérivés

La source brute est immuable. Les opérations de nettoyage et de retargeting produisent de nouveaux fichiers ou de nouvelles Actions reliés au parent par un manifeste.

Revenir à la source reste possible lorsque le filtre, le mapping ou la direction artistique changent. Un export GLB ou un import Godot ne devient jamais l’autorité de la session.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
source_hierarchy:
  immutable_raw:
    - sessions/AST-MOCAP-SESSION-001/raw/**
  working:
    - sessions/AST-MOCAP-SESSION-001/work/**
  selected:
    - clips/source/AST-MOCAP-CLIP-001.blend
  cleaned:
    - clips/clean/AST-MOCAP-CLIP-001-CLEAN.blend
  retargeted:
    - clips/target/AST-MOCAP-CLIP-001-HUMANOID-ASTERIA-V1.blend
  exchange:
    - exports/AST-MOCAP-CLIP-001.glb
  godot_derived:
    - animation_libraries/mocap_scout.tres
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Immuable :** la source brute peut être restreinte mais ne reçoit aucune correction destructive.

- **Travail :** les caches et essais restent reproductibles et séparés.

- **Cible :** chaque retargeting nomme le rig et la version visés.

- **Dérivé :** GLB et ressources Godot sont reconstruits depuis les sources approuvées.

## 8. Panorama des familles de capture

Aucune technologie ne capture directement une animation parfaite. Chaque famille observe certains signaux, reconstruit des poses et laisse des zones d’incertitude différentes.

Le choix commence par l’action à obtenir, les contacts importants, la mobilité du dispositif, le budget, la confidentialité et le temps de correction disponible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
capture_families:
  optical_marker: high_spatial_control_in_calibrated_volume
  inertial: portable_orientation_measurement_with_drift_risk
  markerless_video: accessible_reconstruction_with_occlusion_risk
  depth_or_hybrid: additional_geometry_or_sensor_fusion
  manual_reference: video_only_for_authored_animation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Optique :** les marqueurs facilitent l’identification mais exigent volume et calibration.

- **Inertiel :** les capteurs suivent les orientations sans voir directement le sol ou les collisions.

- **Sans marqueur :** la reconstruction dépend des vues, occultations et modèles utilisés.

- **Référence :** une vidéo peut guider l’animation sans devenir une capture squelettique.

## 9. Capture optique avec marqueurs

Un système optique reconstruit les marqueurs visibles depuis plusieurs caméras calibrées. Les occultations, échanges d’étiquettes et marqueurs déplacés restent possibles.

Le costume, la disposition des marqueurs et la définition du squelette de résolution font partie de la version de session.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
optical_session:
  camera_volume: calibrated
  marker_set: AST-HUMANOID-MARKERS-V1
  occlusion_review: required
  label_swap_review: required
  solve_skeleton: MOCAP-HUMANOID-SOURCE-V1
  raw_2d_and_3d_preserved: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Volume :** les caméras doivent observer une zone commune qualifiée.

- **Marqueurs :** leur position physique et leur étiquette appartiennent au protocole.

- **Résolution :** le squelette reconstruit est un dérivé du signal optique.

- **Preuve :** les données brutes utiles au recalcul sont conservées selon les droits.

## 10. Capture inertielle

Les capteurs inertiels estiment surtout des orientations segmentaires. Ils sont mobiles et moins sensibles aux occultations visuelles, mais peuvent dériver et ne mesurent pas automatiquement un contact exact avec le sol.

La calibration initiale, la pose de référence, la fixation des capteurs et les perturbations magnétiques doivent être documentées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
inertial_session:
  suit_profile: AST-IMU-HUMANOID-V1
  reference_pose: A_POSE_CAPTURE_V1
  sensor_attachment_check: required
  magnetic_environment_note: required
  root_position_source: system_specific
  floor_contact_correction: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Orientation :** les rotations segmentaires sont la donnée principale.

- **Position :** la translation globale peut dépendre d’une estimation ou d’un capteur complémentaire.

- **Dérive :** la stabilité doit être vérifiée sur la durée de la prise.

- **Contact :** les pieds sont contrôlés après résolution plutôt que supposés verrouillés.

## 11. Capture vidéo sans marqueur

La capture sans marqueur estime le mouvement depuis une ou plusieurs vidéos. Les vêtements amples, occultations, flou, cadrages incomplets et ambiguïtés de profondeur peuvent dégrader le résultat.

La vidéo contient potentiellement l’image et la voix d’une personne ; son stockage, son accès et ses droits doivent être plus stricts qu’un simple fichier d’animation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
markerless_session:
  camera_views: [front_oblique, side_oblique]
  full_body_visibility: required
  synchronized_recording: required
  reconstruction_model: qualified_and_versioned
  video_access: restricted
  identity_removal_before_publication: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vues :** des angles complémentaires réduisent certaines ambiguïtés sans les supprimer.

- **Modèle :** l’application, les poids et les paramètres appartiennent à la provenance.

- **Données :** la vidéo source peut contenir des données personnelles.

- **Publication :** le dépôt public ne reçoit ni vidéo brute ni document de consentement signé.

## 12. Capture profondeur, hybride et références

Un capteur de profondeur ajoute une estimation géométrique locale ; une chaîne hybride combine plusieurs modalités. La fusion ne garantit pas une vérité parfaite si leurs temps, axes ou calibrations divergent.

Une simple vidéo de référence reste souvent suffisante lorsque le projet veut une interprétation keyframée plutôt qu’une reconstruction dense.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hybrid_capture:
  modalities: [rgb_video, depth, inertial_optional]
  common_timebase: required
  common_coordinate_frame: required
  calibration_record: required
  fusion_software_version: required
  fallback: authored_animation_from_reference
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Synchronisation :** les modalités doivent désigner le même instant.

- **Repère :** les transformations entre capteurs sont enregistrées.

- **Fusion :** l’outil et sa version sont des dépendances de production.

- **Repli :** une référence vidéo peut être préférée à un signal fusionné fragile.

## 13. Matrice de choix de la méthode

La meilleure méthode est celle qui produit des données corrigeables pour l’action réelle, dans le cadre juridique et budgétaire disponible.

Le tableau de décision est rempli avant réservation du matériel ou téléchargement d’un pack ; une source gratuite mais juridiquement indéterminée reste bloquée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
method_decision:
  action_id: AST-ACT-SCOUT-RADIO-001
  needs:
    ground_contacts: high
    finger_detail: low
    capture_volume: medium
    portability: medium
    performer_privacy: high
  candidates:
    optical_marker: evaluate
    inertial: evaluate
    markerless_video: evaluate
  selected: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Besoin :** les contacts et détails attendus précèdent le choix de technologie.

- **Contraintes :** confidentialité, lieu et temps de correction sont explicites.

- **Candidats :** plusieurs voies peuvent être comparées sans décision anticipée.

- **Statut :** aucune méthode n’est sélectionnée avant qualification réelle.

## 14. Volume, sécurité et conditions de session

Le volume de capture doit être dégagé, éclairé ou instrumenté selon la méthode, avec un sol stable et des accessoires sûrs. La performance ne justifie jamais un risque physique non maîtrisé.

Les limites de déplacement, sorties d’urgence, pauses, hydratation et responsabilités sont communiquées au performeur avant la prise.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
session_safety:
  floor: stable_and_marked
  obstacles: removed_or_padded
  movement_limits: rehearsed
  props: safe_replicas
  emergency_stop: communicated
  fatigue_breaks: scheduled
  incident_log: available
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sol :** les contacts ne sont interprétables que sur une surface connue.

- **Accessoires :** une réplique sûre remplace un objet dangereux ou fragile.

- **Arrêt :** le performeur peut interrompre la prise sans pénalité.

- **Journal :** un incident suspend la session et déclenche une revue.

## 15. Brief du performeur et intention

Le brief décrit la fonction de l’action, le contexte, la vitesse relative, les contacts et les variantes demandées. Il ne réduit pas la personne à une machine qui doit copier une trajectoire.

Une répétition filmée ou observée permet d’ajuster le volume et l’accessoire avant d’enregistrer les prises destinées à la sélection.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
performer_brief:
  action: walk_crouch_radio_stand
  narrative_context: cautious_scout_under_observation
  required_contacts: [feet_floor, hand_radio]
  variants: [neutral, fatigued, urgent]
  forbidden_motion: unsafe_knee_drop
  direction_notes: versioned
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** l’intention influence rythme, posture et regard.

- **Contacts :** les interactions indispensables sont annoncées.

- **Variantes :** elles répondent à des besoins identifiés, pas à une accumulation.

- **Sécurité :** un mouvement dangereux est remplacé avant la prise.

## 16. Consentement, contrat et droit à l’image

L’autorisation d’enregistrer ne signifie pas automatiquement autorisation de modifier, retargeter, entraîner un modèle, redistribuer les données brutes ou exploiter le résultat dans tous les territoires.

Le projet décrit séparément chaque usage. Les documents signés et données d’identité restent dans un stockage restreint, tandis que le dépôt public conserve seulement un identifiant de preuve et un statut.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
consent_record:
  evidence_id: LicenseRef-ASTERIA-MOCAP-CONSENT-001
  capture_authorized: true
  derivative_animation_authorized: true
  commercial_game_use: true
  raw_redistribution: false
  model_training: false
  territory_and_duration: contract_defined
  public_repository_storage: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** chaque droit est un champ distinct au lieu d’un accord global ambigu.

- **Dérivé :** le retargeting et la modification sont autorisés explicitement.

- **Restriction :** la donnée brute peut rester interdite de redistribution.

- **Stockage :** le contrat réel n’est pas versé dans le dépôt public.

## 17. Données personnelles et accès restreint

Les vidéos, voix, silhouettes, mesures corporelles et métadonnées de session peuvent identifier une personne. Le principe de minimisation limite ce qui est collecté, conservé et partagé.

Les accès sont nominatifs, les exports de revue sont réduits au nécessaire et la durée de conservation suit le contrat et la politique du projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
data_handling:
  raw_video_classification: restricted_personal_data
  access_roles: [capture_lead, legal_reviewer]
  public_derivative: skeletal_animation_only_if_authorized
  retention_policy: contract_and_policy_defined
  deletion_request_process: documented
  backup_scope: restricted_storage_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classification :** la sensibilité est décidée avant le stockage.

- **Accès :** le besoin opérationnel détermine les rôles autorisés.

- **Dérivé :** une animation squelettique n’est publiée que si le contrat le permet.

- **Cycle de vie :** conservation, retrait et sauvegarde sont cohérents.

## 18. Fiche de provenance d’une session

La fiche relie personnes sous pseudonyme de production, matériel, logiciels, calibrations, prises, droits et transformations. Elle ne remplace ni le contrat ni la revue humaine.

Les empreintes prouvent l’identité des fichiers enregistrés, pas la légalité ou l’auteur du mouvement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
session_provenance:
  session_id: AST-MOCAP-SESSION-001
  performer_ref: restricted:PERFORMER-001
  method: pending_selection
  hardware_profile: pending
  software_and_versions: []
  calibration_record: pending
  rights_evidence: LicenseRef-ASTERIA-MOCAP-CONSENT-001
  raw_manifest_sha256: pending
  reviewer: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le dépôt utilise une référence et non l’identité civile.

- **Environnement :** matériel, logiciel et calibration sont nécessaires au recalcul.

- **Droits :** la preuve juridique est référencée sans être exposée.

- **Empreinte :** SHA-256 détecte une modification mais ne conclut pas sur les droits.

## 19. Identifiants, prises et noms de fichiers

Les identifiants restent stables même lorsque le titre affiché change. Une prise conserve son numéro et son statut ; une nouvelle sélection crée un nouveau clip sans renommer l’historique.

Les noms évitent les données personnelles et les adjectifs tels que `final_final`.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
naming:
  session: AST-MOCAP-SESSION-001
  take_pattern: AST-MOCAP-SESSION-001-TAKE-{sequence}
  clip_pattern: AST-MOCAP-CLIP-{sequence}
  target_pattern: "{clip_id}-{target_rig_id}-{version}"
  examples:
    - AST-MOCAP-SESSION-001-TAKE-004
    - AST-MOCAP-CLIP-001-HUMANOID-ASTERIA-V1-1.0.0
  forbidden: [performer_real_name, final_final, new_take]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Session :** elle reste l’unité de provenance de l’acquisition.

- **Prise :** la séquence reflète l’ordre de création sans réutilisation.

- **Cible :** le rig et la version rendent la compatibilité visible.

- **Confidentialité :** aucun nom civil n’entre dans les chemins partagés.

## 20. Arborescence de travail

Les données personnelles et brutes ne résident pas dans le dépôt documentaire. Le workspace de production distingue stockage restreint, sources de travail, exports et livraisons.

Les caches de solveur, vidéos proxy et fichiers temporaires peuvent être régénérés ou supprimés selon leur politique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
workspace:
  restricted:
    - mocap/private/contracts/
    - mocap/private/raw_video/
    - mocap/private/raw_sensor/
  versioned_metadata:
    - mocap/manifests/
    - mocap/mappings/
    - mocap/reports/
  source_work:
    - mocap/source_blend/
  exports:
    - mocap/exports_gltf/
  cache:
    - mocap/cache/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Restreint :** contrats et signaux identifiants sont séparés du dépôt public.

- **Métadonnées :** les manifestes publiables évitent les données personnelles.

- **Source :** les fichiers Blender approuvés restent distincts des GLB.

- **Cache :** les dérivés temporaires ne sont pas traités comme des versions.

## 21. Unités, axes et repère de capture

Le signal source doit déclarer unité, axe vertical, direction avant, latéralité et origine. Un mouvement plausible dans un repère incorrect peut être tourné, reflété ou mis à l’échelle sans alerte évidente.

La conversion vers Blender puis Godot suit les conventions du pipeline, sans parent correctif improvisé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
coordinate_contract:
  source_unit: meters
  source_up_axis: declared_by_system
  source_forward_axis: declared_by_system
  handedness: declared_by_system
  floor_plane: calibrated
  blender_contract: metric_minus_y_forward
  godot_arrival: plus_z_forward_after_gltf_conversion
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** les conventions sont lues dans le format ou le logiciel d’acquisition.

- **Sol :** le plan calibré sert aux contrôles de contacts.

- **Blender :** le pipeline hérité du chapitre 4 reste l’autorité.

- **Conversion :** un parent tourné ne masque pas une convention mal comprise.

## 22. Fréquence, temps et synchronisation

La fréquence d’échantillonnage décrit les mesures du système ; le FPS de travail décrit la timeline d’auteur. Les deux peuvent différer sans que l’un soit automatiquement faux.

Les caméras, capteurs, audio de référence et accessoires animés doivent partager un temps corrélé ou une méthode de recalage documentée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
time_contract:
  capture_sample_rate_hz: system_declared
  source_timecode: preserved_if_available
  authoring_fps: 30_candidate
  resampling_method: documented
  synchronized_streams:
    - body_motion
    - reference_video
    - prop_tracking_optional
  dropped_sample_report: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Échantillons :** la fréquence source reste dans les métadonnées.

- **Auteur :** le FPS candidat ne réécrit pas l’histoire temporelle de la prise.

- **Recalage :** la méthode de resampling est versionnée.

- **Perte :** les trous ne sont pas masqués par une interpolation silencieuse.

## 23. Calibration du volume et des capteurs

Une calibration valide le rapport entre dispositifs, sol, origine et échelle. Elle est répétée lorsque le système, le volume ou la fixation des capteurs change.

Une prise de calibration reçoit un identifiant et un résultat ; la phrase « calibré correctement » sans mesure ni journal est insuffisante.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
calibration:
  calibration_id: AST-MOCAP-CAL-001
  session_id: AST-MOCAP-SESSION-001
  floor_plane_recorded: true
  scale_reference_recorded: true
  sensor_alignment_recorded: method_specific
  validation_metrics: pending_runtime
  accepted_by: pending
  expires_on_change: [hardware, volume, attachment]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la session pointe vers une calibration précise.

- **Références :** sol et échelle rendent les translations interprétables.

- **Mesures :** les champs restent en attente tant qu’aucune exécution n’a eu lieu.

- **Invalidation :** un changement matériel déclenche une nouvelle calibration.

## 24. Pose de référence du performeur

La pose de référence de capture n’est pas automatiquement la rest pose du rig cible. Elle décrit comment le système interprète les orientations au début de la session.

A-pose, T-pose et pose neutre sont nommées, photographiées ou enregistrées selon les droits, puis reliées au profil de mapping.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
capture_reference_pose:
  pose_id: A_POSE_CAPTURE_V1
  arms: abducted_candidate_angle
  palms: declared_orientation
  feet: parallel_on_floor
  spine: neutral
  performer_take: AST-MOCAP-SESSION-001-TAKE-CAL-001
  target_rest_pose_equivalence: not_assumed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capture :** la pose initialise le solveur ou fournit une référence.

- **Description :** bras, paumes, pieds et colonne sont explicités.

- **Lien :** la prise de calibration est retrouvable.

- **Limite :** l’équivalence avec la rest pose cible doit être calculée ou corrigée.

## 25. Slate et métadonnées de prise

Avant chaque prise, le slate confirme session, numéro, action, variante, performer de production et événement particulier. Il réduit les ambiguïtés lors de l’ingestion.

Une erreur de slate ne conduit pas à renommer arbitrairement le fichier : le manifeste conserve le nom acquis et ajoute une correction tracée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
take_metadata:
  take_id: AST-MOCAP-SESSION-001-TAKE-004
  action_id: AST-ACT-SCOUT-RADIO-001
  variant: cautious
  calibration_id: AST-MOCAP-CAL-001
  performer_ref: restricted:PERFORMER-001
  slate_status: confirmed
  notes: no_incident
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Corrélation :** la prise est liée au besoin d’animation.

- **Calibration :** le solveur utilisé reste identifiable.

- **Personne :** la référence pseudonymisée pointe vers le stockage restreint.

- **Correction :** une note de manifeste remplace un renommage destructif.

## 26. Procédure d’enregistrement

La session commence par calibration, répétition, prise courte de contrôle et revue. Les prises utiles sont enregistrées avec pauses et notes plutôt qu’en continu sans repères.

Une personne surveille la qualité technique pendant qu’une autre, si disponible, dirige l’intention artistique ; en Solo, ces revues sont séparées dans le temps.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
recording_order:
  - verify_rights_and_safety
  - calibrate_system
  - rehearse_inside_volume
  - record_control_take
  - inspect_contacts_and_occlusion
  - record_directed_variants
  - log_incidents_and_notes
  - close_and_hash_session
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** droits et sécurité précèdent l’allumage de l’enregistrement utile.

- **Contrôle :** une prise courte révèle les défauts avant la série.

- **Direction :** les variantes répondent au brief versionné.

- **Clôture :** manifestes et empreintes figent le lot reçu.

## 27. Revue et sélection des prises

La sélection sépare qualité du signal, qualité de performance et utilité pour le jeu. Une prise techniquement propre peut être artistiquement hors intention ; une prise expressive peut demander trop de réparation.

Le rapport conserve les prises refusées et leur raison sans les publier dans la bibliothèque.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
take_review:
  take_id: AST-MOCAP-SESSION-001-TAKE-004
  signal_quality: pending
  performance_intent: pending
  contact_quality: pending
  repair_cost: pending
  decision: pending
  rejection_codes:
    - RIGHTS_BLOCKED
    - SIGNAL_INCOMPLETE
    - PERFORMANCE_OFF_BRIEF
    - REPAIR_COST_EXCESSIVE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Axes :** signal, intention, contacts et coût sont évalués séparément.

- **Décision :** le statut n’est pas déduit d’une note unique.

- **Refus :** un code stable facilite les statistiques et les reprises.

- **Historique :** une prise refusée n’est pas effacée sans politique de conservation.

## 28. Ingestion, quarantaine et empreintes

L’ingestion copie les fichiers dans une zone de quarantaine, vérifie taille et format, calcule les empreintes puis écrit le manifeste avant toute conversion.

Les outils d’acquisition propriétaires ou formats inconnus restent isolés jusqu’à qualification ; ouvrir un fichier n’autorise pas sa publication.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ingestion:
  input_root: restricted_drop/AST-MOCAP-SESSION-001
  quarantine_root: restricted_quarantine/AST-MOCAP-SESSION-001
  checks: [expected_files, size_limits, format_allowlist, sha256]
  conversion_allowed_after: [rights_check, integrity_check, tool_qualification]
  manifest: mocap/manifests/AST-MOCAP-SESSION-001.yaml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la zone de dépôt ne devient pas la source canonique.

- **Contrôles :** intégrité et formats sont vérifiés avant conversion.

- **Outil :** un convertisseur tiers est traité comme une dépendance de production.

- **Manifeste :** les fichiers acceptés et bloqués sont tous enregistrés.

## 29. Chaîne non destructive de travail

Chaque transformation crée un dérivé nommé : résolution, sélection, nettoyage, retargeting, correction artistique et export. Une étape peut être rejouée depuis son parent.

Les opérations manuelles sont décrites par un rapport ou des marqueurs de version, car elles ne sont pas toujours reproductibles automatiquement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transformation_chain:
  raw_signal: immutable
  solved_source_skeleton: derived
  selected_clip: derived
  cleaned_source_clip: derived
  retargeted_target_clip: derived
  art_directed_clip: approved_candidate
  gltf_export: reproducible_derivative
  manual_changes_report: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Parenté :** chaque dérivé nomme son entrée et son outil.

- **Reprise :** une nouvelle méthode de nettoyage repart d’un parent stable.

- **Manuel :** les corrections sont listées même sans script reproductible.

- **Export :** le GLB peut être reconstruit depuis le candidat approuvé.

## 30. Diagnostic initial du mouvement

Avant de filtrer, l’animateur lit la prise complète, les courbes, la trajectoire du root, les contacts et les vidéos de référence autorisées. Le but est d’identifier les causes plutôt que de lisser tous les canaux.

Le rapport distingue bruit haute fréquence, trous, sauts d’étiquette, dérive, pénétrations et défauts de performance.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
initial_diagnostic:
  clip_id: AST-MOCAP-CLIP-001
  inspect:
    - source_timeline
    - root_trajectory
    - planted_contacts
    - joint_limits
    - reference_video_if_authorized
  anomalies:
    noise: []
    gaps: []
    label_swaps: []
    drift: []
    collisions: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lecture :** la prise complète révèle les erreurs qui traversent une coupe.

- **Causes :** les catégories conduisent à des corrections différentes.

- **Référence :** la vidéo n’est consultée que selon les droits.

- **Rapport :** l’absence d’anomalie doit résulter d’une revue, pas d’un champ omis.

## 31. Filtrage et tolérances

Un filtre réduit certains signaux indésirables mais peut retarder, amortir ou déformer un mouvement utile. Sa fenêtre, son ordre et ses canaux sont donc des paramètres versionnés.

Les seuils varient selon translation, rotation, articulation et fonction. Ils restent `pending_measurement` dans ce chapitre.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
filter_profile:
  profile_id: MOCAP-CLEAN-HUMANOID-V1
  method: pending_selection
  translation_tolerance_m: pending_measurement
  rotation_tolerance_deg: pending_measurement
  channels:
    root: preserve_direction_changes
    feet: preserve_contacts
    hands: preserve_prop_contact
    spine: preserve_rhythm
  before_after_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Méthode :** le nom du filtre seul ne suffit pas sans paramètres.

- **Unités :** mètres et degrés possèdent des tolérances distinctes.

- **Fonction :** un pied planté et une respiration ne se nettoient pas pareil.

- **Comparaison :** la source et le dérivé sont lus côte à côte.

## 32. Trous et interpolation

Un trou court entre deux mesures fiables peut être interpolé ; un intervalle long ou un mouvement occulté complexe peut exiger une reprise, une référence ou une reconstruction manuelle.

Le traitement conserve les bornes du trou, la méthode et un niveau de confiance au lieu de présenter le segment comme mesuré.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gap_repair:
  gap_id: GAP-CLIP001-003
  channel_group: left_wrist
  start_time_s: pending
  end_time_s: pending
  duration_s: derived
  repair_method: pending_selection
  confidence: pending
  measured_segment: false
  human_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bornes :** le segment affecté reste localisable.

- **Méthode :** interpolation et reconstruction manuelle sont distinguées.

- **Confiance :** le dérivé ne prétend pas être une observation brute.

- **Revue :** les contacts ou gestes expressifs nécessitent une validation humaine.

## 33. Pics, jitter et échanges d’étiquettes

Un pic isolé peut provenir d’une mauvaise association, d’un marqueur occulté ou d’un capteur instable. Le supprimer sans examiner les canaux voisins peut casser la continuité.

Les échanges d’étiquettes exigent souvent de corriger l’identité des trajectoires avant de filtrer leurs valeurs.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
spike_review:
  anomaly_id: SPIKE-CLIP001-007
  suspected_cause: [occlusion, label_swap, sensor_shift]
  affected_channels: []
  neighbor_window: pending_measurement
  identity_fix_before_filter: true
  correction_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cause :** le diagnostic précède la modification numérique.

- **Voisins :** les trajectoires liées aident à retrouver la continuité.

- **Identité :** une mauvaise étiquette n’est pas un simple bruit.

- **Statut :** le rapport conserve les anomalies non résolues.

## 34. Trajectoire du root et orientation

Le root décrit le déplacement global utile à l’animation, mais il ne doit pas absorber chaque oscillation du bassin. Sa trajectoire est séparée du mouvement local du squelette.

Les changements de direction, démarrages et arrêts sont préservés ; une ligne artificiellement droite peut supprimer l’intention et créer un décalage avec les pieds.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
root_cleanup:
  source_root: capture_root
  target_motion_root: RootMotion
  preserve:
    - starts
    - stops
    - turns
    - intentional_vertical_change
  remove_or_reassign:
    - sensor_drift
    - pelvis_local_sway
  gameplay_authority: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** root de déplacement et bassin ne portent pas la même responsabilité.

- **Intention :** les changements de direction restent visibles.

- **Dérive :** une correction globale est justifiée par le diagnostic.

- **Autorité :** le déplacement gameplay demeure décidé hors du clip visuel.

## 35. Plan du sol et contacts des pieds

Le sol calibré fournit une référence, mais le pied possède une semelle, un talon et une orientation. Un contact crédible combine hauteur, vitesse relative et phase d’appui.

Le verrouillage est appliqué seulement pendant la phase réellement plantée, avec transitions progressives pour éviter un claquement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foot_contact:
  contact_id: CONTACT-CLIP001-LEFT-01
  foot: left
  phase_start_s: pending
  phase_end_s: pending
  floor_plane: AST-MOCAP-CAL-001
  tracked_points: [heel, ball, toe]
  lock_weight_curve: pending
  max_slide_m: pending_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Phase :** le pied n’est pas verrouillé pendant le swing.

- **Géométrie :** talon, plante et pointe donnent une lecture plus précise.

- **Fondu :** le poids de correction évite une rupture brusque.

- **Mesure :** le glissement maximal sera mesuré sur le pilote réel.

## 36. Glissement des pieds

Le glissement peut venir de la source, d’une mauvaise échelle, d’un root incohérent, d’un retargeting de proportions ou d’un blend runtime. La correction doit viser la cause.

L’IK ne sert pas à cacher un clip dont le root et les contacts sont déjà contradictoires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foot_slide_diagnosis:
  inspect_order:
    - source_contact
    - source_scale_and_floor
    - root_trajectory
    - reference_pose_alignment
    - target_leg_proportions
    - retarget_result
    - runtime_blend
  ik_patch_allowed_after_source_fix: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** la chaîne localise l’étape qui introduit le défaut.

- **Source :** un glissement brut est corrigé avant retargeting.

- **Cible :** les longueurs de jambes peuvent amplifier le décalage.

- **Runtime :** le blend est examiné séparément du clip isolé.

## 37. Contacts des mains et accessoires

Une main qui saisit une radio doit conserver position, orientation et espace de référence cohérents pendant le contact. Le mouvement de l’accessoire peut être capturé, reconstruit ou animé séparément.

La relation main-accessoire est un contrat visuel ; elle ne déclenche pas directement une interaction gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hand_prop_contact:
  contact_id: CONTACT-CLIP001-RADIO-01
  hand: right
  prop_socket: SOCKET_HAND_R
  contact_space: prop_local
  phase: [approach, grasp, hold, release]
  finger_detail: authored_or_separate_capture
  gameplay_event_source: authoritative_system
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Espace :** le contact est plus stable dans le repère de l’accessoire.

- **Phases :** approche et relâchement ne sont pas verrouillés comme la tenue.

- **Doigts :** leur source est explicitée au lieu d’être supposée.

- **Gameplay :** l’animation n’accorde aucune autorité métier.

## 38. Collisions et auto-intersections

Le solveur peut placer une main dans le torse, croiser les genoux ou faire traverser un accessoire. Ces défauts sont évalués depuis plusieurs vues et pendant les transitions.

La correction respecte l’intention et les contraintes anatomiques plutôt que d’éloigner arbitrairement les membres.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
collision_review:
  pairs:
    - [hand_r, torso]
    - [knee_l, knee_r]
    - [radio, chest]
  views: [front, side, game_camera]
  severity: [minor, visible, blocking]
  correction_owner: animator
  runtime_collision_system: out_of_scope
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paires :** les zones à risque sont listées sans prétendre couvrir toute la géométrie.

- **Vues :** une intersection peut être cachée dans un angle.

- **Sévérité :** la caméra et l’usage influencent la décision.

- **Frontière :** la collision physique runtime n’est pas reconstruite depuis la mocap.

## 39. Centre de masse et équilibre

Après nettoyage, le personnage doit encore sembler soutenu par ses appuis. Un filtrage du bassin ou un retargeting de jambes peut déplacer visuellement le centre de masse.

La revue examine bassin, torse, tête, accessoires et base d’appui aux moments de contact, d’accroupissement et de redressement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
balance_review:
  moments: [walk_contact, crouch_low, radio_hold, stand_recovery]
  supports: [foot_l, foot_r]
  tracked_masses: [pelvis, chest, head, radio]
  fail_if:
    - unsupported_static_pose
    - planted_foot_compensation_visible
    - pelvis_jump_after_retarget
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Moments :** les poses fonctionnelles concentrent les risques.

- **Supports :** la base d’appui est reliée aux contacts réels.

- **Masses :** le haut du corps et l’accessoire influencent la lecture.

- **Échec :** un saut de bassin indique souvent une conversion ou une correction incohérente.

## 40. Préserver rythme et direction artistique

Nettoyer ne signifie pas normaliser. Les hésitations, accélérations et asymétries utiles peuvent porter le personnage et le contexte narratif.

La comparaison avant/après utilise les beats de l’action du chapitre 20 : anticipation, contact, tenue, relâchement et récupération.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
art_direction_review:
  source_intent: cautious_scout
  preserve:
    - deliberate_hesitation
    - asymmetric_weight_shift
    - radio_contact_hold
  remove:
    - sensor_jitter
    - accidental_floor_slide
    - calibration_jump
  beats: [anticipation, contact, hold, release, recovery]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Intention :** le brief devient un critère de nettoyage.

- **Conservation :** les asymétries motivées ne sont pas assimilées au bruit.

- **Retrait :** les anomalies techniques sont séparées des choix de performance.

- **Rythme :** les beats permettent de comparer les versions sans dépendre du nombre de clés.

## 41. Densité des clés et réduction

Une prise résolue peut contenir une clé par échantillon. La réduction vise une Action modifiable tout en respectant contacts, extrêmes, changements de direction et détails utiles.

Les tolérances sont testées par canal et par cible ; la version dense reste disponible jusqu’à l’approbation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
key_reduction:
  input: AST-MOCAP-CLIP-001-CLEAN-DENSE
  output: AST-MOCAP-CLIP-001-CLEAN-EDITABLE
  preserve: [contacts, extremes, phase_boundaries, intentional_asymmetry]
  translation_tolerance_m: pending_measurement
  rotation_tolerance_deg: pending_measurement
  compare_targets: [source_rig, short_rig, tall_rig]
  dense_backup: retained
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la version dense est identifiée comme dérivé conservé.

- **Sortie :** la version éditable reçoit un nouvel identifiant ou une version.

- **Tolérances :** les seuils sont mesurés sur les cibles réelles.

- **Comparaison :** une réduction acceptable sur un rig peut échouer sur un autre.

## 42. Mapping du squelette source vers la cible

Le mapping relie une fonction anatomique ou de profil à un os source et un os cible. Des noms identiques ne garantissent ni même hiérarchie, ni même axe, ni même rest pose.

Les os non mappés sont classés : nécessaires à la déformation, auxiliaires, accessoires, contrôleurs ou détails hors périmètre.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bone_mapping:
  profile_id: MAP-MOCAP-HUMANOID-TO-ASTERIA-V1
  source_profile: MOCAP-HUMANOID-SOURCE-V1
  target_profile: HUMANOID-ASTERIA-V1
  required:
    hips: [src:Hips, dst:DEF_pelvis]
    spine: [src:Spine, dst:DEF_spine_01]
    left_upper_leg: [src:LeftUpLeg, dst:DEF_thigh_L]
  optional:
    fingers: partial
    face: excluded
  unmapped_policy: explicit
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le mapping est versionné indépendamment des fichiers d’animation.

- **Fonction :** la clé `hips` décrit un rôle commun aux deux rigs.

- **Optionnel :** les doigts ou le visage peuvent suivre une chaîne séparée.

- **Non mappé :** chaque os absent reçoit une décision, jamais un oubli silencieux.

## 43. Schéma d’un profil de mapping

Un profil contient identité, versions de source et cible, fonctions requises, axes attendus, pose de référence et règles de translation. Il peut être validé sans charger une animation.

La validation refuse les doublons fonctionnels, références inexistantes et fonctions obligatoires absentes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
mapping_profile:
  schema_version: 1
  mapping_id: MAP-MOCAP-HUMANOID-TO-ASTERIA-V1
  source_rig_version: 1.0.0
  target_rig_version: 1.0.0
  reference_pose_pair: REFPAIR-MOCAP-ASTERIA-V1
  functions:
    hips: {source: Hips, target: DEF_pelvis, required: true}
    head: {source: Head, target: DEF_head, required: true}
  translation_policy:
    root: scaled
    other_bones: profile_defined
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** le schéma et les deux rigs peuvent évoluer séparément.

- **Paire :** les poses source et cible sont reliées par un identifiant.

- **Fonctions :** les champs `source`, `target` et `required` rendent le contrat testable.

- **Translation :** le root et les os locaux ne partagent pas nécessairement la même règle.

## 44. Hiérarchie, parents et os auxiliaires

Le retargeting dépend de la chaîne de parents. Mapper une main sans bras cohérent ou un pied sans jambe complète crée des transformations difficiles à interpréter.

Les twist bones, os de déformation supplémentaires et contrôleurs sont traités par le rig cible, pas copiés aveuglément depuis le squelette source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hierarchy_rules:
  required_chains:
    left_arm: [shoulder, upper_arm, lower_arm, hand]
    left_leg: [upper_leg, lower_leg, foot]
  source_controls_exported: false
  target_twist_distribution: target_rig_owned
  accessory_bones: mapped_by_separate_profile
  missing_parent: blocking
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chaînes :** les fonctions sont validées dans leur ordre de parenté.

- **Contrôleurs :** le squelette source de capture ne devient pas le rig de contrôle publié.

- **Twist :** la distribution appartient à la construction du rig cible.

- **Blocage :** un parent obligatoire manquant empêche une conversion fiable.

## 45. Alignement des poses de référence

La correction de pose compare l’orientation fonctionnelle des os dans une pose source et une pose cible. Une différence A-pose/T-pose peut sinon devenir une rotation permanente des épaules.

L’offset est calculé ou édité comme donnée de profil ; il n’est pas enfoui dans une première image d’animation non documentée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reference_pose_pair:
  pair_id: REFPAIR-MOCAP-ASTERIA-V1
  source_pose: A_POSE_CAPTURE_V1
  target_pose: ASTERIA_REST_A_V1
  offsets:
    left_upper_arm: pending
    right_upper_arm: pending
    left_thigh: pending
    right_thigh: pending
  validation_pose: neutral_standing
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paire :** les deux poses sont identifiées et versionnées.

- **Offsets :** les corrections locales restent inspectables.

- **Symétrie :** les côtés ne sont pas forcés identiques si le rig diffère.

- **Validation :** une pose neutre révèle les rotations permanentes indésirables.

## 46. Axes, roll et espaces de transformation

Deux os portant le même nom peuvent avoir des axes locaux différents. Le retargeting doit convertir les orientations dans un espace cohérent plutôt que copier des composantes Euler.

Le roll incorrect du rig cible remonte au chapitre 19 ; le mapping ne doit pas empiler une compensation fragile pour le masquer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transform_spaces:
  source_rotation: local_to_source_parent
  profile_function_space: canonical_humanoid
  target_rotation: local_to_target_parent
  direct_euler_component_copy: forbidden
  target_roll_fix_in_mapping: forbidden
  global_pose_debug: allowed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la rotation est interprétée avec son parent et ses axes.

- **Canonique :** un espace fonctionnel facilite la conversion entre rigs.

- **Cible :** le résultat est reconstruit dans la hiérarchie cible.

- **Diagnostic :** la pose globale aide à comparer sans devenir la solution par défaut.

## 47. Différences de proportions

Un bras plus long atteint plus loin pour la même rotation ; une jambe plus courte modifie hauteur du bassin et longueur de pas. Le retargeting doit décider ce qui préserve orientation, position, contact ou silhouette.

Il n’existe pas un facteur d’échelle unique capable de résoudre toutes les articulations et tous les contacts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
proportion_profile:
  source_height_m: measured
  target_height_m: measured
  segments:
    upper_arm_ratio: derived
    lower_arm_ratio: derived
    upper_leg_ratio: derived
    lower_leg_ratio: derived
    spine_ratio: derived
  preserve_priorities: [feet_contact, hand_radio_contact, center_of_mass, rhythm]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mesure :** les hauteurs et segments proviennent des rigs réels.

- **Ratios :** les proportions sont calculées par chaîne fonctionnelle.

- **Priorités :** les contacts et le rythme guident les compromis.

- **Limite :** la silhouette peut demander une correction artistique après conversion.

## 48. Échelle du root, bassin et translation

La translation globale peut être mise à l’échelle selon un profil, mais la hauteur du bassin dépend aussi des jambes et du sol. Appliquer le ratio de taille à toutes les translations locales produit souvent des contacts incohérents.

Le pipeline sépare déplacement horizontal, hauteur par rapport au sol et oscillation locale du bassin.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
translation_retarget:
  horizontal_root:
    scale_mode: profile_ratio_candidate
  vertical_root:
    source_floor_relative: true
    target_floor_relative: true
  pelvis_local:
    preserve_motion_character: true
    global_height_compensation: separate
  all_local_translations_scaled_uniformly: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Horizontal :** la distance peut suivre un ratio ou une vitesse cible mesurée.

- **Vertical :** le sol sert de référence commune.

- **Bassin :** l’oscillation locale n’est pas confondue avec la hauteur globale.

- **Interdit :** un facteur uniforme sur tous les os ignore les proportions de chaîne.

## 49. Portée des membres et corrections IK

Après retargeting, les pieds et mains peuvent manquer leurs cibles. Une passe IK ou une correction de contraintes peut restaurer un contact, mais elle doit préserver arcs, genoux, coudes et centre de masse.

La correction est bakée ou documentée comme couche dérivée ; elle ne modifie pas silencieusement le rig publié.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
limb_contact_correction:
  targets: [foot_l, foot_r, hand_r_radio]
  solver: qualified_target_rig_controls
  pole_direction_review: required
  stretch_policy: rig_profile_defined
  blend_in_out: required
  bake_to_action: candidate
  source_rig_unchanged: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cibles :** les contacts importants sont nommés.

- **Solveur :** les contrôles du rig cible restent propriétaires de l’IK.

- **Articulations :** la direction des genoux et coudes est revue.

- **Dérivé :** le résultat baké reçoit une version et peut être comparé.

## 50. Colonne, épaules, cou et tête

Les différences de nombre d’os de colonne exigent une distribution contrôlée. Copier toute la rotation sur un seul os concentre la courbure et modifie la silhouette.

Épaules, cou et tête sont revus ensemble afin de préserver regard, respiration et contrepoids sans créer de cassure.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
torso_distribution:
  source_spine_functions: [spine_low, spine_mid, chest]
  target_spine_functions: [spine_01, spine_02, spine_03, chest]
  distribution_weights: pending_measurement
  shoulder_compensation: reviewed
  head_orientation_priority: narrative_and_camera_dependent
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonctions :** les chaînes peuvent avoir un nombre d’os différent.

- **Distribution :** les poids sont mesurés sur les poses extrêmes.

- **Épaules :** leur compensation ne remplace pas l’alignement de référence.

- **Tête :** la priorité dépend du contexte sans appartenir encore à la mise en scène.

## 51. Mains, doigts et visage

Le corps, les doigts et le visage peuvent provenir de systèmes différents et de fréquences différentes. Les fusionner exige une synchronisation et des droits compatibles.

Le pilote traite le contact global de la main ; les doigts détaillés et la synchronisation faciale restent des lots séparés, le facial approfondi étant réservé au chapitre 27.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
detail_channels:
  body: included
  hands:
    global_hand_pose: included
    fingers: optional_separate_source
  face: excluded_from_chapter_pilot
  synchronization: required_if_combined
  rights_compatibility: required_if_combined
  missing_detail_fallback: authored_keyframes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Corps :** la chaîne principale couvre le squelette humanoïde.

- **Doigts :** un dispositif distinct produit une source distincte.

- **Visage :** le périmètre évite d’anticiper la synchronisation faciale.

- **Repli :** les keyframes du chapitre 20 complètent les canaux absents.

## 52. Rigs non humains et profils personnalisés

Un profil humanoïde ne convient pas automatiquement à un quadrupède, une créature à queue ou une morphologie à membres supplémentaires. Les fonctions, chaînes et priorités de contact doivent être redéfinies.

Réutiliser la même prise peut rester impossible si les locomotions et centres de masse ne sont pas homologues.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
custom_profile:
  profile_id: AST-CREATURE-RETARGET-V1
  topology_family: custom
  required_functions: []
  contact_sets: []
  reference_pose: pending
  locomotion_homology_review: required
  humanoid_profile_reuse: forbidden_without_evidence
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Famille :** le profil annonce qu’il ne suit pas le contrat humanoïde.

- **Fonctions :** les chaînes sont définies selon la morphologie réelle.

- **Contacts :** pattes, ailes ou queue reçoivent leurs propres critères.

- **Décision :** l’absence d’homologie peut bloquer le retargeting plutôt que forcer une conversion.

## 53. Préparer la scène Blender de retargeting

Dans Blender, ouvrir une copie de travail contenant le squelette source résolu et un lien ou une version contrôlée du rig cible. Les collections séparent source, cible, contrôles, accessoires et export.

Les transformations d’objet, unités, Action active et plage temporelle sont vérifiées avant d’ajouter contraintes ou outils de transfert.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blender_scene:
  collections:
    - MOCAP_SOURCE
    - TARGET_RIG
    - RETARGET_HELPERS
    - PROPS
    - __EXPORT
  source_armature: ARM_MOCAP_SOURCE
  target_armature: ARM_SCOUT
  active_action: AST_MOCAP_CLIP_001_CLEAN
  frame_range: selected_clip_range
  object_transforms_reviewed: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Collections :** la source et la cible peuvent être masquées ou inspectées indépendamment.

- **Armatures :** les objets reçoivent des noms stables distincts des profils.

- **Action :** la version nettoyée source est l’entrée du retargeting.

- **Export :** seuls les éléments approuvés franchissent la collection `__EXPORT`.

## 54. Contraintes, baking et Action cible

Les contraintes de copie ou le solveur de retargeting sont des mécanismes temporaires. L’Action publiée est bakée sur les os ou contrôleurs autorisés, puis les dépendances temporaires sont retirées de l’export.

Le baking échantillonne un résultat ; il ne valide ni contacts, ni courbes, ni direction artistique. Une passe de réduction et de correction suit la conversion.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
retarget_bake:
  source_action: AST_MOCAP_CLIP_001_CLEAN
  target_action: AST_MOCAP_CLIP_001_SCOUT_RT_V1
  visual_keying: true
  clear_constraints_after_bake: profile_defined
  bake_channels: [location_when_required, rotation]
  preserve_custom_properties: explicit_allowlist
  post_bake_cleanup: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** l’Action source nettoyée reste inchangée.

- **Sortie :** l’Action cible reçoit une identité et une version.

- **Canaux :** seules les propriétés utiles sont échantillonnées.

- **Après :** le résultat dense est revu avant intégration en bibliothèque.

## 55. Valider un profil de mapping avec Python

Le script suivant illustre une validation statique d’un manifeste YAML déjà chargé comme dictionnaire Python. Il vérifie les clés obligatoires, les doublons de fonctions et les os absents des catalogues fournis.

Il ne lit aucun fichier personnel et ne retargete aucune animation. Il produit une liste de diagnostics que l’appelant décide de traiter comme blocage ou avertissement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

def validate_mapping_profile(
    profile: Mapping[str, Any],
    source_bones: Sequence[str],
    target_bones: Sequence[str],
) -> list[str]:
    diagnostics: list[str] = []
    functions = profile.get("functions")
    if not isinstance(functions, Mapping):
        return ["MAPPING_FUNCTIONS_MISSING"]

    source_set = set(source_bones)
    target_set = set(target_bones)
    seen_sources: set[str] = set()
    seen_targets: set[str] = set()

    for function_name, entry in functions.items():
        if not isinstance(function_name, str) or not isinstance(entry, Mapping):
            diagnostics.append("MAPPING_ENTRY_INVALID")
            continue

        source = entry.get("source")
        target = entry.get("target")
        required = entry.get("required", False)
        if not isinstance(source, str) or not isinstance(target, str):
            diagnostics.append(f"MAPPING_NAMES_INVALID:{function_name}")
            continue

        if source not in source_set:
            diagnostics.append(f"SOURCE_BONE_UNKNOWN:{function_name}:{source}")
        if target not in target_set:
            diagnostics.append(f"TARGET_BONE_UNKNOWN:{function_name}:{target}")
        if source in seen_sources:
            diagnostics.append(f"SOURCE_BONE_REUSED:{source}")
        if target in seen_targets:
            diagnostics.append(f"TARGET_BONE_REUSED:{target}")
        if required is not True and required is not False:
            diagnostics.append(f"REQUIRED_FLAG_INVALID:{function_name}")

        seen_sources.add(source)
        seen_targets.add(target)

    return diagnostics
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signature :** `profile` est un `Mapping`, les catalogues sont des `Sequence[str]` et le retour est `list[str]`.

- **Paramètres :** `source_bones` et `target_bones` décrivent les noms réellement disponibles sur chaque rig.

- **Opérateurs :** `not in` teste l’absence, `isinstance` protège les types et `is not True/False` refuse une valeur ambiguë.

- **Retours :** un retour vide signifie seulement que ces contrôles statiques passent, jamais que le mouvement est correct.

- **Effets :** la fonction ne modifie ni le profil ni les séquences reçues ; les ensembles locaux accélèrent les recherches.

- **Limite :** axes, hiérarchie, rest pose et proportions nécessitent d’autres contrôles.

## 56. Préparer le mapping Godot avec `BoneMap`

À l’import, Godot associe le squelette à un `BoneMap` et à un `SkeletonProfile`. Le profil humanoïde fournit des fonctions communes, mais l’auto-mapping par noms doit être inspecté et corrigé.

Une correspondance absente, dupliquée ou erronée peut produire un avertissement sans empêcher l’import ; l’absence d’échec technique ne vaut donc pas acceptation artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_import_mapping:
  skeleton_node: Skeleton3D
  bone_map_resource: res://assets/characters/scout/scout_bone_map.tres
  profile: SkeletonProfileHumanoid
  auto_map:
    allowed: true
    acceptance_without_review: false
  manual_review:
    - hips_and_root
    - spine_chain
    - shoulders_and_limbs
    - hands_and_feet
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ressource :** le `BoneMap` est versionné avec l’asset ou le profil de rig.

- **Profil :** `SkeletonProfileHumanoid` fournit des fonctions humanoïdes standardisées.

- **Automatique :** les motifs de noms accélèrent la saisie sans garantir les axes.

- **Revue :** les chaînes critiques sont inspectées dans la pose de référence et en mouvement.

## 57. Options d’import et partage des animations

Les options de retargeting peuvent supprimer des pistes, conserver certaines positions ou ajuster des axes. Chaque option répond à une structure de données précise et peut dégrader un clip si elle est activée globalement.

Le projet teste une variante à la fois sur la source et les trois rigs pilotes, puis enregistre le preset retenu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
import_retarget_options:
  remove_immutable_tracks: evaluate
  unimportant_positions:
    mode: evaluate
    preserve_root_and_scale_base: required
  overwrite_axis:
    mode: evaluate_with_rest_pose_review
  fix_silhouette:
    enabled: evaluate
    filters: [feet, heels, scale_base]
  preset_id: GODOT-MOCAP-IMPORT-V1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pistes :** supprimer une piste immuable peut simplifier la bibliothèque sans changer l’intention.

- **Positions :** les translations importantes du root et de l’os d’échelle restent protégées.

- **Axes :** écraser les axes peut aider ou casser une rest pose particulière.

- **Silhouette :** les filtres évitent de corriger des zones qui doivent conserver leur orientation.

## 58. Profil personnalisé et `SkeletonProfile`

`SkeletonProfile` décrit des noms fonctionnels, parents, positions de référence et os spéciaux tels que root ou scale base. Un profil personnalisé peut représenter une famille non couverte par l’humanoïde standard.

Le profil n’invente pas les correspondances avec un rig : le `BoneMap` lie ses fonctions aux noms réels de chaque squelette.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skeleton_profile_contract:
  profile_resource: res://assets/rig_profiles/asteria_humanoid_profile.tres
  root_bone: Root
  scale_base_bone: Hips
  groups: [Body, LeftHand, RightHand]
  functions:
    - Hips
    - Spine
    - Chest
    - Head
    - LeftUpperLeg
    - RightUpperLeg
  bone_map_per_rig: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** les fonctions communes sont indépendantes des noms artistiques du rig.

- **Root :** l’os racine reçoit un rôle explicite pour les transformations globales.

- **Échelle :** l’os de base participe aux règles de retargeting de position.

- **Mapping :** chaque rig possède sa propre association au profil partagé.

## 59. `RetargetModifier3D` et frontière runtime

`RetargetModifier3D` peut adapter des poses entre squelettes pendant l’exécution. Cette voie peut être utile pour certaines architectures, mais elle ajoute un coût, une dépendance et des choix de pose globale.

Le chemin de référence du chapitre publie des clips préparés hors runtime. Le modificateur reste une variante à mesurer, pas un moyen de contourner les corrections de source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
runtime_retarget_variant:
  node: RetargetModifier3D
  source_skeleton_profile: configured
  target_skeleton_profile: configured
  use_global_pose:
    false: preserve_exact_bone_lengths
    true: adapt_different_body_shapes_with_tradeoffs
  reference_path: offline_baked_clips
  benchmark_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœud :** le modificateur dépend de profils et mappings valides.

- **Global :** la propriété change la manière dont les formes corporelles sont rapprochées.

- **Référence :** les clips bakés restent plus simples à inspecter et publier.

- **Mesure :** CPU, stabilité et qualité doivent être évalués avant adoption runtime.

## 60. Root motion, événements et contacts après retargeting

Le retargeting peut déplacer les temps de contact ou modifier la trajectoire du root. Les pistes de root motion, phases et événements sont donc revérifiées sur chaque cible.

Un événement visuel ne devient pas une autorité gameplay : le système autoritaire décide encore dégâts, consommation, interaction ou déplacement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
post_retarget_contract:
  animation_id: AST-MOCAP-CLIP-001-SCOUT-RT-V1
  root_motion_profile: RM-HUMANOID-V1
  phase_markers: [left_contact, crouch_low, radio_contact, stand_recovery]
  events:
    radio_visual_contact: candidate
  authoritative_gameplay_effects: excluded
  per_target_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Root :** distance, direction et hauteur sont contrôlées après conversion.

- **Phases :** les marqueurs suivent le mouvement résultant, pas une copie aveugle.

- **Événements :** les pistes visuelles sont filtrées et documentées.

- **Autorité :** les systèmes du Livre II restent propriétaires des mutations métier.

## 61. Intégration dans l’`AnimationLibrary` du chapitre 20

Les clips mocap rejoignent la même nomenclature, les mêmes profils de boucle et les mêmes matrices de transition que les animations keyframées. Leur origine reste visible dans le manifeste.

Un blend entre deux sources exige phases, contacts, vitesses et poses compatibles ; le graphe ne compense pas une mauvaise préparation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
library_entry:
  animation_name: loco_walk_cautious_mocap_v1
  source_kind: motion_capture
  source_clip_id: AST-MOCAP-CLIP-001
  target_rig: HUMANOID-ASTERIA-V1
  loop: false
  phase_profile: PHASE-SCOUT-RADIO-V1
  transition_matrix: res://assets/animations/scout_transitions.yaml
  provenance_manifest: res://assets/provenance/AST-MOCAP-CLIP-001.yaml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** la fonction et la variante restent lisibles dans le graphe.

- **Origine :** la mocap est une source identifiée, pas un niveau de qualité.

- **Phases :** les transitions se fondent sur des repères comparables.

- **Provenance :** le dérivé publié conserve un lien vers sa chaîne de droits et transformations.

## 62. Contrôle statique d’une bibliothèque en GDScript

Le script documentaire suivant vérifie que les animations attendues existent et que leur nom n’est pas vide. Il montre les types, paramètres et valeurs de retour sans prétendre exécuter Godot.

Les contrôles de contacts, poses et rythme exigent une scène et une lecture réelle ; ils ne peuvent pas être déduits de la seule présence d’un nom.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
extends RefCounted
class_name MocapLibraryValidator

func validate_required_animations(
    library: AnimationLibrary,
    required_names: PackedStringArray
) -> PackedStringArray:
    var diagnostics := PackedStringArray()
    if library == null:
        diagnostics.append("ANIMATION_LIBRARY_NULL")
        return diagnostics

    for animation_name: String in required_names:
        if animation_name.is_empty():
            diagnostics.append("ANIMATION_NAME_EMPTY")
            continue
        if not library.has_animation(animation_name):
            diagnostics.append("ANIMATION_MISSING:%s" % animation_name)

    return diagnostics
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `RefCounted` convient à un validateur sans présence obligatoire dans l’arbre de scène.

- **Paramètres :** `library` est une `AnimationLibrary` et `required_names` un `PackedStringArray`.

- **Opérateurs :** `== null`, `not` et `in` contrôlent respectivement l’absence, la négation et l’itération.

- **Méthodes :** `append`, `is_empty` et `has_animation` ajoutent un diagnostic ou interrogent les entrées.

- **Retour :** la fonction renvoie un `PackedStringArray`; un tableau vide ne prouve que la présence des noms demandés.

- **Effets :** la bibliothèque reçue n’est pas modifiée.

## 63. Matrice de tests multi-rigs

Chaque clip candidat est lu sur le rig source, le rig de référence, la morphologie courte et la morphologie grande. Les mêmes caméras, sol et accessoires rendent la comparaison interprétable.

Une réussite sur le rig de référence ne compense pas un défaut bloquant sur une morphologie annoncée compatible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
multi_rig_matrix:
  clip: AST-MOCAP-CLIP-001
  targets:
    source_rig: [contacts, rhythm, collisions]
    HUMANOID-ASTERIA-V1: [contacts, silhouette, root]
    HUMANOID-ASTERIA-SHORT-V1: [contacts, reach, center_of_mass]
    HUMANOID-ASTERIA-TALL-V1: [contacts, reach, center_of_mass]
  common_scene: MOCAP_RETARGET_BENCH_001
  common_cameras: [front, side, game]
  acceptance: all_required_targets
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** elle révèle les défauts introduits avant le retargeting.

- **Référence :** le rig principal vérifie la chaîne d’intégration.

- **Morphologies :** portée et équilibre sont comparés sur des proportions différentes.

- **Porte :** toutes les cibles déclarées obligatoires doivent passer.

## 64. Contrôles visuels

La revue utilise vue de face, profil, caméra de jeu et gros plans sur les contacts. Elle observe le mouvement entier, les transitions d’entrée et de sortie et les poses extrêmes.

Les captures avant/après sont nommées avec clip, cible, version, caméra et instant ou plage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
visual_review:
  views: [front, side, game_camera, contact_closeup]
  inspect:
    - silhouette
    - foot_and_hand_contacts
    - joint_direction
    - center_of_mass
    - prop_alignment
    - transition_boundaries
  capture_naming: "{clip}-{target}-{version}-{view}-{time}"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vues :** aucun angle unique ne suffit pour les contacts et collisions.

- **Séquence :** les transitions sont incluses dans la revue.

- **Noms :** les captures restent reliées à une version précise.

- **Décision :** une capture illustre un verdict humain sans remplacer la lecture animée.

## 65. Mesures quantitatives candidates

Les mesures aident à comparer deux versions : déplacement d’un pied pendant l’appui, écart main-accessoire, discontinuité de trajectoire, densité de clés et distance root.

Les seuils d’acceptation dépendent de l’échelle, de la caméra et de l’usage ; le chapitre définit les unités et laisse les valeurs en attente.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
measurement_plan:
  planted_foot_slide_m: pending_threshold
  hand_prop_error_m: pending_threshold
  root_path_discontinuity_m: pending_threshold
  joint_angle_jump_deg: pending_threshold
  keys_per_second: report_only
  clip_duration_s: measured
  target_scale_m: measured
  repeated_runs: required_when_runtime
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unités :** mètres, degrés, secondes et densité sont distingués.

- **Seuils :** aucune valeur arbitraire n’est promue en budget.

- **Contexte :** caméra, échelle et action accompagnent la mesure.

- **Répétition :** les mesures runtime futures seront répétées et archivées.

## 66. Budget, taille et performance

Le coût dépend du nombre d’os animés, de la densité de clés, de la compression, du nombre de clips chargés et d’un éventuel retargeting runtime.

La campagne future mesure taille source, GLB, ressource importée, mémoire, CPU et temps de chargement séparément.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
performance_campaign:
  variants:
    - dense_baked
    - reduced_keys
    - offline_retargeted
    - runtime_retarget_variant
  measures:
    - source_file_bytes
    - glb_bytes
    - imported_resource_bytes
    - memory_bytes
    - cpu_frame_time_ms
    - load_time_ms
  hardware: reference_machine
  results: pending_runtime
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variantes :** une seule variable principale change par comparaison.

- **Stockage :** source, échange et ressource importée sont mesurés séparément.

- **Runtime :** mémoire, CPU et chargement exigent une exécution réelle.

- **Résultat :** tous les champs restent en attente dans ce chapitre statique.

## 67. Parcours Solo

En Solo, limiter la capture à quelques actions difficiles à reproduire et fortement réutilisées. Préférer un pack légalement clair ou une session courte à une bibliothèque immense non qualifiée.

La même personne sépare les passes : droits et ingestion, sélection, nettoyage, retargeting, puis revue le lendemain ou dans une session distincte pour réduire l’aveuglement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
solo_sequence:
  scope: one_pilot_action
  source_count: minimal
  target_rigs: [reference, one_contrast_morphology]
  passes:
    - rights_and_ingestion
    - take_selection
    - cleanup
    - retarget
    - art_review
    - godot_validation
  stop_rule: acceptance_or_documented_rejection
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** une action pilote ferme la chaîne avant d’acheter ou capturer davantage.

- **Sources :** la quantité ne remplace pas la qualification.

- **Revue :** les passes séparées rendent les décisions plus lisibles.

- **Arrêt :** un rejet documenté est préférable à une correction sans fin.

## 68. Organisation Studio

En Studio, les rôles de capture, données, animation, rig, intégration et juridique possèdent des responsabilités et des approbations séparées. Une petite équipe peut cumuler des rôles sans supprimer les portes.

Le handoff contient fichiers, manifestes, versions, réserves et question précise à résoudre, plutôt qu’un dossier sans statut.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
studio_roles:
  capture_lead: acquisition_and_calibration
  data_steward: restricted_storage_and_manifests
  legal_reviewer: rights_and_consent_status
  animator: cleanup_and_art_direction
  rig_owner: mapping_and_target_compatibility
  integrator: gltf_godot_and_runtime_scene
  approvers: [legal_reviewer, animation_lead, technical_art]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capture :** le responsable garantit la qualité et les notes de session.

- **Données :** les accès et la conservation restent sous une responsabilité nommée.

- **Animation :** le mouvement publié reçoit une direction humaine.

- **Porte :** juridique, artistique et technique doivent approuver leur domaine.

## 69. Automatisation bornée

L’automatisation peut vérifier schémas, noms, os présents, empreintes, plages et rapports. Elle ne peut pas conclure seule qu’un contact est crédible, qu’un consentement couvre l’usage ou qu’une performance est artistiquement juste.

Les scripts utilisent une liste d’entrées, un workspace autorisé, des sorties de staging et des codes de retour stables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
automation_contract:
  allowed:
    - validate_manifests
    - compare_bone_catalogs
    - compute_hashes
    - generate_static_reports
    - detect_candidate_contact_drift
  forbidden_without_human_decision:
    - approve_legal_rights
    - approve_performance_quality
    - publish_animation
  output: staging_only
  exit_codes: documented
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vérification :** les contrôles automatiques portent sur des structures observables.

- **Suggestion :** un drift détecté reste un candidat à examiner.

- **Décision :** droits et qualité artistique restent humains.

- **Publication :** le script prépare un lot sans le promouvoir seul.

## 70. Livrables permanents

Le chapitre prépare les livrables du plan maître sans prétendre les matérialiser. Chaque livrable possède identité, version, source, propriétaire, statut et réserves.

Les données personnelles restent hors du dépôt public ; les manifestes publiables utilisent des références de preuve.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
deliverables:
  - sourced_session_or_clip_manifest
  - mapping_profiles
  - cleaned_source_animations
  - retargeted_target_animations
  - correction_report
  - multi_rig_test_report
  - gltf_export_preset
  - godot_animation_library
  - validation_scene
  - rights_and_provenance_status
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Session :** le manifeste remplace l’exposition des données brutes.

- **Mapping :** les profils sont réutilisables seulement pour des versions compatibles.

- **Correction :** le rapport distingue automatique et manuel.

- **Validation :** tests, bibliothèque et scène restent en réserve jusqu’à matérialisation.

## 71. Porte d’acceptation

Un clip est accepté lorsque sa provenance et ses droits sont traçables, ses contacts et son rythme sont crédibles, son mapping est validé, et le retargeting reste stable sur toutes les morphologies obligatoires.

L’échec d’une seule porte produit un statut explicite : bloqué juridiquement, à reprendre techniquement, à corriger artistiquement ou refusé pour coût excessif.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  legal:
    provenance_traceable: required
    consent_and_rights: approved
  technical:
    mapping_valid: required
    contacts_credible: required
    multi_rig_stable: required
    godot_import: required
  artistic:
    rhythm_coherent: required
    direction_approved: required
  decision: pending_materialization
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Juridique :** les droits sont une porte indépendante de la qualité technique.

- **Technique :** mapping, contacts, cibles et import sont vérifiés.

- **Artistique :** rythme et intention reçoivent une revue humaine.

- **Statut :** la décision reste en attente tant que les livrables n’existent pas.

## 72. Checklist de sortie

Avant publication, vérifier que les fichiers temporaires et données personnelles sont exclus, que le manifeste pointe vers les bonnes empreintes et que le clip importé correspond à la version approuvée.

La checklist accompagne le lot ; elle ne remplace pas les rapports détaillés ni les signatures d’approbation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
release_checklist:
  - raw_and_personal_data_excluded
  - rights_status_approved
  - source_and_target_versions_locked
  - mapping_profile_locked
  - correction_report_complete
  - multi_rig_report_complete
  - gltf_hash_recorded
  - godot_library_versioned
  - runtime_reservations_explicit
  - rollback_source_available
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exclusion :** le lot publiable ne contient pas de données restreintes.

- **Versions :** sources, cibles et mapping forment un ensemble cohérent.

- **Preuves :** rapports et empreintes relient décision et fichiers.

- **Reprise :** la source approuvée permet de reconstruire ou retirer le dérivé.

## 73. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 73.1 Accepter un clip sans droits qualifiés

**Symptôme ou risque :** le mouvement est techniquement utilisable mais aucun contrat ne couvre le retargeting ou l’usage commercial.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
clip:
  source: downloaded_pack.fbx
  licence: free
  commercial_use: assumed
  status: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le mot `free` ne décrit ni la licence, ni le titulaire, ni les droits de modification et de redistribution. Le statut approuvé fabrique une conclusion juridique sans preuve.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
clip:
  clip_id: AST-MOCAP-CLIP-001
  licence: LicenseRef-PROVIDER-CONTRACT-2026-001
  commercial_use: confirmed_by_human_review
  modification_and_retargeting: confirmed
  raw_redistribution: forbidden
  status: legally_qualified
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction référence une preuve exacte, sépare les usages et conserve la restriction de redistribution. Une personne autorisée peut relire la décision.

### 73.2 Modifier la source brute

**Symptôme ou risque :** une nouvelle méthode de nettoyage ne peut plus être comparée au signal reçu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
raw_take:
  path: raw/TAKE-004.fbx
  operation: open_and_overwrite_after_cleanup
  backup: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier brut perd son intégrité et son empreinte ne correspond plus au lot reçu. Les corrections manuelles deviennent impossibles à distinguer du signal d’origine.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
raw_take:
  path: restricted/raw/TAKE-004.fbx
  operation: immutable
working_copy:
  path: work/TAKE-004-CLEAN-v001.blend
  parent_sha256: recorded
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La source reste immuable et le dérivé nomme son parent. Une autre personne peut reproduire ou contester la passe de nettoyage.

### 73.3 Mapper uniquement par noms

**Symptôme ou risque :** le clip s’importe mais les bras ou jambes tournent dans des axes incohérents.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
mapping:
  method: same_name
  rest_pose_review: false
  hierarchy_review: false
  axis_review: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Deux os de même nom peuvent posséder des parents, axes locaux, roll et poses de référence différents. Le nom ne constitue qu’un indice.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
mapping:
  method: profile_functions
  hierarchy_review: true
  reference_pose_pair: REFPAIR-MOCAP-ASTERIA-V1
  axis_review: true
  auto_map_followed_by_manual_review: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil relie des fonctions, puis la hiérarchie, les poses et les axes sont inspectés. L’auto-mapping accélère la saisie sans devenir une approbation.

### 73.4 Confondre A-pose et rest pose

**Symptôme ou risque :** les épaules restent levées ou tournées pendant toutes les animations.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reference_pose:
  source: T_POSE
  target: A_POSE
  offset_correction: omitted
  first_frame_used_as_hidden_fix: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La différence permanente est enfouie dans l’animation et pollue chaque clip. La première image n’est pas un profil de conversion versionné.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reference_pose_pair:
  source: T_POSE_CAPTURE_V1
  target: ASTERIA_REST_A_V1
  offsets: stored_in_mapping_profile
  neutral_pose_validation: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les offsets appartiennent au mapping et sont testés sur une pose neutre. Tous les clips utilisent la même correction inspectable.

### 73.5 Lisser tous les canaux uniformément

**Symptôme ou risque :** les contacts deviennent mous et le personnage perd ses changements de rythme.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
filter:
  method: global_smoothing
  window: 20
  channels: all
  before_after_review: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une fenêtre arbitraire traite de la même manière root, pieds, mains et colonne. Elle peut décaler les contacts et supprimer des accélérations intentionnelles.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
filter:
  profile: MOCAP-CLEAN-HUMANOID-V1
  channels:
    feet: contact_preserving
    root: direction_preserving
    spine: rhythm_preserving
  parameters: pending_measurement
  before_after_review: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction distingue les fonctions, laisse les paramètres à mesurer et exige une comparaison. Le filtre devient une décision traçable plutôt qu’un bouton global.

### 73.6 Masquer le glissement avec l’IK

**Symptôme ou risque :** les pieds semblent fixés mais le bassin saute et les genoux se retournent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
foot_fix:
  source_slide_review: skipped
  root_review: skipped
  target_ik_weight: 1.0
  bake: immediate
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’IK force un résultat local sans corriger la source, l’échelle ou le root. La compensation se reporte sur les articulations et le centre de masse.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
foot_fix:
  diagnosis: [source_contact, scale, root, reference_pose, proportions]
  source_correction: completed_first
  target_ik: blended_only_during_contact
  knee_direction_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La chaîne localise d’abord la cause, puis l’IK corrige un résidu pendant la phase de contact. Les articulations et l’équilibre restent contrôlés.

### 73.7 Appliquer une échelle uniforme à toutes les translations

**Symptôme ou risque :** les mains dépassent l’accessoire et les pieds quittent le sol sur une morphologie différente.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
retarget_scale:
  ratio: target_height / source_height
  apply_to: every_bone_translation
  segment_ratios: ignored
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La taille globale ne décrit pas les proportions des bras, jambes et colonne. Le facteur unique amplifie les translations locales qui ne devraient pas toutes être mises à l’échelle.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
retarget_scale:
  root_horizontal: profile_ratio_candidate
  root_vertical: floor_relative
  pelvis_local: preserve_character
  segment_ratios: measured
  contact_corrections: per_chain
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare déplacement, sol, bassin et chaînes. Les contacts prioritaires guident les ajustements de chaque morphologie.

### 73.8 Copier doigts et visage sans source compatible

**Symptôme ou risque :** les doigts restent rigides ou les pistes faciales écrasent des contrôles incompatibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
detail_mapping:
  body: auto
  fingers: copy_all
  face: copy_all
  source_channels_verified: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les systèmes peuvent avoir des os, fréquences, noms et droits différents. Copier des pistes inexistantes ou incompatibles ne crée pas une animation valide.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
detail_mapping:
  body: mapped_and_reviewed
  fingers: optional_separate_pipeline
  face: excluded_from_chapter_pilot
  fallback: authored_keyframes
  rights_compatibility: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque famille de canaux reçoit un périmètre explicite. Les détails absents utilisent une source séparée ou des keyframes plutôt qu’une copie aveugle.

### 73.9 Traiter un avertissement d’import comme acceptable

**Symptôme ou risque :** Godot importe le fichier mais certaines fonctions du profil sont absentes ou dupliquées.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
godot_import:
  completed: true
  warnings: ignored
  bone_map_review: skipped
  status: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un import terminé signifie que le fichier a été traité, pas que le mapping et la silhouette sont corrects. Les avertissements peuvent signaler une incompatibilité fonctionnelle.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
godot_import:
  completed: true
  warnings: triaged
  bone_map_review: required
  neutral_and_motion_tests: required
  status: pending_acceptance
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les diagnostics sont classés, puis la pose neutre et le mouvement sont testés. Le statut reste en attente jusqu’à la porte artistique et technique.

### 73.10 Valider sur un seul rig

**Symptôme ou risque :** le clip paraît correct sur le personnage de référence mais glisse ou se déséquilibre sur les variantes annoncées.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
validation:
  targets: [HUMANOID-ASTERIA-V1]
  camera: presentation_front
  contacts_measured: false
  decision: universal_compatibility
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une seule morphologie et une seule caméra ne prouvent pas la compatibilité multi-rigs. La conclusion dépasse les données observées.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
validation:
  targets:
    - HUMANOID-ASTERIA-V1
    - HUMANOID-ASTERIA-SHORT-V1
    - HUMANOID-ASTERIA-TALL-V1
  cameras: [front, side, game]
  contacts_and_balance: reviewed
  decision: limited_to_tested_profiles
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La matrice couvre les morphologies promises et plusieurs vues. La décision reste limitée aux profils réellement testés.

## 74. Références techniques officielles

Les pages officielles suivantes servent de base à la qualification technique. Elles doivent être relues lors d’une mise à jour de Blender, Godot ou du format d’échange.

Les sources juridiques et contrats réels dépendent du pays, du fournisseur et du projet ; le chapitre ne remplace pas un conseil juridique.

- [Godot — Retargeting des squelettes 3D](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/retargeting_3d_skeletons.html)
- [Godot — SkeletonProfile](https://docs.godotengine.org/en/stable/classes/class_skeletonprofile.html)
- [Godot — SkeletonProfileHumanoid](https://docs.godotengine.org/en/stable/classes/class_skeletonprofilehumanoid.html)
- [Godot — RetargetModifier3D](https://docs.godotengine.org/en/stable/classes/class_retargetmodifier3d.html)
- [Blender Manual — Poser une armature](https://docs.blender.org/manual/en/latest/animation/armatures/posing/index.html)
- [Blender Manual — Contraintes d’animation](https://docs.blender.org/manual/en/latest/animation/constraints/index.html)

Ces liens couvrent import, profils, mapping, retargeting runtime, pose d’armature et pile de contraintes. Les chemins `stable` et `latest` sont revérifiés lors d’une qualification ; les contrats et consentements restent des preuves privées propres au projet.

## 75. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient une chaîne mocap non destructive, juridiquement qualifiée et limitée à des clips utiles. Le pilote officiel est `AST-MOCAP-PILOT-SCOUT-001`, avec trois cibles humanoïdes et une scène de validation commune à matérialiser.

La porte exige provenance et droits approuvés, mapping versionné, contacts crédibles, rythme cohérent, stabilité multi-rigs et import Godot vérifié. Toutes les données, mesures, animations et scènes restent en réserve tant que la campagne réelle n’est pas exécutée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_mocap_decisions:
  pilot_id: AST-MOCAP-PILOT-SCOUT-001
  session_id: AST-MOCAP-SESSION-001
  mapping_id: MAP-MOCAP-HUMANOID-TO-ASTERIA-V1
  reference_pose_pair: REFPAIR-MOCAP-ASTERIA-V1
  import_preset: GODOT-MOCAP-IMPORT-V1
  target_rigs:
    - HUMANOID-ASTERIA-V1
    - HUMANOID-ASTERIA-SHORT-V1
    - HUMANOID-ASTERIA-TALL-V1
  canonical_chain: raw_to_clean_to_retarget_to_art_directed_to_godot
  acceptance: legal_plus_artistic_plus_technical
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** pilote, session, mapping, paire de poses et preset deviennent les références permanentes.

- **Dépendances :** les rigs du chapitre 19 et la bibliothèque du chapitre 20 restent obligatoires.

- **Porte :** juridique, artistique et technique doivent réussir sans compensation mutuelle.

- **Réserves :** aucune donnée brute, animation, scène, mesure ou test runtime n’est déclaré produit.
