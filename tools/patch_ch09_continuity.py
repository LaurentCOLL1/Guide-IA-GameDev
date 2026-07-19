from pathlib import Path

path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")

replacements = [
    ('version: "3.8.0"', 'version: "3.9.0"'),
    ('**En cours : 8 chapitres sur 30.**', '**En cours : 9 chapitres sur 30.**'),
    ('9. Sauvegardes, chargements et compatibilité des versions — prochain chapitre.', '9. Sauvegardes, chargements et compatibilité des versions — terminé au niveau `static-review`.'),
    ('Chapitres 3 à 8 : **Élevée**.', 'Chapitres 3 à 9 : **Élevée**.'),
    ('- format de sauvegarde complet réservé au chapitre 9.', '''- snapshot de partie distinct des dépôts SQLite ;
- format JSON versionné sous `user://saves/` ;
- empreinte canonique du payload avec précision numérique contrôlée ;
- slots validés, fichier temporaire, copie `.bak` et remplacement contrôlé ;
- sauvegarde future refusée et protégée contre l’écrasement ;
- migrations de sauvegarde linéaires et append-only ;
- validation complète avant application au monde ;
- verrou de chargement maintenu jusqu’à application ou annulation ;
- mémoire vectorielle réservée au chapitre 10.'''),
    ('## 16. Erreurs à ne pas reproduire', '## 17. Erreurs à ne pas reproduire'),
    ('## 17. État courant', '## 18. État courant'),
    ('- progression : 8 chapitres sur 30 ;', '- progression : 9 chapitres sur 30 ;'),
    ('- chapitre 8 : version `1.0.0` ;', '- chapitre 8 : version `1.0.0` ;\n- chapitre 9 : version `1.0.0` ;'),
    ('## 18. Prochaine action', '## 19. Prochaine action'),
    ('Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md', 'Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md'),
    ('''- rôle d’une sauvegarde par rapport aux dépôts SQLite ;
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
- audit statique sans PDF intermédiaire.''', '''- rôle de la mémoire vectorielle dans `Project Asteria` ;
- embeddings locaux et choix d’un modèle compatible avec la plateforme AMD ;
- découpage des documents et taille des segments ;
- métadonnées, identifiants stables et provenance ;
- création et mise à jour d’un index vectoriel ;
- recherche par similarité et filtres ;
- séparation entre connaissance source, index dérivé et sauvegarde ;
- gestion des suppressions et réindexations ;
- évaluation de la qualité de récupération ;
- confidentialité et fonctionnement local ;
- chemin déterministe lorsque le service vectoriel est indisponible ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.'''),
    ('## 19. Journal', '## 20. Journal'),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"Continuity replacement not found: {old[:160]}")
    text = text.replace(old, new, 1)

chapter9_section = '''## 16. Chapitre 9 — état détaillé

Fichier : `Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- sauvegarde définie comme snapshot logique, distinct de SQLite ;
- document JSON `project-asteria-save`, version courante `2` ;
- slots `manual`, `auto` et `quick` avec identifiants validés ;
- métadonnées d’affichage séparées du payload d’autorité ;
- types Godot convertis explicitement ;
- représentation canonique et SHA-256 du payload ;
- entiers JSON exacts limités à 53 bits ;
- taille de fichier limitée avant parsing ;
- écriture dans `.tmp`, relecture et validation avant remplacement ;
- copie `.bak` uniquement depuis un principal valide ;
- sauvegarde future refusée et jamais écrasée par un ancien build ;
- principal corrompu incapable de remplacer une bonne copie de secours ;
- migrations `N` vers `N + 1` appliquées sur une copie en mémoire ;
- validation du format courant et de toutes les sections avant application ;
- section inconnue refusée en mode strict ;
- identité du slot comparée au fichier demandé ;
- verrou conservé jusqu’à `finish_apply()` ou `cancel_load()` ;
- restauration multi-repositories encore réservée à un lot transactionnel runtime ;
- mémoire vectorielle réservée au chapitre 10.

Livrables documentés :

- `src/core/save/save_slot_id.gd` ;
- `src/core/save/save_value_codec.gd` ;
- `src/core/save/canonical_json.gd` ;
- `src/core/save/save_integrity.gd` ;
- `src/core/save/save_section.gd` ;
- `src/core/save/save_document_builder.gd` ;
- `src/core/save/save_document_validator.gd` ;
- `src/core/save/save_document_reader.gd` ;
- `src/core/save/save_file_store.gd` ;
- `src/core/save/save_migration.gd` ;
- `src/core/save/save_migration_v1_to_v2.gd` ;
- `src/core/save/save_migration_runner.gd` ;
- `src/core/save/save_section_registry.gd` ;
- `src/core/save/save_coordinator.gd` ;
- `src/features/beacons/infrastructure/beacon_save_section.gd` ;
- `src/app/save_bootstrap.gd` ;
- `scenes/learning/ch09_save_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-09.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-09.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

'''
marker = '## 17. Erreurs à ne pas reproduire'
if marker not in text:
    raise SystemExit("Chapter 9 insertion marker not found")
text = text.replace(marker, chapter9_section + marker, 1)

text = text.replace(
    '- ne pas traiter le fichier SQLite comme un slot de sauvegarde complet ;',
    '''- ne pas traiter le fichier SQLite comme un slot de sauvegarde complet ;
- ne pas écrire directement dans le fichier final ;
- ne pas promettre une atomicité universelle non documentée ;
- ne pas laisser une sauvegarde future tomber silencieusement sur son `.bak` ;
- ne pas écraser une sauvegarde future avec un ancien build ;
- ne pas copier un principal corrompu vers une bonne copie `.bak` ;
- ne pas appliquer une section avant la validation globale ;
- ne pas libérer le verrou avant application ou annulation ;''',
    1,
)

journal = '''### 2026-07-19 — version 3.9.0

- création et audit statique du chapitre 9 ;
- distinction entre dépôts SQLite et snapshots de partie ;
- format JSON versionné avec empreinte canonique ;
- slots validés, fichier temporaire, copie `.bak` et remplacement contrôlé ;
- sauvegardes futures protégées contre le fallback et l’écrasement ;
- migrations en mémoire et validation avant application ;
- chargement en plusieurs phases avec verrou jusqu’à fin ou annulation ;
- première partie du Livre II terminée, 9 chapitres sur 9 ;
- progression globale à 9 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 10 ;
- PDF non construit.

'''
marker = '### 2026-07-19 — version 3.8.0'
if marker not in text:
    raise SystemExit("Journal insertion marker not found")
text = text.replace(marker, journal + marker, 1)

path.write_text(text, encoding="utf-8", newline="\n")
Path("tools/patch_ch09_continuity.py").unlink()
Path(".github/workflows/patch-ch09-continuity.yml").unlink()
