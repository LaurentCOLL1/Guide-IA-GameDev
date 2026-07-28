---
title: "Livre V — Fiche 14 : Schémas SQLite et migrations"
id: "DOC-L5-CH14"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 14
last-verified: "2026-07-29T01:06:05+02:00"
audit-status: "complete"
audit-date: "2026-07-29T01:06:05+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-14.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "sqlite-schema-migration-reference"
reference-database:
  name: "SQLite"
  version: "3.53.4"
  release-date: "2026-07-24"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Schémas SQLite et migrations

> **Type de document :** cartes de schéma, matrices de décision, patrons DDL, migrations et requêtes de diagnostic.
> **Référence documentaire :** SQLite `3.53.4`, publié le 24 juillet 2026 ; intégration Godot conservée au chapitre propriétaire.
> **Repère :** **[LECTURE]** désigne un extrait minimal à étudier, pas une commande à lancer sur une base réelle sans adaptation et sauvegarde.
> **Principe :** une base ouvrable n’est ni un schéma compatible, ni une migration sûre, ni une sauvegarde restaurable, ni une preuve d’intégrité métier.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat d’une base | [SQL-00](#sql-00--contrat-dune-base) |
| choisir SQLite ou un autre support | [Matrice A](#matrice-a--sélection-par-besoin) |
| identifier version, fichier et capacités | [SQL-01](#sql-01--identité-version-et-capacités) |
| choisir affinité, type ou table `STRICT` | [SQL-02](#sql-02--types-affinités-et-strict) |
| convertir les types du projet | [Matrice B](#matrice-b--types-et-représentations) |
| choisir clés et identité de ligne | [SQL-03](#sql-03--clés-rowid-et-identité) |
| poser les contraintes du schéma | [SQL-04](#sql-04--contraintes-et-valeurs-dérivées) |
| définir les relations et suppressions | [SQL-05](#sql-05--clés-étrangères) |
| concevoir et diagnostiquer les index | [SQL-06](#sql-06--index-et-plan-de-requête) |
| configurer chaque connexion | [SQL-07](#sql-07--connexion-journal-et-pragmas) |
| choisir transaction ou savepoint | [SQL-08](#sql-08--transactions-verrous-et-savepoints) |
| consulter un DDL de référence | [SQL-09](#sql-09--ddl-de-référence) |
| versionner et appliquer les migrations | [SQL-10](#sql-10--manifestes-et-migrations) |
| choisir une stratégie de changement | [Matrice C](#matrice-c--stratégies-de-migration) |
| sauvegarder, restaurer et gérer WAL | [SQL-11](#sql-11--sauvegarde-restauration-et-wal) |
| contrôler sécurité et acceptation | [SQL-12](#sql-12--diagnostics-sécurité-et-acceptation) |

---

<!-- l5:card -->
## SQL-00 — Contrat d’une base

| Élément | Décision obligatoire |
|---|---|
| autorité | quelles données sont canoniques et lesquelles sont dérivées |
| identité | nom logique, chemin, `application_id` et propriétaire |
| moteur | bibliothèque SQLite exacte, options de compilation et adaptateur |
| modèle | tables, relations, cardinalités, nullabilité et invariants |
| types | affinités, tables ordinaires ou `STRICT`, conversions et unités |
| clés | identité métier, clé technique, `rowid` ou `WITHOUT ROWID` |
| contraintes | `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY` |
| index | requête propriétaire, ordre des colonnes, sélectivité et coût d’écriture |
| connexion | clés étrangères, journal, synchronisation, délai d’attente et sécurité |
| transactions | frontière atomique, mode `BEGIN`, savepoints et stratégie d’échec |
| version | `user_version`, manifeste, historique et checksums |
| migration | préconditions, SQL, backfill, validation, rollback ou restauration |
| sauvegarde | état fermé, Backup API, `VACUUM INTO`, rétention et test de restauration |
| diagnostic | intégrité, clés étrangères, schéma, plans et journaux |
| preuve | version SQLite, fixtures, commandes, résultats, artefacts et réserves |

**Réponse rapide :** SQLite fournit stockage, transactions et langage SQL ; le schéma définit les formes admissibles ; la couche applicative décide de la sémantique. Le [périmètre du chapitre propriétaire](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#3-périmètre-et-frontières) conserve l’intégration, les dépôts et le bootstrap. Le [système de sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) décide ce qui constitue une partie restaurable.

---

<!-- l5:matrix -->
## Matrice A — Sélection par besoin

| Besoin principal | Support de départ | Pourquoi | Source propriétaire | Limite |
|---|---|---|---|---|
| donnée éditable dans l’Inspector | Resource `.tres` | typage Godot et édition visuelle | [matrice des données](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#5-matrice-de-décision) | pas une base relationnelle |
| échange entre outils | JSON ou CSV validé | interopérabilité explicite | [matrice des formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-a--sélection-par-besoin) | chargement ou import à valider |
| configuration locale non secrète | `ConfigFile`, JSON ou Resource | valeurs bornées et lisibles | [configuration technique](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#42-configuration-technique) | aucun secret |
| état relationnel persistant | SQLite | contraintes, requêtes et transactions | [pourquoi SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#4-pourquoi-sqlite-convient-à-project-asteria) | schéma et migrations nécessaires |
| historique filtrable | SQLite avec index mesurés | relations et ordre | [modèle relationnel](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#9-modéliser-les-données-relationnelles) | rétention à définir |
| snapshot complet de partie | enveloppe de sauvegarde | cohérence métier et migrations de document | [choix du format](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#6-choisir-le-format-de-référence) | SQLite peut contribuer sans être le contrat complet |
| recherche vectorielle | base vectorielle ou index dérivé | similarité et filtres spécialisés | [frontière de la mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#3-périmètre-et-frontières) | appartient à la fiche 15 |
| cache régénérable | fichier ou base dédiée | suppression sans perte de source | [fichiers runtime](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-09--configurations-et-fichiers-runtime) | jamais promu comme autorité |

**Décision :** choisir SQLite pour un besoin relationnel et transactionnel, pas parce qu’un fichier unique semble pratique. Une même donnée ne doit pas devenir autoritaire dans plusieurs supports.

---

<!-- l5:card -->
## SQL-01 — Identité, version et capacités

| Notion | Rôle | Politique |
|---|---|---|
| version SQLite | fonctions et corrections du moteur réellement lié | enregistrer `sqlite_version()` au runtime |
| version documentaire | référence de la fiche | SQLite `3.53.4`, vérifiée le 29 juillet 2026 |
| version de l’adaptateur | API Godot ou Python utilisée | épingler et qualifier séparément |
| `PRAGMA user_version` | entier libre géré par l’application | refléter la dernière migration validée |
| `PRAGMA application_id` | identifiant entier dans l’en-tête | refuser une famille de base inattendue |
| `PRAGMA schema_version` | compteur interne géré par SQLite | lire pour diagnostic, ne pas utiliser comme version métier |
| `sqlite_schema` | définitions des tables, index, vues et triggers | inspecter, ne pas modifier dans le profil normal |
| options de compilation | fonctionnalités présentes ou absentes | conserver `PRAGMA compile_options` dans la preuve |
| extension chargée | fonctions ou virtual tables supplémentaires | allowlist, version et licence |
| fichier principal | pages de la base | ne pas oublier journal ou WAL selon l’état |

La page officielle des [versions SQLite](https://sqlite.org/chronology.html) identifie `3.53.4` comme version publiée le 24 juillet 2026. La fiche ne suppose pas que Godot-SQLite, Python ou un autre binding embarque cette même version. Le [chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#64-réserve-de-compatibilité) conserve la qualification de l’addon et de Godot `4.7.1-stable`.

**Piège :** `user_version` appartient à l’application ; `schema_version` appartient au mécanisme interne de cache du schéma. Les intervertir peut provoquer des décisions de migration incorrectes.

---

<!-- l5:card -->
## SQL-02 — Types, affinités et `STRICT`

| Concept | Tables ordinaires | Tables `STRICT` |
|---|---|---|
| typage | type attaché principalement à la valeur | type de colonne contrôlé à l’insertion |
| noms de types | affinité dérivée d’un nom déclaré | seulement `INT`, `INTEGER`, `REAL`, `TEXT`, `BLOB`, `ANY` |
| conversion | conversion selon affinité lorsque possible | conversion sans perte ou erreur de contrainte |
| `ANY` | peut convertir un texte numérique | préserve valeur et type exacts |
| clé primaire | nuances historiques selon déclaration | colonnes de clé implicitement non nulles, avec cas spécial `INTEGER PRIMARY KEY` |
| intégrité | structure et contraintes | `quick_check` et `integrity_check` vérifient aussi les types |
| compatibilité | très large | nécessite SQLite `3.37.0` ou plus récent |

Les [types SQLite](https://sqlite.org/datatype3.html) sont dynamiques. Les [tables `STRICT`](https://sqlite.org/stricttables.html) ajoutent une discipline par table sans modifier le format de pages. Elles ne remplacent ni `CHECK`, ni clés étrangères, ni validation métier.

**Décision du guide :** préférer `STRICT` pour les nouvelles tables contrôlées lorsque la version minimale du moteur est qualifiée. Conserver une table ordinaire lorsqu’une compatibilité plus ancienne, un type déclaré spécifique ou un import tolérant le justifie explicitement.

---

<!-- l5:matrix -->
## Matrice B — Types et représentations

| Valeur logique | SQLite | Contraintes ou codec | Réserve |
|---|---|---|---|
| booléen | `INTEGER` | `CHECK (value IN (0,1))` | ne pas accepter tout entier non nul comme contrat persistant |
| entier | `INTEGER` | bornes métier | signé 64 bits dans le moteur |
| montant exact | `INTEGER` | nombre de centimes, devise séparée | pas de `REAL` pour une arithmétique exacte |
| décimal mesuré | `REAL` | unité, plage et tolérance | flottant binaire |
| texte | `TEXT` | longueur, normalisation et syntaxe | collation à déclarer si l’ordre importe |
| identifiant stable | `TEXT` | `PRIMARY KEY`, `UNIQUE` ou `CHECK` | ne pas utiliser le nom affiché |
| date-heure | `TEXT` ou `INTEGER` | profil UTC/RFC 3339 ou epoch documenté | fuseau et précision obligatoires |
| durée | `INTEGER` ou `REAL` | unité dans le nom ou le contrat | horloge civile distincte du temps monotone |
| octets | `BLOB` | taille et média | aucun sens sans codec |
| JSON | `TEXT` ou `BLOB` | `json_valid()` si JSON1 qualifié, puis schéma métier | la fonction JSON n’impose pas le contrat applicatif |
| enum | `TEXT` stable ou entier fermé | `CHECK` ou table de référence | éviter un ordinal susceptible de changer |
| référence | type identique à la clé parent | `FOREIGN KEY` et index enfant | activation par connexion |
| liste | table enfant | clé étrangère et position si ordre | éviter CSV ou JSON caché sans justification |
| vecteur | colonnes explicites ou BLOB spécialisé | axes, unité et codec | mesurer avant dénormalisation |

Le tableau reprend les [correspondances du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#10-types-sqlite-et-types-godot) et les [pertes de conversion de la fiche 13](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-c--correspondances-et-pertes). Le type de stockage ne porte pas à lui seul l’unité, la sémantique ou la précision.

---

<!-- l5:card -->
## SQL-03 — Clés, `rowid` et identité

| Forme | Usage | Réserve |
|---|---|---|
| `INTEGER PRIMARY KEY` | clé technique locale compacte | alias du `rowid`, sauf nuances des tables `WITHOUT ROWID` |
| `AUTOINCREMENT` | interdit toute réutilisation de valeur déjà émise | coût supplémentaire ; rarement nécessaire |
| clé métier `TEXT` | identité stable partagée avec le domaine | longueur et syntaxe contrôlées |
| clé composée | identité naturellement multi-colonnes | propagation dans les tables enfants |
| `UNIQUE` | identité alternative | politique de `NULL` à comprendre |
| `WITHOUT ROWID` | table dominée par une clé primaire non entière ou composée | mesurer taille et accès ; API `rowid` indisponible |
| clé opaque externe | synchronisation ou import | provenance et collision |
| chemin de fichier | localisation | ne doit pas devenir identité métier |

La déclaration exacte `INTEGER PRIMARY KEY` possède une sémantique spéciale ; `INT PRIMARY KEY` n’est pas équivalent. L’[exemple d’événement du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#121-integer-primary-key) évite `AUTOINCREMENT` parce que la non-réutilisation absolue n’est pas un invariant requis.

**Règle :** une clé technique identifie une ligne ; un identifiant métier identifie une entité au-delà du fichier. Ne jamais recycler un identifiant métier pour une autre signification.

---

<!-- l5:card -->
## SQL-04 — Contraintes et valeurs dérivées

| Élément | Protège | Ne protège pas |
|---|---|---|
| `NOT NULL` | présence d’une valeur | chaîne vide ou valeur sentinelle |
| `CHECK` | invariant local déterministe | relation vers une autre table |
| `UNIQUE` | unicité d’une ou plusieurs expressions de colonne | normalisation métier non définie |
| `PRIMARY KEY` | identité principale | validité sémantique de la clé |
| `DEFAULT` | valeur lors d’une insertion qui omet la colonne | anciennes lignes ou `NULL` fourni explicitement |
| colonne générée | valeur dérivée dans la ligne | logique avec effets ou non déterministe |
| `COLLATE` | comparaison et ordre de texte | traduction ou recherche linguistique complète |
| trigger | réaction SQL à une mutation | gouvernance implicite ou code métier caché |
| `ON CONFLICT` | stratégie locale de violation | idempotence métier générale |

Les contraintes simples doivent vivre au plus près des données, puis être doublées par la validation applicative lorsque le diagnostic ou le contexte métier l’exige. L’[exemple `CHECK` du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#113-check) illustre cette double frontière.

**Profil du guide :** limiter les triggers aux invariants véritablement relationnels et documentés. Une mise à jour métier importante ne doit pas être cachée dans un trigger inconnu de la couche applicative.

---

<!-- l5:card -->
## SQL-05 — Clés étrangères

| Décision | Choix possibles | Contrôle |
|---|---|---|
| activation | `PRAGMA foreign_keys = ON` pour chaque connexion | relire la valeur après ouverture |
| parent | `PRIMARY KEY` ou `UNIQUE` déclaré dans la table | collation compatible |
| enfant | type et colonnes correspondants | index généralement nécessaire |
| temporalité | immédiate ou `DEFERRABLE INITIALLY DEFERRED` | violation différée contrôlée au `COMMIT` |
| suppression | `RESTRICT`, `NO ACTION`, `CASCADE`, `SET NULL`, `SET DEFAULT` | conséquence métier explicite |
| mise à jour | mêmes actions | éviter de modifier les identités stables |
| contrôle | `PRAGMA foreign_key_check` | aucune ligne attendue |
| migration | relation préservée pendant reconstruction | check avant commit |

SQLite ne garantit pas que les clés étrangères sont actives par défaut ; l’application doit les activer explicitement hors transaction et ne jamais dépendre d’un réglage de compilation. La documentation officielle des [clés étrangères](https://sqlite.org/foreignkeys.html) distingue contraintes immédiates et différées. Le chapitre propriétaire applique cette politique [par connexion](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#141-foreign_keys-avant-louverture).

**Piège :** `integrity_check` ne remplace pas `foreign_key_check`. Les deux portes répondent à des catégories d’erreurs différentes.

---

<!-- l5:card -->
## SQL-06 — Index et plan de requête

| Index | Usage | Réserve |
|---|---|---|
| clé primaire ou unique | identité et recherche exacte | peut déjà créer une structure interne |
| simple | filtre ou tri sur une colonne | sélectivité faible parfois inutile |
| composite | préfixe commun de filtres et d’ordres | ordre des colonnes décisif |
| partiel | sous-ensemble défini par `WHERE` | prédicat stable et déterministe |
| d’expression | calcul déterministe fréquemment filtré | expression identique dans la requête |
| couvrant | fournit toutes les colonnes nécessaires | coût de stockage et d’écriture |
| index enfant de clé étrangère | accélère contrôles et cascades | à créer explicitement dans de nombreux cas |

| Question | Outil |
|---|---|
| l’index est-il considéré ? | `EXPLAIN QUERY PLAN` |
| quels index existent ? | `PRAGMA index_list(table)` |
| quelles colonnes ou expressions ? | `PRAGMA index_xinfo(index)` |
| quelles statistiques ? | `sqlite_stat1` après analyse qualifiée |
| l’index sert-il les requêtes réelles ? | tests avec volume représentatif et plans conservés |

L’[index composite du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#123-index-composite) place l’identifiant de balise avant la date parce que la requête propriétaire filtre d’abord par balise. Un index n’est pas « bon » isolément : il répond à une requête, un volume et une distribution mesurés.

**Règle :** ne jamais ajouter un index seulement pour faire disparaître un scan observé sur une fixture minuscule. Mesurer lectures, écritures, taille et plans sur un corpus représentatif ; les campagnes générales appartiennent à la fiche 21.

---

<!-- l5:card -->
## SQL-07 — Connexion, journal et pragmas

| Réglage | Portée | Profil de départ | Validation |
|---|---|---|---|
| `foreign_keys` | connexion | `ON` | relire `1` |
| `trusted_schema` | connexion | `OFF` lorsque compatible | requêtes de démarrage et fonctions qualifiées |
| `busy_timeout` | connexion | durée bornée | exercer conflit et expiration |
| `journal_mode` | fichier | `WAL` seulement après qualification | relire le mode retourné |
| `synchronous` | connexion | `FULL` dans le chapitre propriétaire | mesurer avant réduction |
| `query_only` | connexion | `ON` pour un lecteur dédié | vérifier qu’aucune écriture n’est requise |
| `application_id` | fichier | identifiant non nul du projet | vérifier avant migration |
| `user_version` | fichier | dernière migration appliquée | comparer au manifeste |
| `max_page_count` | fichier | borne selon politique | erreur `SQLITE_FULL` qualifiée |
| `mmap_size` | connexion/fichier | `0` pour une base non fiable | politique de sécurité |
| `temp_store` | connexion | choix explicite si nécessaire | volume et confidentialité |

Le mode WAL permet généralement lecteurs et écrivain simultanés, mais la documentation officielle avertit que [des opérations peuvent encore retourner `SQLITE_BUSY`](https://sqlite.org/wal.html#sometimes_queries_return_sqlite_busy_in_wal_mode). Le [chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#143-mode-wal) exige de relire le mode réellement obtenu et conserve `synchronous = FULL` comme défaut prudent.

**Frontière :** un pragma n’est pas une constante universelle. Sa portée peut être la connexion, le fichier ou la compilation ; chaque connexion est configurée et contrôlée avant usage.

---

<!-- l5:card -->
## SQL-08 — Transactions, verrous et savepoints

| Forme | Moment du verrou d’écriture | Usage |
|---|---|---|
| transaction implicite | autour d’une instruction | opération isolée sans composition applicative |
| `BEGIN DEFERRED` | au premier accès nécessitant le verrou | valeur par défaut, conflit possible plus tard |
| `BEGIN IMMEDIATE` | dès le début pour l’écriture | migration ou unité qui doit échouer tôt |
| `BEGIN EXCLUSIVE` | verrou plus fort selon journal | cas spécialisé, rarement nécessaire en WAL |
| `SAVEPOINT name` | dans ou hors transaction | sous-unité réversible |
| `ROLLBACK TO name` | conserve le savepoint | annule une partie |
| `RELEASE name` | fusionne la sous-unité | peut déclencher le contrôle d’un savepoint transactionnel |
| `COMMIT` | publie l’unité | peut échouer, notamment avec contrainte différée |
| `ROLLBACK` | annule l’unité | doit rester possible après erreur |

Une transaction protège l’atomicité des instructions SQL de la connexion ; elle ne rend pas atomiques des fichiers externes, appels réseau ou effets Godot. La [transaction explicite du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#16-transaction-explicite) utilise `BEGIN IMMEDIATE` afin de détecter tôt un écrivain concurrent.

**Patron :** valider les entrées avant `BEGIN`, garder la transaction courte, vérifier chaque code, tenter `ROLLBACK` après échec et enregistrer séparément l’échec du rollback. Ne jamais faire attendre une interface, un modèle IA ou un service réseau dans une transaction ouverte.

---

<!-- l5:card -->
## SQL-09 — DDL de référence

| Objet | Autorité | Décision |
|---|---|---|
| `schema_migrations` | runner | version, nom, checksum et date d’application |
| `beacon_state` | état persistant courant | clé métier stable et invariants simples |
| `beacon_activation_event` | historique dépendant | clé technique, parent et date |
| index composite | requête d’historique | balise puis date |

> **[LECTURE] DDL minimal compatible avec une base de test SQLite moderne.**

```sql
CREATE TABLE schema_migrations (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    checksum TEXT NOT NULL CHECK (length(checksum) = 64),
    applied_at_utc TEXT NOT NULL
) STRICT;

CREATE TABLE beacon_state (
    beacon_id TEXT PRIMARY KEY,
    is_enabled INTEGER NOT NULL DEFAULT 1
        CHECK (is_enabled IN (0, 1)),
    activation_count INTEGER NOT NULL DEFAULT 0
        CHECK (activation_count >= 0),
    updated_at_utc TEXT NOT NULL
) STRICT;

CREATE TABLE beacon_activation_event (
    event_id INTEGER PRIMARY KEY,
    beacon_id TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    occurred_at_utc TEXT NOT NULL,
    FOREIGN KEY (beacon_id)
        REFERENCES beacon_state(beacon_id)
        ON DELETE CASCADE
) STRICT;

CREATE INDEX idx_beacon_event_beacon_time
    ON beacon_activation_event(beacon_id, occurred_at_utc);
```

**Entrées :** moteur SQLite `3.37.0+`, clés étrangères activées et conventions d’identifiants du projet. **Sortie :** trois tables et un index. **Effets :** modification du schéma courant. **Réserve :** ce DDL ne remplace pas les migrations versionnées du Companion Pack et ne doit pas être appliqué à une base existante sans inspection.

La forme reprend les [deux premières migrations pédagogiques](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#11-première-migration-sql) sans recopier les couches Godot, dépôts et scènes.

---

<!-- l5:card -->
## SQL-10 — Manifestes et migrations

| Champ | Contrat |
|---|---|
| version | entier strictement croissant et jamais réutilisé |
| nom | verbe et objet stables |
| chemin | fichier SQL versionné sous une racine contrôlée |
| checksum | SHA-256 des octets normalisés définis par le projet |
| version minimale | moteur et capacités requises |
| préconditions | version installée, tables, colonnes et absence d’anomalie |
| transaction | mode, durée et comportement sur `SQLITE_BUSY` |
| backfill | ordre, lots, valeurs par défaut et reprise |
| postconditions | schéma, compteurs, contraintes et plans essentiels |
| preuve | base source, copie préalable, commandes, codes et artefacts |
| retrait | restauration ou migration corrective, jamais réécriture silencieuse |

> **[LECTURE] Squelette d’application d’une migration unique.**

```sql
BEGIN IMMEDIATE;

-- DDL ou transformation de données de la version 2.

INSERT INTO schema_migrations(
    version, name, checksum, applied_at_utc
) VALUES (
    2, 'add_beacon_activation_event', :checksum, :applied_at_utc
);

PRAGMA user_version = 2;
COMMIT;
```

**Paramètres :** `:checksum` et `:applied_at_utc` sont liés par l’adaptateur ; ils ne proviennent pas d’une concaténation. **Retour :** succès seulement si DDL, historique, `user_version` et `COMMIT` réussissent. **Échec :** `ROLLBACK`, base non promue et diagnostic conservé.

Le [runner du chapitre 8](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#18-runner-de-migrations) combine `user_version` et table d’historique, vérifie les checksums déjà appliqués et refuse une base future. Une migration publiée est immuable ; sa correction prend une nouvelle version.

---

<!-- l5:matrix -->
## Matrice C — Stratégies de migration

| Changement | Stratégie de départ | Validation décisive | Réserve |
|---|---|---|---|
| renommer une table | `ALTER TABLE ... RENAME TO` | schéma, vues, triggers et clés étrangères | `legacy_alter_table` modifie le comportement |
| renommer une colonne | `ALTER TABLE ... RENAME COLUMN` | références et SQL préparé | ambiguïtés provoquent un refus |
| ajouter une colonne simple | `ALTER TABLE ... ADD COLUMN` | défaut, nullabilité et anciennes lignes | restrictions sur contraintes et références |
| supprimer une colonne admissible | `ALTER TABLE ... DROP COLUMN` | dépendances du schéma | indisponible si la colonne est encore référencée |
| modifier type, clé ou contrainte | reconstruction contrôlée de table | copie, compteurs, `foreign_key_check`, intégrité | suivre la procédure officielle complète |
| ajouter ou retirer un index | `CREATE INDEX` / `DROP INDEX` | plans de requête et coût d’écriture | aucune amélioration supposée |
| backfill borné | mises à jour par lots dans une migration | compteurs, reprise et temps | ne pas ouvrir une transaction interminable |
| scinder une table | nouvelles tables, copie, validation, bascule | cardinalités et références |
| fusionner des colonnes | nouvelle colonne puis backfill | pertes et normalisation |
| réécrire `sqlite_schema` | exclu du profil normal | base jetable seulement | risque direct de corruption |
| migration destructive | copie préalable et porte explicite | restauration réellement exercée | aucune suppression silencieuse |
| base future | lecture de l’identité et de `user_version`, puis refus | aucune écriture | ne jamais rétrograder automatiquement |

La documentation officielle d’[`ALTER TABLE`](https://sqlite.org/lang_altertable.html) réserve la reconstruction en plusieurs étapes aux changements structurels complexes et recommande test séparé et sauvegarde. Le profil du guide n’utilise pas `PRAGMA writable_schema` sur une base de production.

---

<!-- l5:card -->
## SQL-11 — Sauvegarde, restauration et WAL

| Méthode | Base ouverte | Résultat | Usage |
|---|---|---|---|
| copie de fichier fermé | non | copie du fichier principal cohérent | parcours simple après fermeture et checkpoint |
| Online Backup API | oui | snapshot vers une autre base | copie progressive contrôlée |
| `VACUUM INTO` | oui | copie compactée dans un nouveau fichier | export ou sauvegarde bornée |
| commande CLI `.backup` | oui via shell | utilise les mécanismes SQLite | opération d’administration qualifiée |
| copie brute du seul fichier en WAL | oui | potentiellement incomplète | interdite |
| archive de base fermée | non | conteneur de transport | empreinte, rétention et restauration nécessaires |

Le [service pédagogique de copie préalable](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md#24-bootstrap-de-la-base) effectue un checkpoint, ferme la connexion, crée une copie, rouvre puis migre. L’[Online Backup API officielle](https://sqlite.org/backup.html) et `VACUUM INTO` offrent des stratégies pour une base active lorsque le binding les expose correctement.

| Porte de restauration | Attendu |
|---|---|
| identité | `application_id` reconnu |
| version | `user_version` supportée |
| ouverture | aucune création implicite de base vide à la place de la source |
| intégrité | `quick_check` ou `integrity_check` égal à `ok` |
| relations | `foreign_key_check` sans ligne |
| migrations | checksums historiques concordants |
| données | compteurs et invariants critiques vérifiés |
| bascule | destination remplacée seulement après validation |
| preuve | copie restaurée dans un workspace isolé |

**Règle :** une sauvegarde non restaurée pendant un test n’est qu’un fichier supposé utile. Le plan de reprise complet, la rétention et les incidents appartiennent au [Livre IV, chapitre 15](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md).

---

<!-- l5:card -->
## SQL-12 — Diagnostics, sécurité et acceptation

| Symptôme ou porte | Requête ou contrôle | Résultat attendu |
|---|---|---|
| identité inconnue | `PRAGMA application_id` | valeur du projet |
| version future | `PRAGMA user_version` | valeur inférieure ou égale au manifeste |
| corruption rapide | `PRAGMA quick_check` | une ligne `ok` |
| contrôle complet | `PRAGMA integrity_check` | une ligne `ok` |
| relations | `PRAGMA foreign_key_check` | aucune ligne |
| schéma réel | `PRAGMA table_list`, `table_xinfo`, `index_list`, `index_xinfo` | objets attendus |
| migration divergente | table `schema_migrations` + SHA-256 | nom et checksum concordants |
| requête lente | `EXPLAIN QUERY PLAN` | plan conservé et interprété |
| verrou | code `SQLITE_BUSY` / `SQLITE_LOCKED` | politique bornée, pas boucle infinie |
| disque plein | `SQLITE_FULL`, quota et `max_page_count` | échec explicite sans succès partiel |
| base non fiable | limites, `trusted_schema=OFF`, fonctions et extensions bornées | aucune capacité implicite |
| SQL dynamique | paramètres pour valeurs, allowlist pour identifiants | aucune concaténation non fiable |

> **[LECTURE] Requêtes minimales de contrôle après migration.**

```sql
PRAGMA application_id;
PRAGMA user_version;
PRAGMA quick_check;
PRAGMA foreign_key_check;
PRAGMA table_list;
PRAGMA index_list('beacon_activation_event');
EXPLAIN QUERY PLAN
SELECT event_id, occurred_at_utc
FROM beacon_activation_event
WHERE beacon_id = ?
ORDER BY occurred_at_utc;
```

**Entrée :** base migrée dans un workspace contrôlé. **Sortie :** identité, version, intégrité, relations, inventaire et plan. **Limite :** un plan de requête dépend de la version SQLite, des statistiques et des données ; il n’est pas une promesse de performance.

La page officielle [Defense Against The Dark Arts](https://sqlite.org/security.html) recommande des limites réduites, le mode défensif et `trusted_schema=OFF` pour les bases ou SQL non fiables. Ces protections complètent, sans remplacer, provenance, permissions de fichier, sandbox, sauvegardes et mise à jour du moteur.

| Porte | État de cette fiche |
|---|---|
| exactitude documentaire SQLite `3.53.4` | revue officielle |
| DDL et migrations de test | campagne temporaire prévue |
| tables ordinaires et `STRICT` | fixtures temporaires prévues |
| clés étrangères et cascades | fixtures temporaires prévues |
| transactions et savepoints | fixtures temporaires prévues |
| index et plans | fixtures temporaires prévues |
| backup et restauration | base temporaire prévue |
| migration depuis données de production | non exécutée |
| Godot-SQLite et export natif | non exécutés |
| concurrence réelle multi-processus | non exécutée |
| charge, fuzzing et sécurité offensive | non exécutés |
| PDF | non produit |

**Acceptation documentaire :** la fiche reste `static-review`. Les bases SQLite temporaires peuvent qualifier les patrons SQL dans la version runtime enregistrée, mais ne qualifient ni l’addon Godot, ni un export, ni une base de production. Un schéma ou runner permanent devient `qualified` seulement après campagne conservant moteur, options, migrations, bases sources, sauvegardes, résultats, artefacts et réserves.
