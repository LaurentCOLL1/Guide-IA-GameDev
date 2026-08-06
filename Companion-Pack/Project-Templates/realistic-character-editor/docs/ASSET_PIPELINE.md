# Pipeline d’assets réalistes — Blender vers Godot

## Objectif

Remplacer le mannequin procédural par un humain réaliste sans modifier l’interface ni le format de sauvegarde.

## Versions de référence

- Blender `5.2.x` ;
- Godot `4.7.x` ;
- échange `glTF 2.0` dans un conteneur `.glb` ;
- unités métriques ;
- axe vertical `Y` côté Godot après export.

## Contrat de base

Le corps source doit conserver :

- une topologie commune entre les variantes ;
- un ordre de sommets stable ;
- des frontières compatibles pour la tête, les mains, les pieds et les modules ;
- un squelette unique ;
- des UV stables ;
- des noms reproductibles ;
- une provenance documentée.

## Shape keys obligatoires

Le fichier `scripts/blend_shape_driver.gd` définit le contrat exact. Chaque paramètre signé utilise une cible négative et une cible positive.

```text
morph_stature_neg          morph_stature_pos
morph_head_small           morph_head_large
morph_shoulders_narrow     morph_shoulders_wide
morph_chest_small          morph_chest_large
morph_waist_narrow         morph_waist_wide
morph_hips_narrow          morph_hips_wide
morph_torso_short          morph_torso_long
morph_arms_short           morph_arms_long
morph_legs_short           morph_legs_long
morph_muscle_low           morph_muscle_high
morph_adipose_low          morph_adipose_high
morph_hands_small          morph_hands_large
morph_feet_small           morph_feet_large
morph_jaw_narrow           morph_jaw_wide
morph_nose_small           morph_nose_large
morph_eyes_close           morph_eyes_wide
```

Cibles d’âge :

```text
age_infant
age_early_childhood
age_childhood
age_adolescence
age_young_adult
age_mature_adult
age_elder
```

## Règles de sculpture

1. Travailler depuis une base neutre et symétrique.
2. Préserver la position des articulations compatibles avec le rig.
3. Éviter les changements de topologie entre variantes.
4. Créer des correctifs de pose séparés des morphologies principales.
5. Tester les combinaisons extrêmes, pas seulement chaque curseur isolément.
6. Éviter qu’un morphotype déduise automatiquement une origine, une personnalité ou une capacité.
7. Traiter l’âge par plusieurs couches : proportions, volumes, posture, peau, cheveux et rides.

## Rig et déformations

Le rig de production doit au minimum prévoir :

- bassin, colonne, cou et tête ;
- clavicule, bras, avant-bras, mains et doigts ;
- cuisses, jambes, pieds et orteils ;
- mâchoire, yeux et paupières ;
- bones correctifs pour épaules, hanches, genoux et coudes ;
- correctifs de volume pilotés par la pose.

Les proportions extrêmes doivent être testées sur :

- bras levés ;
- accroupissement ;
- torsion de colonne ;
- marche ;
- course ;
- assise ;
- expressions faciales ;
- interaction avec les vêtements.

## Peau réaliste

Prévoir au minimum :

- albédo sans lumière peinte ;
- normal map principale ;
- micro-normal de pores ;
- roughness ;
- masque de sous-surface ou approximation compatible ;
- masques de pigmentation et rougeur ;
- cartes de rides ou détails pilotés par l’âge ;
- variations localisées pour lèvres, oreilles, mains, genoux et coudes.

## Import Godot

1. Exporter le personnage en `.glb` avec armature, skin, matériaux et shape keys.
2. Importer le GLB dans `res://assets/characters/`.
3. Créer une scène héritée pour éviter de modifier directement la scène importée.
4. Repérer le `MeshInstance3D` du corps.
5. Appeler `BlendShapeDriver.validate_contract(mesh_instance)` pendant les tests.
6. Appliquer `BlendShapeDriver.apply(mesh_instance, character_definition)` à chaque modification.
7. Conserver le mannequin procédural comme mode dégradé lorsque l’asset est absent.

## Modules anatomiques adultes

Les modules adultes doivent :

- être séparés du corps canonique ;
- partager le rig et les frontières nécessaires ;
- être chargés uniquement lorsque `age_years >= 18` ;
- rester masqués par défaut ;
- disposer de leur propre provenance et licence ;
- ne jamais être inclus dans un preset mineur ;
- être exclus des captures automatiques et des miniatures.

## Validation

Bloquer l’asset si l’un des points suivants échoue :

- shape key manquante ;
- ordre de sommets incompatible ;
- clipping majeur ;
- volume détruit en pose ;
- frontière de module visible ;
- UV étirés ;
- matériau non traçable ;
- module adulte accessible à un personnage mineur ;
- budget de triangles ou mémoire non documenté.
