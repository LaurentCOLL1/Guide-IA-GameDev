---
title: "Audit — Livre V, Fiche 14 : Schémas SQLite et migrations"
id: "DOC-L5-QA-AUDIT-CH14"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 14
last-verified: "2026-07-29T01:06:05+02:00"
audit-date: "2026-07-29T01:06:05+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 14 : Schémas SQLite et migrations

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire des schémas SQLite, transactions, migrations, sauvegardes et diagnostics. Une campagne temporaire de 36 contrôles a créé uniquement des bases synthétiques dans un répertoire isolé.

La référence documentaire est SQLite `3.53.4`, publiée le 24 juillet 2026. La campagne a réellement utilisé SQLite `3.45.1` via Python `3.12.3` et le module `sqlite3` `2.6.0`. Cette différence est conservée : la campagne qualifie les patrons exercés sur son runtime, pas la totalité des comportements de SQLite `3.53.4` ni un binding Godot.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| contrat de base | autorité, identité, moteur, schéma, migration et preuve | systèmes des Livres II et IV |
| identité et version | `application_id`, `user_version`, `schema_version`, options de compilation | adaptateur et manifeste du projet |
| types | affinités, stockage dynamique et tables `STRICT` | codecs et modèles applicatifs |
| clés | clé métier, clé technique, `rowid`, `WITHOUT ROWID`, `AUTOINCREMENT` | domaine propriétaire |
| contraintes | `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, colonnes générées | validation métier complémentaire |
| relations | clés étrangères, actions et temporalité différée | modèle relationnel du Livre II |
| index | simples, composites, partiels, expressions et plans | requêtes et mesures propriétaires |
| connexion | clés étrangères, journal, synchronisation, délai et sécurité | adaptateur SQLite |
| transactions | modes `BEGIN`, rollback et savepoints | unité de travail applicative |
| DDL | trois tables et un index de référence | migrations permanentes du Companion Pack |
| migrations | manifeste, checksum, version, reconstruction et base future | runner du Livre II |
| sauvegarde | copie fermée, Backup API, `VACUUM INTO`, WAL et restauration | Livre IV, chapitre 15 |
| diagnostics | intégrité, relations, schéma, plans et verrous | fiches 20 et 21 |
| sécurité | paramètres, limites, schéma non fiable et extensions | politiques des Livres I et IV |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express placé avant les cartes ;
- tables de décision avant les paragraphes ;
- consultation non linéaire et paragraphes courts ;
- liens profonds vers les tutoriels propriétaires ;
- trois extraits SQL minimaux, tous précédés du repère `[LECTURE]` ;
- entrées, sorties, effets, paramètres et réserves décrits proportionnellement ;
- aucune procédure Godot, installation d’addon ou scène recopiée ;
- aucun résultat d’apprentissage ni synthèse de tutoriel importé ;
- niveau de preuve et limites visibles.

## 4. Couverture du plan maître

| Exigence | Réponse |
|---|---|
| types | SQL-02 et Matrice B |
| clés | SQL-03 |
| contraintes | SQL-04 et SQL-05 |
| index | SQL-06 |
| transactions | SQL-07 et SQL-08 |
| modèles de migrations | SQL-10 et Matrice C |
| sauvegarde et restauration | SQL-11 |
| schémas de référence | SQL-09 |
| DDL | bloc minimal SQL-09 |
| migrations | bloc minimal SQL-10 |
| diagrammes | relations et dépendances exprimées par matrices compactes |
| requêtes de diagnostic | SQL-12 |
| création et migration d’une base de test | campagne temporaire 36/36 |

## 5. Exactitude technique statique

Les sources officielles SQLite ont été revues le 29 juillet 2026 : chronologie et version `3.53.4`, typage dynamique, tables `STRICT`, clés étrangères, pragmas, transactions, `ALTER TABLE`, Backup API, `VACUUM INTO`, WAL, limites et recommandations de sécurité.

La fiche distingue notamment :

- version documentaire du moteur et version réellement liée par un binding ;
- `application_id`, `user_version` et `schema_version` ;
- classe de stockage, affinité et type `STRICT` ;
- `INTEGER PRIMARY KEY` et autres déclarations de clé ;
- clé technique et identifiant métier ;
- contrainte immédiate et clé étrangère différée ;
- `integrity_check` et `foreign_key_check` ;
- transaction et savepoint ;
- migration, backfill, reconstruction et restauration ;
- copie fermée, Online Backup API et `VACUUM INTO` ;
- WAL et absence de garantie contre `SQLITE_BUSY` ;
- paramètres de valeurs et identifiants SQL dynamiques allowlistés.

## 6. Campagne temporaire SQLite

Le run spécialisé a exécuté 36 cas, tous réussis, sur `Linux-6.17.0-1020-azure-x86_64-with-glibc2.39` avec :

- Python `3.12.3` ;
- module `sqlite3` `2.6.0` ;
- moteur SQLite `3.45.1` ;
- 58 options de compilation enregistrées ;
- bases créées dans un répertoire temporaire synthétique ;
- aucun fichier utilisateur ou de production.

Les cas couvrent :

- version et options de compilation ;
- `application_id`, `user_version`, `schema_version`, clés étrangères et `trusted_schema` ;
- création de tables `STRICT` et refus de types ou contraintes invalides ;
- clé primaire, orphelin, cascade et contrainte différée ;
- rollback, savepoint et paramètres SQL ;
- migrations 1 et 2, checksums, divergence et refus d’une base future ;
- ajout de colonne et reconstruction de table ;
- présence d’index et utilisation dans un plan ;
- `quick_check`, `integrity_check` et `foreign_key_check` ;
- Backup API, `VACUUM INTO`, WAL et délai d’attente ;
- `WITHOUT ROWID` et identité de famille.

## 7. Corrections issues de la campagne

1. Le premier passage s’est arrêté avant exécution : le garde-fou attendait 36 cas alors que 35 étaient enregistrés. Un contrôle utile sur la séparation `schema_version` / `user_version` a complété la campagne.
2. Le second passage a obtenu 32/36. Les quatre échecs provenaient de `sqlite3.Connection.executescript()`, qui termine implicitement une transaction en cours. Le helper de fixture a été remplacé par des appels `execute()` unitaires, préservant `BEGIN IMMEDIATE ... COMMIT`.
3. Aucun de ces deux problèmes ne contredisait le DDL ou le contrat lecteur ; ils concernaient uniquement le harnais Python temporaire.

## 8. Frontières conservées

- l’intégration Godot-SQLite, l’adaptateur, les dépôts et le bootstrap restent au Livre II, chapitre 8 ;
- les snapshots et migrations de sauvegarde restent au Livre II, chapitre 9 ;
- les bases vectorielles restent à la fiche 15 ;
- la reprise après incident reste au Livre IV, chapitre 15 ;
- les diagnostics transversaux restent à la fiche 20 ;
- les benchmarks et mesures restent à la fiche 21 ;
- les compatibilités restent à la fiche 22 ;
- les licences et conformités restent à la fiche 25 ;
- les fichiers SQL, runners, bases et fixtures permanents restent au Companion Pack.

## 9. Métriques documentaires

| Mesure | Valeur |
|---|---:|
| lignes | 487 |
| titres | 18 |
| cartes | 13 |
| matrices | 3 |
| liens Markdown | 47 |
| liens vers Livres I à IV | 20 |
| liens profonds propriétaires | 19 |
| liens officiels | 8 |
| blocs clôturés | 3 |
| blocs SQL | 3 |
| fixtures SQLite | 36 |
| fixtures réussies | 36 |

## 10. Réserves

- aucun binaire Godot, projet, GDExtension ou addon chargé ;
- aucune qualification de Godot-SQLite ou d’un export natif ;
- aucune base utilisateur, de production ou du Companion Pack traitée ;
- aucune concurrence réelle multiprocessus ;
- aucune campagne de charge, fuzzing ou sécurité offensive ;
- aucune migration destructive sur données réelles ;
- aucun test de panne disque, coupure de processus ou corruption injectée ;
- aucun benchmark de taille ou de durée ;
- aucune approbation juridique organisationnelle ;
- aucun PDF produit.

## 11. Acceptation

La fiche est acceptée au niveau `static-review` lorsque le lot permanent, les liens, les cartes, les repères, les empreintes et les validateurs documentaires passent. Les 36 fixtures qualifient uniquement les comportements enregistrés du runtime SQLite `3.45.1` et du binding Python de la campagne. Un schéma, une migration ou un runner permanent ne devient `qualified` qu’après campagne sur les moteurs, bindings, plateformes et bases sources réellement distribués.
