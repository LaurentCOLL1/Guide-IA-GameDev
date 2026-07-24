---
title: "Livre III — Chapitre 23 : Effets visuels, particules et simulations"
id: "DOC-L3-CH23"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 23
last-verified: "2026-07-24T19:28:11+02:00"
audit-status: "complete"
audit-date: "2026-07-24T19:28:11+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-23.md"
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

# Effets visuels, particules et simulations

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH23`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Un effet visuel transforme un événement, une matière ou une ambiance en information perceptible. Il doit renforcer la lecture de l’action sans recouvrir la silhouette utile, cacher un danger ou fabriquer une règle de jeu qui n’existe pas dans les systèmes autoritaires.

Le chapitre construit une méthode de production et d’intégration pour des VFX modulaires. Il couvre les particules GPU et CPU, les shaders, les simulations précalculées, les caches, les collisions, le pooling, la transparence, l’overdraw, les variantes de qualité et les mesures à réaliser dans Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
chapter_role:
  input: approved_visual_intent_and_gameplay_event
  transformation: authored_vfx_asset_and_runtime_presentation
  output: versioned_effect_preset_with_quality_variants
  authority: visual_feedback_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** l’effet part d’une intention approuvée, d’un événement ou d’un phénomène à représenter.
- **Transformation :** la production sépare la source, les dérivés, le preset Godot et les profils de qualité.
- **Autorité :** le VFX visualise un fait ; il ne décide jamais dégâts, collision métier ou progression.
- **Preuve :** les structures sont relues statiquement et aucune scène n’est déclarée exécutée.
- **Sortie :** le livrable attendu est un preset versionné, réutilisable et mesurable.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura choisir entre `GPUParticles3D`, `CPUParticles3D`, shader, maillage, décalque, flipbook ou simulation précalculée. Il saura aussi organiser les sources, les caches, les presets et les variantes de qualité.

Il saura préparer des effets de feu, fumée, impacts, magie, météo, boue, fluides corporels stylisés, hologrammes, poussière atmosphérique, buée, bulles, geysers, traces de pas, débris et phénomènes astronomiques sans confondre démonstration visuelle et validation de production.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
learning_outcomes:
  perception: [readability, hierarchy, timing, silhouette_preservation]
  systems: [gpu_particles, cpu_particles, particle_shader, spatial_shader]
  authored_assets: [mesh, decal, flipbook, cached_simulation]
  runtime: [pooling, lifetime, collision_proxy, quality_profile]
  performance: [overdraw, transparency, lights, distance, measurement]
  governance: [provenance, version, manifest, acceptance_gate]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Perception :** la lisibilité et l’ordre d’apparition des informations priment sur la quantité d’éléments.
- **Systèmes :** chaque technique est choisie selon le besoin, pas selon son prestige visuel.
- **Runtime :** les instances, durées de vie et collisions restent bornées par des contrats explicites.
- **Performance :** les budgets sont des hypothèses tant qu’ils ne sont pas mesurés dans le build.
- **Gouvernance :** sources, caches, licences, versions et décisions humaines restent traçables.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les scènes, scripts, shaders et manifestes présentés sont des modèles documentaires ; ils ne prouvent ni rendu correct, ni stabilité, ni coût CPU ou GPU.

Aucun preset, cache Blender, flipbook, texture, maillage, scène Godot, capture de profilage ou benchmark n’est déclaré produit. Les valeurs numériques sont des candidats à remplacer par des mesures réalisées sur le matériel de référence et les plateformes réellement ciblées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
evidence_level:
  chapter: static-review
  vfx_library_materialized: false
  godot_test_scene_created: false
  gpu_particles_executed: false
  cpu_particles_executed: false
  shaders_compiled: false
  simulations_baked: false
  caches_versioned: false
  runtime_profile_captured: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est relue sans prétendre qu’un pipeline VFX existe déjà.
- **Assets :** aucune texture, simulation, scène ou bibliothèque n’est annoncée comme matérialisée.
- **Compilation :** les shaders et scripts restent des exemples statiques à adapter et compiler.
- **Mesures :** overdraw, temps GPU, mémoire, nombre d’instances et stabilité restent à établir.
- **Publication :** le PDF du Livre III demeure différé jusqu’à la fin du Livre.

## 4. Frontières avec les chapitres voisins

Le chapitre 16 reste propriétaire des matériaux PBR généraux. Le chapitre 22 reste propriétaire de la mise en scène, des caméras et de la timeline. Le chapitre 24 traitera l’interface ; le chapitre 26 produira l’audio ; le chapitre 28 consolidera l’import et le réimport universels.

Le Livre II conserve l’autorité sur combat, compétences, environnement, météo logique, quêtes et autres règles. Un VFX peut recevoir un événement typé et publier un signal de fin visuelle, mais il ne valide jamais un impact, une consommation ou une récompense.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ownership:
  chapter_16: surface_materials_and_pbr_library
  chapter_22: cinematic_staging_camera_and_timeline
  chapter_23: vfx_assets_particle_systems_and_visual_simulations
  chapter_24: user_interface_and_hud
  chapter_26: sound_effects_ambience_and_mix
  chapter_28: global_import_reimport_and_asset_gate
  book_ii: authoritative_gameplay_rules
  invariant: vfx_never_decides_gameplay
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Matériaux :** les VFX réutilisent les conventions de surfaces sans redéfinir le pipeline PBR.
- **Cinématique :** la timeline orchestre un effet approuvé mais ne devient pas sa source canonique.
- **Gameplay :** les systèmes métier décident le fait avant l’émission de sa représentation visuelle.
- **Import :** la qualification globale des dérivés reste réservée au chapitre 28.
- **Invariant :** aucun callback graphique ne modifie directement l’état autoritaire.

## 5. Pilote VFX de Project Asteria

Le pilote `AST-VFX-PILOT-RELAY-STORM-001` reprend la station-relais abandonnée du chapitre 22. Il réunit un impact métallique, des étincelles, une poussière de sol, une fumée froide, un hologramme instable et une pluie locale, afin de tester plusieurs familles sans disperser la production.

Le pilote reste volontairement réduit. Les phénomènes rares du plan maître — geyser, éclipses, disque d’accrétion, bulles ou buée — deviennent des fiches de décision et des presets candidats, pas des assets prétendument terminés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
asteria_vfx_pilot:
  id: AST-VFX-PILOT-RELAY-STORM-001
  location: AST-ENV-RELAY-001
  effect_set:
    - AST-VFX-IMPACT-METAL-001
    - AST-VFX-SPARKS-001
    - AST-VFX-DUST-GROUND-001
    - AST-VFX-SMOKE-COLD-001
    - AST-VFX-HOLOGRAM-001
    - AST-VFX-RAIN-LOCAL-001
  quality_profiles: [low, reference, high]
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** le pilote possède une identité stable indépendante de la cinématique qui le consomme.
- **Couverture :** le lot combine impacts, émission continue, transparence, distorsion et météo locale.
- **Profils :** trois variantes candidates permettront une comparaison sans supposer leur coût.
- **Réutilisation :** les presets doivent rester utilisables hors de la station-relais.
- **Réserve :** aucun effet de la liste n’est déclaré créé ou approuvé.

## 6. Fonction visuelle et information transmise

Avant de choisir une technologie, il faut écrire ce que le joueur doit comprendre : origine d’un impact, direction d’un danger, matériau touché, intensité, durée, état persistant ou simple ambiance. Un effet sans fonction peut ajouter du bruit tout en réduisant la lisibilité.

La hiérarchie distingue le signal critique, le renforcement secondaire et l’ornement. Le signal critique reste visible dans la variante basse ; l’ornement peut disparaître lorsque la distance, la qualité ou le budget l’exige.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
visual_function:
  critical_signal:
    question: what_must_the_player_understand
    survives_low_quality: true
  secondary_reinforcement:
    question: what_material_or_force_is_confirmed
    survives_low_quality: conditional
  ambience:
    question: what_mood_or_world_motion_is_added
    survives_low_quality: optional
  rejection: effect_without_readable_purpose
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signal critique :** l’information nécessaire au gameplay conserve une forme lisible dans tous les profils.
- **Renforcement :** la matière, la force ou la direction sont confirmées sans doubler inutilement le signal.
- **Ambiance :** les couches décoratives sont les premières réduites lorsque le budget se resserre.
- **Décision :** chaque couche possède une raison observable et une priorité explicite.
- **Rejet :** un effet sans fonction documentée ne franchit pas la revue.

## 7. Taxonomie des familles d’effets

Une bibliothèque devient maintenable lorsque les effets sont classés par comportement et non uniquement par nom spectaculaire. Les familles utiles distinguent impulsion, émission continue, volume atmosphérique, trace, surface projetée, distorsion, lumière transitoire et simulation mise en cache.

Cette taxonomie facilite les budgets, le pooling et les tests. Deux effets visuellement différents peuvent partager la même architecture si leur cycle de vie et leurs contraintes de rendu sont similaires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
vfx_families:
  burst: [impact, sparks, debris]
  continuous: [fire, smoke, rain, geyser]
  atmospheric: [dust_beam, fog, suspended_particles]
  trail: [projectile, footstep, magic_ribbon]
  projected: [decal, mud, wet_mark]
  distortion: [heat, shield, hologram]
  cached: [fluid_flipbook, smoke_flipbook, geometry_cache]
  celestial: [solar_eclipse, lunar_eclipse, accretion_disk]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Impulsion :** les bursts demandent une émission courte, une fin certaine et un recyclage rapide.
- **Continu :** les émissions persistantes nécessitent une activation, une désactivation et une stabilisation.
- **Atmosphère :** les volumes subtils sont contrôlés par distance, profondeur et couverture d’écran.
- **Dérivés :** les caches et flipbooks restent liés à leur source et à leur manifeste.
- **Céleste :** les phénomènes astronomiques exigent échelle, composition et plausibilité séparées du gameplay.

## 8. Architecture d’un asset VFX

L’asset VFX sépare la source canonique, les textures ou caches dérivés, la scène de preset, les scripts de pilotage et la fiche de validation. Cette séparation permet de régénérer un flipbook ou un cache sans perdre les décisions d’intégration.

Un preset ne contient pas de référence directe à une scène gameplay spécifique. Les ancrages, couleurs d’équipe, intensités ou directions arrivent par paramètres documentés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
vfx_asset:
  id: AST-VFX-SPARKS-001
  source:
    path: art/vfx/sources/sparks/
    canonical: true
  derived:
    textures: art/vfx/derived/sparks/
    caches: art/vfx/cache/sparks/
  runtime:
    scene: res://vfx/presets/ast_vfx_sparks_001.tscn
    controller: res://vfx/runtime/vfx_instance.gd
  validation:
    scene: res://vfx/tests/test_vfx_sparks_001.tscn
    report: docs/vfx/AST-VFX-SPARKS-001.md
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** les fichiers éditables ou procéduraux restent la référence de reconstruction.
- **Dérivés :** textures, caches et exports peuvent être supprimés puis régénérés depuis la source.
- **Runtime :** la scène Godot expose une interface stable sans dépendre d’un niveau particulier.
- **Validation :** une scène dédiée isole cadrage, distances, profils et mesures.
- **Identité :** l’identifiant relie manifeste, preset, rapport et dépendances.

## 9. Nommage, versions et statut

Le nom d’un effet décrit sa fonction, sa matière et sa variante plutôt qu’un jugement vague comme `cool` ou `final`. La version change lorsque le contrat, les dépendances ou la représentation exigent une nouvelle qualification.

Les statuts distinguent concept, source en cours, dérivé généré, candidat intégré, approuvé et retiré. `final` n’est pas un état suffisant car il n’explique ni la revue ni les réserves.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
vfx_identity:
  id: AST-VFX-IMPACT-METAL-001
  version: 1.0.0
  status: candidate
  function: impact_confirmation
  material_family: metal
  variant: reference
  owner: vfx
  approval:
    artistic: pending
    gameplay_readability: pending
    performance: pending
    legal: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** la fonction et la matière permettent de retrouver l’effet sans connaître son apparence exacte.
- **Version :** une modification de contrat déclenche une nouvelle qualification, pas un suffixe improvisé.
- **Statut :** le vocabulaire sépare production, intégration et approbation.
- **Propriétaire :** la responsabilité de maintenance est explicite en mode Studio.
- **Approbations :** les domaines artistique, gameplay, performance et juridique ne se compensent pas.

## 10. Choisir GPU, CPU, shader, maillage ou cache

Le choix technique dépend du nombre d’éléments, du besoin de lecture sur le CPU, des collisions, de la détermination visuelle, de la couverture d’écran et de la possibilité de précalculer. `GPUParticles3D` convient aux grandes populations visuelles ; `CPUParticles3D` reste utile lorsque la compatibilité ou un comportement CPU limité le justifie.

Un shader convient à une déformation ou une modulation continue de pixels ou de sommets. Un maillage, un décalque ou un flipbook peut être plus prévisible qu’un système de particules. Une simulation précalculée est pertinente lorsqu’un résultat complexe doit être reproduit sans recalcul complet au runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
technology_decision:
  high_count_visual_only: GPUParticles3D
  low_count_cpu_compatible: CPUParticles3D
  surface_or_vertex_transformation: shader
  persistent_projected_mark: decal_or_mesh
  authored_frame_sequence: flipbook
  expensive_repeatable_motion: cached_simulation
  gameplay_authority_required: external_system
  decision_requires_measurement: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **GPU :** les grandes populations restent visuelles et évitent des lectures CPU inutiles.
- **CPU :** le choix CPU doit répondre à une contrainte réelle plutôt qu’à une préférence.
- **Shader :** la transformation continue d’une surface ne nécessite pas toujours des particules.
- **Cache :** un calcul précalculé devient un dérivé versionné avec dépendances et limites.
- **Mesure :** la sélection finale dépend du build, du renderer et du matériel ciblé.

## 11. Anatomie de GPUParticles3D

`GPUParticles3D` sépare le nombre d’éléments, la durée de vie, le traitement, le dessin et la boîte de visibilité. Le nœud ne dessine rien tant qu’un matériau de traitement et au moins un draw pass ou une scène de dessin ne sont pas définis.

Le débutant doit distinguer `process_material`, qui fait évoluer les particules, du matériau porté par le maillage dessiné. Modifier l’un ne remplace pas l’autre.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
gpu_particles_contract:
  node: GPUParticles3D
  emission:
    amount: candidate
    lifetime_seconds: candidate
    one_shot: depends_on_effect
  processing:
    material: ParticleProcessMaterial_or_particle_shader
    fixed_fps: candidate
    preprocess_seconds: candidate
  drawing:
    draw_passes: [mesh_or_quad]
    material: StandardMaterial3D_or_ShaderMaterial
  culling:
    visibility_aabb: measured_from_motion
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Émission :** le nombre et la durée de vie définissent une population maximale à vérifier.
- **Traitement :** le matériau de processus calcule mouvement, couleur, échelle et collisions.
- **Dessin :** le draw pass fournit la géométrie réellement rendue.
- **Culling :** la boîte de visibilité doit couvrir les trajectoires utiles sans être arbitrairement immense.
- **Précondition :** un système incomplet peut être actif sans produire d’image exploitable.

## 12. ParticleProcessMaterial et courbes de vie

`ParticleProcessMaterial` offre des paramètres de direction, vitesse, gravité, accélérations, échelle, couleur, animation, turbulence et collision. Les courbes de vie doivent raconter l’apparition, la lecture et la disparition de l’effet.

Une courbe n’est pas décorative : une étincelle peut être brillante et petite au départ, s’étirer pendant son mouvement puis perdre rapidement son alpha. Une fumée peut au contraire gagner en taille tout en perdant contraste et opacité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
particle_lifecycle:
  spawn:
    scale: small
    alpha: visible
    velocity: strong
  readable_phase:
    scale_curve: authored
    color_ramp: material_specific
    animation: optional
  decay:
    alpha_curve: fade_before_end
    velocity_damping: effect_specific
  collision_mode: disabled_until_justified
  randomness: bounded_and_reviewed
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Naissance :** les premières images portent le signal principal et la direction.
- **Lecture :** courbes et rampes maintiennent la matière reconnaissable pendant la phase utile.
- **Extinction :** la disparition évite une coupure brutale et libère le preset à une durée prévisible.
- **Collision :** elle reste désactivée tant qu’un besoin et un budget ne sont pas établis.
- **Variation :** le hasard est borné afin de préserver silhouette et intention.

## 13. Formes d’émission et repères locaux

La forme d’émission doit correspondre au phénomène : point pour une étincelle concentrée, boîte pour une zone de poussière, anneau pour une onde, surface de maillage pour une désintégration. Une forme trop large dilue l’origine du signal.

`local_coords` décide si les particules déjà émises suivent le transform du nœud. Un projectile qui laisse une traînée dans le monde demande souvent des coordonnées globales ; une aura attachée à un personnage peut demander un comportement local.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
emission_design:
  shape: point_box_sphere_ring_or_mesh
  origin_is_readable: true
  local_coordinates:
    projectile_trail: false
    attached_aura: candidate
  initial_velocity:
    direction_space: documented
    spread_degrees: candidate
  transform_source: socket_or_world_anchor
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Forme :** le volume d’émission reste cohérent avec la taille et l’origine du phénomène.
- **Coordonnées :** le choix local ou global évite qu’une traînée se déplace après son émission.
- **Direction :** l’espace de référence des vecteurs est documenté pour prévenir les inversions.
- **Ancrage :** un socket ou un point monde fournit un contrat stable au preset.
- **Revue :** la forme est inspectée depuis plusieurs angles et distances.

## 14. Quantité, durée de vie et population maximale

La charge ne dépend pas seulement de `amount`. Une émission continue combine quantité, durée de vie, fréquence de renouvellement, nombre d’instances actives et surface couverte. Une petite particule transparente répétée sur tout l’écran peut coûter davantage qu’un maillage opaque plus complexe.

Le manifeste conserve des valeurs candidates et une population maximale théorique. La validation remplace ensuite ces candidats par des mesures et des limites adaptées aux contextes de jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
population_budget:
  per_instance:
    amount: candidate
    lifetime_seconds: candidate
    emission_mode: burst_or_continuous
  scene:
    simultaneous_instances: candidate
    theoretical_live_particles: amount_times_instances
  review:
    screen_coverage: measure
    gpu_time: measure
    memory: measure
  acceptance: pending_runtime_profile
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Instance :** quantité et durée de vie définissent le nombre d’éléments vivants.
- **Scène :** le nombre d’instances simultanées compte autant que le preset isolé.
- **Couverture :** la surface de pixels traités doit être inspectée à proximité.
- **Profilage :** temps GPU et mémoire restent des résultats de mesure.
- **Acceptation :** aucun budget n’est déclaré tenu avant la campagne runtime.

## 15. Preprocess, Fixed FPS et stabilité temporelle

`preprocess` simule un temps initial avant l’apparition, utile pour une fumée déjà établie. Une valeur élevée peut exécuter de nombreuses étapes avant la première image et provoquer un pic de coût.

`fixed_fps` borne la fréquence de traitement des particules. L’augmenter peut améliorer certaines collisions ou mouvements rapides, mais accroît le travail. Il faut comparer stabilité visuelle, tunneling et coût plutôt que choisir une valeur universelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
temporal_processing:
  preprocess_seconds:
    purpose: establish_continuous_effect
    value: candidate
    startup_spike: measure
  fixed_fps:
    purpose: simulation_step_rate
    value: candidate
    collision_tradeoff: documented
  interpolation: evaluate
  one_shot_restart: test
  slow_motion_behavior: test
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préparation :** le prétraitement sert uniquement aux effets qui doivent paraître déjà installés.
- **Fréquence :** le pas fixe est choisi selon le mouvement et les collisions visuelles.
- **Interpolation :** le rendu entre étapes doit être observé lors des variations de framerate.
- **Redémarrage :** les effets one-shot sont testés après recyclage et réémission.
- **Mesure :** le pic de démarrage et le coût continu sont séparés.

## 16. Graine, hasard et reproductibilité visuelle

Le hasard donne de la variété, mais il complique les comparaisons. Une graine fixe permet de revoir exactement un effet dans une capture, un replay ou une matrice de qualité.

La production peut conserver une graine de référence pour la validation puis autoriser une variation bornée en jeu. La reproductibilité visuelle ne signifie pas que l’effet devient déterministe pour les règles gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
randomness_policy:
  review_seed: 23001
  use_fixed_seed_during_qualification: true
  runtime_variation:
    enabled: candidate
    bounded_parameters: [spread, scale, hue_shift, lifetime]
  gameplay_dependency_on_particle_state: forbidden
  capture_replay_consistency: evaluate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Revue :** une graine stable facilite les comparaisons avant/après.
- **Variation :** seuls des paramètres bornés changent afin de conserver la fonction visuelle.
- **Gameplay :** aucune règle ne lit la position ou la survie d’une particule.
- **Capture :** les replays et rendus de revue peuvent demander une apparence répétable.
- **Limite :** la graine ne remplace pas un test sur plusieurs variations.

## 17. Draw passes, maillages et matériaux

Un draw pass peut utiliser un quad, un maillage simple, un ruban ou une géométrie spécifique. Le matériau du maillage contrôle transparence, émission, éclairage, profondeur et animation de texture.

Plusieurs draw passes enrichissent un effet, mais multiplient les géométries et matériaux évalués. Chaque couche doit apporter une information ou une matière distincte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
draw_stack:
  pass_1:
    geometry: quad
    purpose: luminous_core
    material: AST-MAT-VFX-CORE-001
  pass_2:
    geometry: ribbon
    purpose: directional_streak
    material: AST-MAT-VFX-TRAIL-001
  pass_3:
    geometry: mesh_fragment
    purpose: material_debris
    material: AST-MAT-VFX-METAL-001
  reject_unused_passes: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Géométrie :** chaque pass choisit une forme adaptée à la lecture attendue.
- **Matériau :** les propriétés de rendu restent distinctes du mouvement des particules.
- **Couches :** noyau, traînée et débris ont des fonctions différentes.
- **Coût :** un pass ajouté augmente le travail même si son apport est subtil.
- **Rejet :** une couche sans bénéfice observable est supprimée.

## 18. Transparence, profondeur et overdraw

La transparence devient coûteuse lorsque plusieurs surfaces couvrent les mêmes pixels. La fumée, la pluie et les halos peuvent créer un overdraw élevé à proximité de la caméra ou lorsqu’ils s’empilent.

La réponse ne consiste pas seulement à réduire le nombre de particules. Il faut aussi contrôler la taille des quads, la texture, la découpe, l’ordre de profondeur, la contribution lumineuse et les couches simultanées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
transparency_review:
  particle_quad:
    trimmed_texture: true
    screen_size_limit: candidate
    soft_edges: evaluate
  material:
    transparency_mode: candidate
    vertex_lighting: evaluate
    receives_shadows: evaluate
  scene:
    overlapping_layers: count
    close_camera_case: test
  overdraw_budget: measure_in_target_build
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Texture :** un sprite recadré évite de traiter de grandes zones transparentes inutiles.
- **Taille :** la couverture d’écran est limitée dans les vues rapprochées.
- **Matériau :** l’éclairage et les ombres sont activés seulement si la lecture les justifie.
- **Scène :** les empilements réels sont testés, pas uniquement un preset isolé.
- **Budget :** l’overdraw est observé avec les outils du renderer ciblé.

## 19. Billboards, orientation et traînées

Un billboard fait face à la caméra ; il convient aux sprites volumétriques stylisés mais peut révéler sa planéité lors de rotations rapides ou de vues latérales. Une orientation selon la vélocité renforce la direction d’une étincelle ou d’un projectile.

Les traînées exigent une durée, un maillage compatible et un matériau configuré. Elles doivent rester lisibles sans créer de rubans trop larges ou de courbes qui traversent la caméra.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
orientation_and_trails:
  sprite_smoke:
    transform_align: face_camera
    failure_case: visible_flatness
  spark:
    transform_align: velocity
    stretch: candidate
  trail:
    enabled: candidate
    lifetime_seconds: candidate
    mesh: RibbonTrailMesh
    material_supports_trails: required
  camera_crossing: test
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Billboard :** la face caméra simplifie le volume mais demande une revue multi-angle.
- **Vélocité :** l’alignement directionnel communique le mouvement sans multiplier les sprites.
- **Traînée :** durée, maillage et matériau forment un contrat indivisible.
- **Caméra :** les croisements proches révèlent les artefacts de largeur et d’orientation.
- **Décision :** le mode d’alignement dépend du phénomène et de la vue.

## 20. Sous-émetteurs et chaînes d’événements visuels

Un sous-émetteur peut produire un effet au démarrage, pendant la vie, à la fin ou lors d’une collision de particule. Il permet par exemple de remplacer une étincelle par un petit flash et une poussière au contact.

La chaîne doit rester bornée. Un sous-émetteur ne doit pas créer récursivement des populations imprévisibles, ni transmettre une conséquence gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
subemitter_chain:
  parent: AST-VFX-SPARK-PARENT-001
  trigger: collision
  child: AST-VFX-SPARK-CONTACT-001
  maximum_children_per_parent: candidate
  recursion: forbidden
  gameplay_event_emission: forbidden
  visual_completion_signal: optional
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Parent :** le preset principal décrit la trajectoire avant contact.
- **Déclencheur :** le mode de sous-émission correspond à une étape visuelle précise.
- **Enfant :** le flash de contact possède sa propre durée et son propre budget.
- **Borne :** le nombre de descendants et la récursion sont explicitement limités.
- **Signal :** une fin visuelle peut être publiée sans appliquer de conséquence métier.

## 21. Collisions de particules 3D

Les particules GPU entrent en collision avec des nœuds `GPUParticlesCollision3D`, pas directement avec les corps physiques standards. Le matériau de traitement doit aussi utiliser un mode de collision compatible.

Boîte, sphère, heightfield et SDF répondent à des besoins différents. Les colliders grossiers coûtent généralement moins qu’une représentation fine ; le SDF doit être réservé aux volumes qui le justifient.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
particle_collision:
  process_material:
    collision_mode: rigid_or_hide_on_contact
  proxies:
    simple_room: GPUParticlesCollisionBox3D
    rounded_volume: GPUParticlesCollisionSphere3D
    outdoor_ground: GPUParticlesCollisionHeightField3D
    complex_static_space: GPUParticlesCollisionSDF3D
  physics_body_collision_alone: insufficient
  validation: overlap_aabb_and_fast_particle_cases
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Matériau :** le mode de collision est une précondition du traitement des contacts.
- **Proxy :** la forme la plus simple compatible avec le besoin est privilégiée.
- **Physique :** un corps standard ne remplace pas automatiquement un collider de particules.
- **Chevauchement :** les boîtes de visibilité et de collision doivent se rencontrer.
- **Vitesse :** les particules rapides sont testées contre des surfaces minces.

## 22. Visibility AABB et disparition prématurée

La `visibility_aabb` définit la région dans laquelle le système reste actif et visible. Si les particules quittent cette boîte, elles peuvent disparaître ou cesser d’interagir avec colliders et attracteurs.

La boîte est générée ou mesurée à partir des trajectoires attendues, puis vérifiée pour les vents, explosions et mouvements de l’émetteur. Une boîte énorme évite certains pops mais réduit le bénéfice du culling.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
visibility_bounds:
  source: generated_then_reviewed
  covers:
    - emission_volume
    - maximum_expected_trajectory
    - trail_extent
    - collision_region
  excludes:
    - unrelated_level_space
  tests:
    - camera_enters_and_leaves
    - emitter_moves
    - wind_changes_direction
    - burst_reaches_extreme
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la boîte part d’une génération ou d’une mesure plutôt que d’une valeur arbitraire.
- **Couverture :** émission, trajectoire, traînée et collision sont incluses.
- **Culling :** l’espace étranger au preset reste exclu pour conserver l’intérêt de la visibilité.
- **Mouvement :** le déplacement de l’émetteur et les variations de force sont examinés.
- **Symptôme :** les disparitions soudaines conduisent d’abord à vérifier cette boîte.

## 23. Turbulence, attracteurs et champs vectoriels

La turbulence 3D ajoute une variation spatiale riche, mais son bruit peut coûter cher sur le GPU. Elle doit être comparée à des alternatives plus simples : courbes, forces directionnelles, texture animée ou mouvement du maillage.

Les attracteurs créent des comportements de convergence, vortex ou flux. Leur zone d’influence et leur priorité doivent rester compréhensibles lorsque plusieurs champs se superposent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
forces:
  turbulence:
    enabled: candidate
    noise_scale: candidate
    influence: bounded
    gpu_cost: measure
  attractors:
    box: local_flow
    sphere: convergence
    vector_field: authored_complex_motion
  overlap_policy: documented
  low_quality_fallback: simple_directional_force
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Turbulence :** le bruit 3D est activé seulement si son apport résiste à la revue.
- **Attracteur :** chaque forme correspond à un comportement spatial explicite.
- **Superposition :** les zones multiples possèdent une politique d’influence lisible.
- **Repli :** la variante basse peut employer une force directionnelle moins coûteuse.
- **Mesure :** le coût est relevé dans la scène cible et non déduit de l’apparence.

## 24. CPUParticles3D et compatibilité

`CPUParticles3D` traite les particules sur le CPU et n’offre pas nécessairement toutes les fonctions ou le même rendu que la voie GPU. La conversion entre les deux fournit un point de départ, pas une équivalence garantie.

Le choix CPU peut convenir à un faible nombre d’éléments, à un profil de compatibilité ou à un besoin particulier du projet. Il doit être testé avec le reste de la simulation et des systèmes CPU.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
cpu_particles_decision:
  node: CPUParticles3D
  reasons:
    - compatibility_profile
    - low_particle_count
    - constrained_feature_set
  conversion_from_gpu:
    allowed: as_starting_point
    visual_equivalence: not_assumed
  cpu_budget:
    frame_time: measure
    concurrent_emitters: measure
  gameplay_state_readback: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Motif :** la voie CPU répond à une contrainte explicite.
- **Conversion :** les propriétés converties sont revues car les fonctions diffèrent.
- **Budget :** le temps CPU est mesuré avec les autres systèmes actifs.
- **Concurrence :** plusieurs émetteurs sont testés ensemble.
- **Autorité :** les particules restent visuelles même lorsqu’elles sont calculées sur le CPU.

## 25. Particle shaders personnalisés

Un particle shader permet de contrôler les états de particule au-delà des propriétés standard. Il expose des fonctions de démarrage et de traitement, ainsi que des données comme la transformation, la vélocité, la couleur et les valeurs personnalisées.

Le shader reste limité à la représentation. Les paramètres utiles arrivent comme uniforms ou données préparées ; aucune décision gameplay n’est encodée dans un seuil graphique.

> **[LECTURE] Exemple de shader candidat — Ne pas saisir sans adaptation.**
```glsl
shader_type particles;

uniform float upward_speed = 1.5;
uniform float fade_start = 0.65;

void start() {
    VELOCITY = vec3(0.0, upward_speed, 0.0);
    COLOR = vec4(1.0);
    CUSTOM.y = 0.0;
}

void process() {
    CUSTOM.y += LIFETIME > 0.0 ? DELTA / LIFETIME : 1.0;
    float normalized_age = clamp(CUSTOM.y, 0.0, 1.0);
    float fade = 1.0 - smoothstep(fade_start, 1.0, normalized_age);
    COLOR.a = fade;
}
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** `shader_type particles` sélectionne le pipeline de calcul des particules.
- **Uniforms :** vitesse et début du fondu restent des paramètres de preset.
- **Démarrage :** `start` initialise les données propres à une nouvelle particule.
- **Traitement :** `process` met à jour l’alpha selon un âge normalisé candidat.
- **Limite :** la formule doit être compilée et vérifiée contre les built-ins de la version ciblée.

## 26. Shaders spatiaux, distorsion et réfraction

La chaleur, les boucliers et les hologrammes peuvent utiliser un shader spatial qui déforme des UV, module l’émission ou échantillonne l’écran. Ces techniques sont sensibles à l’ordre de rendu, à la résolution et à la couverture d’écran.

Une distorsion doit rester localisée et désactivable dans une variante de confort. L’échantillonnage de l’écran ou de la profondeur est traité comme une dépendance du renderer à qualifier.

> **[LECTURE] Exemple de shader candidat — Ne pas saisir sans adaptation.**
```glsl
shader_type spatial;
render_mode unshaded, cull_disabled;

uniform sampler2D noise_texture;
uniform float distortion_strength = 0.01;
uniform float pulse_speed = 1.0;

void fragment() {
    vec2 noise_uv = UV + vec2(TIME * 0.05, -TIME * 0.03);
    float noise = texture(noise_texture, noise_uv).r * 2.0 - 1.0;
    float pulse = 0.5 + 0.5 * sin(TIME * pulse_speed);
    ALBEDO = vec3(0.05, 0.55, 0.75);
    EMISSION = ALBEDO * (1.0 + pulse);
    ALPHA = clamp(0.35 + noise * distortion_strength * 10.0, 0.0, 1.0);
}
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pipeline :** `spatial` cible une surface 3D et `unshaded` évite un éclairage non souhaité.
- **Bruit :** la texture animée module l’apparence sans ajouter de particules.
- **Pulsation :** l’uniform et le temps créent une variation bornée pour l’hologramme.
- **Alpha :** la transparence est limitée afin d’éviter des valeurs hors domaine.
- **Réserve :** la vraie réfraction d’écran et son coût doivent être qualifiés dans Forward+.

## 27. Décalques, maillages et solutions hybrides

Un impact persistant peut être représenté par un décalque ou un petit maillage plutôt que par des particules vivantes. Une onde peut combiner un maillage animé et quelques particules secondaires.

La solution hybride réduit parfois l’aléatoire et facilite le culling. Elle exige cependant une politique de durée, de chevauchement, de nettoyage et de variation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
hybrid_effect:
  burst_particles:
    purpose: immediate_energy_and_direction
    lifetime: short
  decal:
    purpose: persistent_surface_mark
    lifetime: bounded
  mesh:
    purpose: readable_wave_or_volume
    animation: shader_or_animation_player
  cleanup:
    maximum_persistent_marks: candidate
    replacement_policy: oldest_or_least_visible
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Burst :** les particules transmettent l’énergie initiale sans rester actives longtemps.
- **Décalque :** la trace de surface persiste avec un nombre borné.
- **Maillage :** une forme stable porte l’onde ou le volume principal.
- **Nettoyage :** les marques anciennes sont recyclées selon une politique explicite.
- **Variation :** rotation, échelle et texture restent bornées pour éviter les répétitions.

## 28. Simulations précalculées

Une simulation de fumée, liquide, débris ou géométrie peut être calculée hors runtime puis exportée sous forme de cache, flipbook, texture volumique ou séquence de maillages. Le résultat devient un dérivé reproductible, pas une source indépendante.

Le précalcul convient aux phénomènes complexes et répétables. Il est moins adapté lorsqu’une interaction libre avec le monde doit être recalculée selon l’état gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
precomputed_simulation:
  source_scene: art/vfx/sources/AST-VFX-SIM-001.blend
  simulation_domain: documented
  frame_range: documented
  cache:
    path: art/vfx/cache/AST-VFX-SIM-001/
    format: qualified
    generated: true
  runtime_derivative:
    type: flipbook_or_geometry_cache
    interaction_level: limited
  regeneration: source_plus_manifest
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la scène éditable conserve domaines, émetteurs et paramètres.
- **Plage :** les images calculées et la fréquence sont enregistrées.
- **Cache :** le dossier généré peut être recréé et n’est pas modifié manuellement.
- **Runtime :** le dérivé expose seulement les interactions compatibles avec son format.
- **Reconstruction :** source et manifeste suffisent à relancer la production.

## 29. Caches Blender, bake et manifeste

Un bake verrouille un état de simulation. Modifier les paramètres sans effacer et recalculer le cache produit une divergence entre la scène et le résultat enregistré.

Le manifeste conserve version de Blender, scène source, plage d’images, fréquence, résolution, dépendances, empreinte du cache et commande ou procédure de reconstruction. Les caches volumineux suivent la politique de stockage du projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
simulation_manifest:
  id: AST-VFX-SIM-SMOKE-001
  blender_version: 5.2.0
  source_file: art/vfx/sources/AST-VFX-SIM-SMOKE-001.blend
  frame_start: candidate
  frame_end: candidate
  fps: candidate
  domain_resolution: candidate
  cache_directory: art/vfx/cache/AST-VFX-SIM-SMOKE-001/
  cache_sha256: pending
  bake_status: not_executed
  regeneration_procedure: documented_before_bake
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** la version de Blender fait partie du contexte de reconstruction.
- **Source :** le fichier canonique est distinct du répertoire de cache.
- **Paramètres :** plage, fréquence et résolution sont des candidats tant que le bake n’existe pas.
- **Empreinte :** le hash du cache reste `pending` avant matérialisation.
- **Procédure :** la reconstruction est écrite avant d’accepter le dérivé.

## 30. Flipbooks et feuilles d’animation

Un flipbook stocke plusieurs images d’une simulation dans une texture découpée en cellules. Il simplifie le runtime mais peut révéler des boucles, consommer de la mémoire et perdre de la profondeur.

Le preset documente le nombre de colonnes et lignes, la fréquence, la boucle, l’interpolation et la convention d’alpha. La texture source et le processus de génération restent conservés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
flipbook:
  texture: AST-TEX-VFX-SMOKE-FLIPBOOK-001
  grid:
    columns: candidate
    rows: candidate
  frames: candidate
  playback:
    fps: candidate
    loop: false
    interpolation: evaluate
  channels:
    color: documented
    alpha: documented
  source_simulation: AST-VFX-SIM-SMOKE-001
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Grille :** colonnes, lignes et nombre d’images doivent correspondre au shader ou au matériau.
- **Lecture :** fréquence et boucle dépendent du rôle de l’effet.
- **Interpolation :** le lissage entre cases est observé sur les mouvements rapides.
- **Canaux :** la signification de l’alpha et des couleurs est explicite.
- **Traçabilité :** la texture reste liée à la simulation qui l’a produite.

## 31. Feu et fumée

Le feu combine généralement noyau lumineux, flammes, fumée, étincelles et lumière transitoire. Toutes ces couches ne sont pas obligatoires : la distance, le style et le budget déterminent ce qui reste.

La fumée porte le volume et la direction du flux. Elle doit éviter les quads géants superposés devant la caméra. La couleur, la densité et la vitesse dépendent du combustible et de la direction artistique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
fire_smoke_preset:
  layers:
    flame_core:
      technique: flipbook_or_shader
      critical: true
    smoke:
      technique: gpu_particles
      critical: conditional
    sparks:
      technique: gpu_particles
      critical: false
    light:
      technique: pooled_omnilight
      critical: false
  low_quality:
    smoke_amount_ratio: reduced
    dynamic_light: disabled
  safety: no_gameplay_damage_authority
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Noyau :** la forme principale reste lisible même lorsque les couches secondaires sont réduites.
- **Fumée :** quantité, taille et transparence sont adaptées à la distance.
- **Étincelles :** elles renforcent la matière sans devenir indispensables.
- **Lumière :** une source dynamique est optionnelle et mutualisée.
- **Sécurité :** l’effet ne décide jamais si le feu inflige des dégâts.

## 32. Impacts, étincelles et débris

Un impact efficace indique le point, la normale, la direction de la force et la matière touchée. Le système gameplay fournit ces données après avoir validé le contact.

Les étincelles et débris restent visuels. Les fragments de maillage ne remplacent pas les objets physiques autoritaires ; leur collision éventuelle sert seulement à la présentation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
impact_request:
  effect_id: AST-VFX-IMPACT-METAL-001
  position: from_authoritative_hit
  normal: from_authoritative_hit
  incoming_direction: from_authoritative_hit
  material_family: metal
  intensity: normalized_candidate
  visual_debris:
    collision: optional
    gameplay_damage: false
  persistent_mark: optional_decal
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Position :** le point provient du résultat autoritaire, pas d’une particule.
- **Normale :** elle oriente le flash, les étincelles et le décalque.
- **Matière :** la famille sélectionne couleur, débris et son futur sans coder une règle.
- **Débris :** les fragments n’appliquent aucune conséquence.
- **Trace :** le décalque persistant suit une politique de nombre et de durée.

## 33. Magie, énergie et hologrammes

Les effets magiques ou technologiques utilisent formes, couleurs, rythmes et distorsions cohérents avec la bible visuelle. Une couleur ne doit pas être l’unique moyen d’identifier un type d’effet.

L’hologramme pilote combine silhouette stable, lignes de balayage, bruit, pulsation et coupures bornées. Une variante de confort réduit le scintillement et la distorsion.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
energy_language:
  school_or_device: relay_hologram
  identifiers:
    shape: broken_concentric_grid
    rhythm: slow_pulse
    color: cyan_candidate
    motion: upward_scan
  accessibility:
    non_color_cue: shape_and_rhythm
    reduced_flicker_variant: required
    reduced_distortion_variant: required
  gameplay_truth_source: external_system
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Forme :** la géométrie fournit un identifiant perceptible sans dépendre de la couleur.
- **Rythme :** la pulsation indique l’état sans clignotement agressif.
- **Couleur :** la teinte reste une couche supplémentaire de signification.
- **Confort :** des variantes réduisent scintillement et distorsion.
- **Autorité :** l’état réel de l’appareil vient du système gameplay.

## 34. Météo locale et précipitations

La météo visuelle est souvent découpée autour de la caméra ou des zones actives plutôt que simulée sur toute la carte. Pluie, neige, poussière et feuilles utilisent des volumes, masques et variantes selon l’abri.

Le système météo du Livre II décide l’état logique. Le VFX reçoit intensité, direction du vent et zones protégées, puis adapte sa représentation sans modifier la simulation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
weather_vfx_request:
  weather_state: from_world_simulation
  intensity: normalized
  wind_vector: provided
  camera_volume:
    radius: candidate
    height: candidate
  shelter_mask: provided_or_sampled
  layers:
    near_streaks: candidate
    mid_particles: candidate
    distant_fog: candidate
  world_state_writeback: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État :** la météo logique existe avant la représentation.
- **Volume :** les précipitations proches suivent une zone bornée autour du joueur.
- **Abri :** un masque évite la pluie à travers les surfaces protégées.
- **Couches :** proche, milieu et distance peuvent utiliser des techniques différentes.
- **Interdiction :** le preset n’écrit pas dans la simulation du monde.

## 35. Fluides corporels, boue et matières salissantes

Les fluides corporels sont traités selon la classification d’âge, le ton et les options de confort du projet. La version par défaut peut rester stylisée, limitée et désactivable.

Boue, sang stylisé, huile ou autres matières combinent burst, décalque, variation de surface et nettoyage borné. La matière visuelle n’est jamais utilisée pour prouver une blessure ou un état gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
substance_effect:
  family: mud_or_stylized_body_fluid
  content_profile:
    default: restrained
    reduced_or_disabled_variant: required
  layers:
    burst: optional
    decal: optional
    surface_wetness: optional
  persistence:
    maximum_marks: candidate
    cleanup: bounded
  gameplay_injury_authority: external
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** l’intensité respecte le public, le contexte et les préférences.
- **Couches :** burst, trace et surface sont activés selon le besoin.
- **Persistance :** le nombre de marques et leur durée sont bornés.
- **Confort :** une variante réduite ou désactivée reste disponible.
- **Autorité :** l’état de santé est décidé hors du VFX.

## 36. Poussière atmosphérique, brouillard et rayons

La poussière dans un rayon de soleil fonctionne par contraste, faible densité et mouvement lent. Trop de particules détruit l’impression de profondeur et attire l’attention sur le système.

Le brouillard volumétrique, les `FogVolume` et les particules ne sont pas interchangeables. Une atmosphère globale peut utiliser le système de fog, tandis que quelques grains proches ajoutent une échelle locale.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
atmospheric_stack:
  global:
    technique: environment_fog_or_fog_volume
    density: candidate
  local_beam:
    technique: mesh_or_fog_volume
    alignment: light_direction
  suspended_dust:
    technique: sparse_gpu_particles
    speed: slow
    amount: low_candidate
  close_camera_overdraw: test
  readability_preservation: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Global :** le brouillard structure la profondeur à l’échelle de la scène.
- **Rayon :** un volume local suit la direction de lumière approuvée.
- **Grains :** la poussière reste rare et lente pour ne pas ressembler à de la neige.
- **Caméra :** la vue rapprochée révèle l’overdraw et la taille des sprites.
- **Lisibilité :** les silhouettes gameplay restent séparées du fond.

## 37. Buée, condensation et bulles de savon

La buée sur une vitre est une propriété de surface : masque, bruit, variation de rugosité, transparence et zones essuyées. Elle peut utiliser un shader ou une texture animée plutôt qu’un système de particules.

Les bulles de savon demandent iridescence, silhouette sphérique, mouvement lent et éclatement. Le nombre, la taille à l’écran et les reflets doivent rester compatibles avec le renderer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
surface_and_bubbles:
  condensation:
    technique: surface_shader
    controls: [fog_mask, wiped_area, roughness, opacity]
  soap_bubbles:
    technique: gpu_particles_with_sphere_mesh
    controls: [iridescence, drift, size, pop]
  variants:
    low: fewer_bubbles_and_simple_material
    reference: candidate
    high: optional_reflection_detail
  screen_coverage: measure
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Condensation :** la buée suit la surface et ses zones de contact.
- **Bulles :** un petit maillage sphérique porte mieux la silhouette qu’un quad plat.
- **Éclatement :** la fin peut déclencher un sous-effet visuel borné.
- **Profils :** la matière et le nombre varient séparément.
- **Mesure :** réflexions et transparence sont testées selon la couverture d’écran.

## 38. Geysers, jets et écoulements

Un geyser combine colonne principale, gouttelettes, brume, éclaboussures et surface mouillée. La colonne peut utiliser un maillage ou un flipbook ; les particules ajoutent la fragmentation.

La trajectoire et la zone de danger viennent du gameplay ou de la simulation du monde. Le VFX adapte sa hauteur et son intensité à des paramètres bornés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
geyser_layers:
  core_column:
    technique: animated_mesh_or_flipbook
  droplets:
    technique: gpu_particles
    collision: visual_proxy_optional
  mist:
    technique: transparent_particles
  splash:
    technique: burst_and_decal
  parameters:
    height: normalized_input
    intensity: normalized_input
  hazard_authority: external_system
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Colonne :** la forme principale reste stable et lisible à distance.
- **Gouttelettes :** les particules ajoutent la rupture sans définir le volume dangereux.
- **Brume :** la transparence est contrôlée près de la caméra.
- **Éclaboussure :** burst et trace de surface ont une durée bornée.
- **Danger :** le système autoritaire fournit la zone et l’état.

## 39. Éclipses solaire et lunaire

Une éclipse est d’abord un événement d’éclairage et de composition. Le disque occultant, la couronne, la pénombre, la couleur atmosphérique et les ombres doivent rester cohérents avec le ciel et le calendrier du monde.

Le VFX peut fournir une couronne, un halo ou une transition atmosphérique. Le système temporel et astronomique décide l’alignement réel et la durée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
eclipse_visualization:
  event_state: from_world_time_and_celestial_system
  solar:
    layers: [occluding_disk, corona, atmospheric_shift]
  lunar:
    layers: [earth_shadow, color_shift, sky_response]
  transition:
    duration: from_authoritative_event
    comfort_fade: required
  exposure_and_tonemapping: qualify
  world_time_writeback: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Événement :** l’alignement céleste est calculé hors du preset.
- **Solaire :** disque, couronne et atmosphère sont des couches distinctes.
- **Lunaire :** ombre et couleur suivent une logique visuelle séparée.
- **Transition :** un fondu de confort évite une variation brutale.
- **Exposition :** tonemapping et luminosité doivent être testés dans le renderer cible.

## 40. Disque d’accrétion autour d’un trou noir

Le disque d’accrétion exige une lecture claire de la rotation, de la température, de la profondeur et de la silhouette centrale. Une représentation scientifique complète dépasse le besoin d’un VFX de jeu ; le niveau de stylisation est annoncé.

Un maillage annulaire, un shader de flux, des particules rares et un halo peuvent suffire. Toute distorsion gravitationnelle d’écran est traitée comme un effet candidat coûteux et dépendant du renderer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
accretion_disk:
  artistic_model: declared_stylization
  layers:
    disk_mesh: animated_shader
    hot_band: emissive_gradient
    sparse_particles: optional
    central_shadow: mesh_or_mask
    lensing_distortion: optional_candidate
  scale_reference: documented
  scientific_claim: limited
  gameplay_gravity_authority: external
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Modèle :** le chapitre distingue représentation artistique et simulation scientifique.
- **Disque :** le maillage et le shader portent la rotation principale.
- **Émission :** un gradient traduit la température de manière stylisée.
- **Distorsion :** le lensing est optionnel et qualifié séparément.
- **Autorité :** la gravité gameplay ne dépend pas de l’image.

## 41. Traces de pas, traînées et marques au sol

Une trace de pas associe type de surface, orientation, position, intensité et durée. Le système de déplacement ou de terrain valide le contact, puis demande une représentation.

Les traces peuvent employer décalques, maillages, modification de matériau ou texture de terrain selon la plateforme. Leur nombre et leur effacement sont toujours bornés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
footprint_request:
  contact:
    position: authoritative
    normal: authoritative
    foot_id: left_or_right
    surface_family: provided
  visual:
    technique: decal_mesh_or_surface_mask
    opacity: candidate
    lifetime_seconds: candidate
  pool:
    maximum_active: candidate
    eviction: oldest_noncritical
  movement_authority: external
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contact :** position, normale et pied viennent du système d’animation ou de locomotion validé.
- **Surface :** la famille choisit forme, couleur et comportement de la trace.
- **Technique :** le choix dépend du terrain, du renderer et de la persistance.
- **Pool :** un maximum actif empêche l’accumulation infinie.
- **Autorité :** la trace ne confirme pas à elle seule que le pas gameplay a eu lieu.

## 42. Pooling des instances VFX

Créer et détruire une scène à chaque impact peut provoquer des allocations, des pics et une pression sur le ramasse-miettes. Un pool conserve un nombre borné d’instances réutilisables.

Le pool doit réinitialiser l’état du preset : émission, timers, transforms, paramètres, sous-émetteurs et signaux. Une instance recyclée ne doit pas conserver la couleur ou la durée du précédent usage.

> **[VSC] Visual Studio Code — créer ou modifier `res://vfx/runtime/vfx_pool.gd` :**
```gdscript
class_name VfxPool
extends Node

@export var scene: PackedScene
@export_range(1, 256, 1) var capacity: int = 32

var _available: Array[Node3D] = []
var _active: Array[Node3D] = []

func _ready() -> void:
    for index: int in range(capacity):
        var instance := scene.instantiate() as Node3D
        instance.visible = false
        add_child(instance)
        _available.append(instance)

func acquire() -> Node3D:
    if _available.is_empty():
        return null
    var instance: Node3D = _available.pop_back()
    _active.append(instance)
    instance.visible = true
    return instance

func release(instance: Node3D) -> void:
    var active_index: int = _active.find(instance)
    if active_index < 0:
        return
    _active.remove_at(active_index)
    instance.visible = false
    instance.global_transform = Transform3D.IDENTITY
    if instance.has_method("reset_vfx"):
        instance.call("reset_vfx")
    _available.append(instance)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capacité :** le pool préalloue un nombre borné d’instances à qualifier.
- **Acquisition :** la méthode renvoie `null` lorsque le budget est épuisé au lieu de créer sans limite.
- **Libération :** `erase` vérifie que l’instance appartient bien aux actifs.
- **Réinitialisation :** visibilité, transform et état spécifique sont remis à zéro.
- **Limite :** le cast, les signaux et la politique de saturation doivent être testés dans le projet réel.

## 43. Durée de vie, fin visuelle et nettoyage

Un effet one-shot doit avoir une fin certaine, même si une particule, un son futur ou une animation secondaire se bloque. Le contrôleur combine une durée maximale et un signal de fin visuelle.

Les effets continus séparent `start`, `stop_emission` et `finish`. Arrêter l’émission ne supprime pas immédiatement les particules encore vivantes.

> **[VSC] Visual Studio Code — créer ou modifier `res://vfx/runtime/vfx_instance.gd` :**
```gdscript
class_name VfxInstance
extends Node3D

signal visual_finished(instance: VfxInstance)

@export_range(0.05, 60.0, 0.05) var maximum_duration: float = 5.0
@onready var particles: GPUParticles3D = $GPUParticles3D

var _elapsed: float = 0.0
var _running: bool = false

func play() -> void:
    _elapsed = 0.0
    _running = true
    particles.restart()
    particles.emitting = true

func stop_emission() -> void:
    particles.emitting = false

func _process(delta: float) -> void:
    if not _running:
        return
    _elapsed += delta
    if _elapsed >= maximum_duration:
        finish_visual()

func finish_visual() -> void:
    if not _running:
        return
    _running = false
    particles.emitting = false
    visual_finished.emit(self)

func reset_vfx() -> void:
    _running = false
    _elapsed = 0.0
    particles.emitting = false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signal :** `visual_finished` annonce seulement la fin de présentation.
- **Borne :** `maximum_duration` fournit un filet de sécurité candidat.
- **Lecture :** `play` redémarre et réinitialise l’horloge de l’instance.
- **Arrêt :** `stop_emission` laisse les particules existantes terminer selon leur durée.
- **Réinitialisation :** le pool récupère un état neutre sans conséquence gameplay.

## 44. Contrat entre gameplay et VFX

Le système gameplay émet une requête visuelle après avoir décidé l’événement. La requête contient un identifiant d’effet et des données de présentation validées : position, orientation, intensité normalisée et famille de matière.

Le service VFX peut refuser une requête inconnue ou saturée sans annuler l’événement gameplay. L’absence d’effet est une dégradation visuelle, pas un rollback métier.

> **[VSC] Visual Studio Code — créer ou modifier `res://vfx/runtime/vfx_service.gd` :**
```gdscript
class_name VfxService
extends Node

enum RequestResult {
    ACCEPTED,
    UNKNOWN_EFFECT,
    POOL_EXHAUSTED,
    INVALID_REQUEST,
}

var _pools: Dictionary[StringName, VfxPool] = {}

func request_effect(effect_id: StringName, transform: Transform3D, parameters: Dictionary) -> RequestResult:
    if effect_id == StringName():
        return RequestResult.INVALID_REQUEST
    var pool := _pools.get(effect_id) as VfxPool
    if pool == null:
        return RequestResult.UNKNOWN_EFFECT
    var instance := pool.acquire() as VfxInstance
    if instance == null:
        return RequestResult.POOL_EXHAUSTED
    instance.global_transform = transform
    if instance.has_method("apply_visual_parameters"):
        instance.call("apply_visual_parameters", parameters)
    instance.visual_finished.connect(pool.release, CONNECT_ONE_SHOT)
    instance.play()
    return RequestResult.ACCEPTED
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultats :** l’énumération distingue acceptation, identifiant inconnu, saturation et requête invalide.
- **Validation :** l’identifiant et le transform sont contrôlés avant toute acquisition.
- **Pool :** le service ne crée pas une instance lorsque la capacité est épuisée.
- **Paramètres :** le dictionnaire transporte uniquement des données visuelles bornées.
- **Découplage :** un refus VFX ne modifie pas la décision gameplay déjà prise.

## 45. Éclairage, émission et ombres

Les VFX lumineux peuvent utiliser matériau émissif, bloom, lumière dynamique ou combinaison. Une lumière par particule est rarement justifiée ; quelques sources mutualisées donnent souvent une lecture suffisante.

Les ombres, le fog et les contributions environnementales sont évalués séparément. Une fumée qui reçoit toutes les lumières peut devenir opaque ou coûteuse.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
lighting_policy:
  emissive_material:
    default: preferred_for_small_effects
  dynamic_light:
    pooled: true
    maximum_active: candidate
    shadows: disabled_unless_required
    range: bounded
  particle_material:
    vertex_lighting: evaluate
    receives_fog: evaluate
    receives_shadows: evaluate
  exposure_case: test_in_dark_and_bright_scenes
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Émission :** le matériau fournit une impression de lumière sans créer une source réelle.
- **Lumière :** les nœuds dynamiques sont mutualisés et bornés.
- **Ombres :** elles restent désactivées sauf bénéfice clairement observé.
- **Fog :** la contribution atmosphérique est vérifiée pour éviter la disparition du signal.
- **Exposition :** l’effet est testé dans des scènes sombres et lumineuses.

## 46. LOD et variantes de qualité

Le LOD VFX réduit d’abord les couches décoratives, les lumières, la turbulence, les collisions et la résolution des dérivés. Le signal critique garde une forme simple à longue distance.

Les profils `low`, `reference` et `high` sont des presets explicites. Changer `amount` seul ne suffit pas lorsque le coût vient de la transparence, du shader ou de la couverture d’écran.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
quality_profiles:
  low:
    amount_ratio: reduced
    turbulence: false
    collisions: false
    dynamic_light: false
    derivative_resolution: low
  reference:
    amount_ratio: candidate
    turbulence: candidate
    collisions: candidate
    dynamic_light: candidate
    derivative_resolution: reference
  high:
    decorative_layers: optional
    shader_detail: optional
  invariant:
    critical_signal_preserved: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bas :** le profil retire les fonctions coûteuses tout en conservant le signal.
- **Référence :** les candidats sont mesurés sur la configuration principale.
- **Haut :** les couches supplémentaires restent optionnelles et justifiées.
- **Dérivés :** la résolution des flipbooks et caches peut varier par profil.
- **Invariant :** la compréhension de l’événement ne dépend pas du niveau de qualité.

## 47. Tests multi-distance et couverture d’écran

Un effet est observé au contact, à distance de jeu, à la limite de visibilité et hors champ. La taille des sprites, la fréquence d’animation et le contraste peuvent fonctionner à une distance et échouer à une autre.

La matrice inclut aussi plusieurs angles, ratios d’image et vitesses de caméra. Les effets atmosphériques proches sont particulièrement sensibles aux croisements de caméra.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
distance_matrix:
  distances:
    contact: inspect_clipping_and_overdraw
    gameplay: inspect_readability
    far: inspect_simplified_signal
    culled: inspect_clean_disappearance
  views:
    - frontal
    - lateral
    - top_down_candidate
  camera:
    static: true
    fast_pan: true
    crossing_effect: true
  aspect_ratios: [16:9, 16:10, 21:9]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contact :** la vue proche révèle clipping, taille des quads et couches transparentes.
- **Jeu :** la distance nominale vérifie la fonction visuelle.
- **Lointain :** le signal simplifié doit rester stable ou disparaître proprement.
- **Caméra :** panoramique rapide et traversée détectent pops et artefacts.
- **Ratios :** la couverture d’écran est comparée sur plusieurs géométries.

## 48. Budgets par contexte

Un budget VFX combine nombre d’instances, particules vivantes, draw passes, matériaux transparents, lumières, collisions, textures, caches et temps de frame. Il est défini par contexte : combat dense, exploration, cinématique ou météo.

Le chapitre ne fixe pas de chiffres universels. Il prépare des champs à mesurer sur la RX 6750 XT, le Ryzen 7 2700 et les autres profils ciblés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
vfx_budget_context:
  id: AST-VFX-BUDGET-REFERENCE-001
  scenario: relay_storm_combat_candidate
  simultaneous_effects: measure
  live_particles: measure
  transparent_screen_coverage: measure
  dynamic_lights: measure
  collision_proxies: measure
  gpu_frame_time_ms: measure
  cpu_frame_time_ms: measure
  vram_megabytes: measure
  acceptance_thresholds: define_after_baseline
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénario :** le budget est lié à une situation reproductible.
- **Population :** instances et particules vivantes sont relevées ensemble.
- **Pixels :** la couverture transparente complète les simples comptes d’objets.
- **Temps :** CPU et GPU sont mesurés séparément.
- **Seuils :** les limites sont décidées après une baseline réelle.

## 49. Instrumentation candidate

Une instrumentation légère peut compter les requêtes, refus, instances actives et saturations. Elle ne remplace pas le profiler GPU ni les captures du renderer.

Les compteurs sont utiles pour reproduire un scénario et comprendre si une dégradation vient du nombre d’effets ou d’un preset individuel.

> **[VSC] Visual Studio Code — créer ou modifier `res://vfx/runtime/vfx_metrics.gd` :**
```gdscript
class_name VfxMetrics
extends RefCounted

var requested: int = 0
var accepted: int = 0
var unknown_effect: int = 0
var pool_exhausted: int = 0
var invalid_request: int = 0
var active_instances: int = 0
var peak_active_instances: int = 0

func record_result(result: VfxService.RequestResult) -> void:
    requested += 1
    match result:
        VfxService.RequestResult.ACCEPTED:
            accepted += 1
        VfxService.RequestResult.UNKNOWN_EFFECT:
            unknown_effect += 1
        VfxService.RequestResult.POOL_EXHAUSTED:
            pool_exhausted += 1
        VfxService.RequestResult.INVALID_REQUEST:
            invalid_request += 1

func set_active_instances(value: int) -> void:
    active_instances = maxi(value, 0)
    peak_active_instances = maxi(peak_active_instances, active_instances)

func snapshot() -> Dictionary:
    return {
        "requested": requested,
        "accepted": accepted,
        "unknown_effect": unknown_effect,
        "pool_exhausted": pool_exhausted,
        "invalid_request": invalid_request,
        "active_instances": active_instances,
        "peak_active_instances": peak_active_instances,
    }
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Compteurs :** chaque résultat de requête est distingué pour le diagnostic.
- **Pic :** le maximum actif décrit la pression sur les pools pendant le scénario.
- **Snapshot :** le dictionnaire fournit un état sérialisable pour un rapport.
- **Borne :** le nombre actif est corrigé à zéro minimum.
- **Limite :** ces métriques ne mesurent ni overdraw ni temps GPU.

## 50. Scène de test VFX

La scène de test isole les presets sur un fond sombre, un fond clair, une surface métallique, un terrain et une géométrie de collision. Elle fournit des repères de distance et une caméra contrôlable.

Un scénario dense reproduit plusieurs instances simultanées. Les captures, logs et mesures sont associés au commit, au profil de qualité et au renderer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
test_scene:
  path: res://vfx/tests/test_vfx_library.tscn
  environments:
    - dark_neutral
    - bright_neutral
    - relay_reference
  surfaces:
    - metal
    - stone
    - mud
    - glass
  cameras:
    - contact
    - gameplay
    - far
    - moving
  scenarios:
    - isolated
    - simultaneous_reference
    - saturation
  evidence: not_materialized
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Environnements :** les fonds sombres et clairs révèlent les pertes de contraste.
- **Surfaces :** les impacts et projections sont comparés sur plusieurs matières.
- **Caméras :** distance et mouvement sont reproductibles.
- **Scénarios :** isolé, charge nominale et saturation répondent à des questions différentes.
- **Preuve :** la scène et les captures restent à matérialiser.

## 51. Lisibilité, accessibilité et confort

Les flashs, scintillements, secousses, contrastes extrêmes et motifs rapides peuvent gêner ou empêcher certains joueurs. Un effet critique utilise forme, rythme, position ou son futur en plus de la couleur.

Les variantes de confort réduisent flash, distorsion, densité et mouvement de caméra associé sans supprimer l’information nécessaire.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
comfort_profile:
  critical_information:
    color_only: forbidden
    alternative_cues: [shape, rhythm, direction, icon_or_audio_future]
  controls:
    flash_intensity: reducible
    flicker_frequency: bounded
    distortion: reducible_or_disableable
    particle_density: reducible
    screen_shake: separate_system
  photosensitivity_review: required
  subtitle_safe_area: respected_when_cinematic
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Information :** la couleur n’est jamais l’unique canal du signal critique.
- **Flash :** l’intensité et la fréquence sont bornées et réductibles.
- **Distorsion :** une variante peut la supprimer tout en conservant la silhouette.
- **Densité :** le nombre baisse sans effacer la fonction.
- **Revue :** le confort fait partie de l’acceptation, pas d’une correction tardive.

## 52. Organisation Solo et Studio

En Mode Solo, la bibliothèque reste courte : quelques architectures polyvalentes, trois profils de qualité et une scène de test commune. Les effets rares sont documentés comme décisions réutilisables avant toute production coûteuse.

En Mode Studio, chaque famille possède un propriétaire, un budget, une revue art-gameplay-performance et une politique de publication. Les sources, dérivés et caches volumineux suivent des règles de stockage partagées.

Dans les deux modes, la porte d’acceptation reste identique : fonction lisible, provenance qualifiée, paramètres versionnés, dégradation contrôlée et mesures dans le build. Le nombre de personnes ne change pas la définition d’un effet terminé.

### 52.1 Mode Solo

Le producteur seul privilégie les presets d’impact, poussière, fumée, pluie locale et hologramme du pilote. Il évite une simulation précalculée tant qu’un flipbook ou un shader simple répond au besoin.

Une feuille de suivi unique relie identifiant, source, preset, profil de qualité, mesure et décision. La saturation d’un pool produit une dégradation acceptable plutôt qu’une création illimitée.

### 52.2 Mode Studio

Le Studio sépare direction VFX, technical art, intégration, gameplay, performance et validation juridique. Les interfaces de requête et les budgets sont approuvés avant la multiplication des assets.

Les caches et textures générées sont publiés par lot avec manifeste, empreinte et version d’outil. Une revue conjointe décide si une couche artistique justifie son coût.

## 53. Provenance, licences et restrictions

Chaque texture, bruit, flipbook, maillage, cache, shader tiers ou référence visuelle possède une source et une licence. Une ressource libre n’est pas automatiquement redistribuable dans toutes les formes.

Les assets générés par un outil conservent le modèle, la version, les paramètres et les restrictions applicables. Les captures réelles de fluides corporels, de personnes ou de lieux privés demandent une qualification spécifique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
provenance:
  asset_id: AST-VFX-HOLOGRAM-001
  source_type: authored_or_qualified_third_party
  author_or_provider: pending
  license_id: pending
  attribution: pending
  redistribution:
    source_files: pending
    derived_textures: pending
    runtime_build: pending
  generation:
    tool: documented
    version: documented
    parameters: documented
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** l’auteur, le fournisseur ou le processus interne est identifiable.
- **Licence :** un identifiant remplace les termes vagues comme gratuit ou libre.
- **Redistribution :** source, dérivé et build peuvent avoir des droits différents.
- **Génération :** outil, version et paramètres permettent une reprise.
- **Approbation :** le statut reste en attente tant que les droits ne sont pas vérifiés.

## 54. Bibliothèque, presets et paquet de livraison

La bibliothèque VFX publie des scènes de preset, matériaux, textures dérivées, manifests et rapports. Les sources lourdes ou privées peuvent rester dans un stockage de production, mais leur présence et leur accès sont documentés.

Le paquet de livraison n’inclut que les dépendances nécessaires au runtime. Les fichiers de bake, scènes de travail et captures de revue ne sont pas chargés par le jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
delivery_package:
  runtime:
    - res://vfx/presets/
    - res://vfx/materials/
    - res://vfx/textures/
    - res://vfx/runtime/
  production:
    - art/vfx/sources/
    - art/vfx/cache/
    - docs/vfx/
  excluded_from_runtime:
    - source_blend_files
    - raw_simulation_cache
    - review_captures
    - private_legal_documents
  starter_kit_status: not_materialized
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Runtime :** seuls les presets et dépendances nécessaires sont exportés.
- **Production :** sources, caches et rapports restent accessibles au pipeline.
- **Exclusion :** les fichiers lourds ou privés ne sont pas embarqués.
- **Documentation :** le manifeste relie les deux espaces sans exposer de données sensibles.
- **Starter Kit :** aucun paquet réutilisable n’est déclaré produit à ce stade.

## 55. Porte d’acceptation

Un effet n’est accepté que si sa fonction reste lisible, sa source est qualifiée, son preset est versionné, ses variantes sont cohérentes et son coût mesuré dans les scénarios ciblés.

Une réussite artistique ne compense pas une saturation, une licence inconnue ou une information gameplay masquée. Les quatre décisions restent indépendantes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
acceptance_gate:
  artistic:
    intent_and_material_readable: pending
  gameplay:
    critical_information_preserved: pending
    no_authoritative_side_effect: true
  technical:
    quality_profiles_tested: pending
    pooling_and_cleanup_tested: pending
    runtime_budget_measured: pending
  legal:
    provenance_and_license_approved: pending
  decision: blocked_until_all_required_checks_pass
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Artistique :** l’intention, la matière et le rythme sont jugés sur les vues cibles.
- **Gameplay :** le signal critique reste visible et aucune conséquence n’est appliquée.
- **Technique :** profils, nettoyage, saturation et budget demandent des preuves runtime.
- **Juridique :** provenance et droits sont approuvés séparément.
- **Décision :** la porte reste bloquée tant qu’une vérification obligatoire est en attente.

## 56. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 56.1 Le VFX applique directement les dégâts

**Symptôme ou risque :** un ennemi perd des points de vie uniquement lorsque la particule d’impact entre en collision ; un effet désactivé en qualité basse change donc le résultat du combat.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```gdscript
func _on_particle_collision(target: Node) -> void:
    target.apply_damage(25)
    spawn_sparks(target.global_position)
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la conséquence métier dépend d’un événement graphique non garanti, non déterministe et susceptible d’être désactivé. La qualité visuelle devient alors une règle de combat.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```gdscript
func resolve_authoritative_hit(target: CombatTarget, hit: HitResult) -> void:
    target.apply_damage(hit.damage)
    vfx_service.request_effect(
        &"AST-VFX-IMPACT-METAL-001",
        Transform3D(Basis.looking_at(hit.normal), hit.position),
        {"intensity": hit.visual_intensity}
    )
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le système de combat applique d’abord le résultat autoritaire, puis demande une représentation. Un refus ou une réduction du VFX ne modifie pas les dégâts.

### 56.2 La population et la durée de vie sont sans borne

**Symptôme ou risque :** après plusieurs minutes de combat, le nombre d’instances augmente, la mémoire monte et des effets anciens restent actifs hors champ.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
effect:
  spawn_policy: instantiate_every_request
  amount: 5000
  lifetime_seconds: 120
  maximum_instances: unlimited
  cleanup: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la quantité, la durée et les créations simultanées n’ont aucun plafond. Le preset isolé peut sembler correct tandis que la scène accumule des populations impossibles à recycler.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
effect:
  spawn_policy: bounded_pool
  amount: candidate
  lifetime_seconds: candidate
  maximum_instances: candidate
  cleanup: visual_finished_or_timeout
  saturation: degrade_without_gameplay_rollback
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le pool, la durée maximale et la politique de saturation bornent la charge. Les candidats restent à mesurer dans un scénario dense.

### 56.3 La fumée remplit l’écran de quads transparents

**Symptôme ou risque :** à proximité d’un feu, le framerate chute alors que le nombre de particules paraît faible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
smoke:
  quad_size: huge
  texture_trimmed: false
  overlapping_layers: 6
  dynamic_lighting: per_pixel
  close_camera_test: skipped
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la couverture de pixels et l’empilement transparent dominent le coût. Compter uniquement les particules masque l’overdraw réel.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
smoke:
  quad_size: bounded_by_screen_coverage
  texture_trimmed: true
  overlapping_layers: reviewed
  vertex_lighting: evaluate
  close_camera_test: required
  overdraw_measurement: pending
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la texture est recadrée, la taille et les couches sont contrôlées, puis la vue proche est profilée. La décision dépend de mesures et non du seul nombre d’éléments.

### 56.4 Les particules GPU sont censées heurter un PhysicsBody3D

**Symptôme ou risque :** les étincelles traversent le sol malgré la présence d’un collider physique gameplay.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
collision_setup:
  world_collider: StaticBody3D
  particle_collision_proxy: none
  process_material_collision_mode: disabled
  expected: particles_bounce
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les particules GPU n’utilisent pas automatiquement les corps physiques standards et le matériau de traitement désactive en plus les collisions.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
collision_setup:
  world_collider: StaticBody3D
  particle_collision_proxy: GPUParticlesCollisionBox3D
  process_material_collision_mode: rigid
  visibility_aabb_overlap: verified
  fast_particle_case: tested
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un proxy de collision pour particules, un mode compatible et un chevauchement de boîtes satisfont les préconditions. Les particules rapides restent un cas de test séparé.

### 56.5 La visibility AABB reste à sa valeur par défaut

**Symptôme ou risque :** un nuage ou une traînée disparaît dès que l’origine de l’émetteur quitte l’écran, alors que des particules devraient encore être visibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
culling:
  visibility_aabb: default
  maximum_trajectory: unknown
  trail_extent: ignored
  moving_emitter_test: skipped
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la boîte ne couvre ni la trajectoire ni la traînée. Le culling se fonde sur une région trop petite autour de l’origine.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
culling:
  visibility_aabb: generated_then_reviewed
  maximum_trajectory: included
  trail_extent: included
  moving_emitter_test: required
  unrelated_level_space: excluded
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la boîte est dérivée du mouvement attendu puis limitée au volume utile. Les cas avec émetteur mobile et vent sont vérifiés.

### 56.6 Preprocess et Fixed FPS sont augmentés sans mesure

**Symptôme ou risque :** une fumée apparaît déjà établie, mais provoque un pic au chargement et les collisions coûtent trop cher.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
temporal:
  preprocess_seconds: 20
  fixed_fps: 240
  reason: looks_smoother
  startup_profile: absent
  collision_profile: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les valeurs élevées multiplient les étapes de simulation sans objectif mesuré. La formulation esthétique ne définit ni stabilité ni budget.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
temporal:
  preprocess_seconds: smallest_value_that_meets_visual_need
  fixed_fps: collision_and_motion_candidate
  startup_profile: required
  continuous_profile: required
  alternative: thicker_proxy_or_simpler_motion
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque valeur répond à un besoin et fait l’objet de mesures distinctes. Une géométrie de collision plus robuste ou un mouvement simplifié peut éviter une fréquence excessive.

### 56.7 Une nouvelle scène est instanciée pour chaque impact

**Symptôme ou risque :** les rafales d’impacts provoquent allocations, pics et collecte mémoire alors que les effets sont courts et répétitifs.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```gdscript
func spawn_impact(scene: PackedScene, transform: Transform3D) -> void:
    var effect := scene.instantiate() as Node3D
    get_tree().current_scene.add_child(effect)
    effect.global_transform = transform
    effect.tree_exited.connect(func() -> void: effect.queue_free())
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** chaque requête crée une nouvelle hiérarchie et dépend d’une destruction ultérieure. Aucun plafond ni état de saturation n’est défini.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```gdscript
func spawn_impact(effect_id: StringName, transform: Transform3D) -> VfxService.RequestResult:
    return vfx_service.request_effect(
        effect_id,
        transform,
        {"quality_profile": current_quality_profile}
    )
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le service utilise un pool borné, renvoie un statut explicite et applique une politique de qualité. La saturation devient un résultat visuel contrôlé.

### 56.8 Un seul profil de qualité est déclaré universel

**Symptôme ou risque :** l’effet est acceptable sur la configuration de référence mais masque l’action ou dépasse le budget sur un autre profil.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
quality:
  profile: universal
  amount: fixed
  turbulence: always_on
  collision: always_on
  dynamic_light: always_on
  tested_platforms: [reference_only]
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les fonctions coûteuses et la densité ne disposent d’aucun repli. Une seule machine ne prouve pas une compatibilité générale.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
quality:
  profiles: [low, reference, high]
  low:
    critical_signal: preserved
    turbulence: false
    collision: false
    dynamic_light: false
  tested_platforms: targeted_profiles
  decision_scope: limited_to_measured_builds
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les profils retirent les couches coûteuses tout en gardant l’information critique. La conclusion est limitée aux builds et matériels réellement mesurés.

### 56.9 Le cache précalculé n’a ni source ni manifeste

**Symptôme ou risque :** une simulation fonctionne dans un dossier local, mais personne ne sait avec quelle scène, version ou plage d’images elle a été calculée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
cache:
  directory: cache_final/
  source_file: unknown
  blender_version: unknown
  frame_range: unknown
  parameters: unknown
  hash: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le dérivé n’est pas reconstructible et son nom `final` ne décrit aucune qualification. Toute correction oblige à deviner le contexte.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
cache:
  directory: art/vfx/cache/AST-VFX-SIM-001/
  source_file: art/vfx/sources/AST-VFX-SIM-001.blend
  blender_version: 5.2.0
  frame_range: documented
  parameters: documented
  hash: recorded_after_bake
  regeneration: documented
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la source, l’outil, la plage, les paramètres, l’empreinte et la procédure relient le cache à une reconstruction vérifiable.

### 56.10 Le placeholder cinématique est traité comme asset final

**Symptôme ou risque :** un flash temporaire de la timeline du chapitre 22 est copié dans le build sans licence, variante de qualité, test de confort ni budget.

> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
cinematic_dependency:
  source: timeline_placeholder
  status: final
  provenance: absent
  quality_profiles: none
  comfort_variant: none
  runtime_measurement: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un placeholder communique un timing mais ne constitue pas une production VFX approuvée. Il contourne les portes artistique, juridique, technique et de confort.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
cinematic_dependency:
  source: AST-VFX-HOLOGRAM-001
  status: candidate
  provenance: qualified_before_approval
  quality_profiles: [low, reference, high]
  comfort_variant: reduced_flicker_and_distortion
  runtime_measurement: required
  timeline_role: orchestration_only
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la timeline consomme un preset identifié et candidat. Provenance, profils, confort et mesures restent obligatoires avant l’approbation.

## 57. Checklist de production et validation

La checklist est utilisée avant toute déclaration d’acceptation. Une case non vérifiée reste une réserve ; elle n’est pas transformée en réussite par la présence d’un exemple dans ce chapitre.

- [ ] fonction visuelle et priorité définies ;
- [ ] identifiant, version, source et propriétaire enregistrés ;
- [ ] technologie choisie selon le besoin et non par habitude ;
- [ ] paramètres, durées de vie et pools bornés ;
- [ ] transparence, overdraw, lumières et collisions inspectés ;
- [ ] `visibility_aabb` générée puis revue ;
- [ ] variantes `low`, `reference` et `high` comparées ;
- [ ] distance, angle, ratio et mouvement de caméra testés ;
- [ ] variante de confort et repères non colorimétriques disponibles ;
- [ ] cache ou flipbook relié à sa source et à son manifeste ;
- [ ] provenance, licence et redistribution qualifiées ;
- [ ] scène de test et scénarios de saturation matérialisés ;
- [ ] mesures CPU, GPU, mémoire et couverture transparente enregistrées ;
- [ ] aucune règle gameplay appliquée par le VFX ;
- [ ] décision humaine et réserves consignées ;

## 58. Références techniques officielles

Les liens suivants sont les références primaires utilisées pour les particules, les collisions, les shaders, les matériaux transparents, l’optimisation GPU et les simulations précalculées. Ils doivent être relus lors d’une mise à jour de Godot, Blender ou du renderer.

Les pages de classe décrivent les contrats disponibles ; elles ne prouvent pas qu’un preset, un cache ou un budget particulier fonctionne dans Project Asteria.

- [Godot 4.7 — Systèmes de particules 3D](https://docs.godotengine.org/en/4.7/tutorials/3d/particles/index.html)
- [Godot 4.7 — Créer un système de particules 3D](https://docs.godotengine.org/en/4.7/tutorials/3d/particles/creating_a_3d_particle_system.html)
- [Godot 4.7 — Propriétés des particules 3D](https://docs.godotengine.org/en/4.7/tutorials/3d/particles/properties.html)
- [Godot 4.7 — Collisions de particules 3D](https://docs.godotengine.org/en/4.7/tutorials/3d/particles/collision.html)
- [Godot 4.7 — Turbulence des particules](https://docs.godotengine.org/en/4.7/tutorials/3d/particles/turbulence.html)
- [Godot 4.7 — GPUParticles3D](https://docs.godotengine.org/en/4.7/classes/class_gpuparticles3d.html)
- [Godot 4.7 — CPUParticles3D](https://docs.godotengine.org/en/4.7/classes/class_cpuparticles3d.html)
- [Godot 4.7 — ParticleProcessMaterial](https://docs.godotengine.org/en/4.7/classes/class_particleprocessmaterial.html)
- [Godot 4.7 — Référence des shaders](https://docs.godotengine.org/en/4.7/tutorials/shaders/shader_reference/index.html)
- [Godot 4.7 — Optimisation GPU](https://docs.godotengine.org/en/4.7/tutorials/performance/gpu_optimization.html)
- [Godot — StandardMaterial3D et transparence](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html)
- [Blender 5.0 Manual — Cache des fluides](https://docs.blender.org/manual/en/5.0/physics/fluid/type/domain/cache.html)
- [Blender 5.0 Manual — Nœud Simulation](https://docs.blender.org/manual/en/5.0/physics/simulation_nodes.html)
- [Livre III — Chapitre 16 : Textures, matériaux et pipeline PBR](CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md)
- [Livre III — Chapitre 22 : Cinématiques, caméras et mise en scène](CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md)

## 59. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-VFX-PILOT-RELAY-STORM-001` comme pilote commun à la station-relais : impact métallique, étincelles, poussière de sol, fumée froide, hologramme instable et pluie locale. Chaque effet possède une identité, une source canonique, des dérivés régénérables, un preset Godot, un pool borné, trois profils de qualité et une scène de validation à matérialiser. Les demandes arrivent après la décision gameplay et ne transportent que position, orientation, matière et intensité visuelle.

La porte d’acceptation de Project Asteria exige une fonction lisible, une provenance approuvée, une `visibility_aabb` revue, un cycle de vie certain, une saturation contrôlée, une variante de confort, des tests multi-distance et des mesures CPU, GPU, mémoire et overdraw dans le build. Les simulations précalculées doivent être reliées à leur source, leur version d’outil, leur manifeste et leur empreinte. Tant que ces preuves n’existent pas, la bibliothèque reste bloquée au niveau `static-review` et ne revendique ni stabilité, ni coût, ni rendu final.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
asteria_vfx_decisions:
  pilot_id: AST-VFX-PILOT-RELAY-STORM-001
  request_contract: visual_only_after_authoritative_event
  library_root: res://vfx/
  source_root: art/vfx/sources/
  cache_root: art/vfx/cache/
  quality_profiles: [low, reference, high]
  pooling: bounded
  comfort_variant: required
  test_scene: res://vfx/tests/test_vfx_library.tscn
  acceptance: artistic_plus_gameplay_readability_plus_technical_plus_legal
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** le lot de station-relais reste la référence de qualification.
- **Contrat :** le VFX reçoit un événement déjà décidé et n’applique aucun effet métier.
- **Racines :** sources, caches et runtime sont séparés pour permettre la reconstruction.
- **Profils :** qualité et confort font partie du contrat de livraison.
- **Porte :** les quatre domaines doivent réussir sans compensation mutuelle.
- **Réserve :** aucun preset, cache, test ou benchmark n’est déclaré produit.
