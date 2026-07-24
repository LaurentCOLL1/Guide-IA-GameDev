---
title: "Livre III — Chapitre 19 : Rigging et skinning"
id: "DOC-L3-CH19"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 19
last-verified: "2026-07-24T04:10:00+02:00"
audit-status: "complete"
audit-date: "2026-07-24T04:10:00+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-19.md"
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

# Rigging et skinning

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH19`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Transformer un personnage finalisé en système de déformation contrôlable, exportable et réutilisable sans confondre le squelette livré avec les outils internes de l’animateur.

Le fil rouge utilise `AST-RIG-PILOT-SCOUT-001`, un éclaireur humanoïde équipé d’une veste, de bottes, d’une sacoche et de sockets d’accessoires. Le chapitre documente les contrats ; aucun rig Blender, GLB ou test Godot n’est présenté comme produit.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
Maillage final approuvé
    ↓
Convention d’axes, échelle et rest pose
    ↓
Squelette de déformation
    ↓
Rig de contrôle non exporté
    ↓
Skinning et corrections
    ↓
Poses extrêmes et rapport
    ↓
Export glTF filtré
    ↓
Import Godot, retargeting et sockets
    ↓
Porte d’acceptation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendance :** le maillage final, ses matériaux et ses LOD sont gelés avant le bind.

- **Séparation :** les contrôleurs Blender ne deviennent pas automatiquement des os de déformation.

- **Validation :** chaque étape produit une preuve ou une réserve explicite.

- **Limite :** les animations elles-mêmes appartiennent au chapitre 20.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura concevoir une hiérarchie stable, régler le roll, distinguer IK et FK, limiter les influences, corriger les poids et préparer le retargeting.

Il saura aussi diagnostiquer les inversions d’axes, les volumes écrasés, les glissements de sockets et les incompatibilités de rest pose.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  skeleton: [hierarchy, naming, roll, rest_pose]
  controls: [constraints, ik, fk, spaces]
  skinning: [weights, influences, correctives]
  exchange: [gltf, skeleton3d, bone_map, sockets]
  evidence: [pose_grid, report, structural_validation]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Squelette :** la hiérarchie et les orientations sont traitées comme une interface versionnée.

- **Contrôles :** les mécanismes d’animation restent remplaçables tant que le squelette livré est stable.

- **Skinning :** les poids sont évalués en mouvement plutôt qu’en pose neutre uniquement.

- **Échange :** Blender et Godot partagent noms, rests et responsabilités explicites.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les commandes, structures YAML, scripts Python et GDScript sont des contrats documentaires non exécutés.

Les angles, nombres d’os, limites d’influences et seuils de qualité sont des candidats à mesurer sur le pilote réel et les plateformes de référence.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static-review
  blender_execution: false
  rig_created: false
  weights_painted: false
  gltf_exported: false
  godot_imported: false
  deformation_tests_executed: false
  pdf_produced: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la cohérence documentaire est vérifiée sans revendiquer une production 3D.

- **Valeurs :** les paramètres chiffrés restent candidats tant qu’aucun test réel n’existe.

- **Traçabilité :** les réserves empêchent de transformer un exemple en résultat de production.

- **Publication :** le PDF du Livre III reste différé à la fin du livre.

## 4. Frontières avec les chapitres voisins

Le chapitre 18 demeure propriétaire des LOD et proxies. Le chapitre 20 créera les poses animées, cycles, courbes et blend trees. Le chapitre 21 approfondira la capture de mouvement.

Le chapitre 28 prendra en charge l’intégration globale ; ici, Godot sert uniquement à vérifier la structure importée, les rests, les profils de retargeting et les sockets.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapter_18: lod_chain
  chapter_19: rigging_and_skinning
  chapter_20: authored_animation
  chapter_21: motion_capture
  chapter_28: global_asset_integration
  book_iv: whole_game_optimization
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** le chapitre 18 fournit des représentations géométriques déjà approuvées.

- **Autorité :** le présent chapitre possède squelette, contrôles, poids et contrats d’export.

- **Aval :** les animations consomment le rig sans redéfinir sa structure publiée.

- **Exclusion :** aucun système gameplay n’est placé dans l’armature.

## 5. Asset pilote et cas de validation

Le pilote humanoïde combine articulations standards, accessoires rigides, vêtement proche du corps et sacoche secondaire. Il expose les problèmes typiques sans nécessiter un système facial complet.

Une grille de poses couvre accroupissement, portée haute, torsion, course extrême, appui unipodal et prises d’accessoire.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pilot:
  asset_id: AST-RIG-PILOT-SCOUT-001
  body_type: humanoid
  deformable_parts: [body, jacket, boots]
  rigid_accessories: [radio, pouch]
  sockets: [hand_r, hand_l, back, hip_r]
  test_families: [torso, limbs, hands, accessories]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Choix :** le pilote couvre plusieurs familles de déformation dans un seul contrat.

- **Accessoires :** les éléments rigides testent les sockets et le parenting sans poids diffus.

- **Vêtement :** la veste vérifie les intersections et la continuité des poids.

- **Portée :** le visage détaillé reste hors du pilote afin de garder un lot maîtrisable.

## 6. Contrat de l’asset riggé

Une fiche de rig lie identité, version du maillage, squelette, profil de skinning, sockets, export et preuves. Modifier un nom d’os publié crée une nouvelle version incompatible.

La fiche ne stocke ni animation finale ni logique gameplay ; elle décrit une interface technique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rig_asset:
  asset_id: AST-RIG-PILOT-SCOUT-001
  mesh_version: 1.0.0
  rig_version: 1.0.0
  skeleton_contract: HUMANOID-ASTERIA-V1
  skin_profile: SKIN-HUMANOID-GAME-V1
  export_profile: GLTF-RIGGED-V1
  status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** l’asset et le contrat de squelette possèdent des versions indépendantes.

- **Compatibilité :** un consommateur peut refuser une version de rig non prise en charge.

- **Révision :** chaque changement structurel est visible dans le manifeste.

- **Décision :** le statut reste candidat avant revue de déformation et import.

## 7. Vocabulaire opérationnel

Le squelette de déformation influence le maillage ; le rig de contrôle aide l’animateur ; le skin relie sommets et os ; la rest pose définit le référentiel ; la pose est l’état animé.

Cette distinction évite d’exporter des contrôleurs, de peindre sur des os techniques ou de confondre position neutre et pose de repos.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
terms:
  deform_bone: influences_vertices
  control_bone: drives_other_bones
  helper_bone: solves_or_corrects
  rest_pose: bind_reference
  pose: animated_transform
  skin: mesh_to_bone_binding
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déformation :** seuls les os autorisés reçoivent des groupes de sommets.

- **Contrôle :** les widgets et mécanismes peuvent rester propres à Blender.

- **Référence :** la rest pose participe au bind et au retargeting.

- **Lecture :** un vocabulaire stable réduit les erreurs entre métiers.

## 8. Références anatomiques et mesures

Le placement des pivots suit des repères anatomiques observables : centre de rotation de hanche, axe du genou, ligne de cheville, articulation de l’épaule et base des doigts.

La position est validée en vues orthogonales et en volume, jamais sur une silhouette frontale seule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
landmarks:
  shoulder: humeral_head_center
  elbow: flexion_axis
  wrist: carpal_center
  hip: femoral_head_center
  knee: hinge_axis_candidate
  ankle: talocrural_center
  source: approved_anatomy_reference
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repères :** les pivots sont reliés à des structures fonctionnelles plutôt qu’à des creux visuels.

- **Vues :** face, profil et perspective évitent une erreur de profondeur.

- **Symétrie :** les côtés sont comparés sans supposer un corps parfaitement symétrique.

- **Preuve :** les sources anatomiques et droits restent associés au pilote.

## 9. Axes, unités et transformations

Le maillage et l’armature partagent l’échelle, l’orientation et une transformation propre avant le bind. Une échelle non uniforme dans la chaîne peut déformer les contraintes et compliquer l’export.

Les corrections d’axes sont réalisées à la source plutôt qu’au moyen d’un parent compensatoire caché.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
transform_contract:
  blender_units: meters
  object_scale: [1.0, 1.0, 1.0]
  armature_scale: [1.0, 1.0, 1.0]
  forward_axis_contract: documented
  up_axis_contract: documented
  compensation_parent: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Échelle :** maillage et armature utilisent le même référentiel métrique.

- **Contraintes :** une base propre rend les espaces locaux prévisibles.

- **Export :** les axes de conversion appartiennent au profil glTF, pas à un correctif improvisé.

- **Diagnostic :** toute compensation cachée est traitée comme dette bloquante.

## 10. Rest pose et pose de modélisation

La rest pose est choisie pour faciliter déformation, retargeting et compatibilité des vêtements. Elle n’est pas une pose esthétique destinée à une capture finale.

A-pose ou T-pose sont évaluées selon épaules, aisselles, mains et bibliothèque cible ; la décision est écrite et ne change pas silencieusement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
rest_pose_contract:
  pose_name: ASTERIA_A_REFERENCE
  arms_abduction_deg_candidate: 45
  palms_orientation: inward_candidate
  feet: parallel_candidate
  facial_neutral: true
  change_requires_rebind: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Choix :** la pose répond au pipeline et non à une préférence isolée.

- **Candidat :** les angles restent à confirmer sur le pilote réel.

- **Conséquence :** modifier la rest pose invalide bind, poids, correctifs et parfois animations.

- **Version :** une modification approuvée produit une nouvelle version de squelette.

## 11. Nommage des os

Les noms sont uniques, stables, lisibles et dépourvus de caractères interdits ou ambigus. Les suffixes de côté restent cohérents dans Blender, le manifeste et Godot.

Les contrôleurs portent un préfixe distinct et ne réutilisent jamais le nom d’un os de déformation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bone_naming:
  deform_prefix: DEF_
  control_prefix: CTRL_
  mechanism_prefix: MCH_
  side_suffixes: [_L, _R, _C]
  examples: [DEF_upper_arm_L, DEF_spine_02, CTRL_hand_R]
  unique_names_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préfixes :** chaque rôle est visible sans ouvrir les propriétés internes.

- **Côtés :** les outils de miroir utilisent une convention constante.

- **Godot :** les noms exportés restent compatibles avec la recherche d’os et les BoneMaps.

- **Migration :** renommer un os publié exige un tableau de correspondance.

## 12. Hiérarchie et ordre parental

La hiérarchie de déformation suit le transfert de mouvement : racine, bassin, colonne, ceintures, membres et extrémités. Les os techniques ne créent pas de dépendance cyclique.

Un parent logique n’est pas forcément connecté physiquement ; la connexion est choisie selon le besoin de translation indépendante.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hierarchy:
  root: DEF_root
  pelvis: DEF_pelvis
  spine: [DEF_spine_01, DEF_spine_02, DEF_chest]
  left_arm: [DEF_clavicle_L, DEF_upper_arm_L, DEF_forearm_L, DEF_hand_L]
  left_leg: [DEF_thigh_L, DEF_shin_L, DEF_foot_L, DEF_toe_L]
  cycles_allowed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Flux :** le parent transmet un mouvement attendu à ses descendants.

- **Connexion :** un espace entre tête et queue peut être intentionnel et documenté.

- **Ordre :** les parents précèdent les enfants dans l’interface moteur.

- **Contrôle :** les mécanismes restent hors de la hiérarchie exportée lorsque possible.

## 13. Racine, bassin et déplacement global

`DEF_root` fournit le repère du squelette ; `DEF_pelvis` porte le bassin et la colonne. Le déplacement de gameplay ou root motion ne doit pas être décidé par un nom d’os implicite.

Le chapitre documente le contrat d’os racine, mais la production des courbes de root motion appartient au chapitre 20.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
root_contract:
  skeleton_root: DEF_root
  pelvis_bone: DEF_pelvis
  root_motion_track: reserved_for_chapter_20
  gameplay_authority: external
  scale_reference_bone: DEF_pelvis
  zero_transform_in_rest: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Repère :** la racine stabilise l’ensemble du squelette.

- **Bassin :** le centre corporel reste distinct du déplacement global.

- **Gameplay :** le rig n’accorde aucune autorité de locomotion au runtime.

- **Retargeting :** l’os de référence d’échelle est déclaré explicitement.

## 14. Squelette de déformation

Le squelette exporté contient uniquement les os nécessaires au maillage, aux correctifs approuvés et aux sockets contractualisés. Chaque os supplémentaire augmente maintenance, poids et compatibilité.

La propriété de déformation est activée uniquement lorsque l’os doit posséder un groupe de sommets.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
deform_skeleton_policy:
  export_roles: [DEF, SOCKET]
  control_roles_exported: false
  mechanism_roles_exported: false
  deform_flag_required_for_vertex_groups: true
  unused_bones: forbidden
  review_owner: rig_lead
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Budget :** le nombre d’os est une ressource de production et de runtime.

- **Poids :** un os non déformant ne reçoit pas de groupe par accident.

- **Export :** les rôles autorisés sont filtrés par collection et manifeste.

- **Revue :** chaque exception possède un propriétaire et une justification.

## 15. Rig de contrôle non exporté

Le rig de contrôle offre formes personnalisées, IK/FK, espaces et contraintes sans modifier l’interface publiée du squelette de déformation.

Les contrôleurs servent l’ergonomie de l’animateur ; ils ne sont pas une garantie de compatibilité glTF.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
control_rig:
  collection: RIG_CONTROLS
  export: false
  controls: [root, cog, chest, head, hands, feet]
  mechanisms: [ik_solver, pole_targets, space_switch]
  custom_shapes: allowed
  dependency_on_gameplay: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ergonomie :** les contrôles correspondent aux gestes de l’animateur.

- **Encapsulation :** les contraintes peuvent évoluer sans renommer les os exportés.

- **Filtrage :** la collection de contrôle est exclue du paquet glTF.

- **Sécurité :** aucune règle gameplay n’est encodée dans un contrôleur.

## 16. Collections d’os et visibilité

Les collections d’os regroupent déformation, contrôles, mécanismes, correctifs et sockets. La visibilité de travail ne doit pas modifier le contenu exporté par accident.

Un preset d’affichage permet de revoir rapidement uniquement la hiérarchie publiée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bone_collections:
  DEFORM: {visible: true, export_candidate: true}
  CONTROLS: {visible: true, export_candidate: false}
  MECHANISMS: {visible: false, export_candidate: false}
  CORRECTIVES: {visible: false, export_candidate: true}
  SOCKETS: {visible: true, export_candidate: true}
  export_review_preset: DEFORM_CORRECTIVES_SOCKETS
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation :** les rôles sont séparés sans multiplier les armatures.

- **Affichage :** masquer un os ne change pas automatiquement son statut d’export.

- **Preset :** la revue de livraison montre uniquement l’interface publiée.

- **Automatisation :** les scripts vérifient les rôles au lieu de dépendre de l’état visuel.

## 17. Orientation et roll des os

Le roll définit l’orientation locale autour de la longueur de l’os dans la rest pose. Une chaîne cohérente facilite contraintes, axes de rotation, miroir et retargeting.

Le recalcul automatique est un point de départ ; les épaules, avant-bras, mains et doigts sont inspectés individuellement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
roll_policy:
  limbs_reference_axis: documented
  mirrored_chains: equivalent_local_axes
  twist_chains: continuous_roll
  fingers: consistent_flexion_axis
  automatic_recalculate: review_required
  zero_roll_everywhere: forbidden_assumption
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Définition :** le roll appartient au référentiel local de repos.

- **Chaînes :** une continuité cohérente réduit les retournements de contraintes.

- **Miroir :** les côtés doivent se comporter symétriquement sans axes opposés imprévus.

- **Revue :** un roll numériquement simple n’est pas nécessairement anatomiquement correct.

## 18. Symétrie et asymétries contrôlées

La structure de base est créée symétriquement lorsque l’anatomie et le costume le permettent. Les asymétries réelles sont ensuite introduites comme décisions explicites.

Un accessoire porté d’un seul côté ne justifie pas de casser la convention des os corporels.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
symmetry_policy:
  base_skeleton: mirrored
  side_names: enforced
  body_asymmetry: documented_exception
  accessory_asymmetry: socket_level
  weight_mirror: reviewed
  pose_comparison: bilateral
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** la symétrie accélère création et diagnostic.

- **Exceptions :** une asymétrie possède une raison anatomique ou artistique.

- **Accessoires :** les différences de costume restent aux sockets ou aux poids locaux.

- **Tests :** les poses bilatérales révèlent les divergences de roll et d’influence.

## 19. Bassin et colonne

Le bassin porte les jambes et la colonne ; la chaîne vertébrale répartit flexion, extension et torsion sans concentrer tout le mouvement sur un seul os.

Le nombre d’os dépend de la silhouette, des vêtements et des besoins d’animation, pas d’une valeur universelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
torso_chain:
  pelvis: DEF_pelvis
  spine_bones: [DEF_spine_01, DEF_spine_02, DEF_chest]
  optional_upper_chest: candidate
  bend_distribution: measured_in_pose_grid
  twist_distribution: progressive
  scale_animation: discouraged
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bassin :** il relie membres inférieurs et tronc sans devenir une racine globale.

- **Répartition :** plusieurs segments produisent une courbure plus contrôlable.

- **Budget :** un os est conservé seulement s’il améliore une pose observée.

- **Échelle :** la déformation privilégie rotations et translations prévues.

## 20. Cou et tête

La chaîne du cou soutient orientation de tête et lecture de silhouette. La tête possède un référentiel stable pour caméra, regard et accessoires futurs.

Les contrôles de regard et l’animation faciale ne sont pas produits ici, mais les os de référence nécessaires sont réservés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
head_chain:
  neck: [DEF_neck_01, DEF_neck_02]
  head: DEF_head
  eye_reference_bones: [DEF_eye_L, DEF_eye_R]
  jaw_bone: optional_candidate
  camera_socket: SOCKET_head_camera
  facial_animation: chapter_20_boundary
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cou :** la courbure est répartie selon les poses cibles.

- **Tête :** son axe local demeure stable pour les dépendances aval.

- **Références :** les yeux et la mâchoire sont inclus seulement si le pilote les utilise.

- **Frontière :** aucune courbe de regard ou faciale n’est créée dans ce chapitre.

## 21. Bras, clavicules et avant-bras

La clavicule accompagne l’élévation du bras ; l’épaule, le coude et le poignet conservent des axes locaux cohérents. L’avant-bras peut recevoir une chaîne de twist.

Le pivot de l’épaule est vérifié en portée haute, croisement et main derrière le dos.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
arm_chain:
  clavicle: DEF_clavicle_L
  upper_arm: DEF_upper_arm_L
  forearm: DEF_forearm_L
  hand: DEF_hand_L
  twist: [DEF_upper_arm_twist_L, DEF_forearm_twist_L]
  validation_poses: [overhead, cross_body, behind_back]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clavicule :** elle participe au geste plutôt que de laisser l’humérus tout compenser.

- **Axes :** le coude se plie dans un plan prévisible pour IK et FK.

- **Twist :** la rotation axiale est distribuée sur la longueur du membre.

- **Validation :** les poses difficiles déterminent la qualité réelle de la chaîne.

## 22. Mains et doigts

La paume possède un repère stable ; chaque doigt suit une chaîne cohérente de flexion. Les métacarpiens sont ajoutés seulement si leur mouvement améliore la silhouette ou les prises.

Le pouce reçoit une orientation distincte adaptée à l’opposition plutôt qu’une copie des autres doigts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hand_contract:
  palm: DEF_hand_L
  thumb: [DEF_thumb_01_L, DEF_thumb_02_L, DEF_thumb_03_L]
  index: [DEF_index_01_L, DEF_index_02_L, DEF_index_03_L]
  metacarpals: optional_by_pose_test
  curl_axis: consistent_per_digit
  grip_socket: SOCKET_grip_L
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paume :** elle sert de base aux doigts et au socket de prise.

- **Pouce :** son opposition exige un axe et un placement spécifiques.

- **Métacarpiens :** ils sont justifiés par les poses de prise, pas par habitude.

- **Socket :** la prise rigide reste distincte des poids des doigts.

## 23. Jambes, genoux et chevilles

La hanche, le genou et la cheville forment une chaîne dont le plan de flexion est stable. Le genou ne doit pas être aligné sur une vue frontale seulement.

La longueur des segments et le placement des pivots sont comparés aux repères anatomiques et au volume du maillage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
leg_chain:
  thigh: DEF_thigh_L
  shin: DEF_shin_L
  foot: DEF_foot_L
  toe: DEF_toe_L
  twist: [DEF_thigh_twist_L, DEF_shin_twist_L]
  validation_poses: [deep_squat, high_step, kneel]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hanche :** le pivot soutient flexion, abduction et rotation.

- **Genou :** son axe évite les déviations latérales de l’IK.

- **Cheville :** elle conserve un repère utile au pied et aux contrôles.

- **Tests :** accroupissement et agenouillement révèlent les erreurs de placement.

## 24. Pieds, orteils et appuis

Le pied distingue cheville, plante, pivot d’orteil et points de roulement du rig de contrôle. Seuls les os qui déforment ou servent de socket sont exportés.

Les pivots de heel roll et toe roll peuvent rester des mécanismes Blender.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
foot_contract:
  deform: [DEF_foot_L, DEF_toe_L]
  controls: [CTRL_foot_L, CTRL_toe_L]
  mechanisms: [MCH_heel_roll_L, MCH_ball_roll_L]
  ground_contact_reference: SOCKET_sole_L
  export_mechanisms: false
  sole_alignment_test: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déformation :** le pied et l’orteil suffisent souvent au maillage.

- **Contrôle :** les pivots de roulement améliorent l’ergonomie sans polluer l’export.

- **Contact :** un repère de semelle aide les tests aval sans fixer la physique.

- **Validation :** les appuis sont revus sur sol plat et pente candidate.

## 25. Os faciaux et secondaires

Le pilote peut conserver yeux et mâchoire si leur présence est requise par le profil humanoïde. Les systèmes faciaux complets, cheveux dynamiques et chaînes de tissu suivent des contrats dédiés.

Un os secondaire n’est ajouté que si son animation ou sa déformation sera réellement produite et testée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
secondary_bone_policy:
  eyes: optional_required_by_profile
  jaw: optional_required_by_content
  facial_full_rig: excluded
  cloth_secondary_rig: separate_contract
  hair_secondary_rig: separate_contract
  unused_secondary_bones: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** le chapitre prépare l’interface sans développer un rig facial complet.

- **Coût :** chaque os secondaire augmente poids, tests et retargeting.

- **Contrat :** tissu et cheveux peuvent utiliser un squelette distinct versionné.

- **Décision :** un os sans contenu aval identifié est supprimé.

## 26. Contraintes et ordre d’évaluation

Les contraintes transforment les contrôles en poses du squelette de déformation. Leur ordre, espace propriétaire, cible et influence sont documentés.

Une contrainte qui corrige visuellement une erreur d’orientation ne remplace pas la correction du rest.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
constraint_record:
  owner: DEF_forearm_L
  type: COPY_ROTATION
  target: MCH_forearm_twist_driver_L
  owner_space: LOCAL
  target_space: LOCAL
  influence: 0.5
  purpose: distribute_twist
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaire :** l’os affecté est nommé sans ambiguïté.

- **Espaces :** local et monde ne sont pas interchangeables.

- **Influence :** la valeur est liée à une fonction mesurable.

- **Dette :** les contraintes ne cachent pas une rest pose incorrecte.

## 27. Chaînes IK

L’IK résout une chaîne depuis une cible et un pole target. La longueur de chaîne, les limites articulaires et l’orientation initiale déterminent sa stabilité.

Les mains et pieds utilisent des cibles séparées du squelette de déformation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ik_chain:
  end_bone: DEF_shin_L
  target: CTRL_foot_IK_L
  pole_target: CTRL_knee_pole_L
  chain_length: 2
  stretch: false
  rest_bend: small_nonzero
  validation: [front, side, extreme_reach]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chaîne :** deux segments couvrent cuisse et tibia sans entraîner le bassin.

- **Pole :** la cible stabilise le plan du genou.

- **Repos :** une légère flexion évite une solution ambiguë parfaitement droite.

- **Tests :** les vues multiples révèlent les flips et dérives.

## 28. Pole targets et plans de flexion

Le pole target est placé dans le plan anatomique de flexion et à une distance suffisante pour rester stable. Sa position n’est pas copiée mécaniquement d’un autre personnage.

Le pole angle est calculé après réglage du roll, puis conservé dans le profil du rig.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pole_target:
  chain: left_leg
  control: CTRL_knee_pole_L
  basis: rest_pose_flexion_plane
  distance_rule: proportional_to_limb_length
  pole_angle_deg: measured
  mirror_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plan :** le pole suit la direction naturelle du genou ou du coude.

- **Distance :** un placement proportionnel résiste mieux aux changements d’échelle.

- **Roll :** le réglage vient après l’orientation locale des os.

- **Miroir :** les deux côtés sont comparés en pose identique.

## 29. Contrôles FK

La FK expose une rotation hiérarchique directe, utile pour arcs libres, balancements et gestes où l’extrémité ne doit pas rester fixée.

Les formes de contrôle indiquent l’axe principal et évitent de masquer le maillage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
fk_controls:
  arm_L: [CTRL_upper_arm_FK_L, CTRL_forearm_FK_L, CTRL_hand_FK_L]
  parent_space: local_chain
  rotation_mode: project_standard
  translation_locked: true
  scale_locked: true
  custom_shape_orientation: axis_readable
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hiérarchie :** chaque contrôle entraîne naturellement ses descendants.

- **Canaux :** les transformations non prévues sont verrouillées.

- **Rotation :** un mode standard réduit les divergences entre rigs.

- **Lisibilité :** les formes montrent la fonction sans devenir partie de l’export.

## 30. Commutation IK/FK

La commutation mélange deux solutions vers le même squelette de déformation. Le snap conserve la pose mondiale de la main ou du pied lors du changement.

Le paramètre de mélange appartient au rig de contrôle ; les os exportés reçoivent seulement le résultat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ik_fk_switch:
  property: arm_ik_fk_L
  range: [0.0, 1.0]
  snap_fk_to_ik: required
  snap_ik_to_fk: required
  deform_output: DEF_arm_chain_L
  exported_property: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mélange :** une propriété contrôle l’influence des deux solutions.

- **Snap :** les outils alignent les contrôleurs avant de changer de mode.

- **Sortie :** une seule chaîne de déformation est livrée.

- **Frontière :** l’animation des commutations sera traitée au chapitre 20.

## 31. Changement d’espace

Un contrôle peut suivre monde, bassin, poitrine ou tête selon le geste. Le changement d’espace doit préserver la transformation visuelle et être limité aux besoins réels.

Multiplier les espaces sans cas d’usage augmente les risques de snap et la charge d’animation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
space_switch:
  control: CTRL_hand_IK_L
  allowed_spaces: [WORLD, CHEST, ROOT]
  default: WORLD
  preserve_world_transform_on_switch: true
  keyable: chapter_20
  undocumented_spaces: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Choix :** chaque espace correspond à un besoin d’animation identifié.

- **Conservation :** la main ne saute pas lors du changement.

- **Défaut :** un comportement stable est défini pour les nouvelles scènes.

- **Budget :** les espaces inutilisés sont supprimés.

## 32. Étirement et limites articulaires

L’étirement peut aider une pose stylisée ou une correction minime, mais ne doit pas masquer une mauvaise proportion ou un target inaccessible.

Les limites servent de garde-fou du contrôle, sans prétendre reproduire une biomécanique médicale.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
limb_limits:
  ik_stretch: disabled_by_default
  stretch_max_ratio_candidate: 1.02
  elbow_flexion_deg_candidate: [0, 150]
  knee_flexion_deg_candidate: [0, 155]
  hyperextension: blocked_candidate
  production_measurement_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** le rig conserve les proportions sauf décision artistique.

- **Candidat :** les angles ne sont pas des vérités anatomiques universelles.

- **Contrôle :** les limites préviennent les poses destructrices courantes.

- **Mesure :** le pilote réel décide des valeurs acceptables.

## 33. Twist bones et distribution axiale

Les twist bones distribuent la rotation autour des bras et jambes pour éviter un pincement concentré. Leur influence est progressive et validée sur le volume.

Ils ne compensent pas une topologie insuffisante autour de l’articulation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
twist_distribution:
  source: DEF_forearm_L
  bones: [DEF_forearm_twist_01_L, DEF_forearm_twist_02_L]
  rotation_factors: [0.33, 0.66]
  axis: local_limb_axis
  weights: longitudinal_gradient
  topology_review_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la rotation provient de l’os principal du segment.

- **Facteurs :** la torsion est répartie graduellement.

- **Poids :** le gradient suit la longueur plutôt qu’un anneau brutal.

- **Topologie :** une densité et des boucles adaptées restent nécessaires.

## 34. Épaules, clavicules et omoplates

L’élévation du bras combine clavicule, humérus et éventuellement correctif d’omoplate. Une solution purement automatique produit souvent une aisselle écrasée.

Les poses hautes sont évaluées avec la veste et les accessoires visibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shoulder_system:
  clavicle_driver: CTRL_clavicle_L
  upper_arm_driver: CTRL_upper_arm_FK_L
  scapula_corrective: optional
  corrective_trigger: arm_elevation_candidate
  test_angles_deg: [45, 90, 140]
  jacket_intersection_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Coordination :** plusieurs éléments partagent le mouvement de l’épaule.

- **Correctif :** l’omoplate est ajoutée seulement si la pose le justifie.

- **Échantillons :** plusieurs élévations révèlent les ruptures progressives.

- **Costume :** la validation inclut le vêtement final.

## 35. Os correctifs

Un os correctif répare un volume local de manière contrôlable lorsqu’une pondération standard ne suffit pas. Son déclenchement, son axe et ses poids sont documentés.

Les correctifs ne sont pas multipliés avant d’avoir testé topologie, roll et poids de base.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
corrective_bone:
  name: DEF_shoulder_corrective_L
  trigger: upper_arm_elevation
  driver_space: local
  affected_region: deltoid_and_armpit
  export: true
  fallback_review: topology_then_weights
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cause :** le correctif répond à un défaut observé dans une pose précise.

- **Espace :** son calcul reste stable dans le référentiel choisi.

- **Export :** un os correctif déformant appartient au contrat publié.

- **Ordre :** les solutions simples sont vérifiées avant d’ajouter une dépendance.

## 36. Sockets et accessoires

Les sockets sont des os ou repères dédiés aux accessoires rigides : prise de main, dos, hanche, tête. Ils suivent un os parent sans recevoir de poids diffus.

Le socket décrit une transformation ; l’autorité d’équiper, détacher ou utiliser l’objet reste dans le gameplay.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
sockets:
  SOCKET_grip_R: {parent: DEF_hand_R, purpose: held_item}
  SOCKET_back: {parent: DEF_chest, purpose: stowed_item}
  SOCKET_hip_R: {parent: DEF_pelvis, purpose: holster}
  SOCKET_head_camera: {parent: DEF_head, purpose: reference_only}
  gameplay_authority: external
  versioned_transforms: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rigidité :** un accessoire rigide suit une transformation plutôt qu’un champ de poids.

- **Parent :** le socket est attaché à l’os fonctionnel approprié.

- **Autorité :** le rig ne décide pas quand un objet est équipé.

- **Version :** déplacer un socket publié exige une validation de compatibilité.

## 37. Modificateur Armature et ordre des modificateurs

Le modificateur Armature relie le maillage au squelette et utilise groupes de sommets ou enveloppes selon le profil. Son ordre par rapport aux correctifs de surface est explicite.

`Preserve Volume` est évalué sur le pilote ; il n’est pas activé par réflexe pour tous les assets.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
armature_modifier:
  object: SCOUT_BODY
  armature: AST_RIG_SCOUT
  vertex_groups: true
  bone_envelopes: false
  preserve_volume: candidate_test
  modifier_order: documented
  bind_version: 1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** le modificateur pointe vers l’armature canonique.

- **Méthode :** les groupes contrôlés remplacent les enveloppes pour la livraison.

- **Volume :** l’option est comparée sur les articulations difficiles.

- **Ordre :** les autres modificateurs sont évalués selon le résultat exporté.

## 38. Bind initial et groupes de sommets

Le bind crée une première relation entre maillage et os. Les groupes portent exactement les noms des os déformants et excluent contrôleurs, mécanismes et sockets.

La réussite d’un bind automatique ne constitue jamais une approbation des poids.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bind_contract:
  mesh: SCOUT_BODY
  armature: AST_RIG_SCOUT
  method_candidate: automatic_weights
  allowed_group_prefix: DEF_
  empty_deform_groups: reported
  control_groups: forbidden
  status_after_bind: requires_manual_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Noms :** les groupes correspondent à l’interface de déformation.

- **Filtre :** les rôles non déformants ne reçoivent aucun poids.

- **Rapport :** les groupes vides ou sommets non référencés sont signalés.

- **Revue :** le bind n’est qu’un point de départ.

## 39. Poids automatiques et nettoyage manuel

Les poids automatiques accélèrent l’initialisation, puis chaque articulation est examinée en mouvement. Les erreurs de proximité sont courantes entre bras et torse, doigts voisins ou jambes et accessoires.

Le nettoyage utilise sélection de sommets, masques et groupes verrouillés plutôt qu’un brossage imprécis sur tout le personnage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
automatic_weight_review:
  generated: candidate
  mandatory_regions: [shoulders, elbows, wrists, hips, knees, ankles, fingers]
  proximity_false_positives: reported
  manual_cleanup: required
  pose_driven_review: true
  approval: human
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Initialisation :** l’automatique fournit une estimation rapide.

- **Régions :** les zones à fort risque possèdent une liste de contrôle.

- **Méthode :** les corrections ciblent des sommets identifiés.

- **Décision :** une revue humaine approuve la déformation.

## 40. Normalisation des poids

Un workflow normalisé rend les influences lisibles : la somme des groupes déformants d’un sommet est contrôlée, les groupes verrouillés sont compris et `Auto Normalize` maintient la cohérence pendant la peinture.

La normalisation n’améliore pas à elle seule une distribution anatomiquement mauvaise.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
weight_normalization:
  normalize_all_before_review: true
  auto_normalize_during_paint: true
  locked_groups_reviewed: true
  zero_total_vertices: forbidden
  normalization_is_quality_proof: false
  report_tolerance: project_defined
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Somme :** les influences relatives sont maîtrisées et comparables.

- **Verrous :** un groupe verrouillé peut empêcher le résultat attendu et doit être visible.

- **Zéro :** un sommet sans influence est bloquant pour un mesh skinné.

- **Qualité :** une somme correcte ne garantit pas un bon volume.

## 41. Budget d’influences par sommet

Le nombre maximal d’influences est défini selon moteur, plateforme et profil d’asset. Les influences minuscules sont nettoyées avant limitation, puis la déformation est revue.

Réduire brutalement les influences peut créer une cassure sur l’épaule ou le bassin.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
influence_budget:
  max_influences_candidate: 4
  cleanup_threshold_candidate: 0.001
  normalize_after_limit: true
  platform_profiles: [desktop, mobile]
  before_after_pose_review: required
  measured_export_count: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Budget :** la limite répond au profil de livraison.

- **Nettoyage :** les contributions négligeables sont supprimées avant troncature.

- **Normalisation :** les poids restants retrouvent une somme cohérente.

- **Comparaison :** la silhouette est vérifiée avant et après limitation.

## 42. Verrous, masques et sélection

Les groupes validés sont verrouillés pendant le travail sur une région voisine. Les masques de visage ou de sommets réduisent les coups de pinceau accidentels.

Un verrou oublié est diagnostiqué avant de conclure que Blender ignore la peinture.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
weight_edit_session:
  active_region: left_shoulder
  visible_groups: [DEF_clavicle_L, DEF_upper_arm_L, DEF_chest]
  locked_approved_groups: true
  vertex_mask: enabled
  auto_normalize: enabled
  session_note: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Isolation :** seuls les groupes utiles à la région sont exposés.

- **Protection :** les zones déjà approuvées ne changent pas silencieusement.

- **Masque :** la sélection réduit les erreurs sur la face opposée.

- **Diagnostic :** les verrous sont inspectés avant toute réparation destructive.

## 43. Miroir des poids

Le miroir utilise noms de côté et correspondance topologique. Il accélère la base symétrique, puis chaque côté est revu avec ses asymétries de maillage et de costume.

Un miroir réussi techniquement peut être faux sur une sacoche latérale ou un pli asymétrique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
weight_mirror:
  source_side: L
  target_side: R
  naming_convention: suffix
  topology_correspondence: verified
  asymmetric_regions_excluded: [pouch_contact, jacket_fold_R]
  bilateral_pose_review: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Correspondance :** la géométrie et les noms permettent une association déterministe.

- **Exclusions :** les asymétries connues ne sont pas écrasées.

- **Gain :** le miroir fournit une base cohérente pour les deux côtés.

- **Revue :** les poses symétriques et asymétriques sont comparées.

## 44. Méthode de revue par articulation

Chaque articulation est testée dans plusieurs angles, avec affichage du maillage, des poids et du squelette. Une correction est évaluée sur les poses voisines pour éviter une amélioration locale qui dégrade ailleurs.

Le rapport conserve captures candidates et décision par région.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
joint_review:
  joint: elbow_L
  samples_deg: [0, 45, 90, 135]
  views: [front, side, perspective]
  overlays: [wireframe, weights, bones]
  neighboring_regions_checked: [forearm, upper_arm]
  decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Échantillons :** plusieurs angles révèlent la progression de la déformation.

- **Vues :** le volume est examiné au-delà de la silhouette.

- **Voisinage :** la correction ne doit pas déplacer le défaut vers un segment adjacent.

- **Preuve :** la décision reste traçable par articulation.

## 45. Poids des épaules

Les poids d’épaule répartissent clavicule, poitrine, bras et correctifs. La frontière ne suit pas une ligne circulaire uniforme autour de l’humérus.

La qualité est jugée en élévation, rotation et croisement avec la veste active.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
shoulder_weights:
  primary_groups: [DEF_clavicle_L, DEF_upper_arm_L, DEF_chest]
  corrective_group: DEF_shoulder_corrective_L
  radial_gradient_only: false
  poses: [raise_90, raise_140, cross_body]
  clothing_visible: true
  armpit_volume_gate: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Répartition :** plusieurs os partagent la peau et le vêtement.

- **Forme :** le gradient suit les volumes plutôt qu’un anneau régulier.

- **Correctif :** l’influence supplémentaire répond à une pose précise.

- **Porte :** l’aisselle doit conserver un volume et une lecture acceptables.

## 46. Poids des coudes et genoux

Les articulations charnières conservent plis internes, volume externe et glissement progressif des tissus. Des boucles topologiques adaptées restent indispensables.

Les poids sont comparés avec et sans `Preserve Volume` lorsque le profil le permet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hinge_joint_weights:
  joints: [elbow_L, knee_L]
  inner_fold: compressed_controlled
  outer_volume: preserved
  loop_density: chapter_17_dependency
  preserve_volume_comparison: required
  extreme_pose_intersection: reported
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pli :** la face interne accepte une compression contrôlée.

- **Volume :** la face externe ne doit pas s’effondrer.

- **Topologie :** le skinning ne remplace pas les boucles nécessaires.

- **Comparaison :** les options du modificateur sont évaluées sur le même échantillon.

## 47. Poids des poignets et chevilles

Poignets et chevilles combinent flexion et rotation ; les poids doivent éviter un étranglement net à la frontière du segment.

Les chaussures et gants rigides peuvent nécessiter des zones plus attachées qu’une peau nue.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
distal_joint_weights:
  wrist_groups: [DEF_forearm_L, DEF_hand_L, DEF_forearm_twist_02_L]
  ankle_groups: [DEF_shin_L, DEF_foot_L, DEF_shin_twist_L]
  hard_surface_clothing_mask: asset_specific
  twist_test: required
  flexion_test: required
  silhouette_gate: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transition :** plusieurs groupes créent une continuité plutôt qu’une coupure.

- **Costume :** la rigidité visuelle du vêtement influence la distribution.

- **Rotation :** le twist est évalué séparément de la flexion.

- **Porte :** le contour et le volume doivent rester cohérents.

## 48. Poids des hanches et du bassin

Le bassin distribue torse, cuisses et fessiers lors de flexion, abduction et torsion. Une dépendance excessive au pelvis rigidifie la jambe ; une dépendance excessive à la cuisse arrache le torse.

L’accroupissement profond constitue le test principal du pilote.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
hip_weights:
  groups: [DEF_pelvis, DEF_thigh_L, DEF_spine_01]
  gluteal_corrective: optional
  test_poses: [deep_squat, side_step, twist]
  garment_regions: [jacket_hem, trousers]
  pelvis_lock_assumption: forbidden
  approval: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Partage :** le volume traverse plusieurs zones anatomiques.

- **Mobilité :** les poses couvrent flexion, latéralité et torsion.

- **Vêtement :** les ourlets et pantalons sont inclus dans la revue.

- **Décision :** un correctif n’est ajouté qu’après observation du pilote.

## 49. Poids des mains et des doigts

Les doigts utilisent des gradients courts et précis, avec attention aux membranes, ongles et gants. Les sommets ne doivent pas recevoir l’influence d’un doigt voisin par simple proximité.

Une série de prises teste fermeture progressive, pince et poing.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
finger_weight_tests:
  gestures: [relaxed, fist, pinch, cylindrical_grip]
  neighbor_finger_leak: forbidden
  thumb_webbing_review: required
  glove_rigidity: asset_specific
  max_influences: profile_candidate
  grip_socket_alignment: checked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gestes :** plusieurs prises révèlent des défauts invisibles en main ouverte.

- **Isolation :** les doigts voisins ne tirent pas le même sommet sans justification.

- **Pouce :** la membrane exige une revue spécifique.

- **Socket :** la prise rigide reste alignée malgré la fermeture des doigts.

## 50. Correctifs par shape keys

Une shape key corrective peut restaurer un volume pour une combinaison de rotations difficile à obtenir par poids seuls. Elle possède une pose déclencheuse, un delta local et une règle d’export qualifiée.

Les drivers Blender ne sont pas supposés compatibles glTF ; la stratégie moteur doit être décidée avant production en série.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
corrective_shape:
  name: CORR_shoulder_raise_L
  trigger_pose: upper_arm_elevation_120
  sculpt_space: posed_mesh
  driver_in_blender: candidate
  gltf_export_support: must_be_qualified
  godot_runtime_strategy: explicit
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déclencheur :** la correction correspond à une combinaison de pose identifiable.

- **Delta :** seuls les sommets nécessaires sont modifiés.

- **Échange :** les drivers ne sont pas confondus avec une animation exportable garantie.

- **Stratégie :** la solution Godot est décidée avant généralisation.

## 51. Grille de poses de validation

Une grille standard compare tous les rigs d’une même famille. Elle inclut rest, locomotion extrême, amplitudes articulaires, torsion, prise et silhouettes asymétriques.

Les poses sont des tests techniques ; leur animation finale sera produite au chapitre 20.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
pose_grid:
  neutral: [rest, relaxed]
  torso: [bend_forward, bend_side, twist]
  arms: [overhead, cross_body, behind_back]
  legs: [deep_squat, high_step, kneel]
  hands: [fist, pinch, grip]
  accessories: [draw, stow, shoulder_carry]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Couverture :** la grille cible les défauts fréquents de chaque région.

- **Comparaison :** les mêmes poses servent aux versions successives.

- **Accessoires :** les sockets sont évalués avec objets témoins.

- **Frontière :** les poses ne constituent pas une bibliothèque d’animation livrée.

## 52. Poses extrêmes et limites d’acceptation

Les extrêmes ne cherchent pas une beauté parfaite hors contexte ; ils vérifient que le rig échoue de manière connue et que la plage utile reste exploitable.

Chaque défaut est classé bloquant, acceptable avec réserve ou hors plage contractuelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
extreme_pose_gate:
  pose: deep_squat
  intended_range: production
  volume_loss: measured_candidate
  self_intersection: classified
  socket_drift: checked
  severity: pending
  decision_owner: rig_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plage :** la pose indique si elle appartient réellement au contenu visé.

- **Mesures :** les pertes et dérives sont observées plutôt qu’imaginées.

- **Classement :** un défaut possède une sévérité et une décision.

- **Responsable :** la revue identifie l’autorité qui accepte la réserve.

## 53. Rapport de déformation

Le rapport relie version du maillage, version du rig, pose, angle, région, symptôme, capture, correction et décision. Les captures sans paramètres ne suffisent pas.

Une correction régressive rouvre les poses précédemment approuvées de la même région.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
deformation_issue:
  issue_id: RIG-DEF-0017
  rig_version: 1.0.0-candidate.3
  pose: overhead_reach_L
  region: shoulder_L
  symptom: armpit_collapse
  correction: weight_and_corrective_bone
  regression_scope: [cross_body, behind_back]
  status: open
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque défaut peut être suivi sans dépendre d’un commentaire oral.

- **Contexte :** version et pose rendent le problème reproductible.

- **Correction :** la stratégie choisie est visible et révisable.

- **Régression :** les poses liées sont automatiquement remises en revue.

## 54. Filtrage d’export

L’export inclut maillages skinnés, squelette de déformation, correctifs approuvés et sockets autorisés. Contrôleurs, mécanismes, formes personnalisées et objets de test restent dans la source Blender.

Le filtre utilise une collection canonique plutôt qu’une sélection manuelle fragile.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
export_filter:
  collection: __EXPORT_RIGGED
  include_roles: [MESH, DEF_BONE, CORRECTIVE_BONE, SOCKET]
  exclude_roles: [CONTROL, MECHANISM, CUSTOM_SHAPE, TEST_PROP]
  hidden_state_is_filter: false
  selection_is_filter: false
  manifest_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Collection :** le contenu livré est défini par une source stable.

- **Rôles :** les éléments autorisés et interdits sont explicites.

- **État visuel :** masquage et sélection ne décident pas de la livraison.

- **Manifeste :** le paquet décrit ce qui a réellement été exporté.

## 55. Contrat glTF et GLB

Le GLB constitue la livraison par défaut. Le profil conserve transforms, skin, hiérarchie, noms et animations de test seulement si elles sont explicitement autorisées.

Les contraintes et contrôleurs Blender sont évalués puis baked si une animation doit être exportée au chapitre 20 ; ils ne sont pas supposés transférés comme logique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
gltf_rigged_profile:
  container: GLB
  export_collection: __EXPORT_RIGGED
  skins: true
  deform_bones_only: true
  animations: false_for_chapter_19
  apply_modifiers: qualified
  extras: manifest_controlled
  source_sha256: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conteneur :** le GLB regroupe la livraison inspectable.

- **Skin :** le bind et le squelette sont inclus sans les outils de contrôle.

- **Animation :** le chapitre n’exporte pas de bibliothèque animée finale.

- **Traçabilité :** l’empreinte relie la sortie à sa source et son preset.

## 56. Scène Godot dérivée

L’import produit une scène dérivée contenant `Skeleton3D`, maillages skinnés et nœuds d’attache. La scène importée n’est pas modifiée directement ; une scène héritée ou enveloppe porte les ajouts du projet.

Le nom des nœuds peut varier selon l’import ; la validation recherche les types et contrats plutôt qu’un chemin supposé universel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
AST_RiggedScout.tscn
└── RiggedScoutRoot (Node3D)
    ├── ImportedModel (Node3D)
    │   ├── Skeleton3D
    │   └── ScoutBody (MeshInstance3D)
    ├── Attachments (Node3D)
    │   ├── GripRight (BoneAttachment3D)
    │   └── BackSocket (BoneAttachment3D)
    └── Validation (Node)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dérivation :** la ressource importée reste régénérable.

- **Skeleton :** la hiérarchie de repos est inspectée dans le moteur.

- **Attachments :** les dépendances de projet sont ajoutées hors de la source importée.

- **Robustesse :** les scripts utilisent types, noms d’os et manifeste.

## 57. Sémantique de Skeleton3D

Dans Godot, le rest définit le transform de référence et la pose décrit l’état appliqué. La pose dite globale reste relative au `Skeleton3D`, pas au monde entier.

Les noms d’os sont uniques et la hiérarchie doit conserver un parent précédent l’enfant.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
skeleton3d_checks:
  unique_bone_names: true
  forbidden_name_characters: [":", "/"]
  parent_index_before_child: true
  rest_transforms_finite: true
  rest_scale_uniform_candidate: true
  pose_reset_matches_rest: required
  world_space_assumption: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rest :** le bind et le retargeting utilisent un référentiel explicite.

- **Pose :** les transformations locales et relatives sont distinguées du monde.

- **Noms :** les caractères incompatibles sont bloqués avant publication.

- **Hiérarchie :** l’ordre parental est vérifié structurellement.

## 58. BoneMap, SkeletonProfile et retargeting

Le retargeting ne se limite pas à des noms similaires. Les os sont mappés vers un profil, les rests sont comparés et les options de translation, rotation et échelle sont qualifiées.

`SkeletonProfileHumanoid` convient au pilote humanoïde ; une créature nécessiterait un profil custom.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
retarget_profile:
  source_skeleton: HUMANOID-ASTERIA-V1
  godot_profile: SkeletonProfileHumanoid
  bone_map_resource: res://assets/rigs/profiles/asteria_humanoid_bonemap.tres
  rest_alignment_review: required
  translation_tracks: qualified
  rotation_tracks: qualified
  scale_tracks: discouraged
  unmapped_bones: reported
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** le squelette virtuel fournit une interface cible stable.

- **Map :** chaque os essentiel est associé explicitement.

- **Rest :** les orientations de repos sont comparées avant partage d’animation.

- **Rapport :** les os non mappés et tracks retirées restent visibles.

## 59. BoneAttachment3D et sockets moteur

`BoneAttachment3D` suit un os du `Skeleton3D` parent ou externe. Le mode de suivi est préféré pour les accessoires ; `override_pose` est réservé aux cas qualifiés car il peut interagir avec les modifiers du squelette.

Le nœud porte le contenu de projet sans renommer l’os source.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
bone_attachment:
  node: GripRight
  type: BoneAttachment3D
  bone_name: DEF_hand_R
  use_external_skeleton: false
  override_pose: false
  attached_scene: res://assets/props/grip_reference.tscn
  socket_contract: SOCKET_grip_R
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** le nom d’os correspond au contrat publié.

- **Suivi :** l’attache copie la transformation sans prendre le contrôle de la pose.

- **External :** un squelette externe n’est utilisé que si l’arborescence le requiert.

- **Contenu :** la scène attachée reste indépendante du fichier importé.

## 60. Validateur structurel Godot

Un script de validation vérifie présence du squelette, noms requis, parents, rests finis, maillage skinné et sockets. Il ne juge pas la beauté d’une déformation.

Le script renvoie des diagnostics déterministes et ne modifie jamais l’asset pendant le contrôle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```gdscript
@tool
extends Node

const REQUIRED_BONES := [&"DEF_root", &"DEF_pelvis", &"DEF_head"]

func validate_skeleton(skeleton: Skeleton3D) -> PackedStringArray:
    var errors := PackedStringArray()
    for bone_name in REQUIRED_BONES:
        if skeleton.find_bone(bone_name) < 0:
            errors.append("missing_bone:%s" % bone_name)
    for index in skeleton.get_bone_count():
        var parent := skeleton.get_bone_parent(index)
        if parent >= index:
            errors.append("invalid_parent_order:%d" % index)
    return errors
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le validateur reçoit un `Skeleton3D` déjà importé.

- **Noms :** les os minimaux sont vérifiés par `StringName`.

- **Parents :** l’ordre invalide devient un diagnostic lisible.

- **Limite :** aucune note esthétique n’est automatisée.

## 61. Mode Solo, Mode Studio et porte d’acceptation

En Solo, un rig humanoïde de référence et une grille de poses limitée précèdent toute généralisation. En Studio, les responsabilités rig, skin, animation, intégration et QA sont séparées par des critères de passage.

L’acceptation exige hiérarchie stable, rolls cohérents, poids revus, poses extrêmes classées, export filtré, import structurel valide, sockets alignés et provenance qualifiée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  hierarchy_reviewed: required
  roll_consistent: required
  influence_budget_respected: required
  pose_grid_reviewed: required
  export_manifest_complete: required
  godot_structure_valid: required
  retarget_profile_checked: required
  provenance_qualified: required
  runtime_deformation_benchmark: pending
  decision: pending_human_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Solo :** la portée reste concentrée sur un pilote reproductible.

- **Studio :** chaque passage possède propriétaire, entrée, sortie et décision.

- **Porte :** aucune qualité partielle ne compense un contrat structurel cassé.

- **Réserve :** les tests runtime restent nécessaires avant approbation de production.


## 62. Diagnostics et corrections

<!-- qa:error-correction-section -->

Les cas suivants utilisent la séquence symptôme, exemple fautif, explication directe, exemple corrigé et justification. Les valeurs restent pédagogiques et doivent être remplacées par les observations du pilote réel.

### 62.1 Utiliser les contrôleurs comme squelette exporté

**Symptôme ou risque :** Godot importe des os `CTRL_` et `MCH_` inutiles, tandis que les groupes de sommets ne correspondent plus au contrat.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
export:
  include_all_armature_bones: true
  deform_filter: disabled
  control_shapes: selected
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le paquet confond ergonomie Blender et interface de déformation, ce qui augmente les os et fragilise le retargeting.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
export:
  collection: __EXPORT_RIGGED
  include_roles: [DEF_BONE, CORRECTIVE_BONE, SOCKET]
  controls_and_mechanisms: excluded
  manifest_check: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction filtre les rôles publiés et rend la livraison vérifiable par manifeste.

### 62.2 Réparer un mauvais roll avec une contrainte

**Symptôme ou risque :** Le coude fonctionne dans une pose mais retourne lorsque la main change d’espace.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
bone: DEF_forearm_L
roll_review: skipped
constraint_offset_deg: 173
purpose: hide_axis_problem
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La contrainte masque une orientation locale incorrecte et propage une dépendance instable dans les autres modes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
bone: DEF_forearm_L
roll_basis: limb_chain_standard
mirror_axis_review: passed
constraints: functional_only
pose_grid: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction rétablit le référentiel de repos avant d’ajouter les contraintes fonctionnelles.

### 62.3 Changer la rest pose après le skinning

**Symptôme ou risque :** Les poids semblent corrects dans Blender mais le retargeting produit des épaules décalées.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
rest_pose:
  changed_after_bind: true
  rebind: false
  corrective_shapes_rebuilt: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le bind, les poids, les correctifs et les rests Godot ne partagent plus la même référence.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
rest_pose_change:
  new_skeleton_version: required
  rebind: required
  weights_review: required
  correctives_rebuilt: required
  retarget_profile_revalidated: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction traite la rest pose comme une interface versionnée et revalide toutes les dépendances.

### 62.4 Faire confiance aux poids automatiques

**Symptôme ou risque :** Le bras entraîne le torse et la sacoche lorsque la main se lève.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
bind:
  method: automatic_weights
  manual_review: skipped
  status: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La proximité géométrique a attribué des influences plausibles numériquement mais fausses fonctionnellement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
bind:
  method: automatic_weights
  mandatory_joint_review: true
  accessory_false_positive_scan: true
  pose_grid: required
  status: candidate
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise l’automatique comme initialisation puis exige une revue en mouvement.

### 62.5 Limiter les influences sans comparaison

**Symptôme ou risque :** Le compteur respecte quatre influences, mais l’épaule présente une cassure nouvelle.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
weights:
  limit_total: 4
  cleanup_before_limit: false
  normalize_after: false
  visual_review: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La troncature a supprimé des contributions utiles sans nettoyage ni renormalisation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
weights:
  cleanup_threshold: measured
  limit_total: platform_profile
  normalize_after: true
  before_after_pose_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction prépare les poids puis compare la déformation sur les mêmes poses.

### 62.6 Miroiter une région asymétrique

**Symptôme ou risque :** La sacoche droite déforme aussi le côté gauche après un miroir global.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
mirror_weights:
  all_vertices: true
  asymmetric_regions: ignored
  topology_check: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le miroir écrase des décisions locales et suppose une correspondance qui n’existe pas autour de l’accessoire.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
mirror_weights:
  symmetric_base_only: true
  excluded_regions: [pouch_contact, jacket_fold_R]
  topology_correspondence: verified
  bilateral_review: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction profite de la symétrie sans détruire les régions volontairement différentes.

### 62.7 Utiliser un socket comme autorité gameplay

**Symptôme ou risque :** L’objet est considéré équipé uniquement parce qu’un `BoneAttachment3D` existe.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func is_equipped() -> bool:
    return $GripRight.get_child_count() > 0
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La présence visuelle d’un enfant de socket n’est ni une décision d’inventaire ni une preuve d’autorité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func update_visual_attachment(item_scene: PackedScene) -> void:
    # L’état équipé provient du système gameplay autoritaire.
    _replace_socket_visual(item_scene)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite le rig à la représentation et reçoit l’état décidé ailleurs.

### 62.8 Supposer que les noms suffisent au retargeting

**Symptôme ou risque :** Une animation partagée tord les bras malgré des noms d’os identiques.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
retargeting:
  bone_names_match: true
  rest_alignment_review: false
  bone_map: omitted
  status: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les orientations et rests diffèrent ; la correspondance textuelle ne garantit pas une transformation compatible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
retargeting:
  bone_map: required
  skeleton_profile: SkeletonProfileHumanoid
  rest_alignment_review: required
  unmapped_bones_reported: true
  status: candidate
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction valide profil, mapping et rest avant de partager des animations.

### 62.9 Activer override_pose sur une attache ordinaire

**Symptôme ou risque :** Le socket entre en conflit avec un modifier de squelette et produit des sauts.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
bone_attachment:
  bone_name: DEF_hand_R
  override_pose: true
  purpose: attach_prop
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une simple représentation d’accessoire prend inutilement le contrôle de la pose de l’os.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
bone_attachment:
  bone_name: DEF_hand_R
  override_pose: false
  purpose: follow_prop_socket
  modifier_interaction_review: not_needed
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise le mode de suivi correspondant au besoin réel.

### 62.10 Valider uniquement la pose neutre

**Symptôme ou risque :** Le personnage paraît correct au repos mais l’aisselle s’effondre en portée haute.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
rig_review:
  poses: [rest]
  clothing_visible: false
  extreme_angles: skipped
  decision: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La pose neutre n’exerce ni les articulations, ni les correctifs, ni les contacts du vêtement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
rig_review:
  pose_grid: required
  clothing_visible: true
  extreme_angles: classified
  sockets_checked: true
  decision: pending_human_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction évalue le rig dans les situations qui révèlent réellement ses défauts.


## 63. Checklist de livraison

La livraison documentaire est prête lorsque le lecteur peut identifier la source canonique, la version du squelette, les rôles d’os, le profil de skinning, la grille de poses, le filtre d’export, le profil de retargeting, les sockets, les réserves et l’autorité de décision. Les fichiers et mesures de production restent à créer dans les outils réels.

- [ ] squelette de déformation matérialisé et revu ;
- [ ] rig de contrôle opérationnel dans Blender ;
- [ ] roll, axes et hiérarchie approuvés ;
- [ ] poids normalisés et budget d’influences mesuré ;
- [ ] correctifs justifiés par des poses ;
- [ ] sockets vérifiés avec accessoires témoins ;
- [ ] export GLB et manifeste produits ;
- [ ] import Godot et `Skeleton3D` inspectés ;
- [ ] `BoneMap` et profil de retargeting testés ;
- [ ] rapport de déformation fermé par revue humaine.

## 64. Références techniques primaires

Les procédures s’appuient sur les manuels officiels Blender relatifs aux armatures, au bone roll, aux contraintes et au weight paint, ainsi que sur la documentation stable Godot de `Skeleton3D`, `BoneAttachment3D`, `SkeletonProfile`, `RetargetModifier3D` et de l’import de scènes 3D. Toute différence observée dans Blender `5.2.0` ou Godot `4.7.1-stable` doit être enregistrée dans le rapport de qualification avant de modifier le contrat.

## 65. Conclusion

Un rig publiable n’est pas le plus complexe : c’est celui dont la hiérarchie, les rests, les axes, les poids, les correctifs, les sockets et l’export sont compris et testables. Le chapitre établit cette interface sans revendiquer sa matérialisation. Les animations, courbes, cycles, événements et blend trees seront construits au chapitre 20 sur ce socle versionné.
