---
title: "Livre III — Chapitre 11 : Vêtements, armures et accessoires"
id: "DOC-L3-CH11"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 11
last-verified: "2026-07-23T11:50:40+02:00"
audit-status: "complete"
audit-date: "2026-07-23T11:50:40+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-11.md"
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

# Vêtements, armures et accessoires

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH11`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Les chapitres 6 et 7 ont défini les bases humaines et humanoïdes, leurs proportions, leurs zones de déformation et leurs profils de rig. Le chapitre 10 a approfondi le visage, la peau, les yeux et la pilosité. Le présent chapitre ne recommence aucun de ces travaux. Il construit un système visuel d'équipement porté : vêtements souples, pièces rembourrées, armures déformables ou rigides, capes, sacs, ceintures, bijoux et accessoires attachés au corps.

Le fil rouge utilise un kit pilote de `Project Asteria`, identifié `AST-WEAR-KIT-WARDEN-001`. Le kit comprend une couche de base, une tunique, un pantalon, une veste courte, une ceinture, une épaulière, des brassards, des bottes, une cape courte et plusieurs accessoires non tenus. Il relie layering, tailles, patrons, marges de mouvement, topologie, skinning, attaches, collisions simplifiées, masquage corporel, variantes, matériaux, LOD, export GLB et validation Godot.

Un vêtement ne devient pas compatible parce qu'il paraît correctement posé sur une pose neutre. Il doit rester cohérent dans les poses extrêmes, respecter l'ordre des couches, suivre le squelette sans volumes écrasés, éviter les intersections visibles, conserver ses attaches, contrôler la simulation, réduire son coût à distance et déclarer les morphologies ou combinaisons qu'il ne prend pas en charge.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Base humaine ou humanoïde validée
    ↓
Brief du kit porté et catégories de pièces
    ↓
Règles de layering et matrice de compatibilité
    ↓
Patrons, volumes, épaisseurs et marges de mouvement
    ↓
Topologie, coutures et zones de déformation
    ↓
Skinning, rigidité locale et attaches
    ↓
Collisions simplifiées et simulation Blender
    ↓
Prévention du clipping et masquage corporel
    ↓
Matériaux, atlas, variantes et LOD
    ↓
Export GLB et scène Godot dérivée
    ↓
Poses extrêmes, combinaisons, coût et décision
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** le système part d'une morphologie et d'un rig déjà qualifiés.
- **Ordre :** les règles de compatibilité précèdent la fabrication détaillée des pièces.
- **Preuve :** la pose neutre ne suffit jamais ; poses extrêmes, combinaisons et distances doivent être testées.
- **Frontière :** les objets tenus et les armes appartiennent au chapitre 12 ; les règles d'inventaire et d'équipement restent dans le Livre II.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- transformer un besoin narratif et visuel en kit porté modularisable ;
- distinguer couche, emplacement, catégorie, variante, taille et profil morphologique ;
- définir un ordre de layering explicite et détecter les combinaisons incompatibles ;
- concevoir patrons, volumes, épaisseurs, coutures et marges de mouvement ;
- choisir entre pièce skinnée, pièce rigide attachée, pièce simulée ou solution hybride ;
- transférer des poids sans accepter aveuglément le résultat automatique ;
- préparer des zones rigides, des corrections de poids et des os secondaires sans redéfinir le rig de production ;
- placer des attaches stables pour ceintures, sacs, bijoux, capes et éléments décoratifs ;
- créer des collisions simplifiées destinées au test ou à la simulation Blender ;
- prévenir le clipping par coupe, volume, skinning, masquage et règles de compatibilité ;
- documenter les morphologies, poses et combinaisons non prises en charge ;
- préparer des atlas et regroupements de matériaux sans remplacer le pipeline PBR du chapitre 16 ;
- définir des LOD géométriques, matériels et fonctionnels ;
- importer un kit GLB dans une scène Godot dérivée ;
- écrire un validateur structurel non destructif et comprendre ses paramètres, types, retours et opérateurs ;
- conserver des réserves explicites lorsque Blender ou Godot n'ont pas été exécutés.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les contrats, procédures Blender, règles de compatibilité, exemples de scène Godot et scripts GDScript sont relus. Ils ne constituent pas une preuve d'exécution.

Aucun vêtement, aucune armure, aucun accessoire, aucun patron, aucun skinning, aucune simulation, aucune collision, aucun atlas, aucun LOD, aucun GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme produits. Les nombres de sommets, influences, couches, matériaux, collisions, distances ou seuils sont des budgets provisoires à confirmer sur le matériel de référence.

La simulation de tissu décrite dans Blender est une étape de fabrication et de validation. Le chapitre ne suppose pas qu'un cache Blender devient automatiquement une simulation runtime dans Godot. Une pièce destinée au jeu doit être convertie vers une représentation explicitement prise en charge : maillage skinné, animation bakée qualifiée, os secondaires, forme corrective ou autre solution mesurée.

## 4. Périmètre et frontières

Le chapitre couvre :

- layering et ordre des couches ;
- patrons, volumes, coutures, épaisseurs et marges de mouvement ;
- skinning aux rigs de référence ;
- rigidité locale et pièces d'armure attachées ;
- simulation de tissu et collisions simplifiées dans Blender ;
- attaches, accessoires portés et points de fixation ;
- prévention du clipping et masquage corporel ;
- tailles, morphologies, variantes et matrice de compatibilité ;
- atlas, réduction des matériaux et profils LOD ;
- export GLB, scène Godot dérivée et validation structurelle.

Le chapitre ne couvre pas :

- la création des bases humaines ou humanoïdes des chapitres 6 et 7 ;
- le lookdev facial, les cheveux et la pilosité du chapitre 10 ;
- les objets tenus, armes, projectiles et prises en main du chapitre 12 ;
- le pipeline PBR transversal du chapitre 16 ;
- la retopologie, les UV et le baking génériques du chapitre 17 ;
- le rig de production final et ses contrôleurs du chapitre 19 ;
- les cycles, simulations d'animation et outils d'animation du chapitre 20 ;
- les règles d'inventaire, de statistiques, de combat ou d'équipement du Livre II.

> **[LECTURE] Matrice des responsabilités — Ne pas saisir.**

```yaml
chapter_11:
  owns:
    - wearable_layer_contract
    - garment_and_armor_fit_profiles
    - wearable_skinning_profiles
    - attachment_and_simulation_proxies
    - wearable_compatibility_matrix
    - wearable_lod_profiles
  prepares:
    - chapter_19_rig_validation
    - chapter_20_animation_tests
    - chapter_28_import_integration
  does_not_own:
    - inventory_rules
    - combat_statistics
    - held_objects_and_weapons
    - general_pbr_pipeline
    - production_animation_controllers
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** chaque valeur est une chaîne nommant une responsabilité documentaire.
- **Préparation :** `prepares` fournit des entrées et des tests futurs sans exécuter les chapitres concernés.
- **Exclusion :** `does_not_own` empêche le système visuel de devenir propriétaire des règles métier.
- **Résultat attendu :** toute tâche du chapitre doit se rattacher à une responsabilité de `owns`.

## 5. Prérequis et fichiers à ouvrir

Avant de commencer, le lecteur doit disposer :

- d'une base humaine ou humanoïde validée à l'échelle du projet ;
- d'un squelette de référence et de noms d'os stables ;
- de poses extrêmes ou d'une liste de poses à créer au chapitre 20 ;
- d'un identifiant stable pour chaque pièce ;
- d'un registre de provenance et de droits ;
- d'un budget provisoire par plateforme ;
- d'une scène Godot de validation de personnage ;
- des conventions Blender et Godot du projet.

Le lecteur ouvre :

- **[APP] Blender 5.2.0** pour les patrons, volumes, topologie, skinning, collisions et simulations de fabrication ;
- **[APP] Godot 4.7.1-stable** pour l'import, la scène dérivée, les combinaisons, les LOD et les mesures ;
- **[VSC] Visual Studio Code** pour les contrats YAML, les matrices CSV ou JSON et le validateur GDScript ;
- **[PS] PowerShell 7** pour créer les dossiers et lancer les contrôles documentaires.

> **[LECTURE] Arborescence de travail proposée — Ne pas saisir.**

```text
art/
├── blender/wearables/
│   └── AST-WEAR-KIT-WARDEN-001/
├── wearables/
│   ├── briefs/
│   ├── layers/
│   ├── patterns/
│   ├── fit/
│   ├── skinning/
│   ├── attachments/
│   ├── simulation/
│   ├── masks/
│   ├── compatibility/
│   ├── materials/
│   ├── variants/
│   └── lod/
├── exports/wearables/
├── provenance/
└── budgets/
tests/
└── art/wearables/
    ├── wearable_validation_lab.tscn
    ├── wearable_asset_validator.gd
    ├── reports/
    └── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les fichiers Blender restent séparés des exports GLB.
- **Contrats :** layering, ajustement, skinning, attaches, simulation, masques et compatibilité possèdent des dossiers distincts.
- **Tests :** scène, script, rapports et captures sont regroupés sous `tests/art/wearables`.
- **Publication :** les preuves internes ne sont pas ajoutées au manuel lecteur.

## 6. Kit pilote et intentions d’usage

Le kit pilote doit répondre à des scènes réellement prévues : exploration, dialogue, marche, course, accroupissement, montée d'escalier, combat sans arme tenue dans ce chapitre, chute contrôlée et plan rapproché. La sélection évite de produire dix variantes décoratives avant d'avoir démontré qu'une combinaison complète résiste aux poses.

Les pièces pilotes sont classées par comportement :

- **couche de base** : près du corps, principalement skinnée ;
- **tunique et pantalon** : textiles souples, skinnés avec corrections locales ;
- **veste** : textile plus épais, zones semi-rigides ;
- **ceinture et brassards** : pièces proches du corps avec attaches stables ;
- **épaulière** : armure rigide ou semi-rigide, parentage et poids limités ;
- **bottes** : volumes structurés, compatibilité avec pieds et sol ;
- **cape courte** : pièce secondaire pouvant nécessiter simulation de fabrication ou os dédiés ;
- **sac et bijoux** : accessoires portés, sans logique d'inventaire dans ce chapitre.

> **[LECTURE] Contrat du kit pilote — Ne pas saisir.**

```yaml
kit_id: AST-WEAR-KIT-WARDEN-001
character_profiles:
  - AST-CHR-HUMAN-BASE-001
  - AST-CHR-HUMANOID-SLENDER-001
use_cases:
  - exploration
  - dialogue
  - locomotion
  - crouch
  - stairs
  - combat_pose_without_held_weapon
pieces:
  - id: AST-WEAR-BASE-001
    behavior: skinned_close_fit
  - id: AST-WEAR-TUNIC-001
    behavior: skinned_soft
  - id: AST-WEAR-SHOULDER-001
    behavior: rigid_attached
  - id: AST-WEAR-CAPE-001
    behavior: hybrid_secondary_motion
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** chaque pièce possède un identifiant stable indépendant de son nom affiché.
- **Profils :** `character_profiles` limite explicitement les bases visées.
- **Comportement :** `behavior` oriente la stratégie de déformation avant la production détaillée.
- **État :** le lot reste `blocked` tant que les assets et tests ne sont pas matérialisés.

## 7. Vocabulaire de production

- **Layering** : ordre et règles de coexistence des couches portées.
- **Slot visuel** : zone ou fonction de présentation ; il ne constitue pas une règle d'inventaire.
- **Fit profile** : contrat d'ajustement pour une morphologie et une pose de référence.
- **Ease** : marge volontaire entre le corps et le vêtement.
- **Skinning** : association des sommets aux os par poids.
- **Pièce rigide attachée** : géométrie suivant un os ou un petit ensemble d'os sans déformation textile.
- **Proxy de collision** : volume simplifié utilisé pour une simulation ou un contrôle.
- **Masque corporel** : règle de visibilité de régions du corps sous une pièce opaque.
- **Compatibilité** : décision documentée entre pièce, morphologie, couche, rig et pose.
- **LOD fonctionnel** : simplification qui conserve les traits et attaches nécessaires.

> **[LECTURE] Fiche d'une pièce portée — Ne pas saisir.**

```yaml
wearable_piece:
  id: AST-WEAR-TUNIC-001
  category: torso_soft
  visual_slots:
    - torso_inner
    - upper_arm_inner
  layer_index: 20
  fit_profile: AST-FIT-HUMAN-MEDIUM-001-v001
  deformation_profile: AST-SKIN-TORSO-SOFT-001-v001
  material_profile: AST-MAT-CLOTH-WOOL-001-v001
  lod_profile: AST-WEAR-LOD-TUNIC-001-v001
  gameplay_item_definition: external_reference_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** le profil visuel ne contient ni statistiques ni règles d'équipement.
- **Layering :** `layer_index` fournit un ordre, mais les conflits restent décrits par la matrice.
- **Références :** fit, déformation, matériau et LOD sont des contrats versionnés.
- **Lien métier :** `gameplay_item_definition` est seulement une référence externe.

## 8. Définir l’architecture des couches

Un ordre numérique seul ne suffit pas. Deux pièces peuvent partager un niveau mais occuper des régions différentes, ou être incompatibles malgré des indices distincts. Le système doit donc combiner une catégorie de couche, les régions corporelles couvertes, une enveloppe attendue, des règles d'inclusion ou d'exclusion, un traitement du corps masqué, une priorité et une preuve de combinaison.

Une hiérarchie simple pour le kit pilote peut être :

- `10` : peau et sous-vêtement technique ;
- `20` : couche textile intérieure ;
- `30` : couche textile extérieure ;
- `40` : armure ou renfort ;
- `50` : ceinture, sangle et petit accessoire ;
- `60` : cape, sac ou élément secondaire externe.

Ces nombres sont des conventions de tri, pas une garantie automatique de compatibilité.

> **[LECTURE] Règles de couches — Ne pas saisir.**

```yaml
layer_rules:
  categories:
    body_base:
      index: 10
    textile_inner:
      index: 20
    textile_outer:
      index: 30
    armor:
      index: 40
    straps_accessories:
      index: 50
    external_secondary:
      index: 60
  explicit_conflicts:
    - pair: [AST-WEAR-TUNIC-001, AST-WEAR-HEAVY-COAT-001]
      regions: [torso, upper_arm]
      reason: insufficient_clearance
  explicit_requirements:
    - piece: AST-WEAR-SHOULDER-001
      requires_any:
        - AST-WEAR-PADDED-BASE-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catégories :** les indices fournissent l'ordre général des couches.
- **Conflits :** une paire incompatible indique les régions et la cause.
- **Prérequis :** certaines pièces exigent une couche de support pour éviter flottement ou intersection.
- **Résultat attendu :** l'assemblage peut refuser une combinaison avant le test visuel.

## 9. Construire la matrice de compatibilité

La matrice doit répondre à une question précise : cette pièce, dans cette variante et sur cette morphologie, peut-elle être combinée avec cette autre pièce pour les poses ciblées ? Une réponse binaire sans cause est difficile à corriger. Utiliser au minimum `supported`, `conditional`, `blocked`, `untested` et `not_applicable`.

Chaque décision doit porter une cause stable et une preuve attendue.

> **[LECTURE] Extrait de matrice de compatibilité — Ne pas saisir.**

```csv
piece_a,piece_b,character_profile,status,condition_or_reason,evidence
AST-WEAR-TUNIC-001,AST-WEAR-BELT-001,AST-CHR-HUMAN-BASE-001,conditional,belt_variant_wide,pose_grid_pending
AST-WEAR-JACKET-001,AST-WEAR-SHOULDER-001,AST-CHR-HUMAN-BASE-001,blocked,shoulder_volume_overlap,correction_pending
AST-WEAR-CAPE-001,AST-WEAR-BACKPACK-001,AST-CHR-HUMAN-BASE-001,untested,shared_back_volume,simulation_pending
AST-WEAR-BASE-001,AST-WEAR-TUNIC-001,AST-CHR-HUMAN-BASE-001,supported,body_mask_profile_applied,pose_grid_pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Colonnes :** chaque ligne relie deux pièces, une morphologie, un statut, une cause et une preuve.
- **Statuts :** `untested` n'est jamais assimilé à `supported`.
- **Conditions :** une compatibilité conditionnelle nomme la variante ou le masque requis.
- **Évolutivité :** le CSV peut être converti en JSON ou en ressource sans changer le sens des décisions.

## 10. Tailles et profils morphologiques

Un système modulaire robuste ne promet pas une adaptation continue à toutes les silhouettes. Il définit un nombre limité de profils réellement testés. Une taille visuelle n'est pas une taille commerciale universelle ; c'est un ensemble de dimensions, d'enveloppes et de corrections associé à une base.

Pour chaque profil, documenter stature et échelle du squelette, dimensions utiles, volumes saillants, longueur des membres, amplitude des poses ciblées, variantes de patron, statut du skinning, masques et incompatibilités connues.

> **[LECTURE] Profil d'ajustement — Ne pas saisir.**

```yaml
fit_profile: AST-FIT-HUMAN-MEDIUM-001-v001
character_base: AST-CHR-HUMAN-BASE-001
reference_pose: A_pose
measurement_set:
  shoulder_width_m: provisional
  chest_circumference_m: provisional
  waist_circumference_m: provisional
  hip_circumference_m: provisional
  inseam_m: provisional
clearance_zones:
  shoulder: review_required
  elbow: review_required
  hip: review_required
  knee: review_required
supported_pose_set: AST-POSE-WEARABLE-001-v001
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs :** les dimensions restent `provisional` tant qu'elles ne sont pas mesurées.
- **Zones :** les articulations critiques exigent une revue séparée.
- **Pose :** la compatibilité référence un jeu de poses versionné.
- **État :** aucune taille n'est acceptée sur la seule pose A.

## 11. Patrons, volumes et marges de mouvement

Même lorsque le vêtement est modélisé directement en 3D, penser en panneaux aide à contrôler couture, direction du tissu, épaisseur et déformation. Le patron n'a pas besoin d'être industriel, mais il doit expliquer quelles surfaces forment la pièce, où se trouvent les coutures, dans quelle direction le tissu se déforme, où la pièce reste proche du corps et où une marge devient nécessaire.

La marge de mouvement ne consiste pas à gonfler uniformément le maillage. Une marge excessive aux épaules fait flotter la pièce, tandis qu'une marge insuffisante à l'aine ou au coude crée une intersection immédiate.

> **[LECTURE] Profil de patron — Ne pas saisir.**

```yaml
pattern_profile: AST-PATTERN-TUNIC-001-v001
panels:
  - front
  - back
  - sleeve_left
  - sleeve_right
seams:
  - shoulder
  - side
  - underarm
ease_zones:
  chest: controlled
  shoulder: articulated
  elbow: articulated
  waist: belt_dependent
grain_or_deformation_direction:
  torso: vertical_primary
  sleeves: longitudinal_primary
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Panneaux :** la liste décrit la construction logique de la pièce.
- **Coutures :** les jonctions deviennent des zones de contrôle, pas seulement des détails visuels.
- **Marge :** chaque zone possède une intention plutôt qu'une distance universelle.
- **Déformation :** la direction attendue aide à orienter topologie et matériaux.

## 12. Blockout d’ajustement

Le blockout vérifie silhouette, épaisseur, chevauchement et amplitude avant les détails. Dans Blender :

1. dupliquer une version de travail de la base autorisée ;
2. créer les volumes majeurs avec peu de polygones ;
3. conserver les pièces séparées ;
4. vérifier face, profil, dos et vue trois quarts ;
5. appliquer les poses critiques ;
6. comparer les couches superposées ;
7. corriger les volumes avant coutures, plis et ornements.

Ne pas utiliser le modificateur `Shrinkwrap` comme solution finale automatique. Il peut aider au démarrage, mais un vêtement exactement collé au corps ne conserve ni épaisseur ni marge.

> **[LECTURE] Revue du blockout — Ne pas saisir.**

```yaml
blockout_review:
  piece: AST-WEAR-JACKET-001
  views:
    - front
    - side
    - back
    - three_quarter
  poses:
    - A_pose
    - arms_forward
    - arms_overhead
    - crouch
  checks:
    silhouette: pending
    layer_clearance: pending
    joint_clearance: pending
    ground_contact: not_applicable
  decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vues :** plusieurs angles empêchent d'accepter une correction valable uniquement de face.
- **Poses :** la revue expose épaules, aisselles, taille et hanches.
- **Contrôles :** silhouette et marges sont évaluées séparément.
- **Décision :** le blockout reste bloqué tant qu'une ligne `pending` subsiste.

## 13. Topologie, coutures et épaisseur

La topologie doit soutenir la déformation prévue. Pour un vêtement souple :

- suivre les grands flux du corps sans copier chaque boucle ;
- ajouter de la densité aux articulations réellement sollicitées ;
- éviter les triangles fins dans les zones qui plient ;
- conserver des bords propres autour des ouvertures ;
- prévoir les plis structurels sans sculpter chaque pli en géométrie ;
- séparer coutures géométriques utiles et coutures de texture ;
- contrôler l'épaisseur avec une stratégie stable.

Pour une armure rigide, la priorité change : préserver plans, arêtes, jeux entre plaques et pivots visuels. Une plaque ne doit pas se courber comme un textile parce qu'elle reçoit trop d'influences.

> **[LECTURE] Profil topologique — Ne pas saisir.**

```yaml
topology_profile: AST-TOPO-WEAR-JACKET-001-v001
deformation_zones:
  shoulder:
    density: high
    loop_direction: follows_rotation
  elbow:
    density: medium
    compression_space: required
  torso:
    density: medium
    planar_regions: preserved
openings:
  neck: reinforced
  cuffs: reinforced
  hem: reinforced
thickness:
  method: solidify_then_review
  export_state: applied_or_equivalent_required
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Densité :** elle dépend de la déformation et non d'une valeur uniforme.
- **Ouvertures :** cou, poignets et ourlet reçoivent une structure explicite.
- **Épaisseur :** la méthode peut rester non destructive pendant le travail, mais l'état exporté doit être qualifié.
- **État :** le profil ne valide pas la topologie sans poses.

## 14. Profils de skinning

Le skinning doit être conçu par famille de pièce. Un vêtement près du corps peut réutiliser une partie des poids corporels ; une veste épaisse nécessite souvent des corrections ; une cape peut utiliser des os supplémentaires ou une représentation différente ; une plaque rigide doit être liée à peu d'os.

Limiter les influences aide la stabilité et l'export, mais une limite ne doit pas détruire une zone complexe. Le chapitre documente une politique provisoire et exige un contrôle après normalisation.

> **[LECTURE] Profil de skinning — Ne pas saisir.**

```yaml
skinning_profile: AST-SKIN-TUNIC-001-v001
source_skeleton: AST-RIG-HUMAN-001-v001
strategy:
  torso: transferred_then_corrected
  shoulders: manual_review
  elbows: transferred_then_corrected
  hem: reduced_influence_set
influence_policy:
  target_max_per_vertex: provisional
  normalize: required
  zero_weight_vertices: forbidden
rigid_regions:
  - belt_buckle
pose_test_set: AST-POSE-WEARABLE-001-v001
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Stratégie :** chaque région indique si les poids sont transférés, corrigés ou définis manuellement.
- **Influences :** la limite reste provisoire et doit être contrôlée après normalisation.
- **Rigidité :** une boucle de ceinture ne doit pas hériter d'un comportement textile.
- **Test :** le profil référence le même jeu de poses que la compatibilité.

## 15. Transfert de poids et corrections

Le transfert de poids accélère la première passe, mais il ne comprend ni épaisseur, ni superposition, ni comportement matériel. Après transfert :

1. vérifier les sommets sans poids ;
2. normaliser les influences ;
3. inspecter épaules, aisselles, coudes, taille, hanches, genoux et chevilles ;
4. comparer les volumes intérieur et extérieur ;
5. corriger les rigidités locales ;
6. tester la silhouette sous plusieurs angles ;
7. documenter les écarts entre morphologies.

La copie de poids depuis le corps peut créer un double défaut : le corps traverse le vêtement et le vêtement reproduit exactement les compressions du corps.

> **[LECTURE] Rapport de transfert — Ne pas saisir.**

```yaml
weight_transfer_review:
  source_mesh: AST-CHR-HUMAN-BASE-001
  target_mesh: AST-WEAR-TUNIC-001
  automatic_transfer: completed_in_future
  required_checks:
    - zero_weight_vertices
    - non_normalized_vertices
    - excessive_influences
    - shoulder_volume
    - underarm_compression
    - hip_clearance
  corrective_pass: pending
  pose_review: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source et cible :** le transfert relie une base connue à une pièce distincte.
- **Contrôles :** les erreurs numériques et visuelles sont séparées.
- **Correction :** le transfert automatique n'est qu'une première passe.
- **État :** aucune pièce n'est acceptée avant la revue des poses.

## 16. Armures rigides et zones semi-rigides

Trois stratégies principales sont possibles :

- **parentage à un os** pour une pièce réellement rigide et localisée ;
- **skinning à influences limitées** pour une pièce qui suit plusieurs volumes sans se courber fortement ;
- **décomposition en plaques** pour préserver les jeux mécaniques.

Une épaulière peut suivre le bras supérieur, le torse ou un os dédié selon le rig. Le chapitre ne crée pas cet os dans le rig final ; il spécifie le besoin et prépare le test du chapitre 19.

Les sangles et rembourrages peuvent être skinnés séparément de la plaque. Mélanger plaque, sangle et tissu dans un même comportement rend les corrections difficiles.

> **[LECTURE] Profil d'une pièce d'armure — Ne pas saisir.**

```yaml
armor_profile: AST-ARMOR-SHOULDER-001-v001
components:
  plate:
    behavior: rigid_attached
    parent_candidate: upper_arm_l
  padding:
    behavior: skinned_soft
    skinning_profile: AST-SKIN-SHOULDER-PAD-001-v001
  straps:
    behavior: skinned_semi_rigid
required_tests:
  - arm_down
  - arm_forward
  - arm_side
  - arm_overhead
rig_requirement:
  dedicated_helper_bone: candidate_only
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Composants :** plaque, rembourrage et sangles peuvent employer des comportements différents.
- **Parent candidat :** l'os n'est pas adopté sans test de pose.
- **Exigence de rig :** un os auxiliaire reste une demande, pas une modification silencieuse.
- **État :** les quatre poses doivent être qualifiées.

## 17. Attaches et points de fixation

Un accessoire porté doit suivre un repère local stable. Les attaches possibles incluent parentage direct à un os, `BoneAttachment3D` dans la scène Godot dérivée, skinning limité, os secondaire documenté ou chaîne de pièces avec pivot local contrôlé.

Chaque attache doit déclarer l'os ou socket candidat, la transformation locale, la région de dégagement, les pièces incompatibles, le comportement en LOD et la preuve de pose.

> **[LECTURE] Profil d'attache — Ne pas saisir.**

```yaml
attachment_profile: AST-ATTACH-BELT-POUCH-001-v001
accessory: AST-WEAR-POUCH-001
parent_bone: pelvis
local_transform:
  position_m: [0.12, -0.03, 0.04]
  rotation_deg: [0.0, 12.0, -4.0]
  scale: [1.0, 1.0, 1.0]
clearance_region: right_hip
conflicts:
  - AST-WEAR-LONG-COAT-001
lod_behavior:
  lod0: separate_mesh
  lod1: merged_or_simplified_candidate
  lod2: remove_if_silhouette_preserved
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transformation :** les valeurs sont locales à l'os parent.
- **Dégagement :** la poche possède une région réservée dans la matrice.
- **LOD :** l'accessoire peut être fusionné ou retiré seulement si la silhouette reste lisible.
- **État :** les valeurs ne sont pas validées sans import et poses.

## 18. Accessoires portés et mouvement secondaire

Le chapitre inclut les accessoires fixés au personnage : cape, sac, pendentif, boucle, plume, corde, sangle ou étui vide. Il exclut l'objet tenu et l'arme fonctionnelle du chapitre 12.

Pour chaque accessoire, choisir entre rigidité complète, skinning léger, os secondaires, animation bakée, simulation de fabrication ou suppression dans les LOD. Un pendentif qui oscille peut être préparé par des pivots et limites, mais le chapitre ne revendique pas l'exécution runtime.

> **[LECTURE] Profil de mouvement secondaire — Ne pas saisir.**

```yaml
secondary_motion_profile: AST-SECONDARY-CAPE-001-v001
piece: AST-WEAR-CAPE-001
source_method: blender_cloth_candidate
runtime_representation_candidates:
  - skinned_bones
  - baked_animation
  - reduced_static_shape
collision_proxies:
  - torso_capsule
  - shoulder_capsules
  - pelvis_capsule
forbidden_assumption: direct_blender_cache_runtime_support
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la simulation Blender peut servir à la fabrication ou au test.
- **Candidats runtime :** plusieurs représentations doivent être comparées.
- **Collisions :** les proxies restent simplifiés et dédiés au besoin.
- **Interdiction :** un cache Blender n'est jamais présumé compatible avec Godot.

## 19. Proxies de collision

Les collisions de simulation ne doivent pas reprendre le maillage complet du corps. Utiliser des volumes simples correspondant aux régions utiles : capsules pour membres, volume simplifié du torse, épaules, bassin et éventuellement accessoires proches.

Les proxies réduisent le coût, évitent les accroches sur les doigts ou petits détails, stabilisent les tests, reproduisent la configuration et distinguent collision de fabrication et collision gameplay. Une collision de tissu n'est pas une hitbox, une collision de déplacement ou une règle de combat.

> **[LECTURE] Profil de collisions de simulation — Ne pas saisir.**

```yaml
simulation_collision_profile: AST-CLOTH-COLLISION-HUMAN-001-v001
purpose: blender_cloth_manufacturing_test
proxies:
  - id: torso_capsule
    source_region: torso
  - id: upper_arm_l_capsule
    source_region: upper_arm_l
  - id: upper_arm_r_capsule
    source_region: upper_arm_r
  - id: pelvis_capsule
    source_region: pelvis
excluded_regions:
  - fingers
  - facial_features
  - hair
gameplay_collision_reference: none
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **But :** le profil nomme explicitement la simulation Blender.
- **Volumes :** seules les régions susceptibles de toucher la pièce sont retenues.
- **Exclusions :** les petits détails instables sont retirés.
- **Séparation :** aucune collision gameplay n'est dérivée de ce profil.

## 20. Simulation de tissu dans Blender

La simulation est utile pour explorer chute, compression, plis et collisions. Elle ne remplace ni le design du patron ni le skinning. Avant de lancer une simulation :

1. appliquer ou documenter l'échelle ;
2. vérifier les normales ;
3. préparer les coutures et contraintes ;
4. simplifier le maillage de simulation ;
5. construire les proxies de collision ;
6. fixer les points réellement attachés ;
7. choisir une plage de poses et de mouvements ;
8. versionner les paramètres ;
9. conserver le cache hors des sources publiées si le projet le prévoit ;
10. comparer la simulation au résultat destiné au jeu.

Les paramètres physiques dépendent de l'échelle, du maillage et du résultat artistique. Le chapitre n'impose aucune valeur universelle.

> **[LECTURE] Profil d'essai de tissu — Ne pas saisir.**

```yaml
cloth_test_profile: AST-CLOTH-CAPE-001-v001
software: Blender
mesh_role: simulation_proxy
scale_check: required
normal_check: required
pin_group: cape_shoulders
collision_profile: AST-CLOTH-COLLISION-HUMAN-001-v001
test_actions:
  - idle_turn
  - walk
  - run
  - crouch
cache_policy:
  source_cache_versioned: false
  approved_result_manifested: true
parameter_values: pending_measurement
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Maillage :** le proxy de simulation peut être distinct du maillage final.
- **Attache :** `pin_group` identifie les sommets fixés.
- **Actions :** plusieurs mouvements révèlent des défauts différents.
- **Paramètres :** aucune valeur n'est déclarée correcte avant mesure.

## 21. Convertir ou baker un résultat de simulation

Après un test réussi, décider ce qui devient source de production : une forme de repos améliorée, des plis sculptés ou bakés, une animation bakée limitée, une chaîne d'os secondaires, des formes correctives ou un maillage simplifié sans simulation runtime.

Conserver version Blender, profil de simulation, plage d'images, action source, méthode de conversion, perte acceptable, statut de l'export et limites observées. Un cache non versionné ne doit pas devenir l'unique source d'un asset.

> **[LECTURE] Décision de conversion — Ne pas saisir.**

```yaml
simulation_conversion:
  source_profile: AST-CLOTH-CAPE-001-v001
  source_action: walk
  frame_range: pending
  selected_representation: pending_decision
  candidates:
    - rest_shape_revision
    - corrective_shapes
    - skinned_secondary_bones
    - baked_animation
  cache_is_canonical: false
  export_test: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** le profil et l'action permettent de reproduire le test.
- **Décision :** la représentation finale reste ouverte jusqu'à comparaison.
- **Canon :** le cache n'est jamais la seule source.
- **Export :** la décision reste bloquée sans test GLB.

## 22. Prévenir le clipping

Le clipping doit être réduit par plusieurs leviers, dans cet ordre :

1. refuser les combinaisons incompatibles ;
2. corriger le patron ou les volumes ;
3. corriger le skinning ;
4. ajuster les couches et attaches ;
5. masquer les régions du corps réellement couvertes ;
6. employer des formes correctives si le rig les autorise ;
7. accepter une limite documentée lorsque la correction serait disproportionnée.

Un masque corporel ne doit pas cacher une erreur visible aux ouvertures. Il ne doit pas supprimer des régions nécessaires à une autre pièce autorisée.

> **[LECTURE] Cas de clipping — Ne pas saisir.**

```yaml
clipping_resolution:
  case_id: AST-CLIP-CASE-014
  pieces:
    - AST-WEAR-TUNIC-001
    - AST-WEAR-BELT-001
  pose: crouch
  observed_region: lower_torso
  attempted_fixes:
    - fit_volume_adjustment
    - weight_correction
  body_mask_candidate: abdomen_lower
  opening_visibility_check: pending
  other_combination_regression: pending
  decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cas :** chaque problème est relié à des pièces, une pose et une région.
- **Ordre :** le masque n'est proposé qu'après les corrections de volume et de poids.
- **Régression :** les autres combinaisons doivent être retestées.
- **Décision :** le cas reste bloqué tant que les ouvertures ne sont pas vérifiées.

## 23. Masquage de géométrie corporelle

Le masque peut être implémenté par variantes de maillage, surfaces séparées, groupes de régions ou autre mécanisme compatible avec le pipeline. Le contrat reste indépendant de l'implémentation.

Une région masquée doit être entièrement couverte par une pièce opaque, inaccessible dans les poses autorisées, compatible avec les autres couches, restaurée lorsque la pièce est retirée, conservée dans les LOD où elle redevient visible et testée sous plusieurs angles.

> **[LECTURE] Profil de masque corporel — Ne pas saisir.**

```yaml
body_mask_profile: AST-BODY-MASK-TUNIC-001-v001
wearable: AST-WEAR-TUNIC-001
regions_hidden:
  - torso_upper
  - torso_mid
regions_never_hidden:
  - neck
  - wrists
  - hands
conditions:
  opacity_required: opaque
  compatible_outer_layers_required: true
  removal_restores_body: true
pose_and_camera_review: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Régions :** les zones masquées et protégées sont explicitement distinguées.
- **Conditions :** l'opacité et les couches externes font partie du contrat.
- **Réversibilité :** retirer la pièce doit restaurer le corps.
- **Preuve :** poses et caméras sont nécessaires avant acceptation.

## 24. Matériaux, atlas et frontière du chapitre 16

Le chapitre 11 peut définir les besoins matériels propres au kit : textile mat, cuir, métal peint, métal nu, rembourrage, nombre de surfaces, possibilités d'atlas, masques de teinte, variantes de salissure ou d'usure visuelle et exigences de transparence.

Il ne redéfinit pas les cartes PBR, les espaces colorimétriques, la compression ni la bibliothèque générale. Ces règles appartiennent au chapitre 16.

> **[LECTURE] Plan matériel du kit — Ne pas saisir.**

```yaml
wearable_material_plan: AST-WEAR-MAT-PLAN-001-v001
surfaces:
  cloth:
    profile: AST-MAT-CLOTH-WOOL-001-v001
  leather:
    profile: AST-MAT-LEATHER-001-v001
  painted_metal:
    profile: AST-MAT-METAL-PAINTED-001-v001
atlas_candidates:
  - [cloth, leather]
  - [small_accessories]
tint_masks:
  primary: required
  secondary: optional
transparent_materials:
  allowed_only_with_overdraw_test: true
chapter_16_dependency: required
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** le kit référence les matériaux sans redéfinir leur pipeline.
- **Atlas :** les groupes sont des candidats à valider contre la qualité et les UV.
- **Teintes :** les masques permettent des variantes sans multiplier toutes les textures.
- **Transparence :** elle reste conditionnée à un test d'overdraw.

## 25. Variantes, usure visuelle et personnalisation

Les variantes du chapitre restent visuelles : couleurs et matières autorisées, longueur de manche ou d'ourlet, présence d'ornements, versions propres, poussiéreuses ou usées, emblèmes et ajustements morphologiques qualifiés.

Elles ne définissent ni rareté, ni protection, ni valeur, ni bonus. Une variante doit conserver les mêmes contrats d'attache et de compatibilité, ou déclarer une nouvelle version.

> **[LECTURE] Variante visuelle — Ne pas saisir.**

```yaml
wearable_variant: AST-WEAR-TUNIC-001-VAR-FOREST
base_piece: AST-WEAR-TUNIC-001
visual_changes:
  primary_tint: forest_green
  secondary_tint: muted_brown
  emblem: AST-EMBLEM-WARDEN-001
  wear_state: light
geometry_changes:
  sleeve_length: unchanged
fit_profile: AST-FIT-HUMAN-MEDIUM-001-v001
compatibility_profile: AST-COMPAT-TUNIC-001-v001
gameplay_stats: excluded
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Héritage :** la variante référence une pièce de base.
- **Changements :** les modifications visuelles sont distinguées des changements géométriques.
- **Compatibilité :** le profil reste explicite même si la géométrie ne change pas.
- **Exclusion :** aucune statistique n'est portée par la variante.

## 26. Profils LOD

Le LOD d'un kit porté doit considérer :

- réduction géométrique de chaque pièce ;
- fusion ou suppression de petits accessoires ;
- conservation de la silhouette ;
- réduction des surfaces et matériaux ;
- simplification des sangles et coutures ;
- remplacement d'une simulation ou chaîne secondaire ;
- cohérence du masque corporel ;
- continuité des attaches ;
- distance d'apparition ;
- coût de la combinaison complète, pas seulement d'une pièce isolée.

Une boucle de ceinture peut disparaître si elle ne modifie pas la silhouette. Une épaulière ou une cape ne peut pas disparaître au même seuil si elle définit l'identité du personnage.

> **[LECTURE] Profil LOD du kit — Ne pas saisir.**

```yaml
wearable_lod_profile: AST-WEAR-LOD-WARDEN-001-v001
lod0:
  pieces: all
  accessories: all
  material_slots: provisional
  secondary_motion: full_candidate
lod1:
  pieces: all
  accessories: simplified
  material_slots: reduced_candidate
  secondary_motion: reduced_candidate
lod2:
  silhouette_pieces:
    - jacket
    - shoulder_armor
    - cape
  small_accessories: removed_or_baked
  body_mask_consistency: required
distance_thresholds_m: pending_measurement
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** chaque LOD décrit pièces, accessoires, matériaux et mouvement secondaire.
- **Silhouette :** les pièces identitaires sont protégées.
- **Masques :** la géométrie corporelle ne doit pas réapparaître lors d'une transition.
- **Distances :** les seuils restent à mesurer dans Godot.

## 27. Assemblage modulaire

L'assemblage doit rester déterministe : mêmes identifiants, mêmes profils et mêmes règles produisent la même combinaison. L'outil d'assemblage visuel doit :

1. charger les pièces demandées ;
2. vérifier le profil de personnage ;
3. appliquer les conflits et prérequis ;
4. résoudre les variantes conditionnelles ;
5. appliquer les masques corporels ;
6. relier les meshes au squelette et aux attaches ;
7. choisir le LOD ou profil de qualité ;
8. produire un rapport ;
9. refuser toute combinaison indéterminée.

Le chapitre ne développe pas le système d'inventaire. Il décrit un assemblage de présentation testable.

> **[LECTURE] Requête d'assemblage — Ne pas saisir.**

```json
{
  "assembly_request": "AST-ASSEMBLY-TEST-001",
  "character_profile": "AST-CHR-HUMAN-BASE-001",
  "pieces": [
    "AST-WEAR-BASE-001",
    "AST-WEAR-TUNIC-001",
    "AST-WEAR-BELT-001",
    "AST-WEAR-SHOULDER-001",
    "AST-WEAR-CAPE-001"
  ],
  "quality_profile": "closeup",
  "resolve_unknown_as": "blocked",
  "result": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la requête contient la morphologie, les pièces et le profil de qualité.
- **Fermeture :** `resolve_unknown_as` bloque une combinaison non testée.
- **Indépendance :** aucun contenu d'inventaire ou de combat n'est nécessaire.
- **Résultat :** le rapport sera généré après la validation structurelle.

## 28. Préparer l’export GLB

Le lot exporté doit contenir uniquement les éléments nécessaires : meshes portés, squelette ou liaisons compatibles, skinning, matériaux et textures prises en charge, animations de test seulement si leur inclusion est volontaire, noms stables et LOD lorsque le pipeline les transporte ou les référence.

Avant export :

1. vérifier unités et transformations ;
2. vérifier noms d'os et de pièces ;
3. vérifier poids et sommets sans influence ;
4. vérifier modificateurs appliqués ou supportés ;
5. vérifier matériaux et transparence ;
6. vérifier orientation des normales ;
7. vérifier l'absence d'objets de travail ;
8. exporter une version immuable ;
9. enregistrer l'empreinte.

> **[LECTURE] Profil d'export — Ne pas saisir.**

```yaml
gltf_export_profile: AST-GLTF-WEARABLE-001-v001
container: GLB
source_collection: EXPORT_WEARABLES
include:
  meshes: true
  skinning: true
  materials: true
  selected_animations: false
exclude:
  simulation_caches: true
  collision_work_meshes: true
  reference_body: true
naming_check: required
transform_check: required
weight_check: required
godot_import_test: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conteneur :** GLB regroupe la scène exportée selon le pipeline du projet.
- **Inclusion :** le skinning et les matériaux sont explicitement requis.
- **Exclusion :** caches, maillages de travail et corps de référence ne sont pas publiés.
- **État :** l'export reste bloqué jusqu'au test d'import.

## 29. Scène Godot dérivée

Ne jamais modifier directement la scène importée comme source canonique. Créer une scène dérivée qui ajoute personnage pilote, squelette de référence, pièces portées, attaches, caméras, lumières, contrôleur de poses, commutateur de combinaisons, commutateur de LOD, validateur structurel et panneau de rapport.

La scène doit pouvoir tester une pièce seule et une combinaison complète.

> **[LECTURE] Arbre de scène proposé — Ne pas saisir.**

```text
WearableValidationLab (Node3D)
├── ReferenceRig (Node3D)
│   ├── ImportedCharacter (Node3D)
│   │   ├── Skeleton3D
│   │   ├── BodyMesh (MeshInstance3D)
│   │   └── Wearables (Node3D)
│   │       ├── BaseLayer (MeshInstance3D)
│   │       ├── Tunic (MeshInstance3D)
│   │       ├── Belt (MeshInstance3D)
│   │       ├── ShoulderArmor (MeshInstance3D)
│   │       └── Cape (MeshInstance3D)
│   └── Attachments (Node3D)
├── PoseController (Node)
├── CombinationController (Node)
├── LodController (Node)
├── LightingRig (Node3D)
├── Cameras (Node3D)
└── WearableAssetValidator (Node)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** le personnage importé reste sous une scène de validation dérivée.
- **Meshes :** chaque pièce peut référencer le même `Skeleton3D` et une ressource `Skin` qualifiée.
- **Contrôleurs :** poses, combinaisons et LOD produisent des rapports distincts.
- **Validateur :** le nœud inspecte la structure sans modifier les assets.

## 30. Contrat du validateur GDScript

Le validateur vérifie uniquement des propriétés observables : présence du squelette, pièces requises, association des meshes skinnés, ressource `Skin` lorsque nécessaire, noms de pièces et attaches, surfaces, matériaux, profils et métadonnées attendus, masques, LOD et statut de combinaison.

Il ne juge pas la beauté, le tombé ou le réalisme. Ces décisions exigent captures et revue humaine.

> **[VSC] Créer `tests/art/wearables/wearable_asset_validator.gd`.**

```gdscript
extends Node
class_name WearableAssetValidator

@export var character_root: Node3D
@export var required_piece_names: PackedStringArray = []
@export var required_attachment_names: PackedStringArray = []

func validate() -> Dictionary:
    var errors: Array[String] = []
    var warnings: Array[String] = []

    if character_root == null:
        errors.append("character_root_missing")
        return _result(errors, warnings)

    var skeleton := _find_skeleton(character_root)
    if skeleton == null:
        errors.append("skeleton_missing")

    _check_required_meshes(character_root, skeleton, errors, warnings)
    _check_required_attachments(character_root, errors)
    return _result(errors, warnings)

func _find_skeleton(root: Node) -> Skeleton3D:
    if root is Skeleton3D:
        return root as Skeleton3D
    for child in root.get_children():
        var found := _find_skeleton(child)
        if found != null:
            return found
    return null

func _check_required_meshes(
    root: Node,
    skeleton: Skeleton3D,
    errors: Array[String],
    warnings: Array[String]
) -> void:
    for piece_name in required_piece_names:
        var node := root.find_child(piece_name, true, false)
        if node == null:
            errors.append("piece_missing:%s" % piece_name)
            continue
        if not node is MeshInstance3D:
            errors.append("piece_not_mesh_instance:%s" % piece_name)
            continue

        var mesh_instance := node as MeshInstance3D
        if mesh_instance.mesh == null:
            errors.append("piece_mesh_missing:%s" % piece_name)
        if skeleton != null and mesh_instance.skeleton.is_empty():
            warnings.append("skeleton_path_empty:%s" % piece_name)

func _check_required_attachments(root: Node, errors: Array[String]) -> void:
    for attachment_name in required_attachment_names:
        var node := root.find_child(attachment_name, true, false)
        if node == null:
            errors.append("attachment_missing:%s" % attachment_name)

func _result(errors: Array[String], warnings: Array[String]) -> Dictionary:
    return {
        "accepted": errors.is_empty(),
        "errors": errors,
        "warnings": warnings
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `WearableAssetValidator` étend `Node` et peut être attaché à la scène de test.
- **Entrées :** `character_root`, `required_piece_names` et `required_attachment_names` sont configurés dans l'inspecteur.
- **Retour :** `validate()` renvoie un `Dictionary` contenant `accepted`, `errors` et `warnings`.
- **Récursion :** `_find_skeleton()` parcourt les enfants et retourne le premier `Skeleton3D` trouvé ou `null`.
- **Types :** `Array[String]` impose des messages textuels et `PackedStringArray` stocke les noms requis.
- **Opérateurs :** `==`, `!=`, `not`, `is` et `and` contrôlent présence, type et chemins.
- **Formatage :** l'opérateur `%` insère le nom de la pièce dans un code stable.
- **Invariant :** une erreur bloque l'acceptation ; un avertissement seul ne la bloque pas.
- **Limite :** le script ne mesure ni clipping, ni qualité de skinning, ni coût GPU.

## 31. Étendre le rapport avec les surfaces et matériaux

Le nombre de surfaces n'est pas une qualité en soi. Il sert à repérer une multiplication inattendue des matériaux. Le validateur peut relever nombre de surfaces par mesh, matériaux absents, matériaux transparents, noms de surfaces et dépassements du budget provisoire.

Toute limite reste configurable et ne doit pas être codée comme vérité universelle.

> **[VSC] Ajouter l'inspection suivante au validateur.**

```gdscript
@export_range(1, 32, 1) var provisional_surface_limit: int = 8

func inspect_surfaces(mesh_instance: MeshInstance3D) -> Dictionary:
    var surface_count: int = 0
    if mesh_instance.mesh != null:
        surface_count = mesh_instance.mesh.get_surface_count()

    var missing_material_surfaces: Array[int] = []
    for surface_index in range(surface_count):
        if mesh_instance.get_active_material(surface_index) == null:
            missing_material_surfaces.append(surface_index)

    return {
        "surface_count": surface_count,
        "over_provisional_limit": surface_count > provisional_surface_limit,
        "missing_material_surfaces": missing_material_surfaces
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** `provisional_surface_limit` est un entier éditable borné de 1 à 32.
- **Retour :** `inspect_surfaces()` renvoie un dictionnaire de mesures structurelles.
- **Boucle :** `range(surface_count)` produit les indices valides de surface.
- **Méthode :** `get_active_material()` retourne le matériau effectivement utilisé ou `null`.
- **Comparaison :** `>` signale un dépassement provisoire sans prétendre mesurer le coût total.
- **Limite :** le rapport ne remplace pas une mesure de draw calls ou d'overdraw.

## 32. Jeu de poses de validation

Les poses doivent révéler les zones critiques : A-pose, bras devant, bras latéraux, bras au-dessus de la tête, torsion du torse, assise, accroupissement, pas long, montée de marche, flexion profonde du coude et du genou, course et réception si prévue.

Pour chaque pose, capturer face, profil, dos et trois quarts, puis noter clipping, écrasement, perte de volume, flottement, glissement d'attache, comportement de l'armure, continuité des masques, silhouette et limite acceptable ou bloquante.

> **[LECTURE] Jeu de poses — Ne pas saisir.**

```yaml
pose_test_set: AST-POSE-WEARABLE-001-v001
poses:
  - A_pose
  - arms_forward
  - arms_side
  - arms_overhead
  - torso_twist
  - seated
  - crouch
  - long_step
  - stair_step
  - run_contact
views:
  - front
  - side
  - back
  - three_quarter
checks:
  - clipping
  - volume_loss
  - floating
  - attachment_drift
  - rigid_plate_bending
  - mask_consistency
  - silhouette
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Poses :** le jeu couvre épaules, torse, hanches, genoux et mouvement global.
- **Vues :** une erreur cachée de face peut devenir visible de dos.
- **Contrôles :** les défauts de skinning, attache et masquage sont distingués.
- **État :** le jeu reste bloqué sans captures et décisions.

## 33. Protocole de performance

Mesurer la combinaison complète dans Godot, pas seulement chaque pièce : CPU, GPU, mémoire vidéo, mémoire système, meshes visibles, surfaces, matériaux, draw calls, ombres, transparence, overdraw, coût du squelette, skinning, changement de LOD et nombre de personnages équipés simultanément.

Scénarios minimaux : personnage seul en gros plan, personnage à distance de dialogue, groupe proche, groupe moyen, densité cible, transition de LOD et combinaison la plus coûteuse autorisée. Aucune valeur n'est inventée dans ce chapitre.

> **[LECTURE] Manifeste de benchmark — Ne pas saisir.**

```json
{
  "benchmark_id": "AST-BENCH-WEARABLE-001",
  "hardware_profile": "reference_windows_amd",
  "scenarios": [
    "single_closeup",
    "single_dialogue",
    "near_group",
    "medium_group",
    "target_density",
    "lod_transition",
    "worst_supported_combination"
  ],
  "metrics": [
    "cpu_ms",
    "gpu_ms",
    "vram_mb",
    "system_memory_mb",
    "visible_meshes",
    "material_surfaces",
    "draw_calls",
    "overdraw_capture",
    "skeleton_skinning_cost"
  ],
  "values": "pending_measurement",
  "status": "blocked"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénarios :** les cas isolés et de groupe sont séparés.
- **Mesures :** temps, mémoire, surfaces, draw calls et skinning sont relevés ensemble.
- **Valeurs :** aucune mesure n'est simulée dans le document.
- **Décision :** le benchmark reste bloqué jusqu'à exécution sur le matériel de référence.

## 34. Provenance et droits

Chaque pièce doit conserver auteur ou équipe, source des références, licence ou statut interne, textures et motifs externes, emblèmes, transformations, outils et versions, consentement lorsque des vêtements réels identifiables ou des scans sont utilisés, et restrictions de redistribution.

Une facture, un téléchargement gratuit ou une image trouvée en ligne ne suffit pas à qualifier les droits.

> **[LECTURE] Registre de provenance — Ne pas saisir.**

```yaml
provenance_record: AST-PROV-WEAR-TUNIC-001-v001
asset: AST-WEAR-TUNIC-001
creator: internal_team
references:
  - id: AST-REF-CLOTHING-014
    usage: construction_reference
    rights_status: pending_review
textures:
  - id: AST-TEX-CLOTH-023
    license_id: pending
emblems:
  - id: AST-EMBLEM-WARDEN-001
    ownership: internal
tools:
  blender: 5.2.0
distribution_status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Références :** chaque source possède un identifiant et un usage limité.
- **Textures :** une licence manquante bloque la diffusion.
- **Emblèmes :** la propriété est qualifiée séparément.
- **État :** `distribution_status` reste bloqué tant qu'un droit est en attente.

## 35. Parcours Solo

Le parcours Solo privilégie un kit pilote complet avant une grande garde-robe, deux profils morphologiques au maximum au départ, peu de catégories de couches, des pièces combinables avec règles strictes, peu de matériaux partagés, des masques simples, une scène unique de validation et un rapport par combinaison prioritaire.

Le créateur Solo refuse les combinaisons coûteuses à maintenir au lieu de promettre une compatibilité universelle.

> **[LECTURE] Périmètre Solo — Ne pas saisir.**

```yaml
solo_scope:
  pilot_kit: AST-WEAR-KIT-WARDEN-001
  character_profiles_max: 2
  supported_complete_combinations: limited
  cloth_runtime_simulation: excluded_until_measured
  material_library: compact
  validation_scene: wearable_validation_lab
  unknown_compatibility_policy: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limite :** le nombre de profils et combinaisons est volontairement restreint.
- **Simulation :** aucune simulation runtime n'est adoptée sans mesure.
- **Bibliothèque :** des matériaux partagés réduisent la maintenance.
- **Politique :** toute compatibilité inconnue reste bloquée.

## 36. Parcours Studio

Le parcours Studio ajoute propriétaires par famille de pièce, profils morphologiques versionnés, bibliothèque de patrons, conventions de skinning, revue croisée art-rig-animation-intégration, matrice centralisée, tests automatiques, campagnes de poses et performance par plateforme, catalogue de matériaux et historique des dérogations.

La responsabilité de création, skinning, intégration et validation peut être séparée, mais le contrat d'asset reste commun.

> **[LECTURE] Répartition Studio — Ne pas saisir.**

```yaml
studio_roles:
  garment_artist:
    owns:
      - pattern
      - topology
      - visual_variants
  technical_artist:
    owns:
      - skinning_profile
      - simulation_conversion
      - lod_profile
  integration_artist:
    owns:
      - glb_import
      - derived_scene
      - assembly_report
  reviewer:
    owns:
      - compatibility_decision
      - pose_review
      - performance_gate
publication:
  approved_versions_immutable: true
  exceptions_require_owner_and_reason: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôles :** chaque responsabilité possède un propriétaire identifiable.
- **Partage :** les équipes travaillent sur les mêmes profils versionnés.
- **Publication :** une version approuvée n'est pas modifiée silencieusement.
- **Dérogations :** toute exception exige propriétaire et cause.

## 37. Porte d’acceptation

Une pièce ou un kit est accepté seulement si l'identifiant, la provenance et le statut juridique sont complets ; le profil morphologique est explicite ; couches, conflits et prérequis sont déclarés ; patron, volumes et marges ont été revus ; skinning et zones rigides ont été testés ; attaches sont stables ; collisions et simulations ont un but clair ; clipping majeur est absent ; masques ne créent pas de trous ; combinaisons autorisées sont identifiées ; LOD conservent silhouette et attaches ; GLB est importé ; matériaux respectent le budget mesuré ; performances sont mesurées ; réserves restantes sont acceptées par un responsable.

Le statut `accepted` n'est jamais attribué par défaut.

> **[LECTURE] Porte d'acceptation — Ne pas saisir.**

```yaml
acceptance_gate: AST-GATE-WEARABLE-001-v001
required:
  provenance: pending
  legal_status: pending
  fit_review: pending
  layering_review: pending
  skinning_pose_grid: pending
  attachment_review: pending
  simulation_or_conversion_review: pending
  clipping_review: pending
  body_mask_review: pending
  compatibility_matrix: pending
  lod_review: pending
  glb_import: pending
  performance_measurement: pending
decision:
  blocking_failures: unknown
  reviewer: unassigned
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exigences :** chaque ligne correspond à une preuve distincte.
- **Décision :** le nombre d'échecs reste inconnu avant exécution.
- **Responsabilité :** un responsable humain doit être assigné.
- **Fermeture :** `blocked` est conservé tant qu'une preuve est `pending`.

## 38. Erreurs fréquentes et corrections

### 38.1 Autoriser toutes les combinaisons par défaut

**Symptôme :** des pièces se traversent ou écrasent leurs volumes alors que le catalogue les annonce compatibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
compatibility:
  default: supported
  untested_pairs: accepted
  conflict_reasons: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une paire non testée devient implicitement valide et aucune cause ne permet d'expliquer les échecs.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
compatibility:
  default: blocked
  untested_pairs: untested
  conflict_reasons: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction ferme le système par défaut et exige une décision explicable pour chaque paire.

### 38.2 Coller le vêtement au corps avec Shrinkwrap

**Symptôme :** la pièce semble correcte en pose neutre mais n'a plus d'épaisseur ni de marge aux articulations.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
fit:
  shrinkwrap_offset_m: 0.0
  ease_profile: none
  pose_review: A_pose_only
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un collage exact copie le corps et ne réserve aucun espace pour les couches ou le mouvement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
fit:
  shrinkwrap_use: blockout_only
  ease_profile: AST-EASE-TUNIC-001-v001
  pose_review: AST-POSE-WEARABLE-001-v001
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite Shrinkwrap au blockout, ajoute une marge documentée et impose le jeu de poses.

### 38.3 Accepter le transfert de poids automatique

**Symptôme :** les épaules s'effondrent, les aisselles pincent et la ceinture se courbe comme du tissu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
weight_transfer:
  automatic: complete
  manual_review: false
  rigid_regions: ignored
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le transfert ne comprend ni l'épaisseur ni les zones rigides et aucune correction n'est prévue.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
weight_transfer:
  automatic: first_pass
  manual_review: required
  rigid_regions:
    - belt_buckle
  pose_grid: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction traite l'automatisation comme une première passe et protège les régions rigides.

### 38.4 Utiliser le maillage complet du corps comme collision de tissu

**Symptôme :** la simulation accroche les doigts, les détails du visage ou de petites irrégularités et devient instable.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
cloth_collision:
  source: full_character_render_mesh
  simplification: none
  purpose: unspecified
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le maillage de rendu contient des détails inutiles et mélange les usages de collision.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
cloth_collision:
  source: AST-CLOTH-COLLISION-HUMAN-001-v001
  simplification: capsules_and_simple_hulls
  purpose: blender_cloth_manufacturing_test
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise des proxies simples et nomme explicitement le but de la collision.

### 38.5 Supposer que le cache Blender fonctionnera dans Godot

**Symptôme :** la cape n'a aucun mouvement secondaire après l'import GLB.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
cloth_result:
  blender_cache: approved
  glb_export: expected_to_include_cache
  godot_representation: automatic
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le cache de simulation n'est pas un contrat d'échange runtime garanti par GLB.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
cloth_result:
  blender_cache: manufacturing_evidence
  runtime_representation:
    candidates:
      - skinned_bones
      - baked_animation
      - reduced_static_shape
  godot_import_test: pending
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare preuve de fabrication et représentation runtime, puis exige un test d'import.

### 38.6 Masquer tout le torse sous une tunique

**Symptôme :** le cou, les poignets ou une ouverture de veste révèlent des trous dans le personnage.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
body_mask:
  hidden_regions:
    - entire_torso_and_arms
  opening_review: none
  removal_restores_body: assumed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le masque dépasse les régions réellement couvertes et ne vérifie ni ouvertures ni réversibilité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
body_mask:
  hidden_regions:
    - torso_upper
    - torso_mid
  protected_regions:
    - neck
    - wrists
    - hands
  opening_review: pending
  removal_restores_body: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite les régions, protège les ouvertures et impose le retour du corps.

### 38.7 Déformer une plaque d’armure comme un textile

**Symptôme :** l'épaulière se plie au milieu lorsque le bras se lève.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
armor_plate:
  skinning: copied_from_body
  influence_count: unrestricted
  rigid_review: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les poids corporels font courber une pièce qui devrait préserver ses plans.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
armor_plate:
  behavior: rigid_attached
  parent_candidate: upper_arm_l
  padding_behavior: skinned_soft
  rigid_review: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare plaque et rembourrage et teste un parentage rigide.

### 38.8 Créer les objets tenus et les armes dans ce chapitre

**Symptôme :** le kit vestimentaire contient pivots de prise, dégâts, projectiles et statistiques.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
chapter_11:
  owns:
    - clothing
    - held_weapons
    - projectile_collisions
    - combat_stats
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les objets tenus appartiennent au chapitre 12 et les règles de combat au Livre II.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
chapter_11:
  owns:
    - worn_clothing
    - worn_armor
    - body_attached_accessories
  deferred:
    held_objects_and_weapons: chapter_12
    combat_rules: Livre_II
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve les éléments portés et déplace clairement les autres responsabilités.

### 38.9 Supprimer les pièces identitaires trop tôt dans les LOD

**Symptôme :** le personnage garde ses triangles budgétés mais perd sa cape et son épaulière reconnaissables.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod2:
  cape: removed
  shoulder_armor: removed
  triangle_budget: passed
  silhouette_test: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le budget géométrique ignore les traits qui portent l'identité visuelle.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod2:
  cape: simplified
  shoulder_armor: preserved
  triangle_budget: provisional
  silhouette_test: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction protège les pièces identitaires et maintient le test de silhouette.

### 38.10 Déclarer le kit terminé après la revue Blender

**Symptôme :** les pièces semblent correctes dans Blender mais n'ont jamais été importées, combinées ni mesurées dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
combination_test: not_executed
performance_test: not_executed
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une revue Blender ne prouve ni le skin dans Godot, ni les attaches, ni les masques, ni le coût.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
combination_test: not_executed
performance_test: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve le blocage jusqu'aux preuves moteur.

## 39. Livrables à conserver

Le plan maître exige cinq livrables permanents :

1. **kits vestimentaires** — pièces, variantes, sources, exports et manifeste ;
2. **règles de layering** — catégories, ordre, conflits, prérequis et masques ;
3. **profils de skinning** — stratégies par région, rigidités, corrections et poses ;
4. **collisions de simulation** — proxies, but, paramètres et conversion ;
5. **matrice de compatibilité** — pièces, morphologies, conditions, causes et preuves.

L'arborescence du début du chapitre devient l'inventaire permanent. Les exports restent distincts des sources, les caches restent non canoniques et les rapports QA internes ne sont pas ajoutés au manuel lecteur.

> **[LECTURE] Manifeste de livraison — Ne pas saisir.**

```yaml
deliverable_manifest: AST-WEAR-DELIVERY-001-v001
wearable_kits:
  pilot: AST-WEAR-KIT-WARDEN-001
  status: blocked
layering_rules:
  profile: AST-LAYER-RULES-001-v001
  status: blocked
skinning_profiles:
  profiles:
    - AST-SKIN-TUNIC-001-v001
    - AST-SKIN-SHOULDER-PAD-001-v001
  status: blocked
simulation_collisions:
  profile: AST-CLOTH-COLLISION-HUMAN-001-v001
  status: blocked
compatibility_matrix:
  profile: AST-COMPAT-WEARABLES-001-v001
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifeste :** les cinq livrables du plan maître sont regroupés dans un lot versionné.
- **Profils :** chaque livrable renvoie vers des contrats séparés.
- **État :** tous restent bloqués tant que les assets et preuves ne sont pas produits.
- **Traçabilité :** le manifeste devient l'entrée de la revue de production.

## 40. Synthèse opérationnelle pour Project Asteria

Le chapitre 11 fournit à `Project Asteria` une méthode complète pour produire un système visuel d'équipement porté. Le kit du Gardien est encadré par un brief d'usage, des catégories de comportement, des règles de layering, des profils morphologiques, des patrons, des marges de mouvement, une topologie, des profils de skinning, des zones rigides, des attaches, des proxies de collision, une simulation Blender qualifiée, une stratégie de conversion, des masques corporels, des matériaux, des variantes, des LOD, une matrice de compatibilité, un export GLB, une scène Godot dérivée et un validateur structurel.

Le kit reste bloqué tant que les pièces, patrons, poids, attaches, collisions, simulations, masques, atlas, LOD, GLB, scène Godot, combinaisons et mesures ne sont pas réellement produits. Le chapitre prépare les tests de rig, d'animation et d'intégration sans définir les contrôleurs de production. Les objets tenus et armes sont réservés au chapitre 12 ; les règles d'inventaire et de combat restent dans le Livre II.

## 41. Références techniques officielles

Les références suivantes doivent être consultées et qualifiées lors de la matérialisation :

- [Blender Manual — Cloth](https://docs.blender.org/manual/en/latest/physics/cloth/index.html) ;
- [Blender Manual — Collision](https://docs.blender.org/manual/en/latest/physics/collision.html) ;
- [Blender Manual — Armature Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/armature.html) ;
- [Blender Manual — Data Transfer Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/modify/data_transfer.html) ;
- [Blender Manual — Surface Deform Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/surface_deform.html) ;
- [Blender Manual — Shrinkwrap Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/shrinkwrap.html) ;
- [Blender Manual — Solidify Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/solidify.html) ;
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html) ;
- [Godot 4.7 — MeshInstance3D](https://docs.godotengine.org/en/4.7/classes/class_meshinstance3d.html) ;
- [Godot 4.7 — Skeleton3D](https://docs.godotengine.org/en/4.7/classes/class_skeleton3d.html) ;
- [Godot 4.7 — Skin](https://docs.godotengine.org/en/4.7/classes/class_skin.html) ;
- [Godot 4.7 — BoneAttachment3D](https://docs.godotengine.org/en/4.7/classes/class_boneattachment3d.html) ;
- [Godot 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) ;
- [Godot 4.7 — ResourceImporterScene](https://docs.godotengine.org/en/4.7/classes/class_resourceimporterscene.html) ;
- [Godot — Mesh level of detail](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html) ;
- [Godot — Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html).

Les pages `latest` ou `stable` ne sont utilisées que lorsqu'une page versionnée équivalente n'est pas exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d'appliquer la procédure.
