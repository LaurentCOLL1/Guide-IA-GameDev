---
title: "Audit — Livre V, Fiche 18 : Référence graphique et 3D"
id: "DOC-L5-QA-AUDIT-CH18"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 18
audit-date: "2026-07-29T13:59:00+02:00"
last-verified: "2026-07-29T13:59:00+02:00"
audit-level: "static-review"
document-format: "reference-cards"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit — Fiche 18 : Référence graphique et 3D

## 1. Décision

**Décision : accepté au niveau `static-review`, sans revendication de production 3D ou de runtime.**

La fiche respecte le profil spécialisé du Livre V : index express, cartes techniques, matrices de choix, paragraphes courts, liens profonds vers les méthodes propriétaires et absence de tutoriel complet recopié.

Les valeurs chiffrées restent des conventions de repère ou des dimensions d’étalon déjà décidées dans le dépôt. Aucun budget de triangles, textures, LOD, rig, mémoire ou performance n’est présenté comme universel ou mesuré.

## 2. Périmètre du plan maître

Le plan maître demande :

- unités et axes ;
- formats et conventions ;
- PBR ;
- UV ;
- LOD ;
- rigs ;
- budgets contextualisés ;
- import et export ;
- erreurs visuelles fréquentes ;
- tables techniques, presets, schémas et checklists ;
- validation par comparaison aux assets pilotes.

La fiche couvre les dix premiers éléments sous forme de treize cartes, trois matrices et diagrammes compacts. Les presets restent décrits comme contrats versionnés et non comme fichiers exécutables. La comparaison aux assets pilotes n’a pas été exécutée, car aucun asset, preset ou scène du Companion Pack n’a été matérialisé.

## 3. Comparaison avec les chapitres voisins

### Fiche 17 — Patrons de gameplay

La fiche 17 possède machines à états, capacités, commandes, inventaires, quêtes, simulation et commits multi-autorités. La fiche 18 traite uniquement des représentations graphiques et 3D ; aucun mesh, socket, animation, suffixe ou import ne reçoit d’autorité gameplay.

### Fiche 19 — Référence audio

La fiche 19 possédera formats audio, fréquences, loudness, boucles, spatialisation, TTS/STT, bus et diagnostics audio. La fiche 18 s’arrête aux assets visuels et à leur chaîne 3D.

### Fiche 20 — Catalogue des erreurs et diagnostics

La fiche 18 contient un index compact de symptômes visuels relié aux corrections propriétaires. Elle ne remplace pas le catalogue transversal par outil, message, cause et version prévu à la fiche 20.

### Livre III — Méthodes propriétaires

Les méthodes complètes restent dans :

- chapitre 4 pour Blender, unités, axes, pivots, fichiers et échange ;
- chapitre 5 pour provenance, droits et licences des assets ;
- chapitre 16 pour textures, matériaux et PBR ;
- chapitre 17 pour retopologie, UV, cages et baking ;
- chapitre 18 pour LOD, HLOD, imposteurs et optimisation géométrique ;
- chapitre 19 pour rigging et skinning ;
- chapitre 20 pour animation ;
- chapitre 21 pour capture et retargeting ;
- chapitre 28 pour import, remaps, intégration et réimportation ;
- chapitre 29 pour la porte technique et artistique.

La fiche indexe les contrats communs sans recopier les procédures Blender, Godot, scripts, presets ou campagnes.

## 4. Forme documentaire

Mesures calculées sur le contenu final :

| Mesure | Valeur |
|---|---:|
| lignes | 500 |
| titres | 19 |
| cartes `<!-- l5:card -->` | 13 |
| matrices `<!-- l5:matrix -->` | 3 |
| liens Markdown | 91 |
| renvois vers les Livres I à IV | 63 |
| liens profonds vers les Livres I à IV | 35 |
| diagrammes compacts | 7 |
| blocs clôturés | 0 |
| titres dupliqués | 0 |

L’index express ouvre chaque carte ou matrice. Les identifiants `G3D-00` à `G3D-12` restent uniques.

## 5. Couverture des cartes

| Unité | Couverture |
|---|---|
| G3D-00 | contrat : famille, source, unité, repère, format, transformation, profil et preuve |
| Matrice A | entrée par problème, carte et chapitre propriétaire |
| G3D-01 | métrique, unités, axes Blender–Godot et transformations |
| G3D-02 | origines, pivots, AABB, sockets et collection d’export |
| Matrice B | GLB, glTF séparé, `.blend`, FBX, OBJ et surfaces Godot |
| G3D-03 | source, travail, cache, export, livraison, import et intégration |
| G3D-04 | canaux PBR, espaces colorimétriques et packing ORM |
| G3D-05 | seams, îlots, densité, marges, cages et baking |
| G3D-06 | silhouette, topologie, normales, tangentes, surfaces et sommets exportés |
| G3D-07 | LOD, HLOD, imposteurs, billboards, ombres, collisions et transitions |
| G3D-08 | squelette, rest pose, skinning, BoneMap, sockets et retargeting |
| G3D-09 | sidecars, caches, scènes importées, remaps, post-import et rollback |
| G3D-10 | géométrie, rendu, textures, animation, mémoire, temps, perception et protocole |
| G3D-11 | presets, profils, manifestes, checklists et pilotes documentaires |
| Matrice C | niveaux de preuve et portes de promotion |
| G3D-12 | symptômes visuels, vérifications, causes possibles et acceptation |

## 6. Exactitude des conventions

La fiche conserve les décisions de `Project Asteria` :

- une unité Blender représente un mètre ;
- `Unit Scale = 1.0` ne répare pas une géométrie incorrecte ;
- Blender utilise `Z` haut et `-Y` avant pour les assets orientés ;
- Godot utilise `Y` haut et `+Z` avant du modèle après conversion glTF ;
- GLB constitue la livraison de référence, glTF séparé sert à l’inspection et `.blend` direct reste une variante Solo qualifiée ;
- la source `.blend`, l’export, la livraison, le sidecar, le cache, la scène importée et la scène d’intégration ont des autorités distinctes ;
- les cartes de couleur et les cartes de données utilisent des traitements colorimétriques distincts ;
- la normale tangentielle de référence est compatible OpenGL pour Godot ;
- un LOD visuel ne contrôle ni collision ni autorité gameplay ;
- le squelette de déformation reste distinct du rig de contrôle ;
- les noms d’os seuls ne prouvent pas la compatibilité de retargeting ;
- la scène importée n’est pas une surface de personnalisation durable ;
- toute mesure est liée à un asset, une caméra, un renderer, une plateforme et un protocole.

## 7. Diagnostics et règle sémantique des erreurs

`G3D-12` est un index compact de symptômes, vérifications, causes possibles et sources propriétaires. Il ne porte pas le marqueur d’une section détaillée de correction et ne contient aucun faux couple exemple fautif/corrigé incomplet.

Les exemples détaillés restent dans les sections conformes des chapitres propriétaires. La future fiche 20 conservera le catalogue transversal des messages et procédures de diagnostic.

## 8. Validation documentaire légère

Workflow temporaire : `Temporary Livre V Chapter 18 Finalizer`.

Run final : `30451780779`.

Tête source : `5ef3d50223e12e82445aa40a04d6dd469b22bb05`.

Commandes exécutées sans PDF :

- `python tools/validate_chapters.py --root . --report dist/QA-CHAPTERS.md` ;
- `python tools/validate_livre_v_references.py --check` ;
- `python tools/check_code_explanation_structure.py --check` ;
- `python tools/check_context_markers.py --check` ;
- `python tools/audit_contextes_semantiques.py --check`.

Les validations ont réussi sur le lot final avant commit. Aucun workflow PDF, Pandoc, XeLaTeX, qpdf ou rendu visuel n’a été lancé.

## 9. Doublons, liens et repères

- aucun titre dupliqué ;
- aucun bloc clôturé à expliquer ;
- aucun paragraphe long recopié depuis les chapitres propriétaires ;
- ordre continu du Livre V maintenu dans `contents.txt` ;
- chemin canonique et identifiant `DOC-L5-CH18` conformes ;
- densité de renvois vers les Livres I à IV supérieure au minimum du protocole ;
- plusieurs liens profonds visent des sous-sections réellement présentes ;
- aucune structure tutoriel interdite ;
- aucune commande à exécuter ;
- aucune URL externe ou brute ;
- aucun PDF intermédiaire.

## 10. Niveau de preuve

Les assertions techniques sont limitées aux contrats déjà consignés dans le dépôt. La fiche ne revendique pas :

- l’exécution de Blender, Godot ou de l’importeur glTF ;
- la création d’un GLB, mesh, texture, matériau, UV, cage ou bake ;
- la création d’un LOD, HLOD, imposteur, billboard ou proxy ;
- la création d’un rig, skinning, animation ou retargeting ;
- la création d’un preset, sidecar, remap ou scène d’intégration ;
- une comparaison de pilotes ou une revue artistique ;
- une mesure CPU, GPU, RAM, VRAM, import ou chargement ;
- une campagne de plateforme ou de renderer ;
- une donnée utilisateur, personnelle ou de production.

Le niveau reste `static-review`.

## 11. Intégrité

Empreinte SHA-256 du chapitre :

`a0c694103dc1385e5168ad4653c7081058888fe4e3ae04625d3f00232cf8d015`

L’empreinte de cet audit est enregistrée dans la preuve finale.

## 12. Réserves

- aucun asset pilote matérialisé ou comparé malgré le critère futur du plan maître ;
- aucun preset, checklist exécutable ou fixture permanente du Companion Pack créé ;
- aucune importation, réimportation ou comparaison Blender–Godot exécutée ;
- aucune capture, mesure de performance, mémoire ou qualité runtime ;
- aucune qualification Mobile, Compatibility ou autre plateforme ;
- aucune approbation artistique ou juridique organisationnelle ;
- aucun PDF produit ;
- licence globale et accessibilité avancée du PDF toujours ouvertes.

## 13. Critère d’acceptation

La fiche est acceptée parce qu’un lecteur peut :

1. trouver immédiatement la convention ou le symptôme recherché ;
2. distinguer source, export, livraison, import et intégration ;
3. vérifier unités, axes, pivot et AABB ;
4. relier canaux PBR, UV, baking et géométrie à leurs méthodes propriétaires ;
5. distinguer LOD, HLOD, imposteur et proxies ;
6. relier rig, skinning et retargeting sans déplacer l’autorité gameplay ;
7. choisir un chemin d’échange selon les données à préserver ;
8. traiter budgets et presets comme contextuels et versionnés ;
9. distinguer revue statique, import, mesure et décision humaine ;
10. comprendre qu’aucun asset ou runtime n’a été exécuté.
