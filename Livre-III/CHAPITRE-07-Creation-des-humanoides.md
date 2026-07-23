---
title: "Livre III — Chapitre 7 : Création des humanoïdes"
id: "DOC-L3-CH07"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 7
last-verified: "2026-07-23T01:49:34+02:00"
audit-status: "complete"
audit-date: "2026-07-23T01:49:34+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-07.md"
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
# Création des humanoïdes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH07`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11
## 1. Rôle du chapitre

Le chapitre 6 a défini une base humaine de production : proportions, topologie de déformation, modules, matériaux préparatoires, budgets LOD et scène de validation. Le présent chapitre apprend à dériver de cette base des **espèces humanoïdes distinctes** sans traiter chaque différence visuelle comme une simple décoration ni sacrifier la crédibilité du mouvement, du rig, des interactions ou des équipements.

Un humanoïde conserve une organisation corporelle suffisamment proche du contrat bipède de référence pour partager une partie des outils, animations ou équipements. Cette proximité n’implique jamais une compatibilité automatique. Une espèce peut posséder deux bras et deux jambes tout en nécessitant un bassin, des pieds, une colonne, une tête, des mains, des sockets ou une locomotion incompatibles avec la base humaine.

Le livrable attendu n’est pas une collection illimitée d’aliens. Il s’agit d’un **système d’adaptation versionné** qui explique, pour chaque espèce pilote, ce qui reste commun, ce qui varie, ce qui exige un profil spécialisé et ce qui doit être refusé.
> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Base humaine validée
    ↓
Fiche d'espèce et fonction dans le monde
    ↓
Registre des écarts anatomiques
    ↓
Silhouette primaire et proportions fonctionnelles
    ↓
Topologie, modules et interfaces adaptés
    ↓
Profil de rig et BoneMap qualifiés
    ↓
Matrice vêtements, armures, sockets et interactions
    ↓
Variations culturelles gouvernées
    ↓
LOD préservant les traits distinctifs
    ↓
Export GLB et scènes Godot de test
    ↓
Décision : compatible, compatible sous conditions ou incompatible
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** la chaîne impose une justification fonctionnelle avant tout ajout de corne, membre, posture ou module.
- **Déroulement :** chaque adaptation est comparée à la base humaine, puis propagée vers le rig, les équipements, le LOD et les tests.
- **Invariant :** un trait distinctif ne devient jamais compatible par défaut parce que la silhouette reste globalement bipède.
- **Résultat attendu :** une personne peut identifier les exceptions d’une espèce sans ouvrir tous ses fichiers Blender ou Godot.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- distinguer humanoïde, humain stylisé, animal anthropomorphe et créature non humanoïde ;
- rédiger une fiche d’espèce liée à la direction artistique et au gameplay prévu sans créer le système de gameplay ;
- comparer une anatomie au contrat humain par écarts explicites ;
- adapter proportions, colonne, ceintures, membres, extrémités, tête, posture et centre de masse ;
- préserver une locomotion crédible et des interactions réalisables ;
- définir les traits qui peuvent rester des modules et ceux qui imposent une nouvelle base ;
- versionner un profil de rig et déclarer la compatibilité de retargeting ;
- construire ou qualifier un `BoneMap` Godot sans confondre noms d’os et poses de repos ;
- gérer vêtements, armures, sockets et masques corporels par matrice de compatibilité ;
- créer des variations culturelles sans réduire une espèce à un stéréotype unique ;
- définir des LOD qui conservent la lecture de l’espèce ;
- préparer des scènes Godot de silhouette, équipement, mouvement et coût ;
- appliquer un parcours Solo réduit ou un parcours Studio gouverné ;
- diagnostiquer les incompatibilités sans les cacher par des corrections destructives.
## 3. Niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Les procédures Blender, les contrats de profils, les règles d’import Godot, le retargeting et les scripts proposés ont été relus contre les documentations officielles citées à la fin du chapitre.

Aucune espèce humanoïde réelle de `Project Asteria`, aucun fichier `.blend`, aucun rig, aucun `BoneMap`, aucune animation, aucun vêtement, aucun export GLB et aucune scène Godot ne sont revendiqués comme matérialisés. Les nombres de triangles, distances de LOD, amplitudes articulaires et plafonds de compatibilité sont des **hypothèses de production** à remplacer ou confirmer par des mesures.

Le chapitre n’établit aucune vérité biologique, médicale, ethnique ou anthropologique. Les espèces fictives sont conçues pour un univers de jeu ; les variations culturelles décrivent des pratiques, objets, environnements et histoires internes au monde, jamais des équivalences simplistes avec des populations réelles.
## 4. Périmètre et frontières

Le chapitre définit :

- les critères qui permettent de rester dans une famille humanoïde ;
- la fiche d’espèce et le registre des écarts ;
- l’adaptation fonctionnelle de l’anatomie ;
- les silhouettes et proportions distinctives ;
- les modules propres à l’espèce ;
- les profils de rig, de retargeting et de skinning ;
- les matrices de compatibilité des équipements ;
- les sockets et interactions ;
- les variations culturelles gouvernées ;
- les profils LOD et scènes de test ;
- les parcours Solo et Studio.

Il ne définit pas :

- les humains de base du chapitre 6 ;
- les animaux du chapitre 8 ;
- les créatures réellement non humanoïdes du chapitre 9 ;
- le lookdev détaillé des visages, peaux, yeux, cheveux et pilosités du chapitre 10 ;
- la fabrication complète des vêtements et armures du chapitre 11 ;
- le rig final et le skinning de production du chapitre 19 ;
- les bibliothèques d’animations et le retargeting de production du chapitre 20 ;
- les comportements, statistiques, capacités ou interactions métier du Livre II ;
- les cultures comme systèmes politiques, sociaux ou narratifs complets.

> **Frontière essentielle :** le chapitre qualifie la **forme visuelle et ses contrats d’intégration**. Il n’attribue pas automatiquement capacités, personnalité, intelligence, moralité, faction ou rôle narratif à une anatomie.
## 5. Prérequis

Le lecteur doit connaître :

- la bible visuelle et les règles de silhouette du chapitre 2 ;
- la provenance des références et concepts des chapitres 3 et 5 ;
- les unités, axes, collections, versions et exports du chapitre 4 ;
- la base humaine, ses modules et ses budgets du chapitre 6 ;
- les modes Objet, Édition, Sculpture, Pose et Peinture de poids de Blender ;
- l’import de scènes 3D et l’inspecteur avancé de Godot ;
- les notions de hiérarchie d’os, pose de repos, skinning et LOD.

Le projet doit déjà disposer :

- d’une base humaine de référence identifiée ;
- d’une convention de noms d’os et de modules ;
- d’une collection d’export ;
- d’un registre de provenance ;
- d’une politique de versions ;
- d’un espace de test Godot distinct des scènes de jeu.
## 6. Vocabulaire opérationnel

### 6.1 Humanoïde

Espèce fictive dont l’organisation générale permet de réutiliser une partie du contrat bipède humain : axe du tronc, tête, membres principaux, posture et interactions. La définition est technique et liée au projet, pas universelle.

### 6.2 Trait distinctif

Caractéristique nécessaire à l’identification de l’espèce : silhouette crânienne, longueur des membres, posture, oreilles, cornes, queue, nombre de doigts, forme des pieds, membrane ou autre volume. Un détail décoratif n’est distinctif que s’il reste lisible dans les conditions de jeu prévues.

### 6.3 Écart anatomique

Différence mesurable par rapport à la base humaine : proportion, articulation, orientation, nombre de segments, amplitude, centre de masse, contact au sol ou interface de module.

### 6.4 Profil d’espèce

Document versionné qui regroupe les écarts, modules, rig, compatibilités, budgets, LOD, tests et propriétaires de décision.

### 6.5 Compatibilité complète

Le même rig, les mêmes poses de repos, les mêmes noms d’os, les mêmes interfaces et les mêmes équipements fonctionnent dans les limites validées, sans correctif spécifique.

### 6.6 Compatibilité conditionnelle

La réutilisation est possible après une adaptation déclarée : BoneMap, masque de corps, correctif de pose, variante de vêtement, socket spécialisé ou exclusion d’animation.

### 6.7 Incompatibilité

Le contrat commun ne peut pas produire un résultat acceptable sans reconstruire une partie significative de l’asset. L’incompatibilité est une information utile, pas un échec à dissimuler.

### 6.8 Retargeting partiel

Transfert limité à un sous-ensemble d’os ou de mouvements. Les parties non mappées utilisent une animation propre, restent statiques ou reçoivent un traitement spécialisé.

### 6.9 Socket

Point de fixation ou repère d’interaction versionné : main, dos, tête, bouche, hanche, selle, arme, accessoire ou effet. Son nom seul ne garantit pas son orientation ni son volume libre.

### 6.10 Silhouette culturelle

Variation d’habillement, d’outil, de posture sociale ou de construction matérielle issue d’un contexte interne au monde. Elle ne remplace pas l’identité anatomique de l’espèce.
## 7. Définir la fonction de l’espèce avant sa forme

Une espèce humanoïde est conçue à partir de contraintes observables :

- environnements fréquentés ;
- modes de déplacement réellement prévus ;
- interactions avec portes, sièges, armes, outils et véhicules ;
- distances habituelles à la caméra ;
- importance des gros plans ;
- fréquence à l’écran ;
- nombre de variantes ;
- besoins de retargeting ;
- vêtements et armures attendus ;
- plateformes cibles.

La fonction n’impose pas une apparence unique. Elle élimine toutefois les décisions contradictoires. Une espèce censée utiliser les mêmes ateliers que les humains doit pouvoir atteindre les commandes, franchir les passages et tenir les outils, ou documenter les adaptations du monde.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMANOID-SPECIES-BRIEF.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
display_name: "Vélari"
profile_version: v001
design_status: "concept_review"
world_function:
  habitats:
    - "canopée tempérée"
    - "cités verticales"
  locomotion:
    primary: "biped_walk"
    secondary:
      - "short_climb"
  shared_interactions:
    - "human_scale_doors"
    - "standard_tools"
    - "one_handed_weapons"
camera:
  expected_distance_m:
    near: 1.0
    gameplay: 6.0
    crowd: 24.0
production:
  expected_variants: 6
  animation_reuse_target: "conditional"
  equipment_reuse_target: "conditional"
provenance_status: "under_review"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `world_function` et `shared_interactions` transforment l’intention visuelle en contraintes vérifiables.
- **Décision :** `conditional` autorise la réutilisation seulement lorsque les adaptations nécessaires sont enregistrées.
- **Limite :** le profil ne définit ni statistiques, ni capacités, ni comportement de gameplay.
- **Résultat attendu :** l’équipe peut refuser une forme séduisante qui contredit les interactions ou les distances de lecture prévues.

## 8. Construire le registre des écarts anatomiques

Le registre compare chaque zone à la base humaine. Il ne se limite pas à « plus long » ou « différent ». Il indique :

- la mesure ou relation concernée ;
- la cause visuelle ou fonctionnelle ;
- les systèmes affectés ;
- le niveau de compatibilité ;
- les tests requis ;
- la décision de repli.

Une différence locale peut avoir des conséquences globales. Des avant-bras plus longs déplacent la portée des mains, les coudes sur les manches, la longueur des armes, les poses d’interaction et la composition de l’écran. Une tête plus large affecte les cols, casques, caméras rapprochées et volumes de collision visuels.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMANOID-DEVIATION-LEDGER.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
human_base_id: AST-ASSET-MESH-HUMANBASE-001
human_base_version: v001
deviations:
  - deviation_id: DEV-001
    region: "forearm"
    measurement: "length_ratio_to_upper_arm"
    human_reference: 0.82
    species_target: 1.08
    tolerance: 0.03
    affects:
      - "sleeves"
      - "weapon_reach"
      - "elbow_pose"
      - "retargeting"
    compatibility: "conditional"
    required_tests:
      - "reach_panel"
      - "sleeve_bend"
  - deviation_id: DEV-002
    region: "foot"
    measurement: "contact_pattern"
    human_reference: "plantigrade"
    species_target: "semi_digitigrade"
    affects:
      - "leg_rig"
      - "boots"
      - "ground_contact"
      - "locomotion"
    compatibility: "incompatible_with_human_boots"
    required_tests:
      - "idle_contact"
      - "walk_contact"
unresolved: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** `human_base_id` et sa version fixent le contrat exact utilisé pour la comparaison.
- **Propagation :** `affects` rend visibles les systèmes à revalider au lieu de garder la différence dans le seul maillage.
- **Statuts :** `conditional` et `incompatible_with_human_boots` sont plus précis qu’un booléen compatible ou non.
- **Résultat attendu :** chaque écart possède une conséquence, un test et une décision exploitable.

## 9. Classer les écarts par impact

Le projet utilise quatre classes :

| Classe | Signification | Exemple | Décision habituelle |
|---|---|---|---|
| A | surface ou détail sans changement de contrat | motif cutané, petite crête | même base et même rig |
| B | volume modulaire compatible | oreilles longues, petites cornes | module spécialisé |
| C | proportion ou articulation modifiée | avant-bras longs, pieds semi-digitigrades | profil de rig et équipements dédiés |
| D | organisation corporelle différente | quatre bras, jambes inversées, absence de bassin comparable | nouvelle base ; vérifier frontière avec chapitre 9 |

Une accumulation de classes B et C peut justifier une nouvelle base, même si chaque différence semble gérable isolément. La décision dépend du coût total de correctifs, pas seulement du nombre de changements.
## 10. Adapter proportions, posture et centre de masse

Les proportions doivent être contrôlées dans plusieurs états :

- pose de construction ;
- repos naturel ;
- marche ;
- course ou déplacement secondaire ;
- interaction à hauteur humaine ;
- position assise ;
- port d’un équipement ;
- silhouette à distance.

La posture de repos ne doit pas compenser une anatomie incohérente. Déplacer constamment le bassin vers l’avant pour empêcher une espèce de tomber révèle souvent un centre de masse ou une géométrie des pieds non résolus.

Le centre de masse visuel ne constitue pas une simulation biomécanique exacte. Il fournit un contrôle de plausibilité : la projection du tronc et des masses principales doit rester compatible avec les appuis dans les poses prévues.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMANOID-ANATOMY-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
reference_height_m: 1.86
construction_pose: "asteria_humanoid_relaxed_a_v001"
body_axis:
  default_lean_degrees: 4.0
  head_forward_offset_m: 0.03
proportions:
  head_to_height: 0.125
  arm_span_to_height: 1.09
  pelvis_width_to_height: 0.145
  forearm_to_upper_arm: 1.08
supports:
  stance: "semi_digitigrade"
  contact_points:
    - "left_forefoot"
    - "right_forefoot"
  heel_visual_clearance_m: 0.08
motion_constraints:
  shoulder_abduction_degrees: 155
  elbow_flexion_degrees: 145
  hip_flexion_degrees: 115
  knee_flexion_degrees: 150
values_status: "provisional_until_pose_tests"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Unités :** les distances utilisent des mètres et les amplitudes des degrés pour éviter les conversions implicites.
- **Précondition :** la pose de construction nommée doit être identique pour le maillage, le rig et les exports comparés.
- **Réserve :** `provisional_until_pose_tests` interdit de présenter ces amplitudes comme mesurées.
- **Résultat attendu :** les proportions et amplitudes peuvent être comparées entre versions et espèces.

## 11. Colonne, ceintures et tête

### 11.1 Colonne et thorax

Une colonne plus longue ou plus flexible modifie :

- le nombre d’os nécessaires ;
- la distribution de la torsion ;
- les vêtements du torse ;
- la hauteur des sockets ;
- la distance entre bassin et épaules ;
- le retargeting des animations de respiration, esquive et locomotion.

Ajouter des vertèbres au rig ne suffit pas. La topologie et la distribution des poids doivent permettre leur action, et les animations partagées doivent définir ce que deviennent les segments supplémentaires.

### 11.2 Ceinture scapulaire

Des épaules hautes, étroites, mobiles ou déportées affectent l’omoplate, la clavicule, la rotation du bras et les emmanchures. Les bras ne doivent pas être déplacés par translation simple depuis la base humaine lorsque la ceinture change.

### 11.3 Bassin

Le bassin détermine l’orientation des jambes, la largeur des vêtements, la pose assise et le transfert de poids. Une espèce avec bassin étroit et fémurs très écartés exige une solution de topologie et de rig propre.

### 11.4 Tête et cou

Une tête allongée, lourde, inclinée ou dotée de volumes arrière change le cou, les cols, les casques et les caméras. Le cou doit soutenir la silhouette dans les poses rapides sans intersections avec les épaules.
## 12. Membres, mains, pieds et segments supplémentaires

### 12.1 Bras et jambes

Pour chaque membre, documenter :

- nombre de segments ;
- orientation des articulations ;
- amplitude ;
- torsion ;
- volume de compression ;
- fonction des extrémités ;
- compatibilité avec les outils et contacts.

### 12.2 Mains

Le nombre de doigts peut varier sans empêcher toute interaction, mais il modifie :

- groupes de sommets ;
- profil de main ;
- gants ;
- poignées ;
- poses de préhension ;
- animations fines ;
- profil `SkeletonProfileHumanoid` si les doigts ne peuvent pas être mappés correctement.

Une main à trois doigts ne doit pas recevoir cinq chaînes humaines invisibles uniquement pour « passer » un validateur. Les os non représentés doivent être exclus ou gérés par un profil spécialisé.

### 12.3 Pieds

Plantigrade, semi-digitigrade et digitigrade ne partagent pas automatiquement :

- la hauteur de cheville ;
- la pose de repos ;
- le contact au sol ;
- les chaussures ;
- le déroulé du pas ;
- la longueur apparente de la jambe.

### 12.4 Queue, oreilles, cornes et membranes

Ces traits sont classés comme :

- module statique ;
- module déformable ;
- chaîne secondaire animée ;
- volume soumis aux collisions ;
- détail à retirer dans certains LOD.

Ils restent hors du retargeting humain principal sauf décision explicite.
## 13. Préserver une silhouette immédiatement reconnaissable

La lecture de l’espèce est évaluée à trois niveaux :

1. **silhouette primaire** : hauteur, largeur, rapport tronc-membres, posture et masse principale ;
2. **silhouette secondaire** : tête, pieds, mains, queue, cornes, oreilles et volumes latéraux ;
3. **détails tertiaires** : motifs, plis, pores, petites écailles ou ornements.

Une espèce ne doit pas dépendre exclusivement des détails tertiaires. Lorsque les textures ou petites excroissances disparaissent, sa silhouette primaire et au moins un trait secondaire doivent rester distinctifs.
> **[VSC] Visual Studio Code — Créer : `art/blender/tests/HUMANOID-SILHOUETTE-TEST.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
backgrounds:
  - "neutral_light"
  - "neutral_dark"
  - "gameplay_forest"
distances_m:
  - 2
  - 8
  - 20
views:
  - "front"
  - "side"
  - "three_quarter"
  - "back"
required_traits:
  primary:
    - "long_forearms"
    - "narrow_torso"
    - "forward_balanced_stance"
  secondary:
    - "swept_ears"
    - "semi_digitigrade_feet"
acceptance:
  minimum_primary_visible: 2
  minimum_secondary_visible_at_8m: 1
  reviewer_count: 2
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variables :** `distances_m`, `views` et `backgrounds` empêchent une validation limitée à une belle vue de studio.
- **Seuil :** l’acceptation exige plusieurs traits, pas une reconnaissance subjective non documentée.
- **Limite :** ce test évalue la lecture visuelle ; il ne valide ni anatomie, ni animation, ni performance.
- **Résultat attendu :** les réductions de détail peuvent être comparées sans perdre l’identité de l’espèce.

## 14. Adapter la topologie sans recopier mécaniquement la base humaine

La topologie commune est conservée lorsque les mêmes zones se déforment de manière comparable. Elle est modifiée lorsque :

- une articulation change d’emplacement ou d’orientation ;
- un volume se comprime différemment ;
- un segment supplémentaire apparaît ;
- une interface modulaire change ;
- une silhouette exige une répartition différente des arêtes ;
- un trait distinctif doit survivre aux LOD.

Étirer les sommets d’une base humaine conserve les boucles, mais pas nécessairement leur fonction. Un coude déplacé sans redistribution place les boucles de compression au mauvais endroit. Un pied digitigrade dérivé par simple rotation de la cheville concentre les arêtes dans une zone qui n’est plus l’articulation principale.

Les quads restent utiles pour la lisibilité et les subdivisions, mais la priorité est la déformation et l’export. Les triangles contrôlés sont acceptables lorsqu’ils ne créent ni pincement, ni changement de silhouette, ni instabilité entre LOD.
## 15. Choisir entre variante, module et nouvelle base

### 15.1 Variante de la base

Choisir une variante lorsque :

- les articulations principales restent au même endroit relatif ;
- le rig commun suffit ;
- les vêtements principaux restent ajustables ;
- les différences peuvent être portées par proportions, sculpture ou shape keys contrôlées.

### 15.2 Module

Choisir un module lorsque :

- la frontière peut être versionnée ;
- le trait se remplace sans modifier le tronc ;
- les normales, UV, matériaux et poids sont compatibles ;
- les collisions et sockets restent maîtrisés.

### 15.3 Nouvelle base

Créer une nouvelle base lorsque :

- plusieurs articulations changent ;
- le contact au sol est différent ;
- le nombre de membres principaux change ;
- les équipements communs exigent trop de correctifs ;
- la topologie humaine devient un obstacle ;
- la majorité des animations doivent être spécialisées.

Le coût d’une nouvelle base peut être inférieur au coût permanent d’exceptions fragiles.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMANOID-MODULE-CONTRACT.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
module_id: AST-MODULE-VELARI-HEAD-001
species_id: AST-SPECIES-VELARI-001
module_type: "head"
version: v001
interface:
  boundary_id: AST-IFACE-NECK-RING-002
  vertex_count: 64
  vertex_order_hash: "sha256:TO_BE_MEASURED"
  normal_policy: "matched_custom_normals"
  uv_policy: "species_head_udim"
  scale: 1.0
rig:
  required_bones:
    - "Neck"
    - "Head"
  optional_bones:
    - "Ear.L"
    - "Ear.R"
materials:
  slots:
    - "MAT_Skin"
    - "MAT_Eye"
compatibility:
  human_body_v001: "incompatible_boundary"
  velari_body_v001: "compatible"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interface :** `boundary_id`, le nombre de sommets et l’empreinte d’ordre forment le contrat géométrique.
- **Dépendances :** les os et slots de matériaux requis empêchent un module visuellement correct mais techniquement incomplet.
- **Compatibilité :** l’incompatibilité avec la base humaine reste explicite au lieu d’être corrigée par soudure improvisée.
- **Résultat attendu :** un module peut être remplacé ou refusé avant l’export sans inspecter manuellement chaque sommet.

## 16. Construire un profil de rig d’espèce

Le profil de rig distingue :

- **os communs** : mappables vers le profil humanoïde ;
- **os renommés** : même fonction, nom différent ;
- **os supplémentaires** : oreilles, queue, segments de colonne, doigts ou appendices ;
- **os absents** : fonctions humaines non représentées ;
- **os de contrôle Blender** : exclus de l’export ;
- **os de déformation** : exportés avec poids ;
- **os de socket** : exportés ou recréés selon la politique.

La hiérarchie, les poses de repos et les axes importent autant que les noms. Deux squelettes portant `Hips`, `Spine` et `Head` peuvent produire un mauvais retargeting si leurs orientations ou longueurs diffèrent fortement.
> **[VSC] Visual Studio Code — Créer : `art/blender/rigs/profiles/VELARI-RIG-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
profile_id: AST-RIGPROFILE-VELARI-001
species_id: AST-SPECIES-VELARI-001
version: v001
reference_pose: "asteria_humanoid_relaxed_a_v001"
export_armature: "ARM_Velari_Deform"
root_bone: "Root"
scale_base_bone: "Hips"
common_bones:
  - "Root"
  - "Hips"
  - "Spine"
  - "Chest"
  - "Neck"
  - "Head"
  - "UpperArm.L"
  - "LowerArm.L"
  - "Hand.L"
  - "UpperLeg.L"
  - "LowerLeg.L"
renamed_bones:
  UpperChest: "ThoraxHigh"
extra_bones:
  - name: "EarBase.L"
    policy: "species_animation"
  - name: "EarTip.L"
    policy: "species_animation"
absent_profile_bones:
  - "LeftLittleDistal"
  - "RightLittleDistal"
control_bones_exported: false
deform_influences:
  default: 4
  exception_limit: 8
  exception_requires_measurement: true
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** `export_armature` distingue le squelette livré des contrôleurs et mécanismes Blender.
- **Mapping :** `renamed_bones`, `extra_bones` et `absent_profile_bones` documentent les trois formes principales d’écart.
- **Influences :** quatre influences constituent le profil compatible ; toute extension à huit exige un test du renderer cible.
- **Résultat attendu :** le profil peut piloter l’audit d’export, la création du BoneMap et la matrice d’animations.

## 17. Comprendre `SkeletonProfileHumanoid` et `BoneMap`

Godot fournit `SkeletonProfileHumanoid`, un profil humanoïde standardisé comportant 56 os répartis en groupes. Le profil ne transforme pas automatiquement n’importe quel squelette en humain compatible.

Le `BoneMap` associe les os importés aux noms du profil. Pour partager correctement des animations, il faut aussi traiter :

- les poses de repos ;
- l’orientation des os ;
- le sens des axes ;
- le parentage ;
- l’échelle ;
- la hauteur de référence ;
- les pistes d’animation à conserver ou supprimer.

Le profil humanoïde sert lorsque l’espèce reste suffisamment proche. Une espèce qui ne peut pas représenter proprement les os requis utilise un profil personnalisé ou un retargeting partiel.
> **[LECTURE] Exemple de table de qualification d’un BoneMap — Ne pas saisir.**

```text
Profil Godot              Os importé Vélari       Statut
Root                      Root                    exact
Hips                      Hips                    exact
Spine                     Spine                   exact
Chest                     Chest                   exact
UpperChest                ThoraxHigh              renamed
Neck                      Neck                    exact
Head                      Head                    exact
LeftUpperArm              UpperArm.L              mapped
LeftLowerArm              LowerArm.L              mapped
LeftHand                  Hand.L                  mapped
LeftLittleDistal          —                       absent
RightLittleDistal         —                       absent
EarBase.L                 — hors profil           species_only
EarTip.L                  — hors profil           species_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lecture :** la table sépare les correspondances exactes, renommées, absentes et propres à l’espèce.
- **Précondition :** chaque correspondance doit être contrôlée dans la pose de repos et pas uniquement par son libellé.
- **Frontière :** les os `species_only` ne sont pas ajoutés artificiellement au profil humanoïde.
- **Résultat attendu :** les animations partagées et spécialisées peuvent être attribuées sans ambiguïté.

## 18. Qualifier le retargeting local et global

`RetargetModifier3D` peut transférer position, rotation et échelle entre squelettes selon un profil. Deux stratégies doivent être distinguées :

- **pose locale** : tolère mieux certaines différences de forme et peut ignorer l’effet de parents absents ;
- **pose globale** : prend en compte la chaîne globale, mais exige des longueurs d’os compatibles sous peine d’expansion ou de compression visibles.

Le projet ne choisit pas globalement un mode pour toutes les espèces. Il qualifie chaque famille d’animations :

- locomotion ;
- interactions ;
- combat ;
- expressions corporelles ;
- poses assises ;
- animations de foule ;
- cinématiques.

Une animation peut être compatible pour le torse et incompatible pour les pieds. Le résultat devient alors un retargeting partiel avec couches spécialisées.
> **[VSC] Visual Studio Code — Créer : `art/blender/rigs/profiles/VELARI-RETARGET-POLICY.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
profile_id: AST-RETARGET-VELARI-001
source_profile: AST-RIGPROFILE-HUMAN-001
target_profile: AST-RIGPROFILE-VELARI-001
families:
  locomotion_walk:
    mode: "local_pose"
    shared_bones:
      - "Root"
      - "Hips"
      - "Spine"
      - "Chest"
      - "UpperArm"
      - "LowerArm"
    excluded_bones:
      - "Foot"
      - "Toes"
      - "EarBase"
      - "EarTip"
    correction_layer: "velari_walk_contact_v001"
    status: "conditional"
  seated_human_chair:
    mode: "none"
    reason: "pelvis_and_leg_contact_not_qualified"
    status: "blocked"
  upper_body_gesture:
    mode: "local_pose"
    correction_layer: null
    status: "candidate"
validation:
  rest_pose_match: "pending"
  foot_contact: "pending"
  hand_contact: "pending"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Granularité :** la politique qualifie des familles d’animations au lieu de déclarer l’espèce entière compatible.
- **Exclusions :** les pieds et oreilles reçoivent des couches propres lorsque le profil humain ne décrit pas leur mouvement.
- **Échec fermé :** `blocked` empêche l’usage d’une animation assise non qualifiée.
- **Résultat attendu :** le pipeline sait quelles pistes partager, corriger, spécialiser ou refuser.

## 19. Préparer les poids et influences

Blender associe les déformations aux groupes de sommets et aux os de déformation. Les poids automatiques constituent un point de départ, jamais une preuve de qualité.

Pour chaque espèce :

- contrôler les compressions et étirements aux articulations ;
- normaliser les poids ;
- supprimer les influences résiduelles ;
- vérifier la symétrie seulement lorsque l’anatomie est réellement symétrique ;
- limiter les influences selon le profil d’import ;
- conserver les os de contrôle hors des groupes exportés ;
- tester les modules avec le même squelette.

Godot propose un import à quatre influences, compatible avec tous les renderers, et un mode utilisant toutes les influences disponibles jusqu’à huit, potentiellement moins compatible. `Project Asteria` retient quatre influences par défaut et n’autorise huit influences qu’après mesure et justification.
## 20. Concevoir la compatibilité des vêtements et armures

La compatibilité n’est pas déduite d’un nom de taille. Elle dépend :

- du volume corporel ;
- des articulations ;
- de la longueur des segments ;
- des ouvertures ;
- des volumes distinctifs ;
- des masques de corps ;
- du skinning ;
- du LOD ;
- des matériaux ;
- des sockets.

Quatre résultats sont utilisés :

- `compatible` ;
- `compatible_with_variant` ;
- `compatible_with_mask`;
- `incompatible`.

Une armure humaine peut être compatible avec le torse d’une espèce, mais exiger des manches, gants, bottes et casque propres.
> **[VSC] Visual Studio Code — Créer : `art/blender/equipment/HUMANOID-EQUIPMENT-COMPATIBILITY.csv` — Ne pas saisir.**

```csv
species_id,equipment_id,region,status,required_variant,body_mask,test_set,owner
AST-SPECIES-VELARI-001,AST-EQUIP-TUNIC-001,torso,compatible_with_variant,velari_sleeves_v001,torso_under_cloth,cloth_basic,character_art
AST-SPECIES-VELARI-001,AST-EQUIP-GLOVE-001,hands,incompatible,,,grip_and_fingers,character_art
AST-SPECIES-VELARI-001,AST-EQUIP-BOOT-001,feet,incompatible,,,walk_contact,character_art
AST-SPECIES-VELARI-001,AST-EQUIP-HELM-001,head,compatible_with_variant,velari_helm_v002,ears_hidden,head_turn,character_art
AST-SPECIES-VELARI-001,AST-EQUIP-BELT-001,pelvis,compatible,,pelvis_under_belt,seated_and_run,character_art
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clé :** le triplet espèce, équipement et région évite de conclure qu’un objet est globalement compatible.
- **Adaptations :** `required_variant` et `body_mask` rendent les correctifs reproductibles.
- **Test :** chaque ligne pointe vers un ensemble de poses ou interactions à exécuter.
- **Résultat attendu :** l’interface d’équipement peut filtrer les combinaisons sans deviner depuis le maillage.

## 21. Définir les sockets et espaces libres

Un socket contient au minimum :

- un identifiant stable ;
- un parent osseux ;
- une transformation locale ;
- un axe avant et un axe supérieur ;
- un volume libre attendu ;
- une liste de catégories compatibles ;
- une version ;
- des tests.

Les sockets homologues peuvent porter le même rôle sans partager exactement la même transformation. Le socket `hand_grip_r` d’un Vélari peut être décalé pour une paume différente tout en restant compatible avec une arme conçue autour d’un volume de prise.
> **[VSC] Visual Studio Code — Créer : `art/blender/rigs/sockets/VELARI-SOCKETS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
profile_version: v001
sockets:
  - socket_id: "hand_grip_r"
    parent_bone: "Hand.R"
    local_position_m: [0.015, -0.025, 0.01]
    local_rotation_degrees: [0.0, 90.0, 0.0]
    forward_axis: "-Y"
    up_axis: "+Z"
    clearance_radius_m: 0.055
    categories:
      - "one_handed_weapon"
      - "standard_tool"
    test_set: "right_hand_grip"
  - socket_id: "back_carry"
    parent_bone: "Chest"
    local_position_m: [0.0, 0.10, 0.08]
    local_rotation_degrees: [0.0, 0.0, 0.0]
    forward_axis: "-Y"
    up_axis: "+Z"
    clearance_radius_m: 0.18
    categories:
      - "backpack"
      - "sheathed_weapon"
    test_set: "torso_twist_and_run"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transformations :** positions et rotations sont locales à l’os parent et utilisent des unités explicites.
- **Orientation :** `forward_axis` et `up_axis` évitent une correction spécifique à chaque objet attaché.
- **Volume :** `clearance_radius_m` transforme le clipping en contrainte testable.
- **Résultat attendu :** un équipement peut être attaché de manière cohérente entre Blender et Godot.

## 22. Organiser les variations culturelles sans stéréotype réducteur

Une espèce n’est pas une culture unique. Les variations culturelles sont décrites selon plusieurs axes indépendants :

- région ;
- climat ;
- période ;
- activité ;
- statut ;
- ressources ;
- technologie ;
- croyances ou institutions fictives ;
- échanges avec d’autres groupes ;
- choix individuels.

Les variations ne doivent pas :

- attribuer une personnalité à une anatomie ;
- associer automatiquement un trait physique à une profession ;
- copier une culture réelle sans contexte ni provenance ;
- uniformiser tous les membres ;
- utiliser une caricature comme raccourci visuel ;
- rendre un équipement incompatible obligatoire pour représenter le groupe.

L’anatomie commune reste identifiable sous plusieurs cultures, et une même culture peut être partagée par plusieurs espèces dans l’univers.
> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMANOID-CULTURAL-VARIANTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
anatomy_profile: AST-SPECIES-VELARI-001-v001
variants:
  - variant_id: VELARI-CANOPY-TRADER-001
    region: "canopy_trade_route"
    period: "current"
    activities:
      - "trade"
      - "maintenance"
    materials:
      - "woven_fiber"
      - "repaired_leather"
    silhouette_layers:
      - "short_cloak"
      - "tool_harness"
    anatomy_changes: []
  - variant_id: VELARI-URBAN-ARCHIVIST-001
    region: "vertical_city"
    period: "current"
    activities:
      - "archive_work"
    materials:
      - "dyed_textile"
      - "light_metal"
    silhouette_layers:
      - "long_tabard"
      - "document_case"
    anatomy_changes: []
forbidden_inferences:
  - "occupation_from_body_shape"
  - "personality_from_species"
  - "culture_from_skin_pattern"
review:
  worldbuilding: "pending"
  cultural_sensitivity: "pending"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** `anatomy_changes` vide confirme que la culture ne modifie pas silencieusement le profil anatomique.
- **Contexte :** région, période, activité et matériaux expliquent les choix visuels.
- **Garde :** `forbidden_inferences` documente les raccourcis explicitement interdits.
- **Résultat attendu :** plusieurs silhouettes culturelles restent compatibles avec la même espèce sans la réduire à un uniforme.

## 23. Préparer les matériaux et traits de surface

Le chapitre 10 approfondira peau, yeux, cheveux et pilosité. Ici, le profil d’espèce prépare seulement :

- familles de matériaux ;
- nombre de slots ;
- zones UV ;
- masques de variation ;
- canaux nécessaires ;
- traits qui influencent la silhouette ;
- traits qui disparaissent dans les LOD ;
- limites de transparence.

Une crête opaque peut être géométrique au LOD proche et intégrée à la silhouette du crâne au LOD lointain. Une membrane transparente peut nécessiter un matériau et un ordre de rendu propres. Ces décisions doivent être anticipées sans finaliser le shader.
## 24. Définir les LOD autour des traits distinctifs

La simplification suit cet ordre :

1. préserver la silhouette primaire ;
2. préserver les articulations et contacts ;
3. conserver au moins un trait secondaire ;
4. fusionner les petits volumes ;
5. réduire les chaînes secondaires ;
6. simplifier les matériaux ;
7. retirer les détails tertiaires ;
8. remplacer les animations secondaires par des approximations ou un état statique.

Un LOD n’est pas accepté parce qu’il possède moins de triangles. Il doit conserver :

- l’identité de l’espèce ;
- les proportions ;
- les contacts au sol ;
- les sockets importants ;
- les modules visibles ;
- l’absence d’intersection majeure ;
- la compatibilité des équipements déclarés.
> **[VSC] Visual Studio Code — Créer : `art/blender/lod/VELARI-LOD-PROFILE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
source_version: v001
levels:
  LOD0:
    intended_use: "closeup"
    target_triangles: 90000
    ear_chain_bones: 4
    hand_profile: "full"
    required_traits:
      - "long_forearms"
      - "semi_digitigrade_feet"
      - "swept_ears"
  LOD1:
    intended_use: "gameplay_near"
    target_triangles: 45000
    ear_chain_bones: 2
    hand_profile: "reduced"
    required_traits:
      - "long_forearms"
      - "semi_digitigrade_feet"
      - "swept_ears"
  LOD2:
    intended_use: "gameplay_mid"
    target_triangles: 18000
    ear_chain_bones: 0
    hand_profile: "merged_fingers"
    required_traits:
      - "long_forearms"
      - "semi_digitigrade_feet"
      - "ear_silhouette"
  LOD3:
    intended_use: "crowd_far"
    target_triangles: 7000
    ear_chain_bones: 0
    hand_profile: "mitten"
    required_traits:
      - "body_ratio"
      - "ear_silhouette"
thresholds_status: "unmeasured"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Budgets :** `target_triangles` fournit des plafonds provisoires, pas des mesures de performance.
- **Dégradation :** les chaînes d’oreilles et doigts sont réduites avant la silhouette principale.
- **Identité :** `required_traits` fixe ce qui doit survivre à chaque niveau.
- **Résultat attendu :** un LOD peut être refusé même s’il respecte son nombre de triangles.

## 25. Budgéter géométrie, os, matériaux et variantes

Le budget d’une espèce comprend :

- triangles par LOD ;
- sommets après séparation UV et normales ;
- os de déformation ;
- os supplémentaires ;
- influences par sommet ;
- matériaux ;
- textures ;
- variantes simultanées ;
- animations spécialisées ;
- coût des équipements ;
- temps de production et de revue.

Les valeurs sont d’abord des plafonds. Une mesure réelle précise :

- version de l’asset ;
- version du moteur ;
- renderer ;
- résolution ;
- distance ;
- animation ;
- nombre d’instances ;
- matériel ;
- méthode de capture.
> **[VSC] Visual Studio Code — Créer : `art/blender/budgets/VELARI-PRODUCTION-BUDGET.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
profile_version: v001
geometry:
  LOD0_triangles_max: 90000
  LOD1_triangles_max: 45000
  LOD2_triangles_max: 18000
  LOD3_triangles_max: 7000
rig:
  deform_bones_max: 72
  species_extra_bones_max: 12
  influences_default: 4
  influences_exception_max: 8
materials:
  material_slots_max: 5
  texture_sets_max: 3
variants:
  resident_morph_variants_max: 4
  equipment_variants_per_region_max: 3
performance:
  gpu_time_ms: null
  cpu_animation_time_ms: null
  memory_mib: null
measurement_status: "not_measured"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** le budget additionne coûts de maillage, squelette, matériaux et variantes.
- **Valeurs nulles :** les mesures runtime restent `null` tant qu’un protocole réel n’a pas été exécuté.
- **Exceptions :** huit influences ou des os supplémentaires consomment un budget identifié.
- **Résultat attendu :** les décisions de qualité et de performance peuvent être arbitrées sur des données comparables.

## 26. Organiser les fichiers Blender et collections

Chaque espèce pilote possède :

- une source canonique ;
- un profil d’espèce ;
- une collection de base ;
- des collections de modules ;
- une armature de déformation ;
- des contrôleurs non exportés ;
- des poses de test ;
- des LOD ;
- une collection d’export ;
- des manifestes.

Les variantes culturelles et équipements restent séparés de l’anatomie source. Les corrections d’animation ne doivent pas être appliquées au maillage de base sans nouvelle version.
> **[LECTURE] Collections Blender recommandées — Ne pas saisir.**

```text
AST_Species_Velari
├── 00_REFERENCE
├── 10_BASE
│   ├── MSH_Velari_Body
│   ├── MSH_Velari_Head
│   ├── MSH_Velari_Hands
│   └── MSH_Velari_Feet
├── 20_MODULES
│   ├── MOD_Ears
│   └── MOD_Crests
├── 30_RIG
│   ├── ARM_Velari_Deform
│   └── ARM_Velari_Control
├── 40_TEST_POSES
├── 50_EQUIPMENT_FIT
├── 60_LOD
│   ├── LOD0
│   ├── LOD1
│   ├── LOD2
│   └── LOD3
└── 90__EXPORT
    ├── ARM_Velari_Deform
    ├── MSH_Velari_Body_LOD0
    └── SOCKETS
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** `10_BASE` conserve l’anatomie source ; `90__EXPORT` contient uniquement le résultat d’échange.
- **Exclusion :** l’armature de contrôle reste hors de la collection d’export.
- **Tests :** poses et équipements sont séparés pour éviter de publier une déformation temporaire.
- **Résultat attendu :** une ouverture du fichier permet d’identifier immédiatement les éléments livrés et ceux réservés au travail.

## 27. Exporter vers glTF et Godot

Le chemin de référence reste GLB. glTF transporte :

- maillages ;
- hiérarchie de joints ;
- skins ;
- attributs `JOINTS_n` et `WEIGHTS_n` ;
- matériaux compatibles ;
- animations exportées ;
- morph targets lorsque pris en charge.

Le manifeste d’export enregistre :

- source et version ;
- profil d’espèce ;
- profil de rig ;
- LOD ;
- matériaux ;
- animations incluses ;
- influences ;
- fichiers et empreintes ;
- réserves.

Les contrôleurs Blender, références, caches et poses de travail sont exclus.
> **[VSC] Visual Studio Code — Créer : `art/blender/exports/manifests/VELARI-EXPORT-MANIFEST.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
export_id: AST-EXPORT-VELARI-LOD0-001
species_id: AST-SPECIES-VELARI-001
source_asset: AST-ASSET-MESH-VELARI-001
source_version: v001
rig_profile: AST-RIGPROFILE-VELARI-001
retarget_policy: AST-RETARGET-VELARI-001
container: "GLB"
collection: "90__EXPORT"
lod: "LOD0"
included:
  meshes:
    - "MSH_Velari_Body_LOD0"
  armature:
    - "ARM_Velari_Deform"
  sockets:
    - "hand_grip_r"
    - "back_carry"
excluded:
  - "ARM_Velari_Control"
  - "00_REFERENCE"
  - "40_TEST_POSES"
skin:
  default_influences: 4
animations: []
sha256: "TO_BE_GENERATED"
runtime_status: "not_exported"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Traçabilité :** source, profils et LOD permettent de relier le GLB à ses contrats.
- **Périmètre :** `included` et `excluded` empêchent l’export accidentel des contrôleurs ou références.
- **Intégrité :** l’empreinte reste un emplacement explicite tant que le fichier n’existe pas.
- **Résultat attendu :** Godot reçoit un paquet minimal dont l’autorité et les réserves sont connues.

## 28. Configurer l’import et le retargeting dans Godot

Dans l’import avancé :

1. sélectionner le `Skeleton3D` ;
2. créer ou assigner un `BoneMap` ;
3. choisir `SkeletonProfileHumanoid` seulement si le profil d’espèce est compatible ;
4. vérifier les correspondances ;
5. aligner les poses de repos ;
6. choisir la politique d’influences ;
7. contrôler les animations importées ;
8. réimporter ;
9. ouvrir une scène héritée de validation ;
10. ne jamais modifier directement la scène importée comme source d’autorité.

Les pistes d’os absents sont supprimées ou redirigées selon la politique. Les os supplémentaires restent disponibles pour des animations propres à l’espèce.
## 29. Construire les scènes Godot de validation

La validation utilise des scènes distinctes :

- silhouette ;
- pose et amplitude ;
- locomotion ;
- retargeting ;
- équipement ;
- sockets ;
- LOD ;
- performance.

Une scène unique peut orchestrer ces panneaux, mais chaque résultat doit rester attribuable à un test.
> **[LECTURE] Arbre de scène Godot recommandé — Ne pas saisir.**

```text
HumanoidValidationLab (Node3D)
├── EnvironmentRig (Node3D)
├── DistanceMarkers (Node3D)
├── SpeciesUnderTest (Node3D)
│   ├── ImportedModel (Node3D)
│   │   └── Skeleton3D
│   │       ├── RetargetModifier3D
│   │       └── SocketTargets (Node3D)
│   ├── EquipmentVariants (Node3D)
│   ├── CollisionReferences (Node3D)
│   └── LodController (Node)
├── HumanReference (Node3D)
├── PoseSequence (AnimationPlayer)
├── MovementTrack (Path3D)
├── Cameras (Node3D)
│   ├── NearCamera
│   ├── GameplayCamera
│   └── CrowdCamera
├── MetricsCollector (Node)
└── ValidationOverlay (CanvasLayer)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Comparaison :** `HumanReference` rend visibles les écarts d’échelle et de portée.
- **Isolation :** équipements, collisions de référence et LOD restent des enfants séparés du modèle importé.
- **Mesure :** `MetricsCollector` collecte des observations sans devenir propriétaire du maillage.
- **Résultat attendu :** les problèmes de silhouette, mouvement, socket et coût peuvent être reproduits dans une scène dédiée.

## 30. Valider structure, os et sockets par GDScript

Le script suivant contrôle uniquement des invariants structurels :

- présence du squelette ;
- présence des os obligatoires ;
- absence de doublons de noms ;
- présence des sockets requis ;
- cohérence minimale du nombre d’influences déclaré.

Il ne valide ni qualité artistique, ni déformation, ni retargeting visuel.
> **[VSC] Visual Studio Code — Créer : `game/tools/validation/humanoid_profile_validator.gd` — Ne pas saisir.**

```gdscript
@tool
class_name HumanoidProfileValidator
extends Node

@export var skeleton_path: NodePath
@export var required_bones: PackedStringArray = []
@export var required_socket_paths: Array[NodePath] = []
@export_range(1, 8, 1) var declared_influence_limit: int = 4

func validate_profile() -> PackedStringArray:
    var problems := PackedStringArray()
    var skeleton := get_node_or_null(skeleton_path) as Skeleton3D

    if skeleton == null:
        problems.append("Skeleton3D introuvable au chemin déclaré.")
        return problems

    var seen := {}
    for bone_index in skeleton.get_bone_count():
        var bone_name := String(skeleton.get_bone_name(bone_index))
        if seen.has(bone_name):
            problems.append("Nom d'os dupliqué : %s" % bone_name)
        else:
            seen[bone_name] = true

    for required_bone in required_bones:
        if skeleton.find_bone(required_bone) == -1:
            problems.append("Os obligatoire absent : %s" % required_bone)

    for socket_path in required_socket_paths:
        if get_node_or_null(socket_path) == null:
            problems.append("Socket absent : %s" % socket_path)

    if declared_influence_limit not in [4, 8]:
        problems.append("La limite d'influences doit être 4 ou 8.")

    return problems
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** `NodePath`, `PackedStringArray` et la limite d’influences sont configurés dans l’inspecteur de la scène de test.
- **Codes de résultat :** la fonction renvoie une liste vide en cas de conformité structurelle ou plusieurs messages explicites.
- **Déroulement :** le squelette est résolu, les noms sont indexés, puis les os, sockets et limites déclarées sont contrôlés.
- **Limite :** le script ne mesure pas les poids, poses de repos, contacts ni performances.

## 31. Définir la batterie de poses et mouvements

La batterie minimale comprend :

- repos naturel ;
- extension des bras ;
- bras croisés si anatomiquement possible ;
- prise d’objet ;
- rotation du tronc ;
- flexion profonde ;
- pas long ;
- course ;
- arrêt ;
- montée de marche ;
- position assise compatible ou explicitement bloquée ;
- port d’équipement ;
- changement de LOD en mouvement.

Les poses impossibles pour l’espèce ne sont pas forcées. Elles sont remplacées par un test fonctionnel équivalent ou déclarées incompatibles avec l’interaction.
> **[VSC] Visual Studio Code — Créer : `art/blender/tests/VELARI-POSE-TESTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
rig_profile: AST-RIGPROFILE-VELARI-001
tests:
  - test_id: POSE-REST-001
    animation: "velari_idle_neutral_v001"
    checks:
      - "balanced_support"
      - "ear_clearance"
      - "no_neck_intersection"
  - test_id: POSE-REACH-001
    animation: "human_reach_panel_v003"
    retarget_policy: "conditional"
    checks:
      - "hand_target_distance"
      - "elbow_volume"
      - "sleeve_clearance"
  - test_id: MOVE-WALK-001
    animation: "human_walk_forward_v004"
    correction_layer: "velari_walk_contact_v001"
    checks:
      - "forefoot_contact"
      - "no_visible_sliding"
      - "pelvis_stability"
  - test_id: EQUIP-BACK-001
    animation: "velari_run_v001"
    equipment:
      - "AST-EQUIP-BACKPACK-001"
    checks:
      - "back_socket_stability"
      - "ear_and_pack_clearance"
results: []
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Références :** chaque test nomme l’animation, le profil et les équipements réellement concernés.
- **Retargeting :** une animation humaine peut être testée avec une couche corrective sans devenir automatiquement approuvée.
- **Résultats :** la liste reste vide tant que la scène n’a pas été exécutée.
- **Résultat attendu :** les régressions sont attribuables à un test, une version et un contrat précis.

## 32. Mesurer la compatibilité et le coût

Une campagne de mesure consigne :

- modèle et LOD ;
- nombre d’instances ;
- animation ;
- équipements ;
- profil d’influences ;
- renderer ;
- résolution ;
- caméra ;
- CPU et GPU ;
- mémoire ;
- durée de capture ;
- résultat visuel ;
- anomalies.

Le coût doit être comparé à la base humaine et à une scène vide. Une espèce avec os secondaires, matériaux transparents et plusieurs variantes peut être plus chère malgré un nombre de triangles similaire.
> **[VSC] Visual Studio Code — Créer : `game/benchmarks/humanoids/VELARI-MEASUREMENT-RECORD.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
measurement_id: AST-MEASURE-VELARI-001
species_id: AST-SPECIES-VELARI-001
asset_version: v001
engine: "Godot 4.7.1-stable"
renderer: "Forward+"
hardware_profile: "ASTERIA-WIN-AMD-REF"
resolution: [1920, 1080]
scene: "res://tools/validation/humanoid_validation_lab.tscn"
instances: 1
lod: "LOD0"
animation: "velari_idle_neutral_v001"
equipment: []
skin_influences: 4
capture_seconds: 30
results:
  gpu_time_ms: null
  cpu_animation_time_ms: null
  memory_mib: null
visual_findings: []
status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** moteur, renderer, matériel, résolution et scène rendent la mesure comparable.
- **Variables :** LOD, animation, équipements et influences identifient les principaux facteurs de coût.
- **Intégrité :** les résultats restent `null` et le statut `not_executed` avant toute capture.
- **Résultat attendu :** une mesure future peut remplacer les budgets sans perdre ses conditions expérimentales.

## 33. Revue croisée et responsabilités

Une espèce pilote traverse les revues suivantes :

| Revue | Question principale | Autorité |
|---|---|---|
| direction artistique | l’espèce appartient-elle à l’univers et reste-t-elle identifiable ? | direction artistique |
| anatomie fonctionnelle | proportions, appuis et amplitudes sont-ils cohérents avec les actions ? | character art / animation |
| topologie | les boucles accompagnent-elles les déformations prévues ? | character art |
| rig | hiérarchie, poses de repos et profils sont-ils explicites ? | rigging |
| équipement | la matrice correspond-elle aux résultats de pose ? | character art / technical art |
| animation | retargeting et couches spécialisées sont-ils qualifiés ? | animation |
| performance | budgets et LOD respectent-ils les cibles mesurées ? | technical art |
| provenance | sources et modules sont-ils publiables ? | responsable de provenance |

Un avis esthétique ne remplace pas une validation de contact au sol. Un test de performance ne décide pas de la qualité culturelle ou narrative.
> **[VSC] Visual Studio Code — Créer : `art/blender/reviews/VELARI-REVIEW-GATE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
profile_version: v001
gates:
  artistic_direction:
    owner: "art_direction"
    status: "pending"
  anatomy_and_motion:
    owner: "character_animation"
    status: "pending"
  topology_and_modules:
    owner: "character_art"
    status: "pending"
  rig_and_retargeting:
    owner: "rigging"
    status: "pending"
  equipment_and_sockets:
    owner: "technical_art"
    status: "pending"
  performance_and_lod:
    owner: "technical_art"
    status: "pending"
  provenance:
    owner: "asset_governance"
    status: "pending"
publication:
  allowed_statuses:
    - "accepted"
    - "accepted_with_documented_limits"
  current_status: "blocked"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités :** chaque porte possède un propriétaire au lieu d’une approbation collective indéterminée.
- **Échec fermé :** `blocked` reste la valeur initiale jusqu’à la fermeture de toutes les portes obligatoires.
- **Limites :** `accepted_with_documented_limits` conserve les incompatibilités dans la décision de publication.
- **Résultat attendu :** une espèce ne peut pas être publiée parce qu’un seul domaine l’a jugée satisfaisante.

## 34. Mode Solo

Le parcours Solo retient :

- une espèce pilote complète avant toute famille de variantes ;
- une base humaine commune réutilisée autant que possible ;
- un seul profil de rig spécialisé ;
- une matrice d’équipement limitée aux objets réellement visibles ;
- un petit nombre de variations culturelles combinables ;
- des animations humaines partagées seulement après test ;
- des LOD produits selon les distances réellement utilisées ;
- une scène Godot de validation unique mais structurée par panneaux.

Le créateur Solo accepte explicitement les incompatibilités plutôt que de multiplier les correctifs invisibles.
## 35. Mode Studio

Le parcours Studio ajoute :

- profils d’espèce versionnés ;
- propriétaires de chaque incompatibilité ;
- bibliothèques de BoneMaps et poses de repos ;
- schémas de modules partagés ;
- matrices d’équipement centrales ;
- contrats de sockets ;
- revues croisées ;
- tests automatisés de structure ;
- campagnes de mouvement et de foule ;
- historique des dérogations ;
- publication immuable des versions acceptées ;
- procédure de retrait d’un profil défectueux.

Les équipes concept, character art, rigging, animation, technical art, narration et provenance partagent les mêmes identifiants.
## 36. Porte d’acceptation

Une espèce est acceptée lorsque :

- sa fonction et son périmètre sont définis ;
- ses écarts à la base humaine sont enregistrés ;
- sa silhouette reste lisible aux distances prévues ;
- sa posture et sa locomotion ne contredisent pas ses appuis ;
- sa topologie accompagne les articulations ;
- ses modules possèdent des interfaces versionnées ;
- son profil de rig distingue os communs, renommés, absents et supplémentaires ;
- son BoneMap et ses poses de repos sont qualifiés ;
- ses familles d’animations ont un statut ;
- ses équipements et sockets possèdent une matrice ;
- ses variations culturelles évitent les inférences interdites ;
- ses LOD conservent les traits distinctifs ;
- ses budgets sont mesurés ou explicitement provisoires ;
- ses preuves de provenance sont suffisantes ;
- aucune réserve bloquante n’est masquée.

Une incompatibilité documentée peut être acceptable. Une compatibilité supposée ne l’est pas.
> **[VSC] Visual Studio Code — Créer : `art/blender/checklists/HUMANOID-ACCEPTANCE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
species_id: AST-SPECIES-VELARI-001
profile_version: v001
checks:
  species_brief_complete: false
  deviations_registered: false
  silhouette_tests_passed: false
  anatomy_motion_reviewed: false
  topology_reviewed: false
  module_interfaces_verified: false
  rig_profile_verified: false
  bone_map_verified: false
  rest_pose_verified: false
  animation_families_qualified: false
  equipment_matrix_verified: false
  sockets_verified: false
  cultural_variants_reviewed: false
  lod_traits_preserved: false
  performance_measured: false
  provenance_accepted: false
blocking_reservations: []
decision:
  status: "blocked"
  decided_by: null
  decided_at: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État initial :** tous les contrôles restent faux tant que leurs preuves ne sont pas produites.
- **Réserves :** `blocking_reservations` sépare les problèmes bloquants des limites acceptables.
- **Décision humaine :** `decided_by` et `decided_at` empêchent une publication purement automatisée.
- **Résultat attendu :** la porte peut être relue et rejouée pour chaque nouvelle version de l’espèce.

## 37. Erreurs fréquentes, diagnostics et corrections

<!-- qa:error-correction-section -->

Les cas suivants doivent être relus comme des diagnostics reproductibles. Chaque correction rend visible le contrat qui manquait.
### 37.1 Déclarer compatible parce que la silhouette est bipède

**Symptôme ou risque :** les animations ou équipements humains sont appliqués sans test dès que l’espèce possède deux bras et deux jambes.

**Exemple fautif :**

```yaml
species_id: AST-SPECIES-VELARI-001
humanoid: true
human_compatible: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le booléen fusionne anatomie, rig, poses de repos, équipements, sockets et animations dans une seule affirmation impossible à auditer.

**Exemple corrigé :**

```yaml
species_id: AST-SPECIES-VELARI-001
compatibility:
  rig: "conditional"
  retargeting:
    locomotion: "conditional"
    seated: "blocked"
  equipment:
    torso: "compatible_with_variant"
    hands: "incompatible"
    feet: "incompatible"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction qualifie séparément les domaines et conserve les incompatibilités nécessaires aux outils de production.

### 37.2 Étirer la base humaine sans déplacer les boucles

**Symptôme ou risque :** les coudes ou genoux plient au milieu d’une zone étirée et provoquent pincement ou perte de volume.

**Exemple fautif :**

```text
Base humaine
→ mise à l'échelle du bras en mode Édition
→ articulation déplacée
→ boucles de coude laissées à leur position d'origine
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la géométrie change de proportion, mais les boucles conçues pour la compression restent décalées par rapport au nouvel axe de rotation.

**Exemple corrigé :**

```text
Base humaine
→ positionner les repères osseux de l'espèce
→ déplacer et redistribuer les boucles autour du nouvel axe
→ tester flexion, torsion et manche
→ enregistrer l'écart dans le profil
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction reconstruit la fonction de la topologie autour de l’articulation réelle et ajoute un test de vêtement.

### 37.3 Mapper des os uniquement par nom

**Symptôme ou risque :** le BoneMap paraît complet, mais les membres tournent dans un axe incorrect ou changent de volume.

**Exemple fautif :**

```yaml
bone_map:
  Hips: Hips
  Spine: Spine
  LeftUpperArm: UpperArm.L
rest_pose_check: "skipped"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** des noms correspondants ne prouvent ni l’orientation, ni le parentage, ni la longueur, ni la pose de repos des os.

**Exemple corrigé :**

```yaml
bone_map:
  Hips: Hips
  Spine: Spine
  LeftUpperArm: UpperArm.L
qualification:
  names: "passed"
  hierarchy: "passed"
  rest_pose: "pending"
  bone_axes: "pending"
  scale: "pending"
status: "blocked_until_qualification"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction sépare les contrôles nécessaires et bloque le retargeting tant que les poses et axes ne sont pas vérifiés.

### 37.4 Forcer tous les doigts humains dans une main différente

**Symptôme ou risque :** des os sans géométrie ou sans fonction reçoivent des poids artificiels et perturbent les animations de préhension.

**Exemple fautif :**

```text
Main à trois doigts
→ conserver cinq chaînes complètes
→ masquer deux doigts dans le maillage
→ transférer toutes les animations humaines
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les chaînes cachées ne correspondent pas à l’anatomie, compliquent le skinning et créent des pistes sans résultat visuel fiable.

**Exemple corrigé :**

```text
Main à trois doigts
→ définir un profil de main propre
→ mapper les fonctions réellement équivalentes
→ déclarer les os humains absents
→ créer des poses de prise spécialisées
→ qualifier chaque famille d'outil
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction représente l’anatomie réelle et limite le partage d’animations aux fonctions effectivement compatibles.

### 37.5 Réutiliser des bottes plantigrades sur des pieds digitigrades

**Symptôme ou risque :** la chaussure flotte, écrase le pied ou force une pose de repos incompatible avec le contact au sol.

**Exemple fautif :**

```csv
species_id,equipment_id,region,status
AST-SPECIES-VELARI-001,AST-EQUIP-BOOT-001,feet,compatible
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la ligne ne mentionne ni le profil de pied, ni la pose, ni les contacts, et présente la compatibilité comme acquise.

**Exemple corrigé :**

```csv
species_id,equipment_id,region,status,required_variant,test_set
AST-SPECIES-VELARI-001,AST-EQUIP-BOOT-001,feet,incompatible,,walk_contact
AST-SPECIES-VELARI-001,AST-EQUIP-FOOTWRAP-003,feet,compatible_with_variant,velari_wrap_v001,walk_contact
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction refuse l’objet inadapté et enregistre une variante testable conçue pour l’appui de l’espèce.

### 37.6 Attacher un équipement à un socket sans axes

**Symptôme ou risque :** les armes ou sacs arrivent avec une rotation différente selon l’espèce et reçoivent des correctifs par objet.

**Exemple fautif :**

```yaml
socket_id: hand_grip_r
parent_bone: Hand.R
position: [0.0, 0.0, 0.0]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la transformation ne définit ni unités, ni rotation, ni axes, ni volume libre, donc chaque consommateur doit deviner.

**Exemple corrigé :**

```yaml
socket_id: hand_grip_r
parent_bone: Hand.R
local_position_m: [0.015, -0.025, 0.01]
local_rotation_degrees: [0.0, 90.0, 0.0]
forward_axis: "-Y"
up_axis: "+Z"
clearance_radius_m: 0.055
test_set: "right_hand_grip"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction fournit un repère complet et un test commun à toutes les catégories compatibles.

### 37.7 Réduire l’espèce à une culture unique

**Symptôme ou risque :** tous les membres portent les mêmes couleurs, objets et rôles, et l’anatomie sert de raccourci narratif.

**Exemple fautif :**

```yaml
species_id: AST-SPECIES-VELARI-001
culture: "forest_traders"
personality: "secretive"
occupation: "merchant"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la structure déduit personnalité et profession depuis l’espèce et efface les variations régionales, historiques et individuelles.

**Exemple corrigé :**

```yaml
species_id: AST-SPECIES-VELARI-001
cultural_variants:
  - region: "canopy_trade_route"
    activities: ["trade", "maintenance"]
  - region: "vertical_city"
    activities: ["archive_work", "craft"]
forbidden_inferences:
  - "personality_from_species"
  - "occupation_from_body_shape"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction décrit plusieurs contextes et interdit explicitement les inférences qui transformeraient l’espèce en stéréotype.

### 37.8 Supprimer le trait distinctif au premier LOD

**Symptôme ou risque :** l’espèce devient visuellement humaine dès la distance de gameplay malgré un budget de triangles respecté.

**Exemple fautif :**

```yaml
LOD1:
  target_triangles: 45000
  remove:
    - "ears"
    - "digitigrade_foot_shape"
  status: "accepted"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la simplification retire les deux traits secondaires qui portent la reconnaissance et n’inclut aucun test de silhouette.

**Exemple corrigé :**

```yaml
LOD1:
  target_triangles: 45000
  preserve:
    - "ear_silhouette"
    - "semi_digitigrade_foot_profile"
    - "long_forearm_ratio"
  simplify:
    - "ear_internal_loops"
    - "finger_segments"
  required_test: "humanoid_silhouette_8m"
  status: "candidate"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction réduit les détails internes tout en préservant les traits nécessaires à la lecture de l’espèce.

### 37.9 Utiliser huit influences sans qualification

**Symptôme ou risque :** le modèle paraît correct sur un poste mais devient incompatible avec un renderer ou une cible de livraison.

**Exemple fautif :**

```yaml
skin:
  influences: 8
reason: "better_quality"
platform_tests: []
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la qualité supposée remplace la qualification technique et aucune cible n’est associée au choix.

**Exemple corrigé :**

```yaml
skin:
  default_influences: 4
  exception_influences: 8
  exception_regions:
    - "shoulder"
    - "hip"
qualification:
  renderers:
    - "Forward+"
  target_platforms:
    - "windows_reference"
  comparison_required: true
status: "pending_measurement"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction conserve le profil compatible par défaut et borne l’exception à des régions, cibles et comparaisons précises.

### 37.10 Corriger le retargeting en modifiant la source importée

**Symptôme ou risque :** une réimportation efface les corrections et personne ne sait si l’autorité réside dans Blender ou Godot.

**Exemple fautif :**

```text
Importer Velari.glb
→ ouvrir la scène importée
→ déplacer les os et modifier le maillage directement
→ sauvegarder la scène importée
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la scène importée est générée ; les modifications locales sont fragiles, non traçables et peuvent disparaître au prochain import.

**Exemple corrigé :**

```text
Corriger la pose de repos ou les poids dans la source Blender
→ versionner le profil et réexporter le GLB
→ configurer BoneMap et options d'import
→ créer une scène Godot héritée pour les couches de validation
→ conserver les correctifs runtime dans des nœuds dédiés
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la correction maintient Blender comme autorité de l’asset, l’import comme transformation reproductible et la scène héritée comme couche Godot.

## 38. Livrables permanents du chapitre

Le chapitre matérialise les cinq livrables du plan maître :

1. **bases humanoïdes** : fiche d’espèce, écarts et critères permettant de dériver ou créer une base ;
2. **règles d’adaptation anatomique** : proportions, articulations, topologie, modules, posture et locomotion ;
3. **profils de rig** : hiérarchie, os communs, renommés, absents et supplémentaires, BoneMap et politique de retargeting ;
4. **matrice de compatibilité des équipements** : régions, variantes, masques, sockets et tests ;
5. **scènes de test** : silhouette, poses, mouvement, équipement, LOD, retargeting et mesures.

Les exemples de fichiers constituent des modèles documentaires. Ils ne prouvent pas l’existence des assets de `Project Asteria`.
## 39. Décisions retenues pour `Project Asteria`

`Project Asteria` retient les décisions suivantes :

- la base humaine du chapitre 6 reste le contrat de comparaison ;
- chaque espèce possède un identifiant et un profil versionné ;
- les écarts anatomiques sont propagés vers rig, animations, équipements, sockets et LOD ;
- une compatibilité est qualifiée par domaine ;
- `SkeletonProfileHumanoid` n’est utilisé que lorsque la structure et les poses de repos le permettent ;
- les os supplémentaires restent hors du retargeting humain principal ;
- quatre influences constituent le profil par défaut ;
- les mains, pieds et casques reçoivent des variantes lorsque l’anatomie l’exige ;
- les cultures restent distinctes de l’anatomie et des capacités ;
- les traits distinctifs survivent aux distances de gameplay ;
- une incompatibilité documentée est préférable à un correctif silencieux ;
- aucune mesure runtime n’est inventée.
## 40. Références techniques officielles

- [Godot Engine — Retargeting 3D Skeletons](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/retargeting_3d_skeletons.html)
- [Godot Engine — `SkeletonProfile`](https://docs.godotengine.org/en/stable/classes/class_skeletonprofile.html)
- [Godot Engine — `SkeletonProfileHumanoid`](https://docs.godotengine.org/en/stable/classes/class_skeletonprofilehumanoid.html)
- [Godot Engine — `RetargetModifier3D`](https://docs.godotengine.org/en/stable/classes/class_retargetmodifier3d.html)
- [Godot Engine 4.7 — Import configuration](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html)
- [Godot Engine 4.7 — Available 3D formats](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)
- [Blender Manual 5.0 — Armature Structure](https://docs.blender.org/manual/en/5.0/animation/armatures/structure.html)
- [Blender Manual 5.0 — Weight Paint, Using Vertex Groups](https://docs.blender.org/manual/en/5.0/sculpt_paint/weight_paint/usage.html)
- [Blender Manual 5.0 — Shape Keys Introduction](https://docs.blender.org/manual/en/5.0/animation/shape_keys/introduction.html)
- [Khronos — glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
