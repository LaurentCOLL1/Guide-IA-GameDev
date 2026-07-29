---
title: "Audit — Livre V, Fiche 16 : Patrons d’architecture"
id: "DOC-L5-QA-AUDIT-CH16"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 16
audit-date: "2026-07-29T06:49:56+02:00"
audit-level: "static-review"
document-format: "reference-cards"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit — Fiche 16 : Patrons d’architecture

## 1. Décision

**Décision : accepté au niveau `static-review`, avec preuve runtime limitée aux contrats synthétiques.**

La fiche respecte le profil spécialisé du Livre V : consultation non linéaire, cartes et matrices en premier, paragraphes courts, renvois fréquents vers les chapitres propriétaires et absence de tutoriel complet dupliqué.

Aucun patron n’est présenté comme architecture universelle. Chaque choix reste lié à un problème, un contexte, des conséquences, une alternative et une porte de validation.

## 2. Périmètre du plan maître

Le plan maître demande :

- composition ;
- services ;
- repositories ;
- événements ;
- états ;
- problème, contexte, solution et conséquences ;
- anti-patterns ;
- lien avec `Project Asteria` ;
- fiches de patrons ;
- diagrammes ;
- exemples ;
- matrice d’usage ;
- validation par exemples testables et limites explicites.

La fiche couvre ces obligations avec treize cartes, trois matrices, sept diagrammes compacts et des exemples `Project Asteria`.

La propriété d’état et le cycle de vie sont traités comme questions d’architecture transversale. Les machines à états, capacités, inventaires, quêtes et simulations spécialisées restent à la fiche 17.

## 3. Forme documentaire

Mesures calculées sur la tête `dd26f85e540436cc86b2cc7523b8ea9ac623a882` :

| Mesure | Valeur |
|---|---:|
| lignes | 409 |
| titres | 19 |
| cartes `<!-- l5:card -->` | 13 |
| matrices `<!-- l5:matrix -->` | 3 |
| liens Markdown | 65 |
| renvois vers les Livres I à IV | 34 |
| liens profonds vers les Livres I à IV | 21 |
| liens officiels | 13 |
| diagrammes compacts | 7 |
| blocs clôturés | 0 |

L’index express ouvre directement chaque carte ou matrice. Les titres courts utilisent les identifiants `ARC-00` à `ARC-12`.

## 4. Couverture des cartes

| Unité | Couverture |
|---|---|
| ARC-00 | contrat d’un patron : problème, contexte, forces, structure, autorité, état, preuve et sortie |
| Matrice A | sélection par problème, solution de départ, anti-pattern et source propriétaire |
| ARC-01 | modules, couches, frontières et direction des dépendances |
| ARC-02 | composition root, création, injection, démarrage, arrêt et diagnostic |
| Matrice B | scène, `Node`, `RefCounted`, `Resource`, Autoload, Python et services |
| ARC-03 | composition, héritage, variantes et diagnostic de hiérarchie fragile |
| ARC-04 | services d’application, commandes, requêtes, événements et contrôleurs |
| ARC-05 | repositories, mapping, transactions et unité de travail bornée |
| ARC-06 | ports, adaptateurs et couche anti-corruption |
| ARC-07 | appels directs, signaux, médiation, bus typé et file durable |
| ARC-08 | propriétaire d’état, vues dérivées, durée de vie, démarrage et arrêt |
| ARC-09 | façade de module, contrat public et détails internes |
| ARC-10 | stratégies, fabriques, registres bornés et plugins |
| ARC-11 | coutures de test, doubles, tests de contrat et graphes de dépendances |
| Matrice C | gains, coûts, portes minimales et signaux de retrait |
| ARC-12 | anti-patterns, diagnostics et dix portes d’acceptation |

## 5. Sources internes propriétaires

Les renvois principaux visent notamment :

- Livre II, chapitre 4 — vocabulaire architectural, feature-first, direction des dépendances, composition, frontières et couches ;
- Livre II, chapitre 5 — injection, repository, bus typé, registre, cycle de vie et composition root ;
- Livre II, chapitres 8 et 9 — SQLite, transactions, sauvegarde et restauration ;
- Livre II, chapitres 11 à 13 — adaptateurs, protocoles et séparation production/runtime ;
- Livre II, chapitres 27 et 28 — tests, diagnostic et reproductibilité ;
- Livre II, chapitre 30 — autorités, dépendances et profils Solo/Studio ;
- Livre IV, chapitres 2, 4, 5 et 14 — QA, débogage, observabilité et CI ;
- Livre V, fiches 14 et 15 — stockage relationnel et index vectoriels comme adaptateurs spécialisés.

Les liens profonds ont été contrôlés automatiquement. Aucun contenu propriétaire long n’est recopié.

## 6. Sources officielles et spécialisées

Sources relues le 29 juillet 2026 :

- Godot 4.7 — Project organization ;
- Godot 4.7 — Scene organization ;
- Godot 4.7 — Autoloads versus regular nodes ;
- Godot 4.7 — Resources ;
- Martin Fowler — Inversion of Control Containers and the Dependency Injection pattern ;
- Martin Fowler — Repository ;
- Martin Fowler — What do you mean by “Event-Driven”?.

La documentation Godot confirme la flexibilité de l’organisation, l’intérêt de scènes autonomes ou faiblement couplées, l’injection depuis un contexte propriétaire, la distinction entre `Node` et `Resource`, ainsi que les coûts de l’accès global.

Les articles de Martin Fowler sont utilisés comme sources historiques spécialisées pour distinguer injection et Service Locator, caractériser Repository et séparer plusieurs styles événementiels. Ils ne sont pas présentés comme normes obligatoires de Godot.

## 7. Campagne synthétique exécutée

Workflow : `Temporary Livre V Chapter 16 Architecture Fixtures`.

Run final avec métriques : `30423850824`.

Tête source : `dd26f85e540436cc86b2cc7523b8ea9ac623a882`.

Artefact : `8712843349`.

Digest : `sha256:f5b8a0cbf70a3e0667a89736bf11a61ddbc03d37158270d29d62033e48ed862f`.

Runtime :

- CPython `3.12.3` ;
- plateforme `Linux-6.17.0-1020-azure-x86_64-with-glibc2.39` ;
- backend de fixture `python-stdlib-synthetic-architecture-graphs` ;
- durée `4.818 ms` ;
- 67 cas ;
- 67 réussites ;
- 0 échec.

Les cas couvrent :

- direction de dépendances et refus domaine → infrastructure ;
- graphes acycliques, cycles et ordre topologique ;
- ordre de démarrage et arrêt inverse ;
- dépendances explicites et détection du Service Locator ;
- choix appel, signal, bus ou file ;
- commandes, requêtes et événements après commit ;
- propriétaire unique de l’état ;
- cycle `CREATED → CONFIGURED → STARTED → STOPPED` ;
- repositories mémoire et substitut SQLite synthétique ;
- préparation, commit et compensation d’une unité de travail ;
- traduction de contrats externes ;
- façades bornées ;
- stratégies, fabriques et registres ;
- capacités de plugins ;
- composition et détection d’héritage profond ;
- manifests déterministes et ADR ;
- profils Solo/Studio ;
- doubles et tests de contrat ;
- détection de God object, manager générique et événements trop larges.

## 8. Limites de la campagne

La campagne n’exécute pas :

- Godot Engine ;
- GDScript ;
- une scène, un `Node`, une `Resource` ou un Autoload ;
- un addon ;
- SQLite ou un autre stockage ;
- un service réseau ou IA ;
- un processus compagnon ;
- une architecture de production ;
- une plateforme Windows, WSL ou export natif ;
- des données utilisateur, personnelles, secrètes ou de production.

Les graphes, repositories et unités de travail sont synthétiques. Ils qualifient les assertions du harnais, pas un composant permanent du Companion Pack.

## 9. Validation documentaire

Le workflow permanent `Validate Chapters Without PDF`, run `30423747724`, a réussi sur le chapitre brut.

Étapes réussies :

- structure, métadonnées, liens et doublons ;
- cartes et liens profonds du Livre V ;
- explications de code ;
- présence et cohérence des repères ;
- couverture des contextes ;
- absence de PDF.

Le chapitre ne contient aucun bloc clôturé. Aucun résultat runtime Godot n’est suggéré.

## 10. Frontières et absence de duplication

La fiche 16 :

- indexe les patrons transversaux ;
- renvoie aux tutoriels propriétaires des Livres II à IV ;
- ne reproduit pas le bootstrap complet du chapitre 5 ;
- ne reproduit pas les repositories SQLite du chapitre 8 ;
- ne reproduit pas les protocoles des chapitres 11 et 12 ;
- ne reproduit pas les suites de tests du chapitre 27 ;
- ne définit pas les patrons de gameplay de la fiche 17 ;
- ne matérialise aucun fichier permanent du Companion Pack.

Les exemples `Project Asteria` sont compacts et servent uniquement à reconnaître les responsabilités et conséquences.

## 11. Sécurité, licences et conformité

La fiche impose :

- capacités minimales pour les plugins ;
- validation des données externes ;
- traduction des erreurs tierces ;
- absence de droit implicite pour un addon ou service ;
- conservation de l’autorité métier hors des sorties IA et adaptateurs ;
- inventaire et qualification des dépendances avant adoption.

Les sources Godot sont sous licence documentaire du projet Godot. Les pages de Martin Fowler sont citées par lien et paraphrasées sans reproduction longue.

Aucune approbation juridique organisationnelle n’a été réalisée. La licence globale de la collection reste ouverte.

## 12. Intégrité

Empreinte SHA-256 du chapitre :

`23d740ea8746baf7aee5480536b0c89448d5e150e56bb0e543d8f74903fe0e38`

L’empreinte de cet audit est enregistrée dans la preuve finale.

## 13. Réserves

- niveau maintenu à `static-review` ;
- preuve runtime limitée à 67 contrats synthétiques en bibliothèque standard Python ;
- aucun graphe du projet réel n’a été extrait ;
- aucun import GDScript ou dépendance Godot n’a été analysé ;
- aucune scène de bootstrap ou façade permanente n’a été créée ;
- aucun test de performance, charge, concurrence ou mémoire ;
- aucune campagne multiplateforme ;
- aucun addon ou format binaire qualifié ;
- aucune approbation juridique ;
- aucun PDF produit ;
- licence globale et accessibilité avancée du PDF toujours ouvertes.

## 14. Critère d’acceptation

La fiche est acceptée parce qu’un lecteur peut :

1. partir d’un problème architectural plutôt que d’un nom de patron ;
2. identifier autorité, état, dépendances et cycle de vie ;
3. choisir une option plus simple lorsque l’indirection n’est pas justifiée ;
4. rejoindre le tutoriel propriétaire par un lien profond ;
5. distinguer appel, commande, événement et état ;
6. localiser composition, domaine, application, présentation et infrastructure ;
7. reconnaître Service Locator, God object, façade fuyante et héritage fragile ;
8. associer chaque patron à une porte de validation ;
9. comprendre les limites des fixtures synthétiques ;
10. distinguer revue statique, test de contrat et runtime Godot réel.
