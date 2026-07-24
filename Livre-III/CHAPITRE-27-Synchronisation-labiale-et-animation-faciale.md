---
title: "Livre III — Chapitre 27 : Synchronisation labiale et animation faciale"
id: "DOC-L3-CH27"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 27
last-verified: "2026-07-24T23:50:00+02:00"
audit-status: "complete"
audit-date: "2026-07-24T23:50:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-27.md"
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

# Synchronisation labiale et animation faciale

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH27`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Une synchronisation labiale crédible ne consiste pas à ouvrir et fermer la bouche sur l’amplitude sonore. Elle transforme une voix approuvée, une transcription et un profil linguistique en événements temporels qui pilotent des formes faciales, des mouvements de mâchoire, le regard, les clignements et des gestes complémentaires.

Le chapitre définit la chaîne de données, les conventions d’auteur, les profils de qualité et les portes de validation. Il ne remplace ni la direction d’acteur, ni la production audio du chapitre 26, ni les décisions narratives et gameplay du Livre II.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: approved_voice_transcript_and_character_face_rig
  transformation: phoneme_timing_viseme_mapping_and_facial_performance
  output: versioned_timing_assets_animation_tracks_and_quality_profiles
  authority: presentation_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la voix, la transcription, le visage et le rig doivent déjà être identifiés et compatibles.
- **Transformation :** la chaîne convertit les unités linguistiques en poses et courbes temporelles révisables.
- **Sortie :** les timings et animations sont des dérivés versionnés qui peuvent être régénérés.
- **Autorité :** aucune piste faciale ne valide une quête, un dialogue ou un état métier.
- **Preuve :** aucun asset facial, alignement ou test runtime n’est déclaré matérialisé.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura distinguer graphèmes, phonèmes et visèmes, définir un jeu minimal de formes faciales, annoter ou extraire des timings, construire des courbes de coarticulation et intégrer le résultat dans Godot.

Il saura aussi préparer des profils par langue et par niveau de qualité, relier bouche, yeux, sourcils, tête et gestes sans suranimation, puis organiser des tests en gros plan, à distance et en foule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  linguistics: [grapheme, phoneme, allophone, viseme, silence]
  rigging: [blendshape, jaw_bone, eyelids, brows, corrective_shapes]
  timing: [manual_annotation, forced_alignment, review, coarticulation]
  performance: [gaze, blink, head_motion, gesture, emotion]
  integration: [animation_tracks, runtime_driver, language_profile, facial_lod]
  validation: [close_up, gameplay_distance, crowd, multiple_voices]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Linguistique :** les unités écrites, sonores et visuelles sont séparées avant tout mapping.
- **Rig :** les formes de bouche s’appuient sur une base neutre et des correctifs testables.
- **Timing :** l’automatisation produit un brouillon qui reste révisable par une personne.
- **Performance :** la bouche n’est qu’un sous-système du jeu d’acteur facial.
- **Validation :** la qualité est observée à plusieurs distances et sur plusieurs voix.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les fichiers, schémas et scripts montrés sont des contrats pédagogiques ; ils ne prouvent ni la qualité d’un rig, ni la précision d’un alignement, ni la stabilité d’une animation dans un build.

Les nombres proposés pour les durées, poids, distances ou fréquences sont des candidats à mesurer. Ils doivent être remplacés ou confirmés par une campagne sur les personnages, langues, plateformes et caméras réellement retenus.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  viseme_set_created: false
  face_rig_modified: false
  timings_generated: false
  timings_manually_reviewed: false
  godot_animation_created: false
  close_up_test_executed: false
  crowd_test_executed: false
  runtime_profile_recorded: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est relue sans annoncer une implémentation terminée.
- **Rig :** aucune forme, mâchoire ou correctif n’est déclaré créé dans Blender.
- **Timings :** aucun alignement automatique ou manuel n’est présenté comme exécuté.
- **Godot :** aucune scène, animation ou mesure de coût n’est revendiquée.
- **Publication :** le PDF du Livre III reste différé jusqu’à la clôture du Livre.

## 4. Frontières avec les chapitres voisins

Le chapitre 10 conserve l’anatomie et les formes du visage. Le chapitre 19 conserve l’architecture du rig et du skinning. Le chapitre 26 conserve les voix, le montage, les droits, les bus et le mix.

Le chapitre 27 possède le mapping phonème-visème, les timings, la coarticulation et la performance faciale. Le chapitre 28 consolidera les presets d’import et la réimportation sans redéfinir les conventions artistiques.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapter_10: face_anatomy_skin_eyes_hair_and_base_shapes
  chapter_19: rig_skinning_bones_and_deformation_contracts
  chapter_26: voice_source_editing_rights_mix_and_runtime_stream
  chapter_27: linguistic_mapping_timing_and_facial_performance
  chapter_28: import_reimport_and_integration_presets
  book_ii: narrative_and_gameplay_authority
  invariant: facial_animation_never_commits_domain_state
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Visage :** la géométrie et l’anatomie restent des dépendances amont.
- **Rig :** les os, blendshapes et correctifs doivent respecter un contrat déjà versionné.
- **Audio :** la voix approuvée est consommée sans réouvrir son montage ou ses droits.
- **Import :** les réglages répétitifs seront industrialisés au chapitre suivant.
- **Invariant :** la fin d’une animation ne décide jamais d’un résultat narratif.

## 5. Pilote facial de Project Asteria

Le pilote `AST-FACE-PILOT-RELAY-DIALOGUE-001` réutilise les deux lignes radio du pilote audio `AST-AUDIO-PILOT-RELAY-STORM-001`. Il cible un gros plan bref sur l’éclaireur, une réponse distante et une variante de foule simplifiée.

Ce périmètre permet d’évaluer voix, visèmes, regard, clignements, émotion, LOD et coût sans prétendre couvrir tous les personnages ou toutes les langues.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_face_pilot:
  id: AST-FACE-PILOT-RELAY-DIALOGUE-001
  audio_source: AST-AUDIO-PILOT-RELAY-STORM-001
  characters: [scout_close_up, remote_operator_mid_shot]
  languages: [fr_reference, en_candidate]
  quality_profiles: [hero_close_up, gameplay_mid, crowd_low]
  deliverables:
    - viseme_mapping
    - reviewed_timing_track
    - facial_animation_candidate
    - language_profiles
    - distance_test_plan
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** un dialogue court concentre les décisions sur un lot contrôlable.
- **Audio :** la voix est une dépendance identifiée et ne change pas silencieusement.
- **Langues :** le français est le profil de référence et l’anglais reste un candidat à qualifier.
- **Qualité :** les profils rapproché, gameplay et foule n’utilisent pas le même coût.
- **Réserve :** aucune animation ni prise n’est déclarée produite.

## 6. Graphème, phonème, allophone et visème

Un graphème appartient à l’écriture, un phonème distingue des unités sonores dans une langue, un allophone est une réalisation contextuelle et un visème regroupe des sons dont l’apparence labiale peut être similaire.

Le mapping doit donc partir de la langue et de la prononciation réelle, pas seulement des lettres du texte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
linguistic_units:
  grapheme: written_symbol_or_sequence
  phoneme: contrastive_sound_category_in_a_language
  allophone: contextual_realization
  viseme: visual_mouth_category
  silence: timed_non_speech_region
  rule: never_map_letters_directly_to_mouth_shapes
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Graphème :** la forme écrite n’indique pas toujours la prononciation.
- **Phonème :** la catégorie sonore dépend de la langue.
- **Visème :** plusieurs phonèmes peuvent partager une apparence proche.
- **Silence :** les pauses et respirations sont des événements à part entière.
- **Règle :** le texte seul ne suffit pas à animer la bouche.

## 7. Différences linguistiques et variantes de prononciation

Deux langues peuvent employer des inventaires sonores, des rythmes syllabiques et des contrastes labiaux différents. Une même langue varie aussi selon l’accent, le registre, le débit et le locuteur.

Un profil linguistique enregistre les conventions du projet sans prétendre normaliser toutes les prononciations possibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
language_profile:
  id: AST-FACE-LANG-FR-001
  locale: fr-FR
  pronunciation_dictionary: versioned_candidate
  phone_inventory: project_specific
  viseme_map: AST-FACE-VISEME-MAP-FR-001
  review_required_for: [proper_names, acronyms, dialectal_forms, shouting]
  fallback: manual_annotation
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le profil est versionné indépendamment des animations.
- **Dictionnaire :** les mots et noms propres doivent être qualifiés.
- **Inventaire :** les phones utilisés correspondent au modèle ou à l’annotation retenue.
- **Revue :** les performances atypiques demandent un contrôle humain.
- **Repli :** l’annotation manuelle reste disponible.

## 8. Jeu minimal de visèmes

Un jeu minimal vise l’intelligibilité sans multiplier les formes difficiles à sculpter, corriger et exporter. Il doit couvrir fermetures bilabiales, contacts labiodentaux, ouvertures vocaliques, arrondissements et formes neutres.

Le nombre final dépend du style, du rig, de la caméra et des langues, pas d’une liste universelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
candidate_viseme_set:
  neutral: VSM_REST
  bilabial_closed: VSM_MBP
  labiodental: VSM_FV
  alveolar_dental: VSM_TDLN
  postalveolar: VSM_SHZHCHJ
  velar: VSM_KG
  rounded_vowel: VSM_UO
  spread_vowel: VSM_EI
  open_vowel: VSM_A
  rhotic_or_language_specific: VSM_R
  status: candidate_until_character_tests
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Neutre :** la pose de repos évite un visage figé ou constamment ouvert.
- **Consonnes :** les groupes sont définis par visibilité et besoin du projet.
- **Voyelles :** ouverture, étirement et arrondissement restent séparés.
- **Spécifique :** une langue peut nécessiter un groupe supplémentaire.
- **Statut :** le jeu n’est accepté qu’après tests multi-personnages.

## 9. Architecture des formes faciales

Les visèmes peuvent combiner blendshapes, rotation de mâchoire et contrôleurs du rig. La mâchoire porte l’ouverture globale, tandis que les lèvres, joues et commissures affinent la forme.

Une forme isolée ne doit pas compenser une mauvaise topologie ou un skinning instable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_rig_layers:
  base:
    neutral_shape: required
    jaw_bone: optional_but_explicit
  speech:
    viseme_shapes: additive_candidates
    tongue_shapes: only_if_visible_and_budgeted
  expression:
    brows: separate
    eyelids: separate
    cheeks_and_nasolabial: separate
  corrective:
    jaw_lip_combinations: authored_when_needed
  invariant: speech_and_expression_can_be_blended_without_double_transform
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** la pose neutre et la mâchoire définissent le référentiel.
- **Parole :** les visèmes n’emportent pas toute l’expression.
- **Expression :** yeux et sourcils restent composables.
- **Correctifs :** les combinaisons difficiles sont traitées explicitement.
- **Invariant :** deux couches ne doivent pas appliquer deux fois la même déformation.

## 10. Nommage stable des blendshapes

Les noms affichés dans Blender ne doivent pas devenir des conventions improvisées par personnage. Un identifiant stable permet le mapping, la validation et la réimportation.

Les suffixes de côté et de correctif doivent rester déterministes afin d’éviter les heuristiques fragiles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blendshape_naming:
  prefix: FACE
  categories:
    viseme: FACE_VSM_<TOKEN>
    expression: FACE_EXP_<TOKEN>
    corrective: FACE_COR_<TOKEN>
    eye: FACE_EYE_<TOKEN>_<SIDE>
  sides: [L, R, C]
  examples:
    - FACE_VSM_MBP
    - FACE_EXP_SMILE_L
    - FACE_COR_JAWOPEN_SMILE
    - FACE_EYE_BLINK_R
  display_labels_separate: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préfixe :** il distingue les formes faciales des autres morph targets.
- **Catégories :** visème, expression et correctif ne sont pas interchangeables.
- **Côtés :** les formes asymétriques utilisent un suffixe stable.
- **Exemples :** les identifiants restent lisibles sans dépendre de l’interface.
- **Affichage :** la traduction ou le label humain reste séparé.

## 11. Catalogue des visèmes

Chaque visème possède un identifiant, une intention perceptuelle, des bornes de poids et une liste de phones associés par profil linguistique.

Le catalogue est une source de conception ; les courbes d’une réplique sont des dérivés qui le référencent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
viseme_catalog_entry:
  id: VSM_MBP
  blendshape: FACE_VSM_MBP
  jaw_weight_candidate: 0.05
  lip_weight_range: [0.0, 1.0]
  visual_intent: lips_closed_with_soft_contact
  forbidden_compensation: extreme_jaw_translation
  phone_maps:
    fr-FR: [m, b, p]
    en: [m, b, p]
  acceptance_status: draft
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le token reste stable entre langues et personnages compatibles.
- **Poids :** les bornes sont des candidats à qualifier, pas des résultats.
- **Intention :** la forme est décrite par son effet visible.
- **Interdit :** une compensation non anatomique est explicitement refusée.
- **Mapping :** les phones sont rattachés au profil linguistique.

## 12. Formes correctives

Une forme corrective résout une combinaison problématique, par exemple mâchoire ouverte plus sourire. Elle ne devient pas un nouveau visème et ne doit pas être déclenchée par un phonème.

Le correctif dépend de variables de pose et doit rester testable en isolation puis en combinaison.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
corrective_shape:
  id: FACE_COR_JAWOPEN_SMILE
  inputs:
    jaw_open: [0.45, 1.0]
    smile_average: [0.35, 1.0]
  activation: smooth_product
  output_range: [0.0, 1.0]
  speech_mapping: forbidden
  validation: [isolated, combined, left_right_asymmetry]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les seuils utilisent des valeurs candidates du rig.
- **Activation :** la montée progressive évite un saut visible.
- **Sortie :** le correctif reste borné.
- **Parole :** aucun phone ne l’active directement.
- **Validation :** les combinaisons symétriques et asymétriques sont revues.

## 13. Mâchoire, lèvres, langue et dents

La mâchoire pilote surtout l’ouverture et la projection globale. Les lèvres gèrent fermeture, étirement et arrondissement. La langue n’est animée que lorsqu’elle est visible et utile à la lecture.

Les dents et la langue ne doivent pas traverser les lèvres ou la géométrie interne pendant les extrêmes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
oral_controls:
  jaw:
    channels: [open, forward, side]
    default_authority: rig_control
  lips:
    channels: [close, funnel, pucker, spread, upper_raise, lower_drop]
  tongue:
    channels: [tip_up, tip_forward, body_raise]
    quality_gate: visible_and_budgeted
  collision_review:
    pairs: [teeth_lips, tongue_teeth, tongue_palate, lips_each_other]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mâchoire :** les degrés de liberté sont identifiés au lieu d’un simple poids global.
- **Lèvres :** les axes perceptuels restent combinables.
- **Langue :** elle n’est activée que si la caméra et le budget le justifient.
- **Collisions :** les intersections internes font partie de la revue.
- **Autorité :** les contrôleurs du rig restent la source de déformation.

## 14. Yeux, paupières et sourcils

Les yeux et sourcils portent attention, émotion et lisibilité. Ils ne doivent pas suivre mécaniquement chaque phonème.

Les paupières doivent accompagner le regard vertical et conserver une fermeture propre sur plusieurs directions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
eye_brow_contract:
  eyes:
    target_space: character_local
    vergence: distance_aware_candidate
    max_rotation: rig_qualified
  eyelids:
    blink_shapes: [FACE_EYE_BLINK_L, FACE_EYE_BLINK_R]
    look_compensation: required_if_needed
  brows:
    channels: [inner_up, outer_up, down, squeeze]
  speech_dependency: none_direct
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Regard :** la cible est convertie dans l’espace local du personnage.
- **Vergence :** la convergence dépend de la distance et doit être mesurée.
- **Paupières :** la fermeture et les correctifs de regard sont séparés.
- **Sourcils :** les canaux permettent asymétrie et émotion.
- **Parole :** aucun phone ne commande directement les yeux.

## 15. Pose neutre et état de repos

La pose neutre est la référence de toutes les formes relatives. Elle doit être reproductible après import et compatible avec le visage au repos du personnage.

Un repos crédible peut comporter de très faibles variations, mais celles-ci appartiennent à une couche d’idle et non à la base géométrique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
neutral_pose:
  id: AST-FACE-NEUTRAL-001
  mouth: relaxed_closed_or_character_specific
  jaw: rig_zero
  tongue: hidden_rest
  eyelids: open_reference
  brows: neutral_reference
  symmetry: measured_not_assumed
  idle_noise_layer: separate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la pose neutre est versionnée comme référence.
- **Bouche :** la fermeture peut varier selon le personnage mais reste documentée.
- **Zéro :** les contrôleurs du rig reviennent à des valeurs connues.
- **Symétrie :** une asymétrie anatomique peut être conservée si elle est intentionnelle.
- **Idle :** les micro-variations ne contaminent pas la base.

## 16. Contrat de données d’une réplique

Une réplique relie la voix, le texte affiché, la langue, le locuteur, le profil facial et les dérivés de timing. Le chemin de fichier seul ne constitue pas une identité.

La durée audio, la version de transcription et l’empreinte doivent permettre de détecter une désynchronisation après remplacement de la voix.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
dialogue_face_cue:
  id: AST-DLG-RELAY-SCOUT-001
  speaker_id: AST-CHAR-SCOUT-001
  audio_asset_id: AST-AUD-VOICE-SCOUT-001
  audio_version: 1.0.0
  audio_sha256: pending
  transcript_id: AST-TXT-RELAY-SCOUT-001
  locale: fr-FR
  face_profile_id: AST-FACE-PROFILE-SCOUT-001
  timing_asset_id: AST-FACE-TIMING-RELAY-SCOUT-001
  duration_seconds: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Réplique :** un identifiant stable relie les systèmes sans dépendre d’un nom affiché.
- **Audio :** version et empreinte détectent les remplacements.
- **Transcription :** le texte utilisé pour l’alignement est identifié.
- **Profil :** le personnage choisit un mapping et un niveau de qualité.
- **Durée :** la valeur reste en attente tant que le fichier n’est pas mesuré.

## 17. Manifeste de voix consommé depuis le chapitre 26

Le manifeste vocal fournit les droits, la version, la langue, le locuteur et les dérivés autorisés. Le présent chapitre ne modifie pas ces décisions.

Un timing facial devient invalide si la voix, son montage temporel ou sa transcription change.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
voice_manifest_dependency:
  source_manifest: AST-AUDIO-VOICE-MANIFESTS-001
  required_fields:
    - audio_asset_id
    - immutable_source_reference
    - approved_runtime_export
    - locale
    - transcript_reference
    - timing_change_indicator
    - consent_scope_reference
  invalidation:
    audio_content_changed: regenerate_and_review
    leading_silence_changed: regenerate_and_review
    transcript_changed: realign
    gain_only_changed: timing_may_remain_valid_after_check
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** le manifeste audio reste l’autorité sur la voix.
- **Champs :** la chaîne faciale consomme uniquement les informations nécessaires.
- **Invalidation :** les changements temporels déclenchent une régénération.
- **Gain :** une modification de niveau ne change pas forcément le timing mais exige une vérification.
- **Droits :** la référence de consentement reste séparée du fichier public.

## 18. Transcription et lexique de prononciation

La transcription d’alignement peut différer du sous-titre affiché : nombres, sigles, hésitations et mots étrangers doivent refléter la prononciation entendue.

Le lexique associe des formes normalisées à une ou plusieurs prononciations, sans supprimer les variantes réellement jouées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pronunciation_entry:
  token: "ASTERIA-7"
  locale: fr-FR
  display_text: "Asteria-7"
  alignment_text: "astéria sept"
  pronunciations:
    - phones: [a, s, t, e, r, j, a, s, ɛ, t]
      context: reference_take
  source: manually_reviewed_candidate
  unknown_phone_policy: block_alignment
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Token :** la clé reste liée à la transcription de production.
- **Affichage :** le sous-titre peut conserver une forme différente.
- **Alignement :** le texte reflète ce qui est prononcé.
- **Prononciations :** plusieurs variantes peuvent être documentées.
- **Inconnu :** un phone non reconnu bloque au lieu d’être ignoré.

## 19. Annotation manuelle des timings

L’annotation manuelle reste la voie la plus contrôlable pour les répliques importantes, les performances atypiques et les langues peu couvertes par un modèle.

Les frontières ne sont pas des vérités absolues : elles servent à construire une performance visuelle et doivent être relues en boucle avec l’audio.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
manual_annotation_tiers:
  utterance: [start, end, text]
  words: [start, end, normalized_word]
  phones: [start, end, phone]
  breaths: [start, end, type]
  acting_notes: [time, note]
  reviewer: required
  time_unit: seconds_from_runtime_audio_start
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Réplique :** le tier global borne la durée utile.
- **Mots :** les segments facilitent la navigation et le diagnostic.
- **Phones :** les unités fines alimentent le mapping visuel.
- **Respirations :** elles influencent bouche, poitrine et pauses.
- **Temps :** l’origine correspond au fichier runtime réellement joué.

## 20. Alignement forcé comme brouillon

Un aligneur forcé combine une transcription, un dictionnaire de prononciation et un modèle acoustique pour proposer des frontières de mots et de phones. Il accélère le travail mais ne garantit pas une animation correcte.

Les cris, chuchotements, chevauchements, noms propres, accents et prises très expressives doivent recevoir une revue renforcée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
forced_alignment_job:
  id: AST-FACE-ALIGN-JOB-001
  audio: approved_runtime_voice
  transcript: normalized_alignment_text
  dictionary: language_profile_dictionary
  acoustic_model: qualified_version
  output: words_and_phones_textgrid
  automatic_acceptance: forbidden
  review_flags: [oov, low_confidence, overlap, non_speech, expressive_delivery]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les trois dépendances sont versionnées ensemble.
- **Sortie :** le TextGrid reste un dérivé de travail.
- **Acceptation :** aucun résultat automatique n’est publié directement.
- **Drapeaux :** les cas risqués sont signalés à la revue.
- **Version :** un changement de modèle peut modifier les frontières.

## 21. Structure d’un TextGrid

Un TextGrid sépare des intervalles et points d’annotation sur un axe temporel. Le projet doit fixer les noms de tiers et leur signification pour éviter les fichiers incompatibles.

Les labels doivent rester dans un vocabulaire fermé ou être validés avant conversion vers les visèmes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
textgrid_contract:
  tiers:
    words:
      kind: IntervalTier
      labels: normalized_words
    phones:
      kind: IntervalTier
      labels: language_phone_inventory
    breaths:
      kind: IntervalTier
      labels: [inhale, exhale, mouth_noise, silence]
    notes:
      kind: TextTier
      labels: reviewer_comments
  time_origin: runtime_audio_start
  encoding: UTF-8
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tiers :** chaque couche possède un type et un vocabulaire.
- **Mots :** les labels utilisent la normalisation de l’alignement.
- **Phones :** les symboles doivent appartenir au profil linguistique.
- **Notes :** les points de revue restent séparés des données automatiques.
- **Origine :** le temps est aligné sur l’export audio runtime.

## 22. Normalisation et validation des timings

Le convertisseur vérifie l’ordre temporel, les bornes, les chevauchements autorisés et la durée du fichier. Il refuse les valeurs non finies ou négatives.

Une réparation silencieuse peut masquer un défaut d’alignement ; les corrections automatiques doivent être limitées et enregistrées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
timing_validation:
  duration_source: decoded_runtime_audio
  requirements:
    finite_times: true
    non_negative: true
    start_before_end: true
    ordered_within_tier: true
    end_not_after_audio: true
  overlap_policy:
    phones: forbidden_except_explicit_transition_layer
    notes: allowed
  automatic_clamp: forbidden
  report_required: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durée :** la borne vient du fichier décodé réellement utilisé.
- **Finitude :** NaN et infinités sont refusés.
- **Ordre :** chaque intervalle possède un début strictement antérieur à la fin.
- **Chevauchement :** la politique dépend du tier.
- **Rapport :** tout refus ou correction reste traçable.

## 23. Mapping des phones vers les visèmes

Le mapping linguistique produit un token de visème et éventuellement des modificateurs de mâchoire, de langue ou d’arrondissement. Il ne crée pas encore la courbe finale.

Les phones inconnus doivent être signalés ; les convertir silencieusement en repos détruit l’intelligibilité et masque un défaut de dictionnaire.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
phone_to_viseme_map:
  locale: fr-FR
  entries:
    m: {viseme: VSM_MBP, jaw: 0.05}
    p: {viseme: VSM_MBP, jaw: 0.05}
    f: {viseme: VSM_FV, jaw: 0.12}
    u: {viseme: VSM_UO, jaw: 0.28, rounding: 1.0}
    a: {viseme: VSM_A, jaw: 0.72}
  unknown_phone: error
  silence_phone: VSM_REST
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Langue :** le mapping appartient à un profil précis.
- **Entrées :** plusieurs phones peuvent partager le même visème.
- **Modificateurs :** la mâchoire et l’arrondissement complètent la forme.
- **Inconnu :** une valeur non reconnue bloque la conversion.
- **Silence :** le repos est explicite et distinct d’une erreur.

## 24. Coarticulation

La bouche anticipe souvent le son suivant et conserve une partie du précédent. Une succession de poses carrées produit un mouvement mécanique, même avec des timings phonétiques exacts.

La coarticulation se construit par fenêtres d’attaque, de maintien et de relâchement, puis par règles de priorité entre fermeture, ouverture et arrondissement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
coarticulation_profile:
  anticipation_ms_candidate: 55
  release_ms_candidate: 70
  minimum_hold_ms_candidate: 20
  priorities:
    bilabial_closure: high
    labiodental_contact: high
    strong_rounding: medium
    open_vowel: medium
    rest: low
  values_status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Anticipation :** la pose peut commencer avant la frontière acoustique.
- **Relâchement :** le précédent ne tombe pas instantanément à zéro.
- **Maintien :** une durée minimale évite les impulsions invisibles.
- **Priorité :** les contacts lisibles peuvent dominer les transitions.
- **Statut :** les millisecondes restent des candidats à tester.

## 25. Attaque, maintien et relâchement

Chaque événement visème est converti en une enveloppe temporelle. La forme de l’enveloppe dépend du débit, de la durée du phone et de l’importance visuelle.

Une enveloppe trop large fusionne les syllabes ; une enveloppe trop étroite crée des claquements et des poids élevés sans lecture.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
viseme_envelope:
  event:
    phone_start: 1.240
    phone_end: 1.330
    viseme: VSM_MBP
  attack:
    start: 1.185
    curve: ease_out
  hold:
    target_weight: 0.92
  release:
    end: 1.395
    curve: ease_in
  status: illustrative_candidate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Événement :** les frontières acoustiques restent la référence initiale.
- **Attaque :** l’anticipation commence avant le phone.
- **Maintien :** le poids cible dépend du rig et du contexte.
- **Relâchement :** la pose décroît après la frontière.
- **Statut :** les valeurs ne sont pas une mesure exécutée.

## 26. Mélange et normalisation des poids

Plusieurs visèmes peuvent se chevaucher pendant la coarticulation. Le mélange doit conserver les fermetures et éviter que la somme de poids produise une déformation extrême.

La normalisation globale n’est pas toujours correcte : une forme corrective ou un contact bilabial peut nécessiter une règle dédiée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
viseme_blend_policy:
  max_total_weight_candidate: 1.25
  normalization:
    default: weighted_clamp
    bilabial_closure: preserve_priority
    corrective_shapes: evaluated_after_primary_visemes
  negative_weights: forbidden
  over_one_shape_weight: rig_specific_and_disabled_by_default
  report_saturation: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Somme :** la borne protège le rig mais reste à mesurer.
- **Priorité :** les fermetures lisibles ne sont pas diluées arbitrairement.
- **Correctifs :** ils sont évalués après les formes principales.
- **Bornes :** les poids négatifs sont refusés.
- **Diagnostic :** les saturations sont enregistrées pour la revue.

## 27. Silences, respirations et bruits de bouche

Le silence n’est pas un trou de données. Il peut contenir une fermeture progressive, une respiration, une préparation de phrase ou un retour à l’émotion neutre.

Les bruits de bouche ne doivent pas déclencher automatiquement un visème s’ils ne participent pas à l’intelligibilité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
non_speech_event:
  types:
    silence:
      mouth_target: contextual_rest
    inhale:
      mouth_target: small_open_candidate
      chest_or_head_note: optional
    exhale:
      mouth_target: relaxed_release
    mouth_noise:
      mouth_target: manual_review
  blink_suggestion: never_mandatory
  narrative_authority: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Silence :** la pose dépend du contexte de jeu d’acteur.
- **Inspiration :** une légère ouverture peut être utile mais reste candidate.
- **Expiration :** le relâchement est distinct d’un visème.
- **Bruit :** la revue décide s’il doit être visible.
- **Autorité :** aucun événement non verbal ne modifie la narration.

## 28. Consonnes fermées, fricatives et voyelles

Les consonnes fermées comme les bilabiales exigent un contact lisible. Les fricatives labiodentales demandent une relation lèvre-dents. Les voyelles structurent surtout ouverture, étirement et arrondissement.

La précision acoustique ne justifie pas une suraccentuation visuelle qui déforme l’identité du personnage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
articulation_review:
  bilabial:
    check: lips_make_visible_contact
  labiodental:
    check: lower_lip_near_upper_teeth_without_intersection
  open_vowel:
    check: jaw_and_lip_opening_preserve_identity
  rounded_vowel:
    check: funnel_and_pucker_without_excessive_projection
  fast_speech:
    check: preserve_key_contacts_and_reduce_minor_shapes
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bilabiale :** la fermeture doit être visible dans les plans qui l’exigent.
- **Labiodentale :** le contact ne traverse pas les dents.
- **Ouverture :** la mâchoire et les lèvres restent anatomiquement cohérentes.
- **Arrondissement :** la projection est bornée par l’identité du visage.
- **Débit :** les contacts principaux sont conservés quand le détail est réduit.

## 29. Émotion et parole

L’émotion modifie la posture du visage mais ne doit pas remplacer le signal articulatoire. Un sourire, une tension ou une peur se mélange aux visèmes avec des masques et des correctifs.

Une expression globale trop forte peut empêcher la fermeture des lèvres ou décaler les dents, ce qui rend la parole moins lisible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
speech_expression_blend:
  speech_layer:
    channels: [jaw, lips, tongue]
    priority: intelligibility
  expression_layer:
    channels: [brows, cheeks, lip_corners, eyelids]
    weight: acting_direction
  masks:
    allow_shared_channels: explicit_only
  corrective_layer:
    evaluation: after_speech_and_expression
  review: extreme_emotions_and_fast_dialogue
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Parole :** les canaux essentiels à l’articulation gardent leur lisibilité.
- **Expression :** les zones émotionnelles restent pilotables.
- **Masques :** un canal partagé doit être déclaré.
- **Correctif :** les interactions sont résolues après le mélange.
- **Revue :** les extrêmes sont testés avec un débit réel.

## 30. Prosodie, intensité et accentuation

La prosodie peut influencer amplitude gestuelle, ouverture de mâchoire, sourcils et mouvements de tête. Elle ne doit pas être déduite d’un simple volume instantané.

Les accents linguistiques et émotionnels sont des suggestions de performance, puis une personne valide leur pertinence artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
prosody_features:
  sources:
    transcript_emphasis: authored
    pitch_contour: optional_analysis
    intensity_contour: optional_analysis
    phrase_boundaries: reviewed
  outputs:
    jaw_emphasis: bounded_modifier
    brow_accent: sparse_candidate
    head_nod: acting_note_only
  automatic_final_animation: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les annotations humaines et analyses restent séparées.
- **Hauteur :** le contour mélodique peut aider sans dicter l’acting.
- **Intensité :** le niveau sonore ne devient pas directement un poids facial.
- **Sorties :** les modificateurs restent bornés et rares.
- **Interdit :** aucune animation finale n’est acceptée automatiquement.

## 31. Clignements

Les clignements répondent à la physiologie, à l’attention et au jeu d’acteur, pas à une minuterie uniforme. Ils peuvent accompagner une transition de regard ou une frontière de phrase sans devenir systématiques.

Le système doit permettre clignements complets, partiels et asymétriques lorsque le rig et la direction le justifient.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blink_profile:
  spontaneous_interval_range_seconds_candidate: [2.5, 7.0]
  duration_seconds_candidate: [0.08, 0.18]
  suppress_during:
    - critical_eye_contact
    - already_closed_pose
  allow_near:
    - gaze_shift
    - phrase_boundary
  deterministic_seed_source: character_and_take_id
  values_status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Intervalle :** la plage évite un rythme parfaitement périodique.
- **Durée :** la vitesse dépend du style et du plan.
- **Suppression :** certains moments exigent les yeux ouverts ou déjà fermés.
- **Placement :** les frontières ne déclenchent qu’une suggestion.
- **Déterminisme :** une graine stable facilite la comparaison des prises.

## 32. Regard et cible d’attention

Le regard doit identifier une cible, un espace de conversion et une durée de maintien. Les yeux, la tête et le torse n’arrivent pas nécessairement en même temps.

Une cible perdue doit conduire à un repli sûr plutôt qu’à une rotation extrême ou un saut vers l’origine du monde.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gaze_cue:
  target_id: AST-GAZE-RELAY-PANEL-001
  target_space: world
  start_time: 0.420
  end_time: 1.850
  eye_lead_seconds_candidate: 0.08
  head_follow_weight_candidate: 0.35
  lost_target_policy: hold_then_return_to_reference
  max_angles: rig_profile
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** l’identité reste distincte de sa position.
- **Temps :** la fenêtre de regard appartient à la prise.
- **Décalage :** les yeux peuvent précéder la tête.
- **Perte :** le système conserve puis revient à une référence.
- **Angles :** les limites viennent du profil du rig.

## 33. Saccades et micro-mouvements oculaires

Un regard parfaitement fixe paraît souvent artificiel, mais un bruit aléatoire continu donne une impression nerveuse. Les micro-mouvements doivent être rares, bornés et liés à la tâche.

À distance ou en foule, ils peuvent être supprimés sans perte d’information.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
eye_micro_motion:
  mode: sparse_saccades
  amplitude_degrees_candidate: [0.2, 1.2]
  interval_seconds_candidate: [0.6, 2.5]
  distribution: non_uniform
  pause_during: [blink, large_gaze_shift, facial_lod_low]
  deterministic_seed: take_id
  values_status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode :** des impulsions rares remplacent un bruit continu.
- **Amplitude :** la plage doit rester invisible comme mécanisme.
- **Intervalle :** la distribution évite la périodicité.
- **Pause :** les grands mouvements et LOD bas désactivent le détail.
- **Graine :** la prise reste reproductible pendant la revue.

## 34. Mouvements de tête

La tête ponctue l’attention, l’accentuation et la respiration. Elle ne doit pas suivre chaque syllabe ni être générée uniquement à partir de l’amplitude.

Les mouvements sont définis dans un espace local, avec des limites du rig et une séparation entre animation d’acting et contrôle gameplay de la caméra.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
head_gesture:
  id: AST-FACE-HEAD-NOD-001
  type: nod
  time_window: [1.10, 1.42]
  amplitude_degrees_candidate: 4.0
  ease: smooth_in_out
  local_space: head_parent
  camera_authority: none
  gameplay_authority: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le geste peut être revu et réutilisé comme note d’acting.
- **Fenêtre :** la durée est liée à la réplique.
- **Amplitude :** la valeur reste candidate jusqu’au test.
- **Espace :** le parent du cou ou de la tête fournit le référentiel.
- **Autorité :** le geste ne pilote ni caméra ni gameplay.

## 35. Gestes complémentaires

Les mains, épaules et torse peuvent soutenir une phrase, mais le présent chapitre ne redéfinit pas la bibliothèque corporelle du chapitre 20. Il fournit seulement des événements temporels et des notes d’acting.

La synchronisation entre geste et parole doit rester souple : un geste peut anticiper ou suivre le mot accentué.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gesture_sync_note:
  cue_id: AST-GESTURE-RELAY-WARN-001
  dialogue_cue_id: AST-DLG-RELAY-SCOUT-001
  anchor:
    type: word
    token: "proches"
    offset_seconds_candidate: -0.18
  body_animation_ref: existing_animation_or_new_request
  facial_dependency: none_direct
  ownership: animation_library
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cue :** l’événement garde une identité indépendante.
- **Ancre :** un mot ou une frontière de phrase fournit le repère.
- **Décalage :** l’anticipation est explicite.
- **Référence :** le geste corporel appartient à la bibliothèque d’animation.
- **Dépendance :** le visage et le corps se synchronisent sans se posséder.

## 36. Asymétrie et identité du personnage

Un visage vivant n’est pas toujours parfaitement symétrique. L’asymétrie peut provenir de l’anatomie, de l’émotion ou du jeu d’acteur, mais elle doit rester intentionnelle et compatible avec les visèmes.

Les formes de parole principales restent lisibles des deux côtés avant l’ajout de variations.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_asymmetry:
  anatomical_baseline: character_specific
  speech_primary_shapes:
    symmetric_requirement: readable_not_mathematically_identical
  acting_offsets:
    lip_corner_bias: authored_candidate
    brow_bias: authored_candidate
    blink_offset: sparse_candidate
  random_asymmetry: disabled_by_default
  review: front_three_quarter_profile
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Anatomie :** la base propre au personnage est conservée.
- **Parole :** la lisibilité prime sur une symétrie numérique.
- **Acting :** les écarts sont des décisions d’auteur.
- **Aléatoire :** aucun biais arbitraire n’est ajouté par défaut.
- **Vues :** la revue couvre plusieurs angles.

## 37. Micro-expressions

Les micro-expressions peuvent enrichir un gros plan, mais elles coûtent du temps d’auteur, des formes et de la bande passante d’animation. Elles ne doivent pas masquer la bouche ni devenir un bruit permanent.

Elles appartiennent aux profils de haute qualité et peuvent disparaître entièrement dans les profils gameplay ou foule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
micro_expression_profile:
  enabled_in: [hero_close_up]
  disabled_in: [crowd_low]
  channels: [brow_tension, lip_corner_twitch, eyelid_pressure]
  duration_seconds_candidate: [0.12, 0.45]
  maximum_simultaneous: 1
  random_generation: forbidden_without_review
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le détail est réservé aux plans qui le montrent.
- **Canaux :** les formes sont limitées à des zones précises.
- **Durée :** les valeurs restent candidates.
- **Concurrence :** une seule micro-expression évite la surcharge.
- **Revue :** aucune génération aléatoire n’est publiée seule.

## 38. Export des blendshapes vers Godot

Les shape keys de Blender deviennent des blend shapes ou morph targets lors de l’export compatible. Le chapitre 28 fixera les presets et la réimportation ; ici, le contrat porte sur les noms, la neutralité et les valeurs attendues.

Une forme manquante ou renommée doit bloquer le profil facial plutôt que produire une animation partielle silencieuse.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_blendshape_contract:
  source: blender_shape_keys
  exchange: glTF_or_GLB_candidate
  required_names:
    - FACE_VSM_MBP
    - FACE_VSM_FV
    - FACE_VSM_A
    - FACE_EYE_BLINK_L
    - FACE_EYE_BLINK_R
  missing_shape_policy: block_profile_activation
  reorder_tolerance: by_name_only
  import_preset_owner: chapter_28
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** les shape keys restent dans le fichier canonique du personnage.
- **Échange :** le format final sera qualifié par la chaîne d’import.
- **Noms :** le contrat vérifie les identifiants indispensables.
- **Ordre :** le mapping se fait par nom et non par index.
- **Propriétaire :** le preset d’import appartient au chapitre 28.

## 39. Pistes de blend shapes dans AnimationPlayer

Godot peut animer les poids de blend shapes dans des pistes dédiées. Les courbes importées ou créées doivent partager une origine temporelle avec la voix runtime.

Les pistes audio et faciales peuvent coexister dans une séquence de présentation, mais la voix reste une dépendance référencée et non une source d’autorité métier.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
animation_track_plan:
  animation_id: AST-FACE-ANIM-RELAY-SCOUT-001
  length_source: approved_runtime_audio_duration
  tracks:
    - type: blend_shape
      target: FACE_VSM_MBP
    - type: blend_shape
      target: FACE_VSM_A
    - type: value
      target: face_driver/jaw_open
    - type: value
      target: face_driver/gaze_target_weight
  audio_reference: AST-AUD-VOICE-SCOUT-001
  loop: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Animation :** l’identifiant relie la prise et les courbes.
- **Durée :** la voix runtime fournit la borne.
- **Pistes :** blendshapes et propriétés du driver restent distinctes.
- **Audio :** la ressource est référencée par identité.
- **Boucle :** une réplique n’est pas répétée implicitement.

## 40. AnimationTree et couches faciales

`AnimationTree` peut mélanger parole, expression et idle avec des filtres de pistes. Il doit être utilisé comme autorité de lecture lorsque la scène l’active, tandis que `AnimationPlayer` conserve les animations sources.

Les filtres empêchent une couche faciale de modifier le corps ou une couche corporelle d’écraser involontairement la bouche.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_animation_tree:
  source_player: CharacterAnimationPlayer
  root: AnimationNodeBlendTree
  layers:
    body_base:
      filter: body_tracks
    facial_speech:
      filter: face_speech_tracks
    facial_expression:
      filter: face_expression_tracks
    blink_one_shot:
      filter: eyelid_tracks
  playback_authority: AnimationTree
  source_editing_authority: AnimationPlayer
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** les animations restent stockées dans `AnimationPlayer`.
- **Graphe :** le blend tree compose les couches.
- **Filtres :** chaque couche cible des pistes explicites.
- **Lecture :** `AnimationTree` pilote les transitions et mélanges actifs.
- **Édition :** `AnimationPlayer` conserve la création des clips sources.

## 41. Ressource typée de timing facial

Une ressource de timing transporte des événements validés sans exposer directement un dictionnaire libre aux scènes. Elle conserve la version de schéma, la langue et les dépendances.

Les tableaux retournés doivent être traités comme immuables ou copiés avant modification afin d’éviter qu’une scène altère la source partagée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_timing_asset:
  schema_version: 1
  id: AST-FACE-TIMING-RELAY-SCOUT-001
  locale: fr-FR
  audio_asset_id: AST-AUD-VOICE-SCOUT-001
  audio_sha256: pending
  events:
    - {start: 0.18, end: 0.31, phone: m, viseme: VSM_MBP}
    - {start: 0.31, end: 0.44, phone: a, viseme: VSM_A}
  review_status: draft
  immutable_after_publication: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** la version permet les migrations futures.
- **Identité :** le timing reste séparé du fichier audio.
- **Empreinte :** un changement de voix invalide le dérivé.
- **Événements :** chaque intervalle garde phone et visème pour le diagnostic.
- **Publication :** une version approuvée devient immuable.

## 42. Driver facial runtime

Le driver runtime applique des poids calculés à des cibles prévalidées. Il ne recherche pas des nœuds ou blendshapes à chaque frame et ne crée pas de données de conception.

Les échecs de binding sont détectés au chargement ; le profil peut alors se désactiver proprement plutôt que produire un visage partiellement animé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
runtime_driver_contract:
  initialization:
    resolve_targets_once: true
    validate_required_channels: true
    failure_policy: disable_face_profile_and_report
  frame_update:
    input: sampled_facial_pose
    writes: prebound_blendshape_and_rig_channels
    allocations: forbidden_in_steady_state
  domain_events_emitted: none
  file_io: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Initialisation :** les cibles sont résolues une seule fois.
- **Validation :** les canaux requis bloquent un profil incomplet.
- **Frame :** le driver reçoit une pose déjà calculée.
- **Coût :** aucune allocation régulière n’est autorisée comme objectif.
- **Autorité :** le driver n’émet aucun événement métier.

## 43. Échantillonnage déterministe des courbes

Pour comparer deux builds, la même prise et le même profil doivent produire les mêmes poids au même temps logique. Le système ne dépend pas de la fréquence d’image pour l’ordre des événements.

La pose est échantillonnée au temps de lecture de la voix ou à une horloge de présentation explicitement synchronisée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
sampling_policy:
  time_source: audio_playback_position_or_synced_presentation_clock
  frame_rate_dependency: none_for_event_order
  interpolation: cubic_or_linear_per_channel
  out_of_range:
    before_start: neutral
    after_end: release_to_neutral
  deterministic_inputs:
    - timing_asset_version
    - face_profile_version
    - take_id
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Temps :** la source est définie et synchronisée avec la voix.
- **Frame :** le framerate n’ordonne pas les événements.
- **Interpolation :** chaque canal choisit une méthode qualifiée.
- **Bornes :** la pose retourne au neutre hors de la prise.
- **Déterminisme :** les versions et identités suffisent à reproduire le résultat.

## 44. Interpolation et tangentes

Les courbes linéaires sont prévisibles mais peuvent paraître mécaniques. Les courbes cubiques offrent des transitions plus organiques, à condition de contrôler les dépassements.

Les canaux de contact, comme une fermeture bilabiale, peuvent exiger des tangentes plus fermes que les sourcils ou le regard.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
curve_policy:
  viseme_default: cubic_clamped
  jaw_default: cubic_clamped
  blink: authored_fast_close_slow_open
  gaze: smooth_step_candidate
  corrective: derived_from_inputs
  overshoot:
    speech_contacts: forbidden
    expression_channels: rig_qualified_only
  tangent_review: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Visèmes :** les courbes cubiques sont bornées.
- **Mâchoire :** le même principe évite les claquements.
- **Clignement :** la fermeture et l’ouverture peuvent avoir des vitesses différentes.
- **Dépassement :** les contacts de parole ne dépassent pas leur maximum.
- **Revue :** les tangentes sont inspectées, pas seulement les clés.

## 45. Lissage et latence

Un filtre de lissage peut réduire le bruit mais ajoute un retard. Un lissage uniforme sur tous les canaux dégrade les contacts rapides et rend les bilabiales molles.

Les paramètres sont définis par famille de canal et mesurés contre l’intelligibilité, pas seulement contre une courbe plus jolie.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
smoothing_profile:
  channels:
    jaw_open:
      method: critically_damped_candidate
      response_ms: pending
    lip_closure:
      method: minimal_or_none
    brows:
      method: low_frequency_smoothing_candidate
    gaze:
      method: velocity_limited_candidate
  maximum_added_latency_ms: pending_measurement
  bypass_comparison_required: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mâchoire :** un amortissement peut stabiliser l’ouverture.
- **Fermeture :** les contacts rapides limitent le lissage.
- **Sourcils :** les variations lentes tolèrent davantage de filtrage.
- **Regard :** une limite de vitesse protège les yeux.
- **Comparaison :** le bypass révèle le retard ajouté.

## 46. Auteur manuel ou génération runtime

Une animation pré-calculée offre un résultat révisable et stable pour les dialogues importants. Une génération runtime peut réduire le volume de données ou traiter du contenu dynamique, mais elle complique la validation et le déterminisme.

Le projet choisit par catégorie de dialogue, sans imposer une seule solution à toutes les scènes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
authoring_strategy:
  cinematic_hero_dialogue:
    mode: reviewed_baked_animation
  gameplay_authored_dialogue:
    mode: reviewed_timing_with_runtime_sampling
  dynamic_or_generated_dialogue:
    mode: runtime_candidate_with_strict_fallback
  fallback:
    mode: bounded_jaw_and_rest_pose
  publication_gate:
    automatic_output: draft_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cinématique :** les plans rapprochés utilisent des animations revues.
- **Gameplay :** les timings peuvent être échantillonnés au runtime.
- **Dynamique :** le contenu imprévisible reste un candidat à encadrer.
- **Repli :** une mâchoire bornée vaut mieux qu’un rig cassé.
- **Porte :** toute sortie automatique reste brouillon avant approbation.

## 47. Profils par langue

Un profil de langue relie inventaire de phones, dictionnaire, mapping de visèmes et règles de coarticulation. Il ne doit pas supposer qu’un mapping français convient à l’anglais, au japonais ou à une langue fictive.

Les traductions qui modifient durée et rythme produisent de nouveaux timings, même si le personnage et le sens narratif restent identiques.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
language_profiles:
  fr-FR:
    id: AST-FACE-LANG-FR-001
    status: reference_candidate
  en:
    id: AST-FACE-LANG-EN-001
    status: pending_qualification
  fictional_relay_code:
    id: AST-FACE-LANG-RELAY-001
    status: manual_only
  shared_viseme_shapes: allowed_when_tested
  shared_timings_between_locales: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Français :** le profil de référence reste à matérialiser.
- **Anglais :** un inventaire et un dictionnaire distincts sont qualifiés.
- **Fictif :** une langue inventée peut nécessiter une annotation manuelle.
- **Formes :** les mêmes blendshapes peuvent être partagées après test.
- **Timings :** deux locales ne réutilisent jamais aveuglément les mêmes frontières.

## 48. Profils de qualité faciale

Le niveau de qualité définit canaux actifs, précision temporelle, fréquence d’échantillonnage et correctifs. Il conserve toujours les signaux essentiels à l’intelligibilité quand la bouche reste visible.

Une réduction de qualité ne doit pas modifier l’identité de la réplique ni sa durée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_quality_profiles:
  hero_close_up:
    visemes: full
    eyes_brows: full
    correctives: full
    micro_expressions: enabled
  gameplay_mid:
    visemes: reduced_but_readable
    eyes_brows: essential
    correctives: selected
    micro_expressions: disabled
  crowd_low:
    visemes: minimal_or_baked
    eyes_brows: sparse
    correctives: disabled
    update_rate: reduced_candidate
  audio_timing: unchanged
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gros plan :** tous les canaux qualifiés peuvent être actifs.
- **Gameplay :** les formes secondaires sont réduites.
- **Foule :** le profil privilégie les silhouettes faciales lisibles.
- **Temps :** la voix et les frontières ne changent pas avec le LOD.
- **Mesure :** les fréquences et coûts restent à profiler.

## 49. LOD facial en gros plan

Le gros plan révèle les intersections, les tangentes, les micro-glissements et les incohérences entre regard et parole. La porte exige plusieurs angles et plusieurs expressions.

Le test doit utiliser la caméra, la focale, l’éclairage et le matériau de production, pas seulement le viewport de Blender.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
close_up_test:
  profile: hero_close_up
  cameras: [front, three_quarter_left, three_quarter_right, profile]
  lighting: production_reference_and_flat_diagnostic
  checks:
    - lip_contact
    - teeth_and_tongue_intersections
    - eyelid_closure
    - curve_overshoot
    - expression_speech_blend
    - gaze_targeting
  runtime_required: true
  status: not_executed
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le test active la qualité maximale.
- **Caméras :** plusieurs angles révèlent des défauts différents.
- **Lumière :** une vue diagnostique complète l’éclairage artistique.
- **Contrôles :** la liste couvre articulation, collisions et acting.
- **Statut :** aucune exécution n’est revendiquée.

## 50. LOD facial à distance de gameplay

À distance moyenne, certaines nuances disparaissent mais les ouvertures, fermetures et directions du regard peuvent rester utiles. Le test mesure ce qui est réellement perceptible à la résolution cible.

Les formes coûteuses sont supprimées seulement si la compréhension et l’identité restent stables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gameplay_distance_test:
  profile: gameplay_mid
  camera_distance_m_candidate: [2.5, 8.0]
  resolutions: [1920x1080, 2560x1440]
  motion_context: [idle_dialogue, walking_dialogue]
  checks:
    - major_viseme_readability
    - gaze_direction_readability
    - expression_identity
    - temporal_stability
  values_status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distance :** la plage est un candidat lié aux caméras du jeu.
- **Résolution :** le rendu est observé sur plusieurs cibles.
- **Mouvement :** la locomotion peut masquer le détail facial.
- **Contrôles :** la lisibilité prime sur la fidélité des micro-formes.
- **Statut :** aucune mesure n’est annoncée.

## 51. LOD facial en foule

Une foule exige des limites de personnages animés, de canaux et de fréquence de mise à jour. Les personnages hors importance peuvent utiliser une animation pré-calculée, un jeu minimal ou aucune parole visible.

La priorité dépend de la taille écran, de la caméra, du rôle narratif et de l’audibilité, pas uniquement de la distance.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
crowd_facial_policy:
  priority_inputs:
    - screen_size
    - narrative_importance
    - current_speaker
    - camera_focus
    - audibility
  tiers:
    high: hero_close_up
    medium: gameplay_mid
    low: crowd_low
    none: neutral_or_baked_idle
  hysteresis: required
  maximum_active_faces: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Priorité :** plusieurs signaux déterminent le niveau.
- **Locuteur :** la personne entendue peut recevoir un profil supérieur.
- **Paliers :** la réduction est explicite.
- **Hystérésis :** elle évite les changements rapides de qualité.
- **Budget :** le nombre actif reste à mesurer.

## 52. Budgets candidats

Le budget facial sépare nombre de blendshapes, pistes, clés, personnages actifs, temps CPU, mémoire et bande passante. Une seule valeur de « qualité » ne suffit pas.

Les objectifs sont des hypothèses de départ et doivent être remplacés par des mesures du build cible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_budget_candidates:
  hero_close_up:
    active_blendshape_channels: pending
    key_count_per_second: pending
    cpu_ms: pending
  gameplay_mid:
    active_blendshape_channels: pending
    update_hz: pending
    cpu_ms: pending
  crowd_low:
    active_faces: pending
    update_hz: pending
    memory_mb: pending
  measurement_hardware: reference_configuration
  status: unmeasured
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canaux :** le nombre de formes actives est mesuré séparément.
- **Clés :** la densité de courbe influence mémoire et évaluation.
- **CPU :** chaque profil possède son propre coût.
- **Foule :** nombre actif et fréquence sont distingués.
- **Statut :** aucun budget n’est déclaré atteint.

## 53. Compression et réduction des clés

La réduction de clés peut alléger les animations mais déplacer un contact labial ou lisser une fermeture. Elle doit être évaluée sur l’image et contre une erreur temporelle ou de poids.

Les pistes critiques peuvent recevoir une tolérance plus stricte que les sourcils ou micro-expressions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
key_reduction_policy:
  critical_channels:
    - FACE_VSM_MBP
    - FACE_VSM_FV
    - jaw_open
  tolerance:
    critical: strict_candidate
    secondary: moderate_candidate
  preserve:
    - contact_peaks
    - phrase_boundaries
    - blink_extremes
  compare:
    - max_weight_error
    - timing_shift_ms
    - visual_review
  status: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Critiques :** les contacts lisibles sont protégés.
- **Tolérance :** les valeurs restent à qualifier.
- **Préservation :** certains extrema ne peuvent pas être supprimés.
- **Comparaison :** erreur numérique et revue visuelle sont combinées.
- **Statut :** aucune compression n’est validée ici.

## 54. Tests sur plusieurs voix

Un mapping acceptable sur une seule voix ne garantit pas la robustesse. Le test doit couvrir débits, hauteurs, accents, émotions et timbres différents, dans la limite des droits disponibles.

Les résultats sont attachés aux prises et profils testés ; ils ne sont pas généralisés à toutes les voix.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
multi_voice_matrix:
  dimensions:
    tempo: [slow, reference, fast]
    delivery: [neutral, whispered, shouted, emotional]
    speaker: [voice_a, voice_b, voice_c_candidate]
    locale: [fr-FR, en_candidate]
  required_evidence:
    - reviewed_timings
    - close_up_capture
    - gameplay_distance_capture
    - defect_log
  generalization: forbidden_beyond_tested_scope
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Débit :** les transitions rapides et lentes révèlent des défauts distincts.
- **Jeu :** chuchotement et cri perturbent les alignements automatiques.
- **Locuteur :** plusieurs timbres limitent le surapprentissage à une prise.
- **Preuves :** les captures et défauts sont liés à chaque cas.
- **Portée :** aucune conclusion universelle n’est autorisée.

## 55. Localisation et remplacement d’une voix

Toute nouvelle locale ou nouvelle prise change potentiellement durée, accents et frontières. Le système doit invalider les timings concernés et préserver les animations qui ne dépendent pas du texte.

Les gestes ancrés à un mot doivent être remappés ou convertis vers un repère sémantique lors de la localisation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
localization_invalidation:
  new_audio_take:
    facial_timing: regenerate
    viseme_curves: regenerate
    gaze_notes: review
    emotion_layer: review
  new_locale:
    language_profile: required
    pronunciation_dictionary: required
    word_anchored_gestures: remap
  unchanged:
    character_rig: reusable_if_compatible
    body_animation: reusable_after_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Prise :** les timings et courbes dépendent du fichier sonore.
- **Locale :** un nouveau profil linguistique est obligatoire.
- **Gestes :** les ancres lexicales sont remappées.
- **Rig :** la structure faciale peut être réutilisée si compatible.
- **Corps :** les clips sont revus même s’ils restent valides.

## 56. Scène de test et matrice de caméras

Une scène de validation charge un personnage, une voix, une animation et plusieurs caméras sans systèmes métier inutiles. Elle permet de répéter les mêmes comparaisons.

Le script de test enregistre les identifiants et versions ; il ne prétend pas mesurer tant que la scène n’est pas réellement exécutée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
validation_scene_plan:
  scene: res://scenes/validation/facial/ch27_face_validation.tscn
  fixtures:
    character: AST-CHAR-SCOUT-001
    audio: AST-AUD-VOICE-SCOUT-001
    timing: AST-FACE-TIMING-RELAY-SCOUT-001
  cameras:
    - close_front
    - close_three_quarter
    - gameplay_mid
    - crowd_reference
  outputs:
    - capture_manifest
    - defect_log
    - performance_report
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scène :** le chemin proposé reste un livrable à créer.
- **Fixtures :** les identifiants rendent les essais reproductibles.
- **Caméras :** chaque profil possède une vue de référence.
- **Sorties :** captures, défauts et mesures sont séparés.
- **Réserve :** aucune scène n’est annoncée comme existante.

## 57. Critères d’acceptation

Une animation faciale est acceptée lorsque les dépendances sont qualifiées, les formes sont stables, les timings sont relus et le résultat reste intelligible aux distances prévues.

L’acceptation artistique et l’acceptation technique sont indépendantes ; un fichier peut être techniquement valide mais jouer faux, ou être convaincant mais dépasser les budgets.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_acceptance_gate:
  dependencies:
    audio_manifest: approved
    transcript: reviewed
    rig_profile: compatible
    language_profile: qualified
  artistic:
    intelligibility: pass
    acting_direction: approved
    mechanical_motion: absent_or_accepted_exception
  technical:
    missing_channels: 0
    invalid_times: 0
    runtime_errors: 0
    budgets: measured_and_within_target
  human_approval: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** la porte ne démarre pas avec des sources inconnues.
- **Artistique :** intelligibilité et jeu d’acteur sont revus séparément.
- **Technique :** les erreurs de données sont bloquantes.
- **Budgets :** les coûts doivent être mesurés.
- **Humain :** aucun outil ne prononce seul l’acceptation finale.

## 58. Mode Solo

En mode Solo, le périmètre reste réduit : un personnage pilote, un jeu minimal de visèmes, une langue de référence et quelques répliques importantes corrigées manuellement.

Les dialogues secondaires peuvent utiliser un profil simplifié, mais les règles de provenance, d’invalidation et de mesure restent les mêmes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
solo_scope:
  pilot_characters: 1
  reference_locales: 1
  viseme_set: minimal
  hero_lines: manually_reviewed
  secondary_lines: reviewed_alignment_candidate
  tools: [Blender, Praat_or_equivalent, Godot]
  automation: transparent_and_optional
  acceptance: same_contract_reduced_volume
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Volume :** le lot pilote reste maîtrisable par une personne.
- **Langue :** une seule locale est qualifiée en premier.
- **Répliques :** les lignes importantes reçoivent une correction manuelle.
- **Outils :** la chaîne utilise peu d’applications et des formats lisibles.
- **Contrat :** la réduction de volume ne réduit pas la traçabilité.

## 59. Mode Studio

En mode Studio, la production sépare direction de performance, linguistique, rig facial, animation, intégration et QA. Les rôles peuvent être cumulés, mais les responsabilités et validations restent identifiables.

Les conventions multilingues, les outils d’annotation et les profils par plateforme sont versionnés et revus comme des dépendances de production.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
studio_roles:
  performance_director: acting_and_take_approval
  linguist_or_localization: transcript_lexicon_and_phone_review
  facial_rigger: shapes_controls_and_correctives
  facial_animator: curves_coarticulation_gaze_and_blinks
  technical_animator: tools_export_and_runtime_driver
  integrator: godot_scene_and_profiles
  qa: distance_language_and_performance_campaign
  legal_or_production: consent_and_access_control
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Direction :** la prise et l’intention d’acting sont approuvées.
- **Langue :** les prononciations et phones sont revus.
- **Rig :** les formes et correctifs restent sous responsabilité dédiée.
- **Technique :** les outils et l’intégration sont séparés de l’animation artistique.
- **QA :** les campagnes couvrent langues, distances et plateformes.

## 60. Provenance, consentement et confidentialité

Les voix, scans faciaux, vidéos de référence et performances peuvent contenir des données personnelles ou des droits voisins. Le dépôt public ne conserve ni contrats, ni identités sensibles, ni prises non autorisées.

Le chapitre 26 reste l’autorité sur les consentements vocaux ; le présent chapitre ajoute les usages de référence vidéo, capture faciale, entraînement et dérivation d’animation lorsqu’ils existent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_rights_manifest:
  voice_consent_ref: restricted_reference
  facial_video_consent_ref: separate_if_recorded
  scan_or_likeness_ref: separate_if_used
  model_training_permission: explicit_decision
  retargeting_and_derivative_animation: explicit_scope
  public_repository:
    contracts: forbidden
    personal_identity: minimized
    raw_reference_video: forbidden_by_default
  withdrawal_process: documented
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Voix :** la référence renvoie au manifeste du chapitre 26.
- **Vidéo :** l’enregistrement facial reçoit une portée séparée.
- **Entraînement :** aucune permission n’est déduite d’un autre usage.
- **Dépôt :** les documents sensibles restent hors du public.
- **Retrait :** la procédure identifie les dérivés affectés.

## 61. Livrables et état de maturité

Les livrables permanents sont un jeu de visèmes, un profil de rig facial, des mappings linguistiques, un pipeline de timing, une animation pilote et des rapports de validation.

Chaque livrable progresse de brouillon à candidat, revu puis approuvé. La présence d’un fichier ne suffit pas à changer son état.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facial_deliverables:
  viseme_set: AST-FACE-VISEME-SET-001
  rig_profile: AST-FACE-PROFILE-SCOUT-001
  language_profiles:
    - AST-FACE-LANG-FR-001
    - AST-FACE-LANG-EN-001
  timing_pipeline: AST-FACE-TIMING-PIPELINE-001
  pilot_animation: AST-FACE-ANIM-RELAY-SCOUT-001
  validation_campaign: AST-FACE-VALIDATION-001
  states: [draft, candidate, reviewed, approved, withdrawn]
  automatic_state_promotion: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Visèmes :** le jeu possède une identité propre.
- **Profil :** le personnage relie canaux et limites du rig.
- **Langues :** chaque locale reçoit un mapping versionné.
- **Campagne :** les preuves de distance et performance sont regroupées.
- **État :** seule une décision explicite promeut un livrable.

## 62. Diagnostics et corrections

<!-- qa:error-correction-section -->

Les cas suivants décrivent des défauts fréquents de synchronisation labiale et leur correction. Chaque correction reste à vérifier sur les personnages, langues et caméras réellement utilisés.

### 62.1 Les lettres du sous-titre pilotent directement la bouche

**Symptôme ou risque :** la prononciation réelle diverge du texte et les visèmes arrivent au mauvais moment.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lip_sync:
  input: subtitle_characters
  mapping:
    "p": VSM_MBP
    "h": VSM_A
  timing: fixed_milliseconds_per_letter
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le système confond écriture et son, ignore les lettres muettes, les digrammes, la durée réelle et les variantes de prononciation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lip_sync:
  input: reviewed_phone_intervals
  language_profile: AST-FACE-LANG-FR-001
  mapping: phone_to_viseme
  timing_origin: approved_runtime_audio
  unknown_phone: error
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les phones relus et alignés sur la voix réelle alimentent un mapping linguistique versionné ; les unités inconnues bloquent au lieu d’être devinées.

### 62.2 Tous les phonèmes reçoivent un visème distinct

**Symptôme ou risque :** le rig contient des dizaines de formes très proches, difficiles à sculpter et impossibles à lire à distance.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
viseme_policy:
  one_shape_per_phone: true
  phone_count: 42
  language_scope: assumed_universal
  distance_review: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le nombre de formes suit l’inventaire acoustique plutôt que les différences visibles et multiplie les coûts sans preuve de lisibilité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
viseme_policy:
  grouped_by_visible_articulation: true
  minimal_set: character_and_language_qualified
  language_specific_extensions: allowed
  distance_review: required
  corrective_shapes: separate
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les phones sont regroupés par apparence utile, les extensions restent possibles et les correctifs ne deviennent pas des visèmes.

### 62.3 L’alignement automatique est publié sans revue

**Symptôme ou risque :** les noms propres, cris et chuchotements produisent des frontières incorrectes qui arrivent directement dans le jeu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
alignment:
  tool_output: final
  out_of_vocabulary_words: ignored
  confidence_review: none
  expressive_delivery: accepted_automatically
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un aligneur produit une hypothèse dépendante du dictionnaire, du modèle et de la prise ; les cas atypiques ne sont ni signalés ni corrigés.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
alignment:
  tool_output: draft
  out_of_vocabulary_words: blocking_flag
  review_queue: [low_confidence, overlap, shout, whisper, proper_name]
  human_approval: required
  published_asset: versioned_after_review
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le résultat automatique reste un brouillon, les risques alimentent une file de revue et seule une version approuvée devient publiable.

### 62.4 Les visèmes sont des clés carrées sans coarticulation

**Symptôme ou risque :** la bouche saute d’une pose à l’autre et chaque syllabe paraît mécanique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
curves:
  interpolation: constant
  anticipation: 0
  release: 0
  overlap: forbidden
  pose_weight: 1.0_for_every_phone
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les transitions ignorent l’anticipation et le relâchement naturels ; des poids identiques écrasent les différences de durée et d’importance.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
curves:
  interpolation: clamped_cubic
  anticipation: profile_candidate
  release: profile_candidate
  overlap: priority_blend
  pose_weight: context_and_rig_dependent
  saturation_report: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Des enveloppes bornées se chevauchent selon des priorités lisibles, tandis que les poids restent liés au rig et au contexte.

### 62.5 Le volume sonore pilote directement l’ouverture de mâchoire

**Symptôme ou risque :** les consonnes fortes ouvrent la bouche et les voyelles calmes deviennent invisibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
jaw_driver:
  input: audio_rms
  mapping: linear_0_to_1
  smoothing_ms: 250
  phoneme_data: ignored
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’amplitude ne décrit ni le lieu d’articulation ni la forme des lèvres ; le lissage ajoute en plus un retard uniforme.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
jaw_driver:
  input: reviewed_viseme_pose
  articulation: phone_and_language_profile
  prosody_modifier: bounded_optional
  smoothing: per_channel
  audio_rms: diagnostic_only
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La mâchoire vient de la pose articulatoire, la prosodie reste un modificateur borné et l’amplitude ne sert qu’au diagnostic.

### 62.6 Les expressions écrasent les fermetures de lèvres

**Symptôme ou risque :** un sourire ou une grimace empêche les bilabiales et rend certains mots illisibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
face_layers:
  speech_weight: 1.0
  expression_weight: 1.0
  shared_lip_channels: unrestricted
  corrective_shapes: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Deux couches écrivent les mêmes canaux sans masque ni priorité, puis aucune forme corrective ne résout les combinaisons extrêmes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
face_layers:
  speech_priority: intelligibility
  expression_masks: explicit
  shared_lip_channels: bounded
  corrective_shapes: evaluated_after_blend
  extreme_emotion_review: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les canaux partagés sont bornés, la parole conserve ses contacts essentiels et les combinaisons difficiles activent des correctifs revus.

### 62.7 Le signal de fin d’animation valide le dialogue

**Symptôme ou risque :** une animation interrompue ou désactivée en LOD modifie l’état narratif.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func _on_face_animation_finished() -> void:
    dialogue_service.mark_line_heard(line_id)
    quest.complete_objective(objective_id)
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une couche de présentation acquiert l’autorité métier et rend la progression dépendante du rendu, du LOD ou d’un bug facial.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func on_dialogue_line_committed(event: DialogueLineCommitted) -> void:
    facial_presenter.request_take(event.face_cue_id)

func _on_face_animation_finished() -> void:
    facial_presenter.release_take()
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le domaine commet d’abord la réplique puis demande la présentation ; la fin d’animation ne gère que le cycle de vie facial.

### 62.8 Les timings sont réutilisés après remplacement de la voix

**Symptôme ou risque :** les lèvres restent calées sur une ancienne prise dont les silences et le débit ont changé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
timing_asset:
  audio_path: res://audio/voice/latest.ogg
  audio_hash: absent
  reuse_after_audio_change: true
  transcript_version: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le chemin mutable ne permet pas de savoir quelle prise a produit les timings et aucune invalidation n’est déclenchée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
timing_asset:
  audio_asset_id: AST-AUD-VOICE-SCOUT-001
  audio_version: 2.0.0
  audio_sha256: measured
  transcript_id: AST-TXT-RELAY-SCOUT-001
  invalidation: regenerate_and_review
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Identité, version, empreinte et transcription lient le dérivé à sa source ; tout changement temporel force une régénération et une revue.

### 62.9 Un profil facial unique est utilisé pour gros plan et foule

**Symptôme ou risque :** des dizaines de canaux sont évalués sur tous les personnages et les visages lointains oscillent entre niveaux.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
facial_quality:
  profile: universal
  blendshape_channels: all
  update_hz: frame_rate
  active_faces: unlimited
  lod_hysteresis: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le coût n’est pas borné, aucun détail n’est adapté à la taille écran et les changements de niveau peuvent clignoter.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
facial_quality:
  profiles: [hero_close_up, gameplay_mid, crowd_low]
  priority_inputs: [screen_size, current_speaker, camera_focus]
  active_faces: measured_limit
  update_hz: per_profile_candidate
  lod_hysteresis: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les profils réduisent les canaux et fréquences selon l’importance, tandis qu’une limite mesurée et une hystérésis stabilisent la foule.

### 62.10 La sortie automatique est déclarée approuvée

**Symptôme ou risque :** un outil de timing ou un modèle facial publie seul une animation sans contrôle de langue, d’acting ou de droits.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
automation:
  output_status: approved
  human_review: optional
  language_profile: inferred
  consent_scope: ignored
  runtime_benchmark: assumed_pass
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le système mélange génération, décision artistique, qualification juridique et preuve de performance sans autorité humaine.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
automation:
  output_status: draft
  language_profile: explicit
  consent_scope_reference: required
  human_review: required
  runtime_benchmark: separate_evidence
  approval_authority: named_role
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La sortie reste un brouillon, les dépendances sont explicites et l’approbation exige une personne ainsi que des preuves runtime séparées.

## 63. Checklist de production et validation

La checklist reste ouverte tant que les fichiers, rigs, scènes et mesures n’existent pas. Un exemple de configuration ou une revue statique ne coche aucune case.

- [ ] voix runtime, transcription et locale identifiées ;
- [ ] droits vocaux, vidéo et capture faciale qualifiés ;
- [ ] pose neutre et rig facial versionnés ;
- [ ] noms de blendshapes validés par identifiant ;
- [ ] jeu minimal de visèmes testé sur plusieurs personnages ;
- [ ] lexique et inventaire de phones qualifiés par langue ;
- [ ] TextGrid ou format de timing validé ;
- [ ] alignement automatique revu humainement ;
- [ ] inconnues, chevauchements et valeurs non finies refusés ;
- [ ] coarticulation, attaques et relâchements évalués ;
- [ ] fermetures bilabiales et labiodentales lisibles ;
- [ ] expression et parole mélangées sans perte de contact ;
- [ ] regard, clignements et gestes complémentaires revus ;
- [ ] profils gros plan, gameplay et foule matérialisés ;
- [ ] compression et réduction de clés comparées ;
- [ ] tests multi-voix et multi-langues exécutés ;
- [ ] tests gros plan, distance et foule capturés ;
- [ ] CPU, mémoire, allocations et nombre de visages mesurés ;
- [ ] réimportation et canaux manquants testés ;
- [ ] approbations artistique, linguistique, technique et juridique consignées.

## 64. Références techniques officielles

Les pages suivantes documentent les mécanismes d’animation, de blend shapes et d’annotation utilisés comme références. Elles ne remplacent ni la revue d’acting, ni la qualification d’un aligneur, ni les tests runtime.

- [Godot 4.7 — Types de pistes d’animation](https://docs.godotengine.org/en/4.7/tutorials/animation/animation_track_types.html)
- [Godot 4.7 — Utiliser `AnimationTree`](https://docs.godotengine.org/en/4.7/tutorials/animation/animation_tree.html)
- [Godot 4.7 — `AnimationPlayer`](https://docs.godotengine.org/en/4.7/classes/class_animationplayer.html)
- [Godot 4.7 — `AnimationTree`](https://docs.godotengine.org/en/4.7/classes/class_animationtree.html)
- [Godot 4.7 — `Animation`](https://docs.godotengine.org/en/4.7/classes/class_animation.html)
- [Godot 4.7 — `Mesh`](https://docs.godotengine.org/en/4.7/classes/class_mesh.html)
- [Blender Manual — Introduction aux Shape Keys](https://docs.blender.org/manual/en/latest/animation/shape_keys/introduction.html)
- [Blender Manual — Drivers](https://docs.blender.org/manual/en/latest/animation/drivers/index.html)
- [Praat — Objet `TextGrid`](https://praat.org/manual/TextGrid.html)
- [Praat — Formats de fichier `TextGrid`](https://praat.org/manual/TextGrid_file_formats.html)
- [Montreal Forced Aligner 3.4 — Guide utilisateur](https://montreal-forced-aligner.readthedocs.io/en/v3.4.1/user_guide/index.html)
- [Montreal Forced Aligner — Évaluer les alignements](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/evaluating_alignments.html)
- [Livre III — Chapitre 10 : Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)
- [Livre III — Chapitre 19 : Rigging et skinning](CHAPITRE-19-Rigging-et-skinning.md)
- [Livre III — Chapitre 20 : Animation procédurale et animation par keyframes](CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md)
- [Livre III — Chapitre 26 : Voix, bruitages, ambiances et musique](CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md)


## 65. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-FACE-PILOT-RELAY-DIALOGUE-001` comme pilote de synchronisation labiale. La chaîne consomme la voix approuvée `AST-AUDIO-PILOT-RELAY-STORM-001`, un profil de rig facial, une transcription, un lexique et un mapping linguistique versionnés.

La porte d’acceptation combine intelligibilité, acting, stabilité des formes, qualité des timings, absence d’intersections, compatibilité linguistique, LOD, coût runtime, droits et approbation humaine. Tant que les formes, timings, scènes et mesures ne sont pas matérialisés, le chapitre reste au niveau `static-review`.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_facial_decisions:
  pilot_id: AST-FACE-PILOT-RELAY-DIALOGUE-001
  viseme_set_id: AST-FACE-VISEME-SET-001
  timing_pipeline_id: AST-FACE-TIMING-PIPELINE-001
  rig_profile_id: AST-FACE-PROFILE-SCOUT-001
  reference_language_profile: AST-FACE-LANG-FR-001
  pilot_animation_id: AST-FACE-ANIM-RELAY-SCOUT-001
  validation_campaign_id: AST-FACE-VALIDATION-001
  source_rule: approved_audio_and_reviewed_transcript
  authority_rule: domain_commit_before_facial_request
  automation_rule: generated_output_is_draft
  acceptance: artistic_plus_linguistic_plus_technical_plus_rights_plus_runtime
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** le dialogue du relais concentre voix, visage, regard et LOD.
- **Visèmes :** le jeu minimal et les profils linguistiques restent versionnés.
- **Pipeline :** alignement, revue, mapping et courbes forment des dérivés traçables.
- **Autorité :** la présentation faciale suit une réplique déjà committée.
- **Réserve :** aucun rig, timing, clip, scène ou benchmark n’est déclaré produit.
