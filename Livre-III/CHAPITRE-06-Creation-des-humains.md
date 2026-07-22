---
title: "Livre III — Chapitre 6 : Création des humains"
id: "DOC-L3-CH06"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 6
last-verified: "2026-07-23T00:42:11+02:00"
audit-status: "complete"
audit-date: "2026-07-23T00:42:11+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-06.md"
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

# Création des humains

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH06`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Les chapitres 1 à 5 ont défini le besoin artistique, la bible visuelle, la chaîne de références, le pipeline Blender et la politique de provenance. Le présent chapitre transforme ces décisions en une **base humaine de production** : un corps neutre, modulaire, crédible, compatible avec les futures étapes de rig, d’animation, de vêtements, de LOD et d’intégration Godot.

Le résultat attendu n’est pas un personnage jouable complet. Il s’agit d’un asset pilote dont les proportions, les variations morphologiques, la topologie, les séparations modulaires, les matériaux préparatoires et les budgets sont suffisamment explicites pour que les chapitres suivants puissent travailler sans reconstruire le contrat de base.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Références anatomiques et bible visuelle
    ↓
Guide de proportions versionné
    ↓
Base humaine neutre et symétrique de construction
    ↓
Topologie de déformation et modules compatibles
    ↓
Variantes morphologiques contrôlées
    ↓
Préparation UV, matériaux et textures
    ↓
Profils LOD et budgets provisoires
    ↓
Export GLB de validation
    ↓
Scène Godot de poses, silhouettes et coût
    ↓
Décision : accepter, corriger ou bloquer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** la chaîne place les décisions anatomiques et techniques avant la multiplication des variantes.
- **Déroulement :** chaque étape produit un livrable qui peut être relu indépendamment avant de devenir une dépendance du rig ou des vêtements.
- **Invariant :** la base de construction reste distincte des exports, des LOD générés et des personnages de jeu.
- **Résultat attendu :** une personne peut expliquer pourquoi une variante est compatible ou non sans se fier uniquement à son apparence.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- constituer des références anatomiques traçables sans transformer une moyenne statistique en norme esthétique ;
- définir des repères de proportions utiles à la production 3D ;
- construire une base neutre qui préserve les volumes osseux, musculaires et adipeux nécessaires aux déformations ;
- organiser les boucles de topologie autour des épaules, hanches, coudes, genoux, mains, pieds et zones expressives ;
- distinguer symétrie de construction, asymétrie anatomique et asymétrie narrative ;
- produire des variantes d’âge adulte, de taille et de corpulence sans stéréotype automatique ;
- séparer corps, tête, mains, pieds et modules tout en gardant des frontières compatibles ;
- préparer les UV, matériaux et textures sans empiéter sur le lookdev détaillé du chapitre 10 ;
- définir des budgets de triangles, surfaces, influences, textures et mémoire comme hypothèses mesurables ;
- préparer des profils LOD qui conservent silhouette, articulations et compatibilité ;
- créer une scène Godot de validation des poses, distances et coûts ;
- documenter les réserves, résultats et décisions sans prétendre à une exécution non réalisée.

## 3. Niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Les procédures Blender, les contrats de données, les paramètres d’import Godot et les scripts de contrôle ont été relus contre les documentations officielles citées à la fin du chapitre.

Aucun fichier `.blend`, aucun corps humain, aucun rig, aucune texture, aucun export GLB, aucune scène Godot et aucune mesure runtime de `Project Asteria` ne sont revendiqués comme matérialisés. Les nombres de triangles, tailles de textures et distances proposés sont des **budgets de conception provisoires**. Ils doivent être remplacés ou confirmés par des mesures conservées lorsque les assets pilotes existent.

Le chapitre ne fournit pas de conseil médical, biométrique ou anthropologique. Les proportions servent à construire des modèles 3D cohérents ; elles ne classent ni la valeur, ni la santé, ni l’identité d’une personne réelle.

## 4. Périmètre et frontières

Le chapitre définit :

- le contrat d’une base humaine générique ;
- les références anatomiques et repères de proportions ;
- la topologie nécessaire aux futures déformations ;
- les variantes morphologiques de base ;
- les séparations modulaires ;
- la préparation des UV et matériaux ;
- les budgets provisoires et profils LOD ;
- la scène de validation Godot ;
- les procédures Solo et Studio.

Il ne définit pas :

- les espèces humanoïdes du chapitre 7 ;
- les animaux du chapitre 8 ;
- les créatures non humanoïdes du chapitre 9 ;
- le visage final, la peau détaillée, les yeux, les dents, les cheveux et la pilosité du chapitre 10 ;
- les vêtements, armures, accessoires, masques de corps et simulations du chapitre 11 ;
- le rig final, le skinning et les contraintes du chapitre 19 ;
- les animations finales et le retargeting de production du chapitre 20 ;
- l’identité, les statistiques, la sauvegarde ou le contrôleur de gameplay traités dans le Livre II ;
- la logique de personnalisation runtime ou l’interface de création de personnage.

> **Frontière essentielle :** ce chapitre produit un **contrat d’asset visuel**. Il ne crée ni le système métier `CharacterDefinition`, ni un personnage jouable, ni une interface de personnalisation.

## 5. Prérequis

Le lecteur doit connaître :

- la bible visuelle du chapitre 2 ;
- les règles de références et de provenance des chapitres 3 et 5 ;
- les unités, axes, noms, dossiers et exports du chapitre 4 ;
- les bases de Blender : modes Objet, Édition et Sculpture, modificateurs, collections et matériaux ;
- la navigation dans l’éditeur 3D de Godot ;
- la différence entre source canonique, export et livraison.

Le projet doit déjà prévoir :

- une échelle métrique cohérente ;
- une collection Blender réservée à l’export ;
- un registre de provenance ;
- une convention de noms ;
- une politique de versions ;
- une racine de tests Godot.

## 6. Vocabulaire de production

### 6.1 Base humaine

Maillage de référence à partir duquel sont dérivées des variantes compatibles. La base n’est pas un individu moyen universel ; elle est un point de construction documenté pour un ensemble d’usages définis.

### 6.2 Morphotype

Configuration de proportions et de volumes : taille, longueur des membres, largeur du bassin, largeur des épaules, masse musculaire, volume adipeux et autres paramètres utiles à la silhouette. Un morphotype ne déduit pas automatiquement âge, métier, origine, personnalité ou capacité.

### 6.3 Topologie de déformation

Organisation des sommets, arêtes et faces conçue pour accompagner un changement de pose sans écrasement, torsion ou étirement incontrôlé.

### 6.4 Boucle de déformation

Ensemble d’arêtes qui entoure ou accompagne une articulation, un volume musculaire ou une zone expressive afin de distribuer la courbure.

### 6.5 Module

Partie interchangeable qui respecte une interface : tête, mains, pieds ou autre élément prévu. L’interface comprend la forme de la frontière, le nombre et l’ordre des sommets, les normales, les UV, les noms et les règles de transformation.

### 6.6 Pose de référence

Pose utilisée comme état de construction et d’échange. Elle ne remplace pas les poses de validation. Une base qui paraît correcte uniquement dans sa pose de référence n’est pas validée.

### 6.7 LOD

Niveau de détail utilisé lorsque la couverture à l’écran diminue. Le LOD doit réduire le coût sans changer brutalement la silhouette, casser les articulations ou invalider les matériaux et modules.

### 6.8 Budget

Plafond de conception ou cible mesurable : triangles, sommets, surfaces, matériaux, textures, influences d’os, mémoire ou temps de rendu. Un budget provisoire n’est pas une mesure.

## 7. Constituer des références anatomiques responsables

Une planche utile associe chaque image à une question de production :

- où se trouvent les repères osseux visibles ;
- comment les masses changent entre repos et mouvement ;
- quelles proportions varient réellement ;
- quelles zones doivent se comprimer ou s’étirer ;
- quels écarts appartiennent à la morphologie, à la posture, à l’objectif ou à la perspective ;
- quelles références sont autorisées pour l’usage prévu.

Les références doivent couvrir plusieurs morphologies, âges adultes, tailles, corpulences et postures. Elles évitent de mélanger photographie en perspective, schéma orthographique, pose dynamique et mesure clinique comme s’ils décrivaient la même chose.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-REFERENCE-SET.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
reference_set_id: AST-HUMAN-REF-001
purpose: "Base humaine de production et tests de déformation."
licence_status: "under_review"
sources:
  - source_id: REF-ANATOMY-001
    kind: "anatomy_diagram"
    view: "front"
    perspective: "orthographic_or_corrected"
    questions:
      - "Repères osseux du bassin et des épaules."
      - "Alignement relatif des articulations."
    allowed_use:
      - "internal_reference"
  - source_id: REF-MOTION-001
    kind: "motion_reference"
    view: "three_quarter"
    perspective: "photographic"
    questions:
      - "Compression du coude."
      - "Glissement de l'omoplate."
    allowed_use:
      - "internal_reference"
exclusions:
  - "Aucune image copiée dans une texture de livraison."
  - "Aucune identité réelle utilisée comme preset de personnage."
review:
  artistic: "pending"
  provenance: "pending"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `questions` relie chaque source à un besoin concret ; `allowed_use` empêche d’étendre silencieusement son usage.
- **Invariant :** une source de référence ne devient jamais une texture ou un asset final sans décision et preuve distinctes.
- **Statuts :** `pending` et `not_executed` rendent visibles les revues et tests encore absents.
- **Résultat attendu :** la planche peut être auditée sans supposer que toutes les images possèdent les mêmes droits ou la même valeur technique.

## 8. Définir le guide de proportions

Les proportions servent de repères, pas de grille punitive. Le guide retient des distances directement mesurables dans Blender :

- hauteur totale ;
- hauteur du sommet du crâne au menton ;
- largeur des épaules ;
- largeur du bassin ;
- hauteur des hanches ;
- hauteur des genoux ;
- longueur bras et avant-bras ;
- longueur cuisse et jambe ;
- longueur main et pied ;
- épaisseur du thorax et du bassin.

Une unité de « tête » peut aider à comparer les silhouettes, mais les dimensions métriques restent l’autorité pour les exports et les collisions futures.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-PROPORTIONS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
guide_id: AST-HUMAN-PROP-001
unit: "meter"
reference_pose: "A_pose_relaxed"
coordinate_contract:
  up_axis: "+Y_in_Godot"
  forward_axis: "+Z_in_Godot"
measurements:
  stature:
    target: 1.72
    tolerance: 0.02
  shoulder_width:
    target: 0.42
    tolerance: 0.03
  hip_width:
    target: 0.32
    tolerance: 0.03
  hip_height:
    target: 0.91
    tolerance: 0.03
  knee_height:
    target: 0.49
    tolerance: 0.03
landmarks:
  - crown
  - chin
  - acromion_left
  - acromion_right
  - elbow_left
  - elbow_right
  - wrist_left
  - wrist_right
  - iliac_left
  - iliac_right
  - knee_left
  - knee_right
  - ankle_left
  - ankle_right
authority:
  dimensions: "metric_measurements"
  head_units: "comparison_only"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** chaque mesure possède une cible et une tolérance de travail ; elles ne décrivent pas une norme humaine.
- **Décision :** `dimensions` place les mètres au-dessus des unités visuelles de tête pour les échanges techniques.
- **Dépendance :** les axes suivent le contrat du chapitre 4 et doivent être contrôlés après import.
- **Résultat attendu :** deux variantes peuvent être comparées avec les mêmes repères sans imposer une silhouette unique.

Les valeurs du manifeste illustrent une base pilote. Elles doivent être adaptées à la bible visuelle et ne deviennent pas des vérités anatomiques générales.

## 9. Choisir la pose de construction

Une A-pose détendue réduit la torsion initiale de l’épaule et laisse de la place au bras. Une T-pose peut simplifier certains profils de retargeting. Le projet choisit une pose de construction, puis conserve des poses de test indépendantes.

Pour `Project Asteria`, le contrat documentaire retient :

- pieds parallèles, légèrement espacés ;
- genoux sans hyperextension ;
- bassin neutre ;
- colonne sans cambrure exagérée ;
- omoplates en position de repos ;
- bras en A-pose modérée ;
- coudes et doigts légèrement fléchis ;
- mains ouvertes sans tension ;
- regard horizontal ;
- origine au sol, sous le centre du personnage.

Le chapitre 19 pourra décider d’une pose de rig différente si le changement est enregistré et testé. La géométrie ne doit pas dépendre d’une correction cachée dans l’armature.

## 10. Construire la base neutre

La base commence par de grands volumes :

1. cage thoracique ;
2. bassin ;
3. colonne et cou ;
4. crâne simplifié ;
5. bras et avant-bras ;
6. cuisses et jambes ;
7. mains et pieds ;
8. transitions articulaires.

Le travail alterne silhouette et volumes transversaux. Une vue frontale ne suffit pas : la profondeur du thorax, l’inclinaison du bassin, la projection des genoux, la voûte plantaire et l’épaisseur des mains influencent le rig et les vêtements.

> **[APP] Blender — Créer la source canonique : `art/blender/sources/characters/humans/AST-HUMAN-BASE-v001.blend`.**

La source contient au minimum :

- collection `AST_HUMAN_BASE`;
- objet `HUMAN_BASE_BODY`;
- objet de référence `HUMAN_GUIDES`;
- collection `VALIDATION_POSES`;
- collection d’export `EXPORT_HUMAN_BASE`;
- modificateur Mirror non appliqué pendant la construction ;
- subdivision uniquement pour l’affichage ou la sculpture contrôlée ;
- échelle d’objet appliquée avant export ;
- historique de versions dans le manifeste.

## 11. Symétrie, asymétrie et reproductibilité

La symétrie réduit le coût de construction et stabilise les interfaces modulaires. Elle ne doit pas effacer les asymétries nécessaires :

- volumes internes non parfaitement symétriques ;
- posture et dominance latérale ;
- cicatrices, handicaps ou variations narratives ;
- différences de tension entre côtés ;
- détails de surface ;
- objets portés.

Le projet conserve trois états distincts :

1. **base de construction symétrique** ;
2. **variante morphologique symétrique** ;
3. **asymétrie ajoutée et documentée**.

Une asymétrie permanente ne doit pas être ajoutée avant que le rig, les vêtements et les LOD puissent la reproduire ou la neutraliser selon le besoin.

## 12. Topologie générale

Une topologie adaptée à la déformation privilégie :

- quadrilatères réguliers dans les zones de mouvement ;
- densité concentrée autour des articulations et silhouettes ;
- flux qui suit les volumes anatomiques ;
- pôles placés hors des lignes de pli principales ;
- continuité entre les modules ;
- triangles réservés aux zones stables ou aux exports contrôlés ;
- absence de faces internes inutiles ;
- normales cohérentes ;
- échelle de densité progressive, sans rupture brutale.

La topologie ne doit pas reproduire chaque muscle. Elle doit fournir assez de degrés de liberté pour que le rig et les correctifs futurs puissent conserver les volumes.

## 13. Épaules et omoplates

L’épaule combine plusieurs mouvements : élévation du bras, rotation de l’humérus, mouvement de la clavicule et glissement de l’omoplate. Une simple charnière sphérique produit souvent un pincement sous l’aisselle et un effondrement du deltoïde.

La base prévoit :

- une boucle autour du deltoïde ;
- un flux depuis le pectoral vers le bras ;
- un flux dorsal vers l’omoplate ;
- une aisselle sans étoile de pôles au point de compression ;
- assez de géométrie pour lever le bras sans déchirer la silhouette ;
- des poses de test à 0°, 45°, 90° et au-dessus de la tête.

Le chapitre 19 décidera des os de clavicule, twist bones et correctifs. Le présent chapitre garantit seulement que la géométrie peut les recevoir.

## 14. Coudes et avant-bras

Le coude demande une zone de compression à l’intérieur et une zone d’étirement à l’extérieur. Deux ou trois boucles proches de l’articulation permettent de répartir la courbure. L’avant-bras doit aussi supporter la pronation et la supination sans vriller brutalement le poignet.

Contrôles visuels :

- le volume du coude reste identifiable à 90° ;
- l’intérieur ne s’interpénètre pas ;
- l’avant-bras conserve une section crédible en rotation ;
- les arêtes ne forment pas une spirale incontrôlée ;
- la frontière avec la main reste compatible.

## 15. Bassin et hanches

Le bassin relie le tronc aux membres inférieurs et reçoit des variations morphologiques importantes. La topologie doit éviter une couture circulaire simple autour de la hanche.

La base prévoit :

- un flux autour de l’aine ;
- une transition entre abdomen, fessiers et cuisse ;
- de la géométrie pour flexion, abduction et rotation ;
- une zone fessière qui conserve le volume en position assise ;
- une profondeur de bassin compatible avec les vêtements ;
- une origine et un repère de hanche clairement documentés.

## 16. Genoux et jambes

Le genou se plie principalement dans un axe, mais la forme visible dépend de la rotule, des condyles, des tendons et de la compression arrière.

La topologie conserve :

- une boucle autour de la rotule ;
- une zone d’étirement au-dessus et au-dessous ;
- une zone de compression derrière le genou ;
- un alignement du genou avec la direction du pied ;
- une transition progressive vers la cheville ;
- des poses de test debout, accroupie et agenouillée.

## 17. Mains

Les mains sont modulaires, mais leur frontière doit rester stable. La base comprend :

- paume avec épaisseur ;
- pouce orienté hors du plan de la paume ;
- articulations principales des doigts ;
- espaces entre les doigts ;
- ongles et plis réservés au détail du chapitre 10 si nécessaire ;
- topologie compatible avec une fermeture du poing ;
- densité suffisante pour les silhouettes proches prévues.

La main de base n’a pas besoin de reproduire chaque tendon. Elle doit se fermer, pointer, saisir et rester compatible avec les futurs rigs et objets.

## 18. Pieds

Le pied supporte le poids et définit les contacts au sol. Une forme de chaussure générique ne suffit pas à une base humaine.

La base prévoit :

- talon ;
- voûte ;
- plante ;
- avant-pied ;
- gros orteil distinct au niveau de la masse ;
- articulation de l’avant-pied ;
- direction de la cheville ;
- semelle de contact compatible avec le sol.

Les orteils individuels peuvent être simplifiés selon les plans de caméra et les chaussures. La décision appartient au budget, pas à une préférence implicite.

## 19. Séparer les modules

`Project Asteria` utilise une base en modules logiques :

- `BODY` : tronc et membres jusqu’aux interfaces ;
- `HEAD` : tête et cou selon la frontière retenue ;
- `HAND_L` et `HAND_R` ;
- `FOOT_L` et `FOOT_R` si l’usage justifie leur interchangeabilité ;
- modules optionnels uniquement après preuve de compatibilité.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-MODULE-CONTRACT.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
contract_id: AST-HUMAN-MODULES-001
base_asset_id: AST-ASSET-MESH-HUMANBASE-001
interfaces:
  neck:
    owner_a: BODY
    owner_b: HEAD
    vertex_count: 32
    vertex_order: "clockwise_from_spine_marker"
    transform_space: "object_local"
    normal_policy: "matched"
    uv_policy: "continuous_or_hidden_seam"
  wrist_left:
    owner_a: BODY
    owner_b: HAND_L
    vertex_count: 24
    vertex_order: "clockwise_from_radius_marker"
    transform_space: "object_local"
    normal_policy: "matched"
  wrist_right:
    mirrors: wrist_left
  ankle_left:
    owner_a: BODY
    owner_b: FOOT_L
    vertex_count: 24
    vertex_order: "clockwise_from_tibia_marker"
    transform_space: "object_local"
    normal_policy: "matched"
  ankle_right:
    mirrors: ankle_left
compatibility:
  topology_revision: 1
  uv_revision: 1
  rig_contract_revision: 0
  lod_contract_revision: 1
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `vertex_count` et `vertex_order` rendent l’interface testable au lieu de la décrire comme « proche ».
- **Dépendances :** les révisions permettent de refuser une tête ou une main construite contre une topologie plus ancienne.
- **Invariant :** les coordonnées sont comparées dans le même espace local et les normales doivent produire une couture invisible ou volontaire.
- **Réserve :** `rig_contract_revision: 0` indique que le rig final n’existe pas encore.
- **Résultat attendu :** une variante incompatible est bloquée avant le skinning ou l’export.

## 20. Variantes morphologiques

Les variantes doivent préserver :

- les interfaces modulaires ;
- le nombre et l’ordre des sommets lorsque des shape keys communes sont prévues ;
- les boucles de déformation ;
- la pose de référence ;
- les UV ou une stratégie explicite de remplacement ;
- les noms d’objets et matériaux ;
- les repères utilisés par le rig futur ;
- les budgets de chaque profil.

Les paramètres ne doivent pas devenir des raccourcis sociaux. Une valeur de corpulence ne change pas automatiquement force, santé, profession, âge ou personnalité. Ces données appartiennent à d’autres systèmes.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-VARIANTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
variant_set_id: AST-HUMAN-VARIANTS-001
base_asset_id: AST-ASSET-MESH-HUMANBASE-001
topology_revision: 1
parameters:
  stature:
    type: float
    unit: meter
    range: [1.50, 2.00]
    default: 1.72
  shoulder_scale:
    type: float
    range: [0.88, 1.14]
    default: 1.0
  pelvis_scale:
    type: float
    range: [0.88, 1.16]
    default: 1.0
  limb_length:
    type: float
    range: [0.92, 1.08]
    default: 1.0
  muscle_volume:
    type: float
    range: [0.0, 1.0]
    default: 0.35
  adipose_volume:
    type: float
    range: [0.0, 1.0]
    default: 0.30
rules:
  - "Aucun paramètre ne modifie l'identité, le métier ou les capacités de gameplay."
  - "Les extrêmes doivent réussir les mêmes poses de validation."
  - "Les modules conservent leurs frontières ou déclarent une révision incompatible."
presets:
  - id: BASELINE
    values:
      stature: 1.72
      shoulder_scale: 1.0
      pelvis_scale: 1.0
      limb_length: 1.0
      muscle_volume: 0.35
      adipose_volume: 0.30
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types et plages :** chaque paramètre possède une unité ou une plage explicite afin d’éviter des valeurs sans contrat.
- **Invariant :** les règles dissocient morphologie visuelle et statistiques de gameplay.
- **Effet de bord attendu :** modifier un extrême peut révéler une incompatibilité de topologie ou de rig ; le preset reste alors bloqué.
- **Résultat attendu :** les variantes peuvent être reproduites et comparées sans dépendre d’un nom subjectif.

## 21. Âge et évolution morphologique

Le chapitre traite seulement des variations adultes nécessaires à la production. Une variation d’âge crédible ne se résume pas à agrandir ou réduire uniformément le corps.

Les changements possibles concernent :

- proportions relatives du crâne, du tronc et des membres ;
- posture ;
- masse musculaire ;
- distribution des volumes ;
- reliefs osseux ;
- élasticité et plis de surface ;
- mains, pieds, cou et épaules ;
- amplitude de mouvement prévue.

Les enfants, adolescents, vieillissement avancé, grossesse, pathologies et handicaps demandent des références, validations et responsabilités spécifiques. Ils ne sont pas générés automatiquement depuis un curseur unique dans ce chapitre.

## 22. Shape keys et variantes de maillage

Les shape keys conviennent aux transformations qui conservent exactement la topologie. Elles peuvent :

- ajuster une proportion ;
- ajouter un volume ;
- corriger une silhouette ;
- préparer un correctif de pose futur ;
- conserver une interpolation entre états compatibles.

Elles ne doivent pas :

- déplacer une interface modulaire hors contrat ;
- provoquer une auto-intersection systématique ;
- remplacer une topologie nécessairement différente ;
- contenir une correction propre à un rig non défini ;
- être utilisées comme unique source d’une variante si leur combinaison n’est pas testée.

Les variantes nécessitant une topologie différente reçoivent un nouvel asset ou une nouvelle révision incompatible, pas une shape key forcée.

## 23. Préparer les UV

Le chapitre prépare, sans finaliser le lookdev :

- une densité de texels cohérente par profil ;
- des coutures placées hors des zones de regard ou cachées par les modules lorsque possible ;
- une marge suffisante entre îlots ;
- une orientation stable des zones symétriques ;
- une décision sur le chevauchement volontaire ;
- des UV distincts si le bake, les lightmaps ou les effets futurs l’exigent ;
- une correspondance documentée entre LOD lorsque la texture est partagée.

La tête peut conserver une UV dédiée pour le chapitre 10. Le corps ne doit pas consommer la totalité du budget de texture avant que vêtements et gros plans soient connus.

## 24. Préparer les matériaux

La base utilise un nombre réduit de surfaces clairement nommées :

- `MAT_BODY_SKIN_PLACEHOLDER`;
- `MAT_HEAD_PLACEHOLDER`;
- `MAT_EYES_PLACEHOLDER` uniquement si les yeux sont inclus dans le test ;
- `MAT_TEETH_PLACEHOLDER` uniquement si nécessaire ;
- `MAT_DEBUG_UV`;
- `MAT_DEBUG_NORMALS`.

Le shader de peau final, les yeux, dents, cheveux et pilosité sont réservés au chapitre 10. Le présent chapitre vérifie :

- que les surfaces sont séparées selon leur futur besoin ;
- que les tangentes et normales sont cohérentes ;
- que les matériaux temporaires ne masquent pas une couture ou un défaut ;
- que le nombre de surfaces reste compatible avec le budget.

## 25. Contrat de topologie et de qualité

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-TOPOLOGY-POLICY.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
policy_id: AST-HUMAN-TOPOLOGY-001
base_asset_id: AST-ASSET-MESH-HUMANBASE-001
requirements:
  manifold_surface: true
  unapplied_negative_scale: false
  duplicate_vertices: 0
  loose_geometry: 0
  internal_faces: 0
  non_planar_faces:
    allowed_only_if_reviewed: true
  deformation_zones:
    shoulder:
      test_angles_deg: [0, 45, 90, 150]
    elbow:
      test_angles_deg: [0, 45, 90, 135]
    hip:
      test_angles_deg: [0, 45, 90, 120]
    knee:
      test_angles_deg: [0, 45, 90, 135]
    wrist:
      test_rotation_deg: [-90, 0, 90]
  modules:
    contract: HUMAN-MODULE-CONTRACT.yaml
  naming:
    vertex_groups: "reserved_for_chapter_19"
  triangulation:
    source_policy: "quads_preferred"
    export_policy: "deterministic_triangulation_required"
acceptance:
  visual_review: "required"
  technical_review: "required"
  rig_review: "pending_chapter_19"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exigences :** les nombres nuls rendent bloquantes les géométries détachées, doublons et faces internes non justifiées.
- **Tests :** les angles décrivent une batterie de poses, pas un rig déjà créé.
- **Frontière :** les groupes de sommets et la revue de rig restent réservés au chapitre 19.
- **Résultat attendu :** le rapport peut distinguer un défaut de géométrie d’une réserve liée à une étape future.

## 26. Budgets provisoires

Les budgets dépendent des plans de caméra, du nombre de personnages visibles, des matériaux, des ombres, de l’animation et du matériel cible. Les valeurs suivantes sont des cibles initiales pour un humanoïde pilote réaliste de `Project Asteria`, pas des résultats mesurés.

| Profil | Usage prévu | Triangles corps complet | Surfaces | Textures corps | Influences prévues |
|---|---|---:|---:|---|---:|
| LOD0 | gros plan contrôlé | ≤ 80 000 | ≤ 6 | jusqu’à 4K selon mesure | jusqu’à 8 si chemin qualifié |
| LOD1 | dialogue et jeu proche | ≤ 45 000 | ≤ 6 | 2K–4K | 4 ou 8 selon import |
| LOD2 | jeu moyen | ≤ 20 000 | ≤ 4 | 2K | 4 |
| LOD3 | distance | ≤ 8 000 | ≤ 3 | 1K–2K | 4 |
| LOD4 | foule lointaine | ≤ 2 500 | ≤ 2 | atlas ou 1K | 4 |

Les nombres de triangles incluent les modules réellement visibles dans le profil. Ils doivent être répartis entre corps, tête, mains, pieds et éléments ajoutés. Une limite élevée n’autorise pas à remplir le budget sans bénéfice visible.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-LOD-BUDGETS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
budget_id: AST-HUMAN-LOD-001
status: "provisional"
measurement_hardware:
  gpu: "AMD Radeon RX 6750 XT 12GB"
  cpu: "Ryzen 7 2700"
  ram_gb: 32
profiles:
  LOD0:
    max_triangles: 80000
    max_surfaces: 6
    max_visible_materials: 6
    max_texture_edge_px: 4096
    silhouette_priority: "highest"
  LOD1:
    max_triangles: 45000
    max_surfaces: 6
    max_visible_materials: 6
    max_texture_edge_px: 4096
  LOD2:
    max_triangles: 20000
    max_surfaces: 4
    max_visible_materials: 4
    max_texture_edge_px: 2048
  LOD3:
    max_triangles: 8000
    max_surfaces: 3
    max_visible_materials: 3
    max_texture_edge_px: 2048
  LOD4:
    max_triangles: 2500
    max_surfaces: 2
    max_visible_materials: 2
    max_texture_edge_px: 1024
rules:
  - "Les seuils de distance sont mesurés dans Godot, jamais déduits du numéro de LOD."
  - "Chaque réduction conserve les interfaces encore utilisées."
  - "Les articulations restent testées après simplification."
  - "Les mesures réelles remplacent les hypothèses sans modifier silencieusement l'historique."
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `provisional` interdit de présenter les plafonds comme une optimisation démontrée.
- **Dépendance matérielle :** le matériel de référence identifie le contexte futur des mesures.
- **Invariant :** les seuils sont choisis selon la couverture écran et les scènes réelles, pas uniquement selon une distance arbitraire.
- **Résultat attendu :** chaque mesure runtime pourra être comparée à une hypothèse versionnée.

## 27. Produire les LOD

Deux approches peuvent coexister :

1. **LOD importés** : variantes créées et contrôlées dans Blender ;
2. **LOD générés par Godot** : simplification à l’import lorsque le résultat respecte la silhouette et les déformations.

Pour une base humaine skinnée, les LOD manuels sont préférables lorsque :

- les mains, le visage ou les articulations demandent un contrôle précis ;
- les modules changent selon la distance ;
- les matériaux doivent être fusionnés ;
- les poids ou blend shapes doivent rester compatibles ;
- la silhouette est une information de gameplay.

La génération automatique reste un outil de proposition. Elle ne supprime pas la revue des poses et des coutures. Godot choisit les LOD de maillage selon une mesure de couverture à l’écran ; les seuils doivent donc être observés dans plusieurs résolutions et champs de vision.

## 28. Préparer le contrat avec le rig

Le chapitre 19 aura l’autorité sur l’armature et le skinning. Le présent chapitre prépare :

- une pose de référence documentée ;
- des articulations placées anatomiquement ;
- une topologie compatible avec des boucles de twist ;
- des noms d’objets stables ;
- une origine cohérente ;
- des variantes qui conservent les repères ;
- un espace pour les correctifs de pose ;
- une décision sur quatre ou huit influences à qualifier dans Godot.

Godot propose un `SkeletonProfileHumanoid` pour standardiser le retargeting. La base humaine doit pouvoir être rapprochée de ce contrat, mais le chapitre ne prétend pas que l’auto-mapping ou la correction de silhouette remplace un rig propre.

## 29. Export de validation

L’export de test utilise glTF 2.0 dans un conteneur GLB, conformément au chapitre 4. Le fichier ne constitue pas une livraison finale.

> **[LECTURE] Contenu minimal de la collection d’export — Ne pas saisir.**

```text
EXPORT_HUMAN_BASE
├── HUMAN_BASE_BODY
├── HUMAN_BASE_HEAD
├── HUMAN_BASE_HAND_L
├── HUMAN_BASE_HAND_R
├── HUMAN_BASE_FOOT_L
├── HUMAN_BASE_FOOT_R
├── HUMAN_VALIDATION_ARMATURE   # provisoire, uniquement si créé pour les poses
└── HUMAN_VALIDATION_MARKERS
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** la collection limite ce qui entre dans le GLB et exclut guides, références et caches.
- **Réserve :** l’armature de validation n’est pas le rig final du chapitre 19.
- **Invariant :** chaque module garde son nom stable afin que la scène Godot puisse le retrouver.
- **Résultat attendu :** un export incomplet ou enrichi d’objets de travail est détectable immédiatement.

Avant export :

- appliquer rotation et échelle selon le contrat du chapitre 4 ;
- vérifier les normales ;
- vérifier l’origine au sol ;
- vérifier les matériaux ;
- vérifier les interfaces modulaires ;
- appliquer une triangulation déterministe dans l’export ou dans la chaîne qualifiée ;
- conserver la source quad dans Blender ;
- enregistrer le manifeste et l’empreinte de l’export.

## 30. Configurer l’import Godot

Dans l’import avancé de la scène 3D :

- conserver les normales et tangentes nécessaires ;
- importer les UV utilisées ;
- choisir quatre influences pour le chemin le plus compatible ou toutes les influences uniquement après qualification du renderer et du matériel ;
- activer la génération de LOD seulement pour un profil testé ;
- conserver ou désactiver la génération de shadow mesh selon la mesure ;
- définir le `BoneMap` uniquement lorsque le squelette existe ;
- ne pas corriger silencieusement une mauvaise échelle ou une mauvaise pose dans Godot sans corriger ou documenter la source.

L’option de génération de LOD peut réduire le coût à distance, mais tous les maillages n’en bénéficient pas. La décision appartient au profil de validation.

## 31. Créer la scène Godot de validation

> **[APP] Godot — Créer : `res://art/tests/humans/HumanBaseValidation.tscn`.**

> **[LECTURE] Arbre de scène attendu — Ne pas saisir.**

```text
HumanBaseValidation (Node3D)
├── WorldEnvironment
├── DirectionalLight3D
├── CameraRig (Node3D)
│   └── Camera3D
├── DistanceMarkers (Node3D)
├── NeutralPose (Node3D)
│   └── HumanBase
├── Pose45 (Node3D)
│   └── HumanBase
├── Pose90 (Node3D)
│   └── HumanBase
├── CrouchPose (Node3D)
│   └── HumanBase
├── SeatedPose (Node3D)
│   └── HumanBase
├── Turntable (Node3D)
├── DebugFloor (MeshInstance3D)
├── Label3D
└── HumanBaseValidation.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation :** chaque pose possède une instance séparée afin de comparer les silhouettes sans dépendre d’une animation.
- **Mesure :** `DistanceMarkers` matérialise les distances observées et `CameraRig` permet de tester plusieurs cadrages.
- **Invariant :** le sol et la lumière sont communs à toutes les variantes.
- **Résultat attendu :** les défauts de pose, de couture, d’échelle et de LOD deviennent comparables dans une scène stable.

La scène doit permettre :

- vue frontale, profil, dos et trois quarts ;
- changement de focale ou de champ de vision ;
- éclairage neutre, rasant et contrasté ;
- fond clair et fond sombre ;
- affichage des wireframes ou normales via matériau de debug ;
- comparaison des LOD ;
- capture des statistiques du moteur ;
- test d’au moins trois variantes morphologiques.

## 32. Script de contrôle statique de la scène

> **[VSC] Visual Studio Code — Créer : `res://art/tests/humans/HumanBaseValidation.gd` — Ne pas saisir.**

```gdscript
extends Node3D

const REQUIRED_VARIANTS: PackedStringArray = [
    "NeutralPose",
    "Pose45",
    "Pose90",
    "CrouchPose",
    "SeatedPose",
]

const REQUIRED_MESH_NAMES: PackedStringArray = [
    "HUMAN_BASE_BODY",
    "HUMAN_BASE_HEAD",
    "HUMAN_BASE_HAND_L",
    "HUMAN_BASE_HAND_R",
]

@export var expected_height_m: float = 1.72
@export_range(0.001, 0.20, 0.001) var height_tolerance_m: float = 0.02

func _ready() -> void:
    var failures := validate_scene_contract()
    if failures.is_empty():
        print("HUMAN_BASE_VALIDATION: scene contract ready")
        return

    for failure in failures:
        push_error(failure)

func validate_scene_contract() -> PackedStringArray:
    var failures := PackedStringArray()

    for variant_name in REQUIRED_VARIANTS:
        if get_node_or_null(NodePath(variant_name)) == null:
            failures.append("Missing pose container: %s" % variant_name)

    var neutral := get_node_or_null("NeutralPose/HumanBase")
    if neutral == null:
        failures.append("Missing NeutralPose/HumanBase")
        return failures

    for mesh_name in REQUIRED_MESH_NAMES:
        if neutral.find_child(mesh_name, true, false) == null:
            failures.append("Missing required mesh: %s" % mesh_name)

    var measured_height := _measure_visual_height(neutral)
    if measured_height <= 0.0:
        failures.append("Unable to measure a positive visual height")
    elif absf(measured_height - expected_height_m) > height_tolerance_m:
        failures.append(
            "Height %.3f m outside %.3f ± %.3f m"
            % [measured_height, expected_height_m, height_tolerance_m]
        )

    return failures

func _measure_visual_height(root: Node) -> float:
    var combined := AABB()
    var initialized := false

    for child in root.find_children("*", "MeshInstance3D", true, false):
        var mesh_instance := child as MeshInstance3D
        if mesh_instance.mesh == null:
            continue

        var local_aabb := mesh_instance.global_transform * mesh_instance.get_aabb()
        if initialized:
            combined = combined.merge(local_aabb)
        else:
            combined = local_aabb
            initialized = true

    return combined.size.y if initialized else 0.0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Constantes :** `REQUIRED_VARIANTS` décrit les conteneurs de poses ; `REQUIRED_MESH_NAMES` décrit les modules indispensables au test.
- **Paramètres :** `expected_height_m` et `height_tolerance_m` sont exposés dans l’inspecteur et utilisent les mètres du guide de proportions.
- **Valeur de retour :** `validate_scene_contract()` renvoie une `PackedStringArray`; une liste vide signifie uniquement que le contrat structurel minimal est satisfait.
- **Déroulement :** le script vérifie d’abord les poses, puis l’instance neutre, les modules et enfin la hauteur visuelle cumulée.
- **Effets de bord :** `_ready()` écrit dans la console et signale les refus avec `push_error`; il ne modifie pas l’asset.
- **Limite :** la mesure par AABB inclut tous les maillages visibles et ne remplace ni un contrôle anatomique, ni une mesure de performance, ni une revue de déformation.
- **Résultat attendu :** une scène incomplète ou une échelle incohérente produit des messages précis au lieu d’un échec silencieux.

## 33. Enregistrer les poses de validation

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-POSE-TESTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
test_set_id: AST-HUMAN-POSES-001
poses:
  neutral:
    required: true
    checks:
      - "symmetry"
      - "ground_contact"
      - "module_seams"
  arm_45:
    required: true
    checks:
      - "deltoid_volume"
      - "armpit_compression"
      - "scapula_transition"
  arm_90:
    required: true
    checks:
      - "shoulder_pinching"
      - "torso_stretch"
      - "wrist_alignment"
  crouch:
    required: true
    checks:
      - "hip_flexion"
      - "knee_compression"
      - "heel_contact"
  seated:
    required: true
    checks:
      - "glute_volume"
      - "thigh_torso_clearance"
      - "spine_balance"
  fist:
    required: true
    checks:
      - "finger_intersections"
      - "thumb_opposition"
      - "palm_volume"
acceptance:
  visible_self_intersections: 0
  broken_module_seams: 0
  collapsed_primary_silhouettes: 0
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tests :** chaque pose nomme les volumes et contacts à examiner ; le fichier n’encode pas une animation.
- **Acceptation :** les valeurs nulles rendent bloquantes les intersections visibles, coutures rompues et silhouettes principales effondrées.
- **Réserve :** `runtime_status` reste `not_executed` jusqu’à la création et la capture des poses.
- **Résultat attendu :** une revue peut enregistrer un résultat par pose au lieu d’un jugement global imprécis.

## 34. Mesurer les performances dans Godot

Les mesures sont réalisées avec :

- la même scène ;
- la même caméra ;
- la même résolution ;
- le même renderer ;
- le même éclairage ;
- le même nombre de personnages ;
- les mêmes animations ou poses ;
- une phase de stabilisation ;
- plusieurs répétitions ;
- les statistiques CPU, GPU, mémoire et rendu disponibles.

Scénarios minimaux :

1. un personnage LOD0 en gros plan ;
2. quatre personnages en jeu proche ;
3. vingt personnages en distance moyenne ;
4. cent silhouettes lointaines si le jeu le prévoit ;
5. variation du champ de vision ;
6. ombres activées puis désactivées ;
7. comparaison LOD importés et générés ;
8. comparaison de quatre et huit influences si les deux chemins sont qualifiés.

Aucune valeur ne doit être copiée depuis une autre machine comme seuil de réussite. Les résultats sont conservés avec le commit, le matériel, la version du moteur et les réglages.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/HUMAN-PERFORMANCE-RESULTS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
result_set_id: AST-HUMAN-PERF-001
status: "not_executed"
environment:
  godot_version: "4.7.1-stable"
  renderer: "Forward+"
  resolution: null
  gpu: "AMD Radeon RX 6750 XT 12GB"
  cpu: "Ryzen 7 2700"
  ram_gb: 32
asset:
  source_commit: null
  export_sha256: null
  topology_revision: 1
  lod_revision: 1
scenarios: []
decision:
  accepted_profiles: []
  rejected_profiles: []
  notes: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Absences explicites :** les champs `null` empêchent d’inventer une résolution, un commit ou une empreinte.
- **Traçabilité :** `topology_revision` et `lod_revision` relient les résultats à la géométrie réellement testée.
- **Décision :** les profils acceptés et rejetés sont séparés des mesures brutes.
- **Résultat attendu :** le fichier peut recevoir des mesures futures sans réécrire l’historique documentaire du chapitre.

## 35. Provenance et identifiants

La base humaine et chaque dépendance significative reçoivent une identité de provenance :

- `AST-ASSET-MESH-HUMANBASE-001` : base logique ;
- une version source `v001`, `v002`, etc. ;
- identifiants distincts pour références, textures, matériaux, modules et outils externes ;
- relation explicite entre variante et base ;
- relation explicite entre LOD et source ;
- empreinte de chaque export livré ;
- statut de publication conforme au chapitre 5.

Une référence anatomique autorisée pour consultation ne devient pas une texture. Une base achetée, scannée ou générée ne devient pas « interne originale » après retopologie.

## 36. Arborescence de travail

> **[LECTURE] Arborescence de référence — Ne pas saisir.**

```text
art/
├── blender/
│   ├── sources/
│   │   └── characters/
│   │       └── humans/
│   │           ├── AST-HUMAN-BASE-v001.blend
│   │           ├── modules/
│   │           ├── variants/
│   │           └── lod/
│   ├── work/
│   │   └── characters/humans/
│   ├── exports/
│   │   └── glb/characters/humans/
│   ├── delivery/
│   │   └── characters/humans/
│   ├── manifests/
│   │   ├── HUMAN-REFERENCE-SET.yaml
│   │   ├── HUMAN-PROPORTIONS.yaml
│   │   ├── HUMAN-MODULE-CONTRACT.yaml
│   │   ├── HUMAN-VARIANTS.yaml
│   │   ├── HUMAN-TOPOLOGY-POLICY.yaml
│   │   ├── HUMAN-LOD-BUDGETS.yaml
│   │   ├── HUMAN-POSE-TESTS.yaml
│   │   └── HUMAN-PERFORMANCE-RESULTS.yaml
│   └── tests/
│       └── humans/
└── provenance/
    └── assets/
        └── AST-ASSET-MESH-HUMANBASE-001.yaml
game/
└── art/
    └── tests/
        └── humans/
            ├── HumanBaseValidation.tscn
            └── HumanBaseValidation.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorités :** `sources/` conserve le maillage modifiable ; `exports/` contient les sorties générées ; `delivery/` contient uniquement les versions approuvées.
- **Séparation :** les manifestes restent lisibles sans ouvrir Blender ou Godot.
- **Dépendance :** la fiche de provenance est rangée sous la politique du chapitre 5.
- **Résultat attendu :** une reprise retrouve les sources, contrats, tests et livraisons sans explorer des dossiers personnels.

## 37. Parcours Mode Solo

Le parcours Solo limite volontairement les variantes :

1. une base humaine ;
2. trois morphotypes pilotes ;
3. une topologie commune ;
4. quatre modules principaux : corps, tête, deux mains ;
5. trois LOD réellement utiles avant d’en ajouter davantage ;
6. une seule UV de corps ;
7. une scène Godot de validation ;
8. un manifeste de résultats.

Priorités :

- corriger les articulations avant les détails ;
- tester les extrêmes avant d’ajouter des presets ;
- conserver un seul rig de référence futur ;
- refuser les modules non compatibles ;
- mesurer un petit groupe de personnages avant de promettre une foule.

Le parcours Solo n’utilise pas une bibliothèque de centaines de curseurs. Il privilégie des variantes clairement utiles au jeu.

## 38. Parcours Mode Studio

Le parcours Studio ajoute :

- propriétaire de la base ;
- propriétaires des modules ;
- revue anatomique et artistique distincte ;
- matrice de compatibilité ;
- bibliothèque de morphotypes ;
- tests automatiques des interfaces ;
- publication immuable des révisions ;
- branche de correction pour chaque changement de topologie ;
- validation par rigging, animation, vêtements et performance ;
- décision explicite lorsqu’une variante rompt la compatibilité.

Aucune équipe ne modifie la frontière du cou, du poignet ou de la cheville sans nouvelle révision du contrat et migration des dépendances.

## 39. Porte d’acceptation

Une base humaine est acceptée pour passer au chapitre 7 ou aux chapitres spécialisés lorsque :

- la provenance des références et de la source est documentée ;
- la source canonique est identifiable ;
- les proportions et tolérances sont enregistrées ;
- les modules respectent leurs interfaces ;
- la topologie est propre ;
- les poses prévues ne montrent pas de rupture majeure ;
- les variantes extrêmes restent compatibles ou sont déclarées incompatibles ;
- les UV et matériaux préparatoires sont nommés ;
- les budgets sont présents ;
- les LOD conservent la silhouette et les articulations ;
- l’export arrive à la bonne échelle et orientation ;
- la scène Godot de validation est complète ;
- les mesures futures ou réalisées sont distinguées ;
- les réserves sont visibles.

> **[LECTURE] Décision de revue — Ne pas saisir.**

```yaml
asset_id: AST-ASSET-MESH-HUMANBASE-001
source_version: v001
decision: blocked
reviews:
  provenance: pending
  anatomy: pending
  topology: pending
  modules: pending
  rig_compatibility: pending_chapter_19
  godot_import: not_executed
  performance: not_executed
blocking_reasons:
  - "Aucun asset pilote matérialisé."
  - "Aucune pose de validation exécutée."
  - "Aucune mesure Godot conservée."
next_allowed_action:
  - "Créer la source pilote dans Blender."
  - "Exécuter la batterie de poses."
  - "Importer le GLB dans la scène de validation."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Décision :** `blocked` est cohérent avec l’absence d’asset réel ; le chapitre documentaire ne crée pas une acceptation fictive.
- **Revues :** chaque spécialité possède son propre statut afin qu’une réussite visuelle ne masque pas une réserve de provenance ou de performance.
- **Frontière :** la compatibilité de rig reste en attente du chapitre 19.
- **Résultat attendu :** la prochaine action autorisée porte sur la matérialisation et les tests, pas sur la publication.

## 40. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 40.1 Utiliser une seule silhouette comme vérité universelle

**Symptôme :** toutes les variantes conservent les mêmes proportions et seuls les volumes sont gonflés ou réduits.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
variant:
  name: "strong"
  scale_xyz: [1.15, 1.15, 1.15]
  gameplay_strength_bonus: 25
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Une mise à l’échelle uniforme ne produit pas une morphologie crédible, et le nom visuel modifie en plus une statistique de gameplay sans contrat.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
variant:
  id: "MORPH-A03"
  parameters:
    stature: 1.78
    shoulder_scale: 1.08
    pelvis_scale: 1.01
    limb_length: 1.02
    muscle_volume: 0.62
  gameplay_effects: []
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

Les paramètres décrivent des dimensions visuelles indépendantes et n’inventent aucune capacité métier.

### 40.2 Appliquer la symétrie avant de valider les modules

**Symptôme :** les mains et la tête ne peuvent plus être remplacées sans couture.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
Mirror appliqué
→ frontière du poignet remodelée librement
→ ordre des sommets différent à gauche et à droite
→ export des mains séparées
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

L’application précoce du miroir puis le remodelage non contrôlé détruisent l’équivalence des interfaces.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
Mirror conservé pendant la construction
→ interface verrouillée par le manifeste
→ test du nombre et de l’ordre des sommets
→ application seulement dans la version publiée
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

Le contrat est vérifié avant la publication et les deux côtés restent reproductibles.

### 40.3 Placer un pôle dans le pli principal d’une articulation

**Symptôme :** l’aisselle ou l’intérieur du coude forme une étoile visible en flexion.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
Pôle à cinq arêtes
position = centre du pli du coude
test_pose = aucun
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Le pôle concentre les changements de direction précisément dans la zone de compression maximale.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
Pôle déplacé vers une zone plus stable
boucles = réparties autour de l’articulation
tests = [45°, 90°, 135°]
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

La courbure est distribuée et le pôle est évalué dans plusieurs poses.

### 40.4 Ajouter les détails avant de stabiliser les volumes

**Symptôme :** le maillage contient pores, plis et ongles, mais la silhouette et les articulations restent incorrectes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
sculpt_detail_level = pores
shoulder_pose_tests = 0
hip_pose_tests = 0
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Le détail augmente le coût de reprise sans résoudre les défauts qui déterminent le rig, les vêtements et la lisibilité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
ordre = volumes → proportions → topologie → poses → modules → UV → détail
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

Chaque niveau est validé avant d’ajouter des informations coûteuses à préserver.

### 40.5 Fusionner les modules sans contrat de frontière

**Symptôme :** chaque nouvelle tête demande une retopologie du cou.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
neck_interface:
  vertex_count: "approximately 30"
  order: "looks aligned"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Les valeurs approximatives ne sont ni testables, ni suffisantes pour partager normales, UV ou poids.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
neck_interface:
  vertex_count: 32
  vertex_order: "clockwise_from_spine_marker"
  topology_revision: 1
  normal_policy: "matched"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

L’interface devient déterministe et possède une révision compatible avec les dépendances.

### 40.6 Déclarer un budget mesuré sans scène réelle

**Symptôme :** le rapport annonce une fréquence d’image précise alors qu’aucun asset n’a été importé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
performance:
  characters: 100
  fps: 60
  status: passed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

La résolution, les matériaux, les poses, le matériel, la scène et les journaux sont absents ; la valeur est invérifiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
performance:
  status: not_executed
  target_characters: 100
  target_fps: 60
  measured_fps: null
  evidence: null
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

La cible reste utile tout en distinguant clairement l’hypothèse de la mesure.

### 40.7 Réduire un LOD en détruisant les articulations

**Symptôme :** le LOD distant est léger au repos mais s’effondre dès que le personnage marche.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
decimation_ratio = 0.10
protected_zones = []
pose_tests = []
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

La réduction ignore les zones de déformation et n’est testée que dans la pose neutre.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
protected_zones = [silhouette, shoulders, elbows, hips, knees, hands]
pose_tests = [walk_contact, walk_pass, crouch, arm_90]
acceptance = no_major_collapse
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

La réduction protège les informations visibles et reçoit les mêmes tests de pose que la base.

### 40.8 Corriger l’échelle uniquement dans Godot

**Symptôme :** le personnage paraît correct dans une scène, mais les animations, collisions et modules utilisent des échelles différentes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
$HumanBase.scale = Vector3(0.01, 0.01, 0.01)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Le nœud masque une source exportée à la mauvaise échelle et propage une transformation non documentée aux dépendances.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
corriger unités et transformations dans Blender
→ réexporter
→ vérifier une échelle (1, 1, 1) dans Godot
→ enregistrer la hauteur mesurée
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

La source et l’import partagent le même contrat et la scène n’a plus besoin d’une compensation cachée.

### 40.9 Associer une morphologie à une identité ou une capacité

**Symptôme :** un preset visuel impose automatiquement force, agilité, origine ou profession.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```json
{
  "body_preset": "elder",
  "intelligence": 18,
  "speed": 4,
  "occupation": "scholar"
}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Le preset mélange apparence, âge supposé, caractéristiques de gameplay et rôle narratif.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```json
{
  "morphology_profile_id": "MORPH-H12",
  "visual_parameters": {
    "stature": 1.68,
    "posture_profile": "P03",
    "muscle_volume": 0.22
  },
  "gameplay_definition_id": "CHAR-DEF-UNASSIGNED"
}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

L’apparence reste une référence d’asset et le système de gameplay conserve son propre identifiant.

### 40.10 Considérer l’auto-mapping comme une validation de rig

**Symptôme :** l’import ne signale pas d’os manquant, donc le personnage est déclaré prêt pour toutes les animations.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
bone_map:
  auto_mapped: true
validation:
  result: "all_animations_compatible"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

Un mapping de noms ne prouve ni la correspondance des rest poses, ni les axes, ni les longueurs d’os, ni les déformations.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
bone_map:
  auto_mapped: true
validation:
  rest_pose_review: pending
  hierarchy_review: pending
  deformation_tests: pending
  animation_set_tests: pending_chapter_20
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

L’outil accélère la préparation, mais chaque propriété nécessaire à la compatibilité reste explicitement à vérifier.

## 41. Checklist de validation

### 41.1 Références et conception

- [ ] les références ont une provenance et un usage documentés ;
- [ ] le guide de proportions utilise des mesures et tolérances explicites ;
- [ ] les variations couvrent plusieurs silhouettes utiles ;
- [ ] aucun preset ne déduit identité, valeur ou capacité ;
- [ ] la pose de construction est documentée.

### 41.2 Géométrie

- [ ] la surface est manifold ou les exceptions sont justifiées ;
- [ ] aucune face interne inutile ;
- [ ] aucune géométrie détachée ;
- [ ] normales cohérentes ;
- [ ] densité concentrée selon silhouette et déformation ;
- [ ] pôles hors des plis principaux ;
- [ ] épaules, coudes, hanches et genoux réussissent les poses prévues ;
- [ ] mains et pieds conservent leurs volumes fonctionnels.

### 41.3 Modules et variantes

- [ ] chaque interface possède nombre et ordre des sommets ;
- [ ] normales et UV sont compatibles ;
- [ ] chaque révision est versionnée ;
- [ ] les shape keys conservent la topologie ;
- [ ] les extrêmes morphologiques sont testés ;
- [ ] les incompatibilités sont bloquées, pas masquées.

### 41.4 Matériaux et LOD

- [ ] surfaces et matériaux temporaires sont nommés ;
- [ ] UV préparées et densité documentée ;
- [ ] budgets déclarés comme provisoires ou mesurés ;
- [ ] chaque LOD conserve la silhouette ;
- [ ] articulations testées après réduction ;
- [ ] seuils Godot observés dans la scène réelle ;
- [ ] différences entre LOD importés et générés enregistrées.

### 41.5 Godot et preuve

- [ ] export à l’échelle et orientation attendues ;
- [ ] modules présents sous leurs noms stables ;
- [ ] scène de poses complète ;
- [ ] éclairages et fonds de debug disponibles ;
- [ ] script structurel sans erreur ;
- [ ] mesures associées au matériel et au commit ;
- [ ] aucun résultat runtime inventé ;
- [ ] preuves et réserves conservées ;
- [ ] aucun PDF intermédiaire produit.

## 42. Livrables à conserver

Le chapitre produit les modèles permanents suivants :

1. `HUMAN-REFERENCE-SET.yaml` ;
2. `HUMAN-PROPORTIONS.yaml` ;
3. `HUMAN-MODULE-CONTRACT.yaml` ;
4. `HUMAN-VARIANTS.yaml` ;
5. `HUMAN-TOPOLOGY-POLICY.yaml` ;
6. `HUMAN-LOD-BUDGETS.yaml` ;
7. `HUMAN-POSE-TESTS.yaml` ;
8. `HUMAN-PERFORMANCE-RESULTS.yaml` ;
9. la source Blender `AST-HUMAN-BASE-v001.blend` lorsqu’elle sera matérialisée ;
10. la scène Godot `HumanBaseValidation.tscn` et son script lorsqu’ils seront matérialisés ;
11. la fiche de provenance et les empreintes des exports ;
12. le rapport de revue de la base humaine.

Ces modèles documentaires préparent les cinq livrables du plan maître :

- base humaine de référence ;
- variantes morphologiques ;
- guide de proportions ;
- budgets et profils LOD ;
- scène Godot de validation.

## 43. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient une base humaine modulaire, construite en A-pose détendue, mesurée en unités métriques et conservée dans une source Blender canonique. La topologie concentre sa densité sur les silhouettes, les articulations et les interfaces nécessaires aux futurs rigs, vêtements et LOD.

Les variantes morphologiques utilisent des paramètres visuels indépendants des statistiques de gameplay. Elles conservent la topologie et les interfaces lorsqu’elles doivent partager modules, UV ou shape keys ; toute rupture reçoit une révision incompatible explicite.

Les budgets restent provisoires tant qu’aucun asset réel n’a été mesuré dans Godot. La scène de validation doit comparer poses, silhouettes, éclairages, distances et profils LOD sur le matériel de référence. L’automatisation contrôle la structure et les valeurs mesurables, tandis que l’acceptation anatomique et artistique reste humaine.

Le visage détaillé, la peau, les yeux, les cheveux et la pilosité restent au chapitre 10 ; les vêtements au chapitre 11 ; le rig et le skinning au chapitre 19 ; les animations et le retargeting de production au chapitre 20. Le système métier des personnages demeure dans le Livre II.

## 44. Références officielles consultées

- Blender Manual `5.0` — données de maillage, modificateurs, groupes de sommets, shape keys, armatures et organisation des données ;
- Godot Engine documentation stable — import avancé des scènes 3D, génération de LOD, shadow meshes, `ImporterMesh`, `MeshInstance3D`, `Skeleton3D`, `SkeletonProfileHumanoid` et retargeting ;
- Khronos Group — spécification glTF `2.0.1`, maillages, skins et morph targets ;
- documentation interne du dépôt : chapitres 2 à 5 du Livre III, chapitre 14 du Livre II, protocole QA et plan maître du Livre III.
