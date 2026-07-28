---
title: "Protocole éditorial et QA des fiches du Livre V"
id: "DOC-L5-QA-PROTOCOLE-FICHES"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
category: "quality-protocol"
last-verified: "2026-07-28T11:28:35+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Protocole éditorial et QA des fiches du Livre V

## 1. Statut du protocole

Le Livre V n’est pas un Livre pédagogique supplémentaire. Il transforme les connaissances des Livres I à IV en **fiches, matrices, recettes minimales, catalogues et index** consultables rapidement.

Ce protocole est le profil spécialisé du Livre V. Il conserve les obligations communes d’intégrité, de preuve, de sécurité, de licence, de liens et de gouvernance. Il remplace les règles tutoriel incompatibles du protocole général d’audit post-création.

## 2. Règles du protocole général qui restent obligatoires

Toute fiche du Livre V doit encore respecter :

- un chemin canonique et un identifiant stable ;
- un front matter valide ;
- une version, une date de vérification et un niveau de preuve ;
- des liens locaux résolus ;
- des fragments internes visant une sous-section existante lorsqu’ils sont utilisés ;
- l’absence de doublons significatifs ;
- la séparation entre revue statique et exécution runtime ;
- la qualification des licences, sources et compatibilités pertinentes ;
- une branche dédiée, une pull request et une preuve QA ;
- la mise à jour coordonnée de l’index, de la roadmap, du plan maître et de la continuité ;
- l’absence de PDF intermédiaire, sauf modification directe de la chaîne de publication.

## 3. Règles tutoriel qui ne sont pas imposées au Livre V

Les fiches du Livre V ne sont pas obligées de reproduire :

- une introduction progressive destinée à être lue depuis la page précédente ;
- une section « Résultats d’apprentissage » ;
- une démonstration complète du début à la fin ;
- l’explication ligne par ligne de notions déjà enseignées dans les Livres I à IV ;
- les dix repères d’utilisation dans chaque document ;
- dix cas d’erreurs détaillés ;
- un exemple fautif et corrigé pour chaque ligne de diagnostic ;
- une synthèse finale consacrée à `Project Asteria` ;
- une checklist longue et un critère de passage rédigés comme dans un tutoriel ;
- des variantes Solo et Studio lorsque la fiche ne dépend pas de l’organisation du travail.

Une recette minimale qui contient du code ou une commande reste expliquée proportionnellement à son objectif. Elle décrit les entrées, la sortie, les préconditions et les risques importants, puis renvoie au tutoriel propriétaire pour l’enseignement complet.

## 4. Types de fiches

| Type | Fonction principale | Forme privilégiée |
|---|---|---|
| orientation | trouver le bon Livre, chapitre ou prérequis | table de navigation et liens directs |
| outil | identifier rôle, version, compatibilité et alternatives | carte normalisée |
| modèle | comparer famille, licence, mémoire et contexte | matrice datée |
| recette | accomplir une opération minimale | étapes courtes ou extrait minimal |
| format | rappeler structure, champs et contraintes | table ou exemple compact |
| patron | choisir une solution selon le contexte | problème, décision, limites et renvois |
| diagnostic | partir d’un symptôme vers des vérifications | table symptôme → contrôle → source |
| benchmark | comparer des mesures reproductibles | protocole et résultats datés |
| checklist | vérifier un livrable ou une porte | liste courte et actionnable |
| index | relier besoins, outils, systèmes et sources | matrice ou liste croisée |

## 5. Contrat minimal d’une fiche

Chaque fiche substantielle porte le marqueur invisible `<!-- l5:card -->`. Une matrice autonome porte `<!-- l5:matrix -->`.

Une fiche contient les éléments pertinents parmi les suivants :

| Élément | Obligation |
|---|---|
| besoin ou question | obligatoire |
| réponse rapide | obligatoire |
| source propriétaire | obligatoire |
| prérequis | obligatoire lorsque la réponse dépend d’une notion antérieure |
| validation ou mesure | obligatoire lorsqu’un résultat doit être qualifié |
| version et date | obligatoire pour les informations susceptibles d’évoluer |
| niveau de preuve | obligatoire lorsqu’une exécution pourrait être supposée |
| limites | obligatoire lorsqu’une réponse n’est pas universelle |
| alternatives | obligatoire lorsqu’un choix raisonnable existe |
| licence ou provenance | obligatoire pour un outil, modèle, asset ou service tiers |

Tous les champs ne sont pas répétés mécaniquement lorsque la fiche est une simple ligne d’index. La densité doit servir la consultation, pas reproduire un formulaire vide.

## 6. Politique de liens internes

Les liens vers les Livres I à IV sont le cœur du Livre V.

Pour chaque fiche substantielle :

1. inclure au moins un lien vers le tutoriel propriétaire ;
2. inclure au moins un lien vers un prérequis, une validation ou une alternative ;
3. viser une sous-section précise avec un fragment lorsque son titre est stable ;
4. utiliser le chapitre seul lorsque plusieurs sections sont nécessaires ou lorsque l’ancre serait fragile ;
5. ne pas remplacer un lien par une copie longue du contenu source ;
6. vérifier la cible et le fragment lors de l’audit ;
7. mettre à jour la fiche lorsque le titre ou l’ancre source change.

À l’échelle d’un chapitre de fiches, la QA vérifie une densité minimale de renvois vers les Livres I à IV et la présence de fragments précis. Le seuil est un garde-fou, pas un objectif éditorial maximal.

## 7. Forme visuelle

Le Livre V doit se distinguer des Livres précédents :

- titres courts fondés sur un identifiant de fiche ou une question ;
- tables de décision et matrices en premier ;
- paragraphes courts ;
- liens directement visibles dans les cellules ou les réponses ;
- séparateurs entre familles de fiches ;
- absence de longues transitions narratives ;
- absence de répétition des objectifs pédagogiques ;
- procédures réduites au minimum utile ;
- index en début de document lorsque le chapitre dépasse quelques fiches.

Le document doit pouvoir être consulté depuis une recherche, un lien profond ou une table des matières sans lecture des fiches précédentes.

## 8. Code, commandes et exemples

Une fiche de recette peut contenir un bloc seulement lorsqu’il apporte une valeur de référence immédiate.

Le bloc doit alors :

- porter le repère d’utilisation adapté ;
- rester minimal ;
- nommer les entrées ou paramètres indispensables ;
- indiquer la sortie ou le code de retour utile ;
- signaler les opérations destructives ou les privilèges ;
- pointer vers le tutoriel qui explique la syntaxe et le contexte complet.

Le Livre V ne réexplique pas chaque opérateur ou type déjà enseigné. Il explique uniquement ce qui est nécessaire pour adapter correctement la recette.

## 9. Diagnostics

Une fiche de diagnostic privilégie une table compacte :

| Symptôme | Vérification | Cause possible | Source |
|---|---|---|---|

Le format détaillé « exemple fautif / exemple corrigé / différence » n’est obligatoire que lorsque la fiche enseigne réellement une correction de code, de commande ou de structure. Il n’est pas imposé à un index de symptômes, à une matrice de choix ou à une carte de navigation.

## 10. Audit d’une fiche ou d’un chapitre de fiches

L’audit vérifie :

- la conformité au type annoncé ;
- la rapidité de consultation ;
- la présence des marqueurs de fiches ou matrices ;
- la densité et la précision des liens vers les Livres I à IV ;
- l’absence de procédure complète recopiée ;
- la couverture du plan maître ;
- la cohérence des prérequis ;
- la séparation entre information statique, mesure et runtime ;
- l’exactitude des versions, licences et compatibilités ;
- la lisibilité des tables ;
- l’absence de structure tutoriel importée sans nécessité.

L’audit ne récompense pas le nombre de lignes, de blocs ou de diagnostics. Il mesure la capacité à retrouver une information et à rejoindre sa source propriétaire.

## 11. Profil automatique minimal

Le validateur du Livre V contrôle notamment :

- `document-format: "reference-cards"` ;
- au moins quatre marqueurs `<!-- l5:card -->` pour un chapitre composé de plusieurs fiches ;
- au moins une matrice ou un index lorsque le plan l’exige ;
- un nombre minimal de liens vers les Livres I à IV ;
- plusieurs liens avec fragments précis ;
- l’absence des structures tutoriel interdites lorsqu’elles ne sont pas justifiées ;
- les liens locaux, identifiants, dates, audits et doublons communs.

Ces seuils peuvent évoluer avec l’expérience de consultation. Toute modification est enregistrée dans le plan maître et la continuité.

## 12. Critère d’acceptation

Une fiche est acceptée lorsque le lecteur peut :

1. identifier immédiatement la question traitée ;
2. obtenir une réponse concise ;
3. rejoindre le tutoriel propriétaire ;
4. retrouver les prérequis et la validation ;
5. comprendre les limites de la réponse ;
6. distinguer ce qui a été relu de ce qui a réellement été exécuté.

Une fiche longue, narrative et autonome qui pourrait remplacer le tutoriel source est non conforme au Livre V.
