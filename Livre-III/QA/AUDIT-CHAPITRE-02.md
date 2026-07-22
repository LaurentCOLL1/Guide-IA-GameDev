---
title: "Audit du Livre III — Chapitre 2"
id: "DOC-L3-QA-AUDIT-CH02"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH02"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T17:49:18+02:00"
last-verified: "2026-07-22T17:49:18+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 2 — Direction artistique et bible visuelle

## 1. Porte de création

Le chapitre a été créé depuis `main` après clôture du chapitre 1 du Livre III. Aucun chapitre, audit, branche ou pull request concurrent du chapitre 2 n’existait. Le périmètre a été comparé au plan maître détaillé et aux frontières des chapitres 1, 3, 5, 10, 13, 16, 23 à 25, 28 et 29.

Le texte lecteur ne contient aucune donnée de pilotage de conversation, aucun niveau de raisonnement conseillé, aucune procédure QA interne et aucune annonce de chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **2560** ;
- titres Markdown contrôlés hors blocs : **59** ;
- blocs de code ou de données : **62** ;
- blocs significatifs selon le validateur : **62** ;
- marqueurs d’explication : **62** ;
- explications structurées hors section d’erreurs : **42** ;
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

Le chapitre transforme le cahier des charges du chapitre 1 en langage visuel transmissible. Il couvre :

- différence entre vision, direction artistique et bible visuelle ;
- piliers observables, axes d’opposition et priorités ;
- hiérarchie universelle, familiale et propre aux instances ;
- langage des formes, silhouettes, échelles et distances de lecture ;
- composition, hiérarchie, zones focales et zones de repos ;
- palettes du monde, de l’interface, des VFX et couleurs fonctionnelles ;
- valeur, saturation, température et redondance non chromatique ;
- profils colorimétriques, captures comparables et limites d’affichage ;
- familles de matériaux, causalité de l’usure et histoire de surface ;
- lumière, environnement, correspondance tonale, exposition, profondeur et brouillard ;
- niveau de réalisme, simplification et tiers héroïque, standard ou arrière-plan ;
- règles de familles pour personnages, créatures, environnements, objets, UI et VFX ;
- variations culturelles, régionales, sociales et temporelles ;
- catalogue d’exemples conformes, limites et non conformes ;
- grille de revue, dérogations et journal de décisions ;
- contrat de scène Godot, caméras, profils et protocole de capture ;
- mesures et observations conservées sans résultat runtime inventé ;
- provenance des références ;
- parcours Solo et Studio ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- synthèse des décisions retenues pour `Project Asteria`.

## 4. Frontières contrôlées

- le chapitre consomme les budgets et priorités du chapitre 1 sans les modifier silencieusement ;
- il définit la direction mais ne collecte pas encore les références définitives ni les concepts du chapitre 3 ;
- il ne qualifie pas une version de Blender, un addon ou un pipeline DCC ;
- il ne produit aucun personnage, créature, bâtiment, objet, matériau, rig, animation, VFX, audio ou thème UI définitif ;
- il prépare une scène et des profils Godot sans les déclarer matérialisés ;
- il ne définit pas les cartes PBR, presets d’import, LOD ou budgets finaux ;
- il ne donne aucun avis juridique personnalisé ;
- il traduit des états visuels sans reprendre l’autorité des systèmes runtime du Livre II.

## 5. Vérification technique et sources

La revue statique a été comparée aux documentations officielles :

- Godot `Environment` regroupe notamment arrière-plan, lumière ambiante, brouillard, correspondance tonale et ajustements ;
- l’environnement et le ciel peuvent influencer la lumière ambiante et réfléchie ;
- les ajustements interviennent après la correspondance tonale ;
- les thèmes Godot centralisent le style des nœuds `Control` et l’éditeur de thème offre un aperçu ;
- WCAG 2.2 distingue l’usage de la couleur, le contraste du texte et le contraste non textuel.

Le chapitre traite `AgX`, l’exposition `1.0`, les distances, ratios de distribution et nombres d’angles comme hypothèses documentées à exercer. Aucun rendu, contraste, coût GPU, import, scène ou capture n’est présenté comme exécuté.

## 6. Explications pédagogiques

Les **62** blocs possèdent **62** marqueurs. Les **42** blocs hors erreurs expliquent selon le besoin réel : rôle, champs et types, unités, relations, dépendances, déroulement, effets de bord, invariants, vérification et limites.

Les dix cas d’erreurs respectent directement la séquence :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique structurée ne s’intercale dans les séquences d’erreurs.

## 7. Contrôles particuliers

- tous les blocs possèdent un repère d’utilisation reconnu ;
- les fichiers à créer ou modifier utilisent `[VSC]` avec un chemin ;
- les structures, arbres et tableaux de lecture utilisent `[LECTURE]` ;
- les sections Solo et Studio utilisent du Markdown ordinaire ;
- les identifiants de règles, décisions, exceptions, profils et assets restent distincts ;
- les valeurs `null`, `not_executed` et compteurs nuls évitent d’inventer une exécution ;
- la couleur n’est jamais le seul canal d’une information essentielle ;
- les matériaux et usures sont reliés à des causes ;
- les variations régionales dérivent de contraintes plutôt que d’un stéréotype unique ;
- le processus de dérogation ne modifie pas la règle générale ;
- les captures restent dérivées et ne remplacent pas les sources ;
- aucun test runtime, scène, asset pilote ou benchmark n’est revendiqué.

## 8. Réserves

- Starter Kit non matérialisé ;
- fichiers proposés sous `docs/`, `tools/`, `scenes/` et `captures/` non créés dans un projet Godot réel ;
- bible visuelle réelle non produite à partir de références sélectionnées ;
- références, auteurs, licences et droits non renseignés ;
- version Blender et addons non qualifiés ;
- assets pilotes non produits ;
- scène Godot de validation non matérialisée ;
- script de caméras non analysé ni exécuté ;
- profils d’environnement, tonemapper, exposition et brouillard non exercés ;
- contrastes UI non mesurés ;
- captures non produites ;
- coûts GPU, mémoire et temps de frame non mesurés ;
- revue Solo ou Studio non exécutée ;
- PDF du Livre III non construit, conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 2 du Livre III est **accepté au niveau `static-review`**. Il fournit la grammaire, les livrables et les portes de revue demandés, tout en maintenant ouvertes la collecte des références, la production des concepts, la matérialisation des assets pilotes et la validation dans Godot.
