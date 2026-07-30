# Intégration

## Python

Définir `PYTHONPATH` sur `python/src`, puis importer `asteria_database`. Le Pack ne requiert pas d’installation globale.

## Godot

Aucun addon natif n’est distribué. Une intégration Godot doit rester derrière un adaptateur du projet et reproduire les mêmes contrats :

- identité `application_id` ;
- version `user_version` ;
- historique des migrations et SHA-256 ;
- requêtes paramétrées ;
- clés étrangères activées par connexion ;
- transaction courte et rollback ;
- sauvegarde cohérente ;
- validation avant restauration.

Les migrations SQL peuvent être copiées dans `res://data/sql/migrations/` à condition que leur manifeste et leurs octets restent identiques. Une nouvelle empreinte exige une nouvelle migration, pas une réécriture.

## Export

Les fichiers `.sql` et `manifest.json` doivent être inclus explicitement lorsqu’un exporteur ne les reconnaît pas comme ressources. Aucun export n’a été exécuté par ce lot.

## Frontière Code Library

Le Pack 4 conserve les collections, validateurs génériques, services, repository mémoire, machine à états, interactions, conversions et aides de test. Le Pack 5 fournit uniquement les composants dépendant réellement de SQLite et du schéma livré.

## Frontière AI Library

Les files, retries, cache de fournisseur et politiques réseau restent au Pack 3. `derived_cache_entry` illustre seulement une table non autoritaire et recréable.
