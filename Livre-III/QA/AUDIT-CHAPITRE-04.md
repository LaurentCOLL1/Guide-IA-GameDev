---
title: "Audit du Livre III — Chapitre 4"
id: "DOC-L3-QA-AUDIT-CH04"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH04"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T22:25:35+02:00"
last-verified: "2026-07-22T22:25:35+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 4 — Pipeline Blender et organisation des fichiers

## 1. Porte de création

Le chapitre a été créé depuis `main` après fusion et clôture QA du chapitre 3 du Livre III. Le chemin canonique, l’ordre, les livrables et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`. Aucun chapitre, audit, preuve, branche ou pull request concurrente du chapitre 4 n’existait avant l’ouverture du lot.

Le niveau GPT-5.6 Sol **Élevée** a été annoncé avant la rédaction en raison des dépendances entre conventions Blender, bibliothèques, chemins, export glTF, import Godot, automatisation et reproductibilité multi-poste. Cette recommandation reste absente du texte lecteur.

## 2. Résultats documentaires

- lignes finales : **2042** ;
- titres Markdown contrôlés hors blocs : **62** ;
- blocs de code ou de données : **48** ;
- blocs significatifs selon la revue : **48** ;
- marqueurs d’explication : **48** ;
- explications structurées hors section d’erreurs : **28** ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- titres dupliqués : **0** ;
- blocs significatifs dupliqués : **0** ;
- paragraphes longs dupliqués : **0** ;
- sections Solo ou Studio placées dans un bloc de code : **0** ;
- métadonnée de processus de raisonnement : **0** ;
- instruction de prochaine étape dans le texte lecteur : **0**.

## 3. Complétude pédagogique

Le chapitre couvre :

- qualification de Blender `4.5 LTS` comme branche documentaire et obligation d’épingler la version corrective réelle ;
- politique restrictive pour addons et extensions ;
- distinction entre source canonique, travail, cache, export, livraison et archive ;
- arborescence canonique de `Project Asteria` ;
- conventions d’identifiants, de fichiers, de datablocks et de collections ;
- template Blender avec unités métriques, axes, face avant, origine, pivot et transforms ;
- collections de travail, de publication et de validation ;
- Link, Append et Library Overrides avec responsabilités distinctes ;
- chemins relatifs, dépendances externes, textures et bibliothèques ;
- stratégie de sauvegarde, version immuable et reprise ;
- exclusion des caches et temporaires des sources publiées ;
- choix entre GLB, glTF séparé et import direct `.blend` ;
- asset de calibration mesurable ;
- validateur Python statique proposé pour Blender ;
- exécution PowerShell explicite et traitement du code de sortie ;
- contrat d’export, staging, empreintes et promotion vers une livraison ;
- import Godot, paramètres d’import et scène de validation ;
- boucle aller-retour bornée et préservation des scènes de gameplay ;
- réouverture sur une autre machine ;
- procédures Solo et Studio ;
- responsabilités, budgets, mesures, licences et sécurité ;
- checklists d’ouverture et de livraison ;
- migration contrôlée d’une version de Blender ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- livrables permanents et application à `Project Asteria`.

## 4. Comparaison au plan maître

Tous les éléments obligatoires du chapitre 4 sont présents :

- template Blender et préférences de projet ;
- unités métriques, orientations et conventions de pivots ;
- collections, bibliothèques liées et overrides ;
- arborescence source, travail, cache, export et archive ;
- stratégie de versions et sauvegardes ;
- formats d’échange, presets et limites ;
- test aller-retour Blender vers Godot ;
- template, conventions, arborescence, presets et checklists comme livrables ;
- parcours Solo et Studio ;
- critères de bonne échelle, orientation, position, réouverture et distinction des sources et sorties.

## 5. Frontières contrôlées

- le chapitre consomme les décisions des chapitres 1 à 3 sans modifier silencieusement le cahier des charges, la bible ou les concepts ;
- il prépare l’environnement de production sans enseigner la modélisation spécialisée ;
- il ne remplace pas le chapitre 5 pour l’analyse détaillée de provenance, licences, consentement et retrait ;
- il ne produit pas d’humain, créature, objet, bâtiment, terrain, végétation, matériau PBR, retopologie, rig, animation ou LOD définitif ;
- il ne présente pas un export techniquement valide comme asset artistique ou juridiquement approuvé ;
- il ne présente pas un `.blend`, un GLB ou un manifeste d’exemple comme matérialisé ;
- il ne revendique aucune exécution Blender, export, import Godot, réouverture multi-poste ou benchmark ;
- il ne construit pas le PDF du Livre III.

## 6. Vérification technique et sources

La revue statique a été comparée aux sources officielles consultées le 22 juillet 2026 :

- Blender `4.5 LTS` est une branche à support long ;
- les unités métriques et `Unit Scale` appartiennent aux propriétés de scène ; `Unit Scale` influence l’affichage des valeurs et ne répare pas seul la géométrie ;
- les collections organisent logiquement les objets et facilitent Link ou Append ;
- les chemins Blender relatifs utilisent la base du fichier `.blend` ;
- Link conserve une dépendance vers la bibliothèque source, Append copie les données, et Library Override fournit une édition locale contrôlée ;
- l’exporteur glTF de Blender propose notamment GLB, glTF séparé, sélection ou collection active, conversion d’axes et mémorisation des réglages ;
- Godot recommande glTF 2.0, accepte `.glb` et `.gltf`, et importe `.blend` en appelant Blender puis en passant par glTF ;
- l’import direct `.blend` exige Blender sur chaque poste et peut ajouter de la friction en équipe ;
- Godot utilise Y comme axe vertical et la convention d’asset orienté vers `+Z`, correspondant à `-Y` comme face avant dans Blender ;
- l’Import dock et les Advanced Import Settings configurent la ressource importée sans transformer Godot en source canonique du modèle.

Le mapping exact des options, le chemin de Blender et la version corrective doivent être vérifiés lors de la matérialisation. Aucun addon fictif, temps d’export, taille de GLB ou performance n’est inventé.

## 7. Explications pédagogiques

Les **48** blocs possèdent **48** marqueurs. Les **28** blocs hors erreurs expliquent selon le besoin : rôle, entrées, paramètres, types, dépendances, déroulement, sorties, effets de bord, invariants, sécurité, résultat attendu et limites.

Les dix cas d’erreurs respectent directement la séquence :

1. symptôme ou risque ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique structurée ne s’intercale dans ces séquences.

## 8. Contrôles particuliers

- front matter YAML valide ;
- identifiant `DOC-L3-CH04` unique dans le lot ;
- blocs YAML parsés sans erreur ;
- script Python parsé statiquement sans erreur de syntaxe ;
- tous les blocs possèdent un repère reconnu ;
- commandes PowerShell sous `[PS]` ;
- fichiers à créer ou modifier sous `[VSC]` avec chemin ;
- actions Blender et Godot sous `[APP]` ;
- structures non exécutables sous `[LECTURE]` ;
- sections Solo et Studio en Markdown ordinaire ;
- source, staging, export, livraison, cache et archive distingués ;
- états `not_executed`, `not_materialized`, `blocked` et valeurs nulles empêchent d’inventer des preuves ;
- le texte lecteur ne contient ni procédure QA interne, ni prochaine action, ni niveau de raisonnement.

## 9. Réserves

- Blender `4.5 LTS` non installé ni exécuté pour `Project Asteria` ;
- version corrective exacte non épinglée dans un manifeste réel ;
- addons et extensions réels non sélectionnés ni qualifiés ;
- template `.blend` non matérialisé ;
- bibliothèques liées et overrides non créés ;
- arborescence, manifests et presets réels non créés ;
- asset de calibration non modélisé ;
- script Blender proposé non exécuté ;
- export GLB/glTF non produit ;
- empreintes de source et d’export non calculées ;
- import Godot et scène de validation non matérialisés ;
- test aller-retour non exécuté ;
- réouverture sur une seconde machine non exécutée ;
- budgets de temps, taille et fiabilité non mesurés ;
- revue de licences détaillée laissée au chapitre 5 ;
- PDF du Livre III non construit conformément à la politique de fin de Livre.

## 10. Décision

Le chapitre 4 du Livre III est **accepté au niveau `static-review`**. Il fournit le template cible, les conventions de fichiers, la séparation des états, les règles de bibliothèques, le contrat glTF/GLB, le contrôle statique et la porte Blender vers Godot demandés, tout en maintenant ouvertes la matérialisation du pipeline, les mesures runtime et la validation juridique détaillée.
