---
title: "Livre V — Fiche 24 : Checklists de production et de publication"
id: "DOC-L5-CH24"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 24
last-verified: "2026-07-29T23:31:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T23:31:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-24.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "phase-gates-checklists-evidence-exceptions-approvals-and-reopening"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Checklists de production et de publication

> **Type de document :** contrats de checklist, portes par phase, vues Solo/Studio, formulaires de preuve, règles d’exception, approbation et réouverture.
> **Lecture :** choisir la phase, charger uniquement les contrôles applicables, joindre les preuves propriétaires, puis rendre une décision explicite sans convertir une case cochée en preuve.
> **Principe :** une checklist rappelle et consolide ; elle ne remplace ni la procédure, ni le test, ni l’approbateur, ni l’artefact qui démontrent le résultat.

## Règles de lecture

| Règle | Conséquence |
|---|---|
| une ligne = une assertion vérifiable | éviter les items composites et les formulations vagues |
| l’obligation vient d’une politique ou d’un risque nommé | ne pas marquer arbitrairement tout comme obligatoire |
| la preuve reste chez son propriétaire | le lien ou l’identifiant est enregistré, pas recopié |
| `non_applicable` exige une justification | une case ignorée ne devient pas automatiquement hors périmètre |
| une exception possède portée et expiration | aucune dérogation permanente implicite |
| une signature atteste une décision bornée | elle ne prouve pas personnellement tous les contrôles |
| une checklist peut être rouverte | changement de build, preuve expirée ou incident invalide la clôture |

**Réponse rapide :** le cycle officiel de [production, validation et publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#1-le-cycle-de-vie-officiel) définit les phases ; la [stratégie QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#1-rôle-du-chapitre) définit risques, preuves et portes. La présente fiche fournit leur forme transversale de consultation.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir une ligne de checklist complète | [CHK-00](#chk-00--contrat-dun-item-de-checklist) |
| distinguer obligation, recommandation et option | [Matrice A](#matrice-a--obligation-statut-et-action) |
| choisir phase, lot et porte | [CHK-01](#chk-01--phase-lot-portée-et-porte) |
| écrire un contrôle atomique | [CHK-02](#chk-02--formulation-atomicité-et-oracle) |
| joindre une preuve traçable | [CHK-03](#chk-03--preuve-source-et-traçabilité) |
| trouver le chapitre propriétaire | [Matrice B](#matrice-b--routage-des-contrôles-par-phase) |
| préparer un lot avant production | [CHK-04](#chk-04--préparation-entrées-et-prérequis) |
| intégrer contenu, code et assets | [CHK-05](#chk-05--production-intégration-et-candidat) |
| fermer la QA produit | [CHK-06](#chk-06--qa-sécurité-accessibilité-et-localisation) |
| qualifier export et package | [CHK-07](#chk-07--build-export-package-et-installation) |
| préparer publication et support | [CHK-08](#chk-08--publication-distribution-et-support) |
| adapter Solo et Studio | [CHK-09](#chk-09--vues-solo-studio-et-séparation-des-rôles) |
| rendre une décision de porte | [Matrice C](#matrice-c--décisions-de-porte-et-réouverture) |
| encadrer une exception | [CHK-10](#chk-10--écarts-réserves-dérogations-et-expiration) |
| approuver et signer | [CHK-11](#chk-11--approbation-signature-et-responsabilité) |
| maintenir, rouvrir et retirer | [CHK-12](#chk-12--versionnement-réouverture-historique-et-retrait) |

---

<!-- l5:card -->
## CHK-00 — Contrat d’un item de checklist

| Champ | Règle |
|---|---|
| identifiant | stable, unique dans le registre et indépendant de la formulation affichée |
| phase | préparation, production, intégration, QA, build, publication, exploitation ou archivage |
| porte | transition exacte que l’item protège |
| objet | lot, commit, build, asset, package, page, canal, sauvegarde ou archive identifié |
| assertion | phrase affirmative et testable, sans « vérifier que tout va bien » |
| obligation | `required`, `recommended` ou `optional`, avec autorité et justification |
| applicabilité | condition qui rend l’item applicable au lot et au scénario |
| méthode | revue, test, mesure, inspection, comparaison, restauration ou approbation |
| oracle | condition observable de réussite, d’échec, de blocage ou d’indétermination |
| preuve | identifiant, lien, artefact, rapport, capture, manifeste, empreinte ou décision |
| propriétaire | rôle qui prépare ou exécute le contrôle |
| approbateur | rôle autorisé à accepter le résultat ou l’exception |
| statut | état courant, distinct de l’obligation |
| réserve | limite connue qui reste visible après décision |
| expiration | date, version ou événement qui force une nouvelle revue |
| historique | auteur, horodatage, changement, motif et lien vers le prédécesseur |

**Réponse rapide :** la [définition de « terminé »](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#2-définition-de-terminé) fournit les attentes générales ; le [vocabulaire QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#5-vocabulaire-opérationnel) sépare preuve, réserve, dérogation et porte.

**Diagramme compact :** `risque ou obligation → item atomique → méthode + oracle → preuve propriétaire → décision bornée → expiration ou réouverture`.

**Niveau de preuve :** `static-review`. Aucun formulaire n’est rempli, aucune case n’est cochée et aucune publication de `Project Asteria` n’est approuvée dans cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Obligation, statut et action

| Dimension | Valeur | Signification | Action permise |
|---|---|---|---|
| obligation | `required` | condition imposée par politique, risque, contrat ou plateforme | la porte ne passe pas sans réussite ou dérogation autorisée |
| obligation | `recommended` | contrôle dont l’absence augmente un risque connu | exiger justification si omis |
| obligation | `optional` | contrôle utile seulement dans certains scénarios | exécuter si valeur supérieure au coût |
| statut | `not_started` | aucun travail ni preuve enregistrés | planifier, ne pas conclure |
| statut | `in_progress` | contrôle commencé mais non clos | conserver propriétaire et échéance |
| statut | `passed` | oracle satisfait avec preuve consultable | consommer la preuve dans la porte |
| statut | `passed_with_reservation` | oracle principal satisfait avec limite acceptée | afficher réserve, propriétaire et suivi |
| statut | `failed` | oracle non satisfait | corriger ou refuser la porte |
| statut | `blocked` | précondition ou moyen absent | lever le blocage ou reporter |
| statut | `indeterminate` | preuve insuffisante ou contradictoire | compléter ou décider `HOLD` |
| statut | `not_applicable` | relation sans sens dans le périmètre identifié | conserver justification et approbateur |
| statut | `waived` | écart temporairement accepté | conserver risque, portée, expiration et autorité |
| statut | `stale` | preuve invalidée par l’âge ou un changement | réexécuter avant consommation |
| statut | `superseded` | item remplacé par une version identifiée | suivre le successeur, garder l’historique |

**Décision :** obligation et statut ne sont jamais fusionnés. Un contrôle `optional` peut échouer sans bloquer une porte ; un contrôle `required` non commencé ne devient pas réussi parce qu’il est absent de la vue.

---

<!-- l5:card -->
## CHK-01 — Phase, lot, portée et porte

| Question | Réponse attendue |
|---|---|
| quelle phase ? | nom canonique et critères d’entrée/sortie |
| quel lot ? | identifiant, version, commit, build ou ensemble d’assets |
| quel scénario ? | Solo, Studio, développement, CI, test, release, publication ou maintenance |
| quelle cible ? | plateforme, locale, canal, renderer, architecture ou profil |
| quelle porte ? | transition autorisée si les contrôles applicables sont résolus |
| quelle autorité ? | politique, chapitre propriétaire, contrat de plateforme ou décision de projet |
| quelles dépendances ? | preuves amont nécessaires avant d’ouvrir la phase |
| quelle fenêtre ? | date de gel, échéance, période d’observation ou version limite |
| quelle sortie ? | `PASS`, `PASS_WITH_RESERVATIONS`, `HOLD`, `REJECT` ou `REOPENED` |
| quel repli ? | retour au lot précédent, correction ciblée, réduction de portée ou annulation |

**Réponse rapide :** les [critères d’entrée et de sortie](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#5-vocabulaire-opérationnel) précèdent la checklist. Les [branches, pull requests et promotions](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#7-choisir-une-stratégie-de-branches) identifient le lot technique sans remplacer la décision produit.

**Diagramme compact :** `phase amont close → entrées identifiées → contrôles applicables → décision → phase aval ou retour contrôlé`.

**Limite :** une checklist « release » générique ne peut pas qualifier simultanément tous les OS, locales, canaux et profils ; chaque vue porte une cible explicite.

---

<!-- l5:card -->
## CHK-02 — Formulation, atomicité et oracle

| Formulation utile | Formulation refusée |
|---|---|
| « le package `P` possède un manifeste dont l’empreinte correspond aux octets » | « package vérifié » |
| « le test `T` satisfait l’oracle `O` sur le build `B` » | « tests OK » |
| « aucune clé privée n’apparaît dans le lot livré selon le scan `S` » | « sécurité faite » |
| « la locale `L` passe pseudo-localisation et revue en contexte » | « traduction terminée » |
| « le candidat s’installe et se lance sur une machine propre `M` » | « export fonctionnel » |
| « la déclaration publique cite uniquement les fonctions d’accessibilité qualifiées » | « accessible » |
| « l’archive relie sources, outils, licences, rapports et procédure de reconstruction » | « sauvegarde créée » |

**Méthode :** séparer les verbes `préparer`, `exécuter`, `observer`, `approuver`, `publier`, `restaurer` et `archiver`. Un item ne mélange pas l’action et son approbation lorsqu’elles peuvent échouer indépendamment.

**Réponse rapide :** le [contrat d’un cas de test](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#6-contrat-dun-cas) possède entrée, action, attendu et preuve ; la [porte d’asset](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#1-rôle-du-chapitre) sépare contrôle technique, revue artistique et décision.

**Diagramme compact :** `objet exact + verbe unique + oracle observable + preuve nommée = item clôturable`.

**Limite :** une phrase atomique peut dépendre de plusieurs artefacts ; elle reste atomique si un seul jugement est rendu.

---

<!-- l5:card -->
## CHK-03 — Preuve, source et traçabilité

| Type de preuve | Ce qu’elle peut attester | Ce qu’elle ne prouve pas seule |
|---|---|---|
| rapport de test | scénario, environnement, résultat et oracle | absence de défaut hors scénario |
| artefact CI | exécution d’un job et sorties conservées | qualité du produit entier |
| manifeste et checksum | identité et intégrité d’octets | authenticité, licence ou innocuité |
| capture | état visuel ou interface observée | comportement complet ou accessibilité universelle |
| rapport de revue | décision humaine et réserves | exécution technique non jointe |
| matrice de compatibilité | statut daté d’une relation | support de toutes les versions voisines |
| benchmark | mesure selon protocole identifié | propriété universelle de la solution |
| reçu de plateforme | soumission, traitement ou approbation nommé | publication dans tous les territoires |
| preuve de restauration | récupération d’un objet ou service | reconstruction historique complète |
| signature | attestation d’une identité ou décision selon le contrat | véracité de tout le contenu signé |

**Réponse rapide :** la [fiche 21](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md#matrice-c--niveaux-de-preuve-et-déclarations-permises) borne les mesures ; la [fiche 22](CHAPITRE-22-Matrices-de-compatibilite.md#comp-02--sources-preuves-et-traçabilité) borne la compatibilité ; le [chapitre DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#6-cartographier-la-chaîne-de-confiance) relie commit, run, artefact et approbation.

**Diagramme compact :** `item → preuve primaire → empreinte ou identifiant → source propriétaire → consommateur de porte`.

**Intégrité :** une case ne contient jamais « voir Slack », « testé hier » ou un chemin local non partagé comme preuve unique.

---

<!-- l5:matrix -->
## Matrice B — Routage des contrôles par phase

| Famille de contrôle | Propriétaire documentaire | Preuve consommée par la checklist |
|---|---|---|
| cycle documentaire et publication du guide | [Volume 0, chapitre 10](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#20-critères-de-blocage-dune-publication) | statut, compilation, liens, licences et blocages |
| architecture Solo/Studio | [Livre II, chapitre 30](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles) | responsabilités, plateformes et approbations |
| tests unitaires, intégration et simulation | [Livre II, chapitre 27](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md#3-portfolio-de-tests) | suites, scénarios, graines et résultats |
| validation d’un asset | [Livre III, chapitre 29](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#4-frontières-avec-les-chapitres-voisins) | manifeste, import, mesures et revue |
| stratégie QA et risques | [Livre IV, chapitre 2](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#1-rôle-du-chapitre) | risques, portes, réserves et dérogations |
| tests fonctionnels et régression | [Livre IV, chapitre 3](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#6-contrat-dun-cas) | cas, attendu, observé, résultat et preuve |
| CI, artefacts et promotion | [Livre IV, chapitre 14](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#8-définir-les-portes-de-pull-request) | run, commit, artefact, permissions et approbation |
| sauvegarde et reprise | [Livre IV, chapitre 15](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md#1-rôle-du-chapitre) | copie, restauration, RPO/RTO et exercice |
| export et packaging | [Livre IV, chapitre 16](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#6-distinguer-export-packaging-et-publication) | preset, package, manifeste, signature et machine propre |
| publication et distribution | [Livre IV, chapitre 17](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md#1-rôle-du-chapitre) | page, média, classification, soumission et support |
| accessibilité | [Livre IV, chapitre 18](../Livre-IV/CHAPITRE-18-Accessibilite.md#1-rôle-du-chapitre) | parcours, options, limites et déclaration vérifiée |
| localisation | [Livre IV, chapitre 19](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md#1-rôle-du-chapitre) | catalogues, polices, pseudo-localisation et revue |
| correctifs et rollback | [Livre IV, chapitre 20](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md#4-modèle-mental-une-mise-à-jour-est-une-transaction-distribuée) | canaux, migration, observation, arrêt et récupération |
| maintenance et archivage | [Livre IV, chapitre 22](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#4-modèle-mental-conserver-un-système-pas-seulement-un-zip) | inventaire, fixité, restauration, reconstruction et succession |
| mesures et comparaison | [fiches 21 à 23](CHAPITRE-23-Comparatifs-des-solutions.md#cmp-00--contrat-minimal-dun-comparatif) | résultats datés, compatibilité et décision conditionnelle |
| licences et conformité | future fiche 25 | registre, obligations, attributions et avis spécialisé |

**Décision :** la checklist référence ces preuves sans recopier leurs procédures. Une ligne bloquée ouvre le chapitre propriétaire, pas une procédure parallèle dans la fiche 24.

---

<!-- l5:card -->
## CHK-04 — Préparation, entrées et prérequis

| Contrôle | Niveau par défaut | Preuve attendue |
|---|---|---|
| objectif, public et résultat du lot identifiés | `required` | brief, ticket, fiche de préparation ou contrat |
| périmètre et exclusions écrits | `required` | section de portée versionnée |
| sources canoniques et autorités nommées | `required` | carte de responsabilité ou manifeste |
| dépendances, versions et licences préqualifiées | `required` | inventaire et liens officiels |
| risques de perte, sécurité, confidentialité et publication triés | `required` | registre de risques |
| critères d’entrée et de sortie définis | `required` | politique de porte |
| fixtures, données et assets d’essai autorisés | `required` si test | manifeste de provenance |
| environnement et plateformes cibles déclarés | `required` si exécution | matrice de compatibilité |
| budget de temps, mémoire, taille ou qualité défini | `recommended` | profil ou budget approuvé |
| repli, sauvegarde et annulation préparés | `required` si mutation | procédure propriétaire |
| calendrier et propriétaires assignés | `recommended` Solo, `required` Studio | registre de responsabilités |

**Réponse rapide :** la [préparation d’un contenu](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#3-préparation-dun-nouveau-contenu) fournit le socle documentaire ; la [charte QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#6-charte-qa-de-project-asteria) relie qualités, risques et autorités.

**Diagramme compact :** `besoin → portée → propriétaires → risques → critères → ressources autorisées → phase ouverte`.

**Porte :** aucun travail irréversible ou coûteux n’est lancé lorsque l’autorité, la source ou le retour arrière restent inconnus.

---

<!-- l5:card -->
## CHK-05 — Production, intégration et candidat

| Domaine | Contrôles transversaux |
|---|---|
| code | conventions, analyse statique, tests ciblés, secrets absents, dépendances déclarées |
| données | schéma, types, bornes, migrations, valeurs manquantes et source canonique |
| assets | identité, provenance, famille, profil d’import, budget et revue artistique |
| IA | modèle exact, licence, entrée autorisée, sortie classée brouillon et validation humaine |
| configuration | valeurs par profil, secret séparé, défauts explicites et validation au chargement |
| documentation | objectif, prérequis, liens, versions, résultats attendus et réserves |
| intégration | commit identifié, diff ciblé, conflits résolus et autorité non contournée |
| candidat | contenu gelé, version, manifeste, liste des changements et défauts connus |
| suppression | dépendances, migrations, données, support et archive traités avant retrait |
| reproduction | clone ou environnement propre capable de reconstruire le candidat selon la portée |

**Réponse rapide :** les [incréments cohérents](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#4-rédaction-par-incréments) interdisent les livrables coupés ; la [chaîne de confiance CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#6-cartographier-la-chaîne-de-confiance) exige un candidat relié à sa révision et à ses preuves.

**Diagramme compact :** `sources canoniques → production → validation spécialisée → intégration ciblée → candidat gelé + manifeste`.

**Limite :** le passage d’une tâche à « terminé » dans un gestionnaire de projet ne qualifie ni le candidat ni ses dépendances.

---

<!-- l5:card -->
## CHK-06 — QA, sécurité, accessibilité et localisation

| Famille | Question de porte | Sortie minimale |
|---|---|---|
| fonctionnel | les parcours critiques satisfont-ils leurs oracles ? | rapport de campagne et défauts ouverts |
| régression | les invariants approuvés restent-ils stables ? | suite versionnée et comparaison |
| performance | les budgets applicables sont-ils respectés selon le protocole ? | observations, statistiques et réserves |
| sécurité | secrets, permissions, entrées, dépendances et surfaces ont-ils été revus ? | rapport, exceptions et propriétaire |
| confidentialité | les données sont-elles minimisées, autorisées, protégées et retenues selon la politique ? | registre et décision |
| accessibilité | les barrières ciblées et déclarations ont-elles été vérifiées sur le build ? | parcours, captures, limites et version |
| localisation | chaînes, polices, écritures, voix et interfaces ont-elles été validées par locale ? | couverture, pseudo-localisation et revue |
| compatibilité | les plateformes et versions requises possèdent-elles une preuve actuelle ? | cellules datées et artefacts |
| sauvegarde | migration, chargement, restauration et schémas futurs ont-ils été exercés selon la portée ? | rapport sur copies et rollback |
| diagnostic | logs, corrélation et paquet de support permettent-ils une enquête proportionnée ? | exemple de paquet revu |
| conformité | licences, provenance, attributions et obligations sont-elles résolues ? | registre ou blocage explicite |

**Réponse rapide :** la [validation technique](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#7-validation-technique), la [validation de sécurité](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#9-validation-de-sécurité), l’[accessibilité produit](../Livre-IV/CHAPITRE-18-Accessibilite.md#3-niveau-de-preuve-et-réserves) et la [localisation](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md#5-concevoir-les-locales-prises-en-charge) restent des portes distinctes.

**Porte :** un statut vert global ne masque jamais un blocage de sécurité, de perte de données, de licence ou une déclaration publique non prouvée.

---

<!-- l5:card -->
## CHK-07 — Build, export, package et installation

| Contrôle | Preuve exigée |
|---|---|
| commit, version produit et build ID corrélés | manifeste de build |
| dépendances, templates, SDK et runners identifiés | inventaire ou lockfiles qualifiés |
| preset et profil correspondent à la cible | configuration versionnée |
| ressources privées, tests et secrets exclus | rapport d’inventaire du package |
| octets assemblés dans un staging neuf | journal et liste fermée |
| checksums calculés après fermeture | fichier d’empreintes |
| signature ou notarisation réellement applicable | reçu et identité du signataire |
| package installé hors du dépôt | journal de machine propre |
| lancement et parcours minimal exécutés | résultat de smoke test |
| désinstallation, mise à jour et repli préparés | procédure et test approprié |
| artefact conservé sans reconstruction entre portes | identifiant d’artefact et promotion |
| défauts connus, limites et plateformes bloquées publiés | note de candidat |

**Réponse rapide :** le [chapitre 16](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#4-prérequis-et-frontières) possède presets, packages, signature et installation ; le [chapitre 14](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) possède artefacts et promotion.

**Diagramme compact :** `commit → build identifié → staging fermé → manifeste + empreintes → installation propre → candidat de publication`.

**Blocage :** une archive produite, un export local ou une CI verte ne vaut pas installation et lancement sur la plateforme cible.

---

<!-- l5:card -->
## CHK-08 — Publication, distribution et support

| Contrôle | Applicabilité |
|---|---|
| même build qualifié relié à la fiche produit | toute publication |
| titre, descriptions, captures et vidéos exacts | page publique |
| déclarations de fonctionnalités et limites prouvées | toute communication |
| prix, territoires, taxes et devises approuvés | offre commerciale |
| classification d’âge et contenus sensibles traités | plateformes concernées |
| licences, marques, attributions et crédits prêts | toute distribution |
| confidentialité, collecte et services tiers déclarés | si données ou réseau |
| accessibilité et langues annoncées limitées aux preuves | toute page correspondante |
| canaux, branches, clés et accès test définis | bêta ou accès anticipé |
| soumission, revue et reçus archivés | plateforme avec portail |
| date, fuseaux, embargo et communication coordonnés | lancement planifié |
| support, diagnostic, statut et escalade opérationnels | avant ouverture au public |
| correctif, interruption et rollback préparés | toute version distribuée |
| notes de version et défauts connus publiés | release ou mise à jour |

**Réponse rapide :** la [préparation d’une publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#13-préparation-dune-publication) définit le lot documentaire ; le [chapitre 17](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md#1-rôle-du-chapitre) possède pages, soumissions et support ; le [chapitre 20](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md#1-rôle-du-chapitre) possède l’après-lancement.

**Limite :** la checklist ne saisit aucun prix réel, ne crée aucun compte et n’effectue aucun téléversement.

---

<!-- l5:card -->
## CHK-09 — Vues Solo, Studio et séparation des rôles

| Responsabilité | Vue Solo | Vue Studio |
|---|---|---|
| préparation | même personne, session dédiée et journal | producteur et propriétaire nommés |
| exécution | scripts locaux reproductibles | CI et environnements contrôlés |
| relecture | pause et seconde passe explicite | relecteur indépendant selon le risque |
| sécurité | auto-revue séparée et preuve conservée | responsable sécurité pour exceptions critiques |
| licences | registre vérifié avant publication | responsable juridique ou licences |
| accessibilité | parcours documentés sans prétendre représenter tous les utilisateurs | sessions, experts ou panels selon le risque |
| publication | auto-approbation explicitement enregistrée | approbateur indépendant |
| secrets | stockage séparé du dépôt | séparation des accès et environnements protégés |
| archive | copie indépendante et test planifié | dépositaire et propriétaire technique distincts |
| réouverture | événement déclencheur enregistré | notification aux rôles affectés et nouvelle approbation |

**Réponse rapide :** la [revue Solo et Studio](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#11-revue-solo-et-revue-studio) autorise le cumul de rôles sans fusionner les étapes ; les [deux enveloppes opérationnelles](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles) ajoutent des contrôles sans changer le cœur.

**Diagramme compact :** `mêmes items et mêmes oracles → profondeur de preuve et indépendance adaptées au risque`.

**Porte :** un projet Solo n’imite pas une fausse équipe ; il sépare dans le temps préparation, exécution, revue et décision.

---

<!-- l5:matrix -->
## Matrice C — Décisions de porte et réouverture

| Décision | Conditions minimales | Effet | Réouverture automatique |
|---|---|---|---|
| `PASS` | tous les `required` applicables réussis, preuves actuelles, aucune réserve bloquante | phase aval autorisée | changement d’objet, preuve expirée ou incident pertinent |
| `PASS_WITH_RESERVATIONS` | objectifs principaux atteints, réserves acceptées, suivi et expiration | phase aval limitée au périmètre accepté | échéance, aggravation ou hypothèse invalidée |
| `HOLD` | contrôle bloqué, indéterminé ou preuve attendue | aucune promotion ; travail de résolution autorisé | preuve nouvelle ou précondition levée |
| `REJECT` | échec bloquant ou risque non acceptable | candidat refusé ou retour en correction | nouveau candidat identifié |
| `REOPENED` | décision antérieure invalidée | statut de porte retiré, contrôles affectés repassés à traiter | nouvelle décision formelle |
| `CANCELLED` | lot retiré ou objectif abandonné | clôture sans promotion | reprise seulement sous nouvel identifiant |
| `SUPERSEDED` | lot remplacé par un successeur | historique conservé, décisions non transférées | aucune ; évaluer le successeur |

**Autorité :** une automatisation peut proposer `HOLD` ou signaler un échec, mais la politique du projet détermine qui rend `PASS`, accepte une réserve ou autorise une dérogation.

**Diagramme compact :** `preuves + écarts + exceptions → décision → portée autorisée → surveillance → réouverture éventuelle`.

---

<!-- l5:card -->
## CHK-10 — Écarts, réserves, dérogations et expiration

| Champ d’exception | Obligation |
|---|---|
| identifiant | stable et recherchable |
| règle concernée | item et autorité exacts |
| écart observé | fait séparé de l’interprétation |
| risque | conséquence, probabilité et population exposée selon la méthode du projet |
| justification | raison de ne pas corriger avant la porte |
| portée | build, plateforme, locale, canal, durée et utilisateurs concernés |
| compensation | contrôle, surveillance, limitation ou repli |
| propriétaire | responsable du suivi |
| approbateur | autorité distincte si le risque l’exige |
| expiration | date, version, nombre d’expositions ou événement |
| sortie | correction, retrait, renouvellement explicite ou abandon |
| preuve | décision, discussion, rapport et artefacts liés |

**Réponse rapide :** la [stratégie QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md#5-vocabulaire-opérationnel) définit réserve et dérogation ; les [critères de blocage](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#20-critères-de-blocage-dune-publication) identifient les cas qui ne doivent pas être contournés silencieusement.

**Interdictions :** pas de dérogation implicite, sans expiration, réutilisée sur un nouveau build ou signée par un rôle sans autorité.

---

<!-- l5:card -->
## CHK-11 — Approbation, signature et responsabilité

| Élément | Règle |
|---|---|
| signataire | identité ou rôle autorisé, résolu dans un registre d’accès |
| objet signé | checklist, décision, manifeste ou rapport identifié par version et empreinte |
| assertion | décision exacte : revue effectuée, risque accepté, lot approuvé ou archive scellée |
| portée | plateforme, locale, canal, build et période |
| préconditions | preuves obligatoires consultables au moment de la signature |
| séparation | préparateur, exécuteur et approbateur distincts lorsque le risque le requiert |
| horodatage | date et fuseau, sans reconstruire une heure inconnue |
| mécanisme | signature manuscrite, approbation de PR, reçu de portail ou signature cryptographique selon le contrat |
| révocation | événement qui retire l’autorité ou invalide la décision |
| conservation | durée, emplacement, accès et lien vers l’objet |
| données | minimisation des données personnelles et absence de secret dans le formulaire |
| responsabilité | la signature atteste la décision, pas une garantie universelle ni un transfert de propriété technique |

**Réponse rapide :** la [chaîne de confiance](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#6-cartographier-la-chaîne-de-confiance) sépare validation et environnement protégé ; les [responsabilités d’archive](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#6-établir-les-responsabilités) montrent qu’une approbation dépend du rôle et de la succession.

**Limite :** une case portant un nom ne devient pas une signature cryptographique ; une signature cryptographique ne prouve pas que l’approbateur avait l’autorité organisationnelle.

---

<!-- l5:card -->
## CHK-12 — Versionnement, réouverture, historique et retrait

| Événement | Traitement |
|---|---|
| changement de formulation sans changement d’oracle | nouvelle version mineure de vue, identité stable |
| changement d’obligation, d’oracle ou d’autorité | nouvelle version du contrat et revue des lots ouverts |
| nouveau build ou commit | nouvelle instance de checklist, pas copie déclarée réussie |
| nouvelle plateforme, locale ou canal | vue distincte avec applicabilité recalculée |
| preuve expirée ou dépendance mise à jour | items affectés en `stale` et porte rouverte |
| incident après publication | réouverture ciblée, conservation de la décision historique |
| contrôle supprimé | motif, successeur et date de retrait |
| phase abandonnée | instance `cancelled`, preuves conservées selon la rétention |
| fin de support | checklist de retrait, données, communication, comptes et archive |
| archive | contrat, preuves, décisions, exceptions et historique corrélés au lot |

**Réponse rapide :** la [maintenance après publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#18-maintenance-après-publication), la [transaction de mise à jour](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md#4-modèle-mental-une-mise-à-jour-est-une-transaction-distribuée) et le [dossier de version](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#4-modèle-mental-conserver-un-système-pas-seulement-un-zip) empêchent de figer une checklist hors de son contexte.

**Cycle :** `draft → active → instantiated → decided → reopened ou closed → superseded → retired`, avec historique append-only des décisions.

**Limite :** réouvrir ne réécrit pas le passé ; la décision antérieure reste vraie pour l’objet et les preuves de son époque.

## Frontières documentaires

Cette fiche possède le contrat transversal des items, vues, preuves, exceptions, approbations et décisions. Elle ne possède pas :

- les procédures de production, de test, d’export, de publication, d’accessibilité, de localisation, de rollback ou d’archive ;
- les valeurs réelles d’un lot, d’un build, d’un prix, d’une classification, d’une plateforme ou d’une locale ;
- la décision juridique sur les licences et la conformité, réservée à la future fiche 25 ;
- les tables globales de navigation, synonymes et croisements, réservées à la future fiche 26 ;
- les formulaires exécutables, tableurs, signatures, bases de preuves et automatisations, réservés au Companion Pack.

**Règles permanentes :**

1. une checklist ne prouve rien sans preuve propriétaire ;
2. une case vide n’est ni un échec ni une non-applicabilité ;
3. un item obligatoire ne disparaît pas d’une vue pour permettre le passage ;
4. une réussite sur un build ne se transfère pas automatiquement au suivant ;
5. une dérogation ne dépasse jamais sa portée et son expiration ;
6. une signature atteste une décision bornée ;
7. une porte peut rester indéterminée ;
8. un incident ou changement pertinent peut rouvrir une décision ;
9. l’historique est conservé sans modifier rétroactivement les anciennes décisions ;
10. aucune checklist de cette fiche n’est présentée comme exécutée.
