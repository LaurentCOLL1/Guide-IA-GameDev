---
title: "Livre III — Chapitre 9 : Création des créatures"
id: "DOC-L3-CH09"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 9
last-verified: "2026-07-23T09:06:37+02:00"
audit-status: "complete"
audit-date: "2026-07-23T09:06:37+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-09.md"
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
    qualification: "documentation-reviewed"
  exchange:
    format: "glTF 2.0"
    default-container: "GLB"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Création des créatures

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH09`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Le chapitre 8 a établi un système de production pour des animaux réels ou directement observables : familles anatomiques, masses, appuis, cycles, surfaces, LOD et scènes de validation. Le présent chapitre ne recommence pas ce travail. Il explique comment partir d'une idée fantastique et la transformer en **créature de production** dont la silhouette, l'anatomie, les mouvements possibles, les volumes de collision et les points d'attache restent cohérents entre concept, Blender et Godot.

Une créature ne devient pas crédible parce qu'elle additionne des cornes, des yeux et des membres. Elle devient lisible lorsque chaque forme répond à une fonction prévue, possède une place dans l'architecture du corps et conserve ses contraintes pendant les poses, les attaques, les LOD et l'import moteur.

Le fil rouge `Project Asteria` utilise un pilote documentaire nommé **Veilleur des brumes**. Il s'agit d'un grand hexapode terrestre : quatre membres porteurs, deux membres antérieurs spécialisés dans l'interaction et la menace, une crête sensorielle et une queue stabilisatrice. Ce pilote sert à tester une anatomie spéculative complète ; il ne constitue ni un ennemi jouable terminé, ni une fiche de statistiques, ni une intelligence artificielle.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Intention narrative et besoin de lecture
    ↓
Fonctions visibles et contraintes
    ↓
Analogues réels sourcés
    ↓
Anatomie spéculative et centre de masse artistique
    ↓
Silhouette primaire, secondaire et tertiaire
    ↓
Blockout métrique et topologie de déformation
    ↓
Profil de rig, sockets et volumes de collision
    ↓
Poses de capacité et tests de lisibilité
    ↓
Variantes et LOD
    ↓
Export GLB et scène Godot dérivée
    ↓
Validation structurelle, visuelle et budgétaire
    ↓
Décision : accepter, corriger ou bloquer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre des dépendances :** une fonction est définie avant la forme qui la représente ; le rig et les collisions arrivent après la stabilisation des masses.
- **Séparation des responsabilités :** les volumes de collision décrivent l'encombrement prévu de l'asset, sans fixer les dégâts, résistances ou règles de combat.
- **Résultat attendu :** chaque décision visuelle peut être reliée à une intention, à une contrainte anatomique et à une preuve à produire.
- **Limite :** aucune étape ne crée l'intelligence artificielle, le comportement autonome, la navigation ou la résolution des attaques du Livre II.


## 2. Résultats d'apprentissage

À la fin du chapitre, le lecteur sait :

- transformer une idée narrative en besoins visuels observables ;
- distinguer inspiration, analogie biologique, extrapolation et invention pure ;
- relier capacité, organe visible, coût, contrepartie et limite ;
- construire une anatomie spéculative cohérente sans prétendre à une vérité scientifique ;
- organiser silhouette primaire, secondaire et tertiaire ;
- vérifier centre de masse artistique, appuis, poussées, freinages et contrepoids ;
- préparer une topologie compatible avec les déformations prévues ;
- décrire un profil de rig sans produire le rig final du chapitre 19 ;
- placer sockets, volumes de collision et zones de lecture sans déplacer l'autorité du gameplay ;
- documenter poses d'anticipation, d'action et de récupération sans produire la bibliothèque d'animations du chapitre 20 ;
- construire des variantes qui conservent l'identité de la créature ;
- définir des LOD qui préservent silhouette, signaux d'action et points d'attache ;
- importer un GLB dans une scène Godot dérivée ;
- écrire un validateur structurel non destructif ;
- préparer des tests de reconnaissance, de collisions, de poses et de coût ;
- conserver des réserves explicites lorsque Blender ou Godot n'ont pas été exécutés.


## 3. Niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Les contrats de données, procédures Blender, principes de collisions et exemple GDScript sont relus contre les références officielles listées en fin de chapitre.

Aucun concept final, aucune planche anatomique, aucun modèle, aucune armature, aucune animation, aucun volume de collision, aucun socket, aucun GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme matérialisés. Les nombres de triangles, d'os, de matériaux, de volumes ou de distances sont des budgets provisoires destinés à être confirmés ou remplacés.

L'anatomie spéculative présentée est une méthode de conception artistique. Elle ne démontre pas qu'un organisme pourrait réellement vivre, respirer, se reproduire ou évoluer. Lorsqu'une capacité dépend d'une physique réelle — vol, nage, sustentation, force, vitesse ou stabilité — le chapitre exige une revue spécialisée avant toute affirmation.


## 4. Périmètre et frontières

Le chapitre définit :

- la fiche de concept fonctionnel d'une créature ;
- une matrice capacité, forme, coût et limitation ;
- les analogues réels et leur provenance ;
- l'anatomie spéculative, les masses et les appuis ;
- les silhouettes et traits distinctifs ;
- le blockout, la topologie et les zones de déformation ;
- le profil préparatoire de rig ;
- les sockets et volumes de collision ;
- les poses de lisibilité ;
- les variantes et LOD ;
- les scènes Godot de validation ;
- les parcours Solo et Studio.

Il ne définit pas :

- les familles animales réelles, cycles zoologiques et surfaces générales déjà traités au chapitre 8 ;
- le lookdev détaillé de la peau, des yeux, des cheveux, du pelage ou des muqueuses du chapitre 10 ;
- les vêtements, armures et accessoires du chapitre 11 ;
- les objets tenus et armes du chapitre 12 ;
- le rig final, les contrôleurs et le skinning de production du chapitre 19 ;
- la bibliothèque d'animations, les blend trees et le root motion du chapitre 20 ;
- les règles de combat, dégâts, faiblesse, ciblage ou statistiques du Livre II ;
- l'intelligence artificielle, la navigation, les perceptions ou les comportements autonomes du Livre II.

> **Frontière essentielle :** le chapitre rend les actions prévues **visuellement et techniquement représentables**. Il ne décide pas si une action réussit, combien elle inflige de dégâts ni quand un agent doit l'utiliser.


## 5. Prérequis

Le lecteur doit connaître :

- la bible visuelle du chapitre 2 ;
- la collecte de références et la provenance des chapitres 3 et 5 ;
- les unités, axes, collections, versions et exports du chapitre 4 ;
- les principes de bases humaines et humanoïdes des chapitres 6 et 7 ;
- les familles animales, masses, appuis, profils de rig et LOD du chapitre 8 ;
- les bases de Blender : maillage, sculpture, armature, contraintes et peinture de poids ;
- les bases de Godot : scènes 3D, import, `Skeleton3D`, `BoneAttachment3D`, `CollisionShape3D`, `AnimationPlayer`, `MeshInstance3D` et ressources.

Le projet doit déjà posséder les dossiers `art/blender`, `art/references`, `art/rig`, `art/exports`, `art/provenance` et `tests/art`, ainsi qu'une convention d'identifiants stables.


## 6. Vocabulaire de production

### 6.1 Anatomie spéculative

Organisation inventée du corps qui reste cohérente avec les fonctions, contraintes et règles visuelles déclarées. Elle peut s'écarter du vivant réel, mais elle ne change pas arbitrairement d'une planche ou d'une pose à l'autre.

### 6.2 Analogue réel

Animal, plante, structure mécanique ou phénomène réel utilisé pour répondre à une question précise. Un analogue n'est pas copié intégralement et ne prouve pas la plausibilité de l'ensemble.

### 6.3 Fonction visible

Capacité ou contrainte qui doit être comprise par la silhouette, la pose ou le mouvement : portage, propulsion, saisie, protection, perception, menace, fuite ou stabilisation.

### 6.4 Contrepartie

Limite visuelle ou mécanique qui empêche une capacité de devenir gratuite : masse supplémentaire, amplitude réduite, exposition, temps de préparation ou perte de stabilité.

### 6.5 Silhouette primaire

Contour global reconnu à grande distance : nombre de masses, hauteur, largeur, posture et ligne d'action.

### 6.6 Silhouette secondaire

Formes qui précisent la famille : membres, tête, queue, ailes, crêtes, carapace et grands appendices.

### 6.7 Détail tertiaire

Écailles, pores, petites pointes, motifs et micro-reliefs. Il enrichit la surface mais ne doit pas porter seul l'identité.

### 6.8 Volume fonctionnel

Volume simplifié associé à une fonction de production : enveloppe corporelle, zone d'interaction, espace de mouvement, socket ou proxy de collision.

### 6.9 Pose de capacité

Pose extrême ou transition courte utilisée pour vérifier qu'une capacité reste lisible et déformable. Elle ne constitue pas une animation finale.

### 6.10 Socket

Point d'attache nommé et versionné, généralement associé à un os ou un nœud, destiné à un effet, un accessoire, une origine de projectile ou une interaction.

### 6.11 Zone de lecture

Région visuelle que le joueur doit identifier : tête, organe sensoriel, membre d'attaque, ouverture, point protégé ou point exposé. Elle ne contient pas nécessairement une règle de dégâts.

### 6.12 Contrat de créature

Ensemble versionné qui relie identité, fonctions, anatomie, rig, collisions, sockets, LOD, provenance et réserves.


## 7. Écrire le brief fonctionnel

Le brief ne commence pas par « une créature impressionnante ». Il décrit où elle apparaît, à quelle distance, sous quel angle, ce que le joueur doit comprendre et quelles actions doivent être reconnaissables.

Pour le Veilleur des brumes, les hypothèses documentaires sont :

- présence dans des zones humides et rocheuses ;
- taille supérieure à un humain, mais compatible avec les couloirs prévus ;
- lecture principale à moyenne distance ;
- locomotion terrestre stable ;
- deux membres antérieurs pouvant menacer, manipuler ou protéger ;
- crête sensorielle visible de face et de trois quarts ;
- queue utilisée comme contrepoids visuel ;
- posture de repos basse et posture d'alerte plus haute ;
- aucune capacité chiffrée ni décision d'IA dans le contrat artistique.

> **[VSC] Visual Studio Code — Créer : `art/creatures/briefs/AST-CRT-MIST-WARDEN-001.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
display_name_working: "Veilleur des brumes"
production_status: concept_contract
narrative_role: "Gardien territorial ancien"
gameplay_reading:
  camera_profile: ASTERIA_GAMEPLAY_CAMERA_v001
  primary_distance: medium
  required_readings:
    - locomotion_direction
    - alert_state
    - manipulation_limb
    - threat_limb
    - exposed_sensor_crest
environment:
  habitat: humid_rocky_lowlands
  doorway_clearance_m: null
  terrain_constraints:
    - uneven_ground
    - shallow_water
scale:
  target_height_m: 2.8
  target_length_m: 5.4
  status: provisional
runtime_authority:
  damage: forbidden
  artificial_intelligence: forbidden
  navigation: forbidden
review:
  art_direction: pending
  anatomy: pending
  gameplay_readability: pending
  provenance: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les dimensions sont des nombres décimaux en mètres ; les listes contiennent des identifiants textuels stables.
- **Valeurs nulles :** `doorway_clearance_m` reste `null` tant que les métriques du niveau ne sont pas disponibles.
- **Frontière :** les trois champs `forbidden` interdisent d'ajouter des règles runtime dans une fiche artistique.
- **Résultat attendu :** le brief fournit des questions vérifiables à la modélisation, au rig et à la scène Godot.


## 8. Construire la matrice fonction, forme, coût et limite

Chaque capacité prévue doit répondre à cinq questions :

1. que doit comprendre le joueur ;
2. quelle forme porte cette information ;
3. quel mouvement ou espace cette forme exige ;
4. quel coût de production elle ajoute ;
5. quelle limite empêche l'ensemble de devenir incohérent.

La matrice sépare une **fonction de lecture** d'une règle de gameplay. Par exemple, un membre peut être identifié comme membre de menace sans contenir un nombre de dégâts.

> **[VSC] Visual Studio Code — Créer : `art/creatures/contracts/CREATURE-FUNCTION-MATRIX.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
functions:
  - function_id: stable_terrestrial_support
    visible_structure:
      - locomotor_leg_front_pair
      - locomotor_leg_rear_pair
      - low_pelvic_mass
    required_motion:
      - compression
      - extension
      - terrain_adaptation
    production_cost:
      rig_chains: 4
      contact_markers: 4
    limitation:
      code: limited_vertical_jump_reading
      note: "La masse et les appuis bas ne suggèrent pas un saut vertical libre."
  - function_id: directed_manipulation
    visible_structure:
      - manipulator_pair
      - shoulder_guard
    required_motion:
      - reach
      - fold
      - cross_body
    production_cost:
      rig_chains: 2
      optional_digits: true
    limitation:
      code: support_reduced_during_use
      note: "Les membres spécialisés ne sont pas les appuis principaux."
  - function_id: sensory_alert
    visible_structure:
      - dorsal_crest
      - head_raise
    required_motion:
      - fold
      - deploy
    production_cost:
      secondary_bones: provisional
    limitation:
      code: crest_exposed_when_deployed
      note: "La crête devient plus visible pendant l'alerte."
gameplay_values_included: false
status: under_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Relations :** chaque entrée relie une fonction à des structures, mouvements, coûts et limites.
- **Entiers et booléens :** `rig_chains` estime un nombre de chaînes ; `optional_digits` indique une décision encore conditionnelle.
- **Invariant :** `gameplay_values_included` reste faux ; aucune valeur de dégâts, de défense ou de vitesse n'est stockée ici.
- **Résultat attendu :** une forme sans fonction ou une fonction sans forme devient immédiatement visible pendant la revue.


## 9. Qualifier les analogues réels

Une anatomie inventée gagne en cohérence lorsqu'elle emprunte des solutions locales à plusieurs analogues réels. Le Veilleur des brumes peut étudier :

- la stabilité et la distribution des masses de grands quadrupèdes ;
- la manipulation de certains membres antérieurs ;
- les queues utilisées comme contrepoids ;
- les crêtes, antennes ou organes déployables ;
- les protections osseuses ou kératinisées ;
- la locomotion sur terrain humide.

Ces analogues répondent à des questions distinctes. Ils ne sont pas fusionnés comme un collage littéral et ne justifient pas à eux seuls une biomécanique complète.

> **[VSC] Visual Studio Code — Créer : `art/references/creatures/MIST-WARDEN-ANALOGS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
reference_set_id: AST-CRT-REF-MW-001
creature_id: AST-CRT-MIST-WARDEN-001
questions:
  - question_id: Q-SUPPORT-001
    text: "Comment répartir une masse longue sur quatre appuis porteurs ?"
  - question_id: Q-MANIP-001
    text: "Comment replier un membre spécialisé sans couper la silhouette du thorax ?"
  - question_id: Q-CREST-001
    text: "Comment une structure sensorielle se déploie-t-elle sans traverser le cou ?"
sources:
  - source_id: REF-MW-SUPPORT-001
    kind: anatomy_reference
    analogue_scope: support_and_mass_only
    answers: [Q-SUPPORT-001]
    provenance_status: under_review
  - source_id: REF-MW-MANIP-001
    kind: motion_reference
    analogue_scope: folding_pattern_only
    answers: [Q-MANIP-001]
    provenance_status: under_review
  - source_id: REF-MW-CREST-001
    kind: morphology_reference
    analogue_scope: deployment_and_overlap_only
    answers: [Q-CREST-001]
    provenance_status: under_review
forbidden_claims:
  - "L'assemblage prouve la viabilité biologique."
  - "Une source unique autorise la copie de l'organisme complet."
review_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** `analogue_scope` limite explicitement ce qui est emprunté à chaque source.
- **Traçabilité :** `answers` relie chaque source à une question de production.
- **Droits :** `provenance_status` reste distinct de la pertinence anatomique.
- **Limite :** les affirmations interdites empêchent de confondre cohérence artistique et preuve scientifique.


## 10. Définir le niveau de spéculation

Toutes les parties d'une créature ne possèdent pas le même niveau de preuve. Le contrat distingue :

- **observé** : solution directement décrite par une référence qualifiée ;
- **extrapolé** : solution dérivée de plusieurs analogues avec hypothèses visibles ;
- **fantastique contraint** : forme inventée, mais soumise à des règles internes ;
- **non résolu** : élément qui bloque la production tant qu'une décision n'est pas prise.

> **[LECTURE] Échelle de spéculation — Ne pas saisir.**

```yaml
speculation_levels:
  observed:
    evidence_required: qualified_reference
    production_rule: preserve_observed_constraint
  extrapolated:
    evidence_required: multiple_analogues
    production_rule: document_assumptions_and_limits
  constrained_fantasy:
    evidence_required: internal_consistency_review
    production_rule: preserve_shape_motion_and_cost_contract
  unresolved:
    evidence_required: none
    production_rule: block_dependent_work
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clés :** chaque niveau est un identifiant fermé, utilisable dans les fiches de structures.
- **Dépendances :** `evidence_required` décrit la preuve minimale avant acceptation.
- **Blocage :** `unresolved` interdit de poursuivre silencieusement une partie dépendante.
- **Résultat attendu :** la revue sait quelles parties sont observées, extrapolées ou purement fantastiques.


## 11. Organiser les masses et le centre de masse artistique

Le centre de masse physique réel dépend de densités, volumes et matériaux qui ne sont pas établis dans un concept. Le chapitre utilise donc un **centre de masse artistique** : un repère visuel qui aide à vérifier si la posture semble soutenue.

Pour le pilote :

- le thorax porte les membres spécialisés ;
- le bassin reste bas et proche des quatre appuis ;
- la tête et la crête créent un poids visuel avant ;
- la queue compense les changements de posture ;
- les membres spécialisés ne sont pas supposés porter la masse principale ;
- la pose d'alerte déplace le poids visuel sans faire flotter les appuis.

> **[VSC] Visual Studio Code — Créer : `art/creatures/anatomy/MIST-WARDEN-MASS-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
units: meters
body_axes:
  forward: "-Y"
  up: "+Z"
landmarks:
  thorax_center: [0.0, -0.65, 1.45]
  pelvis_center: [0.0, 0.45, 1.10]
  head_base: [0.0, -1.45, 1.75]
  tail_base: [0.0, 1.05, 1.20]
visual_mass_reference:
  thorax: 0.34
  pelvis: 0.30
  head_and_crest: 0.12
  locomotor_limbs: 0.14
  manipulator_limbs: 0.06
  tail: 0.04
  sum_expected: 1.0
  physical_mass_claim: false
support_contacts:
  - support_front_left
  - support_front_right
  - support_rear_left
  - support_rear_right
review_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vecteurs :** chaque repère est un tableau de trois nombres `[x, y, z]` en mètres dans les axes Blender retenus.
- **Addition :** les ratios artistiques doivent totaliser `1.0`, ce qui facilite les comparaisons sans prétendre mesurer des kilogrammes.
- **Booléen :** `physical_mass_claim: false` interdit de présenter le profil comme simulation biomécanique.
- **Résultat attendu :** le blockout, le rig et les poses utilisent les mêmes repères de masse et d'appui.


## 12. Vérifier les appuis et le polygone de support

Une pose terrestre paraît stable lorsque la projection du centre de masse artistique reste compatible avec la zone formée par les appuis actifs. Le chapitre n'effectue pas une simulation physique complète ; il documente une règle de revue :

- identifier les appuis réellement actifs ;
- projeter le repère de masse sur le plan du sol ;
- vérifier qu'il ne se situe pas manifestement hors de la zone de support ;
- documenter les poses dynamiques où l'inertie ou un déplacement rapide justifie une exception ;
- ne pas conserver une pose impossible uniquement parce qu'elle paraît spectaculaire.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/SUPPORT-POSES.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
poses:
  - pose_id: neutral_support
    active_contacts:
      - support_front_left
      - support_front_right
      - support_rear_left
      - support_rear_right
    projected_mass_inside_support: not_measured
    dynamic_exception: false
  - pose_id: alert_raise
    active_contacts:
      - support_front_left
      - support_front_right
      - support_rear_left
      - support_rear_right
    projected_mass_inside_support: not_measured
    dynamic_exception: false
  - pose_id: manipulation_reach
    active_contacts:
      - support_front_left
      - support_front_right
      - support_rear_left
      - support_rear_right
    projected_mass_inside_support: not_measured
    dynamic_exception: false
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État non mesuré :** la chaîne `not_measured` distingue une preuve absente d'un résultat faux.
- **Exception :** `dynamic_exception` ne peut être vrai qu'avec une justification de mouvement conservée dans le rapport.
- **Granularité :** chaque pose possède sa propre liste d'appuis et sa propre décision.
- **Limite :** le fichier prépare une revue de stabilité visuelle, pas un solveur physique.


## 13. Construire les trois niveaux de silhouette

### 13.1 Silhouette primaire

La silhouette primaire doit rester reconnaissable en aplat :

- corps long et bas ;
- quatre appuis porteurs ;
- deux membres spécialisés plus hauts ;
- tête inclinée vers l'avant ;
- crête sensorielle déployable ;
- queue longue servant de contrepoids.

### 13.2 Silhouette secondaire

La silhouette secondaire précise :

- différence entre membres porteurs et manipulateurs ;
- articulation visible de la crête ;
- carapace partielle des épaules ;
- séparation thorax, bassin et queue ;
- extrémités d'appui larges pour terrain humide.

### 13.3 Détail tertiaire

Le détail tertiaire comprend motifs, plis, plaques secondaires et micro-reliefs. Il ne doit pas compenser une silhouette primaire faible.

> **[VSC] Visual Studio Code — Créer : `art/creatures/silhouette/MIST-WARDEN-SILHOUETTE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
primary_traits:
  - long_low_body
  - four_support_legs
  - raised_manipulator_pair
  - deployable_dorsal_crest
  - counterbalance_tail
secondary_traits:
  - shoulder_guard_arc
  - broad_wetland_feet
  - segmented_crest_base
  - narrow_head_wide_thorax
tertiary_traits:
  - surface_plate_pattern
  - localized_scars
  - moisture_streaks
distance_tests:
  near: not_executed
  gameplay: not_executed
  far: not_executed
silhouette_decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** les traits sont répartis par importance perceptuelle, pas par ordre de modélisation.
- **Tests :** les trois distances empêchent une validation limitée au gros plan.
- **LOD :** les traits primaires et certains traits secondaires deviendront des contraintes de simplification.
- **Décision :** `pending` reste bloquant tant que les captures ne sont pas produites.


## 14. Définir les vues de contrôle

Une créature peut fonctionner en vue concept et échouer en caméra de jeu. Les vues minimales sont :

- latérale ;
- frontale ;
- arrière ;
- trois quarts avant ;
- trois quarts arrière ;
- dessus ;
- dessous lorsque des collisions ou appuis s'y trouvent ;
- caméra de jeu ;
- contre-plongée si la taille de la créature l'impose.

La focale, la distance et l'éclairage de chaque capture sont enregistrés. Une comparaison n'est valable que si les paramètres restent identiques entre variantes et LOD.

> **[LECTURE] Plan de captures — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "capture_profile": "AST-CREATURE-CAPTURE-v001",
  "views": [
    {"id": "side", "required": true},
    {"id": "front", "required": true},
    {"id": "rear", "required": true},
    {"id": "three_quarter_front", "required": true},
    {"id": "three_quarter_rear", "required": true},
    {"id": "top", "required": true},
    {"id": "gameplay", "required": true}
  ],
  "camera_parameters_locked": true,
  "lighting_profile": "ASTERIA_NEUTRAL_LOOKDEV_v001",
  "status": "planned"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Objets JSON :** chaque vue possède un identifiant et un booléen `required`.
- **Verrouillage :** `camera_parameters_locked` impose une comparaison reproductible.
- **Dépendance :** `lighting_profile` pointe vers un éclairage versionné, sans dupliquer sa définition.
- **Résultat attendu :** les captures peuvent être comparées entre blockout, maillage, LOD et variante.


## 15. Concevoir le blockout métrique

Le blockout répond aux problèmes de volume avant toute surface détaillée. Dans Blender :

1. créer les masses principales avec des primitives simples ;
2. placer les quatre appuis porteurs ;
3. réserver l'espace des deux membres spécialisés ;
4. vérifier la largeur de passage ;
5. tester la hauteur de la pose basse et de la pose d'alerte ;
6. ajouter la queue comme contrepoids ;
7. représenter la crête par un volume simple ;
8. comparer les vues ;
9. conserver les paramètres dans le manifeste ;
10. bloquer la sculpture si les fonctions restent ambiguës.

> **[LECTURE] Collections Blender du pilote — Ne pas saisir.**

```text
CRT_AST_MIST_WARDEN_001
├── 00_REFERENCE
├── 10_FUNCTION_BLOCKOUT
├── 20_ANATOMY_BLOCKOUT
├── 30_SCULPT
├── 40_RETOPO
├── 50_RIG_TEST
├── 60_COLLISION_PROXIES
├── 70_SOCKET_MARKERS
├── 80_LOD_SOURCE
├── 90_VALIDATION
└── __EXPORT
    ├── MESH
    ├── ARMATURE
    ├── COLLISION_PROXIES
    └── SOCKET_MARKERS
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** références, sculpture et LOD sources restent hors de `__EXPORT`.
- **Proxies :** collisions et sockets possèdent des collections propres afin d'éviter leur fusion avec le maillage de rendu.
- **Nommage :** le préfixe `CRT` distingue la famille de production des animaux `ANM`.
- **Reprise :** chaque étape peut être retrouvée sans deviner quel objet est canonique.


## 16. Passer du blockout à l'anatomie spéculative

L'anatomie détaillée ne doit pas contredire le blockout fonctionnel. Pour chaque articulation :

- nommer les segments ;
- déclarer l'axe principal de flexion ;
- déclarer les amplitudes nécessaires ;
- réserver les volumes musculaires ou structurels ;
- identifier les zones rigides ;
- vérifier les intersections ;
- conserver un volume suffisant autour des articulations ;
- documenter les structures fantastiques sans analogue direct.

Les membres spécialisés du Veilleur possèdent une attache thoracique distincte des membres porteurs. Cette séparation évite de faire porter à une même articulation six fonctions incompatibles.

> **[VSC] Visual Studio Code — Créer : `art/creatures/anatomy/MIST-WARDEN-ANATOMY-CONTRACT.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "body_regions": {
    "axial": ["pelvis", "abdomen", "thorax", "neck", "head", "tail"],
    "support_limb_chains": [
      "support_front_left",
      "support_front_right",
      "support_rear_left",
      "support_rear_right"
    ],
    "specialized_limb_chains": [
      "manipulator_left",
      "manipulator_right"
    ],
    "sensory_structures": ["crest"]
  },
  "deformation_hotspots": [
    "thorax_to_manipulator",
    "pelvis_to_rear_support",
    "tail_base",
    "crest_fold",
    "neck_raise"
  ],
  "rigid_regions": [
    "shoulder_guard",
    "crest_core"
  ],
  "unresolved_regions": [],
  "review_status": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tableaux :** les régions regroupent des identifiants stables et non des noms d'affichage.
- **Zones chaudes :** `deformation_hotspots` prépare la topologie, les poids et les poses de test.
- **Rigidité :** `rigid_regions` signale les zones qui ne doivent pas se déformer comme du tissu mou.
- **Blocage :** toute entrée dans `unresolved_regions` doit empêcher la validation du maillage dépendant.


## 17. Préparer la topologie de déformation

La topologie suit les mouvements prévus, non la décoration. Les boucles se concentrent :

- autour des attaches des six membres ;
- aux changements de section du thorax et du bassin ;
- à la base de la queue ;
- à la jonction cou-tête ;
- autour de la crête déployable ;
- aux extrémités qui doivent conserver une forme de contact ;
- aux plaques qui glissent les unes sous les autres.

Une structure fantastique peut nécessiter une topologie originale, mais elle conserve les mêmes contrôles : volume, torsion, pli, collision et silhouette.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/MIST-WARDEN-DEFORMATION-POSES.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
pose_tests:
  - pose_id: neutral_low
    required: true
  - pose_id: alert_high
    required: true
  - pose_id: manipulator_full_reach
    required: true
  - pose_id: manipulator_cross_body
    required: true
  - pose_id: front_support_deep_compression
    required: true
  - pose_id: rear_support_full_extension
    required: true
  - pose_id: neck_max_raise
    required: true
  - pose_id: crest_full_deploy
    required: true
  - pose_id: tail_max_lateral
    required: true
acceptance:
  volume_loss: not_measured
  self_intersection: not_measured
  plate_overlap: not_measured
  silhouette_break: not_measured
  socket_drift: not_measured
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** les poses ciblent les zones qui cumulent déformation et importance de lecture.
- **Mesures séparées :** perte de volume, intersection, chevauchement et dérive de socket ne sont pas fusionnés.
- **Socket :** `socket_drift` vérifie qu'un point d'attache reste cohérent pendant les poses.
- **Frontière :** ces poses préparent le rig final sans définir ses contrôleurs.


## 18. Définir le profil préparatoire de rig

Le profil de rig décrit les os déformants et les chaînes nécessaires. Il ne prescrit pas encore les contrôleurs, les interfaces d'animateur ou les contraintes finales.

Les conventions obligatoires sont :

- un os racine explicite ;
- une pose de repos versionnée ;
- des noms de chaînes stables ;
- une orientation d'os cohérente ;
- des paires gauche-droite vérifiées ;
- des os de déformation séparés des os de contrôle ;
- des budgets d'influences ;
- des sockets associés à des os identifiés ;
- un statut runtime non exécuté.

> **[VSC] Visual Studio Code — Créer : `art/rig/profiles/MIST-WARDEN-RIG-PROFILE.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "rig_profile_id": "AST-RIG-MIST-WARDEN-001-v001",
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "rest_pose": "mist_warden_neutral_low_v001",
  "root_bone": "root",
  "required_chains": {
    "spine": ["pelvis", "spine_01", "spine_02", "thorax", "neck_01", "head"],
    "support_front_left": ["sf_upper.L", "sf_lower.L", "sf_ankle.L", "sf_foot.L"],
    "support_front_right": ["sf_upper.R", "sf_lower.R", "sf_ankle.R", "sf_foot.R"],
    "support_rear_left": ["sr_upper.L", "sr_lower.L", "sr_ankle.L", "sr_foot.L"],
    "support_rear_right": ["sr_upper.R", "sr_lower.R", "sr_ankle.R", "sr_foot.R"],
    "manipulator_left": ["manip_base.L", "manip_upper.L", "manip_lower.L", "manip_tip.L"],
    "manipulator_right": ["manip_base.R", "manip_upper.R", "manip_lower.R", "manip_tip.R"],
    "tail": ["tail_01", "tail_02", "tail_03", "tail_04", "tail_05"],
    "crest": ["crest_01", "crest_02", "crest_03"]
  },
  "orientation_convention": {
    "primary_axis": "bone_local_y",
    "roll_policy": "paired_chains_reviewed"
  },
  "influence_budget": {
    "target_max_per_vertex": 4,
    "exception_max_per_vertex": 8,
    "exception_requires_review": true
  },
  "runtime_status": "not_executed"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dictionnaire :** `required_chains` associe un rôle à une liste ordonnée d'os.
- **Ordre :** les listes vont de l'attache vers l'extrémité, ce qui facilite les contrôles de hiérarchie.
- **Influences :** quatre influences constituent la cible ; huit restent une exception mesurée, jamais une valeur automatiquement acceptée.
- **Frontière :** IK, contraintes, contrôleurs et correctifs de pose restent au chapitre 19.


## 19. Concevoir les sockets

Un socket doit répondre à une consommation connue. Exemples :

- origine d'un effet de crête ;
- point d'attache d'un accessoire ;
- origine visuelle d'une projection ;
- point de saisie d'un objet ;
- repère de caméra de validation ;
- point de contact d'une interaction.

Un socket n'est pas placé « approximativement près de la main ». Il possède un identifiant, un os parent, une transform locale, une orientation et une liste de consommateurs autorisés.

> **[VSC] Visual Studio Code — Créer : `art/creatures/contracts/MIST-WARDEN-SOCKETS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
sockets:
  - socket_id: socket_manipulator_left_tip
    parent_bone: manip_tip.L
    local_position_m: [0.0, -0.18, 0.0]
    local_rotation_deg: [0.0, 0.0, 0.0]
    consumers:
      - interaction_preview
      - held_prop_visual
    gameplay_authority: false
  - socket_id: socket_crest_effect
    parent_bone: crest_03
    local_position_m: [0.0, 0.0, 0.12]
    local_rotation_deg: [0.0, 0.0, 0.0]
    consumers:
      - visual_effect
      - validation_marker
    gameplay_authority: false
  - socket_id: socket_head_focus
    parent_bone: head
    local_position_m: [0.0, -0.35, 0.08]
    local_rotation_deg: [0.0, 0.0, 0.0]
    consumers:
      - focus_marker
    gameplay_authority: false
review_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transforms :** les positions et rotations sont locales à l'os parent, ce qui évite de les enregistrer en coordonnées mondiales fragiles.
- **Consommateurs :** la liste fermée empêche un usage implicite par un système non prévu.
- **Autorité :** `gameplay_authority: false` rappelle que le socket fournit un repère, pas une décision métier.
- **Godot :** l'intégration utilisera un `BoneAttachment3D` ou une structure équivalente liée au `Skeleton3D`.


## 20. Séparer volumes visuels, collisions et zones de lecture

Trois notions ne doivent pas être fusionnées :

1. **maillage de rendu** : forme détaillée destinée à l'image ;
2. **proxy de collision** : forme simplifiée destinée aux contacts physiques ou aux requêtes ;
3. **zone de lecture** : région que la présentation met en évidence.

Une zone de lecture peut être plus petite ou plus grande qu'un proxy. Une règle de dégâts peut ensuite référencer un identifiant de zone, mais elle reste propriétaire de ses valeurs dans le Livre II.

Godot recommande des formes de collision simples pour les objets dynamiques. Une créature articulée ne doit pas utiliser par défaut son maillage détaillé comme collision mobile.

> **[VSC] Visual Studio Code — Créer : `art/creatures/contracts/MIST-WARDEN-COLLISION-PROXIES.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "proxies": [
    {
      "proxy_id": "body_core",
      "shape": "capsule",
      "parent_bone": "spine_02",
      "purpose": ["body_clearance", "contact_query"],
      "dimensions_m": {"radius": 0.72, "height": 2.10},
      "runtime_status": "not_tested"
    },
    {
      "proxy_id": "head",
      "shape": "sphere",
      "parent_bone": "head",
      "purpose": ["clearance", "focus_query"],
      "dimensions_m": {"radius": 0.42},
      "runtime_status": "not_tested"
    },
    {
      "proxy_id": "manipulator_left",
      "shape": "capsule",
      "parent_bone": "manip_lower.L",
      "purpose": ["sweep_preview"],
      "dimensions_m": {"radius": 0.18, "height": 0.90},
      "runtime_status": "not_tested"
    }
  ],
  "damage_values_included": false,
  "mesh_collision_for_dynamic_body": false,
  "decision": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Formes :** les chaînes `capsule` et `sphere` décrivent des familles de `Shape3D` simples.
- **Dimensions :** le dictionnaire varie selon la forme ; une capsule utilise rayon et hauteur, une sphère seulement le rayon.
- **Usages :** `purpose` décrit les requêtes prévues sans promettre leur implémentation.
- **Sécurité d'architecture :** aucune valeur de dégâts n'est incluse et le maillage détaillé n'est pas retenu comme collision dynamique.


## 21. Préparer les zones d'impact sans définir le combat

Le concept peut identifier :

- une zone protégée ;
- une zone exposée pendant une pose ;
- une zone impossible à cibler ;
- un membre dont la perte visuelle demanderait une variante ;
- une surface qui doit transmettre un signal de contact.

Ces zones deviennent des identifiants et des repères. Elles ne contiennent ni multiplicateur de dégâts, ni points de vie, ni effet de statut.

> **[VSC] Visual Studio Code — Créer : `art/creatures/contracts/MIST-WARDEN-READABILITY-ZONES.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
zones:
  - zone_id: crest_exposed
    visual_state_required: crest_deployed
    presentation_cue:
      - silhouette_open
      - material_contrast
    gameplay_values: forbidden
  - zone_id: shoulder_guard
    visual_state_required: any
    presentation_cue:
      - hard_surface
      - low_specular_variation
    gameplay_values: forbidden
  - zone_id: manipulator_tip_left
    visual_state_required: manipulator_extended
    presentation_cue:
      - motion_arc
      - socket_marker
    gameplay_values: forbidden
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conditions :** `visual_state_required` indique quand la zone doit être lisible.
- **Indices :** `presentation_cue` contient des moyens visuels, pas des règles de résultat.
- **Frontière :** `gameplay_values: forbidden` protège l'autorité du système de combat.
- **Résultat attendu :** les artistes, animateurs et développeurs parlent des mêmes zones sans dupliquer les statistiques.


## 22. Définir les poses de capacité

Une capacité prévue doit rester lisible en trois moments :

- **anticipation** : le joueur comprend qu'une action se prépare ;
- **action** : la forme et la direction restent claires ;
- **récupération** : la créature retrouve une posture stable.

Le chapitre ne crée pas les animations finales. Il produit des poses de contrôle qui vérifient :

- espace nécessaire ;
- intersections ;
- continuité du centre de masse artistique ;
- visibilité du membre actif ;
- cohérence des sockets ;
- enveloppe de collision prévue ;
- conservation de la silhouette.

> **[VSC] Visual Studio Code — Créer : `art/animation/manifests/MIST-WARDEN-ABILITY-POSES.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "ability_visual_id": "manipulator_sweep_preview",
  "poses": [
    {
      "pose_id": "anticipation",
      "frame_role": "preparation",
      "required_readings": ["active_side", "sweep_direction"]
    },
    {
      "pose_id": "action_peak",
      "frame_role": "maximum_extension",
      "required_readings": ["active_limb", "clear_arc", "stable_support"]
    },
    {
      "pose_id": "recovery",
      "frame_role": "return_to_support",
      "required_readings": ["reduced_threat", "restored_balance"]
    }
  ],
  "timing_seconds": null,
  "damage_window": "forbidden",
  "runtime_status": "not_executed"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôles :** `frame_role` décrit la fonction visuelle de chaque pose sans imposer un numéro d'image.
- **Temps :** `timing_seconds` reste nul parce que l'animation finale n'existe pas.
- **Interdiction :** `damage_window` n'est pas un champ de durée ; la valeur littérale `forbidden` empêche son usage métier.
- **Résultat attendu :** les poses peuvent être validées avant d'investir dans une animation complète.


## 23. Vérifier les amplitudes et les espaces de mouvement

Chaque appendice possède :

- une amplitude minimale requise ;
- une amplitude maximale autorisée ;
- des zones interdites ;
- une enveloppe de mouvement ;
- des collisions avec le corps ;
- des contraintes de caméra ou de niveau.

Les nombres ne sont pas copiés d'un autre asset. Ils sont établis depuis le blockout, puis mesurés dans Blender et Godot.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/MIST-WARDEN-MOTION-ENVELOPES.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
envelopes:
  - envelope_id: manipulator_left_reach
    parent_chain: manipulator_left
    minimum_reach_m: null
    maximum_reach_m: null
    body_intersection_allowed: false
    floor_intersection_allowed: false
    measured_in_blender: false
    measured_in_godot: false
  - envelope_id: crest_deployment
    parent_chain: crest
    minimum_angle_deg: null
    maximum_angle_deg: null
    neck_intersection_allowed: false
    camera_clipping_reviewed: false
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs :** les distances sont en mètres et les angles en degrés, explicités par le suffixe du champ.
- **Booléens :** les intersections sont refusées par défaut ; une exception demanderait une justification.
- **Double mesure :** Blender et Godot sont séparés pour détecter un changement d'export ou d'import.
- **Résultat attendu :** aucune amplitude n'est déclarée valide avant mesure.


## 24. Construire les surfaces sans anticiper le chapitre 10

Le chapitre 9 définit seulement les surfaces nécessaires à l'identité et à la fonction :

- plaques rigides sur les épaules ;
- membrane ou tissu souple autour de la crête ;
- peau ou couverture générale provisoire ;
- zones humides ou sèches ;
- contrastes nécessaires aux signaux ;
- limites entre matériaux.

Il ne détaille pas les shaders de peau, yeux, dents, muqueuses, cheveux ou pilosité. Ces sujets appartiennent au chapitre 10.

> **[VSC] Visual Studio Code — Créer : `art/creatures/surfaces/MIST-WARDEN-SURFACE-ZONES.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
zones:
  - zone_id: body_soft_surface
    functional_role: flexible_cover
    material_family: provisional_skin
    chapter_10_lookdev_required: true
  - zone_id: shoulder_guard
    functional_role: rigid_protection_reading
    material_family: provisional_plate
    chapter_10_lookdev_required: true
  - zone_id: crest_membrane
    functional_role: deployable_signal
    material_family: provisional_translucent_surface
    chapter_10_lookdev_required: true
material_slots_budget: 4
actual_material_slots: null
export_status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Familles provisoires :** les noms décrivent un besoin et non un shader final.
- **Dépendance :** `chapter_10_lookdev_required` rend explicite le travail laissé au chapitre suivant.
- **Budget :** quatre slots est un plafond de conception à mesurer et non un résultat.
- **Réserve :** aucun matériau ou export n'est déclaré produit.


## 25. Créer des variantes sans diluer l'identité

Une variante acceptable conserve :

- les traits de silhouette primaires ;
- les fonctions visibles ;
- les chaînes de rig nécessaires ;
- les sockets obligatoires ;
- les zones de lecture ;
- les dimensions compatibles ou explicitement requalifiées ;
- les limites de production.

Les variations peuvent porter sur :

- longueur de crête ;
- proportions secondaires ;
- plaques ;
- cicatrices ;
- palette ;
- adaptation régionale ;
- âge visuel ;
- état narratif.

Une variation de proportions peut invalider rig, collisions, animation, LOD et passages de niveau. Elle n'est jamais traitée comme simple changement de couleur.

> **[VSC] Visual Studio Code — Créer : `art/creatures/variants/MIST-WARDEN-VARIANTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
base_variant: adult_standard
identity_traits_required:
  - four_support_legs
  - raised_manipulator_pair
  - deployable_dorsal_crest
  - counterbalance_tail
variants:
  - variant_id: marsh_adult
    changed_domains:
      - color_palette
      - moisture_pattern
      - crest_edge_shape
    rig_compatibility: expected_not_tested
    collision_compatibility: expected_not_tested
  - variant_id: elder_guardian
    changed_domains:
      - proportions
      - plate_volume
      - crest_length
    rig_compatibility: separate_review_required
    collision_compatibility: separate_review_required
    lod_compatibility: separate_review_required
forbidden_inferences:
  - "Une couleur ne fixe pas l'agressivité."
  - "Une grande crête ne fixe pas une valeur de puissance."
  - "Une variante régionale n'est pas automatiquement une nouvelle espèce."
runtime_status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `identity_traits_required` définit les traits qui ne peuvent pas disparaître sans créer une autre créature.
- **Domaines :** chaque variante déclare précisément ce qu'elle modifie.
- **Compatibilité :** une modification de proportions impose des revues séparées du rig, des collisions et des LOD.
- **Frontière :** les inférences de gameplay sont explicitement interdites.


## 26. Définir les LOD de créature

Les LOD doivent préserver plus que les triangles :

- silhouette primaire ;
- séparation des six membres ;
- lecture de la crête ;
- direction du membre actif ;
- sockets nécessaires à la distance concernée ;
- volumes de collision appropriés ;
- matériaux essentiels ;
- ombres et transparences ;
- animations ou représentations compatibles.

Un LOD distant peut remplacer des doigts par une forme fusionnée, mais il ne peut pas transformer un membre de menace en simple excroissance illisible.

> **[VSC] Visual Studio Code — Créer : `art/budgets/MIST-WARDEN-LOD-PROFILE.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "camera_profile": "ASTERIA_GAMEPLAY_CAMERA_v001",
  "lods": [
    {
      "lod": 0,
      "intended_use": "close_inspection",
      "triangle_budget": 90000,
      "deforming_bone_budget": 128,
      "material_slots_budget": 4,
      "required_traits": [
        "crest",
        "six_limb_separation",
        "manipulator_tips",
        "shoulder_guard"
      ]
    },
    {
      "lod": 1,
      "intended_use": "near_gameplay",
      "triangle_budget": 52000,
      "deforming_bone_budget": 96,
      "material_slots_budget": 4,
      "required_traits": [
        "crest",
        "six_limb_separation",
        "manipulator_direction"
      ]
    },
    {
      "lod": 2,
      "intended_use": "mid_gameplay",
      "triangle_budget": 24000,
      "deforming_bone_budget": 64,
      "material_slots_budget": 3,
      "required_traits": [
        "crest",
        "support_vs_manipulator_reading",
        "tail"
      ]
    },
    {
      "lod": 3,
      "intended_use": "far_silhouette",
      "triangle_budget": 7000,
      "deforming_bone_budget": 32,
      "material_slots_budget": 2,
      "required_traits": [
        "primary_silhouette",
        "crest",
        "tail"
      ]
    }
  ],
  "distance_thresholds_m": null,
  "measured_performance": null,
  "status": "provisional"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Budgets :** les nombres sont des plafonds provisoires à confirmer sur le matériel de référence.
- **Traits requis :** chaque LOD possède un contrat perceptuel en plus de son budget.
- **Distances :** `null` interdit d'inventer des seuils avant la scène caméra.
- **Résultat attendu :** une réduction géométrique qui détruit un trait requis est refusée même si elle respecte le nombre de triangles.


## 27. Préparer l'export GLB

L'export suit les conventions du chapitre 4 :

- source `.blend` versionnée ;
- collection `__EXPORT` unique ;
- unités métriques ;
- axes et transforms relus ;
- os de déformation sélectionnés ;
- objets de contrôle exclus lorsque possible ;
- collisions et sockets nommés ;
- LOD explicitement listés ;
- matériaux qualifiés ;
- empreintes calculées après production réelle.

> **[VSC] Visual Studio Code — Créer : `art/exports/creatures/AST-CRT-MIST-WARDEN-001.export.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "asset_id": "AST-CRT-MIST-WARDEN-001",
  "source_blend": "art/blender/creatures/AST-CRT-MIST-WARDEN-001_v001.blend",
  "export_glb": "art/exports/creatures/AST-CRT-MIST-WARDEN-001_v001.glb",
  "export_collection": "__EXPORT",
  "rig_profile_id": "AST-RIG-MIST-WARDEN-001-v001",
  "lods_included": [0, 1, 2, 3],
  "collision_proxy_ids": [
    "body_core",
    "head",
    "manipulator_left"
  ],
  "socket_ids": [
    "socket_manipulator_left_tip",
    "socket_crest_effect",
    "socket_head_focus"
  ],
  "animations_included": [],
  "source_sha256": null,
  "export_sha256": null,
  "export_status": "not_executed"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** rig, collisions et sockets sont référencés par identifiant stable.
- **Animations vides :** le tableau vide confirme qu'aucun clip final n'est prétendu dans ce chapitre.
- **Empreintes :** les SHA-256 restent nulles jusqu'à l'existence des fichiers.
- **Statut :** `not_executed` empêche de confondre le manifeste et un GLB réel.


## 28. Structurer la scène Godot dérivée

La scène importée n'est pas modifiée directement. Une scène dérivée ajoute :

- configuration d'import ;
- collisions ;
- `BoneAttachment3D` pour les sockets ;
- contrôleur de validation ;
- caméras ;
- éclairage ;
- ligne de LOD ;
- marqueurs de silhouette ;
- rapports.

> **[LECTURE] Arbre de scène de validation Godot — Ne pas saisir.**

```text
CreatureValidationLab (Node3D)
├── LightingRig (Node3D)
├── GroundReference (MeshInstance3D)
├── ScaleGrid (Node3D)
├── Cameras (Node3D)
│   ├── CameraNear (Camera3D)
│   ├── CameraGameplay (Camera3D)
│   └── CameraFar (Camera3D)
├── CreatureUnderTest (Node3D)
│   ├── ImportedCreature (instance)
│   ├── Skeleton3D
│   │   ├── CrestEffectSocket (BoneAttachment3D)
│   │   ├── ManipulatorSocket (BoneAttachment3D)
│   │   └── HeadFocusSocket (BoneAttachment3D)
│   ├── CollisionProxies (Node3D)
│   ├── ReadabilityMarkers (Node3D)
│   └── AnimationPlayer
├── LodComparison (Node3D)
│   ├── LOD0
│   ├── LOD1
│   ├── LOD2
│   └── LOD3
└── ValidationController (Node)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scène dérivée :** `ImportedCreature` reste l'instance importée ; les personnalisations sont placées autour d'elle.
- **Sockets :** les `BoneAttachment3D` suivent des os sans transformer le squelette en registre global.
- **Collisions :** les proxies restent regroupés et inspectables séparément du rendu.
- **Comparaison :** les quatre LOD sont visibles dans une même scène pour contrôler la silhouette.


## 29. Écrire le validateur structurel Godot

Le validateur vérifie la présence des éléments attendus. Il ne juge ni la qualité artistique, ni les dégâts, ni l'intelligence artificielle.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/creature_asset_validator.gd` — Ne pas saisir.**

```gdscript
extends Node
class_name CreatureAssetValidator

enum ValidationCode {
    OK,
    MISSING_ASSET_ROOT,
    MISSING_SKELETON,
    MISSING_REQUIRED_BONE,
    MISSING_REQUIRED_SOCKET,
    MISSING_COLLISION_PROXY,
    INVALID_VISUAL_BOUNDS,
    INVALID_PROXY_DIMENSIONS,
}

@export var asset_root_path: NodePath
@export var required_bones: Array[StringName] = []
@export var required_socket_names: Array[StringName] = []
@export var required_proxy_names: Array[StringName] = []
@export var minimum_height_m: float = 0.1
@export var maximum_height_m: float = 20.0

func validate_asset() -> Dictionary:
    var result := {
        "code": ValidationCode.OK,
        "messages": PackedStringArray(),
        "measurements": {}
    }

    var asset_root := get_node_or_null(asset_root_path)
    if asset_root == null:
        result.code = ValidationCode.MISSING_ASSET_ROOT
        result.messages.append("Racine de créature introuvable.")
        return result

    var skeleton := _find_first_skeleton(asset_root)
    if skeleton == null:
        result.code = ValidationCode.MISSING_SKELETON
        result.messages.append("Skeleton3D requis mais absent.")
    else:
        _validate_bones(skeleton, result)

    _validate_named_nodes(
        asset_root,
        required_socket_names,
        "BoneAttachment3D",
        ValidationCode.MISSING_REQUIRED_SOCKET,
        result
    )
    _validate_named_nodes(
        asset_root,
        required_proxy_names,
        "CollisionShape3D",
        ValidationCode.MISSING_COLLISION_PROXY,
        result
    )

    var bounds := _collect_visual_bounds(asset_root)
    result.measurements["aabb_size"] = bounds.size
    var height := bounds.size.y
    result.measurements["height_m"] = height
    if height < minimum_height_m or height > maximum_height_m:
        result.code = _keep_first_error(
            result.code,
            ValidationCode.INVALID_VISUAL_BOUNDS
        )
        result.messages.append(
            "Hauteur visuelle hors plage : %.3f m." % height
        )

    return result

func _find_first_skeleton(root: Node) -> Skeleton3D:
    if root is Skeleton3D:
        return root as Skeleton3D
    for child in root.get_children():
        var found := _find_first_skeleton(child)
        if found != null:
            return found
    return null

func _validate_bones(
    skeleton: Skeleton3D,
    result: Dictionary
) -> void:
    for bone_name in required_bones:
        if skeleton.find_bone(bone_name) == -1:
            result.code = _keep_first_error(
                result.code,
                ValidationCode.MISSING_REQUIRED_BONE
            )
            result.messages.append(
                "Os requis absent : %s." % bone_name
            )

func _validate_named_nodes(
    root: Node,
    required_names: Array[StringName],
    expected_type: String,
    failure_code: int,
    result: Dictionary
) -> void:
    var found_names := {}
    for node in root.find_children("*", expected_type, true, false):
        found_names[StringName(node.name)] = true

    for required_name in required_names:
        if not found_names.has(required_name):
            result.code = _keep_first_error(
                result.code,
                failure_code
            )
            result.messages.append(
                "%s requis absent : %s." % [
                    expected_type,
                    required_name
                ]
            )

func _collect_visual_bounds(root: Node) -> AABB:
    var combined := AABB()
    var initialized := false
    for node in root.find_children("*", "VisualInstance3D", true, false):
        var visual := node as VisualInstance3D
        var world_bounds := visual.global_transform * visual.get_aabb()
        if not initialized:
            combined = world_bounds
            initialized = true
        else:
            combined = combined.merge(world_bounds)
    return combined

func _keep_first_error(current: int, candidate: int) -> int:
    if current == ValidationCode.OK:
        return candidate
    return current
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe et héritage :** `extends Node` permet d'attacher le validateur à la scène ; `class_name` rend le type réutilisable.
- **Énumération :** `ValidationCode` fournit des entiers nommés. `OK` représente l'absence de défaut structurel trouvé.
- **Paramètres exportés :** `NodePath`, `Array[StringName]` et `float` sont configurés dans l'inspecteur. Les deux hauteurs possèdent des valeurs par défaut sûres pour détecter une AABB vide ou aberrante.
- **Retour :** `validate_asset()` renvoie un `Dictionary` détaché avec un code, une collection de messages et des mesures ; il ne modifie pas la créature.
- **Opérateurs :** `== -1` teste l'absence d'un os ; `or` refuse une hauteur sous le minimum ou au-dessus du maximum ; `not` inverse le résultat de `has()`.
- **Recherche récursive :** `_find_first_skeleton()` parcourt les enfants jusqu'au premier `Skeleton3D`.
- **Types attendus :** `_validate_named_nodes()` reçoit le nom de classe Godot sous forme de `String` et utilise `find_children()` pour collecter les nœuds compatibles.
- **AABB :** chaque volume local est transformé dans l'espace global puis fusionné avec `merge()`.
- **Gestion des résultats :** `_keep_first_error()` conserve le premier code bloquant tout en permettant d'ajouter plusieurs messages.
- **Limites :** le script ne teste ni la forme des collisions, ni la dérive des sockets, ni les performances, ni la lisibilité artistique.


## 30. Vérifier les collisions et les sockets dans Godot

Le contrôle runtime à préparer comprend :

- présence des proxies ;
- dimensions positives ;
- absence d'échelle non uniforme sur `CollisionShape3D` ;
- association au bon os ou parent ;
- inclusion raisonnable du maillage ;
- absence de collision avec le corps au repos ;
- suivi pendant les poses ;
- cohérence des sockets entre LOD compatibles ;
- réimport sans perte de configuration.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/COLLISION-SOCKET-REPORT.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
creature_id: AST-CRT-MIST-WARDEN-001
checks:
  collision_shapes_present: not_executed
  dimensions_positive: not_executed
  non_uniform_scale_absent: not_executed
  body_proxy_contains_expected_volume: not_executed
  manipulator_proxy_follows_pose: not_executed
  socket_parent_bones_valid: not_executed
  socket_transform_stable: not_executed
  socket_lod_compatibility: not_executed
  reimport_preserves_scene_overrides: not_executed
measurements:
  maximum_socket_drift_m: null
  maximum_proxy_gap_m: null
  maximum_proxy_penetration_m: null
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** chaque contrôle possède son propre statut pour éviter un « validé » global ambigu.
- **Mesures :** les distances restent nulles avant exécution.
- **Réimport :** le rapport vérifie la conservation des personnalisations de la scène dérivée.
- **Décision :** `pending` reste la valeur sûre d'un rapport vide.


## 31. Tester la lisibilité gameplay sans implémenter le gameplay

Le test de lisibilité demande à une personne ou à une procédure de capture d'identifier :

- direction générale ;
- état de repos ou d'alerte ;
- membre spécialisé actif ;
- direction d'une action préparée ;
- zone exposée ;
- orientation de la tête ;
- différence entre créature et animal réel du chapitre 8 ;
- maintien de ces lectures aux LOD.

Le test ne demande pas de deviner les dégâts, le niveau ou les statistiques.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/READABILITY-TEST-PLAN.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "test_id": "AST-CRT-READABILITY-001",
  "creature_id": "AST-CRT-MIST-WARDEN-001",
  "camera_profiles": [
    "near",
    "gameplay",
    "far"
  ],
  "poses": [
    "neutral_low",
    "alert_high",
    "manipulator_anticipation",
    "manipulator_action_peak"
  ],
  "questions": [
    "orientation_identified",
    "alert_state_identified",
    "active_limb_identified",
    "action_direction_identified",
    "crest_state_identified"
  ],
  "response_time_seconds": null,
  "participants": null,
  "runtime_status": "not_executed",
  "decision": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** caméras et poses sont référencées par identifiant pour reproduire le test.
- **Questions fermées :** les identifiants décrivent ce qui doit être reconnu sans demander une interprétation libre de statistiques.
- **Données absentes :** temps de réponse et nombre de participants restent nuls.
- **Résultat attendu :** la créature ne passe pas la porte tant que les lectures principales ne sont pas démontrées.


## 32. Mesurer le coût

La campagne de performance fixe :

- build ;
- résolution ;
- caméra ;
- nombre de créatures ;
- LOD actifs ;
- nombre d'os déformants ;
- animations actives ;
- collisions actives ;
- ombres ;
- matériaux ;
- durée d'échantillonnage ;
- CPU, GPU, mémoire, triangles et appels de dessin.

Une scène témoin sans créature est obligatoire.

> **[VSC] Visual Studio Code — Créer : `tests/art/creatures/CREATURE-PERFORMANCE-PLAN.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
test_id: AST-CRT-PERF-001
hardware_profile: AMD_RX6750XT_R7_2700_32GB
engine: Godot_4_7_1_ForwardPlus
resolution: [1920, 1080]
camera_profile: ASTERIA_GAMEPLAY_CAMERA_v001
scenarios:
  - scenario_id: baseline_empty
    near_creatures: 0
    mid_creatures: 0
    far_creatures: 0
  - scenario_id: boss_like_single
    near_creatures: 1
    mid_creatures: 0
    far_creatures: 0
  - scenario_id: encounter_mixed_distance
    near_creatures: 1
    mid_creatures: 2
    far_creatures: 4
metrics:
  cpu_frame_ms: not_measured
  gpu_frame_ms: not_measured
  draw_calls: not_measured
  visible_triangles: not_measured
  deforming_bones: not_measured
  video_memory_mb: not_measured
  system_memory_mb: not_measured
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Témoin :** `baseline_empty` permet d'estimer le coût ajouté par les créatures.
- **Scénarios :** proximité et densité changent séparément.
- **Mesures :** aucune valeur n'est préremplie ni dérivée d'un autre projet.
- **Limite :** le plan ne promet aucune performance tant que la scène n'est pas exécutée.


## 33. Provenance, licences et contenus sensibles

Le pilote relie :

- concepts et moodboards ;
- références réelles ;
- modèles, scans ou bases achetés ;
- modèles IA, workflows et entrées génératives ;
- textures et matériaux ;
- fichiers Blender ;
- exports ;
- transformations ;
- auteur et responsable de validation ;
- restrictions de redistribution.

Une créature inspirée d'une œuvre existante peut devenir juridiquement problématique même si sa topologie est originale. La revue doit rechercher une proximité de silhouette, de signes distinctifs, de nom et de contexte.

> **[VSC] Visual Studio Code — Créer : `art/provenance/MIST-WARDEN-ASSET-RECORD.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: AST-CRT-MIST-WARDEN-001
asset_kind: creature_pilot
sources:
  concept_boards: []
  real_world_references:
    - reference_set_id: AST-CRT-REF-MW-001
  purchased_models: []
  scans: []
  generated_inputs: []
rights:
  production_use: under_review
  redistribution: forbidden_until_review
  similarity_review: pending
  attribution_required: unknown
transformations:
  - "Functional brief."
  - "Original speculative anatomy."
  - "Original modeling planned."
delivery:
  source_blend: planned
  export_glb: planned
  manifests: planned
decision: blocked_until_rights_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tableaux vides :** une catégorie sans source est explicitement vide ; elle n'est pas omise.
- **Similarité :** `similarity_review` ajoute une porte distincte des licences de fichiers.
- **Décision :** la livraison reste bloquée tant que les droits ne sont pas qualifiés.
- **Frontière :** le document enregistre un statut et ne fournit pas d'avis juridique personnalisé.


## 34. Parcours Mode Solo

En Mode Solo :

1. produire une seule créature pilote complète ;
2. limiter les fonctions à celles nécessaires au vertical slice ;
3. utiliser un nombre réduit de chaînes et de sockets ;
4. préparer quatre poses de capacité ;
5. créer des proxies simples ;
6. produire trois ou quatre LOD seulement si la caméra les exige ;
7. réutiliser le laboratoire de validation ;
8. bloquer les variantes avant la validation du pilote ;
9. conserver tous les manifestes ;
10. préférer une identité forte à une accumulation de détails.

L'objectif est de démontrer une chaîne complète avant de multiplier les espèces ou variantes.


## 35. Parcours Mode Studio

En Mode Studio :

- attribuer des propriétaires au concept, à l'anatomie, au modèle, au rig, aux collisions et à l'intégration ;
- organiser une revue croisée concept, animation, gameplay et technique ;
- versionner toutes les matrices ;
- maintenir une bibliothèque de poses ;
- relier sockets et zones de lecture aux consommateurs autorisés ;
- enregistrer les changements de dimensions ;
- mesurer les conséquences sur niveaux, caméras et collisions ;
- séparer décision artistique et décision gameplay ;
- conserver les captures et rapports par build ;
- automatiser uniquement les contrôles structurels et mesurables ;
- faire valider humainement la silhouette et la lisibilité.


## 36. Porte d'acceptation

> **[LECTURE] Checklist d'acceptation d'une créature pilote — Ne pas saisir.**

```yaml
identity_and_rights:
  stable_creature_id: false
  functional_brief_approved: false
  analogues_qualified: false
  rights_review_complete: false
anatomy:
  speculation_levels_declared: false
  mass_profile_reviewed: false
  support_poses_reviewed: false
  deformation_regions_defined: false
silhouette:
  primary_traits_reviewed: false
  gameplay_camera_readable: false
  far_lod_readable: false
rig_and_sockets:
  rig_profile_versioned: false
  required_bones_present: false
  sockets_present: false
  socket_pose_tests_passed: false
collisions_and_zones:
  proxy_contract_versioned: false
  proxy_shapes_tested: false
  readability_zones_documented: false
godot:
  glb_imported: false
  derived_scene_created: false
  structural_validator_passed: false
  reimport_test_passed: false
performance:
  reference_scenarios_measured: false
  budget_decision_recorded: false
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portes indépendantes :** droits, anatomie, silhouette, rig, collisions, Godot et performance peuvent bloquer séparément.
- **État initial :** toutes les valeurs sont fausses avant preuve réelle.
- **Décision :** `blocked` est obligatoire pour un template non exécuté.
- **Résultat attendu :** le passage à `accepted` exige des rapports conservés, pas une validation orale.

## 37. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->


### 37.1 Ajouter des appendices sans fonction

**Symptôme :** la créature possède de nombreux membres et cornes, mais personne ne sait lesquels portent, attaquent ou perçoivent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
appendage: horn_pair_07
function: decorative
motion_requirement: unknown
rig_cost: ignored
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une forme coûte topologie, rig, animation, collisions et LOD sans apporter une lecture ou une fonction vérifiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
appendage: dorsal_crest
function: sensory_alert
motion_requirement: deploy_and_fold
rig_cost: reviewed
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction relie la forme à une fonction, à un mouvement et à un coût à revoir.


### 37.2 Concevoir une attaque avant les appuis

**Symptôme :** la pose d'action semble puissante, mais le corps flotte ou bascule dès que le membre spécialisé s'étend.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
pose: attack_peak
active_supports: unknown
mass_projection: ignored
decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une extension importante déplace le poids visuel et ne peut pas être validée sans appuis ni stabilité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
pose: manipulator_action_peak
active_supports:
  - support_front_left
  - support_front_right
  - support_rear_left
  - support_rear_right
mass_projection: pending_measurement
decision: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction rend les appuis explicites et bloque la décision jusqu'à la mesure.


### 37.3 Remplacer la silhouette par des détails

**Symptôme :** la créature paraît unique en gros plan, mais devient une masse générique à la caméra de jeu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
identity:
  primary_silhouette: generic_quadruped
  tertiary_details: 120_unique_scales
gameplay_view: not_tested
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les micro-détails disparaissent avec la distance, les mipmaps et les LOD.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
identity:
  primary_silhouette:
    - four_support_legs
    - raised_manipulator_pair
    - deployable_dorsal_crest
  tertiary_details: optional
gameplay_view: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction porte l'identité sur des formes visibles à distance et rend la vue de jeu obligatoire.


### 37.4 Utiliser le maillage rendu comme collision dynamique

**Symptôme :** les contacts sont instables et le coût physique augmente avec chaque détail du modèle.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
dynamic_collision:
  source: render_mesh_lod0
  shape: concave
  simplification: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un maillage concave détaillé n'est pas le proxy mobile de référence et couple la physique au rendu.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
dynamic_collision:
  source: authored_proxies
  shapes:
    - capsule
    - sphere
  render_mesh_dependency: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise des formes simples séparées du maillage visuel.


### 37.5 Mettre des dégâts dans la fiche artistique

**Symptôme :** une modification de silhouette change silencieusement les valeurs de combat.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
zone_id: crest_exposed
damage_multiplier: 2.5
stun_seconds: 4.0
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les valeurs de combat appartiennent à l'autorité du Livre II et ne doivent pas être définies par l'asset.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
zone_id: crest_exposed
presentation_cue:
  - silhouette_open
  - material_contrast
gameplay_values: forbidden
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve la lecture visuelle et interdit les valeurs métier.


### 37.6 Placer un socket en coordonnées mondiales

**Symptôme :** le point d'effet se décale après déplacement, rotation ou réimport de la créature.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
socket_id: crest_effect
world_position: [12.4, 3.1, -8.7]
parent_bone: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une position mondiale dépend de la scène et ne suit pas l'os pendant les poses.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
socket_id: socket_crest_effect
parent_bone: crest_03
local_position_m: [0.0, 0.0, 0.12]
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction exprime le socket dans l'espace local de l'os parent.


### 37.7 Forcer la créature dans un profil animal existant

**Symptôme :** les six membres partagent des chaînes inadaptées et les poses spécialisées deviennent impossibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
rig_profile: AST-RIG-QUAD-001-v001
creature: hexapod_with_manipulators
compatibility: assumed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le profil quadrupède du chapitre 8 ne décrit pas les deux membres spécialisés ni la crête.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
rig_profile: AST-RIG-MIST-WARDEN-001-v001
creature: AST-CRT-MIST-WARDEN-001
compatibility: tested_per_chain
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction crée un contrat propre et exige une compatibilité par chaîne.


### 37.8 Créer des variantes par échelle aléatoire

**Symptôme :** les collisions, sockets et animations ne correspondent plus aux proportions.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
variant_generation:
  scale_range: [0.6, 1.8]
  rig_recheck: false
  collision_recheck: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une échelle globale extrême modifie passages, vitesse visuelle, portée, volumes et contraintes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
variant_generation:
  changed_domains:
    - proportions
  rig_recheck: required
  collision_recheck: required
  level_clearance_recheck: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction révèle les dépendances et impose leur requalification.


### 37.9 Supprimer les signaux d'action dans les LOD

**Symptôme :** la créature reste visible, mais le membre actif et la crête disparaissent avant que l'action ne soit lisible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod2:
  triangles: 18000
  crest: removed
  manipulator_separation: merged
  budget_status: passed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le budget géométrique ne suffit pas si les traits nécessaires au gameplay visuel disparaissent.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod2:
  triangles: 18000
  crest: preserved
  manipulator_direction: preserved
  readability_test: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction protège les traits requis et maintient le test en attente.


### 37.10 Déclarer la créature terminée sans Godot

**Symptôme :** le modèle est accepté dans Blender alors que collisions, sockets, LOD et réimport n'ont jamais été vérifiés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
validator: not_executed
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une revue Blender ne prouve ni le contrat d'import, ni les nœuds, ni les collisions, ni les performances.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
validator: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve le blocage jusqu'aux preuves moteur.


## 38. Livrables à conserver

Le plan maître exige cinq livrables permanents :

1. **fiches de créatures** — rôle, fonctions, limites, analogues et statut ;
2. **planches anatomiques** — masses, appuis, silhouettes, articulations et zones de déformation ;
3. **modèles pilotes** — sources Blender et exports lorsqu'ils seront matérialisés ;
4. **rigs et volumes de collision** — profils, sockets, proxies et rapports ;
5. **tests de lisibilité gameplay** — captures, poses, LOD et résultats.

> **[LECTURE] Arborescence finale attendue — Ne pas saisir.**

```text
art/
├── blender/creatures/
├── creatures/
│   ├── briefs/
│   ├── contracts/
│   ├── anatomy/
│   ├── silhouette/
│   ├── surfaces/
│   └── variants/
├── references/creatures/
├── rig/profiles/
├── animation/manifests/
├── budgets/
├── exports/creatures/
└── provenance/
tests/
└── art/creatures/
    ├── creature_validation_lab.tscn
    ├── creature_asset_validator.gd
    ├── reports/
    └── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les fichiers Blender et références restent séparés des exports.
- **Contrats :** briefs, anatomie, collisions, sockets, surfaces et variantes possèdent des dossiers identifiables.
- **Tests :** scènes, scripts, rapports et captures sont regroupés sous `tests/art/creatures`.
- **Publication :** les rapports QA internes ne sont pas ajoutés au manuel lecteur.


## 39. Synthèse opérationnelle pour Project Asteria

Le chapitre 9 fournit à `Project Asteria` une méthode complète pour transformer un concept fantastique en créature de production. Le Veilleur des brumes est défini par un brief fonctionnel, une matrice de capacités, des analogues limités, une anatomie spéculative, des masses, des appuis, une silhouette, une topologie préparatoire, un profil de rig, des sockets, des proxies de collision, des zones de lecture, des poses, des variantes, des LOD et une scène Godot de validation.

L'asset reste bloqué tant que les concepts, modèles, rigs, collisions, sockets, exports, scènes, tests de lisibilité et mesures ne sont pas matérialisés. Le chapitre ne revendique donc aucune créature terminée. Il prépare les chapitres 10, 19, 20 et 23 sans redéfinir le lookdev détaillé, le rig final, l'animation de production, les VFX ou les systèmes de gameplay du Livre II.


## 40. Références techniques officielles

Les références suivantes ont été consultées pour qualifier les fonctions et limites citées :

- [Blender Manual — Armature Structure](https://docs.blender.org/manual/en/5.0/animation/armatures/structure.html) ;
- [Blender Manual — Bone Roll](https://docs.blender.org/manual/en/latest/animation/armatures/bones/editing/bone_roll.html) ;
- [Blender Manual — Bone Constraints](https://docs.blender.org/manual/en/3.4/animation/armatures/posing/bone_constraints/introduction.html) ;
- [Blender Manual — Inverse Kinematics](https://docs.blender.org/manual/en/3.6/animation/armatures/bones/properties/inverse_kinematics.html) ;
- [Blender Manual — Retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) ;
- [Blender Manual — Mirror Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/mirror.html) ;
- [Godot 4.7 — Skeleton3D](https://docs.godotengine.org/en/4.7/classes/class_skeleton3d.html) ;
- [Godot 4.7 — BoneAttachment3D](https://docs.godotengine.org/en/4.7/classes/class_boneattachment3d.html) ;
- [Godot 4.7 — CollisionShape3D](https://docs.godotengine.org/en/4.7/classes/class_collisionshape3d.html) ;
- [Godot 4.7 — Shape3D](https://docs.godotengine.org/en/4.7/classes/class_shape3d.html) ;
- [Godot 4.7 — Collision shapes 3D](https://docs.godotengine.org/en/4.7/tutorials/physics/collision_shapes_3d.html) ;
- [Godot 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) ;
- [Godot 4.7 — ResourceImporterScene](https://docs.godotengine.org/en/4.7/classes/class_resourceimporterscene.html) ;
- [Godot — Mesh level of detail](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html) ;
- [Godot — Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html).

Les pages `latest` ou `stable` ne sont utilisées que lorsqu'une page `4.7` ou `5.0` équivalente n'est pas exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d'appliquer la procédure.
