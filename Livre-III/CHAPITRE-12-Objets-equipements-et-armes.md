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

- d’une direction artistique et d’un registre de provenance ;
- d’un système d’unités et d’axes validé par le chapitre 4 ;
- d’une main, d’un squelette et de noms d’os de référence ;
- d’un inventaire des interactions prévues, sans leurs règles métier ;
- d’un budget provisoire par plateforme ;
- d’une scène Godot de personnage et d’une scène d’environnement de test ;
- des conventions de matériaux, même si leur production détaillée appartient au chapitre 16.

Le lecteur ouvre :

- **[APP] Blender 5.2.0** pour les références, le blockout, les pivots, les pièces mobiles et les exports ;
- **[APP] Godot 4.7.1-stable** pour la scène dérivée, les attaches, collisions, LOD et mesures ;
- **[VSC] Visual Studio Code** pour les contrats YAML, manifestes JSON et le validateur GDScript ;
- **[PS] PowerShell 7** pour créer les dossiers et lancer les contrôles documentaires ;
- **[WEB] navigateur** uniquement pour les documentations officielles et les références dont la licence est enregistrée.

> **[PS] Créer l’arborescence de travail.**

```powershell
$paths = @(
    "art/blender/props/AST-PROP-KIT-EXPLORER-001",
    "art/props/briefs",
    "art/props/dimensions",
    "art/props/pivots",
    "art/props/sockets",
    "art/props/collisions",
    "art/props/states",
    "art/props/materials",
    "art/props/lod",
    "art/exports/props",
    "tests/art/props/reports",
    "tests/art/props/captures"
)

foreach ($path in $paths) {
    New-Item -ItemType Directory -Path $path -Force | Out-Null
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `$paths` est un tableau de chaînes contenant des chemins relatifs au dépôt.
- **Boucle :** `foreach` traite chaque chemin sans dépendre de l’ordre du système de fichiers.
- **Paramètres :** `-Force` rend la création idempotente et `Out-Null` masque les objets retournés.
- **Effet de bord :** les dossiers sont créés ; aucun fichier source ou export n’est produit.
- **Résultat attendu :** les sources Blender restent séparées des contrats, exports, rapports et captures.

> **[LECTURE] Arborescence canonique — Ne pas saisir.**

```text
art/
├── blender/props/
│   └── AST-PROP-KIT-EXPLORER-001/
├── props/
│   ├── briefs/
│   ├── dimensions/
│   ├── pivots/
│   ├── sockets/
│   ├── collisions/
│   ├── states/
│   ├── materials/
│   └── lod/
├── exports/props/
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

- **Sources :** les `.blend` restent sous `art/blender/props` et ne sont jamais remplacés par un export.
- **Contrats :** dimensions, pivots, sockets, collisions, états et LOD possèdent des dossiers séparés.
- **Tests :** scène, script, rapports et captures sont regroupés sous `tests/art/props`.
- **Publication :** les preuves internes ne sont pas ajoutées au manuel lecteur.

## 6. Bibliothèque pilote et cas d’usage

La bibliothèque pilote ne cherche pas à couvrir tout le catalogue du jeu. Elle sélectionne cinq objets qui exercent des contraintes différentes et réutilisables :

| Objet | Cas principal | Contraintes révélées |
|---|---|---|
| Lanterne | tenir, poser, suspendre | poignée, gravité visuelle, point lumineux, base stable |
| Marteau d’arpentage | tenir, ranger | prise unique, tête lourde, centre de masse visuel |
| Lame courte fictive | tenir, rengainer | garde, prise, fourreau, silhouette |
| Bouclier léger | main secondaire | prise décentrée, avant-bras, surface large |
| Dispositif à impulsion fictif | tenir, viser visuellement | prise, point d’émission, pièce mobile, repère VFX |

Chaque objet reçoit un identifiant stable, une fonction observable, des interactions prévues, des états visuels et des limites. Une entrée de catalogue n’accorde aucune capacité de gameplay ; elle décrit uniquement ce que l’asset doit permettre de tester.

> **[LECTURE] Manifeste initial de la bibliothèque — Ne pas saisir.**

```yaml
library_id: AST-PROP-KIT-EXPLORER-001
version: 1
assets:
  - id: AST-PROP-LANTERN-001
    category: held_and_placeable
    priority: high
  - id: AST-TOOL-SURVEY-HAMMER-001
    category: held_tool
    priority: high
  - id: AST-WPN-SHORT-BLADE-001
    category: held_weapon_visual
    priority: high
  - id: AST-EQP-BUCKLER-001
    category: offhand_equipment
    priority: medium
  - id: AST-DEVICE-PULSE-001
    category: fictional_emitter_device
    priority: medium
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `library_id` et chaque `id` sont stables et indépendants du nom affiché.
- **Types :** `version` est un entier ; `assets` est une liste de dictionnaires ; les autres valeurs sont des chaînes.
- **Priorité :** `priority` ordonne la production sans signifier que l’asset est accepté.
- **État :** `blocked` reste obligatoire tant que les assets et preuves n’existent pas.
- **Frontière :** `held_weapon_visual` ne contient aucune donnée de dégâts ou de combat.

## 7. Vocabulaire fonctionnel

Avant de modéliser, distinguer les termes suivants :

- **origine d’objet** : repère de transformation principal exporté avec l’objet ;
- **pivot fonctionnel** : point autour duquel une rotation ou un placement doit être évalué ;
- **socket** : repère nommé servant à attacher un autre nœud ou à aligner l’objet ;
- **prise principale** : repère de la main qui porte l’objet ;
- **prise secondaire** : repère optionnel utilisé par une seconde main ;
- **monture** : repère de rangement sur le dos, la ceinture, un fourreau ou l’environnement ;
- **volume de détection** : région utilisée pour détecter une interaction potentielle ;
- **collision physique** : forme participant au moteur physique ;
- **proxy d’impact** : volume descriptif destiné à un futur système autoritaire ;
- **point d’émission** : repère visuel pour VFX, son ou projectile futur ;
- **état visuel** : variante de représentation sans décision métier ;
- **LOD** : représentation simplifiée sélectionnée selon distance, taille écran ou profil.

Un même emplacement ne doit pas recevoir plusieurs responsabilités implicites. L’origine peut coïncider avec la prise principale, mais seulement si ce choix est documenté et reste stable.

## 8. Brief fonctionnel par objet

Le brief transforme une intention narrative en observations testables. Il évite les formulations comme « faire une belle épée » ou « rendre la lanterne réaliste », qui ne donnent aucune décision de production.

> **[LECTURE] Brief fonctionnel de la lanterne — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
functions:
  - held_in_right_hand
  - placed_on_flat_surface
  - suspended_from_hook
visual_invariants:
  - handle_clears_fingers
  - base_remains_stable
  - light_origin_stays_inside_lantern
moving_parts:
  - handle
required_sockets:
  - grip_primary
  - mount_hook
  - light_origin
forbidden_claims:
  - runtime_light_validated
  - physics_stability_measured
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonctions :** `functions` énumère des usages observables sans règles métier.
- **Invariants :** `visual_invariants` décrit ce qui doit rester vrai dans chaque usage.
- **Pièces mobiles :** `moving_parts` force la création d’un pivot distinct pour la poignée.
- **Sockets :** les noms sont des contrats de scène et doivent rester stables après publication.
- **Réserves :** `forbidden_claims` interdit de présenter une hypothèse comme un résultat exécuté.

> **[LECTURE] Brief fonctionnel de la lame courte — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
functions:
  - held_primary
  - stored_in_sheath
  - displayed_on_table
visual_invariants:
  - grip_axis_matches_hand_contract
  - guard_clears_fingers
  - blade_enters_sheath_without_intersection
required_sockets:
  - grip_primary
  - sheath_entry
  - sheath_mount
excluded_data:
  - damage
  - reach
  - attack_speed
  - durability_rules
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Usage :** tenir, ranger et exposer sont trois configurations visuelles distinctes.
- **Alignement :** l’axe de prise et l’entrée du fourreau sont testés sans définir d’animation finale.
- **Exclusions :** `excluded_data` protège la frontière avec inventaire et combat.
- **Décision :** l’asset reste bloqué jusqu’aux tests Blender et Godot.

## 9. Références dimensionnelles et ergonomie

Une image de concept ne constitue pas une mesure. La perspective, la focale, les proportions stylisées et l’absence d’échelle peuvent produire des erreurs importantes. Les dimensions proviennent de sources qualifiées, de mesures internes cohérentes ou de comparaisons avec la main et le personnage de référence.

Pour chaque objet, enregistrer :

- longueur, largeur, hauteur et épaisseur maximales ;
- dimensions de la zone de prise ;
- dégagement nécessaire aux doigts et aux articulations ;
- distance entre prise et centre de masse visuel ;
- rayon d’encombrement pendant les poses ;
- hauteur de pose au sol ou sur support ;
- tolérances de fourreau, support ou monture ;
- incertitude et origine de chaque valeur.

> **[LECTURE] Fiche dimensionnelle — Ne pas saisir.**

```yaml
asset_id: AST-TOOL-SURVEY-HAMMER-001
unit: meter
dimensions:
  overall_length: 0.42
  head_width: 0.14
  grip_length: 0.13
  grip_diameter: 0.032
reference_basis:
  - internal_character_hand_profile
  - licensed_tool_reference_set
uncertainty:
  overall_length: provisional
  grip_diameter: provisional
review:
  hand_clearance: pending
  pose_alignment: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** `unit: meter` rend les nombres comparables avec Blender et Godot.
- **Dimensions :** les valeurs sont des nombres décimaux provisoires, pas des vérités universelles.
- **Sources :** `reference_basis` relie la fiche au profil de main et aux références autorisées.
- **Incertitude :** chaque valeur non mesurée est explicitement marquée `provisional`.
- **Blocage :** la revue des doigts et des poses est obligatoire avant acceptation.

## 10. Provenance des références

Chaque planche, photographie, scan ou modèle externe possède une fiche de provenance. Une référence peut être consultée sans être redistribuable ; un modèle acheté peut être utilisable sans autoriser sa republication comme source.

> **[LECTURE] Entrée de provenance — Ne pas saisir.**

```yaml
reference_id: REF-PROP-HAMMER-001
kind: dimensional_reference
source_uri: pending_private_registry
author: pending
rights_holder: pending
licence_id: pending
allowed_uses:
  - internal_reference
redistribution:
  source_image: false
  derived_measurements: pending
review_owner: art_legal
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** auteur, titulaire des droits, licence et usages autorisés restent distincts.
- **Confidentialité :** `source_uri` pointe vers un registre privé plutôt que vers un document sensible dans le dépôt public.
- **Redistribution :** l’image et les mesures dérivées peuvent avoir des statuts différents.
- **Responsabilité :** `review_owner` nomme le rôle qui doit fermer l’incertitude.
- **État :** une licence ou un titulaire inconnu maintient la référence bloquée.

## 11. Échelle et gabarit de contrôle

Dans Blender, importer ou lier le gabarit de main et le personnage de référence sans modifier leur source. Placer l’objet dans une collection de travail et comparer sa boîte englobante au profil dimensionnel.

Contrôler au minimum :

1. l’unité de scène et l’échelle d’objet ;
2. la longueur réelle de la boîte englobante ;
3. le dégagement des doigts en pose neutre ;
4. l’encombrement dans les poses de marche, course et interaction ;
5. la hauteur de pose au sol ;
6. la cohérence avec les objets proches du décor.

> **[LECTURE] Rapport d’échelle — Ne pas saisir.**

```json
{
  "asset_id": "AST-PROP-LANTERN-001",
  "source_unit": "meter",
  "object_scale": [1.0, 1.0, 1.0],
  "bounding_box_m": [0.18, 0.18, 0.31],
  "checks": {
    "hand_clearance": "pending",
    "ground_contact": "pending",
    "character_ratio": "pending"
  },
  "status": "blocked"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tableaux :** `object_scale` et `bounding_box_m` sont des listes ordonnées de trois nombres.
- **Invariant :** l’échelle exportée doit rester uniforme et documentée.
- **Contrôles :** les chaînes `pending` empêchent une validation implicite.
- **Résultat attendu :** le rapport compare la source Blender au gabarit sans modifier l’un ou l’autre.

## 12. Axes, orientation et origine

Le projet fixe une convention unique pour les objets tenus. Le sens exact dépend du pipeline du chapitre 4 ; le chapitre 12 ne le redéfinit pas. Chaque objet enregistre cependant :

- l’axe longitudinal ;
- le sens « avant » ;
- le sens « haut » ;
- la position de l’origine ;
- la rotation au repos ;
- la transformation attendue au socket de main.

L’origine ne doit pas être déplacée après publication sans nouvelle version, car les scènes, animations et attaches peuvent dépendre de sa transformation.

> **[LECTURE] Contrat d’orientation — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
coordinate_contract: AST-COORD-OBJECT-001-v001
longitudinal_axis: local_z
forward_direction: local_negative_z
up_direction: local_y
origin_role: grip_primary
rest_transform:
  position_m: [0.0, 0.0, 0.0]
  rotation_deg: [0.0, 0.0, 0.0]
  scale: [1.0, 1.0, 1.0]
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat partagé :** `coordinate_contract` renvoie vers la convention du pipeline plutôt que de la recopier.
- **Repères :** les axes sont des chaînes explicites, pas une interprétation visuelle.
- **Transformation :** position, rotation et échelle sont trois listes de nombres séparées.
- **Invariant :** une échelle uniforme et une origine stable sont exigées.
- **Réserve :** les valeurs doivent être contrôlées après import GLB.

## 13. Taxonomie des pivots

Un objet peut nécessiter plusieurs pivots sans déplacer son origine principale :

- `pivot_primary` — origine ou pivot principal de placement ;
- `pivot_moving_<name>` — pivot d’une pièce mobile ;
- `pivot_ground` — repère de pose au sol ;
- `pivot_display` — repère d’exposition ;
- `pivot_storage` — repère de rangement ;
- `pivot_environment` — repère d’ancrage au décor.

Dans Blender, une origine d’objet appartient à l’objet. Les repères secondaires sont représentés par des objets vides nommés et orientés. Ils doivent rester sans échelle non uniforme.

> **[LECTURE] Hiérarchie Blender proposée — Ne pas saisir.**

```text
AST-PROP-LANTERN-001
├── GEO_lantern_body
├── GEO_lantern_handle
├── PIVOT_handle
├── SOCKET_grip_primary
├── SOCKET_mount_hook
├── SOCKET_light_origin
└── COLLISION_proxy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hiérarchie :** le corps, la poignée, les repères et la collision restent des objets distincts.
- **Pivot mobile :** `PIVOT_handle` porte l’axe de rotation de la poignée.
- **Sockets :** le préfixe `SOCKET_` facilite la lecture et la validation automatique.
- **Collision :** `COLLISION_proxy` ne remplace pas le maillage de rendu.
- **Résultat attendu :** l’export conserve une structure assez explicite pour être contrôlée dans Godot.

## 14. Conventions de sockets

Un socket est un repère transformé, nommé et versionné. Il ne contient pas de règle métier. Les noms de base proposés sont :

| Socket | Usage visuel |
|---|---|
| `grip_primary` | main porteuse |
| `grip_secondary` | seconde main optionnelle |
| `mount_belt` | rangement à la ceinture |
| `mount_back` | rangement au dos |
| `mount_sheath` | liaison avec un fourreau |
| `mount_environment` | fixation à un support |
| `interaction_focus` | point de focalisation visuelle |
| `vfx_origin` | point de départ d’un effet |
| `audio_origin` | point d’émission sonore |
| `projectile_origin` | origine descriptive d’un projectile futur |

La présence d’un socket ne garantit pas que le système futur l’utilise. Elle garantit seulement qu’un repère existe et peut être évalué.

> **[LECTURE] Manifeste de sockets — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
sockets:
  grip_primary:
    required: true
    parent: root
  grip_secondary:
    required: false
    parent: root
  vfx_origin:
    required: true
    parent: emitter_head
  audio_origin:
    required: true
    parent: emitter_head
  projectile_origin:
    required: false
    parent: emitter_head
socket_scale_policy: uniform_only
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dictionnaire :** `sockets` associe chaque nom stable à un contrat.
- **Obligation :** `required` est un booléen et distingue les repères indispensables des options.
- **Parent :** le parent explicite suit correctement une pièce mobile.
- **Échelle :** `uniform_only` interdit les transformations susceptibles de déformer l’orientation.
- **Frontière :** `projectile_origin` ne définit ni vitesse, ni trajectoire, ni dégâts.

## 15. Prise principale et prise secondaire

La prise principale doit être testée avec une main réelle du projet, pas avec un cylindre arbitraire. Examiner :

- fermeture des doigts ;
- contact de la paume ;
- dégagement de la garde, du levier ou de la poignée ;
- orientation du poignet ;
- position apparente du centre de masse ;
- absence de pénétration dans l’avant-bras ;
- cohérence en vue première et troisième personne si ces vues existent.

Une prise secondaire est un repère d’aide. Elle ne force pas une animation à deux mains et ne remplace pas l’IK du chapitre 20.

> **[LECTURE] Profil de prise — Ne pas saisir.**

```yaml
profile_id: AST-GRIP-SHORT-BLADE-001-v001
asset_id: AST-WPN-SHORT-BLADE-001
primary:
  socket: grip_primary
  hand_profile: AST-HAND-HUMAN-M-001-v001
  wrist_alignment: pending
  finger_clearance: pending
secondary:
  socket: null
  allowed: false
center_of_mass_visual:
  relation_to_grip: forward
  review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** `hand_profile` lie la prise à une main versionnée.
- **Valeur nulle :** `socket: null` indique qu’aucune prise secondaire n’est prévue.
- **Booléen :** `allowed: false` empêche une interprétation à deux mains.
- **Centre de masse :** la relation est visuelle et ne prétend pas mesurer une masse physique.
- **Blocage :** poignet et doigts doivent être contrôlés avant acceptation.

## 16. Rangement, fourreaux et montures

Un objet rangé utilise un repère différent de la prise. Le fourreau, le crochet ou le support possède son propre socket. Tester :

- l’entrée et la sortie sans intersection ;
- la profondeur de rangement ;
- la cohérence avec les vêtements du chapitre 11 ;
- le dégagement pendant la marche et l’accroupissement ;
- la visibilité des pièces identitaires ;
- les variantes de morphologie autorisées.

> **[LECTURE] Contrat de rangement — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
storage:
  carrier_asset: AST-WEAR-SHEATH-SHORT-001
  object_socket: mount_sheath
  carrier_socket: sheath_entry
  insertion_axis: local_negative_z
  depth_m: provisional
  clearance_review: pending
  wearable_compatibility: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Deux assets :** l’objet et le fourreau conservent des identités séparées.
- **Deux sockets :** chaque côté de la liaison expose son propre repère.
- **Axe :** `insertion_axis` décrit l’orientation sans définir l’animation.
- **Dimension :** `depth_m` reste provisoire jusqu’au test réel.
- **Dépendance :** la compatibilité avec les vêtements doit être relue avec le chapitre 11.

## 17. Pièces mobiles et dégagements

Une pièce mobile possède :

- un pivot local ;
- une plage visuelle candidate ;
- une position de repos ;
- un volume de dégagement ;
- une liste d’éléments susceptibles d’entrer en collision ;
- un statut de validation.

Le chapitre ne définit pas les contrôleurs finaux. Il prépare seulement des transforms et des limites que le rig ou l’animation pourront consommer.

> **[LECTURE] Profil de pièce mobile — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
part: handle
pivot: PIVOT_handle
rest_rotation_deg: 0.0
candidate_range_deg:
  min: -75.0
  max: 75.0
clearance_against:
  - lantern_body
  - character_hand
  - character_forearm
animation_owner: chapter_20
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plage candidate :** `min` et `max` sont des nombres provisoires, pas des limites finales.
- **Dégagement :** `clearance_against` indique les géométries à vérifier.
- **Responsabilité :** `animation_owner` réserve le contrôleur final au chapitre 20.
- **Résultat attendu :** la poignée peut être testée sans intégrer de logique runtime.
- **Réserve :** aucune collision ni animation n’est annoncée comme exécutée.

## 18. Silhouette et lisibilité de fonction

La silhouette doit indiquer rapidement :

- où l’objet se tient ;
- quelle extrémité est fonctionnelle ;
- quelles pièces sont mobiles ;
- comment il se pose ou se range ;
- quel côté est orienté vers l’avant ;
- quels détails disparaîtront dans les LOD.

La lisibilité n’exige pas d’exagérer chaque détail. Elle exige de hiérarchiser les masses principales, les vides utiles et les contrastes de matériau.

> **[LECTURE] Carte de silhouette — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
primary_shape: shallow_disc
functional_cues:
  - forearm_clearance
  - central_grip
  - reinforced_rim
identity_cues:
  - asymmetrical_notch
  - radial_boss
lod_protection:
  - outer_contour
  - boss_volume
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Forme primaire :** `primary_shape` décrit la masse dominante.
- **Indices fonctionnels :** `functional_cues` expliquent la prise et la protection visuelle sans statistique.
- **Identité :** `identity_cues` contient les traits qui distinguent l’objet.
- **LOD :** `lod_protection` indique les volumes à préserver lors de la simplification.
- **État :** la silhouette doit être capturée et comparée avant acceptation.

## 19. Blockout métrique

Le blockout utilise des primitives et des valeurs lisibles. Il doit démontrer :

- dimensions globales ;
- prise et orientation ;
- centre de masse visuel ;
- pièces mobiles ;
- pose au sol ;
- rangement ;
- interactions avec la main, l’avant-bras et le décor.

Ne pas détailler les vis, gravures ou dommages avant cette validation. Une erreur de longueur ou de pivot ne sera pas corrigée par un matériau plus riche.

> **[LECTURE] Journal de blockout — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
blockout_version: 1
checks:
  dimensions_match_profile: pending
  grip_clearance: pending
  handle_rotation: pending
  ground_stability: pending
  hook_mount: pending
  character_silhouette: pending
decision: blocked
review_notes: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** `blockout_version` augmente lorsque les volumes fonctionnels changent.
- **Contrôles :** chaque vérification possède un statut indépendant.
- **Décision :** `blocked` évite de poursuivre par inertie.
- **Notes :** `review_notes` est une liste vide prête à recevoir des observations.
- **Résultat attendu :** le blockout est évalué avant toute finition.

## 20. Topologie et séparation des pièces

La topologie suit l’usage :

- pièces immobiles séparées seulement si cela facilite matériau, LOD ou remplacement ;
- pièces mobiles obligatoirement séparées ou préparées pour une articulation ;
- densité accrue autour des courbes de silhouette et des petits rayons réellement visibles ;
- surfaces planes conservées simples ;
- détails répétitifs déplacés vers texture ou normal lorsque pertinent ;
- normales et arêtes dures contrôlées avant export.

Les choix génériques de retopologie, d’UV et de baking restent au chapitre 17.

> **[LECTURE] Profil de topologie — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
parts:
  body:
    behavior: static
    topology_focus: silhouette_and_bevels
  emitter_head:
    behavior: movable
    topology_focus: pivot_clearance
  trigger_guard:
    behavior: static
    topology_focus: finger_clearance
  indicator:
    behavior: material_state
    topology_focus: minimal_geometry
generic_uv_baking_owner: chapter_17
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Parties :** chaque sous-objet associe comportement et priorité topologique.
- **Pièce mobile :** `emitter_head` reçoit une attention spécifique autour du pivot.
- **Détail matériel :** `indicator` évite une géométrie inutile lorsque le matériau suffit.
- **Frontière :** `generic_uv_baking_owner` réserve la méthode générale au chapitre 17.
- **État :** la topologie n’est pas déclarée créée.

## 21. Ombrage, biseaux et normales

Un objet hard-surface crédible dépend souvent plus de ses transitions que de sa densité brute. Contrôler :

- largeur relative des biseaux ;
- continuité des normales ;
- arêtes réellement coupantes ou volontairement adoucies ;
- absence de facettes sur les courbes importantes ;
- cohérence du tangent space après GLB ;
- silhouette sous lumière rasante.

Le chapitre peut définir un profil spécialisé, mais la bibliothèque PBR et les réglages généraux appartiennent au chapitre 16.

> **[LECTURE] Profil d’ombrage — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
bevel_policy:
  visible_edges: required
  width: provisional
normal_policy:
  custom_normals: candidate
  glb_tangent_review: pending
lighting_tests:
  - soft_front
  - hard_side
  - rim_back
general_pbr_owner: chapter_16
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Biseaux :** la largeur reste provisoire et dépend de l’échelle réelle.
- **Normales :** `custom_normals` est une candidate, pas une obligation universelle.
- **Éclairages :** trois directions révèlent les cassures et facettes.
- **Frontière :** les règles PBR communes restent au chapitre 16.
- **Blocage :** le tangent space doit être comparé dans Godot.

## 22. Matériaux, atlas et variantes

Les objets pilotes utilisent des matériaux provisoires pour distinguer bois, métal, verre, cuir, tissu ou surface émissive. Le chapitre documente les groupes et les besoins, sans établir le pipeline PBR général.

Pour réduire les changements de matériau :

- grouper les surfaces compatibles ;
- partager un atlas seulement entre assets dont les cycles de vie et résolutions sont compatibles ;
- éviter de fusionner un matériau transparent avec un matériau opaque sans justification ;
- préserver les variantes utiles ;
- mesurer draw calls, mémoire et qualité réelle dans Godot.

> **[LECTURE] Profil matériel provisoire — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
material_slots:
  - id: MAT_lantern_metal
    family: painted_metal
  - id: MAT_lantern_glass
    family: transparent_glass
  - id: MAT_lantern_emissive
    family: emissive_insert
atlas_candidate:
  group: AST-ATLAS-PROP-EXPLORER-001
  decision: pending
general_material_owner: chapter_16
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Slots :** chaque matériau possède un identifiant local et une famille.
- **Transparence :** le verre reste séparé pour conserver ses contraintes de rendu.
- **Atlas :** `decision: pending` empêche un regroupement prématuré.
- **Frontière :** le chapitre 16 reste propriétaire des matériaux généraux.
- **Mesure :** l’acceptation dépendra des draw calls et de la mémoire observés.

## 23. Volumes de détection d’interaction

Un volume de détection indique où une interaction peut être proposée. Il ne décide pas si l’action est autorisée. Dans Godot, un `Area3D` peut porter une ou plusieurs `CollisionShape3D`, mais la logique métier doit rester dans le système d’interaction du Livre II.

Le volume doit être :

- assez large pour être accessible ;
- assez précis pour ne pas sélectionner l’objet voisin ;
- distinct du maillage de rendu ;
- aligné avec le point de focalisation ;
- testé dans un environnement encombré.

> **[LECTURE] Profil de détection — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
interaction_area:
  node_type: Area3D
  shape_type: BoxShape3D
  dimensions_m: provisional
  focus_socket: interaction_focus
  collision_layer_profile: AST-LAYER-INTERACTABLE-001-v001
  authorization_owner: Livre_II_interaction_system
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœud :** `Area3D` décrit une région de détection, pas un corps solide.
- **Forme :** `BoxShape3D` est une primitive candidate simple à contrôler.
- **Couche :** le profil de collision est référencé plutôt que codé en nombre arbitraire.
- **Autorité :** l’autorisation reste dans le système d’interaction du Livre II.
- **Réserve :** dimensions et comportement doivent être testés dans la scène.

## 24. Collisions physiques

La collision physique doit correspondre à l’usage et au coût :

- primitives pour les formes simples ;
- plusieurs convexes pour les volumes complexes dynamiques ;
- concave réservée aux géométries statiques lorsque le contrat l’autorise ;
- maillage de rendu jamais accepté automatiquement comme collision finale ;
- échelle uniforme sur `CollisionShape3D` ;
- marge et tolérances mesurées dans la scène.

> **[LECTURE] Profil de collision physique — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
physics_collision:
  body_candidate: RigidBody3D
  shapes:
    - type: CylinderShape3D
      purpose: main_disc
    - type: BoxShape3D
      purpose: central_grip
  mesh_generated_collision: testing_only
  non_uniform_scale: forbidden
  gameplay_authority: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Corps candidat :** `RigidBody3D` reste une hypothèse à qualifier selon l’usage final.
- **Formes :** deux primitives remplacent un maillage concave coûteux.
- **Génération :** `testing_only` interdit de promouvoir automatiquement une collision dérivée du rendu.
- **Échelle :** la non-uniformité est explicitement refusée.
- **Frontière :** la collision ne contient aucune règle de dégâts.

## 25. Proxies d’impact et point d’émission

Un proxy d’impact est un volume descriptif préparé pour un futur système. Il peut représenter une tête d’outil, une surface de bouclier ou une zone de contact. Il ne calcule ni dégâts, ni priorité, ni équipe.

Un point d’émission est un `Marker3D` ou un repère importé. Il indique où placer un VFX, un son ou un projectile futur. Son orientation doit être testée avec un gizmo visible.

> **[LECTURE] Profil d’émission — Ne pas saisir.**

```yaml
asset_id: AST-DEVICE-PULSE-001
emission:
  socket: projectile_origin
  node_type: Marker3D
  forward_axis: local_negative_z
  vfx_socket: vfx_origin
  audio_socket: audio_origin
  trajectory: excluded
  velocity: excluded
  damage: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repère :** `Marker3D` rend la position et l’orientation visibles dans l’éditeur.
- **Axe :** `forward_axis` doit correspondre au contrat exporté.
- **Séparation :** VFX, son et projectile peuvent partager une pièce parente sans partager le même socket.
- **Exclusions :** trajectoire, vitesse et dégâts restent absents.
- **Résultat attendu :** le repère peut être validé sans simuler de tir.

## 26. Intégration aux mains et au squelette

Dans la scène de personnage, l’objet est placé sous un `BoneAttachment3D` lié à l’os de main approprié. Le nœud d’attache suit l’os ; l’objet conserve sa transformation locale de correction.

La correction doit rester dans la scène dérivée ou dans un profil versionné. Ne pas déplacer arbitrairement le pivot source pour corriger un seul personnage.

> **[LECTURE] Hiérarchie d’attache — Ne pas saisir.**

```text
CharacterRoot
└── Skeleton3D
    ├── BoneAttachment3D_HandR
    │   └── EquippedObject
    └── BoneAttachment3D_HandL
        └── OffhandObject
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Squelette :** `BoneAttachment3D` copie la transformation de l’os sélectionné.
- **Main droite :** l’objet principal est instancié sous l’attache correspondante.
- **Main gauche :** l’équipement secondaire possède une branche indépendante.
- **Correction :** les offsets locaux ne modifient pas la source GLB.
- **Frontière :** la sélection d’objet équipé reste une responsabilité du Livre II.

> **[LECTURE] Profil d’attache personnage — Ne pas saisir.**

```yaml
profile_id: AST-ATTACH-SHORT-BLADE-HUMAN-001-v001
asset_id: AST-WPN-SHORT-BLADE-001
skeleton_profile: AST-RIG-HUMAN-001-v001
bone_attachment:
  bone_name: hand_r
  object_socket: grip_primary
local_correction:
  position_m: [0.0, 0.0, 0.0]
  rotation_deg: [0.0, 0.0, 0.0]
  scale: [1.0, 1.0, 1.0]
pose_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Références :** asset, squelette et profil d’attache sont versionnés séparément.
- **Os :** `bone_name` doit exister dans le squelette importé.
- **Socket :** `object_socket` sélectionne la prise de l’objet.
- **Correction locale :** les trois composantes restent explicites et mesurables.
- **Blocage :** la grille de poses doit confirmer l’alignement.

## 27. États visuels et dégradation

Un état visuel décrit une représentation possible :

- intact ;
- utilisé ou sali ;
- usé ;
- endommagé visuellement ;
- éteint ou activé visuellement ;
- ouvert ou fermé ;
- vide ou chargé visuellement, si pertinent.

L’état ne décide pas quand la transition se produit. Il ne contient ni points de durabilité, ni seuil de dégâts, ni consommation. Les règles métier sélectionnent un identifiant d’état ; l’asset fournit la représentation correspondante.

> **[LECTURE] Profil d’états visuels — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
visual_states:
  intact:
    mesh_variant: default
    emissive_variant: off
  lit:
    mesh_variant: default
    emissive_variant: warm
  worn:
    mesh_variant: worn
    emissive_variant: off
  broken_visual:
    mesh_variant: broken
    emissive_variant: off
state_selection_owner: Livre_II_item_runtime
transition_logic: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dictionnaire :** chaque clé d’état associe variantes de maillage et de matériau.
- **Autorité :** `state_selection_owner` indique qui choisira l’état au runtime.
- **Exclusion :** les transitions et seuils ne sont pas définis ici.
- **Réutilisation :** un même maillage peut servir à plusieurs états matériels.
- **État documentaire :** les variantes restent bloquées tant qu’elles ne sont pas produites.

## 28. Variantes sans duplication métier

Une variante visuelle peut changer :

- couleur ;
- finition ;
- gravure ;
- niveau d’usure ;
- emblème ;
- petites pièces décoratives ;
- silhouette secondaire si elle conserve les sockets et collisions.

Elle ne doit pas inventer un nouvel objet métier lorsque seule l’apparence change. Inversement, une géométrie qui modifie fortement prise, encombrement ou collision peut nécessiter un profil d’asset distinct.

> **[LECTURE] Famille de variantes — Ne pas saisir.**

```yaml
family_id: AST-PROP-LANTERN-FAMILY-001-v001
base_asset: AST-PROP-LANTERN-001
variants:
  - id: brass_clean
    geometry_profile: base
    material_profile: brass_clean
  - id: iron_worn
    geometry_profile: base
    material_profile: iron_worn
  - id: hooded
    geometry_profile: hooded
    material_profile: iron_worn
compatibility_invariants:
  - grip_primary
  - mount_hook
  - interaction_collision
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Famille :** les variantes partagent un identifiant de famille et une base.
- **Géométrie :** `hooded` peut modifier une pièce sans changer les contrats indispensables.
- **Invariants :** prises, monture et collision doivent rester compatibles.
- **Frontière :** les différences de statistiques ne figurent pas dans le profil visuel.
- **Décision :** une rupture d’invariant impose un asset ou profil distinct.

## 29. LOD géométriques et fonctionnels

Un LOD ne réduit pas seulement les triangles. Il peut aussi :

- fusionner de petites pièces ;
- supprimer des mécanismes non visibles ;
- réduire le nombre de matériaux ;
- remplacer une transparence par une surface opaque ;
- désactiver un mouvement secondaire ;
- conserver les sockets indispensables ;
- simplifier les collisions ;
- préserver la silhouette et l’orientation fonctionnelle.

Les seuils sont mesurés dans Godot. Une distance copiée depuis un autre projet n’est pas une preuve.

> **[LECTURE] Profil LOD de la lanterne — Ne pas saisir.**

```yaml
asset_id: AST-PROP-LANTERN-001
lod_profiles:
  lod0:
    geometry: full
    materials: 3
    moving_handle: true
    required_sockets:
      - grip_primary
      - mount_hook
      - light_origin
  lod1:
    geometry: simplified
    materials: 2
    moving_handle: false
    required_sockets:
      - grip_primary
      - mount_hook
      - light_origin
  lod2:
    geometry: silhouette_proxy
    materials: 1
    moving_handle: false
    required_sockets:
      - mount_hook
thresholds: pending_measurement
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** chaque LOD combine géométrie, matériaux, mouvements et sockets.
- **Fonction :** les repères indispensables restent présents tant que l’usage les exige.
- **Simplification :** la poignée peut devenir statique lorsque sa mobilité n’est plus perceptible.
- **Seuils :** `pending_measurement` interdit une distance inventée.
- **Résultat attendu :** la silhouette et l’usage restent lisibles malgré la réduction.

## 30. Collisions et états selon le LOD

La collision ne suit pas automatiquement le LOD de rendu. Une collision de gameplay ou d’interaction peut rester stable lorsque le maillage change. Les collisions purement décoratives peuvent être simplifiées ou désactivées, mais cette décision doit être documentée.

> **[LECTURE] Profil de collision par représentation — Ne pas saisir.**

```yaml
asset_id: AST-EQP-BUCKLER-001
representations:
  equipped:
    render_lod: dynamic
    interaction_area: disabled
    physical_collision_profile: equipped_proxy
  dropped_near:
    render_lod: dynamic
    interaction_area: enabled
    physical_collision_profile: dropped_convex
  distant_static:
    render_lod: lod2
    interaction_area: disabled
    physical_collision_profile: static_simple
selection_owner: presentation_layer
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Représentations :** équipé, posé proche et distant statique sont des contextes différents.
- **Détection :** l’`interaction_area` peut être désactivée lorsque l’objet est déjà équipé.
- **Collision :** chaque contexte référence un profil distinct.
- **Autorité :** `presentation_layer` sélectionne la représentation sans modifier l’état métier.
- **Réserve :** les profils doivent être mesurés et testés.

## 31. Collection d’export et GLB

La source Blender contient travail, références, guides et objets exclus. La collection `__EXPORT` ne contient que ce qui doit traverser vers Godot :

- maillages de rendu ;
- pièces mobiles nécessaires ;
- repères exportés ;
- armature éventuelle si réellement requise ;
- propriétés personnalisées qualifiées ;
- collisions explicitement destinées à l’import.

Les propriétés personnalisées peuvent être exportées comme `extras` glTF, mais leur présence doit être vérifiée après import. Un nom ou un champ non normalisé ne devient pas automatiquement un contrat moteur.

> **[LECTURE] Collection d’export — Ne pas saisir.**

```text
__EXPORT
└── AST-PROP-LANTERN-001
    ├── GEO_body
    ├── GEO_handle
    ├── SOCKET_grip_primary
    ├── SOCKET_mount_hook
    ├── SOCKET_light_origin
    └── COLLISION_static_simple
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** `__EXPORT` évite un export manuel variable.
- **Maillages :** corps et poignée restent séparés car la poignée possède un pivot.
- **Repères :** les sockets nécessaires traversent avec des noms stables.
- **Collision :** seule la collision qualifiée est incluse.
- **Exclusion :** références, guides et caches restent hors du GLB.

> **[LECTURE] Preset d’export documentaire — Ne pas saisir.**

```yaml
preset_id: AST-GLTF-PROP-001-v001
format: GLB
selection_source: collection___EXPORT
apply_modifiers: reviewed_per_object
export_custom_properties: true
export_materials: true
export_animations: false
export_cameras: false
export_lights: false
post_export_checks:
  - node_names
  - transforms
  - sockets
  - materials
  - bounds
  - collisions
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conteneur :** `GLB` regroupe la scène et ses données d’échange.
- **Sélection :** la collection dédiée remplace une sélection manuelle.
- **Propriétés :** les propriétés personnalisées sont exportées comme candidates à vérifier.
- **Animations :** elles sont désactivées dans ce preset d’objet statique ou attaché.
- **Contrôles :** l’export n’est accepté qu’après inspection des nœuds, transforms et volumes.

## 32. Scène Godot importée et scène dérivée

Godot importe le GLB comme scène. Cette scène importée peut être régénérée lors d’une réimportation ; elle ne reçoit pas directement les nœuds métier ou les corrections manuelles.

Créer une scène dérivée qui ajoute :

- racine de présentation ;
- collisions et `Area3D` ;
- `Marker3D` de contrôle ;
- nœuds d’éclairage ou VFX provisoires ;
- script de validation ;
- variantes et logique de présentation non autoritaire.

> **[LECTURE] Hiérarchie de scène dérivée — Ne pas saisir.**

```text
PropValidationRoot
├── ImportedObject
├── InteractionArea
│   └── CollisionShape3D
├── PhysicsBodyCandidate
│   └── CollisionShape3D
├── SocketDebug
│   ├── Marker3D_GripPrimary
│   ├── Marker3D_Mount
│   └── Marker3D_Emission
├── CameraRig
├── LightingRig
└── PropAssetValidator
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Import :** `ImportedObject` reste une instance de la scène générée depuis le GLB.
- **Détection :** `InteractionArea` possède sa forme propre.
- **Physique :** le corps candidat et sa collision sont séparés de la détection.
- **Repères :** les `Marker3D` rendent les sockets inspectables.
- **Validation :** le script lit la structure sans modifier l’asset.

## 33. Contrat de scène Godot

Le contrat de scène décrit les nœuds requis selon la catégorie de l’objet. Un objet posé peut exiger une collision physique ; un objet purement attaché peut ne pas en avoir. Les exigences restent déclaratives.

> **[VSC] Créer `tests/art/props/contracts/AST-PROP-LANTERN-001.yaml`.**

```yaml
asset_id: AST-PROP-LANTERN-001
root_type: Node3D
required_nodes:
  - path: ImportedObject
    type: Node3D
  - path: InteractionArea
    type: Area3D
  - path: InteractionArea/CollisionShape3D
    type: CollisionShape3D
required_sockets:
  - grip_primary
  - mount_hook
  - light_origin
required_visual_states:
  - intact
  - lit
required_lod_profiles:
  - lod0
  - lod1
  - lod2
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemins :** chaque entrée de `required_nodes` associe un chemin relatif et un type attendu.
- **Sockets :** la liste est comparée aux repères importés ou dérivés.
- **États :** les identifiants visuels n’incluent aucune règle de transition.
- **LOD :** trois profils sont attendus sans imposer leurs seuils.
- **Décision :** le contrat reste bloqué tant que la scène n’est pas matérialisée.

## 34. Validateur GDScript structurel

Le validateur suivant vérifie une scène déjà instanciée. Il ne crée pas les nœuds manquants, ne corrige pas les transforms et ne décide pas si un objet peut être équipé.

> **[VSC] Créer `tests/art/props/prop_asset_validator.gd`.**

```gdscript
class_name PropAssetValidator
extends Node

enum ValidationCode {
    OK,
    ROOT_MISSING,
    IMPORTED_OBJECT_MISSING,
    REQUIRED_NODE_MISSING,
    REQUIRED_SOCKET_MISSING,
    COLLISION_SHAPE_MISSING,
    NON_UNIFORM_COLLISION_SCALE,
    INVALID_LOD_PROFILE
}

const EPSILON: float = 0.0001

func validate_scene(
    root: Node,
    required_node_paths: Array[NodePath],
    required_socket_names: PackedStringArray,
    required_lod_names: PackedStringArray
) -> Dictionary:
    var issues: Array[Dictionary] = []

    if root == null:
        return _result(ValidationCode.ROOT_MISSING, issues)

    if root.get_node_or_null(^"ImportedObject") == null:
        issues.append(_issue(
            ValidationCode.IMPORTED_OBJECT_MISSING,
            "ImportedObject",
            "La scène importée est absente."
        ))

    _validate_required_nodes(root, required_node_paths, issues)
    _validate_sockets(root, required_socket_names, issues)
    _validate_collision_shapes(root, issues)
    _validate_lod_profiles(root, required_lod_names, issues)

    var code := ValidationCode.OK
    if not issues.is_empty():
        code = int(issues[0]["code"]) as ValidationCode

    return _result(code, issues)

func _validate_required_nodes(
    root: Node,
    paths: Array[NodePath],
    issues: Array[Dictionary]
) -> void:
    for path: NodePath in paths:
        if root.get_node_or_null(path) == null:
            issues.append(_issue(
                ValidationCode.REQUIRED_NODE_MISSING,
                String(path),
                "Un nœud requis est absent."
            ))

func _validate_sockets(
    root: Node,
    socket_names: PackedStringArray,
    issues: Array[Dictionary]
) -> void:
    var socket_root := root.get_node_or_null(^"ImportedObject")
    if socket_root == null:
        return

    for socket_name: String in socket_names:
        if not _contains_named_node(socket_root, socket_name):
            issues.append(_issue(
                ValidationCode.REQUIRED_SOCKET_MISSING,
                socket_name,
                "Un socket requis est absent."
            ))

func _contains_named_node(root: Node, expected_name: String) -> bool:
    if String(root.name).to_lower() == expected_name.to_lower():
        return true

    for child: Node in root.get_children():
        if _contains_named_node(child, expected_name):
            return true

    return false

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
        var uniform_xy := absf(scale_value.x - scale_value.y) <= EPSILON
        var uniform_yz := absf(scale_value.y - scale_value.z) <= EPSILON
        if not (uniform_xy and uniform_yz):
            issues.append(_issue(
                ValidationCode.NON_UNIFORM_COLLISION_SCALE,
                collision.get_path(),
                "La collision utilise une échelle non uniforme."
            ))

func _validate_lod_profiles(
    root: Node,
    lod_names: PackedStringArray,
    issues: Array[Dictionary]
) -> void:
    var lod_root := root.get_node_or_null(^"LOD")
    if lod_root == null and not lod_names.is_empty():
        issues.append(_issue(
            ValidationCode.INVALID_LOD_PROFILE,
            "LOD",
            "La racine LOD est absente."
        ))
        return

    for lod_name: String in lod_names:
        if lod_root.get_node_or_null(NodePath(lod_name)) == null:
            issues.append(_issue(
                ValidationCode.INVALID_LOD_PROFILE,
                lod_name,
                "Un profil LOD requis est absent."
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

- **Classe :** `PropAssetValidator` étend `Node` afin d’être instancié dans une scène de test.
- **Énumération :** `ValidationCode` fournit des codes stables plutôt que des chaînes libres comme autorité.
- **Paramètres :** `validate_scene` reçoit une racine `Node`, des chemins `Array[NodePath]` et deux listes `PackedStringArray`.
- **Valeur de retour :** chaque fonction publique renvoie un `Dictionary` contenant `ok`, `code` et une copie profonde des problèmes.
- **Opérateurs :** `==`, `!=`, `not`, `and` et `<=` comparent les états et la tolérance d’échelle.
- **Récursion :** `_contains_named_node` parcourt les enfants et renvoie un booléen dès qu’un nom correspond.
- **Conversions :** `as CollisionShape3D`, `int()`, `str()` et `NodePath()` rendent les types attendus explicites.
- **Effets de bord :** le script ne modifie aucun nœud ; il ajoute seulement des dictionnaires à la liste locale `issues`.
- **Invariant :** une collision doit avoir une `Shape3D` et une échelle uniforme à `EPSILON` près.
- **Limite :** la présence structurelle ne prouve ni l’alignement visuel, ni la qualité des collisions, ni les performances.

## 35. Rapport JSON du validateur

Le rapport conserve les codes et sujets sans prétendre que le contrôle a été exécuté dans ce chapitre.

> **[SORTIE] Exemple de rapport attendu — Ne pas saisir.**

```json
{
  "asset_id": "AST-PROP-LANTERN-001",
  "validator": "PropAssetValidator",
  "executed": false,
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

- **Exécution :** `executed: false` empêche de confondre l’exemple et une preuve runtime.
- **Résultat :** `ok`, `code` et `issues` reproduisent le contrat du validateur.
- **Notes :** la liste explique la limite de la sortie.
- **Persistance :** un rapport réel serait conservé sous `tests/art/props/reports`.
- **Décision :** l’absence de problèmes dans un exemple non exécuté ne vaut aucune acceptation.

## 36. Tests d’alignement et grille de poses

Tester chaque objet dans les poses qui révèlent ses défauts :

- main ouverte et fermée ;
- poignet neutre, flexion et déviation ;
- bras le long du corps ;
- marche et course ;
- accroupissement ;
- rangement et extraction ;
- pose au sol ;
- interaction avec une table, un crochet ou un support ;
- vues première et troisième personne lorsque pertinentes.

> **[LECTURE] Grille d’alignement — Ne pas saisir.**

```yaml
suite_id: AST-POSE-PROP-001-v001
asset_id: AST-WPN-SHORT-BLADE-001
poses:
  neutral_grip: pending
  wrist_flexion: pending
  walk_cycle_sample: pending
  crouch_sample: pending
  sheath_insert: pending
  sheath_remove: pending
  table_display: pending
captures:
  front: pending
  side: pending
  hand_closeup: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Suite :** le jeu de poses possède un identifiant versionné.
- **Échantillons :** les entrées décrivent des configurations de contrôle, pas des animations produites.
- **Captures :** trois vues permettent de comparer échelle, intersection et prise.
- **Décision :** toute valeur `pending` maintient le blocage.
- **Frontière :** les animations complètes restent au chapitre 20.

## 37. Tests d’environnement et d’interaction

Placer les objets dans un petit laboratoire comprenant :

- sol plat ;
- table ;
- étagère ;
- crochet ;
- coffre ;
- mur proche ;
- personnage de référence ;
- plusieurs objets voisins ;
- éclairages neutres et rasants.

Vérifier la sélection, le chevauchement, la stabilité de pose, les ombres, les collisions et la lisibilité des repères.

> **[LECTURE] Scénarios d’environnement — Ne pas saisir.**

```yaml
lab_id: AST-PROP-VALIDATION-LAB-001-v001
scenarios:
  - id: floor_drop
    object: AST-EQP-BUCKLER-001
    checks:
      - collision_fit
      - resting_orientation
  - id: shelf_selection
    object: AST-PROP-LANTERN-001
    checks:
      - interaction_isolation
      - focus_socket
  - id: hook_mount
    object: AST-PROP-LANTERN-001
    checks:
      - mount_alignment
      - handle_clearance
  - id: character_hold
    object: AST-TOOL-SURVEY-HAMMER-001
    checks:
      - grip_alignment
      - forearm_clearance
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénarios :** chaque entrée associe un objet et des contrôles observables.
- **Sélection :** `interaction_isolation` vérifie que les objets voisins ne sont pas détectés à tort.
- **Monture :** le crochet révèle les erreurs de pivot et de dégagement.
- **Personnage :** la prise est contrôlée avec le gabarit réel.
- **État :** le laboratoire n’est pas annoncé comme matérialisé.

## 38. Campagne de performance

Mesurer dans Godot, sur le matériel de référence :

- triangles et sommets réellement importés ;
- nombre de surfaces et matériaux ;
- draw calls ;
- mémoire des maillages et textures ;
- coût des transparences ;
- coût des collisions ;
- nombre d’objets simultanés ;
- coût des LOD et transitions ;
- temps de chargement et réimportation ;
- différences entre objet équipé, posé et distant.

> **[LECTURE] Plan de mesure — Ne pas saisir.**

```yaml
benchmark_id: AST-PROP-BENCH-001-v001
hardware_profile: AST-HW-RX6750XT-001-v001
scenarios:
  equipped_single:
    object_count: 1
    measurements: pending
  shelf_dense:
    object_count: provisional
    measurements: pending
  dropped_cluster:
    object_count: provisional
    measurements: pending
  distant_display:
    object_count: provisional
    measurements: pending
metrics:
  - frame_time_cpu_ms
  - frame_time_gpu_ms
  - draw_calls
  - mesh_memory_bytes
  - texture_memory_bytes
  - physics_step_ms
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Matériel :** `hardware_profile` relie les mesures à la machine de référence.
- **Scénarios :** un objet équipé, une étagère dense, un groupe au sol et un affichage distant couvrent des coûts différents.
- **Nombres :** `provisional` signale que les densités ne sont pas encore fixées.
- **Métriques :** CPU, GPU, mémoire, draw calls et physique sont mesurés séparément.
- **Blocage :** aucune valeur n’est inventée dans le chapitre.

## 39. Parcours Solo et Studio

### 39.1 Mode Solo

Le parcours Solo limite la bibliothèque aux objets réellement visibles dans le vertical slice. Il réutilise :

- une convention de pivots ;
- une convention de sockets ;
- trois familles de collisions ;
- un laboratoire Godot ;
- un petit atlas lorsque la mesure le justifie ;
- une grille de poses commune.

La priorité est donnée à un objet complet par famille avant d’ajouter des variantes.

### 39.2 Mode Studio

Le parcours Studio sépare les responsabilités :

| Responsabilité | Propriétaire principal |
|---|---|
| brief fonctionnel et silhouette | direction artistique |
| dimensions et ergonomie | prop artist avec revue animation |
| pivots et sockets | prop artist et technical artist |
| collisions | technical artist et intégration |
| matériaux | lookdev |
| LOD | prop artist et performance |
| scènes dérivées | intégration Godot |
| validation finale | revue croisée |

Les identifiants, versions, profils et preuves sont publiés dans un catalogue partagé. Une modification de pivot ou de socket après approbation exige une nouvelle version et une revue des dépendances.

## 40. Porte d’acceptation

Un objet ne passe pas au statut accepté tant que les preuves suivantes ne sont pas réunies :

- brief fonctionnel approuvé ;
- provenance et droits qualifiés ;
- dimensions et incertitudes enregistrées ;
- origine, axes et pivots contrôlés ;
- sockets présents et orientés ;
- prise et rangement testés ;
- pièces mobiles vérifiées ;
- topologie et ombrage relus ;
- matériaux et atlas qualifiés ;
- collisions adaptées à chaque usage ;
- états visuels et variantes disponibles ;
- LOD produits et mesurés ;
- GLB importé ;
- scène Godot dérivée matérialisée ;
- alignements, interactions et performance mesurés ;
- réserves fermées ou explicitement acceptées par un responsable.

> **[LECTURE] Porte d’acceptation — Ne pas saisir.**

```yaml
gate_id: AST-PROP-GATE-001-v001
asset_id: AST-PROP-LANTERN-001
evidence:
  brief: pending
  provenance: pending
  dimensions: pending
  pivots: pending
  sockets: pending
  grip_and_mounts: pending
  moving_parts: pending
  topology_and_shading: pending
  materials: pending
  collisions: pending
  visual_states: pending
  lod: pending
  glb_import: pending
  godot_scene: pending
  alignment_tests: pending
  performance: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Porte :** chaque preuve possède un statut indépendant.
- **Décision :** `blocked` reste obligatoire dès qu’une preuve est absente.
- **Traçabilité :** `gate_id` et `asset_id` relient la décision au bon objet.
- **Responsabilité :** un humain ferme ou accepte explicitement les réserves.
- **Résultat attendu :** l’apparence seule ne suffit pas à publier l’asset.

## 41. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 41.1 Modéliser depuis une image sans échelle

**Symptôme :** l’objet paraît crédible isolément mais devient trop grand ou trop petit dans la main.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
dimensions:
  source: concept_image
  perspective_review: none
  hand_profile: none
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une image en perspective sans référence mesurée ne fournit pas d’échelle fiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
dimensions:
  source:
    - licensed_reference_set
    - character_hand_profile
  uncertainty: documented
  hand_review: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction croise des références, consigne l’incertitude et exige un test avec la main du projet.

### 41.2 Déplacer l’origine pour corriger une seule animation

**Symptôme :** l’objet s’aligne dans une scène mais casse ses poses au sol, son fourreau et ses autres personnages.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
origin_change:
  reason: fix_one_animation
  version_increment: false
  dependency_review: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’origine est un contrat partagé ; la modifier pour un cas local déplace toutes les dépendances.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
origin_change:
  source_origin: preserved
  local_attachment_profile: AST-ATTACH-FIX-001-v001
  dependency_review: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve la source et place l’ajustement dans un profil local versionné.

### 41.3 Utiliser le même repère pour prise et rangement

**Symptôme :** la lame est correcte en main mais traverse le fourreau ou s’oriente mal à la ceinture.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
sockets:
  grip_primary: object_origin
  mount_sheath: object_origin
  insertion_axis: assumed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La prise et le rangement ont des orientations et profondeurs différentes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
sockets:
  grip_primary: SOCKET_grip_primary
  mount_sheath: SOCKET_mount_sheath
  insertion_axis: local_negative_z
  sheath_test: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare les repères et rend l’axe d’insertion vérifiable.

### 41.4 Promouvoir la collision générée depuis le maillage

**Symptôme :** un objet dynamique coûte cher, accroche le décor ou se comporte différemment selon sa triangulation.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
collision:
  source: render_mesh
  generated: automatic
  runtime_use: final
  review: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La géométrie de rendu n’est ni simplifiée ni qualifiée pour la physique.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
collision:
  source: dedicated_proxy
  shapes:
    - BoxShape3D
    - CylinderShape3D
  generated_collision: testing_only
  runtime_review: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise des primitives contrôlables et limite la génération automatique au diagnostic.

### 41.5 Appliquer une échelle non uniforme à CollisionShape3D

**Symptôme :** la forme de collision ne correspond pas au gizmo ou produit des contacts inattendus.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
collision_shape:
  scale: [1.0, 0.5, 2.0]
  resource_dimensions: unchanged
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une `CollisionShape3D` mise à l’échelle différemment sur chaque axe peut se comporter de manière imprévisible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
collision_shape:
  scale: [1.0, 1.0, 1.0]
  resource_dimensions: adjusted
  verification: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve une échelle uniforme et modifie la ressource de forme elle-même.

### 41.6 Définir dégâts et portée dans le manifeste visuel

**Symptôme :** une variante de matériau modifie implicitement les règles de combat.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
material_variant: iron_worn
damage: 25
reach_m: 1.2
attack_speed: 1.1
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le manifeste d’asset devient une seconde autorité de combat et mélange apparence et règles métier.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
asset_id: AST-WPN-SHORT-BLADE-001
visual_variant: iron_worn
content_definition_id: ITEM-SHORT-BLADE-001
combat_data: excluded
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve un lien vers la définition métier sans recopier ses valeurs.

### 41.7 Utiliser un seul volume pour interaction, physique et impact

**Symptôme :** l’objet est difficile à sélectionner et sa physique ne correspond pas à sa zone de contact visuelle.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
volumes:
  universal_shape: render_bounds
  interaction: universal_shape
  physics: universal_shape
  impact: universal_shape
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les trois usages ont des besoins de précision, coût et autorité différents.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
volumes:
  interaction: AST-AREA-LANTERN-001-v001
  physics: AST-COLL-LANTERN-DROP-001-v001
  impact_proxy: AST-IMPACT-LANTERN-001-v001
  shared_geometry: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction attribue un profil distinct à chaque responsabilité.

### 41.8 Orienter le point d’émission à l’œil

**Symptôme :** le VFX part latéralement ou vers l’arrière après import.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
emission_socket:
  position: visually_placed
  forward_axis: undocumented
  godot_gizmo_review: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une position correcte ne garantit pas une orientation cohérente entre Blender et Godot.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
emission_socket:
  name: projectile_origin
  forward_axis: local_negative_z
  godot_gizmo_review: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction documente l’axe et exige une inspection du gizmo après import.

### 41.9 Supprimer les prises dans les LOD

**Symptôme :** l’objet distant redevient proche ou équipé mais ne possède plus les repères nécessaires.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod2:
  geometry: silhouette_proxy
  sockets: removed_all
  reuse_when_equipped: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le même LOD ne peut pas être réutilisé comme objet équipé s’il a perdu ses repères fonctionnels.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod2:
  geometry: silhouette_proxy
  sockets:
    - mount_environment
  allowed_representations:
    - distant_static
  equipped_representation: lod0_or_lod1
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite le LOD au contexte distant et conserve le socket encore utile.

### 41.10 Déclarer l’objet terminé après la revue Blender

**Symptôme :** le modèle paraît correct dans Blender mais son pivot, ses sockets, ses collisions ou ses matériaux sont incorrects dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
alignment_tests: not_executed
performance_tests: not_executed
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
performance_tests: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction maintient le blocage jusqu’aux preuves Godot et aux mesures.

## 42. Livrables à conserver

Le plan maître exige cinq livrables permanents :

1. **bibliothèque d’objets pilotes** — sources, variantes, états, exports et manifeste ;
2. **conventions de pivots et sockets** — axes, noms, transformations et politiques de version ;
3. **collisions** — détection, physique, proxies et responsabilités ;
4. **LOD** — géométrie, matériaux, fonctions, collisions et seuils ;
5. **scènes Godot d’équipement** — scènes importées, scènes dérivées, attaches et rapports.

> **[LECTURE] Manifeste de livraison — Ne pas saisir.**

```yaml
deliverable_manifest: AST-PROP-DELIVERY-001-v001
object_library:
  profile: AST-PROP-KIT-EXPLORER-001
  status: blocked
pivot_and_socket_conventions:
  profile: AST-PROP-SOCKET-CONVENTIONS-001-v001
  status: blocked
collisions:
  profile: AST-PROP-COLLISIONS-001-v001
  status: blocked
lod:
  profile: AST-PROP-LOD-001-v001
  status: blocked
godot_equipment_scenes:
  profile: AST-PROP-GODOT-SCENES-001-v001
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifeste :** les cinq livrables du plan maître sont regroupés dans un lot versionné.
- **Profils :** chaque livrable pointe vers un contrat indépendant.
- **État :** toutes les entrées restent bloquées tant que les fichiers et preuves ne sont pas produits.
- **Traçabilité :** le manifeste sert d’entrée à la revue de production.
- **Frontière :** aucune règle d’inventaire ou de combat n’est ajoutée.

## 43. Synthèse opérationnelle pour Project Asteria

Le chapitre 12 fournit à `Project Asteria` une méthode complète pour produire des objets individuels cohérents avec leur usage. La bibliothèque de l’Explorateur est encadrée par des briefs fonctionnels, des références dimensionnelles, un registre de provenance, des profils d’échelle, des conventions d’axes, d’origines, de pivots et de sockets, des prises, des montures, des pièces mobiles, des topologies, des profils d’ombrage, des matériaux provisoires, des collisions distinctes, des états visuels, des variantes, des LOD, un preset GLB, une scène Godot dérivée, un validateur structurel, une grille de poses et une campagne de performance.

Les objets restent bloqués tant que les dimensions, modèles, prises, pivots, sockets, collisions, états, matériaux, LOD, GLB, scènes Godot, alignements et mesures ne sont pas réellement produits. Le chapitre prépare les attaches de rig, les animations, les VFX et l’intégration, mais ne définit ni statistiques, ni dégâts, ni trajectoires, ni règles d’équipement.

## 44. Références techniques officielles

Les références suivantes doivent être consultées et qualifiées lors de la matérialisation :

- [Blender Manual — Pivot Point](https://docs.blender.org/manual/en/5.0/editors/3dview/controls/pivot_point/index.html) ;
- [Blender Manual — Individual Origins](https://docs.blender.org/manual/en/5.0/editors/3dview/controls/pivot_point/individual_origins.html) ;
- [Blender Manual — Empties](https://docs.blender.org/manual/en/latest/modeling/empties.html) ;
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/5.0/addons/import_export/scene_gltf2.html) ;
- [Godot 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) ;
- [Godot 4.7 — Import configuration](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html) ;
- [Godot 4.7 — MeshInstance3D](https://docs.godotengine.org/en/4.7/classes/class_meshinstance3d.html) ;
- [Godot 4.7 — BoneAttachment3D](https://docs.godotengine.org/en/4.7/classes/class_boneattachment3d.html) ;
- [Godot 4.7 — Marker3D](https://docs.godotengine.org/en/4.7/classes/class_marker3d.html) ;
- [Godot 4.7 — Area3D](https://docs.godotengine.org/en/4.7/classes/class_area3d.html) ;
- [Godot 4.7 — CollisionShape3D](https://docs.godotengine.org/en/4.7/classes/class_collisionshape3d.html) ;
- [Godot 4.7 — Collision shapes 3D](https://docs.godotengine.org/en/4.7/tutorials/physics/collision_shapes_3d.html) ;
- [Godot 4.7 — Shape3D](https://docs.godotengine.org/en/4.7/classes/class_shape3d.html) ;
- [Godot 4.7 — Mesh level of detail](https://docs.godotengine.org/en/4.7/tutorials/3d/mesh_lod.html) ;
- [Godot 4.7 — Visibility ranges](https://docs.godotengine.org/en/4.7/tutorials/3d/visibility_ranges.html).

Les pages `latest` ou `stable` ne sont utilisées que lorsqu’aucune page versionnée équivalente n’est exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d’appliquer la procédure.
