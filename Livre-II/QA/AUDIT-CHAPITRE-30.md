---
title: "Audit du Livre II — Chapitre 30"
id: "DOC-L2-QA-AUDIT-CH30"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH30"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-22T07:41:06+02:00"
last-verified: "2026-07-22T07:41:06+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 30 — Architecture Solo et architecture Studio

## 1. Porte de création

Le chapitre a été préparé depuis `main` après fusion de la qualification Python du chapitre 29. Aucune branche ni pull request concurrente consacrée au chapitre 30 n’était ouverte. Le niveau de production **Élevée** a été annoncé dans la conversation et reste une donnée de gouvernance absente du chapitre lecteur.

La règle demandée par le mainteneur est devenue permanente : toute dépendance future ajoutée, supprimée ou mise à jour dans le Starter Kit doit être qualifiée avant adoption sur les versions Python, plateformes et usages concernés.

## 2. Résultats

- lignes finales : **1932** ;
- titres Markdown contrôlés hors blocs : **39** ;
- blocs de code ou de données : **65** ;
- blocs significatifs selon le validateur : **59** ;
- marqueurs d’explication : **65** ;
- explications structurées hors sections d’erreurs : **45** ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- titres dupliqués : **0** ;
- blocs significatifs dupliqués : **0** ;
- paragraphes longs dupliqués : **0** ;
- métadonnée de niveau de raisonnement dans le chapitre : **0** ;
- sections Solo ou Studio placées dans un bloc de code : **0** ;
- procédure QA destinée au mainteneur dans le chapitre lecteur : **0** ;
- chemin ou niveau d’une prochaine étape dans le chapitre lecteur : **0**.

## 3. Complétude et frontières

Le chapitre synthétise les vingt-neuf chapitres précédents sans créer de nouvelle autorité métier. Il couvre deux enveloppes opérationnelles partageant un même cœur : Mode Solo et Mode Studio.

Le périmètre comprend :

- invariants communs et carte des autorités ;
- organisation physique par fonctionnalité ;
- graphe de dépendances et racine de composition ;
- profils d’architecture typés ;
- procédures Solo et responsabilités Studio ;
- manifestes d’environnement ;
- règle permanente de qualification des dépendances du Starter Kit ;
- inventaires, verrous par plateforme et dépendances transitives natives ;
- ADR, propriétaires de code, classification des changements et revues ;
- cycle de contenu, manifestes et promotion ;
- portes de validation, CI et exécution headless ;
- presets d’export, paquets candidats et provenance ;
- secrets, services IA facultatifs et replis ;
- diagnostics, incidents et rollback ;
- transition progressive Solo vers Studio ;
- plan de matérialisation du Starter Kit ;
- critères d’acceptation et synthèse finale de `Project Asteria`.

Les domaines, dépôts, commandes, événements et formats persistés définis aux chapitres 1 à 29 conservent leur autorité. Le chapitre 30 ne transforme ni la composition, ni la CI, ni une revue humaine en permission métier.

## 4. Revue statique des références

La revue technique a été comparée aux documentations officielles Godot stables pour l’organisation du projet, les Autoloads, les exports et l’exécution en ligne de commande. Les points retenus sont compatibles avec les contrats suivants :

- Godot utilise directement l’arborescence du projet et recommande un nommage cohérent limitant les problèmes de casse ;
- un Autoload est un nœud global chargé tôt, pas une justification pour créer un gestionnaire universel ;
- `export_presets.cfg` peut porter la configuration d’export versionnée ;
- l’export automatisé utilise un binaire d’éditeur et un preset nommé ;
- le mode headless convient aux environnements sans affichage ;
- les tags personnalisés d’export ne doivent pas être supposés actifs comme dans un paquet lorsque le projet est simplement lancé depuis l’éditeur.

Cette revue ne constitue ni une ouverture du projet complet avec Godot 4.7.1-stable, ni un export réel, ni une campagne de plateforme.

## 5. Explications pédagogiques

Les **65** blocs possèdent **65** marqueurs. Les **45** blocs hors erreurs utilisent des rubriques spécifiques : rôle concret, paramètres et types, direction des dépendances, effets de bord, invariants, résultat attendu ou limites.

Les dix cas d’erreurs respectent directement la séquence obligatoire :

1. symptôme ou risque ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique structurée ne s’intercale dans ces cas.

## 6. Contrôles particuliers

- `recommended-reasoning` et le niveau GPT sont absents du chapitre ;
- les calques terminologiques interdits sont absents ;
- le Mode Solo et le Mode Studio partagent les mêmes règles métier ;
- aucun super-manager transversal n’est introduit ;
- la composition ne devient pas un Service Locator ;
- les Autoloads ne reçoivent pas d’autorité universelle ;
- les outils de production restent séparés du runtime joueur ;
- les services IA restent facultatifs pour les fonctions essentielles ;
- les tags d’export ne modifient pas le domaine ;
- les dépendances futures du Starter Kit exigent une qualification avant adoption ;
- les verrous sont distingués par plateforme et série Python lorsque nécessaire ;
- Linux hébergé n’est pas présenté comme preuve complète d’un WSL réel ;
- les manifestes et empreintes ne sont pas présentés comme signatures ;
- la publication reste distincte de la validation métier ;
- Solo et Studio restent en Markdown ordinaire dans leur section dédiée ;
- la synthèse finale est consacrée à `Project Asteria`.

## 7. Réserves

- Starter Kit non matérialisé ;
- projet complet non ouvert sous Godot 4.7.1-stable ;
- scripts GDScript non analysés ni exécutés ;
- profils d’architecture non chargés ;
- graphe de composition non instancié ;
- presets d’export non matérialisés ;
- modèles d’export non installés ;
- paquets Windows et Linux non construits ;
- WSL réel non qualifié ;
- dépendances futures du Starter Kit non connues ;
- verrous, SBOM et licences du kit non générés ;
- simulations et migrations non exécutées ;
- reproductibilité octet par octet non mesurée ;
- signature et provenance réelles non produites ;
- PDF complet du Livre II non construit ni inspecté.

## 8. Décision

Le chapitre 30 est **accepté au niveau `static-review`**. La rédaction des trente chapitres du Livre II est complète. La prochaine porte de projet est la validation technique et documentaire transversale, suivie de la compilation et de l’inspection du PDF complet du Livre II.
