---
title: "Audit — Livre V, Fiche 12 : Référence Python"
id: "DOC-L5-QA-AUDIT-CH12"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 12
last-verified: "2026-07-28T22:48:26+02:00"
audit-date: "2026-07-28T22:48:26+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 12 : Référence Python

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire de Python pour l’automatisation du guide sans devenir un cours général, sans matérialiser un paquet et sans revendiquer d’exécution.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| interpréteur et environnements | CPython, exécutable, `venv`, `uv`, caches et matrice | Livre I, chapitre 4 |
| valeurs et typage | types intégrés, annotations, unions et garde runtime | documentation Python et outils de typage futurs |
| collections et modèles | séquences, associations, ensembles, dataclasses et protocoles | Livre II, chapitre 29 pour les manifestes |
| flux et erreurs | retours, exceptions, context managers et reprise | contrat de la couche applicative |
| fonctions et itération | paramètres, callables, générateurs et async | référence Python |
| modules et imports | modules, paquets, garde principale et ressources | architecture d’automatisation du Livre II |
| fichiers et sérialisation | `Path`, encodage, staging, JSON, archives et empreintes | chapitre 13 pour les formats |
| CLI et processus | `argparse`, codes, stdout, stderr et `subprocess` | Livre II, chapitre 29 et fiche 10 |
| tests | cas, fixtures, oracles, déterminisme et instabilité | Livre II, chapitre 27 |
| dépendances | `pyproject.toml`, groupes, verrou, index et SBOM | Livre I, chapitre 4 |
| packaging | sdist, wheel, build isolé et points d’entrée | spécifications PyPA |
| correspondances GDScript | notions comparables et différences d’autorité | fiche 11 |
| sécurité et acceptation | données non fiables, archives, processus et portes | Livre IV et Companion Pack futur |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express placé avant les cartes ;
- tables utilisées avant les paragraphes explicatifs ;
- paragraphes courts et consultation non linéaire ;
- absence de résultats d’apprentissage et de démonstration linéaire ;
- absence de synthèse `Project Asteria` importée du profil tutoriel ;
- aucun bloc de code clôturé ;
- renvois fréquents vers les sources propriétaires ;
- niveau de preuve visible lorsque l’exécution pourrait être supposée.

## 4. Couverture du plan maître

| Exigence du chapitre 12 | Réponse |
|---|---|
| environnements | PY-01 |
| types | PY-02 et PY-03 |
| fonctions | PY-05 |
| fichiers | PY-07 |
| CLI | PY-08 |
| tests | PY-09 |
| automatisation et outils du guide | PY-00, Matrice A et PY-08 |
| dépendances | PY-10 |
| packaging | PY-11 |
| correspondances GDScript | Matrice C |
| aide-mémoire | index, cartes et matrices |
| recettes | formes inline et renvoi vers la fiche 10 |
| conventions | contrats visibles dans chaque table |
| validation future | PY-12 et Companion Pack |

## 5. Frontières

- le cours d’installation et d’environnement reste au Livre I, chapitre 4 ;
- les chaînes d’automatisation complètes restent au Livre II, chapitre 29 ;
- les recettes exécutables restent à la fiche 10 ;
- la syntaxe GDScript reste à la fiche 11 ;
- les formats et schémas restent au chapitre 13 ;
- les campagnes exécutées et benchmarks restent au chapitre 21 ;
- la compatibilité transversale reste au chapitre 22 ;
- les licences et conformités restent au chapitre 25 ;
- les modules, tests et distributions permanents restent au Companion Pack.

## 6. Exactitude technique statique

Les versions CPython `3.14.6` et `3.13.14` correspondent aux cibles enregistrées dans le dépôt. Les documentations Python 3.14 et PyPA ont été revues le 28 juillet 2026 pour `venv`, `typing`, `pathlib`, `argparse`, `subprocess`, `unittest`, `pyproject.toml`, groupes de dépendances, métadonnées, points d’entrée et distributions sources.

La fiche distingue correctement :

- langage, implémentation, interpréteur et environnement ;
- module importé et distribution installée ;
- annotation statique et validation runtime ;
- dépendance directe, transitive, verrou et preuve de compatibilité ;
- arbre source, sdist, wheel et installation éditable ;
- exception interne et code de sortie de processus ;
- checksum, provenance, signature et innocuité ;
- ressemblance syntaxique et autorité architecturale.

## 7. Métriques

| Mesure | Valeur |
|---|---:|
| lignes | 403 |
| titres | 18 |
| cartes | 13 |
| matrices | 3 |
| liens Markdown | 60 |
| renvois vers les Livres I à IV | 21 |
| liens profonds propriétaires | 21 |
| liens officiels | 19 |
| blocs clôturés | 0 |

## 8. Contrôles et réserves

- structure, métadonnées, liens locaux et doublons : soumis au validateur permanent ;
- marqueurs et fragments du Livre V : soumis au validateur spécialisé ;
- repères de contexte : aucun bloc procédural n’impose de légende ;
- PDF : interdit pour cette validation légère ;
- aucun interpréteur Python téléchargé ou lancé ;
- aucun module compilé, importé ou exécuté ;
- aucun test runner, analyseur de types, linter ou scanner lancé ;
- aucun environnement virtuel créé ou synchronisé ;
- aucune dépendance installée ou verrouillée ;
- aucun processus natif appelé ;
- aucun fichier, archive ou donnée non fiable traité ;
- aucune sdist, wheel ou commande installable construite ;
- aucune matrice Windows, WSL/Linux, Solo ou Studio exécutée ;
- aucune compatibilité de backend IA ou GPU qualifiée ;
- aucun fichier permanent du Companion Pack matérialisé ;
- aucune approbation juridique organisationnelle réalisée.

## 9. Décision finale

Accepté au niveau `static-review` après réussite des validations légères et enregistrement de la preuve QA. Les statuts `syntax-checked`, `tested`, `qualified` et `published` restent interdits sans campagne exécutée.
