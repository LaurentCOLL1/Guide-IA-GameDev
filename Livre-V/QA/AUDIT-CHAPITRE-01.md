---
title: "Audit post-création — Livre V, chapitre 1"
id: "DOC-L5-AUDIT-CH01"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 1
audit-date: "2026-07-28T09:26:30+02:00"
last-verified: "2026-07-28T09:26:30+02:00"
audit-level: "static-review"
target-document: "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"
---

# Audit post-création — Chapitre 1

## 1. Décision

Le chapitre 1 — **Carte générale de la collection** est accepté au niveau `static-review`.

La décision porte sur la cohérence documentaire, la couverture du plan maître, la navigation interne, les repères, les exemples, les diagnostics et l’extension des validateurs au Livre V. Elle ne qualifie aucun parcours utilisateur mesuré, artefact du Companion Pack, test runtime, compatibilité matérielle ou publication commerciale.

## 2. Périmètre comparé au plan maître

Les quatre objectifs sont couverts :

1. structure Volume 0, Livres I à V et Companion Pack ;
2. dépendances et parcours Solo/Studio ;
3. entrées par besoin, outil ou système ;
4. prérequis et ordre conseillé.

Les quatre livrables sont présents :

- carte de navigation ;
- matrice Livre/compétence ;
- parcours débutant, production et dépannage ;
- index des prérequis.

La frontière est respectée : le chapitre ne résume pas tous les tutoriels, ne construit pas les arbres de décision détaillés du chapitre 2 et ne matérialise pas les bibliothèques du Companion Pack.

## 3. Comparaison avec les chapitres voisins

Le chapitre 2 du Livre V possède les arbres de décision et les critères pondérés. Le présent chapitre fournit seulement les points d’entrée et les relations générales.

Le chapitre 3 possédera les fiches des logiciels et outils. Le présent chapitre explique comment trouver ces fiches et leurs tutoriels propriétaires sans écrire leurs installations détaillées.

Le chapitre 26 possédera les index croisés complets. Le présent chapitre définit le contrat initial des identifiants, prérequis et routes.

## 4. Contrôle pédagogique

Le chapitre définit le vocabulaire avant les routes, distingue lecture progressive et ciblée, explique les statuts de preuve et fournit des parcours adaptés à un débutant.

L’exemple Python explique les fonctions, paramètres, types, retours, méthodes de normalisation et opérateurs. Les commandes PowerShell, CMD, WSL et conteneur expliquent leurs paramètres, codes de retour et sorties.

## 5. Repères d’utilisation

Les dix repères obligatoires sont présents : `[PS]`, `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]`, `[VSC]`, `[WEB]`, `[APP]`, `[SORTIE]` et `[LECTURE]`.

Chaque bloc clôturé possède un repère cohérent. Les structures de référence ne sont pas présentées comme des commandes.

## 6. Diagnostics sémantiques

La section d’erreurs contient dix cas détaillés. Chaque cas montre :

- un symptôme ou risque ;
- un exemple fautif ;
- l’invariant violé ;
- un exemple corrigé ;
- l’invariant restauré et la différence.

## 7. Contrôle technique statique

- front matter et identifiant stable relus ;
- liens relatifs vérifiés par les validateurs ;
- routes comparées à `contents.txt` et aux index ;
- exemples YAML, JSON, Markdown, Python, PowerShell, batch et Bash relus statiquement ;
- aucun test runtime ou artefact non matérialisé revendiqué ;
- validateurs permanents étendus explicitement au Livre V.

## 8. Contrôle anti-doublon

Métriques du chapitre :

- lignes : 1095 ;
- titres : 51 ;
- blocs clôturés : 33 ;
- marqueurs d’explication : 33 ;
- diagnostics détaillés : 10 ;
- titres dupliqués : 0 ;
- blocs dupliqués : 0 ;
- paragraphes longs dupliqués : 0.

Les rappels sur l’autorité, les statuts et les frontières sont contextualisés. Aucune longue procédure d’un Livre précédent n’est recopiée.

## 9. Gouvernance du lot

Le lot permanent contient :

1. `Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md` ;
2. `Livre-V/QA/AUDIT-CHAPITRE-01.md` ;
3. `Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml` ;
4. `Livre-V/index.md` ;
5. `ROADMAP.md` ;
6. `contents.txt` ;
7. `CONTINUITE-PROJET.md` ;
8. `plans/LIVRE-V-PLAN-MAITRE.md` ;
9. `tools/validate_chapters.py` ;
10. `tools/check_context_markers.py`.

Les deux outils sont modifiés uniquement pour reconnaître le Livre V et appliquer les mêmes contrôles documentaires. L’ordre des chapitres et le plan maître ne sont pas restructurés.

## 10. Réserves

- aucun test de recherche avec lecteur réel n’a été exécuté ;
- aucun temps de localisation n’a été mesuré ;
- aucun index interactif HTML ou autre format non linéaire n’a été matérialisé ;
- aucun artefact du Companion Pack n’a été créé ;
- aucune exécution runtime n’a été effectuée ;
- la licence globale et le balisage avancé des publications restent ouverts.

## 11. Conclusion

Le chapitre est débutant-compatible, conforme au plan maître et cohérent avec les Livres existants. Il peut ouvrir le Livre V au niveau `static-review` avec les réserves déclarées.
