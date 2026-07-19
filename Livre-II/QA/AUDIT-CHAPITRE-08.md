---
title: "Audit du Livre II — Chapitre 8"
id: "DOC-L2-QA-CH08"
status: "complete"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
audit-date: "2026-07-19"
audit-level: "static-review"
pdf-built: false
---

# Audit du Livre II — Chapitre 8

## 1. Objet

Le présent rapport audite :

> **[LECTURE] Fichier contrôlé — Ne pas saisir.**

```text
Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md
```

Le chapitre doit introduire une persistance relationnelle locale sans confondre SQLite avec les `Resource` de conception ni consommer le périmètre du système de sauvegarde du chapitre 9.

## 2. Décision

**Décision : accepté avec réserves au niveau `static-review`.**

Aucune non-conformité documentaire ou technique majeure n’est laissée ouverte dans le texte. Les réserves concernent l’installation et l’exécution réelles de la GDExtension, les migrations sur une base matérialisée, la restauration d’une copie et la qualification d’un export Windows.

Aucun PDF intermédiaire n’a été construit, conformément à la politique du Livre II.

La validation finale légère a réussi :

- `Validate Chapters Without PDF`, run `29684886165` ;
- `Validate Usage Contexts`, run `29684886159` ;
- 56 sources déclarées ;
- 55 identifiants uniques ;
- 8 chapitres du Livre II continus ;
- 0 erreur bloquante ;
- 0 incohérence sémantique ;
- 1 143 blocs sur 1 143 précédés d’un repère ;
- aucun titre, bloc significatif ou paragraphe long dupliqué dans le Livre II.

## 3. Correspondance avec le plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| rôle de SQLite | sections 4 et 5 | conforme |
| intégration Godot | sections 6 et 7 | conforme avec réserve runtime |
| schéma et types | sections 9 à 12 | conforme |
| clés, contraintes et index | sections 11 et 12 | conforme |
| requêtes paramétrées | section 15 | conforme |
| transactions | sections 16 et 26 | conforme |
| dépôt derrière contrat | sections 20 à 23 | conforme |
| migrations numérotées | sections 17, 18 et 29 | conforme |
| rollback et copie préalable | sections 18, 19 et 24 | conforme |
| diagnostic d’intégrité | sections 24, 27, 31 et 32 | conforme |
| modes Solo et Studio | sections 34 et 35 | conforme |
| frontière avec la sauvegarde | sections 3, 33.10 et 37 | conforme |

## 4. Vérification de l’intégration tierce

L’intégration de référence est Godot-SQLite `4.7`, distribuée par la Godot Asset Library sous licence MIT.

Les sources primaires relues confirment :

- la branche Godot 4.x ;
- la prise en charge annoncée de Windows ;
- les méthodes `open_db()`, `close_db()`, `query()` et `query_with_bindings()` ;
- les propriétés `path`, `foreign_keys`, `query_result` et `error_message` ;
- le traitement récursif de la queue `pzTail` après `sqlite3_prepare_v2`, qui permet plusieurs instructions dans une même chaîne SQL ;
- la liaison native des valeurs `null`, booléennes, entières, flottantes, textuelles et binaires.

L’entrée de l’Asset Library cible Godot 4.5. La compatibilité exacte avec Godot `4.7.1-stable` n’est donc pas revendiquée sans exécution.

## 5. Architecture auditée

La dépendance respecte les frontières du chapitre 4 :

> **[LECTURE] Sens des dépendances — Ne pas saisir.**

```text
service applicatif
    ↓
BeaconStateRepository
    ↓
SqliteBeaconStateRepository
    ↓
DatabaseConnection
    ↓
SqliteDatabaseConnection
    ↓
Godot-SQLite
```

Le domaine et les services applicatifs n’importent ni la classe `SQLite`, ni un chemin de fichier, ni une chaîne SQL.

L’adaptateur instancie la classe native par `ClassDB`, vérifie le journal WAL et les clés étrangères, et conserve séparément un code d’erreur et un message.

## 6. Schéma et migrations

Le schéma initial comprend :

- `beacon_state` comme état courant persistant ;
- `beacon_activation_event` comme historique un-à-plusieurs ;
- `schema_migrations` comme historique de schéma ;
- `PRAGMA user_version` comme version rapide.

Les migrations sont :

- ordonnées ;
- continues à partir de `1` ;
- append-only ;
- identifiées par version, nom et chemin ;
- vérifiées par SHA-256 ;
- exécutées sous `BEGIN IMMEDIATE` ;
- annulées par `ROLLBACK` en cas d’échec.

Une base dont la version est plus récente que l’application est refusée avant la création ou la modification de la table d’historique.

## 7. Copie préalable et intégrité

La copie préalable n’est créée que lorsqu’une migration est en attente.

Le cycle documenté est :

1. ouverture et récupération SQLite ;
2. lecture de `user_version` ;
3. checkpoint WAL ;
4. fermeture de toutes les connexions ;
5. copie du fichier principal ;
6. réouverture ;
7. migration ;
8. `quick_check` ;
9. `foreign_key_check`.

La restauration exige une base fermée et supprime les anciens fichiers `-wal` et `-shm` avant de remplacer le fichier principal.

## 8. Requêtes et erreurs

Les valeurs dynamiques utilisent des paramètres positionnels `?`.

Les noms de tables, colonnes et versions de `PRAGMA user_version` ne sont pas liés comme des valeurs ; ils proviennent uniquement de constantes ou du manifeste interne validé.

Le contrat distingue :

- `OK` avec zéro ligne ;
- `ERR_DOES_NOT_EXIST` produit par le dépôt après une lecture réussie ;
- une erreur SQL ;
- une cardinalité ou une ligne corrompue.

Cette distinction empêche une panne de stockage d’être masquée comme une absence métier normale.

## 9. Règle sémantique des erreurs et corrections

La section `Erreurs fréquentes et corrections` porte :

> **[LECTURE] Marqueur QA présent dans le chapitre — Ne pas saisir.**

```html
<!-- qa:error-correction-section -->
```

Elle comporte onze cas détaillés. Chaque cas contient :

- un symptôme ou risque ;
- un exemple fautif ;
- une correction ;
- un exemple corrigé ou une architecture corrigée ;
- une explication `Différence`.

Les cas couvrent `res://`, les bindings, les migrations historiques, les transactions, les clés étrangères, WAL, les index, les threads, les données de conception, la frontière des sauvegardes et les erreurs de lecture masquées.

## 10. Non-conformités corrigées pendant l’audit

1. **Résultat vide ambigu** — ajout de `last_error_code()` dans la connexion et le dépôt.
2. **Dépendance native statique** — instanciation isolée par `ClassDB` dans l’adaptateur.
3. **WAL supposé actif** — lecture et validation du mode réellement retourné.
4. **Clés étrangères supposées actives** — contrôle du `PRAGMA foreign_keys` égal à `1`.
5. **Schéma futur modifié avant refus** — lecture de version déplacée avant la table d’historique.
6. **Manifeste permissif** — versions continues, noms uniques et chemins obligatoires.
7. **Migration historique partiellement vérifiée** — contrôle du nom et du checksum.
8. **Copie à chaque lancement** — copie limitée aux migrations en attente.
9. **Copie WAL ouverte** — checkpoint et fermeture obligatoires.
10. **Restauration avec journaux anciens** — suppression des sidecars `-wal` et `-shm`.
11. **Événement insuffisamment validé** — identifiants et date contrôlés avant transaction.
12. **Source multi-instructions non démontrée** — implémentation native épinglée et relue.

## 11. Audit des repères

Les blocs utilisent :

- `[APP]` pour Godot et l’export ;
- `[PS]` pour les commandes PowerShell ;
- `[VSC]` pour les fichiers à créer ;
- `[LECTURE]` pour SQL, arborescences et exemples non exécutables ;
- `[SORTIE]` pour les résultats attendus.

Les exemples fautifs sont explicitement non exécutables.

## 12. Frontières préservées

Le chapitre 8 ne définit pas :

- les slots de sauvegarde ;
- les snapshots complets ;
- les miniatures et métadonnées de partie ;
- la migration d’un format de sauvegarde ;
- le chargement progressif du monde ;
- l’autosave et la rotation des slots.

Ces sujets restent réservés au chapitre 9.

## 13. Réserves runtime

Le niveau demeure `static-review` jusqu’à la conservation de preuves pour :

- l’installation de Godot-SQLite `4.7` ;
- le chargement de sa bibliothèque Windows x86_64 dans Godot 4.7.1 ;
- l’exécution des deux migrations ;
- la persistance entre deux lancements ;
- un rollback provoqué ;
- une divergence de checksum ;
- la création et la restauration d’une copie ;
- les contrôles d’intégrité ;
- un export Windows exécuté sur une machine propre.

## 14. Porte PDF

La compilation Pandoc/XeLaTeX et l’inspection visuelle sont différées jusqu’à la fin du Livre II.

> **[SORTIE] État de la porte PDF — Ne pas saisir.**

```text
PDF construit : non
Justification : politique de validation légère par chapitre
```

## 15. Conclusion

Le chapitre couvre le périmètre prévu, respecte l’architecture du projet, enseigne les garanties et limites de SQLite, protège les migrations et maintient une séparation nette avec le système de sauvegarde.

Les portes documentaires et statiques ont réussi. Il est déclaré **rédigé, repéré et audité au niveau `static-review`**, sous réserve des seuls tests runtime différés et du PDF de fin de Livre.
