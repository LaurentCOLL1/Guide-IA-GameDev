---
title: "Livre III — Chapitre 10 : Visages, peau, yeux, cheveux et pilosité"
id: "DOC-L3-CH10"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 10
last-verified: "2026-07-23T10:56:17+02:00"
audit-status: "complete"
audit-date: "2026-07-23T10:56:17+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-10.md"
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

# Visages, peau, yeux, cheveux et pilosité

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH10`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Les chapitres 6 et 7 ont défini les bases humaines et humanoïdes : proportions, volumes, zones expressives, compatibilité avec les rigs et limites morphologiques. Le chapitre 9 a ajouté les contrats de créatures, de silhouettes, de sockets et de collisions. Le présent chapitre ne recommence aucun de ces travaux. Il se concentre sur les éléments que le regard humain juge immédiatement en gros plan : visage, peau, yeux, bouche, dents, cheveux, barbe, sourcils, cils et pilosité.

Le fil rouge utilise une tête pilote documentaire de `Project Asteria`, identifiée `AST-CHR-FACE-PILOT-001`. Cette tête sert à relier la sculpture, la topologie, les matériaux spécialisés, les formes faciales de préparation, les solutions capillaires, les LOD et la scène de validation Godot. Elle n'est pas déclarée produite : le chapitre décrit les contrats, les choix, les contrôles et les preuves à obtenir.

Un visage crédible ne dépend pas d'un seul shader. Sa qualité résulte d'un accord entre volumes, transitions anatomiques, asymétrie, microdétails, orientation du regard, humidité, intersections, densité capillaire, éclairage et distance d'observation. Une amélioration locale peut détériorer l'ensemble : davantage de pores peut rendre la peau minérale, davantage de transparence peut créer des artefacts, davantage de cheveux peut détruire le budget, et davantage de blendshapes peut rendre les formes impossibles à maintenir.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Base humaine ou humanoïde validée
    ↓
Références et droits qualifiés
    ↓
Repères anatomiques et volumes du visage
    ↓
Topologie de déformation
    ↓
Sculpture primaire, secondaire et tertiaire
    ↓
Asymétrie contrôlée
    ↓
Matériaux peau, yeux, bouche et dents
    ↓
Cheveux, barbe, sourcils, cils et pilosité
    ↓
Formes faciales de préparation
    ↓
LOD géométriques, capillaires et matériels
    ↓
Export GLB et scène Godot dérivée
    ↓
Éclairage, intersections, transparence et coût
    ↓
Décision : accepter, corriger ou bloquer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** le visage part d'une base déjà dimensionnée ; il ne redéfinit ni le corps ni le squelette complet.
- **Ordre :** les volumes et la topologie précèdent les détails de peau et les solutions capillaires.
- **Preuve :** chaque étape produit un contrat ou un rapport vérifiable avant la décision.
- **Frontière :** la synchronisation labiale, les timings de voix et l'acting final restent au chapitre 27.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- transformer une intention de gros plan en critères observables ;
- distinguer forme primaire, forme secondaire, pli, pore et bruit ;
- placer les principaux repères du visage sans confondre méthode artistique et diagnostic médical ;
- organiser une topologie compatible avec ouverture de bouche, clignement, sourire, compression et étirement ;
- introduire une asymétrie contrôlée sans casser les correspondances nécessaires aux formes faciales ;
- séparer les responsabilités des cartes de couleur, roughness, normal et displacement ;
- préparer un matériau de peau avec diffusion sous-surface sans inventer de valeur universelle ;
- construire un œil en plusieurs volumes et contrôler cornée, iris, pupille, sclère et film humide ;
- préparer bouche, dents, langue et gencives en évitant les intersections visibles ;
- choisir entre géométrie, hair cards, courbes de cheveux, texture ou mélange de solutions ;
- organiser sourcils, cils, barbe, duvet et fourrure selon distance et budget ;
- préparer des shape keys de test sans produire les visèmes et timings du chapitre 27 ;
- définir des LOD cohérents pour la tête, les yeux, les cheveux et les matériaux ;
- importer la tête dans une scène Godot dérivée ;
- écrire un validateur structurel non destructif et comprendre ses fonctions, paramètres, types, retours et opérateurs ;
- conserver des réserves explicites lorsque Blender ou Godot n'ont pas été exécutés.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les contrats de données, procédures Blender, principes de matériau, organisation de scène et exemple GDScript sont relus. Ils ne constituent pas une preuve d'exécution.

Aucune tête finale, aucune sculpture, aucune retopologie, aucune texture, aucun matériau, aucun œil, aucune dentition, aucun groom, aucune hair card, aucun blendshape, aucun GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme produits. Les nombres de sommets, résolutions de texture, intensités, rayons, distances, nombres de cartes ou densités capillaires sont des budgets provisoires à confirmer sur le matériel de référence.

Le chapitre ne présente pas les proportions faciales comme des normes biologiques universelles. Les visages humains et humanoïdes varient fortement selon l'âge, l'ascendance, la morphologie, l'état de santé, les expressions, les choix artistiques et la stylisation. Les références doivent être diverses, consenties lorsque nécessaire et utilisées sans transformer une moyenne en règle.

## 4. Périmètre et frontières

Le chapitre couvre :

- topologie faciale et zones de déformation ;
- sculpture, asymétrie et variation ;
- matériaux spécialisés de peau, yeux, bouche, dents et muqueuses ;
- solutions de cheveux, barbe, sourcils, cils, duvet et pilosité ;
- transparence et intersections ;
- shape keys de préparation et expressions de test ;
- LOD géométriques, capillaires et matériels ;
- export GLB, scène dérivée et validation structurelle dans Godot ;
- tests de gros plan sous plusieurs éclairages.

Le chapitre ne couvre pas :

- la création complète des bases humaines et humanoïdes, déjà traitée aux chapitres 6 et 7 ;
- les silhouettes et collisions de créatures du chapitre 9 ;
- les vêtements, armures et accessoires du chapitre 11 ;
- le pipeline PBR transversal et les bibliothèques générales de matériaux du chapitre 16 ;
- la retopologie, les UV et le baking génériques du chapitre 17 ;
- le rig facial de production et les contraintes avancées du chapitre 19 ;
- les cycles d'animation et outils d'animation du chapitre 20 ;
- les phonèmes, visèmes, timings, coarticulation et synchronisation labiale du chapitre 27 ;
- les règles de dialogue, de gameplay ou d'intelligence artificielle du Livre II.

> **[LECTURE] Matrice des responsabilités — Ne pas saisir.**

```yaml
chapter_10:
  owns:
    - facial_lookdev_contract
    - skin_eye_mouth_material_profiles
    - hair_and_fur_solution_profiles
    - facial_test_shapes
    - facial_lod_profiles
  prepares:
    - chapter_19_facial_rig
    - chapter_27_lip_sync
  does_not_own:
    - body_anatomy
    - general_pbr_pipeline
    - generic_uv_baking_pipeline
    - dialogue_timing
    - gameplay_rules
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** chaque valeur de liste est une chaîne identifiant une responsabilité documentaire.
- **Préparation :** `prepares` signifie que le chapitre fournit des entrées, pas qu'il réalise le travail futur.
- **Exclusion :** `does_not_own` empêche les doublons et les modifications silencieuses de périmètre.
- **Résultat attendu :** une tâche ne peut être attribuée au chapitre 10 que si elle figure dans `owns` ou soutient directement ces éléments.

## 5. Prérequis et fichiers à ouvrir

Avant de commencer, le lecteur doit disposer :

- d'une base humaine ou humanoïde dont l'échelle, les axes et les zones expressives sont documentés ;
- d'un identifiant d'asset stable ;
- d'un registre de provenance ;
- de références autorisées ;
- d'un budget provisoire par plateforme ;
- d'une scène d'éclairage de référence ;
- des conventions Blender et Godot du projet.

Le lecteur ouvre :

- **[APP] Blender 5.2.0** pour la sculpture, la topologie, les matériaux, les formes faciales et les solutions capillaires ;
- **[APP] Godot 4.7.1-stable** pour l'import, la scène dérivée, les éclairages et les contrôles de coût ;
- **[VSC] Visual Studio Code** pour les contrats YAML, les rapports JSON et le validateur GDScript ;
- **[PS] PowerShell 7** pour créer les dossiers et lancer les contrôles documentaires.

> **[LECTURE] Arborescence de travail proposée — Ne pas saisir.**

```text
art/
├── blender/characters/
│   └── AST-CHR-FACE-PILOT-001/
├── characters/faces/
│   ├── briefs/
│   ├── anatomy/
│   ├── topology/
│   ├── sculpt/
│   ├── materials/
│   ├── eyes/
│   ├── mouth/
│   ├── hair/
│   ├── shapes/
│   └── lod/
├── textures/characters/
├── exports/characters/
├── provenance/
└── budgets/
tests/
└── art/faces/
    ├── face_validation_lab.tscn
    ├── face_asset_validator.gd
    ├── reports/
    └── captures/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les fichiers Blender restent séparés des exports GLB.
- **Spécialités :** peau, yeux, bouche, cheveux et formes possèdent des emplacements distincts.
- **Tests :** la scène, le script, les rapports et les captures sont regroupés sous `tests/art/faces`.
- **Résultat attendu :** un fichier peut être retrouvé par rôle sans dépendre du nom d'une personne.

> **[PS] Création des dossiers PowerShell — À saisir.**

```powershell
$root = "C:\ProjectAsteria"
$folders = @(
  "art\blender\characters\AST-CHR-FACE-PILOT-001",
  "art\characters\faces\briefs",
  "art\characters\faces\anatomy",
  "art\characters\faces\topology",
  "art\characters\faces\sculpt",
  "art\characters\faces\materials",
  "art\characters\faces\eyes",
  "art\characters\faces\mouth",
  "art\characters\faces\hair",
  "art\characters\faces\shapes",
  "art\characters\faces\lod",
  "art\textures\characters",
  "art\exports\characters",
  "tests\art\faces\reports",
  "tests\art\faces\captures"
)

foreach ($folder in $folders) {
  New-Item -ItemType Directory -Force -Path (Join-Path $root $folder) | Out-Null
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `-ItemType Directory` crée un dossier ; `-Force` rend la commande répétable sans erreur si le dossier existe.
- **Type :** `$folders` est un tableau de chaînes ; `$folder` reçoit une chaîne à chaque itération.
- **Opérateur :** `Join-Path` combine le chemin racine et le chemin relatif sans concaténation fragile.
- **Résultat attendu :** les dossiers existent ; aucune source artistique n'est créée par cette commande.

## 6. Contrat de la tête pilote

La tête pilote `AST-CHR-FACE-PILOT-001` doit représenter un cas de production suffisamment exigeant pour tester les gros plans, sans multiplier les variantes. Elle doit être compatible avec la base corporelle choisie, mais conserve un contrat séparé pour que sa topologie, ses matériaux et ses LOD puissent évoluer sans renommer le personnage complet.

Le brief ne doit pas demander « un visage réaliste ». Il doit préciser la distance de caméra, les éclairages, l'âge apparent, le niveau de stylisation, les expressions de test, les solutions capillaires attendues et les plateformes cibles.

> **[LECTURE] Brief fonctionnel de la tête pilote — Ne pas saisir.**

```yaml
asset_id: AST-CHR-FACE-PILOT-001
asset_role: closeup_reference_head
source_body_profile: AST-CHR-HUMAN-BASE-001
camera_requirements:
  hero_closeup_m: 0.7
  dialogue_m: 1.5
  gameplay_m: 4.0
lookdev:
  realism_target: grounded_stylized
  apparent_age_range: adult
  asymmetry: controlled
  weathering: moderate
required_tests:
  - neutral
  - blink
  - jaw_open
  - smile_compression
  - brow_raise
  - side_light
  - back_light
hair_scope:
  scalp_hair: required
  eyebrows: required
  eyelashes: required
  beard: optional
status: draft
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les distances sont des nombres décimaux en mètres ; les états et catégories sont des chaînes.
- **Caméras :** les trois distances empêchent d'optimiser uniquement pour un portrait fixe.
- **Expressions :** les tests sont des poses de déformation, pas des visèmes ou une performance finale.
- **Résultat attendu :** `status: draft` reste inchangé tant que les revues et preuves ne sont pas réalisées.

## 7. Références, consentement et provenance

Les références de visage peuvent contenir des données personnelles et biométriques sensibles. Une image accessible en ligne n'est pas automatiquement réutilisable, redistribuable ou adaptée à un dataset. Le registre doit distinguer :

- référence publique autorisée ;
- photographie interne avec consentement ;
- scan autorisé avec limites d'usage ;
- ressource commerciale avec licence ;
- génération synthétique avec modèle et conditions documentés ;
- référence interdite ou non qualifiée.

Le lecteur doit éviter de construire une tête à partir d'une seule photographie, car la perspective, la focale, l'expression et l'éclairage déforment la lecture. Une référence utile indique au minimum vue, focale approximative, expression, source, droits et question étudiée.

> **[LECTURE] Entrée de provenance faciale — Ne pas saisir.**

```yaml
reference_id: AST-REF-FACE-0042
source_type: licensed_photo_set
provider: pending
consent_or_license: pending_review
redistribution: forbidden_until_review
views:
  - front_neutral
  - profile_neutral
  - three_quarter_neutral
question:
  - eyelid_thickness
  - cheek_to_mouth_transition
bias_review:
  diversity_coverage: pending
  perspective_risk: reviewed
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Blocage :** une licence ou un consentement en attente impose `status: blocked`.
- **Portée :** `question` limite ce que la référence est censée résoudre.
- **Biais :** la diversité et la perspective sont examinées séparément.
- **Résultat attendu :** la référence n'entre pas dans le lot de publication avant qualification.

## 8. Repères anatomiques et volumes

Le visage est construit à partir de volumes, pas à partir de lignes dessinées sur une surface plane. Pour une tête humaine ou humanoïde, les repères artistiques courants comprennent :

- masse crânienne ;
- arcades sourcilières ;
- orbites ;
- pommettes ;
- maxillaire et mandibule ;
- volume nasal ;
- cylindre ou museau de la bouche selon la morphologie ;
- menton ;
- angle mandibulaire ;
- pavillon et implantation de l'oreille ;
- transitions front-tempe-joue ;
- transition lèvre-menton ;
- volumes graisseux et musculaires visibles.

Ces repères ne sont pas des mesures médicales. Ils servent à comparer les volumes dans plusieurs vues et à maintenir une logique de déformation.

> **[LECTURE] Fiche de repères — Ne pas saisir.**

```yaml
landmarks:
  skull_mass:
    review_views: [front, profile, top]
    status: pending
  orbit_rim:
    review_views: [front, profile, three_quarter]
    status: pending
  cheek_mass:
    review_views: [front, profile, three_quarter]
    status: pending
  jaw_hinge:
    review_views: [profile, bottom]
    status: pending
  mouth_cylinder:
    review_views: [profile, three_quarter]
    status: pending
  ear_root:
    review_views: [profile, back]
    status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** chaque repère possède des vues requises et un état indépendant.
- **Tableaux :** les valeurs entre crochets sont des listes de chaînes.
- **Validation :** un repère ne passe à `reviewed` qu'après comparaison des vues.
- **Résultat attendu :** la fiche révèle les zones non résolues avant la sculpture de détail.

## 9. Topologie faciale et zones de déformation

La topologie doit soutenir les déformations prévues. Une topologie propre n'est pas simplement une grille régulière : elle distribue les boucles et la densité selon les changements de forme.

Les zones prioritaires sont :

- contour des paupières ;
- commissures des lèvres ;
- sillon nasogénien ;
- aile du nez ;
- transition joue-bouche ;
- menton et lèvre inférieure ;
- articulation de la mâchoire ;
- sourcil et front ;
- oreille si elle se déforme ;
- implantation des cheveux et barbe si la géométrie doit se raccorder.

Les boucles ne doivent pas être copiées sans réflexion depuis un autre visage. Une mâchoire différente, une bouche stylisée ou un œil non humain peut exiger un flux propre.

> **[LECTURE] Contrat de topologie — Ne pas saisir.**

```yaml
topology_profile: AST-FACE-TOPO-001-v001
mesh_role: deforming_face
regions:
  eyelids:
    closed_loop: required
    radial_support: required
    density: high
  lips:
    closed_loop: required
    mouth_bag_connection: required
    density: high
  cheeks:
    flow: expression_driven
    density: medium
  forehead:
    flow: brow_driven
    density: medium
  ears:
    deformation: limited
    density: low_to_medium
symmetry_phase:
  construction: enabled
  review: broken_controlled
status: draft
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** l'identifiant versionné permet de savoir quelle topologie est utilisée.
- **Densité :** les valeurs `high`, `medium` et `low_to_medium` sont des catégories à remplacer par des mesures dans le rapport.
- **Symétrie :** la construction peut être symétrique, puis une phase contrôlée introduit l'asymétrie.
- **Résultat attendu :** aucune région critique n'est traitée comme une simple surface statique.

## 10. Sculpture primaire, secondaire et tertiaire

La sculpture suit trois niveaux :

1. **formes primaires** — crâne, mâchoire, orbites, museau de bouche, nez, oreilles ;
2. **formes secondaires** — paupières, lèvres, pommettes, plis structurels, volumes graisseux ;
3. **formes tertiaires** — pores, rides fines, cicatrices, duvet et bruit de surface.

Le détail tertiaire ne corrige jamais une erreur primaire. Une pommette mal placée reste fausse même couverte de pores. À chaque niveau, le modèle doit être relu en matériau mat, sous une lumière simple et dans plusieurs vues.

> **[LECTURE] Ordre de sculpture — Ne pas saisir.**

```yaml
sculpt_passes:
  - pass: primary
    tools: [move, grab, smooth]
    acceptance: silhouette_and_mass
  - pass: secondary
    tools: [clay, crease, smooth]
    acceptance: transitions_and_planes
  - pass: tertiary
    tools: [multires_detail, displacement, texture]
    acceptance: scale_consistency
rule: tertiary_never_repairs_primary
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** la liste est séquentielle ; chaque passe dépend de l'acceptation de la précédente.
- **Outils :** les noms décrivent des familles d'outils, pas un preset universel.
- **Règle :** `tertiary_never_repairs_primary` interdit de masquer une erreur de volume avec du bruit.
- **Résultat attendu :** le modèle reste lisible lorsque les textures et microdétails sont désactivés.

## 11. Symétrie et asymétrie contrôlée

La symétrie accélère la construction, facilite certaines corrections et simplifie la création de formes de test. Elle ne doit pas produire un visage parfaitement miroir.

L'asymétrie peut concerner :

- hauteur des sourcils ;
- ouverture des paupières ;
- volume des joues ;
- orientation du nez ;
- hauteur des commissures ;
- implantation capillaire ;
- rides et cicatrices ;
- densité de barbe ;
- pigmentation.

Chaque asymétrie doit avoir une échelle et une raison. Une asymétrie de forme primaire modifie la silhouette et les déformations ; une asymétrie de texture peut rester indépendante du maillage.

> **[LECTURE] Registre d'asymétrie — Ne pas saisir.**

```yaml
asymmetry_profile: AST-FACE-ASYM-001-v001
entries:
  - region: left_brow
    domain: secondary_form
    magnitude: subtle
    mirrored_shape_impact: reviewed
  - region: nose_bridge
    domain: primary_form
    magnitude: low
    mirrored_shape_impact: required
  - region: right_cheek
    domain: pigmentation
    magnitude: medium
    mirrored_shape_impact: none
status: draft
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaines :** `primary_form`, `secondary_form` et `pigmentation` n'ont pas les mêmes conséquences.
- **Impact :** une asymétrie de maillage exige une revue des formes miroirs.
- **Amplitude :** les catégories restent provisoires et doivent être accompagnées de captures.
- **Résultat attendu :** l'asymétrie est traçable et non ajoutée au hasard en fin de production.

## 12. Formes faciales de préparation

Le chapitre prépare des shape keys ou blendshapes de test pour vérifier que la topologie et les matériaux supportent les déformations. Il ne crée pas la bibliothèque de visèmes, les timings de parole ni l'acting final.

Un jeu minimal de préparation peut comprendre :

- `face_neutral` ;
- `blink_left` et `blink_right` ;
- `jaw_open` ;
- `mouth_close` ;
- `smile_compression` ;
- `brow_raise_left` et `brow_raise_right` ;
- `cheek_raise` ;
- `lip_pucker_test` ;
- `lip_stretch_test`.

Ces formes servent à révéler les pincements, pertes de volume, intersections, plis inversés et dérives de matériaux.

> **[LECTURE] Manifeste de formes de test — Ne pas saisir.**

```yaml
shape_profile: AST-FACE-SHAPES-TEST-001-v001
purpose: deformation_validation
shapes:
  - name: blink_left
    type: corrective_test
    range: [0.0, 1.0]
  - name: jaw_open
    type: primary_motion_test
    range: [0.0, 1.0]
  - name: smile_compression
    type: compression_test
    range: [0.0, 1.0]
  - name: lip_pucker_test
    type: volume_test
    range: [0.0, 1.0]
viseme_timing: excluded
dialogue_acting: excluded
status: draft
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plage :** `range` est une liste de deux nombres flottants représentant le minimum et le maximum testés.
- **Type :** la catégorie indique le défaut recherché : correction, mouvement, compression ou volume.
- **Exclusion :** les timings de visèmes et l'acting sont explicitement laissés au chapitre 27.
- **Résultat attendu :** les formes vérifient la topologie sans prétendre constituer un système facial final.

## 13. Matériau de peau : responsabilités

Le matériau de peau combine plusieurs phénomènes :

- couleur de base sans éclairage peint ;
- variation de roughness ;
- relief de moyenne et petite échelle ;
- diffusion sous-surface ;
- zones plus fines ou plus grasses ;
- détails spécifiques comme lèvres, paupières, cicatrices ou rougeurs ;
- réponse aux mipmaps et à la compression.

Aucune valeur unique ne convient à toutes les peaux, à tous les styles et à tous les éclairages. Le projet doit conserver des profils, des captures et des mesures.

> **[LECTURE] Profil de matériau de peau — Ne pas saisir.**

```yaml
material_profile: AST-MAT-SKIN-001-v001
shader_family: skin_specialized
texture_sets:
  base_color:
    color_space: sRGB
    status: pending
  roughness:
    color_space: linear_data
    status: pending
  normal:
    color_space: linear_data
    status: pending
  detail_normal:
    color_space: linear_data
    status: pending
  thickness_or_mask:
    color_space: linear_data
    status: pending
subsurface:
  enabled: planned
  radius_profile: pending_measurement
  mask_source: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Espaces colorimétriques :** la couleur est lue en sRGB ; les cartes de données restent linéaires.
- **Sous-surface :** `planned` documente l'intention sans annoncer une configuration validée.
- **Blocage :** les textures et mesures manquantes imposent `status: blocked`.
- **Résultat attendu :** les responsabilités des cartes sont visibles avant la création du matériau.

## 14. Couleur, roughness et relief

La couleur de base ne doit pas contenir des ombres fixes destinées à simuler l'éclairage. Les variations doivent représenter pigmentation, rougeurs, veines visibles, taches, lèvres et différences de zones.

La roughness contrôle la largeur et l'intensité visuelle des reflets. Une peau uniformément brillante paraît plastique ; une peau uniformément mate paraît poudreuse ou sèche. Le front, le nez, les lèvres, les paupières et les joues peuvent répondre différemment, mais ces différences doivent être observées sous plusieurs lumières.

Le relief doit respecter l'échelle. Les plis et cicatrices importantes appartiennent au maillage ou au displacement selon le plan de production. Les pores peuvent utiliser une normal de détail, mais leur taille apparente doit rester cohérente avec la distance et la résolution.

> **[LECTURE] Table de responsabilité des cartes — Ne pas saisir.**

```yaml
maps:
  base_color:
    stores:
      - pigmentation
      - color_variation
    must_not_store:
      - baked_directional_shadow
  roughness:
    stores:
      - micro_surface_response
    must_not_store:
      - color
  normal:
    stores:
      - medium_scale_relief
    must_not_store:
      - silhouette_change
  detail_normal:
    stores:
      - pores_and_micro_relief
    must_not_store:
      - wrinkles_requiring_deformation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** chaque carte possède un rôle et des interdictions.
- **Normal :** une normal map ne modifie pas la silhouette réelle.
- **Détail :** les plis qui doivent se déplacer avec une expression ne sont pas figés uniquement dans une texture.
- **Résultat attendu :** les erreurs de canal peuvent être diagnostiquées sans examiner le shader complet.

## 15. Diffusion sous-surface

La diffusion sous-surface simule le transport de lumière dans une matière partiellement translucide. Pour la peau, elle adoucit certaines transitions, mais ne remplace ni les volumes ni la roughness.

Une diffusion trop forte efface les détails et donne un aspect cireux. Une diffusion trop faible peut rendre la peau minérale. Le réglage dépend :

- de l'échelle réelle de l'asset ;
- du style ;
- de la couleur de la peau ;
- de l'épaisseur locale ;
- de l'éclairage ;
- du modèle de shader ;
- de la plateforme.

Le profil doit être testé sous lumière frontale, latérale, arrière et environnementale.

> **[LECTURE] Plan de test sous-surface — Ne pas saisir.**

```yaml
subsurface_test:
  asset_id: AST-CHR-FACE-PILOT-001
  scale_verified: false
  lighting_setups:
    - front_soft
    - side_hard
    - back_rim
    - neutral_environment
  comparisons:
    - subsurface_off
    - subsurface_low
    - subsurface_candidate
  evidence:
    captures: pending
    gpu_measurement: pending
    reviewer_decision: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Comparaison :** les variantes sont comparées dans les mêmes conditions.
- **Échelle :** la diffusion n'est pas validée tant que l'échelle n'est pas vérifiée.
- **Preuves :** captures, mesure GPU et décision humaine sont séparées.
- **Résultat attendu :** le profil candidat n'est accepté qu'après comparaison reproductible.

## 16. Construction de l’œil

Un œil de gros plan est plus qu'une sphère colorée. Le système peut comprendre :

- sclère ;
- iris ;
- pupille ;
- volume cornéen ;
- limbe ;
- film humide ;
- caroncule ;
- paupières avec épaisseur ;
- ligne de contact entre paupière et globe ;
- ombre et occlusion locales.

La cornée modifie la lecture de l'iris et des reflets. L'iris peut être une géométrie, une texture ou une combinaison. La pupille et l'iris doivent rester stables lors des rotations et des LOD.

> **[LECTURE] Contrat d'œil — Ne pas saisir.**

```yaml
eye_profile: AST-EYE-001-v001
components:
  sclera_mesh: required
  cornea_mesh: required
  iris_representation: pending_choice
  pupil_representation: pending_choice
  wetline: required_for_closeup
  caruncle: optional_by_style
geometry_checks:
  cornea_intersection: pending
  eyelid_contact: pending
  left_right_scale_match: pending
material_checks:
  sclera_roughness: pending
  cornea_refraction_or_approximation: pending
  iris_depth: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Composants :** chaque volume est explicite au lieu d'être caché dans un matériau monolithique.
- **Choix :** `pending_choice` interdit d'annoncer une solution non décidée.
- **Contrôles :** géométrie et matériau possèdent des preuves séparées.
- **Résultat attendu :** l'œil reste bloqué tant que contacts, échelle et réponse lumineuse ne sont pas vérifiés.

## 17. Paupières, clignement et film humide

Les paupières doivent envelopper le globe plutôt que glisser comme des plaques. Le clignement nécessite :

- une épaisseur de bord ;
- un trajet cohérent sur la cornée ;
- une compression contrôlée ;
- un contact supérieur-inférieur ;
- une gestion des cils ;
- une ligne humide qui ne traverse pas le globe ;
- une forme fermée qui évite un jour lumineux.

La forme `blink_left` teste la topologie et les matériaux. Elle ne définit pas la fréquence, le timing ou l'acting des clignements.

> **[LECTURE] Checklist du clignement — Ne pas saisir.**

```yaml
blink_test:
  shape: blink_left
  checks:
    upper_lid_wraps_globe: false
    lower_lid_supports_contact: false
    no_visible_gap: false
    no_cornea_penetration: false
    wetline_stable: false
    eyelashes_do_not_cross_eye: false
  timing_profile: excluded
  decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Booléens :** chaque contrôle commence à `false` avant exécution.
- **Géométrie :** les contacts et pénétrations sont vérifiés séparément.
- **Exclusion :** le profil temporel appartient au chapitre 27.
- **Résultat attendu :** `decision` reste `blocked` tant qu'un seul contrôle est faux.

## 18. Bouche, dents, gencives et langue

La bouche comprend un volume externe et une cavité interne. Les lèvres doivent conserver leur épaisseur pendant ouverture, fermeture, compression et étirement.

Les éléments internes doivent être préparés :

- sac buccal ou géométrie intérieure ;
- dents supérieures et inférieures ;
- gencives ;
- langue ;
- palais simplifié si visible ;
- transitions humides ;
- occlusion de la profondeur.

Les dents ne doivent pas flotter devant les gencives. La langue ne doit pas traverser les dents au repos. Les lèvres fermées ne doivent pas laisser apparaître un trou noir incohérent ou une ligne lumineuse.

> **[LECTURE] Contrat de bouche — Ne pas saisir.**

```yaml
mouth_profile: AST-MOUTH-001-v001
components:
  mouth_bag: required
  upper_teeth: required
  lower_teeth: required
  gums: required
  tongue: required
  palate: conditional
rest_pose_checks:
  lips_contact: pending
  teeth_inside_lips: pending
  tongue_inside_teeth: pending
  no_light_leak: pending
open_pose_checks:
  jaw_clearance: pending
  tongue_clearance: pending
  gum_visibility: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Condition :** `palate: conditional` signifie qu'il dépend des angles de caméra et du style.
- **Poses :** les contrôles au repos et bouche ouverte sont séparés.
- **Fuite lumineuse :** le sac buccal doit empêcher l'arrière-plan d'apparaître.
- **Résultat attendu :** les intersections visibles empêchent l'acceptation.

## 19. Choisir une solution de cheveux et de pilosité

Les cheveux peuvent être représentés par :

- volumes sculptés ;
- mèches géométriques ;
- hair cards avec transparence ;
- courbes de cheveux ;
- groom converti ou procédural ;
- textures ou masques pour le duvet ;
- mélange de plusieurs solutions.

Le choix dépend de la distance, du style, du mouvement, de la plateforme, du coût de transparence, de la facilité de LOD et du pipeline d'export. Une solution de cinématique n'est pas automatiquement viable pour le gameplay.

> **[LECTURE] Matrice de choix capillaire — Ne pas saisir.**

```yaml
hair_solution_matrix:
  sculpted_mass:
    closeup_quality: medium
    transparency_cost: low
    animation_complexity: low
    lod_stability: high
  hair_cards:
    closeup_quality: high
    transparency_cost: medium_to_high
    animation_complexity: medium
    lod_stability: medium
  curves_or_groom:
    closeup_quality: high
    transparency_cost: profile_dependent
    animation_complexity: high
    lod_stability: pending_pipeline
selection:
  scalp_hair: pending
  eyebrows: pending
  eyelashes: pending
  beard: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catégories :** les appréciations sont des hypothèses de comparaison, pas des mesures.
- **Coût :** la transparence dépend du nombre de couches, du remplissage écran et du renderer.
- **Pipeline :** les courbes ou grooms doivent être qualifiés pour l'export et le moteur.
- **Résultat attendu :** chaque zone peut utiliser une solution différente si les contrats restent compatibles.

## 20. Hair cards et transparence

Une hair card est une bande de géométrie portant une texture avec alpha. Sa qualité dépend :

- de l'orientation des cartes ;
- du tri de transparence ;
- du chevauchement ;
- de la densité ;
- des mipmaps ;
- du seuil alpha ;
- du mouvement ;
- de la lumière arrière ;
- de la distance.

Un grand nombre de cartes superposées augmente l'overdraw, c'est-à-dire le nombre de fois où le même pixel est recalculé. Le budget doit donc mesurer plus que le nombre de triangles.

> **[LECTURE] Profil hair cards — Ne pas saisir.**

```yaml
hair_card_profile: AST-HAIR-CARDS-001-v001
material:
  blend_mode: pending
  alpha_threshold: pending_measurement
  mipmap_policy: pending
geometry:
  card_count_budget: provisional
  layer_depth_budget: provisional
  scalp_coverage: pending_review
tests:
  front_light: pending
  back_light: pending
  side_light: pending
  distance_transition: pending
  overdraw_capture: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Blend mode :** le mode de transparence doit être choisi après test des artefacts et du coût.
- **Budgets :** les nombres ne sont pas inventés ; ils restent `provisional`.
- **Éclairages :** la lumière arrière révèle les halos et les découpes.
- **Résultat attendu :** la solution n'est pas acceptée sans capture d'overdraw et test de distance.

## 21. Courbes de cheveux, groom et conversion

Les courbes de cheveux ou systèmes de groom facilitent la création de mèches et la direction artistique. Leur présence dans Blender ne garantit pas une exportation exploitable.

Le pipeline doit décider :

- la source canonique ;
- le mode de conversion ;
- la représentation exportée ;
- la conservation ou non des guides ;
- la stratégie de LOD ;
- la compatibilité avec les animations ;
- le comportement de réimport ;
- les droits des textures et outils utilisés.

Aucun résultat de conversion n'est revendiqué dans ce chapitre.

> **[LECTURE] Contrat de conversion capillaire — Ne pas saisir.**

```yaml
groom_conversion_profile: AST-GROOM-CONVERT-001-v001
canonical_source: blender_curves
export_representation: pending_choice
conversion_steps:
  - duplicate_source
  - apply_named_profile
  - generate_export_representation
  - validate_uv_and_normals
  - export_glb
  - compare_reimport
preserve:
  original_guides: true
  procedural_settings: true
proof:
  conversion_log: pending
  visual_comparison: pending
  performance_measurement: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source canonique :** les courbes originales sont conservées, même si l'export utilise une autre représentation.
- **Étapes :** la conversion est reproductible et n'écrase pas la source.
- **Preuves :** log, comparaison visuelle et mesure sont indépendants.
- **Résultat attendu :** aucune conversion n'est déclarée stable avant réimport et mesure.

## 22. Sourcils, cils, barbe et duvet

Les différentes pilosités n'ont pas les mêmes contraintes :

- les sourcils participent fortement à l'expression ;
- les cils doivent suivre les paupières et éviter le globe ;
- la barbe modifie la silhouette locale et peut traverser les lèvres ou les vêtements ;
- le duvet influence surtout la réponse à contre-jour ;
- une fourrure faciale humanoïde peut nécessiter plusieurs densités et directions.

Chaque zone doit avoir un parent, une solution, un niveau de détail et un test de déformation.

> **[LECTURE] Profil de pilosité — Ne pas saisir.**

```yaml
facial_hair_profile: AST-FACIAL-HAIR-001-v001
zones:
  eyebrows:
    representation: pending
    deformation_parent: brow_region
    expression_test: required
  eyelashes:
    representation: pending
    deformation_parent: eyelids
    blink_test: required
  beard:
    representation: optional
    deformation_parent: jaw_and_cheeks
    mouth_test: required
  peach_fuzz:
    representation: shader_or_cards
    deformation_parent: skin
    backlight_test: required
status: draft
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Parent :** la pilosité doit suivre la région qui se déforme.
- **Tests :** chaque zone possède une pose ou un éclairage révélateur.
- **Option :** la barbe peut être absente sans invalider la tête pilote.
- **Résultat attendu :** aucune zone n'est ajoutée comme simple décoration sans contrat.

## 23. LOD de la tête, des yeux et des cheveux

Le LOD facial doit préserver les traits utiles à la distance :

- silhouette de la tête ;
- ouverture des yeux ;
- direction du regard si encore visible ;
- contour de la bouche ;
- masse capillaire ;
- contraste des sourcils ;
- signal de clignement ou de parole selon le profil.

Les microdétails peuvent disparaître avant les formes principales. Les cheveux peuvent changer de représentation. Les matériaux peuvent simplifier la diffusion sous-surface, la transparence ou le nombre de textures, mais les transitions doivent être testées.

> **[LECTURE] Profil LOD facial — Ne pas saisir.**

```yaml
facial_lod_profile: AST-FACE-LOD-001-v001
lod0:
  purpose: hero_closeup
  geometry_budget: provisional
  skin_profile: full_candidate
  hair_representation: pending
  test_distance_m: 0.7
lod1:
  purpose: dialogue
  geometry_budget: provisional
  skin_profile: reduced_candidate
  hair_representation: pending
  test_distance_m: 1.5
lod2:
  purpose: gameplay
  geometry_budget: provisional
  skin_profile: simplified_candidate
  hair_representation: pending
  test_distance_m: 4.0
protected_traits:
  - eye_opening
  - mouth_contour
  - brow_direction
  - hair_mass
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distances :** les valeurs proviennent du brief et doivent être testées avec les caméras réelles.
- **Budgets :** les budgets restent provisoires jusqu'aux mesures.
- **Traits protégés :** la simplification ne peut pas supprimer les signaux nécessaires.
- **Résultat attendu :** chaque transition est jugée visuellement et techniquement.

## 24. Export GLB et scène Godot dérivée

Le fichier Blender reste la source canonique. Le GLB est un export. La scène Godot dérivée ajoute les éclairages, caméras, scripts de validation et comparaisons de LOD sans modifier le fichier importé.

L'export doit conserver :

- échelle et axes ;
- maillage et normales ;
- UV ;
- matériaux ou emplacements de remappage ;
- armature nécessaire ;
- shape keys ou animations prises en charge selon le profil ;
- noms stables ;
- hiérarchie ;
- variantes de LOD selon la stratégie choisie.

Les solutions capillaires doivent être vérifiées séparément, car toutes les représentations Blender ne sont pas automatiquement transférées.

> **[LECTURE] Manifeste d'export — Ne pas saisir.**

```yaml
export_manifest: AST-EXPORT-FACE-001-v001
source_blend: art/blender/characters/AST-CHR-FACE-PILOT-001/face_pilot.blend
output_glb: art/exports/characters/AST-CHR-FACE-PILOT-001.glb
include:
  meshes: true
  armature: conditional
  test_shapes: conditional
  materials: true
  hair_representation: pending
exclude:
  sculpt_only_objects: true
  reference_images: true
  internal_guides: true
reimport_comparison: required
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Booléens :** `true` ou `false` rendent les inclusions explicites.
- **Condition :** armature et formes sont incluses seulement si le profil de test l'exige.
- **Exclusion :** les objets de sculpture et références ne sortent pas dans le GLB.
- **Résultat attendu :** l'export reste bloqué tant que la représentation des cheveux et le réimport ne sont pas qualifiés.

> **[LECTURE] Hiérarchie de la scène de validation — Ne pas saisir.**

```text
FaceValidationLab
├── WorldEnvironment
├── LightingRig
│   ├── KeyLight
│   ├── FillLight
│   ├── RimLight
│   └── NeutralEnvironment
├── CameraRig
│   ├── HeroCloseupCamera
│   ├── DialogueCamera
│   └── GameplayCamera
├── Turntable
│   └── FaceAssetInstance
├── ComparisonBackground
├── DebugOverlay
└── FaceAssetValidator
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Éclairage :** les lumières sont nommées afin de reproduire les comparaisons.
- **Caméras :** les trois distances du brief deviennent des points de vue explicites.
- **Instance :** la scène importée est instanciée sous un pivot de rotation.
- **Résultat attendu :** la validation reste séparée de la scène de gameplay.

## 25. Validateur GDScript structurel

Le validateur ne juge pas la beauté du visage. Il vérifie la présence de nœuds, ressources, matériaux et métadonnées attendus. Il doit être non destructif : il lit la scène et produit un rapport sans renommer, déplacer ou supprimer les ressources.

Le script ci-dessous est un exemple documentaire. Il n'a pas été exécuté.

> **[LECTURE] Validateur structurel de tête — Ne pas saisir.**

```gdscript
@tool
extends Node

@export var asset_root_path: NodePath
@export var required_mesh_names: PackedStringArray = [
    "FaceMesh",
    "LeftEye",
    "RightEye"
]
@export var required_material_slots: PackedStringArray = [
    "Skin",
    "EyeCornea",
    "EyeIris",
    "Mouth"
]
@export var report_path: String = "res://tests/art/faces/reports/face_asset_report.json"

func validate_asset() -> Dictionary:
    var report: Dictionary = {
        "errors": [],
        "warnings": [],
        "meshes": {},
        "materials": {},
        "status": "blocked"
    }

    var asset_root: Node = get_node_or_null(asset_root_path)
    if asset_root == null:
        report["errors"].append("asset_root_missing")
        return _finalize_report(report)

    for mesh_name: String in required_mesh_names:
        var mesh_node: Node = asset_root.find_child(mesh_name, true, false)
        report["meshes"][mesh_name] = mesh_node != null
        if mesh_node == null:
            report["errors"].append("missing_mesh:%s" % mesh_name)

    var found_materials: Dictionary = _collect_material_names(asset_root)
    for material_name: String in required_material_slots:
        var present: bool = found_materials.has(material_name)
        report["materials"][material_name] = present
        if not present:
            report["errors"].append("missing_material:%s" % material_name)

    return _finalize_report(report)

func _collect_material_names(root: Node) -> Dictionary:
    var result: Dictionary = {}
    var stack: Array[Node] = [root]

    while not stack.is_empty():
        var current: Node = stack.pop_back()
        if current is MeshInstance3D:
            var mesh_instance: MeshInstance3D = current as MeshInstance3D
            var surface_count: int = mesh_instance.get_surface_override_material_count()
            for surface_index: int in range(surface_count):
                var material: Material = mesh_instance.get_surface_override_material(surface_index)
                if material != null and not material.resource_name.is_empty():
                    result[material.resource_name] = true

        for child: Node in current.get_children():
            stack.append(child)

    return result

func _finalize_report(report: Dictionary) -> Dictionary:
    var errors: Array = report["errors"]
    report["status"] = "accepted" if errors.is_empty() else "blocked"
    return report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Retour principal :** `validate_asset() -> Dictionary` renvoie un dictionnaire contenant erreurs, avertissements, résultats et statut.
- **Paramètres exportés :** `NodePath`, `PackedStringArray` et `String` sont configurables dans l'inspecteur.
- **Recherche :** `get_node_or_null()` évite une exception si la racine manque ; `find_child()` cherche un nœud par nom.
- **Opérateurs :** `==`, `!=`, `not`, `and` et l'expression conditionnelle choisissent les branches et le statut.
- **Boucles :** `for` parcourt les noms et surfaces ; `while` explore la hiérarchie avec une pile.
- **Résultat attendu :** le script retourne `blocked` dès qu'une exigence structurelle manque ; il ne juge ni la couleur ni la qualité artistique.

## 26. Lecture détaillée des fonctions, paramètres et types

### 26.1 `validate_asset() -> Dictionary`

La fonction ne reçoit aucun paramètre explicite. Elle lit les propriétés exportées du nœud. Son type de retour `Dictionary` garantit que l'appelant reçoit une structure clé-valeur.

Les clés principales sont :

- `errors` : tableau d'erreurs bloquantes ;
- `warnings` : tableau d'avertissements ;
- `meshes` : dictionnaire nom-booléen ;
- `materials` : dictionnaire nom-booléen ;
- `status` : chaîne `accepted` ou `blocked`.

Le retour anticipé après l'absence de racine évite de poursuivre avec un nœud nul.

### 26.2 `_collect_material_names(root: Node) -> Dictionary`

Le paramètre `root` est typé `Node`. La fonction crée une pile `Array[Node]`, retire le dernier élément avec `pop_back()`, examine les `MeshInstance3D`, puis ajoute les enfants.

`current is MeshInstance3D` teste le type. `current as MeshInstance3D` produit une référence spécialisée. `range(surface_count)` génère les indices de surface de `0` à `surface_count - 1`.

### 26.3 `_finalize_report(report: Dictionary) -> Dictionary`

Le paramètre et le retour sont des dictionnaires. L'expression :

`"accepted" if errors.is_empty() else "blocked"`

choisit une chaîne selon le résultat booléen de `errors.is_empty()`. La fonction ne modifie aucune ressource artistique ; elle enrichit uniquement le rapport en mémoire.

> **[LECTURE] Exemple de rapport attendu — Ne pas saisir.**

```json
{
  "errors": [
    "missing_material:EyeCornea"
  ],
  "warnings": [],
  "meshes": {
    "FaceMesh": true,
    "LeftEye": true,
    "RightEye": true
  },
  "materials": {
    "Skin": true,
    "EyeCornea": false,
    "EyeIris": true,
    "Mouth": true
  },
  "status": "blocked"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Booléens :** `true` et `false` indiquent la présence structurelle.
- **Erreur :** le préfixe `missing_material:` permet de filtrer les erreurs.
- **Statut :** une seule erreur suffit à produire `blocked`.
- **Limite :** un matériau présent peut encore être visuellement incorrect ; le rapport ne le valide pas artistiquement.

## 27. Éclairage de référence

Un visage doit être testé sous plusieurs éclairages :

- lumière douce frontale pour les transitions ;
- lumière latérale dure pour les plans et défauts de normal ;
- contre-jour pour le duvet et les cheveux ;
- environnement neutre pour le comportement général ;
- fond clair et fond sombre pour la transparence ;
- exposition contrôlée pour les yeux et les dents.

Les captures doivent conserver caméra, focale, exposition, environnement, résolution, profil de qualité et commit de l'asset.

> **[LECTURE] Manifeste de capture — Ne pas saisir.**

```yaml
capture_manifest: AST-FACE-CAPTURE-001-v001
asset_id: AST-CHR-FACE-PILOT-001
camera:
  profile: hero_closeup
  distance_m: 0.7
  focal_length_mm: pending
lighting:
  setup: side_hard
  environment_profile: neutral_reference
render:
  resolution: pending
  quality_profile: reference
evidence:
  asset_commit: pending
  scene_commit: pending
  screenshot_path: pending
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Reproductibilité :** caméra, lumière et profil de rendu sont enregistrés.
- **Focale :** la valeur reste en attente tant que la caméra n'est pas matérialisée.
- **Preuves :** les commits de l'asset et de la scène empêchent les captures orphelines.
- **Résultat attendu :** une capture sans contexte ne peut pas soutenir une décision.

## 28. Protocole de performance

Le coût doit être mesuré dans les scénarios réellement visés. Les éléments à suivre comprennent :

- triangles et sommets par LOD ;
- nombre de surfaces et matériaux ;
- résolutions et mémoire des textures ;
- coût du shader de peau ;
- coût des yeux ;
- overdraw des cheveux ;
- coût des ombres ;
- nombre de personnages visibles ;
- temps CPU et GPU ;
- mémoire vidéo ;
- stabilité des transitions LOD.

Le nombre de triangles seul ne suffit pas. Un visage peu polygonal avec plusieurs matériaux transparents et textures lourdes peut coûter davantage qu'un maillage plus dense mais opaque.

> **[LECTURE] Plan de benchmark facial — Ne pas saisir.**

```yaml
benchmark_profile: AST-FACE-BENCH-001-v001
hardware_profile: project_reference_machine
scenarios:
  - id: hero_closeup_single
    faces_visible: 1
    camera_profile: hero_closeup
  - id: dialogue_pair
    faces_visible: 2
    camera_profile: dialogue
  - id: gameplay_group
    faces_visible: pending
    camera_profile: gameplay
metrics:
  cpu_ms: pending
  gpu_ms: pending
  vram_mb: pending
  draw_calls: pending
  transparent_overdraw: pending
  frame_time_variance: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénarios :** le gros plan, le dialogue et le groupe sont mesurés séparément.
- **Mesures :** toutes les valeurs restent `pending` avant exécution.
- **Variance :** le temps moyen ne suffit pas ; les variations révèlent les instabilités.
- **Résultat attendu :** la décision reste bloquée jusqu'à la campagne réelle.

## 29. Parcours Mode Solo

Le parcours Solo privilégie un ensemble réduit :

1. une seule tête pilote ;
2. une seule famille de matériau de peau ;
3. un système d'œil réutilisable ;
4. une solution principale de cheveux ;
5. un jeu minimal de formes de test ;
6. trois LOD ;
7. une scène d'éclairage ;
8. un validateur structurel ;
9. un benchmark sur la machine de référence.

Le créateur Solo évite de produire immédiatement plusieurs âges, coiffures, barbes et styles. Il stabilise d'abord la chaîne complète.

> **[LECTURE] Checklist Solo — Ne pas saisir.**

```yaml
solo_path:
  pilot_head_count: 1
  skin_profiles: 1
  eye_profiles: 1
  primary_hair_solutions: 1
  test_shapes: minimal
  lod_profiles: 3
  validation_scenes: 1
  runtime_measurements: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limitation volontaire :** les nombres réduisent le risque de multiplier des variantes non validées.
- **Minimal :** `test_shapes: minimal` renvoie au manifeste défini plus haut.
- **Mesures :** la décision ne passe pas tant que les mesures sont en attente.
- **Résultat attendu :** une chaîne complète vaut mieux que plusieurs visages partiellement intégrés.

## 30. Parcours Mode Studio

Le parcours Studio sépare les responsabilités :

- direction artistique ;
- sculpture ;
- topologie ;
- texture et lookdev ;
- cheveux et groom ;
- rig facial ;
- intégration Godot ;
- performance ;
- provenance et droits ;
- validation finale.

Les profils de peau, d'œil, de cheveux et de formes faciales sont versionnés. Une modification de topologie doit prévenir le rig et les formes. Une modification de shader doit être vérifiée sur les plateformes. Une modification de coiffure doit requalifier transparence, ombres et LOD.

> **[LECTURE] Matrice de responsabilité Studio — Ne pas saisir.**

```yaml
studio_ownership:
  face_brief: art_direction
  sculpt: character_modeling
  topology: character_modeling
  skin_and_eye_lookdev: lookdev
  hair_and_groom: grooming
  test_shapes: facial_modeling
  final_facial_rig: chapter_19_owner
  lip_sync_and_timing: chapter_27_owner
  godot_integration: technical_art
  performance: performance_owner
  rights: production_legal
cross_reviews:
  - sculpt_topology
  - topology_shapes
  - lookdev_lighting
  - hair_transparency_performance
  - integration_reimport
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaires :** chaque livrable possède une spécialité responsable.
- **Frontières :** le rig final et la synchronisation labiale renvoient explicitement aux futurs chapitres.
- **Revues :** les interfaces entre spécialités sont contrôlées.
- **Résultat attendu :** aucune modification critique n'est acceptée uniquement par son auteur.

## 31. Porte d’acceptation

La porte d'acceptation agrège les preuves artistiques, techniques, juridiques et de performance. Toutes les valeurs commencent à `false` ou `pending`.

> **[LECTURE] Checklist d'acceptation du visage pilote — Ne pas saisir.**

```yaml
identity_and_rights:
  stable_asset_id: false
  references_qualified: false
  consent_or_licenses_reviewed: false
anatomy_and_topology:
  landmarks_reviewed: false
  primary_forms_reviewed: false
  topology_deformation_tests_passed: false
  asymmetry_profile_reviewed: false
materials:
  skin_profile_reviewed: false
  eye_profile_reviewed: false
  mouth_profile_reviewed: false
  multi_light_review_passed: false
hair_and_fur:
  solution_profile_reviewed: false
  transparency_tests_passed: false
  deformation_tests_passed: false
facial_shapes:
  test_shape_manifest_complete: false
  blink_test_passed: false
  jaw_and_smile_tests_passed: false
lod_and_godot:
  lod_profiles_measured: false
  glb_exported: false
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

- **Indépendance :** chaque domaine peut bloquer la décision.
- **État initial :** les booléens restent faux avant preuve.
- **Godot :** un résultat Blender ne suffit pas à accepter l'asset.
- **Résultat attendu :** `decision: blocked` est obligatoire pour ce template non exécuté.

## 32. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 32.1 Ajouter les pores avant de corriger les volumes

**Symptôme :** la peau paraît détaillée en gros plan, mais le visage reste plat ou déséquilibré en silhouette.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
sculpt_state:
  primary_forms: unresolved
  secondary_forms: unresolved
  pores: complete
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les pores ne corrigent ni le crâne, ni la mâchoire, ni les orbites. Le statut accepté masque donc une erreur de niveau primaire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
sculpt_state:
  primary_forms: reviewed
  secondary_forms: reviewed
  pores: pending
  status: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction impose l'ordre primaire, secondaire puis tertiaire et garde le détail en attente.

### 32.2 Peindre des ombres directionnelles dans la couleur

**Symptôme :** le visage semble correct sous une lumière, puis double les ombres lorsque la lumière change.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
base_color:
  contains:
    - pigmentation
    - left_key_light_shadow
    - nose_cast_shadow
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La couleur de base contient un éclairage fixe qui se superpose aux lumières de Godot.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
base_color:
  contains:
    - pigmentation
    - color_variation
  excludes:
    - directional_lighting
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction réserve la couleur aux propriétés de surface et laisse l'éclairage au moteur.

### 32.3 Utiliser une sphère unique pour tout l’œil

**Symptôme :** l'iris paraît collé, les reflets traversent mal la cornée et le clignement pénètre le globe.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
eye:
  meshes:
    - painted_sphere
  cornea: absent
  wetline: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une sphère peinte ne sépare ni cornée, ni iris, ni film humide et limite les contrôles de contact.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
eye:
  meshes:
    - sclera
    - cornea
    - iris_or_iris_representation
  wetline: required_for_closeup
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare les fonctions optiques et rend la ligne humide vérifiable.

### 32.4 Fermer les paupières par translation verticale

**Symptôme :** le bord de paupière traverse l'œil ou s'en éloigne pendant le clignement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blink:
  upper_lid_motion: translate_down
  globe_wrap: false
  collision_review: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une translation plane ne suit pas la courbure du globe et ne garantit pas le contact.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blink:
  upper_lid_motion: shaped_wrap
  globe_wrap: required
  collision_review: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction traite le clignement comme une déformation enveloppante et maintient la revue en attente.

### 32.5 Donner la même roughness à toute la peau

**Symptôme :** le visage paraît uniformément plastique ou uniformément poudreux.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
skin_material:
  roughness_value: 0.35
  regional_variation: false
  lighting_tests: one_setup
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une valeur uniforme efface les différences de lèvres, paupières, front, nez et joues.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
skin_material:
  roughness_map: required
  regional_variation: reviewed
  lighting_tests:
    - front_soft
    - side_hard
    - back_rim
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction introduit une carte de données et plusieurs éclairages de contrôle.

### 32.6 Empiler des hair cards sans mesurer l’overdraw

**Symptôme :** la coiffure respecte le nombre de triangles mais le coût GPU explose en gros plan.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
hair_cards:
  triangles: within_budget
  layer_depth: unlimited
  overdraw_capture: absent
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le nombre de triangles ignore les couches transparentes recalculées sur les mêmes pixels.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
hair_cards:
  triangles: provisional
  layer_depth: measured
  overdraw_capture: required
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction exige une mesure de profondeur et d'overdraw avant décision.

### 32.7 Attacher les cils à la tête au lieu des paupières

**Symptôme :** les cils flottent lorsque l'œil se ferme.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
eyelashes:
  parent: head
  blink_test: not_required
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le parent ne suit pas la déformation locale des paupières et le test révélateur est absent.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
eyelashes:
  parent: eyelids
  blink_test: required
  status: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction relie les cils à la région déformée et impose le test de clignement.

### 32.8 Créer les visèmes complets dans ce chapitre

**Symptôme :** le lot de lookdev contient des timings de dialogue et des formes linguistiques non validées.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
facial_shapes:
  visemes: complete
  language_profile: french
  dialogue_timing: embedded
  owner: chapter_10
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le chapitre 10 doit seulement préparer la topologie et des formes de test ; les visèmes et timings appartiennent au chapitre 27.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
facial_shapes:
  deformation_tests: complete
  viseme_set: deferred_to_chapter_27
  dialogue_timing: excluded
  owner: chapter_10
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve les tests de déformation et déplace clairement la synchronisation labiale.

### 32.9 Supprimer les yeux et sourcils trop tôt dans les LOD

**Symptôme :** le visage reste visible à distance mais le regard et l'expression deviennent illisibles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
lod2:
  eye_opening: merged
  brow_direction: removed
  triangle_budget: passed
  readability_test: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le budget géométrique ne prouve pas que les signaux faciaux sont conservés.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
lod2:
  eye_opening: preserved
  brow_direction: preserved
  triangle_budget: provisional
  readability_test: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction protège les traits requis et maintient le test en attente.

### 32.10 Déclarer le visage terminé après la revue Blender

**Symptôme :** le shader et les cheveux semblent corrects dans Blender mais n'ont jamais été importés ni mesurés dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
transparency_test: not_executed
performance_test: not_executed
status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une revue Blender ne prouve ni le contrat GLB, ni la transparence, ni les LOD, ni le coût moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
blender_review: passed
glb_export: not_executed
godot_import: not_executed
transparency_test: not_executed
performance_test: not_executed
status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve le blocage jusqu'aux preuves dans Godot.

## 33. Livrables à conserver

Le plan maître exige cinq livrables permanents :

1. **tête de référence** — source, topologie, sculpture, asymétrie et vues de contrôle ;
2. **matériaux peau et yeux** — profils, textures, paramètres, éclairages et captures ;
3. **bibliothèque de cheveux et pilosité** — sources, conversions, matériaux, LOD et preuves ;
4. **blendshapes ou système facial de préparation** — manifeste, formes de test et résultats de déformation ;
5. **profils LOD** — géométrie, matériaux, cheveux, distances et décisions.

L'arborescence de travail du début du chapitre devient l'inventaire permanent. Les exports restent distincts des sources et les rapports QA internes ne sont pas ajoutés au manuel lecteur.

> **[LECTURE] Inventaire de livraison — Ne pas saisir.**

```yaml
deliverable_manifest: AST-FACE-DELIVERY-001-v001
reference_head:
  source: pending
  topology_profile: AST-FACE-TOPO-001-v001
  status: blocked
materials:
  skin_profile: AST-MAT-SKIN-001-v001
  eye_profile: AST-EYE-001-v001
  status: blocked
hair_library:
  card_profile: AST-HAIR-CARDS-001-v001
  groom_profile: AST-GROOM-CONVERT-001-v001
  status: blocked
facial_shapes:
  profile: AST-FACE-SHAPES-TEST-001-v001
  status: blocked
lod:
  profile: AST-FACE-LOD-001-v001
  status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifestes :** chaque livrable renvoie vers un profil versionné.
- **État :** tous les livrables restent bloqués tant qu'ils ne sont pas matérialisés.
- **Traçabilité :** les sources, profils et preuves peuvent évoluer sans changer l'identifiant du lot.
- **Résultat attendu :** le manifeste devient l'entrée de la revue de production.

## 34. Synthèse opérationnelle pour Project Asteria

Le chapitre 10 fournit à `Project Asteria` une méthode complète de lookdev facial. La tête pilote est encadrée par un brief de caméra, des références qualifiées, des repères anatomiques, une topologie de déformation, une sculpture par niveaux, un registre d'asymétrie, des formes de test, des profils de peau, d'œil, de bouche, de cheveux, de pilosité, de LOD, d'export, de capture et de benchmark.

L'asset reste bloqué tant que la tête, les textures, les matériaux, les yeux, la bouche, les cheveux, les formes, les LOD, le GLB, la scène Godot, le validateur et les mesures ne sont pas réellement produits. Le chapitre prépare le rig facial du chapitre 19 et la synchronisation labiale du chapitre 27 sans définir leurs contrôleurs, leurs visèmes, leurs timings ni leur acting.

## 35. Références techniques officielles

Les références suivantes doivent être consultées et qualifiées lors de la matérialisation :

- [Blender Manual — Shape Keys](https://docs.blender.org/manual/en/latest/animation/shape_keys/index.html) ;
- [Blender Manual — Multiresolution Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/multiresolution.html) ;
- [Blender Manual — Subdivision Surface Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/subdivision_surface.html) ;
- [Blender Manual — Sculpting](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/index.html) ;
- [Blender Manual — Hair Curves](https://docs.blender.org/manual/en/latest/modeling/curves/hair/index.html) ;
- [Blender Manual — Principled Hair BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/hair_principled.html) ;
- [Blender Manual — Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) ;
- [Godot 4.7 — StandardMaterial3D](https://docs.godotengine.org/en/4.7/classes/class_standardmaterial3d.html) ;
- [Godot 4.7 — ShaderMaterial](https://docs.godotengine.org/en/4.7/classes/class_shadermaterial.html) ;
- [Godot 4.7 — BaseMaterial3D](https://docs.godotengine.org/en/4.7/classes/class_basematerial3d.html) ;
- [Godot 4.7 — MeshInstance3D](https://docs.godotengine.org/en/4.7/classes/class_meshinstance3d.html) ;
- [Godot 4.7 — Importing 3D scenes](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html) ;
- [Godot — Mesh level of detail](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html) ;
- [Godot — Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html).

Les pages `latest` ou `stable` ne sont utilisées que lorsqu'une page versionnée équivalente n'est pas exposée. Toute différence observée avec Blender `5.2.0` ou Godot `4.7.1-stable` doit être consignée avant d'appliquer la procédure.
