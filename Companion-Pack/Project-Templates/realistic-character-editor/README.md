# Asteria Character Studio — fondation d’éditeur de personnage

Prototype Godot 4 destiné à devenir un éditeur de personnage humain réaliste inspiré des créateurs de personnages de jeux de simulation modernes.

Cette première livraison applique les principes du **Guide IA GameDev** : fonctionnement local, architecture modulaire, données versionnées, séparation entre asset visuel et logique métier, morphologies contrôlées, export GLB et documentation reproductible.

## État réel du prototype

Le projet est **fonctionnel**, mais le mannequin fourni est volontairement procédural et stylisé. Un rendu comparable à *The Sims* ou *inZOI* exige des assets humains sculptés, des textures haute définition, un rig facial, des cheveux et des correctifs de déformation qui ne peuvent pas être remplacés par du code seul.

Le prototype fournit déjà :

- un âge continu de `0` à `120` ans ;
- des stades nourrisson, petite enfance, enfance, adolescence, adulte et senior ;
- une croissance non linéaire de la taille et des proportions ;
- des réglages complets de silhouette, membres, volumes corporels, visage et peau ;
- une caméra orbitale avec zoom ;
- des préréglages d’âge ;
- la génération aléatoire ;
- la sauvegarde et le chargement JSON ;
- un schéma de données versionné ;
- un adaptateur de morph targets Blender/glTF ;
- le chargement automatique d’un corps réaliste GLB lorsqu’il est disponible ;
- un mannequin procédural de secours lorsque l’asset manque ;
- un emplacement de module anatomique adulte ;
- une politique automatique de représentation non explicite pour toute personne de moins de 18 ans ;
- des tests headless pour les règles d’âge, la croissance, les extrêmes et la sérialisation.

## Lancer le projet

1. Installer Godot Engine `4.7.x` ou une version 4.x compatible.
2. Ouvrir le dossier `realistic-character-editor` depuis le gestionnaire de projets Godot.
3. Lancer la scène principale avec `F6` ou le projet avec `F5`.
4. Utiliser le bouton droit de la souris pour tourner autour du personnage et la molette pour zoomer.

La sauvegarde est écrite dans :

```text
user://character_profile.json
```

Pour lancer les tests :

```powershell
godot --headless --path . --script res://tests/run_smoke_tests.gd
```

## Ajouter le corps réaliste

Exporter depuis Blender un personnage GLB respectant le contrat de shape keys, puis placer le fichier exactement ici :

```text
assets/characters/human_base.glb
```

Au lancement, `ProceduralAvatar` détecte automatiquement ce fichier, recherche le premier `MeshInstance3D` contenant des blend shapes, vérifie les morph targets attendues et applique les valeurs de `CharacterDefinition`. Si le fichier est absent ou invalide, l’éditeur utilise le mannequin procédural.

## Arborescence

```text
realistic-character-editor/
├── project.godot
├── manifest.json
├── README.md
├── assets/
│   └── characters/
│       └── README.md
├── data/
│   └── morphology_schema.json
├── docs/
│   ├── ASSET_PIPELINE.md
│   └── SAFETY_AND_SCOPE.md
├── scenes/
│   └── character_editor.tscn
├── scripts/
│   ├── blend_shape_driver.gd
│   ├── character_definition.gd
│   ├── character_editor.gd
│   ├── morphology_rules.gd
│   └── procedural_avatar.gd
└── tests/
    └── run_smoke_tests.gd
```

## Architecture

### `CharacterDefinition`

Source canonique des choix du joueur. La ressource contient l’âge, les paramètres morphologiques, l’apparence, le profil de présentation et les métadonnées du module anatomique adulte.

### `MorphologyRules`

Transforme les curseurs abstraits en dimensions cohérentes. Les courbes de croissance sont destinées à la production 3D, pas à l’évaluation biométrique ou médicale de personnes réelles.

### `ProceduralAvatar`

Charge d’abord `assets/characters/human_base.glb`. Lorsque cet asset n’existe pas, il génère un mannequin de validation avec des primitives Godot afin de tester l’interface, les sauvegardes, les proportions et les règles d’âge.

### `BlendShapeDriver`

Pont vers un véritable mesh Blender. Il associe les propriétés de `CharacterDefinition` à des shape keys signées et à des cibles d’âge exportées en GLB.

## Paramètres disponibles

### Corps

- taille générale ;
- volume de tête ;
- largeur des épaules ;
- volume thoracique ;
- largeur de la taille ;
- largeur du bassin ;
- longueur du torse ;
- longueur des bras ;
- longueur des jambes ;
- masse musculaire ;
- masse adipeuse ;
- taille des mains ;
- taille des pieds.

### Visage et peau

- largeur de la mâchoire ;
- volume du nez ;
- écartement des yeux ;
- pigmentation de peau ;
- rugosité de peau.

## Atteindre un rendu très réaliste

Le code ne doit pas déformer arbitrairement un seul mesh. La production réaliste doit utiliser :

1. une base humaine neutre dans Blender ;
2. une topologie identique pour tous les morphotypes compatibles ;
3. des shape keys principales et correctives ;
4. un squelette unique et des poids testés sur les extrêmes ;
5. des textures PBR de peau avec albédo, normales, roughness, micro-normales et masques ;
6. des cartes de rides pilotées par l’âge et les expressions ;
7. des yeux multicouches ;
8. des dents, une bouche et une langue séparées ;
9. des cheveux en cartes, courbes ou meshes optimisés ;
10. des vêtements adaptés aux morphologies et des masques de corps ;
11. plusieurs LOD ;
12. des tests de silhouette, de pose, de clipping et de performances dans Godot.

Le détail du contrat Blender se trouve dans `docs/ASSET_PIPELINE.md`.

## Anatomie reproductive

L’architecture prévoit un nœud `AdultAnatomySlot` et des métadonnées de profil. Le dépôt ne distribue aucun modèle génital explicite.

- Pour les personnages de moins de 18 ans, le module adulte est désactivé et le vêtement de confidentialité est obligatoire.
- Pour les personnages adultes, un studio peut connecter un module externe neutre, non érotisé et correctement licencié.
- Le module doit être séparé du corps principal, contrôlé par une option de confidentialité et exclu des miniatures, télémétries, captures automatiques et outils destinés aux mineurs.

## Limites connues

- Le mannequin procédural n’est pas photoréaliste.
- Les profils de présentation sont stockés mais ne pilotent pas encore un ensemble de morph targets dédié.
- Aucun rig, animation, vêtement, coiffure ou shader de peau avancé n’est fourni.
- Les courbes de croissance sont des hypothèses de conception à valider artistiquement.
- Les shape keys Blender doivent être sculptées et exportées séparément.
- Cette branche n’a pas pu être exécutée avec Godot dans l’environnement de création ; les tests sont fournis pour être lancés sur une machine équipée du moteur.

## Prochain jalon recommandé

Créer dans Blender un premier corps adulte neutre avec les 32 shape keys signées définies dans `blend_shape_driver.gd`, l’exporter vers `assets/characters/human_base.glb`, puis compléter les correctifs de pose, le shader de peau, les coiffures et les vêtements.

## Licence

Code proposé sous licence MIT, conformément à la politique du Companion Pack. Les assets humains, scans, textures et références ajoutés ultérieurement doivent conserver leur provenance et leur licence d’origine.
