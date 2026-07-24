---
title: "Livre III — Chapitre 18 : LOD, imposteurs et optimisation géométrique"
id: "DOC-L3-CH18"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 18
last-verified: "2026-07-24T02:35:00+02:00"
audit-status: "complete"
audit-date: "2026-07-24T02:35:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-18.md"
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

# LOD, imposteurs et optimisation géométrique

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH18`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre



Le chapitre 17 a figé le maillage final, ses UV, sa triangulation, ses normales et ses textures bakées. Le présent chapitre construit ensuite une chaîne de représentations moins coûteuses qui conserve l’identité visuelle de l’asset lorsque sa taille à l’écran diminue. Il ne corrige pas une mauvaise retopologie et ne remplace pas la mesure globale du jeu réservée au Livre IV.

Le fil rouge utilise `AST-LOD-PILOT-SIGNAL-TOWER-001`, une tour de signalisation statique comportant un socle, une structure verticale, une plateforme, un boîtier technique, une antenne et des haubans. Sa silhouette reste reconnaissable à longue distance, tandis que ses détails internes offrent plusieurs niveaux de simplification.

Une chaîne LOD n’est pas une suite arbitraire de pourcentages. Chaque représentation possède une plage d’usage, un coût mesuré, une silhouette attendue, des matériaux, des ombres, une collision éventuelle et une règle de transition.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
Asset final approuvé
    ↓
Mesure du coût et de la taille écran
    ↓
Définition des budgets et plages
    ↓
Création LOD1, LOD2 et proxy lointain
    ↓
Imposteur ou billboard lorsque pertinent
    ↓
Collisions et ombres simplifiées
    ↓
Configuration Godot des transitions
    ↓
Benchmark avant/après
    ↓
Revue visuelle et porte d’acceptation
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Dépendance :** la chaîne commence après gel du LOD0 et des données du chapitre 17.



- **Progression :** chaque niveau est produit puis évalué avant de poursuivre vers une représentation plus pauvre.



- **Moteur :** Godot reçoit des plages et des dépendances explicites plutôt qu’une distance implicite non documentée.



- **Preuve :** la décision finale combine métriques, captures et revue humaine.



## 2. Résultats d’apprentissage



À la fin du chapitre, le lecteur saura relier la taille projetée d’un asset à un budget géométrique, choisir entre LOD manuel et LOD automatique, protéger la silhouette pendant la décimation, simplifier matériaux et collisions, créer un imposteur orienté, configurer les plages de visibilité Godot et construire un benchmark reproductible.

Le lecteur saura également reconnaître les cas où une réduction de triangles n’améliore pas le coût réel : multiplication des surfaces, sommets exportés, transparence, ombres, mauvaise AABB ou transitions trop fréquentes.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
learning_outcomes:
  budgets: [screen_size, gameplay_importance, platform]
  geometry: [manual_lod, automatic_lod, silhouette]
  proxies: [impostor, billboard, shadow, collision]
  godot: [visibility_ranges, hysteresis, lod_bias]
  evidence: [benchmark, captures, comparative_table]
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Budgets :** les seuils dépendent de la perception et de la plateforme.



- **Géométrie :** la réduction est contrôlée par la silhouette et le shading.



- **Proxies :** les représentations lointaines ont des responsabilités distinctes.



- **Évidence :** aucune optimisation n’est acceptée sans comparaison reproductible.



## 3. Niveau de preuve et réserves



Le chapitre est accepté au niveau `static-review`. Les procédures Blender, structures de fichiers, profils YAML, exemples Python, scènes Godot et scripts GDScript ont été relus comme contrats documentaires. Ils ne constituent pas une exécution de Blender, un export glTF, une génération d’imposteur, un benchmark ou une mesure GPU.

Les distances, ratios, tailles écran, budgets de triangles et seuils cités servent d’exemples candidats. Ils doivent être remplacés par des valeurs issues du projet réel, de la caméra réelle et du matériel de référence.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
evidence_level:
  chapter: static-review
  blender_execution: false
  godot_execution: false
  benchmark_executed: false
  captures_produced: false
  pdf_produced: false
  candidate_values_are_final: false
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Statut :** la validation porte sur la cohérence documentaire.



- **Exécution :** aucun outil 3D ou moteur n’est présenté comme lancé.



- **Mesures :** les nombres du chapitre restent des points de départ.



- **Publication :** le PDF du Livre III reste différé à la fin du livre.



## 4. Frontières avec les chapitres voisins



Le chapitre 17 demeure propriétaire du low poly final, des UV, des cages et du baking. Le chapitre 19 prend en charge squelette, skinning et déformations. Le chapitre 28 traitera l’intégration globale des assets dans Godot. Les systèmes de gameplay qui choisissent une qualité ou une distance restent dans le Livre II, tandis que l’optimisation transversale du jeu appartient au Livre IV.

Le présent chapitre peut définir un proxy de collision ou d’ombre pour un niveau lointain, mais ne redéfinit ni la navigation, ni la physique complète, ni la politique de streaming du monde.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
ownership:
  chapter_17: final_mesh_uv_bake
  chapter_18: lod_chain_impostors_geometry_benchmark
  chapter_19: rigging_skinning
  chapter_28: global_godot_asset_integration
  book_ii: gameplay_authority
  book_iv: whole_game_optimization
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Amont :** le LOD0 provient du chapitre 17.



- **Présent :** la chaîne de représentations et ses preuves sont l’autorité du chapitre.



- **Aval :** rigging et intégration globale conservent leurs responsabilités.



- **Exclusion :** aucune règle gameplay ou optimisation globale n’est déplacée ici.



## 5. Pilote de production



`AST-LOD-PILOT-SIGNAL-TOWER-001` est choisi parce qu’il combine grandes masses, détails répétitifs, éléments fins et silhouette asymétrique. Le socle et le boîtier éprouvent les surfaces planes ; l’antenne et les haubans éprouvent les éléments fins ; la plateforme permet de mesurer la disparition des détails internes.

Le pilote doit exister comme asset approuvé avant création de sa chaîne. Le chapitre ne prétend pas que ses fichiers ont été produits.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
asset:
  id: AST-LOD-PILOT-SIGNAL-TOWER-001
  category: static_landmark
  scale_meters: candidate
  gameplay_importance: navigation_landmark
  silhouette_features:
    - offset_platform
    - antenna_crown
    - asymmetric_service_box
  thin_features:
    - guy_wires
    - railings
  current_status: not_materialized
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Identité :** l’identifiant reste stable dans tous les fichiers et rapports.



- **Importance :** le rôle de repère visuel justifie une silhouette conservée plus longtemps.



- **Difficultés :** les éléments fins reçoivent des décisions explicites de conservation ou remplacement.



- **Réserve :** la production réelle du pilote reste bloquée.



## 6. Vocabulaire opérationnel



Un LOD est une représentation géométrique choisie selon un critère de visibilité. Un HLOD regroupe plusieurs objets en une représentation agrégée. Un imposteur remplace un volume par une ou plusieurs images capturées. Un billboard est un plan orienté vers la caméra ou autour d’un axe. Un proxy de collision ou d’ombre représente uniquement une responsabilité physique ou lumineuse.

Ces termes ne sont pas interchangeables : un imposteur peut être un billboard, mais un billboard peut aussi afficher une texture peinte sans capture volumétrique.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
LOD0      représentation proche approuvée
LOD1      simplification légère
LOD2      simplification forte
HLOD      agrégation de plusieurs instances
Imposteur capture visuelle d'un volume
Billboard plan orienté vers la caméra
Proxy     géométrie dédiée à une responsabilité
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **LOD :** les niveaux conservent l’identité d’un même asset.



- **HLOD :** l’agrégation vise aussi la réduction des instances et surfaces.



- **Imposteur :** la vue lointaine encode l’apparence plutôt que la géométrie complète.



- **Proxy :** collision, ombre et occlusion peuvent utiliser des géométries séparées.



## 7. Objectif perceptuel avant objectif numérique



La réduction de coût n’est utile que si l’erreur perceptuelle reste acceptable à la distance prévue. La silhouette, les ruptures de valeur, la lisibilité gameplay et les ombres dominantes sont évaluées avant le nombre de triangles.

Un asset de repérage peut conserver plus longtemps son antenne ou son contraste qu’un décor secondaire de même taille. Le profil encode cette importance plutôt que d’utiliser une règle universelle.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
perceptual_contract:
  primary_signal: silhouette
  secondary_signals:
    - large_value_breaks
    - navigation_readability
    - dominant_shadow
  removable_first:
    - hidden_backfaces
    - internal_fasteners
    - subpixel_bevels
  decision: visual_review_required
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Signal primaire :** la silhouette reste prioritaire pour un landmark.



- **Signaux secondaires :** les grandes masses visuelles guident la simplification.



- **Ordre :** les détails sous-pixel et invisibles disparaissent avant les contours.



- **Décision :** une revue humaine conclut sur l’acceptabilité.



## 8. Taille écran comme variable de décision



Une distance seule ne suffit pas : le champ de vision, la résolution, l’échelle de l’asset et la caméra modifient sa taille projetée. Le contrat utilise donc une hauteur relative ou un diamètre projeté, puis traduit ce signal en distances candidates pour une caméra donnée.

Les calculs pédagogiques servent à préparer les tests ; Godot doit ensuite confirmer le comportement avec la caméra réelle.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```python
from math import tan, radians

def projected_height_pixels(height_m: float, distance_m: float, vertical_fov_deg: float, viewport_height_px: int) -> float:
    if height_m <= 0.0 or distance_m <= 0.0 or viewport_height_px <= 0:
        raise ValueError("dimensions positives requises")
    frustum_height = 2.0 * distance_m * tan(radians(vertical_fov_deg) * 0.5)
    return height_m / frustum_height * viewport_height_px
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Paramètres :** `height_m`, `distance_m`, le FOV vertical et la hauteur du viewport décrivent le cas observé.



- **Retour :** la fonction fournit une estimation de hauteur projetée en pixels.



- **Garde :** les dimensions invalides sont refusées avant le calcul.



- **Limite :** la formule ne remplace ni la bounding box réelle ni une capture moteur.



## 9. Importance gameplay et priorité visuelle



Deux objets occupant la même surface écran peuvent recevoir des profils différents. Un ennemi, une porte interactive ou un landmark supportent moins de dégradation qu’un débris secondaire. Le profil doit rester une donnée de production, jamais une décision cachée dans le nom du fichier.

L’importance gameplay ne donne pas au chapitre l’autorité sur le système de jeu ; elle informe seulement le budget visuel.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
importance_profiles:
  landmark:
    silhouette_weight: high
    transition_tolerance: low
  interactable:
    recognition_weight: high
    transition_tolerance: low
  ambient_prop:
    silhouette_weight: medium
    transition_tolerance: medium
  filler:
    silhouette_weight: low
    transition_tolerance: high
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Landmark :** la reconnaissance à longue distance domine.



- **Interactif :** l’objet doit rester identifiable avant interaction.



- **Ambiant :** une perte modérée de détail est acceptable.



- **Filler :** le profil autorise une simplification plus agressive après mesure.



## 10. Profils par plateforme



Les mêmes assets peuvent utiliser des seuils et niveaux distincts selon la plateforme, le renderer, la résolution et les objectifs de performance. Le profil ne doit pas dupliquer les meshes sans raison : il peut sélectionner une chaîne commune avec des seuils différents.

Aucune plateforme n’est qualifiée par le seul nom `desktop`, `mobile` ou `web`. Chaque profil cite matériel, renderer et scénario de mesure.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
platform_profiles:
  desktop_reference:
    renderer: Forward+
    lod_chain: full
    soft_fades: allowed
  mobile_reference:
    renderer: Mobile
    lod_chain: reduced
    soft_fades: disabled
  web_reference:
    renderer: Compatibility
    lod_chain: reduced
    occlusion_assumption: not_guaranteed
  status: candidates_until_benchmarked
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Desktop :** le profil candidat autorise les transitions douces du renderer Forward+.



- **Mobile :** le profil évite de dépendre d’un fondu non pris en charge.



- **Web :** les hypothèses d’occlusion restent prudentes.



- **Statut :** aucune garantie n’existe avant benchmark réel.



## 11. Établir la baseline



Avant toute simplification, le LOD0 est mesuré dans une scène vide et dans une scène représentative. Les statistiques comprennent triangles, sommets exportés, surfaces, matériaux, mémoire estimée, temps CPU/GPU lorsque disponible et comportement des ombres.

La baseline cite la version de l’asset, du moteur, du renderer et de la caméra. Sans cette identité, un gain ne peut pas être reproduit.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
baseline:
  asset_version: v001
  engine: 4.7.1-stable
  renderer: Forward+
  camera_profile: CAM-BENCHMARK-01
  scenarios:
    - isolated_asset
    - repeated_instances
    - representative_outpost
  metrics:
    - triangles
    - exported_vertices
    - surfaces
    - draw_calls
    - gpu_time_ms
    - cpu_frame_time_ms
  status: pending_measurement
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Identité :** version, moteur et caméra rendent la mesure comparable.



- **Scénarios :** l’objet isolé ne suffit pas à prédire le coût en scène.



- **Métriques :** géométrie, surfaces et temps sont séparés.



- **Réserve :** les valeurs restent absentes tant que la scène n’est pas exécutée.



## 12. Budget de la chaîne



Le budget fixe des plafonds candidats par niveau, mais aussi des obligations de perception. Il peut exprimer un ratio relatif au LOD0 et un plafond absolu, car un même ratio produit des coûts très différents selon l’asset source.

Le budget n’autorise jamais une réduction automatique sans contrôle de silhouette, normales, matériaux et ombres.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
lod_budget:
  lod0:
    triangle_ratio: 1.0
    role: close
  lod1:
    triangle_ratio_candidate: 0.55
    silhouette_error: low
  lod2:
    triangle_ratio_candidate: 0.18
    silhouette_error: bounded
  impostor:
    triangle_budget_candidate: 2
    view_count_candidate: 12
  approval: pending_real_asset
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **LOD0 :** la référence proche reste inchangée.



- **LOD1 :** la simplification légère vise les détails internes.



- **LOD2 :** la réduction forte conserve les masses et contours.



- **Imposteur :** le plan et le nombre de vues sont des candidats à mesurer.



## 13. Triangles et sommets exportés



Le nombre de faces Blender ne suffit pas. Les seams UV, arêtes dures, matériaux et discontinuités d’attributs peuvent dupliquer des sommets à l’export. Une simplification qui réduit les faces mais multiplie les ruptures peut décevoir.

Le rapport conserve les statistiques DCC et les statistiques importées pour expliquer l’écart.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
geometry_counts:
  blender:
    faces: pending
    triangles_after_modifier: pending
  gltf:
    primitives: pending
    indexed_vertices: pending
  godot:
    surfaces: pending
    array_vertex_count: pending
    array_index_count: pending
  comparison_required: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Blender :** les faces et triangles évalués décrivent la source.



- **glTF :** primitives et sommets indexés décrivent l’échange.



- **Godot :** surfaces et arrays décrivent le mesh importé.



- **Comparaison :** les écarts signalent des séparations invisibles dans le simple compteur de faces.



## 14. Matériaux, surfaces et draw calls



Un LOD géométriquement léger peut rester coûteux s’il conserve de nombreux slots, surfaces ou états transparents. La réduction des matériaux est donc planifiée avec le chapitre 16, sans redéfinir les cartes PBR.

Une fusion de slots exige des UV et textures compatibles. Elle n’est pas imposée lorsque la lisibilité ou la réutilisation d’une bibliothèque serait dégradée.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
surface_policy:
  lod0:
    material_slots: preserve_approved
  lod1:
    merge_candidates: [small_metal_parts, hidden_fasteners]
  lod2:
    target_surface_groups: [structure, emissive_marker]
  impostor:
    material_slots: 1
  alpha_pipeline: measure_separately
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **LOD0 :** les matériaux approuvés restent la référence.



- **LOD1 :** seuls les petits groupes compatibles sont candidats à la fusion.



- **LOD2 :** les grandes fonctions visuelles remplacent les nombreux sous-matériaux.



- **Transparence :** l’imposteur est mesuré séparément à cause du pipeline alpha.



## 15. Mémoire et stockage



Ajouter trois meshes et un atlas d’imposteur peut augmenter la mémoire et la taille du paquet. Le gain de rasterisation doit être comparé à ce coût, surtout lorsque l’asset apparaît peu ou reste proche de la caméra.

Le rapport sépare mémoire géométrique, textures, import et stockage source. Les sources Blender ne sont pas comptées comme mémoire runtime.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
memory_report:
  runtime:
    mesh_lod0_bytes: pending
    mesh_lod1_bytes: pending
    mesh_lod2_bytes: pending
    impostor_texture_bytes: pending
  package:
    glb_bytes: pending
    imported_resources_bytes: pending
  source:
    blend_bytes: excluded_from_runtime
  decision: pending
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Runtime :** les meshes et textures réellement chargés sont comptés séparément.



- **Paquet :** la taille distribuée reste distincte de la mémoire résidente.



- **Source :** le `.blend` n’est pas confondu avec une ressource runtime.



- **Décision :** le gain doit justifier le coût additionnel de la chaîne.



## 16. Architecture de la chaîne LOD



Une chaîne possède des niveaux ordonnés, des plages qui se chevauchent uniquement selon une règle contrôlée et un dernier niveau capable de disparaître ou de devenir un imposteur. Les trous de visibilité sont interdits.

Le nombre de niveaux dépend du coût et de la durée visible de chaque transition. Un niveau intermédiaire qui n’apparaît que quelques images peut coûter plus en maintenance qu’il n’économise.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
lod_chain:
  asset_id: AST-LOD-PILOT-SIGNAL-TOWER-001
  levels:
    - id: LOD0
      representation: mesh_manual
    - id: LOD1
      representation: mesh_manual
    - id: LOD2
      representation: mesh_manual_or_import_generated
    - id: IMP
      representation: impostor_billboard
  gaps_allowed: false
  redundant_levels_allowed: false
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Ordre :** les niveaux suivent une dégradation perceptuelle croissante.



- **Représentations :** mesh manuel, mesh généré et imposteur restent identifiés.



- **Continuité :** aucune plage vide ne doit faire disparaître l’asset prématurément.



- **Maintenance :** un niveau redondant est supprimé plutôt que conservé par habitude.



## 17. Nommage et collections Blender



Les objets portent l’identifiant d’asset, le niveau et la fonction. Les collections séparent sources, niveaux, collisions, ombres, capture et export. Le suffixe `LOD` ne remplace pas une fiche de profil.

Les noms déterministes facilitent l’audit et évitent de confondre un mesh de rendu avec un proxy physique.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
AST-LOD-PILOT-SIGNAL-TOWER-001/
├── __SOURCE
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD0
├── __LOD
│   ├── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD1
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD2
├── __PROXY
│   ├── AST-LOD-PILOT-SIGNAL-TOWER-001_COLLISION
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_SHADOW
├── __IMPOSTOR_CAPTURE
└── __EXPORT
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Source :** le LOD0 approuvé reste séparé des dérivés.



- **Niveaux :** chaque simplification possède un objet explicite.



- **Proxies :** collision et ombre ne sont jamais pris pour des meshes visuels.



- **Export :** la frontière contient uniquement les candidats livrés.



## 18. Origine, échelle et boîtes englobantes



Tous les niveaux partagent origine, orientation et échelle appliquée. Une variation d’origine crée un saut au changement de niveau ; une AABB incorrecte provoque une disparition ou un culling incohérent.

Les éléments lointains très fins ne doivent pas étendre artificiellement la boîte sans nécessité. Le rapport conserve la boîte de chaque représentation.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
transform_contract:
  origin: shared_asset_origin
  scale_applied: true
  orientation: inherited_from_lod0
  aabb:
    lod0: measured
    lod1: measured
    lod2: measured
    impostor: measured_with_rotation
  pivot_changes_after_publish: forbidden
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Origine :** toutes les représentations commutent sans translation.



- **Échelle :** les facteurs résiduels ne masquent pas une géométrie mal dimensionnée.



- **AABB :** chaque niveau est vérifié, y compris le billboard en rotation.



- **Publication :** un pivot publié ne change pas silencieusement.



## 19. Geler le LOD0



Le LOD0 est la référence de silhouette, matériaux, normales et proportions. Toute modification du LOD0 après production des niveaux dérivés invalide au minimum les comparaisons et peut exiger une régénération complète.

Le manifeste enregistre l’empreinte de la source approuvée pour détecter cette dérive.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
lod0_freeze:
  source_file: AST-LOD-PILOT-SIGNAL-TOWER-001_LOD0.blend
  source_sha256: pending
  mesh_object: AST-LOD-PILOT-SIGNAL-TOWER-001_LOD0
  approved_version: v001
  downstream_invalidated_on_change:
    - lod1
    - lod2
    - impostor
    - captures
    - benchmark
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Source :** le fichier et l’objet approuvés sont nommés.



- **Empreinte :** la preuve détecte un changement de contenu.



- **Version :** la chaîne dépend d’une version immuable.



- **Invalidation :** les dérivés sont recalculés lorsque la référence change.



## 20. Choisir entre LOD manuel et automatique



Le LOD manuel convient aux silhouettes importantes, aux hard-surfaces et aux éléments dont la disparition doit être décidée artistiquement. Le LOD automatique Godot est utile comme repli, pour des familles secondaires ou comme niveau supplémentaire évalué à l’import.

Les deux approches peuvent coexister : un LOD1 manuel peut lui-même bénéficier de niveaux internes générés, à condition que le comportement soit mesuré et documenté.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
strategy_matrix:
  manual:
    use_when: [landmark, hard_surface, authored_silhouette]
    strengths: [control, repeatability, material_decisions]
  automatic_godot:
    use_when: [secondary_assets, batch_candidates, fallback]
    strengths: [import_pipeline, low_authoring_cost]
  mixed:
    use_when: [manual_near_auto_far]
  mandatory_review: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Manuel :** la forme et les matériaux sont contrôlés par l’artiste.



- **Automatique :** le coût d’auteur diminue mais la revue reste nécessaire.



- **Mixte :** les responsabilités des niveaux proches et lointains sont séparées.



- **Revue :** aucun mode n’est approuvé automatiquement.



## 21. Décimation Collapse dans Blender



Le mode Collapse fusionne progressivement des sommets selon la forme. Son ratio est calculé à partir des triangles ; il ne doit pas être lu comme un pourcentage exact de quads restants. La symétrie et un groupe de sommets peuvent protéger certaines zones.

Le modifier reste non destructif jusqu’à la validation. Une copie versionnée est créée avant application.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
blender_decimate_collapse:
  modifier: Decimate
  mode: COLLAPSE
  ratio_candidate: 0.55
  symmetry_axis: X
  vertex_group: LOD_PROTECT
  triangulate_result: controlled
  apply_after_visual_review: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Mode :** Collapse cible une réduction générale de la géométrie.



- **Ratio :** la valeur candidate est évaluée sur la silhouette et les triangles.



- **Protection :** symétrie et groupe de sommets limitent les dégâts sur les signaux majeurs.



- **Application :** le modifier n’est figé qu’après revue.



## 22. Décimation Planar pour les surfaces rigides



Le mode Planar dissout les détails sur les zones presque planes. Les délimitations par normales, matériaux, seams, arêtes sharp et UV peuvent empêcher une dissolution nuisible.

Sur la tour, il peut alléger les panneaux du boîtier et le socle, mais ne remplace pas une suppression manuelle des pièces invisibles.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
blender_decimate_planar:
  mode: DISSOLVE
  angle_limit_candidate_deg: 3.0
  delimit:
    - NORMAL
    - MATERIAL
    - SEAM
    - SHARP
    - UV
  targets:
    - service_box_panels
    - base_slabs
  visual_review: required
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Angle :** la limite candidate définit ce qui est considéré comme presque plan.



- **Délimitations :** les ruptures de shading, matériaux et UV sont protégées.



- **Cibles :** les grandes surfaces rigides sont traitées en priorité.



- **Revue :** les contours et reflets restent inspectés après dissolution.



## 23. Un-Subdivide et topologies régulières



Un-Subdivide tente de retirer des boucles issues d’une subdivision régulière. Il convient aux grilles propres mais devient imprévisible après des modifications locales importantes. Les itérations paires correspondent généralement à des niveaux de subdivision entiers.

La méthode est réservée aux pièces dont l’historique et la structure la rendent pertinente.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
blender_unsubdivide:
  mode: UNSUBDIV
  candidate_iterations: 2
  allowed_topology: regular_subdivision_grid
  rejected_topology:
    - boolean_heavy
    - irregular_local_edits
    - mixed_density_without_history
  approval: per_object
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Itérations :** la valeur candidate correspond à une réduction de subdivision simple.



- **Admissible :** une grille régulière conserve un résultat prévisible.



- **Rejet :** les topologies altérées ne sont pas forcées dans cette méthode.



- **Granularité :** l’approbation se fait pièce par pièce.



## 24. Masques de protection et priorités locales



Les groupes de sommets servent à préserver plateforme, antenne, coins du boîtier et attaches de haubans. Ils n’autorisent pas à ignorer les artefacts créés autour de la frontière du masque.

La carte de priorité est versionnée avec le niveau qu’elle produit.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
vertex_priority:
  group: LOD_PROTECT
  weights:
    antenna_crown: 1.0
    platform_outer_silhouette: 1.0
    service_box_corners: 0.8
    guy_wire_anchors: 0.7
    hidden_internal_braces: 0.0
  smoothing_passes_candidate: 2
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Groupe :** un nom stable relie l’intention au modifier.



- **Poids élevés :** les signaux de silhouette et d’identité résistent davantage.



- **Poids faibles :** les détails internes deviennent prioritaires pour la réduction.



- **Lissage :** la transition de poids évite une frontière trop abrupte.



## 25. Préserver la silhouette



La silhouette est contrôlée depuis plusieurs azimuts, élévations et distances. Une vue unique masque souvent un décrochement, une plateforme ou une asymétrie importante.

Les erreurs sont évaluées en pixels ou par superposition de contours, puis qualifiées visuellement. Une tolérance numérique ne remplace pas la lecture de l’objet.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
silhouette_review:
  azimuths_deg: [0, 45, 90, 135, 180, 225, 270, 315]
  elevations_deg: [-10, 0, 15, 30]
  screen_heights_px_candidate: [512, 256, 128, 64, 32]
  overlays:
    - lod0_outline
    - candidate_outline
    - difference_mask
  human_decision: required
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Angles :** les vues réparties révèlent les déformations directionnelles.



- **Élévations :** les vues basses et hautes contrôlent plateforme et couronne.



- **Tailles :** la différence est observée aux tailles d’usage.



- **Décision :** le masque aide la revue sans remplacer le jugement.



## 26. Normales, tangentes et triangulation des LOD



Chaque niveau possède ses propres normales et sa triangulation gelée. Les tangentes sont générées ou exportées selon le contrat du chapitre 17. Copier aveuglément les normales du LOD0 sur une topologie différente n’est pas une preuve de shading correct.

Les changements de normales sont inspectés sous lumière tournante et dans Godot.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
lod_shading_contract:
  per_level:
    triangulation: frozen_before_export
    normals: reviewed
    tangents: exported_or_mikktspace_fallback_recorded
  comparison:
    blender_rotating_light: required
    godot_rotating_light: required
  copied_normals_without_review: forbidden
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Triangulation :** chaque niveau exporte une structure stable.



- **Normales :** le shading est recalculé pour la topologie réelle.



- **Tangentes :** la source est enregistrée comme au chapitre 17.



- **Comparaison :** les deux applications doivent montrer un résultat cohérent.



## 27. UV et continuité des textures



Un LOD peut conserver les UV du LOD0 si la simplification respecte les attributs, ou utiliser un nouvel unwrap si la fusion des matériaux l’exige. Toute nouvelle carte nécessite une nouvelle qualification de densité, marges et bake.

Le chapitre ne rebake pas automatiquement les cartes : il renvoie au contrat du chapitre 17 lorsque la projection change.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
uv_policy_by_lod:
  lod1:
    preferred: preserve_lod0_uv_when_valid
    rebake_trigger: topology_or_projection_break
  lod2:
    preferred: simplified_uv_or_atlas
    rebake_required_if_new_uv: true
  impostor:
    uv: capture_atlas
  chapter_17_contract_applies: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **LOD1 :** la continuité est préférée lorsque la réduction la permet.



- **LOD2 :** un atlas simplifié peut justifier un nouvel unwrap.



- **Imposteur :** ses UV servent à l’atlas de vues.



- **Frontière :** tout nouveau bake suit les règles du chapitre précédent.



## 28. Simplifier les matériaux par niveau



Les microvariations, couches secondaires et matériaux invisibles à distance peuvent être fusionnés ou remplacés. Les émissions importantes pour le landmark restent distinctes si leur lisibilité le justifie.

Le profil décrit les fonctionnalités retirées ; il ne suffit pas de réduire le nombre de slots sans mesurer le shader obtenu.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
material_lod_profile:
  lod0: full_pbr
  lod1:
    remove: [micro_normal, interior_decal]
    keep: [base_color, normal, roughness, emission_marker]
  lod2:
    remove: [micro_normal, secondary_masks]
    merge: [metal_parts, painted_structure]
  impostor:
    shading: captured_appearance
  validation: under_reference_lights
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **LOD0 :** le matériau complet reste la référence.



- **LOD1 :** les détails sous-pixel sont retirés avant les grands signaux.



- **LOD2 :** les groupes compatibles sont fusionnés.



- **Validation :** plusieurs éclairages évitent une optimisation valable dans une seule scène.



## 29. Textures et résolution par LOD



Une chaîne peut partager les textures du LOD0, sélectionner des mipmaps naturels ou utiliser un atlas plus petit. Dupliquer des textures sans bénéfice mesuré augmente la mémoire et le paquet.

La résolution de l’imposteur dépend du nombre de vues, de la taille écran et de la compression. Elle reste une décision de benchmark.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
texture_strategy:
  lod1: share_lod0_textures
  lod2:
    option_a: share_lod0_with_mipmaps
    option_b: reduced_atlas_if_memory_gain_measured
  impostor:
    atlas_resolution_candidate: 2048
    view_count_candidate: 12
    alpha_padding_required: true
  duplicate_without_measurement: forbidden
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Partage :** les niveaux proches évitent une duplication inutile.



- **LOD2 :** le nouvel atlas n’est choisi que si le gain complet est positif.



- **Imposteur :** résolution et vues restent des paramètres candidats.



- **Interdiction :** la mémoire supplémentaire exige une preuve.



## 30. Collisions simplifiées



La collision ne change pas nécessairement avec le LOD visuel. Pour un landmark statique, une collision simple peut rester constante tant que le joueur peut l’atteindre. À très longue distance, l’objet peut ne plus être physiquement pertinent selon les règles gameplay, mais cette décision appartient au système propriétaire.

Le chapitre produit un proxy candidat et documente sa plage, sans désactiver la physique depuis le visuel.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
collision_proxy:
  asset_id: AST-LOD-PILOT-SIGNAL-TOWER-001
  representation: convex_or_primitive_set
  shared_across_visual_lods: true
  visual_lod_drives_collision: false
  gameplay_authority_required_for_disable: true
  review:
    walkable_clearance: pending
    interaction_volume: pending
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Proxy :** la collision utilise une géométrie dédiée.



- **Partage :** le même proxy peut accompagner plusieurs LOD visuels.



- **Autorité :** le système de jeu décide d’une éventuelle désactivation.



- **Revue :** les volumes de déplacement et d’interaction restent à tester.



## 31. Proxies d’ombre



Les ombres peuvent conserver un mesh plus simple que le visuel, surtout à distance. Un proxy trop grossier crée toutefois une ombre incohérente ou flottante. Godot permet aussi de rendre uniquement les ombres d’une géométrie dédiée.

Le profil distingue ombre proche, ombre lointaine et éventuelle suppression selon la taille écran.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
shadow_profile:
  near:
    source: visual_lod
  mid:
    source: AST-LOD-PILOT-SIGNAL-TOWER-001_SHADOW
  far:
    source: none_or_impostor_policy
  shadows_only_instance: candidate
  review_times:
    - morning_low_sun
    - noon
    - evening_low_sun
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Proche :** le visuel peut fournir une ombre détaillée.



- **Intermédiaire :** un proxy réduit le coût tout en conservant la masse.



- **Lointain :** la suppression reste une décision mesurée.



- **Revue :** les angles de soleil bas révèlent les erreurs de forme.



## 32. LOD automatique des meshes dans Godot



Godot peut générer des niveaux internes lors de l’import des meshes et les sélectionner automatiquement selon leur taille à l’écran. Cette voie réduit le coût d’auteur mais ne fusionne pas les matériaux et ne remplace pas un HLOD ou un imposteur.

Le profil d’import et le `lod_bias` sont versionnés. La génération automatique est comparée au LOD manuel sur le même asset.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
godot_mesh_lod:
  import_generated: candidate
  selection_basis: screen_size
  lod_bias_default: 1.0
  compare_against:
    - manual_lod1
    - manual_lod2
  does_not_replace:
    - material_merging
    - hlod_grouping
    - impostor_capture
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Génération :** les niveaux internes sont produits à l’import.



- **Sélection :** le moteur se fonde sur la taille projetée.



- **Biais :** la valeur par défaut reste la référence de test.



- **Limites :** matériaux, agrégation et imposteurs exigent d’autres contrats.



## 33. Profil d’import Godot



Le fichier glTF est réimporté avec des options versionnées. Les réglages liés au LOD ne sont pas changés manuellement poste par poste sans mise à jour du preset ou du manifeste.

Les fichiers `.import` peuvent être versionnés lorsque le dépôt le prévoit ; le cache `.godot` reste généré.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
godot_import_profile:
  source: res://assets/asteria/signal_tower/AST-LOD-PILOT-SIGNAL-TOWER-001.glb
  generate_lods: true
  ensure_tangents: true
  create_shadow_meshes: candidate
  import_script: none
  import_settings_versioned: true
  generated_cache_versioned: false
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Source :** le chemin identifie le GLB candidat.



- **LOD :** la génération automatique est explicitement activée ou désactivée.



- **Tangentes :** la cohérence avec le chapitre 17 reste conservée.



- **Versionnement :** les réglages sont tracés, le cache généré ne l’est pas.



## 34. Utiliser `lod_bias` pour le diagnostic



`GeometryInstance3D.lod_bias` modifie la rapidité avec laquelle un mesh passe à un niveau interne moins détaillé. Une valeur nulle force le niveau le plus bas ; une valeur supérieure à un conserve plus longtemps le détail.

Le biais sert à inspecter et comparer, pas à masquer une chaîne mal conçue avec une valeur extrême.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```gdscript
@tool
extends MeshInstance3D

@export_range(0.0, 4.0, 0.05) var diagnostic_lod_bias: float = 1.0

func apply_diagnostic_bias() -> void:
    lod_bias = diagnostic_lod_bias
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Type :** le script étend `MeshInstance3D`, donc possède la propriété `lod_bias`.



- **Paramètre :** `diagnostic_lod_bias` est borné pour l’inspecteur.



- **Retour :** `apply_diagnostic_bias()` ne renvoie rien et applique seulement la valeur.



- **Usage :** le script sert à une revue dans l’éditeur, pas à une politique runtime cachée.



## 35. Plages de visibilité manuelles



Les plages de visibilité s’appliquent aux nœuds héritant de `GeometryInstance3D`. `visibility_range_begin` masque l’instance lorsqu’elle est trop proche ; `visibility_range_end` la masque lorsqu’elle est trop loin. Une valeur nulle désactive le contrôle correspondant.

Chaque niveau manuel possède des plages complémentaires et une origine commune.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```gdscript
func configure_range(instance: GeometryInstance3D, begin_m: float, end_m: float) -> void:
    assert(instance != null)
    assert(begin_m >= 0.0)
    assert(end_m == 0.0 or end_m > begin_m)
    instance.visibility_range_begin = begin_m
    instance.visibility_range_end = end_m
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Paramètre objet :** `instance` reçoit tout nœud dérivé de `GeometryInstance3D`.



- **Distances :** `begin_m` et `end_m` utilisent les unités 3D du projet.



- **Gardes :** les plages négatives ou inversées sont refusées.



- **Effet :** la fonction configure la visibilité sans choisir le niveau à la place du profil.



## 36. Hystérésis contre les oscillations



Lorsque le fade est désactivé, les marges de début et de fin agissent comme distances d’hystérésis. Elles évitent qu’un niveau commute à chaque image lorsque la caméra oscille près du seuil.

La marge est proportionnée à la vitesse de caméra et à la distance du seuil, puis vérifiée par un aller-retour reproductible.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
visibility_hysteresis:
  lod0:
    end_m_candidate: 45.0
    end_margin_m_candidate: 4.0
  lod1:
    begin_m_candidate: 41.0
    begin_margin_m_candidate: 4.0
    end_m_candidate: 110.0
    end_margin_m_candidate: 8.0
  test:
    camera_motion: forward_backward
    threshold_crossings: repeated
    flicker_allowed: false
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Chevauchement :** les seuils et marges créent une zone stable.



- **Vitesse :** la marge doit être éprouvée avec les mouvements réels.



- **Test :** l’aller-retour répété révèle les oscillations.



- **Critère :** aucun clignotement de niveau n’est accepté.



## 37. Fondus et contraintes de renderer



Les modes de fondu `SELF` et `DEPENDENCIES` offrent des transitions plus douces, mais Godot les prend en charge uniquement avec Forward+. En Mobile ou Compatibility, ils se comportent comme un changement sans fondu doux et sans hystérésis équivalente.

Le profil de plateforme ne doit donc pas dépendre d’un effet indisponible.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
fade_policy:
  Forward+:
    allowed_modes: [DISABLED, SELF, DEPENDENCIES]
    preferred_candidate: DEPENDENCIES
  Mobile:
    allowed_modes: [DISABLED]
  Compatibility:
    allowed_modes: [DISABLED]
  fallback_requires_hysteresis_review: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Forward+ :** les trois modes peuvent être évalués.



- **Mobile :** le profil évite de compter sur un fondu doux.



- **Compatibility :** la même prudence s’applique.



- **Repli :** le passage au changement sec exige une nouvelle revue de popping.



## 38. Dépendances de visibilité et HLOD



`visibility_parent` relie une représentation détaillée à une représentation agrégée. Le mode `DEPENDENCIES` peut faire apparaître les dépendances pendant que le parent s’efface. L’arbre doit rester acyclique et lisible.

Pour la tour, un HLOD peut remplacer tour, clôture et petits accessoires par une représentation groupée, sans modifier leurs identités métier.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
Outpost_HLOD
├── SignalTower_HLOD        ← représentation lointaine
├── SignalTower_LOD0        → visibility_parent: SignalTower_HLOD
├── FenceCluster_LOD0       → visibility_parent: Outpost_HLOD
└── PropCluster_LOD0        → visibility_parent: Outpost_HLOD
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Parent :** la représentation lointaine reçoit les dépendances.



- **Enfants :** les géométries détaillées conservent leurs nœuds et identités.



- **Transition :** le moteur peut coordonner leur visibilité.



- **Frontière :** le HLOD visuel ne fusionne pas les états gameplay.



## 39. Déduire des seuils candidats



Les seuils candidats partent d’une taille écran minimale pour chaque niveau, puis sont convertis en distances avec la caméra de benchmark. Ils sont ensuite ajustés par revue perceptuelle.

Les seuils enregistrent le FOV et la résolution de calcul afin de rester interprétables.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```python
from math import tan, radians

def distance_for_projected_height(height_m: float, target_px: float, vertical_fov_deg: float, viewport_height_px: int) -> float:
    if min(height_m, target_px, vertical_fov_deg, float(viewport_height_px)) <= 0.0:
        raise ValueError("arguments strictement positifs")
    frustum_ratio = target_px / float(viewport_height_px)
    return height_m / (2.0 * tan(radians(vertical_fov_deg) * 0.5) * frustum_ratio)
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Entrées :** hauteur réelle, taille cible, FOV et viewport définissent la caméra.



- **Retour :** la fonction produit une distance candidate.



- **Garde :** les valeurs nulles ou négatives sont refusées.



- **Ajustement :** la distance calculée doit encore passer la revue moteur.



## 40. Tester plusieurs caméras



Une vue première personne, une caméra troisième personne et une caméra stratégique n’exposent pas les mêmes transitions. Les profils peuvent partager les meshes tout en utilisant des seuils distincts.

Le benchmark inclut les FOV extrêmes réellement autorisés, le zoom et les résolutions dynamiques si le projet les utilise.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
camera_matrix:
  first_person:
    vertical_fov_deg: candidate
    transition_priority: low_popping
  third_person:
    vertical_fov_deg: candidate
    transition_priority: balanced
  tactical:
    vertical_fov_deg: candidate
    transition_priority: large_instance_count
  zoom_extremes_tested: required
  dynamic_resolution_tested: if_enabled
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Première personne :** les changements proches sont particulièrement visibles.



- **Troisième personne :** le profil équilibre perception et nombre d’instances.



- **Tactique :** la densité d’objets devient un facteur majeur.



- **Options :** zoom et résolution dynamique sont inclus lorsqu’ils existent.



## 41. Définir l’imposteur



L’imposteur remplace la tour par une capture de son apparence. Un imposteur à vue unique convient mal à une caméra tournant librement autour d’une silhouette asymétrique ; un atlas multi-vues réduit cette erreur au prix de texture et de logique de sélection.

Le choix dépend du nombre d’angles visibles et de la taille écran finale.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
impostor_profile:
  type: multi_view_billboard
  azimuth_views_candidate: 8
  elevation_bands_candidate: 2
  total_views_candidate: 16
  channels:
    required: [color_alpha]
    optional: [normal, depth]
  camera_freedom: full_orbit
  approval: pending_capture_test
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Type :** le multi-vues répond à une caméra orbitale.



- **Angles :** azimuts et élévations couvrent la silhouette asymétrique.



- **Canaux :** couleur et alpha sont obligatoires, normales et profondeur restent optionnelles.



- **Statut :** la capture réelle doit encore être comparée au mesh.



## 42. Rig de capture d’imposteur



La capture utilise une caméra orthographique ou une perspective contrôlée, un pivot partagé et un éclairage défini. L’arrière-plan reste transparent et les cadres partagent la même échelle.

La capture ne doit pas cuire une lumière incompatible avec le projet si l’imposteur doit réagir à l’éclairage dynamique.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
impostor_capture_rig:
  target_origin: shared_asset_origin
  camera:
    projection: orthographic_candidate
    framing: constant_across_views
  background: transparent
  lighting:
    mode: neutral_or_project_specific
    baked_directional_light: forbidden_without_profile
  output:
    premultiplied_alpha: explicitly_recorded
    padding_px: measured
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Pivot :** la rotation des vues reste centrée sur l’origine de l’asset.



- **Cadrage :** toutes les cases conservent une échelle comparable.



- **Éclairage :** la capture ne fige pas une direction arbitraire.



- **Alpha :** le mode et le padding sont documentés pour éviter les halos.



## 43. Atlas de vues



L’atlas associe chaque angle à une cellule et conserve un manifeste. L’ordre lexical ou angulaire doit être déterministe ; un script ne doit pas supposer un ordre de fichiers fourni par le système.

Les cellules vides et les variantes de résolution sont interdites sans version de schéma.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```json
{
  "schema_version": 1,
  "asset_id": "AST-LOD-PILOT-SIGNAL-TOWER-001",
  "grid": {"columns": 8, "rows": 2},
  "views": [
    {"index": 0, "azimuth_deg": 0, "elevation_deg": 0},
    {"index": 1, "azimuth_deg": 45, "elevation_deg": 0},
    {"index": 8, "azimuth_deg": 0, "elevation_deg": 20}
  ],
  "ordering": "elevation_then_azimuth"
}
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Schéma :** la version protège les consommateurs futurs.



- **Grille :** colonnes et lignes décrivent la texture.



- **Vues :** chaque index cite ses angles.



- **Ordre :** la règle déterministe évite une sélection incohérente.



## 44. Alpha, padding et halos



Les bords transparents doivent recevoir une couleur dilatée compatible avec la compression et les mipmaps. Un fond noir sous alpha crée souvent un halo sombre à distance.

Le type d’alpha, la dilation, la compression et le filtrage sont testés ensemble dans Godot.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
impostor_alpha:
  mode: straight_or_premultiplied_recorded
  color_dilation_px_candidate: 16
  atlas_cell_padding_px_candidate: 8
  mipmaps: enabled
  compression_profile: qualified
  tests:
    - bright_background
    - dark_background
    - fog
    - oblique_view
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Mode :** l’alpha choisi est explicite.



- **Dilation :** la couleur des bords survit aux mipmaps.



- **Padding :** les cellules ne contaminent pas leurs voisines.



- **Tests :** plusieurs fonds et angles révèlent les franges.



## 45. Normales et profondeur d’imposteur



Un atlas de normales permet un éclairage approximatif ; une profondeur peut améliorer le parallax ou la reconstruction, mais augmente la complexité et le coût. Ces canaux ne sont ajoutés que si la comparaison visuelle justifie leur mémoire.

Les normales suivent l’orientation OpenGL du pipeline Godot et leur espace est documenté.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
impostor_auxiliary_channels:
  normal:
    enabled_candidate: true
    convention: OpenGL
    space: view_or_world_recorded
  depth:
    enabled_candidate: false
    normalization: near_far_recorded_if_enabled
  selection_rule: measurable_visual_gain
  memory_cost_recorded: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Normale :** la convention et l’espace évitent une interprétation ambiguë.



- **Profondeur :** les plans de normalisation deviennent obligatoires si le canal est activé.



- **Sélection :** un gain visuel mesuré justifie chaque canal.



- **Mémoire :** le coût additionnel reste visible dans le rapport.



## 46. Orientation du billboard



Un billboard peut faire face entièrement à la caméra ou tourner seulement autour de l’axe vertical. Pour une tour verticale, le verrouillage Y évite une inclinaison irréaliste lorsque la caméra monte ou descend.

Le mode du matériau et la géométrie du plan sont vérifiés avec la caméra au-dessus et au-dessous de l’horizon.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
billboard_orientation:
  asset_type: vertical_landmark
  preferred: y_billboard
  fallback: full_billboard
  pivot: base_center
  camera_tests:
    - ground_level
    - elevated_view
    - steep_downward_view
  roll_allowed: false
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Type :** la verticalité guide le choix d’orientation.



- **Préférence :** le verrouillage axial conserve la tour droite.



- **Pivot :** la base reste ancrée au terrain.



- **Tests :** les vues élevées vérifient l’absence d’inclinaison ou de flottement.



## 47. Ombres des imposteurs



Une carte alpha peut projeter une ombre coûteuse ou instable. Le profil choisit entre aucune ombre, ombre simplifiée par proxy, ou ombre alpha selon la distance et le renderer.

L’ombre de l’imposteur ne doit pas révéler brutalement son orientation de plan.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
impostor_shadow_policy:
  close_to_mid: simplified_shadow_mesh
  far: disabled_candidate
  alpha_shadow: evaluate_only_if_needed
  orientation_artifact_test: required
  low_sun_test: required
  performance_measurement: required
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Intermédiaire :** un mesh simple conserve une masse d’ombre stable.



- **Lointain :** la suppression est candidate lorsque l’ombre devient sous-pixel.



- **Alpha :** le coût et l’artefact sont évalués avant adoption.



- **Mesure :** la décision combine rendu et performance.



## 48. Profils par famille d’assets



Architecture, végétation, foule et objets n’utilisent pas la même chaîne. Les bâtiments peuvent bénéficier d’HLOD ; la végétation emploie souvent billboards et MultiMesh ; une foule combine LOD de mesh, animation et éventuellement imposteurs, mais l’animation reste hors de ce chapitre.

Les profils partagent le même format de preuve.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
family_profiles:
  architecture:
    techniques: [manual_lod, hlod, simplified_collision]
  vegetation:
    techniques: [mesh_lod, billboard, multimesh]
  crowd_visual:
    techniques: [mesh_lod, impostor_candidate]
    animation_owner: chapter_20
  props:
    techniques: [automatic_lod, manual_lod_for_hero]
  common_evidence: benchmark_and_capture
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Architecture :** l’agrégation et la collision sont majeures.



- **Végétation :** les répétitions et billboards dominent.



- **Foule :** le visuel est documenté sans reprendre l’animation.



- **Commun :** toutes les familles exigent benchmark et captures.



## 49. LOD et MultiMesh



`MultiMeshInstance3D` réduit le coût d’instances répétées, mais une collection MultiMesh ne choisit pas automatiquement un LOD différent par instance de la même manière qu’un arbre de nœuds individuels. Les groupes peuvent être séparés par bande de distance ou gérés par un système spécialisé.

La stratégie doit mesurer le coût CPU de reclassement et le coût GPU des groupes.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
multimesh_lod_strategy:
  source_family: repeated_signal_posts
  groups:
    - id: near_mesh
      representation: lod0_or_lod1
    - id: mid_mesh
      representation: lod2
    - id: far_billboard
      representation: billboard
  reassignment_frequency: bounded
  cpu_and_gpu_metrics_required: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Groupes :** chaque bande utilise une représentation homogène.



- **Proximité :** les instances proches conservent davantage de détail.



- **Reclassement :** la fréquence de migration reste bornée.



- **Mesures :** CPU et GPU sont examinés ensemble.



## 50. AABB, culling et rotations



Les imposteurs, meshes orientés et objets avec éléments fins exigent une boîte englobante valide. Une AABB trop petite provoque un culling prématuré ; une boîte immense réduit l’efficacité du frustum et de l’occlusion.

Les rotations du billboard et les variations de shader sont incluses dans la boîte testée.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```gdscript
func validate_aabb(instance: GeometryInstance3D) -> PackedStringArray:
    var issues := PackedStringArray()
    if instance == null:
        issues.append("instance_absente")
        return issues
    var bounds := instance.get_aabb() if instance is MeshInstance3D else instance.custom_aabb
    if bounds.size.x <= 0.0 or bounds.size.y <= 0.0 or bounds.size.z <= 0.0:
        issues.append("aabb_vide_ou_plate")
    return issues
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Paramètre :** la fonction reçoit une instance géométrique.



- **Retour :** un `PackedStringArray` contient les anomalies structurelles.



- **Branche :** un `MeshInstance3D` peut fournir son AABB de mesh ; les autres utilisent le contrat personnalisé.



- **Limite :** le script ne remplace pas une revue de culling avec caméra mobile.



## 51. Relation avec l’occlusion culling



L’occlusion culling complète le LOD mais ne le remplace pas. Dans de grands espaces ouverts, Godot recommande généralement de privilégier mesh LOD et plages de visibilité, car peu d’objets masquent réellement la scène. L’occlusion ajoute aussi un coût CPU.

Le chapitre ne crée pas une campagne globale d’occlusion ; il vérifie seulement que les proxies LOD n’invalident pas les occluders du projet.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
occlusion_boundary:
  lod_is_primary_for_open_landscape: true
  occlusion_cpu_cost_measured_elsewhere: true
  web_support_assumption: not_guaranteed
  lod_proxy_used_as_occluder: only_after_review
  chapter_scope: compatibility_check_only
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Ouvert :** les distances et LOD restent prioritaires lorsque les masques sont rares.



- **Coût :** l’occlusion possède une charge CPU distincte.



- **Web :** la prise en charge n’est pas supposée par défaut.



- **Frontière :** la campagne complète reste hors du chapitre.



## 52. Concevoir la scène de benchmark



La scène contient un asset isolé, une grille d’instances, un outpost représentatif et un parcours de caméra. Les lumières, ombres, environnement, résolution et renderer sont figés. Les variantes diffèrent uniquement par la chaîne LOD testée.

Un benchmark qui change en même temps la caméra, les matériaux et le nombre d’instances ne permet pas d’attribuer le gain.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
Benchmark_LOD_SignalTower.tscn
├── WorldEnvironment
├── DirectionalLight3D
├── CameraPath3D
├── Scenario_Isolated
├── Scenario_Grid_100
├── Scenario_Outpost
├── Variant_Baseline
├── Variant_ManualLOD
├── Variant_AutoLOD
└── Variant_Impostor
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Environnement :** l’éclairage et le renderer restent communs.



- **Parcours :** la caméra suit la même trajectoire pour chaque variante.



- **Scénarios :** isolé, répétitions et scène réelle couvrent plusieurs coûts.



- **Variantes :** une seule stratégie change à la fois.



## 53. Scénarios et répétitions



Chaque variante est exécutée plusieurs fois après une phase de chauffe. Les captures de temps utilisent une durée ou un nombre d’images défini, sans sélectionner uniquement le meilleur résultat.

Les événements externes, compilation de shaders et import initial sont séparés de la mesure stable.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
benchmark_protocol:
  warmup_seconds_candidate: 10
  capture_seconds_candidate: 30
  repetitions_candidate: 5
  aggregation: median_and_percentiles
  exclude:
    - first_import
    - shader_compilation_spike
    - editor_background_tasks
  retain_raw_samples: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Chauffe :** les caches et shaders atteignent un état plus stable.



- **Durée :** la fenêtre candidate couvre plusieurs transitions.



- **Répétitions :** la médiane et les percentiles réduisent l’effet d’un échantillon isolé.



- **Traçabilité :** les données brutes restent disponibles.



## 54. Métriques à collecter



Les métriques incluent temps CPU et GPU, images par seconde uniquement comme lecture secondaire, triangles visibles, draw calls, surfaces, mémoire, nombre de transitions et anomalies visuelles. Le FPS seul masque les différences à haut débit.

Les mesures sont corrélées avec la position caméra et la variante.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```json
{
  "sample": {
    "frame": 1200,
    "camera_distance_m": 87.4,
    "variant": "manual_lod",
    "cpu_frame_ms": null,
    "gpu_frame_ms": null,
    "visible_triangles": null,
    "draw_calls": null,
    "lod_switches": 0,
    "visual_flags": []
  }
}
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Corrélation :** frame, distance et variante rendent l’échantillon interprétable.



- **Temps :** CPU et GPU restent séparés.



- **Charge :** triangles et draw calls expliquent le résultat.



- **Qualité :** les anomalies visuelles accompagnent les métriques.



## 55. Manifeste de captures



Chaque capture cite caméra, distance, FOV, niveau actif, renderer, éclairage et commit. Les noms d’images seuls ne suffisent pas à prouver le contexte.

Le manifeste peut référencer des images produites plus tard sans les annoncer comme existantes dans ce chapitre.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
capture_manifest:
  schema_version: 1
  benchmark_scene: Benchmark_LOD_SignalTower.tscn
  commit: pending
  captures:
    - id: CAP-LOD-001
      camera_profile: CAM-BENCHMARK-01
      distance_m: pending
      active_representation: pending
      renderer: Forward+
      lighting: noon
      file: pending
  current_status: not_produced
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Schéma :** la structure peut évoluer explicitement.



- **Scène :** la source de capture est nommée.



- **Contexte :** distance, niveau, renderer et lumière accompagnent l’image.



- **Statut :** aucun fichier n’est présenté comme produit.



## 56. Tableau comparatif avant/après



Le tableau met la baseline et les variantes sur les mêmes lignes. Les gains négatifs ou non concluants sont conservés ; ils ne sont pas supprimés du rapport.

Une colonne qualité relie les métriques à la revue visuelle.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```markdown
| Variante | Triangles | Draw calls | GPU ms | Mémoire | Popping | Décision |
|---|---:|---:|---:|---:|---|---|
| Baseline LOD0 | à mesurer | à mesurer | à mesurer | à mesurer | référence | en attente |
| LOD manuel | à mesurer | à mesurer | à mesurer | à mesurer | à revoir | en attente |
| LOD automatique | à mesurer | à mesurer | à mesurer | à mesurer | à revoir | en attente |
| Imposteur | à mesurer | à mesurer | à mesurer | à mesurer | à revoir | en attente |
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Lignes :** chaque stratégie utilise les mêmes colonnes.



- **Mesures :** les cellules restent explicitement en attente.



- **Qualité :** le popping est traité comme un résultat.



- **Décision :** aucune variante n’est approuvée avant données réelles.



## 57. Revue visuelle structurée



La revue observe silhouette, matériaux, transparence, ombres, ancrage au sol, stabilité de transition et lisibilité gameplay. Elle se déroule à vitesse réelle, au ralenti et image par image.

Les captures fixes complètent mais ne remplacent pas la vidéo ou le parcours interactif pour le popping.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
visual_review:
  dimensions:
    - silhouette
    - material_response
    - alpha_edges
    - shadow_shape
    - ground_anchor
    - transition_stability
    - gameplay_readability
  playback:
    - real_time
    - slow_motion
    - frame_step
  reviewers: human_required
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Dimensions :** la revue couvre plus que le contour.



- **Temps réel :** la perception normale reste le critère principal.



- **Ralentissement :** les causes de popping deviennent visibles.



- **Humain :** la décision artistique n’est pas automatisée seule.



## 58. Porte de non-régression



Toute modification du LOD0, des matériaux, de la caméra, de l’import ou du renderer invalide une partie des résultats. La matrice de non-régression indique quels tests relancer.

La chaîne n’est pas considérée stable parce qu’un seul benchmark ancien a réussi.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
regression_matrix:
  lod0_geometry_change: [rebuild_lods, recapture_impostor, rerun_all]
  material_change: [review_lods, recapture_impostor, rerun_visual]
  camera_fov_change: [recompute_thresholds, rerun_transitions]
  renderer_change: [review_fade_modes, rerun_performance]
  import_setting_change: [reimport, verify_mesh_lod, rerun_comparison]
  evidence_expiration: explicit
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Géométrie :** les dérivés et mesures sont invalidés.



- **Matériau :** l’imposteur capturé peut devenir obsolète.



- **Caméra :** les seuils de taille écran changent.



- **Renderer :** les fondus et performances doivent être requalifiés.



## 59. Provenance et dérivations



Chaque LOD, atlas et proxy est une transformation du LOD0 approuvé. Le manifeste enregistre outil, version, paramètres, auteur, date et empreintes. Un générateur automatique ne supprime pas la responsabilité humaine de revue.

Les textures d’imposteur héritent des droits et restrictions de toutes leurs sources visuelles.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
derivation_record:
  source_asset: AST-LOD-PILOT-SIGNAL-TOWER-001_LOD0
  source_version: v001
  source_sha256: pending
  outputs:
    - AST-LOD-PILOT-SIGNAL-TOWER-001_LOD1
    - AST-LOD-PILOT-SIGNAL-TOWER-001_LOD2
    - AST-LOD-PILOT-SIGNAL-TOWER-001_IMP
  tool_versions:
    blender: 5.2.0
    godot: 4.7.1-stable
  reviewer: pending
  rights_inherited: true
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Source :** le dérivé remonte à un asset approuvé.



- **Sorties :** meshes et imposteur sont identifiés.



- **Outils :** les versions rendent la transformation reproductible.



- **Droits :** la capture n’efface pas les obligations de provenance.



## 60. Modes Solo et Studio



En mode Solo, une petite bibliothèque de profils génériques suffit : landmark statique, prop courant, végétation répétée et bâtiment modulaire. Le créateur valide d’abord la tour pilote, conserve les paramètres dans un manifeste simple et évite de multiplier les niveaux tant que le benchmark ne montre pas leur utilité.



En mode Studio, les responsabilités peuvent être séparées entre artiste LOD, lookdev, technical artist, intégrateur Godot et responsable performance. Les mêmes contrats d’identifiants, de dérivation, de captures et de métriques évitent les décisions orales impossibles à reproduire.



- **Solo :** privilégier une chaîne courte, un benchmark stable et des paramètres versionnés.

- **Studio :** définir propriétaires, critères de passage, profils par plateforme et revue croisée.

- **Commun :** ne jamais approuver une réduction uniquement sur son ratio de triangles.

- **Escalade :** toute exception de silhouette, mémoire ou renderer est inscrite dans le rapport.



## 61. Diagnostics et corrections



<!-- qa:error-correction-section -->



Les cas suivants utilisent la séquence symptôme, exemple fautif, explication, correction et justification. Les valeurs restent pédagogiques et doivent être remplacées par les mesures du projet.



### 61.1 Réduire par pourcentage sans budget perceptuel



**Symptôme ou risque :** Le LOD2 perd la couronne d’antenne alors que le compteur de triangles respecte la cible.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
lod2:
  decimate_ratio: 0.10
  protected_features: []
  screen_size_test: skipped
  decision: approved_because_ratio_met
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Le ratio devient l’unique critère et ignore silhouette, importance gameplay et distance réelle.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
lod2:
  triangle_ratio_candidate: 0.18
  preserve: [antenna_crown, platform_outline]
  screen_size_test: required
  decision: pending_visual_review
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction traite le ratio comme candidat, protège les signaux majeurs et reporte l’approbation après revue.



### 61.2 Utiliser la distance seule pour tous les FOV



**Symptôme ou risque :** Le changement paraît correct en caméra tactique mais brutal en première personne.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
thresholds:
  lod1_end_m: 60
  basis: distance_only
  fov_recorded: false
  applies_to_all_cameras: true
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La distance ne tient pas compte du FOV, de la résolution ni de la taille projetée.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
thresholds:
  basis: projected_screen_height
  camera_profiles: [first_person, third_person, tactical]
  distances: measured_per_profile
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction conserve une base perceptuelle et traduit ensuite les seuils pour chaque caméra.



### 61.3 Laisser les niveaux avec des origines différentes



**Symptôme ou risque :** La tour saute latéralement à chaque transition.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
objects:
  LOD0_origin: base_center
  LOD1_origin: geometry_center
  IMP_origin: atlas_center
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Les représentations ne partagent pas le même repère de transformation.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
objects:
  shared_origin: asset_base_center
  transforms_applied: true
  pivot_check: passed_before_export
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction impose un pivot commun et une vérification avant export.



### 61.4 Activer un fondu doux sur un renderer incompatible



**Symptôme ou risque :** La transition Mobile reste sèche malgré un profil annonçant un cross-fade.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
mobile_profile:
  renderer: Mobile
  fade_mode: DEPENDENCIES
  expected: soft_crossfade
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Les fondus `SELF` et `DEPENDENCIES` ne fournissent pas le même comportement hors Forward+.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
mobile_profile:
  renderer: Mobile
  fade_mode: DISABLED
  hysteresis_margin: measured
  popping_review: required
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction utilise le mode réellement pris en charge et compense par une hystérésis testée.



### 61.5 Conserver trop de matériaux dans les LOD lointains



**Symptôme ou risque :** Les triangles baissent mais les draw calls restent presque identiques.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
lod2:
  triangles: reduced
  material_slots: 9
  surface_review: skipped
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La réduction géométrique n’adresse pas les surfaces et états de rendu.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
lod2:
  triangles: reduced
  material_groups: [structure, emissive_marker]
  draw_calls: measured
  visual_review: required
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction regroupe les fonctions compatibles et mesure le résultat complet.



### 61.6 Créer un imposteur sans padding de couleur



**Symptôme ou risque :** Un contour sombre apparaît autour de la tour avec les mipmaps.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
impostor:
  transparent_background_rgb: [0, 0, 0]
  dilation_px: 0
  mipmaps: true
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Les texels transparents noirs contaminent les bords filtrés.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
impostor:
  edge_color_dilation_px: measured
  cell_padding_px: measured
  mipmaps: true
  bright_dark_background_tests: required
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction dilate la couleur, isole les cellules et vérifie les franges sur plusieurs fonds.



### 61.7 Lier directement collision et LOD visuel



**Symptôme ou risque :** Le joueur traverse la tour lorsque la caméra franchit le seuil lointain.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
on_lod_changed(level):
  collision_shape.disabled = level >= 2
  physics_authority_checked = false
  visual_event_is_authoritative = true
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Le visuel acquiert une autorité physique qui appartient au système gameplay.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
collision_policy:
  proxy_shared_across_visual_lods: true
  disable_requires_gameplay_authority: true
  visual_callback_mutates_physics: false
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction sépare le proxy physique du changement visuel et exige une décision du système propriétaire.



### 61.8 Comparer des benchmarks avec des scènes différentes



**Symptôme ou risque :** La variante LOD semble plus rapide mais utilise moins de lumières et d’instances.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
baseline:
  instances: 100
  shadows: enabled
optimized:
  instances: 60
  shadows: disabled
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Plusieurs variables changent simultanément, donc le gain ne peut pas être attribué au LOD.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
benchmark:
  shared_scene: Benchmark_LOD_SignalTower.tscn
  instances: 100
  shadows: enabled
  only_changed_variable: lod_strategy
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction fige la scène et ne change qu’une stratégie à la fois.



### 61.9 Forcer une AABB immense pour éviter le culling



**Symptôme ou risque :** La tour ne disparaît plus, mais le culling devient inefficace dans toute la scène.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
custom_aabb: [-10000, -10000, -10000, 20000, 20000, 20000]
measured: false
rotation_tested: false
reason: avoid_all_culling_bugs
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Une boîte globale masque le défaut local et empêche une élimination efficace.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
aabb_policy:
  bounds: measured_from_all_billboard_rotations
  extra_margin: minimal_measured
  culling_path_test: required
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction calcule une boîte adaptée et teste le parcours de caméra.



### 61.10 Approuver un LOD automatique sans inspection



**Symptôme ou risque :** Les haubans disparaissent de manière irrégulière selon l’angle.



> **[LECTURE] Exemple fautif — Ne pas saisir.**



```yaml
godot_import:
  generate_lods: true
  review: skipped
  decision: approved
```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La génération automatique ne connaît pas la priorité artistique des éléments fins.



> **[LECTURE] Exemple corrigé — Ne pas saisir.**



```yaml
godot_import:
  generate_lods: true
  compare_with_manual_candidate: true
  silhouette_angles: 8
  decision: pending_human_review
```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction conserve l’automatisation comme candidat et impose comparaison et revue multi-angle.



## 62. Porte d’acceptation



La chaîne est acceptée uniquement lorsque les meshes, imposteurs, profils de distance, scène de benchmark et tableau comparatif existent réellement. Les métriques doivent montrer un gain utile sans dégradation perceptuelle excessive aux distances prévues.



La décision finale reste humaine. Les validateurs peuvent contrôler la présence des fichiers, les plages, les identifiants et les métriques, mais pas déclarer seuls une silhouette acceptable.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```yaml
acceptance_gate:
  lod_chain:
    lod0: approved_source
    lod1: produced_and_reviewed
    lod2: produced_and_reviewed
  impostor:
    atlas: produced
    alpha_edges: passed
    orientation: passed
  distance_profiles:
    cameras: measured
    platforms: measured
    hysteresis: passed
  shadows_and_collision:
    proxies: reviewed
    gameplay_authority_preserved: true
  benchmark:
    baseline: complete
    variants: complete
    raw_samples: retained
    comparative_table: complete
  visual_review:
    silhouette: passed
    popping: within_approved_tolerance
  human_approval: required
  current_status: blocked
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Chaîne :** les niveaux proches et lointains doivent être produits et revus.



- **Imposteur :** atlas, bords et orientation possèdent des critères séparés.



- **Profils :** caméras, plateformes et hystérésis sont mesurées.



- **Benchmark :** baseline, variantes, échantillons et tableau sont complets.



- **Décision :** le statut reste bloqué tant que les preuves sont absentes.



## 63. Livrables du chapitre



Le chapitre prépare les cinq livrables permanents du plan maître : chaîne LOD, imposteurs, profils de distance, scène de benchmark et tableau comparatif. Les sources et dérivés restent séparés des exports et rapports.



> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**



```text
production/AST-LOD-PILOT-SIGNAL-TOWER-001/
├── source/
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD0.blend
├── lod/
│   ├── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD1.blend
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_LOD2.blend
├── impostor/
│   ├── AST-LOD-PILOT-SIGNAL-TOWER-001_IMP.ext
│   └── impostor-manifest-v001.json
├── exchange/
│   └── AST-LOD-PILOT-SIGNAL-TOWER-001_v001.glb
├── godot/
│   └── Benchmark_LOD_SignalTower.tscn
└── reports/
    ├── distance-profiles-v001.yaml
    ├── benchmark-raw-v001.json
    └── comparative-table-v001.md
```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Source :** le LOD0 approuvé reste canonique.



- **LOD :** les niveaux manuels sont versionnés séparément.



- **Imposteur :** texture et manifeste décrivent la capture.



- **Moteur :** le GLB et la scène de benchmark portent la chaîne candidate.



- **Rapports :** profils, données brutes et comparaison rendent la décision traçable.



## 64. Sources officielles qualifiées



Les mécanismes du chapitre sont reliés aux documentations officielles. Le manuel Blender décrit le modifier Decimate et ses modes Collapse, Un-Subdivide et Planar. La documentation Godot 4.7 décrit le LOD automatique des meshes, les plages de visibilité, l’hystérésis, les modes de fondu, `lod_bias`, les billboards et les limites de l’occlusion culling.



La documentation Blender 5.0 sert de référence publique détaillée lorsque la documentation 5.2 n’expose pas encore la même granularité. Les libellés d’interface sont revérifiés dans Blender 5.2 avant production.



- [Blender Manual — Decimate Modifier](https://docs.blender.org/manual/en/5.0/modeling/modifiers/generate/decimate.html)

- [Godot 4.7 — Mesh level of detail](https://docs.godotengine.org/en/4.7/tutorials/3d/mesh_lod.html)

- [Godot 4.7 — Visibility ranges](https://docs.godotengine.org/en/4.7/tutorials/3d/visibility_ranges.html)

- [Godot 4.7 — GeometryInstance3D](https://docs.godotengine.org/en/4.7/classes/class_geometryinstance3d.html)

- [Godot 4.7 — StandardMaterial3D](https://docs.godotengine.org/en/4.7/classes/class_standardmaterial3d.html)

- [Godot 4.7 — Occlusion culling](https://docs.godotengine.org/en/4.7/tutorials/3d/occlusion_culling.html)

- [Godot 4.7 — Importing 3D scenes](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html)



## 65. Conclusion



Une bonne chaîne LOD ne se résume ni à un ratio de décimation ni à une série de distances. Elle relie taille écran, importance gameplay, silhouette, surfaces, mémoire, ombres, collisions, renderer et caméra dans un contrat mesuré. L’imposteur n’est utile que si son coût texture et ses artefacts restent inférieurs à ceux du mesh qu’il remplace.



`AST-LOD-PILOT-SIGNAL-TOWER-001` fournit un pilote complet pour comparer LOD manuel, LOD automatique, HLOD, imposteur, billboard et proxies. Tant que les meshes, textures, scènes, captures et mesures n’existent pas, le chapitre reste au niveau `static-review` et aucune amélioration runtime n’est revendiquée.
