---
title: "Livre III — Chapitre 13 : Architecture, bâtiments et kits modulaires"
id: "DOC-L3-CH13"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 13
last-verified: "2026-07-23T14:35:47+02:00"
audit-status: "complete"
audit-date: "2026-07-23T14:35:47+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-13.md"
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

# Architecture, bâtiments et kits modulaires

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH13`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11
## 1. Rôle du chapitre
Le chapitre 12 a défini les objets individuels, leurs pivots, sockets, collisions et représentations. Le présent
chapitre change d’échelle : il organise des pièces architecturales réutilisables pour construire plusieurs bâtiments
cohérents sans recopier un bâtiment complet. Il traite les murs, sols, plafonds, toits, ouvertures, coins, jonctions,
escaliers, façades, intérieurs et pièces de transition comme une bibliothèque de modules mesurés.
Le fil rouge utilise le kit pilote `AST-ARCH-KIT-WAYSTATION-001` de `Project Asteria`. Ce kit doit permettre
d’assembler au moins une halte de route, un petit entrepôt et une tour de guet basse à partir des mêmes conventions.
Cette variété oblige à tester la grille, les connecteurs, les pivots, les tolérances, les collisions, la navigation,
l’occlusion, la lumière, les matériaux partagés, les variantes et les LOD sans confondre asset architectural et
système de construction du joueur.
> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**
```text
Besoin d'environnement et plans d'usage
    ↓
Métriques humaines et grille canonique
    ↓
Catalogue de modules et contrats de connexion
    ↓
Blockout de plusieurs bâtiments
    ↓
Coins, ouvertures, transitions et intérieurs
    ↓
Pivots, snapping et tolérances
    ↓
Géométrie, collisions, navigation et occlusion
    ↓
Matériaux partagés, variantes et rupture de répétition
    ↓
Export GLB, scènes dérivées et bibliothèque Godot
    ↓
LOD de module, HLOD de bâtiment et campagnes de mesure
    ↓
Porte d'acceptation du kit
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Dépendances :** le kit part de la bible visuelle, des conventions Blender et des objets du chapitre 12.
- **Ordre :** la métrique et les connecteurs sont fixés avant la géométrie détaillée.
- **Preuve :** plusieurs bâtiments doivent être assemblés pour démontrer la réutilisation réelle.
- **Frontière :** la construction par le joueur, les coûts et les permissions restent dans le Livre II.
## 2. Résultats d’apprentissage
- transformer un besoin d’environnement en grille métrique et catalogue de modules ;
- distinguer module, variante, connecteur, pivot, cellule, travée et bâtiment assemblé ;
- définir une grille principale et des sous-incréments sans multiplier les exceptions ;
- concevoir murs, sols, toits, ouvertures, coins, jonctions et transitions compatibles ;
- préparer intérieurs et façades sans produire deux systèmes contradictoires ;
- placer origines, pivots et repères de snapping de manière stable ;
- contrôler les tolérances, les chevauchements et les fuites de lumière ;
- séparer maillage de rendu, collision, géométrie de navigation et occluder ;
- choisir entre scènes modulaires classiques, `GridMap` et assemblages hybrides ;
- préparer une `MeshLibrary` lorsque la régularité du kit la justifie ;
- documenter les limites de navigation entre régions et les joints de navmesh ;
- définir LOD de module et HLOD de bâtiment sans inventer de distances ;
- réduire la répétition par règles contrôlées plutôt que par transformations arbitraires ;
- écrire un validateur GDScript non destructif et comprendre ses types, paramètres, retours et opérateurs ;
- conserver des réserves explicites lorsque Blender, Godot ou le runtime n’ont pas été exécutés.
## 3. Niveau de preuve et réserves
Le chapitre est accepté au niveau `static-review`. Les contrats YAML et JSON, procédures Blender, hiérarchies Godot,
exemples de `GridMap`, profils de navigation, profils d’occlusion et scripts GDScript sont relus contre les
documentations officielles. Ils ne constituent pas une preuve d’exécution.
Aucun module architectural, aucun bâtiment, aucune collision, aucune navigation, aucun occluder, aucun matériau, aucun
atlas, aucun LOD, aucun HLOD, aucun GLB, aucune `MeshLibrary`, aucune scène Godot et aucune mesure runtime de `Project
Asteria` ne sont revendiqués comme produits. Les dimensions, tailles de cellule, tolérances, budgets, densités,
distances et seuils sont des valeurs candidates à confirmer.
La destruction est abordée uniquement comme préparation visuelle : joints, pièces remplaçables, états et proxies. Les
fractures, dégâts, réplications, coûts de réparation et décisions de destruction appartiennent aux systèmes runtime
concernés.
## 4. Périmètre et frontières
Le chapitre couvre :
- grille métrique, dimensions humaines, travées et sous-incréments ;
- catégories de modules et règles d’assemblage ;
- coins, jonctions, ouvertures, transitions, intérieurs et façades ;
- pivots, origines, connecteurs, snapping et tolérances ;
- blockout de plusieurs bâtiments avec le même kit ;
- collisions statiques, navigation et occlusion préparatoires ;
- matériaux partagés, variantes, trim sheets et atlas comme contrats, sans refaire le chapitre 16 ;
- LOD de module, HLOD de bâtiment et rupture de répétition ;
- export GLB, scènes Godot dérivées, `GridMap` optionnel et validation structurelle.
Le chapitre ne couvre pas :
- les objets individuels, prises et équipements du chapitre 12 ;
- les terrains, routes, rivières, tuiles de monde et streaming du chapitre 14 ;
- le pipeline PBR transversal du chapitre 16 ;
- la retopologie, les UV, le baking et la texel density génériques du chapitre 17 ;
- les rigs ou animations finales des chapitres 19 et 20 ;
- les VFX de destruction du chapitre 23 ;
- l’intégration globale et les importeurs du chapitre 28 ;
- les règles de construction, de chantier, de coût, de propriété ou de permissions du Livre II.
> **[LECTURE] Matrice des responsabilités — Ne pas saisir.**
```yaml
chapter_13:
  owns:
    - architectural_metric_and_grid_contract
    - modular_connection_rules
    - architectural_render_collision_nav_occlusion_profiles
    - module_and_building_lod_profiles
    - architectural_validation_scenes
  prepares:
    - chapter_14_terrain_connections
    - chapter_16_shared_material_pipeline
    - chapter_17_uv_and_baking
    - chapter_23_destruction_vfx
    - chapter_28_import_integration
  does_not_own:
    - individual_props
    - player_construction_rules
    - economy_or_inventory_costs
    - world_streaming
    - general_pbr_pipeline
    - authoritative_destruction
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Type :** chaque valeur est une chaîne qui nomme une responsabilité documentaire.
- **Préparation :** `prepares` fournit des interfaces futures sans exécuter les chapitres concernés.
- **Exclusion :** `does_not_own` empêche le kit visuel de devenir une seconde autorité gameplay.
- **Résultat attendu :** toute procédure du chapitre doit se rattacher à une responsabilité de `owns`.
## 5. Prérequis et outils à ouvrir
- une bible visuelle et un cahier des charges d’environnement ;
- les conventions Blender du chapitre 4 ;
- un registre de provenance du chapitre 5 ;
- des personnages de référence pour vérifier portes, escaliers, garde-corps et mobilier fixe ;
- les objets du chapitre 12 nécessaires aux tests d’échelle ;
- un profil provisoire de caméra et de déplacement ;
- des budgets provisoires par plateforme ;
- une liste de bâtiments réellement nécessaires au vertical slice.
- **[APP] Blender 5.2.0** pour la grille, les blockouts, modules, origines, connecteurs et exports ;
- **[APP] Godot 4.7.1-stable** pour les scènes dérivées, `GridMap`, collisions, navigation, occlusion et mesures ;
- **[VSC] Visual Studio Code** pour les contrats YAML/JSON et le validateur GDScript ;
- **[PS] PowerShell 7** pour créer les dossiers et lancer les contrôles documentaires ;
- **[WEB] navigateur** pour les documentations officielles et références dont les droits sont enregistrés.
> **[PS] Créer l’arborescence de travail.**
```powershell
$Root = "art/architecture/AST-ARCH-KIT-WAYSTATION-001"
$Paths = @(
    "$Root/briefs",
    "$Root/metrics",
    "$Root/modules",
    "$Root/connectors",
    "$Root/collisions",
    "$Root/navigation",
    "$Root/occlusion",
    "$Root/materials",
    "$Root/variants",
    "$Root/lod",
    "art/blender/architecture/AST-ARCH-KIT-WAYSTATION-001",
    "art/exports/architecture/AST-ARCH-KIT-WAYSTATION-001",
    "tests/art/architecture/reports",
    "tests/art/architecture/captures"
)
foreach ($Path in $Paths) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
}
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Entrées :** `$Root` est une chaîne et `$Paths` un tableau de chemins relatifs.
- **Boucle :** `foreach` traite chaque chemin sans dépendre de son existence préalable.
- **Paramètres :** `-ItemType Directory` crée un dossier, `-Force` rend l’opération idempotente.
- **Effet de bord :** les dossiers sont créés ; aucun module ni export n’est produit.
- **Résultat attendu :** sources Blender, contrats, exports, rapports et captures restent séparés.
> **[LECTURE] Arborescence canonique — Ne pas saisir.**
```text
art/
├── blender/architecture/
│   └── AST-ARCH-KIT-WAYSTATION-001/
├── architecture/
│   └── AST-ARCH-KIT-WAYSTATION-001/
│       ├── briefs/
│       ├── metrics/
│       ├── modules/
│       ├── connectors/
│       ├── collisions/
│       ├── navigation/
│       ├── occlusion/
│       ├── materials/
│       ├── variants/
│       └── lod/
├── exports/architecture/
├── provenance/
└── budgets/
tests/
└── art/architecture/
    ├── architecture_validation_lab.tscn
    ├── architecture_kit_validator.gd
    ├── reports/
    └── captures/
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Sources :** les `.blend` restent distincts des GLB et scènes Godot dérivées.
- **Contrats :** métriques, modules, connecteurs et proxies occupent des dossiers séparés.
- **Tests :** scène, script, rapports et captures sont regroupés sous `tests/art/architecture`.
- **Publication :** les preuves internes ne sont pas ajoutées au manuel lecteur.
## 6. Vocabulaire minimal
| Terme | Définition opérationnelle |
|---|---|
| Module | pièce réutilisable possédant dimensions, origine, connecteurs et responsabilités. |
| Cellule | volume élémentaire de la grille utilisé pour l’indexation ou le placement. |
| Travée | largeur architecturale répétable, souvent composée de plusieurs cellules. |
| Connecteur | contrat d’interface décrivant position, orientation et compatibilité. |
| Pivot | repère autour duquel une pièce est placée ou transformée. |
| Joint | zone de rencontre entre deux modules. |
| Tolérance | écart maximal candidat accepté avant apparition d’un défaut. |
| Variante | représentation compatible qui conserve les interfaces obligatoires. |
| LOD | représentation simplifiée d’un module ou d’un petit assemblage. |
| HLOD | représentation hiérarchique qui remplace plusieurs nœuds par un groupe simplifié. |
## 7. Kit pilote et bâtiments de preuve
Le kit pilote vise une architecture de pierre et bois à échelle humaine. Il ne cherche pas à couvrir une ville
entière. Il doit démontrer la réutilisation avec trois assemblages de preuve :
| Assemblage | Fonction visuelle | Contraintes révélées |
|---|---|---|
| Halte de route | petit bâtiment ouvert au public | porte, fenêtre, auvent, intérieur simple. |
| Entrepôt | volume plus long et répétitif | travées répétées, grande ouverture, toit continu. |
| Tour de guet basse | volume vertical compact | coins, escaliers, plancher supérieur, parapet. |
> **[LECTURE] Brief du kit pilote — Ne pas saisir.**
```yaml
kit_id: AST-ARCH-KIT-WAYSTATION-001
target_buildings:
  - AST-BLD-WAYSTATION-001
  - AST-BLD-STOREHOUSE-001
  - AST-BLD-WATCHTOWER-001
visual_language:
  structure: stone_and_timber
  climate: temperate_humid
  age_profile: maintained_with_local_repairs
required_module_families:
  - floors
  - walls
  - corners
  - openings
  - roofs
  - stairs
  - interior_transitions
proof_status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identités :** le kit et les trois bâtiments possèdent des identifiants distincts.
- **Langage visuel :** structure, climat et âge orientent la conception sans remplacer la bible.
- **Familles :** la liste définit le minimum nécessaire aux trois bâtiments.
- **Blocage :** aucun assemblage n’est déclaré construit.
## 8. Partir des usages, pas des façades
Avant de dessiner les modules, écrire les usages : circuler, entrer, monter, se couvrir, voir, stocker et éclairer.
Une façade séduisante ne prouve ni une porte utilisable, ni un escalier compatible, ni un intérieur assemblable.
> **[LECTURE] Matrice usage-espace-module — Ne pas saisir.**
```yaml
uses:
  enter_building:
    spatial_need: clear_doorway
    modules:
      - wall_door_single
      - threshold
  move_between_floors:
    spatial_need: stair_and_landing
    modules:
      - stair_straight
      - landing
      - floor_opening
  see_outside:
    spatial_need: window_and_reveal
    modules:
      - wall_window_small
      - interior_reveal
  store_large_crates:
    spatial_need: wide_opening
    modules:
      - wall_gate_double
      - reinforced_header
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Clés :** chaque usage devient une entrée stable liée à un besoin spatial.
- **Modules :** la liste matérialise les dépendances nécessaires à l’usage.
- **Frontière :** les permissions d’ouverture ou de stockage restent dans le gameplay.
- **Résultat attendu :** aucune famille de modules n’est créée sans besoin observable.
## 9. Références dimensionnelles et incertitudes
Les dimensions architecturales sont croisées entre plusieurs références : photos avec échelle connue, plans, relevés
fiables, normes accessibles et mesures internes au projet. Une photo perspective unique ne devient jamais une mesure
autoritaire.
> **[LECTURE] Registre dimensionnel — Ne pas saisir.**
```yaml
reference_set: AST-ARCH-REF-WAYSTATION-001-v001
measurements:
  human_height_reference_m:
    value: provisional
    sources:
      - AST-REF-HUMAN-001
  doorway_clear_width_m:
    value: provisional
    sources:
      - AST-REF-DOOR-PLAN-001
      - AST-REF-DOOR-PHOTO-002
  floor_to_floor_height_m:
    value: provisional
    sources:
      - AST-REF-SECTION-001
uncertainty_policy:
  single_photo_measurement: forbidden
  conflicting_sources: blocked
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Valeurs :** `provisional` empêche de confondre hypothèse et mesure validée.
- **Sources :** chaque dimension conserve plusieurs références lorsque possible.
- **Refus :** une photo isolée ne peut pas fixer une cote.
- **Décision :** un conflit de sources maintient le kit bloqué.
## 10. Grille principale, sous-grille et travées
Une grille modulaire doit être assez simple pour être appliquée sans calcul mental permanent. Le kit utilise une
cellule principale candidate et une sous-grille destinée aux détails compatibles. Les valeurs restent provisoires
jusqu’au blockout avec personnages, portes, escaliers et objets.
> **[LECTURE] Contrat de grille — Ne pas saisir.**
```yaml
grid_profile: AST-ARCH-GRID-001-v001
unit_system: metric
primary_cell_m:
  x: provisional
  y: provisional
  z: provisional
secondary_increment_m: provisional
bay_width_cells: provisional
vertical_levels:
  ground: 0
  floor_1: provisional
  roof_eave: provisional
absolute_grid_snap_required: true
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Système :** la grille est métrique et indépendante de l’affichage de l’éditeur.
- **Cellule :** les trois axes sont explicités car la hauteur peut suivre un rythme différent.
- **Sous-grille :** elle sert aux détails compatibles, pas à réparer chaque module.
- **Snapping :** le placement vise la grille absolue plutôt que des déplacements relatifs.
- **Réserve :** aucune dimension n’est présentée comme validée.
## 11. Dimensions humaines de contrôle
Le kit est contrôlé avec des gabarits simples : personnage debout, personnage accroupi, largeur d’épaules, dégagement
de main, rayon de virage candidat, objet porté et caméra. Ces gabarits ne deviennent pas la géométrie finale.
> **[LECTURE] Gabarits de contrôle — Ne pas saisir.**
```yaml
gauge_set: AST-ARCH-GAUGES-001-v001
gauges:
  human_standing: AST-GAUGE-HUMAN-STANDING-001
  human_crouched: AST-GAUGE-HUMAN-CROUCH-001
  carried_crate: AST-GAUGE-CRATE-001
  camera_third_person: AST-GAUGE-CAMERA-TP-001
  navigation_agent_candidate: AST-GAUGE-NAV-AGENT-001
checks:
  doorway_clearance: pending
  stair_headroom: pending
  corridor_turning: pending
  camera_clipping: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Références :** chaque gabarit possède une identité réutilisable.
- **Contrôles :** portes, escaliers, couloirs et caméra sont vérifiés séparément.
- **Navigation :** le profil d’agent reste candidat et ne remplace pas les paramètres du runtime.
- **État :** toutes les vérifications sont en attente.
## 12. Catalogue et identifiants des modules
Un module reçoit un identifiant stable, une famille, une version, des dimensions, des connecteurs et un statut. Le nom
affiché peut évoluer ; l’identifiant ne dépend ni du nom de l’objet Blender ni de sa position dans une scène.
> **[LECTURE] Entrée de catalogue — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-SOLID-A-001
version: 1
family: wall
variant_role: base
dimensions_cells: [1, 1, 1]
source_blend: art/blender/architecture/AST-ARCH-KIT-WAYSTATION-001/walls.blend
export_glb: art/exports/architecture/AST-ARCH-KIT-WAYSTATION-001/wall_solid_a.glb
connectors:
  - edge_left
  - edge_right
  - floor_bottom
  - ceiling_top
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identité :** `module_id` reste stable alors que la version augmente.
- **Dimensions :** `dimensions_cells` est un tableau ordonné selon le contrat de grille.
- **Chemins :** source Blender et export GLB sont séparés.
- **Connecteurs :** les interfaces obligatoires sont déclarées avant la géométrie finale.
## 13. Familles minimales de modules
Le kit pilote ne commence pas par une collection exhaustive. Il commence par les familles nécessaires aux trois
bâtiments de preuve. Chaque famille doit démontrer une fonction d’assemblage différente et posséder au moins un module
de base, un module de transition et un cas limite documenté.
| Famille | Modules pilotes | Question vérifiée |
|---|---|---|
| sols | dalle pleine, bord, ouverture verticale | la trame porte-t-elle murs et circulations ? |
| murs | plein, porte, fenêtre, demi-module | les ouvertures restent-elles alignées ? |
| coins | intérieur, extérieur, terminaison | les épaisseurs se rencontrent-elles sans surépaisseur ? |
| toitures | pan, rive, faîtage, angle | les pentes et débords se raccordent-ils ? |
| circulations | escalier, palier, garde-corps | les niveaux et dégagements restent-ils compatibles ? |
| façades | pilastre, bandeau, encadrement | la variation respecte-t-elle la grille ? |
> **[LECTURE] Couverture minimale du catalogue — Ne pas saisir.**
```yaml
kit_id: AST-ARCH-KIT-WAYSTATION-001
required_families:
  floor:
    minimum_roles: [field, edge, vertical_opening]
  wall:
    minimum_roles: [solid, door, window, half]
  corner:
    minimum_roles: [inside, outside, end_cap]
  roof:
    minimum_roles: [slope, eave, ridge, corner]
  circulation:
    minimum_roles: [stair, landing, railing]
proof_buildings:
  - AST-ARCH-BLD-WAYSTATION-001
  - AST-ARCH-BLD-STOREHOUSE-001
  - AST-ARCH-BLD-WATCHTOWER-LOW-001
coverage_review: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Dictionnaire :** `required_families` associe une famille à une liste de rôles minimaux.
- **Listes :** les valeurs entre crochets sont des chaînes, non des fichiers déjà produits.
- **Preuve :** les trois bâtiments doivent consommer le catalogue selon des combinaisons distinctes.
- **Blocage :** une famille absente ou non testée empêche l’acceptation du kit.
## 14. Connecteurs et règles d’assemblage
Un module ne s’assemble pas parce que ses sommets paraissent proches. Il expose des connecteurs nommés qui décrivent
une interface : position, orientation, type, compatibilités et tolérance. Deux connecteurs ne sont compatibles que si
leurs types, leurs plans de contact et leur orientation relative satisfont la règle du kit.
- **connecteur de bord** : raccord horizontal entre modules voisins ;
- **connecteur vertical** : empilement entre niveaux ;
- **connecteur d’ouverture** : interface porte, fenêtre, trappe ou passage ;
- **connecteur de toiture** : rive, faîtage, noue ou changement de pente ;
- **connecteur de terrain** : repère préparatoire pour le raccord au sol du chapitre 14 ;
- **terminaison** : interface explicitement fermée, qui ne demande aucun voisin.
> **[LECTURE] Contrat de connecteur — Ne pas saisir.**
```yaml
connector_id: edge_right
connector_type: wall_edge
local_transform:
  position_cells: [1, 0, 0]
  rotation_deg: [0, 90, 0]
  scale: [1, 1, 1]
interface_plane: yz
polarity: neutral
compatible_with:
  - wall_edge
  - wall_corner_entry
tolerance_profile: AST-ARCH-TOLERANCE-001-v001
termination_allowed: false
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Transformation :** la position est exprimée en cellules afin de rester liée au contrat de grille.
- **Orientation :** `rotation_deg` rend le plan d’interface contrôlable après import.
- **Compatibilité :** la liste ferme les raccords autorisés au lieu de les déduire d’un nom visuel.
- **Tolérance :** le profil est référencé et versionné séparément.
- **Invariant :** le connecteur conserve une échelle uniforme.
## 15. Tolérances, joints et étanchéité visuelle
Une tolérance n’est pas un espace libre ajouté au hasard. Elle encadre les écarts numériques et visuels acceptables
entre deux modules. Le kit distingue la tolérance géométrique, le recouvrement visuel volontaire et le joint de
matériau. Les trois ne doivent pas se compenser silencieusement.
- les plans de raccord principaux doivent être exprimés dans le même espace local ;
- les extrémités destinées à se toucher partagent une cote nominale ;
- un recouvrement décoratif est déclaré comme tel et ne masque pas une grille incohérente ;
- les coins possèdent des règles propres pour éviter doubles épaisseurs ou jours ;
- les seuils, plinthes et bandeaux ne réparent pas une collision mal alignée ;
- la tolérance finale est vérifiée après export et instanciation répétée.
> **[LECTURE] Profil de tolérances — Ne pas saisir.**
```yaml
tolerance_profile: AST-ARCH-TOLERANCE-001-v001
geometric_gap_m: provisional
visual_overlap_m: provisional
angular_deviation_deg: provisional
rules:
  wall_to_wall: flush
  floor_to_wall: seated
  roof_to_wall: declared_overhang
  corner_inside: no_double_thickness
  corner_outside: controlled_cap
verification:
  two_module_pair: pending
  ten_module_chain: pending
  exported_scene: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Valeurs :** les trois seuils restent provisoires tant que les chaînes de modules ne sont pas mesurées.
- **Règles :** chaque liaison possède une intention différente plutôt qu’un écart universel.
- **Propagation :** la chaîne de dix modules révèle les erreurs cumulatives invisibles sur une paire.
- **Preuve moteur :** le contrôle après export détecte les transformations ou arrondis introduits par l’échange.
## 16. Origines, pivots et points de snapping
L’origine d’un module sert au placement canonique. Elle se trouve sur une interface ou un point de grille stable,
jamais au centre par habitude. Les points secondaires sont des objets vides dans Blender ou des `Marker3D` dans une
scène dérivée. Ils ne remplacent pas l’origine ; ils décrivent des raccords ou des repères de contrôle
supplémentaires.
> **[LECTURE] Hiérarchie Blender d’un mur avec porte — Ne pas saisir.**
```text
AST-ARCH-WALL-DOOR-A-001
├── GEO_wall_door_a
├── SOCKET_edge_left
├── SOCKET_edge_right
├── SOCKET_floor_bottom
├── SOCKET_ceiling_top
├── SOCKET_door_leaf
├── GUIDE_door_clearance
├── COLLISION_wall_left
├── COLLISION_wall_right
├── COLLISION_lintel
└── META_architecture_module
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Géométrie :** le maillage de rendu est séparé des repères et des collisions.
- **Interfaces :** les quatre sockets structuraux décrivent le placement dans la grille.
- **Ouverture :** `SOCKET_door_leaf` prépare un futur vantail sans définir sa logique.
- **Guide :** le volume de dégagement reste exclu de l’export final s’il sert uniquement à la fabrication.
- **Métadonnée :** l’identité du module est contrôlable sans dépendre du nom du fichier.
> **[LECTURE] Convention de pivot — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-DOOR-A-001
origin_role: lower_left_grid_interface
origin_cells: [0, 0, 0]
forward_axis: local_negative_y
up_axis: local_z
snap_points:
  edge_left: [0, 0, 0]
  edge_right: [1, 0, 0]
  floor_bottom: [0, 0, 0]
  ceiling_top: [0, 0, 1]
transform_policy:
  scale: uniform_only
  mirror: explicit_variant_only
  arbitrary_rotation: forbidden
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Origine :** le coin inférieur gauche fournit un repère reproductible pour les chaînes de murs.
- **Axes :** avant et haut sont documentés avant l’export.
- **Points :** les positions en cellules évitent de recopier des mètres dans chaque module.
- **Transformations :** le miroir et les rotations libres ne sont pas des corrections implicites.
## 17. Snapping dans Blender
Dans Blender, le blockout utilise les unités métriques, le snapping incrémental et la grille absolue lorsque le
placement doit retomber sur les coordonnées du kit. Un déplacement relatif peut conserver un décalage initial ;
l’alignement absolu ramène le repère choisi sur la grille. Le lecteur vérifie toujours la transformation numérique
dans le panneau latéral au lieu de se fier uniquement au dessin de la grille.
> **[LECTURE] Profil de snapping Blender — Ne pas saisir.**
```yaml
blender_snap_profile: AST-ARCH-BLENDER-SNAP-001-v001
unit_system: METRIC
unit_scale: 1.0
transform_orientation: GLOBAL
snap_element: INCREMENT
absolute_grid_snap: true
primary_increment_m: provisional
secondary_increment_m: provisional
rotation_steps_deg:
  structural: 90
  roof_candidate: provisional
scale_policy: applied_and_uniform
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Unités :** `unit_scale` reste à `1.0` et ne corrige pas une géométrie mal dimensionnée.
- **Orientation :** le repère global protège la cohérence de la grille structurelle.
- **Incrément :** les pas sont candidats tant que le blockout n’est pas approuvé.
- **Rotation :** les rotations structurelles sont discrètes ; les pentes de toiture sont qualifiées séparément.
- **Échelle :** les instances restent uniformes et les transformations sont contrôlées avant export.
## 18. Porte de blockout à trois bâtiments
Avant toute finition, les modules bruts doivent construire les trois bâtiments pilotes. Le test cherche les trous, les
doubles épaisseurs, les raccords impossibles, les modules manquants, les circulations bloquées et les répétitions
visuelles évidentes. Une pièce décorative ne peut pas compenser une famille structurelle absente.
| Bâtiment | Combinaisons obligatoires | Risque principal |
|---|---|---|
| maison-relais | intérieur, façade, porte, fenêtres, toiture simple | caméra et circulation intérieure |
| entrepôt | grande travée, peu d’ouvertures, longue chaîne de murs | dérive cumulative et monotonie |
| tour basse | empilement vertical, escalier, palier, toiture compacte | hauteurs et raccord vertical |
> **[LECTURE] Porte de blockout — Ne pas saisir.**
```yaml
gate_id: AST-ARCH-BLOCKOUT-GATE-001-v001
buildings:
  AST-ARCH-BLD-WAYSTATION-001:
    assembled: false
    missing_modules: unknown
    circulation_review: pending
  AST-ARCH-BLD-STOREHOUSE-001:
    assembled: false
    chain_drift_review: pending
  AST-ARCH-BLD-WATCHTOWER-LOW-001:
    assembled: false
    vertical_alignment_review: pending
acceptance:
  holes_visible: unknown
  overlaps_unplanned: unknown
  unique_modules_required: unknown
decision: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Booléens :** `assembled: false` déclare honnêtement que les scènes ne sont pas produites.
- **Inconnues :** `unknown` empêche une absence de mesure d’être interprétée comme un succès.
- **Critères :** les contrôles portent sur structure, circulation et couverture du catalogue.
- **Décision :** la finition est bloquée jusqu’à l’assemblage des trois preuves.
## 19. Famille de murs, ouvertures et linteaux
La famille de murs partage hauteur, épaisseur nominale, positions de connecteurs et rythme de travée. Une porte ou une
fenêtre n’est pas un trou découpé tardivement dans un mur final : elle est un module ou une composition prévue dont
les montants, le linteau, la collision et le raccord de matériau sont contrôlés.
- mur plein pour la cadence de base ;
- mur avec porte et zone de dégagement ;
- mur avec fenêtre et appui cohérent ;
- demi-module ou module de rattrapage autorisé ;
- terminaison de mur ;
- version intérieure lorsque les deux faces ne partagent pas le même besoin visuel.
> **[LECTURE] Contrat de la famille mur — Ne pas saisir.**
```yaml
family_id: AST-ARCH-WALL-FAMILY-A-001-v001
shared_dimensions:
  thickness_m: provisional
  level_height_m: provisional
  bay_width_m: provisional
modules:
  solid: AST-ARCH-WALL-SOLID-A-001
  door: AST-ARCH-WALL-DOOR-A-001
  window: AST-ARCH-WALL-WINDOW-A-001
  half: AST-ARCH-WALL-HALF-A-001
  end_cap: AST-ARCH-WALL-END-A-001
shared_connectors:
  - edge_left
  - edge_right
  - floor_bottom
  - ceiling_top
opening_clearance_review: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Dimensions partagées :** les membres de la famille réutilisent un seul contrat.
- **Modules :** les rôles fonctionnels pointent vers des identifiants stables.
- **Connecteurs :** une ouverture ne change pas l’interface structurelle externe.
- **Dégagement :** portes et fenêtres restent bloquées tant que personnages, caméra et collision ne sont pas testés.
## 20. Coins, jonctions et transitions
Les coins concentrent les erreurs d’épaisseur, de matériau et de collision. Le kit choisit une stratégie explicite :
coin dédié, mur maître avec retour, pilier de jonction ou combinaison limitée. Il ne mélange pas ces stratégies selon
la convenance de chaque bâtiment.
| Cas | Solution candidate | Contrôle |
|---|---|---|
| coin extérieur | module dédié ou cap contrôlé | silhouette, épaisseur, collision |
| coin intérieur | module dédié sans double paroi | espace utile et joint de matériau |
| jonction en T | module de jonction | ordre des faces et navigation |
| fin de mur | terminaison | absence d’interface ouverte |
| changement de hauteur | transition versionnée | raccord de toit et façade |
> **[LECTURE] Matrice de jonctions — Ne pas saisir.**
```yaml
junction_profile: AST-ARCH-JUNCTIONS-A-001-v001
strategies:
  outside_corner: dedicated_module
  inside_corner: dedicated_module
  t_junction: junction_module
  wall_end: end_cap
  height_transition: explicit_transition
forbidden:
  - arbitrary_wall_overlap
  - hidden_gap_with_decoration
  - non_uniform_scale_patch
pair_tests: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Stratégies :** chaque cas possède un propriétaire géométrique clair.
- **Interdictions :** les réparations visuelles qui cassent collision ou grille sont refusées.
- **Tests :** `pair_tests` exige une scène de comparaison pour chaque liaison.
- **Résultat attendu :** les bâtiments utilisent les mêmes règles de coin.
## 21. Sols, plafonds et ouvertures verticales
Les sols portent la grille horizontale et la relation entre niveaux. Le kit sépare dalle pleine, bord, trémie
d’escalier, ouverture technique et plafond visible. Une ouverture verticale est dimensionnée avec l’escalier, le
garde-corps, la caméra et la navigation ; elle ne résulte pas d’une suppression arbitraire de faces.
> **[LECTURE] Profil de dalle — Ne pas saisir.**
```yaml
family_id: AST-ARCH-FLOOR-FAMILY-A-001-v001
modules:
  field: AST-ARCH-FLOOR-FIELD-A-001
  edge: AST-ARCH-FLOOR-EDGE-A-001
  stair_opening: AST-ARCH-FLOOR-OPEN-STAIR-A-001
  service_opening: AST-ARCH-FLOOR-OPEN-SERVICE-A-001
  ceiling_visible: AST-ARCH-CEILING-A-001
level_contract: AST-ARCH-LEVELS-001-v001
checks:
  underside_visibility: pending
  stair_clearance: pending
  camera_clearance: pending
  navigation_boundary: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Famille :** sol, bord, ouvertures et plafond restent reliés mais distincts.
- **Niveaux :** le contrat vertical évite les hauteurs spécifiques à un bâtiment.
- **Visibilité :** le dessous doit être traité lorsque le joueur peut le voir.
- **Navigation :** la trémie doit découper la surface praticable au lieu d’être masquée visuellement.
## 22. Escaliers, paliers et garde-corps
Un escalier modulaire doit joindre exactement deux niveaux du contrat. Ses marches, sa pente, son palier et son volume
libre sont contrôlés avec le gabarit humain et le profil de navigation candidat. Le chapitre documente la géométrie et
les proxies ; il ne définit pas le contrôleur de déplacement du joueur.
> **[LECTURE] Contrat d’escalier — Ne pas saisir.**
```yaml
module_id: AST-ARCH-STAIR-STRAIGHT-A-001
connects_levels:
  from: 0
  to: 1
run_cells: provisional
rise_m: provisional
step_count: provisional
landing_modules:
  start: AST-ARCH-LANDING-A-001
  end: AST-ARCH-LANDING-A-001
clearance:
  headroom: pending
  carried_object: pending
  camera: pending
navigation:
  profile: AST-NAV-AGENT-001-v001
  bake_review: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Niveaux :** l’escalier se lie au contrat vertical plutôt qu’à une hauteur dessinée localement.
- **Dimensions :** course, hauteur et nombre de marches restent provisoires.
- **Dégagements :** personnage, objet porté et caméra sont trois contrôles distincts.
- **Navigation :** le profil est préparé sans annoncer de navmesh généré.
- **Frontière :** la vitesse et le comportement de montée restent hors du chapitre.
## 23. Toitures, rives et changements de pente
La toiture est une famille modulaire complète, pas un dernier couvercle. Le kit prévoit pans, rives, égouts, faîtages,
angles et raccords aux murs. Les débords, épaisseurs et pentes doivent se rencontrer selon des connecteurs dédiés. Les
formes exceptionnelles sont limitées et versionnées.
> **[LECTURE] Profil de toiture — Ne pas saisir.**
```yaml
family_id: AST-ARCH-ROOF-FAMILY-A-001-v001
pitch_profile: AST-ARCH-ROOF-PITCH-A-001-v001
modules:
  slope: AST-ARCH-ROOF-SLOPE-A-001
  eave: AST-ARCH-ROOF-EAVE-A-001
  ridge: AST-ARCH-ROOF-RIDGE-A-001
  gable_end: AST-ARCH-ROOF-GABLE-A-001
  outside_corner: AST-ARCH-ROOF-CORNER-OUT-A-001
  inside_valley: AST-ARCH-ROOF-VALLEY-A-001
overhang_m: provisional
weathering_direction: documented_not_authored
terrain_or_weather_simulation: excluded
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Pente :** un profil partagé évite des angles presque identiques et incompatibles.
- **Modules :** les raccords difficiles sont des entrées explicites du catalogue.
- **Débord :** la cote reste à confirmer avec la façade et la caméra.
- **Usure :** la direction peut être documentée, mais le pipeline de matériaux détaillé appartient au chapitre 16.
- **Frontière :** aucune simulation climatique ou de terrain n’est ajoutée.
## 24. Intérieurs et façades
Le kit doit soutenir des intérieurs jouables et des façades lisibles. Les deux faces d’un mur peuvent partager une
base structurelle tout en ayant des traitements visuels différents. Un intérieur ne doit pas être une coque externe
retournée : épaisseurs, embrasures, plinthes, plafonds, jonctions et visibilité depuis les ouvertures sont contrôlés.
> **[LECTURE] Profil intérieur-façade — Ne pas saisir.**
```yaml
profile_id: AST-ARCH-SURFACE-ZONES-A-001-v001
structural_module: AST-ARCH-WALL-WINDOW-A-001
surface_zones:
  exterior_field: material_slot_exterior
  interior_field: material_slot_interior
  opening_reveal: material_slot_reveal
  trim: material_slot_trim
visibility_tests:
  outside_to_inside: pending
  inside_to_outside: pending
  close_camera: pending
material_pipeline_owner: chapter_16
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Zones :** les surfaces sont nommées par fonction plutôt que par matériau définitif.
- **Ouverture :** l’embrasure reçoit un traitement propre et ne laisse pas apparaître une tranche brute.
- **Vues :** les deux sens de visibilité et la caméra proche sont testés.
- **Autorité :** le chapitre 16 reste propriétaire du pipeline PBR et des matériaux finaux.
## 25. Variantes et rupture de répétition
La variété vient d’abord des combinaisons de modules, puis de variantes contrôlées. Le kit protège les dimensions,
connecteurs, collisions et surfaces de raccord. Les variations décoratives ne déplacent pas les interfaces et ne
créent pas une nouvelle règle d’assemblage cachée.
- variantes de finition ou d’usure liées aux zones de matériau ;
- encadrements, volets, auvents et enseignes comme modules secondaires ;
- panneaux de façade interchangeables ;
- petits décalages de détail autorisés seulement hors interfaces ;
- rotation ou miroir uniquement lorsqu’un profil explicite le permet ;
- composition asymétrique obtenue par choix de modules plutôt que par déformation libre.
> **[LECTURE] Famille de variantes — Ne pas saisir.**
```yaml
variant_family: AST-ARCH-WALL-SOLID-A-VARIANTS-001-v001
base_module: AST-ARCH-WALL-SOLID-A-001
variants:
  - id: clean
    geometry_profile: base
    surface_profile: clean
  - id: patched
    geometry_profile: patch_overlay
    surface_profile: worn
  - id: timber_brace
    geometry_profile: brace_overlay
    surface_profile: clean
protected_invariants:
  - dimensions_cells
  - snap_points
  - structural_collision_profile
  - navigation_boundary
random_selection_owner: excluded
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Base :** les variantes réutilisent un module structurel commun.
- **Superpositions :** les ajouts décoratifs restent hors des plans de raccord.
- **Invariants :** dimensions, snapping, collision et navigation ne changent pas silencieusement.
- **Sélection :** le chapitre ne définit pas de tirage aléatoire runtime.
## 26. Matériaux partagés, atlas et frontière du pipeline PBR
Le kit architectural prépare des zones, des identifiants de matériaux et des règles de partage. Il ne refait pas le
cours PBR du chapitre 16. Les modules proches doivent éviter une multiplication arbitraire des matériaux ; les
surfaces répétitives peuvent utiliser des matériaux tilables, des trim sheets ou un atlas seulement après analyse de
la densité, des raccords et de la mémoire.
| Stratégie | Usage candidat | Risque à contrôler |
|---|---|---|
| matériau tilable | grandes surfaces répétitives | échelle et raccord visibles |
| trim sheet | bords, cadres, bandeaux | orientation et densité cohérentes |
| atlas | petits modules ou variantes | marges, mipmaps et mémoire |
| matériau unique par module | exception justifiée | draw calls et maintenance |
| overlay/decal | salissure ou réparation locale | surcoût et z-fighting |
> **[LECTURE] Contrat de zones matérielles — Ne pas saisir.**
```yaml
material_contract: AST-ARCH-MATERIAL-ZONES-001-v001
zones:
  structural_field:
    sharing: kit_wide
  trim:
    sharing: kit_wide
  roof:
    sharing: roof_family
  glass_candidate:
    sharing: opening_family
  variation_overlay:
    sharing: optional
strategies_under_review:
  - tiling
  - trim_sheet
  - atlas
material_count_budget: provisional
pbr_authority: chapter_16
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Zones :** les noms décrivent des fonctions de surface communes au kit.
- **Partage :** la portée évite de dupliquer un matériau pour chaque module.
- **Choix :** tiling, trim sheet et atlas restent des stratégies à mesurer.
- **Budget :** le nombre de matériaux n’est pas présenté comme une limite validée.
- **Frontière :** le chapitre 16 possède les cartes, espaces colorimétriques, compression et shaders finaux.
## 27. Topologie, normales et arêtes de raccord
La topologie doit soutenir la silhouette, l’ombrage et les interfaces. Un bord de snapping reste géométriquement
simple, aligné et protégé contre les modifications décoratives. Les normales, arêtes dures et éventuels bevels sont
qualifiés pour ne pas créer de couture lumineuse entre deux modules partageant pourtant le même plan.
- conserver les plans de raccord propres et sans vertices flottants ;
- éviter les bevels qui déplacent la cote nominale de l’interface ;
- séparer les arêtes visibles des plans cachés de jonction ;
- tester l’ombrage sous lumière rasante et avec plusieurs rotations autorisées ;
- documenter toute dépendance à des normales personnalisées ;
- réserver retopologie, UV et baking génériques au chapitre 17.
> **[LECTURE] Contrat d’arêtes de raccord — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-SOLID-A-001
interface_edges:
  edge_left:
    plane: x_zero
    bevel_crossing: forbidden
    decorative_vertices: forbidden
  edge_right:
    plane: x_max
    bevel_crossing: forbidden
    decorative_vertices: forbidden
normal_policy:
  interface_consistency: required
  custom_normals: candidate
lighting_tests:
  neutral: pending
  grazing: pending
  repeated_chain: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Plans :** les interfaces sont définies par des plans contrôlables.
- **Bevel :** une arête décorative ne peut pas modifier la cote de raccord.
- **Normales :** la stratégie reste candidate tant qu’elle n’est pas testée après export.
- **Lumières :** la chaîne répétée révèle les coutures d’ombrage entre modules.
## 28. Collisions architecturales
La collision architecturale suit l’usage de l’espace, pas le détail du rendu. Les murs, sols, escaliers et garde-corps
utilisent des proxies dédiés. Une collision concave peut convenir à une géométrie statique qualifiée, tandis que les
éléments mobiles ou destructibles candidats doivent employer des formes adaptées à leur futur corps physique. Le
chapitre ne crée aucune règle de destruction ou de dégâts.
| Élément | Proxy candidat | Contrôle |
|---|---|---|
| mur plein | boîte ou coque statique simple | épaisseur et absence de fuite |
| mur avec ouverture | plusieurs boîtes | passage libre et linteau |
| sol | boîte mince ou surface statique qualifiée | continuité et hauteur |
| escalier | rampe simplifiée ou marches selon contrôleur | contact et navigation |
| garde-corps | boîtes/capsules simples | blocage sans détails inutiles |
| toiture accessible | proxy dédié | pente et bords |
> **[LECTURE] Profil de collision architecturale — Ne pas saisir.**
```yaml
collision_profile: AST-ARCH-COLLISION-A-001-v001
module_id: AST-ARCH-WALL-DOOR-A-001
body_role: static_architecture
shapes:
  - id: wall_left
    type: BoxShape3D
  - id: wall_right
    type: BoxShape3D
  - id: lintel
    type: BoxShape3D
render_mesh_collision:
  generated_for_diagnostic: allowed
  promotion_to_final: forbidden
non_uniform_scale: forbidden
construction_or_damage_rules: excluded
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** `static_architecture` décrit le contexte sans imposer une scène runtime finale.
- **Formes :** trois boîtes préservent l’ouverture de porte.
- **Diagnostic :** une collision générée depuis le rendu peut aider à comparer, jamais être promue automatiquement.
- **Échelle :** les dimensions se règlent dans les ressources de forme.
- **Frontière :** construction, dégâts et destruction restent hors du contrat visuel.
## 29. Géométrie de navigation et raccords
La navigation est préparée par une géométrie propre et des contrats de raccord. Deux régions qui se chevauchent
visuellement ne sont pas nécessairement connectées : leurs bords doivent être compatibles avec le processus de
génération et la carte de navigation. Les portes, escaliers, trémies et changements de niveau sont donc testés comme
interfaces de navigation, pas seulement comme ouvertures de rendu.
- séparer géométrie visuelle et géométrie source du navmesh ;
- documenter le profil d’agent candidat et les marges associées ;
- conserver des bords partagés ou suffisamment proches selon la configuration qualifiée ;
- exclure obstacles décoratifs non pertinents de la source de navigation ;
- vérifier les portes ouvertes, les paliers, les escaliers et les coins intérieurs ;
- attendre la synchronisation du serveur de navigation avant de conclure sur une requête runtime.
> **[LECTURE] Contrat de navigation du kit — Ne pas saisir.**
```yaml
navigation_profile: AST-ARCH-NAV-A-001-v001
agent_profile: AST-NAV-AGENT-001-v001
source_geometry:
  include:
    - floors
    - stairs
    - landings
  exclude:
    - decorative_overlays
    - visual_roof_details
interfaces:
  doorway:
    shared_edge_review: pending
  stair_to_floor:
    elevation_review: pending
  room_to_corridor:
    connectivity_review: pending
navigation_layers: provisional
bake_owner: godot_validation_scene
runtime_queries_executed: false
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** les surfaces praticables sont sélectionnées séparément du rendu.
- **Interfaces :** chaque transition reçoit un contrôle de bord ou d’altitude.
- **Couches :** les valeurs restent provisoires et ne sont pas codées en nombres arbitraires.
- **Exécution :** `false` empêche de revendiquer un bake ou une requête réelle.
- **Autorité :** la scène de validation produit la preuve, pas le manifeste seul.
## 30. Occlusion et proxies d’occluders
L’occlusion culling peut réduire le rendu de géométries masquées, mais ses occluders doivent être simples, stables et
représentatifs des grands volumes. Un mur ou un bâtiment statique peut recevoir un proxy ; une porte mobile, un petit
ornement ou un maillage très détaillé n’est pas automatiquement un bon occluder. Les gains et le coût sont mesurés
dans la scène, jamais déduits du nombre de polygones.
> **[LECTURE] Profil d’occlusion — Ne pas saisir.**
```yaml
occlusion_profile: AST-ARCH-OCCLUSION-A-001-v001
building_role: static_shell
occluders:
  exterior_walls:
    type: BoxOccluder3D
    complexity: simple
  roof_mass:
    type: BoxOccluder3D
    complexity: simple
excluded:
  - doors_moving
  - window_frames
  - decorative_trim
  - small_props
bake_or_runtime_update: pending_qualification
performance_measurement: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Volumes :** les grandes masses utilisent des formes simples plutôt que le maillage de rendu.
- **Exclusions :** les éléments mobiles ou petits ne deviennent pas des occluders par défaut.
- **Mise à jour :** le choix entre bake et recalcul doit être qualifié pour la scène réelle.
- **Mesure :** aucun gain de performance n’est inventé.
## 31. Préparation visuelle de la destruction
Le plan maître demande de préparer la destruction, mais le chapitre ne définit ni santé du bâtiment, ni dégâts, ni
physique de ruine autoritaire. Il prépare seulement des frontières visuelles possibles : panneaux séparables, états
endommagés, points de rupture artistiques, proxies de débris et surfaces intérieures à révéler.
> **[LECTURE] Profil de préparation à la destruction — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-SOLID-A-001
destruction_visual_preparation:
  intact_representation: wall_solid_a
  damaged_candidate: wall_solid_a_damaged
  breach_candidate: wall_solid_a_breach
  reveal_surfaces:
    - inner_structure
    - broken_edge
  debris_proxy_profile: AST-ARCH-DEBRIS-WALL-A-001-v001
state_selection_owner: Livre_II_domain_construction
physics_fracture: excluded
damage_values: excluded
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Représentations :** les états candidats restent des assets visuels séparés.
- **Surfaces :** les faces révélées sont prévues afin d’éviter des trous non texturés.
- **Autorité :** le système de domaine du Livre II choisira éventuellement l’état.
- **Exclusions :** fracture physique et valeurs de dégâts ne sont pas enseignées ici.
## 32. Collection d’export et livraison GLB
Le fichier Blender conserve références, guides, variantes de travail et modules refusés. La collection `__EXPORT`
contient uniquement les modules, repères et métadonnées destinés à l’échange. Un GLB peut regrouper une famille ou un
module selon la stratégie mesurée ; le choix est enregistré et reproductible.
> **[LECTURE] Frontière d’export du kit — Ne pas saisir.**
```text
SCENE_ARCH_KIT_WAYSTATION
├── __REFERENCE
├── __GUIDES
├── __WORK
├── __COLLISION_SOURCE
└── __EXPORT
    ├── AST-ARCH-WALL-SOLID-A-001
    ├── AST-ARCH-WALL-DOOR-A-001
    ├── AST-ARCH-CORNER-OUT-A-001
    ├── AST-ARCH-FLOOR-FIELD-A-001
    ├── AST-ARCH-STAIR-STRAIGHT-A-001
    └── AST-ARCH-ROOF-SLOPE-A-001
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Séparation :** références, guides, travail et sources de collision restent hors de la frontière.
- **Sélection :** l’export utilise une collection stable plutôt qu’une sélection manuelle occasionnelle.
- **Modules :** chaque racine porte son identité et ses repères.
- **Réserve :** la liste ne prétend pas que les maillages existent.
> **[LECTURE] Manifeste d’export — Ne pas saisir.**
```yaml
export_manifest: AST-ARCH-EXPORT-001-v001
source_blend: art/blender/architecture/AST-ARCH-KIT-WAYSTATION-001/kit_master.blend
source_collection: __EXPORT
format: glTF_2_0
container: GLB
strategy: family_or_module_pending_measurement
apply_modifiers: qualified_per_module
custom_properties: enabled
export_path: art/exports/architecture/AST-ARCH-KIT-WAYSTATION-001/
source_sha256: pending
export_sha256: pending
blender_execution: false
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** le `.blend`, la collection et le chemin d’export sont explicites.
- **Stratégie :** regroupement par famille ou module reste à mesurer dans Godot.
- **Propriétés :** les identifiants et contrats peuvent traverser comme métadonnées qualifiées.
- **Empreintes :** source et export auront des hachages distincts.
- **Exécution :** `false` maintient la réserve sur Blender et le GLB.
## 33. Scène importée et scène Godot dérivée
Godot importe le GLB comme source générée. Le projet crée ensuite une scène dérivée ou une scène d’intégration qui
instancie cette source et ajoute collisions, navigation, occluders, LOD, métadonnées et scripts de validation.
Modifier directement la scène importée crée une divergence fragile au prochain réimport.
> **[LECTURE] Hiérarchie d’un module dérivé — Ne pas saisir.**
```text
WallDoorA
├── ImportedModule
│   └── AST-ARCH-WALL-DOOR-A-001
├── Collision
│   ├── StaticBody3D
│   └── CollisionShape3D
├── NavigationSource
│   └── MeshInstance3D
├── Occlusion
│   └── OccluderInstance3D
├── SnapPoints
│   ├── edge_left
│   ├── edge_right
│   ├── floor_bottom
│   └── ceiling_top
└── Metadata
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Import :** `ImportedModule` conserve la scène générée sans modification locale.
- **Proxies :** collision, navigation et occlusion possèdent des branches distinctes.
- **Snapping :** les repères peuvent être importés ou recréés à partir d’un contrat vérifié.
- **Métadonnées :** l’identité et la version restent accessibles au validateur.
- **Réimport :** la scène dérivée survit au remplacement du GLB.
> **[LECTURE] Profil de scène dérivée — Ne pas saisir.**
```yaml
scene_profile: AST-ARCH-GODOT-MODULE-001-v001
module_id: AST-ARCH-WALL-DOOR-A-001
imported_scene: res://art/architecture/imported/wall_door_a.glb
derived_scene: res://art/architecture/modules/wall_door_a.tscn
branches:
  collision: required
  navigation_source: required
  occlusion: optional
  snap_points: required
  lod: optional
imported_scene_editing: forbidden
godot_import_test: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Chemins :** source importée et scène possédée par le projet sont séparées.
- **Branches :** chaque responsabilité est déclarée comme obligatoire ou optionnelle.
- **Interdiction :** la scène générée ne devient pas une source éditée à la main.
- **Test :** l’import et le réimport restent à exécuter.
## 34. Choisir entre scènes modulaires, GridMap et approche hybride
Une bibliothèque de scènes modulaires est le chemin général : elle accepte des modules de tailles variées, des
hiérarchies riches et des compositions manuelles ou outillées. `GridMap` devient intéressant lorsque les cellules et
orientations sont régulières et qu’une `MeshLibrary` stable existe. Une approche hybride peut employer `GridMap` pour
les masses régulières et des scènes pour escaliers complexes, portes, toitures ou détails.
| Approche | Forces | Limites |
|---|---|---|
| scènes modulaires | souple, hiérarchies riches, contrôle explicite | placement plus outillé ou manuel |
| GridMap | édition cellulaire rapide, catalogue régulier | cellules, indices et orientations plus contraints |
| hybride | masse rapide et exceptions riches | deux contrats à maintenir et tester |
> **[LECTURE] Arbre de décision — Ne pas saisir.**
```yaml
placement_strategy:
  regular_cell_dimensions: unknown
  module_hierarchy_complexity: unknown
  arbitrary_sizes_required: unknown
  repeated_large_layouts: unknown
  rich_per_instance_logic: unknown
decision:
  modular_scenes: candidate
  gridmap: candidate_if_regular
  hybrid: candidate_if_boundaries_documented
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Questions :** les cinq entrées doivent être résolues par le kit réel.
- **Scènes :** elles restent candidates par défaut lorsque les tailles ou hiérarchies varient.
- **GridMap :** il est conditionné par une régularité démontrée.
- **Hybride :** les frontières entre les deux systèmes doivent être documentées.
- **Blocage :** aucune solution n’est prescrite sans preuve.
## 35. MeshLibrary et identité stable
Une `MeshLibrary` associe des items à des indices utilisés par `GridMap`. L’indice est une représentation technique,
pas l’identité canonique du module. Le projet conserve donc un mapping versionné entre `module_id`, indice de
bibliothèque et source. Réordonner la bibliothèque sans migration peut changer le sens de cellules existantes.
> **[LECTURE] Mapping MeshLibrary — Ne pas saisir.**
```yaml
mesh_library_profile: AST-ARCH-MESHLIB-A-001-v001
resource_path: res://art/architecture/grid/waystation_mesh_library.tres
items:
  AST-ARCH-WALL-SOLID-A-001:
    library_index: provisional
    source_scene: res://art/architecture/modules/wall_solid_a.tscn
  AST-ARCH-WALL-DOOR-A-001:
    library_index: provisional
    source_scene: res://art/architecture/modules/wall_door_a.tscn
  AST-ARCH-CORNER-OUT-A-001:
    library_index: provisional
    source_scene: res://art/architecture/modules/corner_out_a.tscn
index_is_identity: false
migration_required_on_reindex: true
generation_executed: false
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Ressource :** le chemin `.tres` appartient au projet et reste distinct des GLB.
- **Mapping :** les clés sont les identifiants stables ; les indices sont des valeurs techniques.
- **Migration :** un changement d’indice exige une procédure pour les cartes existantes.
- **Exécution :** aucune MeshLibrary n’est annoncée comme générée.
## 36. Profil GridMap
Si `GridMap` est retenu, la taille de cellule, le centrage, l’échelle des items, la taille des octants et la
navigation doivent correspondre au contrat du kit. `cell_scale` ne sert pas à réparer des modules de mauvaise taille.
Le bake de navigation intégré reste une option à qualifier par rapport aux scènes et régions de navigation du projet.
> **[LECTURE] Profil GridMap candidat — Ne pas saisir.**
```yaml
gridmap_profile: AST-ARCH-GRIDMAP-A-001-v001
mesh_library: AST-ARCH-MESHLIB-A-001-v001
cell_size:
  x: provisional
  y: provisional
  z: provisional
cell_center:
  x: false
  y: false
  z: false
cell_scale: 1.0
cell_octant_size: provisional
allowed_orientations_deg: [0, 90, 180, 270]
bake_navigation: candidate
navigation_map_assignment: pending
runtime_building_system: excluded
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Cellule :** les trois dimensions doivent correspondre à la grille architecturale.
- **Centrage :** des valeurs `false` sont candidates lorsque les origines sont sur les interfaces de cellule.
- **Échelle :** `1.0` interdit de masquer des dimensions incohérentes.
- **Octants :** la taille influence regroupement et coût et doit être mesurée.
- **Navigation :** bake et carte de navigation restent à tester.
- **Frontière :** le système de construction runtime du Livre II n’est pas implémenté.
## 37. LOD de module et HLOD de bâtiment
Le LOD de module simplifie un mur, une toiture ou un escalier. Le HLOD de bâtiment remplace un ensemble complet par
une représentation agrégée lorsque la distance et l’usage le permettent. Les deux décisions sont séparées : un
bâtiment encore visitable ne peut pas perdre ses intérieurs ou collisions simplement parce qu’il est loin de la caméra
actuelle.
- LOD de module : géométrie, matériaux, petits détails et éventuellement proxies ;
- HLOD de bâtiment : coque agrégée, matériaux fusionnés, intérieurs conditionnels ;
- collision : profil indépendant du rendu ;
- navigation : conservée ou désactivée selon la représentation réellement active ;
- occlusion : peut utiliser un proxy commun au bâtiment ;
- seuils : mesurés selon taille écran, caméra, vitesse et transition.
> **[LECTURE] Profil LOD et HLOD — Ne pas saisir.**
```yaml
lod_profile: AST-ARCH-LOD-WAYSTATION-001-v001
module_lod:
  lod0:
    geometry: full
    materials: provisional
  lod1:
    geometry: simplified
    materials: reduced
  lod2:
    geometry: silhouette_preserving
    materials: minimal
building_hlod:
  exterior_shell:
    representation: aggregated_shell
    interiors: excluded
    allowed_when:
      - not_enterable
      - no_active_interior_view
  enterable:
    representation: modular_or_near_hlod
    interiors: required
visibility_range_strategy: pending_measurement
fade_strategy: pending_measurement
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Niveaux :** le LOD de module et le HLOD du bâtiment sont deux structures distinctes.
- **Entrabilité :** la coque distante n’est autorisée que lorsqu’aucune vue intérieure n’est requise.
- **Visibilité :** les plages Godot restent à mesurer et ne sont pas copiées d’un autre projet.
- **Transition :** le mode de fondu est également soumis au coût et aux artefacts.
## 38. Laboratoire de validation architectural
Le laboratoire Godot assemble les trois bâtiments, une rue courte et des points de vue intérieurs et extérieurs. Il
contient des gabarits humains, une caméra mobile, des éclairages neutres et rasants, des visualisations de collision,
de navigation et d’occlusion, ainsi que des scénarios de LOD. Le chapitre décrit la scène sans la matérialiser.
> **[LECTURE] Hiérarchie du laboratoire — Ne pas saisir.**
```text
ArchitectureValidationLab
├── ReferenceGauges
│   ├── HumanStanding
│   ├── HumanCrouched
│   └── CameraClearance
├── Buildings
│   ├── Waystation
│   ├── Storehouse
│   └── WatchtowerLow
├── StreetContext
├── Navigation
│   └── NavigationRegion3D
├── Occlusion
│   └── OccluderInstance3D
├── Cameras
│   ├── ExteriorCamera
│   ├── InteriorCamera
│   └── TraversalCamera
├── Lighting
│   ├── Neutral
│   └── Grazing
├── Diagnostics
│   ├── GridOverlay
│   ├── ConnectorGizmos
│   └── CollisionDebug
└── ArchitectureKitValidator
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Bâtiments :** les trois preuves partagent le même catalogue.
- **Contexte :** la rue courte révèle façades, coins, entrées et raccords au sol.
- **Navigation :** une région dédiée fournit un endroit explicite pour générer et interroger le navmesh.
- **Occlusion :** les proxies sont inspectés indépendamment du rendu.
- **Caméras :** extérieur, intérieur et traversée couvrent des défauts différents.
- **Diagnostics :** grille, connecteurs et collisions restent visibles pendant la validation.
> **[LECTURE] Profil du laboratoire — Ne pas saisir.**
```yaml
lab_id: AST-ARCH-VALIDATION-LAB-001-v001
scene_path: res://tests/art/architecture/architecture_validation_lab.tscn
buildings:
  - AST-ARCH-BLD-WAYSTATION-001
  - AST-ARCH-BLD-STOREHOUSE-001
  - AST-ARCH-BLD-WATCHTOWER-LOW-001
diagnostics:
  grid_overlay: required
  connector_gizmos: required
  collision_debug: required
  navigation_debug: required
  occlusion_debug: required
executed: false
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Chemin :** la scène de test reste hors du manuel lecteur et des sources importées.
- **Diagnostics :** chaque système dispose d’une visualisation obligatoire.
- **Exécution :** `false` interdit toute conclusion runtime.
- **Décision :** le laboratoire restera bloqué tant que scènes et assets ne sont pas matérialisés.
## 39. Validateur structurel GDScript
Le validateur suivant inspecte une scène de laboratoire sans déplacer, renommer ni supprimer de nœud. Il contrôle la
racine, les identifiants de modules, les points de snapping, les formes de collision, les profils de navigation, les
occluders et un profil de grille candidat. Il ne remplace ni une inspection visuelle, ni un bake, ni une mesure de
performance.
> **[VSC] Créer le validateur : `tests/art/architecture/architecture_kit_validator.gd`.**
```gdscript
class_name ArchitectureKitValidator
extends Node

enum ValidationCode {
    OK = 0,
    ROOT_MISSING = 1,
    MODULE_ID_MISSING = 2,
    MODULE_ID_DUPLICATE = 3,
    REQUIRED_MODULE_MISSING = 4,
    SNAP_POINT_MISSING = 5,
    COLLISION_SHAPE_MISSING = 6,
    NON_UNIFORM_COLLISION_SCALE = 7,
    NAVIGATION_PROFILE_MISSING = 8,
    OCCLUDER_RESOURCE_MISSING = 9,
    GRID_PROFILE_INVALID = 10
}

const EPSILON: float = 0.0001
const MODULE_META_KEY: StringName = &"architecture_module_id"

func validate_scene(
    root: Node,
    required_module_ids: PackedStringArray,
    required_snap_names: PackedStringArray,
    require_navigation: bool,
    require_occlusion: bool
) -> Dictionary:
    var issues: Array[Dictionary] = []

    if root == null:
        issues.append(_issue(
            ValidationCode.ROOT_MISSING,
            "root",
            "La racine de validation est absente."
        ))
        return _result(ValidationCode.ROOT_MISSING, issues)

    var found_module_ids := _collect_module_ids(root, issues)
    _validate_required_modules(
        found_module_ids,
        required_module_ids,
        issues
    )
    _validate_snap_points(
        root,
        required_snap_names,
        issues
    )
    _validate_collision_shapes(root, issues)

    if require_navigation:
        _validate_navigation_profiles(root, issues)

    if require_occlusion:
        _validate_occluders(root, issues)

    var code := ValidationCode.OK
    if not issues.is_empty():
        code = int(issues[0]["code"]) as ValidationCode

    return _result(code, issues)

func validate_grid_profile(
    cell_size: Vector3,
    secondary_increment: float
) -> Dictionary:
    var issues: Array[Dictionary] = []

    if not _is_positive_finite_vector(cell_size):
        issues.append(_issue(
            ValidationCode.GRID_PROFILE_INVALID,
            "cell_size",
            "Chaque composante de cell_size doit être finie et positive."
        ))

    if (
        not is_finite(secondary_increment)
        or secondary_increment <= 0.0
    ):
        issues.append(_issue(
            ValidationCode.GRID_PROFILE_INVALID,
            "secondary_increment",
            "La sous-grille doit être finie et strictement positive."
        ))

    if (
        _is_positive_finite_vector(cell_size)
        and is_finite(secondary_increment)
        and secondary_increment > 0.0
    ):
        _validate_increment_divides_axis(
            cell_size.x,
            secondary_increment,
            "cell_size.x",
            issues
        )
        _validate_increment_divides_axis(
            cell_size.y,
            secondary_increment,
            "cell_size.y",
            issues
        )
        _validate_increment_divides_axis(
            cell_size.z,
            secondary_increment,
            "cell_size.z",
            issues
        )

    var code := ValidationCode.OK
    if not issues.is_empty():
        code = int(issues[0]["code"]) as ValidationCode

    return _result(code, issues)

func _collect_module_ids(
    root: Node,
    issues: Array[Dictionary]
) -> Dictionary:
    var found: Dictionary = {}

    for node: Node in _walk_nodes(root):
        if not node.has_meta(MODULE_META_KEY):
            continue

        var raw_id: Variant = node.get_meta(MODULE_META_KEY)
        var module_id := str(raw_id).strip_edges()

        if module_id.is_empty():
            issues.append(_issue(
                ValidationCode.MODULE_ID_MISSING,
                node.get_path(),
                "Une métadonnée de module est vide."
            ))
            continue

        if found.has(module_id):
            issues.append(_issue(
                ValidationCode.MODULE_ID_DUPLICATE,
                module_id,
                "Le même identifiant est porté par plusieurs nœuds."
            ))
            continue

        found[module_id] = node.get_path()

    return found

func _validate_required_modules(
    found: Dictionary,
    required: PackedStringArray,
    issues: Array[Dictionary]
) -> void:
    for module_id: String in required:
        if not found.has(module_id):
            issues.append(_issue(
                ValidationCode.REQUIRED_MODULE_MISSING,
                module_id,
                "Un module requis est absent du laboratoire."
            ))

func _validate_snap_points(
    root: Node,
    required_names: PackedStringArray,
    issues: Array[Dictionary]
) -> void:
    for module_node: Node in _nodes_with_meta(root, MODULE_META_KEY):
        for snap_name: String in required_names:
            if not _contains_named_node(module_node, snap_name):
                issues.append(_issue(
                    ValidationCode.SNAP_POINT_MISSING,
                    "%s:%s" % [
                        str(module_node.get_meta(MODULE_META_KEY)),
                        snap_name
                    ],
                    "Un point de snapping requis est absent."
                ))

func _validate_collision_shapes(
    root: Node,
    issues: Array[Dictionary]
) -> void:
    for node: Node in root.find_children(
        "*",
        "CollisionShape3D",
        true,
        false
    ):
        var collision := node as CollisionShape3D

        if collision.shape == null:
            issues.append(_issue(
                ValidationCode.COLLISION_SHAPE_MISSING,
                collision.get_path(),
                "La CollisionShape3D ne référence aucune Shape3D."
            ))
            continue

        var scale_value := collision.scale
        var uniform_xy := (
            absf(scale_value.x - scale_value.y) <= EPSILON
        )
        var uniform_yz := (
            absf(scale_value.y - scale_value.z) <= EPSILON
        )

        if not (uniform_xy and uniform_yz):
            issues.append(_issue(
                ValidationCode.NON_UNIFORM_COLLISION_SCALE,
                collision.get_path(),
                "La collision utilise une échelle non uniforme."
            ))

func _validate_navigation_profiles(
    root: Node,
    issues: Array[Dictionary]
) -> void:
    var regions := root.find_children(
        "*",
        "NavigationRegion3D",
        true,
        false
    )

    if regions.is_empty():
        issues.append(_issue(
            ValidationCode.NAVIGATION_PROFILE_MISSING,
            "NavigationRegion3D",
            "Aucune région de navigation n'est présente."
        ))
        return

    for node: Node in regions:
        var region := node as NavigationRegion3D
        if region.navigation_mesh == null:
            issues.append(_issue(
                ValidationCode.NAVIGATION_PROFILE_MISSING,
                region.get_path(),
                "La région ne référence aucune NavigationMesh."
            ))

func _validate_occluders(
    root: Node,
    issues: Array[Dictionary]
) -> void:
    var occluders := root.find_children(
        "*",
        "OccluderInstance3D",
        true,
        false
    )

    if occluders.is_empty():
        issues.append(_issue(
            ValidationCode.OCCLUDER_RESOURCE_MISSING,
            "OccluderInstance3D",
            "Aucun occluder n'est présent."
        ))
        return

    for node: Node in occluders:
        var instance := node as OccluderInstance3D
        if instance.occluder == null:
            issues.append(_issue(
                ValidationCode.OCCLUDER_RESOURCE_MISSING,
                instance.get_path(),
                "L'instance ne référence aucune ressource d'occlusion."
            ))

func _nodes_with_meta(
    root: Node,
    key: StringName
) -> Array[Node]:
    var result: Array[Node] = []

    for node: Node in _walk_nodes(root):
        if node.has_meta(key):
            result.append(node)

    return result

func _walk_nodes(root: Node) -> Array[Node]:
    var result: Array[Node] = [root]
    var cursor := 0

    while cursor < result.size():
        var current := result[cursor]
        cursor += 1

        for child: Node in current.get_children():
            result.append(child)

    return result

func _contains_named_node(
    root: Node,
    expected_name: String
) -> bool:
    if String(root.name).to_lower() == expected_name.to_lower():
        return true

    for child: Node in root.get_children():
        if _contains_named_node(child, expected_name):
            return true

    return false

func _is_positive_finite_vector(value: Vector3) -> bool:
    return (
        is_finite(value.x)
        and is_finite(value.y)
        and is_finite(value.z)
        and value.x > 0.0
        and value.y > 0.0
        and value.z > 0.0
    )

func _validate_increment_divides_axis(
    axis_length: float,
    increment: float,
    subject: String,
    issues: Array[Dictionary]
) -> void:
    var ratio := axis_length / increment
    var nearest := roundf(ratio)

    if absf(ratio - nearest) > EPSILON:
        issues.append(_issue(
            ValidationCode.GRID_PROFILE_INVALID,
            subject,
            "La sous-grille ne divise pas cet axe à la tolérance admise."
        ))

func _issue(
    code: ValidationCode,
    subject: Variant,
    message: String
) -> Dictionary:
    return {
        "code": int(code),
        "subject": str(subject),
        "message": message
    }

func _result(
    code: ValidationCode,
    issues: Array[Dictionary]
) -> Dictionary:
    return {
        "ok": code == ValidationCode.OK,
        "code": int(code),
        "issues": issues.duplicate(true)
    }
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Classe :** `ArchitectureKitValidator` étend `Node` pour être instancié dans le laboratoire.
- **Énumération :** `ValidationCode` fournit des identifiants numériques stables pour les catégories de problème.
- **Entrées :** `validate_scene` reçoit la racine, deux `PackedStringArray` et deux booléens de politique.
- **Valeur de retour :** les deux fonctions publiques renvoient un `Dictionary` avec `ok`, `code` et une copie profonde des problèmes.
- **Métadonnée :** `MODULE_META_KEY` utilise un `StringName` pour lire l’identité stable des modules.
- **Collecte :** `_walk_nodes` réalise un parcours itératif en largeur et évite de modifier l’arbre.
- **Dictionnaire :** `_collect_module_ids` associe un identifiant à un `NodePath` et détecte les doublons.
- **Recherche :** `find_children` sélectionne les types Godot sans supposer une profondeur fixe.
- **Collisions :** une `CollisionShape3D` doit référencer une `Shape3D` et conserver une échelle uniforme à `EPSILON` près.
- **Navigation :** une `NavigationRegion3D` doit référencer une `NavigationMesh`, mais sa présence ne prouve pas la connectivité.
- **Occlusion :** une `OccluderInstance3D` doit référencer une ressource, sans garantir un gain.
- **Grille :** `validate_grid_profile` refuse les composantes non finies, nulles ou négatives et contrôle la divisibilité par la sous-grille.
- **Opérateurs :** `==`, `<=`, `>`, `and`, `or` et `not` combinent comparaisons, tolérances et politiques.
- **Conversions :** `str()`, `int()` et `as` rendent les types attendus explicites.
- **Effets de bord :** le validateur ne transforme aucune scène ; il remplit seulement des tableaux locaux.
- **Limite :** la structure ne prouve ni l’absence de trous, ni la qualité visuelle, ni la navigation runtime, ni les performances.
## 40. Rapport JSON du validateur
Un rapport réel conserve le commit, la scène, le profil de grille, les modules attendus et le résultat. L’exemple
suivant reste explicitement non exécuté et ne contient aucune mesure inventée.
> **[SORTIE] Exemple de rapport attendu — Ne pas saisir.**
```json
{
  "kit_id": "AST-ARCH-KIT-WAYSTATION-001",
  "validator": "ArchitectureKitValidator",
  "scene": "res://tests/art/architecture/architecture_validation_lab.tscn",
  "executed": false,
  "grid_profile": {
    "cell_size": null,
    "secondary_increment": null
  },
  "required_buildings": [
    "AST-ARCH-BLD-WAYSTATION-001",
    "AST-ARCH-BLD-STOREHOUSE-001",
    "AST-ARCH-BLD-WATCHTOWER-LOW-001"
  ],
  "result": {
    "ok": false,
    "code": 1,
    "issues": []
  },
  "notes": [
    "Exemple documentaire uniquement."
  ]
}
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Exécution :** `executed: false` interdit d’interpréter le document comme une preuve moteur.
- **Valeurs nulles :** la grille n’est pas remplacée par des dimensions imaginées.
- **Bâtiments :** les trois preuves sont enregistrées dans le contexte du rapport.
- **Résultat :** `ok`, `code` et `issues` reprennent le contrat GDScript.
- **Stockage :** un rapport réel serait conservé sous `tests/art/architecture/reports`.
## 41. Matrice d’assemblage
La matrice teste les paires et chaînes les plus risquées avant les bâtiments complets. Chaque scénario nomme les
modules, les connecteurs utilisés, le nombre de répétitions et les captures attendues.
> **[LECTURE] Matrice de scénarios — Ne pas saisir.**
```yaml
suite_id: AST-ARCH-ASSEMBLY-SUITE-001-v001
scenarios:
  - id: wall_chain
    modules:
      - AST-ARCH-WALL-SOLID-A-001
      - AST-ARCH-WALL-WINDOW-A-001
    repetitions: provisional
    checks:
      - cumulative_drift
      - shading_seam
  - id: outside_corner
    modules:
      - AST-ARCH-WALL-SOLID-A-001
      - AST-ARCH-CORNER-OUT-A-001
    checks:
      - thickness
      - collision_continuity
  - id: stair_level_join
    modules:
      - AST-ARCH-STAIR-STRAIGHT-A-001
      - AST-ARCH-LANDING-A-001
      - AST-ARCH-FLOOR-FIELD-A-001
    checks:
      - elevation
      - headroom
      - navigation
  - id: roof_ridge
    modules:
      - AST-ARCH-ROOF-SLOPE-A-001
      - AST-ARCH-ROOF-RIDGE-A-001
    checks:
      - pitch_match
      - light_leak
captures: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Scénarios :** chaîne, coin, liaison verticale et toiture couvrent quatre familles de défauts.
- **Répétitions :** le nombre reste provisoire jusqu’au choix de la grille.
- **Contrôles :** géométrie, ombrage, collision et navigation sont distingués.
- **Captures :** la preuve visuelle est obligatoire mais non produite ici.
## 42. Tests de collision, navigation et caméra
Le laboratoire est parcouru avec les visualisations de débogage. Les collisions sont contrôlées contre les surfaces
visibles ; la navigation est interrogée après synchronisation ; la caméra teste les coins, plafonds bas, escaliers et
petites pièces. Un succès dans un seul système ne masque pas l’échec d’un autre.
> **[LECTURE] Campagne spatiale — Ne pas saisir.**
```yaml
campaign_id: AST-ARCH-SPATIAL-TESTS-001-v001
collision:
  doorway_passage: pending
  wall_leaks: pending
  stair_contact: pending
  roof_access: pending
navigation:
  room_to_corridor: pending
  stair_to_floor: pending
  doorway_edges: pending
  disconnected_islands: pending
camera:
  interior_corners: pending
  stair_headroom: pending
  doorway_transition: pending
  exterior_overhangs: pending
server_sync_waited: false
runtime_executed: false
decision: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Systèmes :** collision, navigation et caméra disposent de résultats séparés.
- **Îlots :** la campagne recherche explicitement les zones non connectées.
- **Synchronisation :** `server_sync_waited: false` indique que le protocole n’a pas été exécuté.
- **Runtime :** aucune traversée réelle n’est revendiquée.
- **Décision :** toute entrée en attente conserve le blocage.
## 43. Lisibilité architecturale et répétition
La validation visuelle compare les bâtiments sous plusieurs distances et éclairages. Elle recherche les répétitions de
fenêtres, de joints, de toitures et de salissure, mais aussi les variations qui détruisent l’identité du kit. Les
captures sont faites avec une focale et une exposition documentées afin de rendre les comparaisons utiles.
> **[LECTURE] Grille de captures — Ne pas saisir.**
```yaml
capture_suite: AST-ARCH-VISUAL-001-v001
views:
  street_long:
    purpose: repetition_and_silhouette
  facade_close:
    purpose: joints_and_material_scale
  interior_room:
    purpose: thickness_and_openings
  roof_high:
    purpose: ridge_and_repetition
  grazing_light:
    purpose: normals_and_seams
comparisons:
  three_buildings_same_kit: pending
  variant_balance: pending
  identity_preserved: pending
camera_profile: pending
lighting_profile: pending
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Vues :** chaque caméra cible un défaut particulier.
- **Comparaison :** les trois bâtiments permettent de juger variété et cohérence ensemble.
- **Profils :** caméra et éclairage seront enregistrés pour rendre les captures comparables.
- **État :** aucune image n’est annoncée comme produite.
## 44. Campagne de performance
Les mesures sont réalisées dans Godot sur le matériel de référence avec une scène vide témoin. Le kit est testé sous
plusieurs compositions afin de distinguer coût géométrique, matériaux, collisions, navigation, occlusion et LOD/HLOD.
Les nombres de modules et seuils restent provisoires avant cette campagne.
- temps CPU et GPU par image ;
- draw calls et changements de matériaux ;
- mémoire des maillages et textures ;
- temps d’import et de chargement ;
- coût de la physique statique ;
- temps de génération et de synchronisation de navigation ;
- coût et bénéfice de l’occlusion ;
- transitions de LOD/HLOD et artefacts visuels ;
- comparaison scènes modulaires, GridMap et hybride si les trois restent candidates.
> **[LECTURE] Plan de benchmark — Ne pas saisir.**
```yaml
benchmark_id: AST-ARCH-BENCH-001-v001
hardware_profile: AST-HW-RX6750XT-001-v001
baseline_scene: pending
scenarios:
  single_waystation:
    module_count: provisional
    measurements: pending
  three_buildings:
    module_count: provisional
    measurements: pending
  repeated_street:
    module_count: provisional
    measurements: pending
  interior_exterior_transition:
    measurements: pending
  hlod_transition:
    measurements: pending
variants:
  modular_scenes: candidate
  gridmap: candidate
  hybrid: candidate
metrics:
  - frame_time_cpu_ms
  - frame_time_gpu_ms
  - draw_calls
  - mesh_memory_bytes
  - texture_memory_bytes
  - physics_step_ms
  - navigation_bake_ms
  - load_time_ms
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Matériel :** le profil relie chaque résultat à la configuration Windows/AMD de référence.
- **Témoin :** la scène de base permet de soustraire le coût du laboratoire.
- **Scénarios :** bâtiment unique, groupe, rue et transitions couvrent des charges distinctes.
- **Variantes :** les stratégies de placement ne sont comparées que si elles restent pertinentes.
- **Métriques :** CPU, GPU, appels, mémoire, physique, navigation et chargement sont séparés.
- **Blocage :** aucune valeur n’est créée avant l’exécution.
## 45. Parcours Solo et Studio
### 45.1 Mode Solo
Le parcours Solo limite le kit aux modules nécessaires au vertical slice et aux trois bâtiments de preuve. Il
privilégie une grille simple, une seule famille de murs, une toiture principale, une circulation verticale et quelques
variantes réutilisables. La scène modulaire générale est prioritaire ; `GridMap` n’est ajouté que si le gain d’édition
est démontré.
- un seul contrat de grille ;
- un catalogue compact avec connecteurs explicites ;
- trois bâtiments avant les détails supplémentaires ;
- collisions et navigation simples ;
- un laboratoire Godot partagé ;
- un profil de LOD/HLOD mesuré avant extension.
### 45.2 Mode Studio
Le parcours Studio sépare responsabilité artistique, architecture, modélisation, technique, intégration et
performance. Les changements de grille ou de connecteur passent par une demande versionnée, car ils peuvent invalider
tous les modules et scènes existants.
| Responsabilité | Propriétaire principal |
|---|---|
| grille, travées et gabarits | architecture et direction artistique |
| catalogue et géométrie | environment artists |
| connecteurs, collisions et proxies | technical art |
| matériaux partagés | lookdev |
| navigation et occlusion | intégration Godot |
| LOD/HLOD et budgets | performance et environment art |
| scènes de preuve | intégration et QA artistique |
| publication du kit | responsable de contenu |
> **[LECTURE] Porte de changement Studio — Ne pas saisir.**
```yaml
change_request: AST-ARCH-CHANGE-001
affected_contract:
  - grid_profile
  - connector_profile
impact_analysis:
  modules: pending
  buildings: pending
  collisions: pending
  navigation: pending
  lod_hlod: pending
approval:
  architecture: pending
  technical_art: pending
  integration: pending
migration_plan: required
status: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Contrats :** grille et connecteurs sont traités comme des interfaces publiques du kit.
- **Impact :** chaque famille de dépendances reçoit une analyse explicite.
- **Approbations :** les spécialités concernées doivent valider le changement.
- **Migration :** une modification acceptée doit expliquer comment les scènes existantes évoluent.
## 46. Porte d’acceptation
Le kit ne devient pas accepté parce qu’un module est beau ou qu’un bâtiment paraît complet. La porte exige des preuves
cohérentes sur les cinq livrables du plan maître et maintient les réserves tant que Blender et Godot n’ont pas été
exécutés.
1. la grille et la sous-grille sont mesurées avec les gabarits humains ;
2. le catalogue couvre les familles minimales et possède des identifiants stables ;
3. les connecteurs, pivots et tolérances sont vérifiés après export ;
4. les trois bâtiments sont assemblés sans trous ni décalages non prévus ;
5. coins, ouvertures, escaliers et toitures respectent les règles communes ;
6. les collisions correspondent à la géométrie jouable ;
7. la navigation relie les espaces attendus sans îlots involontaires ;
8. les occluders sont simples, qualifiés et mesurés ;
9. la répétition est contrôlée sans casser l’identité ;
10. les matériaux partagés et surfaces sont conformes à la frontière du chapitre 16 ;
11. les LOD de modules et HLOD de bâtiments conservent les usages nécessaires ;
12. les scènes importées et dérivées restent séparées ;
13. les rapports, captures, provenance et empreintes sont conservés ;
14. aucune règle de construction par le joueur n’est dupliquée.
> **[LECTURE] Décision de la porte — Ne pas saisir.**
```yaml
acceptance_gate: AST-ARCH-ACCEPTANCE-001-v001
deliverables:
  modular_kit: blocked
  metric_grid: blocked
  assembly_rules: blocked
  test_scenes: blocked
  budgets_and_lod: blocked
runtime_checks:
  blender_export: not_executed
  godot_import: not_executed
  assembly_tests: not_executed
  navigation_tests: not_executed
  performance_tests: not_executed
decision: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Livrables :** les cinq entrées correspondent exactement au plan maître.
- **Runtime :** chaque famille d’exécution est déclarée séparément.
- **Valeurs :** `blocked` et `not_executed` empêchent une acceptation implicite.
- **Décision :** le chapitre fournit la méthode, pas les preuves matérielles.
## 47. Erreurs fréquentes et diagnostics
<!-- qa:error-correction-section -->
Les dix cas suivants décrivent des défauts reproductibles. Chaque correction rétablit un contrat mesurable sans
prétendre que les scènes de `Project Asteria` ont déjà été exécutées.
### 47.1 Définir la grille après la modélisation
**Symptôme :** chaque mur possède une largeur légèrement différente et les coins exigent des corrections locales.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
modules:
  wall_a_width_m: 3.02
  wall_b_width_m: 2.97
  window_wall_width_m: 3.01
grid_profile: to_be_defined_later
status: accepted
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Les modules ont déjà créé leurs propres cotes ; une grille ajoutée ensuite ne peut pas supprimer les incompatibilités sans reprise.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
grid_profile: AST-ARCH-GRID-001-v001
module_width_cells: 1
dimensions_m: provisional
blockout_review: pending
status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La correction rend la grille antérieure aux modules et maintient les dimensions bloquées jusqu’au blockout.
### 47.2 Placer toutes les origines au centre
**Symptôme :** chaque module demande un offset différent pour retomber sur la grille ou s’aligner à un voisin.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-SOLID-A-001
origin_role: bounding_box_center
snap_points: absent
placement_offset: manual_per_instance
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le centre de boîte ne représente aucune interface structurelle et transfère la correction à chaque instance.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
module_id: AST-ARCH-WALL-SOLID-A-001
origin_role: lower_left_grid_interface
snap_points:
  - edge_left
  - edge_right
placement_test: pending
status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** L’origine est liée à la grille et les interfaces permettent un placement répétable sans offset caché.
### 47.3 Superposer des murs pour fabriquer les coins
**Symptôme :** les coins sont plus épais, z-fightent ou possèdent une collision double.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
outside_corner:
  method: overlap_two_full_walls
  hidden_faces: ignored
  collision_overlap: accepted
  material_seam: hidden_with_trim
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La superposition mélange deux volumes complets et masque la faute avec une décoration sans résoudre géométrie ni collision.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
outside_corner:
  method: dedicated_module
  module_id: AST-ARCH-CORNER-OUT-A-001
  thickness_review: pending
  collision_review: pending
status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Un module dédié possède une seule épaisseur, une interface contrôlée et un proxy de collision qualifiable.
### 47.4 Corriger un module par une échelle non uniforme
**Symptôme :** le mur s’aligne visuellement mais ses ouvertures, collisions et matériaux sont déformés.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
instance:
  module_id: AST-ARCH-WALL-DOOR-A-001
  scale: [1.0, 1.15, 0.92]
  grid_fit: visual_only
  status: accepted
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** L’instance ne respecte plus le contrat de cellule et déforme toutes les responsabilités dépendantes de la géométrie.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
instance:
  module_id: AST-ARCH-WALL-DOOR-A-001
  scale: [1.0, 1.0, 1.0]
  dimensions_source: AST-ARCH-GRID-001-v001
  grid_fit_review: pending
  status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** L’échelle uniforme conserve le contrat et renvoie la correction aux dimensions de la source ou à un module versionné.
### 47.5 Utiliser le maillage de rendu comme collision finale
**Symptôme :** les portes accrochent, les escaliers vibrent et la physique dépend du détail décoratif.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
collision:
  source: render_mesh
  generation: automatic
  runtime_use: final
  simplification: none
  review: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le rendu contient des détails et une triangulation qui ne décrivent pas la surface jouable au coût attendu.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
collision:
  source: dedicated_proxy
  shapes:
    - BoxShape3D
    - BoxShape3D
    - BoxShape3D
  generated_from_render: diagnostic_only
  runtime_review: pending
  status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Des formes dédiées représentent les volumes utiles et la génération automatique reste un outil de comparaison.
### 47.6 Supposer que deux navmeshes superposés sont connectés
**Symptôme :** l’agent atteint le seuil de porte mais ne trouve aucun chemin vers la pièce voisine.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
navigation_regions:
  room_a: baked
  room_b: baked
  overlap_m: provisional
connectivity_test: skipped
status: accepted
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Un chevauchement visuel ne garantit pas des bords compatibles ni une connexion dans la carte de navigation.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
navigation_regions:
  room_a: pending_bake
  room_b: pending_bake
interface:
  doorway_shared_edge_review: pending
  map_assignment_review: pending
path_query_after_sync: pending
status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La correction contrôle l’interface, la carte et une requête après synchronisation avant de conclure.
### 47.7 Employer le bâtiment détaillé comme occluder
**Symptôme :** l’occlusion coûte cher, se recalcule souvent ou produit des masquages instables.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
occluder:
  source: full_render_building
  windows_and_trim: included
  moving_doors: included
  performance_review: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le proxy hérite de détails et d’éléments mobiles inutiles au masquage des grandes masses.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
occluder:
  source: dedicated_simple_proxies
  shapes:
    - exterior_wall_boxes
    - roof_mass_box
  moving_doors: excluded
  performance_review: pending
  status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Des volumes simples et stables représentent l’enveloppe à masquer et restent soumis à une mesure.
### 47.8 Randomiser les rotations sans respecter les connecteurs
**Symptôme :** les variantes cassent la façade, retournent les normales ou déplacent portes et toitures.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
variation:
  rotation_deg: random_0_to_360
  mirror: random
  connector_review: none
  collision_review: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Une transformation arbitraire modifie les interfaces et suppose à tort que tous les modules sont symétriques.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
variation:
  allowed_rotations_deg: [0, 90, 180, 270]
  mirror: explicit_variant_only
  connector_invariants: required
  collision_review: pending
  status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Les transformations sont limitées par le contrat et le miroir devient une variante contrôlée.
### 47.9 Supprimer les intérieurs dans un HLOD encore visitable
**Symptôme :** une caméra intérieure voit disparaître murs, plafonds ou collisions pendant une transition de distance.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
building_hlod:
  distant_shell:
    interiors: removed
    collisions: removed
  activation:
    distance_only: true
  enterable: true
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La distance de la caméra ne suffit pas lorsque le bâtiment reste visitable ou visible depuis une ouverture.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
building_hlod:
  exterior_shell:
    interiors: excluded
    allowed_when:
      - not_enterable
      - no_active_interior_view
  enterable_representation:
    interiors: required
    collision_profile: maintained
  thresholds: pending_measurement
  status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La représentation dépend de l’usage et de la visibilité intérieure, puis attend des seuils mesurés.
### 47.10 Déclarer le kit terminé après un seul bâtiment Blender
**Symptôme :** la maison-relais paraît correcte, mais l’entrepôt révèle une dérive et la tour ne peut pas joindre ses
niveaux.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
blender_building:
  waystation: passed_visual_review
storehouse: not_assembled
watchtower: not_assembled
godot_import: not_executed
navigation: not_executed
performance: not_executed
status: accepted
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Un bâtiment favorable ne prouve ni la couverture du catalogue, ni l’empilement, ni les systèmes moteur.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
blender_buildings:
  waystation: pending
  storehouse: pending
  watchtower: pending
godot_import: not_executed
assembly_suite: not_executed
navigation: not_executed
performance: not_executed
status: blocked
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Les trois bâtiments et les preuves Godot restent obligatoires avant toute acceptation.
## 48. Livrables à conserver
Le plan maître exige cinq livrables permanents, maintenus comme contrats versionnés et séparés des caches.
1. **kit modulaire** — catalogue, familles, sources, exports, variantes et provenance ;
2. **grille métrique** — unités, cellules, sous-grille, niveaux, travées et gabarits ;
3. **règles d’assemblage** — connecteurs, pivots, tolérances, coins, transitions et transformations autorisées ;
4. **scènes de test** — bâtiments pilotes, laboratoire, matrices, captures et rapports ;
5. **budgets et LOD** — coûts provisoires, mesures, LOD de modules, HLOD de bâtiments et décisions.
> **[LECTURE] Manifeste de livraison — Ne pas saisir.**
```yaml
deliverable_manifest: AST-ARCH-DELIVERY-001-v001
modular_kit:
  profile: AST-ARCH-KIT-WAYSTATION-001
  status: blocked
metric_grid:
  profile: AST-ARCH-GRID-001-v001
  status: blocked
assembly_rules:
  profile: AST-ARCH-ASSEMBLY-RULES-001-v001
  status: blocked
test_scenes:
  profile: AST-ARCH-VALIDATION-LAB-001-v001
  status: blocked
budgets_and_lod:
  profile: AST-ARCH-LOD-WAYSTATION-001-v001
  status: blocked
provenance_review: pending
publication_decision: blocked
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Manifeste :** les cinq livrables correspondent exactement au plan maître.
- **Profils :** chaque entrée renvoie vers un contrat indépendant et versionné.
- **Provenance :** les droits et sources doivent être qualifiés avant publication.
- **Décision :** aucun fichier ou résultat runtime n’est déclaré produit.
## 49. Synthèse opérationnelle pour Project Asteria
Le chapitre 13 fournit à `Project Asteria` une méthode complète pour produire un kit architectural modulaire. Le kit
de la Maison-relais est encadré par une grille métrique, des gabarits humains, un catalogue stable, des familles de
murs, coins, sols, ouvertures, escaliers et toitures, des connecteurs, pivots et tolérances, des règles d’intérieur et
de façade, des variantes, des zones matérielles, des collisions dédiées, une géométrie de navigation, des occluders
simples, une préparation visuelle de la destruction, un export GLB, des scènes Godot dérivées, un choix raisonné entre
scènes modulaires, `GridMap` et hybride, des profils LOD/HLOD, un laboratoire, un validateur structurel et une
campagne de performance.
Les trois bâtiments restent bloqués tant que la grille, les modules, les scènes Blender, les GLB, les collisions, le
navmesh, les occluders, les LOD, les HLOD, les captures et les mesures ne sont pas réellement produits. Le chapitre
prépare les raccords aux terrains et l’intégration à la construction runtime, mais ne crée ni terrain, ni streaming de
monde ouvert, ni règles de construction par le joueur.
## 50. Références techniques officielles
Les références suivantes encadrent la matérialisation et doivent être requalifiées si les versions changent :
- [Blender Manual — Snapping](https://docs.blender.org/manual/en/5.0/editors/3dview/controls/snapping.html) ;
- [Blender Manual — Collections](https://docs.blender.org/manual/en/5.0/scene_layout/collections/collections.html) ;
- [Blender Manual — Asset Libraries](https://docs.blender.org/manual/en/5.0/files/asset_libraries/index.html) ;
- [Blender Manual — Empties](https://docs.blender.org/manual/en/5.0/modeling/empties.html) ;
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/5.0/addons/import_export/scene_gltf2.html) ;
- [Godot 4.7 — Importing 3D scenes](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html) ;
- [Godot 4.7 — Import configuration](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html) ;
- [Godot 4.7 — GridMap](https://docs.godotengine.org/en/4.7/classes/class_gridmap.html) ;
- [Godot 4.7 — Using GridMaps](https://docs.godotengine.org/en/4.7/tutorials/3d/using_gridmaps.html) ;
- [Godot 4.7 — MeshLibrary](https://docs.godotengine.org/en/4.7/classes/class_meshlibrary.html) ;
- [Godot 4.7 — GeometryInstance3D](https://docs.godotengine.org/en/4.7/classes/class_geometryinstance3d.html) ;
- [Godot 4.7 — Visibility ranges](https://docs.godotengine.org/en/4.7/tutorials/3d/visibility_ranges.html) ;
- [Godot 4.7 — Collision shapes 3D](https://docs.godotengine.org/en/4.7/tutorials/physics/collision_shapes_3d.html) ;
- [Godot 4.7 — Using navigation meshes](https://docs.godotengine.org/en/4.7/tutorials/navigation/navigation_using_navigationmeshes.html) ;
- [Godot 4.7 — Connecting navigation meshes](https://docs.godotengine.org/en/4.7/tutorials/navigation/navigation_connecting_navmesh.html) ;
- [Godot 4.7 — NavigationRegion3D](https://docs.godotengine.org/en/4.7/classes/class_navigationregion3d.html) ;
- [Godot 4.7 — Occlusion culling](https://docs.godotengine.org/en/4.7/tutorials/3d/occlusion_culling.html) ;
- [Godot 4.7 — OccluderInstance3D](https://docs.godotengine.org/en/4.7/classes/class_occluderinstance3d.html).
