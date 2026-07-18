---
title: "Plan maître détaillé — Livre III"
id: "DOC-PLAN-L3"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
book: "Livre III"
chapter-count: 30
---

# Plan maître détaillé — Livre III

> **Titre du Livre :** Production des contenus et des assets  
> **Statut :** non commencé  
> **Rôle :** transformer la direction artistique en assets traçables, optimisés et directement intégrables dans Godot.

## Règles transversales du Livre III

Chaque chapitre doit couvrir, selon le sujet :

- provenance et droits d’utilisation ;
- conventions de fichiers, dossiers, noms et versions ;
- budget technique mesurable ;
- variante Solo et variante Studio ;
- importation ou exploitation dans Godot ;
- contrôle visuel et technique ;
- reprise après erreur ;
- livrables réutilisables dans le Companion Pack.

Un asset ne peut pas être déclaré terminé sans : source, licence, auteur ou outil, version, paramètres de génération, dimensions, formats, dépendances, contraintes d’utilisation et validation dans Godot.

## Chapitre 1 — Préproduction et cahier des charges artistique

**Objectifs**

- traduire la vision du jeu en contraintes visuelles et techniques ;
- définir catégories d’assets, quantités, priorités, budgets et niveaux de qualité ;
- établir calendrier, responsabilités, risques et critères d’acceptation ;
- distinguer prototype, vertical slice, production et finition.

**Livrables**

- cahier des charges artistique ;
- matrice des assets ;
- budgets polygones, textures, matériaux, rigs et animations ;
- calendrier de production ;
- checklist d’acceptation.

**Frontière et validation**

Le chapitre ne choisit pas encore le style final : il prépare les décisions du chapitre 2. Validation par cohérence entre ambitions, matériel de référence, temps disponible et volume d’assets.

## Chapitre 2 — Direction artistique et bible visuelle

**Objectifs**

- définir formes, silhouettes, proportions, couleurs, lumière et matériaux ;
- cadrer le niveau de réalisme et les variations autorisées ;
- établir règles de cohérence entre personnages, environnements, UI et VFX ;
- définir des exemples conformes et non conformes.

**Livrables**

- bible visuelle versionnée ;
- palettes, références de matériaux et règles d’éclairage ;
- planches de silhouettes et échelles ;
- critères de revue artistique.

**Frontière et validation**

Le chapitre définit la direction, sans produire les assets définitifs. Validation par tests sur quelques assets pilotes et lisibilité dans Godot.

## Chapitre 3 — Références, concept art et ComfyUI

**Objectifs**

- collecter légalement des références ;
- organiser moodboards, annotations et provenance ;
- créer des concepts avec ComfyUI sans confondre concept et asset final ;
- versionner workflows, modèles, seeds, prompts et paramètres ;
- sélectionner humainement les propositions cohérentes.

**Livrables**

- dossiers de références sourcées ;
- workflows ComfyUI JSON ;
- manifestes de modèles et licences ;
- planches de concepts annotées ;
- rapport de sélection.

**Frontière et validation**

Aucun concept généré n’est directement considéré comme texture ou modèle final. Validation par conformité à la bible visuelle et traçabilité complète.

## Chapitre 4 — Pipeline Blender et organisation des fichiers

**Objectifs**

- configurer unités, axes, échelle, collections et conventions ;
- définir fichiers sources, bibliothèques liées, variantes et exports ;
- organiser sauvegardes, versions, caches et rendus ;
- établir un pipeline reproductible de Blender vers Godot.

**Livrables**

- template Blender ;
- conventions de collections et nommage ;
- arborescence canonique ;
- presets d’export ;
- checklist d’ouverture et de livraison.

**Frontière et validation**

Le chapitre prépare l’environnement commun ; les techniques de modélisation viennent ensuite. Validation par export d’un asset test correctement orienté, dimensionné et importé.

## Chapitre 5 — Provenance, licences et validation des assets

**Objectifs**

- distinguer licence, droit d’auteur, consentement, marque et droit à l’image ;
- enregistrer source, auteur, outil, version, restrictions et modifications ;
- gérer assets générés, achetés, libres et créés en interne ;
- bloquer les éléments non redistribuables ou juridiquement incertains.

**Livrables**

- registre de provenance ;
- modèle de fiche d’asset ;
- matrice des licences ;
- procédure de retrait et remplacement ;
- contrôles automatiques minimaux.

**Frontière et validation**

Le chapitre ne fournit pas d’avis juridique personnalisé. Validation par capacité à retracer chaque asset jusqu’à sa source et à déterminer ses droits de distribution.

## Chapitre 6 — Création des humains

**Objectifs**

- étudier proportions, anatomie, diversité et variations ;
- construire une base modulaire compatible vêtements et animations ;
- gérer topologie, déformations, niveaux de détail et textures ;
- éviter stéréotypes, incohérences anatomiques et surcoût inutile.

**Livrables**

- base humaine de référence ;
- variantes morphologiques ;
- guide de proportions ;
- budgets et LOD ;
- scène Godot de validation.

**Frontière et validation**

Les détails du visage, des cheveux et vêtements sont approfondis aux chapitres 10 et 11. Validation par poses extrêmes, silhouettes et performances.

## Chapitre 7 — Création des humanoïdes

**Objectifs**

- adapter anatomie et proportions à des espèces humanoïdes ;
- conserver compatibilité avec rigs, vêtements et interactions ;
- définir éléments modulaires et variations culturelles ;
- maintenir lisibilité et crédibilité biologique.

**Livrables**

- bases humanoïdes ;
- règles d’adaptation anatomique ;
- profils de rig ;
- matrice de compatibilité des équipements.

**Frontière et validation**

Ne couvre pas les créatures non humanoïdes du chapitre 9. Validation par locomotion, équipement et silhouette à distance.

## Chapitre 8 — Création des animaux

**Objectifs**

- analyser anatomie, locomotion et comportement ;
- gérer quadrupèdes, oiseaux, poissons et autres familles ;
- prévoir pelage, plumes, écailles, variantes et LOD ;
- préparer rigs et cycles adaptés.

**Livrables**

- modèles animaux pilotes ;
- fiches anatomiques ;
- rigs de base ;
- cycles de locomotion ;
- budgets par distance.

**Frontière et validation**

Les comportements de simulation appartiennent au Livre II. Validation par mouvements crédibles, contacts au sol et performance en groupe.

## Chapitre 9 — Création des créatures

**Objectifs**

- concevoir une anatomie fantastique crédible ;
- relier silhouette, capacités, habitat et gameplay ;
- anticiper rig, collisions, attaques et points faibles ;
- créer variantes sans perdre l’identité visuelle.

**Livrables**

- fiches de créatures ;
- planches anatomiques ;
- modèles pilotes ;
- rigs et volumes de collision ;
- tests de lisibilité gameplay.

**Frontière et validation**

Le chapitre crée l’asset, pas son IA. Validation par cohérence fonctionnelle, animation possible et reconnaissance immédiate.

## Chapitre 10 — Visages, peau, yeux, cheveux et pilosité

**Objectifs**

- construire visages et expressions crédibles ;
- gérer peau, yeux, dents, cheveux, barbe, fourrure et transparence ;
- choisir entre géométrie, cartes, groom et shaders ;
- équilibrer réalisme et performances.

**Livrables**

- tête de référence ;
- matériaux peau et yeux ;
- bibliothèque de cheveux/pilosité ;
- blendshapes ou système facial ;
- profils LOD.

**Frontière et validation**

La synchronisation labiale complète est au chapitre 27. Validation par gros plans, éclairages variés et animation faciale.

## Chapitre 11 — Vêtements, armures et accessoires

**Objectifs**

- créer couches, attaches, variantes et tailles ;
- gérer clipping, déformation, simulation et collisions ;
- concevoir modularité et compatibilité morphologique ;
- optimiser matériaux, géométrie et LOD.

**Livrables**

- kits vestimentaires ;
- règles de layering ;
- profils de skinning ;
- collisions de simulation ;
- matrice de compatibilité.

**Frontière et validation**

Les objets tenus et armes sont au chapitre 12. Validation par mouvements extrêmes, combinaisons d’équipement et absence de clipping majeur.

## Chapitre 12 — Objets, équipements et armes

**Objectifs**

- respecter échelle, prise en main et usage ;
- définir états, variantes, dégâts visuels et usure ;
- préparer pivots, sockets, collisions et LOD ;
- relier asset visuel et données de gameplay sans les confondre.

**Livrables**

- bibliothèque d’objets pilotes ;
- conventions de pivots et sockets ;
- collisions ;
- LOD ;
- scènes Godot d’équipement.

**Frontière et validation**

Les règles d’inventaire et combat appartiennent au Livre II. Validation par animation, interaction et cohérence d’échelle.

## Chapitre 13 — Architecture, bâtiments et kits modulaires

**Objectifs**

- définir métriques, modules, snapping et variations ;
- concevoir murs, sols, toits, ouvertures et intérieurs ;
- gérer collisions, destruction, occlusion et navigation ;
- éviter répétition visuelle et erreurs d’assemblage.

**Livrables**

- kit modulaire ;
- grille métrique ;
- règles d’assemblage ;
- scènes de test ;
- budgets et LOD.

**Frontière et validation**

La construction par le joueur est traitée dans le Livre II. Validation par assemblage de plusieurs bâtiments sans trous ni écarts.

## Chapitre 14 — Terrains, paysages et mondes ouverts

**Objectifs**

- créer heightmaps, reliefs, routes, rivières et littoraux ;
- organiser tuiles, streaming et niveaux de détail ;
- gérer eau, collisions, navigation et transitions ;
- préparer grands espaces sans épuiser mémoire et temps de chargement.

**Livrables**

- terrain pilote ;
- découpage spatial ;
- profils de streaming ;
- matériaux de terrain ;
- scène de benchmark.

**Frontière et validation**

La simulation écologique est au Livre II. Validation par traversal, streaming, mémoire et absence de ruptures visibles.

## Chapitre 15 — Végétation et biomes

**Objectifs**

- définir espèces, densités, saisons et règles de distribution ;
- créer arbres, plantes, herbes et débris ;
- gérer instancing, imposteurs, vent et interaction ;
- assurer cohérence écologique et performance.

**Livrables**

- bibliothèque végétale ;
- profils de biome ;
- cartes de distribution ;
- shaders de vent ;
- benchmark de densité.

**Frontière et validation**

Le système dynamique de biome appartient au Livre II. Validation par diversité, distance d’affichage et coût GPU/CPU.

## Chapitre 16 — Textures, matériaux et pipeline PBR

**Objectifs**

- expliquer albedo, normal, roughness, metallic, AO, height et emissive ;
- gérer espaces colorimétriques, compression et résolutions ;
- définir texel density et bibliothèques de matériaux ;
- créer matériaux Godot cohérents.

**Livrables**

- guide PBR ;
- presets d’export ;
- bibliothèque de matériaux ;
- profils de compression ;
- scène d’éclairage de référence.

**Frontière et validation**

Le chapitre ne traite pas encore UV et baking en profondeur. Validation sous plusieurs éclairages et sur le matériel de référence.

## Chapitre 17 — UV, retopologie et baking

**Objectifs**

- produire une topologie animable et optimisée ;
- déplier UV avec densité cohérente ;
- créer cages et baker normales, AO et autres maps ;
- diagnostiquer artefacts, seams et tangentes.

**Livrables**

- maillage haute et basse résolution ;
- UV ;
- cages ;
- textures bakées ;
- rapport de contrôle.

**Frontière et validation**

Le chapitre 18 traite les LOD après création du modèle final. Validation par absence d’artefacts majeurs et comparaison high/low poly.

## Chapitre 18 — LOD, imposteurs et optimisation géométrique

**Objectifs**

- définir seuils de distance et budgets ;
- créer LOD manuels ou automatiques contrôlés ;
- produire imposteurs et billboards ;
- gérer transitions et popping ;
- mesurer le gain réel.

**Livrables**

- chaîne LOD ;
- imposteurs ;
- profils de distance ;
- scène de benchmark ;
- tableau avant/après.

**Frontière et validation**

L’optimisation globale du jeu appartient au Livre IV. Validation par qualité perceptuelle et réduction mesurée du coût.

## Chapitre 19 — Rigging et skinning

**Objectifs**

- créer squelettes, contrôleurs et contraintes ;
- définir nomenclature et orientations ;
- peindre les poids et corriger les déformations ;
- préparer retargeting, accessoires et export.

**Livrables**

- rigs de référence ;
- conventions d’os ;
- profils de skinning ;
- poses de test ;
- fichiers d’export.

**Frontière et validation**

L’animation est au chapitre 20. Validation par poses extrêmes, absence d’écrasement et compatibilité Godot.

## Chapitre 20 — Animation procédurale et animation par keyframes

**Objectifs**

- créer poses, cycles, transitions et courbes ;
- utiliser couches, blend trees et animation procédurale ;
- gérer root motion, événements et boucles ;
- organiser bibliothèques et variantes.

**Livrables**

- cycles de base ;
- bibliothèque d’animations ;
- blend tree pilote ;
- profils d’export ;
- scène Godot animée.

**Frontière et validation**

La mocap est au chapitre 21. Validation par transitions fluides, vitesse cohérente et absence de glissement.

## Chapitre 21 — Capture de mouvement et retargeting

**Objectifs**

- sélectionner sources et licences ;
- nettoyer bruit, glissements et collisions ;
- mapper squelettes ;
- retargeter vers plusieurs morphologies ;
- corriger manuellement les résultats.

**Livrables**

- sessions ou clips sourcés ;
- profils de mapping ;
- animations nettoyées ;
- rapport de corrections ;
- tests multi-rigs.

**Frontière et validation**

La mocap ne remplace pas la direction d’animation. Validation par contacts, rythme et cohérence avec la personnalité du personnage.

## Chapitre 22 — Cinématiques, caméras et mise en scène

**Objectifs**

- transformer storyboard en séquence ;
- gérer focales, mouvements, cadrage et continuité ;
- synchroniser animation, audio, lumière et effets ;
- préparer timelines, reprises et export.

**Livrables**

- storyboard ;
- animatique ;
- séquence Godot ;
- liste de plans ;
- versions de revue.

**Frontière et validation**

La caméra de gameplay est au Livre II. Validation par lisibilité narrative, rythme et fonctionnement dans le build.

## Chapitre 23 — Effets visuels, particules et simulations

**Objectifs**

- créer feu, fumée, impacts, magie, météo et débris ;
- choisir GPU/CPU, shader, particules ou simulation pré-calculée ;
- gérer collisions, pooling, LOD et lumière ;
- établir budgets par contexte.

**Livrables**

- bibliothèque VFX ;
- presets ;
- scènes de test ;
- budgets ;
- variantes de qualité.

**Frontière et validation**

Les effets ne doivent pas masquer l’information de gameplay. Validation par lisibilité, coût et comportement sur plusieurs distances.

## Chapitre 24 — Interface utilisateur

**Objectifs**

- définir composants, thèmes, grilles et hiérarchie ;
- créer menus, HUD, inventaires et fenêtres ;
- gérer résolutions, ratios, clavier, souris et manette ;
- intégrer icônes, animations et feedback.

**Livrables**

- design system UI ;
- composants réutilisables ;
- écrans pilotes ;
- thème Godot ;
- tests multi-résolution.

**Frontière et validation**

Les règles UX et accessibilité sont approfondies au chapitre 25. Validation par cohérence visuelle et navigation complète.

## Chapitre 25 — Expérience utilisateur et accessibilité visuelle

**Objectifs**

- améliorer lisibilité, compréhension et feedback ;
- gérer tailles, contrastes, daltonisme, motion et focus ;
- réduire charge cognitive ;
- tester navigation et erreurs utilisateur.

**Livrables**

- checklist UX ;
- profils d’accessibilité ;
- variantes de contraste ;
- scénarios de tests ;
- rapport utilisateur.

**Frontière et validation**

L’accessibilité globale audio/commandes est reprise au Livre IV. Validation avec tests réels ou protocoles documentés.

## Chapitre 26 — Voix, bruitages, ambiances et musique

**Objectifs**

- organiser enregistrement, génération, montage et mixage ;
- gérer formats, loudness, boucles, spatialisation et variations ;
- documenter consentement, licences et provenance ;
- intégrer bus audio et événements dans Godot.

**Livrables**

- bibliothèque audio ;
- manifestes de voix ;
- presets de mix ;
- scènes audio ;
- rapport de loudness.

**Frontière et validation**

Les outils d’installation audio sont au Livre I. Validation par écoute, niveaux, transitions et consommation mémoire.

## Chapitre 27 — Synchronisation labiale et animation faciale

**Objectifs**

- expliquer phonèmes, visèmes et blendshapes ;
- générer ou annoter timings ;
- synchroniser voix, visage, yeux et gestes ;
- gérer langues, performances et LOD facial.

**Livrables**

- jeu de visèmes ;
- pipeline de timing ;
- animation pilote ;
- profils par langue ;
- tests gros plan/distance.

**Frontière et validation**

Le chapitre ne remplace pas le jeu d’acteur. Validation par intelligibilité, naturel et stabilité sur plusieurs voix.

## Chapitre 28 — Importation et intégration dans Godot

**Objectifs**

- configurer presets d’import ;
- gérer scènes importées, héritées et réimportation ;
- associer matériaux, animations, collisions et scripts ;
- éviter modifications perdues lors d’un réimport ;
- automatiser les réglages répétitifs.

**Livrables**

- presets d’import ;
- scènes d’intégration ;
- scripts post-import ;
- matrice format/usage ;
- checklist de réimport.

**Frontière et validation**

Le chapitre consolide les assets produits précédemment. Validation par réimport reproductible sans perte de données.

## Chapitre 29 — Validation technique et artistique des assets

**Objectifs**

- définir portes qualité ;
- comparer à la bible visuelle et aux budgets ;
- vérifier formats, pivots, matériaux, collisions, rigs et LOD ;
- produire rapports, statuts et demandes de correction.

**Livrables**

- checklist universelle ;
- scènes de validation ;
- rapport d’asset ;
- système de statut ;
- critères d’acceptation finale.

**Frontière et validation**

Ce chapitre ne remplace pas la QA du jeu complet. Validation par répétabilité du contrôle par une autre personne ou un script.

## Chapitre 30 — Automatisation Blender, ComfyUI et production en lots

**Objectifs**

- automatiser tâches répétitives sans masquer les décisions artistiques ;
- utiliser scripts Blender, queues ComfyUI et manifestes ;
- gérer lots, reprise, erreurs, seeds et déterminisme ;
- enregistrer provenance et rapports ;
- intégrer les contrôles à la CI.

**Livrables**

- scripts de lots ;
- templates de manifestes ;
- workflows automatisés ;
- rapports ;
- exemples du Companion Pack.

**Frontière et validation**

L’automatisation ne doit jamais valider seule la qualité artistique. Validation par reprise après échec, traçabilité et comparaison manuelle d’échantillons.

## Critères de clôture du Livre III

- les 30 chapitres sont rédigés, repérés et audités ;
- un asset pilote complet traverse la chaîne concept → Blender/ComfyUI → validation → Godot ;
- les règles de provenance et licences sont appliquées ;
- les budgets sont mesurés sur le matériel de référence ;
- les livrables réutilisables sont versés au Companion Pack ;
- le PDF est compilé et inspecté ;
- `CONTINUITE-PROJET.md`, `ROADMAP.md`, l’index et les preuves QA sont à jour.
