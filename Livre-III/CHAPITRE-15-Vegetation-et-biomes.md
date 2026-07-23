---
title: "Livre III — Chapitre 15 : Végétation et biomes"
id: "DOC-L3-CH15"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 15
last-verified: "2026-07-23T17:45:00+02:00"
audit-status: "complete"
audit-date: "2026-07-23T17:45:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-15.md"
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

# Végétation et biomes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH15`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre


Le chapitre 14 a défini le terrain, les cellules, les tuiles, le streaming et les interfaces de navigation. Le présent chapitre peuple cette infrastructure avec une végétation lisible, réutilisable et mesurable, sans transformer les assets artistiques en système écologique autoritaire.

Le fil rouge utilise le biome pilote `AST-VEG-BIOME-DELTA-001`, installé dans la région `AST-WORLD-REGION-DELTA-001`. Il combine une ripisylve humide, une prairie ouverte, une lisière rocheuse et des zones perturbées autour des routes et bâtiments. Ce biome n’est pas une simulation botanique complète : il sert à éprouver les contrats d’espèces, de variantes, de distribution, de vent, d’instancing, de distance et de densité avant toute extension.

Une bibliothèque végétale n’est pas une collection de beaux arbres isolés. Elle associe profils d’espèces, silhouettes, niveaux de détail, matériaux, cartes de distribution, règles d’exclusion, groupes d’instancing, collisions ciblées, réponses au vent, variantes de saison et scènes de benchmark. La preuve principale est une scène dense et traversable dans Godot, pas une capture avantageuse dans Blender.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Brief de biome et fonctions visuelles
    ↓
Catalogue d'espèces et provenance
    ↓
Silhouettes, échelles et familles de variantes
    ↓
Sources Blender, pivots et hiérarchie de vent
    ↓
Feuillage, opacité, matériaux et atlas préparatoires
    ↓
LOD, imposteurs et représentations lointaines
    ↓
Cartes de distribution, exclusions et graines
    ↓
Lots MultiMesh par cellule, espèce et niveau
    ↓
Collisions, navigation et interaction locale
    ↓
Benchmark de densité, overdraw, mémoire et distance
    ↓
Porte d'acceptation du biome pilote
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** le biome reçoit le terrain, les cellules et les raccords du chapitre 14.

- **Ordre :** les fonctions écologiques et visuelles sont définies avant la multiplication des variantes.

- **Preuve :** la densité, les transitions et le coût doivent être mesurés dans une scène Godot réelle.

- **Frontière :** les populations dynamiques, la régénération et les saisons autoritaires appartiennent au Livre II.

## 2. Résultats d’apprentissage


À la fin du chapitre, le lecteur saura :

- transformer un besoin de paysage en biome pilote mesurable ;
- distinguer espèce, morphotype, variante, saison, état de santé et instance ;
- définir un catalogue végétal compact avant de produire des centaines d’assets ;
- analyser silhouette, port, échelle, densité du feuillage et fonction de lecture ;
- construire arbres, arbustes, herbes, fleurs, couvre-sols et débris ;
- préparer pivots, axes, origines et zones d’ancrage cohérentes ;
- séparer tronc, branches, feuilles, cartes, collisions et données de vent ;
- choisir entre géométrie, cartes alpha, imposteurs et représentation agrégée ;
- créer des profils LOD sans inventer de distances ;
- organiser des variantes de taille, saison et santé sans duplication anarchique ;
- encoder humidité, pente, altitude, exposition et exclusions dans des cartes de distribution ;
- produire un placement déterministe et reproductible ;
- regrouper les instances dans des `MultiMeshInstance3D` adaptés au culling ;
- comprendre que le `MultiMesh` est cullé comme un ensemble et non instance par instance ;
- limiter collisions et interactions aux végétaux qui en ont besoin ;
- préparer un vent hiérarchisé sans synchroniser rigidement toutes les plantes ;
- mesurer overdraw, ombres, mémoire, temps CPU/GPU et distance d’affichage ;
- conserver toutes les réserves lorsque Blender, Godot ou le runtime n’ont pas été exécutés.

## 3. Niveau de preuve et réserves


Le chapitre est accepté au niveau `static-review`. Les contrats YAML, procédures Blender, hiérarchies Godot, exemples de shader, profils `MultiMesh`, règles de distribution et scripts GDScript ont été relus contre les documentations officielles. Ils ne constituent pas une preuve d’exécution.

Aucune espèce, aucun arbre, aucun arbuste, aucune herbe, aucune fleur, aucun atlas, aucun shader de vent, aucune carte de distribution, aucun `MultiMesh`, aucun imposteur, aucune collision, aucune scène de biome et aucune mesure de performance de `Project Asteria` ne sont revendiqués comme produits. Les tailles, densités, distances, résolutions, budgets, amplitudes et fréquences présentés comme exemples restent des candidats à mesurer.

Le chapitre s’appuie sur le nœud Blender `Instance on Points` comme outil de prévisualisation et d’assemblage, sans supposer que les instances Blender deviennent automatiquement le système runtime Godot. Dans Godot, `MultiMesh` sert aux grands groupes d’instances identiques, mais son groupe est cullé comme une seule primitive ; le découpage spatial reste donc une décision de performance à mesurer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence:
  level: static-review
  blender_execution: not_executed
  godot_execution: not_executed
  shader_compilation: not_executed
  multimesh_population: not_executed
  density_benchmark: not_executed
  cpu_gpu_measurement: not_executed
  distance_validation: not_executed
  pdf: not_built
decision:
  documentation: reviewed
  production_assets: blocked
  runtime_claims: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les statuts textuels distinguent clairement relecture, exécution et mesure.

- **Réserve :** `not_executed` empêche de présenter un exemple comme un résultat de production.

- **Décision :** le document peut être accepté tandis que les assets et performances restent bloqués.

- **PDF :** la compilation du Livre III reste différée jusqu’à la fin du livre.

## 4. Périmètre et frontières


Le chapitre couvre :

- brief de biome, fonctions visuelles et continuités avec le terrain ;
- catalogue d’espèces, morphotypes, variantes et provenance ;
- arbres, arbustes, herbes, fleurs, couvre-sols et débris ;
- pivots, échelles, ancrages, hiérarchies et zones de vent ;
- feuillage géométrique, cartes alpha et opacité ;
- variantes de taille, saison, couleur et santé ;
- cartes et règles de distribution ;
- instancing Blender pour prévisualisation et `MultiMesh` Godot pour runtime ;
- regroupement par cellule, espèce, matériau et niveau de détail ;
- collisions ciblées, navigation, ombres et interactions locales ;
- LOD, imposteurs et représentations agrégées ;
- benchmark de densité, distance, overdraw, mémoire et coût CPU/GPU.

Le chapitre ne couvre pas :

- le terrain, les tuiles et le streaming général du chapitre 14 ;
- le pipeline PBR transversal du chapitre 16 ;
- les UV et le baking détaillés du chapitre 17 ;
- les animations générales du chapitre 20 ;
- les VFX météorologiques du chapitre 23 ;
- l’intégration globale du chapitre 28 ;
- les populations dynamiques, la croissance, la reproduction, la mortalité ou la succession écologique du Livre II ;
- les règles gameplay de récolte, ressources, dégâts ou régénération.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
responsibility_matrix:
  chapter_14:
    owns: [terrain, cells, streaming, roads, water_interfaces]
  chapter_15:
    owns: [vegetation_assets, biome_profiles, placement_maps, wind_profiles, density_benchmarks]
  chapter_16:
    owns: [pbr_channels, color_spaces, compression, master_materials]
  livre_ii:
    owns: [ecological_state, growth, populations, regeneration, gameplay_harvest]
status:
  boundaries_reviewed: true
  runtime_integration: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** chaque chapitre possède une responsabilité distincte et vérifiable.

- **Données :** les profils artistiques peuvent lire des données du Livre II sans les remplacer.

- **Limite :** les matériaux locaux n’anticipent pas le cours transversal du chapitre 16.

- **Statut :** l’intégration runtime reste explicitement en attente.

## 5. Le biome pilote de Project Asteria


`AST-VEG-BIOME-DELTA-001` doit permettre une lecture immédiate des zones humides, des sols ouverts, des lisières et des espaces perturbés. Le biome est construit autour de peu d’espèces fortement combinables plutôt que d’un catalogue immense impossible à mesurer.

La région pilote comprend quatre sous-contextes :

1. une rive humide dominée par arbres souples, roseaux et débris flottés ;
2. une prairie ouverte où la silhouette et le mouvement du vent sont lisibles ;
3. une lisière rocheuse qui utilise arbustes bas, mousses et bois mort ;
4. des abords anthropisés où la végétation se raréfie autour des routes et bâtiments.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
biome_id: AST-VEG-BIOME-DELTA-001
region_id: AST-WORLD-REGION-DELTA-001
visual_functions:
  wet_edge: signal_water_and_soft_ground
  open_meadow: preserve_long_sightlines
  rocky_edge: break_terrain_repetition
  disturbed_ground: clarify_human_activity
pilot_species_count: provisional
production_status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** le biome et la région restent reliés par des références stables.

- **Fonctions :** chaque sous-contexte possède un rôle de lecture avant une liste d’espèces.

- **Nombre :** le volume d’espèces est provisoire et doit être ajusté par les besoins du vertical slice.

- **Statut :** aucune production d’asset n’est déclarée.

## 6. Brief de traversée et lignes de vue


La végétation doit renforcer le parcours sans le rendre illisible. Les masses hautes peuvent cadrer une route, les herbes basses peuvent signaler un sol praticable, et les zones dégagées doivent préserver les repères du chapitre 14. Une densité visuellement riche mais qui masque portes, ennemis, ressources ou horizons essentiels est un échec fonctionnel.

Le brief enregistre donc les couloirs à garder ouverts, les zones de silhouette forte, les espaces d’approche des bâtiments et les distances où une transition de représentation peut devenir perceptible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
traversal_brief: AST-VEG-TRAVERSAL-DELTA-001-v001
protected_sightlines:
  - route_to_waystation
  - lake_to_watchtower
  - meadow_to_pass
clearance_zones:
  - building_entrances
  - road_shoulders
  - navigation_portals
visual_mass_zones:
  - river_bend
  - rocky_ledge
review_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les lignes de vue proviennent du brief territorial du chapitre 14.

- **Exclusions :** les dégagements protègent navigation, accès et lecture gameplay.

- **Masse :** les zones denses sont placées là où elles servent la composition.

- **Validation :** la revue doit être effectuée en caméra de jeu et non uniquement en vue aérienne.

## 7. Vocabulaire de production végétale


Le vocabulaire doit empêcher les glissements entre une donnée botanique, un mesh et une instance runtime.

- **espèce** : identité conceptuelle et visuelle ;
- **morphotype** : forme générale réutilisable, par exemple arbre jeune ou mature ;
- **variante** : asset alternatif compatible avec le même contrat ;
- **saison** : état visuel préparé, non calendrier autoritaire ;
- **santé** : apparence saine, stressée ou morte, sans simulation de croissance ;
- **prototype** : ressource source ou mesh partagé ;
- **instance** : occurrence placée dans une cellule ;
- **lot** : groupe d’instances rendu ensemble.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
vegetation_terms:
  species: stable_concept_identity
  morphotype: structural_form_family
  variant: compatible_visual_alternative
  season: prepared_visual_state
  health: prepared_condition_state
  prototype: shared_source_asset
  instance: placed_occurrence
  batch: jointly_rendered_group
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Concept :** l’espèce ne se confond pas avec un fichier mesh.

- **Structure :** le morphotype décrit une famille de silhouette et d’âge apparent.

- **Runtime :** l’instance et le lot appartiennent au placement et au rendu.

- **Frontière :** saison et santé sont des états visuels préparés, pas une simulation écologique.

## 8. Catalogue minimal d’espèces


Le catalogue pilote doit couvrir plusieurs échelles et fonctions sans dupliquer le même rôle. Une espèce haute ne remplace pas un couvre-sol, et une fleur de ponctuation ne remplace pas une masse d’herbe.

Le premier lot proposé comporte huit entrées fictives :

- aulne des brumes, arbre de rive ;
- saule lacustre, arbre souple de silhouette étalée ;
- genêt de schiste, arbuste de lisière ;
- roseau argenté, plante verticale humide ;
- graminée du delta, masse basse de prairie ;
- iris cendré, ponctuation florale ;
- mousse de faille, couvre-sol rocheux ;
- bois flotté sombre, débris organique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
catalog_id: AST-VEG-CATALOG-DELTA-001-v001
entries:
  - AST-VEG-TREE-MIST-ALDER-001
  - AST-VEG-TREE-LAKE-WILLOW-001
  - AST-VEG-SHRUB-SHALE-BROOM-001
  - AST-VEG-REED-SILVER-001
  - AST-VEG-GRASS-DELTA-001
  - AST-VEG-FLOWER-ASH-IRIS-001
  - AST-VEG-GROUNDCOVER-FAULT-MOSS-001
  - AST-VEG-DEBRIS-DARK-DRIFTWOOD-001
catalog_status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** les entrées couvrent canopée, sous-étage, strate herbacée et débris.

- **Identité :** chaque prototype possède un identifiant stable indépendant du nom de fichier.

- **Fiction :** les noms servent le monde de `Project Asteria` et n’impliquent pas une validation botanique réelle.

- **Statut :** le catalogue demeure un contrat de production.

## 9. Fiche d’espèce et provenance


Chaque espèce doit relier sa fonction, ses références, ses droits, ses dimensions, ses variantes et ses budgets. Une photographie de plante trouvée en ligne ne constitue ni une source redistribuable ni une licence d’utilisation.

La fiche distingue les références d’observation, les textures réellement utilisées, les scans éventuels et les décisions artistiques. Les sources bloquées ne sont pas remplacées silencieusement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
species_id: AST-VEG-TREE-MIST-ALDER-001
display_name: Aulne des brumes
functional_role: wet_edge_canopy
source_status:
  visual_references: pending_rights_review
  texture_sources: none_selected
  scan_sources: none
  generated_inputs: none
dimensions:
  mature_height_m: provisional
  crown_width_m: provisional
owner: environment_art
approval: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Provenance :** les références et les textures sont qualifiées séparément.

- **Dimensions :** les mesures sont candidates tant qu’aucun gabarit n’a été approuvé.

- **Responsabilité :** le propriétaire de la fiche est explicite.

- **Décision :** l’asset reste bloqué sans sources et échelle validées.

## 10. Références visuelles et critères observables


Les références doivent répondre à des questions précises : comment les branches se distribuent-elles, où le feuillage se concentre-t-il, quelle portion du tronc reste visible, comment la silhouette varie-t-elle entre jeune et mature, et comment la plante réagit-elle au vent ?

Les adjectifs seuls — « organique », « luxuriant », « réaliste » — ne suffisent pas. Ils doivent être traduits en critères observables : densité de couronne, angle moyen des branches principales, proportion de vide, rapport hauteur-largeur, fréquence des ruptures et taille apparente des masses de feuilles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reference_questions:
  silhouette:
    - crown_height_ratio
    - crown_width_ratio
    - visible_trunk_ratio
  branching:
    - primary_branch_count_range
    - branch_angle_distribution
    - asymmetry_pattern
  foliage:
    - cluster_scale
    - void_ratio
    - edge_irregularity
  motion:
    - trunk_rigidity
    - branch_flexibility
    - leaf_response
status: pending_observation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Questions :** chaque référence est reliée à une propriété observable.

- **Mesure :** les ratios peuvent être comparés sans prétendre reproduire une espèce réelle.

- **Mouvement :** le vent est préparé dès la lecture de la structure.

- **Statut :** les valeurs ne sont pas inventées avant l’observation.

## 11. Échelle, gabarits et ancrage au sol


Les plantes doivent être comparées aux personnages, bâtiments, routes et cellules du chapitre 14. Une végétation produite sans gabarit commun dérive rapidement : herbes trop hautes, arbres miniatures ou collisions disproportionnées.

L’origine d’un asset végétal se place sur sa zone d’ancrage au sol. L’axe vertical suit la convention du projet, et la rotation aléatoire se fait autour de cet axe. Les racines visibles ou pierres intégrées ne doivent pas déplacer silencieusement le pivot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
scale_contract: AST-VEG-SCALE-001-v001
reference_objects:
  - AST-CHR-HUMAN-GUIDE-001
  - AST-ARCH-DOOR-GUIDE-001
  - AST-WORLD-TILE-GUIDE-001
origin:
  role: ground_anchor
  vertical_axis: project_up_axis
  rotation_axis: vertical_axis
root_overhang:
  allowed: visual_only
  pivot_shift: forbidden_after_publish
status: pending_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Références :** les gabarits relient végétation, personnages, architecture et terrain.

- **Origine :** le point d’ancrage permet un placement répétable sur le sol.

- **Invariant :** le pivot ne change pas silencieusement après publication.

- **Mesure :** les dimensions finales attendent une comparaison en scène.

## 12. Architecture des sources Blender


Une source Blender claire sépare prototypes, cartes de feuillage, collisions, volumes de vent et collections de prévisualisation. Les instances de Geometry Nodes peuvent accélérer la composition et tester une distribution, mais les prototypes doivent rester identifiables et exportables indépendamment.

La collection `__EXPORT` ne contient que les éléments destinés à l’échange. Les collections de références, de mesures et de prévisualisation ne sont pas exportées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
AST-VEG-TREE-MIST-ALDER-001.blend
├── __SOURCE
│   ├── TRUNK
│   ├── BRANCHES
│   ├── FOLIAGE_CARDS
│   └── WIND_GUIDES
├── __COLLISION
│   └── COL_TRUNK
├── __LOD
│   ├── LOD0
│   ├── LOD1
│   ├── LOD2
│   └── IMPOSTOR_SOURCE
├── __EXPORT
│   └── approved_export_candidates
└── __PREVIEW
    └── instance_on_points_tests
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** source, collision, LOD et prévisualisation restent indépendants.

- **Export :** la collection `__EXPORT` constitue le contrat d’échange.

- **Prévisualisation :** les instances Geometry Nodes ne sont pas confondues avec les instances runtime.

- **Maintenance :** les noms stables facilitent audit, dérivation et remplacement.

## 13. Arbres : tronc, branches et couronne


Un arbre pilote commence par la silhouette et les masses, pas par des milliers de feuilles. Le tronc principal fixe l’inclinaison générale, les branches primaires construisent la couronne et les branches secondaires organisent les clusters de feuillage.

La couronne doit présenter des vides. Une sphère uniformément remplie est difficile à lire, coûteuse en transparence et peu crédible au vent. Les masses sont évaluées en contre-jour, en vue latérale et à distance de jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
tree_blockout:
  species_id: AST-VEG-TREE-MIST-ALDER-001
  stages:
    - trunk_axis
    - primary_branches
    - crown_masses
    - secondary_breakup
    - foliage_clusters
  review_views:
    - front
    - side
    - top
    - gameplay_distance
    - backlit
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** le volume principal précède le détail de feuille.

- **Branches :** les niveaux structuraux servent aussi la hiérarchie de vent.

- **Vues :** la silhouette est contrôlée sous plusieurs orientations et éclairages.

- **Statut :** aucun blockout réel n’est déclaré.

## 14. Arbustes et lisières


Les arbustes doivent créer une strate intermédiaire entre arbres et herbes. Ils servent à masquer les raccords de terrain, casser les lignes trop géométriques et guider le regard, mais ne doivent pas former un mur opaque permanent.

Un arbuste efficace combine un noyau de volume, quelques branches lisibles et des clusters de feuillage. Les variantes doivent modifier silhouette et densité, pas seulement la teinte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shrub_profile: AST-VEG-SHRUB-SHALE-BROOM-001-v001
structural_layers:
  core_volume: required
  readable_branches: required
  foliage_clusters: required
variant_axes:
  silhouette: [compact, spread, wind_shaped]
  density: [sparse, standard, dense]
  color: secondary_only
collision:
  default: none
  exceptional_large_variant: pending_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Strates :** l’arbuste occupe le sous-étage sans remplacer les arbres ou les herbes.

- **Variantes :** silhouette et densité sont prioritaires sur une recoloration.

- **Collision :** la plupart des arbustes restent sans collision physique.

- **Revue :** les exceptions doivent être justifiées par leur usage.

## 15. Herbes, fleurs et couvre-sols


Les petites plantes sont visibles en masse. Leur qualité dépend donc davantage du rythme, de la silhouette collective, du mouvement et de l’overdraw que du détail d’un exemplaire isolé.

Les touffes d’herbe sont construites avec un nombre limité de lames ou cartes croisées, selon la cible. Les fleurs utilisent des ponctuations contrôlées ; elles ne doivent pas être réparties uniformément. Les couvre-sols peuvent employer géométrie basse, decals ou matériaux locaux selon le besoin, sans anticiper le pipeline PBR complet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ground_strata:
  grass_clump:
    prototype: AST-VEG-GRASS-DELTA-001
    role: continuous_mass
  flower_cluster:
    prototype: AST-VEG-FLOWER-ASH-IRIS-001
    role: sparse_accent
  moss_patch:
    prototype: AST-VEG-GROUNDCOVER-FAULT-MOSS-001
    role: rocky_transition
distribution:
  grass: broad_with_exclusions
  flower: clustered_sparse
  moss: slope_and_moisture_limited
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Masse :** les herbes forment la base visuelle continue.

- **Accent :** les fleurs restent rares pour conserver leur fonction de ponctuation.

- **Transition :** le couvre-sol relie roche et terrain sans masquer les interfaces.

- **Distribution :** chaque strate possède des règles différentes.

## 16. Débris organiques et bois mort


Le bois mort, les branches tombées, feuilles sèches et amas organiques apportent histoire et variation. Ils ne doivent toutefois pas devenir un bruit uniforme ajouté partout.

Les débris sont traités comme des props végétaux compatibles avec les cellules du chapitre 14. Leur placement suit ruissellement, lisières, berges, zones de vent ou activité humaine. Les pièces assez grandes pour bloquer un personnage reçoivent une collision dédiée ; les petits éléments restent visuels.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
debris_profile: AST-VEG-DEBRIS-DARK-DRIFTWOOD-001-v001
placement_causes:
  - river_deposition
  - shoreline_accumulation
  - storm_fall
  - disturbed_ground
size_classes:
  small:
    collision: none
  medium:
    collision: review
  large:
    collision: dedicated_proxy
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cause :** le placement découle d’un processus visuel compréhensible.

- **Classes :** les dimensions déterminent le besoin de collision.

- **Performance :** les petits débris restent des éléments de rendu.

- **Statut :** les modèles et collisions restent à produire.

## 17. Topologie et budget géométrique


Le nombre de triangles n’est pas un objectif isolé. Le budget dépend du nombre d’instances visibles, du nombre de matériaux, de la transparence, des ombres, du vent et de la distance. Une feuille très légère mais affichée des centaines de milliers de fois peut coûter davantage qu’un tronc plus détaillé.

Les budgets sont exprimés par prototype et par scène de densité. Ils restent provisoires jusqu’aux mesures dans Godot sur le matériel de référence.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
geometry_budget_profile: AST-VEG-BUDGET-DELTA-001-v001
prototype_metrics:
  triangles: pending_measurement
  vertices: pending_measurement
  surfaces: pending_measurement
  materials: pending_measurement
scene_metrics:
  visible_instances_peak: pending_measurement
  visible_triangles_peak: pending_measurement
  transparent_pixel_cost: pending_measurement
  shadow_casters_peak: pending_measurement
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Prototype :** les coûts d’un asset sont enregistrés avant instancing.

- **Scène :** la densité visible transforme le coût unitaire en coût réel.

- **Transparence :** l’overdraw est mesuré séparément des triangles.

- **Décision :** aucun budget n’est accepté sans campagne Godot.

## 18. Feuillage : géométrie, cartes et opacité


Le feuillage peut employer de la géométrie, des cartes alpha ou une combinaison. Les cartes réduisent la géométrie mais augmentent le risque d’overdraw, de tri et de halo. La géométrie augmente le nombre de sommets mais peut mieux contrôler les silhouettes proches.

Dans Godot, un matériau envoyé dans le pipeline transparent coûte plus cher et peut présenter des problèmes de tri. Pour de nombreuses feuilles, l’alpha scissor ou une stratégie de découpe adaptée est généralement plus contrôlable que l’alpha blend généralisé, mais le choix doit être validé sous les éclairages du projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foliage_representation:
  near:
    leaf_geometry: optional
    alpha_cards: allowed
    alpha_mode: scissor_candidate
  mid:
    clustered_cards: preferred_candidate
    double_sided: review
  far:
    reduced_clusters: candidate
    impostor: candidate
forbidden_defaults:
  - full_alpha_blend_everywhere
  - unique_material_per_variant
validation: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Proximité :** la représentation proche dépend de la taille apparente et du style.

- **Distance :** les clusters réduits et imposteurs sont des candidats, pas des automatismes.

- **Opacité :** le mélange alpha généralisé est interdit comme valeur par défaut.

- **Validation :** le choix doit être testé pour tri, halo et overdraw.

## 19. Atlas, matériaux partagés et frontière PBR


Le chapitre prépare les regroupements nécessaires aux végétaux : familles d’atlas, masques de vent, variations par instance et conventions de nommage. Il ne redéfinit pas les espaces colorimétriques, compressions, canaux PBR ou matériaux maîtres du chapitre 16.

Un atlas partagé peut réduire les changements de matériau, mais un atlas immense qui mélange toutes les espèces devient difficile à maintenir. Les regroupements suivent les familles, les usages et les plateformes ciblées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
vegetation_material_contract: AST-VEG-MAT-CONTRACT-001-v001
families:
  bark:
    atlas_group: trees_delta
  foliage:
    atlas_group: wetland_foliage
  grass:
    atlas_group: ground_strata
instance_variation:
  color: allowed_with_limits
  custom_data: reserved_for_wind_and_state
pbr_authority: chapter_16
status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Familles :** les atlas regroupent des usages compatibles plutôt que tout le catalogue.

- **Variation :** la couleur par instance ne remplace pas des textures ou matériaux validés.

- **Données :** les canaux personnalisés sont réservés par contrat.

- **Autorité :** la définition PBR complète demeure au chapitre 16.

## 20. Pivots, normales et orientation


Les pivots de végétation se placent au point d’ancrage. Les normales des cartes doivent éviter les variations incohérentes entre clusters. Les arbres inclinés conservent un axe local utile au vent et au placement.

Les variantes miroir sont explicites : un miroir arbitraire peut inverser les normales, casser le vent ou modifier l’asymétrie. Les rotations aléatoires autour de l’axe vertical sont autorisées seulement si le prototype le supporte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
orientation_contract:
  origin_role: ground_anchor
  local_up: project_up_axis
  random_yaw:
    allowed: true
    axis: local_up
  random_pitch_roll:
    allowed: false
    exceptions: [fallen_debris]
  mirror:
    allowed: explicit_variant_only
normal_review: pending
wind_axis_review: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ancrage :** l’origine correspond au contact principal avec le terrain.

- **Rotation :** le lacet aléatoire préserve l’axe vertical du prototype.

- **Exceptions :** les débris tombés suivent un contrat différent.

- **Revue :** normales et axes de vent restent à inspecter en scène.

## 21. Variantes de silhouette


Une bibliothèque crédible exige plusieurs silhouettes, mais chaque variante doit justifier son coût. Les variantes proches peuvent partager tronc, branches secondaires, matériaux ou cartes, tandis que les différences majeures sont conservées dans des prototypes distincts.

Le minimum utile pour un arbre pilote est souvent une famille jeune, mature et déformée par l’environnement. Le nombre exact dépend de la fréquence d’apparition et de la distance d’observation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
variant_family: AST-VEG-TREE-MIST-ALDER-FAMILY-001
shared_data:
  bark_material: intended
  foliage_atlas: intended
  wind_profile: intended
morphotypes:
  - young_upright
  - mature_spread
  - river_wind_shaped
duplication_review: pending
production_status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Partage :** les données communes réduisent le coût de maintenance.

- **Morphotypes :** les silhouettes répondent à des âges apparents et contraintes distinctes.

- **Revue :** la duplication géométrique doit être quantifiée.

- **Statut :** la famille n’est pas encore produite.

## 22. Variantes de saison et de santé


Les saisons et états de santé sont des représentations préparées. Le chapitre ne décide pas quand elles s’activent ni comment elles évoluent. Le Livre II peut sélectionner un état visuel via des données de contenu, mais l’asset reste passif.

Les variantes doivent partager autant de données que possible. Une saison ne doit pas entraîner quatre copies complètes d’un arbre si seules la couleur, la densité des feuilles et quelques clusters changent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
visual_state_family:
  species_id: AST-VEG-TREE-MIST-ALDER-001
  seasons:
    fresh:
      foliage_density: profile_fresh
      material_variant: foliage_fresh
    dry:
      foliage_density: profile_reduced
      material_variant: foliage_dry
  health:
    healthy: standard_structure
    stressed: reduced_clusters
    dead: branch_only_variant
authority:
  selection: livre_ii_or_content_data
  transition_logic: outside_chapter
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Partage :** les états réutilisent structure et matériaux lorsque possible.

- **Saison :** la densité et la teinte sont des profils, pas des événements temporels.

- **Santé :** l’état mort peut nécessiter une silhouette distincte.

- **Autorité :** la logique de sélection ne réside pas dans l’asset.

## 23. Hiérarchie de vent


Le vent doit suivre la structure : tronc peu mobile, branches principales lentes, rameaux plus souples, feuilles rapides. Une simple oscillation identique sur tous les sommets produit un effet de gelée et synchronise la forêt.

Les poids ou masques de vent sont préparés dans l’asset. Le shader reçoit un temps global, une direction, une intensité et une phase par instance. Les amplitudes restent à mesurer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
wind_profile: AST-VEG-WIND-TREE-FLEX-001-v001
layers:
  trunk:
    frequency: low_candidate
    amplitude: minimal_candidate
  primary_branches:
    frequency: low_candidate
    amplitude: moderate_candidate
  twigs:
    frequency: medium_candidate
    amplitude: higher_candidate
  leaves:
    frequency: high_candidate
    amplitude: local_candidate
instance_phase:
  source: deterministic_custom_data
status: pending_shader_test
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hiérarchie :** chaque niveau structurel possède une réponse distincte.

- **Phase :** la variation par instance évite une synchronisation rigide.

- **Paramètres :** fréquences et amplitudes restent des candidats.

- **Test :** le shader doit être compilé et observé avant acceptation.

## 24. Shader de vent pédagogique


L’exemple suivant montre une architecture de shader, pas un shader validé pour la production. Le déplacement combine une onde globale et une phase par instance ; un masque de sommet limite la déformation à la végétation souple.

Le code doit être adapté aux canaux réellement exportés, au renderer et aux matériaux du chapitre 16.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```glsl
shader_type spatial;
render_mode cull_disabled;

uniform vec3 wind_direction = vec3(1.0, 0.0, 0.0);
uniform float wind_strength = 0.0;
uniform float wind_frequency = 0.0;

void vertex() {
    float bend_mask = COLOR.r;
    float instance_phase = INSTANCE_CUSTOM.x;
    float wave = sin(TIME * wind_frequency + instance_phase);
    vec3 direction = normalize(wind_direction);
    VERTEX += direction * wave * wind_strength * bend_mask;
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les uniforms décrivent direction, intensité et fréquence, tandis que `COLOR.r` porte le masque.

- **Instance :** `INSTANCE_CUSTOM.x` fournit une phase distincte par occurrence.

- **Effet :** le déplacement ne s’applique qu’aux sommets pondérés par `bend_mask`.

- **Limites :** normales, collisions, ombres et amplitudes doivent être validées en scène.

## 25. Interaction locale avec le personnage


L’interaction locale ne doit pas transformer chaque brin d’herbe en corps physique. Une solution courante transmet au shader une ou plusieurs positions d’influence proches du joueur, puis courbe visuellement les plantes. Les objets importants peuvent employer une animation ou un nœud interactif séparé.

La logique de récolte, destruction ou régénération reste hors du chapitre. L’interaction décrite ici est visuelle et locale.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
local_interaction:
  default:
    method: shader_influence_field
    physical_bodies_per_blade: forbidden
  exceptional_assets:
    method: dedicated_scene
    examples:
      - large_breakable_branch
      - harvestable_named_plant
  gameplay_authority: external
  visual_recovery: pending_test
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** un champ shader traite les masses sans corps physique individuels.

- **Exceptions :** les objets nommés ou interactifs reçoivent une scène dédiée.

- **Autorité :** la récolte et les dégâts restent dans les systèmes gameplay.

- **Test :** la courbure et le retour visuel doivent être observés en mouvement.

## 26. Profils LOD des plantes


Chaque prototype reçoit des représentations adaptées à sa taille apparente. Les changements peuvent réduire géométrie, nombre de clusters, ombres, complexité du vent ou matériaux. Les distances ne sont pas copiées d’un autre projet : elles sont mesurées dans la caméra et la résolution cibles.

Un arbre peut disposer de plusieurs meshes, alors qu’une petite herbe peut disparaître directement ou être intégrée à une représentation agrégée de cellule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
lod_profile: AST-VEG-LOD-TREE-MIST-ALDER-001-v001
levels:
  LOD0:
    representation: full_tree
    shadows: candidate
    wind: full_profile_candidate
  LOD1:
    representation: reduced_clusters
    shadows: candidate
    wind: simplified_candidate
  LOD2:
    representation: low_cluster_mesh
    shadows: off_candidate
    wind: minimal_candidate
  impostor:
    representation: billboard_or_octagonal_candidate
thresholds:
  source: pending_measurement
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** chaque représentation réduit plusieurs dimensions du coût.

- **Ombres :** leur maintien dépend de la distance et du rôle de silhouette.

- **Imposteur :** la technique reste un candidat à produire et tester.

- **Seuils :** les distances finales proviendront du benchmark.

## 27. Imposteurs et représentations lointaines


Un imposteur remplace un volume complexe par une représentation basée sur une ou plusieurs vues. Il réduit la géométrie, mais introduit des coûts de texture, de mémoire, de transition et parfois de parallaxe.

Les imposteurs doivent conserver silhouette, teinte moyenne et réaction à la lumière suffisamment crédibles à la distance d’usage. Ils ne sont pas utiles pour toutes les plantes ; les petits végétaux peuvent simplement disparaître ou être agrégés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
impostor_contract:
  source_views: pending
  capture_lighting: neutral_reference
  alpha_mode: pending_review
  normal_data: optional_candidate
  wind_response: limited_candidate
  transition:
    method: pending_measurement
    popping_review: required
  memory_cost: pending_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capture :** les vues doivent être produites sous une lumière contrôlée.

- **Données :** normales et vent sont optionnels selon le bénéfice mesuré.

- **Transition :** le popping est une porte de validation explicite.

- **Coût :** l’économie géométrique est comparée au coût texture et mémoire.

## 28. Cartes de distribution


Les cartes de distribution décrivent où une famille peut apparaître. Elles ne doivent pas contenir l’état écologique complet du monde. Les canaux peuvent représenter humidité, exposition, perturbation, densité ou exclusions, à condition que leur sens soit versionné.

Une carte doit être alignée avec les cellules et le repère du chapitre 14. Son origine, son étendue, sa résolution et sa convention de bord sont enregistrées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
distribution_map: AST-VEG-DIST-DELTA-001-v001
spatial_reference:
  region_id: AST-WORLD-REGION-DELTA-001
  origin: inherited_from_world_partition
  extent: pending
  resolution: pending
channels:
  r: moisture_candidate
  g: open_ground_candidate
  b: disturbance_candidate
  a: exclusion_candidate
border_contract: shared_with_neighbor_cells
status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Alignement :** la carte hérite du repère spatial de la région.

- **Canaux :** chaque composante possède une sémantique versionnée.

- **Bord :** les cellules voisines doivent partager une convention de raccord.

- **Statut :** résolution et étendue restent à produire.

## 29. Règles de pente, altitude et humidité


Une espèce ne se place pas seulement selon une texture peinte. Les règles peuvent filtrer pente, altitude relative, distance à l’eau, exposition, type de sol et proximité d’une route. Ces valeurs restent artistiques tant qu’elles ne sont pas reliées à la simulation du Livre II.

Les règles sont évaluées dans un ordre stable. Un point exclu ne doit pas être réintroduit par une étape ultérieure de randomisation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
placement_rule: AST-VEG-RULE-REED-SILVER-001-v001
prototype_id: AST-VEG-REED-SILVER-001
requirements:
  moisture_mask: high_candidate
  distance_to_water: bounded_candidate
  slope: low_candidate
  disturbance: allowed_candidate
exclusions:
  - roads
  - building_pads
  - navigation_portals
  - deep_water
evaluation_order:
  - exclusions
  - habitat_requirements
  - density
  - variation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Prototype :** la règle référence une identité d’asset stable.

- **Exclusions :** les zones interdites sont évaluées avant la densité.

- **Habitat :** les seuils restent des candidats artistiques à mesurer.

- **Ordre :** la randomisation ne peut pas annuler une exclusion.

## 30. Densité et regroupement spatial


La densité doit être exprimée dans une unité claire, par exemple instances candidates par surface ou nombre maximal par lot. Une valeur sans surface, sans taille de cellule et sans distribution n’est pas comparable.

Le regroupement spatial détermine le culling. Un seul `MultiMesh` couvrant tout le monde peut être rendu dès qu’une petite partie de sa boîte est visible. À l’inverse, trop de petits lots augmentent le nombre de nœuds et de ressources. La taille optimale se mesure.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
density_profile: AST-VEG-DENSITY-MEADOW-001-v001
unit: instances_per_square_meter_candidate
species_weights:
  AST-VEG-GRASS-DELTA-001: pending
  AST-VEG-FLOWER-ASH-IRIS-001: pending
batch_partition:
  inherited_cell: true
  subcell_grouping: candidate
  maximum_extent: pending_measurement
culling_review: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** la densité doit être reliée à une surface.

- **Poids :** les espèces sont combinées sans imposer un nombre non mesuré.

- **Découpage :** les lots suivent au minimum les cellules du chapitre 14.

- **Mesure :** la taille des groupes est déterminée par culling et coût CPU.

## 31. Placement déterministe et graines


Un placement reproductible facilite les comparaisons, les captures, les tests et les corrections. La graine ne garantit pas à elle seule une identité stable : l’algorithme, l’ordre des points, les versions d’assets et les règles doivent également être enregistrés.

Les identifiants de cellules et d’espèces participent à la graine dérivée. Une modification de règle doit produire une nouvelle version du profil.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
placement_seed_contract:
  global_seed: project_defined
  derived_from:
    - region_id
    - cell_id
    - species_id
    - rule_version
  deterministic_order:
    - sort_candidate_points
    - apply_exclusions
    - evaluate_rules
    - choose_variant
  algorithm_version: AST-VEG-SCATTER-ALG-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Graine :** elle est dérivée d’identifiants stables et non d’un hasard implicite.

- **Ordre :** les points candidats sont triés avant filtrage.

- **Version :** l’algorithme fait partie de la reproductibilité.

- **Limite :** une seed identique ne suffit pas si les règles ou assets changent.

## 32. Prévisualisation avec Geometry Nodes


Dans Blender, `Instance on Points` peut ajouter une référence de géométrie sur des points sans dupliquer toutes les données sous-jacentes. Cette fonction est utile pour examiner silhouette collective, densité et variation avant export.

La prévisualisation Blender ne doit pas devenir une source runtime opaque. Les points, graines et règles sont exportés ou reconstruits selon un contrat explicite, et les prototypes restent séparés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Geometry Nodes preview
Input terrain or proxy surface
    ↓
Distribute candidate points
    ↓
Apply slope and mask selection
    ↓
Pick prototype from controlled collection
    ↓
Set deterministic rotation and scale
    ↓
Instance on Points
    ↓
Compare silhouette and density
    ↓
Do not treat preview as runtime proof
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la surface de prévisualisation doit partager le repère du terrain.

- **Sélection :** les masques et pentes sont appliqués avant instancing.

- **Variation :** rotation et échelle sont déterministes et bornées.

- **Frontière :** la vue Blender ne prouve ni culling, ni mémoire, ni coût Godot.

## 33. Choisir entre scènes individuelles et MultiMesh


Une scène individuelle convient aux plantes uniques, interactives ou porteuses de logique. Un `MultiMeshInstance3D` convient aux grands ensembles de prototypes identiques dont les transformations et données par instance suffisent.

Godot indique qu’un `MultiMesh` est une primitive de dessin unique très efficace, mais que les instances individuelles ne sont pas cullées séparément. Il faut donc découper les lots par zones pertinentes et éviter un `MultiMesh` mondial unique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
representation_decision:
  named_interactive_tree:
    node_type: derived_scene
    reason: unique_state_or_interaction
  repeated_large_tree:
    node_type: MultiMeshInstance3D_candidate
    partition: cell_or_subcell
  grass_mass:
    node_type: MultiMeshInstance3D_candidate
    partition: measured_group
  rare_flower:
    node_type: multimesh_or_shared_scene
    decision: benchmark
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interaction :** les assets porteurs d’état utilisent une scène dédiée.

- **Répétition :** les grands groupes identiques sont candidats au `MultiMesh`.

- **Culling :** chaque lot est spatialement borné.

- **Benchmark :** les catégories intermédiaires sont décidées par mesure.

## 34. Ressource MultiMesh et formats d’instance


La ressource `MultiMesh` enregistre un mesh partagé, un nombre d’instances, des transformations et éventuellement des couleurs ou données personnalisées. Ces canaux doivent être définis avant de remplir le buffer.

Les données par instance servent par exemple à une phase de vent, une variation de teinte limitée, un index d’état visuel ou un masque d’interaction. Elles ne doivent pas devenir un stockage gameplay caché.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
func create_multimesh(
    mesh: Mesh,
    instance_count: int,
    use_colors: bool,
    use_custom_data: bool
) -> MultiMesh:
    var result := MultiMesh.new()
    result.transform_format = MultiMesh.TRANSFORM_3D
    result.use_colors = use_colors
    result.use_custom_data = use_custom_data
    result.mesh = mesh
    result.instance_count = max(instance_count, 0)
    result.visible_instance_count = result.instance_count
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `mesh`, `instance_count` et les deux booléens définissent le format avant allocation.

- **Retour :** la fonction retourne une ressource `MultiMesh` initialisée, jamais un nœud de scène.

- **Opérateur :** `max(instance_count, 0)` interdit un nombre négatif d’instances.

- **Effet :** la fonction alloue les emplacements mais ne remplit aucune transformation.

## 35. Remplir les transformations


Les transformations sont construites dans le repère local du lot. La position mondiale doit être convertie si le `MultiMeshInstance3D` est déplacé avec sa cellule. L’échelle et la rotation sont bornées par le profil d’espèce.

Une erreur de repère produit des végétaux décalés à l’activation d’une cellule. Le test doit donc déplacer la cellule entière et vérifier que ses lots restent alignés au terrain.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
func populate_transforms(
    target: MultiMesh,
    local_transforms: Array[Transform3D]
) -> void:
    var count: int = min(target.instance_count, local_transforms.size())
    for index: int in range(count):
        target.set_instance_transform(index, local_transforms[index])
    target.visible_instance_count = count
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** la ressource cible et le tableau typé de transformations utilisent le même repère local.

- **Boucle :** `range(count)` ne dépasse ni la capacité ni le nombre de données disponibles.

- **Effet :** chaque emplacement reçoit une transformation puis le nombre visible est ajusté.

- **Retour :** la fonction ne retourne rien et modifie seulement la ressource passée.

## 36. Couleur et données personnalisées par instance


La couleur par instance peut apporter une variation légère, mais elle ne doit pas compenser un catalogue insuffisant. Les données personnalisées sont précieuses et doivent être documentées par composante.

Un contrat possible réserve `x` à la phase de vent, `y` à une intensité locale, `z` à un index d’état visuel normalisé et `w` à une valeur libre future. La convention doit rester stable entre script et shader.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
instance_custom_data_contract:
  x:
    meaning: wind_phase
    range: normalized
  y:
    meaning: wind_strength_multiplier
    range: normalized
  z:
    meaning: visual_state_index
    range: normalized
  w:
    meaning: reserved
    range: normalized
instance_color:
  use: subtle_tint_only
  gameplay_data: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canaux :** chaque composante possède un sens unique.

- **Shader :** le même contrat doit être utilisé dans le code et le matériau.

- **Variation :** la teinte reste subtile pour éviter une recoloration aléatoire.

- **Frontière :** aucune donnée gameplay autoritaire n’est cachée dans le rendu.

## 37. Boîte englobante et culling des lots


Un `MultiMesh` est cullé comme un ensemble. Sa boîte englobante doit donc couvrir toutes ses instances, y compris leur mouvement au vent. Une boîte trop petite fait disparaître des plantes ; une boîte immense maintient le lot visible trop longtemps.

Le découpage par cellule ou sous-cellule et la boîte personnalisée éventuelle sont validés avec des caméras latérales, des hauteurs différentes et des mouvements rapides.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
multimesh_culling_profile:
  partition_key:
    - cell_id
    - species_id
    - lod_level
    - material_family
  bounds:
    source: computed_from_instances_candidate
    wind_margin: pending_measurement
    custom_aabb: optional_candidate
  tests:
    - lateral_camera
    - elevated_camera
    - fast_traversal
    - cell_activation_boundary
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clé :** les lots combinent espace, espèce, niveau et matériau.

- **Boîte :** les transformations et le vent participent à l’étendue.

- **Option :** `custom_aabb` n’est utilisé qu’après diagnostic.

- **Tests :** plusieurs caméras recherchent disparitions et sur-rendu.

## 38. Découpage par cellule et streaming


Le chapitre 14 possède les cellules, leur activation et leur retrait. Le chapitre 15 fournit des ressources végétales attachées à ces cellules. Les lots ne doivent pas survivre silencieusement au retrait de leur propriétaire spatial.

Le manifeste de cellule référence profils de biome, cartes de distribution et lots dérivés. Les caches peuvent être régénérés ; les profils sources restent canoniques.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
cell_vegetation_manifest:
  cell_id: AST-WORLD-CELL-DELTA-03-07
  biome_profile: AST-VEG-BIOME-DELTA-001
  distribution_map: AST-VEG-DIST-DELTA-001-v001
  derived_batches:
    - grass_lod0_group_a
    - reeds_lod0_group_b
    - trees_lod1_group_a
  ownership:
    load: world_cell
    unload: world_cell
  source_of_truth: biome_and_distribution_profiles
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cellule :** le propriétaire spatial est explicite.

- **Sources :** le biome et la carte restent canoniques.

- **Dérivés :** les lots peuvent être reconstruits et supprimés.

- **Cycle :** chargement et retrait suivent l’autorité du chapitre 14.

## 39. Collisions ciblées


La collision est réservée aux volumes qui influencent réellement la navigation ou la physique : troncs importants, grosses souches, branches tombées ou rochers intégrés. Les feuilles, herbes, fleurs et petits arbustes ne reçoivent pas une collision individuelle.

Les collisions restent des proxies simples. Un arbre proche peut utiliser quelques capsules ou boîtes ; son feuillage détaillé n’est pas un volume physique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
vegetation_collision_policy:
  large_tree_trunk:
    collision: dedicated_simple_proxy
  large_stump:
    collision: dedicated_simple_proxy
  fallen_log:
    collision: dedicated_proxy_if_blocking
  shrub:
    collision: none_by_default
  grass:
    collision: none
  flower:
    collision: none
  foliage_cards:
    collision: forbidden
navigation_review: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** seuls les volumes qui bloquent réellement reçoivent une collision.

- **Proxy :** la forme physique reste plus simple que le rendu.

- **Interdiction :** les cartes de feuillage ne deviennent jamais collision.

- **Navigation :** les effets sur le navmesh doivent être testés.

## 40. Navigation et dégagements


Les plantes influencent la navigation de trois manières : collision physique, exclusion de placement et lisibilité visuelle. Une herbe sans collision peut néanmoins masquer un bord ou une porte ; une forêt peut rester physiquement traversable mais visuellement impénétrable.

Les cartes d’exclusion protègent portes, chemins, points d’apparition et bords de navmesh. Les gros troncs doivent être présents avant la génération ou la mise à jour de navigation selon le pipeline retenu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
navigation_clearance:
  protected_interfaces:
    - doors
    - stairs
    - bridges
    - navigation_links
    - spawn_points
  visual_clearance:
    - critical_signage
    - quest_landmarks
    - combat_readability_zones
  blocking_trunks:
    navmesh_integration: pending_pipeline_decision
  small_plants:
    navmesh_effect: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interfaces :** les zones de passage restent libres de végétation conflictuelle.

- **Lisibilité :** certaines exclusions sont visuelles plutôt que physiques.

- **Troncs :** leur prise en compte dépend du pipeline de navigation.

- **Petites plantes :** elles ne modifient pas le navmesh.

## 41. Ombres et éclairage


Les ombres végétales donnent du volume, mais elles peuvent coûter cher lorsque des milliers d’instances projettent des cartes alpha. Les profils doivent distinguer arbres proches, arbustes moyens, herbes et représentations lointaines.

Les ombres peuvent être réduites ou supprimées selon le LOD. Cette décision doit être observée sous plusieurs heures et éclairages, sans imposer les choix du chapitre 16.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shadow_profile: AST-VEG-SHADOW-DELTA-001-v001
categories:
  canopy_near:
    cast_shadow: candidate
  canopy_far:
    cast_shadow: reduced_or_off_candidate
  shrubs:
    cast_shadow: measured_candidate
  grass:
    cast_shadow: off_default_candidate
  impostors:
    cast_shadow: special_review
validation_lighting:
  - overcast
  - low_sun
  - night_key_light
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catégories :** les plantes ne partagent pas toutes la même politique d’ombre.

- **Distance :** les représentations lointaines peuvent réduire ce coût.

- **Éclairage :** les artefacts sont recherchés sous plusieurs conditions.

- **Mesure :** les choix restent provisoires jusqu’au benchmark.

## 42. Visibilité, LOD et HLOD dans Godot


Les propriétés de plage de visibilité des nœuds héritant de `GeometryInstance3D` peuvent servir aux LOD manuels et HLOD artistiques. Elles s’appliquent notamment à `MeshInstance3D` et `MultiMeshInstance3D`. Les transitions et marges doivent être réglées avec la caméra réelle.

Les LOD automatiques de mesh et les plages de visibilité peuvent coexister, mais leur combinaison doit rester lisible. Le chapitre évite d’empiler plusieurs systèmes sans matrice de test.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_visibility_profile:
  near_multimesh:
    visibility_range_begin: pending
    visibility_range_end: pending
    fade_mode: pending_review
  far_multimesh:
    visibility_range_begin: pending
    visibility_range_end: pending
    fade_mode: pending_review
  sector_hlod:
    representation: canopy_mass_candidate
    activation: pending_measurement
compatibility_test:
  automatic_mesh_lod: pending
  manual_ranges: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœuds :** les plages concernent les instances de géométrie, y compris les `MultiMeshInstance3D`.

- **Transition :** début, fin et fondu restent à mesurer.

- **HLOD :** une masse de canopée peut remplacer plusieurs lots à grande distance.

- **Compatibilité :** la combinaison avec le LOD automatique doit être testée.

## 43. Overdraw et transparence


L’overdraw mesure combien de fois les mêmes pixels sont retraités, problème fréquent avec les cartes de feuilles et les herbes croisées. Une scène peut avoir peu de triangles et rester coûteuse parce que plusieurs couches transparentes couvrent l’écran.

Le benchmark doit inclure vues de face, vues rasantes, contre-jour et caméra au cœur d’une masse. Le nombre de cartes, leur remplissage utile et leur taille à l’écran sont examinés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
overdraw_test_matrix:
  views:
    - meadow_front
    - meadow_grazing_angle
    - canopy_backlit
    - inside_shrub_mass
  variables:
    - card_count
    - alpha_coverage
    - alpha_mode
    - double_sided
    - shadow_casting
  metrics:
    - gpu_frame_time
    - transparent_pass_cost
    - visible_pixel_layers
status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Vues :** les angles défavorables sont inclus au lieu d’une seule capture flatteuse.

- **Variables :** géométrie, opacité et ombres sont modifiées séparément.

- **Mesures :** le coût GPU est relié à la complexité transparente.

- **Statut :** aucun résultat n’est annoncé.

## 44. Scène de benchmark de densité


La scène `AST-VEG-BENCH-DENSITY-001` compare plusieurs densités, tailles de lots, profils d’ombre, LOD et méthodes de représentation. Elle utilise un parcours reproductible et des points de caméra fixes.

Les essais froids et chauds sont séparés. Les mesures incluent temps CPU/GPU, mémoire, pics de frame, nombre de lots visibles, instances visibles, triangles et coût des passes transparentes. Les valeurs sont enregistrées avec matériel, versions et paramètres.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
benchmark_scene: AST-VEG-BENCH-DENSITY-001
hardware_profile:
  gpu: AMD_Radeon_RX_6750_XT_12GB
  cpu: Ryzen_7_2700
  ram_gb: 32
software:
  os: Windows_11
  godot: 4.7.1-stable
  renderer: Forward+
test_axes:
  density: [low_candidate, medium_candidate, high_candidate]
  batch_extent: [small_candidate, medium_candidate, large_candidate]
  shadows: [off, selected, broad]
  representation: [mesh, reduced_mesh, impostor_candidate]
results: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plateforme :** le matériel et les versions rendent les résultats comparables.

- **Axes :** une variable est modifiée par série contrôlée.

- **Profils :** les étiquettes ne prétendent pas fixer des nombres avant mesure.

- **Résultats :** la section reste vide tant que la scène n’est pas exécutée.

## 45. Collecte de mesures


Les mesures doivent être enregistrées dans un format tabulaire et liées à un commit, une scène, un profil de qualité et un parcours. Une moyenne seule ne suffit pas ; les pics et la variabilité sont importants pour le streaming et la densité.

Les captures visuelles accompagnent les chiffres afin de relier performance et qualité de transition.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```csv
run_id,commit,scene,quality_profile,camera_route,density_profile,batch_profile,cpu_ms,gpu_ms,memory_mb,visible_instances,visible_batches,notes
pending,pending,AST-VEG-BENCH-DENSITY-001,pending,route_a,low_candidate,small_candidate,pending,pending,pending,pending,pending,not_executed
pending,pending,AST-VEG-BENCH-DENSITY-001,pending,route_a,medium_candidate,medium_candidate,pending,pending,pending,pending,pending,not_executed
pending,pending,AST-VEG-BENCH-DENSITY-001,pending,route_a,high_candidate,large_candidate,pending,pending,pending,pending,pending,not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Colonnes :** chaque ligne conserve contexte matériel, scène et profils.

- **Temps :** CPU et GPU sont séparés.

- **Charge :** instances et lots visibles expliquent les variations.

- **Statut :** `pending` et `not_executed` empêchent toute fausse mesure.

## 46. Modes Solo et Studio


### Mode Solo

Le parcours Solo limite le biome à quelques espèces fortement réutilisables. Il privilégie un arbre, un arbuste, une herbe, une fleur, un couvre-sol et un débris avant toute extension. Les variantes sont créées seulement lorsqu’elles résolvent une répétition visible dans le vertical slice. Le benchmark cible d’abord le matériel de référence et une seule scène représentative.

### Mode Studio

Le parcours Studio versionne le catalogue par biome, sépare conception botanique, modélisation, lookdev, intégration et performance, puis utilise des matrices de qualité par plateforme. Les lots sont produits par familles, avec revues de provenance, silhouettes, matériaux, vent, LOD, distribution et coût. Les données de simulation du Livre II sont consommées par contrat et ne sont pas dupliquées dans les assets.

## 47. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 47.1 Créer un nœud ou un corps par brin d’herbe

**Symptôme :** la prairie fonctionne dans une petite zone mais le nombre de nœuds et de corps explose dès que la densité augmente.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
grass_runtime:
  representation: one_scene_per_blade
  physics_body_per_blade: true
  animation_player_per_blade: true
  expected_instances: very_high
  status: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le contrat transforme une masse répétitive en milliers de scènes et de corps physiques, alors que la majorité des brins n’a ni état unique ni interaction autoritaire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
grass_runtime:
  representation: MultiMeshInstance3D_candidate
  prototype: AST-VEG-GRASS-DELTA-001
  partition: measured_subcell_groups
  local_interaction: shader_field
  physics_body_per_blade: false
  status: blocked_until_benchmark
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le prototype partagé, les lots spatiaux et l’interaction shader réduisent les responsabilités par instance tout en maintenant une porte de mesure.

### 47.2 Utiliser un seul MultiMesh pour tout le monde

**Symptôme :** une petite portion de forêt visible maintient des instances très éloignées dans le même lot et les retraits de cellules deviennent impossibles à isoler.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
forest_batch:
  scope: whole_world
  multimesh_count: 1
  culling_unit: global
  cell_ownership: none
  unload_policy: never
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un `MultiMesh` est cullé comme un ensemble ; une boîte mondiale supprime le bénéfice du culling spatial et casse l’autorité des cellules.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
forest_batches:
  partition_keys: [cell_id, species_id, lod_level, material_family]
  culling_unit: measured_batch
  cell_ownership: required
  unload_policy: follow_cell
  batch_extent: pending_measurement
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les lots suivent les cellules et des clés stables, ce qui permet culling, chargement et retrait indépendants avant d’affiner leur taille par benchmark.

### 47.3 Randomiser la distribution sans contraintes

**Symptôme :** des roseaux apparaissent sur les routes, dans les bâtiments et au sommet des pentes sèches.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
scatter:
  points: random_uniform
  habitat_rules: none
  exclusions: none
  seed: current_time
  result: accepted_if_dense
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La densité aléatoire ignore humidité, pente, interfaces et reproductibilité ; elle ne peut ni être corrigée précisément ni comparée entre versions.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
scatter:
  seed_contract: AST-VEG-SCATTER-ALG-001
  exclusions: [roads, building_pads, navigation_portals]
  habitat_rules: AST-VEG-RULE-REED-SILVER-001-v001
  density_profile: pending
  result: blocked_until_visual_and_runtime_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le placement devient déterministe, filtré par exclusions et habitat, puis reste bloqué jusqu’aux revues appropriées.

### 47.4 Accepter des échelles et rotations illimitées

**Symptôme :** certaines plantes sont écrasées, flottent ou se couchent tandis que les arbres deviennent méconnaissables.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
variation:
  uniform_scale: random_0_to_4
  pitch_deg: random_0_to_360
  roll_deg: random_0_to_360
  yaw_deg: random_0_to_360
  species_constraints: ignored
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les transformations arbitraires détruisent l’ancrage, la silhouette et la fonction de l’espèce, et peuvent invalider collision et vent.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
variation:
  uniform_scale_range: species_profile_candidate
  yaw_deg: deterministic_0_to_360
  pitch_roll:
    default: zero
    exceptions: [fallen_debris]
  anchor_review: required
  status: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les variations sont bornées par espèce, le lacet reste compatible avec l’ancrage et les inclinaisons sont réservées aux prototypes qui les supportent.

### 47.5 Utiliser l’alpha blend pour tout le feuillage

**Symptôme :** les feuilles se trient mal, les masses deviennent laiteuses et le coût GPU augmente fortement en vue rasante.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
foliage_material:
  alpha_mode: blend
  card_layers: unlimited
  double_sided: true
  shadow_casting: true
  overdraw_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le mélange alpha généralisé multiplie les couches transparentes et les problèmes de tri sans porte d’overdraw.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
foliage_material:
  alpha_mode: scissor_candidate
  card_layers: bounded_by_profile
  double_sided: review
  shadow_casting: lod_profile
  overdraw_test: required
  status: blocked
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le mode d’opacité, les couches, les faces doubles et les ombres deviennent des décisions mesurées dans une matrice dédiée.

### 47.6 Synchroniser toutes les plantes avec la même onde

**Symptôme :** la prairie entière oscille comme une surface rigide et les arbres paraissent constitués d’un seul matériau élastique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```glsl
float phase = 0.0;
float bend_mask = 1.0;
float wave = sin(TIME * frequency + phase);
VERTEX.x += wave * strength * bend_mask;
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une phase unique et un déplacement identique ignorent la structure de la plante et synchronisent toutes les instances.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```glsl
float bend_mask = COLOR.r;
float phase = INSTANCE_CUSTOM.x;
float wave = sin(TIME * frequency + phase);
VERTEX += normalize(wind_direction) * wave * strength * bend_mask;
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le masque limite la déformation aux zones souples et la phase par instance casse la synchronisation, tout en conservant des paramètres à mesurer.

### 47.7 Ajouter une collision à chaque plante

**Symptôme :** la création des cellules devient lente, le navmesh est bruité et le personnage accroche des éléments purement visuels.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
collision_policy:
  tree: render_mesh
  shrub: render_mesh
  grass: capsule_per_clump
  flower: capsule_per_plant
  foliage_cards: mesh_collision
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La politique confond rendu et physique et crée des milliers de volumes sans effet gameplay utile.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
collision_policy:
  large_tree_trunk: dedicated_simple_proxy
  large_stump: dedicated_simple_proxy
  fallen_log: proxy_if_blocking
  shrub: none_by_default
  grass: none
  flower: none
  foliage_cards: forbidden
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Seuls les volumes réellement bloquants reçoivent des proxies simples, tandis que les strates visuelles restent sans collision.

### 47.8 Dupliquer chaque saison comme un asset complet

**Symptôme :** les corrections de tronc ou de LOD doivent être répétées dans plusieurs fichiers qui divergent rapidement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
season_variants:
  spring: full_duplicate_asset
  summer: full_duplicate_asset
  autumn: full_duplicate_asset
  winter: full_duplicate_asset
shared_data: none
version_link: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les copies complètes rompent le partage de structure, multiplient les corrections et rendent l’identité de la famille ambiguë.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
visual_state_family:
  shared_structure: source_tree_family
  shared_lod_rules: intended
  material_variants: [fresh, dry]
  foliage_density_profiles: [full, reduced, none]
  dead_structure: explicit_variant
  version_link: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La famille partage structure et règles, ne duplique que les différences nécessaires et conserve un lien de version entre états.

### 47.9 Valider la densité sur une capture fixe

**Symptôme :** la prairie paraît riche sur une image mais s’effondre en mouvement, à contre-jour ou sur le matériel de référence.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
density_review:
  evidence: one_beauty_screenshot
  camera: fixed
  gpu_measurement: none
  movement_test: none
  overdraw_test: none
  decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une capture unique ne révèle ni popping, ni overdraw, ni variation de frame, ni coût des lots pendant une traversée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
density_review:
  scene: AST-VEG-BENCH-DENSITY-001
  routes: [walk, sprint, elevated_camera]
  lighting: [overcast, low_sun, backlit]
  metrics: [cpu_ms, gpu_ms, memory_mb, visible_instances, visible_batches]
  captures: required
  decision: pending_measurement
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La scène reproductible combine parcours, éclairages, mesures et captures avant toute décision de densité.

### 47.10 Placer la simulation écologique dans le profil artistique

**Symptôme :** un artiste modifie un atlas et change involontairement croissance, reproduction ou régénération du monde.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
biome_asset:
  foliage_atlas: wetland_foliage
  growth_rate: 1.7
  reproduction_probability: 0.8
  mortality_rule: drought
  respawn_timer_seconds: 300
  authority: environment_art
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier mélange représentation visuelle et règles métier dynamiques, ce qui crée deux autorités concurrentes avec le Livre II.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
biome_visual_profile:
  foliage_atlas: wetland_foliage
  species_catalog: AST-VEG-CATALOG-DELTA-001-v001
  distribution_profile: AST-VEG-DIST-DELTA-001-v001
  prepared_visual_states: [fresh, dry, stressed, dead]
runtime_ecology_reference:
  authority: livre_ii
  state_selection_interface: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil artistique conserve assets et états préparés, tandis que la simulation et la sélection autoritaire restent référencées dans le Livre II.

## 48. Livrables à conserver


Le plan maître exige cinq livrables permanents, versionnés et séparés des caches :

1. **bibliothèque végétale** — espèces, prototypes, variantes, provenance, collisions et LOD ;
2. **profils de biome** — fonctions visuelles, strates, transitions et contrats avec le terrain ;
3. **cartes de distribution** — repère, canaux, exclusions, versions et règles ;
4. **shaders de vent** — hiérarchies, masques, paramètres et variantes de qualité ;
5. **benchmark de densité** — scène, parcours, profils, mesures, captures et décisions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
deliverable_manifest: AST-VEG-DELIVERY-001-v001
vegetation_library:
  profile: AST-VEG-CATALOG-DELTA-001-v001
  status: blocked
biome_profiles:
  profile: AST-VEG-BIOME-DELTA-001
  status: blocked
distribution_maps:
  profile: AST-VEG-DIST-DELTA-001-v001
  status: blocked
wind_shaders:
  profile: AST-VEG-WIND-TREE-FLEX-001-v001
  status: blocked
density_benchmark:
  profile: AST-VEG-BENCH-DENSITY-001
  status: blocked
publication_decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Manifeste :** les cinq entrées correspondent exactement au plan maître.

- **Profils :** chaque livrable possède une identité stable.

- **Statuts :** aucun fichier de production ou résultat runtime n’est déclaré.

- **Publication :** la décision reste bloquée jusqu’aux campagnes réelles.

## 49. Porte d’acceptation


Le biome pilote n’est accepté que si la bibliothèque couvre les strates nécessaires, si les espèces restent reconnaissables, si les distributions préservent parcours et interfaces, si les transitions LOD ne produisent pas de rupture majeure et si les densités respectent les budgets mesurés.

La validation compare au moins une zone humide, une prairie, une lisière et une zone perturbée. Elle inclut vues proches, moyennes et lointaines, déplacement du joueur, plusieurs éclairages, chargement de cellule et retrait.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate: AST-VEG-GATE-DELTA-001-v001
required:
  species_library_review: pending
  provenance_review: pending
  scale_and_pivot_review: pending
  wind_shader_test: pending
  distribution_alignment: pending
  protected_sightlines: pending
  collision_navigation_review: pending
  lod_impostor_transitions: pending
  cell_load_unload_test: pending
  density_benchmark: pending
  cpu_gpu_memory_budgets: pending
decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** la porte combine art, données, moteur et performance.

- **Interfaces :** terrain, navigation et streaming sont inclus.

- **Mesures :** les budgets doivent provenir du benchmark.

- **Décision :** un seul élément obligatoire en attente maintient le biome bloqué.

## 50. Synthèse opérationnelle pour Project Asteria


Le chapitre 15 fournit une méthode complète pour construire le biome du delta : brief de traversée, catalogue compact, fiches d’espèces, provenance, échelle, sources Blender, arbres, arbustes, herbes, fleurs, couvre-sols, débris, feuillage, atlas préparatoires, variantes de silhouette, états saisonniers et de santé, hiérarchie de vent, interaction locale, LOD, imposteurs, cartes de distribution, règles de pente et humidité, densité, placement déterministe, prévisualisation Geometry Nodes, lots `MultiMesh`, culling, collisions, navigation, ombres, overdraw et benchmark.

La bibliothèque reste bloquée tant que les références, modèles, textures, shaders, cartes, instances, collisions, scènes, mesures et captures ne sont pas réellement produits. Le chapitre prépare l’intégration aux cellules du chapitre 14 et aux données écologiques du Livre II, mais ne crée ni système dynamique de biome, ni croissance, ni population, ni régénération.

## 51. Références techniques officielles


Les références suivantes encadrent la matérialisation et doivent être requalifiées si les versions changent :

- [Godot — Optimization using MultiMeshes](https://docs.godotengine.org/en/stable/tutorials/performance/using_multimesh.html) ;
- [Godot — Using MultiMeshInstance3D](https://docs.godotengine.org/en/stable/tutorials/3d/using_multi_mesh_instance.html) ;
- [Godot — GeometryInstance3D](https://docs.godotengine.org/en/stable/classes/class_geometryinstance3d.html) ;
- [Godot — MeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_meshinstance3d.html) ;
- [Godot — Visibility ranges (HLOD)](https://docs.godotengine.org/en/4.5/tutorials/3d/visibility_ranges.html) ;
- [Blender Manual — Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ;
- [glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html).
