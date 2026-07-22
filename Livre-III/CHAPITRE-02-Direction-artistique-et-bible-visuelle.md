---
title: "Livre III — Chapitre 2 : Direction artistique et bible visuelle"
id: "DOC-L3-CH02"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 2
last-verified: "2026-07-22T17:49:18+02:00"
audit-status: "complete"
audit-date: "2026-07-22T17:49:18+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-02.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"----

# Direction artistique et bible visuelle

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH02`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+
## 1. Rôle du chapitre

Le chapitre 1 a transformé la vision générale de `Project Asteria` en programme de production : familles d’assets, priorités, budgets initiaux, calendrier, risques et critères d’acceptation. Ce deuxième chapitre fixe maintenant le **langage visuel commun** qui permettra à des personnages, bâtiments, objets, interfaces et effets produits à des moments différents de paraître appartenir au même univers.

Une direction artistique n’est pas une collection d’images appréciées par l’équipe. Elle définit des décisions observables : formes dominantes, proportions, hiérarchie des détails, rapports de couleurs, comportements des matériaux, règles d’éclairage, densité visuelle, niveau de réalisme, lisibilité à différentes distances et écarts autorisés. La **bible visuelle** enregistre ces décisions, leurs exemples et leurs limites.

Le résultat attendu est un document assez précis pour guider une personne débutante, assez souple pour accepter des variantes culturelles et régionales, et assez vérifiable pour qu’une revue artistique ne se résume pas à « j’aime » ou « je n’aime pas ».

> **[LECTURE] Chaîne de décision artistique — Ne pas saisir.**

```text
Valeurs du projet
    ↓
Piliers artistiques observables
    ↓
Grammaire de formes, proportions, couleurs, matières et lumière
    ↓
Règles par famille d’assets
    ↓
Exemples conformes, limites et non conformes
    ↓
Assets pilotes dans une scène Godot commune
    ↓
Mesures, captures, revue et version suivante de la bible
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le flux transforme des intentions émotionnelles en règles vérifiables, puis confronte ces règles à des assets visibles dans le moteur.

- **Déroulement :** Chaque niveau dépend du précédent : une palette n’est pas choisie isolément, elle traduit des piliers et sert des fonctions de lecture.

- **Boucle de révision :** Les captures et mesures réalisées dans Godot peuvent invalider une règle qui fonctionnait seulement dans un logiciel d’image ou sur une illustration statique.

- **Invariant :** La bible enregistre une décision et ses raisons ; elle ne remplace ni le jugement humain ni les contraintes techniques propres à chaque asset.

- **Résultat attendu :** Une personne qui n’a pas participé aux premières discussions peut appliquer les règles et expliquer pourquoi un résultat est conforme, limite ou non conforme.

## 2. Prérequis, outils et fichiers de travail

Le lecteur doit avoir terminé le chapitre 1 et disposer de son cahier des charges, de la matrice des assets et de la liste des assets pilotes. Il doit aussi connaître la configuration de référence : Windows 11, Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Godot `4.7.1-stable` en Forward+.

Aucune version de Blender n’est imposée ici. Le chapitre décrit des contrats de direction artistique indépendants du DCC. Les concepts et références produits au chapitre 3, puis les sources Blender du chapitre 4, devront respecter cette bible.

Préparer les chemins suivants dans l’organisation cible de `Project Asteria` :

- `docs/art/VISUAL-BIBLE.md` : document principal ;
- `docs/art/VISUAL-DECISIONS.yaml` : décisions structurées et identifiants ;
- `docs/art/palettes/` : palettes versionnées ;
- `docs/art/materials/` : fiches de familles de matériaux ;
- `docs/art/lighting/` : profils d’éclairage et captures ;
- `docs/art/review/ART-REVIEW-GRID.md` : grille de revue ;
- `docs/art/exceptions/` : dérogations approuvées ;
- `scenes/validation/art_direction/` : scène Godot de comparaison ;
- `captures/art_direction/` : sorties de revue non autoritaires.

Ces chemins décrivent des livrables cibles. Ils ne prouvent pas que le Starter Kit ou la scène Godot existent déjà.

> **[VSC] Visual Studio Code — Créer : `docs/art/VISUAL-BIBLE.md` — Ne pas saisir.**

```markdown
# Bible visuelle — Project Asteria

- Version : 1.0.0
- Périmètre : vertical slice
- Propriétaire : art-direction-owner
- Référence moteur : Godot 4.7.1-stable, Forward+
- Plateforme de revue : Windows 11, RX 6750 XT 12 Go
- Statut : brouillon de validation
- Date de prochaine revue : 2026-08-12

## Piliers
1. ...
2. ...
3. ...

## Règles obligatoires
- ...

## Variations autorisées
- ...

## Cas non conformes
- ...
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le fichier centralise les règles destinées aux producteurs d’assets sans mélanger les preuves internes de QA du livre.

- **Métadonnées importantes :** La version, le périmètre, le propriétaire, le moteur et la plateforme indiquent quelle décision s’applique et dans quel contexte elle a été observée.

- **Statut :** `brouillon de validation` indique que les règles doivent encore être éprouvées sur les assets pilotes ; il ne constitue pas un état runtime du jeu.

- **Structure :** Les piliers expliquent l’intention, les règles obligatoires réduisent l’ambiguïté, les variations préservent la diversité et les cas non conformes montrent les limites.

- **Résultat attendu :** Une revue peut citer une section précise de la bible plutôt que dépendre d’une préférence orale non versionnée.

## 3. Distinguer vision, direction artistique et bible visuelle

La **vision** exprime l’expérience globale recherchée : exploration d’un monde ancien, tensions entre sociétés, nature active, technologie rare ou mémoire fragmentée. Elle donne un cap mais ne suffit pas à décider la forme d’une porte, la saturation d’un avertissement ou la densité d’un costume.

La **direction artistique** choisit comment cette vision devient perceptible : silhouettes, rythmes, contrastes, matériaux, cadrages, motifs, lumière et degré de simplification.

La **bible visuelle** est le contrat versionné qui rend cette direction transmissible. Elle contient des règles, des exemples, des mesures et des exceptions. Elle n’est jamais figée par principe, mais toute modification importante doit être justifiée et versionnée.

> **[LECTURE] Différences entre les trois niveaux — Ne pas saisir.**

```yaml
visual_system:
  vision:
    statement: "un monde vivant construit sur les traces de civilisations disparues"
    horizon: "collection et jeu complet"
  art_direction:
    statement: "opposer des masses naturelles souples à des structures humaines angulaires"
    horizon: "langage visuel du projet"
  visual_bible:
    rule_id: "shape.contrast.nature_civilization"
    requirement: "les environnements naturels dominent par des courbes et ruptures irrégulières"
    exception_process: "dérogation versionnée avec capture dans Godot"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La structure sépare le sens général, le choix esthétique et la règle applicable.

- **Champs et types :** Chaque niveau possède une chaîne `statement`; la règle ajoute un identifiant stable, une exigence et un processus d’exception.

- **Horizon :** La vision traverse toute la collection, la direction concerne le langage commun et la bible décrit les décisions actuellement applicables.

- **Invariant :** Une phrase de vision ne doit pas être utilisée comme critère direct de validation d’un asset sans règle intermédiaire observable.

- **Résultat attendu :** Une demande de correction peut viser `shape.contrast.nature_civilization` au lieu de demander vaguement de rendre un bâtiment « plus Asteria ».

## 4. Définir des piliers artistiques observables

Un pilier artistique associe une valeur perceptuelle à des signes observables. Les adjectifs seuls — « réaliste », « épique », « sombre », « organique » — sont insuffisants car deux personnes peuvent leur donner des significations opposées.

Pour le vertical slice, retenir trois à cinq piliers. Au-delà, les arbitrages deviennent difficiles. Chaque pilier doit contenir :

- une intention ;
- des manifestations attendues ;
- des signes à éviter ;
- les familles d’assets concernées ;
- un exemple de conflit avec un autre pilier ;
- une règle de priorité.

> **[VSC] Visual Studio Code — Ajouter à : `docs/art/VISUAL-DECISIONS.yaml` — Ne pas saisir.**

```yaml
pillars:
  - id: "pillar.traces_and_repair"
    intention: "montrer que le monde conserve les conséquences du temps"
    expected_signs:
      - "réparations lisibles mais fonctionnelles"
      - "patines orientées par l’usage"
      - "matériaux anciens associés à des ajouts récents"
    avoid:
      - "salissure uniforme"
      - "dégâts décoratifs sans cause"
    applies_to:
      - "architecture"
      - "props"
      - "characters"
    priority: 90

  - id: "pillar.readable_complexity"
    intention: "conserver une lecture immédiate malgré une richesse de détails"
    expected_signs:
      - "silhouette identifiable avant le détail"
      - "zones de repos entre groupes de détails"
      - "contraste réservé aux informations importantes"
    avoid:
      - "microdétail homogène"
      - "contraste maximal partout"
    priority: 100
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les piliers deviennent des entrées identifiables et comparables plutôt que des slogans.

- **Types importants :** `expected_signs`, `avoid` et `applies_to` sont des listes ; `priority` est un entier utilisé uniquement pour arbitrer les conflits de direction.

- **Priorité :** La valeur ne mesure pas la qualité d’un pilier. Elle indique lequel doit l’emporter lorsqu’un choix ne peut satisfaire deux intentions simultanément.

- **Effet sur la revue :** Un asset peut être corrigé en citant un signe attendu manquant ou un comportement explicitement interdit.

- **Limite :** Les priorités proposées appartiennent au vertical slice et restent à confirmer par les assets pilotes.

## 5. Construire un vocabulaire avec des oppositions

Une direction devient plus claire lorsque chaque terme est placé entre deux extrêmes. `Réaliste` peut par exemple signifier anatomie crédible, matériaux physiquement plausibles, proportions mesurées ou absence de stylisation. Il faut préciser quelles dimensions sont concernées.

Créer des axes avec :

- un extrême gauche ;
- un extrême droit ;
- une position cible ;
- une tolérance ;
- les familles concernées ;
- un exemple conforme ;
- un exemple qui dépasse la tolérance.

> **[LECTURE] Axes de positionnement — Ne pas saisir.**

```yaml
style_axes:
  realism:
    left: "symbolique"
    right: "photographique"
    target: 0.72
    tolerance: 0.10
    applies_to: ["characters", "materials", "lighting"]

  detail_density:
    left: "grandes masses calmes"
    right: "microdétail continu"
    target: 0.38
    tolerance: 0.12
    applies_to: ["architecture", "props", "costumes"]

  color_expression:
    left: "neutre et documentaire"
    right: "symbolique et saturé"
    target: 0.46
    tolerance: 0.15
    applies_to: ["world", "ui", "vfx"]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les axes rendent explicite une position relative sans prétendre mesurer mathématiquement une impression artistique.

- **Valeurs numériques :** Les nombres entre `0.0` et `1.0` servent de repères de discussion ; ils ne constituent ni une mesure scientifique ni une propriété à importer dans le jeu.

- **Tolérance :** Elle rappelle qu’une famille ou une scène peut varier sans quitter le langage commun.

- **Dépendance :** Un exemple visuel annoté doit accompagner chaque axe avant qu’il soit utilisé comme porte de validation.

- **Résultat attendu :** Deux réviseurs peuvent expliquer si un écart est volontaire, toléré ou incompatible avec la cible.

## 6. Hiérarchiser la grammaire visuelle

La bible doit distinguer trois niveaux :

1. **universel** : règles communes à tout `Project Asteria` ;
2. **famille** : règles spécifiques aux personnages, environnements, UI, VFX ou objets ;
3. **instance** : choix propre à un asset ou une scène.

Une règle universelle ne doit pas imposer un détail qui n’a de sens que pour une famille. Inversement, une règle d’instance ne doit pas être utilisée pour justifier une incohérence globale.

> **[LECTURE] Héritage des règles visuelles — Ne pas saisir.**

```text
Bible universelle
├── Personnages
│   ├── humains
│   ├── humanoïdes
│   └── créatures
├── Environnements
│   ├── nature
│   ├── architecture ancienne
│   └── installations récentes
├── Objets et équipements
├── Interface
└── Effets visuels

Chaque asset
  = règles universelles
  + règles de sa famille
  + décision d’instance documentée
  + éventuelle dérogation approuvée
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’arbre montre comment une décision se spécialise sans recopier toute la bible dans chaque fiche d’asset.

- **Héritage :** Une règle de famille complète les règles universelles ; elle ne les annule que si une dérogation explicite le permet.

- **Décision d’instance :** Elle décrit un besoin local, comme une cicatrice, un matériau rare ou une silhouette de boss.

- **Invariant :** L’absence de règle spécifique ne supprime pas les contraintes universelles.

- **Résultat attendu :** La provenance d’une décision visuelle reste traçable depuis l’asset jusqu’au pilier qui la justifie.

## 7. Langage des formes et lecture des silhouettes

La silhouette est la première information disponible à distance. Elle doit distinguer une fonction ou une famille avant que les textures, couleurs et petits accessoires soient visibles.

Définir :

- formes dominantes ;
- formes secondaires ;
- rapports pleins/vides ;
- centre de gravité apparent ;
- symétrie ou asymétrie ;
- rythme des répétitions ;
- zones protégées du microdétail ;
- éléments de signature.

Dans `Project Asteria`, l’hypothèse de travail oppose les structures humaines ou institutionnelles plus angulaires aux formes naturelles plus souples et irrégulières. Cette hypothèse doit être éprouvée plutôt que considérée comme vérité définitive.

> **[VSC] Visual Studio Code — Créer : `docs/art/SHAPE-LANGUAGE.yaml` — Ne pas saisir.**

```yaml
shape_families:
  natural:
    primary: ["curve", "broken_curve", "irregular_mass"]
    rhythm: "non_uniform"
    symmetry: "rare"
    protected_negative_space: true

  institutional:
    primary: ["rectangle", "vertical_axis", "repeated_module"]
    rhythm: "controlled"
    symmetry: "frequent"
    protected_negative_space: true

  improvised:
    primary: ["offset_rectangle", "brace", "patch"]
    rhythm: "functional_irregularity"
    symmetry: "conditional"
    protected_negative_space: true

silhouette_tests:
  distances_m: [2, 10, 25, 50]
  backgrounds: ["light", "mid", "dark", "busy"]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le fichier associe des familles de formes à des tests de silhouette reproductibles.

- **Champs importants :** `primary` liste les masses dominantes ; `rhythm` décrit la répétition ; `symmetry` indique une tendance, pas une obligation absolue.

- **Espace négatif :** Les vides protégés empêchent qu’un asset devienne une masse indistincte lorsque ses détails se réduisent.

- **Distances :** Les valeurs sont des hypothèses de capture pour le vertical slice ; elles devront être adaptées à la caméra et à l’échelle réelles.

- **Limite :** Un objet naturel peut contenir des formes angulaires et une institution des courbes. La classification décrit une dominante, pas une interdiction géométrique.

## 8. Échelles, proportions et relations de taille

Une bible visuelle doit conserver la cohérence d’échelle entre personnages, portes, armes, végétation, mobilier et effets. La mesure métrique appartient au pipeline de production, mais la direction artistique fixe aussi des **rapports perceptuels** : hauteur d’une porte par rapport au personnage, largeur d’un outil, volume apparent d’une armure, taille d’un signal de danger.

Conserver une planche d’échelle avec :

- personnage humain de référence ;
- personnage extrême autorisé ;
- animal ou créature pilote ;
- porte, marche et garde-corps ;
- prop héroïque ;
- module architectural ;
- repères de caméra.

> **[LECTURE] Planche d’échelle structurée — Ne pas saisir.**

```yaml
scale_board:
  unit: "meter"
  reference_subject:
    id: "scale.human.reference"
    height: 1.75
  anchors:
    - id: "scale.door.common"
      height: 2.10
      purpose: "passage humain courant"
    - id: "scale.beacon.hero"
      height: 3.80
      purpose: "repère de zone visible au-dessus du personnage"
    - id: "scale.creature.secondary"
      shoulder_height: 0.95
      purpose: "lecture immédiate sans dominer la balise"
  capture_cameras:
    - "eye_level"
    - "gameplay_default"
    - "top_down_review"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La planche relie dimensions métriques, fonction perceptuelle et angles de validation.

- **Types et unités :** Les hauteurs sont des nombres en mètres ; `purpose` reste une chaîne expliquant pourquoi la dimension existe.

- **Référence :** Le sujet de `1.75` m sert d’hypothèse de comparaison, pas de norme imposée à tous les personnages.

- **Caméras :** Plusieurs vues empêchent de valider une proportion uniquement depuis un cadrage avantageux.

- **Résultat attendu :** Une variation de taille peut être discutée par rapport à sa fonction, et non corrigée au hasard après l’import.

## 9. Composition, hiérarchie et zones de repos

Une image jouable contient plus d’informations qu’une illustration : objectif, danger, interaction, mouvement, terrain et interface. La direction artistique doit hiérarchiser ces informations.

Utiliser trois niveaux :

- **focal** : information prioritaire au moment considéré ;
- **support** : éléments qui renforcent le contexte ;
- **repos** : zones de faible contraste et faible densité qui laissent respirer l’image.

Le détail, la saturation, la netteté et le contraste ne doivent pas être maximisés partout. Lorsqu’ils sont uniformes, aucun élément ne domine réellement.

> **[LECTURE] Carte de hiérarchie visuelle — Ne pas saisir.**

```yaml
visual_hierarchy:
  focal:
    max_simultaneous_targets: 2
    allowed_tools:
      - "contrast"
      - "motion"
      - "framing"
      - "local_saturation"
  support:
    purpose: "expliquer l’espace sans rivaliser avec la cible"
  rest:
    minimum_screen_share_hypothesis: 0.25
    properties:
      - "low_detail_density"
      - "limited_value_range"
      - "slow_visual_rhythm"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La carte répartit les moyens de mise en valeur afin d’éviter une concurrence générale.

- **Hypothèse chiffrée :** La part de `0.25` est un point de départ pour les captures du vertical slice, pas une règle universelle de composition.

- **Outils focaux :** Le contraste et la saturation ne sont que deux moyens parmi d’autres ; le mouvement ou le cadrage peuvent suffire.

- **Invariant :** Une zone de repos n’est pas vide de sens. Elle protège la lecture des éléments prioritaires.

- **Vérification :** Les captures en niveaux de gris, en flou et à petite taille doivent encore révéler la hiérarchie principale.

## 10. Distance de lecture et niveaux d’information

Un asset change de fonction perceptuelle avec la distance. À cinquante mètres, sa silhouette et sa valeur globale dominent. À dix mètres, les masses secondaires et les matériaux deviennent lisibles. À deux mètres, les traces d’usage et détails fins peuvent apparaître.

Définir pour chaque asset pilote :

- information lisible de loin ;
- information lisible à moyenne distance ;
- information de proximité ;
- détail qui peut disparaître sans perdre la fonction ;
- détail qui doit être porté par une autre modalité si la couleur ou la texture ne suffit pas.

> **[VSC] Visual Studio Code — Ajouter à la fiche d’asset pilote — Ne pas saisir.**

```yaml
readability_layers:
  far:
    distance_m: 50
    must_read:
      - "asset_family"
      - "major_orientation"
  medium:
    distance_m: 15
    must_read:
      - "functional_state"
      - "main_material_family"
  close:
    distance_m: 2
    must_read:
      - "repair_history"
      - "surface_wear"
  optional_details:
    - "micro_scratches"
    - "small_fasteners"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La structure lie chaque groupe de détails à une distance et à une fonction.

- **Données importantes :** `distance_m` exprime une hypothèse en mètres ; `must_read` liste des informations, pas des techniques de modélisation.

- **Hiérarchie :** Les détails optionnels ne doivent pas recevoir plus de budget que les informations obligatoires.

- **Dépendance :** Les distances réelles devront être confirmées avec la caméra du jeu, le champ de vision et la résolution cible.

- **Résultat attendu :** Un LOD ou une réduction de texture peut être évalué par ce qu’il préserve, pas seulement par sa proximité visuelle avec la source.

## 11. Construire les palettes par fonction

Une palette utile ne se limite pas à une rangée de couleurs harmonieuses. Elle attribue des rôles : fond, surface, accent, danger, interaction, sélection, information, succès, neutralité et indisponibilité.

Séparer :

- palette **monde** ;
- palette **interface** ;
- palette **VFX** ;
- variations régionales ou culturelles ;
- couleurs fonctionnelles réservées.

Une couleur réservée ne doit pas être réutilisée comme décoration dominante si elle porte une information importante.

> **[VSC] Visual Studio Code — Créer : `docs/art/palettes/PALETTE-TOKENS.yaml` — Ne pas saisir.**

```yaml
palette:
  world:
    foundation:
      stone_cool: "#59636A"
      soil_dark: "#2E2A25"
      vegetation_muted: "#5D6B4E"
    accents:
      repair_copper: "#A56B45"
      memory_cyan: "#4EA6B2"

  functional:
    danger: "#D94A3A"
    interaction: "#E0B84F"
    selected: "#63B7FF"
    unavailable: "#777C82"

  rules:
    - "danger_never_decorative_dominant"
    - "interaction_requires_shape_or_motion_backup"
    - "unavailable_requires_value_and_pattern_change"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les tokens donnent un nom fonctionnel stable à une couleur, tandis que la valeur hexadécimale peut évoluer par version.

- **Structure :** `world` décrit l’ambiance générale ; `functional` réserve les signaux ; `rules` enregistre les interdictions ou alternatives.

- **Identité :** Le nom du token est plus stable que sa valeur. Les fichiers consommateurs ne devraient pas copier les valeurs dans plusieurs endroits.

- **Accessibilité :** Les règles imposent une redondance par forme, mouvement, motif ou valeur lorsque la couleur porte une information.

- **Limite :** Les codes proposés sont des hypothèses de bible ; leur contraste et leur rendu réel doivent être testés dans Godot.

## 12. Valeur, saturation et température

La teinte n’est qu’une dimension. Une palette doit également contrôler :

- **valeur** : clarté ou obscurité ;
- **saturation** : intensité chromatique ;
- **température relative** : impression chaude ou froide ;
- **distribution** : proportion de chaque rôle dans l’image.

Deux couleurs différentes mais de valeur proche peuvent devenir indiscernables en niveaux de gris. À l’inverse, une couleur très saturée attire l’attention même si elle n’est pas plus claire.

> **[LECTURE] Budget de couleur par image de jeu — Ne pas saisir.**

```yaml
color_distribution_hypothesis:
  neutral_and_low_saturation: 0.70
  regional_color: 0.20
  functional_accents: 0.08
  exceptional_high_saturation: 0.02

checks:
  - "grayscale_hierarchy"
  - "small_thumbnail"
  - "busy_background"
  - "desaturation_simulation"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le budget propose une distribution d’attention plutôt qu’une recette fixe de teintes.

- **Somme :** Les quatre proportions totalisent `1.0`; cette cohérence facilite une comparaison entre captures.

- **Accent exceptionnel :** La faible part de saturation maximale protège son pouvoir de signal.

- **Contrôles :** Les quatre vérifications révèlent des dépendances excessives à la couleur ou à la taille de l’image.

- **Limite :** Les ratios sont des hypothèses du vertical slice et peuvent varier selon une scène, une cinématique ou un écran d’interface.

## 13. Contraste et information non portée par la couleur seule

La bible doit interdire qu’une information essentielle soit transmise uniquement par une différence de teinte. Un danger, un objectif, une sélection ou un état indisponible doit aussi varier par au moins un autre canal :

- forme ;
- icône ;
- motif ;
- contour ;
- animation ;
- position ;
- texte ;
- son ou retour haptique, lorsque le système le permet.

Pour les textes et composants d’interface, utiliser les critères de contraste comme porte minimale, puis tester réellement les écrans dans Godot. Les ratios ne garantissent pas à eux seuls une bonne hiérarchie ou une lecture confortable.

> **[LECTURE] Matrice des signaux fonctionnels — Ne pas saisir.**

```markdown
| Fonction | Couleur | Forme | Motif ou animation | Texte |
|---|---|---|---|---|
| Danger | rouge-orangé | triangle | pulsation courte | DANGER |
| Interaction | jaune doré | cercle ouvert | apparition douce | Interagir |
| Sélection | bleu clair | contour double | maintien stable | nom de la cible |
| Indisponible | gris | icône barrée | aucune pulsation | raison du refus |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La matrice impose plusieurs canaux perceptuels pour chaque signal important.

- **Colonnes :** Chaque colonne décrit une modalité indépendante ; une cellule vide doit être justifiée si les autres canaux suffisent.

- **Différence fonctionnelle :** L’absence d’animation pour un élément indisponible évite de lui donner une priorité comparable à une action possible.

- **Limite :** Les mots, formes et couleurs proposés doivent être localisés, testés et adaptés à l’interface réelle.

- **Résultat attendu :** Une capture désaturée ou une déficience de perception des couleurs simulée conserve la distinction des quatre fonctions.

## 14. Gérer l’espace colorimétrique et les captures de référence

Une couleur affichée dépend de la chaîne complète : source, profil, texture, éclairage, correspondance tonale, post-traitement, écran et capture. La bible ne doit donc pas traiter une valeur hexadécimale comme une apparence universelle.

Pour la revue :

- conserver les sources dans un espace documenté ;
- distinguer texture de couleur, donnée technique et masque ;
- utiliser une scène Godot de référence ;
- enregistrer le tonemapper et l’exposition ;
- éviter de comparer deux captures produites avec des environnements différents ;
- conserver une capture non étalonnée en plus des versions de présentation.

> **[VSC] Visual Studio Code — Créer : `docs/art/CAPTURE-PROFILE.yaml` — Ne pas saisir.**

```yaml
capture_profile:
  id: "capture.art_direction.v1"
  engine: "Godot 4.7.1-stable"
  renderer: "Forward+"
  viewport:
    width: 1920
    height: 1080
  environment:
    profile: "env.art_direction.neutral"
    tonemap: "AgX"
    exposure: 1.0
    adjustments_enabled: false
  camera:
    fov_degrees: 70.0
  output:
    format: "png"
    include_ui: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le profil rend deux captures comparables en enregistrant moteur, rendu, environnement, caméra et sortie.

- **Types et unités :** La résolution utilise des entiers en pixels ; l’exposition et le champ de vision sont des nombres ; les identifiants restent des chaînes stables.

- **Choix du tonemapper :** `AgX` est une hypothèse de validation à exercer dans la version de Godot ciblée ; la bible doit enregistrer le mode réellement utilisé.

- **Invariant :** Une modification d’environnement ou de caméra exige une nouvelle version du profil au lieu d’écraser silencieusement la référence.

- **Limite :** Ce profil ne calibre pas physiquement l’écran et ne prouve pas une correspondance colorimétrique entre machines.

## 15. Langage des matériaux

La direction artistique fixe la lecture des matériaux avant leur implémentation détaillée au chapitre 16. Elle doit décrire :

- familles de surfaces ;
- réponse diffuse ou spéculaire attendue ;
- rugosité relative ;
- vieillissement ;
- réparations ;
- accumulation de poussière ou d’humidité ;
- échelle des motifs ;
- limites de variation.

Éviter les prescriptions universelles de valeurs PBR sans mesure. La bible décrit d’abord des **relations** : un métal poli doit être plus lisse qu’un métal oxydé ; une réparation récente doit se distinguer d’une base ancienne ; une surface manipulée s’use différemment d’une zone protégée.

> **[VSC] Visual Studio Code — Créer : `docs/art/materials/MATERIAL-FAMILIES.yaml` — Ne pas saisir.**

```yaml
material_families:
  ancient_stone:
    visual_read: "masse froide, poreuse, stratifiée"
    roughness_relation: "higher_than_repair_metal"
    wear_logic:
      - "edges_softened_by_contact"
      - "water_marks_follow_gravity"
      - "protected_recesses_keep_darker_deposits"

  repair_metal:
    visual_read: "ajout fonctionnel plus récent"
    roughness_relation: "lower_than_ancient_stone"
    wear_logic:
      - "contact_polish_near_handles"
      - "oxidation_near_joints"
      - "fasteners_remain_structurally_readable"

  living_fiber:
    visual_read: "matière souple, directionnelle, sensible à l’humidité"
    roughness_relation: "varies_with_wetness"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les familles décrivent une lecture et une logique d’usure avant de fixer des textures ou shaders.

- **Relations :** `roughness_relation` compare des familles ; cette approche reste utile lorsque les valeurs numériques sont encore inconnues.

- **Causalité :** Les marques suivent le contact, la gravité, l’eau ou les assemblages. Elles ne sont pas distribuées uniformément pour créer artificiellement du détail.

- **Frontière :** Le chapitre 16 définira les cartes PBR, résolutions, compression et réglages précis.

- **Résultat attendu :** Un matériau peut être rejeté parce que son vieillissement contredit sa fonction, même s’il est techniquement bien exécuté.

## 16. Usure, patine et histoire visible

L’usure raconte l’usage d’un objet. Elle doit répondre à quatre questions :

1. quelle action a produit la marque ;
2. où cette action se répète ;
3. quel matériau réagit ;
4. depuis combien de temps la marque existe.

Définir des couches d’histoire :

- fabrication initiale ;
- usage normal ;
- dommage exceptionnel ;
- réparation ;
- entretien récent ;
- exposition au climat.

> **[LECTURE] Chronologie d’une surface — Ne pas saisir.**

```yaml
surface_history:
  asset_id: "prop.beacon.ancient_01"
  layers:
    - stage: "original_construction"
      signs: ["cut_stone", "deep_engraving"]
    - stage: "long_exposure"
      signs: ["edge_softening", "mineral_streaks"]
    - stage: "failure"
      signs: ["fracture_on_load_path"]
    - stage: "recent_repair"
      signs: ["copper_brace", "fresh_fasteners"]
    - stage: "current_use"
      signs: ["polished_handle", "clean_access_panel"]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La chronologie empêche de mélanger des marques incompatibles dans une texture décorative sans cause.

- **Ordre :** La liste est chronologique ; une réparation doit recouvrir ou interrompre certains signes plus anciens.

- **Dépendance physique :** La fracture doit suivre un chemin de charge plausible et la zone manipulée doit montrer un contact répétitif.

- **Effet narratif :** Les couches visuelles suggèrent l’histoire sans imposer une vérité narrative au système de quêtes du Livre II.

- **Résultat attendu :** Une revue peut distinguer une patine intentionnelle d’un bruit visuel généralisé.

## 17. Définir la grammaire de lumière

La lumière guide la lecture, révèle les matériaux et établit une ambiance. La bible fixe :

- direction dominante ;
- dureté relative ;
- rapport entre sujet et fond ;
- usage des couleurs de lumière ;
- comportement des intérieurs et extérieurs ;
- traitement des zones dangereuses ;
- limites du brouillard, du glow et de l’exposition automatique.

Godot applique l’environnement, l’éclairage ambiant, la correspondance tonale et les ajustements au rendu final. Une modification de ciel peut aussi changer l’éclairage ambiant et réfléchi, même lorsque le ciel n’est pas directement visible.

> **[VSC] Visual Studio Code — Créer : `docs/art/lighting/LIGHTING-PROFILES.yaml` — Ne pas saisir.**

```yaml
lighting_profiles:
  neutral_review:
    id: "env.art_direction.neutral"
    purpose: "comparer formes, valeurs et matériaux"
    key_light:
      direction: "front_side_45"
      softness: "medium"
      color_role: "neutral_warm"
    fill:
      source: "environment"
      strength_relation: "lower_than_key"
    background:
      value_role: "mid"
    post_processing:
      glow: false
      auto_exposure: false

  gameplay_overcast:
    id: "env.gameplay.overcast"
    purpose: "vérifier la lisibilité dans une ambiance froide diffuse"
    key_light:
      direction: "top_side"
      softness: "high"
      color_role: "cool_neutral"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les profils séparent un environnement de diagnostic neutre d’une ambiance de gameplay.

- **Relations :** La force du remplissage est décrite relativement à la lumière principale tant qu’aucune mesure réelle n’est enregistrée.

- **Post-traitement :** Glow et exposition automatique sont désactivés dans la revue neutre afin de ne pas masquer les valeurs propres de l’asset.

- **Identité :** Chaque profil possède un identifiant stable qui doit être cité par les captures et rapports de comparaison.

- **Limite :** Les paramètres Godot précis restent à matérialiser et à vérifier sur le matériel de référence.

## 18. Correspondance tonale, exposition et post-traitement

La correspondance tonale transforme les valeurs lumineuses avant l’affichage. Elle influence le contraste, les hautes lumières et la saturation. La bible doit donc enregistrer le mode choisi pour chaque profil de revue.

Règles initiales :

- ne pas utiliser le post-traitement pour sauver un matériau mal équilibré ;
- conserver un profil neutre avec ajustements désactivés ;
- comparer au moins une ambiance claire et une ambiance sombre ;
- vérifier les hautes lumières saturées ;
- documenter tout changement d’exposition ;
- éviter l’exposition automatique si elle ne sert pas réellement le gameplay et complique les comparaisons.

> **[LECTURE] Contrat d’environnement Godot — Ne pas saisir.**

```yaml
godot_environment_contract:
  neutral_review:
    world_environment_scene: "res://scenes/validation/art_direction/world_environment_neutral.tscn"
    tonemap_mode: "AgX"
    exposure: 1.0
    adjustment_enabled: false
    auto_exposure_enabled: false
    glow_enabled: false

  stress_bright:
    purpose: "détecter clipping et perte de teinte"
    exposure_variant: "higher_than_neutral"

  stress_dark:
    purpose: "détecter perte de silhouette et valeurs bouchées"
    exposure_variant: "lower_than_neutral"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le contrat relie une scène Godot à un profil de revue et à deux cas de stress.

- **Chemin :** Le fichier `.tscn` est une cible du futur Starter Kit ; il n’est pas déclaré matérialisé dans ce chapitre.

- **Valeurs :** `1.0` sert de point de départ documenté. Les variantes claire et sombre restent relatives tant qu’aucune scène n’a été exécutée.

- **Précondition :** Tous les assets comparés doivent utiliser le même profil, la même caméra et les mêmes réglages de rendu.

- **Résultat attendu :** Les défauts révélés par une ambiance ne disparaissent pas dans une capture sélectionnée uniquement pour flatter l’asset.

## 19. Profondeur, brouillard et perspective atmosphérique

La profondeur peut être renforcée par :

- diminution progressive du contraste ;
- réduction de saturation ;
- changement de température ;
- brouillard ;
- chevauchement de plans ;
- échelle ;
- mouvement relatif.

Le brouillard ne doit pas supprimer la lecture d’un objectif ou d’un danger. Il doit aussi être budgété, car les effets volumétriques ont un coût et peuvent varier selon le renderer ou la qualité choisie.

> **[LECTURE] Règles de profondeur — Ne pas saisir.**

```yaml
depth_language:
  foreground:
    contrast: "high_if_focal"
    detail: "high"
    saturation: "controlled"
  midground:
    contrast: "medium"
    detail: "medium"
    saturation: "regional"
  background:
    contrast: "lower"
    detail: "low"
    saturation: "reduced"

fog_rules:
  - "never_hide_mandatory_navigation_anchor"
  - "preserve_character_silhouette_at_gameplay_distance"
  - "test_on_reference_hardware"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les plans visuels organisent la profondeur sans dépendre uniquement d’un effet volumétrique.

- **Relations :** Les valeurs `high`, `medium` et `low` sont relatives au profil de scène et devront être accompagnées de captures.

- **Navigation :** Le brouillard ne peut pas masquer un repère nécessaire au déplacement ou à la compréhension du danger.

- **Performance :** La règle de test rappelle qu’une ambiance valide visuellement peut être refusée si elle dépasse le budget.

- **Frontière :** Les paramètres de brouillard et l’optimisation détaillée seront traités dans les chapitres de terrain, VFX et validation.

## 20. Niveau de réalisme et simplification contrôlée

Le réalisme n’interdit pas la simplification. Un projet jouable doit supprimer ou exagérer certains détails pour préserver :

- silhouette ;
- animation ;
- interaction ;
- lecture à distance ;
- performance ;
- cohérence avec l’interface et les effets.

La bible doit distinguer :

- plausibilité structurelle ;
- fidélité des matériaux ;
- complexité géométrique ;
- densité de détails ;
- exagération fonctionnelle ;
- stylisation symbolique.

> **[VSC] Visual Studio Code — Ajouter à : `docs/art/VISUAL-DECISIONS.yaml` — Ne pas saisir.**

```yaml
realism_contract:
  structural_plausibility: "high"
  material_plausibility: "high"
  anatomical_exaggeration: "limited_for_readability"
  microdetail_density: "selective"
  functional_exaggeration:
    allowed:
      - "larger_grip_for_animation"
      - "clearer_damage_state"
      - "wider_silhouette_gap"
    forbidden:
      - "decoration_that_obscures_function"
      - "scale_change_without_gameplay_review"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le contrat décompose le mot `réalisme` en dimensions qui peuvent être arbitrées séparément.

- **Valeurs :** Les chaînes `high`, `limited_for_readability` et `selective` sont des catégories éditoriales à définir par des exemples visuels.

- **Exagération :** Elle est autorisée lorsqu’elle sert la lecture, l’animation ou l’état fonctionnel.

- **Refus :** Une décoration qui cache une poignée, une articulation ou une zone interactive contredit la fonction.

- **Résultat attendu :** Une simplification peut être approuvée sans être confondue avec un manque de finition.

## 21. Niveaux de traitement : héroïque, standard et arrière-plan

Tous les assets ne reçoivent pas le même niveau de traitement. La bible doit relier la qualité visible à l’usage défini au chapitre 1.

Trois classes initiales :

- **héroïque** : cadrages proches, interaction importante ou forte valeur narrative ;
- **standard** : usage fréquent à distance de jeu ;
- **arrière-plan** : contribution à la masse et à l’ambiance, sans inspection proche normale.

Ces classes modifient la densité de détail, le nombre de variantes, la qualité des transitions et la quantité de preuves requises. Elles ne changent pas les obligations de provenance, d’échelle et de cohérence.

> **[LECTURE] Niveaux de traitement visuel — Ne pas saisir.**

```yaml
visual_tiers:
  hero:
    close_readability: true
    unique_story_layers: true
    silhouette_uniqueness: "high"
    review_angles: 8
  standard:
    close_readability: "limited"
    unique_story_layers: "optional"
    silhouette_uniqueness: "medium"
    review_angles: 4
  background:
    close_readability: false
    unique_story_layers: false
    silhouette_uniqueness: "group_level"
    review_angles: 2
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les tiers alignent l’effort artistique sur le contexte d’usage.

- **Types :** Les booléens indiquent une obligation ; les chaînes qualifient une attente ; `review_angles` est un nombre minimal d’angles de contrôle proposé.

- **Invariant :** Un asset d’arrière-plan reste correctement dimensionné, licencié et importable ; seule sa richesse perceptuelle est réduite.

- **Dépendance :** La classe doit venir de la matrice d’assets du chapitre 1 et ne peut pas être choisie après coup pour justifier une économie.

- **Limite :** Le nombre d’angles est une hypothèse de revue, à adapter aux formes et à la caméra.

## 22. Personnages, costumes et visages

La bible du personnage doit définir avant la modélisation détaillée :

- rapports de proportions ;
- masses corporelles ;
- langage des costumes ;
- zones de silhouette protégées ;
- hiérarchie du visage ;
- relation entre fonction sociale et équipement ;
- niveau d’asymétrie ;
- traitement de l’usure ;
- variations culturelles sans stéréotype réducteur.

Le chapitre 6 produira les humains, le chapitre 7 les humanoïdes, le chapitre 10 les visages et le chapitre 11 les vêtements. Ici, on fixe seulement le cadre commun.

> **[VSC] Visual Studio Code — Créer : `docs/art/families/CHARACTERS.yaml` — Ne pas saisir.**

```yaml
character_direction:
  silhouette:
    priority_order:
      - "body_mass"
      - "role_equipment"
      - "cultural_layer"
      - "small_accessories"
  face:
    realism: "credible_structure_selective_detail"
    expression_readability: "preserve_at_gameplay_camera"
  costume:
    layer_logic:
      - "base"
      - "protection"
      - "role"
      - "personal_history"
  forbidden:
    - "accessories_that_merge_arm_and_torso_silhouettes"
    - "culture_encoded_by_single_color_only"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fiche hiérarchise la construction d’un personnage avant les décisions de topologie et de tissu.

- **Ordre de priorité :** La masse corporelle et l’équipement de rôle doivent rester lisibles avant les petits accessoires.

- **Couches :** Le costume raconte protection, fonction et histoire sans accumuler des éléments indépendants.

- **Diversité :** Une culture ne peut pas être réduite à une couleur unique ; formes, matériaux, assemblages et usage doivent contribuer.

- **Frontière :** Les rigs, déformations, cheveux et matériaux détaillés restent dans les chapitres spécialisés.

## 23. Animaux et créatures

Les êtres non humains doivent posséder une logique de silhouette, de locomotion et d’habitat. Une créature spectaculaire mais impossible à articuler, nourrir, déplacer ou identifier en jeu ne satisfait pas la bible.

Définir :

- ligne d’action dominante ;
- nombre et rôle des membres ;
- masse supportée ;
- surface de contact ;
- zone de regard supposée ;
- signes d’adaptation au biome ;
- différences entre repos, déplacement et menace ;
- détails qui restent lisibles en animation.

> **[LECTURE] Contrat visuel d’une créature pilote — Ne pas saisir.**

```yaml
creature_visual_contract:
  id: "creature.secondary.pilot"
  silhouette_signature:
    - "low_forward_mass"
    - "raised_sensory_fins"
    - "split_tail_gap"
  locomotion_read:
    rest: "stable_triangle"
    walk: "alternating_low_wave"
    alert: "vertical_fin_expansion"
  habitat_signs:
    - "mud_protected_joints"
    - "water_shedding_surface"
  animation_constraints:
    - "keep_eye_line_visible"
    - "preserve_tail_gap_in_side_view"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le contrat relie forme, locomotion et habitat avant la sculpture définitive.

- **États :** Repos, marche et alerte doivent produire des lectures différentes sans changer arbitrairement l’anatomie.

- **Contraintes d’animation :** La ligne du regard et le vide de la queue sont protégés car ils participent à l’identité.

- **Causalité :** Les articulations et surfaces décrites répondent à l’environnement boueux et humide.

- **Frontière :** Le comportement écologique et l’IA restent dans le Livre II ; les chapitres 8 et 9 produiront les modèles et rigs.

## 24. Architecture et environnements

L’environnement doit exprimer l’usage, l’époque, le pouvoir et l’entretien. La bible fixe :

- module dominant ;
- orientation des lignes ;
- rapport entre plein et ouverture ;
- échelle des motifs ;
- types de réparation ;
- relation au terrain ;
- hiérarchie des entrées ;
- comportement des matériaux ;
- règles de signalétique ;
- contraste entre structures anciennes, institutions et constructions improvisées.

> **[VSC] Visual Studio Code — Créer : `docs/art/families/ENVIRONMENTS.yaml` — Ne pas saisir.**

```yaml
environment_direction:
  ancient_infrastructure:
    geometry: ["large_mass", "deep_recess", "vertical_marker"]
    material_story: ["weathered_stone", "rare_conductive_inlay"]
    openings: "few_and_hierarchical"

  current_institution:
    geometry: ["repeated_module", "controlled_axis", "visible_threshold"]
    material_story: ["maintained_surface", "standardized_fastener"]
    openings: "ordered"

  improvised_settlement:
    geometry: ["offset_module", "brace", "adapted_reuse"]
    material_story: ["mixed_age", "visible_repair", "local_resource"]
    openings: "functional_irregularity"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fiche distingue trois familles d’environnement par géométrie, histoire matérielle et ouvertures.

- **Hiérarchie :** Les entrées et seuils rendent le pouvoir et l’usage lisibles avant les décorations.

- **Réemploi :** L’irrégularité improvisée doit rester fonctionnelle et causale ; elle ne signifie pas désordre aléatoire.

- **Relation au chapitre 13 :** Les modules, pivots, collisions et métriques précises seront définis lors de la production des kits.

- **Résultat attendu :** Deux bâtiments de régions différentes peuvent varier tout en restant identifiables comme appartenant à la même famille institutionnelle.

## 25. Objets, équipements et interfaces physiques

Un objet doit montrer :

- où il se tient ;
- comment il s’active ;
- quelle partie bouge ;
- quel état est dangereux ;
- quels matériaux supportent les efforts ;
- où l’entretien se produit ;
- quelles zones doivent rester libres pour l’animation ou l’interaction.

L’identité visuelle ne doit pas masquer la fonction. Les boutons, poignées, charnières, lames, surfaces de contact et points d’attache doivent rester lisibles.

> **[LECTURE] Grille fonctionnelle d’un prop — Ne pas saisir.**

```markdown
| Zone | Fonction | Lecture requise | Traitement visuel |
|---|---|---|---|
| poignée | prise | moyenne distance | contraste de valeur et usure de contact |
| charnière | rotation | proximité | axe visible et matériau structurel |
| panneau | accès | moyenne distance | contour et changement de plan |
| danger | chaleur | loin et moyen | forme, couleur réservée et effet local |
| fixation | assemblage | proximité | répétition cohérente, sans bruit uniforme |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La grille relie chaque zone à sa fonction, sa distance de lecture et son traitement.

- **Lecture requise :** Une information de sécurité doit rester visible plus loin qu’un détail d’assemblage.

- **Redondance :** La chaleur utilise forme, couleur et effet au lieu de dépendre uniquement du rouge.

- **Usure :** La poignée reçoit une trace de contact parce qu’elle est manipulée, non parce que toutes les arêtes doivent être éclaircies.

- **Frontière :** Le chapitre 12 produira les objets, pivots, sockets, collisions et états visuels définitifs.

## 26. Interface utilisateur et continuité avec le monde

L’interface ne doit pas imiter littéralement tous les matériaux du monde au point de perdre sa lisibilité. Elle reprend plutôt :

- proportions ;
- rythme ;
- rayon des formes ;
- densité ;
- hiérarchie ;
- accents fonctionnels ;
- motifs culturels ;
- mouvement.

Les textes, contrôles et retours d’état restent prioritaires. Le chapitre 24 développera le design system complet ; la bible actuelle fixe la relation entre monde et interface.

> **[VSC] Visual Studio Code — Créer : `docs/art/families/UI-VISUAL-DIRECTION.yaml` — Ne pas saisir.**

```yaml
ui_visual_direction:
  relation_to_world:
    inherit:
      - "angular_institutional_frames"
      - "copper_repair_accent"
      - "layered_history_motif"
    do_not_inherit:
      - "surface_noise_behind_text"
      - "low_contrast_weathering"
      - "irregular_spacing"

  functional_tokens:
    danger: "palette.functional.danger"
    interaction: "palette.functional.interaction"
    selected: "palette.functional.selected"

  motion:
    default: "short_and_directional"
    decorative_loop: "rare"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fiche choisit quels traits du monde peuvent devenir langage d’interface et lesquels doivent rester exclus.

- **Héritage sélectif :** Les cadres et accents transmettent l’identité ; le bruit de surface et l’espacement irrégulier nuiraient à la lecture.

- **Tokens :** L’interface référence les rôles de palette au lieu de copier leurs valeurs.

- **Mouvement :** Les transitions courtes expliquent un changement ; les boucles décoratives sont rares pour ne pas concurrencer les alertes.

- **Frontière :** Le chapitre 24 définira thèmes Godot, composants, navigation, résolutions et profils d’accessibilité.

## 27. Effets visuels et priorité du gameplay

Les VFX doivent amplifier une information déjà compréhensible, pas la remplacer. La bible fixe :

- forme de l’effet ;
- direction ;
- durée perceptuelle ;
- couleur fonctionnelle ;
- densité ;
- zone à préserver autour du sujet ;
- niveau de luminosité ;
- dégradation à distance ;
- variantes accessibles.

Les effets du chapitre 23 devront respecter ces règles, y compris les phénomènes rares ou spectaculaires. Un effet visuellement impressionnant reste non conforme s’il masque la cible, la zone de danger ou la trajectoire utile.

> **[VSC] Visual Studio Code — Créer : `docs/art/families/VFX-DIRECTION.yaml` — Ne pas saisir.**

```yaml
vfx_direction:
  principles:
    - "shape_before_particles"
    - "direction_matches_gameplay_cause"
    - "focal_brightness_is_bounded"
    - "danger_area_remains_visible"

  classes:
    impact:
      duration_role: "brief"
      silhouette: "radial_or_directional"
    persistent_hazard:
      duration_role: "sustained"
      silhouette: "stable_boundary"
    atmospheric:
      duration_role: "ambient"
      silhouette: "non_competing"

  accessibility:
    color_only_signal: false
    reduced_motion_variant: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fiche sépare impacts, dangers persistants et atmosphère selon leur fonction temporelle et spatiale.

- **Principe de forme :** La frontière ou direction principale doit être lisible avant la multiplication des particules.

- **Luminosité :** Le pic lumineux est borné pour éviter de saturer l’image et de détruire les couleurs voisines.

- **Accessibilité :** Une variante à mouvement réduit et une redondance autre que la couleur sont obligatoires.

- **Frontière :** Les techniques GPU, CPU, shaders et simulations précalculées seront choisies au chapitre 23.

## 28. Variations culturelles, régionales, sociales et temporelles

La cohérence n’exige pas l’uniformité. Une variation doit conserver une base commune et modifier des dimensions identifiées.

Pour chaque culture, région ou groupe social, documenter :

- ressources disponibles ;
- techniques d’assemblage ;
- contraintes climatiques ;
- signes de statut ;
- degré d’entretien ;
- motifs et couleurs ;
- relation à l’ancienne infrastructure ;
- éléments partagés avec l’univers ;
- éléments propres au groupe ;
- éléments explicitement interdits.

Éviter les raccourcis où une culture équivaut à une couleur, un motif ou un accessoire unique.

> **[LECTURE] Profil de variation — Ne pas saisir.**

```yaml
variation_profile:
  id: "region.marsh_settlement"
  inherits:
    - "pillar.traces_and_repair"
    - "shape.improvised"
  environment_drivers:
    - "humidity"
    - "soft_ground"
    - "limited_dry_storage"
  visual_changes:
    materials: ["treated_fiber", "raised_wood", "reused_metal"]
    geometry: ["elevated_walkway", "wide_support", "drainage_gap"]
    palette: ["cool_neutral", "muted_green", "repair_copper"]
  forbidden_shortcuts:
    - "single_color_identity"
    - "random_damage_without_water_logic"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le profil dérive une variation de contraintes matérielles et environnementales plutôt que d’un décor arbitraire.

- **Héritage :** La région conserve les piliers universels et le langage de construction improvisée.

- **Causalité :** L’humidité et le sol mou expliquent les passerelles, supports larges et espaces de drainage.

- **Raccourcis interdits :** La couleur seule et les dégâts aléatoires ne suffisent pas à créer une identité régionale.

- **Résultat attendu :** Une nouvelle région peut être conçue par combinaison de causes, formes et matériaux documentés.

## 29. États temporels, saisons et évolution

Une bible peut définir l’apparence d’un même lieu ou asset à plusieurs moments :

- intact ;
- utilisé ;
- endommagé ;
- réparé ;
- abandonné ;
- réoccupé ;
- sec, humide, gelé ou enneigé ;
- jour, nuit, aube ou tempête.

Ces variantes visuelles ne doivent pas inventer l’état runtime. Elles décrivent comment représenter un état déjà décidé par les systèmes du Livre II.

> **[LECTURE] Table de traduction d’état — Ne pas saisir.**

```yaml
visual_state_mapping:
  maintained:
    signs:
      - "clear_access_path"
      - "recent_fastener"
      - "controlled_surface_cleaning"
  damaged:
    signs:
      - "structural_break_follows_load"
      - "warning_shape_visible"
      - "access_panel_unusable"
  repaired:
    signs:
      - "new_material_layer"
      - "functional_brace"
      - "old_damage_still_partly_readable"

runtime_authority: "state supplied by owning gameplay system"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La table traduit un état fourni par le gameplay en signes visuels cohérents.

- **Autorité :** Le champ `runtime_authority` rappelle que la bible ne décide pas si l’objet est endommagé ou réparé.

- **Continuité :** La réparation conserve une partie de la trace ancienne pour rendre l’histoire visible.

- **Sécurité :** Un état dangereux ou inutilisable doit aussi posséder un signal fonctionnel clair.

- **Frontière :** Les variantes de modèles, matériaux et animations seront produites dans les chapitres d’assets concernés.

## 30. Concevoir des exemples conformes, limites et non conformes

Une règle sans exemples est difficile à appliquer. Pour chaque décision importante, produire au minimum :

- un exemple **conforme** ;
- un exemple **limite**, encore acceptable mais risqué ;
- un exemple **non conforme** ;
- une annotation expliquant la différence.

Le cas limite est essentiel : il montre la tolérance réelle et évite que la bible devienne un catalogue de prohibitions.

> **[VSC] Visual Studio Code — Créer : `docs/art/EXAMPLE-CATALOG.yaml` — Ne pas saisir.**

```yaml
examples:
  - rule_id: "pillar.readable_complexity"
    compliant:
      asset: "beacon_variant_a"
      reason: "large silhouette gaps and detail grouped near interaction"
    borderline:
      asset: "beacon_variant_b"
      reason: "secondary cables begin to merge at 15 meters"
      required_check: "gameplay_camera_capture"
    non_compliant:
      asset: "beacon_variant_c"
      reason: "uniform microdetail erases hierarchy at 15 meters"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le catalogue rattache trois niveaux d’exemple à une règle stable.

- **Cas limite :** Il exige une vérification supplémentaire au lieu d’être accepté ou rejeté automatiquement.

- **Raison :** Chaque classement mentionne un comportement perceptuel observable, pas une préférence générale.

- **Dépendance :** Les noms d’assets doivent correspondre à des captures versionnées ou à des planches de référence traçables.

- **Résultat attendu :** Les nouveaux producteurs comprennent non seulement la cible, mais aussi le seuil où un choix devient risqué.

## 31. Grille de revue artistique

La revue doit séparer les dimensions afin d’éviter qu’un asset séduisant compense mentalement un défaut fonctionnel.

Évaluer au moins :

- silhouette ;
- échelle ;
- hiérarchie ;
- palette ;
- matériaux ;
- lumière ;
- fonction ;
- cohérence de famille ;
- cohérence universelle ;
- provenance ;
- budget ;
- qualité des preuves.

Utiliser des statuts explicites : `accepté`, `accepté avec action`, `à corriger`, `bloqué`, `dérogation requise`.

> **[VSC] Visual Studio Code — Créer : `docs/art/review/ART-REVIEW-GRID.md` — Ne pas saisir.**

```markdown
# Grille de revue artistique

| Critère | Statut | Observation | Action | Propriétaire |
|---|---|---|---|---|
| silhouette à 25 m | à corriger | l’accessoire fusionne avec le torse | déplacer ou réduire | character-art |
| palette fonctionnelle | accepté | interaction lisible sans dépendre de la teinte | aucune | ui-art |
| histoire matérielle | accepté avec action | usure cohérente, capture sombre manquante | ajouter capture | material-art |
| provenance | bloqué | source de motif non renseignée | compléter le registre | art-production |

## Décision
- Statut global :
- Règles citées :
- Dérogation :
- Prochaine revue :
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La grille transforme une revue en observations, actions et responsabilités traçables.

- **Statuts :** `bloqué` interdit la promotion ; `accepté avec action` permet une suite seulement si l’action ne remet pas en cause le critère essentiel.

- **Règles citées :** Chaque observation doit viser une règle ou un identifiant de la bible lorsqu’il existe.

- **Provenance :** Une source juridique inconnue peut bloquer un asset même si son rendu est excellent.

- **Résultat attendu :** La décision globale peut être comprise sans réécouter une réunion ou interpréter des commentaires dispersés.

## 32. Processus de dérogation

Une dérogation autorise un écart justifié sans modifier la règle générale. Elle est appropriée lorsqu’un besoin unique, une contrainte technique ou une intention narrative rend la règle inadaptée à un cas précis.

Une dérogation doit contenir :

- règle concernée ;
- asset ou périmètre ;
- raison ;
- conséquences ;
- alternatives étudiées ;
- preuves ;
- propriétaire de la décision ;
- date d’expiration ou de réexamen ;
- décision d’intégrer ou non le cas à la prochaine bible.

> **[VSC] Visual Studio Code — Créer : `docs/art/exceptions/EXC-BEACON-GLOW-001.yaml` — Ne pas saisir.**

```yaml
exception:
  id: "exc.beacon_glow.001"
  rule_id: "palette.functional.high_saturation_reserved"
  scope:
    assets: ["prop.beacon.ancient_01"]
    scenes: ["vertical_slice.validation_zone"]
  reason: "the beacon is the only long-distance navigation anchor"
  alternatives_reviewed:
    - "larger silhouette marker"
    - "animated mechanical flag"
  safeguards:
    - "glow disabled in neutral material review"
    - "brightness bounded in gameplay profile"
  owner: "art-direction-owner"
  review_on: "2026-09-01"
  status: "approved_for_vertical_slice"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La dérogation limite un écart à un asset et une scène déterminés.

- **Alternatives :** Les solutions étudiées montrent que l’exception n’est pas un raccourci choisi sans comparaison.

- **Garde-fous :** Le glow est neutralisé dans la revue de matériau et sa luminosité reste bornée en gameplay.

- **Durée :** La date de revue empêche qu’une exception temporaire devienne une règle tacite permanente.

- **Invariant :** Une dérogation n’écrase pas la règle d’origine et ne s’applique pas automatiquement à d’autres assets.

## 33. Versionner les décisions et gérer les changements

Toute modification importante doit préciser :

- identifiant de décision ;
- ancienne valeur ;
- nouvelle valeur ;
- raison ;
- assets affectés ;
- coût de migration ;
- date d’application ;
- responsable ;
- besoin de réimport ou de nouvelle capture.

Utiliser un changement majeur lorsque la grammaire ou les livrables deviennent incompatibles, un changement mineur pour une règle nouvelle compatible et un correctif pour une clarification sans modification d’intention.

> **[VSC] Visual Studio Code — Ajouter à : `docs/art/VISUAL-DECISIONS.yaml` — Ne pas saisir.**

```yaml
decision_log:
  - id: "decision.palette.interaction.v2"
    previous: "#E9C65C"
    next: "#E0B84F"
    reason: "reduce competition with memory_cyan under neutral review"
    affected:
      - "ui_theme"
      - "interaction_vfx"
      - "signage_material"
    migration:
      requires_asset_review: true
      requires_reimport: true
      requires_new_captures: true
    owner: "art-direction-owner"
    effective_from: "visual_bible_1.1.0"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le journal explique une évolution de token et les éléments qui doivent être revus.

- **Compatibilité :** Le changement de couleur paraît mineur, mais il peut toucher UI, VFX et matériaux ; la migration reste donc explicite.

- **Booléens :** Les trois champs `requires_...` empêchent d’oublier les étapes d’application.

- **Identité :** La décision possède son propre identifiant, distinct du token de palette et de la version de bible.

- **Résultat attendu :** Une capture ancienne peut être reliée à la version qui l’a produite et ne pas être comparée comme si elle utilisait les nouvelles règles.

## 34. Construire la scène Godot de validation

La scène de validation doit comparer des assets sous des conditions contrôlées. Elle contient au minimum :

- `WorldEnvironment` ;
- lumière principale ;
- sol et fond neutres ;
- repères métriques ;
- caméras enregistrées ;
- emplacement pour plusieurs assets ;
- panneaux de valeur claire, moyenne et sombre ;
- option d’affichage en situation plus complexe ;
- profils d’environnement neutre, clair et sombre.

Le chapitre ne matérialise pas cette scène. Il définit son contrat pour qu’elle puisse être créée dans le Starter Kit.

> **[LECTURE] Arbre cible de la scène Godot — Ne pas saisir.**

```text
ArtDirectionValidation (Node3D)
├── WorldEnvironment
├── Lighting
│   ├── KeyLight (DirectionalLight3D)
│   └── OptionalRimLight (DirectionalLight3D)
├── Reference
│   ├── MeterGrid
│   ├── HumanScale
│   ├── ValuePanelLight
│   ├── ValuePanelMid
│   └── ValuePanelDark
├── AssetSlots
│   ├── SlotA
│   ├── SlotB
│   └── SlotC
├── Cameras
│   ├── CloseCamera
│   ├── GameplayCamera
│   ├── FarCamera
│   └── TopCamera
└── ReviewUI (CanvasLayer)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’arbre sépare environnement, éclairage, références, emplacements d’assets, caméras et interface de revue.

- **Responsabilités :** `AssetSlots` accueille les variantes sans déplacer les références ; `Cameras` conserve les points de comparaison.

- **Échelle :** La grille et le personnage de référence révèlent immédiatement une erreur de dimension ou de pivot.

- **Fond :** Les trois panneaux de valeur détectent une silhouette qui ne fonctionne que sur un arrière-plan particulier.

- **Limite :** L’arbre est un contrat de scène ; aucun nœud n’est déclaré créé ou exécuté dans ce chapitre.

## 35. Préparer un contrôleur de caméras de revue

Un petit script pourra sélectionner des caméras nommées sans déplacer manuellement le point de vue entre les captures. Il doit rester un outil de validation, sans autorité sur la caméra de gameplay.

> **[VSC] Visual Studio Code — Créer : `tools/art_direction/review_camera_rig.gd` — Ne pas saisir.**

```gdscript
@tool
class_name ReviewCameraRig
extends Node3D

@export var cameras: Array[Camera3D] = []
@export var default_index: int = 0

func activate_camera(index: int) -> Error:
    if index < 0 or index >= cameras.size():
        return ERR_INVALID_PARAMETER

    var target := cameras[index]
    if target == null:
        return ERR_DOES_NOT_EXIST

    for camera in cameras:
        if camera != null:
            camera.current = camera == target

    return OK

func activate_default() -> Error:
    return activate_camera(default_index)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `ReviewCameraRig` active un cadrage enregistré pour rendre les captures comparables.

- **Propriétés exportées :** `cameras` est un tableau de `Camera3D`; `default_index` est l’indice utilisé par `activate_default()`.

- **Paramètre et codes de retour :** `index` doit viser une entrée existante. La fonction renvoie `ERR_INVALID_PARAMETER`, `ERR_DOES_NOT_EXIST` ou `OK`.

- **Déroulement :** Après validation, la boucle désactive implicitement les autres caméras en assignant `current` uniquement à la cible.

- **Effet de bord :** La propriété `current` des caméras est modifiée dans la scène de revue.

- **Limite :** Le script n’effectue aucune capture et n’est pas revendiqué comme analysé ou exécuté dans Godot.

## 36. Préparer des profils de revue plutôt qu’un réglage unique

Un asset doit être observé dans plusieurs profils :

1. **neutre** : révèle forme, valeur et matériau ;
2. **clair** : teste hautes lumières et saturation ;
3. **sombre** : teste silhouette et détails noyés ;
4. **fond chargé** : teste concurrence visuelle ;
5. **gameplay** : teste la scène réelle ;
6. **accessibilité** : teste réduction de mouvement et signaux redondants.

> **[VSC] Visual Studio Code — Créer : `docs/art/review/REVIEW-PROFILES.yaml` — Ne pas saisir.**

```yaml
review_profiles:
  - id: "review.neutral"
    required: true
    camera_set: ["close", "gameplay", "far"]
  - id: "review.bright_stress"
    required: true
    camera_set: ["gameplay"]
  - id: "review.dark_stress"
    required: true
    camera_set: ["gameplay"]
  - id: "review.busy_background"
    required: true
    camera_set: ["gameplay", "far"]
  - id: "review.accessibility"
    required: true
    camera_set: ["gameplay"]
  - id: "review.presentation"
    required: false
    camera_set: ["close"]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les profils séparent les contrôles obligatoires d’une capture de présentation facultative.

- **Tableaux :** `camera_set` liste les cadrages requis pour chaque profil, afin de ne pas produire inutilement toutes les combinaisons.

- **Précondition :** Chaque profil doit citer un environnement et une version de bible dans le rapport de capture.

- **Présentation :** Une capture flatteuse ne peut pas remplacer les profils neutres et de stress.

- **Résultat attendu :** La revue détecte les défauts de lecture avant que les assets soient multipliés dans le catalogue.

## 37. Protocole de capture et nommage

Chaque capture doit permettre de retrouver :

- asset ;
- variante ;
- version ;
- profil ;
- caméra ;
- date ;
- bible ;
- build ou commit lorsque disponible.

Les captures servent à la comparaison et à la revue. Elles ne remplacent pas les sources, les fichiers importés ni les décisions.

> **[LECTURE] Convention de nommage des captures — Ne pas saisir.**

```text
captures/art_direction/
  prop.beacon.ancient_01/
    v0003/
      bible-1.0.0__review-neutral__camera-close.png
      bible-1.0.0__review-neutral__camera-gameplay.png
      bible-1.0.0__review-dark-stress__camera-gameplay.png
      bible-1.0.0__review-busy-background__camera-far.png
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le chemin regroupe les captures par asset et version, puis encode bible, profil et caméra dans le nom.

- **Version :** `v0003` représente une révision de l’asset, distincte de `bible-1.0.0`.

- **Comparabilité :** Deux images ne sont comparées directement que si les profils et caméras sont compatibles ou si la différence est l’objet du test.

- **Source canonique :** Le dossier de captures reste dérivé ; supprimer une capture ne doit pas supprimer la source de l’asset.

- **Résultat attendu :** Une décision de revue peut citer une image sans ambiguïté.

## 38. Comparer les assets pilotes

Le chapitre 1 a retenu plusieurs assets pilotes complémentaires. La bible doit être testée sur au moins :

- balise ou prop héroïque ;
- personnage ;
- animal ou créature ;
- module architectural ;
- végétation ;
- élément d’interface ;
- effet visuel.

Un langage qui fonctionne seulement sur un prop ne peut pas encore être déclaré transversal.

> **[VSC] Visual Studio Code — Créer : `docs/art/review/PILOT-COMPARISON.md` — Ne pas saisir.**

```markdown
# Comparaison des assets pilotes

| Asset pilote | Silhouette | Palette | Matériaux | Éclairage | Fonction | Décision |
|---|---|---|---|---|---|---|
| balise ancienne | à produire | à produire | à produire | à produire | navigation | en attente |
| personnage pilote | à produire | à produire | à produire | à produire | incarnation | en attente |
| créature secondaire | à produire | à produire | à produire | à produire | monde vivant | en attente |
| module architectural | à produire | à produire | à produire | à produire | espace | en attente |
| thème UI pilote | à produire | à produire | n/a | à produire | information | en attente |
| VFX d’interaction | à produire | à produire | n/a | à produire | feedback | en attente |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La table force la bible à couvrir plusieurs familles avant son verrouillage.

- **État :** `à produire` indique honnêtement qu’aucun asset pilote n’est matérialisé dans ce chapitre.

- **Valeur `n/a` :** Elle distingue un critère non applicable d’un travail manquant.

- **Fonction :** Chaque pilote représente un problème différent : navigation, incarnation, monde, espace, information ou retour d’action.

- **Résultat attendu :** La prochaine version de la bible sera fondée sur des écarts observés entre familles, pas uniquement sur une planche de références.

## 39. Mesures et observations à conserver

La direction artistique produit des observations qualitatives, mais certaines propriétés sont mesurables :

- résolution de capture ;
- distance caméra ;
- champ de vision ;
- dimensions ;
- temps de frame ;
- mémoire ;
- nombre de matériaux ;
- visibilité d’un signal ;
- ratio de contraste d’un texte ;
- réussite d’une classification conforme/non conforme.

Les mesures doivent rester liées à un scénario, une version et un profil.

> **[VSC] Visual Studio Code — Créer : `docs/art/review/ART-REVIEW-RECORD.yaml` — Ne pas saisir.**

```yaml
review_record:
  asset_id: "prop.beacon.ancient_01"
  asset_version: "v0003"
  visual_bible_version: "1.0.0"
  capture_profile: "capture.art_direction.v1"
  engine: "Godot 4.7.1-stable"
  measurements:
    camera_distance_m: null
    frame_time_ms: null
    gpu_memory_delta_mb: null
    ui_contrast_ratio: null
  observations:
    silhouette_far: "not_executed"
    material_read_neutral: "not_executed"
    functional_state_read: "not_executed"
  decision: "pending_runtime_validation"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le rapport rassemble contexte, mesures, observations et décision sans inventer de résultat.

- **Valeurs nulles :** `null` indique qu’une mesure n’a pas été réalisée ; zéro aurait une signification technique différente.

- **Statuts :** `not_executed` et `pending_runtime_validation` empêchent de présenter une revue statique comme un test moteur.

- **Traçabilité :** La version de bible et le profil de capture permettent de reproduire la comparaison.

- **Résultat attendu :** Lors de la matérialisation, les champs sont remplis à partir d’une exécution réelle et conservés avec les captures.

## 40. Provenance et droits des références visuelles

La bible peut inclure des références externes, mais chaque référence doit avoir :

- source ;
- auteur ou fournisseur ;
- URL ou emplacement ;
- date d’accès ;
- licence ou statut ;
- usage autorisé ;
- restrictions ;
- modifications ;
- raison de sa présence.

Une référence n’est pas automatiquement redistribuable dans un manuel, un dépôt ou un produit. Une image utilisée seulement en interne ne doit pas être copiée dans une publication sans droit adapté.

> **[VSC] Visual Studio Code — Créer : `docs/art/REFERENCE-REGISTER.yaml` — Ne pas saisir.**

```yaml
references:
  - id: "ref.architecture.weathering.001"
    title: "masonry repair reference"
    source: "to_be_selected"
    author: null
    url: null
    accessed_on: null
    license: "unknown"
    allowed_uses: []
    restrictions:
      - "do_not_redistribute"
      - "do_not_train_without_permission"
    purpose:
      - "study_repair_layers"
    status: "blocked_until_documented"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le registre montre l’état d’une référence avant sélection et empêche son usage silencieux.

- **Valeurs inconnues :** Les champs `null`, la licence `unknown` et le statut bloqué indiquent qu’aucune source réelle n’a encore été choisie.

- **Restrictions :** L’interdiction de redistribution protège le dépôt et le futur manuel tant que les droits ne sont pas établis.

- **Usage :** `purpose` décrit ce qui doit être étudié sans transformer la référence en asset ou texture.

- **Frontière :** Le chapitre 3 organisera la collecte de références et les workflows ComfyUI ; le chapitre 5 détaillera provenance et licences.

## 41. Mode Solo

En Mode Solo, la bible doit rester courte et directement exploitable. Une personne seule ne doit pas maintenir plusieurs documents qui répètent les mêmes règles.

Priorités recommandées :

- trois piliers maximum pour le vertical slice ;
- un fichier principal et quelques annexes structurées ;
- une palette monde et une palette fonctionnelle ;
- une scène de validation ;
- une grille de revue ;
- un petit ensemble d’exemples conformes et non conformes ;
- une revue planifiée après chaque asset pilote ;
- aucune dérogation orale non enregistrée.

Le créateur peut être à la fois auteur et réviseur, mais il doit séparer les moments : produire, laisser reposer, puis revoir avec la grille et les profils de capture.

## 42. Mode Studio

En Mode Studio, la bible devient un contrat partagé. Elle doit préciser :

- propriétaire de la direction artistique ;
- propriétaires des familles ;
- droits de modification ;
- procédure de commentaire ;
- historique des décisions ;
- réunion de revue ;
- dérogations ;
- délai de réponse ;
- statut de promotion ;
- responsabilités de migration.

Une revue importante doit inclure au moins une personne qui n’a pas produit l’asset. Les commentaires doivent citer une règle, une capture et une action attendue. Une préférence personnelle peut être discutée, mais elle ne bloque pas une livraison sans règle ou besoin fonctionnel associé.

## 43. Contrat commun entre Solo et Studio

Les deux parcours partagent les mêmes invariants :

- source de vérité versionnée ;
- règles observables ;
- exemples annotés ;
- scènes et profils de comparaison ;
- provenance ;
- dérogations explicites ;
- distinction entre source, capture et décision ;
- validation dans Godot avant verrouillage.

> **[LECTURE] Responsabilités comparées — Ne pas saisir.**

```markdown
| Responsabilité | Solo | Studio |
|---|---|---|
| propriétaire de la bible | créateur principal | direction artistique nommée |
| revue | revue différée structurée | revue croisée |
| dérogation | fiche obligatoire | approbation par rôle |
| migration | liste personnelle versionnée | plan assigné par famille |
| preuve | captures et grille | captures, grille et décision partagée |
| règle commune | aucune décision seulement orale | aucune décision seulement orale |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le tableau adapte la gouvernance sans créer deux directions artistiques incompatibles.

- **Différence principale :** Le Studio sépare davantage les responsabilités ; le Solo sépare surtout les moments de production et de revue.

- **Dérogation :** Dans les deux cas, l’écart est écrit et limité.

- **Migration :** Toute modification de bible doit identifier les assets concernés, même si une seule personne effectue le travail.

- **Invariant :** Une décision orale non enregistrée n’est pas une règle applicable.

## 44. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 44.1 Accumuler des images sans formuler de règles

**Symptôme :** Les producteurs choisissent chacun une référence différente et les assets paraissent appartenir à plusieurs univers.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
# Moodboard
- image spectaculaire A
- image spectaculaire B
- image spectaculaire C

Conclusion : "faire quelque chose dans cet esprit"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les producteurs choisissent chacun une référence différente et les assets paraissent appartenir à plusieurs univers. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
# Décision issue du moodboard
- Pilier : complexité lisible
- Signe attendu : détails groupés autour des fonctions
- Signe interdit : microdétail uniforme
- Exemple conforme : référence B, zone annotée 2
- Cas limite : référence C, arrière-plan seulement
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le moodboard corrigé produit des règles, des signes et des limites citables au lieu de déléguer l’interprétation à chaque personne.
### 44.2 Employer des adjectifs non observables

**Symptôme :** Deux réviseurs demandent des corrections opposées tout en utilisant le même mot « réaliste ».

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
style:
  realism: "élevé"
  mood: "épique"
  quality: "cinématographique"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Deux réviseurs demandent des corrections opposées tout en utilisant le même mot « réaliste ». La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
realism_contract:
  structural_plausibility: "high"
  material_plausibility: "high"
  microdetail_density: "selective"
  functional_exaggeration: "allowed_for_readability"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les dimensions du réalisme sont séparées et peuvent être accompagnées d’exemples, ce qui réduit les interprétations contradictoires.
### 44.3 Maximiser le contraste et le détail partout

**Symptôme :** La cible, le décor et l’interface rivalisent ; le joueur ne sait plus où regarder.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
visual_rule:
  contrast: "maximum"
  saturation: "high"
  detail_density: "high"
  apply_to: "all_assets"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La cible, le décor et l’interface rivalisent ; le joueur ne sait plus où regarder. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
visual_hierarchy:
  focal: "high_contrast_or_motion"
  support: "medium_contrast"
  rest: "low_detail_and_limited_value_range"
  max_simultaneous_focal_targets: 2
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction réserve les moyens de mise en valeur aux éléments prioritaires et protège des zones de repos.
### 44.4 Utiliser une couleur comme unique information

**Symptôme :** Un état reste compréhensible sur l’écran du créateur mais disparaît pour certains joueurs ou en image désaturée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
states:
  available: "green"
  unavailable: "red"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un état reste compréhensible sur l’écran du créateur mais disparaît pour certains joueurs ou en image désaturée. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
states:
  available:
    color: "interaction"
    icon: "open_circle"
    label: "Disponible"
  unavailable:
    color: "unavailable"
    icon: "barred_circle"
    label: "Indisponible"

```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction associe couleur, forme et texte afin que la différence survive à une perception chromatique réduite.
### 44.5 Valider les matériaux sous une seule lumière flatteuse

**Symptôme :** Un matériau accepté devient illisible, trop brillant ou sans volume dans la scène de jeu.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
review:
  environment: "sunset_presentation"
  camera: "close"
  decision: "approved"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un matériau accepté devient illisible, trop brillant ou sans volume dans la scène de jeu. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
review_profiles:
  required:
    - "neutral"
    - "bright_stress"
    - "dark_stress"
    - "gameplay"
  optional:
    - "presentation"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les profils obligatoires séparent la preuve de diagnostic de la capture de présentation et exposent les défauts sous plusieurs conditions.
### 44.6 Distribuer l’usure au hasard

**Symptôme :** La surface paraît bruyante et ancienne, mais aucune marque ne correspond au contact, à l’eau ou à une réparation.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
wear:
  edge_damage: "everywhere"
  scratches: "random"
  dirt: "uniform_noise"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La surface paraît bruyante et ancienne, mais aucune marque ne correspond au contact, à l’eau ou à une réparation. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
wear:
  contact_zones: ["handle", "foot_step"]
  water_paths: ["vertical_streak_below_joint"]
  protected_deposits: ["deep_recess"]
  repair_layer: ["recent_copper_brace"]
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction relie chaque signe à une cause et à une zone, ce qui transforme le bruit en histoire matérielle lisible.
### 44.7 Confondre cohérence et uniformité

**Symptôme :** Toutes les régions utilisent les mêmes formes, matériaux et couleurs ; le monde perd sa diversité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
regions:
  palette: "same"
  architecture: "same"
  materials: "same"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Toutes les régions utilisent les mêmes formes, matériaux et couleurs ; le monde perd sa diversité. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
region:
  inherits: ["universal_pillars", "shared_functional_colors"]
  varies_by:
    - "climate"
    - "resources"
    - "construction_technique"
    - "social_maintenance"

```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve des piliers universels tout en dérivant les variations de contraintes propres à chaque région.
### 44.8 Modifier la bible sans plan de migration

**Symptôme :** Les nouveaux assets suivent la règle modifiée, mais les anciens restent incohérents et personne ne sait lesquels reprendre.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
change:
  token: "interaction"
  new_value: "#E0B84F"
  status: "done"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les nouveaux assets suivent la règle modifiée, mais les anciens restent incohérents et personne ne sait lesquels reprendre. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
change:
  decision_id: "decision.palette.interaction.v2"
  affected: ["ui_theme", "interaction_vfx", "signage_material"]
  requires_reimport: true
  requires_new_captures: true
  owner: "art-direction-owner"
  effective_from: "visual_bible_1.1.0"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction identifie la portée, les actions et la version d’application, ce qui rend la migration planifiable.
### 44.9 Accepter une dérogation orale

**Symptôme :** Un écart temporaire est copié par d’autres assets et devient une nouvelle norme sans décision.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
exception:
  reason: "le directeur artistique a dit que c'était bon"
  scope: "probablement seulement cette scène"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un écart temporaire est copié par d’autres assets et devient une nouvelle norme sans décision. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
exception:
  id: "exc.beacon_glow.001"
  rule_id: "palette.functional.high_saturation_reserved"
  scope:
    assets: ["prop.beacon.ancient_01"]
  safeguards:
    - "brightness_bounded"
  review_on: "2026-09-01"
  status: "approved_for_vertical_slice"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite l’écart, cite la règle, impose un garde-fou et prévoit une révision.
### 44.10 Déclarer la bible validée sans assets pilotes dans Godot

**Symptôme :** Le document paraît complet, mais ses palettes, proportions et règles d’éclairage n’ont jamais été confrontées au moteur.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```yaml
visual_bible:
  status: "final"
  pilot_assets: []
  godot_captures: []
  runtime_review: "not_needed"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le document paraît complet, mais ses palettes, proportions et règles d’éclairage n’ont jamais été confrontées au moteur. La formulation ne fournit pas un contrat assez précis pour être reproduit ou vérifié.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```yaml
visual_bible:
  status: "draft_validated_static"
  pilot_assets:
    required: 7
    produced: 0
  godot_captures:
    required: true
    produced: 0
  next_status: "runtime_validated_after_pilot_review"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve un statut honnête et rend explicites les preuves encore manquantes avant le verrouillage.

## 45. Checklist d’acceptation de la bible visuelle

Avant de déclarer la bible prête pour la production des concepts et assets pilotes :

- trois à cinq piliers sont formulés avec signes attendus et comportements interdits ;
- les axes de style possèdent exemples et tolérances ;
- la grammaire universelle est distincte des règles de famille ;
- silhouettes, échelles et niveaux de lecture sont documentés ;
- les palettes séparent monde, interface, VFX et fonctions ;
- aucune information essentielle ne dépend de la couleur seule ;
- les familles de matériaux possèdent une logique d’usage et d’usure ;
- les profils d’éclairage et de capture sont versionnés ;
- le niveau de réalisme est décomposé en dimensions observables ;
- les tiers héroïque, standard et arrière-plan sont définis ;
- personnages, créatures, environnements, props, UI et VFX possèdent un cadre ;
- les variations culturelles et régionales dérivent de causes, pas de stéréotypes simples ;
- chaque règle importante possède exemple conforme, limite et non conforme ;
- la grille de revue et le processus de dérogation sont prêts ;
- les changements exigent un plan de migration ;
- les références visuelles possèdent une provenance ou restent bloquées ;
- la scène Godot, les profils et les captures sont décrits sans être déclarés exécutés ;
- le statut reste statique tant que les assets pilotes et la scène moteur ne sont pas matérialisés.

## 46. Livrables à conserver

Le lot du chapitre conserve :

1. `docs/art/VISUAL-BIBLE.md` ;
2. `docs/art/VISUAL-DECISIONS.yaml` ;
3. `docs/art/SHAPE-LANGUAGE.yaml` ;
4. `docs/art/palettes/PALETTE-TOKENS.yaml` ;
5. `docs/art/materials/MATERIAL-FAMILIES.yaml` ;
6. `docs/art/lighting/LIGHTING-PROFILES.yaml` ;
7. `docs/art/review/ART-REVIEW-GRID.md` ;
8. `docs/art/review/REVIEW-PROFILES.yaml` ;
9. `docs/art/review/ART-REVIEW-RECORD.yaml` ;
10. `docs/art/REFERENCE-REGISTER.yaml` ;
11. les fiches de familles personnages, environnements, UI et VFX ;
12. les futures captures et dérogations versionnées.

> **[LECTURE] Manifest du lot de direction artistique — Ne pas saisir.**

```yaml
visual_direction_package:
  version: "1.0.0"
  status: "static_definition_complete"
  source_files:
    - "docs/art/VISUAL-BIBLE.md"
    - "docs/art/VISUAL-DECISIONS.yaml"
    - "docs/art/SHAPE-LANGUAGE.yaml"
    - "docs/art/palettes/PALETTE-TOKENS.yaml"
    - "docs/art/materials/MATERIAL-FAMILIES.yaml"
    - "docs/art/lighting/LIGHTING-PROFILES.yaml"
    - "docs/art/review/ART-REVIEW-GRID.md"
  runtime_evidence:
    godot_scene_materialized: false
    pilot_assets_produced: 0
    captures_produced: 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le manifeste énumère les sources attendues et sépare leur définition documentaire des preuves runtime.

- **Statut :** `static_definition_complete` signifie que les contrats sont décrits, pas qu’ils ont été validés dans le moteur.

- **Booléens et compteurs :** Les valeurs `false` et `0` indiquent honnêtement l’absence de scène, d’assets et de captures.

- **Source canonique :** Les fichiers de bible et décisions sont des sources ; les futures captures restent des preuves dérivées.

- **Résultat attendu :** Une reprise de conversation ou de production peut identifier ce qui est défini et ce qui doit encore être matérialisé.

## 47. Références techniques officielles

Les décisions techniques de validation s’appuient sur les documentations officielles suivantes :

- Godot — ressource `Environment`, environnements et post-traitement ;
- Godot — `WorldEnvironment`, lumière ambiante, correspondance tonale, ajustements et LUT ;
- Godot — système de thèmes et éditeur de thèmes pour les interfaces ;
- W3C WAI — WCAG 2.2, notamment utilisation de la couleur, contraste minimal et contraste non textuel.

Ces références ne remplacent pas les captures dans la version exacte du projet. La documentation peut décrire une possibilité ; seule la scène matérialisée permet de confirmer le rendu, le coût et la lisibilité sur le matériel de référence.

## 48. Décisions retenues pour Project Asteria

`Project Asteria` adopte une direction artistique structurée autour de traces du temps, de réparations lisibles et d’une complexité hiérarchisée. Les formes naturelles sont principalement souples et irrégulières ; les structures institutionnelles emploient des axes et modules contrôlés ; les constructions improvisées montrent un réemploi fonctionnel.

La silhouette et la fonction précèdent le microdétail. Les palettes distinguent ambiance du monde et signaux fonctionnels. Un état important utilise toujours plusieurs canaux perceptuels. Les matériaux vieillissent selon contact, gravité, humidité, contrainte et entretien. La lumière et la correspondance tonale sont enregistrées dans des profils de revue afin de rendre les captures comparables.

Les variations culturelles, régionales, sociales et temporelles héritent de règles universelles mais dérivent de ressources, climat, techniques et usage. Les exceptions sont versionnées, limitées et révisables. La bible reste en définition statique tant que les assets pilotes, la scène Godot et les captures comparatives ne sont pas matérialisés.
