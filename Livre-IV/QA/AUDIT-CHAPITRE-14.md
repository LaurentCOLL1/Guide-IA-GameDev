---
title: "Audit post-création — Livre IV, chapitre 14"
id: "DOC-L4-QA-AUDIT-CH14"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH14"
chapter-version: "1.0.0"
audit-date: "2026-07-26T21:42:29+02:00"
last-verified: "2026-07-26T21:42:29+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 14

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des scripts CI de `Project Asteria`, de configuration des workflows, de qualification des actions externes, d’installation des runners, de configuration des secrets ou d’OIDC, d’exécution des matrices, de construction des artefacts, de génération d’attestations et de reconstruction depuis un clone neuf.

Aucun build Godot, test runtime, package, cache, attestation, échange OIDC, déploiement, publication, mesure de durée ou preuve de reproductibilité binaire n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- automatiser validations, tests, constructions et préparation du packaging ;
- gérer branches, pull requests, tags, versions, commits, runs et build IDs ;
- protéger les secrets et distinguer les niveaux de confiance ;
- créer des matrices de plateformes explicites ;
- conserver logs, rapports, manifestes, empreintes et procédures de reprise ;
- préparer une reconstruction propre depuis un clone neuf.

Les livrables sont préparés sous forme de contrats : modèles de workflows, scripts canoniques, conventions de version, politiques d’artefacts, registres de dépendances, portes de promotion et procédure de reconstruction.

## 3. Frontières contrôlées

- le chapitre 3 conserve la définition des suites, cas, fixtures et oracles de test ;
- le chapitre 13 conserve l’exploitation du serveur dédié, les credentials runtime, le pare-feu et le durcissement réseau ;
- le chapitre 14 possède l’orchestration CI/CD, les branches, tags, matrices, artefacts et preuves automatisées ;
- le chapitre 15 conserve RPO, RTO, sauvegardes globales, restaurations et reprise après catastrophe ;
- le chapitre 16 conserve les presets Godot, formats, installateurs, signatures de plateforme et détails du packaging ;
- le chapitre 17 conserve boutiques, distribution commerciale et publication ;
- aucune validation documentaire ne devient une preuve de build, d’installation ou de déploiement.

## 4. Contrôles pédagogiques

- CI, livraison, déploiement et publication distingués ;
- branches courtes, pull requests et tags immuables documentés ;
- version produit, commit, run, tentative, build ID et empreinte séparés ;
- scripts canoniques séparés des workflows YAML ;
- événements `pull_request`, `push`, `workflow_dispatch`, tags et `pull_request_target` qualifiés ;
- permissions minimales de `GITHUB_TOKEN` documentées ;
- entrées de contexte traitées comme non fiables ;
- actions externes inventoriées et destinées à être épinglées ;
- matrices explicites avec `fail-fast`, caractère requis et timeout ;
- vérification de Godot et des archives par SHA-256 ;
- environnement Python isolé et dépendances verrouillées ;
- cache, artefact et source canonique séparés ;
- staging confiné et nettoyé ;
- workflow de pull request sans secrets préparé ;
- appel Godot headless orchestré sans définir les presets du chapitre 16 ;
- construction et promotion séparées ;
- workflow réutilisable et sorties typées préparés ;
- rétention, manifeste fermé et vérification stricte documentés ;
- logs, rapports et résumé d’échec distingués ;
- secrets ciblés, environnements protégés et OIDC encadrés ;
- concurrence, timeouts et retries bornés ;
- statuts d’échec et tentatives séparés ;
- reproductibilité de procédure distinguée de la reproductibilité binaire ;
- attestations, scan de secrets, dépendances et runners auto-hébergés encadrés ;
- clone neuf, modes Solo/Studio, budgets et porte de promotion préparés ;
- tous les repères `[PS]`, `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]`, `[VSC]`, `[WEB]`, `[APP]`, `[SORTIE]` et `[LECTURE]` sont utilisés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- synthèse opérationnelle `Project Asteria` présente.

## 5. Contrôles documentaires

- lignes : 2 663 ;
- titres : 106 ;
- blocs de code ou données : 66 ;
- blocs significatifs : 56 ;
- marqueurs d’explication : 66 ;
- explications structurées hors diagnostics : 46 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- section Solo/Studio en Markdown ordinaire ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre respecte la syntaxe et les frontières générales de GitHub Actions : événements, jobs, steps, permissions, `workflow_call`, matrices, `needs`, environnements, sorties, concurrence, timeouts, artefacts et OIDC. Il distingue l’exécution de code non fiable des jobs autorisés à accéder à des secrets ou à des identités de déploiement.

Il documente l’épinglage des actions par SHA complet comme cible Studio, l’usage de `persist-credentials: false` pour les validations sans écriture, la différence entre caches reconstructibles et artefacts, ainsi que la promotion du même artefact après vérification.

Pour Godot, il conserve la version de référence `4.7.1-stable`, utilise `--headless`, `--path`, `--export-debug` ou `--export-release`, exige un preset fourni et vérifie le code de retour et la sortie. Il ne prétend pas qu’un preset, template ou export a été exécuté.

Les exemples Python expliquent types, paramètres, valeurs de retour, exceptions, effets de bord, confinement des chemins, appels de processus, empreintes, manifestes, retries et archives stables. Les exemples PowerShell, batch et Bash propagent les codes de retour et bornent leurs entrées.

## 7. Contrôle des régressions

- `main` reste la branche principale intégrée ;
- une branche dédiée et une pull request restent obligatoires ;
- le chapitre ne déplace pas silencieusement un tag ;
- une pull request non fiable ne reçoit aucun secret ;
- `pull_request_target` n’est pas utilisé pour exécuter le code proposé avec des privilèges ;
- un code de retour non nul reste bloquant ;
- un cache ne devient pas source canonique ni preuve ;
- un candidat est promu sans reconstruction ;
- le staging refuse les chemins sortants et les fichiers inattendus ;
- les actions externes ne sont pas supposées sûres par leur seul tag ;
- les artefacts n’embarquent ni workspace complet ni credentials ;
- les retries ne masquent pas les tests déterministes ;
- les rapports distinguent non-exécution, échec, timeout et panne d’infrastructure ;
- aucune reproductibilité binaire n’est affirmée sans campagne ;
- aucune métrique de CI n’acquiert d’autorité de publication ;
- le chapitre ne consomme pas les responsabilités des chapitres 15 à 17 ;
- l’approbation finale reste humaine et réversible.

## 8. Réserves ouvertes

- scripts `tools/ci/*` de `Project Asteria` non matérialisés ;
- workflows CI/CD de `Project Asteria` non matérialisés ;
- protections de branche et rulesets non configurés dans un dépôt de jeu ;
- actions externes hors checkout non épinglées ni qualifiées ;
- versions et empreintes Godot/templates non installées dans une chaîne ;
- lockfiles et dépendances CI non matérialisés ;
- runners Windows/Linux et runners spécialisés non qualifiés ;
- cache miss et cache poisoning non testés ;
- matrice de plateformes non exécutée ;
- tests rapides, complets et de plateforme non exécutés ;
- exports et packages non produits ;
- manifestes et empreintes d’artefact non produits sur un build réel ;
- rétention réelle non configurée ni mesurée ;
- secrets, environnements et approbations non configurés ;
- échange OIDC non exécuté ;
- SBOM et attestations non générés ;
- scan de secrets et analyse de dépendances non exécutés ;
- promotion du même artefact non exercée ;
- reprise après timeout ou panne de runner non exercée ;
- reconstruction depuis clone neuf non exécutée ;
- comparaison de deux constructions indépendantes non réalisée ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt doivent confirmer structure, repères, explications, liens, doublons, frontières et absence de PDF. La preuve QA peut être fermée avec les réserves déclarées, sans revendiquer les exécutions nécessaires au niveau `runtime-tested`.
