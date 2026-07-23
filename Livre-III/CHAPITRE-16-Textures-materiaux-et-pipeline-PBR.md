---
title: "Livre III — Chapitre 16 : Textures, matériaux et pipeline PBR"
id: "DOC-L3-CH16"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 16
last-verified: "2026-07-23T21:15:00+02:00"
audit-status: "complete"
audit-date: "2026-07-23T21:15:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-16.md"
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

# Textures, matériaux et pipeline PBR

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH16`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11
## 1. Rôle du chapitre
Les chapitres précédents ont préparé des humains, créatures, objets, bâtiments, terrains et végétaux. Ils ont parfois
défini des matériaux provisoires afin de vérifier une silhouette ou une séparation fonctionnelle, mais ils n’ont pas
établi le contrat transversal qui garantit qu’une roche, une peau, un métal, un tissu et un feuillage réagissent de
manière cohérente à la lumière.
Le présent chapitre construit ce contrat. Il relie les images sources, les canaux PBR, les espaces colorimétriques,
les résolutions, les mipmaps, la compression, la densité de texels, les familles de matériaux, l’export glTF et la
configuration Godot. La qualité n’est pas jugée dans une seule vue flatteuse : elle est comparée sous plusieurs
éclairages et selon un budget mémoire explicite.
Le laboratoire fil rouge est `AST-MAT-LAB-PBR-001`. Il contient des sphères étalons, des plans, des coins, un objet
aux courbures variées et plusieurs échantillons de Project Asteria. Il n’est pas une galerie promotionnelle ; il doit
révéler les incohérences de couleur, d’échelle, de rugosité, de normales, de répétition et de compression.
> **[LECTURE] Chaîne de référence — Ne pas saisir.**
```text
Source canonique et provenance
    ↓
Images de travail et rôles de canaux
    ↓
Espaces colorimétriques et formats
    ↓
Résolution, densité de texels et budget mémoire
    ↓
Matériaux tilables, trim sheets, atlas et détails
    ↓
Principled BSDF de contrôle dans Blender
    ↓
Export glTF / GLB et textures livrées
    ↓
Import Godot, compression et mipmaps
    ↓
StandardMaterial3D ou ORMMaterial3D
    ↓
Scène d'éclairage comparative
    ↓
Captures, mesures et porte d'acceptation
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Ordre :** les décisions sur les données précèdent le réglage artistique afin d’éviter des corrections tardives.
- **Source :** la source canonique reste distincte des images exportées et des ressources importées par Godot.
- **Preuve :** la scène comparative et les mesures de mémoire sont les sorties de validation attendues.
- **Frontière :** les découpes UV, les cages et le baking approfondi restent au chapitre 17.
## 2. Résultats d’apprentissage
À la fin du chapitre, le lecteur saura :
- distinguer base color, metallic, roughness, normal, ambient occlusion, height, emissive et opacity ;
- identifier les cartes de couleur qui utilisent sRGB et les cartes de données qui doivent rester linéaires ;
- choisir un format source et un format de livraison selon la précision, la transparence et le HDR ;
- estimer la mémoire brute et comprendre l’effet des mipmaps et de la compression GPU ;
- définir des profils de résolution sans imposer une taille unique à tous les assets ;
- mesurer et documenter une densité de texels cohérente ;
- construire une bibliothèque réduite de matériaux maîtres ;
- choisir entre matériau tilable, trim sheet, atlas, détail local et décalcomanie ;
- préparer un Principled BSDF Blender comme référence de lookdev, sans supposer une identité automatique avec Godot ;
- configurer les textures d’un `StandardMaterial3D` ou d’un `ORMMaterial3D` ;
- gérer filtre, répétition, anisotropie, mipmaps et compression selon l’usage ;
- construire une scène d’éclairage neutre, chaude, froide et contrastée ;
- comparer des captures avec caméra, exposition et environnement verrouillés ;
- conserver les réserves lorsque textures, matériaux, imports ou benchmarks n’ont pas été exécutés.
## 3. Niveau de preuve et réserves
Le chapitre est accepté au niveau `static-review`. Les contrats de données, procédures Blender, exemples GDScript,
profils d’import et matrices de validation ont été relus contre la documentation officielle. Cette relecture ne prouve
ni le rendu final, ni la fidélité entre applications, ni la consommation mémoire sur la machine de référence.
Aucune texture de Project Asteria, aucun matériau Blender, aucun `StandardMaterial3D`, aucun `ORMMaterial3D`, aucun
preset d’import, aucune scène d’éclairage, aucune capture comparative et aucune mesure de VRAM ne sont revendiqués
comme produits. Les résolutions, densités, tailles de lots et budgets présentés restent des candidats à mesurer.
> **[LECTURE] Statut de preuve — Ne pas saisir.**
```yaml
evidence:
  level: static-review
  blender_execution: not_executed
  godot_import: not_executed
  material_compilation: not_executed
  lighting_comparison: not_executed
  texture_memory_measurement: not_executed
  pdf: not_built
decision:
  documentation: reviewed
  material_library: blocked
  runtime_claims: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Statuts :** chaque activité possède un état distinct au lieu d’un unique drapeau de réussite.
- **Réserve :** `not_executed` interdit de présenter un exemple comme résultat observé.
- **Décision :** la documentation peut être acceptée alors que la bibliothèque de production reste bloquée.
- **PDF :** la compilation est différée jusqu’à la fin du Livre III.
## 4. Périmètre et frontières
Le chapitre couvre le modèle metallic-roughness, les espaces colorimétriques, les formats d’image, la mémoire, les
mipmaps, la compression, la densité de texels, les matériaux tilables, les trim sheets, les atlas, les détails,
l’organisation des sources, les matériaux Blender de contrôle, l’export glTF, l’import Godot et la scène de
comparaison.
Il ne refait pas les matériaux préparatoires spécifiques du terrain et de la végétation. Il ne détaille pas la découpe
UV, les cages, le baking de normales ou l’analyse d’artefacts tangentiels, qui appartiennent au chapitre 17. Il ne
remplace pas l’optimisation globale du chapitre 18 ni l’intégration complète du chapitre 28.
> **[LECTURE] Matrice de responsabilités — Ne pas saisir.**
```yaml
responsibility_matrix:
  chapter_14:
    owns: [terrain_layers, terrain_masks, streaming_interfaces]
  chapter_15:
    owns: [foliage_families, biome_variants, wind_contracts]
  chapter_16:
    owns: [pbr_channels, color_spaces, texture_profiles, master_materials, lighting_lab]
  chapter_17:
    owns: [retopology, uv_layout, cages, baking, tangent_artifacts]
  chapter_18:
    owns: [lod_chain, impostors, geometry_optimization]
status:
  boundaries_reviewed: true
  production_integration: pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Autorité :** chaque chapitre possède un périmètre de décision identifiable.
- **Continuité :** les matériaux préparatoires deviennent des consommateurs du pipeline commun sans être recréés.
- **Dépendance :** le chapitre 17 fournit ensuite les UV et cartes bakées nécessaires.
- **Statut :** l’intégration réelle reste en attente.
## 5. Laboratoire PBR de Project Asteria
`AST-MAT-LAB-PBR-001` sert de scène commune à toutes les familles de matériaux. Il doit contenir une sphère lisse, une
sphère facettée, un plan vertical, un plan horizontal, un coin intérieur, un cylindre, un objet à chanfreins et un
échantillon d’asset réel. Ces formes révèlent des défauts différents.
La scène utilise des caméras verrouillées et des environnements nommés. Toute capture indique le commit, le matériau,
le profil d’import et l’environnement. Une comparaison sans ces métadonnées ne peut pas expliquer un écart.
> **[LECTURE] Brief du laboratoire — Ne pas saisir.**
```yaml
lab:
  id: AST-MAT-LAB-PBR-001
  units: meters
  renderer: Forward+
  probes:
    - smooth_sphere
    - faceted_sphere
    - horizontal_plane
    - vertical_plane
    - interior_corner
    - beveled_reference_asset
  cameras: [close, medium, grazing]
  environments: [neutral, warm, cool, high_contrast]
  results: pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Formes :** chaque géométrie révèle une catégorie d’artefact de réflexion, de normale ou de répétition.
- **Caméras :** la vue rasante est indispensable pour la rugosité, les mipmaps et l’anisotropie.
- **Environnements :** plusieurs éclairages empêchent la validation sous une seule condition avantageuse.
- **Résultats :** `pending` conserve l’absence de scène exécutée.
## 6. Contrat d’un matériau
Un matériau n’est pas seulement un nom dans Blender ou Godot. C’est un ensemble versionné qui relie une famille
visuelle, des images sources, des canaux, des espaces colorimétriques, une échelle réelle, une densité de texels, des
règles de répétition, des profils d’import et des limites d’usage.
Le contrat sépare l’identité du matériau de ses variantes. Une variation humide, poussiéreuse ou brûlée peut
réutiliser les mêmes données de base et modifier uniquement certains paramètres ou masques, à condition que la
provenance et l’autorité de chaque variation soient explicites.
> **[LECTURE] Contrat de matériau — Ne pas saisir.**
```yaml
material:
  id: AST-MAT-STONE-SLATE-001
  version: 1
  family: stone
  physical_scale_m: [2.0, 2.0]
  workflow: metallic_roughness
  channels:
    base_color: AST-TEX-SLATE-BASE-001
    normal: AST-TEX-SLATE-NRM-001
    roughness: AST-TEX-SLATE-RGH-001
    ao: AST-TEX-SLATE-AO-001
  color_space:
    base_color: srgb
    normal: linear_data
    roughness: linear_data
    ao: linear_data
  usage: [architecture, props]
  status: draft
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identité :** `id` et `version` permettent de relier sources, exports et captures.
- **Échelle :** `physical_scale_m` indique la surface réelle couverte par un cycle de texture.
- **Canaux :** chaque image possède un rôle unique et traçable.
- **Espaces :** les couleurs d’affichage et les données numériques ne suivent pas la même conversion.
## 7. Le modèle metallic-roughness
Le pipeline de référence utilise le modèle metallic-roughness de glTF et des matériaux PBR de Godot. Le base color
décrit la couleur diffuse d’un diélectrique ou la réflectance colorée d’un métal. Le canal metallic indique la nature
conductrice. La roughness contrôle l’étalement des reflets. La normal map perturbe la direction apparente de la
surface.
Ce modèle ne transforme pas automatiquement une image en matière crédible. Les canaux doivent rester cohérents entre
eux. Une rayure profonde visible dans la normale mais absente de la roughness, ou une zone métallique peinte comme un
diélectrique sans transition, produit une lecture contradictoire.
> **[LECTURE] Résumé du workflow — Ne pas saisir.**
```yaml
metallic_roughness:
  base_color:
    meaning: visible_reflectance_or_diffuse_color
    color_space: srgb
  metallic:
    meaning: conductor_fraction
    color_space: linear_data
  roughness:
    meaning: microfacet_spread
    color_space: linear_data
  normal:
    meaning: tangent_space_direction_perturbation
    color_space: linear_data
  occlusion:
    meaning: local_indirect_light_attenuation
    color_space: linear_data
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Base color :** la carte représente une couleur perceptuelle et utilise sRGB.
- **Données :** metallic, roughness, normal et occlusion représentent des nombres, pas des couleurs d’affichage.
- **Cohérence :** les canaux décrivent la même matière et doivent être revus ensemble.
- **Limite :** les valeurs artistiques restent à qualifier sous la scène de référence.
## 8. Base color et albedo
La base color doit éviter les ombres peintes, les reflets photographiques et les variations d’exposition provenant de
la source. Ces informations appartiennent à l’éclairage ou aux autres canaux. Une légère variation de couleur peut
décrire le matériau, mais elle ne doit pas figer une direction lumineuse.
Pour les métaux, la base color décrit la couleur de réflexion. Pour les diélectriques, elle décrit la couleur diffuse.
Le terme albedo est souvent employé de manière générale ; le contrat du projet utilise `base_color` pour rester aligné
sur glTF et Godot.
> **[LECTURE] Contrat base color et albedo — Ne pas saisir.**
```yaml
base_color:
  source: de_lit_or_authored
  baked_lighting: forbidden
  captured_specular: forbidden
  alpha_usage: explicit_only
  color_space: srgb
  validation: neutral_and_warm_light
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 9. Metallic
Le canal metallic n’est pas un réglage de brillance. Il distingue principalement métal et non-métal. Les matières
composites ou peintes utilisent des transitions liées à une cause : peinture écaillée, oxydation, poussière ou
assemblage de plusieurs matériaux.
Un gris intermédiaire généralisé crée souvent une matière physiquement ambiguë. Il peut être légitime sur des pixels
de transition filtrés, mais la source doit rester principalement binaire lorsque la surface représente des zones
matérielles distinctes.
> **[LECTURE] Contrat metallic — Ne pas saisir.**
```yaml
metallic:
  default_dielectric: 0.0
  default_metal: 1.0
  broad_mid_gray: review_required
  transition_causes: [paint_edge, contamination, filtering]
  color_space: linear_data
  validation: reflection_response
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 10. Roughness
La roughness contrôle la largeur et la netteté des reflets. Une surface très rugueuse diffuse le reflet sur une zone
large ; une surface peu rugueuse conserve un reflet plus net. Elle ne décrit pas directement la force d’une lumière ni
la couleur du matériau.
La carte doit suivre les causes microscopiques : polissage, usure, graisse, poussière, humidité, rayure ou porosité.
Une simple copie en niveaux de gris de la base color crée une corrélation arbitraire entre couleur et microstructure.
> **[LECTURE] Contrat roughness — Ne pas saisir.**
```yaml
roughness:
  source: authored_from_surface_causes
  inverted_gloss: only_if_documented
  copied_from_base_color: forbidden
  wet_variant: separate_profile_or_mask
  color_space: linear_data
  grazing_angle_review: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 11. Normal map
La normal map de référence est une carte tangentielle. Ses composantes représentent une direction, pas une couleur.
Elle doit être importée comme donnée linéaire et marquée comme normal map afin que la compression et l’interprétation
soient adaptées.
Les détails de grande amplitude ne doivent pas être cachés dans une normal map. Silhouette, chanfreins importants,
joints profonds et déformations visibles en vue rasante restent des décisions géométriques ou de height/displacement
selon le cas.
> **[LECTURE] Contrat normal map — Ne pas saisir.**
```yaml
normal_map:
  space: tangent
  handedness: project_contract
  color_space: linear_data
  compression_profile: normal_rg_candidate
  strength: measured_per_material
  silhouette_changes: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 12. Ambient occlusion
L’ambient occlusion représente une atténuation locale de l’éclairage indirect dans des creux proches. Elle ne doit pas
contenir une ombre directionnelle, une ombre portée de grande taille ou une salissure permanente sans cause.
L’AO peut être packée avec roughness et metallic selon le contrat ORM. Le chapitre 17 traite son baking. Ici, la
responsabilité porte sur son interprétation, son canal, sa résolution et son intégration dans le matériau.
> **[LECTURE] Contrat ambient occlusion — Ne pas saisir.**
```yaml
ambient_occlusion:
  meaning: local_indirect_attenuation
  directional_shadow: forbidden
  large_scale_lighting: forbidden
  packing_channel: red_if_orm
  color_space: linear_data
  bake_authority: chapter_17
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 13. Height et déplacement
Une height map encode une hauteur relative. Elle peut servir au parallax, à un déplacement réel ou à des opérations de
production, mais ces usages n’ont pas le même coût ni les mêmes limites. Le contrat indique toujours l’interprétation
attendue.
La plage de hauteur doit être liée à une unité ou à une amplitude mesurable. Sans ce lien, deux matériaux utilisant le
même gris moyen peuvent produire des reliefs incompatibles. Le chapitre ne promet pas que le déplacement Blender est
exporté automatiquement vers Godot.
> **[LECTURE] Contrat height et déplacement — Ne pas saisir.**
```yaml
height:
  reference_level: 0.5
  physical_range_mm: pending_measurement
  usages: [authoring, parallax_candidate]
  geometry_displacement_export: not_assumed
  color_space: linear_data
  bake_authority: chapter_17
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 14. Emissive
L’emissive décrit une contribution lumineuse apparente de la surface. Elle ne garantit pas qu’une lumière dynamique
éclaire réellement l’environnement. L’effet visuel, le bloom et une éventuelle source lumineuse restent des
responsabilités séparées.
La carte emissive peut utiliser une couleur sRGB lorsqu’elle représente une couleur visible. Son intensité est un
paramètre matériel ou de scène. Une capture doit indiquer l’exposition, car un réglage d’exposition peut masquer une
intensité excessive.
> **[LECTURE] Contrat emissive — Ne pas saisir.**
```yaml
emissive:
  texture_color_space: srgb
  intensity: pending_measurement
  dynamic_light_source: separate_node_if_required
  bloom_dependency: documented
  exposure_locked_for_comparison: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 15. Opacity, transmission et subsurface
L’opacité, la transmission et la diffusion sous-surface ne sont pas des variantes interchangeables. Une feuille
découpée, un verre transmissif, une peau et une fumée ont des mécanismes et des coûts différents.
Le mode alpha est choisi à partir du besoin réel. L’alpha scissor convient souvent aux découpes nettes, tandis que
l’alpha blend est réservé aux transitions réellement semi-transparentes. Les faces doubles, ombres et profondeur
doivent être testées ensemble.
> **[LECTURE] Contrat opacity, transmission et subsurface — Ne pas saisir.**
```yaml
surface_modes:
  cutout_foliage: alpha_scissor_candidate
  glass: transmission_or_transparency_profile
  skin: subsurface_profile
  smoke: vfx_authority
  double_sided: review_required
  sorting_and_overdraw_test: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Rôle :** les champs séparent l’interprétation du canal de son réglage artistique.
- **Espace :** les cartes de données restent linéaires tandis que les couleurs visibles utilisent sRGB lorsque précisé.
- **Validation :** les décisions restent liées à une scène ou une revue identifiable.
- **Frontière :** le baking ou le système VFX est laissé au chapitre propriétaire lorsqu’il est mentionné.
## 16. Espaces colorimétriques
Une texture sRGB est décodée pour retrouver une valeur lumineuse linéaire avant les calculs de rendu. Cette conversion
est adaptée aux couleurs destinées à être vues. Elle est incorrecte pour une roughness, une normal map ou un masque,
car elle déforme les nombres stockés.
Le contrat ne se limite pas à l’extension du fichier. Deux PNG identiques peuvent avoir des rôles différents. L’espace
colorimétrique est donc défini par l’usage du canal et vérifié dans l’outil de destination.
> **[LECTURE] Table des espaces — Ne pas saisir.**
```yaml
color_space_policy:
  srgb:
    - base_color
    - emissive_color
  linear_data:
    - metallic
    - roughness
    - normal
    - ambient_occlusion
    - height
    - masks
  review_required:
    - packed_textures_with_mixed_semantics
    - scanned_images_with_embedded_lighting
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **sRGB :** la conversion s’applique aux couleurs perceptuelles.
- **Linéaire :** les cartes de données conservent leurs valeurs numériques.
- **Pack :** un fichier regroupant plusieurs données doit être traité comme données et non comme couleur.
- **Scan :** une image photographique doit être dé-éclairée ou qualifiée avant usage.
## 17. Formats d’image et précision
Le format source doit conserver la précision nécessaire aux opérations de production. Un fichier de travail peut
utiliser une précision supérieure à la livraison finale. Les fichiers livrés sont choisis selon HDR, alpha, nombre de
canaux, compatibilité d’import et coût.
PNG convient aux textures SDR sans perte à huit bits par canal. OpenEXR convient aux données HDR ou à certaines
sources de production à haute précision. JPEG introduit une compression destructive et n’a pas d’alpha ; il est
généralement évité pour normales, masques et données critiques.
> **[LECTURE] Profils de formats — Ne pas saisir.**
```yaml
formats:
  png_8bit:
    uses: [base_color_sdr, masks, normal_delivery]
    alpha: supported
    hdr: false
  exr:
    uses: [hdr_source, high_precision_intermediate]
    alpha: supported
    hdr: true
  jpeg:
    uses: [reference_only, noncritical_preview]
    alpha: false
    data_maps: forbidden
  godot_imported:
    location: res://.godot/imported/
    access: ResourceLoader_only
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** le format de travail peut conserver plus de précision que le format livré.
- **JPEG :** la compression destructive est réservée aux références ou aperçus non critiques.
- **Import :** les ressources transformées par Godot sont chargées par `ResourceLoader`, pas par accès direct au cache.
- **Limite :** le profil final dépend de la plateforme et doit être mesuré.
## 18. Résolution et mémoire
La résolution est un budget, pas un label de qualité. Une texture 4096² contient quatre fois plus de pixels qu’une
texture 2048². Le coût brut dépend du nombre de canaux et de bits par canal, puis les mipmaps et la compression
modifient le coût réel.
Le projet conserve la résolution source et une limite d’import séparées. Cette séparation permet de réduire le coût
d’une plateforme sans détruire la source canonique. Les textures qui occupent peu de pixels à l’écran ne reçoivent pas
automatiquement la plus grande résolution.
> **[LECTURE] Estimation mémoire non compressée — Ne pas saisir.**
```text
pixels = width × height
bytes_base = pixels × channels × bytes_per_channel
bytes_with_full_mip_chain ≈ bytes_base × 4 / 3

Exemple pédagogique, sans compression :
2048 × 2048 × 4 × 1 octet ≈ 16 MiB pour le niveau principal
chaîne complète de mipmaps ≈ 21,33 MiB
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Calcul :** la surface en pixels est multipliée par le nombre de canaux et la taille d’un canal.
- **Mipmaps :** une chaîne complète ajoute approximativement un tiers au niveau principal.
- **Compression :** ce calcul est un plafond pédagogique et non la mesure finale en VRAM.
- **Mesure :** le format GPU réel et les outils de profilage restent l’autorité.
> **[LECTURE] Profil de résolution — Ne pas saisir.**
```yaml
texture_profile:
  id: AST-TEX-PROFILE-WORLD-001
  source_resolution: authoring_dependent
  import_limits:
    desktop_reference: pending
    reduced_quality: pending
  screen_coverage_gate: required
  texel_density_gate: required
  memory_measurement: pending
  source_preserved: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** la résolution d’auteur n’est pas détruite par les limites d’import.
- **Profils :** chaque qualité peut appliquer une limite différente.
- **Portes :** couverture écran et densité de texels justifient la résolution.
- **Statut :** aucun nombre définitif n’est inventé avant mesure.
## 19. Mipmaps
Les mipmaps sont des versions réduites d’une texture utilisées lorsque la surface occupe moins de pixels à l’écran.
Elles réduisent le scintillement et le bruit à distance et peuvent améliorer l’efficacité d’échantillonnage. Elles
augmentent cependant la mémoire.
Les textures 3D bénéficient généralement de mipmaps. Les exceptions doivent être justifiées, par exemple une texture
de données utilisée d’une manière qui exige un contrôle spécifique. Le filtre et l’anisotropie influencent ensuite la
manière dont les niveaux sont lus.
> **[LECTURE] Politique de mipmaps — Ne pas saisir.**
```yaml
mipmap_policy:
  world_materials:
    generate: true
    review: grazing_surfaces
  normal_maps:
    generate: true
    roughness_filtering: candidate
  masks:
    generate: usage_dependent
  ui_assets:
    authority: ui_chapter
  memory_cost:
    approximation: plus_33_percent
  disable_without_reason: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Monde 3D :** les surfaces observées à distance utilisent une chaîne de mipmaps.
- **Rugosité :** un filtrage lié à la normale peut réduire certains scintillements spéculaires.
- **Masques :** la décision dépend de la manière dont le masque est échantillonné.
- **Coût :** l’augmentation de mémoire est incluse dans le budget.
## 20. Compression GPU
Godot distingue notamment les modes sans perte, avec perte, compressé VRAM, non compressé VRAM et Basis Universal.
Pour les textures 3D, la compression VRAM constitue généralement le point de départ, mais la qualité doit être revue
par type de canal.
La compression réduit la mémoire et la bande passante mais introduit des artefacts. Les normales, gradients doux,
alpha fin et masques étroits sont particulièrement sensibles. Un profil n’est accepté qu’après comparaison visuelle et
mesure.
> **[LECTURE] Profils de compression — Ne pas saisir.**
```yaml
compression_profiles:
  color_opaque:
    mode: VRAM_Compressed_candidate
    high_quality: platform_review
  normal:
    mode: VRAM_Compressed
    normal_map: enabled
  masks:
    mode: VRAM_Compressed_candidate
    channel_pack: optimized_if_semantics_allow
  hdr_environment:
    mode: hdr_profile_review
  source_files:
    destructive_recompression: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Candidats :** les modes proposés sont des points de départ, pas des résultats qualifiés.
- **Normale :** le profil active l’interprétation adaptée aux cartes de normales.
- **Masques :** le packing et la compression dépendent des canaux réellement utilisés.
- **Source :** la compression de livraison ne remplace pas les fichiers canoniques.
## 21. Compression des normales
Une normal map tangentielle utilise surtout les composantes X et Y ; la composante Z peut être reconstruite. Les
formats à deux canaux peuvent préserver ces données mieux qu’une compression couleur générale, selon la plateforme et
le moteur.
Le projet ne force pas un format GPU dans les sources. Il qualifie la texture comme normal map et laisse l’import
produire la ressource adaptée. Les artefacts sont contrôlés sur une sphère lisse, une surface à angle rasant et un
asset aux UV représentatifs.
> **[LECTURE] Contrôle d’import d’une normale — Ne pas saisir.**
```yaml
normal_import:
  semantic: tangent_normal
  color_space: linear_data
  compression:
    mode: VRAM_Compressed
    normal_map: enabled
  mipmaps:
    generate: true
  source_normal:
    path: res://assets/materials/slate/slate_nrm.png
  visual_checks:
    - smooth_sphere
    - grazing_plane
    - representative_asset
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Sémantique :** la texture est déclarée comme normale tangentielle.
- **Compression :** le moteur peut choisir une représentation adaptée aux canaux de direction.
- **Mipmaps :** la carte reste stable à distance sous réserve de revue.
- **Contrôles :** plusieurs géométries révèlent coutures, blocs et inversions.
## 22. Packing ORM
Le packing ORM regroupe ambient occlusion, roughness et metallic dans les canaux rouge, vert et bleu. Il réduit le
nombre d’échantillonnages et de fichiers, mais exige un contrat strict. Une inversion de canal produit un matériau
visuellement plausible dans certaines vues tout en étant techniquement faux.
Le packing ne doit pas mélanger une couleur sRGB et des données linéaires. Le fichier ORM est une texture de données.
Sa résolution doit être justifiée par le canal le plus exigeant, et non automatiquement copiée depuis la base color.
> **[LECTURE] Contrat ORM — Ne pas saisir.**
```yaml
orm_texture:
  id: AST-TEX-SLATE-ORM-001
  color_space: linear_data
  channels:
    r: ambient_occlusion
    g: roughness
    b: metallic
    a: unused
  resolution: profile_driven
  defaults:
    ambient_occlusion: 1.0
    roughness: material_default
    metallic: 0.0
  validation: channel_preview_required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Canaux :** l’ordre rouge-vert-bleu est explicite et aligné sur le contrat ORM.
- **Valeurs par défaut :** un canal absent reçoit une valeur documentée au lieu de données indéfinies.
- **Résolution :** le profil répond aux besoins des canaux packés.
- **Validation :** chaque canal est visualisé séparément avant intégration.
## 23. Densité de texels
La densité de texels relie le nombre de pixels à une distance réelle sur le modèle. Elle permet à des assets voisins
d’afficher un niveau de détail comparable. Une résolution identique ne garantit pas une densité identique, car la
surface UV et la taille physique varient.
Le projet définit des classes de densité par usage et distance de caméra. Les visages, objets en première personne,
architecture lointaine et terrains n’ont pas les mêmes besoins. Les valeurs restent candidates jusqu’à des captures
comparatives.
> **[LECTURE] Calcul de densité — Ne pas saisir.**
```text
densité_px_par_m = longueur_uv_en_pixels / longueur_réelle_en_mètres

Exemple de mesure :
- segment réel : 2 m
- segment correspondant dans la texture : 1024 px
- densité observée : 512 px/m

La valeur n'est acceptable qu'après comparaison à la classe d'usage.
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Entrées :** la mesure utilise une longueur réelle et sa projection dans l’espace texture.
- **Unité :** le résultat en pixels par mètre permet des comparaisons inter-assets.
- **Classe :** la cible dépend de l’usage, de la caméra et de la plateforme.
- **Limite :** une densité uniforme ne remplace pas la hiérarchie visuelle.
> **[LECTURE] Manifeste de densité — Ne pas saisir.**
```yaml
texel_density:
  classes:
    hero_closeup: pending_measurement
    first_person_prop: pending_measurement
    character_body: pending_measurement
    architecture_standard: pending_measurement
    background_large: pending_measurement
  exceptions:
    require_reason: true
    require_capture: true
    require_owner: true
  validation_scene: AST-MAT-LAB-PBR-001
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Classes :** les usages sont séparés au lieu d’une valeur universelle.
- **Exceptions :** tout écart possède une raison, une capture et un responsable.
- **Scène :** la comparaison se déroule dans le laboratoire commun.
- **Statut :** les nombres sont laissés en attente tant qu’aucune campagne n’est réalisée.
## 24. Familles de matériaux maîtres
Une bibliothèque robuste contient peu de familles maîtres : pierre, bois, métal peint, métal nu, tissu, peau, verre,
sol et végétation peuvent partager des structures tout en conservant des paramètres et variantes spécifiques.
Un matériau maître ne doit pas devenir un graphe universel avec toutes les options activées. Chaque fonctionnalité a
un coût de maintenance et parfois un coût runtime. Les familles restent spécialisées et les variantes désactivent les
fonctions inutiles.
> **[LECTURE] Famille de matériau — Ne pas saisir.**
```yaml
material_family:
  id: AST-MAT-FAMILY-PAINTED-METAL-001
  shader_model: metallic_roughness
  required_channels: [base_color, roughness, metallic, normal]
  optional_channels: [ao, detail_mask, emissive]
  variants:
    - clean
    - worn
    - wet
  forbidden_defaults:
    - transparency
    - subsurface
    - refraction
  owner: lookdev
  status: draft
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Requis :** les canaux indispensables définissent le contrat minimal.
- **Optionnel :** les fonctions supplémentaires ne sont activées que par besoin.
- **Variantes :** les états partagent la famille au lieu de dupliquer le matériau complet.
- **Interdits :** les fonctionnalités coûteuses ou incohérentes ne sont pas activées par défaut.
## 25. Matériaux tilables
Un matériau tilable couvre une grande surface par répétition. Il convient aux murs, sols, roches ou terrains lorsque
le motif peut se répéter sans couture visible. Son échelle physique est une donnée obligatoire.
La répétition est combattue par une combinaison mesurée : variations de teinte faibles, détails secondaires, masques
de macro-variation, décals et rupture géométrique. Une accumulation aléatoire de bruit dégrade la lecture et empêche
le diagnostic.
> **[LECTURE] Contrat tilable — Ne pas saisir.**
```yaml
tiling_material:
  id: AST-MAT-WALL-PLASTER-001
  tile_size_m: [2.0, 2.0]
  seamless_edges: required
  macro_variation:
    scale_m: pending
    amplitude: pending
  detail_normal:
    scale_m: pending
    strength: pending
  decals:
    allowed_causes: [repair, moisture_edge, impact]
  repetition_review: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Échelle :** la taille du cycle est exprimée en mètres.
- **Macro :** les variations larges sont séparées du motif de détail.
- **Décals :** les ajouts locaux répondent à une cause lisible.
- **Revue :** la répétition est contrôlée à plusieurs distances.
## 26. Trim sheets
Une trim sheet rassemble des bandes réutilisables : arêtes, cadres, moulures, tôles, câbles ou profils. Elle permet à
plusieurs modèles de partager une texture et une densité cohérente. Elle exige cependant une nomenclature et une mise
en page stables.
Le chapitre définit la bibliothèque et ses contrats. Le placement précis des UV sur les bandes relève du chapitre 17.
Une modification de la largeur ou du sens d’une bande publiée implique une nouvelle version et une revue des
consommateurs.
> **[LECTURE] Plan de trim sheet — Ne pas saisir.**
```yaml
trim_sheet:
  id: AST-TRIM-INDUSTRIAL-001
  version: 1
  physical_width_m: 4.0
  rows:
    - id: edge_narrow
      height_ratio: 0.0625
      intended_width_m: pending
    - id: frame_medium
      height_ratio: 0.125
      intended_width_m: pending
    - id: panel_large
      height_ratio: 0.25
      intended_width_m: pending
  uv_assignment_authority: chapter_17
  consumer_manifest: required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Version :** la disposition est immuable pour les consommateurs d’une version donnée.
- **Ratios :** les bandes sont décrites sans inventer leurs dimensions finales.
- **Autorité UV :** le chapitre 17 réalise l’affectation précise.
- **Manifest :** les assets consommateurs sont identifiés pour toute migration.
## 27. Atlas
Un atlas regroupe plusieurs éléments dans une même image. Il peut réduire les changements de matériau, mais il lie la
résolution, la compression et les mipmaps de contenus différents. Un atlas mal conçu gaspille de l’espace ou provoque
des fuites entre îlots.
Les atlas sont organisés par famille d’usage et par profil de rendu. Les éléments à transparence, les petits
accessoires et les variantes de couleur ne sont pas mélangés automatiquement. Les marges et le baking restent au
chapitre 17.
> **[LECTURE] Contrat d’atlas — Ne pas saisir.**
```yaml
atlas:
  id: AST-ATLAS-PROPS-SMALL-001
  family: small_props
  channels: [base_color, normal, orm]
  shared_resolution: pending
  consumers: manifest_required
  alpha_mode: opaque_by_default
  mip_safe_padding: chapter_17
  mixed_texel_density: review_required
  versioned_layout: true
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Famille :** les contenus regroupés partagent un usage et un profil de rendu.
- **Canaux :** les textures correspondantes utilisent la même disposition.
- **Marges :** la sécurité des mipmaps est préparée par le chapitre 17.
- **Version :** un changement de disposition produit une nouvelle version.
## 28. Détails, masques et décalcomanies
Les détails locaux permettent de réutiliser une base tout en ajoutant une information causale : numéro peint,
réparation, humidité, impact, salissure ou joint. Ils ne doivent pas transformer chaque surface en accumulation
d’effets.
Un masque indique où une variation s’applique. Une décalcomanie projette ou applique un détail local. Le choix dépend
de la répétition, de la profondeur, du coût et de la nécessité de partager la donnée entre plusieurs matériaux.
> **[LECTURE] Politique de détails — Ne pas saisir.**
```yaml
detail_policy:
  reusable_detail_normal:
    use: micro_surface
    scale_contract: required
  masks:
    use: controlled_variants
    color_space: linear_data
  decals:
    use: localized_causal_marks
    stacking_limit: pending_measurement
  vertex_color:
    use: low_frequency_blends
    mesh_contract: required
  random_grunge:
    default: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Détail :** la micro-surface possède une échelle indépendante.
- **Masques :** les variations sont contrôlées et traitées comme données.
- **Décals :** les marques locales sont limitées et justifiées.
- **Refus :** le bruit aléatoire n’est pas une solution par défaut.
## 29. Sources Blender et données livrées
Le fichier Blender conserve les nœuds, images de travail et paramètres nécessaires à la reprise. Les textures livrées
sont placées dans une arborescence stable, avec des noms décrivant l’identité et le canal. Les caches, aperçus
temporaires et chemins personnels restent hors du contrat.
Les matériaux Blender servent au lookdev et à la comparaison. Ils ne sont pas la source autoritaire du matériau
runtime. L’export glTF transporte un sous-ensemble compatible ; les réglages spécifiques de Godot sont versionnés côté
projet.
> **[LECTURE] Arborescence matérielle — Ne pas saisir.**
```text
assets/materials/slate/
├── source/
│   ├── AST-MAT-STONE-SLATE-001.blend
│   └── scans_and_workfiles/
├── textures/
│   ├── AST-TEX-SLATE-BASE-001.png
│   ├── AST-TEX-SLATE-NRM-001.png
│   └── AST-TEX-SLATE-ORM-001.png
├── manifests/
│   ├── material.yaml
│   └── provenance.yaml
└── previews/
    └── non_authoritative/
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Source :** le `.blend` et les fichiers de travail restent distincts des textures livrées.
- **Textures :** les noms relient identité et rôle de canal.
- **Manifestes :** les contrats et la provenance accompagnent les données.
- **Aperçus :** les images de présentation sont explicitement non autoritaires.
## 30. Principled BSDF de contrôle dans Blender
Le Principled BSDF fournit un modèle de contrôle proche du workflow metallic-roughness. Les images sont connectées
selon leur rôle, avec les cartes de données configurées en non-color data. La normal map passe par un nœud dédié avant
l’entrée Normal.
Le graphe reste volontairement lisible. Les fonctions spécifiques non transportées par glTF sont documentées
séparément. Un rendu Blender cohérent ne prouve pas que l’import Godot produira la même image, car l’éclairage, le
tone mapping, la compression et l’implémentation diffèrent.
> **[LECTURE] Pseudo-script Blender de branchement — Ne pas saisir.**
```python
def connect_pbr(material, images):
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    base = load_image_node(images["base_color"], color_space="sRGB")
    rough = load_image_node(images["roughness"], color_space="Non-Color")
    metal = load_image_node(images["metallic"], color_space="Non-Color")
    normal = load_image_node(images["normal"], color_space="Non-Color")
    normal_map = material.node_tree.nodes.new("ShaderNodeNormalMap")

    link(base.outputs["Color"], bsdf.inputs["Base Color"])
    link(rough.outputs["Color"], bsdf.inputs["Roughness"])
    link(metal.outputs["Color"], bsdf.inputs["Metallic"])
    link(normal.outputs["Color"], normal_map.inputs["Color"])
    link(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Entrées :** `material` reçoit le matériau cible et `images` associe chaque rôle à un chemin.
- **Espaces :** la base color utilise sRGB tandis que roughness, metallic et normal restent non-color.
- **Normal :** le nœud `ShaderNodeNormalMap` convertit la couleur encodée en direction.
- **Limite :** les fonctions auxiliaires sont conceptuelles et le script n’a pas été exécuté.
## 31. Nommage et inventaire des textures
Le nom d’une texture indique l’identité stable, la famille et le rôle. Il ne contient pas un chemin personnel, une
date arbitraire ou un terme ambigu comme `final_final`. La version appartient au manifeste ou au système de
versionnement.
Un inventaire central permet de retrouver les consommateurs, les profils d’import, les résolutions et les licences. Il
évite de considérer deux fichiers visuellement proches comme interchangeables.
> **[LECTURE] Inventaire JSON — Ne pas saisir.**
```json
{
  "schema_version": 1,
  "textures": [
    {
      "id": "AST-TEX-SLATE-BASE-001",
      "path": "res://assets/materials/slate/slate_base.png",
      "semantic": "base_color",
      "color_space": "srgb",
      "material_ids": ["AST-MAT-STONE-SLATE-001"],
      "import_profile": "AST-IMPORT-COLOR-3D-001",
      "status": "draft"
    }
  ]
}
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Schéma :** la version permet de faire évoluer l’inventaire.
- **Sémantique :** le rôle du fichier est indépendant de son extension.
- **Consommateurs :** les matériaux liés sont listés.
- **Import :** le profil attendu peut être contrôlé automatiquement.
## 32. Export glTF et limites
glTF 2.0 définit un workflow PBR metallic-roughness et peut transporter des textures liées au matériau. Le conteneur
GLB regroupe scène et données binaires, mais les textures peuvent aussi rester externes selon le pipeline. Le choix
doit être stable et documenté.
Les extensions et fonctions avancées ne sont pas supposées disponibles partout. Le pipeline de référence privilégie le
noyau compatible, puis reconstitue dans Godot les réglages qui ne doivent pas être autoritaires dans Blender.
> **[LECTURE] Preset d’export matériel — Ne pas saisir.**
```yaml
gltf_export:
  container: GLB
  workflow: metallic_roughness
  materials: export
  images:
    mode: project_contract
    destructive_recompression: false
  supported_core:
    - base_color
    - metallic_roughness
    - normal
    - occlusion
    - emissive
  unsupported_or_extended:
    action: document_and_rebuild_in_godot
  validation: reimport_required
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Noyau :** les canaux standards constituent la base d’échange.
- **Images :** la recompression destructive n’est pas ajoutée silencieusement.
- **Extensions :** toute fonction non garantie est reconstruite et documentée côté Godot.
- **Validation :** un export n’est accepté qu’après réimport.
## 33. Import des images dans Godot
Godot importe automatiquement les images placées dans le projet et crée des ressources internes sous
`.godot/imported`. Le code charge la ressource source par son chemin `res://` avec `ResourceLoader`; il ne dépend pas
du nom interne généré.
Le dock Import configure compression, mipmaps, taille limite, normal map et autres options. Les profils sont appliqués
par sémantique. Une image utilisée en 3D peut être détectée et réimportée avec des réglages adaptés, mais le projet
conserve des presets explicites afin d’éviter les surprises.
> **[LECTURE] Profil d’import conceptuel — Ne pas saisir.**
```yaml
godot_import_profile:
  id: AST-IMPORT-COLOR-3D-001
  semantic: base_color
  compression:
    mode: VRAM_Compressed
    high_quality: platform_review
  mipmaps:
    generate: true
  process:
    size_limit: profile_value
  color_space: srgb
  repeat: material_property
  filter: material_property
  validation: reimport_and_compare
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Sémantique :** le profil est choisi par rôle de texture.
- **Compression :** la valeur initiale reste soumise à une revue plateforme.
- **Répétition :** en 3D, repeat et filter appartiennent au matériau ou au sampler.
- **Comparaison :** toute réimportation est contrôlée dans le laboratoire.
## 34. StandardMaterial3D
`StandardMaterial3D` expose les propriétés courantes du rendu 3D sans écrire de shader. Il convient lorsque le
matériau utilise des fonctions standards et qu’une ressource claire est préférable à un shader personnalisé.
Les textures sont affectées selon leur rôle. Les paramètres numériques restent versionnés dans une ressource ou un
manifeste. Le code suivant montre une construction conceptuelle et ne remplace pas la création de ressources `.tres`
contrôlées dans l’éditeur.
> **[LECTURE] Construction conceptuelle d’un StandardMaterial3D — Ne pas saisir.**
```gdscript
func build_standard_material(
    base_color: Texture2D,
    normal: Texture2D,
    roughness: Texture2D,
    metallic: Texture2D
) -> StandardMaterial3D:
    var material := StandardMaterial3D.new()
    material.albedo_texture = base_color
    material.normal_enabled = true
    material.normal_texture = normal
    material.roughness_texture = roughness
    material.metallic_texture = metallic
    material.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC
    return material
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Paramètres :** quatre `Texture2D` représentent les canaux séparés.
- **Retour :** la fonction retourne un `StandardMaterial3D` nouvellement configuré.
- **Normal :** `normal_enabled` active l’interprétation de la carte.
- **Filtre :** l’anisotropie est un candidat pertinent pour les surfaces vues en angle rasant.
## 35. ORMMaterial3D
`ORMMaterial3D` regroupe les canaux ambient occlusion, roughness et metallic dans une texture ORM. Il réduit le nombre
de textures liées et rend le contrat de packing explicite.
Le matériau ne corrige pas un fichier packé dans le mauvais ordre. Le projet vérifie les canaux séparément avant de
construire la ressource. Les valeurs par défaut sont documentées lorsque l’un des canaux est uniforme.
> **[LECTURE] Construction conceptuelle d’un ORMMaterial3D — Ne pas saisir.**
```gdscript
func build_orm_material(
    base_color: Texture2D,
    normal: Texture2D,
    orm: Texture2D
) -> ORMMaterial3D:
    var material := ORMMaterial3D.new()
    material.albedo_texture = base_color
    material.normal_enabled = true
    material.normal_texture = normal
    material.orm_texture = orm
    material.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC
    return material
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Paramètres :** la texture `orm` porte les trois canaux de données.
- **Retour :** la fonction produit une ressource `ORMMaterial3D`.
- **Contrat :** l’ordre R=AO, G=roughness, B=metallic est validé avant l’appel.
- **Limite :** les propriétés exactes sont à confirmer dans la version de moteur réellement exécutée.
## 36. Filtre, répétition et anisotropie
Le filtre détermine comment les texels sont interpolés. Les variantes avec mipmaps réduisent le bruit à distance.
L’anisotropie améliore les surfaces observées sous un angle très oblique, comme un sol ou une route, avec un coût
supplémentaire.
La répétition doit être activée pour les matériaux tilables et désactivée lorsque les UV doivent rester bornés. Le
choix appartient au matériau, pas à un nom de fichier implicite.
> **[LECTURE] Profil de sampler — Ne pas saisir.**
```yaml
sampler_profiles:
  world_tiling:
    filter: linear_with_mipmaps_anisotropic
    repeat: enabled
    anisotropy_level: project_setting_candidate
  unique_atlas:
    filter: linear_with_mipmaps
    repeat: disabled
  pixel_art:
    authority: ui_or_style_specific
  validation:
    angles_deg: [0, 30, 60, 80]
    distances: measured_route
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Tilable :** les surfaces répétées utilisent mipmaps et anisotropie.
- **Atlas :** la répétition est désactivée pour éviter de lire un autre îlot.
- **Niveau :** l’anisotropie globale reste à mesurer.
- **Validation :** plusieurs angles et distances révèlent les défauts de filtrage.
## 37. Scène d’éclairage de référence
La scène de référence isole le matériau de la mise en scène. Elle fixe l’exposition, la caméra, le fond et la
géométrie. Chaque environnement possède une intention : neutre pour comparer les couleurs, chaud et froid pour tester
la stabilité, contrasté pour lire les reflets et les normales.
Une même capture est répétée pour chaque profil d’import. Les réglages ne sont pas ajustés entre deux matériaux afin
de les avantager. Les lumières de production peuvent ensuite être testées dans une seconde étape.
> **[LECTURE] Arbre de scène — Ne pas saisir.**
```text
AST-MAT-LAB-PBR-001
├── WorldEnvironment
├── CameraRig
│   ├── CameraClose
│   ├── CameraMedium
│   └── CameraGrazing
├── LightingProfiles
│   ├── Neutral
│   ├── Warm
│   ├── Cool
│   └── HighContrast
├── Calibration
│   ├── GraySphere
│   ├── MetalSphere
│   └── RoughnessRamp
└── MaterialProbes
    ├── SmoothSphere
    ├── FacetedSphere
    ├── PlanesAndCorner
    └── RepresentativeAsset
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Monde :** `WorldEnvironment` centralise l’environnement actif.
- **Caméras :** les cadrages verrouillés rendent les captures comparables.
- **Calibration :** les étalons vérifient l’éclairage avant d’accuser le matériau.
- **Sondes :** chaque forme cible une catégorie d’artefact.
## 38. Matrice d’éclairage
La matrice d’éclairage décrit les profils, pas leur beauté. La température perçue, la direction, la taille de source
et le contraste sont contrôlés. Une variation ne doit pas changer simultanément exposition, caméra et tone mapping.
Les valeurs numériques sont enregistrées seulement après création réelle de la scène. Le document conserve des
identifiants et des intentions sans inventer de lux, d’EV ou de température finale.
> **[LECTURE] Matrice comparative — Ne pas saisir.**
```csv
profile_id,intent,camera,exposure,environment,light_setup,status
neutral,color_and_roughness,locked,pending,neutral_hdr_or_procedural,pending,not_executed
warm,warm_stability,locked,pending,warm_profile,pending,not_executed
cool,cool_stability,locked,pending,cool_profile,pending,not_executed
high_contrast,specular_and_normal,locked,pending,contrast_profile,pending,not_executed
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Colonnes :** chaque capture conserve intention, caméra, exposition et environnement.
- **Verrou :** la caméra ne change pas entre matériaux.
- **Valeurs :** les réglages restent `pending` jusqu’à la matérialisation.
- **Statut :** `not_executed` interdit toute conclusion visuelle.
## 39. Étalons et rampes
Les étalons évitent de confondre un problème global d’éclairage avec un problème local de matériau. Une sphère grise,
une sphère métallique et une rampe de roughness doivent répondre de façon stable avant toute comparaison d’asset.
Les étalons sont versionnés avec la scène. Leur matériau est minimal et ne partage pas les textures en cours
d’évaluation. Une modification d’environnement déclenche une nouvelle série de captures.
> **[LECTURE] Jeu d’étalons — Ne pas saisir.**
```yaml
calibration_set:
  id: AST-MAT-CALIBRATION-001
  gray_dielectric:
    base_color: controlled_gray
    metallic: 0.0
    roughness: controlled_mid
  metal_reference:
    base_color: controlled_metal_reflectance
    metallic: 1.0
    roughness: controlled_mid
  roughness_ramp:
    steps: fixed_count_candidate
    metallic: 0.0
  shared_textures_with_test_materials: forbidden
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Diélectrique :** la sphère grise contrôle la réponse diffuse.
- **Métal :** la référence métallique révèle le comportement des réflexions.
- **Rampe :** des pas fixes rendent la roughness lisible.
- **Indépendance :** les étalons ne dépendent pas des textures testées.
## 40. Captures comparatives
Une capture utile conserve le commit, la scène, la caméra, le profil d’éclairage, le matériau, le preset d’import, la
résolution de viewport et les réglages d’exposition. Sans ces champs, l’image ne peut pas être reproduite.
Les captures sont nommées par identifiants, pas par appréciation. Les commentaires artistiques sont enregistrés
séparément afin de ne pas modifier le nom de fichier à chaque revue.
> **[LECTURE] Manifeste de capture — Ne pas saisir.**
```yaml
capture:
  id: AST-CAP-MAT-SLATE-NEUTRAL-001
  commit: pending
  scene: AST-MAT-LAB-PBR-001
  camera: CameraGrazing
  lighting_profile: neutral
  material_id: AST-MAT-STONE-SLATE-001
  import_profile: AST-IMPORT-COLOR-3D-001
  viewport: pending
  exposure: pending
  result_path: pending
  status: not_executed
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identité :** la capture est une preuve versionnée.
- **Contexte :** caméra, lumière, matériau et import expliquent l’image.
- **Réglages :** viewport et exposition empêchent des comparaisons trompeuses.
- **Statut :** aucun fichier n’est annoncé avant exécution.
## 41. Budget de textures
Le budget associe résolution, format importé, mipmaps, nombre d’instances matérielles et importance à l’écran. Il ne
se limite pas au poids des PNG sur disque. La VRAM, la bande passante et le nombre de textures simultanément
résidentes doivent être mesurés.
Les budgets sont regroupés par scène et par plateforme. Un matériau rarement visible peut utiliser un profil différent
d’un matériau répété sur tout le monde. Toute exception possède une justification et une capture.
> **[LECTURE] Table de budget — Ne pas saisir.**
```csv
material_id,texture_id,semantic,source_resolution,import_limit,compression,mipmaps,estimated_vram,measured_vram,status
AST-MAT-STONE-SLATE-001,AST-TEX-SLATE-BASE-001,base_color,pending,pending,VRAM_candidate,true,pending,pending,not_executed
AST-MAT-STONE-SLATE-001,AST-TEX-SLATE-NRM-001,normal,pending,pending,normal_profile,true,pending,pending,not_executed
AST-MAT-STONE-SLATE-001,AST-TEX-SLATE-ORM-001,orm,pending,pending,VRAM_candidate,true,pending,pending,not_executed
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Sémantique :** chaque ligne identifie le rôle de la texture.
- **Estimation :** la valeur théorique est séparée de la mesure.
- **Compression :** le profil est enregistré pour expliquer la qualité.
- **Statut :** les champs restent en attente avant import et profilage.
## 42. Bibliothèque de matériaux
La bibliothèque référence des ressources et des manifestes ; elle ne copie pas les textures dans chaque asset. Les
consommateurs utilisent un identifiant stable et peuvent recevoir une variante contrôlée.
En Studio, le catalogue possède un propriétaire, une revue et une politique de dépréciation. En Solo, un simple
manifeste versionné suffit à condition de conserver les mêmes invariants.
> **[LECTURE] Catalogue de matériaux — Ne pas saisir.**
```json
{
  "schema_version": 1,
  "library_id": "AST-MAT-LIBRARY-001",
  "materials": [
    {
      "id": "AST-MAT-STONE-SLATE-001",
      "resource": "res://assets/materials/slate/slate.tres",
      "manifest": "res://assets/materials/slate/material.yaml",
      "families": ["stone", "world"],
      "status": "draft"
    }
  ],
  "deprecated_ids": []
}
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Bibliothèque :** un identifiant racine versionne l’ensemble.
- **Ressource :** le `.tres` runtime est séparé du manifeste de production.
- **Familles :** les recherches et profils peuvent regrouper les matériaux.
- **Dépréciation :** les anciens identifiants ne sont pas réutilisés silencieusement.
## 43. Validateur structurel Godot
Un validateur peut vérifier l’existence des ressources, la classe attendue, les textures obligatoires et l’identité
déclarée. Il ne juge pas la qualité artistique. Son rôle est de détecter les oublis reproductibles avant la revue
visuelle.
Le script doit retourner une liste de diagnostics structurés plutôt que d’arrêter l’éditeur sur la première anomalie.
Les codes restent stables afin que la CI et les rapports puissent les interpréter.
> **[LECTURE] Exemple de validateur — Ne pas saisir.**
```gdscript
class_name MaterialLibraryValidator
extends RefCounted

func validate_material(path: String) -> Array[Dictionary]:
    var diagnostics: Array[Dictionary] = []
    if not ResourceLoader.exists(path):
        diagnostics.append({
            "code": "MAT_RESOURCE_MISSING",
            "path": path,
            "severity": "error"
        })
        return diagnostics

    var resource := ResourceLoader.load(path)
    if not resource is BaseMaterial3D:
        diagnostics.append({
            "code": "MAT_WRONG_TYPE",
            "path": path,
            "severity": "error"
        })
        return diagnostics

    if resource.albedo_texture == null:
        diagnostics.append({
            "code": "MAT_BASE_COLOR_MISSING",
            "path": path,
            "severity": "warning"
        })
    return diagnostics
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Paramètre :** `path` est le chemin `res://` de la ressource à contrôler.
- **Retour :** la fonction retourne un tableau de dictionnaires de diagnostic.
- **Chargement :** `ResourceLoader.exists` évite un chargement inutile lorsque le chemin manque.
- **Limite :** la présence d’une texture ne prouve ni son espace colorimétrique ni sa qualité visuelle.
## 44. Campagne de comparaison
La campagne varie une seule dimension à la fois : profil de compression, limite de résolution, qualité de filtrage ou
variante de matériau. Les captures et mesures utilisent le même parcours et les mêmes caméras.
Le résultat conserve les défauts observés : blocs de compression, scintillement, perte de détail, coutures, reflets
incohérents, répétition ou surcoût mémoire. Une décision indique ce qui est accepté, rejeté ou à retester.
> **[LECTURE] Plan de campagne — Ne pas saisir.**
```yaml
campaign:
  id: AST-MAT-CAMPAIGN-001
  hardware:
    gpu: AMD_Radeon_RX_6750_XT_12GB
    cpu: Ryzen_7_2700
    ram_gb: 32
    os: Windows_11
  engine:
    godot: 4.7.1-stable
    renderer: Forward+
  variables:
    - compression_profile
    - import_size_limit
    - anisotropy_profile
  invariant:
    - scene
    - camera_route
    - exposure
    - material_version
  results: pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Matériel :** la plateforme de référence rend les résultats interprétables.
- **Variables :** une seule famille de réglages change par série.
- **Invariants :** la scène, la caméra, l’exposition et le matériau restent stables.
- **Résultats :** la campagne n’est pas annoncée comme exécutée.
> **[LECTURE] Table de résultats — Ne pas saisir.**
```csv
run_id,commit,material_id,lighting_profile,compression_profile,size_limit,anisotropy,cpu_ms,gpu_ms,vram_mb,visual_defects,decision
pending,pending,AST-MAT-STONE-SLATE-001,neutral,profile_a,pending,pending,pending,pending,pending,not_executed,pending
pending,pending,AST-MAT-STONE-SLATE-001,neutral,profile_b,pending,pending,pending,pending,pending,not_executed,pending
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Contexte :** la ligne relie commit, matériau et éclairage.
- **Performance :** CPU, GPU et VRAM sont séparés.
- **Visuel :** les défauts sont enregistrés avec les chiffres.
- **Décision :** aucune conclusion n’est inscrite avant exécution.
## 45. Sources techniques officielles
Les références de qualification sont la documentation stable de Godot sur l’import des images, les matériaux 3D et le
processus d’import, le manuel Blender sur le Principled BSDF et la gestion des couleurs, ainsi que la spécification
glTF 2.0.
Les pages `latest` de Godot peuvent décrire des fonctions non encore stabilisées. Pour une implémentation, le projet
vérifie la documentation correspondant à la version réellement utilisée. Les liens ci-dessous sont des points d’entrée
et ne remplacent pas la qualification de version.
- [Godot — Importing images](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html)
- [Godot — BaseMaterial3D](https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html)
- [Godot — Standard Material 3D and ORM Material 3D](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html)
- [Godot — Import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html)
- [Blender — Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html)
- [Blender — Color Management](https://docs.blender.org/manual/en/latest/render/color_management.html)
- [Khronos — glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
## 46. Modes Solo et Studio
### Mode Solo
Le parcours Solo commence par quatre familles réellement nécessaires au vertical slice, un profil de couleur, un
profil de données, une scène comparative et un tableau de budget. Il préfère des matériaux tilables réutilisables,
quelques trim sheets et un inventaire simple à une bibliothèque immense.
Chaque nouveau matériau doit résoudre un besoin visible. Une variante n’est ajoutée qu’après comparaison avec le
matériau existant et identification d’une différence qui ne peut pas être obtenue par un paramètre ou un masque
partagé.
### Mode Studio
Le parcours Studio sépare source, lookdev, intégration et validation. Les profils d’import sont gérés par plateforme,
les matériaux possèdent des propriétaires, les captures sont revues par lots et les dépréciations sont suivies par
manifeste.
Les spécialistes peuvent travailler en parallèle à condition que les identifiants, canaux, espaces colorimétriques,
échelles, densités et portes d’acceptation soient communs. Une revue croisée vérifie la cohérence entre Blender, glTF
et Godot.
## 47. Diagnostics et corrections
<!-- qa:error-correction-section -->
### 47.1 Importer toutes les cartes en sRGB
**Symptôme :** la roughness paraît trop contrastée, les masques changent de valeur et les normales produisent des bosses incohérentes.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
texture_import:
  base_color: srgb
  roughness: srgb
  metallic: srgb
  normal: srgb
  masks: srgb
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le réglage applique une courbe perceptuelle à des données numériques. Les valeurs de roughness, metallic, normale et masque ne correspondent plus à celles qui ont été produites.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
texture_import:
  base_color: srgb
  emissive_color: srgb
  roughness: linear_data
  metallic: linear_data
  normal: linear_data
  masks: linear_data
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Les couleurs visibles reçoivent la conversion sRGB tandis que les cartes de données conservent leurs nombres.
### 47.2 Copier la base color dans la roughness
**Symptôme :** les zones claires deviennent systématiquement rugueuses et les zones sombres brillantes, sans relation avec la matière.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
roughness_generation:
  source: base_color_grayscale
  inversion: none
  surface_causes: ignored
  status: accepted
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La luminosité de la couleur ne décrit pas la microstructure. Le procédé crée une corrélation arbitraire et masque les causes comme polissage, graisse ou poussière.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
roughness_generation:
  source: authored_or_measured_surface_response
  causes: [polish, wear, grease, dust, moisture]
  base_color_reference: visual_only
  validation: grazing_light_required
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La roughness est construite depuis des propriétés de surface et contrôlée en vue rasante.
### 47.3 Utiliser une valeur metallic grise partout
**Symptôme :** le matériau semble parfois plastique, parfois métallique, sans séparation lisible entre peinture, métal nu et salissure.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
metallic:
  value: 0.5
  applies_to: whole_material
  material_layers: ignored
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Un gris uniforme décrit une fraction conductrice ambiguë sur tous les pixels et ne correspond pas aux zones matérielles réellement présentes.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
metallic:
  dielectric_regions: 0.0
  exposed_metal_regions: 1.0
  transition_pixels: filtered_edges
  layer_mask: documented
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Les régions diélectriques et métalliques sont explicites, tandis que les valeurs intermédiaires restent limitées aux transitions.
### 47.4 Choisir 4K pour chaque texture
**Symptôme :** la VRAM augmente fortement alors que de nombreux accessoires restent petits à l’écran.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
resolution_policy:
  every_texture: 4096
  screen_coverage: ignored
  texel_density: ignored
  platform_profile: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La résolution est appliquée sans tenir compte de la surface réelle, de la densité, de la caméra ou de la plateforme.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
resolution_policy:
  source_resolution: authoring_need
  import_limit: profile_driven
  gates: [screen_coverage, texel_density, memory_measurement]
  exceptions: documented
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La source est préservée tandis que la livraison dépend de mesures et d’un profil explicite.
### 47.5 Désactiver les mipmaps pour économiser de la mémoire
**Symptôme :** les sols et murs scintillent à distance et produisent du bruit lors des mouvements de caméra.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
mipmaps:
  generate: false
  reason: save_memory
  distance_test: skipped
  aliasing_review: skipped
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La faible économie supprime les niveaux réduits nécessaires lorsque la texture occupe peu de pixels, ce qui provoque aliasing et instabilité.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
mipmaps:
  generate: true
  memory_cost: included_in_budget
  distance_test: required
  roughness_filtering: candidate_if_needed
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** La chaîne de mipmaps stabilise la lecture à distance et son coût est intégré au budget au lieu d’être ignoré.
### 47.6 Packager les canaux ORM dans le mauvais ordre
**Symptôme :** la surface devient métallique dans les creux et la rugosité suit l’occlusion.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
packed_texture:
  r: metallic
  g: ambient_occlusion
  b: roughness
  material_type: ORMMaterial3D
  channel_preview: skipped
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** `ORMMaterial3D` attend un contrat de canaux précis ; l’inversion produit des valeurs plausibles mais appliquées aux mauvaises propriétés.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
packed_texture:
  r: ambient_occlusion
  g: roughness
  b: metallic
  color_space: linear_data
  channel_preview: required
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** L’ordre est aligné sur ORM et chaque canal est contrôlé séparément avant intégration.
### 47.7 Valider le matériau sous une seule lumière chaude
**Symptôme :** le matériau paraît correct dans la capture de présentation mais devient trop saturé ou trop brillant dans les autres scènes.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
material_review:
  lighting_profile: warm_beauty
  camera: free
  exposure: adjusted_per_material
  decision: approved
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** La lumière, la caméra et l’exposition peuvent masquer les défauts et rendent les comparaisons non reproductibles.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
material_review:
  lighting_profiles: [neutral, warm, cool, high_contrast]
  cameras: locked
  exposure: locked_per_campaign
  calibration_set: required
  decision: pending_review
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Plusieurs éclairages et des réglages verrouillés révèlent les écarts sans avantager un matériau.
### 47.8 Considérer le matériau Blender comme autorité runtime
**Symptôme :** les artistes modifient le graphe Blender, mais Godot conserve des paramètres différents et personne ne sait quelle version est correcte.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
authority:
  blender_material: runtime_source_of_truth
  godot_resource: generated_without_manifest
  gltf_limits: ignored
  reimport_review: none
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le graphe Blender peut contenir des fonctions non transportées par glTF et ne couvre pas les réglages d’import ou les ressources propres à Godot.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
authority:
  source_manifest: canonical_contract
  blender_material: lookdev_reference
  gltf_material: exchange_subset
  godot_resource: runtime_derivative
  reimport_review: required
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Le manifeste conserve le contrat, Blender sert au lookdev, glTF transporte un sous-ensemble et Godot possède la dérivation runtime.
### 47.9 Utiliser un atlas sans marges compatibles avec les mipmaps
**Symptôme :** des couleurs ou normales d’un îlot voisin apparaissent à distance sur les bords.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
atlas:
  islands_touching: true
  padding_px: 0
  mipmaps: true
  repeat: enabled
  review: skipped
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Les niveaux réduits filtrent des texels voisins ; l’absence de marge et la répétition rendent les fuites probables.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
atlas:
  padding: chapter_17_mip_safe_contract
  mipmaps: true
  repeat: disabled
  border_capture: required
  layout_versioned: true
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Des marges adaptées, un sampler borné et une capture de bord protègent les îlots à plusieurs niveaux.
### 47.10 Confondre poids sur disque et mémoire GPU
**Symptôme :** le rapport annonce un matériau léger parce que les PNG sont petits, alors que la scène dépasse le budget VRAM.
> **[LECTURE] Exemple fautif — Ne pas saisir.**
```yaml
texture_budget:
  metric: png_file_size
  mipmaps: ignored
  gpu_format: ignored
  residency: ignored
  decision: within_budget
```
<!-- qa:code-explanation -->
**Pourquoi cet exemple est fautif :** Le fichier compressé sur disque ne représente ni le format GPU, ni la chaîne de mipmaps, ni les textures simultanément résidentes.
> **[LECTURE] Exemple corrigé — Ne pas saisir.**
```yaml
texture_budget:
  disk_size: recorded
  imported_format: recorded
  mip_chain: included
  estimated_vram: recorded
  measured_vram: required
  scene_residency: measured
  decision: pending
```
<!-- qa:code-explanation -->
**Pourquoi la correction fonctionne :** Le budget distingue stockage, import, estimation et mesure réelle dans une scène représentative.
## 48. Porte d’acceptation
Un matériau n’est pas accepté parce qu’il paraît réaliste dans une capture. Il doit posséder une identité, une
provenance, des canaux correctement interprétés, un profil de résolution, un espace colorimétrique, un import
reproductible, une densité cohérente et une comparaison sous plusieurs éclairages.
La porte reste bloquée si les textures ne sont pas produites, si la scène n’est pas exécutée ou si la mémoire n’est
pas mesurée. Le niveau `static-review` accepte seulement la procédure et les contrats.
> **[LECTURE] Checklist d’acceptation — Ne pas saisir.**
```yaml
acceptance:
  identity_and_provenance: required
  pbr_channel_semantics: required
  color_spaces: required
  source_and_delivery_separated: required
  texel_density: measured
  import_profiles: applied
  multi_lighting_captures: produced
  compression_artifacts: reviewed
  memory_budget: measured
  godot_runtime_scene: executed
  current_status: blocked_static_review_only
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Documents :** identité, provenance et sémantique sont nécessaires avant la production.
- **Mesures :** densité, mémoire et artefacts exigent une campagne réelle.
- **Scène :** la validation finale se déroule dans Godot.
- **Statut :** le chapitre documentaire ne débloque pas les livrables runtime.
## 49. Livrables permanents à préparer
Le chapitre définit cinq livrables permanents, encore non matérialisés :
- un guide PBR résumant canaux, espaces colorimétriques et conventions ;
- des presets d’export et d’import versionnés ;
- une bibliothèque de matériaux maîtres et de variantes contrôlées ;
- des profils de compression par sémantique et plateforme ;
- une scène d’éclairage de référence avec étalons et captures.
> **[LECTURE] Registre des livrables — Ne pas saisir.**
```yaml
deliverables:
  pbr_guide:
    id: AST-PBR-GUIDE-001
    status: not_materialized
  export_import_presets:
    id: AST-MAT-PRESETS-001
    status: not_materialized
  material_library:
    id: AST-MAT-LIBRARY-001
    status: not_materialized
  compression_profiles:
    id: AST-TEX-COMPRESSION-PROFILES-001
    status: not_materialized
  lighting_scene:
    id: AST-MAT-LAB-PBR-001
    status: not_materialized
```
<!-- qa:code-explanation -->
**Explication structurée du bloc :**
- **Identifiants :** chaque livrable possède une identité réutilisable.
- **Statuts :** aucun fichier n’est présenté comme existant.
- **Réutilisation :** les contrats pourront alimenter le Companion Pack.
- **Dépendance :** les livrables seront complétés par les UV, bakings et mesures des chapitres suivants.
## 50. Synthèse opérationnelle pour Project Asteria
Project Asteria adopte le workflow metallic-roughness, un contrat explicite d’espaces colorimétriques, des sources
distinctes des imports, des profils de résolution pilotés par densité et couverture écran, des mipmaps budgétés, des
compressions qualifiées par sémantique et une bibliothèque réduite de matériaux maîtres.
Les surfaces étendues privilégient les matériaux tilables, trim sheets et détails causaux. Les atlas restent
versionnés et compatibles avec les mipmaps. Blender fournit une référence de lookdev, glTF transporte le sous-ensemble
d’échange et Godot reste l’autorité du matériau runtime dérivé.
La scène `AST-MAT-LAB-PBR-001` devient la porte commune : caméras, exposition, étalons et profils d’éclairage sont
verrouillés ; les captures et mesures conservent commit, matériau et profil d’import. Tant que cette scène, les
textures et les mesures n’existent pas, aucune qualité visuelle ni performance n’est revendiquée.
