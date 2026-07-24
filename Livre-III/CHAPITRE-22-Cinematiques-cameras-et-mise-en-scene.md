---
title: "Livre III — Chapitre 22 : Cinématiques, caméras et mise en scène"
id: "DOC-L3-CH22"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 22
last-verified: "2026-07-24T15:16:59+02:00"
audit-status: "complete"
audit-date: "2026-07-24T15:16:59+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-22.md"
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
    qualification: "documentation-reviewed-against-project-reference"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Cinématiques, caméras et mise en scène

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH22`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+
## 1. Rôle du chapitre
Transformer une intention narrative en séquence Godot lisible, révisable et intégrée au build. La mise en scène organise ce que le public voit, quand il le comprend et comment la séquence rend ensuite l’autorité au gameplay.
Le fil rouge utilise `AST-CINE-PILOT-SCOUT-RELAY-001`. Il prolonge l’action de l’éclaireur et de sa radio définie aux chapitres 20 et 21, mais n’affirme pas que les animations, décors, voix, effets, lumières ou scènes correspondantes existent déjà.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```text

Rig, animations et clip radio candidats
    ↓
Intention dramatique et informations à transmettre
    ↓
Storyboard et liste de plans
    ↓
Blocage spatial et animatique
    ↓
Caméras et timeline Godot
    ↓
Synchronisation des dépendances existantes
    ↓
Tests dans le build et transition vers le gameplay
    ↓
Porte d'acceptation et versions de revue
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Amont :** les rigs, animations et clips restent la responsabilité des chapitres 19 à 21.
- **Transformation :** le chapitre convertit une intention en découpage, positions de caméra, rythme et orchestration.
- **Aval :** la séquence doit terminer dans un état compatible avec les systèmes autoritaires du Livre II.
- **Réserve :** aucun asset, rendu, enregistrement ou test runtime n’est revendiqué comme matérialisé.
## 2. Résultats d’apprentissage
À la fin du chapitre, le lecteur saura écrire un brief dramatique, construire un storyboard, produire une liste de plans, choisir un cadrage et une focale candidate, puis assembler une animatique avant de détailler la séquence.
Il saura également organiser plusieurs `Camera3D`, piloter une timeline avec `AnimationPlayer`, synchroniser des dépendances sans en prendre la propriété, gérer le saut et la fin de séquence, puis préparer des tests reproductibles dans le build.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

learning_outcomes:
  narrative: [dramatic_intent, beats, information_order]
  previsualization: [storyboard, shot_list, blocking, animatic]
  camera: [shot_size, field_of_view, composition, movement, continuity]
  godot: [Camera3D, AnimationPlayer, Path3D, PathFollow3D]
  synchronization: [character_animation, dialogue_placeholder, light, vfx_placeholder]
  integration: [skip, transition_to_gameplay, dependency_check, build_test]
  review: [versions, comments, acceptance_gate]
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Narration :** l’ordre d’apparition des informations devient un contrat observable.
- **Prévisualisation :** le storyboard et l’animatique ferment les choix coûteux avant la finition.
- **Godot :** les nœuds cités orchestrent la lecture sans créer les assets qu’ils consomment.
- **Intégration :** la séquence doit pouvoir finir, être sautée et restituer caméra, entrées et états.
- **Revue :** chaque version possède une décision et des réserves plutôt qu’un suffixe informel.
## 3. Niveau de preuve et réserves
Le chapitre est accepté au niveau `static-review`. Les structures de fichiers, scènes, scripts et timelines sont relues comme documentation, sans prétendre qu’un projet Godot, un storyboard ou une animatique ont été exécutés.
Les durées, focales, vitesses, coûts et seuils présentés comme candidats devront être mesurés ou approuvés sur les assets réels. Une valeur écrite dans un manifeste ne devient jamais une preuve d’expérience utilisateur ou de performance.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

evidence_level:
  chapter: static-review
  storyboard_materialized: false
  shot_list_materialized: false
  animatic_rendered: false
  godot_scene_created: false
  timeline_executed: false
  audio_light_vfx_synchronized: false
  skip_and_transition_tested: false
  build_tested: false
  runtime_measurements: false
  pdf_produced: false
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Statut :** la méthode et les exemples sont contrôlés statiquement.
- **Prévisualisation :** aucune planche, liste de plans ou vidéo n’est déclarée produite.
- **Runtime :** caméras, timeline, saut et transition ne sont pas annoncés comme exécutés.
- **Mesures :** durée réelle, coût CPU/GPU, mémoire et confort restent à établir.
- **Publication :** le PDF du Livre III demeure différé jusqu’à la fin du Livre.
## 4. Frontières avec les chapitres voisins
Le chapitre 20 reste propriétaire des principes d’animation, des Actions, des événements et des graphes. Le chapitre 21 reste propriétaire de la capture, du nettoyage et du retargeting. Le présent chapitre choisit seulement comment ces mouvements candidats sont montrés et synchronisés.
Le chapitre 23 produira les VFX ; le chapitre 26 produira et mixera l’audio ; le chapitre 27 traitera la synchronisation labiale ; le chapitre 28 consolidera l’import global. La caméra de gameplay et les entrées restent sous l’autorité du Livre II.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

ownership:
  chapter_20: authored_animation_and_runtime_animation_graph
  chapter_21: mocap_cleanup_mapping_and_retargeting
  chapter_22: cinematic_decoupage_camera_timeline_and_staging
  chapter_23: vfx_assets_and_particle_simulations
  chapter_26: voice_sfx_ambience_music_and_mix
  chapter_27: lip_sync_and_facial_animation
  chapter_28: global_asset_import_and_reimport
  book_ii_chapter_06: gameplay_camera_and_player_input
  book_ii_chapter_25: narrative_facts_quests_and_authoritative_consequences
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Animation :** une caméra ne corrige pas une pose ou un contact défectueux.
- **Effets :** le chapitre synchronise des placeholders ou assets approuvés sans fabriquer leur bibliothèque.
- **Gameplay :** la séquence demande une suspension ou reprise via un contrat externe.
- **Narration :** les conséquences métier sont décidées par les systèmes du Livre II.
- **Intégration :** les imports et réimports universels restent réservés au chapitre 28.
## 5. Pilote cinématique de Project Asteria
Le pilote montre un éclaireur qui atteint une station-relais abandonnée, s’accroupit, saisit sa radio, entend un fragment de signal et relève la tête vers une lumière lointaine. La scène doit transmettre prudence, isolement, découverte et reprise de contrôle.
La séquence candidate reste courte : un établissement du lieu, une progression lisible, un gros plan de contact, une révélation sonore et visuelle, puis un raccord vers la caméra de gameplay. Chaque plan existe pour une information précise.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

pilot:
  sequence_id: AST-CINE-PILOT-SCOUT-RELAY-001
  dramatic_question: "Le relais est-il réellement abandonné ?"
  protagonist: AST-CHAR-SCOUT-001
  animation_source: AST-MOCAP-PILOT-SCOUT-001
  location_candidate: AST-ENV-RELAY-OUTPOST-001
  prop: AST-PROP-RADIO-001
  target_duration_s: candidate
  shot_count: 7_candidate
  godot_scene: res://cinematics/scout_relay/scout_relay_sequence.tscn
  status: not_materialized
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Question :** la scène est organisée autour d’une incertitude compréhensible.
- **Continuité :** le geste radio consomme le contrat d’animation existant au lieu de le réécrire.
- **Lieu :** l’environnement reçoit un identifiant candidat et reste une dépendance.
- **Durée :** le nombre de secondes et de plans sera validé par l’animatique.
- **Statut :** le pilote décrit une cible de production, pas une séquence déjà créée.
## 6. Vocabulaire de mise en scène
Un plan est une portion continue vue depuis une caméra. Une scène regroupe une unité d’action dans un lieu et un temps cohérents. Une séquence peut réunir plusieurs scènes ou plans pour accomplir une fonction narrative complète.
Le setup décrit la configuration de caméra, lumière et jeu ; la prise désigne une exécution enregistrée ; l’animatique est un montage temporel de storyboards ou de blocs ; la timeline ordonne les événements sans devenir propriétaire de leurs règles.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

terminology:
  shot: continuous_camera_view
  setup: camera_light_and_staging_configuration
  take: recorded_execution_of_a_setup
  scene: coherent_action_unit
  sequence: narrative_unit_composed_of_shots
  storyboard: ordered_visual_intentions
  animatic: timed_previsualization
  timeline: ordered_playback_contract
  cut: instantaneous_change_of_view
  transition: controlled_change_between_views_or_states
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Plan :** la caméra reste continue jusqu’à la coupe ou la fin.
- **Setup :** plusieurs prises peuvent partager une même configuration.
- **Animatique :** le rythme est testé avant les assets finaux.
- **Timeline :** elle orchestre des pistes et appels, sans décider des conséquences métier.
- **Transition :** elle peut concerner la vue, le son ou le passage vers le gameplay.
## 7. Intention dramatique et promesse de lecture
Avant de choisir une focale, écrire ce que le public doit comprendre, ressentir et anticiper. Une intention telle que « rendre le relais immense » est visuelle ; « annoncer une menace sans la montrer » est narrative ; les deux doivent être reliées.
Le brief distingue information obligatoire, information secondaire et ambiguïté volontaire. Une image esthétique qui cache le geste nécessaire au récit est non conforme, même si sa composition est séduisante.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

dramatic_brief:
  sequence_id: AST-CINE-PILOT-SCOUT-RELAY-001
  audience_must_understand:
    - scout_enters_unknown_relay
    - radio_receives_unexpected_signal
    - distant_light_changes_the_goal
  audience_should_feel: [isolation, caution, discovery]
  intentional_unknowns:
    - signal_sender_identity
    - distant_light_origin
  forbidden_confusion:
    - whether_the_scout_heard_the_signal
    - whether_control_has_returned_to_gameplay
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Obligatoire :** les trois faits doivent survivre au montage et au mix.
- **Émotion :** les choix de distance, durée et mouvement soutiennent une sensation nommée.
- **Ambiguïté :** les inconnues volontaires restent différentes d’une information mal montrée.
- **Interdit :** la réception du signal et la reprise du contrôle doivent être explicites.
## 8. Beats, actions et retournements
Un beat est une unité de changement perceptible : entrée, hésitation, contact, révélation, décision ou sortie. Les beats permettent de comparer storyboard, animatique et timeline sans dépendre du numéro d’image.
Chaque beat possède une information, une action visible ou sonore et une conséquence de mise en scène. Une durée candidate peut changer, mais l’ordre causal doit rester lisible.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

beats:
  B01: {event: enter_relay, information: unsafe_space, visual_priority: silhouette}
  B02: {event: stop_and_listen, information: possible_presence, audio_priority: ambience_drop}
  B03: {event: crouch_and_grasp_radio, information: deliberate_contact, visual_priority: hands}
  B04: {event: signal_fragment, information: relay_not_empty, audio_priority: radio}
  B05: {event: distant_light_activates, information: new_direction, visual_priority: depth}
  B06: {event: scout_recovers, information: agency_returns, transition: gameplay}
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identifiants :** les beats restent stables lorsque le montage change.
- **Priorité :** chaque changement indique le canal qui porte l’information.
- **Cause :** le signal précède la lumière afin que la révélation conserve son sens.
- **Transition :** le dernier beat prépare une pose et une caméra compatibles avec le gameplay.
## 9. Manifeste des dépendances
Une cinématique rassemble de nombreux assets et peut sembler fonctionner sur la machine de son auteur tout en perdre une animation ou un son ailleurs. Le manifeste rend chaque dépendance explicite avant le blocage.
Les dépendances sont classées comme obligatoires, remplaçables par placeholder ou exclues du périmètre. Un élément absent ne doit jamais être remplacé silencieusement par une ressource au nom proche.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

dependencies:
  required:
    character_scene: res://characters/scout/scout_animated.tscn
    relay_environment: res://environments/relay/relay_outpost.tscn
    radio_prop: res://props/radio/radio.tscn
    animation_library: res://assets/animations/scout_mocap.tres
  placeholders_allowed:
    dialogue: res://cinematics/placeholders/radio_signal_placeholder.ogg
    vfx: res://cinematics/placeholders/distant_light_placeholder.tscn
  excluded:
    final_audio_mix: chapter_26
    final_vfx_asset: chapter_23
    lip_sync: chapter_27
  missing_required_policy: block_playback
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Obligatoire :** personnage, lieu, accessoire et animation conditionnent la lecture.
- **Placeholder :** une ressource temporaire porte un nom et un statut explicites.
- **Exclusion :** les lots futurs restent propriétaires de leurs productions.
- **Blocage :** une dépendance obligatoire absente empêche une fausse validation.
## 10. Sources canoniques et dérivés
Le brief, le storyboard, la liste de plans et la scène Godot sont des sources différentes. Une vidéo de revue ou une capture d’écran est un dérivé, utile pour commenter mais incapable de remplacer la timeline.
Un changement de durée revient dans la source concernée ; on ne découpe pas seulement la vidéo exportée. Cette règle permet de reconstruire les revues et de comparer les versions.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

source_hierarchy:
  narrative_brief: cinematics/scout_relay/source/brief.md
  storyboard: cinematics/scout_relay/source/storyboard/
  shot_list: cinematics/scout_relay/source/shot_list.yaml
  animatic_source: cinematics/scout_relay/source/animatic.blend
  godot_sequence: res://cinematics/scout_relay/scout_relay_sequence.tscn
  timeline_resource: res://cinematics/scout_relay/scout_relay_timeline.tres
  review_renders: cinematics/scout_relay/review/
  build_captures: cinematics/scout_relay/evidence/
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Brief :** il porte la fonction narrative et les beats.
- **Prévisualisation :** storyboard et animatique restent éditables.
- **Godot :** scène et ressource de timeline sont les sources d’intégration.
- **Preuves :** les rendus et captures nomment la version qui les a produits.
## 11. Identifiants et versions
Les identifiants de séquence, plan, setup et version ne dépendent pas d’un titre marketing. Un plan supprimé reste dans l’historique ; son numéro n’est pas réattribué à un autre cadrage.
Une version de revue décrit un état cohérent du montage. Les suffixes `final`, `final2` ou `vrai_final` sont interdits car ils ne relient pas la décision à une version stable.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

naming:
  sequence: AST-CINE-PILOT-SCOUT-RELAY-001
  shot_pattern: AST-CINE-SR-SH{number:03d}
  setup_pattern: AST-CINE-SR-SETUP{number:03d}
  review_pattern: AST-CINE-SR-REV-{version}
  examples:
    - AST-CINE-SR-SH010
    - AST-CINE-SR-SH020
    - AST-CINE-SR-REV-0.3.0
  forbidden: [final, final2, latest_new, shot_new]
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Séquence :** l’identifiant relie tous les livrables du pilote.
- **Plans :** un pas de dix laisse de la place pour insérer un plan sans renuméroter.
- **Setup :** plusieurs plans peuvent réutiliser une configuration contrôlée.
- **Revue :** la version permet de retrouver commentaires, dépendances et captures.
## 12. Storyboard : information avant détail
Le storyboard doit montrer position des personnages, direction du regard, axe de déplacement, taille de plan et information principale. Il peut rester dessiné simplement tant que la lecture est non ambiguë.
Chaque vignette reçoit un identifiant de plan, une flèche de mouvement, une durée candidate et une note sonore. Les détails de matériaux et de lumière ne doivent pas ralentir la validation du découpage.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

storyboard_frame:
  shot_id: AST-CINE-SR-SH030
  image_ref: storyboard/SH030-contact-radio.png
  shot_size: close_up_hands
  camera_motion: static
  subject_motion: hand_reaches_radio
  screen_direction: left_to_right
  duration_s: candidate
  primary_information: radio_contact
  audio_note: ambience_narrows_before_signal
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Image :** la vignette est une source de prévisualisation versionnée.
- **Mouvement :** caméra et sujet sont décrits séparément.
- **Direction :** le sens écran prépare les raccords avec les plans voisins.
- **Information :** le contact radio justifie le gros plan.
- **Durée :** la valeur reste candidate jusqu’au montage de l’animatique.
## 13. Construire la liste de plans
La liste de plans est un registre, pas un résumé littéraire. Une ligne décrit l’intention du plan, ses bornes, ses dépendances, sa caméra, son statut et la raison de toute modification.
Le plan est accepté seulement si son information reste nécessaire. Un plan décoratif sans fonction peut être supprimé avant d’engager animation, lumière, son et VFX.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

shots:
  - id: AST-CINE-SR-SH010
    purpose: establish_relay_and_isolation
    size: wide
    movement: slow_dolly_in_candidate
    beat_in: B01
    beat_out: B02
    dependencies: [relay_environment, scout_scene]
    status: storyboard
  - id: AST-CINE-SR-SH030
    purpose: prove_radio_contact
    size: close_up
    movement: static
    beat_in: B03
    beat_out: B04
    dependencies: [scout_animation, radio_prop]
    status: storyboard
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **But :** le plan existe pour une information testable.
- **Bornes :** les beats rendent le montage comparable aux autres sources.
- **Dépendances :** l’équipe sait quels assets seront visibles de près.
- **Statut :** storyboard, blocking, animatic et approved restent distincts.
## 14. Valider une liste de plans avec Python
Le script suivant illustre un contrôle statique d’une liste déjà chargée en Python. Il vérifie l’identité, l’ordre et les champs minimaux, sans ouvrir Godot ni juger le cadrage.
Il renvoie des diagnostics textuels. Un retour vide signifie seulement que le schéma contrôlé est cohérent ; il ne prouve ni le rythme, ni la lisibilité, ni la présence des assets.
> **[VSC] Visual Studio Code — Exemple Python à placer dans un outil de validation de production.**
```python

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

def validate_shot_list(shots: Sequence[dict[str, Any]]) -> list[str]:
    diagnostics: list[str] = []
    seen: set[str] = set()
    previous_number = -1

    for index, shot in enumerate(shots):
        shot_id = shot.get("id")
        purpose = shot.get("purpose")
        status = shot.get("status")

        if not isinstance(shot_id, str) or not shot_id:
            diagnostics.append(f"SHOT_ID_INVALID:{index}")
            continue
        if shot_id in seen:
            diagnostics.append(f"SHOT_ID_DUPLICATE:{shot_id}")
        seen.add(shot_id)

        suffix = shot_id.rsplit("SH", 1)[-1]
        if not suffix.isdigit():
            diagnostics.append(f"SHOT_NUMBER_INVALID:{shot_id}")
        else:
            number = int(suffix)
            if number <= previous_number:
                diagnostics.append(f"SHOT_ORDER_INVALID:{shot_id}")
            previous_number = number

        if not isinstance(purpose, str) or not purpose:
            diagnostics.append(f"SHOT_PURPOSE_MISSING:{shot_id}")
        if status not in {"storyboard", "blocking", "animatic", "approved"}:
            diagnostics.append(f"SHOT_STATUS_INVALID:{shot_id}")

    return diagnostics
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Signature :** `shots` est une `Sequence` de dictionnaires et le retour est `list[str]`.
- **Types :** `isinstance` refuse les identifiants et fonctions absents ou d’un type inattendu.
- **Opérateurs :** `in`, `not in`, `<=` et `rsplit` contrôlent doublons, statuts, ordre et suffixe.
- **État local :** `seen` et `previous_number` servent uniquement pendant l’appel.
- **Retour :** les diagnostics sont consommés par l’appelant ; la fonction ne modifie pas la liste.
- **Limite :** composition, continuité et rythme exigent une revue visuelle.
## 15. Tailles de plan et distance narrative
Une taille de plan décrit la place du sujet dans l’image : plan général, plan d’ensemble, plan moyen, plan rapproché, gros plan ou très gros plan. Elle n’est pas définie uniquement par la distance physique, car la focale et la taille du sujet modifient le cadre.
Le pilote réserve le plan général au lieu, le plan moyen au déplacement et le gros plan au contact radio. Répéter des gros plans réduit leur valeur et peut désorienter si aucun plan ne rétablit l’espace.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

shot_size_policy:
  wide: environment_relationship_and_scale
  full: whole_body_action_and_direction
  medium: posture_gesture_and_interaction
  close_up: decisive_object_or_emotion
  extreme_close_up: exceptional_detail_only
  pilot_usage:
    SH010: wide
    SH020: full
    SH030: close_up
    SH040: medium
    SH050: wide_reveal
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Large :** le décor et l’échelle spatiale portent l’information.
- **Corps :** le plan en pied conserve contacts et direction.
- **Rapproché :** le geste et l’accessoire deviennent prioritaires.
- **Gros plan :** il est réservé à un détail narrativement décisif.
- **Séquence :** l’alternance évite une suite de cadres sans géographie.
## 16. Focale, champ de vision et perspective
`Camera3D.fov` exprime un champ de vision vertical en degrés lorsque la caméra utilise la projection perspective. Un champ plus large montre davantage d’espace et accentue la perspective près de la caméra ; un champ plus étroit isole le sujet et comprime visuellement les plans.
La focale physique et le FOV ne sont pas des synonymes parfaits sans connaître la taille du capteur virtuel. Le projet documente le FOV réellement saisi dans Godot, puis décrit l’effet visuel recherché.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

camera_lens_profile:
  camera_id: AST-CINE-SR-CAM-SH030
  projection: perspective
  fov_degrees: candidate
  near_m: candidate
  far_m: candidate
  framing_target: radio_and_hands
  perspective_intent: restrained
  approval_requires:
    - subject_scale_review
    - distortion_review
    - gameplay_fov_transition_review
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Projection :** la perspective conserve la diminution apparente avec la distance.
- **FOV :** la valeur reste candidate jusqu’au test sur le cadre réel.
- **Plans de coupe :** `near` et `far` doivent éviter clipping et perte de précision.
- **Intention :** le profil décrit l’effet attendu sans prétendre simuler une optique mesurée.
- **Raccord :** le passage vers le FOV gameplay doit être inspecté.
## 17. Projection orthographique et usages limités
La projection orthographique conserve la taille apparente avec la distance. Elle convient à une carte, une vue technique ou une intention graphique spécifique, mais elle change fortement la perception de profondeur.
Le pilote principal reste en perspective. Une vue orthographique éventuelle serait une variante explicitement motivée, jamais un correctif pour un cadrage difficile.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

orthographic_variant:
  allowed_for:
    - map_insert
    - technical_overlay
    - explicitly_flat_visual_language
  forbidden_as:
    - perspective_distortion_fix
    - universal_cinematic_default
  camera_property: Camera3D.projection
  size_property: Camera3D.size
  pilot_default: perspective
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Usage :** la projection répond à une fonction visuelle nommée.
- **Propriété :** `projection` sélectionne le modèle de caméra.
- **Taille :** `size` remplace la logique de FOV en orthographique.
- **Défaut :** la séquence du relais conserve une perspective cohérente avec le gameplay.
## 18. Composition et hiérarchie visuelle
La composition dirige l’attention avec position, contraste, lumière, profondeur, lignes, mouvement et netteté. La règle des tiers est une aide, pas une loi capable de remplacer l’intention dramatique.
Chaque plan nomme son sujet primaire, ses éléments secondaires et les distractions à réduire. Un objet lumineux en arrière-plan peut annoncer la révélation, mais ne doit pas voler l’attention avant le beat prévu.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

composition:
  shot_id: AST-CINE-SR-SH040
  primary_subject: scout_reaction
  secondary_subject: radio
  reveal_subject: distant_relay_light
  reveal_visibility_before_B05: obscured_or_low_contrast
  leading_lines: relay_corridor
  negative_space: screen_right
  distraction_review:
    - bright_background_props
    - high_frequency_vfx
    - accidental_tangent_edges
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Primaire :** la réaction doit être lue avant le détail du décor.
- **Secondaire :** la radio maintient la causalité du signal.
- **Révélation :** la lumière change de statut au beat B05.
- **Espace :** la zone vide prépare l’apparition du nouvel objectif.
- **Revue :** contraste, VFX et tangentes sont contrôlés comme sources de distraction.
## 19. Profondeur, plans et séparation
Une image 3D reste lisible lorsque premier plan, sujet et arrière-plan possèdent des rôles distincts. La profondeur peut venir du recouvrement, de l’échelle, de la lumière, du brouillard, du mouvement relatif ou de la netteté.
Le premier plan ne doit pas masquer l’action critique. Les effets de profondeur restent réversibles afin de comparer une image claire avec une version plus atmosphérique.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

depth_layers:
  foreground: relay_frame_and_cables
  subject_plane: scout_and_radio
  background: tower_and_distant_light
  separation_tools:
    - luminance_contrast
    - color_temperature_candidate
    - atmospheric_depth_placeholder
    - relative_motion
  critical_visibility:
    radio_contact: unobstructed
    distant_light_reveal: readable
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Premier plan :** il donne une échelle sans couper le contact radio.
- **Sujet :** le personnage et l’accessoire partagent la couche narrative centrale.
- **Arrière-plan :** la tour porte la révélation et le futur objectif.
- **Outils :** les moyens de séparation sont testés séparément avant cumul.
- **Critères :** les deux informations obligatoires restent visibles.
## 20. Hauteur et angle de caméra
La hauteur par rapport au sujet influence la relation perçue : un angle légèrement bas peut renforcer la structure du relais ; un angle haut peut diminuer le personnage ou clarifier le sol. Ces effets restent contextuels et doivent éviter les clichés automatiques.
Le pivot, la hauteur et l’inclinaison sont enregistrés dans le setup. Une caméra penchée pour créer de la tension reçoit une justification et un raccord prévu.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

camera_setup:
  setup_id: AST-CINE-SR-SETUP020
  target_subject: scout
  height_reference: eye_level_candidate
  pitch_degrees: candidate
  roll_degrees: 0_default
  low_angle_intent: none
  high_angle_intent: none
  dutch_angle:
    allowed: only_if_dramatically_justified
    return_to_level: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Référence :** la hauteur est définie par rapport au sujet ou au décor.
- **Tangage :** la valeur change le partage sol, personnage et architecture.
- **Roulis :** zéro reste la valeur normale afin de préserver l’horizon.
- **Dérogation :** un angle incliné possède une intention et une sortie lisible.
## 21. Direction écran et règle des 180 degrés
Une ligne d’action relie les sujets ou suit le déplacement principal. Placer les caméras du même côté conserve la direction écran et la géographie ; franchir l’axe peut être volontaire si le passage est préparé.
Le pilote garde l’éclaireur se déplaçant de gauche à droite jusqu’à la révélation. Un plan neutre sur l’axe ou un mouvement visible peut autoriser un changement de côté.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

screen_direction:
  action_axis: relay_entrance_to_radio_console
  initial_direction: left_to_right
  camera_side: side_A
  crossing_policy:
    unmotivated_cut: forbidden
    neutral_axis_shot: allowed
    visible_camera_move_across_axis: allowed_after_review
  post_reveal_direction: preserved_candidate
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Axe :** la ligne est définie par le trajet et la console.
- **Côté :** les setups initiaux restent dans le même demi-espace.
- **Interdit :** une coupe non préparée peut inverser le mouvement perçu.
- **Passage :** un plan neutre ou un mouvement rend le changement observable.
## 22. Raccords de regard
Un raccord de regard relie la direction des yeux ou de la tête à ce qui est montré ensuite. Le plan de réaction et le plan de l’objet doivent partager une géographie plausible.
Le chapitre 27 traitera les détails du visage ; ici, la tête, la ligne de regard et le placement de la caméra suffisent à préparer le raccord.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

eyeline_match:
  source_shot: AST-CINE-SR-SH040
  subject: scout_head
  gaze_direction: screen_right_and_up_candidate
  destination_shot: AST-CINE-SR-SH050
  revealed_object: distant_relay_light
  vertical_relation: consistent
  facial_detail: chapter_27_or_authored_placeholder
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** le plan de réaction fournit une direction visible.
- **Destination :** le plan suivant révèle la cible attendue.
- **Verticalité :** la hauteur relative évite un regard qui pointe ailleurs.
- **Frontière :** le facial détaillé reste une dépendance future.
## 23. Raccord dans le mouvement
Couper pendant une action continue peut masquer une différence de cadrage si la phase du geste reste cohérente. Le point de coupe doit être comparé sur les deux plans, surtout lorsque la main touche un accessoire.
Le raccord n’autorise pas deux versions incompatibles du mouvement. Les contacts et phases appartiennent toujours aux animations approuvées.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

match_on_action:
  action: raise_radio
  outgoing_shot: AST-CINE-SR-SH020
  incoming_shot: AST-CINE-SR-SH030
  shared_phase: hand_approach_before_contact
  outgoing_time_s: candidate
  incoming_time_s: candidate
  contact_frame_source: animation_phase_marker
  retime_without_animation_review: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Action :** les deux plans montrent le même geste continu.
- **Phase :** la coupe se place avant le contact afin de préserver la causalité.
- **Temps :** les valeurs sont choisies dans l’animatique puis reportées.
- **Source :** le marqueur d’animation reste l’autorité du contact.
- **Interdit :** un retiming cinématique ne doit pas casser la source sans revue animation.
## 24. Continuité des accessoires et du décor
Position, orientation et état d’un accessoire doivent rester cohérents entre les plans. La radio ne peut pas changer de main ou pivoter sans action visible simplement parce que deux setups utilisent des poses différentes.
Les portes, lumières, particules et objets déplacés suivent la même règle. Une différence volontaire est un beat ; une différence involontaire est une erreur de continuité.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

continuity_log:
  radio:
    owner_socket_before_contact: belt_socket
    hand_during_hold: right
    orientation_profile: AST-RADIO-HOLD-V1
  relay_door:
    state: half_open
  distant_light:
    state_before_B05: off
    state_after_B05: on
  environment_damage:
    version: AST-ENV-RELAY-DAMAGE-V1
  review_per_shot: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Radio :** socket, main et orientation suivent une chronologie explicite.
- **Porte :** son état ne varie pas selon la caméra.
- **Lumière :** le changement est réservé au beat de révélation.
- **Décor :** la version empêche deux plans de charger des variantes incompatibles.
## 25. Mouvements de caméra
Un panoramique tourne la caméra ; un travelling déplace son origine ; un tilt change le tangage ; un truck se déplace latéralement ; un dolly avance ou recule ; une grue modifie hauteur et position. Ces termes décrivent des transformations différentes.
Le mouvement est retenu seulement s’il révèle une information, suit une action ou modifie la relation spatiale. Ajouter un mouvement à chaque plan diminue la stabilité et augmente les raccords à contrôler.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

camera_motion_catalog:
  pan: rotate_around_vertical_axis
  tilt: rotate_around_horizontal_axis
  dolly: translate_forward_or_backward
  truck: translate_laterally
  pedestal: translate_vertically
  crane: combined_position_and_height_path
  orbit: move_around_subject
  static: intentional_fixed_frame
  pilot_rule: one_primary_motion_per_shot_candidate
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rotation :** pan et tilt changent l’orientation sans déplacer l’origine.
- **Translation :** dolly, truck et pedestal déplacent la caméra.
- **Composé :** grue et orbite exigent une trajectoire et un sujet de référence.
- **Statique :** l’absence de mouvement est un choix actif.
- **Règle :** un mouvement principal facilite la lecture et le diagnostic.
## 26. Trajectoires avec `Path3D` et `PathFollow3D`
`Path3D` porte une courbe ; `PathFollow3D` fournit une transformation le long de cette courbe. Une caméra peut être enfant du suiveur afin que la timeline anime sa progression.
La courbe définit le trajet, pas automatiquement le cadrage. L’orientation vers le sujet, les accélérations et les collisions avec le décor doivent être revues séparément.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

path_camera:
  root: Path3D
  follower: PathFollow3D
  camera: Camera3D
  animated_property: PathFollow3D.progress_ratio
  progress_range: [0.0, 1.0]
  orientation_mode: reviewed
  speed_curve: authored_in_timeline
  collision_clearance: manual_review
  reusable_path_without_camera: allowed
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Courbe :** `Path3D` conserve la géométrie de déplacement.
- **Suiveur :** `progress_ratio` est un flottant normalisé de zéro à un.
- **Caméra :** son orientation peut être indépendante de la tangente.
- **Vitesse :** la courbe temporelle se règle dans l’`AnimationPlayer`.
- **Limite :** le chemin ne garantit ni visibilité ni absence d’intersection.
## 27. Mouvement organique et bruit borné
Une vibration légère peut suggérer une caméra portée, du vent ou une structure instable. Elle doit rester une couche séparée, désactivable et limitée en translation, rotation et fréquence.
Un bruit aléatoire non déterministe complique la comparaison des versions. La prévisualisation utilise une seed ou une courbe bakée lorsque la répétabilité est nécessaire.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

camera_noise:
  layer_id: AST-CINE-CAM-NOISE-SUBTLE-V1
  translation_amplitude_m: candidate
  rotation_amplitude_deg: candidate
  frequency_hz: candidate
  seed: fixed_for_review
  blend_weight: animated
  disable_for_accessibility: true
  base_camera_motion_preserved: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Amplitude :** translation et rotation possèdent des unités distinctes.
- **Fréquence :** la vitesse du bruit influence davantage le confort que son seul déplacement.
- **Seed :** les revues comparent le même mouvement.
- **Accessibilité :** la couche peut être réduite ou désactivée.
- **Base :** le bruit n’écrase pas la trajectoire principale.
## 28. Blocage spatial
Le blocage place personnages, accessoires et caméras avec des volumes simples. Il vérifie entrées, sorties, silhouettes, lignes de regard, distances et collisions visuelles avant la finition.
Une pose temporaire peut suffire à tester le cadre, mais elle porte un statut de placeholder. Le blocage ne doit pas être confondu avec une validation d’animation.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

blocking:
  environment: relay_outpost_proxy
  character: scout_proxy_or_approved_scene
  prop: radio_proxy
  cameras:
    - AST-CINE-SR-CAM-SH010
    - AST-CINE-SR-CAM-SH020
    - AST-CINE-SR-CAM-SH030
  check:
    - entrances_and_exits
    - silhouettes
    - eyelines
    - action_axis
    - camera_clearance
  animation_status: placeholder_or_candidate
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Proxy :** les volumes simples ferment les décisions de géographie.
- **Caméras :** chaque plan pointe vers un nœud nommé.
- **Contrôles :** les problèmes spatiaux sont détectés avant le détail.
- **Statut :** une animation temporaire ne devient pas une source approuvée.
## 29. Construire l’animatique
L’animatique assemble les vignettes ou le blocage selon une base temporelle commune. Elle ajoute sons temporaires, coupes et mouvements simples afin d’évaluer le rythme.
Chaque durée reste modifiable jusqu’à ce que les beats soient lisibles. Un plan trop long ou trop court est corrigé dans la source, puis la liste de plans reçoit la nouvelle borne.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

animatic:
  sequence_id: AST-CINE-PILOT-SCOUT-RELAY-001
  timebase_fps: 30_candidate
  shots:
    - {id: SH010, duration_s: candidate, transition: cut}
    - {id: SH020, duration_s: candidate, transition: cut}
    - {id: SH030, duration_s: candidate, transition: cut}
    - {id: SH040, duration_s: candidate, transition: cut}
    - {id: SH050, duration_s: candidate, transition: cut}
  placeholder_audio: explicitly_labeled
  review_focus: [information_order, rhythm, spatial_continuity]
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Base temporelle :** le FPS candidat facilite l’échange sans imposer la durée finale.
- **Plans :** les durées sont reliées aux identifiants de la liste.
- **Transitions :** la coupe reste le défaut afin d’éviter des fondus décoratifs.
- **Son :** les placeholders sont reconnaissables et remplaçables.
- **Revue :** la finition visuelle n’entre pas encore dans la décision.
## 30. Base temporelle et secondes
Godot évalue les animations selon le temps, même si l’éditeur affiche des clés sur une règle. Les secondes restent l’unité d’échange principale entre liste de plans, dialogue, animation et audio.
Le FPS de prévisualisation facilite les calculs d’images mais ne doit pas créer une dérive cumulative. Toute conversion conserve l’instant source et la méthode d’arrondi.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

time_contract:
  unit: seconds
  animatic_fps: 30_candidate
  godot_timeline_length_s: derived_from_approved_animatic
  source_timecodes: preserved_when_available
  frame_to_seconds: frame_index / fps
  rounding_policy: nearest_frame_for_review_only
  dialogue_markers: seconds
  animation_phase_markers: seconds
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Unité :** les secondes relient outils et ressources de fréquences différentes.
- **Formule :** la division produit un temps flottant à partir d’un indice entier.
- **Arrondi :** les images servent à la revue sans remplacer l’instant continu.
- **Marqueurs :** dialogue et animation sont comparés dans le même repère.
## 31. Arborescence de la scène cinématique
La scène cinématique instancie les assets approuvés et ajoute uniquement ses caméras, points de mise en scène, timeline et adaptateurs. Elle n’édite pas directement les scènes importées.
Les nœuds sont regroupés par responsabilité afin que la caméra, le décor et les pistes puissent être inspectés ou remplacés indépendamment.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```text

ScoutRelaySequence
├── World
│   ├── RelayOutpostInstance
│   ├── ScoutInstance
│   └── RadioInstance
├── Staging
│   ├── Marks
│   └── LookTargets
├── Cameras
│   ├── CAM_SH010
│   ├── CAM_SH020
│   ├── CAM_SH030
│   ├── CAM_SH040
│   └── CAM_SH050
├── Timeline
│   └── AnimationPlayer
├── AudioPlaceholders
├── VFXPlaceholders
└── CinematicDirector
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **World :** les assets restent des instances de leurs sources.
- **Staging :** marques et cibles servent uniquement à la mise en scène.
- **Caméras :** chaque plan possède un nœud identifiable.
- **Timeline :** un `AnimationPlayer` orchestre les propriétés de la séquence.
- **Directeur :** le script coordonne démarrage, fin, saut et restitution.
## 32. Scènes importées et scènes dérivées
Une scène GLB ou un personnage importé ne doit pas devenir la surface d’édition cinématique. La scène de séquence instancie une scène dérivée qui protège matériaux, animations et scripts lors de la réimportation.
Les offsets spécifiques au plan restent dans des pivots de staging ou dans la timeline. Une correction permanente du personnage remonte à sa source propriétaire.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

scene_ownership:
  imported_character: res://assets/characters/scout/scout_anim.glb
  derived_character: res://characters/scout/scout_animated.tscn
  cinematic_instance: res://cinematics/scout_relay/scout_relay_sequence.tscn
  direct_edit_imported_scene: forbidden
  cinematic_offsets_live_in:
    - staging_nodes
    - timeline_tracks
  permanent_animation_fix_owner: chapter_20_or_21
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Import :** le GLB peut être régénéré et ne reçoit pas les changements de séquence.
- **Dérivé :** la scène personnage conserve les personnalisations d’intégration.
- **Séquence :** les offsets narratifs restent locaux au pilote.
- **Remontée :** un défaut permanent est corrigé dans l’animation ou le retargeting.
## 33. Configurer les `Camera3D`
Une seule `Camera3D` est active par `Viewport`. Chaque caméra de plan possède projection, FOV, plans de coupe et transformation propres ; son nom reste lié à l’identifiant du plan.
`current` sélectionne la caméra active. Le changement doit être effectué à un instant explicite de la timeline ou par le directeur, sans laisser plusieurs scripts se disputer la propriété.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

cinematic_cameras:
  viewport_rule: one_current_camera
  nodes:
    CAM_SH010: {projection: perspective, fov: candidate}
    CAM_SH020: {projection: perspective, fov: candidate}
    CAM_SH030: {projection: perspective, fov: candidate}
    CAM_SH040: {projection: perspective, fov: candidate}
    CAM_SH050: {projection: perspective, fov: candidate}
  activation_property: Camera3D.current
  ownership: cinematic_director_or_timeline_not_both
  gameplay_camera_restored_on_exit: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Viewport :** une seule vue cinématique rend l’image à un instant donné.
- **Propriétés :** projection et FOV sont enregistrés par plan.
- **Activation :** `current` est un booléen qui sélectionne la caméra.
- **Autorité :** un seul mécanisme contrôle les coupes.
- **Sortie :** la caméra gameplay redevient active dans tous les chemins de fin.
## 34. Changer de caméra sans ambiguïté
Le directeur peut centraliser la sélection des caméras et refuser un identifiant absent. La fonction suivante illustre une table typée de `Camera3D` et un retour booléen.
Elle désactive les caméras connues avant d’activer la cible. Le résultat ne valide pas le cadrage ; il indique seulement que la caméra demandée existe et a été sélectionnée.
> **[VSC] Visual Studio Code — Exemple pour `res://cinematics/shared/cinematic_camera_router.gd`.**
```gdscript

class_name CinematicCameraRouter
extends Node

@export var camera_paths: Dictionary[StringName, NodePath] = {}
var _cameras: Dictionary[StringName, Camera3D] = {}

func _ready() -> void:
    for camera_id: StringName in camera_paths:
        var camera := get_node_or_null(camera_paths[camera_id]) as Camera3D
        if camera != null:
            _cameras[camera_id] = camera

func select_camera(camera_id: StringName) -> bool:
    var target := _cameras.get(camera_id) as Camera3D
    if target == null:
        push_warning("Caméra cinématique absente : %s" % camera_id)
        return false

    for camera: Camera3D in _cameras.values():
        camera.current = false

    target.current = true
    return true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Classe :** le nœud route les identifiants sans déplacer les caméras.
- **Paramètre exporté :** `Dictionary[StringName, NodePath]` relie un identifiant stable à un chemin éditable.
- **Résolution :** `get_node_or_null` peut renvoyer `null`; le cast `as Camera3D` protège le type.
- **Sélection :** `select_camera` reçoit un `StringName` et renvoie `bool`.
- **Effets :** les caméras connues passent à `current = false`, puis la cible à `true`.
- **Limite :** un retour `true` ne prouve ni composition ni continuité.
## 35. Timeline avec `AnimationPlayer`
`AnimationPlayer` lit des ressources `Animation` composées de pistes. La timeline principale peut animer transformations de caméra, propriétés visuelles, activation de placeholders et appels limités.
La durée de l’animation principale correspond à l’animatique approuvée. Les animations de personnage restent dans leurs bibliothèques et sont déclenchées ou synchronisées sans être copiées dans une piste monolithique.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

timeline:
  player: Timeline/AnimationPlayer
  animation: main_sequence
  length_s: derived_from_animatic
  tracks:
    - camera_transforms
    - camera_current_flags_or_router_calls
    - staging_node_transforms
    - character_animation_requests
    - placeholder_audio
    - light_properties
    - vfx_placeholder_properties
    - review_markers
  gameplay_mutations: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Lecteur :** l’`AnimationPlayer` conserve et lit les ressources `Animation`.
- **Durée :** la longueur découle du montage validé.
- **Pistes :** chaque famille possède une responsabilité visible.
- **Animation personnage :** la timeline demande une lecture à la bibliothèque propriétaire.
- **Interdit :** inventaire, quête, sauvegarde ou combat ne sont jamais modifiés par la timeline.
## 36. Types de pistes et effets de bord
Une piste de valeur anime une propriété ; une piste de transformation anime un `Node3D` ; une piste audio déclenche un flux ; une piste de méthode appelle une fonction. Le choix détermine les effets de bord et la capacité de prévisualisation.
Les appels de méthode sont limités à des adaptateurs cinématiques idempotents ou à des demandes visuelles. Une piste éditoriale ne doit pas contenir un appel métier caché.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

track_policy:
  transform_tracks:
    allowed: [Camera3D, staging_pivots, cinematic_props]
  value_tracks:
    allowed: [light_energy, placeholder_visibility, blend_weights]
  audio_tracks:
    allowed: [placeholder_or_approved_streams]
  method_tracks:
    allowed:
      - select_camera
      - request_visual_animation
      - emit_review_marker
    forbidden:
      - grant_item
      - complete_quest
      - apply_damage
      - write_save
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Transformations :** les nœuds de mise en scène sont animés sans modifier leurs sources.
- **Valeurs :** énergie, visibilité et poids restent des propriétés visuelles.
- **Audio :** les flux temporaires ou approuvés sont distingués par provenance.
- **Méthodes :** les fonctions autorisées sont limitées et testables.
- **Autorité :** les mutations métier demeurent hors de l’`AnimationPlayer`.
## 37. Piloter la lecture et recevoir la fin
Le directeur lance une animation nommée et écoute `animation_finished`. Le signal reçoit le `StringName` de l’animation terminée, ce qui permet d’ignorer une animation secondaire.
Le directeur renvoie `false` lorsqu’une dépendance manque ou qu’une autre séquence est active. Cette décision explicite évite les lectures concurrentes.
> **[VSC] Visual Studio Code — Exemple pour `res://cinematics/shared/cinematic_director.gd`.**
```gdscript

class_name CinematicDirector
extends Node

signal sequence_started(sequence_id: StringName)
signal sequence_finished(sequence_id: StringName, reason: StringName)

@export var sequence_id: StringName
@export var timeline_path: NodePath
@onready var _timeline := get_node_or_null(timeline_path) as AnimationPlayer

var _active := false

func _ready() -> void:
    if _timeline != null:
        _timeline.animation_finished.connect(_on_animation_finished)

func start_sequence() -> bool:
    if _active or _timeline == null:
        return false
    if not _timeline.has_animation(&"main_sequence"):
        return false

    _active = true
    sequence_started.emit(sequence_id)
    _timeline.play(&"main_sequence")
    return true

func _on_animation_finished(animation_name: StringName) -> void:
    if not _active or animation_name != &"main_sequence":
        return
    _finish(&"completed")

func _finish(reason: StringName) -> void:
    _active = false
    sequence_finished.emit(sequence_id, reason)
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Signaux :** le démarrage et la fin transportent l’identifiant et la raison.
- **Dépendance :** `timeline_path` est résolu en `AnimationPlayer` et peut produire `null`.
- **Retour :** `start_sequence() -> bool` distingue démarrage et refus contrôlé.
- **Méthodes :** `has_animation`, `play` et `connect` interrogent, lancent et relient la timeline.
- **Condition :** `animation_name != &"main_sequence"` ignore les autres fins.
- **Effets :** la classe modifie son drapeau et émet des signaux, sans appliquer de conséquence gameplay.
## 38. Synchroniser les animations de personnage
La timeline cinématique demande des animations existantes par identifiant stable. Elle peut ajuster l’instant de départ ou le poids visuel, mais toute modification de contact, root motion ou retargeting remonte aux chapitres 20 et 21.
Le raccord d’entrée choisit une pose compatible avec l’état gameplay précédent ; le raccord de sortie prépare une pose compatible avec la reprise. Ces deux transitions sont testées dans les deux sens lorsque la séquence peut être rejouée.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

character_sync:
  actor: AST-CHAR-SCOUT-001
  library: res://assets/animations/scout_mocap.tres
  requested_animation: loco_walk_crouch_radio_stand_v1
  phase_markers:
    enter_frame: walk_approach
    radio_contact: radio_contact
    reveal_reaction: head_raise
    exit_pose: neutral_ready
  root_motion_authority: gameplay_adapter
  retiming_requires_animation_review: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Bibliothèque :** la séquence consomme une animation versionnée.
- **Phases :** les marqueurs relient geste, plans et sons.
- **Sortie :** la pose neutre prépare la restitution du contrôle.
- **Autorité :** le mouvement global reste offert au système de déplacement.
- **Retiming :** une modification de vitesse exige une nouvelle revue animation.
## 39. Synchroniser dialogue et signal radio
Le chapitre peut placer un son temporaire ou approuvé afin de vérifier la compréhension du beat. Le montage final, le loudness, la spatialisation et les droits de voix restent au chapitre 26.
Les marqueurs de début, mot-clé et fin sont exprimés en secondes. Une version de dialogue différente invalide les marqueurs associés et déclenche une nouvelle revue.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

dialogue_sync:
  cue_id: AST-AUDIO-CUE-RADIO-SIGNAL-001
  source_status: placeholder
  stream_path: res://cinematics/placeholders/radio_signal_placeholder.ogg
  start_time_s: candidate
  keyword_marker_s: candidate
  end_time_s: candidate
  spatial_source: radio_prop_candidate
  final_mix_owner: chapter_26
  lip_sync_owner: chapter_27
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Cue :** l’identifiant reste stable lorsque le fichier temporaire est remplacé.
- **Statut :** `placeholder` interdit de traiter le son comme une livraison finale.
- **Temps :** les trois instants structurent le montage et la réaction.
- **Espace :** la radio est une source candidate à valider.
- **Frontières :** mix et synchronisation labiale restent dans leurs chapitres.
## 40. Synchroniser lumière et exposition
La lumière peut porter une révélation, guider le regard ou séparer les plans. La timeline anime uniquement des propriétés approuvées de nœuds cinématiques ou d’instances dérivées.
Une variation d’exposition globale peut modifier tous les plans et masquer des matériaux incorrects. Le pilote préfère une source lumineuse identifiée et compare avant/après.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

lighting_cue:
  cue_id: AST-CINE-LIGHT-CUE-RELAY-001
  beat: B05
  light_node: World/RelayOutpostInstance/DistantSignalLight
  animated_properties:
    visible: [false, true]
    light_energy: [candidate_low, candidate_reveal]
  exposure_override: none_default
  before_after_capture: required
  final_lookdev_owner: chapter_16_and_environment_source
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Cue :** la lumière change à un beat déterminé.
- **Propriétés :** visibilité et énergie restent séparées.
- **Exposition :** aucun correctif global n’est activé par défaut.
- **Comparaison :** les captures vérifient l’information et le matériau.
- **Frontière :** le lookdev permanent remonte aux sources concernées.
## 41. Synchroniser des VFX placeholders
Une particule ou simulation temporaire peut indiquer l’emplacement et la durée d’un futur effet. Son statut, son propriétaire et son remplacement attendu sont visibles dans le manifeste.
Le chapitre 23 décidera technologie, budgets, pooling et qualité. La cinématique ne doit pas concevoir un VFX final dans une piste cachée.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

vfx_cue:
  cue_id: AST-CINE-VFX-CUE-DUST-001
  placeholder_scene: res://cinematics/placeholders/dust_beam_placeholder.tscn
  beat_in: B01
  beat_out: B06
  animated_properties: [visible, intensity_candidate]
  final_asset_id: pending_chapter_23
  gameplay_authority: false
  replacement_required_before_final_acceptance: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Placeholder :** la scène temporaire est isolée dans un dossier explicite.
- **Bornes :** l’effet possède une entrée et une sortie liées aux beats.
- **Propriétés :** seules des valeurs visuelles candidates sont animées.
- **Remplacement :** la porte finale bloque tant que l’asset du chapitre 23 manque.
- **Autorité :** l’effet ne déclenche aucune règle gameplay.
## 42. Marqueurs et événements de revue
Des marqueurs non métier peuvent faciliter la lecture des logs ou des captures : début de plan, contact radio, révélation, demande de sortie. Ils décrivent la timeline et ne changent pas la partie.
Les identifiants sont stables et ordonnés. Une capture de revue indique le marqueur le plus proche afin de retrouver rapidement l’instant.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

review_markers:
  - {id: CINE_MARK_SH010_IN, kind: shot_start}
  - {id: CINE_MARK_SH020_IN, kind: shot_start}
  - {id: CINE_MARK_RADIO_CONTACT, kind: visual_contact}
  - {id: CINE_MARK_SIGNAL_KEYWORD, kind: audio_reference}
  - {id: CINE_MARK_LIGHT_REVEAL, kind: visual_reveal}
  - {id: CINE_MARK_GAMEPLAY_RETURN, kind: integration_request}
  gameplay_mutation: none
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Plan :** les marqueurs de début relient timeline et liste de plans.
- **Contact :** l’instant permet de comparer animation et gros plan.
- **Audio :** le mot-clé reste une référence de synchronisation.
- **Sortie :** la demande d’intégration est consommée par un système externe.
- **Invariance :** aucun marqueur n’applique directement une conséquence.
## 43. Suspendre les entrées de gameplay
Le directeur ne lit pas `Input` pour décider seul de désactiver le joueur. Il émet une demande à l’orchestrateur applicatif, qui connaît le `PlayerController` et peut appeler son contrat `set_gameplay_enabled(value)` établi dans le Livre II.
La suspension doit être symétrique : tout chemin de sortie réactive les entrées ou restaure l’état antérieur. Une exception pendant la séquence ne doit pas laisser le jeu bloqué.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

gameplay_handoff:
  start_request:
    set_gameplay_enabled: false
    capture_previous_input_state: required
    gameplay_camera_current: false
    cinematic_camera_current: true
  exit_request:
    restore_previous_input_state: true
    gameplay_camera_current: true
    cinematic_camera_current: false
  authority: application_orchestrator
  direct_input_map_mutation: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Entrée :** l’état précédent est capturé avant la suspension.
- **Caméras :** la vue gameplay et la vue cinématique s’échangent explicitement.
- **Sortie :** la restauration utilise l’état mémorisé plutôt qu’une hypothèse.
- **Autorité :** l’orchestrateur possède le contrôleur et la caméra gameplay.
- **Interdit :** la séquence ne modifie pas les liaisons de l’Input Map.
## 44. Transition d’entrée depuis le gameplay
L’entrée doit éviter un saut spatial incompréhensible. Le personnage, la caméra et l’état gameplay sont figés ou adaptés selon un contrat visible, puis le premier plan part d’une géographie compatible.
Un fondu peut masquer un chargement, mais il ne résout pas une incohérence de position. La position d’entrée, l’orientation et la caméra précédente sont enregistrées pour le diagnostic.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

entry_transition:
  trigger: authoritative_story_system
  player_state_snapshot: required
  player_anchor: AST-CINE-SR-MARK-ENTRY
  camera_match:
    source: gameplay_camera
    destination: CAM_SH010
    transform_compatibility_review: required
  loading_mask: optional_fade
  sequence_start_after_dependencies_ready: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Déclencheur :** le système narratif autoritaire demande la séquence.
- **Snapshot :** l’état utile à la restauration est conservé.
- **Ancre :** la position d’entrée appartient au staging.
- **Caméra :** le raccord est revu entre deux transformations réelles.
- **Chargement :** la timeline commence seulement lorsque les dépendances sont prêtes.
## 45. Transition de sortie vers le gameplay
La sortie remet le personnage dans un état autorisé, sélectionne la caméra gameplay et restitue les entrées. Le dernier plan prépare l’orientation du joueur et le nouvel objectif sans imposer la logique de quête.
Le directeur émet une raison de fin : terminé, sauté, annulé ou interrompu. L’orchestrateur décide ensuite quelles conséquences autoritaires sont permises.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

exit_transition:
  end_pose: neutral_ready
  player_anchor: AST-CINE-SR-MARK-EXIT
  gameplay_camera_match: over_shoulder_toward_distant_light
  reasons:
    completed: normal_end
    skipped: user_request
    cancelled: dependency_or_scene_exit
    interrupted: authoritative_system
  consequence_owner: narrative_application_service
  cinematic_director_applies_consequences: false
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Pose :** la bibliothèque d’animation fournit un état de reprise.
- **Ancre :** la sortie possède une position et une orientation contrôlées.
- **Raisons :** les chemins de fin sont distingués pour le diagnostic.
- **Conséquences :** un service applicatif consomme la raison.
- **Frontière :** le directeur ne complète ni quête ni objectif.
## 46. Saut, annulation et état final
Une séquence sautée doit produire un état final cohérent sans exécuter aveuglément tous les appels intermédiaires. Les effets purement visuels peuvent être arrêtés ; les conséquences métier sont appliquées une seule fois par le système autoritaire.
Le saut est disponible selon la politique du projet et doit rester accessible au clavier comme à la manette. Une confirmation peut être nécessaire pour une séquence non rejouable.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

skip_policy:
  skippable: true_candidate
  input_action: cinematic_skip
  hold_duration_s: candidate
  confirmation: evaluate
  on_skip:
    - stop_timeline
    - clear_cinematic_placeholders
    - apply_visual_end_pose_if_safe
    - request_authoritative_resolution_once
    - restore_gameplay_camera_and_input
  replay_availability: pending_design
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Action :** le nom logique permet remappage et plusieurs périphériques.
- **Durée :** le maintien éventuel reste à tester pour éviter les sauts accidentels.
- **Nettoyage :** les placeholders cinématiques sont stoppés explicitement.
- **Résolution :** le système autoritaire reçoit une demande idempotente.
- **Restauration :** caméra et entrées sont restituées même lors du saut.
## 47. Arrêter la timeline sans dupliquer les conséquences
La fonction suivante illustre un saut contrôlé. Elle vérifie l’état actif, arrête l’`AnimationPlayer`, puis termine avec une raison stable. Elle ne simule pas les pistes manquées.
L’appelant connecté à `sequence_finished` applique au plus une fois la résolution métier. Le drapeau `_active` rend les appels répétés inoffensifs.
> **[VSC] Visual Studio Code — Ajouter cet exemple au `CinematicDirector` documentaire.**
```gdscript

func skip_sequence() -> bool:
    if not _active or _timeline == null:
        return false

    _timeline.stop()
    _finish(&"skipped")
    return true

func cancel_sequence(reason: StringName = &"cancelled") -> bool:
    if not _active:
        return false

    if _timeline != null:
        _timeline.stop()
    _finish(reason)
    return true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Retours :** les deux fonctions renvoient `bool` pour distinguer action et refus.
- **Garde :** `not _active` empêche une seconde fin de séquence.
- **Arrêt :** `stop()` interrompt la lecture sans appeler les pistes futures.
- **Raison :** un `StringName` stable décrit le chemin de sortie.
- **Effets :** `_finish` émet le signal unique ; aucune conséquence métier n’est exécutée ici.
- **Valeur par défaut :** `cancel_sequence` utilise `&"cancelled"` lorsque l’appelant n’indique rien.
## 48. Interruption par un système autoritaire
Un combat, une déconnexion, un changement de scène ou un état critique peut interrompre une cinématique. La politique définit les événements qui ont priorité et le point de reprise éventuel.
L’interruption ne doit pas dépendre d’un nœud VFX ou audio. Un service applicatif demande l’annulation, puis restaure ou remplace les systèmes selon le nouvel état.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

interruption_policy:
  authoritative_interrupts:
    - scene_unload
    - player_invalidated
    - critical_game_state
  non_authoritative_sources:
    - vfx_completion
    - audio_placeholder_end
    - camera_track_end
  resume:
    allowed: evaluate_per_sequence
    checkpoint_markers: [B03, B05]
  default: cancel_and_restore
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Priorité :** seuls des événements applicatifs nommés interrompent la séquence.
- **Exclusion :** la fin d’un effet ou d’un son ne décide pas de la partie.
- **Reprise :** les checkpoints éventuels correspondent à des beats stables.
- **Défaut :** annuler et restaurer reste plus sûr qu’une reprise implicite.
## 49. Chargement et dépendances prêtes
Une cinématique ne commence pas tant que ses scènes, animations et flux nécessaires ne sont pas disponibles. L’écran de transition ou le gameplay précédent reste responsable de l’attente.
Le directeur reçoit un lot déjà prêt ou un résultat de chargement. Il ne lance pas des chargements synchrones lourds au premier instant de la timeline.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

load_contract:
  required_resources:
    - scout_scene
    - relay_environment
    - radio_prop
    - animation_library
    - main_timeline
  optional_resources:
    - placeholder_audio
    - placeholder_vfx
  start_when: all_required_ready
  optional_missing_policy: labeled_fallback_or_block_by_review
  synchronous_heavy_load_on_first_frame: forbidden
  load_failure_result: controlled_refusal
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Obligatoire :** la séquence refuse une scène ou animation absente.
- **Optionnel :** un fallback n’est utilisé que s’il est prévu et visible.
- **Départ :** la timeline commence après la porte de disponibilité.
- **Performance :** aucun chargement lourd n’est caché dans une coupe.
- **Refus :** l’échec remonte comme résultat contrôlé.
## 50. Tester les chemins de ressources
Une validation statique peut charger les chemins déclarés dans un manifeste ou utiliser `ResourceLoader.exists`. Elle détecte les fautes de chemin avant le test visuel.
Le contrôle ne prouve pas que la ressource possède la bonne version, le bon contenu ou les droits attendus. Ces dimensions restent dans les manifestes et revues.
> **[VSC] Visual Studio Code — Exemple pour `res://cinematics/shared/cinematic_dependency_validator.gd`.**
```gdscript

class_name CinematicDependencyValidator
extends RefCounted

static func validate_paths(
    dependencies: Dictionary[StringName, String]
) -> PackedStringArray:
    var diagnostics := PackedStringArray()

    for dependency_id: StringName in dependencies:
        var path: String = dependencies[dependency_id]
        if path.is_empty():
            diagnostics.append("DEPENDENCY_PATH_EMPTY:%s" % dependency_id)
            continue
        if not ResourceLoader.exists(path):
            diagnostics.append("DEPENDENCY_MISSING:%s:%s" % [dependency_id, path])

    return diagnostics
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Classe :** `RefCounted` suffit pour une validation sans nœud de scène.
- **Paramètre :** le dictionnaire relie `StringName` et chemin `String`.
- **Méthodes :** `is_empty` vérifie la chaîne et `ResourceLoader.exists` l’existence connue.
- **Opérateurs :** `not` inverse le booléen et `in` itère les clés.
- **Retour :** un `PackedStringArray` vide confirme seulement les chemins.
- **Effets :** aucune ressource n’est instanciée ou modifiée.
## 51. Versions de revue et commentaires
Une revue porte sur une version immuable : storyboard, animatique, blocking ou build. Chaque commentaire nomme plan, instant, catégorie, sévérité, décision et propriétaire.
Les commentaires contradictoires sont résolus par l’intention dramatique et la responsabilité du domaine. Modifier directement la version revue sans créer une nouvelle version détruit la traçabilité.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

review_comment:
  review_id: AST-CINE-SR-REV-0.3.0
  shot_id: AST-CINE-SR-SH030
  time_s: candidate
  category: continuity
  severity: blocking
  observation: radio_contact_partially_occluded
  requested_change: raise_camera_and_preserve_screen_direction
  owner: layout_artist
  decision: open
  resolved_in: pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Version :** le commentaire reste attaché au rendu examiné.
- **Localisation :** plan et temps évitent une note vague.
- **Catégorie :** continuité, narration, caméra, animation, son et technique sont distingués.
- **Propriétaire :** une personne ou un rôle prend la correction.
- **Résolution :** la nouvelle version est enregistrée sans réécrire l’historique.
## 52. Procédure de reprise après commentaire
Une reprise commence par reproduire l’observation sur la version citée. L’auteur corrige la source propriétaire, régénère les dérivés, puis répond avec une preuve de comparaison.
Une correction de caméra ne doit pas masquer un défaut d’animation ; une correction de son ne doit pas remplacer une information visuelle obligatoire. Les demandes croisées sont réassignées.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

revision_flow:
  - reproduce_on_review_version
  - identify_owning_source
  - classify_scope_and_dependencies
  - edit_source_not_render
  - regenerate_animatic_or_godot_capture
  - compare_before_after
  - update_shot_list_and_comment
  - request_re_review
  rejection_if:
    - wrong_source_modified
    - dependency_status_hidden
    - evidence_missing
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Reproduction :** la correction part du défaut réellement observé.
- **Propriété :** la source responsable est choisie avant l’édition.
- **Régénération :** les captures sont dérivées de la nouvelle source.
- **Comparaison :** avant/après rend la décision vérifiable.
- **Refus :** une correction sans preuve ou au mauvais niveau ne ferme pas le commentaire.
## 53. Rendus de revue et captures
Un rendu de revue peut être une capture de l’éditeur ou du build. Il porte version, commit, paramètres graphiques, résolution, ratio, caméra et durée.
La compression d’une plateforme vidéo peut masquer banding, saccades ou détails. La preuve conserve au moins une source locale contrôlée et, si nécessaire, des images fixes.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

review_capture:
  sequence_version: 0.3.0
  commit: pending
  source: godot_build_candidate
  resolution: [1920, 1080]
  aspect_ratio: "16:9"
  renderer: Forward+
  quality_profile: reference_candidate
  frame_rate_capture: measured
  camera_sequence: main_sequence
  local_master_retained: true
  external_transcode_not_authoritative: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Version :** la vidéo correspond à un état exact de la séquence.
- **Environnement :** résolution, renderer et profil rendent la comparaison interprétable.
- **Mesure :** le framerate est observé plutôt que supposé.
- **Source :** le master local reste la preuve de référence.
- **Transcode :** une copie externe ne devient pas l’autorité visuelle.
## 54. Ratios d’image et zones sûres
Un cadrage validé en 16:9 peut perdre un sujet ou un sous-titre sur un autre ratio. Les plans sont inspectés dans les formats ciblés, avec les zones réservées à l’interface et aux sous-titres.
Le chapitre ne construit pas l’UI ; il fournit des marges de composition et des captures aux chapitres 24 et 25. La caméra ne doit pas déplacer silencieusement le sujet pour chaque ratio sans profil.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

aspect_ratio_matrix:
  profiles:
    - {ratio: "16:9", status: required}
    - {ratio: "16:10", status: evaluate}
    - {ratio: "21:9", status: evaluate}
  safe_areas:
    subtitles: reserved_bottom_band
    critical_subjects: central_protected_region
    future_ui: chapter_24_contract
  strategies:
    - expand_horizontal_when_safe
    - adjust_camera_per_profile_if_approved
  automatic_unreviewed_crop: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Profils :** chaque ratio reçoit un statut et une capture.
- **Sous-titres :** la bande inférieure reste libre des détails indispensables.
- **Sujets :** les informations critiques demeurent dans une zone protégée.
- **Stratégies :** extension et variante de caméra sont des choix explicites.
- **Interdit :** un recadrage automatique non revu peut couper l’action.
## 55. Confort visuel et réduction du mouvement
Les coupes rapides, vibrations, accélérations, roulis et FOV extrêmes peuvent provoquer inconfort ou perte de repères. Le projet prévoit une variante réduite lorsque l’intention le permet.
Une option de confort ne doit pas supprimer une information obligatoire. Elle remplace ou atténue le mouvement tout en conservant ordre des beats, cadrage utile et durée compréhensible.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

motion_accessibility:
  settings:
    reduce_camera_shake: supported
    reduce_camera_acceleration: evaluate
    disable_dutch_angle: supported_if_used
    comfort_fov_profile: evaluate
  preserved:
    - shot_information
    - beat_order
    - radio_contact_visibility
    - gameplay_return_clarity
  alternate_tracks: candidate
  final_owner: chapter_25_with_chapter_22_inputs
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Réglages :** chaque source d’inconfort peut être traitée séparément.
- **Conservation :** la variante garde les informations narratives obligatoires.
- **Pistes :** une timeline alternative peut remplacer la couche de mouvement.
- **Frontière :** le chapitre 25 consolidera les profils d’accessibilité.
## 56. Sous-titres et lisibilité du dialogue
Le chapitre réserve temps et espace aux sous-titres, mais la production du système UI et ses options appartient aux chapitres 24 et 25. Le cue audio fournit un identifiant et des bornes nécessaires.
Le sous-titre ne doit pas révéler un locuteur ou une information volontairement inconnue. Son contenu, sa localisation et son attribution sont validés avec l’intention narrative.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

subtitle_contract:
  cue_id: AST-AUDIO-CUE-RADIO-SIGNAL-001
  start_time_s: candidate
  end_time_s: candidate
  speaker_label: unknown_signal_candidate
  text_key: cine.scout_relay.radio_signal_01
  safe_area_required: true
  localization_owner: future_localization_pipeline
  ui_owner: chapters_24_25
  timing_revalidated_after_audio_change: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Corrélation :** le même cue relie son, texte et timeline.
- **Bornes :** début et fin restent en secondes.
- **Attribution :** le label respecte l’ambiguïté voulue.
- **Clé :** le texte localisable reste hors de la scène.
- **Revalidation :** une nouvelle voix invalide le timing antérieur.
## 57. Performance et budget de séquence
Le coût dépend des assets visibles, lumières, ombres, particules, animations, flux audio, post-traitements et chargements. Le nombre de plans n’est pas une mesure suffisante.
La campagne future compare la séquence désactivée, la scène bloquée et la version complète sur le matériel de référence. Chaque variation change une famille principale à la fois.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

performance_campaign:
  hardware: reference_machine
  variants:
    - environment_and_character_idle
    - cinematic_blocking_without_placeholders
    - cinematic_with_audio_placeholder
    - cinematic_with_light_cues
    - cinematic_with_vfx_placeholder
    - final_candidate
  measures:
    - cpu_frame_time_ms
    - gpu_frame_time_ms
    - memory_bytes
    - loading_time_ms
    - shader_compilation_events
    - dropped_capture_frames
  results: pending_runtime
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Référence :** la même machine et le même build encadrent la comparaison.
- **Variantes :** les familles sont ajoutées progressivement.
- **Temps :** CPU et GPU sont enregistrés séparément.
- **Chargement :** mémoire, compilation et durée complètent le framerate.
- **Résultat :** aucune valeur n’est déclarée avant exécution.
## 58. Stabilité du build et dépendances perdues
Une séquence peut fonctionner dans l’éditeur mais échouer dans un export si un chemin, un import ou une ressource dynamique manque. Le test final utilise un build candidat et reproduit entrée, lecture, saut et sortie.
Les logs sont conservés avec le commit et le profil d’export. Une capture visuelle ne remplace pas l’absence d’erreurs ou d’avertissements bloquants.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

build_test:
  commit: pending
  export_profile: reference_desktop_candidate
  scenarios:
    - normal_entry_and_completion
    - skip_at_each_allowed_checkpoint
    - cancel_on_scene_unload
    - missing_optional_placeholder
    - repeated_playback
  verify:
    - no_missing_required_resource
    - one_active_camera
    - gameplay_input_restored
    - authoritative_resolution_once
    - no_orphan_audio_or_vfx
  status: pending_runtime
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Build :** le commit et le profil identifient le binaire.
- **Scénarios :** fin, saut, annulation et répétition sont distincts.
- **Caméra :** une seule vue doit rester active.
- **Autorité :** la conséquence est demandée exactement une fois.
- **Nettoyage :** aucun son ou effet cinématique ne survit à la sortie.
## 59. Journalisation et corrélation
Les logs de production utilisent séquence, version, plan et raison de fin. Ils évitent les noms de personnes, chemins privés ou textes de dialogue sensibles.
Le runtime futur journalisera les transitions importantes, pas chaque image de caméra. Une trace concise suffit à reproduire un démarrage refusé ou une restauration manquante.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

cinematic_log_fields:
  sequence_id: required
  sequence_version: required
  playback_instance_id: runtime_generated
  event:
    - start_requested
    - start_refused
    - shot_marker
    - skip_requested
    - finished
  finish_reason: optional_by_event
  commit: build_metadata
  personal_data: forbidden
  per_frame_camera_log: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Corrélation :** une instance distingue deux lectures de la même séquence.
- **Événements :** les transitions significatives suffisent au diagnostic.
- **Raison :** elle apparaît seulement pour les événements concernés.
- **Sécurité :** aucune donnée personnelle n’est nécessaire.
- **Volume :** les transformations de chaque image ne sont pas journalisées.
## 60. Automatisation bornée
L’automatisation peut vérifier identifiants, chemins, ordre, durées positives, caméras référencées et statuts. Elle peut générer un rapport ou une grille de captures.
Elle ne peut pas déclarer seule que la narration est claire, le rythme maîtrisé ou le mouvement confortable. Les décisions artistiques et narratives restent humaines.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

automation_contract:
  allowed:
    - validate_shot_schema
    - check_resource_paths
    - compare_timeline_length_with_animatic
    - detect_duplicate_shot_ids
    - generate_review_manifest
    - request_capture_matrix
  forbidden_without_human_review:
    - approve_narrative_clarity
    - approve_composition
    - approve_rhythm
    - approve_motion_comfort
    - publish_sequence
  output: staging_or_report
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Schéma :** les règles automatiques portent sur des données observables.
- **Comparaison :** une différence de durée devient un diagnostic, pas un verdict.
- **Capture :** l’outil peut demander une matrice sans interpréter les images.
- **Décision :** narration, composition, rythme et confort restent humains.
- **Publication :** le script ne promeut jamais seul la séquence.
## 61. Modes Solo et Studio
### Mode Solo
Limiter le pilote à une séquence courte et à cinq ou sept plans réellement nécessaires. Réutiliser les animations, décors et systèmes existants ; valider storyboard et animatique avant de détailler la timeline.
Séparer les passes dans le temps : écriture, storyboard, montage, caméra, synchronisation, puis revue dans le build. Une personne seule conserve ainsi une seconde lecture et évite de corriger indéfiniment le même plan.
### Mode Studio
Séparer au minimum intention narrative, layout caméra, animation, lumière, audio, VFX, intégration et approbation. Une petite équipe peut cumuler plusieurs rôles, mais chaque porte conserve un propriétaire et une décision.
| Domaine | Mode Solo | Mode Studio |
|---|---|---|
| portée | une séquence pilote | séquences planifiées par priorité |
| revue | passe différée et checklist | dailies et responsables de domaine |
| versions | registre unique | versions immuables et commentaires assignés |
| acceptation | décision personnelle différée | approbations narrative, artistique et technique |
## 62. Handoff entre disciplines
Le handoff contient sources, versions, dépendances, réserves et question précise. Un dossier de fichiers sans statut oblige le destinataire à deviner ce qui est approuvé.
Chaque domaine peut refuser le lot avec un code stable. Le refus ne supprime pas l’historique ; il indique la source à reprendre et la preuve attendue.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

handoff:
  sequence_id: AST-CINE-PILOT-SCOUT-RELAY-001
  source_version: 0.3.0
  from_role: layout
  to_role: animation
  included:
    - approved_animatic
    - shot_list
    - camera_scene
    - dependency_manifest
  reservations:
    - final_audio_missing
    - final_vfx_missing
  question: validate_contact_and_exit_pose
  decision: pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Version :** le destinataire reçoit un état immuable.
- **Contenu :** animatique, plans, caméras et dépendances voyagent ensemble.
- **Réserves :** les lots futurs restent visibles.
- **Question :** la revue attend une réponse précise.
- **Décision :** le statut reste en attente jusqu’au retour du domaine.
## 63. Livrables permanents
Le plan maître exige storyboard, animatique, scène Godot, liste de plans et versions de revue. Le chapitre ajoute les manifestes nécessaires à leur traçabilité sans transformer ces ajouts en nouveau périmètre artistique.
Chaque livrable possède identifiant, version, propriétaire, dépendances, statut et réserves. Les rendus restent des preuves dérivées.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

deliverables:
  - narrative_brief
  - storyboard
  - shot_list
  - approved_animatic
  - godot_cinematic_scene
  - animation_player_timeline
  - camera_setups
  - dependency_manifest
  - review_versions_and_comments
  - build_test_report
  - capture_matrix
  - acceptance_record
  - provenance_and_rights_status
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Plan maître :** les cinq livrables obligatoires restent centraux.
- **Timeline :** la scène et sa ressource de lecture sont distinguées.
- **Dépendances :** le manifeste empêche les pertes silencieuses.
- **Revues :** commentaires et captures relient décision et version.
- **Droits :** chaque asset consommé conserve son statut de provenance.
## 64. Porte d’acceptation
La séquence est acceptée lorsque la lecture narrative est claire, le rythme approuvé, les plans spatialement cohérents, les dépendances présentes et le passage entrée–sortie fonctionne dans le build.
Les portes narrative, artistique, technique et juridique sont indépendantes. Une belle image ne compense pas une ressource sans droits ; un build stable ne compense pas une révélation incompréhensible.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

acceptance_gate:
  narrative:
    required_information_readable: required
    ambiguity_intentional_only: required
    rhythm_approved: required
  visual:
    composition_and_continuity: required
    camera_motion_comfort: required
    animation_contacts_visible: required
  technical:
    dependencies_complete: required
    build_playback: required
    skip_cancel_and_return: required
    no_orphan_tracks: required
  legal:
    consumed_assets_traceable: required
    placeholder_status_visible: required
  decision: pending_materialization
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Narration :** les faits obligatoires et ambiguïtés sont testés séparément.
- **Visuel :** composition, continuité, confort et contacts reçoivent une revue.
- **Technique :** build, chemins de fin et nettoyage doivent réussir.
- **Juridique :** assets et placeholders conservent leur provenance.
- **Statut :** la décision reste en attente tant que le pilote n’existe pas.
## 65. Checklist de livraison
Avant publication, vérifier que toutes les sources et dépendances correspondent à la version approuvée, que les placeholders sont visibles dans les manifestes et que les chemins de sortie restaurent le gameplay.
La checklist accompagne le lot mais ne remplace pas les commentaires détaillés, les logs, les captures ni les approbations.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

release_checklist:
  - narrative_brief_and_beats_locked
  - storyboard_and_shot_list_aligned
  - animatic_duration_approved
  - camera_ids_and_setups_versioned
  - timeline_tracks_reviewed
  - imported_scenes_not_edited_directly
  - animation_audio_light_vfx_dependencies_traced
  - placeholders_explicit
  - entry_skip_cancel_exit_tested
  - gameplay_camera_and_input_restored
  - build_and_aspect_ratio_matrix_captured
  - runtime_reservations_recorded
  - rollback_sources_available
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Création :** brief, storyboard, plans et animatique forment un ensemble cohérent.
- **Caméras :** identifiants et setups permettent la reprise.
- **Dépendances :** animation, audio, lumière et VFX restent traçables.
- **Intégration :** tous les chemins de fin restituent la partie.
- **Preuves :** captures, réserves et sources de rollback accompagnent la décision.
## 66. Diagnostics et corrections
<!-- qa:error-correction-section -->
### 66.1 Ajouter un plan sans fonction narrative
**Symptôme ou risque :** la séquence s’allonge, mais personne ne peut expliquer ce que le nouveau plan apporte.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

shot:
  id: AST-CINE-SR-SH025
  purpose: looks_cool
  duration_s: 4.0
  dependency_cost: ignored
  status: approved
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le but `looks_cool` n’est ni testable ni relié à un beat. Le plan consomme durée, lumière, animation et revue sans information obligatoire.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

shot:
  id: AST-CINE-SR-SH025
  purpose: establish_radio_console_before_contact
  beat_in: B02
  beat_out: B03
  duration_s: candidate
  dependency_cost: reviewed
  status: storyboard
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Le plan corrigé nomme l’information, les bornes et le coût à examiner. Son statut reste en storyboard jusqu’à l’animatique.
### 66.2 Franchir l’axe sans préparation
**Symptôme ou risque :** le personnage semble changer brutalement de direction entre deux coupes.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

continuity:
  outgoing_camera_side: A
  incoming_camera_side: B
  neutral_shot: false
  visible_crossing: false
  screen_direction_review: skipped
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le changement de côté est invisible et aucune image ne rétablit l’espace. Le public peut interpréter le trajet comme un demi-tour.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

continuity:
  outgoing_camera_side: A
  incoming_camera_side: B
  crossing_method: neutral_axis_shot
  screen_direction_before: left_to_right
  screen_direction_after: reviewed
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Un plan sur l’axe rend la transition compréhensible et la direction écran est vérifiée avant et après.
### 66.3 Utiliser un FOV extrême pour résoudre le cadre
**Symptôme ou risque :** le décor paraît déformé et le raccord avec la caméra gameplay provoque un saut visuel.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

camera:
  fov: 140.0
  reason: fit_everything
  distortion_review: false
  gameplay_transition_review: false
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Une valeur extrême masque un problème de composition et modifie fortement la perspective. Aucun contrôle de confort ou de raccord n’est prévu.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

camera:
  fov: candidate_within_tested_profile
  composition: simplify_and_reposition
  distortion_review: required
  gameplay_transition_review: required
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La correction traite le placement et la hiérarchie, puis qualifie le FOV avec deux revues distinctes.
### 66.4 Éditer directement une scène importée
**Symptôme ou risque :** une réimportation du personnage supprime les offsets et pistes créés pour la cinématique.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

scene:
  source: scout_anim.glb
  direct_edits:
    - camera_offset
    - radio_pose_fix
    - material_override
  reimport_protection: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le GLB est un dérivé régénérable. Mélanger offsets de caméra, correction d’animation et matériaux rend la reprise impossible.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

scene:
  imported: scout_anim.glb
  derived: scout_animated.tscn
  cinematic_instance: scout_relay_sequence.tscn
  camera_offset_owner: staging
  radio_pose_fix_owner: animation_source
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La scène dérivée protège l’intégration, le staging conserve le cadrage et le défaut d’animation remonte à sa source.
### 66.5 Faire muter le gameplay depuis une piste de méthode
**Symptôme ou risque :** le saut de cinématique accorde deux fois un objet ou complète une quête dans un ordre différent.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

method_track:
  at_4_2_seconds: grant_item("relay_key")
  at_7_0_seconds: complete_quest("find_relay")
  skip_behavior: execute_remaining_methods
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Les effets métier sont cachés dans la lecture temporelle et dépendent du chemin parcouru. Le saut ou la répétition peut les dupliquer.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

method_track:
  at_4_2_seconds: emit_review_marker("radio_contact")
  at_7_0_seconds: request_visual_exit()
director:
  finish_signal: sequence_finished
application_service:
  resolve_consequence_once: true
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La timeline ne porte que des faits visuels ; un service autoritaire consomme une seule raison de fin et applique les conséquences de façon idempotente.
### 66.6 Désactiver les entrées sans restauration
**Symptôme ou risque :** après une fin, un saut ou une erreur, le joueur ne peut plus déplacer le personnage.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

start:
  player_controller_enabled: false
exit:
  player_controller_enabled: omitted
exception_path: not_handled
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** L’état précédent n’est pas mémorisé et les sorties alternatives ne sont pas couvertes. Une exception laisse la désactivation active.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

start:
  previous_input_state: captured
  request_gameplay_enabled: false
exit_paths: [completed, skipped, cancelled, interrupted]
restore_previous_input_state: required
finally_guard: enabled
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La restauration est fondée sur un snapshot et s’applique à tous les chemins, avec une garde finale.
### 66.7 Traiter un placeholder comme un asset final
**Symptôme ou risque :** la séquence est approuvée avec un son ou un VFX temporaire dont les droits et le coût sont inconnus.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

dependency:
  path: temp_signal.wav
  status: approved
  provenance: unknown
  replacement_required: false
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le nom temporaire, la provenance absente et le statut approuvé cachent une dépendance non qualifiée.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

dependency:
  cue_id: AST-AUDIO-CUE-RADIO-SIGNAL-001
  path: res://cinematics/placeholders/radio_signal_placeholder.ogg
  status: placeholder
  provenance: internal_temporary
  replacement_required_before_final_acceptance: true
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** L’identifiant, le dossier, le statut et la porte de remplacement rendent le caractère provisoire impossible à ignorer.
### 66.8 Lancer la séquence avant le chargement
**Symptôme ou risque :** la première coupe saccade ou une caméra montre brièvement des assets absents.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

start_sequence:
  preload_required: false
  begin_timeline_immediately: true
  missing_resource_policy: continue
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le premier instant de lecture déclenche des chargements et accepte des ressources obligatoires absentes. Le résultat dépend du cache de la machine.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

start_sequence:
  required_dependencies: validated
  begin_after_all_required_ready: true
  optional_missing_policy: labeled_fallback
  load_failure: controlled_refusal
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La porte de disponibilité précède la timeline et distingue dépendances obligatoires, options et refus.
### 66.9 Valider uniquement dans l’éditeur
**Symptôme ou risque :** la cinématique fonctionne dans la scène de test mais perd un chemin ou ne rend pas les entrées dans le build.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

validation:
  editor_preview: passed
  exported_build: not_tested
  skip_paths: not_tested
  repeated_playback: not_tested
  decision: final
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** L’éditeur ne reproduit pas nécessairement l’export, le chargement et tous les chemins de fin. La décision dépasse les observations.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

validation:
  editor_preview: reviewed
  exported_build: required
  paths: [completed, skipped, cancelled, interrupted]
  repeated_playback: required
  logs_and_captures: retained
  decision: pending_runtime
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La matrice exige le build, les sorties, la répétition et les preuves, puis conserve le statut en attente avant exécution.
### 66.10 Valider un seul ratio et ignorer le confort
**Symptôme ou risque :** le sujet est coupé en ultrawide et la vibration rend la séquence inconfortable pour certains joueurs.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml

review:
  aspect_ratios: ["16:9"]
  camera_shake: fixed
  subtitles_safe_area: ignored
  comfort_variant: none
  decision: universal
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Une seule géométrie d’écran et une couche de mouvement imposée ne prouvent pas une compatibilité générale. Les sous-titres peuvent masquer l’action.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml

review:
  aspect_ratios: ["16:9", "16:10", "21:9"]
  camera_shake: separate_disableable_layer
  subtitles_safe_area: reserved
  comfort_variant: evaluated
  decision: limited_to_tested_profiles
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La matrice couvre les profils ciblés, rend la vibration désactivable et limite explicitement la décision aux cas testés.
## 67. Références techniques officielles
Les références officielles suivantes encadrent la qualification technique. Elles seront relues lors d’une mise à jour de Godot ou des contrats de caméra du projet.
Les pages de classe décrivent les propriétés et méthodes ; elles ne fournissent pas une validation narrative, artistique ou de confort du pilote.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

official_references:
  camera_3d: https://docs.godotengine.org/en/stable/classes/class_camera3d.html
  animation_player: https://docs.godotengine.org/en/stable/classes/class_animationplayer.html
  animation_resource: https://docs.godotengine.org/en/stable/classes/class_animation.html
  path_3d: https://docs.godotengine.org/en/stable/classes/class_path3d.html
  path_follow_3d: https://docs.godotengine.org/en/stable/classes/class_pathfollow3d.html
  audio_stream_player: https://docs.godotengine.org/en/stable/classes/class_audiostreamplayer.html
  animation_tutorials: https://docs.godotengine.org/en/stable/tutorials/animation/index.html
  inherited_gameplay_camera_contract: Livre-II/CHAPITRE-06
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Caméra :** la classe couvre projection, FOV, plans de coupe et activation.
- **Timeline :** `AnimationPlayer` et `Animation` couvrent lecture et pistes.
- **Trajectoire :** `Path3D` et `PathFollow3D` couvrent courbe et progression.
- **Audio :** la classe est citée pour la synchronisation, pas pour le mix final.
- **Héritage :** le contrat caméra gameplay reste celui du Livre II.
## 68. Synthèse opérationnelle pour Project Asteria
`Project Asteria` retient `AST-CINE-PILOT-SCOUT-RELAY-001` comme séquence témoin. Son brief, ses beats, son storyboard, sa liste de plans, son animatique, ses caméras et sa timeline sont des sources versionnées distinctes. Les animations des chapitres 20 et 21, le décor, la radio et les placeholders audio/VFX restent des dépendances explicitement qualifiées.
La porte d’acceptation exige une lecture narrative claire, un rythme approuvé, des raccords cohérents, une activation caméra non ambiguë, des chemins de fin complets, une restitution certaine du gameplay et un test dans le build. Tant que les livrables ne sont pas matérialisés, Project Asteria conserve le statut `static-review` et ne revendique ni durée, ni confort, ni stabilité, ni coût runtime mesurés.
> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml

asteria_cinematic_decisions:
  sequence_id: AST-CINE-PILOT-SCOUT-RELAY-001
  brief_id: AST-CINE-SR-BRIEF-V1
  shot_list_id: AST-CINE-SR-SHOTS-V1
  animatic_id: AST-CINE-SR-ANIMATIC-V1
  timeline_animation: main_sequence
  camera_router: AST-CINE-SR-CAMERA-ROUTER-V1
  entry_anchor: AST-CINE-SR-MARK-ENTRY
  exit_anchor: AST-CINE-SR-MARK-EXIT
  canonical_chain: brief_to_storyboard_to_shot_list_to_animatic_to_godot_to_build_review
  consequence_authority: narrative_application_service
  acceptance: narrative_plus_visual_plus_technical_plus_legal
  materialization_status: not_started
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identifiants :** séquence, brief, plans, animatique, routeur et ancres deviennent les références permanentes.
- **Chaîne :** chaque dérivé peut être reconstruit depuis une source approuvée.
- **Autorité :** le service narratif applique les conséquences, jamais la timeline.
- **Porte :** les quatre domaines doivent réussir sans compensation mutuelle.
- **Réserves :** aucun storyboard, rendu, scène, build ou benchmark n’est déclaré produit.
