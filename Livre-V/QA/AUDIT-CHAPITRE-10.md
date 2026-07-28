---
title: "Audit — Livre V, fiche 10 : Bibliothèque de scripts et recettes de code"
id: "DOC-L5-QA-AUDIT-CH10"
status: "complete"
version: "1.0.0"
last-verified: "2026-07-28T21:24:52+02:00"
lang: "fr-FR"
book: "Livre V"
chapter: 10
audit-date: "2026-07-28T21:24:52+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 10 : Bibliothèque de scripts et recettes de code

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des recettes GDScript, Python, PowerShell et Bash, distingue squelettes statiques et composants qualifiés, et ne présente aucun bloc comme parsé, testé ou prêt pour la production.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md` ;
- identifiant : `DOC-L5-CH10` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- documentations officielles de Godot, Python, PowerShell et Bash revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | 528 |
| titres | 18 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 46 |
| renvois vers les Livres I à IV | 18 |
| liens profonds vers les sources propriétaires | 18 |
| liens officiels | 7 |
| blocs clôturés | 8 |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| scripts courts GDScript | règle pure et contrôle `SceneTree` headless |
| scripts courts Python | CLI de staging et chargeur JSON borné |
| scripts courts PowerShell | wrapper de programme natif et propagation du code |
| scripts courts Bash | contrôle de fichier avec statuts explicites |
| contexte et paramètres | environnement, entrées, bornes et dossier courant par carte |
| sorties et erreurs | stdout, stderr, fichiers, codes et sorties partielles distingués |
| recette pédagogique et production | taxonomie de huit statuts de preuve |
| exemples d’appel | appels Godot et Python explicitement non exécutés |
| tests minimaux | douze contrôles par recette et campagne Q1 à Q12 |
| licences | source, snippet, dépendance, fixture et publication distingués |
| code complexe | maintenu hors fiche et réservé au Companion Pack |
| exécution ou statut statique | chaque bloc porte `static-skeleton` et la réserve associée |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les tutoriels détaillés restent dans les Livres I à IV ;
- la fiche 08 conserve workflows et orchestration ;
- la fiche 09 conserve prompts et critères d’évaluation ;
- le chapitre 10 conserve les recettes courtes et leur index ;
- les chapitres 11 et 12 conserveront les références GDScript et Python ;
- le chapitre 13 conservera les formats d’échange ;
- les diagnostics transversaux resteront au chapitre 20 ;
- les campagnes et mesures resteront au chapitre 21 ;
- les compatibilités, checklists et licences resteront aux chapitres 22, 24 et 25 ;
- les fichiers exécutables réels resteront au Companion Pack.

## 6. Séparation définition et exécution

Les cartes distinguent `pedagogical`, `static-skeleton`, `syntax-checked`, `unit-tested`, `integration-tested`, `qualified`, `production` et `withdrawn`. Aucune carte n’annonce :

- un parse GDScript ou un lancement Godot ;
- une compilation, un import ou un test Python ;
- une analyse ou une exécution PowerShell ;
- un `bash -n` ou une exécution WSL ;
- un programme natif réellement appelé ;
- un workspace temporaire, une fixture ou un fichier de staging produit ;
- une compatibilité multiplateforme ou une performance mesurée.

## 7. Code et repères

Les 8 blocs sont précédés d’un repère d’utilisation reconnu. Chaque recette nomme entrées, sorties, erreurs, effets et statut. Le validateur d’explication détaillée ne s’applique pas au Livre V, mais les blocs restent proportionnés et renvoient aux tutoriels propriétaires.

## 8. Sécurité et licences

Les contrôles couvrent chemins canoniques, staging, sorties partielles, programmes allowlistés, arguments séparés, secrets, réseau, privilèges, fichiers tiers, empreintes, licences des snippets et dépendances. Une petite taille de script n’est jamais assimilée à un faible rayon d’impact.

## 9. Liens et sources

Les 18 renvois vers les Livres I à IV évitent de recopier les cours de langage, les tests, la sécurité et l’automatisation. Les 18 fragments ciblent notamment la nature de GDScript, les codes PowerShell, les tests, les journaux et les frontières de workspace.

Les liens externes pointent vers les documentations officielles de Godot 4.7, Python 3.14, PowerShell 7.6 et GNU Bash revues le 28 juillet 2026. Leur présence ne constitue ni installation, ni parse, ni exécution.

## 10. Réserves ouvertes

1. aucun fichier GDScript parsé et aucun moteur Godot lancé ;
2. aucun module Python compilé, importé ou exécuté ;
3. aucun script PowerShell analysé ou exécuté ;
4. aucun script Bash vérifié et aucun WSL utilisé ;
5. aucune fixture, arborescence temporaire ou sortie de staging créée ;
6. aucun programme natif, processus enfant ou timeout testé ;
7. aucun chemin sortant, lien symbolique, secret ou injection testé ;
8. aucune dépendance installée, verrouillée ou reconstruite ;
9. aucune campagne d’idempotence, interruption, repli ou retrait réalisée ;
10. aucune mesure de durée, mémoire, portabilité ou performance produite ;
11. aucune approbation juridique ni artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 11. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, cartes, matrices, liens profonds, repères de tous les blocs et absence de PDF. Les recettes restent `static-reviewed` jusqu’à leurs campagnes propres dans des environnements enregistrés.
