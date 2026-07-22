---
title: "Audit du Livre III — Chapitre 3"
id: "DOC-L3-QA-AUDIT-CH03"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH03"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T20:42:28+02:00"
last-verified: "2026-07-22T20:42:28+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 3 — Références, concept art et ComfyUI

## 1. Porte de création

Le chapitre a été créé depuis `main` après fusion et clôture QA du chapitre 2 du Livre III. Le chemin canonique, l’ordre et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`. Aucun chapitre, audit, branche `ch03` ou pull request ouverte concurrente n’existait avant l’ouverture du lot.

Le texte lecteur ne contient aucune donnée de pilotage de conversation, aucun niveau de raisonnement conseillé, aucune procédure QA interne et aucune annonce du chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **2674** ;
- titres Markdown contrôlés hors blocs : **53** ;
- blocs de code ou de données : **48** ;
- blocs significatifs selon le validateur : **46** ;
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

- distinction entre inspiration, référence, concept, source de production et asset final ;
- questions visuelles fermées avant collecte ;
- registre de provenance, droits, restrictions et contexte d’usage ;
- quarantaine des fichiers externes et empreintes ;
- moodboards annotés et planches comparatives ;
- ComfyUI `0.28.0` comme référence documentaire ;
- séparation entre profil de recherche et profil qualifié ;
- priorité aux nœuds Core ;
- workflow JSON comme source canonique versionnée ;
- manifestes de modèles, custom nodes, environnement et runs ;
- seed replacée dans l’ensemble des paramètres et dépendances ;
- prompts structurés et matrices d’expériences ;
- contrôle des images d’entrée et des métadonnées incorporées ;
- critique anatomique, matérielle, culturelle et fonctionnelle ;
- sélection humaine, rapport de rejet et consolidation ;
- sécurité des custom nodes et principe de moindre dépendance ;
- vérification Python bornée des manifestes et empreintes ;
- contrat de planche de référence dans Godot sans import de concept comme asset ;
- budgets d’itération, règle d’arrêt et parcours Solo ou Studio ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- porte de transmission vers les chapitres de production.

## 4. Frontières contrôlées

- le chapitre applique la bible du chapitre 2 sans la modifier silencieusement ;
- il ne remplace pas le chapitre 5 pour l’analyse juridique détaillée des licences ;
- il ne qualifie pas Blender, les addons, l’organisation des fichiers ou l’export Godot du chapitre 4 ;
- il ne transforme aucune image générée en texture, modèle ou asset final ;
- il ne produit ni retopologie, matériau PBR, rig, animation, VFX, audio ou UI définitive ;
- il ne présente pas une seed comme garantie suffisante de reproductibilité ;
- il ne présente pas un workflow embarqué dans une image comme preuve de droits ;
- il ne revendique aucune accélération AMD Windows sur la RX 6750 XT ;
- il ne donne aucun avis juridique personnalisé.

## 5. Vérification technique et sources

La revue statique a été comparée aux sources officielles consultées le 22 juillet 2026 :

- la version stable ComfyUI `0.28.0` a été publiée le 15 juillet 2026 ;
- les workflows ComfyUI sont des graphes sérialisables en JSON ;
- les images compatibles peuvent embarquer le workflow dans leurs métadonnées ;
- les custom nodes sont du code exécutable et doivent provenir de sources fiables ;
- le registre ComfyUI publie des exigences de sécurité pour les extensions ;
- la prise en charge AMD Windows officielle documentée reste expérimentale et ne qualifie pas RDNA2 ;
- le dépôt officiel ComfyUI est distribué sous GPL-3.0.

Les modèles, checkpoints, LoRA, entrées, custom nodes et licences réellement choisis restent à vérifier lors de leur adoption. Aucun modèle fictif ne reçoit une licence inventée.

## 6. Explications pédagogiques

Les **48** blocs possèdent **48** marqueurs. Les **28** blocs hors erreurs comportent au moins quatre rubriques spécifiques et expliquent selon le besoin : rôle, champs, types, paramètres, ordre, invariants, sécurité, résultat attendu et frontières.

Les dix cas d’erreurs respectent directement la séquence :

1. symptôme ou risque ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique structurée ne s’intercale dans les séquences d’erreurs.

## 7. Contrôles particuliers

- tous les blocs possèdent un repère d’utilisation reconnu ;
- les fichiers à créer ou modifier utilisent `[VSC]` avec un chemin ;
- les commandes PowerShell utilisent `[PS]` ;
- les interfaces graphiques utilisent `[APP]` ou `[WEB]` ;
- les structures et tableaux de lecture utilisent `[LECTURE]` ;
- les sections Solo et Studio utilisent du Markdown ordinaire ;
- les identifiants de références, concepts, workflows, modèles et runs restent distincts ;
- les états `unknown`, `blocked`, `not_executed` et `production_ready: false` évitent d’inventer une qualification ;
- les copies destinées au partage sont séparées des sources de travail ;
- aucune image, workflow, modèle ou scène réelle n’est revendiqué comme produit.

## 8. Réserves

- Starter Kit non matérialisé ;
- dossiers de références et moodboards réels non créés ;
- références, auteurs, licences et droits réels non renseignés ;
- environnement ComfyUI `0.28.0` non installé ni exécuté dans le projet ;
- modèles, checkpoints, LoRA et custom nodes non sélectionnés ni qualifiés ;
- prise en charge AMD Windows de la RX 6750 XT non qualifiée ;
- workflows JSON et manifestes réels non produits ;
- sorties, planches et rapports de sélection non générés ;
- vérificateur Python proposé non exécuté sur un dossier réel ;
- planche Godot non matérialisée ;
- revue anatomique, matérielle, culturelle, Solo ou Studio non exécutée ;
- performances, VRAM, durées et tailles de lots non mesurées ;
- PDF du Livre III non construit, conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 3 du Livre III est **accepté au niveau `static-review`**. Il fournit la chaîne de références et de concepts, les contrats de provenance, les manifestes, les règles de reproductibilité et les portes de sélection demandés, tout en maintenant ouvertes l’installation réelle de ComfyUI, la qualification des dépendances, la production des concepts et la validation runtime.
