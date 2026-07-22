---
title: "Audit du Livre II — Chapitre 29"
id: "DOC-L2-QA-AUDIT-CH29"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH29"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-22T07:05:00+02:00"
last-verified: "2026-07-22T07:05:00+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 29 — Automatisation Python et génération de données

## 1. Porte de création

Le chapitre a été préparé depuis `main` après fusion du chapitre 28 et vérification de l’absence de branche ou pull request concurrente consacrée au chapitre 29. Le niveau de production **Élevée** a été annoncé dans la conversation et reste absent du chapitre lecteur.

## 2. Résultats

- lignes finales : **1714** ;
- titres Markdown contrôlés : **71** ;
- blocs de code ou de données : **65** ;
- marqueurs d’explication : **65** ;
- explications structurées hors sections d’erreurs : **45** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- métadonnée de niveau de raisonnement dans le chapitre : **0** ;
- sections Solo ou Studio placées dans un bloc de code : **0** ;
- procédure QA destinée au mainteneur dans le chapitre lecteur : **0** ;
- chemin ou niveau du chapitre suivant dans le chapitre lecteur : **0**.

## 3. Complétude et frontières

Le chapitre couvre CPython 3.14.6 comme cible principale provisoire, CPython 3.13.14 comme repli, `hatchling 1.31.0`, `jsonschema 4.26.0`, environnements virtuels, métadonnées `pyproject.toml`, verrouillage par version et plateforme, qualification par roues binaires, CLI typées, configuration TOML, codes de sortie, confinement des chemins, écritures contrôlées, JSON canonique, SHA-256, manifestes, RNG locaux, identités dérivées, JSON Schema Draft 2020-12, diagnostics structurés, plans immuables, lancement de Godot, orchestration des validateurs, JSONL borné, checkpoints, staging, parallélisme borné, nouvelle tentative cataloguée, provenance et archives déterministes.

Les pipelines du chapitre 26, les tests et simulations du chapitre 27 et les artefacts de diagnostic du chapitre 28 conservent leur autorité. Python les orchestre sans réécrire leurs critères ni effectuer de commit métier. L’architecture finale Solo/Studio reste au chapitre 30.

## 4. Revue statique des références

Python 3.14.6 et Python 3.13.14 ont été vérifiés contre Python.org. `hatchling 1.31.0` et `jsonschema 4.26.0` déclarent Python 3.14 dans leurs métadonnées PyPI. Les contrats `venv`, `tomllib`, `subprocess`, `concurrent.futures` et `zipfile` ont été relus contre la documentation Python. La structure `pyproject.toml`, la spécification `pylock.toml` et le caractère expérimental et dépendant de la plateforme de `pip lock` ont été vérifiés contre les documentations officielles PyPA et pip.

**État de la matrice de compatibilité :** en attente de l’exécution GitHub Actions. Cette revue ne constitue pas encore une validation du Starter Kit ni d’un WSL réel.

## 5. Explications pédagogiques

Les **65** blocs possèdent **65** marqueurs. Les **45** blocs hors erreurs utilisent des points spécifiques adaptés à chaque extrait : rôle, responsabilités, paramètres et types, retours ou codes d’échec, effets de bord, invariants, résultat attendu et limites.

Les dix cas d’erreurs respectent directement la séquence obligatoire : symptôme, exemple fautif, `Pourquoi cet exemple est fautif`, exemple corrigé, puis `Pourquoi la correction fonctionne`. Aucun wrapper d’explication structurée ne s’intercale dans ces cas.

## 6. Contrôles particuliers

- `recommended-reasoning` et le niveau GPT sont absents du chapitre ;
- les calques terminologiques interdits sont absents ;
- CPython 3.14.6 est présenté comme cible provisoire et CPython 3.13.14 comme repli ;
- `hatchling 1.31.0` et `jsonschema 4.26.0` sont les seules dépendances directes qualifiées ici ;
- l’installation de qualification exige des roues binaires ;
- `pip lock` est décrit comme expérimental et spécifique à la version de Python et à la plateforme ;
- `pip freeze` n’est pas présenté comme un solveur ou verrou ;
- les chemins sont relatifs et confinés ;
- `shell=False` est utilisé pour les processus ;
- les écritures passent par staging et empreintes ;
- RNG, ordre des sources et résultats parallèles sont stabilisés ;
- les retries sont bornés et limités à des codes transitoires ;
- ZIP n’est pas présenté comme chiffré ou signé ;
- les scripts ne reçoivent aucune autorité métier ;
- Solo et Studio restent en Markdown ordinaire.

## 7. Réserves

- CPython 3.14.6 et 3.13.14 non installés dans le Starter Kit ;
- ensemble complet des dépendances futures non résolu ;
- comportement d’un WSL réel non qualifié ;
- `pip lock` non exécuté dans le Starter Kit ;
- schémas JSON non matérialisés ;
- scripts Python non analysés par un type checker ;
- Godot non lancé par l’orchestrateur ;
- génération déterministe non rejouée ;
- parallélisme non exercé sur Windows et WSL ;
- checkpoints et reprises non testés ;
- archives ZIP non comparées octet par octet ;
- aucune publication de données générées ;
- aucun PDF construit.

## 8. Décision

Le chapitre 29 est **accepté au niveau `static-review`**, sous réserve de matérialisation, d’analyse statique Python, de tests runtime et du PDF de fin de Livre II.
