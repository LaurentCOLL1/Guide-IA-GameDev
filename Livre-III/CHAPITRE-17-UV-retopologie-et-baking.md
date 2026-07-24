---
title: "Livre III — Chapitre 17 : UV, retopologie et baking"
id: "DOC-L3-CH17"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre III"
chapter: 17
last-verified: "2026-07-24T11:13:52+02:00"
audit-status: "complete"
audit-date: "2026-07-24T11:13:52+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-17.md"
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
    qualification: "documentation-reviewed-against-5.0-manual"
  exchange:
    format: "glTF 2.0"
    default-container: "GLB"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# UV, retopologie et baking

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH17`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Le chapitre 16 a défini la signification des cartes PBR, les espaces colorimétriques, les formats, les profils de
compression et les matériaux Godot. Le présent chapitre produit la géométrie et les projections nécessaires pour
transférer les détails d’un modèle haute résolution vers un modèle final exploitable, sans redéfinir le pipeline PBR
ni créer la chaîne LOD du chapitre 18.

Le fil rouge utilise `AST-BAKE-PILOT-RELAY-001`, un relais de terrain composé d’une coque rigide, d’un capot biseauté,
de fixations, d’un écran protégé et d’une sangle souple. La coque éprouve les décisions hard-surface ; la sangle
éprouve une topologie locale capable de se courber. Le pilote reste un contrat documentaire : aucun modèle, UV, cage
ou bake n’est revendiqué comme produit.

Retopologiser ne signifie pas seulement réduire le nombre de polygones. Il faut préserver la silhouette, les zones de
déformation, les ruptures de forme, la continuité du shading et la stabilité de la projection. Le résultat est accepté
uniquement si le low poly, ses UV, ses tangentes et les textures bakées restent cohérents dans Blender puis dans
Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Modèle haute résolution et références approuvées
    ↓
Analyse silhouette, déformation et ruptures de forme
    ↓
Maillage basse résolution et triangulation contrôlée
    ↓
Découpe UV, densité, marges et chevauchements qualifiés
    ↓
Cage ou distance de rayons mesurée
    ↓
Bake normal, AO, curvature et cartes auxiliaires
    ↓
Contrôle Blender sous plusieurs angles
    ↓
Export GLB avec normales, UV et tangentes
    ↓
Import Godot et comparaison tangentielle
    ↓
Rapport de contrôle et porte d'acceptation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances :** le modèle détaillé et le guide PBR doivent exister comme références avant la retopologie.

- **Ordre :** la topologie finale et les UV sont stabilisés avant le bake définitif.

- **Preuve :** la comparaison Blender–Godot est requise pour qualifier les tangentes et les seams.

- **Frontière :** les variantes LOD et leurs distances restent au chapitre 18.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- différencier les objectifs d’un asset statique, articulé, souple ou entièrement déformable ;
- préserver la silhouette et les zones de contact avant de réduire les détails internes ;
- construire un edge flow adapté aux articulations sans imposer des quads partout ;
- utiliser l’overlay de retopologie, Poly Build, le snapping et Shrinkwrap de manière contrôlée ;
- stabiliser normales, arêtes dures, seams et triangulation avant le bake final ;
- concevoir une carte UV dont la densité, les marges et les chevauchements sont explicitement qualifiés ;
- mesurer la distorsion avec un checker et corriger les îlots sans détruire leur orientation utile ;
- choisir entre cage, Cage Extrusion et Max Ray Distance selon la géométrie ;
- baker des normales tangentes, de l’AO, de la curvature et des masques auxiliaires sans confondre leur rôle ;
- préparer une normale OpenGL compatible avec Godot et diagnostiquer une inversion du canal vert ;
- vérifier l’existence des UV, normales et tangentes dans le maillage importé ;
- rédiger un rapport qui sépare résultats mesurés, hypothèses et réserves d’exécution.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les procédures Blender, contrats YAML, exemples Python, structures
de scène Godot et scripts GDScript ont été relus contre les documentations officielles disponibles. Ils ne constituent
pas une exécution de Blender, un bake, un export glTF, un import Godot ou une mesure visuelle.

La documentation Blender 5.0 sert de référence publique détaillée lorsque la documentation 5.2 n’est pas encore
exposée avec la même granularité. Les noms d’options doivent être revérifiés dans l’interface 5.2 avant production.
Godot `4.7.1-stable` est la version moteur de référence du dépôt.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence:
  level: static-review
  blender_execution: not_executed
  retopology_created: false
  uv_unwrap_created: false
  cages_created: false
  textures_baked: false
  glb_exported: false
  godot_imported: false
  tangent_comparison: not_executed
  pdf: not_built
decision:
  documentation: reviewed
  production_assets: blocked
  runtime_claims: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les booléens et statuts textuels empêchent de confondre document, asset et exécution.

- **Réserve :** chaque résultat de production reste faux ou non exécuté jusqu’à preuve matérielle.

- **Décision :** la documentation peut être fusionnée alors que le pilote reste bloqué.

- **PDF :** la compilation du Livre III demeure différée jusqu’à la fin du livre.

## 4. Périmètre et frontières

Le chapitre couvre :

- objectifs de retopologie selon asset statique ou déformable ;
- silhouette, edge flow, densité locale, pôles, triangles et n-gons contrôlés ;
- overlay de retopologie, Poly Build, snapping et Shrinkwrap ;
- normales, lissage, ruptures de shading et triangulation finale ;
- UV1, seams, îlots, distorsion, densité de texels, packing et marges ;
- chevauchements autorisés, symétrie, empilement et cas nécessitant des UV uniques ;
- cages, extrusion, distance de rayons, correspondance par noms et projection ;
- bake normal tangent, AO, curvature, ID et masques auxiliaires ;
- contrôle Blender, export glTF, import Godot et comparaison tangentielle ;
- rapport de contrôle, matrice de diagnostic et porte d’acceptation.

Le chapitre ne couvre pas :

- la sémantique générale des cartes PBR, leurs profils de compression ou les matériaux maîtres du chapitre 16 ;
- la création de LOD, imposteurs, distances et benchmarks avant/après du chapitre 18 ;
- le rigging, le skinning et les poids du chapitre 19 ;
- l’animation générale du chapitre 20 ;
- l’intégration globale de toutes les familles d’assets du chapitre 28 ;
- les lightmaps, UV2 et paramètres d’éclairage comme cours autonome ;
- la production effective du pilote ou une validation juridique de ses sources.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
responsibility_matrix:
  chapter_16:
    owns: [pbr_semantics, color_spaces, texture_formats, compression_profiles, godot_materials]
  chapter_17:
    owns: [retopology, uv1_layout, cages, baking, tangent_consistency, bake_diagnostics]
  chapter_18:
    owns: [lod_chain, impostors, distance_profiles, geometric_benchmarks]
  chapter_19:
    owns: [rigging, skinning, deformation_weights]
status:
  boundaries_reviewed: true
  runtime_validation: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** chaque chapitre reçoit une responsabilité exclusive.

- **Entrées :** le chapitre 17 consomme les conventions PBR sans les redéfinir.

- **Sorties :** le maillage finalisé prépare les LOD et le rig sans les produire.

- **Statut :** l’intégration runtime reste explicitement en attente.

## 5. Asset pilote et questions de validation

`AST-BAKE-PILOT-RELAY-001` doit répondre à des questions observables : les biseaux principaux lisent-ils à la distance
cible, la coque conserve-t-elle sa silhouette, la sangle peut-elle se courber sans pincement, les seams restent-ils
discrètes, les détails high poly se projettent-ils sans contamination et le rendu Godot correspond-il au rendu de
contrôle Blender ?

Le pilote comporte deux sous-ensembles qui partagent une même famille de matériaux mais pas les mêmes contraintes
topologiques. La coque est statique ; la sangle reçoit seulement une préparation de déformation, sans rig ni poids.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pilot:
  id: AST-BAKE-PILOT-RELAY-001
  family: field_relay
  components:
    shell:
      deformation: none
      priorities: [silhouette, hard_surface_shading, attachment_clearance]
    strap:
      deformation: local_bending_candidate
      priorities: [edge_flow, thickness, seam_placement]
  validation_views: [front, rear, profile, top, glancing_light, strap_bend_candidate]
  evidence_status: not_produced
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le pilote et ses composants possèdent des identifiants et responsabilités stables.

- **Contraste :** coque statique et sangle souple imposent des décisions topologiques différentes.

- **Vues :** les angles de contrôle rendent visibles les gradients, seams et pincements.

- **Réserve :** le statut interdit de présenter ce contrat comme un asset existant.

## 6. Porte de passage entre les étapes

Chaque étape produit une sortie révisable avant la suivante. Un bake ne doit pas servir à découvrir que le low poly
change encore, et un import Godot ne doit pas être la première occasion d’identifier des UV superposés involontaires.
La porte de passage réduit les corrections en cascade.

Une validation peut revenir à une étape antérieure. Par exemple, une normale tangentielle instable peut révéler une
triangulation non figée, un split de normale incohérent ou une cage trop large.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gates:
  high_ready:
    requires: [source_versioned, transforms_reviewed, material_sets_named]
  low_ready:
    requires: [silhouette_approved, deformation_loops_reviewed, triangulation_locked]
  uv_ready:
    requires: [seams_reviewed, density_checked, overlaps_classified, margins_defined]
  bake_ready:
    requires: [target_images_saved, cage_reviewed, name_matching_verified]
  engine_ready:
    requires: [bakes_reviewed, glb_manifest_created, tangents_exported]
  accepted:
    requires: [blender_comparison_passed, godot_comparison_passed, report_signed]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gardes :** chaque état dépend de preuves antérieures explicites.

- **Réversibilité :** un échec peut renvoyer vers la topologie, les UV ou la cage.

- **Responsabilité :** la signature finale n’est pas remplacée par l’automatisation.

- **Sortie :** l’asset accepté devient une entrée du chapitre 18.

## 7. Retopologie statique et déformable

Un asset statique privilégie la silhouette, les plans, les biseaux visibles et la stabilité du shading. Des triangles
bien placés peuvent être acceptables si leur triangulation est connue et si le résultat ne se déforme pas. Un asset
déformable exige en plus des boucles capables de se comprimer, s’étirer et pivoter autour des zones mobiles.

Le nombre de quads n’est pas un indicateur de qualité isolé. Une grille régulière inutile peut coûter plus cher et
déformer moins bien qu’une densité adaptée aux contraintes. La topologie doit suivre les fonctions de l’asset.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
retopology_profiles:
  static_shell:
    preserve: [outer_silhouette, bevel_highlights, sockets, contact_planes]
    topology_bias: controlled_triangles_allowed
    deformation_test: not_applicable
  flexible_strap:
    preserve: [width, thickness, attachment_transition]
    topology_bias: longitudinal_quads
    deformation_test: bend_and_twist_candidate
review:
  same_polygon_budget_for_both: false
  same_edge_flow_for_both: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** la coque et la sangle reçoivent des priorités distinctes.

- **Triangles :** ils sont autorisés sur la coque lorsqu’ils ne dégradent ni silhouette ni shading.

- **Boucles :** la sangle conserve des quads longitudinaux pour une flexion future.

- **Contrôle :** le même budget ou edge flow n’est pas imposé aux deux composants.

## 8. Source haute résolution

Le high poly est une source de forme et de détails, pas un objet à exporter tel quel. Il doit posséder des volumes
fermes, des intersections comprises, des détails qui survivront à la résolution cible et une version gelée pour le
bake. Les micro-détails inférieurs à quelques texels ne doivent pas dicter la géométrie du low poly.

Les pièces invisibles qui contaminent les rayons sont masquées, séparées ou nommées pour la correspondance. Les
détails flottants sont acceptables si leur projection est contrôlée et si leur provenance reste documentée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
high_source:
  object: AST-BAKE-PILOT-RELAY-001_HP
  state: frozen_candidate
  checks:
    - watertight_where_required
    - no_unintended_duplicate_surfaces
    - bevels_readable_at_target_resolution
    - floating_details_classified
    - hidden_intersections_reviewed
  export_authority: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** le suffixe `_HP` distingue la source haute résolution.

- **Qualité :** les contrôles ciblent les défauts qui perturbent la projection.

- **Détail :** les biseaux doivent rester lisibles à la résolution prévue.

- **Autorité :** le high poly n’est jamais l’asset runtime.

## 9. Contrat du maillage basse résolution

Le low poly porte la silhouette finale, les UV, les normales, les tangentes, les matériaux et éventuellement la
déformation. Il doit être évalué sans normale bakée afin de vérifier que la géométrie seule produit déjà une forme
plausible. La texture ne doit pas cacher une silhouette insuffisante.

Les ouvertures, surfaces de contact et zones vues de profil reçoivent une attention prioritaire. Les détails internes
ou rarement visibles peuvent être transférés dans la normale ou simplifiés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
low_contract:
  object: AST-BAKE-PILOT-RELAY-001_LP
  owns:
    - final_silhouette
    - material_slots
    - uv_primary
    - vertex_normals
    - vertex_tangents
    - final_triangulation
  must_not_depend_on:
    - high_poly_visibility_at_runtime
    - non_exported_modifiers
    - viewport_only_custom_normals
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriété :** le low poly porte toutes les données nécessaires au rendu final.

- **Silhouette :** la forme doit rester crédible avant application de la normale.

- **Export :** aucune dépendance à un modificateur ou réglage uniquement local n’est admise.

- **Stabilité :** la triangulation finale appartient au contrat.

## 10. Nommage et collections Blender

Les collections séparent sources, low poly, cages, cibles de bake et objets de comparaison. Le nommage par base
commune permet une correspondance explicite sans dépendre de l’ordre de sélection. Les suffixes restent courts et
documentés.

Les cages ne sont pas rangées avec les exports. Les images de bake et rapports sont des sorties versionnées,
distinctes du fichier `.blend` source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
AST-BAKE-PILOT-RELAY-001/
├── __SRC_HP
│   ├── relay_shell_HP
│   ├── relay_fasteners_HP
│   └── relay_strap_HP
├── __SRC_LP
│   ├── relay_shell_LP
│   └── relay_strap_LP
├── __BAKE_CAGE
│   ├── relay_shell_CAGE
│   └── relay_strap_CAGE
├── __BAKE_TARGETS
└── __EXPORT
    └── AST-BAKE-PILOT-RELAY-001_LP
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Collections :** les sources, cages, cibles et exports restent séparés.

- **Correspondance :** les bases `relay_shell` et `relay_strap` relient les versions.

- **Sécurité :** les cages ne peuvent pas être exportées par confusion.

- **Sortie :** seul l’objet low poly final entre dans `__EXPORT`.

## 11. Transformations et échelle

Échelle, rotation et unités doivent être cohérentes avant de comparer distances de rayons, largeur de marge ou
densité. Appliquer des transformations sans examen peut modifier un modificateur, une contrainte ou une hiérarchie ;
l’opération doit donc être décidée par composant et enregistrée.

Une cage calculée sur un objet dont l’échelle n’est pas cohérente peut produire une extrusion difficile à interpréter.
Le manifeste conserve les transformations attendues et les exceptions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transform_review:
  unit_system: metric
  scene_scale_contract: inherited_from_chapter_4
  objects:
    relay_shell_LP:
      scale: [1.0, 1.0, 1.0]
      rotation_applied: reviewed
    relay_strap_LP:
      scale: [1.0, 1.0, 1.0]
      deformation_modifiers: review_before_apply
  cage_distance_unit: meters
  status: pending_measurement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unité :** les distances de cage sont exprimées dans le même système métrique.

- **Échelle :** les objets exportables visent une échelle unitaire.

- **Exception :** les modificateurs de la sangle sont examinés avant application.

- **Mesure :** aucune distance numérique définitive n’est inventée.

## 12. Overlay de retopologie

L’overlay de retopologie aide à voir simultanément la nouvelle surface et la source détaillée sans afficher toute la
géométrie arrière comme avec un simple X-Ray. Il ne remplace pas le contrôle des normales, de l’épaisseur ou des
intersections.

Le low poly doit rester légèrement au-dessus de la surface source lorsque le bake l’exige, mais il ne faut pas ajouter
un offset arbitraire qui modifie la silhouette.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
viewport_retopology:
  overlay: enabled_candidate
  xray: disabled_by_default
  source_visibility: controlled
  backface_distraction: reduced
  offset:
    policy: smallest_value_that_avoids_z_fighting
    measured: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Affichage :** l’overlay rend la relation high/low lisible.

- **Limite :** il ne valide ni épaisseur ni projection.

- **Offset :** la valeur doit seulement éviter le conflit visuel.

- **Réserve :** aucune valeur n’est validée sans inspection réelle.

## 13. Poly Build, snapping et fusion

Poly Build combine création, extrusion, déplacement et dissolution de géométrie et convient à la retopologie manuelle.
Le snapping vers la surface aligne les nouveaux sommets sur le high poly ; Auto Merge peut fermer les raccords, mais
doit être contrôlé pour éviter des fusions inattendues.

Une passe régulière vérifie les sommets doublons, les faces inversées et les arêtes non manifold. La vitesse de
construction ne doit pas masquer ces défauts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
retopo_tool_profile:
  tool: Poly_Build
  snapping:
    target: face
    project_individual_elements: review
  auto_merge:
    enabled: candidate
    threshold: measured_scene_unit
  periodic_checks:
    - duplicate_vertices
    - flipped_normals
    - non_manifold_edges
    - accidental_internal_faces
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outil :** Poly Build accélère la création et l’ajustement des faces.

- **Snapping :** la cible est la surface détaillée plutôt qu’une grille arbitraire.

- **Fusion :** le seuil Auto Merge doit être mesuré selon l’échelle.

- **Hygiène :** les contrôles topologiques sont répétés pendant la construction.

## 14. Shrinkwrap et projection de surface

Shrinkwrap peut maintenir le low poly sur la source avec les méthodes Nearest Surface Point, Project ou Target Normal
Project. Le choix dépend de la forme et de la direction de projection. Project peut laisser certains sommets inchangés
s’ils ne rencontrent pas la cible ; Target Normal Project est plus lent mais peut produire une projection plus douce.

Le modificateur est un assistant de construction. Avant le bake final, son effet, son ordre et son application doivent
être stabilisés pour que la cage et la triangulation correspondent au maillage réellement exporté.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shrinkwrap_candidate:
  target: AST-BAKE-PILOT-RELAY-001_HP
  method_by_component:
    shell: nearest_surface_point_candidate
    strap: target_normal_project_candidate
  offset: pending_visual_review
  limit: pending_scale_review
  modifier_order: documented
  apply_before_final_bake: required_decision
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** le high poly est la surface de référence.

- **Méthode :** coque et sangle peuvent employer des projections différentes.

- **Ordre :** la position du modificateur dans la pile est documentée.

- **Gel :** le bake final utilise un état stabilisé du low poly.

## 15. Silhouette avant densité

La silhouette est contrôlée à plusieurs distances et sous plusieurs angles avant de distribuer les polygones internes.
Une arête qui change le contour, une encoche fonctionnelle ou un biseau majeur mérite davantage de géométrie qu’une
grande face plane.

Le profil de la sangle est testé en ligne droite puis dans une courbure candidate. La coque est contrôlée en vue
rasante pour révéler les facettes et gradients inattendus.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
silhouette_review:
  distances: [close_candidate, gameplay_candidate, far_candidate]
  angles: [front, profile, top, three_quarter, glancing]
  preserve_geometry:
    - external_contour
    - handle_opening
    - screen_guard_profile
    - strap_thickness
  transfer_to_normal:
    - engraved_lines
    - shallow_fastener_details
    - micro_surface_relief
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distances :** les profils restent candidats jusqu’à mesure dans la scène.

- **Géométrie :** les éléments qui modifient le contour restent modélisés.

- **Bake :** les détails peu profonds peuvent être transférés dans la normale.

- **Contrôle :** la lumière rasante révèle facettes et gradients.

## 16. Edge flow de la sangle

La sangle reçoit des boucles transversales régulières dans les zones de flexion et des transitions plus denses près
des attaches. Les arêtes suivent la longueur afin de permettre une courbure et une torsion prévisibles. La densité
n’est pas augmentée sur toute la pièce si seule une zone se déforme.

Le chapitre ne peint aucun poids. Il prépare seulement une topologie qui pourra être riggée au chapitre 19.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
strap_edge_flow:
  longitudinal_loops: continuous
  cross_sections:
    flexible_zone: regular_candidate
    attachment_zone: reinforced_transition
    rigid_buckle_zone: reduced_deformation
  poles:
    keep_out_of_primary_bend: true
  skin_weights:
    produced_here: false
    owner: chapter_19
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Direction :** les boucles longitudinales suivent la traction et la torsion.

- **Transition :** l’attache reçoit une densité locale plus forte.

- **Pôles :** ils sont éloignés de la courbure principale.

- **Frontière :** les poids de skinning restent au chapitre 19.

## 17. Topologie hard-surface de la coque

La coque cherche des plans stables, des biseaux cohérents et des changements de normale prévisibles. Les boucles de
soutien ne sont ajoutées que lorsque la silhouette ou le bake l’exige. Un large plan peut rester simple si sa
triangulation et ses normales sont stables.

Les intersections décoratives sont évaluées : certaines peuvent rester en flottants sur le high poly, d’autres
nécessitent un volume low poly pour éviter une projection trop oblique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shell_topology:
  broad_planes: minimal_faces
  major_bevels: explicit_geometry
  shallow_panel_lines: bake_candidate
  sockets:
    gameplay_contact: explicit_geometry
    decorative_recess: bake_candidate
  floating_high_details:
    allowed: true
    requires_projection_test: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plans :** les grandes surfaces évitent une grille inutile.

- **Biseaux :** les ruptures visibles restent géométriques.

- **Fonction :** les sockets de contact ne sont pas remplacées par une texture.

- **Projection :** les flottants nécessitent un test de contamination.

## 18. Quads, triangles, n-gons et pôles

Les quads facilitent l’édition et la déformation, mais ne sont pas une fin en soi. Des triangles contrôlés sont
acceptables sur un asset statique. Les n-gons peuvent servir pendant la construction, mais la triangulation finale
doit être inspectée avant le bake et l’export.

Les pôles concentrent plusieurs boucles. Ils sont déplacés hors des zones de forte courbure, des highlights critiques
et des déformations principales.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
topology_policy:
  quads:
    preferred_for: [editing, strap_bending, loop_continuity]
  triangles:
    allowed_for: [static_termination, hidden_flat_regions]
  ngons:
    construction_only: true
    final_triangulation_review: required
  poles:
    forbidden_zones: [primary_bend, glancing_highlight, silhouette_corner]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Quads :** ils servent surtout la continuité et la déformation.

- **Triangles :** ils restent permis dans les zones statiques maîtrisées.

- **N-gons :** leur triangulation doit être figée et inspectée.

- **Pôles :** ils sont exclus des zones visuellement ou mécaniquement sensibles.

## 19. Densité locale et gradient de résolution

La densité géométrique suit la taille écran, la courbure, la déformation et la fonction. Une transition progressive
évite de connecter brutalement une grille dense à une face presque vide. Les réductions utilisent des terminaisons
propres et sont testées sous lissage.

Le budget en triangles est enregistré comme une mesure de sortie, non comme un objectif universel. Les familles
d’assets recevront des budgets au chapitre 18.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
local_density:
  drivers:
    silhouette_change: high_priority
    deformation: high_priority
    highlight_curvature: medium_priority
    hidden_flat_area: low_priority
  transitions:
    abrupt_ratio_change: forbidden
    reviewed_terminations: required
  polygon_budget:
    value: pending_measurement
    authority: chapter_18_profiles
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Moteurs :** la densité découle de besoins observables.

- **Transition :** les changements brutaux de résolution sont refusés.

- **Mesure :** le nombre final est relevé après validation.

- **Frontière :** les profils de budget restent au chapitre 18.

## 20. Biseaux, arêtes de soutien et shading

Un biseau majeur doit être assez large pour être visible dans la résolution et la distance prévues. Des arêtes de
soutien trop proches peuvent créer des gradients serrés qui se bakent mal. Les petits biseaux peuvent être transférés
à la normale si leur silhouette ne compte pas.

Le low poly est testé avec un matériau neutre et une lumière rasante. Les artefacts ne sont pas corrigés par une
texture avant d’avoir déterminé s’ils proviennent de la géométrie ou des normales.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bevel_decision:
  explicit_geometry_when:
    - changes_silhouette
    - catches_gameplay_readable_highlight
    - defines_contact_edge
  normal_map_when:
    - shallow
    - sub_silhouette
    - stable_under_target_resolution
  review_material: neutral_mid_roughness
  review_light: glancing_candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Géométrie :** les biseaux qui modifient lecture ou contact restent modélisés.

- **Normale :** les détails secondaires peuvent être bakés.

- **Matériau :** un matériau neutre évite de cacher le shading.

- **Éclairage :** la lumière rasante amplifie les défauts.

## 21. Arêtes dures et seams UV

Une arête dure sépare les normales de sommets ; une seam coupe l’espace UV. Elles répondent à des problèmes
différents, même si une même arête peut recevoir les deux. Les décisions doivent être cohérentes avec la stratégie de
bake et l’export.

Une rupture de normale sans séparation UV peut produire une interpolation difficile à baker selon le pipeline. Une
seam inutile sur une surface continue augmente les bordures à protéger et peut rendre les variations plus visibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
edge_split_review:
  edge_id: shell_outer_rim
  hard_normal: candidate
  uv_seam: candidate
  reasons:
    hard_normal: abrupt_surface_angle
    uv_seam: hidden_boundary_and_packability
  require_same_choice_everywhere: false
  final_test: tangent_bake_and_engine_import
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** hard edge et seam sont évaluées indépendamment.

- **Raison :** chaque choix possède une justification géométrique ou UV.

- **Variabilité :** le même couple n’est pas imposé à toutes les arêtes.

- **Preuve :** le bake tangent et l’import moteur décident du résultat final.

## 22. Normales et lissage

Les normales doivent être stabilisées avant le bake définitif. Un changement de lissage après le bake modifie le
repère tangent et peut invalider la carte. Les normales personnalisées ou pondérées sont possibles, mais leur
génération, leur application et leur export doivent être reproductibles.

Le chapitre ne recommande pas d’appliquer aveuglément tous les modificateurs. Il exige que l’état réellement exporté
soit connu et conservé dans le manifeste.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
normal_state:
  mesh: AST-BAKE-PILOT-RELAY-001_LP
  smooth_by_angle: reviewed_candidate
  custom_normals:
    used: pending
    generator: documented_if_used
  modifiers_affecting_normals:
    - bevel_candidate
    - weighted_normal_candidate
  freeze_before_final_bake: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État :** lissage et normales sont enregistrés avant le bake.

- **Modificateurs :** toute opération qui change les normales est identifiée.

- **Reproductibilité :** un générateur de normales doit être documenté.

- **Gel :** aucune modification tardive n’est autorisée sans nouveau bake.

## 23. Triangulation finale

Le GPU rend des triangles. Une face quad ou n-gon peut être triangulée différemment entre étapes, ce qui change
l’interpolation, les tangentes et parfois le rendu de la normale. La triangulation finale doit être figée avant le
bake de production et conservée à l’export.

Le modificateur Triangulate peut rendre l’opération reproductible, mais son ordre dans la pile et sa méthode doivent
être versionnés. Une comparaison du nombre et de l’ordre des triangles est ajoutée au rapport.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
triangulation_contract:
  object: AST-BAKE-PILOT-RELAY-001_LP
  stage: before_final_bake
  method: modifier_candidate
  modifier_order: after_shape_modifiers_before_export
  keep_on_export: true
  validation:
    triangle_count: pending
    topology_hash: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Moment :** la triangulation intervient avant le bake final.

- **Ordre :** elle suit les modificateurs de forme et précède l’export.

- **Conservation :** le même état est utilisé pour Blender et Godot.

- **Preuve :** compte et empreinte topologique restent à mesurer.

## 24. Rôles des cartes UV

La carte UV principale porte les textures de surface. Une éventuelle carte secondaire doit avoir une responsabilité
différente, par exemple un lightmap ou un masque spécifique. Le présent chapitre prépare la structure, mais ne
remplace pas le cours d’éclairage ni les réglages de lightmapping.

Chaque carte UV est nommée, ordonnée et associée à une résolution cible. Un export qui réordonne les cartes doit être
détecté dans Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
uv_sets:
  UV_Primary:
    index: 0
    purpose: pbr_surface_textures
    overlap_policy: classified
  UV_Secondary:
    index: 1
    purpose: optional_lightmap_or_special_mask
    produced_here: false
    owner: later_integration
  order_must_survive_export: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** chaque carte UV possède une identité explicite.

- **Usage :** la carte principale reçoit les textures PBR.

- **Frontière :** la carte secondaire n’est pas produite automatiquement ici.

- **Export :** l’ordre est vérifié après import.

## 25. Stratégie de seams

Les seams sont placées dans les zones cachées, les changements de matériau, les ruptures géométriques ou les endroits
où l’îlot peut être aplati avec moins de distorsion. Une seam visible peut être préférable à une forte distorsion qui
déforme les détails.

La sangle est ouverte le long d’un bord peu visible et séparée aux attaches. La coque utilise ses ruptures naturelles
et évite de couper un highlight continu sans justification.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
seam_plan:
  relay_shell:
    preferred: [rear_lower_edge, panel_breaks, material_boundaries]
    avoid: [hero_front_highlight, screen_guard_center]
  relay_strap:
    preferred: [inner_length_edge, attachment_boundaries]
    avoid: [outer_visible_center]
  review:
    distortion: required
    visibility: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Placement :** les seams suivent visibilité et aptitude au dépliage.

- **Coque :** les ruptures de panneau servent de frontières naturelles.

- **Sangle :** la coupe longitudinale est placée sur la face intérieure.

- **Arbitrage :** distorsion et visibilité sont évaluées ensemble.

## 26. Îlots et continuité

Un îlot trop grand peut être difficile à détendre ; trop d’îlots augmentent les marges, les seams et la charge de
peinture. La découpe vise des surfaces compréhensibles, orientées et suffisamment grandes pour préserver les détails
utiles.

Les éléments répétitifs peuvent partager une orientation commune afin de simplifier le contrôle. Les surfaces qui
doivent recevoir un texte ou une usure directionnelle restent orientées de manière prévisible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
island_policy:
  target:
    coherent_surface_groups: true
    arbitrary_fragmentation: false
  orientation:
    text_panels: upright
    strap_length: u_axis_candidate
    cylindrical_fasteners: consistent
  painting:
    readable_grouping: required
    hidden_micro_islands: minimize
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cohérence :** les îlots suivent des groupes de surface compréhensibles.

- **Orientation :** textes et détails directionnels restent prévisibles.

- **Peinture :** le regroupement facilite les retouches.

- **Coût :** les micro-îlots et leurs marges sont réduits.

## 27. Checker et distorsion

Un checker régulier révèle étirement, compression, cisaillement et discontinuités d’échelle. Le contrôle est effectué
sur la coque, la sangle droite et la sangle dans une courbure candidate. Une grille visuellement régulière n’autorise
pas à masquer une seam importante.

Minimize Stretch peut réduire les différences d’angles entre le maillage et les UV ; il reste un outil d’optimisation,
pas une garantie automatique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
checker_review:
  texture: UV_CHECKER_AST-001
  views: [front, profile, glancing, strap_bent_candidate]
  failures:
    - elongated_cells
    - compressed_cells
    - abrupt_scale_jump
    - mirrored_text_unintended
    - seam_visibility_excessive
  minimize_stretch:
    allowed: true
    final_human_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Texture :** un checker stable rend les comparaisons répétables.

- **Vues :** la déformation candidate de la sangle est incluse.

- **Échecs :** les symptômes visuels sont explicitement listés.

- **Automatisation :** Minimize Stretch ne remplace pas la revue humaine.

## 28. Échelle moyenne des îlots

Average Island Scale rapproche l’échelle relative des îlots. Il ne remplace pas une politique de densité qui accorde
davantage d’espace à un écran lisible, un visage ou un élément héros. Les exceptions sont documentées plutôt que
corrigées silencieusement.

Après l’opération, les îlots prioritaires sont ajustés puis repackés. Le rapport conserve leur densité mesurée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
island_scale_policy:
  baseline_operation: Average_Island_Scale
  exceptions:
    screen_surface:
      priority_multiplier: pending_measurement
      reason: readable_interface_detail
    hidden_backplate:
      priority_multiplier: pending_measurement
      reason: low_visibility
  final_density_report: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** Average Island Scale établit une cohérence initiale.

- **Exceptions :** les surfaces prioritaires peuvent recevoir plus d’espace.

- **Justification :** chaque dérogation répond à une fonction observable.

- **Rapport :** la densité finale est mesurée après packing.

## 29. Densité de texels

La densité relie surface 3D et résolution texture. Elle est mesurée, non déduite du seul pourcentage d’occupation UV.
La politique du chapitre 16 définit les familles de résolution ; le chapitre 17 vérifie que les UV respectent le
profil choisi.

Les composants qui partagent une texture sont comparés avec le même outil et la même unité. Une dérogation pour la
surface d’écran doit rester visible dans le manifeste.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
texel_density_check:
  profile: inherited_from_chapter_16
  unit: pixels_per_meter
  texture_resolution: pending_profile_selection
  components:
    shell: pending
    strap: pending
    screen: pending_exception
  tolerance:
    default: pending_measurement
  result: not_measured
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Héritage :** la famille de résolution vient du pipeline PBR.

- **Unité :** la densité est exprimée en pixels par mètre.

- **Composants :** chaque sous-ensemble est relevé séparément.

- **Réserve :** aucune valeur n’est inventée avant mesure.

## 30. Packing et rotation

Pack Islands optimise l’espace UV tout en conservant une marge. Les méthodes de marge `Scaled`, `Add` et `Fraction`
n’ont pas la même signification. `Fraction` permet de relier la marge à la taille du carré UV, mais peut être plus
lente ; le choix doit être enregistré.

La rotation automatique améliore souvent l’occupation, mais les îlots directionnels peuvent être verrouillés. Les
îlots épinglés sont utilisés avec prudence afin de ne pas bloquer un packing efficace.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pack_profile:
  method: Pack_Islands
  margin_method: Fraction_candidate
  margin_value: derived_from_pixels_and_resolution
  rotation:
    general_islands: allowed
    text_and_directional_islands: locked_candidate
  pinned_islands:
    allowed: true
    reason_required: true
  pack_result:
    utilization: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Méthode :** le profil enregistre le sens de la marge.

- **Conversion :** la valeur UV est dérivée d’un besoin en pixels.

- **Rotation :** les surfaces directionnelles peuvent être verrouillées.

- **Mesure :** l’occupation finale reste à relever.

## 31. Marges UV, bake et mipmaps

Une marge protège les îlots contre le filtrage et les mipmaps. Blender peut étendre les pixels de bord ou utiliser les
faces adjacentes. La marge nécessaire dépend de la résolution, de la compression, du nombre de mipmaps observés et de
la distance cible.

La marge de packing et la dilation de bake sont coordonnées. Une belle disposition sans pixels de protection reste
fragile.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
margin_contract:
  texture_resolution: pending
  uv_pack_margin_pixels: pending
  bake_margin_pixels: pending
  bake_margin_type: adjacent_faces_candidate
  review_conditions:
    - full_resolution
    - mip_level_candidate
    - compressed_import_candidate
    - glancing_angle
  acceptance: no_color_or_normal_bleed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Coordination :** packing et bake utilisent des marges compatibles.

- **Type :** Adjacent Faces est un candidat lorsque la continuité le permet.

- **Conditions :** le contrôle inclut mipmaps et compression.

- **Critère :** aucune fuite de couleur ou de normale n’est admise.

## 32. Chevauchements, symétrie et empilement

Les chevauchements sont classés en intentionnels ou fautifs. Des pièces parfaitement symétriques peuvent partager des
UV si elles n’ont pas besoin d’usure unique, de texte asymétrique ou d’AO distincte. Les faces cachées ne sont pas
empilées automatiquement si elles peuvent recevoir des ombres ou des marques propres.

Un inventaire des groupes empilés permet de comprendre les conséquences sur toutes les cartes bakées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
overlap_registry:
  intentional:
    - group: strap_fastener_pair
      reason: identical_material_and_no_unique_markings
      allowed_maps: [base_color, roughness, metallic, tangent_normal_candidate]
      forbidden_maps: [unique_ao, unique_id]
  forbidden:
    - screen_front_with_backplate
    - shell_left_right_when_asymmetric_wear_required
  accidental_overlap_scan: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Registre :** chaque empilement intentionnel possède une raison.

- **Cartes :** les cartes compatibles et incompatibles sont séparées.

- **Asymétrie :** texte et usure unique interdisent certains miroirs.

- **Contrôle :** un scan recherche les chevauchements non déclarés.

## 33. Carte secondaire et lightmaps

Godot peut utiliser une carte UV secondaire pour certaines techniques d’éclairage. La création ou génération de cette
carte possède ses propres contraintes d’unicité et de marge. Le chapitre ne transforme pas ce sujet en cours autonome,
mais empêche de confondre UV de textures et UV de lightmap.

Si la carte secondaire est générée plus tard, le manifeste indique qu’elle ne doit pas modifier l’ordre de la carte
principale.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
secondary_uv_boundary:
  primary_uv:
    must_survive: true
    owner: chapter_17
  lightmap_uv:
    required_now: false
    overlap: forbidden_if_created
    margins: tool_and_resolution_dependent
    owner: lighting_integration
  import_order_check: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Priorité :** la carte principale reste stable.

- **Lightmap :** son éventuelle carte exige unicité et marges propres.

- **Frontière :** la production appartient à l’intégration d’éclairage.

- **Import :** l’ordre des cartes est contrôlé dans Godot.

## 34. UDIM : exception, pas défaut

Les UDIM peuvent être utiles pour certains assets héros ou pipelines de peinture, mais ils augmentent la complexité de
l’export, des matériaux, de la mémoire et de l’intégration. Le pilote n’en dépend pas par défaut.

Une demande UDIM doit préciser le support réel de la chaîne cible, le nombre de tuiles, la stratégie de réduction et
les conséquences pour Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
udim_decision:
  pilot_default: disabled
  enable_only_if:
    - hero_asset_requirement_approved
    - authoring_toolchain_supported
    - export_and_godot_strategy_verified
    - texture_budget_approved
  tile_count: pending_if_enabled
  fallback: single_tile_material_sets
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** le pilote reste sur une texture simple.

- **Conditions :** l’activation exige une validation de toute la chaîne.

- **Budget :** le nombre de tuiles doit être approuvé.

- **Repli :** plusieurs material sets peuvent remplacer les UDIM.

## 35. Ensembles de bake et correspondance

Les objets sont regroupés en bake sets afin d’éviter qu’un détail d’une pièce se projette sur une autre. La
correspondance par noms réduit la dépendance à l’ordre de sélection. Les suffixes doivent être cohérents et sans
ambiguïté.

Les composants proches mais distincts, comme fixations et coque, sont testés dans des sets séparés si les rayons se
contaminent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bake_sets:
  - base: relay_shell
    high: [relay_shell_HP, relay_fasteners_HP]
    low: relay_shell_LP
    cage: relay_shell_CAGE
    material_set: relay_shell_MAT
  - base: relay_strap
    high: [relay_strap_HP]
    low: relay_strap_LP
    cage: relay_strap_CAGE
    material_set: relay_strap_MAT
matching:
  strategy: name_based
  suffixes: [_HP, _LP, _CAGE]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sets :** coque et sangle sont isolées.

- **High :** plusieurs sources peuvent alimenter une cible.

- **Cage :** chaque low possède sa cage correspondante.

- **Noms :** les suffixes rendent la correspondance déterministe.

## 36. Images cibles et sauvegarde

Blender bake vers le nœud Image Texture actif ou une cible explicitement configurée. L’image doit exister, avoir la
bonne résolution, le bon format, le bon espace de données et être enregistrée. Une image non sauvegardée peut être
perdue à la fermeture.

Chaque carte possède un nom, une version et un statut. Les cartes de données ne sont pas traitées comme des images de
couleur.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bake_targets:
  normal:
    file: AST-BAKE-PILOT-RELAY-001_normal_v001.exr
    data_role: tangent_normal
    color_space: non_color
    saved_before_bake: true
  ao:
    file: AST-BAKE-PILOT-RELAY-001_ao_v001.exr
    data_role: ambient_occlusion
    color_space: non_color
    saved_before_bake: true
  curvature:
    file: AST-BAKE-PILOT-RELAY-001_curvature_v001.exr
    data_role: authoring_mask
    color_space: non_color
    saved_before_bake: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fichiers :** les noms incluent asset, rôle et version.

- **Espace :** les cartes numériques utilisent `non_color`.

- **Sécurité :** les images sont enregistrées avant le calcul.

- **Rôle :** la curvature reste un masque d’auteur, pas une donnée physique runtime.

## 37. Selected to Active

Le bake Selected to Active projette les sources sélectionnées vers l’objet actif low poly. L’ordre de sélection et
l’objet actif doivent être vérifiés avant chaque lot. Une automatisation peut réduire les erreurs, mais elle doit
encore confirmer les noms et les cibles.

Les rayons partent de la surface de projection définie par le low ou sa cage. Un mauvais objet actif peut écrire une
carte vide ou projeter vers la mauvaise topologie.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
selected_to_active_check:
  selected_sources:
    - relay_shell_HP
    - relay_fasteners_HP
  active_target: relay_shell_LP
  selected_to_active: true
  cage: relay_shell_CAGE
  target_image_node: BAKE_normal_active
  preflight_result: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** les sources high sont listées.

- **Actif :** la cible low est explicite.

- **Cage :** la projection utilise la cage dédiée.

- **Préflight :** le bake reste bloqué tant que la vérification n’est pas exécutée.

## 38. Cage automatique et cage manuelle

Une cage est une version gonflée du low poly depuis laquelle les rayons sont lancés. Blender peut la calculer par
extrusion ou utiliser un objet manuel. Une cage manuelle devient utile lorsque l’extrusion uniforme traverse des
pièces, rate des concavités ou capture des détails voisins.

La cage manuelle doit conserver exactement la même topologie et le même ordre de faces que le low poly. Elle peut
déplacer les sommets, mais ne doit pas ajouter, supprimer ou réordonner les faces.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
cage_policy:
  automatic:
    use_when: uniform_clearance_and_simple_surface
    parameter: cage_extrusion
  manual:
    use_when: [concavity, nearby_parts, thin_geometry, local_projection_control]
    topology_must_match_low: true
    face_order_must_match_low: true
    object: relay_shell_CAGE
  review:
    intersections: forbidden
    high_poly_coverage: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Automatique :** l’extrusion uniforme convient aux formes simples.

- **Manuelle :** elle traite les concavités et pièces proches.

- **Invariant :** topologie et ordre des faces correspondent au low.

- **Couverture :** la cage doit envelopper les détails utiles sans intersection.

## 39. Max Ray Distance et extrusion

Sans cage, Max Ray Distance contrôle la distance de lancement des rayons. Avec une cage, Cage Extrusion ou l’objet
cage définit la surface de départ. Une grande valeur ne corrige pas automatiquement un bake : elle augmente le risque
de capturer une autre pièce.

La distance est mesurée sur les écarts réels entre high et low et testée par sous-ensemble. Les valeurs numériques
restent absentes de ce document tant que le pilote n’existe pas.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ray_profile:
  mode: cage_object_candidate
  max_ray_distance:
    active_when_cage_disabled: true
    value: pending_measurement
  cage_extrusion:
    active_when_auto_cage: true
    value: pending_measurement
  rejection:
    arbitrary_large_distance: true
    one_value_for_all_components: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode :** la cage objet est le candidat principal du pilote.

- **Distance :** Max Ray Distance n’est actif que sans cage.

- **Mesure :** les valeurs sont dérivées de la géométrie réelle.

- **Refus :** une valeur large ou universelle est interdite.

## 40. Correspondance par noms

La correspondance par noms évite les projections entre pièces voisines qui partagent la même scène. Les suffixes sont
retirés pour trouver une base commune. Le validateur refuse un high sans low, deux lows pour la même base ou une cage
dont la base ne correspond pas.

Le nommage ne remplace pas le contrôle spatial. Deux pièces bien nommées peuvent encore produire une cage incorrecte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from __future__ import annotations

from collections import defaultdict

SUFFIXES = ("_HP", "_LP", "_CAGE")

def split_role(name: str) -> tuple[str, str]:
    for suffix in SUFFIXES:
        if name.endswith(suffix):
            return name[:-len(suffix)], suffix[1:]
    raise ValueError(f"Rôle de bake absent : {name}")

def build_bake_index(names: list[str]) -> dict[str, dict[str, list[str]]]:
    index: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for name in names:
        base, role = split_role(name)
        index[base][role].append(name)
    return {base: dict(roles) for base, roles in index.items()}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `names` contient les objets du lot de bake.

- **Types :** la fonction retourne une base et un rôle textuel puis un index imbriqué.

- **Erreur :** un objet sans suffixe connu provoque `ValueError` au lieu d’être deviné.

- **Sortie :** l’index permet de vérifier cardinalité et correspondance avant le bake.

## 41. Normale tangentielle

Une normale tangentielle encode une perturbation relative à la surface du low poly. Elle dépend donc des UV, des
normales, des tangentes et de la triangulation. Modifier l’un de ces éléments après le bake peut changer le rendu.

Pour un objet déformable, la normale tangentielle suit la surface pendant l’animation. Une normale objet ne possède
pas la même propriété et reste réservée à des cas spécialisés ou au diagnostic.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
normal_bake:
  space: tangent
  low_state:
    uv_locked: true
    normals_locked: true
    triangulation_locked: true
    tangents_generated_or_exported: true
  deformation_compatibility:
    strap_candidate: tangent_required
  object_space_normal:
    runtime_default: false
    diagnostic_use: allowed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Espace :** le pilote utilise une normale tangentielle.

- **Dépendances :** UV, normales, triangles et tangentes sont figés.

- **Déformation :** la sangle nécessite un repère relatif à la surface.

- **Diagnostic :** la normale objet peut isoler un problème sans devenir le défaut runtime.

## 42. Orientation OpenGL et canal vert

Godot exige des normales OpenGL orientées `X+`, `Y+`, `Z+`. Une carte DirectX utilise généralement l’orientation
opposée pour Y et produit des creux qui deviennent bosses ou l’inverse. Godot peut convertir une carte existante avec
l’option d’import `Normal Map Invert Y`.

Le pipeline choisit une orientation canonique plutôt que de corriger chaque asset au hasard. Pour Project Asteria, le
bake cible directement OpenGL ; l’inversion reste un outil de migration.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
normal_orientation:
  canonical: OpenGL
  axes: [X_plus, Y_plus, Z_plus]
  blender_bake: configure_for_canonical
  godot_import:
    normal_map: enabled_or_detected
    invert_y: false_by_default
  migration_from_directx:
    invert_y: true
    record_conversion: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canon :** la collection adopte OpenGL comme orientation unique.

- **Godot :** l’import normal map est activé ou détecté.

- **Défaut :** aucune inversion n’est appliquée aux cartes canoniques.

- **Migration :** la conversion DirectX est enregistrée explicitement.

## 43. Ambient Occlusion

L’AO bakée décrit une occlusion locale dépendante du high et du low au moment du calcul. Elle ne remplace pas
l’éclairage dynamique et ne doit pas assombrir arbitrairement les zones exposées. Les chevauchements UV et les pièces
démontables doivent être examinés.

Le chapitre 16 définit l’usage du canal AO dans le matériau. Ici, le contrôle porte sur la projection, la portée, le
bruit et les contacts indésirables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ao_bake:
  role: local_occlusion_reference
  static_configuration_only: true
  checks:
    - no_unrelated_part_shadowing
    - no_cage_leak
    - removable_parts_reviewed
    - overlap_compatibility_reviewed
  distance: pending_measurement
  material_usage: inherited_from_chapter_16
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle :** l’AO est une référence locale et non un éclairage complet.

- **Configuration :** elle reflète l’assemblage au moment du bake.

- **Contrôles :** les ombres entre pièces non liées sont recherchées.

- **Frontière :** son branchement matériel reste défini au chapitre 16.

## 44. Curvature

La curvature est principalement un masque de lookdev pour détecter crêtes et creux. Elle peut guider usure, poussière
ou variation, mais ne doit pas imposer automatiquement une histoire matérielle. Une arête exposée n’est pas forcément
usée.

Le bake est contrôlé pour éviter les bandes, le bruit excessif et les ruptures aux seams. Les décisions artistiques
restent humaines.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
curvature_bake:
  role: authoring_mask
  runtime_required: false
  uses:
    - edge_wear_candidate
    - cavity_dirt_candidate
    - procedural_selection
  automatic_final_wear: forbidden
  review:
    banding: required
    seam_discontinuity: required
    scale_consistency: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Masque :** la curvature aide la sélection pendant le lookdev.

- **Runtime :** elle n’est pas obligatoirement livrée au moteur.

- **Interdiction :** aucune usure finale n’est générée sans cause.

- **Contrôle :** banding, seams et échelle sont inspectés.

## 45. Cartes auxiliaires

Les cartes ID, position, épaisseur ou height peuvent soutenir la peinture et les effets. Leur production dépend du
besoin et du logiciel de destination. Elles ne sont pas générées par habitude.

Chaque carte auxiliaire indique si elle est une source d’auteur, une texture runtime ou un intermédiaire supprimable.
Le manifeste empêche de livrer des fichiers inutilisés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
auxiliary_maps:
  material_id:
    purpose: authoring_selection
    runtime: false
  position:
    purpose: procedural_authoring_candidate
    runtime: false
  thickness:
    purpose: subsurface_authoring_candidate
    runtime: pending_material_need
  height:
    purpose: inherited_pbr_need
    runtime: pending_chapter_16_profile
  generation_policy: demand_driven
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** les IDs facilitent les masques de matériaux.

- **Procédural :** position et épaisseur restent des aides candidates.

- **Height :** son rôle vient du profil PBR.

- **Politique :** aucune carte n’est produite sans consommateur identifié.

## 46. Données linéaires et format de sortie

Normales, AO, curvature et masques sont des données. Elles ne doivent pas recevoir une transformation sRGB. Le format
de travail peut conserver davantage de précision ; le format de livraison dépend des profils du chapitre 16 et de
l’import Godot.

Une conversion finale est comparée visuellement à la source de travail afin de détecter banding ou artefacts de
compression.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bake_data_policy:
  normal:
    color_space: non_color
    working_format: high_precision_candidate
  ao:
    color_space: non_color
    working_format: high_precision_candidate
  curvature:
    color_space: non_color
    working_format: high_precision_candidate
  delivery:
    format: inherited_from_chapter_16
    compare_to_working_source: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Données :** les cartes évitent la transformation sRGB.

- **Travail :** un format de précision supérieure peut être conservé.

- **Livraison :** le format final dépend du profil PBR.

- **Comparaison :** la conversion est contrôlée contre la source.

## 47. Dilation de bake

Blender génère une marge autour des îlots pour éviter les discontinuités lors du filtrage et des mipmaps. `Extend`
prolonge les pixels de bord ; `Adjacent Faces` utilise les faces voisines à travers les seams. Le choix doit être
testé avec le type de carte.

Une marge insuffisante apparaît souvent seulement à distance ou après compression. Le contrôle ne se limite pas à la
texture pleine résolution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bake_dilation:
  normal:
    margin_type: adjacent_faces_candidate
    pixels: pending
  ao:
    margin_type: extend_candidate
    pixels: pending
  tests:
    - source_resolution
    - reduced_mip_candidate
    - godot_compressed_import
  bleed_tolerance: none_visible
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Par carte :** normale et AO peuvent utiliser des stratégies différentes.

- **Pixels :** la valeur reste liée à la résolution.

- **Tests :** mipmaps et import compressé sont inclus.

- **Tolérance :** aucune fuite visible n’est acceptée.

## 48. Anticrénelage et suréchantillonnage

Le bake peut être réalisé à une résolution de travail supérieure puis réduit avec un filtre contrôlé, ou utiliser les
options d’échantillonnage disponibles. Cette technique peut améliorer les diagonales et petits détails, mais elle ne
corrige pas une cage ou des UV défectueux.

Le coût mémoire et le temps de calcul doivent être relevés. Le profil reste candidat jusqu’à exécution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
sampling_profile:
  target_resolution: pending
  bake_resolution_multiplier: candidate
  downsample_filter: documented_if_used
  evaluate:
    - diagonal_edges
    - small_fasteners
    - seam_stability
    - memory_cost
    - bake_duration
  status: not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résolution :** la cible finale reste distincte de la résolution de travail.

- **Filtre :** toute réduction est documentée.

- **Qualité :** diagonales, petits détails et seams sont comparés.

- **Coût :** mémoire et durée sont mesurées lors de l’exécution.

## 49. Rayons obliques et skew

Un rayon trop oblique peut déplacer un détail sur le low poly, notamment près d’un angle ou d’une transition. Une cage
locale, une géométrie low mieux alignée ou la séparation du bake set peut réduire le skew. Ajouter des détails high
plus forts n’est pas une correction fiable.

Les motifs circulaires, vis et rainures servent de repères : leur déformation révèle rapidement une projection
oblique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skew_diagnostic:
  reference_details: [circular_fastener, straight_panel_line, screen_border]
  symptoms:
    - oval_fastener
    - bent_line
    - shifted_border
  correction_candidates:
    - local_cage_adjustment
    - low_surface_alignment
    - bake_set_separation
    - explicit_low_geometry
  status: pending_visual_test
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repères :** des formes simples rendent le skew visible.

- **Symptômes :** ovales et lignes déplacées signalent la projection.

- **Corrections :** la cage, le low ou le set sont ajustés.

- **Réserve :** aucune correction n’est validée sans test.

## 50. Géométries fines et surfaces proches

Les sangles, plaques fines et parois proches peuvent recevoir des rayons depuis la face opposée. Une cage manuelle,
une séparation des faces ou un bake set dédié peut être nécessaire. Les normales des faces et l’épaisseur du low
doivent être vérifiées.

Le backface culling dans le viewport aide à repérer les orientations, mais le bake doit être contrôlé par résultat et
non par affichage seul.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
thin_geometry_review:
  components: [relay_strap, screen_guard, shell_lip]
  risks:
    - opposite_side_capture
    - cage_self_intersection
    - inverted_face
    - insufficient_thickness
  mitigation:
    - separate_bake_set
    - manual_cage
    - explicit_thickness
    - normal_orientation_check
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Composants :** les surfaces fines sont identifiées avant le bake.

- **Risques :** capture opposée et auto-intersection sont recherchées.

- **Réponse :** le set, la cage ou l’épaisseur peuvent être modifiés.

- **Normales :** l’orientation des faces est vérifiée.

## 51. Miroir et normales tangentes

Les UV miroir économisent de l’espace, mais ils peuvent révéler des différences de tangentes, de texte ou d’usure. La
symétrie doit être testée après export et sous rotation de la lumière. Un bake correct dans Blender peut encore
diverger si les tangentes ne sont pas exportées ou régénérées de la même manière.

Les composants asymétriques du pilote conservent des UV uniques. Les fixations strictement identiques peuvent être
empilées après comparaison.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
mirrored_uv_test:
  candidate_group: strap_fastener_pair
  required_checks:
    - blender_tangent_normal
    - gltf_export_with_tangents
    - godot_import
    - rotating_key_light
  forbid_when:
    - text_or_logo
    - asymmetric_wear
    - unique_ao
  decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Candidat :** seule une paire réellement identique est étudiée.

- **Chaîne :** Blender, glTF et Godot sont comparés.

- **Éclairage :** la rotation révèle les inversions de relief.

- **Interdiction :** texte, usure ou AO unique imposent des UV uniques.

## 52. Material sets et images multiples

Un asset peut utiliser plusieurs material sets lorsque la résolution, la transparence ou la fonction l’exigent. Le
nombre de matériaux influence les draw calls et doit rester justifié. Le chapitre 16 définit les familles de matériaux
; ici, le découpage doit correspondre aux UV et aux bakes.

Les surfaces de l’écran ne sont pas séparées dans un matériau unique uniquement pour gagner quelques texels sans
mesurer le coût.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
material_sets:
  relay_shell_MAT:
    components: [shell, cap, fasteners]
    uv_map: UV_Primary
    bake_set: relay_shell
  relay_strap_MAT:
    components: [strap, buckle_candidate]
    uv_map: UV_Primary
    bake_set: relay_strap
  screen_MAT:
    separate: pending_need
    reason_required: [shader_behavior, transparency, resolution]
  draw_call_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Alignement :** matériau, UV et bake set partagent les mêmes frontières.

- **Sangle :** son set peut rester séparé pour la projection et le matériau.

- **Écran :** la séparation exige une raison technique.

- **Coût :** les draw calls sont examinés avant acceptation.

## 53. Versionnement des sorties

Les bakes sont des sorties reproductibles liées à une version du high, du low, de la cage, des UV, des paramètres et
du logiciel. Écraser une texture approuvée détruit cette traçabilité. Une nouvelle version est créée lorsque l’un de
ces éléments change.

Le manifeste conserve les empreintes de fichiers et les paramètres. Une empreinte détecte une modification ; elle ne
prouve ni qualité artistique ni validité juridique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bake_manifest:
  asset_id: AST-BAKE-PILOT-RELAY-001
  bake_version: v001
  blender_version: 5.2.0
  inputs:
    high_sha256: pending
    low_sha256: pending
    cage_sha256: pending
    uv_layout_sha256: pending
  parameters_sha256: pending
  outputs:
    normal_sha256: pending
    ao_sha256: pending
    curvature_sha256: pending
  approval: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** le bake possède sa propre version.

- **Entrées :** high, low, cage et UV sont liés par empreinte.

- **Sorties :** chaque texture reçoit une empreinte distincte.

- **Limite :** l’approbation humaine reste séparée des hashes.

## 54. Contrôle Blender

Le contrôle Blender utilise un matériau neutre, les textures bakées, plusieurs éclairages et une rotation de l’objet.
La comparaison high/low est faite à la même caméra. Les seams, gradients, projection et détails fins sont inspectés.

Un mode matcap peut aider à diagnostiquer la géométrie, mais la validation finale utilise un matériau proche du
runtime et des tangentes exportables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
blender_review_scene:
  id: AST-BAKE-REVIEW-BLENDER-001
  cameras: [front, profile, three_quarter, glancing, strap_bend_candidate]
  lights: [soft_neutral, hard_glancing, rotating_key_candidate]
  comparisons:
    - high_reference
    - low_without_bakes
    - low_with_bakes
  result: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scène :** un identifiant stable permet de reproduire les captures.

- **Caméras :** les vues ciblent silhouette, seams et déformation.

- **États :** le low est comparé avec et sans textures.

- **Résultat :** aucun passage n’est déclaré avant exécution.

## 55. Export glTF et tangentes

Godot recommande glTF 2.0. Les normales, UV et tangentes nécessaires doivent être exportées. Si les tangentes sont
absentes, Godot peut les générer avec MikkTSpace via `Ensure Tangents`, mais la documentation recommande de laisser
l’outil 3D les générer quand c’est possible.

Le manifeste enregistre si les tangentes viennent de Blender ou de Godot. Changer de générateur exige une nouvelle
comparaison.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gltf_export:
  container: GLB
  object: AST-BAKE-PILOT-RELAY-001_LP
  include:
    normals: true
    uv_primary: true
    tangents: true
    materials: reference_only
  triangulation: locked
godot_import:
  ensure_tangents: fallback_only
  tangent_source: blender_export_candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** GLB est le conteneur d’échange par défaut.

- **Données :** normales, UV et tangentes sont incluses.

- **Fallback :** Godot génère les tangentes seulement si nécessaire.

- **Comparaison :** la source des tangentes est enregistrée.

## 56. Import Godot et normale

La normale est importée comme normal map afin d’utiliser une compression adaptée aux canaux rouge et vert. Godot
reconstruit ou ignore le bleu dans ses matériaux intégrés selon le format. L’option Invert Y reste désactivée pour la
carte OpenGL canonique.

Les fichiers `.import` contiennent les paramètres et sont versionnés, tandis que le dossier `.godot` généré ne l’est
pas.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
godot_texture_import:
  normal:
    compress_normal_map: enabled_or_detected
    normal_map_invert_y: false
    mipmaps_generate: true
    repeat: inherited_material_need
  ao:
    normal_map_mode: false
    color_space: linear_data
  version_control:
    commit_import_files: true
    commit_dot_godot_folder: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Compression :** la normale utilise le profil normal map.

- **Orientation :** Invert Y reste faux pour OpenGL.

- **Mipmaps :** leur génération est incluse dans le contrôle de marges.

- **Versionnement :** les paramètres `.import` sont conservés, pas le cache `.godot`.

## 57. Validateur structurel Godot

Un validateur peut vérifier que le mesh possède une carte UV, des normales et des tangentes, puis signaler les
surfaces sans matériau. Il ne juge pas la qualité visuelle du bake et ne remplace pas les captures comparatives.

Le script suivant illustre une inspection de `ArrayMesh`. Les indices de tableau sont des constantes Godot et les
vérifications restent bloquées tant que la scène n’est pas matérialisée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
extends Node

func validate_mesh(mesh: Mesh) -> PackedStringArray:
    var issues := PackedStringArray()
    if mesh == null:
        issues.append("mesh_missing")
        return issues

    for surface_index in range(mesh.get_surface_count()):
        var arrays := mesh.surface_get_arrays(surface_index)
        if arrays[Mesh.ARRAY_VERTEX].is_empty():
            issues.append("surface_%d_vertices_missing" % surface_index)
        if arrays[Mesh.ARRAY_NORMAL].is_empty():
            issues.append("surface_%d_normals_missing" % surface_index)
        if arrays[Mesh.ARRAY_TANGENT].is_empty():
            issues.append("surface_%d_tangents_missing" % surface_index)
        if arrays[Mesh.ARRAY_TEX_UV].is_empty():
            issues.append("surface_%d_uv_missing" % surface_index)
        if mesh.surface_get_material(surface_index) == null:
            issues.append("surface_%d_material_missing" % surface_index)
    return issues
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** `mesh` reçoit la ressource à inspecter.

- **Retour :** un `PackedStringArray` accumule des identifiants de problèmes.

- **Boucle :** chaque surface est vérifiée indépendamment.

- **Limite :** le script contrôle la structure, pas la qualité des pixels.

## 58. Scène comparative Godot

La scène Godot reprend des caméras et éclairages comparables à Blender. Elle affiche le low importé avec sa normale,
puis une variante sans normale pour isoler les effets. Une lumière tournante révèle les inversions et discontinuités
tangentielles.

Le rendu est contrôlé avec le renderer de référence Forward+. Aucun résultat n’est inventé dans ce document.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
AST-BAKE-REVIEW-GODOT-001
├── WorldEnvironment
├── NeutralFloor
├── CameraFront
├── CameraProfile
├── CameraGlancing
├── LightSoftNeutral
├── LightHardGlancing
├── LightRotatingCandidate
├── RelayWithBakes
└── RelayWithoutNormal
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** la scène contient les deux états du même asset.

- **Caméras :** les vues correspondent aux défauts recherchés.

- **Lumières :** une clé tournante teste le relief tangent.

- **Comparaison :** les différences sont attribuées à la normale plutôt qu’à la géométrie.

## 59. Manifeste de captures

Chaque capture conserve commit, scène, caméra, renderer, matériau, tangent source et options d’import. Une image sans
ce contexte ne peut pas servir de preuve durable. Les captures Blender et Godot utilisent des noms liés.

Le rapport compare aussi les anomalies observées et leur classification.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```csv
capture_id,commit,application,scene,camera,renderer,tangent_source,normal_orientation,import_profile,result,notes
pending,pending,Blender,AST-BAKE-REVIEW-BLENDER-001,front,Cycles_or_Eevee_candidate,Blender,OpenGL,not_applicable,pending,not_executed
pending,pending,Godot,AST-BAKE-REVIEW-GODOT-001,front,Forward+,Blender_export,OpenGL,normal_profile,pending,not_executed
pending,pending,Godot,AST-BAKE-REVIEW-GODOT-001,glancing,Forward+,Godot_fallback_candidate,OpenGL,normal_profile,pending,not_executed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** commit, application, scène et caméra rendent la capture reproductible.

- **Tangentes :** la source Blender ou fallback Godot est enregistrée.

- **Orientation :** OpenGL est explicitement conservé.

- **Statut :** `pending` et `not_executed` interdisent une fausse preuve.

## 60. Rapport de contrôle

Le rapport distingue défaut, localisation, hypothèse, correction appliquée, nouvelle version et décision. Une
correction ne remplace pas la preuve : le cas est recapturé après modification.

Les erreurs de topologie, UV, cage, bake, import et matériau sont classées séparément pour éviter de modifier
plusieurs variables à la fois.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
review_issue:
  id: BAKE-ISSUE-pending
  asset: AST-BAKE-PILOT-RELAY-001
  category: [topology, uv, cage, bake, tangent, import, material]
  location: pending
  symptom: pending
  hypothesis: pending
  changed_variable: one_only
  correction_commit: pending
  recapture_ids: []
  decision: open
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catégorie :** le défaut est rattaché à une étape précise.

- **Hypothèse :** la cause supposée reste distincte du symptôme.

- **Expérience :** une seule variable est modifiée par essai.

- **Clôture :** des captures nouvelles sont requises avant décision.

## 61. Préflight automatisé Blender

Une automatisation peut vérifier noms, suffixes, cartes UV, images cibles et correspondances. Elle ne doit pas lancer
un bake définitif si une condition est ambiguë. Le script s’arrête sur les erreurs et produit un rapport lisible.

Le pseudo-script suivant montre la logique ; il n’est pas annoncé comme exécuté dans Blender.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from __future__ import annotations

def validate_bake_group(group: dict[str, object]) -> list[str]:
    issues: list[str] = []
    high = group.get("high", [])
    low = group.get("low")
    cage = group.get("cage")
    uv_name = group.get("uv_name")

    if not isinstance(high, list) or not high:
        issues.append("high_missing")
    if not isinstance(low, str) or not low.endswith("_LP"):
        issues.append("low_invalid")
    if cage is not None and (not isinstance(cage, str) or not cage.endswith("_CAGE")):
        issues.append("cage_invalid")
    if uv_name != "UV_Primary":
        issues.append("uv_primary_missing")
    return issues
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le groupe fournit high, low, cage et nom UV.

- **Types :** chaque champ est vérifié avant usage.

- **Erreurs :** les identifiants sont accumulés au lieu de deviner des valeurs.

- **Limite :** la fonction ne lance ni Blender ni bake.

## 62. Coûts et budget

La retopologie réduit le coût géométrique, mais le bake ajoute des textures, tangentes et parfois plusieurs material
sets. Le budget doit donc inclure triangles, sommets après splits, UV, tangentes, mémoire texture et draw calls. Un
low poly avec trop de seams ou hard edges peut générer davantage de sommets GPU que le compteur de sommets Blender ne
le suggère.

Le chapitre 18 mesurera les profils LOD. Ici, le rapport produit l’état de base de l’asset final.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asset_cost_baseline:
  triangles: pending
  vertices_blender: pending
  vertices_exported: pending
  uv_islands: pending
  hard_normal_splits: pending
  material_slots: pending
  texture_memory_imported: pending
  tangent_array_present: pending
  draw_calls_reference_scene: pending
  owner_of_lod_comparison: chapter_18
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Géométrie :** triangles et sommets exportés sont relevés séparément.

- **Splits :** UV et normales peuvent multiplier les sommets GPU.

- **Textures :** la mémoire importée complète le coût.

- **Frontière :** la comparaison LOD reste au chapitre 18.

## 63. Provenance et droits

Le high poly, les alphas, brushes, scans et textures de support possèdent une provenance. Le bake ne nettoie pas
juridiquement une source : une texture dérivée peut encore dépendre de droits insuffisants. Les preuves restent liées
au chapitre 5.

Les cartes générées reçoivent un lien vers leurs entrées et leur workflow. Aucun contrat ou document personnel n’est
placé dans le dépôt public.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
provenance:
  asset_id: AST-BAKE-PILOT-RELAY-001
  high_poly_sources:
    status: pending_qualification
  brushes_and_alphas:
    status: pending_qualification
  scan_inputs:
    status: not_declared
  generated_maps:
    derived_from: [high_poly, low_poly, cage, uv_layout, bake_parameters]
    legal_review: pending
  public_repository_contains_contracts: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** high poly, brushes et scans sont qualifiés séparément.

- **Dérivation :** les cartes bakées référencent toutes leurs entrées.

- **Juridique :** le bake n’efface pas les obligations de licence.

- **Confidentialité :** les contrats ne sont pas stockés publiquement.

## 64. Modes Solo et Mode Studio

### Mode Solo

Le parcours Solo utilise un seul asset pilote et limite les cartes aux besoins identifiés. La retopologie, les UV, la
cage et le bake sont réalisés dans un ordre fixe. Les corrections sont regroupées par cause et le rapport conserve
uniquement les mesures utiles. Un profil canonique de normale OpenGL et un seul export GLB réduisent les variantes.

Le Solo ne multiplie pas les outils ni les résolutions avant d’avoir validé la chaîne complète Blender–Godot.

### Mode Studio

Le parcours Studio peut séparer sculpt, retopologie, UV, lookdev et intégration. Chaque transfert utilise les portes
du chapitre : high gelé, low stabilisé, UV approuvés, cage vérifiée, bakes contrôlés et import moteur comparé. Les
bake sets, paramètres, scripts et rapports sont versionnés.

Une revue croisée est requise pour les actifs héros, les déformations, les exceptions de densité et les chevauchements
intentionnels. Les matrices par plateforme restent coordonnées avec les chapitres 16 et 18.

## 65. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 65.1 Utiliser un remesh automatique pour une sangle déformable

**Symptôme :** la sangle paraît régulière au repos mais se pince et tourne de façon imprévisible dès qu’une flexion est simulée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
strap_retopology:
  method: automatic_remesh
  deformation_analysis: skipped
  longitudinal_flow: ignored
  poles: anywhere
  result: accepted_by_polygon_count
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le remesh ne connaît ni l’axe de flexion ni les attaches ; une densité uniforme et des pôles arbitraires ne constituent pas un edge flow déformable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
strap_retopology:
  method: manual_guided
  longitudinal_flow: continuous
  attachment_transitions: reinforced
  poles: outside_primary_bend
  bend_test: required
  result: pending_deformation_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les boucles suivent la longueur, les attaches reçoivent une transition et les pôles quittent la flexion principale ; l’acceptation dépend d’un test.

### 65.2 Baker avant de figer la triangulation

**Symptôme :** la normale semble correcte dans Blender puis produit des diagonales visibles après export.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
final_bake:
  low_topology: editable
  triangulation: automatic_at_export
  normals: may_change
  uv: may_repack
  bake_status: final
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le repère tangent dépend des UV, normales et triangles ; laisser ces données changer après le bake rend la texture incohérente avec le mesh exporté.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
final_bake:
  low_topology: frozen
  triangulation: locked_before_bake
  normals: frozen
  uv: frozen
  export_uses_same_mesh_state: true
  bake_status: candidate_until_engine_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le bake et l’export partagent le même état géométrique, puis la carte reste candidate jusqu’à comparaison dans Godot.

### 65.3 Confondre arête dure et seam UV

**Symptôme :** des gradients cassent aux biseaux et des seams supplémentaires apparaissent sur des surfaces visuellement continues.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
edge_policy:
  every_hard_edge_is_uv_seam: true
  every_uv_seam_is_hard_edge: true
  reasons: none
  tangent_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les deux mécanismes ont des responsabilités différentes ; les coupler partout augmente splits et marges sans garantir un meilleur bake.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
edge_policy:
  decisions_per_edge:
    hard_normal_reason: surface_angle_or_shading
    uv_seam_reason: unwrap_or_visibility
  combinations_allowed: [both, hard_only, seam_only, neither]
  tangent_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque choix est justifié séparément et les quatre combinaisons restent possibles avant le test tangent.

### 65.4 Utiliser une marge nulle

**Symptôme :** des couleurs ou normales étrangères apparaissent aux seams lorsque la caméra s’éloigne.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
uv_and_bake_margin:
  pack_pixels: 0
  bake_pixels: 0
  mip_test: skipped
  compressed_import_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le filtrage, les mipmaps et la compression échantillonnent au-delà des îlots ; sans dilation, les pixels voisins contaminent les bordures.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
uv_and_bake_margin:
  pack_pixels: derived_from_resolution
  bake_pixels: derived_from_resolution_and_mips
  mip_test: required
  compressed_import_test: required
  result: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les marges sont liées à la résolution et vérifiées dans les conditions qui déclenchent réellement le bleeding.

### 65.5 Augmenter fortement la distance des rayons

**Symptôme :** les fixations et détails d’une pièce voisine apparaissent sur la coque.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
ray_cast:
  cage: disabled
  max_ray_distance: very_large
  per_component_profile: false
  contamination_review: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une distance excessive agrandit le volume de recherche et capture des surfaces sans rapport ; elle masque un problème de set ou de cage.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
ray_cast:
  cage: relay_shell_CAGE
  max_ray_distance: disabled_with_cage
  bake_set: relay_shell
  local_adjustments: reviewed
  contamination_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La cage et le set limitent la projection à la coque, tandis que les ajustements locaux sont inspectés.

### 65.6 Modifier la topologie de la cage

**Symptôme :** le bake échoue, se décale ou projette des détails sur des faces inattendues.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
manual_cage:
  source: duplicate_of_low
  added_edge_loops: true
  deleted_faces: true
  vertex_order_preserved: unknown
  status: accepted_if_enclosing
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une cage manuelle doit conserver la topologie et l’ordre des faces du low ; ajouter ou supprimer des éléments détruit la correspondance.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
manual_cage:
  source: exact_duplicate_of_low
  vertex_positions_adjusted: true
  topology_changed: false
  face_order_preserved: true
  intersection_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Seules les positions changent ; la correspondance topologique reste intacte et l’enveloppe est vérifiée.

### 65.7 Importer une normale DirectX sans conversion

**Symptôme :** les creux deviennent bosses dans Godot alors que la carte paraît correcte dans son outil d’origine.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
normal_map:
  source_orientation: DirectX
  godot_invert_y: false
  canonical_orientation: undefined
  visual_comparison: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Godot attend une normale OpenGL `X+, Y+, Z+` ; une carte DirectX possède un canal Y opposé.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
normal_map:
  source_orientation: DirectX
  canonical_orientation: OpenGL
  godot_invert_y: true
  conversion_recorded: true
  rotating_light_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’inversion Y convertit la carte vers l’orientation attendue et la lumière tournante vérifie le sens du relief.

### 65.8 Empiler des UV qui nécessitent des détails uniques

**Symptôme :** le texte est miroir et l’usure de gauche se répète exactement à droite.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
uv_overlap:
  shell_left_right: stacked
  text: asymmetric
  wear: unique
  ao: unique
  overlap_registry: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’empilement partage tous les pixels ; il est incompatible avec texte, usure et AO asymétriques.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
uv_overlap:
  shell_left_right: unique_islands
  strap_fastener_pair: stacked_candidate
  overlap_registry: required
  map_compatibility_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les surfaces asymétriques deviennent uniques, tandis qu’un groupe réellement identique reste seulement candidat après revue des cartes.

### 65.9 Baker vers une image active incorrecte

**Symptôme :** la texture attendue reste vide ou un ancien fichier est écrasé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
bake_target:
  active_image_node: unknown
  file_saved: false
  version: existing_approved
  preflight: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Blender écrit vers la cible active ; une cible ambiguë et non sauvegardée peut perdre le résultat ou écraser une version approuvée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
bake_target:
  active_image_node: BAKE_normal_active
  file_saved: true
  version: new_candidate
  expected_role: tangent_normal
  preflight: passed_before_bake
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La cible, le rôle et la nouvelle version sont confirmés avant le calcul, ce qui protège les sorties approuvées.

### 65.10 Valider uniquement dans Blender

**Symptôme :** la normale semble correcte dans le DCC mais présente des seams et gradients différents dans Godot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
acceptance:
  blender_review: passed
  gltf_export: not_compared
  godot_review: skipped
  tangent_source: unknown
  decision: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le rendu final dépend de l’export, des tangentes et de l’import ; Blender seul ne prouve pas la cohérence moteur.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
acceptance:
  blender_review: required
  gltf_export: same_frozen_mesh
  godot_review: required
  tangent_source: recorded
  rotating_light_comparison: required
  decision: pending_until_both_pass
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le même mesh figé est comparé dans les deux applications et la source des tangentes est documentée avant approbation.

## 66. Porte d’acceptation

Le pilote est accepté uniquement si les livrables du plan maître sont matérialisés et si les critères visuels sont
vérifiés dans Blender puis Godot. Une absence d’artefact majeur ne signifie pas perfection : les réserves, tolérances
et exceptions restent consignées.

La décision finale exige une revue humaine. Un validateur automatique peut bloquer un manque de structure, mais ne
peut pas décider seul que la silhouette, la déformation ou le shading sont satisfaisants.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  high_resolution_mesh: produced_and_versioned
  low_resolution_mesh: produced_and_versioned
  uv_and_cages: produced_and_reviewed
  baked_textures: produced_and_versioned
  control_report: complete
  topology:
    silhouette: passed
    strap_bend_candidate: passed
  uv:
    density: measured_and_within_profile
    margins: passed_mip_and_compression_test
    overlaps: classified
  bake:
    major_artifacts: none
    tangent_orientation: passed
  applications:
    blender: passed
    godot: passed
  human_approval: required
  current_status: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Livrables :** les cinq sorties du plan maître sont exigées.

- **Topologie :** silhouette et flexion candidate sont séparées.

- **UV et bake :** densité, marges, overlaps et tangentes sont contrôlés.

- **Décision :** le statut reste bloqué tant que les preuves n’existent pas.

## 67. Livrables du chapitre

Le chapitre prépare les livrables permanents suivants :

- un maillage haute résolution versionné ;
- un maillage basse résolution finalisé ;
- une carte UV principale et des cages correspondantes ;
- des textures bakées avec manifeste et empreintes ;
- un rapport de contrôle Blender–Godot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
production/AST-BAKE-PILOT-RELAY-001/
├── source/
│   ├── AST-BAKE-PILOT-RELAY-001_HP.blend
│   ├── AST-BAKE-PILOT-RELAY-001_LP.blend
│   └── AST-BAKE-PILOT-RELAY-001_CAGE.blend
├── textures/
│   ├── AST-BAKE-PILOT-RELAY-001_normal_v001.ext
│   ├── AST-BAKE-PILOT-RELAY-001_ao_v001.ext
│   └── AST-BAKE-PILOT-RELAY-001_curvature_v001.ext
├── exchange/
│   └── AST-BAKE-PILOT-RELAY-001_v001.glb
└── reports/
    ├── bake-manifest-v001.yaml
    └── control-report-v001.md
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** high, low et cage restent séparés et versionnés.

- **Textures :** les cartes portent rôle et version.

- **Échange :** le GLB représente l’état moteur candidat.

- **Rapports :** manifeste et contrôle rendent la chaîne traçable.

## 68. Sources officielles qualifiées

Les mécanismes du chapitre sont reliés aux documentations officielles. Les pages Blender 5.0 décrivent la retopologie
manuelle, Poly Build, le dépliage UV, Pack Islands, Average Island Scale, Minimize Stretch et les paramètres de bake.
La documentation Godot 4.7 décrit glTF, `Ensure Tangents`, l’import d’images, la compression des normales et
l’orientation OpenGL.

Les liens doivent être revérifiés lors d’une future mise à jour de version. Les exemples du chapitre restent des
contrats propres à Project Asteria.

- [Blender Manual — Retopology](https://docs.blender.org/manual/en/5.0/modeling/meshes/retopology.html)
- [Blender Manual — Poly Build](https://docs.blender.org/manual/en/5.0/modeling/meshes/tools/poly_build.html)
- [Blender Manual — UV Operators](https://docs.blender.org/manual/en/5.0/modeling/meshes/editing/uv.html)
- [Blender Manual — UV Editing](https://docs.blender.org/manual/en/5.0/modeling/meshes/uv/editing.html)
- [Blender Manual — Render Baking](https://docs.blender.org/manual/en/5.0/render/cycles/baking.html)
- [Godot 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)
- [Godot 4.7 — Import configuration](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html)
- [Godot 4.7 — Importing images](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_images.html)
- [Godot 4.7 — EditorSceneFormatImporter](https://docs.godotengine.org/en/4.7/classes/class_editorsceneformatimporter.html)

## 69. Conclusion

La qualité d’un bake dépend moins d’un bouton que de la stabilité de toute la chaîne : high lisible, low fonctionnel,
UV mesurés, cage adaptée, données linéaires, tangentes cohérentes et comparaison moteur. Une correction tardive d’UV,
de normales ou de triangulation exige un nouveau bake et une nouvelle preuve.

`AST-BAKE-PILOT-RELAY-001` fournit un contrat complet pour éprouver cette chaîne sans confondre documentation et
production. Tant que les fichiers, captures et mesures n’existent pas, le chapitre reste au niveau `static-review` et
toutes les performances ou qualités runtime demeurent réservées.

## 70. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-BAKE-PILOT-RELAY-001` comme étalon de retopologie, d’UV et de baking. Les sources haute résolution, basse résolution et cage restent séparées et versionnées ; le maillage final possède l’autorité sur la silhouette, la triangulation, les UV, les normales et les tangentes. Les profils statique et déformable sont qualifiés séparément afin qu’une optimisation locale ne dégrade ni les appuis ni les zones de flexion.

Le pipeline Asteria impose une densité de texels mesurée, des marges compatibles avec les mipmaps, des chevauchements explicitement autorisés, un espace tangent MikkTSpace et des normales OpenGL. Chaque bake possède un manifeste reliant sources, paramètres, cartes produites, empreintes et contrôle Blender–Godot. Une modification tardive de topologie, d’UV, de normales ou de triangulation invalide le bake précédent.

La porte reste bloquée tant que les fichiers high, low et cage, les textures, le GLB, les captures comparatives et le rapport de contrôle ne sont pas matérialisés. Le chapitre fixe donc le contrat opérationnel de Project Asteria sans revendiquer une qualité visuelle, une compatibilité de déformation ou une performance runtime mesurée.
