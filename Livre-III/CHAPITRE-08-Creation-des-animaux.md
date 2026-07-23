---
title: "Livre III — Chapitre 8 : Création des animaux"
id: "DOC-L3-CH08"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 8
last-verified: "2026-07-23T04:29:27+02:00"
audit-status: "complete"
audit-date: "2026-07-23T04:29:27+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-08.md"
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

# Création des animaux

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH08`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Les chapitres 6 et 7 ont établi les contrats de production des humains et des humanoïdes. Le présent chapitre change de problème : il organise la création d’animaux dont la silhouette, les appuis, les masses, les surfaces et les cycles de locomotion dépendent d’une anatomie propre, sans forcer ces assets dans une structure humaine.

Le résultat attendu n’est pas une encyclopédie zoologique ni une bibliothèque d’animations finale. Il s’agit d’un **système de production animal** capable de qualifier plusieurs familles — quadrupèdes, oiseaux, poissons, reptiles et morphologies particulières — avec des fiches anatomiques, des profils de rig, des cycles pilotes, des budgets et des scènes Godot de validation.

Le fil rouge `Project Asteria` retient cinq pilotes documentaires : un quadrupède terrestre, un oiseau, un poisson, un reptile bas et une morphologie serpentine. Ces pilotes servent à éprouver les contrats communs ; ils ne constituent pas des espèces de gameplay terminées.
> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Références sourcées et questions anatomiques
    ↓
Fiche de famille et pilote animal
    ↓
Répartition des masses, appuis et amplitude
    ↓
Base maillée et topologie de déformation
    ↓
Profil de rig et tests de skinning
    ↓
Cycles de locomotion pilotes
    ↓
Surface : peau, écailles, plumes ou pelage
    ↓
LOD, budgets et représentation de groupe
    ↓
Export GLB et import Godot
    ↓
Scènes de silhouette, contact, mouvement et coût
    ↓
Décision : accepter, corriger ou bloquer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** la chaîne place l’observation fonctionnelle avant le rig, l’animation ou l’optimisation.
- **Invariant :** un asset proche, un LOD skinné et une représentation distante sont trois livrables distincts.
- **Résultat attendu :** chaque décision peut être reliée à une question anatomique, à un budget et à une scène de test.
- **Limite :** aucune étape ne crée les comportements autonomes ou la simulation écologique du Livre II.


## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- choisir des pilotes animaux représentatifs des besoins réels du projet ;
- constituer des références anatomiques et locomotrices traçables ;
- lire répartition des masses, centre de gravité visuel, colonne, ceintures, membres et contacts ;
- distinguer architecture quadrupède, avienne, aquatique, reptilienne et serpentine ;
- concevoir une base maillée qui conserve silhouette et déformation ;
- définir un profil de rig adapté sans réutiliser aveuglément un squelette humain ;
- préparer des cycles de marche, course, vol, nage et repos comme données mesurables ;
- décider quand employer géométrie, cartes, courbes de cheveux, textures ou imposteurs pour les surfaces ;
- produire des variantes pertinentes d’âge, de sexe, de saison ou de biome sans les rendre obligatoires ;
- définir des LOD qui préservent les traits de reconnaissance et les contacts ;
- distinguer scènes animales proches, LOD skinnés et représentations de groupe distantes ;
- configurer une scène Godot de validation visuelle, structurelle et budgétaire ;
- documenter les réserves sans inventer de mesures runtime.

## 3. Niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Les contrats de données, les procédures Blender, les choix d’export et les scripts Godot ont été relus contre les documentations officielles indiquées en fin de chapitre.

Aucun modèle animal, aucune armature, aucun cycle, aucun système de pelage, aucune texture, aucun export GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme matérialisés. Les nombres de triangles, d’os, de matériaux, de textures, d’instances et de distances sont des **budgets de conception provisoires**.

Les descriptions anatomiques servent à la production 3D. Elles ne remplacent ni une expertise vétérinaire, ni une étude biomécanique, ni une observation propre à une espèce réelle. Les exemples de contacts et de cycles sont des formats de travail : ils doivent être renseignés depuis des références qualifiées pour le pilote effectivement produit.

## 4. Périmètre et frontières

Le chapitre définit :

- les fiches de familles et de pilotes animaux ;
- les références anatomiques et locomotrices ;
- les règles de répartition des masses et des contacts ;
- les topologies et profils de rig préparatoires ;
- les cycles pilotes et leurs métadonnées ;
- les stratégies de pelage, plumes, écailles et surfaces lisses ;
- les variantes pertinentes ;
- les budgets, LOD et représentations de groupes ;
- les scènes Godot de validation ;
- les procédures Solo et Studio.

Il ne définit pas :

- les créatures fantastiques et anatomies inventées du chapitre 9 ;
- le lookdev détaillé commun du chapitre 10 ;
- les vêtements, harnachements et accessoires du chapitre 11 ;
- le rig final et le skinning de production du chapitre 19 ;
- la bibliothèque d’animations finale, le retargeting et les transitions de production du chapitre 20 ;
- le comportement autonome, la prédation, les populations, la reproduction ou l’écologie du Livre II ;
- la navigation, l’évitement, l’IA, les dégâts ou les statistiques de gameplay.

> **Frontière essentielle :** ce chapitre produit des **assets visuels et des contrats de mouvement**. Il ne décide pas pourquoi, quand ou vers où un animal se déplace en jeu.

## 5. Prérequis

Le lecteur doit connaître :

- la bible visuelle du chapitre 2 ;
- les règles de références et de provenance des chapitres 3 et 5 ;
- les unités, axes, collections et exports du chapitre 4 ;
- les contrats de topologie, modules, LOD et validation du chapitre 6 ;
- les principes de profils anatomiques et d’incompatibilités du chapitre 7 ;
- les bases de Blender : maillage, sculpture, armatures, peinture de poids, courbes et Geometry Nodes ;
- les bases de Godot : scènes 3D, import, `Skeleton3D`, `AnimationPlayer`, `AnimationTree`, `MeshInstance3D` et ressources.

Le projet doit déjà disposer d’une arborescence `art/blender`, `art/exports`, `art/manifests` et `tests/art`, ainsi que d’un registre de provenance et d’une convention d’identifiants stables.

## 6. Vocabulaire de production


### 6.1 Famille anatomique

Regroupement de problèmes de production partageant une architecture de corps, des appuis et des contraintes de mouvement. Une famille de production n’est pas une classification biologique complète.

### 6.2 Pilote animal

Asset choisi pour tester une famille avant de multiplier les variantes. Il porte un identifiant, un besoin de jeu, un budget et une liste de réserves.

### 6.3 Ligne d’action

Courbe dominante de la colonne, du cou ou du corps qui organise la lecture de la pose et de la propulsion.

### 6.4 Appui

Zone de contact prévue avec le sol, l’eau, l’air ou un support. Un appui peut être ponctuel, glissant, alterné ou continu selon le pilote.

### 6.5 Phase de contact

Intervalle d’un cycle pendant lequel une extrémité ou une surface participe au support ou à la propulsion.

### 6.6 Phase de transfert

Intervalle pendant lequel une masse ou un membre change de position sans porter l’appui principal.

### 6.7 Cycle pilote

Animation courte utilisée pour vérifier rythme, contacts, amplitude et répétition. Elle n’est pas automatiquement une animation finale.

### 6.8 Profil de rig

Contrat versionné qui décrit hiérarchie, os requis, os optionnels, orientations, pose de repos, limites et compatibilités.

### 6.9 Surface primaire

Peau, écailles, plumes, pelage ou autre couverture qui influence silhouette, matériau, géométrie et LOD.

### 6.10 Représentation de groupe

Forme optimisée destinée à afficher plusieurs animaux. Elle ne possède pas nécessairement toutes les capacités d’un animal proche.

### 6.11 Trait distinctif

Caractéristique de silhouette ou de mouvement qui doit survivre aux LOD pour conserver la reconnaissance du pilote.

### 6.12 Budget de densité

Plafond combinant coût par animal, nombre visible, distance, animation et matériau dans une scène donnée.

## 7. Choisir les pilotes de Project Asteria

Un bon ensemble pilote couvre des problèmes différents sans chercher à représenter tout le règne animal. Le choix dépend des scènes réellement prévues, de la distance de caméra, du nombre simultané, du rôle narratif et du coût de production.

Les cinq pilotes documentaires ci-dessous sont des catégories de travail. Le nom d’espèce définitif, ses références et ses droits restent à renseigner lorsque la direction artistique les aura validés.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/ANIMAL-PILOTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
pilot_set_id: AST-ANIMAL-PILOTS-001
project: Project Asteria
pilots:
  - animal_id: AST-ANM-QUAD-001
    family: terrestrial_quadruped
    production_question: "Appuis alternés, colonne flexible et lecture à moyenne distance."
    expected_max_visible_near: 4
    group_representation_required: true
  - animal_id: AST-ANM-BIRD-001
    family: bird
    production_question: "Silhouette d'aile, pliage des plumes et transition sol-vol."
    expected_max_visible_near: 2
    group_representation_required: true
  - animal_id: AST-ANM-FISH-001
    family: fish
    production_question: "Ondulation, nageoire caudale et groupe aquatique."
    expected_max_visible_near: 8
    group_representation_required: true
  - animal_id: AST-ANM-REPT-001
    family: low_reptile
    production_question: "Corps bas, membres latéraux et contact ventral possible."
    expected_max_visible_near: 3
    group_representation_required: false
  - animal_id: AST-ANM-SERP-001
    family: serpentine
    production_question: "Déformation longue, courbure continue et absence de membres."
    expected_max_visible_near: 2
    group_representation_required: false
selection_status: under_review
runtime_status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `production_question` justifie chaque pilote par un problème concret plutôt que par une préférence visuelle.
- **Budgets :** `expected_max_visible_near` est une hypothèse de scène, pas une mesure de performance.
- **Décision :** `group_representation_required` signale qu’un animal proche ne suffira pas aux besoins de densité.
- **Réserve :** les identités d’espèce et les références restent à qualifier avant toute modélisation.


## 8. Constituer les références anatomiques et locomotrices

Chaque référence doit répondre à une question précise : position d’une articulation, volume en appui, amplitude d’une nageoire, ordre des contacts, pliage d’une aile, écrasement d’un coussinet ou variation saisonnière. Une image spectaculaire sans question de production crée du bruit.

Le jeu de références sépare :

- vues latérales, frontales, dorsales et ventrales ;
- squelette et masses superficielles ;
- repos, appui, propulsion et récupération ;
- sujets adultes, jeunes ou saisonniers seulement si le projet les prévoit ;
- photographie, vidéo, schéma et scan ;
- sources internes autorisées, sources publiques et sources sous licence ;
- contenu observé et interprétation artistique.
> **[VSC] Visual Studio Code — Créer : `art/references/animals/ANIMAL-REFERENCE-SET.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
reference_set_id: AST-ANIMAL-REF-001
animal_id: AST-ANM-QUAD-001
questions:
  - question_id: Q-MASS-001
    text: "Comment la cage thoracique se déplace-t-elle au-dessus des appuis ?"
  - question_id: Q-CONTACT-001
    text: "Quelles zones de l'extrémité touchent réellement le sol ?"
  - question_id: Q-GAIT-001
    text: "Quel ordre de contact est observé pour le cycle retenu ?"
sources:
  - source_id: REF-QUAD-001
    kind: motion_video
    view: lateral
    frame_rate_known: true
    allowed_use: internal_reference
    provenance_status: qualified
    answers:
      - Q-GAIT-001
  - source_id: REF-QUAD-002
    kind: anatomy_diagram
    view: lateral
    allowed_use: internal_reference
    provenance_status: under_review
    answers:
      - Q-MASS-001
      - Q-CONTACT-001
exclusions:
  - "Aucune image copiée directement dans une texture de livraison."
  - "Aucune séquence supposée universelle sans vérifier le pilote choisi."
review:
  anatomy: pending
  art_direction: pending
  provenance: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Traçabilité :** `answers` relie une source à une question et évite l’accumulation non structurée.
- **Mouvement :** `frame_rate_known` indique si le temps observé peut réellement servir à mesurer un cycle.
- **Droits :** `allowed_use` et `provenance_status` empêchent de transformer une référence interne en contenu redistribuable.
- **Limite :** une référence unique ne suffit pas à conclure sur toutes les poses ou tous les individus.


## 9. Lire l’anatomie comme un système de masses

La modélisation commence par les masses qui pilotent la silhouette et le mouvement, non par les détails de surface. Pour chaque pilote, repérer :

- bloc thoracique ou volume principal ;
- bassin ou volume propulsif ;
- colonne et ligne d’action ;
- tête, cou et éventuels contrepoids ;
- ceintures des membres ou attaches de nageoires et d’ailes ;
- longueur utile des segments ;
- extrémités de contact ;
- volumes qui se compriment, glissent ou se tordent ;
- zones dont la silhouette doit rester stable.

Le centre de masse physique réel n’est pas déduit visuellement. Le chapitre utilise un **repère de masse artistique** pour vérifier la cohérence des poses, puis exige une validation spécifique si la physique du jeu dépend d’un calcul réel.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/ANIMAL-ANATOMY-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
animal_id: AST-ANM-QUAD-001
units: meters
body_axes:
  forward: "-Y"
  up: "+Z"
landmarks:
  shoulder_center: [0.0, -0.42, 0.78]
  pelvis_center: [0.0, 0.36, 0.69]
  head_base: [0.0, -0.78, 0.92]
  tail_base: [0.0, 0.61, 0.70]
visual_mass_reference:
  thorax_weight: 0.46
  pelvis_weight: 0.31
  head_neck_weight: 0.15
  appendages_weight: 0.08
  note: "Ratios artistiques normalisés, non biomécaniques."
contact_regions:
  - front_left
  - front_right
  - rear_left
  - rear_right
deformation_hotspots:
  - scapular_slide
  - elbow_fold
  - hip_extension
  - hock_flexion
review_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Coordonnées :** les repères utilisent la convention métrique et les axes du pipeline Blender du Livre III.
- **Ratios :** les poids normalisés aident à comparer les volumes, mais ne représentent pas une masse physique mesurée.
- **Déformation :** `deformation_hotspots` prépare les zones à tester lors du skinning.
- **Résultat attendu :** le profil peut être comparé aux maillages, au rig et aux scènes de test.


## 10. Profils par grande famille


### 10.1 Quadrupèdes terrestres

Un quadrupède ne doit pas être traité comme un humain posé à quatre pattes. La colonne porte une relation différente entre thorax et bassin, les omoplates peuvent contribuer visuellement au déplacement du membre antérieur, et les extrémités définissent le type d’appui. La topologie doit préserver le glissement apparent de l’épaule, la flexion du coude, l’extension de la hanche et la lecture du jarret ou de l’équivalent fonctionnel.

Le pilote précise s’il est plutôt plantigrade, digitigrade ou onguligrade uniquement lorsque cette distinction est utile au maillage et au contact. Le terme ne remplace jamais une étude de la forme réelle de l’extrémité.

### 10.2 Oiseaux

Pour un oiseau, séparer le volume du tronc, le cou, la tête, les membres postérieurs, le squelette fonctionnel de l’aile et les surfaces de plumes. La silhouette de l’aile ne correspond pas au seul squelette : les rémiges et couvertures modifient fortement la forme visible.

Le pliage, l’ouverture et la torsion de l’aile doivent être testés avec des plumes pilotes avant de multiplier la surface. Au sol, vérifier équilibre, hauteur du corps, flexion des doigts et volume des plumes repliées. En vol, documenter les phases du cycle choisi depuis des références mesurables sans prétendre qu’un seul battement convient à toutes les vitesses ou espèces.

### 10.3 Poissons

Le corps d’un poisson est lu par sa section, sa flexibilité longitudinale, la position des nageoires et le rôle visuel de la nageoire caudale. La déformation peut être distribuée sur une chaîne d’os, une courbe de contrôle ou une combinaison ; le profil de rig doit indiquer la méthode.

Le maillage conserve la continuité de la silhouette latérale et dorsale. Les nageoires fines peuvent employer géométrie, cartes ou matériaux transparents selon la distance, mais leurs racines et leur amplitude doivent rester compatibles avec l’animation. Un banc de poissons ne justifie pas automatiquement `MultiMesh` : la représentation distante doit être conçue séparément si chaque individu proche exige un squelette.

### 10.4 Reptiles bas

Pour un reptile bas, observer l’orientation des membres, le rôle du ventre, la torsion de la colonne et les changements de hauteur pendant le déplacement. Un maillage qui fonctionne en pose neutre peut s’interpénétrer dès que le corps se rapproche du sol.

Les écailles ne doivent pas masquer une mauvaise structure. Les grandes plaques qui modifient la silhouette peuvent être géométriques ; le détail secondaire peut être porté par normales et matériaux. La segmentation suit les besoins de déformation plutôt qu’un motif décoratif uniforme.

### 10.5 Morphologies serpentines

Une morphologie serpentine exige une courbure continue, une densité de segments contrôlée et une gestion explicite de la torsion. Trop peu d’os produit des angles visibles ; trop d’os augmente le coût, les risques de poids instables et la complexité d’animation.

Le profil distingue tête, cou fonctionnel éventuel, tronc déformable et extrémité caudale. Les collisions et la locomotion de gameplay restent hors du chapitre ; la scène artistique teste seulement la continuité de la courbe, la conservation du volume et la lisibilité des ondulations.

## 11. Définir l’échelle, les appuis et les contacts

La scène Blender contient un plan métrique, des repères de hauteur et des objets de contact. Chaque extrémité prévue reçoit un point ou une surface de référence. Le contact n’est pas seulement visuel : il sert à détecter glissement, pénétration, flottement et changement de longueur apparent.

Pour l’eau et l’air, le terme « contact » désigne une phase fonctionnelle documentée, par exemple poussée d’une nageoire ou phase descendante d’une aile. Ces phases ne sont pas des collisions physiques au sens du moteur.
> **[VSC] Visual Studio Code — Créer : `art/animation/manifests/ANIMAL-CONTACT-SCHEDULE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
animal_id: AST-ANM-QUAD-001
cycle_id: locomotion_walk_pilot_v001
duration_seconds: 1.2
sample_rate_fps: 30
root_policy: in_place
phases:
  - phase_id: P01
    start_frame: 0
    end_frame: 6
    contacts: [front_left, rear_right]
    reference_source: REF-QUAD-001
  - phase_id: P02
    start_frame: 7
    end_frame: 14
    contacts: [front_left, rear_left, rear_right]
    reference_source: REF-QUAD-001
  - phase_id: P03
    start_frame: 15
    end_frame: 21
    contacts: [front_right, rear_left]
    reference_source: REF-QUAD-001
  - phase_id: P04
    start_frame: 22
    end_frame: 29
    contacts: [front_right, rear_left, rear_right]
    reference_source: REF-QUAD-001
loop_check:
  first_last_pose_delta_status: not_measured
  root_drift_status: not_measured
  contact_slide_status: not_measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exemple local :** l’ordre de contact appartient uniquement au cycle pilote référencé ; il n’est pas présenté comme une règle universelle.
- **Temps :** `sample_rate_fps` et les bornes de frames rendent le planning mesurable.
- **Racine :** `root_policy` indique si le déplacement est intégré à l’animation ou laissé au système externe.
- **Réserves :** les trois statuts `not_measured` empêchent de déclarer le cycle validé avant exécution.


## 12. Construire la base maillée

La base maillée suit un ordre stable :

1. volumes principaux à faible densité ;
2. ligne d’action et sections transversales ;
3. attaches des membres ou appendices ;
4. extrémités et surfaces de contact ;
5. topologie de déformation ;
6. asymétries nécessaires ;
7. détails de silhouette ;
8. préparation des surfaces secondaires.

Les boucles sont concentrées là où la forme se plie, se tord ou change de section. Les zones quasi rigides restent plus simples. La symétrie sert à construire ; elle peut être rompue après validation du contrat commun.
> **[LECTURE] Convention de collections Blender — Ne pas saisir.**

```text
ANM_AST_QUAD_001
├── 00_REFERENCE
├── 10_BLOCKOUT
├── 20_SCULPT
├── 30_RETPO
├── 40_RIG_TEST
├── 50_SURFACE_SOURCE
├── 60_LOD_SOURCE
├── 70_VALIDATION
└── __EXPORT
    ├── MESH
    ├── ARMATURE
    └── MARKERS
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** les sources de sculpture, de surface et de LOD restent hors de la collection d’export.
- **Export :** `__EXPORT` contient uniquement les objets attendus dans le GLB pilote.
- **Validation :** les marqueurs de contact peuvent être exportés seulement s’ils sont explicitement consommés par la scène de test.
- **Reprise :** la structure permet de retrouver le niveau canonique sans confondre source et dérivé.


## 13. Topologie de déformation

Les zones prioritaires varient selon la famille, mais le contrôle suit les mêmes questions :

- la section conserve-t-elle son volume pendant la flexion ;
- les boucles accompagnent-elles la direction du pli ;
- une torsion se distribue-t-elle sur plusieurs segments ;
- la surface de contact reste-t-elle stable au bon moment ;
- les appendices fins gardent-ils une racine propre ;
- les plumes, cartes ou écailles géométriques suivent-elles le support sans collision majeure ;
- le LOD simplifié conserve-t-il les mêmes points de contrôle essentiels.

Les poids automatiques sont un point de départ, jamais une validation. Blender peut nécessiter une correction manuelle des groupes de sommets lorsque le résultat ne correspond pas au mouvement attendu.
> **[LECTURE] Grille de poses de déformation — Ne pas saisir.**

```yaml
schema_version: 1
animal_id: AST-ANM-QUAD-001
pose_tests:
  - pose_id: neutral_reference
    required: true
  - pose_id: shoulder_max_forward
    required: true
  - pose_id: shoulder_max_back
    required: true
  - pose_id: elbow_deep_flex
    required: true
  - pose_id: hip_max_extension
    required: true
  - pose_id: hock_deep_flex
    required: true
  - pose_id: spine_lateral_bend
    required: true
  - pose_id: spine_vertical_bend
    required: true
  - pose_id: tail_base_max_bend
    required: true
acceptance:
  volume_loss: not_measured
  self_intersection: not_measured
  contact_shape: not_measured
  silhouette_break: not_measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** la grille teste les zones qui changent le plus la silhouette et les appuis.
- **Acceptation :** chaque critère reste à mesurer sur le pilote réel.
- **Usage :** les captures comparatives doivent conserver caméra, focale et éclairage.
- **Frontière :** cette grille prépare le chapitre de rig sans livrer le rig final.


## 14. Définir le profil de rig

Le profil de rig est indépendant du maillage et de la bibliothèque d’animations. Il décrit les os nécessaires au pilote, leur hiérarchie, leur rôle, la pose de repos, les orientations et les éléments optionnels.

Une armature animale ne doit pas être rendue compatible avec `SkeletonProfileHumanoid` par simple renommage. Ce profil Godot est conçu pour un squelette humanoïde. Les animaux utilisent leurs propres contrats et leurs propres scènes de validation ; un retargeting entre deux animaux n’est accepté que si la correspondance des chaînes, des poses et des amplitudes est documentée.
> **[VSC] Visual Studio Code — Créer : `art/rig/profiles/ANIMAL-RIG-PROFILE.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "rig_profile_id": "AST-RIG-QUAD-001-v001",
  "animal_id": "AST-ANM-QUAD-001",
  "rest_pose": "quadruped_neutral_v001",
  "root_bone": "root",
  "required_chains": {
    "spine": ["pelvis", "spine_01", "spine_02", "chest", "neck_01", "head"],
    "front_left": ["scapula.L", "upper_front.L", "lower_front.L", "paw_front.L"],
    "front_right": ["scapula.R", "upper_front.R", "lower_front.R", "paw_front.R"],
    "rear_left": ["thigh.L", "shin.L", "hock.L", "paw_rear.L"],
    "rear_right": ["thigh.R", "shin.R", "hock.R", "paw_rear.R"],
    "tail": ["tail_01", "tail_02", "tail_03", "tail_04"]
  },
  "optional_chains": {
    "ears": ["ear.L", "ear.R"],
    "jaw": ["jaw"]
  },
  "orientation_convention": {
    "primary_axis": "bone_local_y",
    "roll_policy": "mirrored_pairs_reviewed"
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

- **Hiérarchie :** les chaînes requises décrivent les responsabilités sans imposer les contrôleurs de production.
- **Pose de repos :** son identifiant doit correspondre aux exports et cycles compatibles.
- **Influences :** quatre est une cible de production, huit une exception à comparer et mesurer ; aucune valeur n’est déclarée validée ici.
- **Frontière :** les contrôleurs IK, contraintes, déformations correctives et outils d’animation restent au chapitre 19.


## 15. Valider les poids et les influences

La peinture de poids suit une procédure reproductible :

1. créer les groupes correspondant aux os déformants ;
2. générer une première répartition ;
3. normaliser les influences ;
4. retirer les influences lointaines sans effet utile ;
5. exécuter la grille de poses ;
6. corriger les zones de volume ;
7. comparer le budget quatre influences et l’exception huit influences ;
8. vérifier le LOD avec le même profil ;
9. documenter les différences.

Les os de contrôle qui ne déforment pas le maillage sont exclus de l’export si le pipeline le permet. Les os de plumes, moustaches, oreilles ou nageoires restent optionnels et doivent justifier leur coût.
> **[SORTIE] Blender — Rapport d’influences attendu — Ne pas saisir.**

```json
{
  "animal_id": "AST-ANM-QUAD-001",
  "mesh_id": "AST-MESH-QUAD-001-LOD0",
  "vertex_count": null,
  "vertices_over_4_influences": null,
  "vertices_over_8_influences": null,
  "zero_weight_vertices": null,
  "non_normalized_vertices": null,
  "deforming_bone_count": null,
  "measured_in_blender": false,
  "measured_after_import": false,
  "decision": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs nulles :** le rapport est un modèle et ne simule pas une mesure absente.
- **Double contrôle :** Blender et Godot sont distingués pour détecter une différence d’export ou d’import.
- **Décision :** `pending` reste bloquant pour un asset destiné à la production.
- **Budget :** le nombre d’os déformants est mesuré séparément du nombre total d’os de contrôle.


## 16. Préparer les cycles de locomotion

Le chapitre prépare des cycles pilotes, pas une bibliothèque finale. Chaque cycle possède :

- un identifiant stable ;
- une source de référence ;
- une durée et une fréquence d’échantillonnage ;
- une politique de racine ;
- des phases de contact ou de poussée ;
- des amplitudes principales ;
- des transitions nécessaires ;
- des critères de boucle ;
- un statut de validation.

Les noms `walk`, `run`, `fly` ou `swim` ne suffisent pas. Deux animaux d’une même famille peuvent nécessiter des rythmes, amplitudes et contacts différents.
> **[VSC] Visual Studio Code — Créer : `art/animation/manifests/ANIMAL-LOCOMOTION-LIBRARY.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "animal_id": "AST-ANM-BIRD-001",
  "rig_profile_id": "AST-RIG-BIRD-001-v001",
  "clips": [
    {
      "clip_id": "bird_idle_ground_v001",
      "kind": "idle",
      "loop": true,
      "root_policy": "in_place",
      "status": "planned"
    },
    {
      "clip_id": "bird_walk_ground_v001",
      "kind": "ground_locomotion",
      "loop": true,
      "root_policy": "in_place",
      "contact_schedule": "BIRD-WALK-CONTACT-v001",
      "status": "planned"
    },
    {
      "clip_id": "bird_takeoff_v001",
      "kind": "transition",
      "loop": false,
      "root_policy": "authored_motion",
      "status": "planned"
    },
    {
      "clip_id": "bird_flight_cycle_v001",
      "kind": "flight",
      "loop": true,
      "root_policy": "in_place",
      "phase_schedule": "BIRD-FLIGHT-PHASES-v001",
      "status": "planned"
    },
    {
      "clip_id": "bird_landing_v001",
      "kind": "transition",
      "loop": false,
      "root_policy": "authored_motion",
      "status": "planned"
    }
  ],
  "runtime_status": "not_executed"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transitions :** décollage et atterrissage sont séparés des boucles afin d’éviter une transition implicite impossible à tester.
- **Racine :** les clips en place et les mouvements auteurs sont identifiés explicitement.
- **Références :** les calendriers de contact ou de phases sont des dépendances versionnées.
- **Statut :** `planned` interdit de considérer la bibliothèque comme produite.


## 17. Quadrupèdes : marche, course et variations

Pour un quadrupède, construire d’abord un cycle lent lisible, puis une locomotion plus rapide seulement si le projet en a besoin. La validation observe :

- ordre et durée des contacts ;
- transfert du thorax et du bassin ;
- rotation et flexion de la colonne ;
- mouvement de la tête et de la queue ;
- compression des extrémités ;
- absence de glissement ;
- continuité entre première et dernière image ;
- compatibilité avec la vitesse attendue.

Les termes trot, galop ou amble ne sont utilisés qu’après qualification du cycle réel. Le chapitre recommande d’enregistrer le calendrier observé plutôt que de choisir un nom puis de forcer l’animation à lui correspondre.

## 18. Oiseaux : sol, battement et plané

Le pilote oiseau sépare au minimum :

- pose au sol ;
- marche ou saut au sol si prévu ;
- préparation du décollage ;
- décollage ;
- battement cyclique ;
- plané ou maintien d’aile si prévu ;
- approche ;
- atterrissage ;
- repliage des ailes.

Les plumes majeures doivent conserver leur ordre, leur chevauchement et leur silhouette pendant le pliage. Une aile correcte en extension peut devenir inutilisable une fois repliée si les cartes ou géométries se traversent. Les phases du battement sont enregistrées depuis une référence du pilote choisi, sans généralisation automatique.

## 19. Poissons : ondulation et nageoires

Le cycle poisson documente :

- portion du corps qui initie l’ondulation ;
- propagation vers la queue ;
- amplitude longitudinale ;
- rôle des nageoires paires et impaires ;
- rotation du corps ;
- accélération ou virage si prévu ;
- continuité de la boucle ;
- interaction visuelle avec le banc.

Une chaîne d’os trop courte crée des cassures. Une chaîne trop longue augmente le coût et rend la correction plus difficile. Le nombre final doit être déterminé par une comparaison de silhouette, de déformation et de coût, non par une convention arbitraire.

## 20. Reptiles et serpents : proximité du sol

Pour un reptile bas, la scène de validation ajoute un plan de sol et plusieurs hauteurs. Elle recherche les pénétrations du ventre, des membres et de la queue, ainsi que les changements brusques de volume lors des torsions.

Pour une forme serpentine, tester des courbes en S, des courbures verticales, des torsions et des changements de rayon. La locomotion de gameplay, les collisions et la résolution du chemin ne sont pas générées par l’animation artistique ; le Livre II reste propriétaire de ces décisions runtime.

## 21. Construire le pelage

Les courbes de cheveux Blender constituent une source utile pour guider et générer du pelage. Les nœuds de génération et d’interpolation reposent notamment sur une surface et une carte UV compatibles. Cette source ne doit pas être confondue avec la représentation livrée dans Godot.

Le pipeline distingue :

- guides de pelage dans la source Blender ;
- densité et masques de régions ;
- longueur, orientation, touffes et variation ;
- conversion éventuelle en cartes ou géométrie ;
- représentation proche ;
- représentation moyenne ;
- matériau ou silhouette distante ;
- budget de transparence et d’overdraw ;
- test d’export réel.

Un GLB n’est pas supposé transporter automatiquement un système de courbes de pelage exploitable tel quel. La représentation de livraison doit être testée et documentée.
> **[VSC] Visual Studio Code — Créer : `art/surfaces/ANIMAL-FUR-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
surface_profile_id: AST-FUR-QUAD-001-v001
animal_id: AST-ANM-QUAD-001
source:
  method: blender_hair_curves
  surface_uv: UV_FUR_ROOT
  guides_status: planned
regions:
  - region_id: body_short
    density_mask: MASK_FUR_BODY
    length_m: 0.018
  - region_id: neck_long
    density_mask: MASK_FUR_NECK
    length_m: 0.045
delivery_profiles:
  close:
    representation: cards_or_mesh_pending_test
  medium:
    representation: reduced_cards_pending_test
  far:
    representation: material_only
export_status: not_tested
godot_status: not_tested
overdraw_budget_status: not_measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** les courbes restent un outil de fabrication et ne préjugent pas du format livré.
- **Régions :** les masques évitent une densité uniforme sans logique anatomique.
- **LOD de surface :** les trois représentations sont séparées pour mesurer silhouette et transparence.
- **Réserves :** export, import et overdraw restent explicitement non testés.


## 22. Construire les plumes

Les plumes sont organisées par groupes fonctionnels et visuels. Les grandes plumes qui modifient l’aile ou la queue peuvent être des objets ou cartes identifiables ; les petites couvertures peuvent être regroupées ou transférées dans le matériau selon la distance.

Le rig de plumes ne doit pas créer un os par élément sans budget. Une solution courante consiste à animer des groupes pilotes et à faire suivre les éléments secondaires, mais la méthode exacte appartient au rig de production. Le chapitre exige seulement une matrice de groupes, de dépendances et de LOD.
> **[VSC] Visual Studio Code — Créer : `art/surfaces/ANIMAL-FEATHER-GROUPS.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "animal_id": "AST-ANM-BIRD-001",
  "groups": [
    {
      "group_id": "primary_flight",
      "silhouette_critical": true,
      "near_representation": "individual_cards_or_meshes",
      "mid_representation": "merged_clusters",
      "far_representation": "baked_wing_surface"
    },
    {
      "group_id": "secondary_flight",
      "silhouette_critical": true,
      "near_representation": "clustered_cards",
      "mid_representation": "merged_clusters",
      "far_representation": "baked_wing_surface"
    },
    {
      "group_id": "body_coverts",
      "silhouette_critical": false,
      "near_representation": "cards_and_material",
      "mid_representation": "material",
      "far_representation": "material"
    }
  ],
  "fold_test_status": "not_executed",
  "export_status": "not_tested"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Criticité :** `silhouette_critical` protège les plumes qui définissent l’aile aux LOD suivants.
- **Réduction :** la représentation change par groupe au lieu de supprimer toutes les plumes à la même distance.
- **Test :** le repliage est une porte distincte de l’extension.
- **Limite :** la structure ne prescrit pas le rig final ni la technique de simulation.


## 23. Écailles, peau et surfaces lisses

Les écailles suivent trois niveaux :

- plaques ou crêtes qui changent la silhouette : géométrie proche, parfois conservée au LOD intermédiaire ;
- relief secondaire : normales, hauteur ou détail de matériau ;
- microstructure : texture et réponse lumineuse.

Le motif d’écaille doit suivre la déformation et éviter les changements de taille arbitraires aux articulations. Les UV, normales tangentes et compression sont testés dans Godot. Pour une peau lisse ou humide, la crédibilité dépend davantage des normales, de la rugosité, de l’épaisseur apparente et de l’éclairage que d’une multiplication de polygones.

## 24. Variantes pertinentes

Une variante est produite seulement lorsqu’elle sert une scène, une lecture ou un système prévu. Les axes possibles incluent :

- âge ou stade de développement ;
- dimorphisme si pertinent et sourcé ;
- saison ;
- biome ;
- état de santé visuel autorisé ;
- coloration régionale ;
- longueur de pelage ou plumage ;
- taille ou corpulence ;
- usure ou cicatrice narrative.

Les variantes ne déduisent pas automatiquement comportement, dangerosité ou rôle. Elles partagent un contrat de rig et de LOD seulement après test.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/ANIMAL-VARIANTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
animal_id: AST-ANM-QUAD-001
base_variant: adult_standard
variants:
  - variant_id: adult_winter
    changed_domains:
      - fur_length
      - fur_density
      - color_palette
    rig_compatibility: expected_not_tested
    lod_compatibility: expected_not_tested
  - variant_id: juvenile
    changed_domains:
      - proportions
      - body_volume
      - gait_timing
    rig_compatibility: separate_review_required
    lod_compatibility: separate_review_required
forbidden_inferences:
  - "La couleur ne détermine pas le comportement."
  - "La taille ne détermine pas automatiquement les statistiques de gameplay."
  - "Une variante saisonnière n'est pas une nouvelle espèce."
runtime_status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaines :** les changements sont listés afin de révéler leurs dépendances.
- **Compatibilité :** une variation de surface peut être attendue compatible, tandis qu’une variation de proportions impose une revue.
- **Séparation :** les inférences de gameplay sont interdites dans le contrat visuel.
- **Réserve :** aucune variante n’est déclarée produite ou exécutée.


## 25. Définir les budgets et les LOD

Les budgets sont définis par contexte de vue et densité. Un animal proche avec pelage, animation et matériaux transparents n’a pas le même coût qu’une silhouette distante dans un groupe.

Godot peut générer des LOD de maillage à l’import et utiliser des plages de visibilité. Ces outils ne garantissent pas la qualité d’une déformation animale. Les LOD manuels restent nécessaires lorsque la silhouette, les os, les cartes de plumes, les nageoires ou les contacts exigent un contrôle artistique.

Les distances ne sont jamais copiées d’un autre projet. Elles sont mesurées avec la caméra, la résolution, le champ de vision et la taille du pilote de `Project Asteria`.
> **[VSC] Visual Studio Code — Créer : `art/budgets/ANIMAL-LOD-PROFILE.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "animal_id": "AST-ANM-QUAD-001",
  "camera_profile": "ASTERIA_GAMEPLAY_CAMERA_v001",
  "lods": [
    {
      "lod": 0,
      "intended_use": "close_hero",
      "triangle_budget": 65000,
      "deforming_bone_budget": 96,
      "material_slots_budget": 4,
      "surface_representation": "full_close"
    },
    {
      "lod": 1,
      "intended_use": "near_gameplay",
      "triangle_budget": 36000,
      "deforming_bone_budget": 72,
      "material_slots_budget": 3,
      "surface_representation": "reduced_close"
    },
    {
      "lod": 2,
      "intended_use": "mid_distance",
      "triangle_budget": 16000,
      "deforming_bone_budget": 48,
      "material_slots_budget": 2,
      "surface_representation": "material_dominant"
    },
    {
      "lod": 3,
      "intended_use": "far_individual",
      "triangle_budget": 5000,
      "deforming_bone_budget": 24,
      "material_slots_budget": 1,
      "surface_representation": "silhouette_only"
    },
    {
      "lod": 4,
      "intended_use": "group_representation",
      "triangle_budget": 800,
      "deforming_bone_budget": 0,
      "material_slots_budget": 1,
      "surface_representation": "static_or_shader_driven_pending_test"
    }
  ],
  "distance_thresholds_m": null,
  "measured_performance": null,
  "status": "provisional"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Budgets provisoires :** les nombres sont des plafonds de conception à remplacer ou confirmer par mesure.
- **Os :** le LOD de groupe prévoit zéro os seulement parce qu’il s’agit d’une représentation distincte, pas d’un maillage skinné tronqué.
- **Distances :** la valeur reste `null` avant test caméra.
- **Surface :** chaque LOD réduit aussi le coût de pelage, de plumes ou de matériaux, pas seulement les triangles.


## 26. Représentations de groupe et instancing

`MultiMesh` permet de dessiner de nombreuses instances d’un même maillage avec peu d’appels de dessin. Il traite cependant l’ensemble comme un seul objet spatial et ignore les blend shapes. Il n’est donc pas présenté comme la solution par défaut aux animaux proches skinnés et animés.

Le pipeline distingue :

- **proche** : scène animale complète, squelette, animation et matériaux validés ;
- **intermédiaire** : LOD skinné simplifié ou scène réduite ;
- **distant individuel** : animation ou représentation simplifiée à tester ;
- **groupe lointain** : maillage statique, imposteur ou animation pilotée par shader, seulement après preuve de compatibilité.

Les groupes éloignés sont découpés spatialement pour éviter un `MultiMesh` couvrant une zone immense dont toutes les instances seraient rendues ensemble. Le `custom_aabb` et les limites de lumière sont vérifiés dans la scène réelle.
> **[VSC] Visual Studio Code — Créer : `tests/art/animals/GROUP-REPRESENTATION-MATRIX.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
animal_id: AST-ANM-FISH-001
profiles:
  - profile_id: near_individual
    node_type: Node3D_scene
    skeleton: required
    animation: required
    max_instances_test: 8
  - profile_id: mid_individual
    node_type: Node3D_scene
    skeleton: reduced
    animation: required
    max_instances_test: 24
  - profile_id: far_school
    node_type: MultiMeshInstance3D_candidate
    skeleton: forbidden
    animation: shader_or_static_pending_test
    spatial_chunk_size_m: 20
    max_instances_test: 256
checks:
  aabb_culling: not_measured
  lighting_limit: not_measured
  blend_shape_dependency_absent: not_verified
  draw_calls: not_measured
  frame_time: not_measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** le groupe lointain est un candidat distinct, non un remplacement silencieux du poisson skinné.
- **Découpage :** `spatial_chunk_size_m` prépare plusieurs groupes spatialement bornés.
- **Contraintes :** le squelette est interdit dans le profil `far_school` afin d’éviter une promesse incompatible avec le contrat retenu.
- **Mesures :** culling, éclairage, draw calls et temps de frame restent à tester.


## 27. Préparer l’export GLB

L’export suit les conventions du chapitre 4 :

- unités métriques ;
- orientation vérifiée ;
- collection `__EXPORT` ;
- noms stables ;
- transformations relues ;
- maillage, armature et animations sélectionnés explicitement ;
- matériaux et textures qualifiés ;
- objets de source exclus ;
- manifeste écrit avant export ;
- empreinte calculée après export.

Les courbes de pelage, les systèmes procéduraux et les objets de construction ne sont pas supposés survivre à l’export. Leur représentation de livraison doit être convertie ou remplacée, puis contrôlée dans Godot.
> **[VSC] Visual Studio Code — Créer : `art/exports/animals/AST-ANM-QUAD-001.export.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "asset_id": "AST-ANM-QUAD-001",
  "source_blend": "art/blender/animals/AST-ANM-QUAD-001_v001.blend",
  "export_glb": "art/exports/animals/AST-ANM-QUAD-001_v001.glb",
  "export_collection": "__EXPORT",
  "rig_profile_id": "AST-RIG-QUAD-001-v001",
  "lods_included": [0, 1, 2, 3],
  "animations_included": [
    "locomotion_walk_pilot_v001",
    "idle_pilot_v001"
  ],
  "surface_delivery": "cards_and_material_pending_test",
  "expected_nodes": [
    "AnimalRoot",
    "Skeleton3D",
    "Body_LOD0"
  ],
  "source_sha256": null,
  "export_sha256": null,
  "export_status": "not_executed"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la source, l’export, le rig et les clips sont reliés par identifiants.
- **Surface :** la représentation de livraison est visible et reste à tester.
- **Intégrité :** les empreintes sont calculées sur les fichiers réels, jamais préremplies.
- **Statut :** `not_executed` interdit de confondre manifeste et export existant.


## 28. Importer et structurer la scène Godot

L’import Godot est contrôlé dans une scène dérivée, pas en modifiant directement la scène importée. Le chapitre vérifie :

- hiérarchie attendue ;
- présence du `Skeleton3D` pour les profils skinnés ;
- animations et boucles ;
- matériaux et transparence ;
- normales et tangentes ;
- LOD et plages de visibilité ;
- échelle et orientation ;
- AABB ;
- ombres ;
- empreinte du GLB ;
- réimport sans perte de configuration.

`AnimationTree` sert à tester les transitions et mélanges, tandis que `AnimationPlayer` reste la source des clips importés. Le chapitre n’implémente pas le contrôleur de locomotion de gameplay.
> **[LECTURE] Arbre de scène de validation Godot — Ne pas saisir.**

```text
AnimalValidationLab (Node3D)
├── LightingRig (Node3D)
├── GroundReference (MeshInstance3D)
├── ScaleGrid (Node3D)
├── CameraNear (Camera3D)
├── CameraGameplay (Camera3D)
├── CameraFar (Camera3D)
├── AnimalNear (Node3D)
│   ├── ImportedAnimal (instance)
│   ├── AnimationTree
│   ├── ContactMarkers (Node3D)
│   └── DebugLabels (Node3D)
├── AnimalLodLine (Node3D)
│   ├── LOD0
│   ├── LOD1
│   ├── LOD2
│   └── LOD3
├── GroupRepresentation (Node3D)
│   ├── NearIndividuals
│   └── FarCandidate
└── ValidationController (Node)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Caméras :** trois profils séparent inspection rapprochée, vue de jeu et lecture lointaine.
- **Ligne LOD :** les niveaux sont visibles simultanément pour comparer silhouette et matériaux.
- **Groupe :** les scènes proches et la représentation distante sont testées côte à côte.
- **Contrôleur :** il orchestre les tests sans devenir un système de gameplay.


## 29. Écrire le validateur structurel Godot

> **[VSC] Visual Studio Code — Créer : `tests/art/animals/animal_asset_validator.gd` — Ne pas saisir.**

```gdscript
extends Node
class_name AnimalAssetValidator

enum ValidationCode {
    OK,
    MISSING_ROOT,
    MISSING_SKELETON,
    MISSING_ANIMATION_PLAYER,
    MISSING_REQUIRED_CLIP,
    INVALID_SCALE,
    INVALID_AABB,
    FORBIDDEN_MULTIMESH_SKELETON_PROFILE,
}

@export var asset_root_path: NodePath
@export var expected_scale_m: float = 1.0
@export var scale_tolerance: float = 0.02
@export var skeleton_required: bool = true
@export var required_clips: Array[StringName] = []

func validate_asset() -> Dictionary:
    var result := {
        "code": ValidationCode.OK,
        "messages": PackedStringArray(),
        "measured": {}
    }

    var asset_root := get_node_or_null(asset_root_path)
    if asset_root == null:
        result.code = ValidationCode.MISSING_ROOT
        result.messages.append("Racine d'asset introuvable.")
        return result

    var skeleton := _find_first_skeleton(asset_root)
    if skeleton_required and skeleton == null:
        result.code = ValidationCode.MISSING_SKELETON
        result.messages.append("Skeleton3D requis mais absent.")

    var player := _find_first_animation_player(asset_root)
    if player == null:
        result.code = _keep_first_error(
            result.code,
            ValidationCode.MISSING_ANIMATION_PLAYER
        )
        result.messages.append("AnimationPlayer introuvable.")
    else:
        _validate_clips(player, result)

    var bounds := _collect_visual_bounds(asset_root)
    result.measured["aabb_size"] = bounds.size
    if bounds.size.length_squared() <= 0.0:
        result.code = _keep_first_error(
            result.code,
            ValidationCode.INVALID_AABB
        )
        result.messages.append("AABB visuelle vide.")

    var height := bounds.size.y
    result.measured["height_m"] = height
    if absf(height - expected_scale_m) > scale_tolerance:
        result.code = _keep_first_error(
            result.code,
            ValidationCode.INVALID_SCALE
        )
        result.messages.append(
            "Hauteur mesurée hors tolérance : %.3f m." % height
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

func _find_first_animation_player(root: Node) -> AnimationPlayer:
    if root is AnimationPlayer:
        return root as AnimationPlayer
    for child in root.get_children():
        var found := _find_first_animation_player(child)
        if found != null:
            return found
    return null

func _validate_clips(
    player: AnimationPlayer,
    result: Dictionary
) -> void:
    var available := player.get_animation_list()
    for clip_id in required_clips:
        if not available.has(clip_id):
            result.code = _keep_first_error(
                result.code,
                ValidationCode.MISSING_REQUIRED_CLIP
            )
            result.messages.append(
                "Clip requis absent : %s." % clip_id
            )

func _collect_visual_bounds(root: Node) -> AABB:
    var combined := AABB()
    var initialized := false
    for node in root.find_children("*", "VisualInstance3D", true, false):
        var visual := node as VisualInstance3D
        var local_bounds := visual.get_aabb()
        var world_bounds := visual.global_transform * local_bounds
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

- **Entrées :** `asset_root_path`, l’échelle attendue, la tolérance, l’exigence de squelette et les clips requis sont configurables par scène.
- **Retour :** `validate_asset()` renvoie un dictionnaire détaché avec code, messages et mesures ; il ne modifie pas l’asset.
- **Parcours :** les fonctions récursives recherchent le premier squelette et le premier lecteur d’animations sans supposer une profondeur fixe.
- **AABB :** les volumes des `VisualInstance3D` sont transformés puis fusionnés ; le résultat doit être confirmé dans le projet réel.
- **Erreur :** `_keep_first_error()` conserve le premier code bloquant tout en collectant les messages suivants.
- **Limite :** le script ne valide ni la qualité anatomique, ni les contacts, ni les performances GPU.


## 30. Mesurer les contacts et le glissement

La scène place des marqueurs sous les appuis et enregistre, pour chaque phase :

- position du marqueur ;
- vitesse relative au sol ;
- distance au plan ;
- pénétration ;
- temps de contact ;
- déplacement de la racine ;
- différence entre première et dernière image.

Un seuil n’est choisi qu’après observation de l’échelle et de la caméra. Les valeurs sont conservées dans un rapport par clip et par LOD. Un cycle peut être artistiquement convaincant tout en échouant sur le glissement mesuré ; les deux décisions restent distinctes.
> **[VSC] Visual Studio Code — Créer : `tests/art/animals/CONTACT-MEASUREMENT.json` — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "animal_id": "AST-ANM-QUAD-001",
  "clip_id": "locomotion_walk_pilot_v001",
  "lod": 0,
  "sample_rate_fps": 30,
  "measurements": {
    "max_contact_slide_m": null,
    "max_ground_penetration_m": null,
    "max_ground_gap_m": null,
    "loop_root_delta_m": null,
    "loop_pose_delta": null
  },
  "thresholds": {
    "contact_slide_m": null,
    "ground_penetration_m": null,
    "ground_gap_m": null
  },
  "runtime_status": "not_executed",
  "decision": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mesures :** toutes les valeurs restent nulles avant exécution.
- **Seuils :** ils sont séparés des résultats afin de documenter leur origine.
- **Granularité :** le rapport est associé à un animal, un clip et un LOD précis.
- **Décision :** un rapport incomplet ne peut pas devenir `accepted`.


## 31. Mesurer le coût

La campagne de performance fixe :

- build de référence ;
- résolution ;
- champ de vision ;
- caméra et trajectoire ;
- nombre d’animaux proches ;
- nombre d’animaux intermédiaires ;
- nombre de représentations distantes ;
- éclairage ;
- ombres ;
- matériaux ;
- animation active ;
- durée d’échantillonnage ;
- compteurs CPU, GPU, mémoire et appels de dessin.

Les résultats sont comparés à une scène témoin sans animaux. Une moyenne seule est insuffisante : conserver au minimum médiane, percentile élevé, maximum observé et contexte de capture lorsque les outils disponibles le permettent.
> **[VSC] Visual Studio Code — Créer : `tests/art/animals/ANIMAL-PERFORMANCE-PLAN.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
test_id: AST-ANIMAL-PERF-001
hardware_profile: AMD_RX6750XT_R7_2700_32GB
engine: Godot_4_7_1_ForwardPlus
resolution: [1920, 1080]
camera_profile: ASTERIA_GAMEPLAY_CAMERA_v001
scenarios:
  - scenario_id: baseline_empty
    near_animals: 0
    mid_animals: 0
    far_instances: 0
  - scenario_id: gameplay_small_group
    near_animals: 4
    mid_animals: 12
    far_instances: 64
  - scenario_id: distant_school
    near_animals: 0
    mid_animals: 8
    far_instances: 256
metrics:
  cpu_frame_ms: not_measured
  gpu_frame_ms: not_measured
  draw_calls: not_measured
  video_memory_mb: not_measured
  system_memory_mb: not_measured
  visible_triangles: not_measured
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Témoin :** `baseline_empty` fournit une référence avant ajout des animaux.
- **Scénarios :** proximité et densité sont variées séparément.
- **Matériel :** le profil de référence rend les résultats comparables.
- **Réserve :** aucun compteur n’est prérempli et la décision reste en attente.


## 32. Provenance, licences et données sensibles

Chaque pilote animal relie :

- références visuelles et vidéos ;
- auteur, fournisseur ou institution ;
- licence ou autorisation ;
- restrictions de redistribution ;
- modèle ou scan source éventuel ;
- textures et photographies ;
- outils de génération ;
- sons ou captures utilisés uniquement comme référence ;
- transformations réalisées ;
- exports produits.

Les scans d’animaux, photogrammétries, bibliothèques de mouvements et modèles achetés ne sont pas supposés redistribuables. Les fichiers de preuve restent hors du dépôt public lorsque leur contrat ou leurs données l’exigent.

Une espèce protégée, un lieu sensible ou des données de suivi réelles peuvent créer des risques de conservation ou de localisation. Le chapitre n’inclut aucune donnée précise de terrain sans revue dédiée.
> **[VSC] Visual Studio Code — Créer : `art/provenance/ANIMAL-ASSET-RECORD.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: AST-ANM-QUAD-001
asset_kind: animal_pilot
sources:
  references:
    - reference_set_id: AST-ANIMAL-REF-001
  purchased_models: []
  scans: []
  motion_libraries: []
  generated_inputs: []
rights:
  production_use: under_review
  redistribution: forbidden_until_review
  attribution_required: unknown
sensitive_data:
  real_world_location_included: false
  protected_species_data_included: false
transformations:
  - "Anatomical study."
  - "Original modeling."
  - "Original topology."
delivery:
  source_blend: planned
  export_glb: planned
  manifests: planned
decision: blocked_until_rights_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources vides :** les tableaux vides sont explicites et ne masquent pas une origine inconnue.
- **Droits :** redistribution reste bloquée tant que la revue n’est pas terminée.
- **Sensibilité :** les données de localisation et d’espèces protégées possèdent des indicateurs séparés.
- **Décision :** la porte juridique est indépendante de la qualité artistique.


## 33. Parcours Mode Solo

En Mode Solo :

1. choisir un seul pilote prioritaire ;
2. limiter la bibliothèque à repos, cycle principal et une transition ;
3. utiliser une surface proche et une surface distante simples ;
4. produire trois LOD avant d’en ajouter davantage ;
5. mesurer une petite scène et une scène de groupe ;
6. conserver les manifestes essentiels ;
7. bloquer les variantes sans besoin de jeu ;
8. réutiliser le même laboratoire Godot pour tous les pilotes.

L’objectif est de prouver une chaîne complète avant d’élargir la diversité.

## 34. Parcours Mode Studio

En Mode Studio :

- attribuer un propriétaire par famille ;
- versionner fiches anatomiques et profils de rig ;
- faire relire les contacts par animation et les surfaces par lookdev ;
- maintenir une matrice de compatibilité entre rig, clips, LOD et variantes ;
- séparer sources de pelage, conversion et représentation moteur ;
- conserver les campagnes de mesure par build ;
- organiser une revue croisée art, rig, animation, intégration et performance ;
- documenter les exceptions et leur date de retrait ;
- automatiser seulement les contrôles structurels et mesurables ;
- réserver la décision artistique à une revue humaine.

## 35. Porte d’acceptation

> **[LECTURE] Checklist d’acceptation d’un pilote animal — Ne pas saisir.**

```yaml
identity_and_rights:
  stable_asset_id: false
  reference_set_qualified: false
  rights_review_complete: false
anatomy:
  family_profile_complete: false
  masses_and_landmarks_reviewed: false
  contact_regions_documented: false
geometry:
  topology_pose_tests_passed: false
  silhouette_review_passed: false
  modular_boundaries_reviewed: false
rig_and_motion:
  rig_profile_versioned: false
  influence_report_complete: false
  required_cycles_present: false
  contact_measurements_passed: false
surfaces:
  delivery_representation_tested: false
  lod_surface_profiles_tested: false
godot:
  glb_imported: false
  structural_validator_passed: false
  lod_transitions_reviewed: false
  group_representation_measured: false
performance:
  reference_scenarios_measured: false
  budget_decision_recorded: false
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portes séparées :** droits, anatomie, géométrie, rig, surfaces, Godot et performance peuvent bloquer indépendamment.
- **État initial :** toutes les valeurs sont fausses tant que les preuves réelles n’existent pas.
- **Décision :** `blocked` est la valeur sûre d’un template non exécuté.
- **Usage :** le passage à `accepted` exige un rapport conservé, pas une impression orale.


## 36. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 36.1 Utiliser un squelette humain pour tous les animaux

**Symptôme :** le maillage suit quelques poses simples, mais les chaînes de membres se plient comme celles d’un bipède.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
rig_profile: humanoid
animal_family: quadruped
compatibility: assumed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le profil humanoïde ne décrit ni la colonne portée horizontalement, ni les chaînes de membres et d’extrémités du pilote.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
rig_profile: AST-RIG-QUAD-001-v001
animal_family: terrestrial_quadruped
compatibility: tested_per_chain
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil animal nomme les chaînes réelles et exige une compatibilité testée.


### 36.2 Nommer un cycle sans documenter les contacts

**Symptôme :** la boucle semble dynamique, mais les appuis glissent ou changent d’ordre sans justification.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
clip_id: animal_run
contacts: unknown
source: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le nom `run` ne prouve ni l’ordre des appuis, ni le rythme, ni la source.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
clip_id: quadruped_fast_cycle_v001
contact_schedule: QUAD-FAST-CONTACT-v001
source: REF-QUAD-MOTION-003
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction lie le clip à un calendrier et à une référence.


### 36.3 Exporter directement les courbes de pelage comme livrable

**Symptôme :** le pelage est correct dans Blender, puis disparaît ou devient inexploitable après export.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
surface_source: blender_hair_curves
delivery: same_as_source
export_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une source procédurale Blender n’est pas automatiquement une représentation Godot compatible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
surface_source: blender_hair_curves
delivery: cards_or_mesh_pending_test
export_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare fabrication et livraison puis rend le test obligatoire.


### 36.4 Employer MultiMesh pour des animaux proches skinnés

**Symptôme :** un groupe proche coûte peu en appels de dessin, mais perd squelette, clips et variations individuelles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
profile: near_animals
node: MultiMeshInstance3D
skeleton: required
individual_animation: required
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `MultiMesh` ne fournit pas le contrat d’une scène skinnée individuelle et traite les instances comme un seul objet de rendu.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
profile: near_animals
node: instanced_animal_scene
skeleton: required
individual_animation: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Une scène instanciée conserve squelette, animation et validation propres.


### 36.5 Réduire seulement les triangles aux LOD

**Symptôme :** le nombre de triangles baisse, tandis que le coût des matériaux, os et transparences reste presque identique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod2:
  triangles: 12000
  fur: full
  materials: 5
  bones: 96
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le coût des surfaces, matériaux et os peut rester dominant même après décimation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod2:
  triangles: 12000
  fur: material_dominant
  materials: 2
  bones: 48
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction réduit plusieurs dimensions du budget et impose une revue.


### 36.6 Déduire un comportement depuis une variante visuelle

**Symptôme :** une différence de couleur ou de taille modifie silencieusement des données de comportement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
variant: dark_fur
aggression_bonus: 25
social_role: predator
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La couleur visuelle ne constitue pas une preuve de comportement ou de statistiques.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
variant: dark_fur
changed_domains: [color_palette]
gameplay_inference: forbidden
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite la variante à son domaine artistique.


### 36.7 Utiliser un seul angle pour valider la silhouette

**Symptôme :** le profil latéral est convaincant, mais les vues frontales ou de jeu révèlent une silhouette incohérente.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
silhouette_review:
  camera: side
  result: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un profil latéral peut masquer largeur, asymétrie, appendices et collisions.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
silhouette_review:
  cameras: [side, front, rear, three_quarter, gameplay]
  result: pending_until_all_reviewed
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction impose plusieurs vues, dont la caméra de jeu.


### 36.8 Valider un contact à l’œil sans mesure

**Symptôme :** les pieds paraissent posés sur une capture, mais la lecture image par image révèle glissement et pénétration.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
contact_slide: looks_ok
ground_penetration: not_checked
decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une impression visuelle ne quantifie ni glissement ni pénétration et ne peut être rejouée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
contact_slide_m: null
ground_penetration_m: null
runtime_status: not_executed
decision: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve les mesures absentes et bloque la décision.


### 36.9 Fusionner la représentation de groupe avec le LOD proche

**Symptôme :** le même fichier est utilisé à toutes les distances, avec des besoins incompatibles entre proximité et densité.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
animal_asset:
  source: one_mesh
  near: same
  far_group: same
  animation: same
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un même asset ne satisfait pas automatiquement squelette proche, LOD et densité lointaine.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
animal_asset:
  near_scene: AST-ANM-FISH-001-near.tscn
  mid_scene: AST-ANM-FISH-001-mid.tscn
  far_group_candidate: AST-ANM-FISH-001-school.tscn
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction crée des livrables distincts avec des tests propres.


### 36.10 Déclarer le pilote terminé sans Godot

**Symptôme :** l’asset est déclaré terminé après la revue Blender alors que l’export et l’import n’ont jamais été exécutés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La conformité Blender ne prouve ni import, ni matériaux, ni LOD, ni coût dans le moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction maintient le blocage jusqu’aux preuves d’intégration.


## 37. Livrables à conserver

Le chapitre définit cinq livrables permanents, conformément au plan maître :

1. **bases animales pilotes** — sources Blender et exports lorsque matérialisés ;
2. **fiches anatomiques** — références, masses, repères, appuis et questions ;
3. **profils de rig de base** — hiérarchies, poses de repos, influences et réserves ;
4. **cycles de locomotion pilotes** — manifestes, calendriers de contacts et rapports de boucle ;
5. **budgets par distance et densité** — LOD, surfaces, os, matériaux, groupes et mesures.

La scène Godot `AnimalValidationLab` constitue l’environnement commun de preuve. Elle est conservée avec les rapports, sans devenir un sixième asset de jeu ni une logique de simulation.
> **[LECTURE] Arborescence finale attendue — Ne pas saisir.**

```text
art/
├── blender/animals/
├── references/animals/
├── rig/profiles/
├── animation/manifests/
├── surfaces/
├── budgets/
├── exports/animals/
├── provenance/
└── manifests/
tests/
└── art/animals/
    ├── animal_validation_lab.tscn
    ├── animal_asset_validator.gd
    ├── reports/
    └── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les fichiers Blender et références restent séparés des exports.
- **Contrats :** rig, animation, surfaces et budgets disposent de dossiers dédiés.
- **Tests :** scènes, scripts, rapports et captures sont regroupés sous `tests/art/animals`.
- **Publication :** les preuves internes ne sont pas ajoutées automatiquement au manuel lecteur.


## 38. Synthèse opérationnelle pour Project Asteria

Le chapitre 8 fournit à `Project Asteria` un plan reproductible pour produire plusieurs familles animales sans les réduire à un rig humain ou à une simple variation de maillage. La chaîne commence par des questions sourcées, décrit masses et appuis, construit maillage et profil de rig, prépare des cycles pilotes, choisit une représentation de surface, puis mesure LOD et densité dans Godot.

La décision de production reste bloquée tant que les cinq pilotes, leurs exports, leurs scènes et leurs mesures ne sont pas matérialisés. Le chapitre ne revendique donc aucun animal terminé ; il fournit les contrats qui permettront aux chapitres 10, 19, 20 et 21 de travailler sans reconstruire l’anatomie, les identités ou les budgets.

## 39. Références techniques officielles

Les références suivantes ont été consultées pour qualifier les fonctions citées :

- [Blender Manual — Armatures et structure des os](https://docs.blender.org/manual/en/5.0/animation/armatures/structure.html) ;
- [Blender Manual — Armature Deform Parent et poids](https://docs.blender.org/manual/fr/4.0/animation/armatures/skinning/parenting.html) ;
- [Blender Manual — Hair Nodes](https://docs.blender.org/manual/en/dev/modeling/geometry_nodes/hair/index.html) ;
- [Blender Manual — Generate Hair Curves](https://docs.blender.org/manual/en/4.2/modeling/geometry_nodes/hair/generation/generate_hair_curves.html) ;
- [Blender Manual — Interpolate Hair Curves](https://docs.blender.org/manual/en/dev/modeling/geometry_nodes/hair/generation/interpolate_hair_curves.html) ;
- [Godot 4.7 — Skeleton3D](https://docs.godotengine.org/en/4.7/classes/class_skeleton3d.html) ;
- [Godot 4.7 — AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html) ;
- [Godot 4.7 — MeshInstance3D](https://docs.godotengine.org/en/4.7/classes/class_meshinstance3d.html) ;
- [Godot 4.7 — MultiMesh](https://docs.godotengine.org/en/4.7/classes/class_multimesh.html) ;
- [Godot — Mesh level of detail](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html) ;
- [Godot — Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html) ;
- [Godot 4.7 — Import process](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html) ;
- [Godot 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html).

Les pages `latest` ou `dev` sont utilisées seulement lorsqu’aucune page versionnée équivalente n’est exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d’appliquer la procédure.
