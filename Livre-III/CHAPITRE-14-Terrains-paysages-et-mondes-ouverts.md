---
title: "Livre III — Chapitre 14 : Terrains, paysages et mondes ouverts"
id: "DOC-L3-CH14"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 14
last-verified: "2026-07-23T16:43:43+02:00"
audit-status: "complete"
audit-date: "2026-07-23T16:43:43+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-14.md"
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

# Terrains, paysages et mondes ouverts

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH14`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Le chapitre 13 a établi les règles des bâtiments et kits modulaires. Le présent chapitre change encore d’échelle : il organise le support territorial qui relie ces bâtiments, porte les routes, reçoit les rivières, découpe l’espace en cellules chargeables et maintient une continuité visuelle lorsque la caméra traverse plusieurs zones.

Le fil rouge utilise la région pilote `AST-WORLD-REGION-DELTA-001` de `Project Asteria`. Elle comprend une vallée encaissée, un plateau habitable, une route principale, un cours d’eau, une rive lacustre et trois interfaces vers les bâtiments du chapitre 13. Cette région n’est pas un monde ouvert final : elle sert à éprouver les contrats de métrique, de tuile, de voisinage, de collision, de navigation, de chargement et de mesure avant toute extension.

Un terrain n’est pas seulement un maillage sculpté. Il associe au minimum une source d’altitude, une représentation de rendu, une collision, des limites de navigation, des raccords architecturaux, des couches matérielles, des données de voisinage, des profils de distance et des scènes de cellule. La beauté d’une vue statique ne suffit donc pas à valider le système.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Brief de région et parcours attendus
    ↓
Échelle du monde et stratégie de coordonnées
    ↓
Découpage région → secteur → cellule → tuile
    ↓
Heightmap, relief macro et corridors de circulation
    ↓
Rivières, lacs, littoraux et raccords aux bâtiments
    ↓
Bordures de tuiles, matériaux et continuité visuelle
    ↓
Collision, navigation et représentation distante
    ↓
Scènes de cellule et manifeste de voisinage
    ↓
Préchargement, activation, retrait et mémoire
    ↓
Benchmarks de traversée, ruptures et temps de chargement
    ↓
Porte d'acceptation de la région pilote
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** la région part de la bible visuelle, des conventions Blender, des matériaux préparatoires et du kit architectural.

- **Ordre :** l’échelle, les coordonnées et le découpage sont fixés avant le sculpt détaillé.

- **Preuve :** la région doit être traversée dans Godot avec des cellules réellement chargées et retirées.

- **Frontière :** le système écologique dynamique et les populations appartiennent au Livre II.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- transformer un besoin de monde en région pilote mesurable ;
- distinguer région, secteur, cellule, tuile, sous-tuile, voisin et interface ;
- décider si les coordonnées standards suffisent avant d’envisager les grandes coordonnées ;
- définir une origine, une orientation et des identifiants spatiaux stables ;
- préparer une heightmap sans confondre image de travail et collision finale ;
- séparer relief macro, formes intermédiaires et détail de surface ;
- contrôler l’érosion au lieu de l’utiliser comme générateur arbitraire ;
- raccorder des tuiles sans fissures ni normales divergentes ;
- concevoir routes, rivières, lacs, littoraux et plateformes de bâtiments ;
- préparer des matériaux de terrain sans refaire le pipeline PBR du chapitre 16 ;
- séparer rendu, collision, navigation, eau et données de streaming ;
- organiser des scènes de cellules chargeables indépendamment ;
- utiliser le chargement en arrière-plan sans bloquer le thread principal ;
- définir voisinage, préchargement, hystérésis, épinglage et éviction ;
- préparer LOD, HLOD et horizons sans inventer de distances ;
- écrire un contrôleur de streaming pédagogique, typé et non autoritaire ;
- mesurer temps de chargement, mémoire, ruptures et continuité de parcours ;
- conserver toutes les réserves lorsque Blender, Godot ou le runtime n’ont pas été exécutés.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les contrats YAML et JSON, procédures Blender, hiérarchies Godot, profils de collision et navigation, exemples de chargement et scripts GDScript ont été relus contre les documentations officielles. Ils ne constituent pas une preuve d’exécution.

Aucun terrain pilote, aucune heightmap, aucune tuile, aucun maillage, aucune route, aucune rivière, aucun lac, aucun matériau, aucune collision, aucun navmesh, aucune scène de cellule, aucun LOD, aucun HLOD, aucun GLB, aucune mesure de mémoire et aucun temps de chargement de `Project Asteria` ne sont revendiqués comme produits. Les dimensions, résolutions, distances, rayons, budgets et seuils présentés comme exemples restent des candidats à confirmer.

Godot ne fournit pas ici un éditeur de terrain propriétaire supposé. Le chapitre décrit un contrat de données et une architecture de cellules compatibles avec des maillages importés, des heightmaps de collision et des scènes dérivées. Tout plugin futur doit être qualifié séparément selon sa licence, sa version, sa maintenance et ses effets sur le format des sources.

> **[LECTURE] Échelle de preuve du chapitre — Ne pas saisir.**

```yaml
evidence:
  level: static-review
  blender_execution: not_executed
  godot_execution: not_executed
  runtime_traversal: not_executed
  heightmap_import: not_executed
  collision_validation: not_executed
  navigation_validation: not_executed
  streaming_validation: not_executed
  memory_measurement: not_executed
  load_time_measurement: not_executed
  pdf: not_built
decision:
  documentation: reviewed
  production_assets: blocked
  runtime_claims: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les valeurs sont des chaînes de statut explicites et non des booléens ambigus.

- **Réserve :** `not_executed` interdit de transformer une procédure relue en résultat mesuré.

- **Décision :** le texte peut être accepté tandis que les assets et preuves runtime restent bloqués.

- **PDF :** la compilation du Livre III reste différée à la fin du livre.

## 4. Périmètre et frontières

Le chapitre couvre :

- brief territorial, parcours, repères et horizons ;
- échelle, origine, précision et stratégie de coordonnées ;
- découpage spatial et identifiants de cellules ;
- sources de hauteur, sculpt, érosion et bordures ;
- routes, rivières, lacs, littoraux et plateformes de bâtiments ;
- matériaux de terrain et masques comme contrats locaux ;
- collision, navigation, eau et raccords de cellules ;
- scènes de cellules, manifestes de voisinage et chargement en arrière-plan ;
- préchargement, activation, retrait, hystérésis et épinglage ;
- LOD, HLOD, horizons, visibilité et occlusion limitée ;
- benchmarks de traversée, mémoire, chargement et ruptures.

Le chapitre ne couvre pas :

- la modélisation des bâtiments du chapitre 13 ;
- les espèces, distributions, saisons et densités végétales du chapitre 15 ;
- le pipeline PBR transversal du chapitre 16 ;
- les UV, retopologies et bakings génériques du chapitre 17 ;
- les VFX météorologiques ou de destruction du chapitre 23 ;
- l’intégration globale et les importeurs du chapitre 28 ;
- la simulation écologique, les populations et la régénération du Livre II ;
- la logique de quête, de propriété ou de construction runtime.

> **[LECTURE] Matrice des responsabilités — Ne pas saisir.**

```yaml
chapter_14:
  owns:
    - world_scale_and_coordinate_contract
    - region_sector_cell_tile_partition
    - terrain_height_and_border_contract
    - road_river_lake_coast_interfaces
    - terrain_render_collision_navigation_profiles
    - cell_scene_and_streaming_manifest
    - terrain_lod_hlod_and_benchmark_protocols
  prepares:
    - chapter_15_vegetation_placement_surfaces
    - chapter_16_terrain_material_pipeline
    - chapter_17_height_and_mask_baking
    - chapter_28_world_import_integration
  does_not_own:
    - architectural_module_library
    - ecological_simulation
    - vegetation_species_catalog
    - general_pbr_rules
    - authoritative_gameplay_state
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriété :** `owns` énumère les décisions que le chapitre doit fermer.

- **Préparation :** `prepares` fournit des interfaces sans anticiper les chapitres futurs.

- **Exclusion :** `does_not_own` empêche le terrain visuel de devenir une seconde autorité écologique ou gameplay.

- **Contrôle :** toute section doit se rattacher à une responsabilité explicite.

## 5. Prérequis et outils à ouvrir

Prérequis documentaires :

- cahier des charges artistique et bible visuelle ;
- kit architectural du chapitre 13, même s’il reste non matérialisé ;
- gabarits de personnages et caméra de référence ;
- liste des parcours nécessaires au vertical slice ;
- profil provisoire de plateforme et de mémoire ;
- conventions Blender et GLB du chapitre 4 ;
- registre de provenance du chapitre 5 ;
- politique de collision, navigation et sauvegarde du projet.

Outils :

- **[APP] Blender 5.2.0** pour blockout, sculpt, maillages, corridors, rives et exports ;
- **[APP] Godot 4.7.1-stable** pour cellules, collisions, navigation, visibilité, chargement et mesures ;
- **[VSC] Visual Studio Code** pour manifestes, profils et scripts ;
- **[PS] PowerShell 7** pour créer l’arborescence et lancer les validateurs ;
- **[WEB] navigateur** pour les documentations officielles et les sources qualifiées.

> **[PS] Créer l’arborescence de travail.**

```powershell
$Root = "art/world/AST-WORLD-REGION-DELTA-001"
$Paths = @(
    "$Root/briefs",
    "$Root/coordinates",
    "$Root/height",
    "$Root/tiles",
    "$Root/roads",
    "$Root/water",
    "$Root/materials",
    "$Root/collisions",
    "$Root/navigation",
    "$Root/streaming",
    "$Root/lod",
    "art/blender/world/AST-WORLD-REGION-DELTA-001",
    "art/exports/world/AST-WORLD-REGION-DELTA-001",
    "tests/art/world/reports",
    "tests/art/world/captures"
)
foreach ($Path in $Paths) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** `$Root` est une chaîne et `$Paths` un tableau de chemins relatifs.

- **Boucle :** `foreach` traite chaque chemin indépendamment.

- **Paramètres :** `-ItemType Directory` crée un dossier et `-Force` rend l’opération répétable.

- **Effet :** l’arborescence est créée ; aucun terrain ni export n’est produit.

## 6. Vocabulaire minimal

- **Région :** ensemble territorial cohérent possédant un brief, des limites et un manifeste.
- **Secteur :** regroupement de cellules utilisé pour l’organisation et la production.
- **Cellule :** unité chargeable ou activable côté moteur.
- **Tuile :** morceau de terrain partageant une grille de bordure avec ses voisins.
- **Sous-tuile :** subdivision de production qui n’est pas nécessairement chargeable.
- **Voisin :** cellule partageant une interface spatiale déclarée.
- **Heightmap :** grille de valeurs décrivant une hauteur unique par position horizontale.
- **Corridor :** bande réservée à une route, une rivière ou une transition.
- **Pad architectural :** surface et interface préparées pour recevoir un bâtiment.
- **Streaming :** chargement, activation et retrait progressifs de ressources selon un contrat.
- **Préchargement :** demande anticipée avant que la cellule soit nécessaire.
- **Épinglage :** interdiction temporaire de retirer une cellule encore requise.
- **Hystérésis :** différence entre seuil d’entrée et seuil de sortie afin d’éviter les bascules répétées.
- **LOD :** représentation moins détaillée d’un même élément.
- **HLOD :** représentation agrégée remplaçant un groupe d’éléments.

> **[LECTURE] Relations entre les unités spatiales — Ne pas saisir.**

```text
AST-WORLD-REGION-DELTA-001
├── sector_north
│   ├── cell_N00_E00
│   │   ├── terrain_tile
│   │   ├── collision_profile
│   │   ├── navigation_region
│   │   └── stream_manifest
│   └── cell_N00_E01
└── sector_south
    ├── cell_S01_E00
    └── cell_S01_E01
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hiérarchie :** une région contient des secteurs, lesquels regroupent des cellules.

- **Cellule :** l’unité moteur rassemble rendu, collision, navigation et manifeste sans fusionner leurs responsabilités.

- **Identité :** les coordonnées logiques font partie du nom mais ne remplacent pas l’identifiant stable.

- **Évolution :** une sous-tuile peut changer sans renommer la région entière.

## 7. Région pilote et parcours de preuve

La région pilote est une zone limitée mais complète. Elle doit montrer plusieurs difficultés dans un même parcours :

1. départ sur le plateau de la Maison-relais ;
2. descente par une route en lacets ;
3. franchissement d’un pont au-dessus du cours d’eau ;
4. passage près d’une rive lacustre ;
5. remontée vers une tour basse ;
6. traversée d’au moins deux frontières de cellule ;
7. retour par un chemin secondaire permettant de comparer la répétition.

Les bâtiments servent de repères et de contraintes de raccord. Ils ne sont pas recréés ici. Le terrain fournit seulement leurs plateformes, pentes d’approche, niveaux d’eau voisins, accès de navigation et zones de visibilité.

> **[LECTURE] Brief fonctionnel de la région pilote — Ne pas saisir.**

```yaml
region_id: AST-WORLD-REGION-DELTA-001
purpose: vertical_slice_world_pipeline
required_landmarks:
  - waystation_pad
  - river_bridge_interface
  - lakeside_viewpoint
  - low_watchtower_pad
required_routes:
  - main_traversal_loop
  - alternate_footpath
required_boundaries:
  - at_least_two_cell_crossings
proof_state:
  blender_blockout: not_executed
  godot_traversal: not_executed
  streaming: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **But :** le brief teste le pipeline plutôt qu’une quantité maximale de kilomètres.

- **Repères :** les landmarks imposent des raccords architecture-terrain observables.

- **Parcours :** deux routes réduisent le risque d’un terrain optimisé pour un seul angle.

- **Statut :** la région reste bloquée jusqu’aux essais Blender et Godot.

## 8. Partir des usages et des lignes de vue

Le relief doit soutenir les actions prévues. Avant de sculpter, on dessine les zones de déplacement, les vues nécessaires, les zones cachées, les entrées de bâtiments et les obstacles. Un sommet spectaculaire qui masque le repère principal ou une vallée qui rend le retour impossible est un échec fonctionnel.

Chaque intention est formulée comme une relation observable : « la Maison-relais reste visible pendant la première minute de descente », « le lac apparaît après le franchissement du col », « la tour sert de repère au retour ». Les durées et distances exactes restent provisoires tant que la vitesse du personnage et la caméra ne sont pas mesurées.

> **[LECTURE] Carte d’usages avant sculpt — Ne pas saisir.**

```yaml
usage_map: AST-WORLD-USAGE-001-v001
areas:
  start_plateau:
    supports: [spawn, orientation, architecture_pad]
  main_valley:
    supports: [road, river, long_view]
  lakeside:
    supports: [shoreline, viewpoint, alternate_path]
  return_ridge:
    supports: [watchtower_landmark, route_choice]
constraints:
  traversal_time: pending_measurement
  sightline_review: pending
  camera_occlusion_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Zones :** chaque aire possède une fonction de parcours.

- **Contraintes :** aucune durée n’est présentée comme validée.

- **Lignes de vue :** elles deviennent des objets de revue et non des impressions.

- **Résultat :** le sculpt doit répondre à cette carte avant d’ajouter du détail.

## 9. Choisir l’échelle et la stratégie de coordonnées

L’échelle mondiale repose sur les mêmes mètres que les personnages et les bâtiments. Une unité Godot correspond au mètre du contrat `Project Asteria`. Les distances de parcours sont déduites des usages, pas d’une envie abstraite de grandeur.

Godot 4.7 documente les grandes coordonnées pour les mondes réellement gigantesques, mais précise qu’elles ont un coût en mémoire et en performance et qu’elles sont souvent inutiles pour un monde à pied de taille modérée centré autour de l’origine. Le projet doit donc mesurer les besoins de précision avant d’activer une compilation en double précision. Le chapitre retient par défaut les coordonnées standards et un découpage centré, avec une porte de décision explicite.

> **[LECTURE] Porte de décision des coordonnées — Ne pas saisir.**

```yaml
coordinate_policy: AST-WORLD-COORD-001-v001
unit_m: 1.0
world_origin_role: region_reference_center
default_precision: standard
large_world_coordinates:
  enabled: false
  required_evidence:
    - measured_precision_artifact
    - platform_memory_review
    - physics_review
    - rendering_review
origin_shifting:
  status: out_of_scope_for_pilot
decision: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** le mètre conserve la compatibilité avec personnages et architecture.

- **Défaut :** la précision standard reste active tant qu’un problème n’est pas mesuré.

- **Porte :** les grandes coordonnées demandent des preuves de précision et de coût.

- **Limite :** le déplacement d’origine n’est pas ajouté comme complexité préventive.

## 10. Définir un repère spatial stable

Le repère associe un axe vertical, une orientation cartographique, une origine et une convention de coordonnées de cellule. Les noms `N`, `S`, `E` et `W` n’ont de sens que si l’orientation est documentée. Une cellule ne doit pas changer d’identité parce qu’un artiste a recentré un maillage dans Blender.

La position locale d’une tuile et sa coordonnée logique sont deux informations distinctes. La première sert aux transforms ; la seconde sert aux manifestes, au voisinage et aux sauvegardes. Les conversions doivent être déterministes et centralisées.

> **[LECTURE] Contrat de repère — Ne pas saisir.**

```yaml
spatial_reference: AST-WORLD-REFERENCE-001-v001
up_axis: Y
horizontal_axes:
  east_west: X
  north_south: Z
origin:
  logical_cell: [0, 0]
  world_position_m: [0.0, 0.0, 0.0]
cell_coordinates:
  order: [east, north]
  integer_only: true
transform_authority: world_partition_service
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Axes :** `Y` porte l’altitude, `X` et `Z` les coordonnées horizontales.

- **Coordonnée logique :** elle reste entière et indépendante du nom de fichier.

- **Autorité :** une seule conversion évite les arrondis divergents.

- **Statut :** les conventions doivent être validées dans Blender et Godot.

## 11. Hiérarchie région, secteur, cellule et tuile

Le découpage doit répondre à plusieurs contraintes contradictoires : taille des fichiers, coût de chargement, opportunités de culling, continuité des bords, navigation, édition en équipe et nombre de nœuds. Une valeur unique ne convient pas à tous les projets.

La cellule est l’unité de streaming de référence. La tuile est l’unité de relief. Pour le pilote, elles peuvent coïncider afin de réduire la complexité, mais le contrat n’impose pas cette égalité à long terme. Un secteur sert à regrouper des cellules pour la production et les revues ; il n’est pas automatiquement chargé comme un bloc.

> **[LECTURE] Profil de partition provisoire — Ne pas saisir.**

```yaml
partition_profile: AST-WORLD-PARTITION-001-v001
region: AST-WORLD-REGION-DELTA-001
sector_role: production_group
cell_role: streaming_unit
terrain_tile_role: height_and_render_unit
pilot_relation:
  cells_per_tile: provisional
  tiles_per_cell: provisional
selection_basis:
  - measured_load_time
  - memory_peak
  - seam_count
  - navigation_boundaries
  - authoring_cost
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôles :** secteur, cellule et tuile ne sont pas synonymes.

- **Pilote :** la relation exacte reste à choisir après une comparaison.

- **Critères :** la décision dépend de mesures et de coût d’édition.

- **Statut :** aucun nombre de mètres ou de cellules n’est figé.

## 12. Identifiants et noms de cellules

Un identifiant stable survit au déplacement d’un fichier, à une traduction et à une réorganisation de secteur. Le nom humain peut évoluer ; l’identifiant logique et la coordonnée restent des données distinctes.

Les chemins dérivés sont construits depuis un manifeste. Ils ne doivent pas être concaténés dans plusieurs scripts avec des conventions différentes. Les coordonnées négatives utilisent un format sans ambiguïté.

> **[LECTURE] Exemple d’identité de cellule — Ne pas saisir.**

```yaml
cell:
  id: AST-WORLD-CELL-DELTA-0001
  region_id: AST-WORLD-REGION-DELTA-001
  sector_id: AST-WORLD-SECTOR-DELTA-NORTH-001
  coordinate:
    east: 0
    north: 1
  scene_path: res://world/delta/cells/cell_0001.tscn
  display_name: "Versant nord"
  revision: 1
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **ID :** `id` ne dépend ni de la coordonnée ni du nom affiché.

- **Coordonnée :** elle sert au voisinage et aux conversions spatiales.

- **Chemin :** il appartient au manifeste et peut être migré.

- **Révision :** toute modification de contrat est traçable.

## 13. Séparer sources, exports et données dérivées

La source Blender, la heightmap haute précision, les masques, les GLB, les scènes importées, les scènes dérivées, les collisions et les rapports ne doivent pas être confondus. Une image utilisée pour le sculpt n’est pas automatiquement la source de collision publiée. Une scène Godot dérivée ne doit pas être écrasée par un réimport.

Les caches, maillages de prévisualisation et miniatures sont reconstructibles. Les sources et manifestes sont versionnés ; les exports suivent la politique du dépôt ; les rapports de benchmark appartiennent aux preuves.

> **[LECTURE] Arborescence canonique — Ne pas saisir.**

```text
art/
├── blender/world/AST-WORLD-REGION-DELTA-001/
├── world/AST-WORLD-REGION-DELTA-001/
│   ├── briefs/
│   ├── coordinates/
│   ├── height/
│   ├── tiles/
│   ├── roads/
│   ├── water/
│   ├── materials/
│   ├── collisions/
│   ├── navigation/
│   ├── streaming/
│   └── lod/
└── exports/world/AST-WORLD-REGION-DELTA-001/
tests/art/world/
├── reports/
└── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les `.blend`, heightmaps maîtres et masques restent séparés des exports.

- **Dérivés :** GLB, scènes importées et caches sont reconstructibles selon la politique du projet.

- **Preuves :** rapports et captures ne sont pas rangés parmi les assets de production.

- **Réimport :** la scène dérivée conserve les nœuds moteur ajoutés manuellement.

## 14. Comprendre la heightmap

Une heightmap encode une hauteur unique pour chaque position horizontale de sa grille. Cette structure convient aux collines, vallées, plateaux et lits de rivière ouverts. Elle ne peut pas représenter seule une grotte, un pont, une arche ou un surplomb, car plusieurs surfaces verticales partageraient la même position horizontale.

La heightmap maître doit conserver assez de précision pour éviter les terrasses. La documentation Godot recommande des données de hauteur sur 16 ou 32 bits, par exemple EXR ou HDR, et avertit qu’une source 8 bits conduit à des paliers visibles. Cette recommandation concerne les données de hauteur, pas toutes les textures de terrain.

> **[LECTURE] Contrat de source d’altitude — Ne pas saisir.**

```yaml
height_source: AST-WORLD-HEIGHT-DELTA-001-v001
representation: single_height_per_horizontal_sample
master_format:
  candidate: EXR
  precision_bits: 32
  qualification: pending_import_test
derived_preview:
  format: PNG
  authority: false
unsupported_without_extra_meshes:
  - caves
  - bridges
  - arches
  - overhangs
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Représentation :** une seule hauteur exclut les volumes superposés.

- **Maître :** le format haute précision reste l’autorité candidate.

- **Aperçu :** un PNG peut servir à la revue mais ne devient pas la source autoritaire.

- **Compléments :** grottes et ponts exigent des maillages et collisions séparés.

## 15. Résolution, étendue et densité d’échantillonnage

La résolution d’une heightmap ne peut pas être choisie sans connaître l’étendue physique qu’elle représente. Le même nombre de pixels peut décrire une petite cour ou une vallée entière, avec une densité d’échantillonnage radicalement différente.

Le contrat enregistre séparément largeur de l’image, profondeur, étendue en mètres et pas horizontal. Ces valeurs doivent produire des bords compatibles entre tuiles. Une résolution plus élevée augmente le détail potentiel, mais aussi la mémoire, le temps de traitement, la taille des sources et le coût des collisions si elle est réutilisée sans simplification.

> **[LECTURE] Calcul documentaire du pas horizontal — Ne pas saisir.**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class HeightGrid:
    samples: int
    extent_m: float

    def spacing_m(self) -> float:
        if self.samples < 2:
            raise ValueError("At least two samples are required.")
        return self.extent_m / float(self.samples - 1)

grid = HeightGrid(samples=0, extent_m=0.0)  # valeurs à remplacer après décision
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** `HeightGrid` regroupe deux valeurs sans les rendre implicites.

- **Fonction :** `spacing_m()` retourne un flottant représentant la distance entre deux échantillons.

- **Contrôle :** deux échantillons au minimum sont nécessaires pour former un intervalle.

- **Réserve :** les zéros sont des placeholders bloquants, pas un profil de production.

## 16. Produire un blockout de relief dans Blender

Le blockout de relief doit rester léger. On commence par les grandes masses : bassin versant, plateau, crête, vallée, lac et corridors. Le détail fin est interdit tant que les parcours et raccords ne fonctionnent pas.

Une méthode possible consiste à utiliser un plan subdivisé, un modificateur de déplacement alimenté par une texture, puis un sculpt non destructif ou une copie de travail. Le modificateur Displace déplace les sommets selon l’intensité d’une texture ; la qualité dépend donc de la densité du maillage, de la précision de la texture et du sens de déplacement. La procédure doit enregistrer force, niveau médian, coordonnées et ordre des modificateurs.

> **[LECTURE] Fiche du blockout Blender — Ne pas saisir.**

```yaml
blender_blockout: AST-WORLD-BLOCKOUT-DELTA-001-v001
scene_units: metric
unit_scale: 1.0
source_height: AST-WORLD-HEIGHT-DELTA-001-v001
modifier_stack:
  - subdivision_candidate
  - displace_candidate
  - controlled_sculpt
displace:
  direction: Z
  strength_m: pending
  midlevel: pending
applied: false
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unités :** le mètre correspond au contrat du projet.

- **Pile :** l’ordre des modificateurs est enregistré pour permettre la reproduction.

- **Paramètres :** force et niveau médian restent à calibrer avec les altitudes attendues.

- **Application :** les modificateurs restent non appliqués tant que la réversibilité est utile.

## 17. Sculpter par niveaux de forme

Le relief se construit en trois niveaux :

- **macro** : vallée, plateau, bassin, crête et horizon ;
- **méso** : talus, terrasse, ravine, berge et replat ;
- **micro** : petites irrégularités qui ne doivent pas porter la silhouette principale.

Le microdétail géométrique est souvent un mauvais usage du budget s’il disparaît dans les matériaux ou les normales du chapitre 16. Le sculpt doit être inspecté depuis la caméra de jeu, en vue aérienne et sur une coupe de pente.

> **[LECTURE] Porte de progression du sculpt — Ne pas saisir.**

```yaml
terrain_sculpt_gate:
  macro:
    route_network_readable: pending
    major_silhouette_review: pending
    drainage_review: pending
  meso:
    slopes_walkable_where_required: pending
    building_pads_connected: pending
    river_banks_consistent: pending
  micro:
    allowed_after_macro_and_meso: true
    gameplay_authority: false
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** les niveaux macro et méso doivent passer avant le micro.

- **Drainage :** les grandes pentes sont revues avant les détails esthétiques.

- **Autorité :** le microdétail n’impose pas de règle gameplay.

- **Décision :** un seul échec conserve la porte bloquée.

## 18. Utiliser l’érosion comme outil contrôlé

L’érosion procédurale peut proposer des ravines et accumulations plausibles, mais elle ne connaît ni les parcours, ni les bâtiments, ni les contraintes de caméra. Elle doit être appliquée sur une branche ou une copie, avec paramètres, seed, masque et comparaison avant/après.

Une érosion qui détruit une plateforme, coupe une route ou inverse un drainage utile est rejetée. La plausibilité géologique ne remplace pas la fonction de jeu ; inversement, une fonction de jeu ne justifie pas une rivière montant une pente sans explication.

> **[LECTURE] Expérience d’érosion — Ne pas saisir.**

```yaml
erosion_experiment: AST-WORLD-EROSION-DELTA-001-v001
input_height: AST-WORLD-HEIGHT-DELTA-001-v001
seed: pending
parameters:
  iterations: pending
  rainfall: pending
  sediment: pending
mask:
  protect_building_pads: true
  protect_main_road: true
comparison:
  drainage: pending
  silhouettes: pending
  traversal: pending
promotion: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Traçabilité :** l’entrée, la seed et les paramètres permettent une comparaison.

- **Masque :** les interfaces critiques sont protégées au lieu d’être réparées après coup.

- **Revue :** drainage, silhouette et parcours sont évalués séparément.

- **Promotion :** la sortie n’écrase jamais directement la heightmap maître.

## 19. Partager exactement les bordures de tuiles

Deux tuiles voisines doivent partager la même rangée d’échantillons à leur interface, ou dériver cette rangée d’une source commune. Copier visuellement les bords n’est pas suffisant : une différence minime peut produire une fissure, une ombre ou une collision disjointe.

Le pipeline choisit une autorité de bordure. Une tuile ne lisse pas seule sa dernière rangée. Les normales de rendu, les collisions et les masques doivent être inspectés après l’assemblage, pas seulement dans les fichiers isolés.

> **[LECTURE] Contrat de bordure — Ne pas saisir.**

```yaml
border_contract: AST-WORLD-BORDER-001-v001
pair:
  cell_a: AST-WORLD-CELL-DELTA-0001
  edge_a: east
  cell_b: AST-WORLD-CELL-DELTA-0002
  edge_b: west
authority:
  shared_height_strip: pending
checks:
  sample_count_equal: pending
  height_values_equal: pending
  normal_continuity: pending
  collision_continuity: pending
  material_mask_continuity: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paire :** les deux bords sont nommés explicitement.

- **Autorité :** une bande partagée évite deux corrections indépendantes.

- **Contrôles :** rendu, collision et matériaux sont testés séparément.

- **Statut :** l’égalité visuelle seule ne peut pas fermer le contrat.

## 20. Prévoir des marges de travail sans créer de chevauchement runtime

Pour sculpter et calculer des normales, une tuile peut conserver une marge de contexte autour de sa zone publiée. Cette marge ne signifie pas que deux cellules doivent rendre deux surfaces complètes superposées. Le pipeline distingue domaine de calcul, domaine publié et bande de raccord.

Les vertices ou pixels de marge sont retirés ou ignorés selon une règle déterministe. La collision suit exactement le domaine publié afin d’éviter les doubles contacts.

> **[LECTURE] Domaine d’une tuile — Ne pas saisir.**

```yaml
tile_domain:
  authored_area:
    includes_context_margin: true
  published_area:
    includes_context_margin: false
  border_strip:
    source: shared_authority
runtime:
  render_overlap: forbidden
  collision_overlap: forbidden
  navigation_overlap_as_connection: forbidden
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Travail :** la marge aide le sculpt et les normales.

- **Publication :** la surface rendue n’inclut pas deux fois la même zone.

- **Physique :** la collision double est interdite.

- **Navigation :** un chevauchement ne prouve jamais une connexion.

## 21. Concevoir les routes comme des corridors

Une route est d’abord un corridor fonctionnel possédant une largeur, une pente, des accotements, des raccords et des zones de croisement. La texture de route vient ensuite. Le corridor modifie ou contraint le relief afin d’éviter les dévers incohérents et les marches invisibles.

Les intersections, lacets, ponts et entrées de bâtiments deviennent des interfaces nommées. Une courbe Blender peut servir de guide, mais la courbe, le maillage de rendu, la collision et les données de navigation restent des livrables différents.

> **[LECTURE] Profil d’un corridor routier — Ne pas saisir.**

```yaml
road_corridor: AST-WORLD-ROAD-MAIN-001-v001
centerline_source: blender_curve_pending
cross_section:
  carriageway_width_m: pending
  shoulder_width_m: pending
  crown_or_crossfall: pending
constraints:
  maximum_slope: pending_measurement
  minimum_turn_radius: pending_measurement
interfaces:
  - waystation_entry
  - bridge_deck
  - watchtower_access
render_mesh: not_produced
collision: not_produced
navigation: not_produced
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la ligne centrale guide le corridor sans devenir le livrable final.

- **Section :** largeur et dévers sont des paramètres mesurables.

- **Interfaces :** les raccords critiques sont nommés.

- **Séparation :** rendu, collision et navigation restent indépendants.

## 22. Raccorder routes et bâtiments

Le terrain reçoit les pads architecturaux définis par des profils d’interface. Le pad possède une altitude de référence, une emprise, une orientation, une zone de transition et des points d’accès. Le bâtiment ne doit pas être enfoncé arbitrairement pour masquer un terrain mal préparé.

La transition comprend le seuil, la pente d’approche, l’écoulement de l’eau, la collision et la navigation. Le terrain et le kit architectural partagent un contrat, mais chaque chapitre conserve son autorité.

> **[LECTURE] Interface terrain-bâtiment — Ne pas saisir.**

```yaml
terrain_architecture_interface: AST-WORLD-PAD-WAYSTATION-001-v001
building_contract: AST-ARCH-KIT-WAYSTATION-001
pad:
  footprint_m: pending
  reference_elevation_m: pending
  orientation_deg: pending
  transition_band_m: pending
access:
  road_connector: waystation_entry
  navigation_connector: pending
drainage:
  away_from_foundation: pending_review
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le contrat architectural est consommé sans être copié.

- **Pad :** emprise, altitude et orientation sont explicites.

- **Accès :** route et navigation possèdent des connecteurs distincts.

- **Drainage :** le raccord doit éviter d’envoyer l’eau vers la fondation.

## 23. Concevoir les rivières depuis le bassin versant

Une rivière doit suivre une logique de collecte et de pente. Le tracé part des hauteurs, des confluences, des zones d’érosion et de la destination de l’eau. Un simple ruban bleu posé sur le terrain produit rapidement des sections en montée, des berges impossibles et des collisions incohérentes.

Le lit, les berges, la surface d’eau et les zones de franchissement sont séparés. Le chapitre prépare ces formes ; les shaders détaillés et VFX de l’eau seront qualifiés selon leurs chapitres respectifs.

> **[LECTURE] Contrat hydrologique du cours d’eau — Ne pas saisir.**

```yaml
river_profile: AST-WORLD-RIVER-DELTA-001-v001
source_points: pending
outlet: lake_delta
centerline: pending
elevation_rule:
  non_increasing_downstream: required
cross_sections:
  count: pending
  bed_width_m: pending
  bank_height_m: pending
interfaces:
  - bridge_crossing
  - lakeside_outlet
flow_simulation:
  authority: none_in_chapter_14
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Altitude :** la règle interdit une remontée non justifiée du cours d’eau.

- **Sections :** le lit et les berges sont décrits par plusieurs coupes.

- **Interfaces :** pont et exutoire sont des points de revue.

- **Frontière :** aucune simulation hydrologique autoritaire n’est créée.

## 24. Créer lacs, littoraux et zones humides

Un lac ou une mer intérieure possède un niveau d’eau de référence, une ligne de rive, des profondeurs candidates et des zones de transition. La ligne de rive doit être stable entre les cellules et cohérente avec les pentes.

Le terrain peut réserver des bandes pour plage, vase, roche ou falaise, mais leur rendu final dépend du pipeline de matériaux. Les zones humides sont des surfaces de placement futures pour le chapitre 15 ; elles ne contiennent pas encore de règles écologiques dynamiques.

> **[LECTURE] Profil du plan d’eau — Ne pas saisir.**

```yaml
water_body: AST-WORLD-LAKE-DELTA-001-v001
type: lake
reference_level_m: pending
shoreline:
  source: pending
  cross_cell_continuity: pending
depth:
  visual_profile: pending
  gameplay_authority: none
transition_zones:
  - beach_candidate
  - mud_candidate
  - rock_candidate
vegetation_surface_tags:
  status: prepared_only
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveau :** une altitude unique sert de référence au plan d’eau.

- **Continuité :** la rive doit traverser les cellules sans saut.

- **Profondeur :** le profil visuel n’impose pas les règles gameplay.

- **Végétation :** seuls des tags de surface sont préparés.

## 25. Séparer eau visuelle, collision et navigation

La surface visuelle de l’eau peut être un maillage, mais elle ne doit pas automatiquement devenir collision ou frontière de navigation. Un personnage, un bateau et un projectile n’ont pas les mêmes règles. Les volumes de détection, limites de nage et obstacles de navigation sont définis par les systèmes propriétaires.

Le chapitre fournit des interfaces spatiales : niveau, emprise, rives et volumes candidats. Il ne décide pas du gameplay de nage ni des dégâts.

> **[LECTURE] Responsabilités d’un plan d’eau — Ne pas saisir.**

```yaml
water_interfaces:
  visual_surface:
    owner: chapter_14
    status: not_produced
  shoreline_collision:
    owner: chapter_14
    status: not_produced
  swim_volume:
    owner: gameplay_system
    status: out_of_scope
  boat_navigation:
    owner: navigation_gameplay
    status: out_of_scope
  damage_or_temperature:
    owner: gameplay_system
    status: out_of_scope
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Visuel :** le chapitre possède la surface et les rives.

- **Gameplay :** nage, bateau et dégâts restent derrière leurs autorités.

- **Statuts :** `not_produced` et `out_of_scope` ne sont pas interchangeables.

- **Intégration :** les systèmes futurs consomment les interfaces sans modifier les sources.

## 26. Matériaux de terrain : responsabilité locale

Le chapitre définit où les matériaux doivent apparaître et comment leurs masques traversent les tuiles. Il ne réexplique pas l’albedo, les normales, la roughness, les espaces colorimétriques ou la compression : ces règles appartiennent au chapitre 16.

Un terrain pilote peut prévoir sol sec, roche, berge et route. Les matériaux restent des identifiants et des zones de mélange jusqu’à leur qualification PBR. Les masques sources doivent conserver une précision et une convention de canaux documentées.

> **[LECTURE] Profil matériel préparatoire — Ne pas saisir.**

```yaml
terrain_material_profile: AST-WORLD-MATERIAL-DELTA-001-v001
layers:
  - id: dry_ground
    material_asset: pending_chapter_16
  - id: exposed_rock
    material_asset: pending_chapter_16
  - id: river_bank
    material_asset: pending_chapter_16
  - id: road_surface
    material_asset: pending_chapter_16
mask_contract:
  source_precision: pending
  channel_mapping: pending
  border_continuity: required
shader_implementation: deferred_to_chapter_16
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couches :** les usages sont identifiés sans inventer les matériaux finaux.

- **Masques :** précision, canaux et continuité deviennent des contrats.

- **Frontière :** le shader et la compression sont différés au chapitre 16.

- **Statut :** le profil ne prétend pas qu’un matériau existe.

## 27. Construire les masques depuis des causes observables

Un masque de roche peut dépendre de la pente et d’une correction artistique ; une berge dépend de la proximité de l’eau et de l’altitude ; une route dépend de son corridor. Les règles procédurales ne doivent pas effacer la direction artistique ni multiplier les valeurs magiques.

Chaque contribution est enregistrée. Un artiste peut peindre une correction, mais cette correction reste une couche distincte et réversible. Les masques voisins partagent leurs bords comme les heightmaps.

> **[LECTURE] Graphe logique d’un masque — Ne pas saisir.**

```yaml
mask_recipe: AST-WORLD-MASK-ROCK-001-v001
inputs:
  slope: required
  altitude: optional
  curvature: optional
  artist_override: optional
combination:
  mode: documented_node_graph
  thresholds: pending_measurement
border_policy:
  shared_samples: required
output:
  authority: source_mask
  material_binding: pending_chapter_16
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** chaque cause du masque est nommée.

- **Seuils :** ils restent à calibrer sur des captures.

- **Override :** la correction artistique ne détruit pas les données procédurales.

- **Bords :** les masques suivent le même contrat de continuité que l’altitude.

## 28. Préparer la collision du terrain

`HeightMapShape3D` représente une grille de hauteurs et convient à une collision de terrain sans grottes ni surplombs. Sa documentation précise que `map_data` doit contenir `map_width × map_depth` valeurs et que `update_map_data_from_image()` peut convertir une image de hauteur. Les ponts, caves et falaises en surplomb exigent des collisions séparées.

La collision ne doit pas hériter automatiquement de toute la densité du maillage de rendu. Le profil compare une heightmap de collision, des maillages concaves statiques localisés et des formes simples. Toute échelle est qualifiée avec le moteur physique retenu ; aucune mise à l’échelle corrective cachée n’est admise.

> **[LECTURE] Profil de collision de cellule — Ne pas saisir.**

```yaml
terrain_collision_profile: AST-WORLD-COLLISION-CELL-001-v001
base_surface:
  candidate: HeightMapShape3D
  height_image: pending
  map_width: pending
  map_depth: pending
special_geometry:
  bridge:
    collision: dedicated
  cave:
    collision: dedicated
  overhang:
    collision: dedicated
checks:
  player_contact: not_executed
  vehicle_contact: not_executed
  border_contact: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** la heightmap couvre seulement les surfaces à hauteur unique.

- **Spécial :** ponts, caves et surplombs disposent de collisions dédiées.

- **Dimensions :** largeur et profondeur restent liées aux données de carte.

- **Tests :** contacts et frontières doivent être exécutés dans Godot.

## 29. Importer une heightmap de collision avec prudence

Une image chargée pour la collision doit être convertie vers un format accepté, puis remappée entre une altitude minimale et maximale. Ces bornes font partie du contrat de cellule. Une différence entre le maillage visuel et la collision produit des pieds flottants, des traversées ou des blocages.

Le code suivant est un exemple pédagogique non exécuté. Il crée une ressource `HeightMapShape3D` en mémoire ; il ne l’enregistre pas et ne modifie aucune scène. La validation réelle doit comparer plusieurs points connus entre heightmap, rendu et collision.

> **[VSC] Exemple GDScript non exécuté pour préparer une collision.**

```gdscript
func build_height_shape(
        height_texture: Texture2D,
        height_min_m: float,
        height_max_m: float
) -> HeightMapShape3D:
    if height_texture == null:
        push_error("Height texture is required.")
        return null
    if height_max_m <= height_min_m:
        push_error("height_max_m must be greater than height_min_m.")
        return null

    var image: Image = height_texture.get_image()
    if image == null or image.is_empty():
        push_error("Height image is unavailable.")
        return null

    image.convert(Image.FORMAT_RF)

    var shape := HeightMapShape3D.new()
    shape.update_map_data_from_image(image, height_min_m, height_max_m)
    return shape
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonction :** `build_height_shape` reçoit une texture et deux flottants, puis retourne une `HeightMapShape3D` ou `null`.

- **Paramètres :** les bornes d’altitude sont explicites et ordonnées.

- **Types :** `Texture2D`, `Image`, `float` et `HeightMapShape3D` limitent les conversions implicites.

- **Retour :** `null` signale un refus contrôlé ; aucun nœud n’est ajouté à la scène.

## 30. Préparer la navigation par cellules

Chaque cellule peut posséder une `NavigationRegion3D`, mais les régions doivent réellement partager des bords compatibles pour se connecter. La superposition de deux navmeshes n’est pas une preuve de connexion. Les marges, couches, cartes et temps de synchronisation sont contrôlés.

Le baking de navigation peut être coûteux. Pour une production stable, les sources, paramètres et résultats doivent être versionnés selon la politique du projet. Un bake en arrière-plan n’autorise pas une requête immédiate avant la fin et la synchronisation du serveur.

> **[LECTURE] Profil de navigation d’une cellule — Ne pas saisir.**

```yaml
navigation_cell_profile: AST-WORLD-NAV-CELL-001-v001
cell_id: AST-WORLD-CELL-DELTA-0001
region_node: NavigationRegion3D
navigation_layers: pending
source_geometry:
  terrain: pending
  architecture_interfaces: pending
  water_exclusions: pending
neighbor_connections:
  east: pending_edge_review
  west: pending_edge_review
  north: pending_edge_review
  south: pending_edge_review
path_tests: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœud :** chaque cellule possède une région identifiable.

- **Sources :** terrain, architecture et exclusions aquatiques sont séparés.

- **Voisins :** chaque bord est qualifié individuellement.

- **Preuve :** les requêtes de chemin doivent traverser réellement les frontières.

## 31. Traiter les raccords de navigation comme des interfaces

Une frontière de cellule possède une bande de raccord et des points de test. Le navmesh de chaque côté doit utiliser des paramètres compatibles. Les obstacles ou différences d’altitude près du bord peuvent empêcher la connexion malgré un rendu continu.

Le protocole teste un chemin dans les deux sens après synchronisation. Une réussite visuelle n’est pas suffisante ; le propriétaire retourné par le serveur et la trajectoire doivent être enregistrés dans un rapport.

> **[LECTURE] Test de raccord de navigation — Ne pas saisir.**

```yaml
navigation_border_test: AST-WORLD-NAV-BORDER-001-v001
pair:
  cell_a: AST-WORLD-CELL-DELTA-0001
  cell_b: AST-WORLD-CELL-DELTA-0002
queries:
  a_to_b:
    start: pending
    target: pending
    result: not_executed
  b_to_a:
    start: pending
    target: pending
    result: not_executed
synchronization_waited: false
edge_connection_margin_recorded: false
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Deux sens :** le test détecte une connexion asymétrique ou un point inaccessible.

- **Synchronisation :** aucune requête n’est interprétée avant mise à jour du serveur.

- **Marge :** la valeur réellement utilisée doit figurer dans le rapport.

- **Statut :** le raccord reste bloqué tant que les deux trajets ne passent pas.

## 32. Définir une scène autonome par cellule

Une cellule chargeable doit pouvoir être instanciée sans dépendre d’un ordre caché dans la scène principale. Sa racine porte son identifiant, son transform logique et ses enfants de rendu, collision, navigation, eau, interfaces et diagnostic.

Les dépendances globales, telles que l’éclairage principal ou les services, ne sont pas dupliquées dans chaque cellule. La cellule expose des points de connexion et des métadonnées ; le contrôleur mondial décide de son cycle de vie.

> **[LECTURE] Hiérarchie d’une scène de cellule — Ne pas saisir.**

```text
WorldCell3D
├── TerrainRender
├── TerrainCollision
├── NavigationRegion3D
├── WaterInterfaces
├── ArchitecturePads
├── DistantReplacement
├── DebugAnchors
└── CellMetadata
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** `WorldCell3D` porte l’identité et le cycle de vie.

- **Séparation :** rendu, collision et navigation restent des enfants distincts.

- **Global :** lumière, météo et services ne sont pas recopiés.

- **Diagnostic :** les ancres de debug permettent de comparer les frontières.

## 33. Décrire chaque cellule par un manifeste

Le manifeste fournit les coordonnées, le chemin de scène, les voisins, les dépendances et les profils. Il permet au contrôleur de raisonner sans ouvrir la scène. Les chemins restent absolus dans l’espace `res://` pour éviter les préfixes implicites.

Le manifeste ne contient pas l’état persistant du gameplay. Il décrit le contenu statique et les dépendances de chargement. Les modifications durables du monde appartiennent aux systèmes de sauvegarde et de simulation.

> **[LECTURE] Manifeste de cellule — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "cell_id": "AST-WORLD-CELL-DELTA-0001",
  "coordinate": {"east": 0, "north": 1},
  "scene_path": "res://world/delta/cells/cell_0001.tscn",
  "neighbors": {
    "east": "AST-WORLD-CELL-DELTA-0002",
    "west": null,
    "north": null,
    "south": "AST-WORLD-CELL-DELTA-0003"
  },
  "profiles": {
    "collision": "AST-WORLD-COLLISION-CELL-001-v001",
    "navigation": "AST-WORLD-NAV-CELL-001-v001",
    "lod": "AST-WORLD-LOD-CELL-001-v001"
  },
  "dependencies": []
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** `schema_version` rend les migrations possibles.

- **Voisins :** l’absence est représentée par `null`, pas par une chaîne vide.

- **Chemin :** `res://` évite une résolution relative divergente.

- **État :** aucune variable gameplay persistante n’est placée dans ce manifeste.

## 34. Définir des états de streaming explicites

Le chargement ne se résume pas à visible ou invisible. Une cellule peut être inconnue, demandée, en chargement, prête en mémoire, active dans l’arbre, épinglée, en retrait ou en erreur. Les transitions illégales doivent être refusées.

Une cellule prête n’est pas nécessairement active. Cette séparation permet de précharger avant l’arrivée du joueur. Inversement, une cellule désactivée peut rester brièvement en cache afin d’éviter un rechargement immédiat.

> **[LECTURE] Machine d’états de cellule — Ne pas saisir.**

```text
UNLOADED
   │ request
   ▼
REQUESTED
   │ background load
   ▼
LOADING ───── failure ─────► FAILED
   │ resource ready
   ▼
READY
   │ instantiate
   ▼
ACTIVE
   │ leave active radius
   ▼
RELEASING
   │ free or cache
   └────────────────────────► UNLOADED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préchargement :** `READY` sépare la ressource chargée de l’instance active.

- **Erreur :** `FAILED` est un état observable et non une exception silencieuse.

- **Retrait :** `RELEASING` permet de fermer navigation et références avant libération.

- **Transitions :** chaque flèche doit être journalisée avec la cellule concernée.

## 35. Charger les ressources en arrière-plan

`ResourceLoader.load_threaded_request()` lance une demande en arrière-plan. `load_threaded_get_status()` doit être interrogé sur des frames différentes ; une boucle serrée dans la même frame annule l’intérêt du chargement asynchrone. `load_threaded_get()` ne doit être appelé qu’après le statut `THREAD_LOAD_LOADED`, sinon il peut bloquer le thread appelant.

L’option `use_sub_threads` n’est pas activée par défaut dans le profil pédagogique : elle peut accélérer certaines charges mais aussi affecter le thread principal. La décision dépend d’un benchmark.

> **[VSC] Contrôleur pédagogique de demande de chargement.**

```gdscript
enum CellLoadState {
    UNLOADED,
    REQUESTED,
    LOADING,
    READY,
    FAILED,
}

var _states: Dictionary[StringName, CellLoadState] = {}
var _paths: Dictionary[StringName, String] = {}

func request_cell(cell_id: StringName, scene_path: String) -> Error:
    if scene_path.is_empty():
        return ERR_INVALID_PARAMETER
    if _states.get(cell_id, CellLoadState.UNLOADED) != CellLoadState.UNLOADED:
        return ERR_ALREADY_IN_USE

    var error := ResourceLoader.load_threaded_request(
        scene_path,
        "PackedScene",
        false,
        ResourceLoader.CACHE_MODE_REUSE
    )
    if error != OK:
        _states[cell_id] = CellLoadState.FAILED
        return error

    _paths[cell_id] = scene_path
    _states[cell_id] = CellLoadState.LOADING
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Enum :** `CellLoadState` limite les statuts à cinq valeurs nommées.

- **Dictionnaires :** les clés `StringName` associent état et chemin à l’identité de cellule.

- **Fonction :** `request_cell` retourne un `Error` et ne crée aucune instance.

- **Opérateurs :** `!=` refuse une seconde demande et `is_empty()` valide le chemin.

## 36. Sonder le chargement sans bloquer

Le sondage s’effectue une fois par frame ou selon un budget. Le tableau de progression est facultatif et ne doit pas être interprété comme un temps restant fiable. Les statuts invalides ou échoués sont journalisés.

Quand la ressource est prête, le contrôleur la récupère et vérifie son type avant de l’ajouter au registre. L’instanciation est une étape séparée qui peut elle-même produire un pic ; elle doit être mesurée.

> **[VSC] Sondage pédagogique des demandes.**

```gdscript
var _ready_scenes: Dictionary[StringName, PackedScene] = {}

func poll_cell(cell_id: StringName) -> CellLoadState:
    if not _paths.has(cell_id):
        return CellLoadState.UNLOADED

    var path: String = _paths[cell_id]
    var progress: Array = []
    var status := ResourceLoader.load_threaded_get_status(path, progress)

    match status:
        ResourceLoader.THREAD_LOAD_IN_PROGRESS:
            return CellLoadState.LOADING
        ResourceLoader.THREAD_LOAD_LOADED:
            var resource: Resource = ResourceLoader.load_threaded_get(path)
            var packed := resource as PackedScene
            if packed == null:
                _states[cell_id] = CellLoadState.FAILED
                return CellLoadState.FAILED
            _ready_scenes[cell_id] = packed
            _states[cell_id] = CellLoadState.READY
            return CellLoadState.READY
        ResourceLoader.THREAD_LOAD_FAILED, ResourceLoader.THREAD_LOAD_INVALID_RESOURCE:
            _states[cell_id] = CellLoadState.FAILED
            return CellLoadState.FAILED
        _:
            _states[cell_id] = CellLoadState.FAILED
            return CellLoadState.FAILED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonction :** `poll_cell` retourne toujours un `CellLoadState` explicite.

- **Négation :** `not _paths.has(cell_id)` protège l’accès au chemin.

- **Match :** chaque statut du chargeur possède un traitement.

- **Cast :** `as PackedScene` vérifie le type avant stockage et peut retourner `null`.

## 37. Instancier une cellule prête

L’instanciation vérifie que la ressource est prête, que l’identifiant n’est pas déjà actif et que la racine possède le contrat attendu. Le parent mondial conserve l’autorité du transform. La cellule ne se place pas elle-même en déduisant sa position depuis son nom.

L’ajout dans l’arbre, l’activation de la collision et la connexion de la navigation peuvent être étalés si les mesures montrent un pic. Le chapitre ne prétend pas qu’un ordre unique est optimal.

> **[VSC] Exemple d’instanciation contrôlée.**

```gdscript
var _active_cells: Dictionary[StringName, Node3D] = {}

func activate_cell(
        cell_id: StringName,
        world_transform: Transform3D,
        world_parent: Node3D
) -> Error:
    if world_parent == null:
        return ERR_INVALID_PARAMETER
    if _active_cells.has(cell_id):
        return ERR_ALREADY_IN_USE

    var packed: PackedScene = _ready_scenes.get(cell_id)
    if packed == null:
        return ERR_DOES_NOT_EXIST

    var instance := packed.instantiate() as Node3D
    if instance == null:
        return ERR_CANT_CREATE

    world_parent.add_child(instance)
    instance.global_transform = world_transform
    _active_cells[cell_id] = instance
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** l’identifiant, le transform et le parent sont fournis explicitement.

- **Retours :** les codes distinguent paramètre invalide, doublon, absence et échec d’instanciation.

- **Cast :** la racine doit être un `Node3D`.

- **Effet :** l’ajout à l’arbre est le seul effet de bord du chemin nominal.

## 38. Précharger par voisinage et vitesse

Le rayon de préchargement dépend de la vitesse, du temps de chargement mesuré, de la direction probable et de la topologie. Un cercle fixe peut être suffisant pour le pilote, mais il ne doit pas être présenté comme universel.

Le manifeste permet de demander d’abord les voisins directs, puis les cellules situées sur le corridor de déplacement. Les téléportations, cinématiques et déplacements rapides exigent une politique distincte.

> **[LECTURE] Politique de préchargement — Ne pas saisir.**

```yaml
preload_policy: AST-WORLD-PRELOAD-001-v001
inputs:
  player_cell: required
  velocity: required
  predicted_route: optional
  measured_load_time: required_before_acceptance
rings:
  active: pending
  ready: pending
  distant: pending
priority:
  - current_route
  - direct_neighbors
  - visible_landmarks
teleport_policy: separate_required
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** position logique, vitesse et temps mesuré alimentent la décision.

- **Anneaux :** les distances restent provisoires.

- **Priorité :** la route et les voisins précèdent les cellules arbitraires.

- **Téléportation :** elle n’utilise pas silencieusement le même profil.

## 39. Ajouter une hystérésis

Sans hystérésis, une caméra proche d’une frontière peut charger et retirer la même cellule à chaque oscillation. Le rayon de sortie doit être supérieur au rayon d’entrée, ou un délai minimal doit empêcher l’éviction immédiate.

L’hystérésis est exprimée en métriques observables et testée sur un parcours de va-et-vient. Elle ne doit pas retenir indéfiniment toutes les cellules.

> **[LECTURE] Profil d’hystérésis — Ne pas saisir.**

```yaml
stream_hysteresis: AST-WORLD-HYSTERESIS-001-v001
activation_distance_m: pending
release_distance_m: pending
minimum_active_time_s: pending
rules:
  release_distance_greater_than_activation: required
  pinned_cells_never_released: true
  memory_budget_can_force_review: true
oscillation_test: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Relation :** le seuil de sortie doit dépasser celui d’entrée.

- **Temps :** une durée minimale peut absorber les allers-retours rapides.

- **Épinglage :** les cellules requises échappent temporairement à l’éviction.

- **Budget :** l’hystérésis reste soumise à la mémoire mesurée.

## 40. Épingler les cellules encore nécessaires

Une cellule est épinglée lorsqu’une référence durable l’exige : joueur présent, requête de navigation active, cinématique, interaction, sauvegarde en cours ou dépendance d’une cellule voisine. Le compteur d’épinglage est préférable à un booléen lorsque plusieurs propriétaires peuvent retenir la même cellule.

Chaque propriétaire doit libérer son épingle. Un diagnostic détecte les cellules retenues sans raison et les retraits tentés avec un compteur positif.

> **[LECTURE] Registre d’épinglage — Ne pas saisir.**

```yaml
cell_pins:
  AST-WORLD-CELL-DELTA-0001:
    player_presence: 1
    active_navigation_query: 0
    cinematic: 0
    save_transaction: 0
rules:
  release_allowed_when_total_zero: true
  negative_counts: forbidden
  owner_required: true
leak_report: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Compteurs :** chaque propriétaire possède une valeur indépendante.

- **Somme :** le retrait n’est autorisé que lorsque le total vaut zéro.

- **Invariant :** un compteur négatif révèle une libération en trop.

- **Diagnostic :** les fuites d’épingles doivent apparaître dans un rapport.

## 41. Retirer une cellule en plusieurs étapes

Le retrait doit empêcher de nouvelles interactions, désactiver ou détacher les interfaces de navigation, attendre les opérations critiques, retirer la scène et libérer les références. `queue_free()` seul ne décrit pas ce protocole.

Les données persistantes ne sont pas sauvegardées automatiquement par le terrain. Le contrôleur demande aux autorités concernées de confirmer leurs transactions avant la libération.

> **[LECTURE] Séquence de retrait — Ne pas saisir.**

```text
Demande de retrait
    ↓
Refuser si cellule épinglée
    ↓
Fermer les nouvelles interactions
    ↓
Détacher navigation et signaux
    ↓
Confirmer les transactions propriétaires
    ↓
Retirer l'instance de l'arbre
    ↓
Libérer les références de ressource selon la politique de cache
    ↓
Marquer UNLOADED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Refus :** une épingle active interrompt la séquence.

- **Navigation :** les interfaces sont fermées avant la disparition du nœud.

- **Transactions :** le terrain coordonne sans posséder l’état métier.

- **Cache :** ressource et instance suivent des politiques distinctes.

## 42. Séparer streaming et sauvegarde

Le manifeste de cellule décrit le contenu statique. Les arbres coupés, coffres ouverts, quêtes, personnages et constructions dynamiques appartiennent aux autorités du Livre II et à la sauvegarde. Charger une cellule déclenche une demande de matérialisation de cet état ; retirer une cellule déclenche une démobilisation coordonnée.

Le terrain ne sérialise pas un snapshot complet de tous les systèmes. Il expose `cell_id` comme clé de contexte et attend des réponses versionnées.

> **[LECTURE] Frontière de persistance — Ne pas saisir.**

```yaml
cell_lifecycle:
  static_content:
    owner: world_content
    source: cell_scene_and_manifest
  persistent_changes:
    owner: save_and_domain_systems
    key: cell_id
  ecological_state:
    owner: book_II_ecology
  quest_state:
    owner: book_II_narrative
  runtime_buildings:
    owner: book_II_construction
stream_controller:
  may_request_materialization: true
  may_mutate_authoritative_state: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statique :** la scène de cellule porte uniquement le contenu publié.

- **Persistant :** les changements sont récupérés par les systèmes propriétaires.

- **Clé :** `cell_id` relie les contextes sans déplacer l’autorité.

- **Interdiction :** le contrôleur ne modifie pas directement l’état métier.

## 43. Préparer les LOD du relief

Le LOD de terrain réduit le nombre de sommets à distance tout en préservant silhouette, bordures et raccords. Les tuiles voisines de niveaux différents peuvent créer des fissures ; le pipeline prévoit des skirts, des bandes de transition, des topologies compatibles ou une contrainte de différence maximale.

Les distances sont calibrées dans Godot selon la caméra, la résolution et la plateforme. Un profil LOD ne contient pas seulement des nombres : il nomme les représentations, leurs sources, leurs erreurs maximales et leurs tests de transition.

> **[LECTURE] Profil LOD d’une tuile — Ne pas saisir.**

```yaml
terrain_lod_profile: AST-WORLD-LOD-TILE-001-v001
levels:
  - id: LOD0
    mesh: not_produced
    geometric_error_m: pending
  - id: LOD1
    mesh: not_produced
    geometric_error_m: pending
  - id: LOD2
    mesh: not_produced
    geometric_error_m: pending
neighbor_rule:
  maximum_level_difference: pending
crack_mitigation:
  method: pending_comparison
thresholds_m: pending_measurement
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** chaque LOD possède un maillage et une erreur géométrique.

- **Voisins :** la différence de niveau doit être contrôlée.

- **Fissures :** la méthode reste à comparer plutôt qu’à supposer.

- **Seuils :** aucune distance n’est déclarée avant mesure.

## 44. Construire un HLOD de secteur et un horizon

Un HLOD remplace plusieurs cellules proches par une représentation agrégée lorsque le joueur est loin. Pour un paysage, l’agrégat peut contenir une silhouette de terrain, des masses architecturales et un matériau distant, sans collisions détaillées ni navigation active.

L’horizon lointain doit être cohérent avec le relief proche et ne pas apparaître comme une seconde montagne décalée. Les `visibility_range_begin`, `visibility_range_end` et marges de `GeometryInstance3D` peuvent participer à la transition, mais leurs valeurs exigent des captures et mesures.

> **[LECTURE] Profil HLOD de secteur — Ne pas saisir.**

```yaml
sector_hlod: AST-WORLD-HLOD-SECTOR-NORTH-001-v001
replaces_cells:
  - AST-WORLD-CELL-DELTA-0001
  - AST-WORLD-CELL-DELTA-0002
representation:
  terrain_shell: not_produced
  architecture_masses: not_produced
  collision: absent
  navigation: absent
visibility_ranges:
  begin_m: pending
  end_m: pending
  margins_m: pending
transition_capture: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Agrégation :** un seul groupe remplace plusieurs cellules.

- **Responsabilités :** collision et navigation ne sont pas conservées dans la vue distante.

- **Marges :** elles servent à l’hystérésis ou au fondu selon la configuration.

- **Preuve :** une capture en mouvement doit vérifier l’horizon et la transition.

## 45. Employer l’occlusion avec discernement

Les grands paysages ouverts offrent peu de volumes capables de masquer durablement la vue. La documentation Godot indique que l’occlusion a un coût CPU et que les scènes ouvertes bénéficient souvent davantage du LOD et des plages de visibilité. Le projet ne doit donc pas activer l’occlusion par réflexe.

Les falaises, canyons, tunnels et masses architecturales peuvent fournir des occluders utiles. Chaque cas est comparé avec l’occlusion désactivée, puis activée, en observant CPU, rendu et artefacts. Les surfaces transparentes ne sont pas utilisées comme preuve d’occlusion.

> **[LECTURE] Décision d’occlusion paysagère — Ne pas saisir.**

```yaml
landscape_occlusion_profile: AST-WORLD-OCCLUSION-001-v001
default:
  enabled: false
candidates:
  - canyon_wall_mass
  - tunnel_mass
  - large_architecture_cluster
excluded:
  - open_plain
  - water_surface
  - vegetation_cards
comparison:
  cpu_cost: not_measured
  visible_instances: not_measured
  artifacts: not_reviewed
decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** l’occlusion reste désactivée sans bénéfice démontré.

- **Candidats :** seules les grandes masses opaques sont envisagées.

- **Exclusions :** plaine, eau et cartes végétales ne servent pas de raccourci.

- **Comparaison :** le coût CPU et le gain de visibilité sont mesurés ensemble.

## 46. Maintenir la continuité de lumière, brouillard et horizon

Le changement de cellule ne doit pas modifier silencieusement le soleil, le ciel, l’exposition ou le brouillard global. Ces paramètres appartiennent à une scène ou un service mondial. Les cellules peuvent fournir des volumes locaux ou des suggestions, mais elles ne dupliquent pas un `WorldEnvironment` concurrent.

Le brouillard peut masquer certaines transitions lointaines, mais il ne doit pas servir à dissimuler des fissures proches ou un chargement tardif. Les profils d’ambiance sont testés sous plusieurs heures et conditions prévues.

> **[LECTURE] Autorités d’environnement — Ne pas saisir.**

```yaml
environment_authority:
  sun: world_scene
  sky: world_scene
  exposure: world_scene
  global_fog: world_scene
cell_contributions:
  local_fog_volume: optional
  reflection_probe: optional
  environment_override: forbidden_by_default
seam_hiding:
  fog_as_primary_fix: forbidden
lighting_tests:
  conditions: pending
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Global :** soleil, ciel, exposition et brouillard ne sont pas dupliqués.

- **Local :** une cellule peut proposer un volume borné.

- **Interdiction :** le brouillard ne remplace pas la correction d’une fissure.

- **Tests :** plusieurs conditions sont nécessaires avant validation.

## 47. Organiser la scène mondiale

La scène mondiale contient le contrôleur, les racines d’instances, l’environnement global, les services de navigation et les outils de diagnostic. Les cellules sont instanciées sous une racine dédiée. Les HLOD et vues distantes possèdent une racine distincte pour permettre leur comparaison.

Le contrôleur ne recherche pas les cellules par parcours fragile dans l’arbre. Les références sont injectées ou résolues une fois au démarrage, puis validées.

> **[LECTURE] Hiérarchie de la scène mondiale — Ne pas saisir.**

```text
WorldRoot
├── WorldEnvironment
├── Sun
├── CellStreamController
├── ActiveCells
├── ReadyCellCache
├── SectorHLOD
├── NavigationWorld
├── WaterWorld
└── WorldDiagnostics
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racines :** cellules actives, cache et HLOD sont séparés.

- **Environnement :** les paramètres globaux n’appartiennent pas aux cellules.

- **Navigation :** le monde fournit la carte ou les services communs.

- **Diagnostic :** les métriques et overlays restent hors des assets.

## 48. Exporter les maillages depuis Blender

Les maillages de terrain, routes, berges et formes spéciales peuvent être exportés en GLB selon les conventions du chapitre 4. La heightmap maître et les masques restent des données séparées lorsque le pipeline les consomme directement.

Chaque collection d’export est explicite. Les axes, unités et transforms sont vérifiés avant publication. Les collisions dédiées peuvent être exportées séparément ou reconstruites dans Godot selon le contrat ; leur méthode n’est pas mélangée silencieusement entre cellules.

> **[LECTURE] Collection Blender de livraison — Ne pas saisir.**

```text
AST-WORLD-CELL-DELTA-0001
├── __EXPORT_RENDER
│   ├── terrain_tile_LOD0
│   ├── road_mesh
│   ├── river_banks
│   └── special_overhangs
├── __EXPORT_COLLISION
│   ├── bridge_collision
│   └── overhang_collision
├── __GUIDES
│   ├── road_centerline
│   ├── river_centerline
│   └── border_anchors
└── __SOURCE
    ├── sculpt_mesh
    └── modifiers
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Export :** rendu et collision sont des collections distinctes.

- **Guides :** courbes et ancres restent disponibles pour contrôle.

- **Source :** le sculpt et les modificateurs ne sont pas confondus avec le GLB.

- **Sélection :** l’export se fonde sur des collections nommées, pas une sélection manuelle.

## 49. Conserver une scène Godot dérivée

La scène importée depuis le GLB est considérée comme dérivée. Une scène héritée ou composée ajoute collision, navigation, métadonnées, interfaces et scripts sans modifier la ressource importée. Le réimport peut alors remplacer le maillage sans effacer les nœuds moteur.

Les heightmaps de collision et manifestes sont référencés par chemins stables. Toute dépendance absente bloque la cellule au lieu de déclencher une correction silencieuse.

> **[LECTURE] Structure importée et dérivée — Ne pas saisir.**

```text
res://art/imported/world/delta/cell_0001.glb
        ↓ import
ImportedCell0001
        ↓ composition
res://world/delta/cells/cell_0001.tscn
├── ImportedCell0001
├── TerrainCollision
├── NavigationRegion3D
├── CellMetadata
└── WorldCellContract
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** le GLB reste remplaçable.

- **Composition :** la scène dérivée ajoute les responsabilités Godot.

- **Contrat :** l’identité et les dépendances ne sont pas stockées dans le nom du maillage.

- **Réimport :** les nœuds moteur survivent à une nouvelle version du GLB.

## 50. Valider la structure d’une cellule

Un validateur non destructif vérifie identifiant, enfants requis, chemins, profil de collision et région de navigation. Il ne crée pas de nœuds manquants et ne corrige pas les transforms. Son rapport distingue erreur bloquante, avertissement et information.

Le script suivant illustre les types, fonctions, paramètres, retours, boucles, casts et opérateurs nécessaires. Il n’a pas été exécuté dans Godot.

> **[VSC] Validateur structurel pédagogique.**

```gdscript
class_name WorldCellValidator
extends RefCounted

const REQUIRED_CHILDREN: Array[StringName] = [
    &"TerrainRender",
    &"TerrainCollision",
    &"NavigationRegion3D",
    &"CellMetadata",
]

func validate(cell_root: Node3D, expected_id: StringName) -> Dictionary:
    var report := {
        "cell_id": String(expected_id),
        "errors": [],
        "warnings": [],
        "info": [],
    }

    if cell_root == null:
        report["errors"].append("Cell root is null.")
        return report

    var metadata := cell_root.get_node_or_null("CellMetadata")
    if metadata == null:
        report["errors"].append("CellMetadata is missing.")
    else:
        var actual_id := StringName(metadata.get_meta("cell_id", ""))
        if actual_id != expected_id:
            report["errors"].append(
                "Cell id mismatch: %s != %s" % [actual_id, expected_id]
            )

    for child_name: StringName in REQUIRED_CHILDREN:
        if cell_root.get_node_or_null(NodePath(child_name)) == null:
            report["errors"].append("Missing child: %s" % child_name)

    var navigation := cell_root.get_node_or_null("NavigationRegion3D")
    if navigation != null and not navigation is NavigationRegion3D:
        report["errors"].append("NavigationRegion3D has an invalid type.")

    report["info"].append("Validation is non-destructive.")
    return report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `WorldCellValidator` hérite de `RefCounted` et ne rejoint pas l’arbre.

- **Fonction :** `validate` reçoit un `Node3D` et un `StringName`, puis retourne un `Dictionary`.

- **Boucle :** `for` parcourt la liste typée des enfants requis.

- **Opérateurs :** `==`, `!=`, `and` et `not ... is` expriment les invariants sans modifier la cellule.

## 51. Expliquer fonctions, paramètres, types et retours

Dans le validateur :

- `validate` est une fonction purement diagnostique à l’exception de la construction du rapport ;
- `cell_root` est nullable en pratique malgré son annotation, donc le garde-fou reste nécessaire ;
- `expected_id` utilise `StringName` pour une identité fréquemment comparée ;
- le `Dictionary` retourné regroupe des tableaux d’erreurs, d’avertissements et d’informations ;
- `get_node_or_null()` évite une exception de chemin ;
- `is NavigationRegion3D` vérifie le type runtime ;
- la fonction retourne tôt lorsque la racine est absente.

Le type `Dictionary` reste volontairement générique pour une sérialisation JSON simple. Une production plus stricte peut introduire une classe de rapport, sans changer les responsabilités.

> **[LECTURE] Forme du rapport du validateur — Ne pas saisir.**

```json
{
  "cell_id": "AST-WORLD-CELL-DELTA-0001",
  "errors": [
    "Missing child: TerrainCollision"
  ],
  "warnings": [],
  "info": [
    "Validation is non-destructive."
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chaînes :** les messages sont destinés au rapport et non au contrôle de flux.

- **Tableaux :** plusieurs diagnostics peuvent coexister.

- **Blocage :** une liste `errors` non vide empêche la promotion.

- **Sérialisation :** la structure est compatible avec un JSON de preuve.

## 52. Construire une scène de benchmark

La scène de benchmark reproduit une traversée définie, avec caméra, vitesse, ordre de cellules et points de capture. Elle enregistre le matériel, le système, les versions, les paramètres, le nombre de répétitions et les unités. Une seule traversée dans l’éditeur ne suffit pas.

Le benchmark doit distinguer temps de demande, temps de ressource prête, temps d’instanciation, pic de frame, mémoire avant/après et éventuelles ruptures. Les captures visuelles complètent les mesures pour les fissures, pops et horizons.

> **[LECTURE] Profil de benchmark — Ne pas saisir.**

```yaml
benchmark_scene: AST-WORLD-BENCH-DELTA-001-v001
route: main_traversal_loop
environment:
  hardware: pending
  os: Windows_11
  godot: 4.7.1-stable
  renderer: Forward+
  build: pending
repetitions: pending
measurements:
  request_to_ready_ms: pending
  ready_to_active_ms: pending
  peak_frame_ms: pending
  memory_peak_mib: pending
  cells_loaded_peak: pending
visual_checks:
  cracks: pending
  material_seams: pending
  lod_pops: pending
  horizon_mismatch: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Environnement :** matériel, build et versions accompagnent les mesures.

- **Phases :** chargement et instanciation sont séparés.

- **Unités :** millisecondes et MiB évitent les valeurs sans dimension.

- **Visuel :** fissures et pops ne sont pas déduits des seules métriques.

## 53. Mesurer les temps de chargement

Le temps `request_to_ready` mesure le chargement de la ressource. `ready_to_active` mesure l’instanciation et l’activation. Le temps jusqu’à une navigation utilisable peut être plus long si le serveur doit synchroniser ses régions. Ces durées sont enregistrées par cellule et par répétition.

Les caches peuvent réduire fortement les passages suivants. Le rapport distingue donc démarrage froid, cache chaud et rechargement après éviction. Les valeurs extrêmes ne sont pas supprimées sans justification.

> **[LECTURE] Ligne de mesure d’une cellule — Ne pas saisir.**

```json
{
  "run_id": "pending",
  "cell_id": "AST-WORLD-CELL-DELTA-0001",
  "cache_state": "cold",
  "request_started_ms": 0,
  "resource_ready_ms": null,
  "instance_active_ms": null,
  "navigation_ready_ms": null,
  "failed": false,
  "notes": []
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Horodatages :** chaque phase possède sa propre valeur.

- **Null :** une phase non atteinte reste `null` au lieu de devenir zéro.

- **Cache :** l’état froid ou chaud est enregistré.

- **Échec :** le booléen est accompagné de notes plutôt que d’une valeur inventée.

## 54. Mesurer la mémoire et les pics de frame

La mémoire est observée avant la traversée, au pic de cellules actives et après éviction. Le rapport précise si la mesure vient du profiler Godot, du système ou d’un outil externe. Les valeurs ne sont pas additionnées entre outils incompatibles.

Les pics de frame sont corrélés avec les événements : récupération de ressource, instanciation, ajout de collision, connexion de navigation, compilation de shader ou libération. Cette corrélation aide à choisir un étalement plutôt qu’une optimisation générale non ciblée.

> **[LECTURE] Journal de corrélation — Ne pas saisir.**

```csv
timestamp_ms,event,cell_id,frame_ms,memory_mib,source
0,benchmark_start,,pending,pending,pending
0,load_request,AST-WORLD-CELL-DELTA-0001,pending,pending,pending
0,resource_ready,AST-WORLD-CELL-DELTA-0001,pending,pending,pending
0,instance_active,AST-WORLD-CELL-DELTA-0001,pending,pending,pending
0,navigation_ready,AST-WORLD-CELL-DELTA-0001,pending,pending,pending
0,cell_released,AST-WORLD-CELL-DELTA-0001,pending,pending,pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **CSV :** chaque ligne relie un événement à une cellule.

- **Temps :** `timestamp_ms` permet la corrélation avec la frame.

- **Source :** l’outil de mesure doit être identifié.

- **Placeholders :** `pending` interdit de présenter l’exemple comme un résultat.

## 55. Tester les ruptures de parcours

Une campagne de rupture traverse chaque frontière à pied, en course, avec la caméra proche du sol et depuis un point haut. Elle vérifie le rendu, la collision, la navigation, les matériaux, l’eau, les LOD et le chargement.

Le test ne se limite pas à une trajectoire centrale. Les diagonales et déplacements parallèles aux frontières exposent davantage les oscillations, fissures et évictions prématurées.

> **[LECTURE] Matrice de test des frontières — Ne pas saisir.**

```yaml
border_test_matrix:
  crossings:
    - direction: orthogonal
      speed: walk
    - direction: orthogonal
      speed: run
    - direction: diagonal
      speed: run
    - direction: parallel_near_border
      speed: walk
  camera_profiles:
    - gameplay_default
    - low_angle
    - elevated_view
  checks:
    - render_crack
    - collision_step
    - navigation_path
    - material_seam
    - water_seam
    - lod_transition
    - stream_oscillation
results: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Directions :** plusieurs angles révèlent des défauts différents.

- **Caméras :** vue basse et vue élevée complètent la caméra standard.

- **Contrôles :** tous les systèmes de frontière sont listés.

- **Résultat :** aucune conclusion n’est tirée avant exécution.

## 56. Parcours Solo et Studio

### 56.1 Mode Solo

Le parcours Solo limite la région pilote et le nombre de cellules. Il privilégie une boucle complète avec un seul pipeline de heightmap, un petit jeu de matériaux préparatoires et des profils de chargement simples. La priorité est de fermer une preuve reproductible avant d’agrandir le monde.

Le même identifiant, le même manifeste et les mêmes portes d’acceptation sont utilisés qu’en Studio. La simplification porte sur la quantité, pas sur la traçabilité.

> **[LECTURE] Priorités Solo — Ne pas saisir.**

```yaml
solo_plan:
  region_count: 1
  pilot_region: AST-WORLD-REGION-DELTA-001
  traversal_loops: 1
  alternate_paths: 1
  material_layers: limited
  streaming_strategy: simple_measured_rings
  automation: optional_after_manual_proof
quality_gates:
  same_as_studio: true
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Quantité :** une région et une boucle suffisent au pilote.

- **Stratégie :** les anneaux simples doivent tout de même être mesurés.

- **Automatisation :** elle vient après une preuve manuelle.

- **Qualité :** les portes ne sont pas réduites.

### 56.2 Mode Studio

Le parcours Studio attribue des propriétaires aux régions, secteurs, heightmaps, routes, eau, matériaux, collisions, navigation et streaming. Les bordures de cellules sont des interfaces contractuelles soumises à revue. Les changements de schéma déclenchent une migration et une validation croisée.

La matrice de plateformes conserve plusieurs profils de mémoire et de distance, mais partage les mêmes sources canoniques. Les benchmarks sont exécutés sur plusieurs machines qualifiées.

> **[LECTURE] Responsabilités Studio — Ne pas saisir.**

```yaml
studio_ownership:
  region_design: environment_team
  height_sources: terrain_team
  roads_and_water: environment_team
  material_bindings: lookdev_team
  collisions: technical_art
  navigation: gameplay_navigation
  streaming: engine_team
  benchmarks: qa_performance
cross_reviews:
  border_contracts: required
  schema_changes: required
  platform_profiles: required
status: provisional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaires :** chaque responsabilité possède une équipe.

- **Revue :** bordures et schémas ne changent pas unilatéralement.

- **Plateformes :** plusieurs profils consomment les mêmes sources.

- **QA :** la performance est mesurée par une fonction identifiable.

## 57. Porte d’acceptation

La région pilote n’est acceptée que lorsque les preuves suivantes existent :

- brief, échelle, repère et partition approuvés ;
- heightmap maître et dérivés traçables ;
- relief macro et méso validé depuis les caméras prévues ;
- routes, rivière, lac et pads architecturaux raccordés ;
- bordures de tuiles sans fissures de rendu ou collision ;
- matériaux et masques continus ;
- collisions testées ;
- chemins de navigation traversant les cellules dans les deux sens ;
- scènes de cellules et manifestes valides ;
- chargement en arrière-plan, activation et retrait testés ;
- hystérésis et épinglage observables ;
- LOD, HLOD et horizon qualifiés ;
- benchmarks froids et chauds enregistrés ;
- mémoire et pics de frame dans des budgets approuvés ;
- provenance et licences qualifiées.

Une valeur manquante produit `blocked`, jamais `accepted_with_assumption`.

> **[LECTURE] Gate d’acceptation — Ne pas saisir.**

```yaml
acceptance_gate: AST-WORLD-REGION-DELTA-GATE-001-v001
documentation:
  brief: reviewed
  coordinate_contract: reviewed
  partition_profile: reviewed
assets:
  height_source: blocked
  terrain_tiles: blocked
  roads: blocked
  water: blocked
  materials: blocked
systems:
  collision: blocked
  navigation: blocked
  streaming: blocked
  lod_hlod: blocked
evidence:
  traversal: blocked
  memory: blocked
  load_times: blocked
  visual_continuity: blocked
  provenance: blocked
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Groupes :** documentation, assets, systèmes et preuves sont séparés.

- **Blocage :** le texte relu ne ferme pas les livrables matériels.

- **Décision :** aucun statut intermédiaire ne masque une preuve absente.

- **Promotion :** tous les groupes doivent passer selon la politique du projet.

## 58. Erreurs fréquentes et diagnostics

<!-- qa:error-correction-section -->

Les dix cas suivants conservent une structure fixe : symptôme, exemple fautif, explication immédiate, exemple corrigé et explication de la correction. Ils servent à diagnostiquer le pipeline, pas à produire des mesures fictives.

### 58.1 Choisir l’échelle après le sculpt

**Symptôme :** la vallée paraît immense dans Blender mais se traverse en quelques secondes dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
terrain:
  sculpt_status: detailed
  world_scale_m: undefined
  character_reference: absent
  route_time: assumed
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le relief détaillé n’est relié ni au mètre, ni au personnage, ni à une durée mesurée ; toute correction tardive déforme pentes, eau et bâtiments.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
terrain:
  world_scale_contract: AST-WORLD-COORD-001-v001
  character_reference: required
  route_time: pending_measurement
  sculpt_status: macro_blockout
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le contrat métrique et les gabarits précèdent le détail, tandis que la durée reste explicitement à mesurer.

### 58.2 Construire un seul maillage géant

**Symptôme :** l’éditeur devient lourd et aucune partie du terrain ne peut être chargée ou retirée indépendamment.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
world_mesh:
  cells: 1
  render_mesh: entire_region_high_density
  collision: entire_region_concave
  streaming: impossible
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le maillage fusionne édition, rendu, collision et streaming en une unité sans budget ni possibilité d’éviction.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
world_partition:
  profile: AST-WORLD-PARTITION-001-v001
  cell_scenes: pending
  terrain_tiles: pending
  collision_profiles: pending
  streaming_benchmark: not_executed
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le découpage devient un contrat à tester et chaque responsabilité peut être mesurée séparément.

### 58.3 Publier une heightmap 8 bits comme source maître

**Symptôme :** les pentes présentent des terrasses malgré un maillage très dense.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
height_source:
  format: PNG
  precision_bits: 8
  authority: master
  import_review: skipped
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La quantification de hauteur est insuffisante pour la source et le format est promu sans test d’import.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
height_source:
  master_format: EXR
  precision_bits: 32
  derived_preview: PNG
  import_review: pending
  collision_comparison: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La source haute précision reste distincte de l’aperçu et attend une comparaison rendu-collision.

### 58.4 Lisser chaque tuile indépendamment

**Symptôme :** une fissure et une cassure de lumière apparaissent sur la frontière.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
tile_a:
  east_edge: smoothed_locally
tile_b:
  west_edge: smoothed_locally
shared_border_authority: none
visual_review: single_tiles_only
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Deux opérations locales produisent des valeurs et normales divergentes sur une interface qui devrait être commune.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
border_contract: AST-WORLD-BORDER-001-v001
shared_height_strip: pending
sample_equality: pending
normal_continuity: pending
assembled_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Une seule autorité de bordure et une revue assemblée remplacent les corrections indépendantes.

### 58.5 Peindre une route sans préparer le relief

**Symptôme :** la texture suggère une route mais le personnage franchit des marches, dévers et talus impossibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
road:
  representation: painted_mask_only
  corridor: absent
  cross_section: absent
  collision_review: skipped
  navigation_review: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le masque visuel ne définit ni géométrie praticable, ni section, ni raccords physiques.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
road_corridor: AST-WORLD-ROAD-MAIN-001-v001
centerline: pending
cross_section: pending
terrain_conform: pending
collision_review: pending
navigation_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le corridor et sa section gouvernent le relief avant que le matériau ne représente la surface.

### 58.6 Tracer une rivière indépendamment des altitudes

**Symptôme :** le cours d’eau remonte une pente et traverse une crête sans coupe.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
river:
  centerline: hand_drawn_for_composition
  elevation_check: none
  watershed: ignored
  outlet: undefined
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le tracé ne possède ni règle de pente, ni bassin versant, ni exutoire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
river_profile: AST-WORLD-RIVER-DELTA-001-v001
watershed_review: pending
non_increasing_elevation: required
outlet: lake_delta
cross_sections: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil relie le cours d’eau aux altitudes et à une destination vérifiable.

### 58.7 Utiliser le maillage de rendu détaillé comme collision

**Symptôme :** la physique accroche sur de petites irrégularités et le chargement de cellule produit un pic.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
terrain_collision:
  source: render_LOD0
  shape: ConcavePolygonShape3D
  density_review: none
  special_geometry: merged
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La collision hérite du détail visuel, fusionne les formes spéciales et n’a aucun budget.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
terrain_collision:
  base_surface: HeightMapShape3D_candidate
  special_geometry: dedicated_collisions
  density_review: pending
  border_contact_test: not_executed
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La surface de base et les volumes spéciaux sont séparés et restent soumis à des contacts mesurés.

### 58.8 Supposer que deux navmeshes superposés sont connectés

**Symptôme :** l’agent atteint la frontière mais refuse de passer dans la cellule voisine.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
navigation:
  cell_a: baked
  cell_b: baked
  meshes_overlap: true
  bidirectional_path_test: skipped
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le chevauchement visuel ne garantit pas des bords similaires ni une connexion dans la même carte.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
navigation_border_test: AST-WORLD-NAV-BORDER-001-v001
shared_edge_review: pending
map_assignment_review: pending
a_to_b: not_executed
b_to_a: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le contrat contrôle l’interface, la carte et deux requêtes après synchronisation.

### 58.9 Charger une cellule avec `load()` dans `_process()`

**Symptôme :** une frame se bloque lors du franchissement de frontière.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func _process(_delta: float) -> void:
    if needs_next_cell:
        var scene = load(next_cell_path)
        add_child(scene.instantiate())
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `load()` est synchrone et l’instanciation se produit dans la même frame sans état, erreur ni budget.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func request_next_cell(cell_id: StringName, path: String) -> Error:
    return request_cell(cell_id, path)

func _process(_delta: float) -> void:
    poll_pending_cells()
    activate_ready_cells_with_budget()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La demande, le sondage et l’activation sont séparés ; le contrôleur peut mesurer et étaler chaque phase.

### 58.10 Déclarer le streaming validé depuis l’éditeur

**Symptôme :** la région paraît fluide sur une courte visite, mais aucun rapport ne contient mémoire, temps ou démarrage froid.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
validation:
  editor_viewport: looks_smooth
  packaged_build: not_tested
  cold_load: not_measured
  memory_peak: not_measured
  border_matrix: not_executed
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une impression dans l’éditeur ne qualifie ni le build, ni les caches, ni les pics, ni les frontières.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
benchmark_scene: AST-WORLD-BENCH-DELTA-001-v001
packaged_build: pending
cold_and_warm_runs: pending
memory_peak: pending
load_phases: pending
border_matrix: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction exige une scène, plusieurs états de cache, des unités et une campagne de frontières avant décision.

## 59. Livrables à conserver

Le plan maître exige cinq livrables permanents, versionnés et séparés des caches :

1. **terrain pilote** — sources de hauteur, relief, routes, eau, collisions et provenance ;
2. **découpage spatial** — repère, régions, secteurs, cellules, tuiles, voisins et interfaces ;
3. **profils de streaming** — états, préchargement, hystérésis, épinglage, activation et retrait ;
4. **matériaux de terrain** — identifiants, masques, bordures et liaisons futures au chapitre 16 ;
5. **scène de benchmark** — parcours, environnement, répétitions, mesures, captures et rapports.

> **[LECTURE] Manifeste de livraison — Ne pas saisir.**

```yaml
deliverable_manifest: AST-WORLD-DELIVERY-DELTA-001-v001
pilot_terrain:
  profile: AST-WORLD-REGION-DELTA-001
  status: blocked
spatial_partition:
  profile: AST-WORLD-PARTITION-001-v001
  status: blocked
streaming_profiles:
  profile: AST-WORLD-PRELOAD-001-v001
  status: blocked
terrain_materials:
  profile: AST-WORLD-MATERIAL-DELTA-001-v001
  status: blocked
benchmark_scene:
  profile: AST-WORLD-BENCH-DELTA-001-v001
  status: blocked
provenance_review: pending
publication_decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifeste :** les cinq entrées correspondent exactement au plan maître.

- **Profils :** chaque livrable possède une identité versionnée.

- **Provenance :** sources et droits restent une porte séparée.

- **Décision :** aucun asset ou benchmark n’est annoncé comme produit.

## 60. Synthèse opérationnelle pour Project Asteria

Le chapitre 14 fournit à `Project Asteria` un contrat complet pour produire une région traversable et chargeable. La région Delta est organisée par une échelle métrique, un repère, une hiérarchie région-secteur-cellule-tuile, des identifiants stables, une heightmap haute précision, un sculpt par niveaux, une érosion contrôlée, des bordures partagées, des corridors de route, un profil de rivière, un plan d’eau, des pads architecturaux, des masques matériels, des collisions, des régions de navigation, des scènes de cellule, des manifestes, un contrôleur de chargement en arrière-plan, une hystérésis, des épingles, des LOD, des HLOD et une scène de benchmark.

La région reste bloquée tant que les sources Blender, heightmaps, maillages, GLB, collisions, navmeshes, scènes, manifestes, matériaux, routes, eau, LOD, HLOD, captures et mesures ne sont pas réellement produits. Le chapitre prépare les surfaces de végétation du chapitre 15 et les matériaux du chapitre 16, mais ne crée ni espèces, ni distributions écologiques, ni pipeline PBR transversal, ni état gameplay autoritaire.

## 61. Références techniques officielles

Les références suivantes encadrent la matérialisation et doivent être requalifiées si les versions changent :

- [Godot 4.7 — Large world coordinates](https://docs.godotengine.org/en/4.7/tutorials/physics/large_world_coordinates.html) ;
- [Godot 4.7 — Background loading](https://docs.godotengine.org/en/4.7/tutorials/io/background_loading.html) ;
- [Godot 4.7 — ResourceLoader](https://docs.godotengine.org/en/4.7/classes/class_resourceloader.html) ;
- [Godot 4.7 — HeightMapShape3D](https://docs.godotengine.org/en/4.7/classes/class_heightmapshape3d.html) ;
- [Godot 4.7 — NavigationRegion3D](https://docs.godotengine.org/en/4.7/classes/class_navigationregion3d.html) ;
- [Godot 4.7 — GeometryInstance3D](https://docs.godotengine.org/en/4.7/classes/class_geometryinstance3d.html) ;
- [Godot 4.7 — Visibility ranges](https://docs.godotengine.org/en/4.7/tutorials/3d/visibility_ranges.html) ;
- [Godot 4.7 — Mesh level of detail](https://docs.godotengine.org/en/4.7/tutorials/3d/mesh_lod.html) ;
- [Godot 4.7 — Occlusion culling](https://docs.godotengine.org/en/4.7/tutorials/3d/occlusion_culling.html) ;
- [Blender Manual — Displace Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/displace.html) ;
- [Blender Manual — Sculpting](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/index.html) ;
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html).
