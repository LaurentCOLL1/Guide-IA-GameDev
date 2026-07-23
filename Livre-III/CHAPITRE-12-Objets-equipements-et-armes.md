---
title: "Livre III — Chapitre 12 : Objets, équipements et armes"
id: "DOC-L3-CH12"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 12
last-verified: "2026-07-23T13:30:28+02:00"
audit-status: "complete"
audit-date: "2026-07-23T13:30:28+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-12.md"
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

# Objets, équipements et armes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH12`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Le chapitre 11 a défini les vêtements, armures portées et accessoires attachés au corps. Le présent chapitre traite les objets individuels que le personnage tient, saisit, range, pose, expose ou utilise comme représentation visuelle : outils, lanternes, boucliers, armes, consommables, conteneurs portatifs et dispositifs fictifs. Il ne recommence ni les règles de layering, ni le skinning des vêtements, ni les systèmes métier d’inventaire et de combat.

Le fil rouge utilise une bibliothèque pilote de `Project Asteria`, identifiée `AST-PROP-KIT-EXPLORER-001`. Elle contient cinq objets aux contraintes différentes :

- `AST-PROP-LANTERN-001` — lanterne tenue, posable et suspendable ;
- `AST-TOOL-SURVEY-HAMMER-001` — outil à une main avec tête visuellement lourde ;
- `AST-WPN-SHORT-BLADE-001` — lame courte fictive avec prise principale et fourreau ;
- `AST-EQP-BUCKLER-001` — petit bouclier tenu en main secondaire ;
- `AST-DEVICE-PULSE-001` — dispositif fictif possédant un repère d’émission, sans balistique ni statistique définie.

Cette diversité force le pipeline à distinguer origine géométrique, pivot fonctionnel, prises, sockets de rangement, volumes de collision, pièces mobiles, états visuels et LOD. Aucun de ces assets n’est déclaré produit dans ce chapitre : les contrats, procédures et contrôles sont documentés au niveau `static-review`.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Besoin narratif et fonction observable
    ↓
Références dimensionnelles et droits
    ↓
Échelle, ergonomie et enveloppes d’usage
    ↓
Origine, axes, pivots et sockets
    ↓
Blockout et pièces mobiles
    ↓
Topologie, ombrage et matériaux provisoires
    ↓
Collisions de prise, interaction et physique
    ↓
États visuels, variantes et dégradation
    ↓
LOD et réduction des matériaux
    ↓
Export GLB et scène Godot dérivée
    ↓
Alignement, interactions, coût et décision
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** l’objet part d’un besoin visuel et d’un rig de référence déjà qualifié.
- **Ordre :** l’échelle et les repères fonctionnels sont fixés avant le détail géométrique.
- **Preuve :** chaque étape produit un contrat ou un rapport vérifiable avant acceptation.
- **Frontière :** les statistiques, dégâts, munitions, règles d’équipement et décisions de combat restent dans le Livre II.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- transformer un besoin d’usage en critères visuels et techniques observables ;
- distinguer objet tenu, objet posé, objet attaché, objet interactif et représentation de projectile ;
- chercher des dimensions de référence sans transformer une photographie en mesure fiable ;
- contrôler échelle, prise en main, dégagement des doigts et centre de masse visuel ;
- définir origine, axes, pivot fonctionnel et repères secondaires ;
- préparer prises principale et secondaire, fourreau, dos, ceinture, environnement et point d’émission ;
- séparer maillage de rendu, volumes de détection, collisions physiques et proxies spécialisés ;
- préparer des pièces mobiles sans inventer leur logique de gameplay ;
- organiser variantes, états d’usure et dégradations visuelles ;
- définir des LOD conservant la fonction et la silhouette ;
- exporter en GLB sans écraser la source Blender ;
- créer une scène Godot dérivée qui ajoute attaches, collisions et contrôles sans modifier la scène importée ;
- écrire un validateur GDScript non destructif et comprendre ses fonctions, paramètres, types, retours et opérateurs ;
- conserver des réserves explicites lorsque Blender, Godot ou le runtime n’ont pas été exécutés.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les contrats YAML et JSON, procédures Blender, exemples de hiérarchie Godot et scripts GDScript sont relus contre les documentations officielles. Ils ne constituent pas une preuve d’exécution.

Aucun objet pilote, aucune arme, aucun outil, aucun pivot, aucun socket, aucune collision, aucun matériau, aucun atlas, aucun LOD, aucun GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme produits. Les dimensions, masses apparentes, nombres de triangles, matériaux, surfaces, collisions, distances et seuils sont des hypothèses de travail à confirmer.

Le chapitre décrit des armes uniquement comme assets visuels de jeu. Il ne fournit ni procédé de fabrication réel, ni calcul balistique, ni instruction d’emploi dans le monde réel. Les effets, dégâts, cadence, portée, munitions, projectiles autoritaires et règles de combat appartiennent au Livre II.

## 4. Périmètre et frontières

Le chapitre couvre :

- références dimensionnelles, ergonomie et fonction visuelle ;
- échelle, orientation, origine et pivots ;
- prises, fourreaux, attaches et sockets d’environnement ;
- pièces mobiles et dégagements mécaniques visuels ;
- blockout, topologie, ombrage et matériaux provisoires ;
- collisions de prise, d’interaction et de physique ;
- point d’émission ou origine de projectile lorsque nécessaire ;
- états visuels, variantes, usure et dégradation ;
- LOD géométriques, matériels et fonctionnels ;
- export GLB, scène Godot dérivée et validation structurelle.

Le chapitre ne couvre pas :

- les vêtements, armures portées et accessoires corporels du chapitre 11 ;
- les grilles, modules, snapping et kits de bâtiments du chapitre 13 ;
- le pipeline PBR transversal du chapitre 16 ;
- la retopologie, les UV et le baking génériques du chapitre 17 ;
- le rig de production et les contraintes finales du chapitre 19 ;
- les animations finales de prise, de frappe, de tir ou de rechargement du chapitre 20 ;
- les VFX d’impact et de projectile du chapitre 23 ;
- les règles d’inventaire, d’équipement, de durabilité, de dégâts, de combat ou de projectile du Livre II.

> **[LECTURE] Matrice des responsabilités — Ne pas saisir.**

```yaml
chapter_12:
  owns:
    - object_function_and_scale_contracts
    - origin_pivot_and_socket_conventions
    - render_and_collision_profiles
    - visual_state_and_lod_profiles
    - godot_equipment_validation_scenes
  prepares:
    - chapter_19_rig_attachment_review
    - chapter_20_animation_alignment_tests
    - chapter_23_vfx_attachment_points
    - chapter_28_import_integration
  does_not_own:
    - wearable_layering
    - inventory_rules
    - combat_statistics
    - authoritative_projectiles
    - building_modular_grid
    - general_pbr_pipeline
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** chaque valeur de liste est une chaîne nommant une responsabilité documentaire.
- **Préparation :** `prepares` fournit des repères et contrats sans exécuter les chapitres futurs.
- **Exclusion :** `does_not_own` empêche l’asset visuel d’acquérir une autorité métier.
- **Résultat attendu :** une tâche du chapitre doit se rattacher à une entrée de `owns` ou soutenir directement cette entrée.

## 5. Prérequis et fichiers à ouvrir

Avant de commencer, le lecteur doit disposer :

- d’une bible visuelle et d’une échelle de référence ;
- d’un personnage ou humanoïde de référence ;
- d’un squelette de référence et de noms d’os stables ;
- d’une main de test et d’une grille de poses ;
- d’identifiants d’assets stables ;
- d’un registre de provenance ;
- de budgets provisoires par plateforme ;
- des conventions Blender et Godot du projet.

Le lecteur ouvre :

- **[APP] Blender 5.2.0** pour les références, gabarits, blockouts, pivots, sockets, géométrie, matériaux provisoires et collections d’export ;
- **[APP] Godot 4.7.1-stable** pour l’import, les scènes dérivées, les attaches, collisions, interactions, LOD et mesures ;
- **[VSC] Visual Studio Code** pour les contrats YAML, rapports JSON et scripts GDScript ;
- **[PS] PowerShell 7** pour créer les dossiers et exécuter les contrôles documentaires.

> **[PS] Créer l’arborescence de travail.**

```powershell
$Root = "art/props/AST-PROP-KIT-EXPLORER-001"
$Folders = @(
    "$Root/briefs",
    "$Root/references",
    "$Root/dimensions",
    "$Root/pivots",
    "$Root/sockets",
    "$Root/collisions",
    "$Root/states",
    "$Root/variants",
    "$Root/lod",
    "art/blender/props/AST-PROP-KIT-EXPLORER-001",
    "art/exports/props/AST-PROP-KIT-EXPLORER-001",
    "tests/art/props/reports",
    "tests/art/props/captures"
)
foreach ($Folder in $Folders) {
    New-Item -ItemType Directory -Force -Path $Folder | Out-Null
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** `$Root` est une chaîne contenant le dossier canonique de la bibliothèque pilote ; `$Folders` est un tableau de chaînes.
- **Boucle :** `foreach` parcourt chaque chemin sans modifier la liste.
- **Paramètres :** `-ItemType Directory` exige un dossier, `-Force` rend la création idempotente et `-Path` reçoit le chemin courant.
- **Effet de bord :** les dossiers sont créés sur le disque ; `Out-Null` masque les objets retournés par PowerShell.
- **Résultat attendu :** l’arborescence existe sans effacer un dossier déjà présent.

> **[LECTURE] Arborescence canonique — Ne pas saisir.**

```text
art/
├── blender/props/
│   └── AST-PROP-KIT-EXPLORER-001/
├── props/
│   └── AST-PROP-KIT-EXPLORER-001/
│       ├── briefs/
│       ├── references/
│       ├── dimensions/
│       ├── pivots/
│       ├── sockets/
│       ├── collisions/
│       ├── states/
│       ├── variants/
│       └── lod/
├── exports/props/
│   └── AST-PROP-KIT-EXPLORER-001/
├── provenance/
└── budgets/
tests/
└── art/props/
    ├── prop_validation_lab.tscn
    ├── prop_asset_validator.gd
    ├── reports/
    └── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les fichiers Blender restent sous `art/blender` et ne sont pas confondus avec les exports.
- **Contrats :** dimensions, pivots, sockets, collisions, états, variantes et LOD possèdent des dossiers distincts.
- **Tests :** scène, validateur, rapports et captures sont regroupés sous `tests/art/props`.
- **Publication :** les rapports QA internes ne sont pas ajoutés au manuel lecteur.

## 6. Bibliothèque pilote et cas d’usage

La bibliothèque pilote n’est pas choisie pour représenter toutes les catégories d’objets. Elle sert à exercer des contraintes différentes avec un lot réduit :

- la lanterne doit être tenue, posée et suspendue ;
- le marteau d’arpentage doit sembler avoir une tête plus lourde que son manche ;
- la lame courte fictive exige prise, garde, fourreau et sécurité visuelle ;
- le bouclier exige une prise secondaire, une sangle et une silhouette lisible ;
- le dispositif fictif exige un repère d’émission, des pièces mobiles et des états lumineux sans définir de tir réel.

La bibliothèque exclut volontairement les objets à deux mains complexes, les véhicules, les machines industrielles, les armes à feu réalistes et les objets nécessitant une simulation mécanique détaillée. Ces exclusions réduisent le risque de transformer un chapitre de production d’assets en manuel de mécanique ou d’armement.

> **[LECTURE] Manifeste initial de la bibliothèque — Ne pas saisir.**

```yaml
library_id: AST-PROP-KIT-EXPLORER-001
status: blocked
objects:
  - id: AST-PROP-LANTERN-001
    category: portable_light
    required_contexts: [held, placed, suspended]
  - id: AST-TOOL-SURVEY-HAMMER-001
    category: hand_tool
    required_contexts: [held, stored]
  - id: AST-WPN-SHORT-BLADE-001
    category: fictional_melee_prop
    required_contexts: [held, sheathed]
  - id: AST-EQP-BUCKLER-001
    category: offhand_prop
    required_contexts: [held, stored]
  - id: AST-DEVICE-PULSE-001
    category: fictional_device
    required_contexts: [held, placed]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `library_id` nomme le lot ; chaque objet possède un identifiant indépendant.
- **Type :** `objects` est une liste de mappings YAML ; `required_contexts` est une liste de chaînes.
- **État :** `blocked` empêche de confondre le manifeste documentaire avec des assets produits.
- **Frontière :** `fictional_melee_prop` et `fictional_device` décrivent une apparence, pas des règles de dégâts ou de tir.

## 7. Vocabulaire fonctionnel

- **origine d’objet** : point local de référence du transform de l’objet ;
- **pivot fonctionnel** : point autour duquel une rotation ou une manipulation doit être évaluée ;
- **socket** : repère nommé fournissant position et orientation pour une attache ;
- **prise principale** : repère aligné avec la main dominante ;
- **prise secondaire** : repère destiné à une deuxième main ou à une sangle ;
- **socket de rangement** : repère utilisé lorsque l’objet est au dos, à la ceinture ou dans un fourreau ;
- **socket d’environnement** : repère permettant de poser, suspendre ou fixer l’objet au décor ;
- **volume d’interaction** : zone de détection qui rend l’objet sélectionnable ou utilisable ;
- **collision physique** : forme utilisée par la physique pour empêcher ou résoudre une pénétration ;
- **proxy d’impact** : volume simplifié utilisé comme entrée visuelle ou de test, sans autorité de dégâts ;
- **point d’émission** : repère orienté d’où un VFX ou un projectile métier pourra partir ;
- **état visuel** : représentation d’une condition, sans devenir l’autorité de cette condition ;
- **LOD fonctionnel** : représentation simplifiée qui conserve les repères et collisions encore nécessaires dans son contexte.

## 8. Brief fonctionnel par objet

Le brief commence par des verbes observables : tenir, poser, suspendre, ranger, ouvrir, allumer, inspecter. Il évite les adjectifs isolés comme « puissant », « rare » ou « rapide », qui appartiennent au design ou aux systèmes métier.

Chaque objet reçoit :

- un propriétaire artistique ;
- une fonction visible ;
- des contextes d’usage ;
- des utilisateurs ou morphologies de référence ;
- des contacts avec les mains, le corps et l’environnement ;
- des pièces mobiles ;
- des états visuels ;
- des repères requis ;
- des preuves attendues ;
- des inconnues bloquantes.

> **[LECTURE] Brief fonctionnel de la lanterne — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
visible_functions:
  - held_by_handle
  - placed_on_base
  - suspended_from_top_loop
reference_users:
  - AST-HUMAN-BASE-001
required_sockets:
  - grip_primary
  - mount_base
  - mount_hanging
  - light_origin
moving_parts:
  - handle
visual_states:
  - unlit
  - lit
  - damaged_visual
unknowns:
  - final_dimensions
  - final_light_profile
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les listes décrivent fonctions, utilisateurs, repères, pièces et états attendus.
- **Inconnues :** `unknowns` conserve les décisions non prises au lieu d’inventer des nombres.
- **État :** `blocked` reste obligatoire tant que dimensions et lumière ne sont pas validées.
- **Frontière :** `lit` est un état visuel ; l’énergie, l’autonomie ou les règles d’usage restent hors de ce manifeste.

> **[LECTURE] Brief fonctionnel de la lame courte — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
visible_functions:
  - held_in_primary_hand
  - stored_in_sheath
required_sockets:
  - grip_primary
  - sheath_entry
  - impact_proxy_origin
visual_states:
  - clean
  - worn
  - damaged_visual
excluded_data:
  - damage
  - reach
  - attack_speed
  - durability_current
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonctions :** les deux fonctions visibles suffisent à guider prises et fourreau.
- **Repères :** `impact_proxy_origin` prépare un contrôle visuel sans devenir une collision de combat.
- **Exclusion :** les quatre champs métier sont explicitement interdits dans le contrat artistique.
- **Résultat attendu :** le brief peut être revu par modélisation, animation et intégration sans débat sur l’équilibrage.

## 9. Références dimensionnelles et ergonomie

Une image isolée ne fournit pas une mesure. La perspective, la focale, le recadrage et l’absence d’objet étalon déforment les proportions apparentes. Pour chaque objet, réunir :

- une fiche fabricant ou muséale lorsque disponible ;
- une photographie avec échelle connue ;
- une vue orthographique ou un dessin coté ;
- une comparaison avec une main et un personnage de référence ;
- une source distincte pour les mécanismes ou attaches ;
- une note d’incertitude pour chaque dimension extrapolée.

L’ergonomie de jeu est ensuite comparée au réel. Une poignée réaliste peut être trop fine pour la silhouette, les gants, le rig ou la caméra. Toute adaptation est documentée comme décision artistique, jamais dissimulée comme mesure historique.

> **[LECTURE] Fiche dimensionnelle — Ne pas saisir.**

```yaml
asset_id: AST-TOOL-SURVEY-HAMMER-001
unit: meter
dimensions:
  total_length:
    value: null
    source: pending
    confidence: unknown
  handle_diameter:
    value: null
    source: pending
    confidence: unknown
  head_width:
    value: null
    source: pending
    confidence: unknown
ergonomic_checks:
  - dominant_hand_clearance
  - glove_clearance
  - wrist_rotation
  - silhouette_at_gameplay_camera
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** `meter` impose la convention métrique du projet.
- **Valeurs nulles :** `null` indique une mesure absente ; ce n’est ni zéro ni une valeur par défaut.
- **Confiance :** chaque dimension sépare la valeur, la source et la confiance.
- **Contrôles :** l’ergonomie inclut la main, le gant, le poignet et la caméra.
- **Résultat attendu :** aucune modélisation finale ne commence tant que les dimensions prioritaires restent inconnues.

## 10. Provenance des références

Les références d’objets peuvent contenir marques, dessins industriels, œuvres protégées ou documents restreints. Le registre conserve :

- URL ou emplacement interne ;
- auteur, titulaire ou institution ;
- date d’accès ;
- licence ou statut ;
- restrictions de copie et de redistribution ;
- usage autorisé dans le projet ;
- transformations appliquées ;
- décision : accepté, limité, remplacé ou bloqué.

Une photographie d’un objet ne transfère pas automatiquement les droits sur la photographie, le design, la marque ou le modèle 3D. Les références bloquées peuvent guider une recherche ultérieure mais ne deviennent pas des sources de production.

> **[LECTURE] Entrée de provenance — Ne pas saisir.**

```yaml
reference_id: AST-REF-PROP-001
asset_scope: AST-PROP-LANTERN-001
source_uri: pending
source_kind: museum_catalog
rights_status: unqualified
allowed_use:
  internal_reference: false
  redistribution: false
brand_review: pending
transformations: []
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** `asset_scope` relie la référence à un objet sans en faire la source unique.
- **Booléens :** `false` interdit l’usage tant que les droits ne sont pas qualifiés.
- **Liste :** `transformations` est vide parce qu’aucune transformation n’est encore documentée.
- **Décision :** `blocked` est cohérent avec `unqualified` et `pending`.

## 11. Échelle et gabarit de contrôle

Dans Blender, vérifier :

1. unités métriques du fichier ;
2. dimensions globales de l’objet ;
3. échelle du personnage de référence ;
4. dimensions de la main et des gants ;
5. hauteur de pose sur une table ou au sol ;
6. passage par une porte ou un couloir lorsque pertinent ;
7. silhouette dans les caméras de dialogue et de gameplay.

Créer des gabarits simples : boîte englobante, cylindre de poignée, volumes de doigts et repères de sol. Ces gabarits ne deviennent pas des collisions automatiquement. Ils servent à vérifier l’échelle avant le détail.

> **[LECTURE] Rapport d’échelle — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
scene_unit: meter
reference_character: AST-HUMAN-BASE-001
reference_hand: hand_l
checks:
  overall_dimensions: pending
  forearm_clearance: pending
  torso_clearance: pending
  camera_readability: pending
approval: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Références :** le personnage et la main donnent un contexte reproductible.
- **Statuts :** chaque contrôle peut être fermé indépendamment.
- **Approbation :** `blocked` empêche une décision globale tant que les contrôles restent en attente.
- **Limite :** le rapport ne contient aucune statistique de protection ou de combat.

## 12. Axes, orientation et origine

L’origine est un contrat d’échange, pas un point décoratif. Avant de la placer, décider :

- l’orientation avant de l’objet ;
- l’axe vertical ;
- le sens d’insertion dans une main ou un support ;
- le plan de pose ;
- la rotation attendue des pièces mobiles ;
- le repère qui doit rester stable entre variantes et LOD.

Dans Blender, les objets exportés doivent respecter la convention du projet sans parent correctif destiné à masquer un axe erroné. Une origine canonique est souvent placée au pivot principal ou à un point stable de fabrication. Les besoins locaux de prise ou de rangement sont portés par des sockets séparés.

> **[LECTURE] Contrat d’orientation — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
coordinate_contract:
  forward_axis: project_forward
  up_axis: project_up
  unit: meter
origin:
  role: canonical_object_origin
  location_rule: base_center
  immutable_after_publication: true
validation:
  blender_gizmo: pending
  godot_gizmo: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** les axes utilisent les conventions du projet plutôt qu’une rotation corrective locale.
- **Origine :** `base_center` rend la pose sur une surface vérifiable.
- **Immutabilité :** le booléen protège les animations, sockets et variantes après publication.
- **Validation :** les deux gizmos doivent être comparés après l’import GLB.

## 13. Taxonomie des pivots

Un objet peut avoir plusieurs pivots fonctionnels sans déplacer son origine canonique :

- pivot de prise ;
- pivot de rotation d’une poignée ;
- pivot de charnière ;
- pivot de pose ;
- pivot de suspension ;
- pivot de prévisualisation ;
- pivot de montage dans l’environnement.

Dans Blender, représenter ces pivots avec des objets vides nommés. Leur transform local doit être lisible et leur parent explicite. Éviter d’appliquer les transformations sans comprendre les conséquences sur les enfants.

> **[LECTURE] Hiérarchie Blender proposée — Ne pas saisir.**

```text
AST_PROP_LANTERN_ROOT
├── GEO_render
├── GEO_handle
├── PIVOT_handle
├── SOCKET_grip_primary
├── SOCKET_mount_base
├── SOCKET_mount_hanging
├── SOCKET_light_origin
├── COL_interaction_proxy
└── COL_physics_proxy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** `AST_PROP_LANTERN_ROOT` porte l’identité et l’origine canonique.
- **Préfixes :** `GEO`, `PIVOT`, `SOCKET` et `COL` séparent les responsabilités.
- **Parentage :** la poignée géométrique et son pivot restent distingués pour la rotation.
- **Résultat attendu :** la hiérarchie permet de retrouver automatiquement les repères sans interpréter le nom du maillage.

## 14. Conventions de sockets

Un socket contient au minimum :

- identifiant stable ;
- rôle ;
- parent ;
- transform local ;
- axe d’insertion ou de sortie ;
- contexte d’usage ;
- morphologie ou rig de référence ;
- état de validation.

Adopter des noms explicites :

- `SOCKET_grip_primary` ;
- `SOCKET_grip_secondary` ;
- `SOCKET_storage_back` ;
- `SOCKET_storage_belt` ;
- `SOCKET_sheath_entry` ;
- `SOCKET_mount_environment` ;
- `SOCKET_emission` ;
- `SOCKET_vfx_impact`.

> **[LECTURE] Manifeste de sockets — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
sockets:
  - id: SOCKET_grip_primary
    role: primary_hand_alignment
    parent: root
    direction_axis: insertion_forward
    status: pending
  - id: SOCKET_emission
    role: visual_emission_origin
    parent: barrel_visual
    direction_axis: emission_forward
    status: pending
  - id: SOCKET_mount_environment
    role: static_display_mount
    parent: root
    direction_axis: mount_normal
    status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liste :** chaque entrée de `sockets` est un mapping indépendant.
- **Parent :** le socket d’émission suit la pièce visuelle concernée ; les autres suivent la racine.
- **Direction :** l’axe est nommé pour être inspecté, pas déduit de la position seule.
- **Frontière :** `visual_emission_origin` prépare VFX et gameplay sans créer de projectile.

## 15. Prise principale et prise secondaire

La prise principale doit être revue avec :

- main ouverte ;
- main fermée ;
- gant ou morphologie épaisse ;
- flexion et extension du poignet ;
- rotation de l’avant-bras ;
- caméra proche ;
- silhouette de gameplay.

La prise secondaire n’est pas une copie. Elle peut définir une orientation différente, une zone glissante, une sangle ou un maintien temporaire. Une arme fictive ou un outil à deux mains n’est accepté qu’après validation des deux prises et de la distance entre les mains.

> **[LECTURE] Profil de prise — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
grips:
  primary:
    socket: SOCKET_grip_primary
    reference_bone: hand_l
    finger_clearance: pending
    wrist_clearance: pending
  secondary_support:
    socket: SOCKET_forearm_support
    reference_bone: forearm_l
    strap_clearance: pending
pose_set: AST-POSE-PROP-GRIP-001-v001
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mappings :** `primary` et `secondary_support` possèdent des responsabilités différentes.
- **Os :** les références servent au test, sans modifier le rig.
- **Dégagements :** `pending` interdit d’affirmer que doigts, poignet et sangle sont compatibles.
- **Jeu de poses :** l’identifiant rend la revue reproductible.

## 16. Rangement, fourreaux et montures

Le rangement doit préciser :

- socket sur l’objet ;
- socket correspondant sur le personnage ou l’environnement ;
- orientation d’insertion ;
- profondeur ;
- dégagement avec le corps et les vêtements ;
- animation candidate ;
- état visible ou masqué ;
- combinaison compatible.

Un fourreau possède une entrée, un axe et une profondeur. Un simple point ne suffit pas. Une monture murale ou une table possède une normale et une zone de contact. Les ajustements restent dans un profil d’intégration, pas dans l’origine canonique de l’objet.

> **[LECTURE] Contrat de rangement — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
storage_profile:
  object_socket: SOCKET_sheath_entry
  character_socket: SOCKET_storage_belt_l
  insertion_axis: sheath_forward
  insertion_depth: pending
  clothing_clearance: pending
  animation_alignment: pending
  compatible_wearable_profiles: []
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Deux repères :** l’objet et le personnage conservent chacun leur socket.
- **Profondeur :** la valeur reste inconnue tant que fourreau et animation ne sont pas testés.
- **Compatibilité :** la liste vide n’autorise aucune combinaison par défaut.
- **Frontière :** le profil décrit un alignement visuel, pas la règle métier qui équipe l’objet.

## 17. Pièces mobiles et dégagements

Les pièces mobiles possibles incluent poignée, couvercle, charnière, levier, sangle, aiguille, bouton ou panneau. Pour chaque pièce :

- axe ou contrainte candidate ;
- amplitude visuelle ;
- volume balayé ;
- collisions potentielles ;
- position neutre ;
- position de rangement ;
- représentation LOD ;
- animation future propriétaire.

Le chapitre ne crée pas les contrôleurs finaux. Il prépare une hiérarchie et des repères que les chapitres de rig et d’animation pourront consommer.

> **[LECTURE] Profil de pièce mobile — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
moving_part:
  id: handle
  pivot: PIVOT_handle
  candidate_axis: local_x
  visual_range_deg: pending
  swept_volume_review: pending
  neutral_pose: down
  lod_policy: preserve_until_lod2
  animation_owner: chapter_20
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Axe candidat :** `local_x` doit être confirmé par le gizmo et l’orientation exportée.
- **Amplitude :** aucune valeur angulaire n’est inventée.
- **Volume balayé :** la revue détecte les intersections avec le corps ou l’environnement.
- **Propriétaire :** l’animation finale reste explicitement hors du chapitre.

## 18. Silhouette et lisibilité de fonction

Une silhouette doit communiquer la fonction avant les détails :

- poignée identifiable ;
- tête, lame, surface de protection ou source lumineuse lisible ;
- orientation avant/arrière compréhensible ;
- zone de manipulation distincte de la zone active ;
- échelle crédible par rapport au personnage ;
- état rangé reconnaissable ;
- variantes liées à la même identité.

Tester en aplats sous trois vues et aux distances prévues. Les détails tertiaires ne corrigent pas une poignée trop courte, une tête trop légère visuellement ou un bouclier sans orientation claire.

> **[LECTURE] Carte de silhouette — Ne pas saisir.**

```yaml
asset_id: AST-TOOL-SURVEY-HAMMER-001
primary_shapes:
  - elongated_handle
  - weighted_head
secondary_shapes:
  - grip_zone
  - head_transition
readability_tests:
  side_silhouette: pending
  front_silhouette: pending
  gameplay_distance: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Formes :** les listes séparent masses principales et transitions secondaires.
- **Tests :** les vues et la distance sont contrôlées indépendamment.
- **État :** aucune silhouette n’est déclarée lisible avant capture.
- **Résultat attendu :** l’outil paraît fonctionnel sans texture ni détail fin.

## 19. Blockout métrique

Le blockout utilise des primitives séparées pour :

- volumes principaux ;
- poignée ;
- pièces mobiles ;
- zone de contact ;
- gabarit de main ;
- gabarit d’environnement ;
- encombrement rangé ;
- enveloppe de mouvement.

Conserver les dimensions dans un rapport, pas uniquement dans le fichier Blender. Une capture orthographique avec règle et gizmo complète le rapport.

> **[LECTURE] Journal de blockout — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
blockout_version: v001
unit: meter
primary_volume: pending
handle_volume: pending
base_contact: pending
swept_handle_envelope: pending
captures:
  front: missing
  side: missing
  perspective_with_hand: missing
review: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** chaque reprise de proportions crée une nouvelle version identifiable.
- **Volumes :** les valeurs restent en attente jusqu’à leur mesure dans Blender.
- **Captures :** `missing` distingue une preuve absente d’un contrôle échoué.
- **Décision :** `blocked` interdit de passer à la production détaillée.

## 20. Topologie et séparation des pièces

La topologie dépend de l’usage :

- zones rigides : plans stables et arêtes contrôlées ;
- poignées : section régulière et biseaux lisibles ;
- charnières : pièces séparées et pivots cohérents ;
- sangles : géométrie ou cartes selon distance ;
- petites fixations : géométrie seulement si la silhouette ou l’ombre le justifie ;
- surfaces cachées : suppression uniquement après preuve qu’elles ne sont jamais visibles ;
- variantes : composants modulaires plutôt que duplication complète lorsque pertinent.

Les opérations génériques de retopologie, UV et baking restent au chapitre 17. Ici, la topologie est décrite par sa fonction et ses frontières de pièces.

> **[LECTURE] Profil de topologie — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
components:
  shield_body:
    behavior: rigid
    silhouette_priority: high
  grip:
    behavior: rigid
    hand_clearance_priority: high
  strap:
    behavior: deformable_candidate
    silhouette_priority: medium
hidden_surface_policy: review_required
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Composants :** chaque pièce possède un comportement et une priorité distincts.
- **Rigidité :** `rigid` décrit la déformation attendue, pas une collision physique.
- **Politique :** aucune surface cachée n’est supprimée par défaut.
- **Résultat attendu :** la topologie peut être revue sans connaître les statistiques de protection.

## 21. Ombrage, biseaux et normales

Les objets rigides réalistes ont rarement des arêtes mathématiquement infinies. Les biseaux :

- capturent la lumière ;
- clarifient les assemblages ;
- évitent une silhouette artificiellement tranchante ;
- consomment de la géométrie ;
- doivent rester cohérents entre LOD.

Les normales pondérées ou personnalisées ne compensent pas une mauvaise silhouette. Vérifier les transformations avant d’appliquer des modificateurs dépendants de l’échelle. Le chapitre 17 approfondit les tangentes et le baking.

> **[LECTURE] Profil d’ombrage — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
shading_profile:
  bevel_strategy: measured_from_scale
  weighted_normals: candidate
  hard_edges: reviewed_with_uv_seams
  transformation_scale: must_be_applied_before_final_review
lod_consistency: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Biseau :** la largeur doit dériver de l’échelle, pas d’une valeur copiée entre objets.
- **Candidat :** `weighted_normals` reste une option à comparer.
- **Arêtes :** leur relation avec les UV est renvoyée au chapitre spécialisé.
- **Précondition :** l’échelle doit être cohérente avant la revue finale des modificateurs.

## 22. Matériaux, atlas et variantes

Le chapitre attribue des familles matérielles provisoires : métal peint, métal nu, bois, cuir, verre, tissu, plastique fictif ou surface émissive. Il ne recrée pas le pipeline PBR du chapitre 16.

Pour chaque objet, documenter :

- nombre de surfaces ;
- familles matérielles ;
- transparence ;
- double face ;
- émission ;
- variantes de couleur ;
- stratégie d’atlas ;
- consolidation prévue par LOD ;
- mémoire provisoire ;
- preuves sous plusieurs éclairages.

> **[LECTURE] Profil matériel provisoire — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
material_slots:
  - painted_metal
  - glass
  - emissive_core
transparency:
  glass: alpha_or_transmission_to_qualify
emission:
  source_socket: SOCKET_light_origin
  gameplay_light_authority: excluded
atlas_candidate: true
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Surfaces :** les trois emplacements correspondent à des comportements visuels distincts.
- **Qualification :** le verre reste à comparer dans Godot avant de choisir son mode.
- **Émission :** le socket localise la source visuelle sans créer la logique d’éclairage ou d’énergie.
- **Atlas :** `true` autorise une étude ; il ne prouve ni gain ni compatibilité.

## 23. Volumes de détection d’interaction

Un volume d’interaction sert à détecter une proximité, une sélection ou un rayon. Il n’empêche pas nécessairement un corps de traverser l’objet. Dans Godot, une `Area3D` avec `CollisionShape3D` peut représenter ce volume, mais la logique d’interaction reste dans le Livre II.

Le profil précise :

- but ;
- forme ;
- couches et masques candidats ;
- distance de sélection ;
- accessibilité depuis plusieurs angles ;
- relation avec les pièces mobiles ;
- état selon le LOD.

> **[LECTURE] Profil d’interaction — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
interaction_volume:
  node_type: Area3D
  shape_candidate: capsule
  purpose: selection_and_proximity
  collision_layer: pending
  collision_mask: pending
  lod_policy: preserve_while_interactable
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœud :** `Area3D` détecte des superpositions sans devenir un corps physique.
- **Forme :** la capsule est un candidat simple à ajuster.
- **Couches :** aucune valeur n’est inventée avant l’intégration au projet.
- **LOD :** le volume est conservé tant que l’objet reste interactif.

## 24. Collisions physiques

Une collision physique correspond au comportement attendu :

- objet posé : boîte, capsule ou combinaison simple ;
- bouclier : forme convexe simplifiée si une interaction physique le justifie ;
- objet décoratif immobile : collision statique qualifiée ;
- petit objet tenu : collision parfois désactivée pendant l’attache ;
- objet complexe : plusieurs primitives plutôt qu’un maillage concave dynamique.

Les primitives sont rapides et prévisibles. Les formes convexes sont plus coûteuses mais adaptées à certaines silhouettes. Les formes concaves sont réservées aux corps statiques appropriés. La collision générée depuis le maillage de rendu sert au diagnostic initial et doit être remplacée ou explicitement qualifiée.

> **[LECTURE] Profil de collision physique — Ne pas saisir.**

```yaml
asset_id: AST-TOOL-SURVEY-HAMMER-001
physics_collision:
  representation: compound_primitives
  parts:
    - role: handle
      shape: capsule
    - role: head
      shape: box
  non_uniform_scale_allowed: false
  generated_mesh_collision: diagnostic_only
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Représentation :** deux primitives suivent mieux les masses qu’une forme unique.
- **Liste :** chaque partie associe un rôle à une forme candidate.
- **Échelle :** `false` bloque les transforms non uniformes sur les nœuds de collision.
- **Diagnostic :** une collision générée ne peut pas être promue automatiquement.

## 25. Proxies d’impact et point d’émission

Le proxy d’impact et le point d’émission ne définissent pas la résolution du combat. Ils permettent :

- une revue visuelle de l’alignement ;
- une zone candidate pour les animations ;
- une origine de VFX ;
- une entrée pour les systèmes métier futurs ;
- une capture de validation.

Pour une lame fictive, le proxy peut suivre sa longueur sans fournir de dégâts. Pour un dispositif fictif, `SOCKET_emission` fournit position et orientation sans créer projectile, cadence, portée ou munition.

> **[LECTURE] Profil d’émission et d’impact — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
emission:
  socket: SOCKET_emission
  direction_axis: emission_forward
  visual_debug_length_m: provisional
  authoritative_projectile: excluded
impact_proxy:
  shape_candidate: capsule
  purpose: alignment_debug_only
  damage_authority: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Direction :** l’axe est explicite et doit être vérifié par un gizmo.
- **Longueur :** `provisional` représente un guide visuel, pas une portée.
- **Exclusions :** projectile et dégâts restent absents du contrat.
- **Résultat attendu :** animation et VFX disposent d’un repère sans duplication métier.

## 26. Intégration aux mains et au squelette

Deux stratégies principales :

1. l’objet est enfant d’un `BoneAttachment3D` lié à l’os de main ;
2. l’objet est placé par un système d’équipement dans un nœud de socket déjà attaché au squelette.

Le chapitre documente les transforms d’ajustement sans décider des règles d’équipement. Le profil inclut :

- rig et os de référence ;
- socket objet ;
- socket personnage ;
- transform d’ajustement ;
- main dominante ;
- prise secondaire ;
- poses validées ;
- animation candidate ;
- statut.

> **[LECTURE] Profil d’attache à la main — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
attachment_profile:
  reference_rig: AST-RIG-HUMAN-001
  bone: hand_r
  character_socket: SOCKET_hand_r
  object_socket: SOCKET_grip_primary
  adjustment_transform: pending
  secondary_grip: not_applicable
  pose_set: AST-POSE-PROP-GRIP-001-v001
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Deux sockets :** le profil aligne un repère du personnage avec un repère de l’objet.
- **Transform :** l’ajustement local reste dans le profil et ne déplace pas l’origine canonique.
- **Sentinelle :** `not_applicable` distingue l’absence voulue d’une donnée inconnue.
- **Jeu de poses :** l’identifiant relie la validation future aux mêmes conditions.

## 27. États visuels et dégradation

Les états visuels possibles :

- propre ;
- poussiéreux ;
- mouillé ;
- usé ;
- ébréché ;
- fissuré ;
- éteint ou allumé ;
- ouvert ou fermé ;
- incomplet ;
- réparation visible.

Ils peuvent être réalisés par matériau, decal, masque, géométrie, pièce alternative ou paramètre de shader. Le chapitre ne stocke ni durabilité courante ni règle de transition. Le système métier choisira l’état visuel par identifiant.

> **[LECTURE] Manifeste d’états visuels — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
visual_states:
  clean:
    material_variant: MAT_LANTERN_CLEAN
  worn:
    material_variant: MAT_LANTERN_WORN
  damaged_visual:
    mesh_variant: GEO_LANTERN_DAMAGED
  lit:
    material_variant: MAT_LANTERN_LIT
business_state_fields: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clés :** chaque état visuel possède un identifiant stable.
- **Ressources :** les états peuvent sélectionner un matériau ou un maillage.
- **Exclusion :** aucun compteur de durabilité ou déclencheur métier n’est stocké.
- **Résultat attendu :** l’intégration peut demander un état par identifiant sans réécrire l’asset.

## 28. Variantes sans duplication métier

Une variante visuelle peut changer :

- couleur ;
- finition ;
- gravure ;
- culture fictive ;
- niveau d’entretien ;
- accessoire décoratif ;
- état de surface ;
- silhouette secondaire.

Elle ne crée pas automatiquement une nouvelle définition métier. Le manifeste sépare :

- `asset_variant_id` ;
- `content_definition_ref` ;
- différences visuelles ;
- composants partagés ;
- matériaux ;
- LOD ;
- preuves.

> **[LECTURE] Variante visuelle — Ne pas saisir.**

```yaml
asset_variant_id: AST-PROP-LANTERN-001-BRASS
base_asset: AST-PROP-LANTERN-001
content_definition_ref: ITEM_LANTERN_STANDARD
visual_changes:
  - brass_finish
  - blue_glass_tint
shared_geometry: true
shared_collision_profile: pending
new_gameplay_definition: false
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence métier :** la variante pointe vers une définition sans recopier ses champs.
- **Changements :** la liste décrit uniquement les différences visuelles.
- **Partage :** géométrie et collision sont qualifiées séparément.
- **Booléen :** `false` empêche de créer une nouvelle règle de jeu par accident.

## 29. LOD géométriques et fonctionnels

Un LOD d’objet ne consiste pas seulement à réduire les triangles. Il doit préserver selon le contexte :

- silhouette ;
- poignée ou zone de prise ;
- pièces mobiles visibles ;
- socket d’attache actif ;
- point d’émission actif ;
- interaction ;
- collision physique ;
- état visuel ;
- matériaux essentiels.

Un objet équipé à moyenne distance n’a pas les mêmes besoins qu’un objet décoratif lointain. Documenter plusieurs représentations :

- `equipped_close` ;
- `equipped_gameplay` ;
- `world_interactable` ;
- `world_distant` ;
- `inventory_preview` si réellement utilisée.

> **[LECTURE] Profil LOD — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
representations:
  equipped_close:
    lod: LOD0
    required_sockets: [SOCKET_grip_primary, SOCKET_emission]
  equipped_gameplay:
    lod: LOD1
    required_sockets: [SOCKET_grip_primary, SOCKET_emission]
  world_interactable:
    lod: LOD1
    required_nodes: [InteractionArea]
  world_distant:
    lod: LOD2
    required_sockets: []
thresholds: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Représentations :** chaque contexte associe un LOD à ses fonctions requises.
- **Sockets :** prise et émission restent présentes tant que l’objet est équipé.
- **Nœuds :** l’aire d’interaction est conservée pour l’objet sélectionnable.
- **Seuils :** les distances restent à mesurer dans Godot.

## 30. Collisions et états selon le LOD

Les collisions et états ne suivent pas obligatoirement la géométrie :

- une collision simple peut être partagée entre LOD ;
- un objet distant peut perdre son interaction ;
- un objet équipé conserve ses prises ;
- un point d’émission reste requis tant que VFX ou gameplay le consomment ;
- une dégradation fine peut être fusionnée dans le matériau ;
- une pièce mobile peut devenir statique à distance ;
- la transition ne doit pas déplacer l’objet.

> **[LECTURE] Matrice fonctionnelle des représentations — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
representations:
  equipped_gameplay:
    render: LOD1
    interaction: disabled
    physics_collision: disabled_while_attached
    light_origin: preserved
    visual_state: preserved
  world_interactable:
    render: LOD1
    interaction: enabled
    physics_collision: enabled
    light_origin: preserved
    visual_state: preserved
  world_distant:
    render: LOD2
    interaction: disabled
    physics_collision: static_or_disabled_to_measure
    light_origin: candidate_for_removal
    visual_state: simplified
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Découplage :** rendu, interaction, physique, lumière et état possèdent des politiques indépendantes.
- **Attache :** la collision peut être désactivée pendant que l’objet suit la main.
- **Distance :** la suppression du repère lumineux reste une décision à mesurer.
- **Résultat attendu :** chaque représentation possède un contrat vérifiable.

## 31. Collection d’export et GLB

La collection `__EXPORT` contient uniquement :

- racine de l’objet ;
- géométries retenues ;
- pièces mobiles ;
- LOD si le profil d’export les inclut ;
- objets vides représentant pivots et sockets ;
- propriétés personnalisées qualifiées ;
- matériaux pris en charge.

Elle exclut :

- références ;
- gabarits de main ;
- guides de mesure ;
- caches ;
- sauvegardes ;
- collisions de diagnostic non retenues ;
- données privées de provenance.

Les propriétés personnalisées peuvent être exportées comme `extras` glTF lorsque le preset le prévoit. Elles restent des métadonnées, pas une garantie d’interprétation automatique par Godot.

> **[LECTURE] Manifeste d’export — Ne pas saisir.**

```yaml
export_id: AST-PROP-EXPORT-001-v001
asset_id: AST-PROP-LANTERN-001
source_blend: art/blender/props/AST-PROP-KIT-EXPLORER-001/lantern.blend
collection: __EXPORT
container: GLB
include:
  - render_meshes
  - moving_parts
  - sockets
  - qualified_custom_properties
exclude:
  - references
  - measurement_guides
  - diagnostic_collisions
  - caches
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** le fichier Blender reste distinct du conteneur GLB.
- **Collection :** l’export est fondé sur un contrat nommé, pas une sélection manuelle.
- **Listes :** `include` et `exclude` rendent le périmètre explicite.
- **État :** le GLB ne peut pas être déclaré produit avant exécution et inspection.

## 32. Scène Godot importée et scène dérivée

Godot importe le GLB comme ressource générée. Ne pas modifier cette scène comme source principale. Créer une scène héritée ou une scène enveloppe qui ajoute :

- `Area3D` d’interaction ;
- collisions physiques ;
- marqueurs de debug ;
- profil d’attache ;
- LOD et plages de visibilité ;
- état visuel ;
- métadonnées de validation ;
- scripts de test.

Cette séparation protège les réimports. Les ajustements artistiques retournent dans Blender ; les nœuds moteur restent dans la scène dérivée.

> **[LECTURE] Hiérarchie Godot dérivée — Ne pas saisir.**

```text
PropDerivedRoot (Node3D)
├── ImportedProp (instance GLB)
├── InteractionArea (Area3D)
│   └── CollisionShape3D
├── PhysicsBody (StaticBody3D ou RigidBody3D selon profil)
│   └── CollisionShape3D
├── SocketDebug (Node3D)
├── LODController (Node3D)
└── ValidationMetadata (Node)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** la scène dérivée possède le transform d’intégration sans réécrire le GLB.
- **Instance :** `ImportedProp` reste remplaçable lors d’un réimport.
- **Responsabilités :** interaction et physique utilisent des branches distinctes.
- **Profil :** le type de corps dépend de l’usage validé, pas du nom de l’objet.

## 33. Contrat de scène Godot

Le contrat JSON ou YAML décrit les nœuds attendus sans supposer leur présence :

> **[LECTURE] Contrat de scène — Ne pas saisir.**

```yaml
scene_id: AST-PROP-SCENE-LANTERN-001
asset_id: AST-PROP-LANTERN-001
imported_scene: res://art/exports/props/AST-PROP-KIT-EXPLORER-001/lantern.glb
derived_scene: res://tests/art/props/lantern_validation.tscn
required_nodes:
  - ImportedProp
  - InteractionArea
  - PhysicsBody
required_sockets:
  - SOCKET_grip_primary
  - SOCKET_mount_base
  - SOCKET_mount_hanging
  - SOCKET_light_origin
collision_profiles:
  interaction: AST-COL-INTERACT-LANTERN-001-v001
  physics: AST-COL-PHYS-LANTERN-001-v001
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemins :** import et scène dérivée sont explicitement séparés.
- **Listes :** nœuds et sockets requis alimentent le validateur structurel.
- **Profils :** interaction et physique renvoient vers deux contrats différents.
- **État :** la scène reste bloquée tant que chemins et nœuds ne sont pas matérialisés.

## 34. Validateur GDScript structurel

Créer **[VSC]** `tests/art/props/prop_asset_validator.gd`.

> **[LECTURE] Exemple GDScript — Ne pas saisir sans créer le fichier indiqué.**

```gdscript
class_name PropAssetValidator
extends RefCounted

const REQUIRED_SOCKET_PREFIX: String = "SOCKET_"

func validate_prop(root: Node, profile: Dictionary) -> Dictionary:
    var errors: Array[String] = []
    var warnings: Array[String] = []

    if root == null:
        errors.append("PROP_ROOT_MISSING")
        return _result(errors, warnings)

    _check_required_nodes(root, profile, errors)
    _check_required_sockets(root, profile, errors)
    _check_collision_shapes(root, errors, warnings)
    _check_lod_contract(root, profile, errors, warnings)

    return _result(errors, warnings)

func _check_required_nodes(
    root: Node,
    profile: Dictionary,
    errors: Array[String]
) -> void:
    var required: Array = profile.get("required_nodes", [])
    for node_name_value: Variant in required:
        var node_name := StringName(str(node_name_value))
        if root.find_child(String(node_name), true, false) == null:
            errors.append("REQUIRED_NODE_MISSING:%s" % node_name)

func _check_required_sockets(
    root: Node,
    profile: Dictionary,
    errors: Array[String]
) -> void:
    var required: Array = profile.get("required_sockets", [])
    var found := _collect_named_nodes(root, REQUIRED_SOCKET_PREFIX)
    for socket_value: Variant in required:
        var socket_name := StringName(str(socket_value))
        if not found.has(socket_name):
            errors.append("REQUIRED_SOCKET_MISSING:%s" % socket_name)

func _collect_named_nodes(root: Node, prefix: String) -> Dictionary:
    var result: Dictionary = {}
    for child: Node in root.get_children():
        if child.name.begins_with(prefix):
            result[child.name] = child
        var descendants := _collect_named_nodes(child, prefix)
        result.merge(descendants, true)
    return result

func _check_collision_shapes(
    root: Node,
    errors: Array[String],
    warnings: Array[String]
) -> void:
    for node: Node in root.find_children("*", "CollisionShape3D", true, false):
        var collision := node as CollisionShape3D
        if collision == null:
            continue
        if collision.shape == null:
            errors.append("COLLISION_SHAPE_RESOURCE_MISSING:%s" % collision.get_path())
        if not _is_uniform_scale(collision.scale):
            errors.append("COLLISION_NON_UNIFORM_SCALE:%s" % collision.get_path())
        if collision.disabled:
            warnings.append("COLLISION_DISABLED:%s" % collision.get_path())

func _is_uniform_scale(value: Vector3) -> bool:
    return is_equal_approx(value.x, value.y) and is_equal_approx(value.y, value.z)

func _check_lod_contract(
    root: Node,
    profile: Dictionary,
    errors: Array[String],
    warnings: Array[String]
) -> void:
    var lod_root_name := StringName(str(profile.get("lod_root", "")))
    if lod_root_name == StringName():
        warnings.append("LOD_ROOT_NOT_DECLARED")
        return

    var lod_root := root.find_child(String(lod_root_name), true, false)
    if lod_root == null:
        errors.append("LOD_ROOT_MISSING:%s" % lod_root_name)
        return

    var expected_lods: Array = profile.get("expected_lods", [])
    for lod_value: Variant in expected_lods:
        var lod_name := StringName(str(lod_value))
        if lod_root.find_child(String(lod_name), true, false) == null:
            errors.append("LOD_NODE_MISSING:%s" % lod_name)

func _result(errors: Array[String], warnings: Array[String]) -> Dictionary:
    return {
        "status": "blocked" if not errors.is_empty() else "reviewable",
        "errors": errors,
        "warnings": warnings,
        "error_count": errors.size(),
        "warning_count": warnings.size(),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe et héritage :** `class_name` rend le validateur référençable ; `RefCounted` convient à un service sans présence dans l’arbre.
- **Entrées :** `validate_prop` reçoit `root: Node`, racine de la scène dérivée, et `profile: Dictionary`, contrat chargé depuis des données validées.
- **Retour :** la fonction renvoie toujours un `Dictionary` structuré ; une racine nulle provoque un retour anticipé avec `PROP_ROOT_MISSING`.
- **Collections typées :** `Array[String]` limite erreurs et avertissements à des chaînes ; `Dictionary` associe des clés aux résultats.
- **Lecture défensive :** `profile.get("required_nodes", [])` renvoie une liste vide si la clé manque ; les valeurs sont converties vers `StringName` après lecture comme `Variant`.
- **Recherche :** `find_child(name, true, false)` cherche récursivement sans exiger que le nœud soit possédé par la scène éditée.
- **Sockets :** `_collect_named_nodes` descend récursivement, sélectionne les noms commençant par `SOCKET_`, puis fusionne les dictionnaires descendants.
- **Paramètres de `merge` :** le second argument `true` autorise les descendants à remplacer une clé identique ; un doublon de nom doit donc être traité par une règle supplémentaire si le projet l’interdit.
- **Collisions :** `find_children("*", "CollisionShape3D", true, false)` collecte les nœuds du type demandé ; le cast `as CollisionShape3D` est vérifié avant usage.
- **Invariants :** une ressource `shape` est obligatoire et l’échelle locale du nœud doit rester uniforme.
- **Opérateurs :** `and` exige les deux comparaisons approximatives ; `not` inverse `is_empty()` ou `has()` ; `==` compare la sentinelle vide ou l’absence d’un nœud.
- **LOD :** une racine non déclarée produit un avertissement, tandis qu’une racine déclarée mais absente produit une erreur.
- **Condition ternaire :** le statut vaut `blocked` si la liste d’erreurs n’est pas vide, sinon `reviewable` ; ce dernier statut n’est pas une acceptation runtime.
- **Effets de bord :** le script ne modifie aucun nœud ; il remplit seulement les listes locales et renvoie un rapport.
- **Limites :** il ne vérifie ni qualité artistique, ni alignement des mains, ni collision réelle, ni performance, ni autorité métier.

## 35. Rapport JSON du validateur

Le rapport sérialise le résultat sans modifier les assets.

> **[LECTURE] Exemple de sortie — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "asset_id": "AST-PROP-LANTERN-001",
  "scene": "res://tests/art/props/lantern_validation.tscn",
  "status": "blocked",
  "errors": [
    "REQUIRED_SOCKET_MISSING:SOCKET_mount_hanging"
  ],
  "warnings": [
    "LOD_ROOT_NOT_DECLARED"
  ],
  "metrics": {
    "error_count": 1,
    "warning_count": 1
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** `schema_version` prépare les migrations futures du format.
- **Identité :** l’asset et la scène sont enregistrés avec le résultat.
- **Listes :** erreurs et avertissements gardent des codes stables et contextualisés.
- **Métriques :** les compteurs sont dérivés du contenu, pas saisis manuellement dans l’implémentation.
- **Décision :** un socket requis absent maintient le statut `blocked`.

## 36. Tests d’alignement et grille de poses

La grille minimale comprend :

- pose neutre ;
- bras détendu ;
- coude fléchi ;
- poignet en flexion et extension ;
- rotation de l’avant-bras ;
- main ouverte ;
- main fermée ;
- prise proche du visage ;
- objet rangé ;
- transition tenue vers rangée à préparer ;
- silhouette à la caméra de gameplay ;
- plan rapproché.

Les animations finales appartiennent au chapitre 20. Ici, des poses statiques ou captures intermédiaires suffisent à repérer pénétrations, orientation inversée et dégagement insuffisant.

> **[LECTURE] Rapport de poses — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
pose_set: AST-POSE-PROP-GRIP-001-v001
checks:
  neutral_grip: pending
  wrist_flexion: pending
  forearm_rotation: pending
  near_face_clearance: pending
  sheathed_alignment: pending
  gameplay_silhouette: pending
captures: []
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Jeu de poses :** l’identifiant garantit que plusieurs objets sont comparés dans les mêmes conditions.
- **Contrôles :** chaque pose révèle un risque différent.
- **Captures :** la liste vide indique qu’aucune preuve n’est produite.
- **Statut :** aucun alignement n’est revendiqué avant les captures.

## 37. Tests d’environnement et d’interaction

Tester l’objet :

- au sol ;
- sur table ;
- contre un mur ;
- suspendu si prévu ;
- près d’un autre objet ;
- dans une porte ou un passage étroit ;
- avec raycast ou volume de proximité du système d’interaction ;
- avec collision active et inactive ;
- dans chaque représentation LOD ;
- sous plusieurs éclairages.

Le test vérifie position, orientation, stabilité, accessibilité, collision et lisibilité. Il ne valide pas la logique métier de collecte ou d’usage.

> **[LECTURE] Matrice d’environnement — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
contexts:
  floor:
    mount_socket: SOCKET_mount_base
    physics: pending
  table:
    mount_socket: SOCKET_mount_base
    physics: pending
  hanging:
    mount_socket: SOCKET_mount_hanging
    physics: pending
  held:
    mount_socket: SOCKET_grip_primary
    physics: disabled_candidate
interaction_detection: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contextes :** chacun nomme le socket et le comportement physique candidat.
- **Attache :** le contexte tenu utilise la prise, pas le pivot de pose.
- **Candidat :** la désactivation physique pendant l’attache reste à mesurer.
- **Frontière :** la détection est testée sans exécuter l’ajout à l’inventaire.

## 38. Campagne de performance

Mesurer séparément :

- triangles et sommets par LOD ;
- surfaces et draw calls ;
- taille des textures et mémoire ;
- nombre de nœuds ;
- nombre et type de formes de collision ;
- coût des objets physiques actifs ;
- coût des aires d’interaction ;
- temps d’import ;
- temps de chargement ;
- coût d’un objet tenu ;
- coût d’un groupe d’objets au sol ;
- transitions LOD ;
- overdraw des surfaces transparentes ou émissives.

Les budgets sont des hypothèses jusqu’à mesure sur la Radeon RX 6750 XT, le Ryzen 7 2700 et les profils de plateforme retenus.

> **[LECTURE] Plan de benchmark — Ne pas saisir.**

```yaml
benchmark_id: AST-BENCH-PROPS-001-v001
scenarios:
  single_equipped_close:
    object_count: 1
    status: pending
  room_with_interactable_props:
    object_count: pending
    status: pending
  distant_prop_cluster:
    object_count: pending
    status: pending
metrics:
  - cpu_frame_time
  - gpu_frame_time
  - vram
  - draw_calls
  - collision_count
  - load_time
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénarios :** gros plan, pièce interactive et groupe distant isolent des coûts différents.
- **Quantités :** seule la scène à objet unique possède une quantité déterminée ; les autres restent à fixer.
- **Métriques :** les noms décrivent des mesures à collecter, pas des valeurs attendues.
- **Décision :** le benchmark reste bloqué sans scènes et captures réelles.

## 39. Parcours Solo et Studio

### 39.1 Mode Solo

- limiter la bibliothèque aux objets réellement visibles dans le vertical slice ;
- partager conventions de pivots, sockets et rapports ;
- produire un objet complet avant de multiplier les variantes ;
- préférer des collisions simples ;
- réutiliser des matériaux maîtres qualifiés ;
- mesurer un petit nombre de scénarios représentatifs ;
- conserver les inconnues plutôt que créer de faux niveaux de précision.

### 39.2 Mode Studio

- assigner un propriétaire par catégorie ;
- faire relire échelle et ergonomie par animation et intégration ;
- versionner les conventions de pivots et sockets ;
- partager des profils de collision ;
- automatiser la validation structurelle ;
- conserver une bibliothèque de gabarits approuvés ;
- séparer création, lookdev, collisions et intégration ;
- exiger des scènes de test communes ;
- publier les versions approuvées comme immuables ;
- gérer les changements d’origine comme ruptures de contrat.

## 40. Porte d’acceptation

Un objet ne passe à l’état accepté que si :

- le brief fonctionnel est approuvé ;
- les références et droits sont qualifiés ;
- les dimensions prioritaires sont mesurées ;
- l’échelle est revue avec personnage, main et environnement ;
- origine, axes et pivots sont approuvés ;
- les sockets requis existent et sont orientés ;
- les prises sont testées ;
- les pièces mobiles ont leurs dégagements ;
- la silhouette est lisible ;
- la géométrie et les matériaux respectent le profil ;
- interaction, physique et impact sont séparés ;
- les collisions sont qualifiées ;
- les états visuels et variantes sont traçables ;
- les LOD préservent les fonctions requises ;
- le GLB est exporté et inspecté ;
- la scène Godot dérivée est matérialisée ;
- le validateur est exécuté ;
- les poses et environnements sont testés ;
- les performances sont mesurées ;
- les réserves bloquantes sont fermées.

> **[LECTURE] Porte de décision — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
gates:
  brief: pending
  rights: pending
  dimensions: pending
  pivots_and_sockets: pending
  geometry_and_materials: pending
  collisions: pending
  lod: pending
  glb_export: pending
  godot_scene: pending
  alignment_tests: pending
  performance: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portes :** chaque domaine peut être fermé indépendamment par une preuve.
- **Statut :** `pending` représente une preuve absente, pas un échec.
- **Décision :** `blocked` reste obligatoire tant qu’une porte n’est pas acceptée.
- **Responsabilité :** la décision finale nécessite une revue humaine.

## 41. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 41.1 Modéliser depuis une image sans échelle

**Symptôme :** l’objet paraît plausible seul mais devient minuscule ou surdimensionné dans la main.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reference:
  source: perspective_image
  known_dimension: none
  confidence: high
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une image en perspective sans référence mesurée ne fournit pas d’échelle fiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reference:
  sources:
    - dimensioned_record
    - scaled_photograph
  unknown_dimensions: documented
  confidence: pending_review
hand_scale_test: required
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction croise des références, consigne l’incertitude et exige un test avec la main du projet.

### 41.2 Déplacer l’origine pour corriger une seule animation

**Symptôme :** la variante corrigée ne s’aligne plus avec le fourreau, les LOD ou les autres scènes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
origin_change:
  reason: one_animation_misaligned
  published_contract_review: skipped
  socket_updates: none
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’origine est un contrat partagé ; la modifier pour un cas local déplace toutes les dépendances.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
origin_change:
  action: preserve_canonical_origin
  integration_adjustment_profile: AST-ATTACH-BLADE-001-v002
  animation_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve la source et place l’ajustement dans un profil local versionné.

### 41.3 Utiliser le même repère pour prise et rangement

**Symptôme :** l’objet est correct dans la main mais traverse le corps lorsqu’il est rangé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
sockets:
  grip_primary: SOCKET_shared
  storage_belt: SOCKET_shared
  insertion_axis: unspecified
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La prise et le rangement ont des orientations et profondeurs différentes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
sockets:
  grip_primary: SOCKET_grip_primary
  storage_belt: SOCKET_sheath_entry
  insertion_axis: sheath_forward
storage_test: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare les repères et rend l’axe d’insertion vérifiable.

### 41.4 Promouvoir la collision générée depuis le maillage

**Symptôme :** la physique devient coûteuse ou instable pour un objet pourtant simple.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
physics_collision:
  source: render_mesh_generated
  simplification_review: none
  dynamic_use: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La géométrie de rendu n’est ni simplifiée ni qualifiée pour la physique.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
physics_collision:
  source: compound_primitives
  generated_collision_use: diagnostic_only
  dynamic_use_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise des primitives contrôlables et limite la génération automatique au diagnostic.

### 41.5 Appliquer une échelle non uniforme à CollisionShape3D

**Symptôme :** la collision ne correspond plus visuellement à sa forme ou produit un comportement imprévisible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
collision_node:
  scale: [1.0, 0.5, 2.0]
  shape_resource_updated: false
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une `CollisionShape3D` mise à l’échelle différemment sur chaque axe peut se comporter de manière imprévisible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
collision_node:
  scale: [1.0, 1.0, 1.0]
  shape_resource_updated: true
  visual_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve une échelle uniforme et modifie la ressource de forme elle-même.

### 41.6 Définir dégâts et portée dans le manifeste visuel

**Symptôme :** deux fichiers deviennent propriétaires de valeurs de combat différentes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
damage: 24
reach_m: 1.2
attack_speed: 1.5
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le manifeste d’asset devient une seconde autorité de combat et mélange apparence et règles métier.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
content_definition_ref: ITEM_SHORT_BLADE_STANDARD
visual_profiles:
  - AST-BLADE-VISUAL-CLEAN-001
combat_values: excluded
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve un lien vers la définition métier sans recopier ses valeurs.

### 41.7 Utiliser un seul volume pour interaction, physique et impact

**Symptôme :** agrandir la zone de sélection élargit aussi la collision et le proxy d’impact.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
volumes:
  universal:
    purpose: [interaction, physics, impact]
    shape: render_mesh
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les trois usages ont des besoins de précision, coût et autorité différents.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
volumes:
  interaction: AST-COL-INTERACT-001
  physics: AST-COL-PHYS-001
  impact_debug: AST-COL-IMPACT-DEBUG-001
authoritative_damage: excluded
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction attribue un profil distinct à chaque responsabilité.

### 41.8 Orienter le point d’émission à l’œil

**Symptôme :** le VFX paraît correct dans Blender mais part latéralement après import.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
emission_socket:
  position_review: passed
  direction_axis: assumed
  godot_gizmo_review: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une position correcte ne garantit pas une orientation cohérente entre Blender et Godot.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
emission_socket:
  position_review: pending
  direction_axis: emission_forward
  blender_gizmo_review: required
  godot_gizmo_review: required
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction documente l’axe et exige une inspection du gizmo après import.

### 41.9 Supprimer les prises dans les LOD

**Symptôme :** l’objet distant fonctionne, mais le même LOD utilisé en main se détache ou revient à l’origine.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod1:
  geometry: simplified
  sockets: removed
  allowed_contexts: [equipped, distant]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le même LOD ne peut pas être réutilisé comme objet équipé s’il a perdu ses repères fonctionnels.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod1:
  geometry: simplified
  sockets: [SOCKET_grip_primary]
  allowed_contexts: [equipped]
lod2:
  sockets: []
  allowed_contexts: [world_distant]
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite le LOD au contexte distant et conserve le socket encore utile.

### 41.10 Déclarer l’objet terminé après la revue Blender

**Symptôme :** l’objet paraît correct dans Blender mais ses pivots, collisions et LOD n’ont jamais été vérifiés dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
alignment_tests: not_executed
performance_test: not_executed
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une revue DCC ne prouve ni l’échange GLB, ni la scène dérivée, ni les mesures moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
alignment_tests: not_executed
performance_test: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction maintient le blocage jusqu’aux preuves Godot et aux mesures.

## 42. Livrables à conserver

Le plan maître exige cinq livrables permanents :

1. **bibliothèque d’objets pilotes** — sources, manifestes, variantes et exports ;
2. **conventions de pivots et sockets** — axes, noms, parents, transforms et usages ;
3. **collisions** — profils d’interaction, physique et impact ;
4. **LOD** — géométrie, matériaux, fonctions, seuils et mesures ;
5. **scènes Godot d’équipement** — imports, scènes dérivées, attaches, collisions et rapports.

L’arborescence du début du chapitre devient l’inventaire permanent. Les sources restent distinctes des exports et les rapports QA internes ne sont pas ajoutés au manuel lecteur.

> **[LECTURE] Manifeste de livraison — Ne pas saisir.**

```yaml
deliverable_manifest: AST-PROP-DELIVERY-001-v001
pilot_library:
  id: AST-PROP-KIT-EXPLORER-001
  status: blocked
pivot_socket_conventions:
  profile: AST-PROP-SOCKET-CONVENTIONS-001-v001
  status: blocked
collisions:
  profiles:
    - AST-COL-INTERACTION-PROPS-001-v001
    - AST-COL-PHYSICS-PROPS-001-v001
    - AST-COL-IMPACT-DEBUG-PROPS-001-v001
  status: blocked
lod:
  profile: AST-PROP-LOD-001-v001
  status: blocked
godot_scenes:
  lab: AST-PROP-VALIDATION-LAB-001
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifeste :** les cinq livrables sont regroupés sous un identifiant versionné.
- **Profils :** collisions d’interaction, de physique et d’impact restent séparées.
- **État :** chaque livrable demeure bloqué jusqu’à sa matérialisation.
- **Traçabilité :** le manifeste sert d’entrée à la revue de production.

## 43. Synthèse opérationnelle pour Project Asteria

Le chapitre 12 fournit à `Project Asteria` une méthode complète pour produire des objets individuels. La bibliothèque de l’Explorateur est encadrée par des briefs fonctionnels, des références qualifiées, des fiches dimensionnelles, des gabarits, une convention d’axes, des origines, des pivots, des sockets de prise, rangement, environnement et émission, des pièces mobiles, des profils de silhouette, de topologie, d’ombrage, de matériaux, de collisions, d’états, de variantes, de LOD, d’export et d’intégration Godot.

La bibliothèque reste bloquée tant que les objets, dimensions, pivots, sockets, géométries, matériaux, collisions, états, variantes, LOD, GLB, scènes Godot, alignements et mesures ne sont pas réellement produits. Le chapitre prépare les rigs, animations, VFX et systèmes métier sans définir leurs contrôleurs, statistiques ou décisions.

## 44. Références techniques officielles

Les références suivantes doivent être consultées et qualifiées lors de la matérialisation :

- [Blender Manual — Object Origin](https://docs.blender.org/manual/en/latest/scene_layout/object/origin.html) ;
- [Blender Manual — Transform](https://docs.blender.org/manual/en/latest/scene_layout/object/editing/transform/introduction.html) ;
- [Blender Manual — Empty Objects](https://docs.blender.org/manual/en/latest/modeling/empties.html) ;
- [Blender Manual — Custom Properties](https://docs.blender.org/manual/en/latest/files/custom_properties.html) ;
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html) ;
- [Godot 4.7 — Importing 3D scenes](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html) ;
- [Godot 4.7 — Import configuration](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html) ;
- [Godot 4.7 — BoneAttachment3D](https://docs.godotengine.org/en/4.7/classes/class_boneattachment3d.html) ;
- [Godot 4.7 — Marker3D](https://docs.godotengine.org/en/4.7/classes/class_marker3d.html) ;
- [Godot 4.7 — Area3D](https://docs.godotengine.org/en/4.7/classes/class_area3d.html) ;
- [Godot 4.7 — CollisionShape3D](https://docs.godotengine.org/en/4.7/classes/class_collisionshape3d.html) ;
- [Godot 4.7 — Shape3D](https://docs.godotengine.org/en/4.7/classes/class_shape3d.html) ;
- [Godot — Mesh level of detail](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html) ;
- [Godot — Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html).

Les pages `latest` ou `stable` ne sont utilisées que lorsqu’aucune page versionnée équivalente n’est exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d’appliquer la procédure.
