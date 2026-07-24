---
title: "Livre III — Chapitre 26 : Voix, bruitages, ambiances et musique"
id: "DOC-L3-CH26"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 26
last-verified: "2026-07-24T22:50:00+02:00"
audit-status: "complete"
audit-date: "2026-07-24T22:50:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-26.md"
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

# Voix, bruitages, ambiances et musique

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH26`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Une chaîne audio fiable transforme des sources enregistrées, générées ou montées en ressources identifiées, traçables, intégrables et mesurables. Elle sépare la prise brute, le dérivé de travail, le master, l’export runtime et le mix réellement entendu dans le jeu.

Le chapitre couvre la voix, les bruitages, les ambiances et la musique sans donner à un fichier audio, à un bus ou à un événement de lecture l’autorité de décider une règle gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: recorded_generated_or_licensed_audio_sources
  transformation: edited_versioned_and_qualified_audio_assets
  output: godot_streams_buses_events_and_measurement_plan
  authority: presentation_and_feedback_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** les sources restent distinctes selon leur origine, leurs droits et leur état de traitement.
- **Transformation :** le montage, le nettoyage et le mix produisent des dérivés versionnés sans écraser la prise brute.
- **Sortie :** Godot reçoit des flux, scènes et presets préparés mais non déclarés exécutés.
- **Autorité :** la lecture audio représente un événement déjà décidé par les systèmes métier.
- **Preuve :** aucun enregistrement, fichier, bus, mesure ou benchmark n’est présenté comme matérialisé.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura classer les familles audio, choisir une chaîne de capture ou de génération, nettoyer sans détruire la source, préparer des boucles et organiser les variantes.

Il saura aussi configurer conceptuellement les lecteurs et bus Godot, préparer la spatialisation, documenter la provenance, estimer la mémoire et construire une campagne de mesure.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  production: [recording, generation, editing, restoration, mastering]
  assets: [voice, sfx, ambience, music, loop, variation]
  integration: [stream_players, buses, effects, zones, events]
  measurement: [loudness, true_peak, memory, concurrency, latency]
  governance: [consent, licence, provenance, withdrawal, reservations]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Production :** les opérations sont classées depuis la source jusqu’au master et à l’export runtime.
- **Assets :** chaque famille reçoit des contraintes de durée, de boucle, de canaux et de variation.
- **Intégration :** les nœuds et bus sont choisis selon le rôle spatial et le coût attendu.
- **Mesure :** loudness, crête vraie, mémoire et voix simultanées restent des dimensions séparées.
- **Gouvernance :** droits, consentements et retraits accompagnent la ressource pendant tout son cycle.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les valeurs numériques proposées sont des cibles candidates ou des exemples de structure ; elles doivent être remplacées ou confirmées par des mesures réelles dans le build et sur les plateformes visées.

La recommandation ITU-R BS.1770-5 décrit des algorithmes de mesure de l’intensité sonore et de la crête vraie. Elle ne fournit pas à elle seule une cible universelle de jeu, car l’usage, la plateforme et la politique de mix restent à définir.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  recordings_created: false
  generated_audio_created: false
  godot_bus_layout_created: false
  loudness_measurements_recorded: false
  memory_profile_recorded: false
  runtime_playback_tested: false
  legal_clearance_completed: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est vérifiée contre des sources officielles sans revendiquer une production terminée.
- **Audio :** aucune prise, génération, restauration, boucle ou export n’est annoncé comme existant.
- **Godot :** aucun bus, effet, scène ou lecteur n’est déclaré configuré dans un projet réel.
- **Mesures :** les objectifs restent candidats jusqu’à une campagne de loudness, mémoire et concurrence.
- **Publication :** le PDF du Livre III reste différé jusqu’à la fin du Livre.

## 4. Frontières avec les chapitres voisins

Le Livre I conserve l’installation des outils audio locaux. Le présent chapitre possède la production, le catalogage, le mix et l’intégration des ressources audio.

Le chapitre 27 utilisera les voix approuvées et leurs timings pour les visèmes et l’animation faciale ; il ne redéfinira ni le consentement, ni le montage, ni les bus de mix.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  book_i_chapter_09: local_audio_tool_installation
  book_iii_chapter_26: audio_sources_assets_mix_and_godot_integration
  book_iii_chapter_27: phonemes_visemes_and_facial_timing
  book_ii_domain: authoritative_game_events
  invariant: audio_playback_never_commits_domain_state
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Livre I :** l’installation et la qualification des applications restent hors du présent chapitre.
- **Chapitre 26 :** la chaîne audio conserve l’autorité sur les sources, dérivés, exports et presets.
- **Chapitre 27 :** la synchronisation faciale consomme une voix et des timings déjà publiés.
- **Gameplay :** les événements métier déclenchent l’audio, jamais l’inverse.
- **Invariant :** un signal de fin de lecture ne devient pas une preuve de réussite gameplay.

## 5. Pilote audio de Project Asteria

Le pilote `AST-AUDIO-PILOT-RELAY-STORM-001` reprend la station-relais, l’éclaireur et l’orage déjà employés par les chapitres 22 et 23. Il limite la campagne à un dialogue radio court, des pas, une porte métallique, une ambiance d’orage, un signal d’alerte et une transition musicale.

Ce lot permet d’évaluer voix, SFX, ambiance, musique, spatialisation et ducking sans prétendre couvrir toute la bibliothèque du jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_audio_pilot:
  id: AST-AUDIO-PILOT-RELAY-STORM-001
  scene_context: abandoned_relay_during_storm
  assets:
    voice: [scout_radio_line, remote_reply]
    sfx: [rubble_steps, metal_door, relay_switch]
    ambience: [wind_bed, rain_layers, distant_thunder]
    music: [exploration_stem, alert_transition]
  integration_targets: [cinematic, gameplay, ui_warning]
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** le pilote réutilise un lieu et une séquence déjà documentés sans recréer leur mise en scène.
- **Voix :** les deux lignes servent à tester intelligibilité, traitement radio et provenance.
- **SFX :** les sons courts couvrent variation, position 3D et concurrence.
- **Ambiance :** les couches longues servent aux boucles, zones et mémoire.
- **Musique :** les stems et transitions restent des candidats de structure à produire et mesurer.

## 6. Typologie fonctionnelle des ressources audio

Une bibliothèque ne se classe pas seulement par extension. La fonction détermine le mode de lecture, la spatialisation, la priorité, la persistance et la stratégie de compression.

Une même source peut produire plusieurs dérivés, mais chaque dérivé possède un identifiant et un usage explicite.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_families:
  voice:
    traits: [semantic, consent_sensitive, localization_sensitive]
  sfx:
    traits: [short, event_bound, often_variable]
  ambience:
    traits: [long, looped, layered, spatial_or_global]
  music:
    traits: [long, structured, transition_sensitive]
  ui:
    traits: [non_positional, brief, high_readability]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Voix :** le contenu sémantique et les droits imposent une traçabilité renforcée.
- **SFX :** la répétition rapide exige des variantes et une politique de concurrence.
- **Ambiance :** les longues durées rendent la boucle, la mémoire et les zones déterminantes.
- **Musique :** les transitions et les stems doivent conserver une structure temporelle cohérente.
- **UI :** les confirmations courtes privilégient la lisibilité et une lecture non positionnelle.

## 7. Séparer source, travail, master et export runtime

La prise brute ou le fichier source reste immuable. Les opérations de nettoyage et montage s’enregistrent dans un projet de travail ou produisent un nouveau dérivé.

Le master conserve une qualité suffisante pour de futurs exports ; l’export runtime est optimisé pour Godot et ne remplace jamais le master.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_asset_states:
  source_raw: immutable
  work_session: editable_non_destructive
  edited_master: versioned_high_quality
  runtime_export: derived_platform_profile
  imported_resource: engine_generated_cache
  published_asset: approved_identity_and_manifest
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la prise originale ou le fichier licencié garde son empreinte et son statut initial.
- **Travail :** les coupes, fades et traitements restent révisables sans modifier la source.
- **Master :** la version éditée sert d’autorité pour les exports futurs.
- **Runtime :** la compression et les canaux répondent à un profil de plateforme.
- **Publication :** l’asset approuvé relie identité, manifeste, droits, master et export.

## 8. Arborescence de production audio

Les chemins séparent les sources restreintes, les sessions de travail, les masters, les exports et les rapports. Les enregistrements contenant des données personnelles ne sont pas placés dans le dépôt public.

Le projet Godot reçoit seulement les dérivés autorisés à être distribués.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
audio/
├── restricted_sources/
│   ├── voices/
│   └── contracts_and_consents/
├── work/
│   ├── editing_sessions/
│   └── renders_for_review/
├── masters/
│   ├── voice/
│   ├── sfx/
│   ├── ambience/
│   └── music/
├── runtime_exports/
└── reports/
    ├── manifests/
    └── loudness/
res://audio/
├── streams/
├── scenes/
└── bus_layouts/
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Restreint :** les identités, contrats et prises sensibles restent dans un stockage à accès limité.
- **Travail :** les sessions et rendus de revue ne sont pas confondus avec des masters approuvés.
- **Masters :** chaque famille possède une source éditée versionnée.
- **Exports :** les fichiers runtime sont régénérables depuis le master et le profil.
- **Godot :** le dépôt du jeu ne contient que les ressources distribuables et leurs métadonnées utiles.

## 9. Identifiants et manifeste de ressource

Un nom de fichier lisible ne suffit pas à suivre les versions et les droits. L’identifiant stable reste indépendant du libellé affiché et de l’emplacement.

Le manifeste relie la fonction, la source, les transformations, les fichiers et les réserves.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_asset:
  id: AST-AUD-SFX-RELAY-DOOR-001
  version: 1.0.0
  family: sfx
  role: metal_door_open
  source_ids: [AST-AUD-SRC-FOLEY-014]
  master_path: masters/sfx/relay_door_open_v001.wav
  runtime_profiles: [desktop_reference]
  licence_status: pending_review
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** l’ID reste stable même si le fichier ou le libellé change.
- **Version :** une modification audible publiée crée une nouvelle version.
- **Sources :** toute couche ou prise contributrice reste référencée.
- **Profils :** les exports runtime sont liés à une configuration de plateforme.
- **Statut :** un droit ou une matérialisation inconnus bloquent l’acceptation.

## 10. Consentement et droits pour la voix

Une autorisation d’enregistrement ne doit pas être interprétée comme une permission générale de modifier, commercialiser, redistribuer, entraîner un modèle ou cloner une voix. Chaque usage reste qualifié séparément.

Les documents sensibles et l’identité réelle restent hors du dépôt public ; le manifeste public utilise une référence de preuve et un statut.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
voice_rights:
  performer_id: restricted_reference
  scopes:
    recording: required
    editing: explicit
    commercial_use: explicit
    redistribution: explicit
    model_training: separate_decision
    voice_cloning: separate_decision
  territory: documented
  duration: documented
  withdrawal_process: documented
  public_personal_data: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interprète :** l’identité complète est conservée dans un registre restreint.
- **Portées :** chaque exploitation reçoit une décision séparée et vérifiable.
- **Durée :** territoire, période et conditions de retrait sont consignés.
- **IA :** entraînement et clonage ne sont jamais déduits d’une autorisation générale.
- **Public :** le dépôt distribué ne contient ni contrat, ni signature, ni donnée personnelle.

## 11. Préparer une session d’enregistrement

La qualité d’une voix dépend davantage d’une préparation reproductible que d’un correctif extrême après coup. La session déclare le lieu, le microphone, la distance, le gain, le format, le texte et les conditions de silence.

Une courte prise de bruit de fond aide à documenter l’environnement, sans justifier une réduction de bruit agressive.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
recording_session:
  id: AST-AUD-REC-VOICE-001
  room: controlled_quiet_space
  microphone: qualified_model_and_pattern
  distance_cm: candidate_and_measured
  sample_format: pcm_24_bit
  sample_rate_hz: 48000
  peak_margin_dbfs: candidate_not_measured
  room_tone_seconds: recorded_before_and_after
  script_version: AST-DLG-RELAY-001-v1
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Session :** un identifiant relie les prises, le texte et la configuration.
- **Microphone :** le modèle, la directivité et la distance doivent être reproductibles.
- **Format :** le PCM de travail conserve une marge d’édition avant l’export runtime.
- **Niveau :** la marge de crête reste une cible à vérifier pendant la capture.
- **Texte :** la version du script empêche de mélanger des formulations différentes.

## 12. Chaîne de capture et surveillance

Le gain d’entrée évite à la fois le clipping et un niveau inutilement faible. Un limiteur de sécurité ne répare pas une saturation déjà produite dans le microphone ou le préampli.

La surveillance au casque vérifie les bruits, frottements, plosives et pertes de connexion pendant la session.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
capture_chain:
  performer: source
  room: acoustic_context
  microphone: transducer
  preamp_gain: set_before_take
  interface_converter: pcm_capture
  recorder: writes_immutable_take
  monitoring: closed_back_headphones
  safety_rule: no_stage_may_clip
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la performance et la pièce sont les premières composantes du signal.
- **Transduction :** microphone et préampli doivent rester dans une plage propre.
- **Conversion :** l’interface écrit un flux PCM selon le format déclaré.
- **Surveillance :** le casque permet de détecter un défaut avant de multiplier les prises.
- **Sécurité :** un étage saturé ne peut pas être restauré par un traitement ultérieur.

## 13. Slate, prises et sélection

Chaque prise porte un numéro, une version de texte et un commentaire court. La sélection ne supprime pas les prises non retenues ; elle crée une décision réversible.

Les meilleures portions de plusieurs prises peuvent être assemblées, mais le montage conserve la provenance de chaque segment.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
take_log:
  session_id: AST-AUD-REC-VOICE-001
  line_id: AST-DLG-RELAY-001-L03
  takes:
    - {take: 1, status: alternate, note: clean_but_flat}
    - {take: 2, status: selected, note: clear_intention}
    - {take: 3, status: hold, note: strong_breath_noise}
  comp_map:
    selected_segments: [take_2_main, take_1_final_word]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ligne :** l’identité du dialogue reste séparée du numéro de prise.
- **Statut :** selected, alternate et hold décrivent une décision sans détruire les fichiers.
- **Note :** le commentaire cite un fait audible et évite les jugements vagues.
- **Montage :** le comp map relie chaque segment à sa prise d’origine.
- **Révision :** une nouvelle sélection peut être reconstruite depuis les sources immuables.

## 14. Génération de voix, SFX ou musique

Une sortie générée reste un brouillon tant que les modèles, licences, entrées, paramètres, consentements et conditions d’exploitation ne sont pas qualifiés. Une ressemblance involontaire ou une donnée d’entrée non autorisée peut bloquer la publication.

La seed seule ne garantit pas une reproduction identique si le modèle, l’application ou le graphe change.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
generated_audio_run:
  id: AST-AUD-GEN-RUN-001
  tool_version: qualified_or_pending
  model_id: exact_model_and_revision
  model_licence: exact_or_blocked
  input_rights: reviewed
  prompt_or_controls: archived_restricted_if_sensitive
  seed: recorded
  output_status: draft
  human_selection: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outil :** l’application et sa version font partie de la provenance.
- **Modèle :** l’identifiant, la révision et la licence sont conservés.
- **Entrées :** les textes, références ou voix doivent être autorisés pour l’usage visé.
- **Reproduction :** seed, paramètres et environnement sont requis ensemble.
- **Décision :** la sortie n’est publiée qu’après revue humaine et qualification juridique.

## 15. Nettoyage non destructif

Le nettoyage retire seulement les défauts réellement identifiés : bruit stationnaire, clics, plosives, résonance ou souffle excessif. Une réduction trop forte crée des artefacts et dégrade les consonnes.

Chaque traitement est comparé en bypass à niveau perçu comparable afin de ne pas confondre volume plus fort et qualité supérieure.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
restoration_chain:
  high_pass: only_if_low_frequency_noise_is_confirmed
  de_click: event_based
  de_plosive: localized
  noise_reduction: conservative_profile
  de_esser: frequency_and_threshold_reviewed
  room_tone: preserved_between_edits
  comparison: loudness_matched_bypass
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Filtrage :** un passe-haut n’est appliqué que si le contenu utile reste intact.
- **Réparation :** clics et plosives sont traités localement plutôt que par un réglage global.
- **Bruit :** la réduction reste conservative pour éviter les textures métalliques.
- **Continuité :** le room tone évite des silences artificiels entre les coupes.
- **Comparaison :** le bypass à niveau égal révèle le bénéfice réel du traitement.

## 16. Montage, fades et silences

Une coupe propre respecte l’attaque, la respiration, la fin de mot et le bruit de fond. Les fades courts évitent les clics sans gommer la consonne ou l’impact.

Les silences narratifs ne sont pas automatiquement supprimés : ils appartiennent au rythme et doivent être distingués des marges techniques.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
edit_decisions:
  trim:
    preserve_pre_roll_ms: candidate
    preserve_tail_ms: candidate
  fades:
    fade_in: short_and_auditioned
    fade_out: follows_room_tone
  breaths:
    policy: keep_reduce_or_remove_by_intent
  silence:
    narrative_pause: preserve
    accidental_gap: repair
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pré-roll :** une marge avant la phrase conserve l’attaque et facilite la synchronisation.
- **Fades :** les courbes éliminent les discontinuités sans amputer le signal utile.
- **Respirations :** la décision dépend du jeu d’acteur et non d’une suppression automatique.
- **Pause :** un silence intentionnel reste une composante du rythme.
- **Réparation :** les trous accidentels utilisent un room tone cohérent et traçable.

## 17. Comprendre niveau de crête, RMS et loudness

La crête décrit un maximum instantané, le RMS une énergie moyenne sur une fenêtre et le loudness une estimation pondérée de la perception. Ces mesures répondent à des questions différentes.

Le mix ne doit pas remplacer une mesure par une autre ni comparer des fichiers sur des fenêtres incompatibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
level_metrics:
  sample_peak:
    purpose: detect_digital_sample_maximum
  true_peak:
    purpose: estimate_inter_sample_peak
  rms:
    purpose: describe_average_energy_window
  loudness:
    purpose: perceptual_weighted_program_measure
  rule: record_method_window_and_units
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Crête échantillon :** elle contrôle les valeurs numériques présentes dans le flux discret.
- **Crête vraie :** elle estime les dépassements possibles entre échantillons lors de la reconstruction.
- **RMS :** la fenêtre et le canal influencent la valeur d’énergie moyenne.
- **Loudness :** l’algorithme et la durée de mesure doivent être documentés.
- **Comparabilité :** méthode, unité et fenêtre accompagnent toujours le résultat.

## 18. Objectifs candidats de loudness

Le pilote définit des plages candidates par famille afin de préparer les mesures, pas pour imposer une norme universelle. Un dialogue radio, une ambiance et un impact n’ont ni la même durée ni la même fonction.

Les valeurs finales seront ajustées après écoute calibrée, mesure BS.1770, test de gameplay et comparaison entre profils.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
candidate_loudness_policy:
  voice_dialogue:
    metric: integrated_or_short_term_by_asset
    target: project_specific_pending_measurement
  ambience:
    metric: long_term_layer_and_mix_context
    target: below_critical_information
  sfx:
    metric: short_term_plus_true_peak
    target: role_and_priority_dependent
  music:
    metric: integrated_by_section_and_mix_state
    target: preserves_voice_and_gameplay_cues
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Voix :** la mesure choisie dépend de la durée et de l’intelligibilité dans le mix.
- **Ambiance :** le lit sonore ne doit pas masquer les signaux prioritaires.
- **SFX :** l’impact est évalué avec sa crête et son contexte de concurrence.
- **Musique :** les sections et états de mix sont comparés séparément.
- **Validation :** aucune cible n’est acceptée avant mesure et écoute dans le build.

## 19. Crête vraie et marge de sécurité

Un fichier sans clipping d’échantillon peut encore produire une crête inter-échantillon lors de la conversion ou de la lecture. La crête vraie complète donc le contrôle du maximum numérique.

La marge candidate doit être vérifiée après les traitements et après l’encodage runtime, car la compression avec perte peut modifier les crêtes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
peak_control:
  source_capture: avoid_analog_and_converter_clipping
  master:
    sample_peak_checked: true
    true_peak_checked: true
  runtime_encode:
    decode_and_remeasure: required
  limiter:
    role: safety_not_loudness_target
  final_margin: platform_profile_pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capture :** la prévention commence avant la conversion numérique.
- **Master :** crête d’échantillon et crête vraie sont contrôlées séparément.
- **Encodage :** le fichier compressé est décodé et remesuré.
- **Limiteur :** il ne doit pas servir à fabriquer artificiellement la cible de loudness.
- **Profil :** la marge finale dépend de la plateforme et reste à qualifier.

## 20. Choisir WAV, Ogg Vorbis ou MP3 dans Godot

Godot propose des options d’import différentes pour WAV et pour Ogg Vorbis ou MP3. Le choix dépend de la durée, de la mémoire, de la boucle, de la latence et de la qualité attendue.

Le master de production reste généralement sans perte, tandis que l’export runtime peut utiliser une compression adaptée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
format_decision:
  wav:
    preferred_for: [short_latency_sensitive_sfx, seamless_pcm_loop_candidates]
    cost: larger_memory_or_storage
  ogg_vorbis:
    preferred_for: [long_ambience, music, voice_when_profile_allows]
    cost: decode_and_lossy_artifacts_to_measure
  mp3:
    preferred_for: [compatibility_specific_use]
    cautions: [loop_padding, lossy_generation, profile_review]
  rule: choose_from_measured_use_not_habit
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **WAV :** les sons courts et sensibles à la latence peuvent privilégier un flux PCM ou compressé sans perte selon l’import.
- **Ogg :** les ressources longues réduisent souvent le stockage au prix d’un décodage et d’artefacts à contrôler.
- **MP3 :** les boucles et délais d’encodage exigent une écoute et une inspection spécifiques.
- **Master :** le format de travail reste distinct du fichier importé dans le moteur.
- **Décision :** durée, concurrence, plateforme et mesure déterminent le profil.

## 21. Fréquence d’échantillonnage, profondeur et canaux

La fréquence d’échantillonnage décrit le nombre d’échantillons par seconde ; la profondeur de bits du PCM décrit la résolution d’amplitude. Elles ne sont ni un FPS d’animation ni une garantie de qualité audible.

Les canaux sont choisis selon l’usage. Un son mono est souvent adapté à une source 3D ponctuelle, tandis qu’une ambiance ou une musique stéréo peut rester non positionnelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
sample_specification:
  production_master:
    sample_rate_hz: 48000
    pcm_bit_depth: 24
  runtime:
    sample_rate_hz: profile_and_source_dependent
    channel_policy:
      point_source_3d: mono_preferred
      ui_and_music: stereo_when_required
      ambience: mono_emitters_plus_stereo_bed_as_designed
  resampling: single_controlled_stage_preferred
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fréquence :** 48 kHz sert ici de référence de travail candidate, pas de preuve de besoin universel.
- **Profondeur :** le PCM 24 bits offre une marge de production avant l’export.
- **Mono :** une source ponctuelle évite d’embarquer une image stéréo contradictoire avec la position 3D.
- **Stéréo :** la musique et les lits globaux peuvent conserver une image non positionnelle.
- **Conversion :** les rééchantillonnages multiples sont évités et documentés.

## 22. Importer les échantillons dans Godot

Le dock Import expose des options selon le format source. Le preset doit être versionné par famille et revu après toute modification de durée, boucle, compression ou canaux.

Une réimportation n’est pas une approbation : elle doit être écoutée et mesurée dans le contexte réel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_import_profile:
  id: AST-AUD-IMPORT-SFX-SHORT-001
  source_format: wav
  family: short_sfx
  loop: false
  compression_mode: candidate
  normalize: false_unless_measured_reason
  trim: false_when_timing_is_contract
  force_mono: source_and_usage_reviewed
  reimport_validation: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Preset :** l’identifiant relie les choix d’import à une famille audio.
- **Boucle :** le statut ne doit pas être activé sur un son qui possède une fin fonctionnelle.
- **Normalisation :** elle n’est pas utilisée pour masquer une chaîne de niveaux incohérente.
- **Trim :** la suppression de silence peut casser un timing ou une synchronisation.
- **Validation :** la ressource réimportée est réécoutée et remesurée.

## 23. Préparer une boucle sans clic

Une boucle propre exige un point de sortie et un point d’entrée compatibles en niveau, pente, timbre et contenu. Un simple découpage à un passage par zéro ne garantit pas la continuité d’un signal complexe.

Les couches d’ambiance longues peuvent utiliser un crossfade, mais sa durée et son contenu doivent rester perceptuellement invisibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
loop_design:
  source_id: AST-AUD-AMB-WIND-001
  loop_start_samples: measured
  loop_end_samples: measured
  continuity_checks:
    - waveform_level
    - waveform_slope
    - spectral_balance
    - modulation_phase
  crossfade:
    enabled: candidate
    duration_ms: auditioned
  tail_policy: separate_one_shot_if_needed
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Points :** les positions sont conservées en échantillons pour éviter un arrondi temporel ambigu.
- **Continuité :** niveau, pente, spectre et modulation sont comparés ensemble.
- **Crossfade :** la durée est écoutée sur plusieurs répétitions.
- **Queue :** une réverbération ou un impact terminal peut devenir un one-shot séparé.
- **Test :** la boucle est vérifiée après encodage et import Godot.

## 24. Métadonnées de boucle et transitions

Le fichier audio ne porte pas toujours de manière portable toutes les intentions de boucle. Le manifeste conserve donc les régions, marqueurs, quantifications et alternatives.

La musique interactive distingue boucle interne, intro, outro, stinger et point de transition.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
loop_manifest:
  asset_id: AST-AUD-MUS-EXPLORE-001
  regions:
    intro: {start_sample: 0, end_sample: 192000}
    loop: {start_sample: 192000, end_sample: 960000}
    outro: {start_sample: 960000, end_sample: 1152000}
  tempo_bpm: candidate_and_verified
  meter: "4/4"
  transition_grid: bar
  exported_regions: separate_streams
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Régions :** les limites sont décrites indépendamment du nom des fichiers.
- **Tempo :** la valeur est vérifiée contre les échantillons et le montage.
- **Mesure :** la signature rythmique structure les points de transition.
- **Grille :** la quantification à la mesure reste un contrat de lecture.
- **Exports :** intro, boucle et outro peuvent être publiées comme flux séparés.

## 25. Variantes et anti-répétition

La variation ne consiste pas à appliquer un pitch aléatoire illimité. Elle combine plusieurs prises ou couches, des écarts bornés et une mémoire courte qui évite de rejouer immédiatement le même fichier.

Le choix audio ne doit jamais modifier le résultat gameplay ; il ne change que la représentation sonore d’un événement déjà validé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
variation_set:
  id: AST-AUD-VAR-FOOTSTEP-RUBBLE-001
  assets: [step_01, step_02, step_03, step_04]
  selection: weighted_no_immediate_repeat
  history_size: 2
  pitch_range: [0.97, 1.03]
  gain_offset_db: [-1.0, 1.0]
  deterministic_gameplay_dependency: none
  saturation_policy: drop_low_priority_duplicate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ensemble :** plusieurs prises réelles réduisent la répétition mieux qu’une transformation extrême.
- **Historique :** la mémoire courte évite le dernier ou les deux derniers choix.
- **Pitch :** la plage reste étroite pour conserver matière et identité.
- **Gain :** les écarts sont bornés et ne remplacent pas le mix.
- **Autorité :** le tirage n’influence ni collision, ni dégâts, ni état du monde.

## 26. Superposer un bruitage

Un SFX peut combiner attaque, corps, texture et queue. Chaque couche doit apporter une fonction audible ; l’empilement gratuit augmente le coût, la densité et le risque de masquage.

Les couches conservent leurs sources et droits, puis le master résultant reçoit une nouvelle identité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
layered_sfx:
  id: AST-AUD-SFX-RELAY-SWITCH-001
  layers:
    transient: metal_click_source
    body: low_mechanical_thump
    texture: electrical_arc_short
    tail: room_reflection_render
  alignment: sample_checked
  phase_review: required
  source_manifest: complete_before_publish
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Attaque :** le transient rend l’action immédiatement identifiable.
- **Corps :** la composante basse donne masse sans masquer le dialogue.
- **Texture :** l’arc électrique précise la fonction de l’objet.
- **Queue :** la réverbération reste cohérente avec la zone.
- **Contrôle :** alignement, phase et provenance sont vérifiés avant publication.

## 27. Construire une ambiance en couches

Une ambiance crédible sépare un lit global stable, des émetteurs localisés et des événements rares. Cette structure permet de réduire une couche, déplacer une source ou changer la météo sans remplacer tout le fichier.

Les événements rares utilisent des intervalles bornés et une densité mesurée pour éviter la répétition perceptible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ambience_stack:
  id: AST-AUD-AMB-RELAY-STORM-001
  global_bed: wind_and_rain_wide
  positioned_emitters:
    - loose_panel_rattle
    - cable_hum
  rare_events:
    - distant_thunder
    - roof_impact
  density_profile: weather_state_candidate
  critical_signal_masking_review: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lit :** la couche large maintient la continuité du lieu.
- **Émetteurs :** les sources localisées renforcent la géométrie perçue.
- **Événements :** les occurrences rares restent séparées de la boucle.
- **Densité :** la fréquence dépend d’un profil d’ambiance, pas d’un hasard illimité.
- **Lisibilité :** les signaux gameplay et la voix sont testés contre le mix complet.

## 28. Organiser la musique en stems et états

Les stems permettent de modifier l’intensité sans couper brutalement la continuité. Ils exigent une durée, un tempo, une phase et un point de départ compatibles.

La logique métier choisit un état musical abstrait ; le système audio décide comment atteindre cet état sans donner à la musique l’autorité sur le gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
music_state:
  cue_id: AST-AUD-MUS-RELAY-001
  stems: [pulse, texture, low_strings, percussion]
  states:
    exploration: [pulse, texture]
    alert: [pulse, texture, low_strings]
    danger: [pulse, texture, low_strings, percussion]
  transition:
    quantization: next_bar
    fallback: crossfade_candidate
  authority: consumes_game_state_event
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Stems :** les fichiers partagent durée, tempo, grille et origine d’échantillon.
- **États :** chaque combinaison conserve une hiérarchie musicale lisible.
- **Transition :** la mesure suivante constitue une option à vérifier dans le build.
- **Repli :** un crossfade reste disponible lorsque la quantification n’est pas applicable.
- **Autorité :** le cue consomme un événement sans changer l’état de danger.

## 29. Utiliser `AudioStreamPlayer` pour les sons non positionnels

`AudioStreamPlayer` convient aux interfaces, menus et musiques de fond non positionnelles. La propriété `bus` route le flux et `max_polyphony` borne le nombre de lectures simultanées du nœud.

Changer la ressource `stream` arrête les sons en cours de ce lecteur ; le cycle de vie doit donc être explicite.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
extends AudioStreamPlayer

@export var cue_id: StringName
@export var default_bus: StringName = &"Music"

func configure(stream_resource: AudioStream) -> void:
    stream = stream_resource
    bus = default_bus
    max_polyphony = 1

func start(from_position: float = 0.0) -> void:
    play(from_position)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `AudioStreamPlayer` joue un flux sans position dans le monde.
- **Identité :** `cue_id` relie le nœud à un catalogue sans utiliser le chemin comme autorité.
- **Routage :** `bus` sélectionne le groupe de mix par son nom stable.
- **Polyphonie :** la valeur `1` interdit ici deux lectures simultanées du même lecteur musical.
- **Appel :** `play()` accepte une position de départ en secondes et ne retourne aucune valeur.

## 30. Utiliser `AudioStreamPlayer3D` pour une source localisée

`AudioStreamPlayer3D` positionne le son selon l’auditeur et expose atténuation, directionnalité et Doppler. Une source ponctuelle utilise de préférence un fichier mono afin que la spatialisation ne lutte pas contre une image stéréo intégrée.

La distance maximale et la courbe d’atténuation restent des paramètres à mesurer dans la scène.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
extends AudioStreamPlayer3D

@export var event_id: StringName
@export var max_hearing_distance_m: float = 24.0

func configure(stream_resource: AudioStream, target_bus: StringName) -> void:
    stream = stream_resource
    bus = target_bus
    max_distance = max_hearing_distance_m
    attenuation_model = AudioStreamPlayer3D.ATTENUATION_INVERSE_DISTANCE
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** le lecteur hérite de `Node3D` et possède une position dans la scène.
- **Distance :** `max_distance` borne la portée de calcul et d’audibilité candidate.
- **Modèle :** l’atténuation inverse reste une hypothèse à écouter et comparer.
- **Routage :** la source spatiale rejoint un bus de famille ou de zone.
- **Source :** le flux mono et la courbe doivent être qualifiés ensemble.

## 31. Atténuation, directionnalité et Doppler

L’atténuation simule la perte de niveau avec la distance, la directionnalité réduit le son hors axe et le Doppler modifie la hauteur selon le mouvement relatif. Ces effets doivent correspondre à la source et rester confortables.

Un filtre de distance ne doit pas masquer un mauvais mix ou une portée gameplay incohérente.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
spatial_profile:
  id: AST-AUD-SPATIAL-METAL-DOOR-001
  attenuation_model: inverse_distance_candidate
  unit_size_m: 1.0
  max_distance_m: measured_in_scene
  emission_angle_enabled: false_for_omnidirectional_source
  doppler_tracking: disabled_unless_motion_requires_it
  distance_filter: auditioned
  gameplay_range_dependency: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Échelle :** `unit_size_m` relie la courbe aux mètres du monde.
- **Distance :** la portée sonore est testée sans devenir une portée d’interaction.
- **Angle :** une porte ou un haut-parleur peut exiger une directivité différente.
- **Doppler :** l’effet n’est activé que pour un mouvement réellement perceptible.
- **Séparation :** les paramètres audio ne décident jamais si l’action gameplay est valide.

## 32. Auditeur audio et caméra

Par défaut, l’audio 3D est entendu depuis la caméra active. Un `AudioListener3D` peut définir un autre point d’écoute, mais son activation doit suivre le cycle de caméra et être restaurée après une cinématique.

Le changement d’auditeur n’est pas un téléport gameplay et ne modifie pas la position autoritaire du personnage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
listener_policy:
  gameplay:
    listener: active_gameplay_camera_or_character_listener
  cinematic:
    listener: cinematic_camera_listener
    enter: make_current_after_scene_ready
    exit: restore_previous_listener
  split_screen:
    status: separate_design_required
  invariant: listener_position_is_presentation_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gameplay :** le point d’écoute suit la convention retenue pour la caméra ou le personnage.
- **Cinématique :** l’auditeur temporaire possède une entrée et une sortie explicites.
- **Restauration :** la référence précédente est conservée avant le changement.
- **Multi-vue :** le split-screen exige une décision distincte et n’est pas supposé résolu.
- **Invariant :** la position d’écoute ne devient jamais l’état métier du joueur.

## 33. Architecture des bus Godot

Les bus regroupent les familles pour appliquer volume, effets, mute et solo de manière cohérente. Une hiérarchie simple facilite les profils de mix, les réglages du joueur et le diagnostic.

Le bus `Master` reste la sortie finale ; les bus enfants ne stockent aucun état gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_buses:
  Master:
    children:
      - Music
      - Voice
      - SFX
      - Ambience
      - UI
  SFX:
    children: [SFX_Critical, SFX_World, SFX_Foley]
  Voice:
    children: [Voice_Dialogue, Voice_Radio]
  Ambience:
    children: [Ambience_Bed, Ambience_Emitters]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Master :** la sortie finale reçoit seulement les traitements globaux justifiés.
- **Familles :** musique, voix, SFX, ambiance et UI peuvent être réglés séparément.
- **Sous-bus :** les signaux critiques sont distingués du décor sonore.
- **Voix :** le traitement radio ne modifie pas le master de dialogue.
- **Ambiance :** lit global et émetteurs localisés restent contrôlables indépendamment.

## 34. Ordre des effets sur un bus

L’ordre des effets modifie le résultat. Une égalisation avant compression ne réagit pas comme la même égalisation après compression ; un limiteur placé trop tôt peut alimenter des traitements ultérieurs qui recréent des crêtes.

Chaque chaîne conserve un objectif, un ordre et une méthode de bypass.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bus_effect_chain:
  bus: Voice_Radio
  effects:
    - {order: 1, type: high_pass_filter, purpose: radio_band_limit}
    - {order: 2, type: equalizer, purpose: intelligibility_shape}
    - {order: 3, type: compressor, purpose: controlled_dynamic_range}
    - {order: 4, type: distortion, purpose: subtle_transmission_texture}
    - {order: 5, type: limiter, purpose: safety_only}
  bypass_review: each_effect_and_full_chain
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** chaque effet reçoit un index stable dans la chaîne.
- **Filtrage :** la bande radio est façonnée avant le contrôle dynamique.
- **Compression :** la plage est réduite sans fabriquer une cible de loudness arbitraire.
- **Texture :** la distorsion reste subtile et réversible.
- **Bypass :** les effets sont comparés individuellement puis comme chaîne complète.

## 35. Presets et états de mix

Un preset de mix décrit des offsets et des activations d’effets, pas des valeurs absolues copiées dans chaque scène. Les états exploration, alerte, dialogue ou pause peuvent modifier plusieurs bus de manière coordonnée.

La transition entre presets doit être bornée et annulable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
mix_snapshot:
  id: AST-AUD-MIX-DIALOGUE-001
  transition_seconds: candidate
  buses:
    Music: {gain_offset_db: -4.0}
    Ambience: {gain_offset_db: -2.0}
    SFX_World: {gain_offset_db: -1.0}
    Voice_Dialogue: {gain_offset_db: 0.0}
  restore: previous_snapshot
  values_status: candidate_not_measured
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Snapshot :** l’identifiant permet de versionner un état de mix cohérent.
- **Offsets :** les valeurs sont relatives au mix de référence et restent candidates.
- **Transition :** la durée évite un saut mais doit être testée avec le dialogue réel.
- **Restauration :** le snapshot précédent est conservé et réappliqué.
- **Preuve :** aucun offset n’est accepté avant mesure et écoute dans le build.

## 36. Ducking et priorité de la voix

Le ducking réduit temporairement une famille lorsque la voix ou un signal critique est actif. Il ne doit pas pomper, supprimer l’ambiance ni être déclenché par un bus trop large.

Le sidechain ou l’enveloppe de contrôle est configuré selon le contenu, puis comparé avec une réduction manuelle de snapshot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ducking_policy:
  trigger_bus: Voice_Dialogue
  affected_buses: [Music, Ambience]
  attack_ms: candidate
  release_ms: candidate
  maximum_reduction_db: candidate
  excludes: [SFX_Critical, UI]
  validation: intelligibility_without_audible_pumping
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déclencheur :** seul le dialogue pertinent ouvre l’enveloppe de réduction.
- **Cibles :** musique et ambiance sont traitées sans toucher aux alertes critiques.
- **Temps :** attaque et relâchement sont écoutés avec des phrases courtes et longues.
- **Amplitude :** la réduction maximale reste une hypothèse à mesurer.
- **Critère :** la voix gagne en intelligibilité sans respiration artificielle du mix.

## 37. Zones, réverbération et détournement de bus

Une zone peut envoyer une source vers un bus de réverbération ou de coloration correspondant à un espace. Le traitement ne remplace pas une prise ou un SFX adapté au lieu.

Les transitions de zone sont testées aux limites et avec plusieurs sources simultanées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_zone:
  id: AST-AUD-ZONE-RELAY-INTERIOR-001
  volume_shape: room_geometry_proxy
  target_bus: Reverb_RelayInterior
  send_amount: candidate
  transition_margin_m: measured
  sources_affected: positioned_world_audio
  music_and_ui_affected: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Volume :** la forme sert de proxy acoustique et ne doit pas devenir une collision gameplay.
- **Bus :** le traitement de pièce reste séparé du bus source.
- **Envoi :** la quantité est ajustée selon la distance et l’écoute.
- **Transition :** une marge évite un changement abrupt à la frontière.
- **Exclusions :** musique et UI restent non positionnelles sauf décision explicite.

## 38. Polyphonie, concurrence et voix simultanées

La polyphonie décrit le nombre de lectures simultanées d’un lecteur ou d’une famille. Une limite trop basse coupe des informations ; une limite absente autorise une accumulation coûteuse.

La politique combine priorité, distance, âge, répétition et importance fonctionnelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
voice_budget:
  family: footsteps
  hard_limit: candidate
  soft_limit: candidate
  priority_order:
    - local_player
    - nearby_visible_actor
    - nearby_hidden_actor
    - distant_actor
  steal_policy: oldest_lowest_priority
  critical_events_never_stolen_by_ambient_duplicates: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites :** soft et hard limit sont mesurés dans un scénario de saturation.
- **Priorité :** le joueur local et les signaux proches sont conservés en premier.
- **Vol :** la voix la moins importante et la plus ancienne est remplacée.
- **Critique :** une alerte ne cède pas sa place à un doublon décoratif.
- **Mesure :** le budget est validé avec CPU, mémoire, latence et lisibilité.

## 39. Pool de lecteurs audio

Instancier un nœud pour chaque son court peut produire des allocations et des cycles de vie difficiles à suivre. Un pool borné réutilise des lecteurs selon la famille et le rôle spatial.

Le pool ne doit pas retenir indéfiniment une ressource lourde ni cacher un dépassement de budget.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
class_name AudioPlayerPool
extends Node

@export var capacity: int = 16
var _free_players: Array[AudioStreamPlayer3D] = []

func acquire() -> AudioStreamPlayer3D:
    if _free_players.is_empty():
        return null
    return _free_players.pop_back()

func release(player: AudioStreamPlayer3D) -> void:
    player.stop()
    player.stream = null
    if _free_players.size() < capacity:
        _free_players.push_back(player)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capacité :** le pool possède une borne explicite à qualifier par scène.
- **Acquisition :** `acquire()` retourne un lecteur ou `null` lorsque le pool est saturé.
- **Libération :** le lecteur est arrêté et sa ressource détachée avant réutilisation.
- **Tableau :** `Array[AudioStreamPlayer3D]` conserve uniquement des lecteurs compatibles.
- **Saturation :** l’appelant applique une politique de priorité plutôt que d’instancier sans limite.

## 40. Contrat d’événement audio

Le système gameplay émet un événement typé après sa décision autoritaire. L’adaptateur audio choisit un asset, une position, un bus et un profil sans pouvoir modifier l’issue de l’action.

L’identité de l’événement et la corrélation facilitent le diagnostic, mais ne servent pas d’autorisation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
class_name AudioCueRequest
extends RefCounted

var cue_id: StringName
var source_entity_id: StringName
var world_position: Vector3
var priority: int
var correlation_id: StringName

func _init(
    p_cue_id: StringName,
    p_source_entity_id: StringName,
    p_world_position: Vector3,
    p_priority: int,
    p_correlation_id: StringName
) -> void:
    cue_id = p_cue_id
    source_entity_id = p_source_entity_id
    world_position = p_world_position
    priority = p_priority
    correlation_id = p_correlation_id
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** `AudioCueRequest` transporte une intention de présentation sans logique métier.
- **Cue :** `cue_id` référence le catalogue audio et non un chemin arbitraire.
- **Position :** `Vector3` sert uniquement à la représentation spatiale.
- **Priorité :** l’entier aide la politique de concurrence sans décider le gameplay.
- **Corrélation :** l’identifiant relie journaux et événement source sans devenir une permission.

## 41. Ne jamais donner d’autorité gameplay à l’audio

La fin d’un fichier, un beat musical ou un seuil de spectre ne doit pas appliquer des dégâts, terminer une quête ou valider une sauvegarde. Le gameplay peut attendre un délai ou un état qu’il possède lui-même, puis demander une présentation audio.

Un signal `finished` sert au cycle de lecture, pas à la vérité métier.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
authority_boundary:
  allowed:
    - play_cue_after_authoritative_event
    - stop_or_fade_presentation
    - report_playback_diagnostic
  forbidden:
    - apply_damage_on_waveform_peak
    - complete_quest_on_stream_finished
    - unlock_door_on_music_bar
    - persist_game_state_from_audio_bus
  rule: domain_commits_before_audio_request
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorisé :** le système audio gère lecture, arrêt, fondu et diagnostic.
- **Interdit :** aucun signal sonore n’applique directement une conséquence métier.
- **Ordre :** le commit autoritaire précède la requête de cue.
- **Échec :** une lecture indisponible ne doit pas annuler une action déjà validée.
- **Test :** les scénarios vérifient que le jeu reste correct avec l’audio désactivé.

## 42. Sous-titres, transcriptions et alternatives

La voix et les alertes importantes doivent pouvoir être comprises sans dépendre exclusivement du son. Le présent chapitre prépare identifiants de texte, rôles de locuteur et événements de sous-titre ; le Livre IV complétera l’accessibilité audio globale.

Le texte n’est pas extrait du fichier comme source autoritaire : il provient du contenu narratif versionné.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_accessibility_binding:
  cue_id: AST-AUD-VO-RELAY-001
  subtitle_key: dialogue.relay.scout.line_03
  speaker_id: AST-CHAR-SCOUT-001
  critical_non_speech_cue:
    visual_event_id: AST-UI-CUE-ALERT-001
  player_controls:
    voice_volume: planned
    music_volume: planned
    sfx_volume: planned
  boundary: full_audio_accessibility_completed_in_book_iv
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** le cue et la clé de sous-titre restent séparés mais corrélés.
- **Locuteur :** l’identité stable évite d’utiliser le nom affiché comme clé.
- **Non verbal :** une alerte critique reçoit un canal visuel ou haptique prévu.
- **Réglages :** les volumes par famille s’appuient sur les bus.
- **Frontière :** les options audio complètes et plateformes restent au Livre IV.

## 43. Estimer la mémoire audio

Pour un PCM non compressé, une estimation simple dépend de la fréquence, de la profondeur, du nombre de canaux et de la durée. Un flux compressé ajoute des coûts de stockage, décodage, buffers et caches qui doivent être mesurés.

L’estimation prépare un budget ; elle ne remplace pas le profileur du build.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def pcm_bytes(
    sample_rate_hz: int,
    bit_depth: int,
    channels: int,
    duration_seconds: float,
) -> int:
    bytes_per_sample = bit_depth // 8
    return int(sample_rate_hz * bytes_per_sample * channels * duration_seconds)

example = pcm_bytes(48_000, 16, 1, 10.0)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** la fonction reçoit fréquence, profondeur, canaux et durée avec des types explicites.
- **Conversion :** `bit_depth // 8` transforme les bits en octets par échantillon.
- **Calcul :** le produit estime la taille PCM brute sans en-tête ni alignement.
- **Retour :** l’entier représente des octets théoriques, pas la mémoire runtime complète.
- **Limite :** buffers, décodage, compression et copies du moteur restent à profiler.

## 44. Compression, streaming et latence

Les sons courts et fréquents peuvent privilégier une lecture à faible latence, tandis que les musiques et ambiances longues peuvent être diffusées en flux. Le compromis dépend aussi de la plateforme et du mode de lecture.

La documentation Godot signale notamment que certains comportements de réverbération sur le Web diffèrent selon le mode de lecture ; chaque plateforme doit donc être testée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
playback_profile:
  short_sfx:
    mode: sample_candidate
    goals: [low_latency, bounded_memory]
  long_music:
    mode: stream_candidate
    goals: [reduced_resident_memory, stable_decode]
  web:
    reverb_and_threading_behavior: platform_test_required
  mobile:
    decode_cpu_and_memory: platform_test_required
  desktop:
    reference_profile: pending_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **SFX :** les sons brefs privilégient une réponse immédiate sous une limite de mémoire.
- **Musique :** le streaming évite de garder toute la durée décodée en mémoire.
- **Web :** le mode de lecture et les threads peuvent modifier réverbération et latence.
- **Mobile :** CPU de décodage et mémoire sont mesurés sur appareil réel.
- **Référence :** le profil desktop reste une base candidate et non une garantie universelle.

## 45. Budgets CPU, mémoire et latence

Le budget audio combine voix simultanées, effets de bus, décodages, mémoire résidente, allocations et latence de déclenchement. Une seule moyenne masque les pointes et les situations de saturation.

Les mesures sont collectées par scénario, plateforme, build et profil de mix.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_budget_record:
  scenario_id: AST-AUD-SCENARIO-STORM-SATURATION-001
  platform: desktop_reference
  build_commit: required
  metrics:
    active_voices_peak: measured
    audio_cpu_ms_peak: measured
    resident_audio_memory_mb: measured
    allocation_spikes: measured
    trigger_to_audible_latency_ms: measured
  repetitions: required
  status: not_executed
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénario :** le contexte de saturation est versionné et reproductible.
- **Build :** le commit relie la mesure au code et aux assets.
- **Pointes :** les maxima complètent les moyennes pour révéler les dépassements.
- **Latence :** le délai entre demande et son audible est mesuré avec une méthode documentée.
- **Statut :** aucune valeur n’est remplie avant exécution réelle.

## 46. Profils de qualité par plateforme

Un même catalogue peut produire plusieurs exports : référence desktop, mémoire réduite, Web ou mobile. Les profils modifient compression, streaming, canaux, polyphonie et effets sans perdre les informations critiques.

La réduction de qualité ne doit pas supprimer une voix, une alerte ou un contraste sonore essentiel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_quality_profiles:
  desktop_reference:
    compression: balanced
    voice_limit: candidate_high
    bus_effects: reference_chain
  memory_reduced:
    compression: stronger_after_audition
    voice_limit: candidate_lower
    ambience_layers: reduced_noncritical
  web:
    playback_mode: platform_qualified
    reverb: compatibility_review
  invariant: critical_voice_and_alert_information_preserved
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le profil desktop sert de comparaison, pas de valeur automatiquement optimale.
- **Mémoire :** les couches décoratives sont réduites avant les signaux critiques.
- **Web :** mode de lecture et réverbération suivent les limites réellement testées.
- **Polyphonie :** les limites varient selon la plateforme et le scénario.
- **Invariant :** dialogue et alertes conservent leur intelligibilité dans chaque profil.

## 47. Scène Godot de validation audio

La scène de test rassemble les lecteurs, bus, zones et commandes nécessaires pour isoler chaque famille puis jouer le pilote complet. Elle ne dépend pas d’une quête ou d’un combat réel.

Les positions, distances et états sont reproductibles afin de comparer deux versions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
AST_Audio_Test_Lab
├── CameraRig
│   └── AudioListener3D
├── NonPositional
│   ├── MusicPlayer
│   ├── VoicePlayer
│   └── UIPlayer
├── PositionedSources
│   ├── DoorEmitter
│   ├── FootstepEmitters
│   └── ThunderEmitter
├── Zones
│   ├── RelayInterior
│   └── ExteriorStorm
└── TestController
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Auditeur :** une position contrôlée permet de répéter les mêmes distances.
- **Non positionnel :** musique, voix de test et UI restent séparées.
- **Émetteurs :** chaque source 3D possède une position et un profil identifiés.
- **Zones :** intérieur et extérieur testent les transitions de bus.
- **Contrôleur :** les scénarios sont lancés sans dépendre d’une règle métier.

## 48. Campagne d’écoute et de mesure

La campagne commence par l’intégrité des fichiers, poursuit avec l’écoute isolée, puis le mix complet, les saturations et les plateformes. Un fichier approuvé seul peut échouer dès qu’il est superposé à la voix ou à la musique.

Les comparaisons utilisent les mêmes scènes, positions, niveaux de sortie et conditions d’écoute.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_validation_campaign:
  phase_1_integrity: [hashes, duration, channels, sample_rate, licence_status]
  phase_2_isolated: [noise, clicks, loop, timbre, true_peak]
  phase_3_mix: [intelligibility, masking, transitions, ducking]
  phase_4_saturation: [voice_limit, steals, cpu, memory, latency]
  phase_5_platforms: [desktop, web, target_devices]
  phase_6_retest: [fixed_build, same_scenario, closure_evidence]
  current_phase: static_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Intégrité :** les métadonnées et droits sont contrôlés avant l’écoute.
- **Isolé :** chaque défaut de source ou de boucle est recherché sans masquage.
- **Mix :** les familles sont testées ensemble avec les événements critiques.
- **Saturation :** le nombre de voix et les coûts sont poussés jusqu’aux limites candidates.
- **Retest :** la fermeture d’un problème exige un build et un scénario comparables.

## 49. Rapport de loudness et de mix

Le rapport conserve la méthode, les unités, les fenêtres, les outils, la version du fichier et le contexte de mesure. Une valeur sans ces éléments n’est pas comparable.

Les décisions d’acceptation restent humaines et indiquent les réserves.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
loudness_report:
  id: AST-AUD-REPORT-LOUDNESS-001
  asset_or_mix_id: AST-AUD-MIX-RELAY-001
  measurement_standard: ITU-R_BS.1770-5
  tool_and_version: required
  metrics:
    integrated_lufs: measured
    short_term_lufs: measured_where_relevant
    loudness_range_lu: measured_where_relevant
    true_peak_dbtp: measured
  decision: pending_human_review
  reservations: explicit
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le rapport cible une version précise d’asset ou de mix.
- **Standard :** l’algorithme de mesure est déclaré explicitement.
- **Outil :** l’application et sa version permettent de reproduire le résultat.
- **Métriques :** chaque unité est enregistrée seulement lorsqu’elle convient au contenu.
- **Décision :** la mesure informe la revue sans remplacer l’écoute ni l’acceptation humaine.

## 50. Provenance et licence d’une bibliothèque audio

Un fichier gratuit, acheté ou marqué royalty-free n’est pas automatiquement redistribuable dans toutes les formes. La licence exacte, l’auteur, le fournisseur, les attributions et les restrictions restent documentés.

Un asset composite hérite des contraintes de toutes ses sources contributrices.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_provenance:
  asset_id: AST-AUD-SFX-RELAY-DOOR-001
  contributors:
    - source_id: AST-AUD-SRC-FOLEY-014
      author: documented
      provider: documented
      licence_id: exact_or_LicenseRef
      attribution: documented
      redistribution: qualified
      ai_training: qualified_or_not_applicable
  composite_clearance: blocked_if_any_source_is_blocked
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Auteur :** la personne ou entité créatrice reste distincte du fournisseur.
- **Licence :** un identifiant exact ou une référence contractuelle remplace les adjectifs vagues.
- **Attribution :** le texte et l’emplacement sont préparés avant publication.
- **Redistribution :** l’intégration au jeu et la distribution des fichiers sources sont distinguées.
- **Composite :** une seule couche bloquée empêche l’acceptation du master composite.

## 51. Manifeste spécifique d’une voix

La voix associe texte, interprète, langue, session, prises, montage, traitement, master, export et autorisations. Les références sensibles pointent vers un stockage restreint.

Le manifeste prépare le chapitre 27 en fournissant une version de dialogue et des timings sans encore produire de visèmes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
voice_manifest:
  asset_id: AST-AUD-VO-SCOUT-RADIO-001
  dialogue_line_id: AST-DLG-RELAY-001-L03
  language: fr-FR
  performer_reference: restricted
  recording_session_id: AST-AUD-REC-VOICE-001
  selected_take_ids: [take_2, take_1_segment]
  edit_session_version: 1.0.0
  master_sha256: pending
  runtime_export_sha256: pending
  timing_handoff_to_chapter_27: planned
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dialogue :** la ligne narrative conserve une identité indépendante du fichier audio.
- **Langue :** le profil linguistique prépare les variantes et la synchronisation.
- **Interprète :** la référence sensible n’expose pas l’identité dans le dépôt public.
- **Empreintes :** master et export reçoivent des SHA-256 distincts après matérialisation.
- **Transmission :** les timings sont préparés pour le chapitre 27 sans créer de visèmes ici.

## 52. Cycle de version et retrait

Une correction audible publiée ne remplace pas silencieusement la version précédente. La nouvelle version indique sa source, ses changements et les dépendances à retester.

Un retrait juridique ou artistique gèle les nouvelles livraisons, conserve les preuves et propose un remplacement versionné.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_version_lifecycle:
  draft: editable
  review: listen_and_measure
  approved: immutable_release
  superseded: retained_for_traceability
  withdrawn: blocked_from_new_builds
  replacement:
    new_asset_id_or_version: required
    dependent_scenes_retested: required
    manifest_history_preserved: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Brouillon :** les changements restent libres tant que l’asset n’est pas publié.
- **Revue :** écoute, mesures, droits et intégration sont contrôlés ensemble.
- **Approuvé :** la version devient immuable et tout changement crée un successeur.
- **Retrait :** le fichier est bloqué sans effacer l’historique ni les preuves.
- **Remplacement :** les scènes et mix dépendants sont retestés avec la nouvelle ressource.

## 53. Revue artistique et technique

La revue artistique juge intention, matière, rythme et cohérence avec la bible sonore. La revue technique contrôle fichiers, boucles, niveaux, droits, mémoire et comportement Godot.

Les deux décisions sont nécessaires : un fichier techniquement propre peut être artistiquement inadéquat, et inversement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
audio_review:
  artistic:
    checks: [intent, material, perspective, rhythm, world_consistency]
    owner: audio_direction_or_delegate
  technical:
    checks: [format, loop, peaks, import, concurrency, memory, rights]
    owner: audio_integration_or_delegate
  acceptance:
    requires: [artistic_pass, technical_pass, provenance_pass]
    unresolved_reservation: blocks_or_documents_exception
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Artistique :** la revue compare le son à sa fonction et à la bible du projet.
- **Technique :** le fichier et son intégration sont inspectés avec des critères reproductibles.
- **Provenance :** les droits constituent une porte indépendante des qualités audibles.
- **Propriétaires :** Solo et Studio peuvent combiner ou séparer les rôles sans supprimer les contrôles.
- **Réserve :** un écart ouvert bloque l’acceptation ou reçoit une exception écrite et limitée.

## 54. Modes Solo et Mode Studio

### Mode Solo

Le parcours Solo limite la bibliothèque pilote, réutilise des presets communs, conserve une arborescence stricte et effectue une écoute systématique au casque puis sur au moins un second dispositif. Une seule personne peut enregistrer, monter et intégrer, mais elle sépare les étapes et réalise une revue différée pour réduire les biais.

### Mode Studio

Le parcours Studio distingue direction audio, enregistrement, montage, sound design, composition, intégration, QA et validation des droits. Les responsabilités sont consignées par asset, les bus et presets sont versionnés, et les demandes de correction conservent leur historique.

Dans les deux modes, les mêmes identifiants, manifestes, réserves, portes d’acceptation et frontières d’autorité s’appliquent. Le Studio ajoute des rôles ; il ne change pas les contrats fondamentaux.


## 55. Starter Kit audio à préparer

Le Starter Kit futur pourra fournir des schémas de manifeste, presets de bus, scènes de test et scripts de rapport. Aucun de ces livrables n’est présenté comme déjà créé dans ce chapitre.

Les modèles doivent rester génériques et ne pas embarquer les voix, contrats ou ressources propres à Project Asteria.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
starter_kit_candidates:
  schemas:
    - audio_asset_manifest.schema.json
    - voice_consent_reference.schema.json
    - loudness_report.schema.json
  godot:
    - default_bus_layout.tres
    - audio_test_lab.tscn
    - audio_player_pool.gd
  templates:
    - recording_session.yaml
    - variation_set.yaml
    - platform_audio_profile.yaml
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schémas :** les documents valident structure et version sans conclure sur les droits.
- **Godot :** le layout, la scène et le pool restent des candidats à matérialiser.
- **Templates :** les fiches donnent des champs reproductibles aux parcours Solo et Studio.
- **Nettoyage :** les données personnelles et assets du fil rouge sont exclus du pack.
- **Statut :** aucun fichier du Starter Kit n’est revendiqué comme produit.

## 56. Porte d’acceptation du pilote audio

Le pilote n’est accepté qu’après validation de la provenance, qualité des sources, montage, boucles, imports, mix, spatialisation, transitions, accessibilité, mémoire et voix simultanées.

Une écoute favorable ne remplace ni les mesures ni les droits ; une mesure conforme ne remplace pas l’intention artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  identity_and_version: required
  provenance_and_rights: required
  source_and_master_integrity: required
  editing_and_loop_review: required
  godot_import_and_playback: required
  bus_mix_and_transitions: required
  loudness_and_true_peak_report: required
  concurrency_memory_and_latency_report: required
  critical_audio_alternative: required
  artistic_and_technical_human_decision: required
  current_status: static_review_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque livrable accepté possède une version et des empreintes.
- **Droits :** une source bloquée empêche la publication du composite.
- **Intégration :** imports, bus, transitions et spatialisation sont exécutés dans Godot.
- **Mesures :** loudness, crête, mémoire, concurrence et latence sont enregistrés.
- **Décision :** les revues artistique et technique ferment la porte ou maintiennent les réserves.

## 57. Plan de campagne du pilote

La campagne commence par les manifestes et fichiers, poursuit par l’écoute isolée, l’intégration Godot, le mix, la saturation et les plateformes. Les corrections importantes sont retestées avec les mêmes scénarios.

Les prises sensibles restent dans leur stockage restreint ; seuls les dérivés autorisés entrent dans le build.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pilot_campaign:
  phase_1_governance: [ids, sources, licences, consent_references]
  phase_2_assets: [editing, loops, masters, runtime_exports]
  phase_3_godot: [imports, players, buses, zones, events]
  phase_4_mix: [voice_priority, ducking, transitions, accessibility]
  phase_5_performance: [voices, cpu, memory, allocations, latency]
  phase_6_platforms: [desktop_reference, web, target_devices]
  phase_7_retest: [fixed_build, same_scenarios, closure]
  current_phase: documentation_static_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gouvernance :** les droits et identités sont vérifiés avant la publication des fichiers.
- **Assets :** masters et exports sont comparés avant l’import moteur.
- **Godot :** lecteurs, bus, zones et contrats d’événements sont exécutés ensemble.
- **Performance :** les scénarios de saturation produisent des métriques par plateforme.
- **Clôture :** une correction n’est fermée qu’après retest et conservation de la preuve.

## 58. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 58.1 La prise brute est écrasée par le nettoyage

**Symptôme ou risque :** un défaut de traitement ne peut plus être annulé et la provenance du signal original disparaît.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
voice_take:
  path: sources/scout_take_02.wav
  action: overwrite_after_noise_reduction
  original_hash: lost
  undo: unavailable
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier source est modifié en place ; aucune empreinte ni dérivé ne permet de reconstruire la prise initiale.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
voice_take:
  source: restricted_sources/scout_take_02.wav
  source_hash: preserved
  work_session: work/voice_relay_v001.session
  master: masters/voice/scout_line_v001.wav
  transformations: append_only
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La source reste immuable, les traitements sont décrits dans une session et le master est un nouveau fichier versionné.

### 58.2 Une autorisation d’enregistrement est traitée comme droit de clonage

**Symptôme ou risque :** une voix enregistrée est utilisée pour entraîner ou cloner sans portée séparée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
consent:
  recording: granted
  inferred_permissions:
    editing: true
    commercial_use: true
    model_training: true
    voice_cloning: true
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le document déduit plusieurs droits sensibles d’une seule permission et ne conserve ni durée, ni territoire, ni retrait.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
consent:
  recording: granted
  editing: explicit_decision
  commercial_use: explicit_decision
  model_training: separate_decision
  voice_cloning: separate_decision
  withdrawal_process: documented
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque portée reçoit une décision distincte ; l’absence d’autorisation ne devient jamais une permission implicite.

### 58.3 La normalisation remplace le mix

**Symptôme ou risque :** tous les fichiers sont normalisés au même maximum mais les voix restent incohérentes et les impacts masquent le dialogue.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
import_policy:
  normalize_all_files: true
  loudness_measurement: absent
  mix_context: ignored
  true_peak_after_encode: not_checked
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un maximum identique ne garantit ni loudness comparable, ni intelligibilité, ni marge après encodage.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
import_policy:
  normalize: disabled_by_default
  loudness_report: required_by_family
  mix_context_review: required
  true_peak_after_encode: measured
  gain_changes: documented_in_mix
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le niveau est décidé avec des mesures adaptées, une écoute en contexte et un contrôle de crête après l’export runtime.

### 58.4 Une boucle est coupée uniquement au passage par zéro

**Symptôme ou risque :** la forme d’onde ne clique pas mais la modulation et le spectre sautent à chaque répétition.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
loop:
  start: first_zero_crossing
  end: last_zero_crossing
  spectral_review: none
  repeated_audition: once
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le passage par zéro contrôle seulement l’amplitude instantanée et ignore la pente, le spectre et la phase des modulations.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
loop:
  start_sample: measured
  end_sample: measured
  checks: [level, slope, spectrum, modulation_phase]
  crossfade: auditioned_candidate
  repeated_audition: extended
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les points sont choisis avec plusieurs critères et la boucle est écoutée sur une durée suffisante après encodage.

### 58.5 Le pitch aléatoire est utilisé comme seule variation

**Symptôme ou risque :** les pas deviennent artificiels et certains sonnent comme une autre matière.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
footsteps:
  assets: [step_01]
  pitch_range: [0.6, 1.5]
  no_repeat_memory: absent
  gain_range_db: [-8, 8]
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une seule prise subit des transformations extrêmes qui changent son identité et créent de fortes variations de niveau.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
footsteps:
  assets: [step_01, step_02, step_03, step_04]
  selection: weighted_no_immediate_repeat
  pitch_range: [0.97, 1.03]
  gain_offset_db: [-1.0, 1.0]
  history_size: 2
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Plusieurs prises fournissent la diversité principale, tandis que pitch et gain restent bornés et la mémoire évite la répétition.

### 58.6 Un son stéréo est utilisé comme source 3D ponctuelle

**Symptôme ou risque :** l’image intégrée lutte avec la position du nœud et la source paraît large ou se déplace mal.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
door_emitter:
  node: AudioStreamPlayer3D
  stream_channels: stereo
  source_width: fixed_in_file
  mono_review: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier porte déjà une spatialisation stéréo qui ne correspond pas nécessairement à la position calculée par Godot.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
door_emitter:
  node: AudioStreamPlayer3D
  stream_channels: mono
  position: door_hinge_or_acoustic_origin
  attenuation_profile: measured
  stereo_room_tail: optional_separate_layer
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La source ponctuelle devient mono et la largeur éventuelle est déplacée dans une couche d’espace séparée et contrôlable.

### 58.7 Le signal `finished` termine une quête

**Symptôme ou risque :** une lecture interrompue ou absente modifie la progression narrative.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func _on_voice_finished() -> void:
    quest.complete_objective("listen_to_message")
    save_game()
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le cycle audio acquiert une autorité métier et rend la quête dépendante du périphérique, du mute et des interruptions.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func on_message_objective_committed(event: ObjectiveCompleted) -> void:
    audio_cues.request(&"relay_message_confirmed", event.correlation_id)

func _on_voice_finished() -> void:
    release_voice_player()
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le domaine termine d’abord l’objectif puis demande un cue ; la fin de lecture ne gère que la ressource de présentation.

### 58.8 La polyphonie est illimitée

**Symptôme ou risque :** une scène de foule accumule les pas et impacts jusqu’à masquer les alertes et dépasser les budgets.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
audio_runtime:
  max_voices: unlimited
  priority: none
  pooling: none
  saturation_test: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Aucune borne, priorité ni politique de vol ne protège le mix et les ressources.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
audio_runtime:
  family_limits: versioned_candidates
  priority: critical_then_local_then_near_then_distant
  pooling: bounded
  steal_policy: oldest_low_priority
  saturation_test: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les limites et priorités rendent le dépassement contrôlable, puis la campagne mesure le point de saturation.

### 58.9 Le terme royalty-free est utilisé comme licence

**Symptôme ou risque :** la provenance ne permet pas de vérifier attribution, redistribution ou usages IA.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
source:
  provider: marketplace
  licence: royalty-free
  author: unknown
  redistribution: assumed
  ai_training: assumed
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un qualificatif commercial vague remplace l’identifiant de licence et plusieurs droits sont supposés.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
source:
  provider: documented
  author: documented
  licence_id: exact_or_LicenseRef
  attribution: documented
  redistribution: qualified
  ai_training: separate_qualification
  evidence_reference: restricted_or_public_as_allowed
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les rôles et droits sont séparés, et chaque conclusion renvoie à une preuve identifiable.

### 58.10 Un profil audio unique est déclaré valable partout

**Symptôme ou risque :** le Web, le mobile et le desktop présentent des écarts de latence, mémoire ou effets non testés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
quality_profile:
  name: universal
  playback_mode: sample
  reverb: enabled
  voice_limit: 128
  platforms_tested: [editor_only]
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les capacités et coûts sont supposés identiques malgré les différences de plateforme et de mode de lecture.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
quality_profiles:
  desktop_reference: pending_measurement
  web: playback_and_reverb_qualified
  mobile: decode_cpu_memory_qualified
  per_profile_voice_limits: measured
  critical_information_preserved: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque plateforme reçoit une qualification dédiée et conserve les voix et alertes critiques malgré les réductions.

## 59. Checklist de production et validation

La checklist reste ouverte tant qu’aucune preuve réelle n’est enregistrée. Un exemple de configuration dans ce chapitre ne coche aucune case.

- [ ] identité, version et fonction de chaque asset définies ;
- [ ] sources, auteurs, fournisseurs, licences et consentements qualifiés ;
- [ ] prises brutes et fichiers sources immuables avec empreintes ;
- [ ] sessions de travail et masters versionnés ;
- [ ] nettoyage comparé en bypass à niveau perçu comparable ;
- [ ] montage, fades, respirations et silences revus ;
- [ ] boucles écoutées sur plusieurs répétitions après encodage ;
- [ ] variantes et mémoire anti-répétition vérifiées ;
- [ ] formats, fréquences, canaux et profils d’import justifiés ;
- [ ] loudness, crête vraie et marge mesurés avec méthode documentée ;
- [ ] lecteurs non positionnels et 3D choisis selon la fonction ;
- [ ] atténuation, directionnalité, Doppler et auditeur testés ;
- [ ] architecture de bus, effets et snapshots versionnés ;
- [ ] ducking, zones et transitions évalués en mix complet ;
- [ ] limites de voix, pooling et politique de saturation exécutés ;
- [ ] alternatives aux informations audio critiques préparées ;
- [ ] mémoire, CPU, allocations et latence mesurés ;
- [ ] profils desktop, Web et appareils cibles qualifiés ;
- [ ] revue artistique, technique et provenance fermée ;
- [ ] réserves et décisions humaines consignées.


## 60. Références techniques officielles

Les pages suivantes fournissent les contrats Godot et les méthodes de mesure utilisés comme références. Elles ne remplacent ni l’écoute dans le build, ni la qualification des plateformes, ni la validation juridique des sources.

- [Godot 4.7 — Importer des échantillons audio](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_audio_samples.html)
- [Godot 4.7 — Flux audio](https://docs.godotengine.org/en/4.7/tutorials/audio/audio_streams.html)
- [Godot 4.7 — `AudioStreamPlayer`](https://docs.godotengine.org/en/4.7/classes/class_audiostreamplayer.html)
- [Godot 4.7 — `AudioStreamPlayer3D`](https://docs.godotengine.org/en/4.7/classes/class_audiostreamplayer3d.html)
- [Godot 4.7 — `AudioEffect`](https://docs.godotengine.org/en/4.7/classes/class_audioeffect.html)
- [Godot 4.7 — `AudioEffectCapture`](https://docs.godotengine.org/en/4.7/classes/class_audioeffectcapture.html)
- [Godot 4.7 — `AudioEffectRecord`](https://docs.godotengine.org/en/4.7/classes/class_audioeffectrecord.html)
- [Godot 4.7 — `AudioServer`](https://docs.godotengine.org/en/4.7/classes/class_audioserver.html)
- [UIT-R — Recommandation BS.1770-5, loudness et crête vraie](https://www.itu.int/rec/R-REC-BS.1770-5-202311-I/fr)
- [EBU — Recommandation R 128](https://tech.ebu.ch/publications/r128)
- [Creative Commons — À propos des licences CC](https://creativecommons.org/share-your-work/cclicenses/)
- [Livre I — Chapitre 9 : Audio IA local](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md)
- [Livre III — Chapitre 22 : Cinématiques, caméras et mise en scène](CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md)
- [Livre III — Chapitre 23 : Effets visuels, particules et simulations](CHAPITRE-23-Effets-visuels-particules-et-simulations.md)
- [Livre III — Chapitre 25 : Expérience utilisateur et accessibilité visuelle](CHAPITRE-25-Experience-utilisateur-et-accessibilite-visuelle.md)


## 61. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-AUDIO-PILOT-RELAY-STORM-001` comme pilote de chaîne audio. Les prises, sources générées ou licenciées, sessions de travail, masters, exports runtime et ressources Godot restent séparés et versionnés.

La porte d’acceptation combine provenance, consentement, qualité artistique, intégrité technique, boucles, import, mix, spatialisation, alternatives aux signaux critiques, loudness, crête vraie, mémoire, concurrence et latence. Tant que les fichiers, scènes et mesures ne sont pas matérialisés, le système reste au niveau `static-review`.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_audio_decisions:
  pilot_id: AST-AUDIO-PILOT-RELAY-STORM-001
  library_id: AST-AUDIO-LIBRARY-001
  bus_layout_id: AST-AUDIO-BUSES-001
  mix_profile_id: AST-AUDIO-MIX-REFERENCE-001
  voice_manifest_root: AST-AUDIO-VOICE-MANIFESTS-001
  loudness_report_id: AST-AUD-REPORT-LOUDNESS-001
  source_rule: immutable_source_and_versioned_derivatives
  authority_rule: domain_commit_before_audio_request
  privacy_rule: no_contract_identity_or_sensitive_take_in_public_repo
  acceptance: rights_plus_art_plus_technical_plus_runtime_measurement
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** le relais sous l’orage réunit voix, SFX, ambiance, musique et intégration.
- **Bibliothèque :** les assets publiés partagent identités, versions et manifestes.
- **Mix :** bus et profils restent versionnés et mesurés par plateforme.
- **Autorité :** les événements métier sont committés avant toute requête sonore.
- **Réserve :** aucun fichier, consentement, scène, rapport ou benchmark n’est revendiqué comme produit.
