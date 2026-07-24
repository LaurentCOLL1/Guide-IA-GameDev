---
title: "Livre III — Chapitre 20 : Animation procédurale et animation par keyframes"
id: "DOC-L3-CH20"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre III"
chapter: 20
last-verified: "2026-07-24T11:13:52+02:00"
audit-status: "complete"
audit-date: "2026-07-24T11:13:52+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-20.md"
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

# Animation procédurale et animation par keyframes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH20`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11


## 1. Rôle du chapitre

Transformer un rig validé en bibliothèque d’animations lisible, exportable et pilotable dans Godot, sans confondre la source artistique, le graphe de lecture et l’autorité gameplay.

Le fil rouge utilise `AST-ANIM-PILOT-SCOUT-001`, dérivé du rig humanoïde du chapitre 19. Le chapitre documente les contrats et les procédures ; aucune animation Blender, bibliothèque importée ou scène Godot n’est présentée comme produite.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Rig approuvé du chapitre 19
    ↓
Convention temporelle et nomenclature
    ↓
Poses clés, timing, spacing et arcs
    ↓
Cycles, transitions et actions ponctuelles
    ↓
Nettoyage des courbes et événements
    ↓
Export glTF et bibliothèques Godot
    ↓
AnimationTree, root motion et couches
    ↓
Ajustements procéduraux bornés
    ↓
Scène de validation et porte d’acceptation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendance :** le rig et le skinning sont gelés avant la création de la bibliothèque.

- **Séparation :** les actions sources restent distinctes du graphe de lecture Godot.

- **Validation :** chaque animation possède des critères de boucle, contacts, vitesse et transitions.

- **Limite :** la capture de mouvement et son nettoyage approfondi appartiennent au chapitre 21.


## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura construire poses, cycles et transitions, nettoyer des courbes, gérer root motion et événements, puis organiser un `AnimationTree`.

Il saura également encadrer les couches additives, les masques, les blend spaces et les corrections procédurales sans masquer les défauts de la source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  authored_animation: [pose, timing, spacing, arcs, curves]
  locomotion: [idle, walk, run, starts, stops, turns]
  runtime_contracts: [root_motion, events, windows, contacts]
  godot_graph: [state_machine, blend_space, layers, one_shot]
  procedural_adjustments: [look, aim, foot_placement]
  evidence: [contact_sheet, curve_report, transition_matrix]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Auteur :** les principes d’animation sont reliés à des critères observables.

- **Runtime :** le graphe consomme des animations sans devenir leur source canonique.

- **Procédural :** les corrections locales sont bornées et désactivables.

- **Preuve :** la porte finale exige rapports, captures et mesures réelles.


## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les fichiers YAML, scripts Blender, GDScript et structures de scène sont des exemples documentaires non exécutés.

Les durées, vitesses, angles, fenêtres et seuils restent des candidats à mesurer sur le pilote réel, sa caméra et sa physique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static-review
  blender_execution: false
  actions_created: false
  curves_cleaned: false
  gltf_exported: false
  godot_imported: false
  animation_tree_executed: false
  runtime_measurements: false
  pdf_produced: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la revue vérifie la cohérence du pipeline et non le rendu final.

- **Valeurs :** aucune durée pédagogique n’est promue en budget de production.

- **Traçabilité :** les réserves distinguent procédure proposée et preuve obtenue.

- **Publication :** le PDF du Livre III reste différé à la fin du livre.


## 4. Frontières avec les chapitres voisins

Le chapitre 19 reste propriétaire du squelette, des poids, des sockets et de la rest pose. Le chapitre 21 traitera acquisition, calibration et nettoyage de mocap. Le chapitre 28 intégrera les assets dans le pipeline global.

Ici, l’IK procédurale et les ajustements de regard sont étudiés uniquement comme corrections runtime au-dessus d’animations déjà lisibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapter_19: rigging_skinning_and_rest_pose
  chapter_20: authored_and_procedural_animation
  chapter_21: motion_capture_pipeline
  chapter_22: cinematics_and_staging
  chapter_28: global_asset_integration
  book_iv: whole_game_runtime_optimization
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** le rig publié est une dépendance et non un matériau à remodeler.

- **Autorité :** le présent chapitre possède actions, courbes, événements et graphes de lecture.

- **Aval :** la mocap pourra fournir de nouvelles sources au même contrat.

- **Exclusion :** la logique de combat ou de déplacement reste autoritaire hors du graphe visuel.


## 5. Asset pilote et scénario de validation

Le pilote est un éclaireur humanoïde avec locomotion, radio tenue en main, visée, accroupissement et interaction courte avec un panneau.

Le scénario impose une boucle de déplacement, un arrêt, un demi-tour, une action ponctuelle du haut du corps et une correction de pieds sur pente.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pilot:
  asset_id: AST-ANIM-PILOT-SCOUT-001
  rig_contract: HUMANOID-ASTERIA-V1
  locomotion: [idle, walk, run, start, stop, turn_180]
  actions: [radio_use, point, interact_panel]
  additive_layers: [breathing, aim_offset]
  procedural_tests: [look_target, foot_placement]
  runtime_scene: ANIM_BENCH_SCOUT_001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Choix :** le pilote couvre locomotion, action et correction procédurale.

- **Réemploi :** le squelette du chapitre 19 reste inchangé.

- **Lisibilité :** les actions sont suffisamment distinctes pour révéler les erreurs de transition.

- **Portée :** le facial détaillé et les cinématiques longues restent hors du pilote.


## 6. Contrat de l’asset animé

Une fiche d’animation lie le rig, l’action source, sa plage temporelle, son mode de boucle, ses contacts, ses événements, son root motion et sa destination Godot.

Changer le squelette, la rest pose ou la convention de root crée une incompatibilité qui exige une nouvelle validation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_asset:
  asset_id: AST-ANIM-PILOT-SCOUT-001
  rig_version: 1.0.0
  animation_set_version: 1.0.0
  timebase_profile: ANIM-30FPS-V1
  root_motion_profile: RM-HUMANOID-V1
  event_profile: EVT-ANIM-V1
  status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la bibliothèque est versionnée indépendamment du fichier Blender.

- **Compatibilité :** le rig et la convention de root sont des dépendances explicites.

- **Événements :** les contacts et fenêtres sont documentés au lieu d’être déduits visuellement.

- **Décision :** le statut reste candidat jusqu’aux tests Blender et Godot.


## 7. Hiérarchie des sources et dérivés

Le fichier Blender et ses Actions sont les sources artistiques. Le GLB est un échange dérivé. Les `AnimationLibrary` et ressources de graphe Godot sont des dérivés d’intégration.

Une correction artistique remonte dans la source ; une configuration de transition appartient au projet Godot et ne doit pas modifier silencieusement l’Action source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
source_hierarchy:
  canonical:
    - SCOUT_ANIM_SOURCE.blend
    - actions_manifest.yaml
  exchange:
    - scout_animation_set.glb
  godot_derived:
    - scout_animation_library.tres
    - scout_animation_tree.tres
    - scout_animation_benchmark.tscn
  cache:
    - .godot/imported/**
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canonique :** les Actions et le manifeste décrivent l’intention artistique.

- **Échange :** le GLB est reproductible et ne devient pas la source.

- **Intégration :** les transitions et paramètres restent versionnés côté Godot.

- **Cache :** les imports générés ne sont jamais édités comme documents maîtres.


## 8. Base temporelle, FPS et unités

Le studio choisit une base temporelle stable pour l’auteur, tout en exprimant les contrats runtime en secondes. Un cycle n’est pas validé seulement par son nombre d’images.

Le pilote propose 30 images par seconde comme profil de travail à confirmer ; les événements exportés utilisent des temps normalisés ou des secondes selon le contrat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
timebase:
  authoring_fps: 30
  runtime_unit: seconds
  frame_zero_policy: reserved_for_reference
  inclusive_end_frame: false
  event_time_formats: [seconds, normalized_phase]
  approval: pending_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Auteur :** le FPS facilite la pose et le nettoyage dans Blender.

- **Runtime :** Godot consomme une durée et non une hypothèse sur l’écran.

- **Boucle :** la dernière pose dupliquée n’est pas exportée deux fois.

- **Réserve :** le profil est candidat tant que le projet réel ne l’a pas approuvé.


## 9. Nomenclature des Actions et bibliothèques

Les noms doivent permettre de retrouver famille, état, direction, variation et version sans dépendre d’un libellé d’interface.

Une convention stable réduit les collisions lors de l’import et rend les graphes inspectables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
action_naming:
  pattern: "{family}_{state}_{direction}_{variant}"
  examples:
    - loco_walk_forward_base
    - loco_turn_left_180
    - upper_radio_use_base
    - additive_breathing_subtle
  forbidden: [Action, NewAction, final_final]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Famille :** le préfixe regroupe locomotion, haut du corps et additif.

- **État :** le nom décrit la fonction et non une opinion artistique.

- **Variation :** une variante explicite évite les suffixes improvisés.

- **Import :** la stabilité des noms protège les références de l’`AnimationTree`.


## 10. Animation RESET et valeurs par défaut

Godot utilise une animation `RESET` pour définir les valeurs par défaut d’un objet importé. Elle doit être courte, déterministe et non jouée comme une action ordinaire.

Elle restaure la pose et les propriétés nécessaires sans encoder une transition gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reset_animation:
  name: RESET
  frames: 1
  contains:
    - skeleton_default_pose
    - exported_property_defaults
  excludes:
    - gameplay_state
    - locomotion_events
    - root_motion_delta
  playback_in_tree: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle :** `RESET` stabilise les valeurs initiales après import.

- **Contenu :** seules les propriétés exportées nécessaires sont remises à leur référence.

- **Exclusion :** aucun événement ou mouvement n’appartient à cette image.

- **Usage :** le graphe ne voyage jamais vers `RESET` comme vers un état animé.


## 11. Stratégie de keyframes

Les clés décrivent des décisions : poses extrêmes, contacts, ruptures de rythme et changements de direction. Une clé sur chaque canal à chaque image transforme l’édition en nettoyage de bruit.

Les Keying Sets limitent les propriétés enregistrées et rendent les Actions comparables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
keyframe_policy:
  keyed_channels: [location_if_required, rotation, scale_if_required]
  keying_set: KS_HUMANOID_BODY
  auto_key:
    allowed: true
    scope: active_keying_set
  key_every_frame:
    allowed_only_for: [baked_procedural_result, imported_mocap]
  cleanup_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Décision :** une clé correspond à une intention de pose ou de rythme.

- **Portée :** le Keying Set empêche l’enregistrement de propriétés accidentelles.

- **Baking :** les clés denses sont admises comme dérivé, pas comme méthode par défaut.

- **Nettoyage :** toute densité importée doit être qualifiée avant publication.


## 12. Méthode pose-à-pose

La passe commence par les poses qui racontent l’action, puis les breakdowns organisent trajectoires et changements de poids. Les in-betweens ne compensent pas une intention illisible.

Chaque pose est revue en silhouette, de face, de profil et depuis la caméra de jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pose_to_pose_pass:
  order:
    - storytelling_extremes
    - contacts
    - breakdowns
    - timing_review
    - in_betweens
    - curve_cleanup
  cameras: [front, side, game_camera]
  approval: pending_human_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Extrêmes :** les premières poses portent l’intention et le contraste.

- **Breakdowns :** elles déterminent arcs, appuis et passage du poids.

- **Caméras :** la vue de jeu peut révéler une silhouette absente en vue orthographique.

- **Décision :** la fluidité n’est évaluée qu’après la lisibilité.


## 13. Timing

Le timing mesure quand une pose ou un contact survient et combien de temps une intention reste lisible. Deux actions de même durée peuvent avoir des rythmes radicalement différents.

Les contacts de pieds, impacts et changements de direction servent de repères stables pour comparer les versions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
timing_sheet:
  action: upper_radio_use_base
  beats:
    - {label: anticipation, frame: candidate}
    - {label: hand_contact, frame: candidate}
    - {label: communication_hold, frame: candidate}
    - {label: release, frame: candidate}
  measured_in: [frames, seconds]
  approved: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repères :** les beats décrivent les moments fonctionnels de l’action.

- **Comparaison :** images et secondes permettent de relire l’auteur et le runtime.

- **Réserve :** les numéros restent candidats avant création de l’Action.

- **Fonction :** le contact peut alimenter un événement sans décider du gameplay.


## 14. Spacing

Le spacing décrit la distance parcourue entre deux échantillons temporels. Il produit accélération, décélération, impact ou flottement même lorsque les clés principales restent identiques.

La revue utilise trajectoires et courbes plutôt qu’une densité uniforme de clés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
spacing_review:
  tracked_points: [root, chest, hand_r, foot_l, foot_r]
  questions:
    - acceleration_readable
    - deceleration_readable
    - contact_has_weight
    - no_unwanted_plateau
  tools: [motion_paths, graph_editor, viewport_playback]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Points :** quelques repères corporels rendent le déplacement mesurable.

- **Accélération :** l’écart entre échantillons doit soutenir l’intention.

- **Contact :** un pied posé ne glisse pas pendant sa phase d’appui.

- **Outils :** courbes et trajectoires complètent la perception visuelle.


## 15. Arcs et trajectoires

Les membres, la tête et le centre de masse décrivent généralement des trajectoires continues. Une cassure non motivée révèle souvent une interpolation, un espace ou un changement de parent incorrect.

Les Motion Paths servent de diagnostic, mais la caméra finale reste l’arbitre artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
arc_review:
  controls: [CTRL_root, CTRL_chest, CTRL_hand_R, CTRL_foot_L]
  motion_path_range: action_range
  inspect:
    - cusps
    - sudden_direction_changes
    - uneven_spacing
    - parent_space_discontinuity
  camera_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Trajectoire :** les chemins rendent visibles les ruptures difficiles à percevoir image par image.

- **Espace :** un changement d’espace peut créer un saut malgré des clés plausibles.

- **Rythme :** la répartition des points montre accélérations et pauses.

- **Limite :** une courbe parfaite ne garantit pas une silhouette convaincante.


## 16. Silhouette, ligne d’action et lecture

La silhouette doit communiquer l’état avant les détails secondaires. Les bras, accessoires et vêtements ne doivent pas fusionner avec le torse aux moments clés.

La ligne d’action organise l’énergie générale sans imposer une pose anatomiquement extrême.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
silhouette_check:
  key_poses: [start, anticipation, contact, extreme, recovery]
  backgrounds: [light, dark, neutral]
  inspect:
    - limb_separation
    - prop_readability
    - center_of_mass
    - action_line
  game_camera_priority: high
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contraste :** plusieurs fonds révèlent les fusions de contour.

- **Moments :** les poses clés reçoivent la revue la plus exigeante.

- **Accessoire :** la radio doit rester identifiable sans casser l’anatomie.

- **Priorité :** la caméra de jeu prime sur une vue de présentation avantageuse.


## 17. Poids, équilibre et centre de masse

Le personnage doit sembler soutenu par ses appuis. Une translation décorative du bassin ne remplace pas le transfert réel du centre de masse.

La grille examine appuis, bassin, cage thoracique et contrepoids des bras ou accessoires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
balance_review:
  supports: [foot_l, foot_r, hand_contact_optional]
  tracked_masses: [pelvis, chest, head, radio]
  states: [idle, walk_contact, run_contact, crouch, turn]
  failure_if:
    - center_of_mass_outside_support_without_momentum
    - planted_foot_slides
    - torso_counterweight_missing
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Appui :** la relation entre masse et support produit la crédibilité.

- **Mouvement :** une sortie temporaire de la base d’appui exige une dynamique lisible.

- **Accessoire :** la masse de la radio influence bras et torse.

- **Échec :** le glissement d’un appui annule immédiatement la sensation de poids.


## 18. Chevauchement et follow-through

Les parties secondaires ne démarrent ni ne s’arrêtent toutes ensemble. Veste, sacoche et antenne suivent le mouvement avec retard, mais restent sous contrôle et sans simulation cachée.

Le pilote sépare les clés artistiques des simulations éventuellement bakées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
overlap_layers:
  authored:
    - chest_follow
    - head_settle
  secondary:
    - pouch_swing
    - radio_antenna
  simulation:
    allowed: false
    future_bake_requires: provenance_and_cleanup
  review: no_uniform_stop
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Décalage :** les parties secondaires prolongent l’action principale.

- **Contrôle :** les amplitudes restent liées à la fonction et au matériau.

- **Source :** une simulation future serait un dérivé identifié.

- **Risque :** un arrêt simultané de tous les contrôleurs produit une rigidité mécanique.


## 19. Holds et moving holds

Une pose tenue ne signifie pas immobilité numérique. Une respiration, un ajustement de regard ou une variation de tension peut préserver la vie sans brouiller l’intention.

Le moving hold reste plus faible que le changement principal et ne doit pas créer de glissement de contact.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
moving_hold:
  base_pose: radio_listen
  allowed_motion:
    - breathing_low_amplitude
    - eye_or_head_micro_adjustment
    - weight_settle
  locked_contacts: [hand_radio, planted_feet]
  forbidden: [root_drift, prop_slide]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** la pose principale reste reconnaissable pendant toute la tenue.

- **Variation :** les micro-mouvements évitent la rigidité sans devenir une nouvelle action.

- **Contacts :** main et pieds restent cohérents.

- **Interdit :** la dérive du root ne doit pas être confondue avec une respiration.


## 20. Anticipation et récupération

L’anticipation prépare une action importante ; la récupération montre son coût et son retour vers un état stable. Elles doivent rester proportionnelles au gameplay et à la caméra.

Une interaction courte n’a pas besoin d’une préparation théâtrale si elle retarde la réponse du joueur.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
action_phases:
  action: interact_panel
  phases:
    - anticipation
    - approach
    - contact
    - functional_hold
    - release
    - recovery
  responsiveness_budget: measured_in_game
  exaggeration: camera_and_style_dependent
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Phases :** la décomposition rend les décisions de rythme explicites.

- **Réponse :** le budget gameplay limite la longueur de l’anticipation.

- **Contact :** la phase fonctionnelle aligne main, cible et événement.

- **Style :** l’exagération dépend de la bible visuelle et de la caméra.


## 21. Extrêmes, breakdowns et in-betweens

Les types de clés servent de repères de production : extrême, breakdown, moving hold, jitter ou clé générée. Ils n’ont pas d’autorité runtime mais améliorent la lecture de l’Action.

Les clés générées doivent rester identifiables afin de pouvoir être recalculées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
keyframe_types:
  extreme: storytelling_or_motion_limit
  breakdown: path_and_weight_decision
  moving_hold: controlled_living_hold
  jitter: dense_reference_or_bake
  generated: replaceable_tool_output
  runtime_semantics: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repère :** la couleur ou la forme aide l’équipe à comprendre l’intention.

- **Breakdown :** ce type ne signifie pas une clé moins importante.

- **Généré :** un outil peut supprimer et reconstruire ces clés.

- **Limite :** Godot ne doit pas interpréter ces catégories comme des états gameplay.


## 22. Dope Sheet et Action Editor

Le Dope Sheet donne une vue d’ensemble des canaux et des clés ; l’Action Editor gère les Actions actives. Ils servent à déplacer le rythme, vérifier les plages et repérer les clés orphelines.

La revue commence par les groupes fonctionnels avant d’entrer dans chaque F-Curve.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
dope_sheet_review:
  modes: [Action_Editor, Dope_Sheet]
  groups: [root, torso, arms, legs, props]
  inspect:
    - action_range
    - keys_outside_range
    - phase_alignment
    - duplicated_end_pose
    - unexpected_channels
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vue globale :** les groupes réduisent la charge visuelle.

- **Plage :** aucune clé utile ne reste hors de l’Action exportée.

- **Boucle :** la pose de fin dupliquée est traitée selon la convention.

- **Canaux :** les propriétés accidentelles sont supprimées avant export.


## 23. Graph Editor et F-Curves

Le Graph Editor révèle accélérations, plateaux, oscillations et dépassements invisibles dans la seule timeline. Chaque courbe est lue avec son rôle, son unité et son espace.

Le nettoyage n’aplatit pas toutes les courbes : il supprime le bruit qui ne sert ni la pose ni le rythme.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
curve_review:
  channels:
    root_translation: meters
    bone_rotation: radians_or_degrees_in_ui
    property_track: typed_value
  inspect:
    - overshoot
    - plateau
    - tangent_discontinuity
    - unnecessary_keys
    - cyclic_boundary
  preserve_intent: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** une translation et une rotation ne partagent pas les mêmes seuils.

- **Rôle :** une courbe de contact ne se nettoie pas comme une respiration.

- **Bruit :** les clés sans intention compliquent les révisions.

- **Intention :** la réduction n’est acceptée qu’après comparaison visuelle.


## 24. Interpolation des segments

Constant, Linear et Bézier répondent à des besoins différents. Le choix se fait par segment et non par préférence globale.

Les contacts mécaniques ou changements discrets peuvent exiger une interpolation constante ; un déplacement régulier peut utiliser Linear ; les mouvements organiques utilisent souvent Bézier contrôlé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
interpolation_policy:
  constant:
    use_for: [discrete_switch, held_property]
  linear:
    use_for: [constant_speed_segment, normalized_driver]
  bezier:
    use_for: [organic_motion, acceleration_profile]
  default_without_review: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Constant :** la valeur change sans état intermédiaire.

- **Linéaire :** la vitesse reste constante entre deux clés.

- **Bézier :** les tangentes définissent accélération et décélération.

- **Revue :** un mode par défaut ne remplace pas l’analyse du mouvement.


## 25. Poignées et Auto Clamped

Les poignées automatiques accélèrent le blocage, mais peuvent produire des dépassements. `Auto Clamped` réduit certains overshoots sans garantir une courbe correcte.

Les poignées alignées ou libres sont réservées aux endroits où l’intention exige un contrôle précis.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
handle_policy:
  blocking: AUTO_CLAMPED
  polish:
    - ALIGNED_when_continuity_required
    - VECTOR_for_sharp_change
    - FREE_for_specific_asymmetry
  overshoot_scan: mandatory
  global_handle_conversion: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Blocage :** les poignées automatiques permettent une première lecture rapide.

- **Dépassement :** une limite articulaire ou un contact peut être franchi entre deux clés.

- **Précision :** le type manuel répond à un besoin local.

- **Interdit :** convertir toutes les courbes uniformément détruit des intentions différentes.


## 26. Overshoot, oscillations et dérive

Un overshoot peut donner de l’énergie ou provoquer une pénétration. Une oscillation peut exprimer une matière secondaire ou signaler des clés incohérentes.

La revue classe chaque dépassement comme intentionnel, toléré ou bloquant.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
curve_anomaly:
  categories: [intentional, tolerated, blocking]
  scan_channels: [feet, hands, root, pelvis, props]
  blocking_examples:
    - planted_foot_crosses_floor
    - hand_leaves_contact
    - root_reverses_unintentionally
  decision_owner: animator_and_integrator
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classification :** toute anomalie n’est pas automatiquement une erreur.

- **Contacts :** les canaux liés à un appui ont une tolérance plus faible.

- **Root :** une inversion de direction peut casser la physique.

- **Décision :** l’animateur et l’intégrateur examinent ensemble les cas ambigus.


## 27. Rotations Euler, quaternions et ordre

Les contrôleurs Blender peuvent employer Euler ou quaternion selon le besoin. Changer de mode au milieu d’une Action sans plan peut créer des sauts ou des courbes impossibles à relire.

L’ordre Euler est documenté par famille de contrôleurs ; les rotations continues sont testées dans Godot après export.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rotation_contract:
  control_defaults:
    limbs: XYZ_euler_candidate
    root: quaternion_or_euler_by_profile
  mode_change_inside_action: forbidden_without_bake
  euler_filter_review: required_when_needed
  export_rotation_test: mandatory
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lisibilité :** Euler offre des courbes séparées mais dépend de l’ordre.

- **Robustesse :** le quaternion évite certaines singularités mais se lit moins directement.

- **Conversion :** un changement de représentation exige comparaison et parfois baking.

- **Export :** le résultat Godot doit être inspecté, pas seulement la vue Blender.


## 28. Nettoyage et réduction de clés

La réduction vise une Action modifiable, pas le plus petit nombre de clés possible. Elle respecte contacts, extrêmes, ruptures de rythme et tolérances par canal.

Une version avant/après est conservée pour comparer mouvement, erreurs et taille.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
key_reduction:
  preserve:
    - contacts
    - extremes
    - event_boundaries
    - intentional_overshoot
  tolerances:
    translation: measured_per_profile
    rotation: measured_per_profile
  compare: [viewport, curves, exported_runtime]
  destructive_without_backup: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Objectif :** la maintenabilité compte autant que la densité.

- **Tolérance :** les unités et fonctions imposent des seuils distincts.

- **Comparaison :** la réduction est examinée dans Blender et après export.

- **Sécurité :** la source dense reste disponible jusqu’à approbation.


## 29. Planification d’un cycle

Un cycle possède une phase, des contacts, un déplacement éventuel et une règle de raccord. La pose de début et de fin ne suffit pas si les vitesses ou tangentes divergent.

Le manifeste décrit la durée logique et les phases plutôt qu’un simple intervalle d’images.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
cycle_contract:
  action: loco_walk_forward_base
  loop: true
  phases: [left_contact, passing, right_contact, passing]
  root_motion: profile_defined
  first_last_pose_duplicate: false
  tangent_continuity: required
  phase_markers: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Phase :** les contacts structurent la boucle.

- **Raccord :** position, vitesse et tangentes sont examinées.

- **Root :** le déplacement suit un profil distinct de la pose.

- **Marqueurs :** les phases facilitent synchronisation et blend spaces.


## 30. Cycle de marche

La marche alterne appuis simples et doubles, passage du bassin et balancement opposé des bras. Le pilote privilégie la stabilité des pieds et la lisibilité à la caméra de jeu.

La cadence, la longueur de pas et le déplacement root sont mesurés ensemble.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
walk_cycle_review:
  contacts: [left, right]
  inspect:
    - foot_lock
    - pelvis_transfer
    - knee_direction
    - arm_counter_swing
    - head_stability
  metrics:
    - cycle_duration
    - stride_length
    - root_distance
    - average_speed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Appuis :** les phases de contact définissent la crédibilité.

- **Bassin :** le transfert de masse évite une glissade mécanique.

- **Métriques :** durée, distance et vitesse doivent être cohérentes.

- **Caméra :** les petits défauts latéraux peuvent devenir visibles en vue de jeu.


## 31. Cycle de course

La course ajoute phases de vol, impacts plus marqués et inclinaison adaptée à la vitesse. Elle n’est pas obtenue par simple accélération temporelle de la marche.

Le root, le torse et les pieds sont comparés aux vitesses gameplay prévues.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
run_cycle_review:
  required_phases: [contact, compression, passing, flight]
  reject_if:
    - walk_time_scaled_only
    - no_flight_phase
    - foot_speed_mismatch
    - torso_energy_missing
  metrics: [cycle_duration, stride_length, root_speed]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** la phase de vol distingue fonctionnellement la course.

- **Impact :** compression et récupération portent le poids.

- **Vitesse :** le déplacement visuel doit correspondre au gameplay.

- **Rejet :** une marche accélérée conserve souvent des appuis et amplitudes incorrects.


## 32. Idle et respiration

L’idle maintient silhouette, disponibilité et personnalité sans attirer constamment l’attention. La respiration est une couche candidate, pas une translation globale du personnage.

Plusieurs durées et variations peuvent réduire la répétition, mais chaque variante conserve les mêmes contrats d’entrée et de sortie.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
idle_set:
  base: loco_idle_base
  variants: [idle_shift_weight, idle_scan_area]
  additive: additive_breathing_subtle
  root_drift: forbidden
  entry_exit_pose_family: neutral_ready
  repetition_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** l’idle principal reste compatible avec toutes les transitions courantes.

- **Variation :** les variantes changent le détail sans casser la disponibilité.

- **Additif :** la respiration peut être filtrée sur le haut du corps.

- **Root :** aucune dérive cumulative ne doit déplacer le personnage.


## 33. Démarrages, arrêts et demi-tours

Les transitions locomotrices absorbent le changement de vitesse ou de direction. Un cross-fade entre deux boucles ne remplace pas toujours un démarrage ou un arrêt dédié.

Le demi-tour distingue rotation visuelle, trajectoire root et orientation gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
locomotion_transitions:
  clips: [start_forward, stop_forward, turn_left_180, turn_right_180]
  entry_contract:
    - speed_range
    - facing_range
    - phase_optional
  exit_contract:
    - target_state
    - root_orientation
    - planted_foot
  fallback_crossfade: documented
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** vitesse et orientation déterminent si la transition convient.

- **Sortie :** la pose finale doit rejoindre une famille stable.

- **Pied :** le choix d’appui influence le sens et la lisibilité.

- **Repli :** un cross-fade existe mais reste identifié comme compromis.


## 34. Contacts et verrouillage des pieds

Un pied en contact doit rester stable relativement au sol pendant la phase prévue. Le verrouillage est d’abord corrigé dans l’Action source avant d’ajouter une IK runtime.

Les contacts sont marqués et comparés au déplacement root.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foot_contact_contract:
  markers: [foot_l_down, foot_l_up, foot_r_down, foot_r_up]
  source_review:
    - local_foot_velocity
    - root_relative_motion
    - floor_penetration
  runtime_ik:
    purpose: terrain_adaptation_only
  source_slide_tolerance: measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Marqueurs :** les phases de contact deviennent vérifiables.

- **Source :** la vitesse locale du pied révèle le glissement.

- **Root :** le déplacement global doit correspondre à la longueur de pas.

- **IK :** la correction terrain ne cache pas un cycle mal construit.


## 35. Contrat de root motion

Le root motion extrait le déplacement animé pour que le personnage visuel reste centré tandis que le gameplay décide comment appliquer le delta. Le graphe ne devient pas propriétaire de la collision.

Le profil précise os source, axes, translation, rotation et traitement des échelles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
root_motion_profile:
  id: RM-HUMANOID-V1
  source_bone: DEF_root
  translation_axes: [x, z]
  vertical_translation: authored_by_exception
  rotation_axis: y
  scale_motion: forbidden
  application_owner: character_movement_system
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** un os unique fournit le delta extrait.

- **Axes :** les composantes autorisées sont explicites.

- **Autorité :** le système de déplacement accepte, adapte ou rejette le delta.

- **Échelle :** la mise à l’échelle animée n’est pas un mouvement de personnage.


## 36. Animation in-place et animation déplacée

Une bibliothèque peut contenir des variantes in-place et root motion, mais leurs usages et noms sont distincts. Supprimer le déplacement à l’import sans manifeste crée une divergence difficile à diagnostiquer.

Le pilote documente la source et le dérivé éventuel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
locomotion_variants:
  root_motion:
    action: loco_walk_forward_rm
    source: authored
  in_place:
    action: loco_walk_forward_ip
    derivation: root_removed_by_verified_process
  phase_equivalence: required
  silent_conversion: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variants :** les deux représentations sont identifiables.

- **Dérivation :** l’in-place peut être produit par une opération reproductible.

- **Phase :** contacts et durée restent alignés pour le blending.

- **Interdit :** une case d’import ne modifie pas silencieusement le contrat.


## 37. Synchronisation avec la vitesse gameplay

La vitesse visuelle doit rester cohérente avec la distance réellement parcourue. Un `TimeScale` peut corriger une plage limitée, mais ne compense pas une longueur de pas incompatible.

Le benchmark compare vitesse cible, vitesse root, facteur temporel et glissement de pied.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
locomotion_speed_match:
  target_speed_mps: measured
  authored_root_speed_mps: measured
  allowed_time_scale_range: profile_defined
  foot_slide_metric: measured
  decision:
    within_range: scale_time
    outside_range: author_new_variant
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mesure :** les vitesses proviennent du projet et de l’Action réelle.

- **Plage :** un facteur extrême déforme rythme et inertie.

- **Glissement :** la cohérence des pieds reste un critère séparé.

- **Décision :** une nouvelle variante peut être préférable à une accélération excessive.


## 38. Événements, contacts et fenêtres d’action

Les animations publient des repères visuels : contact, sortie, sommet ou fenêtre. Le système gameplay décide si une action réussit et ne délègue pas son autorité à une piste d’animation.

Les événements sont stables, nommés et idempotents lorsque nécessaire.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_events:
  profile: EVT-ANIM-V1
  events:
    - {id: foot_l_contact, kind: visual_contact}
    - {id: radio_hand_contact, kind: prop_sync}
    - {id: interact_reach_peak, kind: timing_marker}
  forbidden_authority:
    - apply_damage
    - consume_inventory
    - complete_quest
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repère :** l’événement indique un moment d’animation.

- **Intégration :** le gameplay peut l’utiliser comme signal ou vérification.

- **Idempotence :** un replay ou blend ne doit pas appliquer deux fois une conséquence.

- **Interdit :** les mutations métier restent hors des pistes importées.


## 39. Pistes de méthode et sécurité

Godot peut appeler des méthodes depuis une animation, mais cette capacité exige une surface fermée. Une piste importée ne doit pas exécuter un nom arbitraire ou une mutation autoritaire.

Le pilote privilégie des adaptateurs visuels ou des signaux typés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
const ALLOWED_ANIMATION_EVENTS := {
    &"foot_l_contact": true,
    &"foot_r_contact": true,
    &"radio_hand_contact": true,
}

func relay_animation_event(event_id: StringName) -> void:
    if not ALLOWED_ANIMATION_EVENTS.has(event_id):
        push_warning("Animation event rejected: %s" % event_id)
        return
    animation_event_emitted.emit(event_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liste fermée :** seuls les identifiants publiés traversent l’adaptateur.

- **Signal :** l’animation annonce un repère sans muter directement le métier.

- **Diagnostic :** un identifiant inconnu est refusé et journalisé.

- **Limite :** le chapitre ne définit pas les conséquences gameplay du signal.


## 40. Couches additives

Une couche additive applique une différence par rapport à une pose de référence. Elle convient à respiration, recul léger ou visée, à condition que référence, masque et amplitude soient explicites.

Un clip absolu mal étiqueté comme additif produit des doubles transformations.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
additive_layer:
  action: additive_breathing_subtle
  reference_pose: neutral_ready
  tracks: [spine, chest, shoulders]
  weight_range: [0.0, 1.0]
  excluded: [root, feet, prop_contact_hand]
  validation: zero_weight_and_full_weight
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** l’additif exprime un delta depuis une pose connue.

- **Masque :** les pieds et le root restent protégés.

- **Amplitude :** la plage de poids est testée aux extrêmes.

- **Validation :** zéro doit restituer la base et un doit rester anatomiquement acceptable.


## 41. Masques et filtres de blending

Les filtres déterminent quels os ou pistes participent à une couche. Ils sont versionnés avec le squelette et testés après tout renommage.

Un masque de haut du corps doit protéger bassin, root et contacts des jambes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blend_mask:
  id: MASK-UPPER-BODY-V1
  include: [spine_01, spine_02, chest, neck, head, arms]
  exclude: [root, pelvis_translation, legs, feet]
  inheritance: explicit
  skeleton_contract: HUMANOID-ASTERIA-V1
  orphan_track_scan: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** le masque dépend des noms et de la hiérarchie publiés.

- **Inclusion :** les chaînes utiles sont listées explicitement.

- **Protection :** locomotion et root ne reçoivent pas l’action du haut du corps.

- **Scan :** un os renommé ne doit pas rendre le filtre silencieusement incomplet.


## 42. BlendSpace1D et BlendSpace2D

Un blend space associe des animations à une ou deux dimensions continues, par exemple vitesse et direction. Les points représentent des sources compatibles en phase et en intention.

Ajouter de nombreux points ne corrige pas des cycles incompatibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
locomotion_blend_space:
  dimensions:
    x: lateral_velocity
    y: forward_velocity
  points:
    idle: [0.0, 0.0]
    walk_forward: [0.0, candidate]
    run_forward: [0.0, candidate]
    strafe_left: [candidate, 0.0]
    strafe_right: [candidate, 0.0]
  phase_compatibility: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dimensions :** les paramètres correspondent à des variables mesurables.

- **Points :** les positions restent candidates avant benchmark.

- **Phase :** les cycles doivent partager contacts et durée logique compatibles.

- **Limite :** la densité du graphe ne remplace pas la qualité des sources.


## 43. Modes de synchronisation des blend spaces

Les modes de synchronisation déterminent si les animations inactives avancent et comment les cycles restent en phase. Leur choix dépend du type de contenu.

Les modes cycliques exigent des animations finies et compatibles ; un `TimeSeek` placé au mauvais endroit peut casser la synchronisation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blend_sync_policy:
  locomotion_cycles:
    preferred: CYCLIC_MUTABLE
    requires:
      - finite_animation_nodes
      - immutable_lengths
      - shared_logical_cycle
  one_shots:
    preferred: NONE
  time_seek_after_cyclic_sync: forbidden_without_test
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cycle :** le mode mutable aligne la phase tout en respectant la durée active.

- **Préconditions :** les sources doivent être des animations finies compatibles.

- **One-shot :** une action ponctuelle n’a pas à avancer lorsqu’elle est inactive.

- **Risque :** un repositionnement temporel peut rompre l’alignement attendu.


## 44. Machine à états d’animation

La machine à états organise des familles discrètes : locomotion, saut, interaction ou incapacité. Elle ne remplace pas la machine gameplay ; elle traduit un état autoritaire en lecture visuelle.

Les transitions possèdent conditions, priorité, temps de fondu et politique d’interruption.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_state_machine:
  states: [Locomotion, Crouch, Interact, Disabled]
  transitions:
    - {from: Locomotion, to: Crouch, condition: visual_crouch_requested}
    - {from: Locomotion, to: Interact, condition: visual_interact_requested}
  gameplay_authority: external
  direct_business_state_reads: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Familles :** chaque état peut contenir un blend tree ou un blend space.

- **Adaptation :** des paramètres visuels sont dérivés de l’état autoritaire.

- **Transition :** le graphe décrit la continuité de pose.

- **Interdit :** le graphe ne décide ni compétence, ni inventaire, ni résultat d’action.


## 45. Contrat des transitions

Une transition spécifie l’état source, la destination, la durée, la courbe, l’interruption et les préconditions de pose. Un fondu fixe utilisé partout crée pieds fantômes et contacts incohérents.

La matrice de transitions est testée dans les deux directions lorsque cela a du sens.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transition_contract:
  from: Locomotion
  to: Interact
  blend_seconds: candidate
  switch_mode: at_end_or_immediate_by_action
  interruption: profile_defined
  entry_pose_family: neutral_ready
  contact_requirements: [feet_stable]
  reverse_test: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durée :** le fondu dépend de l’action et de la réponse attendue.

- **Entrée :** une famille de pose réduit les écarts au raccord.

- **Interruption :** les actions non interruptibles doivent être rares et justifiées.

- **Test :** le retour vers locomotion mérite sa propre revue.


## 46. OneShot et actions ponctuelles

`AnimationNodeOneShot` convient à une action temporaire superposée ou intégrée au graphe. La requête de lecture et l’état actif sont distincts de la réussite gameplay.

Filtres, fondus d’entrée et de sortie sont documentés par action.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
func request_radio_visual() -> void:
    animation_tree.set(
        "parameters/RadioOneShot/request",
        AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE
    )

func abort_radio_visual() -> void:
    animation_tree.set(
        "parameters/RadioOneShot/request",
        AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Requête :** le contrôleur demande une lecture visuelle explicite.

- **Filtre :** le nœud peut cibler uniquement le haut du corps.

- **Abort :** une interruption possède une commande dédiée.

- **Autorité :** l’état actif du nœud ne prouve pas que l’action gameplay a réussi.


## 47. Bibliothèques d’animations et import

Les animations importées résident dans un `AnimationPlayer` ou une bibliothèque associée ; `AnimationTree` les référence et contrôle leur lecture. Les scènes importées ne sont pas éditées directement.

Le projet instancie la scène dérivée, ajoute son graphe et conserve les noms stables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_animation_layout:
  imported_scene: res://assets/characters/scout/scout_anim.glb
  derived_scene: res://characters/scout/scout_animated.tscn
  animation_player: Imported/AnimationPlayer
  animation_tree: AnimationTree
  libraries:
    - locomotion
    - upper_body
    - additive
  imported_scene_direct_edit: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** les Actions deviennent des animations accessibles à l’`AnimationPlayer`.

- **Graphe :** l’`AnimationTree` ne contient pas lui-même les animations.

- **Dérivé :** la scène d’intégration référence l’import sans l’écraser.

- **Bibliothèques :** les familles réduisent les collisions et facilitent les revues.


## 48. Root motion dans AnimationTree

Godot peut extraire position, rotation et échelle root motion depuis le résultat mélangé. Le système de déplacement consomme ces deltas pendant la boucle physique et conserve collision et autorité.

L’échelle est rejetée par le profil du pilote.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
func consume_root_motion(delta: float) -> void:
    var local_delta := animation_tree.get_root_motion_position()
    var rotation_delta := animation_tree.get_root_motion_rotation()

    movement_adapter.offer_visual_root_motion(
        local_delta,
        rotation_delta,
        delta
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Extraction :** le delta provient du résultat réellement mélangé.

- **Boucle :** l’adaptateur est appelé dans le contexte temporel du mouvement.

- **Offre :** le système autoritaire peut borner ou rejeter le delta.

- **Échelle :** aucune variation de taille ne pilote la collision.


## 49. Ajustements procéduraux : règle générale

Une correction procédurale résout un écart local et mesuré : pente, cible de regard ou orientation d’arme. Elle doit être désactivable afin de comparer la source seule.

Elle ne sert pas à réparer des arcs, contacts ou poses défectueux dans l’Action.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
procedural_adjustment:
  source_animation_required: readable_without_adjustment
  inputs: validated_runtime_data
  max_correction: profile_defined
  fade_in_out: required
  disable_for_ab_test: true
  bake_back_to_source: separate_process
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** l’animation source reste convaincante sur terrain neutre.

- **Entrées :** la correction consomme des données bornées et vérifiées.

- **Amplitude :** une limite empêche une pose anatomiquement impossible.

- **Comparaison :** le mode désactivé révèle les défauts masqués.


## 50. Regard et visée

Le regard peut combiner animation de base, orientation du torse, tête et yeux. La visée ajoute des limites plus strictes pour l’arme et les mains.

Les cibles passent par un adaptateur visuel et les rotations sont réparties par chaîne.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
look_aim_profile:
  chains:
    torso: {weight: candidate, limit_deg: candidate}
    head: {weight: candidate, limit_deg: candidate}
    eyes: {weight: candidate, limit_deg: candidate}
  target_space: global_validated
  behind_target_policy: fade_or_turn
  weapon_alignment_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Répartition :** plusieurs chaînes évitent une torsion concentrée.

- **Limites :** les angles restent candidats avant test anatomique.

- **Arrière :** une cible derrière le personnage ne doit pas retourner la tête.

- **Arme :** la visée doit préserver mains, socket et silhouette.


## 51. Placement procédural des pieds

Le placement des pieds adapte les contacts à une pente ou une marche. Les raycasts fournissent des cibles ; la correction conserve longueur des jambes, orientation du bassin et limites articulaires.

Le système se désactive lorsque le personnage est en phase de vol ou lorsqu’aucun sol valide n’est trouvé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foot_placement:
  source_contacts: required
  probes: [foot_l, foot_r]
  valid_surface_filter: movement_system_contract
  pelvis_compensation: bounded
  disable_when: [airborne, ragdoll, invalid_surface]
  source_slide_fix: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contacts :** les marqueurs déterminent quand un pied peut être verrouillé.

- **Surface :** le même contrat de sol que le déplacement est utilisé.

- **Bassin :** la compensation évite l’allongement artificiel des jambes.

- **Limite :** l’IK ne corrige pas le glissement intrinsèque du cycle.


## 52. Ajustement de portée et interaction

Une interaction peut ajuster légèrement main, coude ou torse vers une cible validée. Au-delà d’une portée maximale, le gameplay repositionne le personnage ou choisit une autre animation.

Le warping ne doit pas étirer silencieusement les membres.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
interaction_warp:
  action: interact_panel
  target: validated_interaction_anchor
  correctable_axes: [root_yaw, hand_offset_small]
  max_translation: profile_defined
  max_rotation: profile_defined
  fallback: reposition_or_reject
  limb_scale: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** l’ancre est fournie par le système d’interaction.

- **Amplitude :** les corrections petites préservent l’intention source.

- **Repli :** une cible hors enveloppe exige une décision explicite.

- **Interdit :** la mise à l’échelle d’un membre masque une mauvaise mise en place.


## 53. Structure de scène Godot pilote

La scène dérivée sépare modèle importé, `AnimationTree`, adaptateur de paramètres, root motion, événements et outils de validation. Le modèle importé reste intact.

Les nœuds de debug sont désactivés en production mais versionnés dans la scène de benchmark.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
Scène ScoutAnimated:
  CharacterBody3D:
    ImportedModel:
      Skeleton3D: {}
      AnimationPlayer: {}
    AnimationTree: {}
    AnimationParameterAdapter: {}
    RootMotionAdapter: {}
    AnimationEventRelay: {}
    Debug:
      ContactMarkers: {}
      RootMotionTrail: {}
      TransitionOverlay: {}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** le squelette et les animations viennent du GLB.

- **Adaptateur :** les variables gameplay deviennent des paramètres visuels.

- **Relais :** les événements sont filtrés avant diffusion.

- **Debug :** les preuves visuelles sont regroupées et désactivables.


## 54. Adaptateur de paramètres d’AnimationTree

Le code n’écrit pas des chemins de paramètres dispersés dans tout le projet. Un adaptateur centralise noms, conversions, bornes et diagnostics.

Les paramètres manquants sont détectés au chargement plutôt que pendant une action critique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
class_name ScoutAnimationParameters
extends Node

@export var animation_tree: AnimationTree

func set_locomotion_velocity(local_velocity: Vector2) -> void:
    var bounded := local_velocity.limit_length(1.0)
    animation_tree.set(
        "parameters/Locomotion/blend_position",
        bounded
    )

func request_state(state_name: StringName) -> void:
    var playback = animation_tree.get("parameters/playback")
    playback.travel(state_name)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Centralisation :** les chemins du graphe restent dans un seul composant.

- **Borne :** les entrées sont normalisées avant le blend space.

- **Playback :** la machine est contrôlée par son objet de lecture.

- **Contrat :** l’adaptateur reçoit un état visuel déjà décidé ailleurs.


## 55. Validation structurelle du graphe

Un validateur d’éditeur peut vérifier la présence des animations, paramètres, états, filtres et pistes root motion attendus. Il ne juge pas la qualité artistique.

La validation produit un rapport déterministe et échoue sur les dépendances manquantes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
func validate_animation_contract(
    player: AnimationPlayer,
    tree: AnimationTree,
    required_animations: Array[StringName]
) -> PackedStringArray:
    var errors := PackedStringArray()
    for animation_name in required_animations:
        if not player.has_animation(animation_name):
            errors.append("Missing animation: %s" % animation_name)
    if tree.tree_root == null:
        errors.append("AnimationTree has no root node")
    if tree.root_motion_track.is_empty():
        errors.append("Root motion track is not configured")
    return errors
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Présence :** les noms requis sont comparés à la bibliothèque importée.

- **Graphe :** un arbre sans root ne peut pas produire de résultat.

- **Root :** la piste extraite fait partie du contrat du pilote.

- **Limite :** le script ne remplace ni lecture des poses ni benchmark runtime.


## 56. Matrice de tests des animations

La validation croise animation, entrée, sortie, caméra, vitesse, pente et interruption. Une boucle réussie seule ne prouve pas que les transitions fonctionnent.

Chaque cas possède résultat, capture, version et réserve.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_test_matrix:
  dimensions:
    locomotion: [idle, walk, run]
    transition: [start, stop, turn, interact]
    terrain: [flat, slope_up, slope_down, step]
    camera: [game, side]
    interruption: [none, early, late]
  outputs:
    - pass_fail
    - contact_errors
    - root_motion_error
    - capture_ids
    - notes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Croisement :** les défauts apparaissent souvent à une combinaison précise.

- **Terrain :** le placement procédural est testé séparément de la source plate.

- **Interruption :** les entrées et sorties doivent résister à plusieurs moments.

- **Preuve :** les captures sont liées à la version exacte.


## 57. Captures, rapports et comparaison

Le rapport associe Action, graphe, paramètres, scène, caméra et version du moteur. Les captures côte à côte comparent source seule, blending et corrections procédurales.

Une vidéo promotionnelle ne remplace pas les vues de diagnostic.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_evidence:
  scene: ANIM_BENCH_SCOUT_001
  engine: Godot_4_7_1_stable
  captures:
    - source_only
    - animation_tree_blended
    - procedural_adjustments_enabled
    - contact_debug
    - root_motion_trail
  report: scout_animation_validation.md
  reproducible_camera: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** la scène et les versions rendent la preuve relisible.

- **Comparaison :** les couches sont activées progressivement.

- **Debug :** contacts et trajectoire root restent visibles.

- **Caméra :** un cadrage reproductible évite la sélection opportuniste.


## 58. Métriques et budgets

Le benchmark mesure coût CPU/GPU, nombre de squelettes, pistes actives, nœuds de graphe, événements, root motion et corrections procédurales. Les seuils dépendent des plateformes et du nombre de personnages.

Aucun chiffre n’est inventé avant exécution sur la scène cible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_budget_report:
  platform: pending
  character_count: measured
  active_animation_tracks: measured
  animation_tree_nodes_evaluated: measured
  procedural_modifiers: measured
  cpu_frame_time_ms: measured
  gpu_skinning_time_ms: measured
  memory_mb: measured
  acceptance_thresholds: pending_profile
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Charge :** le coût dépend du nombre de personnages et de pistes.

- **Procédural :** chaque correction ajoute un coût mesurable.

- **Plateforme :** les seuils ne sont pas universels.

- **Honnêteté :** toutes les valeurs restent `measured` ou `pending`.


## 59. Mode Solo

En Solo, une seule bibliothèque pilote couvre idle, marche, course, démarrage, arrêt, demi-tour et une interaction. Le graph reste petit et chaque ajout doit résoudre un cas observé.

Les corrections procédurales sont introduites après validation des sources.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
solo_plan:
  phase_1: [idle, walk, run]
  phase_2: [start, stop, turn_180]
  phase_3: [radio_use, interact_panel]
  phase_4: [blend_space, state_machine]
  phase_5: [look, foot_placement]
  rule: validate_before_expand
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** le noyau couvre d’abord les états réellement jouables.

- **Progression :** le graphe vient après les animations sources.

- **Procédural :** les corrections sont ajoutées en dernier.

- **Règle :** aucune bibliothèque massive n’est créée avant preuve du pilote.


## 60. Mode Studio

En Studio, les responsabilités sont séparées entre rigging, animation, intégration, gameplay et QA, mais partagent le même manifeste. Les passages sont formalisés par une version et une décision.

La bibliothèque de poses, la matrice de transitions et les profils d’événements sont gouvernés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
studio_ownership:
  rig_owner: skeleton_and_controls
  animation_owner: actions_and_curves
  integration_owner: import_and_animation_tree
  gameplay_owner: authoritative_state_and_movement
  qa_owner: matrices_captures_and_reports
  shared_contracts:
    - action_manifest
    - event_profile
    - root_motion_profile
    - transition_matrix
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Spécialisation :** chaque discipline possède une sortie vérifiable.

- **Contrats :** les profils réduisent les décisions implicites.

- **Gameplay :** l’autorité reste séparée des pistes visuelles.

- **QA :** les matrices et captures sont reproductibles par une autre personne.


## 61. Porte d’acceptation

La porte vérifie lisibilité, timing, contacts, boucle, courbes, root motion, événements, transitions, couches, correction procédurale, import et performance. Un succès partiel ne compense pas un contact cassé ou une autorité mal placée.

La décision finale est humaine et documentée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  blocking:
    - rig_contract_mismatch
    - major_contact_slide
    - broken_cycle_boundary
    - root_motion_authority_violation
    - missing_required_animation
    - unsafe_method_track
    - transition_dead_end
  measured:
    - locomotion_speed_match
    - procedural_cost
    - animation_cpu_cost
  decision: pending_human_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bloquant :** les erreurs structurelles et d’autorité arrêtent la livraison.

- **Mesure :** vitesse et coût nécessitent une exécution réelle.

- **Global :** cycles et transitions sont jugés ensemble.

- **Humain :** l’automatisation prépare les preuves sans approuver l’expression artistique.


## 62. Diagnostics et corrections

<!-- qa:error-correction-section -->

Les cas suivants utilisent la séquence symptôme, exemple fautif, explication directe, exemple corrigé et justification. Les valeurs restent pédagogiques et doivent être remplacées par les observations du pilote réel.


### 62.1 Enregistrer chaque contrôleur à chaque image

**Symptôme ou risque :** Le Graph Editor devient illisible et une correction de pose exige de retoucher des centaines de clés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
keying:
  every_control_every_frame: true
  generated_key_type: false
  cleanup: skipped
  status: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier traite la densité comme une preuve de qualité et ne distingue plus décisions artistiques, bake et bruit.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
keying:
  keying_set: KS_HUMANOID_BODY
  pose_keys: intentional
  baked_keys: tagged_generated
  cleanup_and_comparison: required
  status: candidate
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction réserve les clés denses aux résultats calculés et conserve une Action modifiable.


### 62.2 Laisser le root motion décider la collision

**Symptôme ou risque :** Le personnage traverse un obstacle parce que le delta animé est appliqué sans validation physique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func _physics_process(delta: float) -> void:
    global_position += animation_tree.get_root_motion_position()
    rotation *= animation_tree.get_root_motion_rotation()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le graphe visuel modifie directement la transformation et contourne le système de déplacement autoritaire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func _physics_process(delta: float) -> void:
    movement_adapter.offer_visual_root_motion(
        animation_tree.get_root_motion_position(),
        animation_tree.get_root_motion_rotation(),
        delta
    )
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction transmet le delta à un adaptateur qui conserve collision, bornes et décision gameplay.


### 62.3 Appliquer des dégâts depuis une piste de méthode

**Symptôme ou risque :** Un blend ou une reprise de lecture applique deux fois les dégâts.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func animation_hit_frame() -> void:
    target.health -= 25
    inventory.consume_ammo(1)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La piste d’animation exécute des mutations métier non idempotentes et devient une autorité cachée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func relay_animation_event(event_id: StringName) -> void:
    if event_id == &"attack_visual_peak":
        animation_event_emitted.emit(event_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction émet un repère visuel ; le système autoritaire décide séparément des conséquences.


### 62.4 Accélérer une marche pour fabriquer une course

**Symptôme ou risque :** Le personnage se déplace vite mais conserve doubles appuis, faible phase aérienne et amplitude de marche.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
locomotion:
  source: loco_walk_forward_base
  playback_speed: 2.4
  runtime_label: run
  visual_review: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La vitesse temporelle change sans transformer la structure biomécanique du cycle.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
locomotion:
  source: loco_run_forward_base
  required_phases: [contact, compression, passing, flight]
  root_speed_match: measured
  transition_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise une course dédiée et mesure son accord avec la vitesse gameplay.


### 62.5 Mélanger des cycles hors phase

**Symptôme ou risque :** Les pieds se croisent et glissent au milieu du blend space.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blend_space:
  points: [walk_left_contact, run_right_contact]
  sync_mode: CYCLIC_MUTABLE
  phase_manifest: omitted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le mode cyclique ne peut pas réparer des sources dont les phases logiques et contacts ne correspondent pas.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blend_space:
  points: [walk_left_contact, run_left_contact]
  sync_mode: CYCLIC_MUTABLE
  phase_manifest: required
  contact_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction aligne les phases avant de demander au graphe de synchroniser les durées.


### 62.6 Utiliser l’IK pour cacher un cycle qui glisse

**Symptôme ou risque :** Le pied semble planté sur une pente mais glisse encore sur sol plat lorsque l’IK est coupée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
foot_ik:
  enabled: always
  source_contact_review: skipped
  purpose: fix_walk_cycle
  max_correction: unlimited
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La correction procédurale masque une erreur source et ajoute des déformations non bornées.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
foot_ik:
  source_contacts: validated
  purpose: terrain_adaptation
  max_correction: profile_defined
  ab_test_disabled_mode: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction exige une source propre puis limite l’IK à l’adaptation locale au terrain.


### 62.7 Modifier directement la scène importée

**Symptôme ou risque :** Une réimportation du GLB efface le graphe, les paramètres et les corrections manuelles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
godot_scene:
  edited_file: scout_anim.glb
  animation_tree_added_inside_import: true
  derived_scene: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier importé est un dérivé régénéré et ne constitue pas une surface d’édition stable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
godot_scene:
  imported_file: scout_anim.glb
  derived_scene: scout_animated.tscn
  animation_tree_owner: derived_scene
  reimport_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction place l’intégration dans une scène dérivée qui survit à la réimportation.


### 62.8 Étiqueter un clip absolu comme additif

**Symptôme ou risque :** Le torse se déplace deux fois et les épaules quittent la pose de locomotion.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
layer:
  action: upper_radio_use_absolute
  mode: additive
  reference_pose: omitted
  mask: all_bones
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le clip contient des transformations absolues et ne définit ni référence ni filtre.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
layer:
  action: additive_breathing_subtle
  mode: additive
  reference_pose: neutral_ready
  mask: MASK-UPPER-BODY-V1
  zero_and_full_weight_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction emploie un delta explicite, un masque versionné et deux tests d’amplitude.


### 62.9 Employer le même cross-fade partout

**Symptôme ou risque :** Les pieds deviennent transparents entre locomotion et interaction, tandis qu’un arrêt paraît trop mou.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
transitions:
  default_blend_seconds: 0.25
  apply_to_all_edges: true
  entry_pose_review: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les transitions ont des contraintes de contact, de réponse et de pose différentes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
transitions:
  matrix: TRANSITIONS-SCOUT-V1
  per_edge_duration: required
  entry_pose_family: required
  interruption_policy: required
  bidirectional_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction traite chaque arête comme un contrat testable plutôt qu’un réglage global.


### 62.10 Valider uniquement les clips isolés

**Symptôme ou risque :** Chaque Action paraît correcte seule, mais les transitions créent sauts, glissements et états bloqués.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
review:
  isolated_actions: passed
  transition_matrix: skipped
  root_motion_blends: skipped
  procedural_ab_test: skipped
  decision: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La revue ignore le comportement émergent du graphe et les interactions entre couches.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
review:
  isolated_actions: required
  transition_matrix: required
  root_motion_blends: required
  procedural_ab_test: required
  benchmark_scene: required
  decision: pending_human_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction valide les sources, le graphe et les ajustements dans la même scène reproductible.


## 63. Checklist de livraison

La livraison documentaire est prête lorsque le lecteur peut identifier le rig compatible, les Actions canoniques, la base temporelle, les phases, les contacts, le root motion, les événements, les couches, les graphes, les corrections procédurales, les preuves et les réserves. Les fichiers et mesures de production restent à créer dans les outils réels.

- [ ] rig du chapitre 19 gelé et compatible ;
- [ ] manifeste d’Actions versionné ;
- [ ] poses, timing, spacing, arcs et silhouettes revus ;
- [ ] courbes nettoyées sans perte d’intention ;
- [ ] idle, marche, course, démarrages, arrêts et demi-tours validés ;
- [ ] contacts et limites de boucle contrôlés ;
- [ ] root motion comparé au mouvement gameplay ;
- [ ] événements filtrés et dépourvus d’autorité métier ;
- [ ] couches additives et masques testés à zéro et pleine amplitude ;
- [ ] blend spaces et synchronisation de phase inspectés ;
- [ ] machine à états et matrice de transitions testées ;
- [ ] IK, regard et warping comparés en mode activé et désactivé ;
- [ ] export GLB, bibliothèques et scène dérivée produits ;
- [ ] benchmark Godot et rapport de captures réalisés ;
- [ ] provenance et licence qualifiées ;
- [ ] décision humaine enregistrée.

## 64. Conclusion

Une animation exploitable n’est ni une collection de poses jolies ni un graphe runtime complexe. C’est un ensemble versionné où intention, rythme, contacts, déplacement, événements, blending et corrections procédurales restent séparés, mesurables et reproductibles.

Le pilote `AST-ANIM-PILOT-SCOUT-001` fournit un contrat complet pour passer du rig du chapitre 19 à une bibliothèque prête pour l’intégration. La capture de mouvement, son calibrage et son nettoyage spécialisé demeurent la responsabilité du chapitre 21.

## Références techniques qualifiées

- Blender Manual 5.0 : keyframes, Dope Sheet, Action Editor, Graph Editor, interpolation et types de clés ; la référence projet Blender 5.2.0 est conservée avec qualification documentaire.
- Godot Engine 4.7/stable : `AnimationPlayer`, `AnimationTree`, `AnimationNodeStateMachine`, blend spaces, `OneShot`, modes de synchronisation et extraction du root motion.
- glTF 2.0 : format d’échange par défaut pour les animations 3D et le squelette du pilote.

## 65. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-ANIM-PILOT-SCOUT-001` comme bibliothèque témoin construite sur le rig gelé du chapitre 19. Les Actions Blender canoniques, leur base temporelle, leurs phases, contacts, boucles, vitesses et événements sont versionnés séparément du graphe de lecture Godot. Le root motion, les fenêtres d’action et les pistes de méthode transportent des faits d’animation ; ils ne prennent pas l’autorité sur les règles de gameplay.

Le runtime Asteria organise locomotion, actions ponctuelles, couches additives, masques, blend spaces et machine à états dans un `AnimationTree` documenté. Chaque transition possède une durée, une politique d’interruption, une compatibilité de phase et une revue bidirectionnelle. Le regard, la visée, le placement des pieds et le warping restent des corrections procédurales bornées, comparées en mode activé et désactivé, et ne servent jamais à masquer une mauvaise animation source.

La porte d’acceptation exige les clips, le manifeste, le GLB, les bibliothèques importées, la matrice de transitions, les captures de contacts et une scène Godot reproductible. Tant que ces éléments ne sont pas exécutés, Project Asteria conserve le niveau `static-review` et ne revendique ni fluidité, ni absence de glissement, ni coût runtime mesuré.
