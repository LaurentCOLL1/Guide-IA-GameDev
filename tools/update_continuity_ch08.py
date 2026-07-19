#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "CONTINUITE-PROJET.md"
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    if text.count(old) != 1:
        raise SystemExit(f"Expected one target, found {text.count(old)}: {old[:100]!r}")
    text = text.replace(old, new, 1)


replace_once('version: "3.7.0"', 'version: "3.8.0"')
replace_once('**En cours : 7 chapitres sur 30.**', '**En cours : 8 chapitres sur 30.**')
replace_once(
    '7. Données avec Resources, JSON et configurations — terminé au niveau `static-review`.\n8. SQLite, migrations et données persistantes — prochain chapitre.\n9. Sauvegardes, chargements et compatibilité des versions.\n',
    '7. Données avec Resources, JSON et configurations — terminé au niveau `static-review`.\n8. SQLite, migrations et données persistantes — terminé au niveau `static-review`.\n9. Sauvegardes, chargements et compatibilité des versions — prochain chapitre.\n',
)
replace_once('Chapitres 3 à 7 : **Élevée**.', 'Chapitres 3 à 8 : **Élevée**.')
replace_once(
    '- SQLite réservé au chapitre 8 et sauvegardes au chapitre 9.\n',
    '- base SQLite mutable sous `user://` ;\n- Godot-SQLite encapsulé derrière `DatabaseConnection` ;\n- requêtes paramétrées obligatoires pour toute valeur dynamique ;\n- clés étrangères, WAL, timeout et synchronisation vérifiés par connexion ;\n- migrations numérotées, append-only, transactionnelles et vérifiées par checksum ;\n- copie fermée créée uniquement avant une migration réellement en attente ;\n- schéma futur refusé avant toute mutation ;\n- `quick_check` et `foreign_key_check` exécutés après migration ;\n- absence de ligne distinguée d’une panne SQL ;\n- format de sauvegarde complet réservé au chapitre 9.\n',
)

chapter8 = '''## 15. Chapitre 8 — état détaillé

Fichier : `Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Intégration de référence : Godot-SQLite `4.7`, licence MIT, distribuée par la Godot Asset Library et encapsulée derrière une abstraction du projet.

Décisions enregistrées :

- base principale sous `user://data/asteria.sqlite3` ;
- aucune dépendance SQLite dans le domaine ou les services applicatifs ;
- `DatabaseConnection` et `BeaconStateRepository` comme contrats ;
- schéma initial `beacon_state` et `beacon_activation_event` ;
- clés étrangères activées et vérifiées sur chaque connexion ;
- requêtes paramétrées pour toutes les valeurs dynamiques ;
- transactions `BEGIN IMMEDIATE`, `COMMIT` et `ROLLBACK` ;
- manifeste de migrations continu à partir de `1` ;
- table `schema_migrations`, `PRAGMA user_version` et SHA-256 ;
- refus d’un schéma futur avant toute écriture ;
- copie préalable seulement lorsqu’une migration est en attente ;
- checkpoint WAL, fermeture et suppression des sidecars avant restauration ;
- `quick_check` et `foreign_key_check` après migration ;
- erreurs de requête distinctes des recherches sans résultat ;
- fichiers `*.sql` explicitement inclus dans l’export ;
- sauvegardes complètes, slots et snapshots réservés au chapitre 9.

Livrables documentés :

- `src/core/persistence/database_connection.gd` ;
- `src/core/persistence/sqlite_database_connection.gd` ;
- `src/core/persistence/database_backup_service.gd` ;
- `src/core/persistence/sql_migration_runner.gd` ;
- `src/features/beacons/application/beacon_state_record.gd` ;
- `src/features/beacons/application/beacon_state_repository.gd` ;
- `src/features/beacons/application/beacon_persistence_service.gd` ;
- `src/features/beacons/infrastructure/sqlite_beacon_state_repository.gd` ;
- `src/app/database_bootstrap.gd` ;
- `data/sql/migrations/001_create_beacon_state.sql` ;
- `data/sql/migrations/002_add_beacon_activation_event.sql` ;
- `scenes/learning/ch08_sqlite_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-08.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-08.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

'''
replace_once('## 15. Erreurs à ne pas reproduire\n', chapter8 + '## 16. Erreurs à ne pas reproduire\n')
replace_once('## 16. État courant\n', '## 17. État courant\n')
replace_once('## 17. Prochaine action\n', '## 18. Prochaine action\n')
replace_once('## 18. Journal\n', '## 19. Journal\n')

replace_once(
    '- ne pas introduire SQLite avant le chapitre 8 ;\n- ne pas utiliser les `.tres` comme sauvegarde du joueur ;\n',
    '- ne pas écrire une base mutable dans `res://` ;\n- ne pas concaténer une valeur dynamique dans SQL ;\n- ne pas modifier une migration déjà appliquée ;\n- ne pas démarrer le gameplay après une migration incomplète ;\n- ne pas copier une base WAL encore ouverte ;\n- ne pas masquer une panne SQL comme une absence de ligne ;\n- ne pas traiter le fichier SQLite comme un slot de sauvegarde complet ;\n- ne pas utiliser les `.tres` comme sauvegarde du joueur ;\n',
)
replace_once('- progression : 7 chapitres sur 30 ;', '- progression : 8 chapitres sur 30 ;')
replace_once(
    '- chapitre 7 : version `1.1.1` ;\n',
    '- chapitre 7 : version `1.1.1` ;\n- chapitre 8 : version `1.0.0` ;\n',
)

start = text.index('## 18. Prochaine action\n')
end = text.index('## 19. Journal\n', start)
next_action = '''## 18. Prochaine action

Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md
```

Périmètre attendu :

- rôle d’une sauvegarde par rapport aux dépôts SQLite ;
- définition d’un snapshot cohérent de partie ;
- slots manuels, autosaves et quicksaves ;
- métadonnées, miniatures et temps de jeu ;
- format de sauvegarde versionné ;
- écriture atomique par fichier temporaire et remplacement ;
- validation avant application au monde ;
- chargement en plusieurs phases ;
- compatibilité ascendante et migrations de sauvegarde ;
- gestion des sauvegardes futures ou corrompues ;
- rotation, rétention et copies de secours ;
- séparation entre données de conception, base persistante et snapshot ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.

'''
text = text[:start] + next_action + text[end:]

journal_entry = '''## 19. Journal

### 2026-07-19 — version 3.8.0

- création et audit statique du chapitre 8 ;
- choix de Godot-SQLite `4.7` sous licence MIT avec réserve Godot 4.7.1 ;
- ajout des contrats de connexion et de dépôt ;
- schéma relationnel des états et événements de balise ;
- requêtes paramétrées et transactions explicites ;
- migrations numérotées, checksums et refus des schémas futurs ;
- backup fermé seulement avant migration et restauration sans sidecars WAL ;
- contrôles `quick_check` et `foreign_key_check` ;
- progression à 8 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 9 ;
- PDF non construit.

'''
replace_once('## 19. Journal\n\n', journal_entry)

path.write_text(text, encoding="utf-8")
print("Chapter 8 continuity update applied.")
