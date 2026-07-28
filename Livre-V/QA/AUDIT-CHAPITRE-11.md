---
title: "Audit — Livre V, fiche 11 : Référence GDScript"
id: "DOC-L5-QA-AUDIT-CH11"
status: "complete"
version: "1.0.0"
last-verified: "2026-07-28T22:02:17+02:00"
lang: "fr-FR"
book: "Livre V"
chapter: 11
audit-date: "2026-07-28T22:02:17+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 11 : Référence GDScript

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle fournit une référence non linéaire de GDScript pour Godot `4.7.1-stable`, relie les notions au chapitre pédagogique propriétaire et ne présente aucune forme comme analysée ou exécutée.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-11-Reference-GDScript.md` ;
- identifiant : `DOC-L5-CH11` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- documentation officielle de Godot `4.7.1-stable` revue le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | 387 |
| titres | 18 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 68 |
| renvois vers les Livres I à IV | 39 |
| liens profonds vers les sources propriétaires | 36 |
| liens officiels | 12 |
| blocs clôturés | 0 |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| syntaxe | déclarations, expressions, contrôle de flux et formes de fonction |
| types | scalaires, textes, mathématiques, collections, objets, `Callable`, `Signal` et `Variant` |
| fonctions | paramètres, retours, statiques, lambdas, appels différés et `await` |
| classes | `class_name`, héritage, composition, classes internes et propriétés |
| annotations | export, onready, tool, warnings, RPC et Inspector |
| collections | tableaux, dictionnaires, types, duplication et mutations |
| opérateurs | matrice par priorité et pièges |
| fonctions courantes | index alphabétique de mots-clés et fonctions |
| chapitre pédagogique | renvois précis vers le Livre II |
| pièges et versions | compatibilité `4.7.1`, docs `stable`, avertissements et migration |
| aide-mémoire | treize cartes et trois matrices consultables isolément |
| exemples minimaux | code inline uniquement, sans fichier exécutable matérialisé |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- l’apprentissage progressif reste au Livre II, chapitre 2 ;
- scènes, nœuds, Resources et signaux restent au Livre II, chapitre 3 ;
- les recettes exécutables restent au chapitre 10 du Livre V ;
- la référence Python reste au chapitre 12 ;
- les formats d’échange restent au chapitre 13 ;
- les diagnostics transversaux restent au chapitre 20 ;
- les campagnes et mesures restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- licences et conformité restent au chapitre 25 ;
- les fichiers testables réels restent au Companion Pack.

## 6. Séparation information et exécution

Aucune carte n’annonce :

- un fichier `.gd` écrit hors du chapitre Markdown ;
- un parse ou import Godot ;
- une scène instanciée ;
- un signal connecté ou émis ;
- une Resource chargée ;
- un avertissement réellement observé ;
- un test unitaire ou d’intégration exécuté ;
- une migration de projet réalisée ;
- une compatibilité autre que la cible documentaire déclarée.

## 7. Liens et sources

Les renvois propriétaires ciblent notamment la nature de GDScript, la structure des fichiers, le typage, les types, les fonctions, les classes, les annotations, les collections, le cycle de vie, les ressources, les erreurs, les avertissements et les tests déterministes.

Les liens externes pointent vers la release Godot `4.7.1`, la référence GDScript, le guide de style, le typage statique, les propriétés exportées, les avertissements et les classes officielles. Leur présence ne constitue ni installation, ni parse, ni exécution.

## 8. Risques et réserves

1. aucun binaire Godot téléchargé ou lancé ;
2. aucun fichier GDScript analysé, importé ou exécuté ;
3. aucune scène, nœud, Resource ou Inspector manipulé ;
4. aucun signal, `Callable`, `await` ou cycle de vie observé ;
5. aucun avertissement configuré ou transformé en erreur ;
6. aucun test de type, collection, opérateur ou propriété exécuté ;
7. aucune vérification de performance du typage réalisée ;
8. aucune migration depuis une version antérieure testée ;
9. aucune compatibilité C#, GDExtension ou plateforme exportée qualifiée ;
10. aucun fichier ou test du Companion Pack matérialisé ;
11. aucune approbation juridique organisationnelle réalisée ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 9. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, cartes, matrices, fragments propriétaires et absence de PDF. Toute allégation de syntaxe confirmée ou de comportement exige ensuite un binaire Godot exact, un projet minimal, des commandes et des artefacts enregistrés.
