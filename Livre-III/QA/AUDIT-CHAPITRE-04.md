---
title: "Audit du Livre III — Chapitre 4"
id: "DOC-L3-QA-AUDIT-CH04"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH04"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T22:37:42+02:00"
last-verified: "2026-07-22T22:37:42+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 4 — Pipeline Blender et organisation des fichiers

## 1. Porte de création

Le chapitre a été repris sur la branche canonique `docs/livre-iii-ch04-pipeline-blender`, qui existait déjà à l’état identique à `main` et ne contenait qu’un fichier lecteur `__PLACEHOLDER__`. Aucun texte, audit finalisé, pull request ouverte ou décision concurrente n’a été écrasé.

La création intervient après la fusion et la clôture QA du chapitre 3. Le chemin, le titre, les résultats d’apprentissage, les livrables, les modes Solo et Studio, les critères de validation et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`.

Le texte lecteur ne contient ni recommandation de raisonnement, ni procédure QA interne, ni chemin du chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **1 578** ;
- titres Markdown contrôlés hors blocs : **52** ;
- sections principales numérotées : **41** ;
- blocs de code, données ou structures : **44** ;
- marqueurs d’explication : **44** ;
- explications structurées hors section d’erreurs : **24** ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- métadonnée de processus de raisonnement : **0** ;
- instruction de prochaine étape dans le texte lecteur : **0**.

Les contrôles automatiques permanents doivent confirmer l’intégrité YAML, les liens locaux, la continuité du Livre III, l’absence de doublons et la conformité des repères avant clôture de la preuve finale.

## 3. Complétude contre le plan maître

Le chapitre couvre :

- qualification documentaire de Blender `5.2.0` Stable et de Godot `4.7.1-stable` ;
- absence d’add-on tiers obligatoire et porte de qualification des extensions futures ;
- template Blender de projet sans dépendance spécifique à un asset ;
- unités métriques, unité pour un mètre et étalon cubique ;
- conversion d’axes Blender vers Godot par glTF ;
- orientation `-Y` dans Blender vers `+Z` pour l’avant d’un modèle dans Godot ;
- origines et pivots fonctionnels ;
- revue bornée des transformations ;
- collections par responsabilité et collection `__EXPORT` unique ;
- différences entre `Append`, `Link` et `Library Overrides` ;
- chemins relatifs, relocalisation et ouverture sur une autre machine ;
- séparation source, travail, bibliothèque, cache, export, livraison et archive ;
- identifiants, noms, états et versions immuables ;
- sauvegardes Blender distinguées du versionnement et des archives ;
- GLB par défaut, glTF séparé lorsque nécessaire et import direct `.blend` limité à l’itération locale ;
- asset test d’un mètre, export, empreinte et import Godot ;
- contrôle Godot borné en GDScript ;
- aller-retour Godot, Blender et Godot avec limites documentées ;
- manifestes de chaîne d’outils, bibliothèques, preset, livraison et rapport ;
- validateur Blender et exporteur GLB proposés ;
- checklists d’ouverture, d’export et de livraison ;
- parcours Solo réduit et parcours Studio avec publication immuable ;
- sécurité des fichiers Blender et extensions ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- synthèse opérationnelle pour `Project Asteria`.

Les cinq livrables demandés par le plan maître sont représentés : template Blender, conventions de collections et nommage, arborescence canonique, preset d’export et checklist d’ouverture, contrôle et livraison.

## 4. Frontières contrôlées

- le chapitre consomme la bible visuelle et les concepts sans les modifier ;
- il prépare le pipeline mais ne produit aucun asset définitif ;
- il ne remplace pas le chapitre 5 pour l’analyse juridique détaillée des licences et consentements ;
- il ne traite pas les techniques spécialisées de modélisation, sculpture, retopologie, UV, matériaux PBR, rig, animation, LOD ou optimisation ;
- il ne présente pas l’import direct `.blend` comme livraison universelle ;
- il ne déduit pas les droits d’un fichier depuis sa seule ouverture dans Blender ;
- il ne prétend pas qu’un aller-retour glTF conserve toutes les fonctions de Godot ou de Blender ;
- il ne revendique aucune exécution runtime, performance ou compatibilité matérielle mesurée ;
- il ne construit aucun PDF intermédiaire.

## 5. Vérification technique et sources officielles

La revue statique a été comparée aux sources officielles consultées le 22 juillet 2026 :

- Blender recommande l’usage d’une version stable officielle pour la production ;
- le panneau d’unités distingue système métrique, échelle d’affichage et unité de longueur ;
- `Link` conserve une référence, tandis que `Append` crée une copie locale ;
- les `Library Overrides` permettent des modifications locales de données liées tout en conservant leur relation ;
- Blender fournit l’échange glTF 2.0 et ses variantes `.glb` et `.gltf` ;
- Godot `4.7` recommande glTF 2.0 et accepte GLB ou glTF séparé ;
- l’import direct `.blend` appelle Blender puis passe par glTF ;
- Godot utilise `Y` vers le haut et attend `+Z` comme avant d’un asset orienté, ce qui correspond à `-Y` dans Blender ;
- OBJ reste limité pour pivots, rigs, animations, UV2 et matériaux PBR ;
- l’export glTF depuis Godot ne couvre pas les particules, `ShaderMaterial` et scènes 2D ;
- la configuration d’import peut être contrôlée dans le dock Import et les réglages avancés.

Les liens officiels sont conservés dans la dernière section du chapitre lecteur. Aucun blog, benchmark communautaire ou valeur runtime non exécutée n’est utilisé comme preuve.

## 6. Explications pédagogiques

Les **44** blocs possèdent **44** marqueurs. Les **24** blocs hors erreurs expliquent selon leur nature : rôle, entrées, paramètres, types, codes de retour, effets de bord, ordre, invariants, limites et résultat attendu.

Les dix cas d’erreurs respectent la séquence directe :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique `Explication structurée du bloc` ne s’intercale dans ces séquences d’erreurs.

## 7. Contrôles particuliers

- chaque bloc clôturé possède un repère reconnu ;
- les commandes PowerShell sont identifiées `[PS]` ;
- les fichiers à créer utilisent `[VSC]` avec leur chemin ;
- les interfaces Blender et Godot utilisent `[APP]` ;
- le téléchargement officiel utilise `[WEB]` ;
- les structures non exécutables utilisent `[LECTURE]` ;
- les sections Solo et Studio restent en Markdown ordinaire ;
- le script Blender ne sauvegarde pas la scène ;
- le script d’export exige une collection `__EXPORT` unique ;
- le script Godot utilise des codes de retour distincts ;
- les manifestes emploient `pending`, `candidate` ou `not_executed` lorsqu’aucune preuve runtime n’existe ;
- les sorties générées ne sont jamais présentées comme sources canoniques ;
- les versions publiées sont immuables.

## 8. Réserves

- Blender `5.2.0` non installé ni exécuté pour `Project Asteria` ;
- template `ASTERIA-BLENDER-TEMPLATE.blend` non matérialisé ;
- profil Blender et liste d’extensions non capturés ;
- arborescence de production réelle non créée ;
- bibliothèques liées et overrides non testés ;
- ouverture sur une seconde machine non réalisée ;
- cube d’un mètre non créé ;
- scripts Blender proposés non exécutés ;
- export GLB et empreintes non produits ;
- import et réimport Godot non exécutés ;
- script GDScript proposé non exécuté ;
- aller-retour et revue visuelle non réalisés ;
- tailles, durées et performances non mesurées ;
- licences des futures extensions et dépendances non qualifiées ;
- Starter Kit non matérialisé ;
- PDF du Livre III non construit conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 4 du Livre III est **accepté au niveau `static-review` sous réserve de réussite des validations documentaires permanentes**. Il installe l’environnement Blender, les conventions de fichiers, les formats d’échange, l’asset test et les portes de contrôle exigés, tout en maintenant ouvertes la matérialisation du template, l’exécution Blender, l’import Godot, l’ouverture sur une seconde machine et la publication de fin de Livre.
