---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.13.0"
lang: "fr-FR"
last-updated: "2026-07-19"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les règles QA, les erreurs à ne pas reproduire et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot.

> **Point d’entrée recommandé :** `REPRISE-NOUVELLE-CONVERSATION.md` fournit le prompt stable à copier dans une nouvelle conversation. Il pointe vers le présent document sans recopier l’état courant ; `CONTINUITE-PROJET.md` reste l’unique source de vérité de la reprise.

## 1. Procédure obligatoire lors d’une reprise

Une nouvelle conversation doit :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. lire le plan maître du Livre ou Pack actif ;
4. vérifier les derniers commits, branches, pull requests et workflows ;
5. ne pas recréer un chapitre, audit ou choix déjà présent ;
6. identifier le prochain chapitre ;
7. annoncer **GPT-5.6 Sol — Moyenne ou Élevée** et justifier le choix ;
8. comparer le périmètre au plan maître ;
9. rédiger, auditer, corriger et lancer la validation légère ;
10. mettre à jour index, roadmap, `contents.txt` et ce fichier ;
11. ne construire le PDF qu’à la fin d'un Livre ou du Companion Pack, sauf modification directe de la chaîne PDF.

## 2. Sources maîtres

- **Livre II :** `Livre-II/index.md` et le présent fichier ;
- **Livre III :** `plans/LIVRE-III-PLAN-MAITRE.md` ;
- **Livre IV :** `plans/LIVRE-IV-PLAN-MAITRE.md` ;
- **Livre V :** `plans/LIVRE-V-PLAN-MAITRE.md` ;
- **Companion Pack :** `plans/COMPANION-PACK-PLAN-MAITRE.md`.

Aucun titre, ordre ou périmètre ne doit être modifié silencieusement.

## 3. Vision et contraintes permanentes

Le guide doit permettre à un débutant de concevoir un jeu 3D réaliste avec :

- Godot et GDScript ;
- Blender ;
- Python, JSON, SQLite et mémoire vectorielle ;
- IA locale pour texte, image, voix, sons et musique ;
- outils gratuits, locaux et majoritairement open source ;
- Windows et GPU AMD comme configuration de référence ;
- parcours Solo et Studio ;
- projet fil rouge `Project Asteria`.

Chaque procédure doit expliquer :

- quel programme ouvrir ;
- où exécuter la commande ;
- où créer ou modifier le fichier ;
- les fonctions, paramètres, types, opérateurs et retours ;
- le résultat attendu ;
- les erreurs et corrections ;
- les frontières avec les chapitres voisins.

## 4. Configuration de référence

- Windows 11 ;
- AMD Radeon RX 6750 XT, 12 Go ;
- Ryzen 7 2700 ;
- 32 Go de RAM ;
- PowerShell 7 ;
- Visual Studio Code ;
- Godot `4.7.1-stable`, édition Standard, GDScript, Forward+ ;
- Docker Desktop pour les services adaptés ;
- ComfyUI natif Windows, ZLUDA expérimental lorsque pertinent.

## 5. Collection

### Volume 0

**Terminé et audité.** Onze chapitres normatifs, annexes, convention des contextes et QA.

### Livre I

**Terminé, repéré et audité.** Dix chapitres :

1. Matériel, Windows, pilotes AMD et accélération locale.
2. Terminal, PowerShell et outils Windows.
3. Git, GitHub et Visual Studio Code.
4. Python et environnements virtuels.
5. Docker et Docker Compose.
6. Open WebUI, Open Terminal et Vane.
7. ComfyUI et workflows graphiques.
8. LLM locaux.
9. Audio IA local.
10. Sécurité, sauvegarde et validation.

### Livre II

**En cours : 12 chapitres sur 30.**

#### Partie A — Fondations Godot, architecture et données

1. Découvrir Godot et créer le projet fil rouge — terminé.
2. Fondamentaux de GDScript — terminé, enrichi et audité contre les doublons.
3. Scènes, nœuds, Resources et signaux — terminé au niveau `static-review`.
4. Architecture modulaire du projet — terminé au niveau `static-review`.
5. Services, gestionnaires, bus d’événements et injection de dépendances — terminé au niveau `static-review`.
6. Entrées, contrôleurs, caméras et interactions — terminé au niveau `static-review`.
7. Données avec Resources, JSON et configurations — terminé au niveau `static-review`.
8. SQLite, migrations et données persistantes — terminé au niveau `static-review`.
9. Sauvegardes, chargements et compatibilité des versions — terminé au niveau `static-review`.

#### Partie B — Plateforme IA locale

10. Mémoire vectorielle, connaissances et recherche sémantique — terminé au niveau `static-review`.
11. Communication Godot avec les services IA locaux — terminé au niveau `static-review`.
12. HTTP, WebSocket, API compatibles OpenAI et files de tâches — terminé au niveau `static-review`.
13. Sécurité et séparation production/runtime de l’IA — prochain chapitre.

#### Partie C — Systèmes de gameplay

14. Personnages.
15. Relations sociales.
16. Famille et générations.
17. Agents IA et comportements autonomes.
18. Combat.
19. Compétences et pouvoirs.
20. Inventaire et réputation des objets.
21. Économie.
22. Monde vivant et simulation écologique.
23. Politique, factions et justice.
24. Construction et gestion de domaines.
25. Narration, quêtes, codex et connaissances.

#### Partie D — Industrialisation

26. Outils d’édition internes et pipelines de contenu.
27. Tests unitaires, tests d’intégration et simulations.
28. Journalisation, diagnostic et reproductibilité.
29. Automatisation Python et génération de données.
30. Architecture Solo et architecture Studio.

### Livres III à V et Companion Pack

Le détail chapitre par chapitre ou pack par pack se trouve dans les quatre plans maîtres. Chaque entrée y possède objectifs, livrables, dépendances, frontières et critères de validation.

## 6. Repères d’utilisation

| Repère | Contexte |
|---|---|
| `[PS]` | PowerShell 7 |
| `[CMD]` | Invite de commandes |
| `[WSL]` | Terminal WSL |
| `[DCT]` | Terminal dans un conteneur |
| `[DCK]` | Docker Desktop |
| `[VSC]` | Visual Studio Code |
| `[WEB]` | Navigateur |
| `[APP]` | Application graphique nommée |
| `[SORTIE]` | Résultat à lire |
| `[LECTURE]` | Exemple de référence |

Forme obligatoire :

> **[LECTURE] Forme normative — Ne pas saisir.**

```text
[CODE] Outil - Action : chemin, cible ou précision
```

## 7. Niveau GPT-5.6 Sol

Avant chaque chapitre :

> **[LECTURE] Modèle d’annonce — Ne pas saisir.**

```text
Chapitre à produire : …
Niveau GPT-5.6 Sol recommandé : Moyenne / Élevée
Justification : …
```

- **Moyenne** : chapitre descriptif ou linéaire ;
- **Élevée** : architecture, code imbriqué, données, IA, sécurité, optimisation ou nombreuses dépendances.

Chapitres 3 à 12 : **Élevée**.

## 8. Audit par chapitre

Chaque chapitre suit :

1. rédaction ;
2. comparaison au plan maître ;
3. audit de complétude ;
4. explication détaillée du code ;
5. contrôle des doublons ;
6. vérification technique contre les sources officielles ;
7. contrôle des repères ;
8. correction des omissions ;
9. contrôle des frontières ;
10. mise à jour de la gouvernance ;
11. rapport QA ;
12. workflows légers ;
13. statut `static-review` ou `runtime-tested`.

Métadonnées minimales :

> **[LECTURE] Exemple YAML — Ne pas créer sans chemin.**

```yaml
status: "reviewed"
audit-status: "complete"
audit-date: "YYYY-MM-DD"
audit-level: "static-review"
audit-report: "Livre-II/QA/..."
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"
```

## 9. Politique PDF

Décision utilisateur du 19 juillet 2026 :

- ne plus construire le PDF après chaque chapitre ;
- construire et inspecter le PDF à la fin de chaque Livre ;
- construire une dernière version à la fin de la collection ;
- autoriser une exception uniquement pour une modification directe de la chaîne PDF ou de la mise en page.

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.5.0`.

Les workflows ont des responsabilités séparées :

- `Validate Chapters Without PDF` : structure, métadonnées, liens, doublons et assertion d’absence de PDF ;
- `Validate Usage Contexts` : présence et cohérence sémantique des repères ;
- `Validate Documentation PDF` : construction manuelle de fin de Livre ou validation exceptionnelle de la chaîne PDF.

La campagne rétroactive des chapitres 5 et 6 est enregistrée dans `Livre-II/QA/VALIDATION-AUTOMATIQUE-CHAPITRES-05-06.yaml`.

## 10. Règle pédagogique du code

À la première apparition, expliquer :

- mot-clé ;
- nom ;
- type ;
- opérateur ;
- paramètre et argument ;
- valeur par défaut ;
- retour ;
- portée ;
- index ou clé ;
- appel de méthode ;
- résultat concret.

Les rappels courts sont permis. Les duplications intégrales sont interdites.

La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif, une correction, un exemple corrigé et l’explication de leur différence.

Les sections détaillées portent `<!-- qa:error-correction-section -->`. Un index compact de symptômes peut porter `<!-- qa:error-correction-index -->` uniquement s’il renvoie vers des exemples détaillés conformes.

## 11. Décisions d’architecture de `Project Asteria`

### 11.1 Architecture générale

- organisation feature-first ;
- couches locales non spéculatives ;
- dépendances orientées vers le domaine et les contrats ;
- composition privilégiée ;
- `src/app` comme point de composition ;
- `core` ne dépend d’aucune fonctionnalité ;
- infrastructure derrière des contrats ;
- matrice de dépendances et ADR comme sources de vérité ;
- déplacements Godot effectués depuis le dock FileSystem ;
- services construits par le bootstrap ;
- registre limité au point de composition ;
- bus d’événements typé et limité ;
- un Autoload par nécessité de durée de vie, pas par commodité ;
- démarrage déterministe et arrêt dans l’ordre inverse.

### 11.2 Entrées et données

- touches physiques absentes du code métier ;
- données de conception séparées de l’état runtime ;
- `Resource` partagées considérées comme immuables pendant le gameplay ;
- identifiants métier stables indépendants des noms affichés et des chemins ;
- JSON validé puis converti vers des types du domaine ;
- configuration mappée vers `AppConfig` avant injection.

### 11.3 SQLite

- base SQLite mutable sous `user://` ;
- Godot-SQLite encapsulé derrière `DatabaseConnection` ;
- requêtes paramétrées obligatoires pour toute valeur dynamique ;
- clés étrangères, WAL, timeout et synchronisation vérifiés par connexion ;
- migrations numérotées, append-only, transactionnelles et vérifiées par checksum ;
- copie fermée créée uniquement avant une migration réellement en attente ;
- schéma futur refusé avant toute mutation ;
- `quick_check` et `foreign_key_check` exécutés après migration ;
- absence de ligne distinguée d’une panne SQL.

### 11.4 Sauvegardes

- snapshot de partie distinct des dépôts SQLite ;
- format JSON versionné sous `user://saves/` ;
- empreinte canonique du payload avec précision numérique contrôlée ;
- slots validés, fichier temporaire, copie `.bak` et remplacement contrôlé ;
- sauvegarde future refusée et protégée contre l’écrasement ;
- migrations de sauvegarde linéaires et append-only ;
- validation complète avant application au monde ;
- verrou de chargement maintenu jusqu’à application ou annulation.

### 11.5 Mémoire vectorielle

- connaissances sources séparées de l’index vectoriel dérivé ;
- mémoire vectorielle exclue de l’autorité des sauvegardes ;
- manifeste de corpus et `source_id` stables comme sources d’identité ;
- fragments limités avec le tokenizer réel et identifiés par UUID déterministe ;
- modèle de référence `intfloat/multilingual-e5-small`, dimension `384`, préfixes `query:` et `passage:` ;
- CPU comme chemin de référence Windows/AMD ;
- accélération DirectML, WinML ou MIGraphX uniquement après mesure runtime ;
- Qdrant utilisé en mode local Python pour le chapitre 10 ;
- stockage Qdrant sous `var/knowledge/`, dérivé et non versionné ;
- provenance, langue, visibilité, tags, modèle et version de schéma conservés dans le payload ;
- remplacement complet d’une source dans le parcours Solo ;
- suppressions propagées depuis le manifeste sans supprimer les sources ;
- visibilités calculées par une politique d’autorisation ;
- score de similarité jamais présenté comme probabilité de vérité ;
- repli lexical construit directement depuis les sources ;
- évaluation par questions de référence, `hit-rate@k` et MRR.

### 11.6 Communication Godot avec l’IA locale

- `LocalAiGateway` constitue le port applicatif indépendant du transport ;
- Godot ne dépend ni de Qdrant, ni du modèle d’embeddings, ni de Python dans le domaine ;
- le chapitre 11 utilise un processus compagnon local et un transport JSON par lignes sur stdio ;
- stdout est réservé au protocole et stderr aux journaux ;
- les enveloppes requête et réponse possèdent format, version et `request_id` ;
- chaque réponse doit corréler une requête encore en attente ;
- les messages et tampons sont bornés ;
- la lecture non bloquante accumule les fragments jusqu’au saut de ligne ;
- le service découvre ses capacités avant de devenir prêt ;
- l’état distingue `STOPPED`, `STARTING`, `READY`, `DEGRADED`, `FAILED` et `STOPPING` ;
- les délais utilisent `Time.get_ticks_msec()` ;
- une réponse tardive après délai ou annulation est ignorée ;
- l’annulation reste coopérative et ne promet pas l’interruption immédiate d’une bibliothèque ;
- le repli déterministe appartient à la fonctionnalité, pas au transport ;
- le repli masque uniquement les indisponibilités prévues, jamais une erreur de contrat ;
- le gameplay essentiel reste autoritaire et indépendant du service IA ;
- les chemins d’exécution proviennent d’une configuration fiable et les arguments restent séparés ;
- le processus compagnon reçoit un arrêt coopératif puis un arrêt forcé seulement après délai ;
- les exports Web et les plateformes non qualifiées utilisent le repli ;
- les adaptateurs réseau du chapitre 12 restent derrière `LocalAiGateway` ;
- secrets, isolation, signature et durcissement de production restent réservés au chapitre 13.

### 11.7 Transports réseau et files de tâches

- `LocalAiGateway` reste le port applicatif canonique ;
- HTTP sert aux échanges bornés et WebSocket aux événements, progressions et flux sélectionnés ;
- les enveloppes HTTP sont versionnées et distinguent résultat de transport, code HTTP et erreur métier ;
- `HTTPRequest.body_size_limit` est configuré avant téléchargement ;
- WebSocket est sondé sans bloquer, avec tampons et files de paquets bornés ;
- les événements de tâche portent une séquence croissante et l’état HTTP final reste l’autorité ;
- les tâches utilisent `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCEL_REQUESTED`, `CANCELLED` et `EXPIRED` ;
- la file prioritaire est bornée et la surcharge produit `429` avec `Retry-After` ;
- une clé d’idempotence est liée à une empreinte canonique du payload et un conflit produit `409` ;
- les retries sont bornés avec backoff exponentiel et jitter ;
- `timeout_ms` est une durée relative convertie en échéance monotone locale ;
- le polling HTTP reste disponible lorsque WebSocket est absent ;
- la compatibilité OpenAI est isolée dans un adaptateur versionné ;
- l’exemple `chat/completions` constitue un sous-ensemble historique et l’API Responses peut être ciblée séparément ;
- la file en mémoire est volatile et ne promet aucune reprise après panne ;
- le repli déterministe masque seulement les indisponibilités prévues ;
- le durcissement de production reste réservé au chapitre 13.

## 12. Chapitre 5 — état résumé

Fichier : `Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions : registre limité au bootstrap, bus typé, cycle de vie explicite, démarrage déterministe, arrêt inverse et nettoyage des démarrages partiels.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-05.md`.

## 13. Chapitre 6 — état résumé

Fichier : `Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions : `InputMap`, séparation entrée/intention/contrôleur/moteur, `CharacterBody3D`, caméra troisième personne, interaction typée, remappage préparatoire et accessibilité.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-06.md`.

## 14. Chapitre 7 — état détaillé

Fichier : `Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- quatre catégories séparées : conception, configuration, runtime et persistance ;
- `BeaconProfile` comme `Resource` de conception ;
- `BeaconRuntimeState` comme état vivant distinct ;
- ressources externes privilégiées pour les données identifiées et cataloguées ;
- cache et partage des `Resource` explicités ;
- duplication superficielle et profonde documentées ;
- `resource_local_to_scene` réservé à des cas locaux ciblés ;
- identifiants `StableId` indépendants de l’affichage ;
- `BeaconCatalog` typé, validé et sans doublons ;
- liste explicite de chemins pour un chargement déterministe ;
- JSON lu avec `FileAccess`, analysé avec `JSON`, validé puis mappé ;
- `format_version` obligatoire pour les documents externes ;
- `ConfigFile` utilisé pour une configuration INI non secrète ;
- valeurs par défaut dans `res://`, surcharge locale dans `user://` ;
- configuration convertie vers `AppConfig` avant injection ;
- SQLite et migrations réservés au chapitre 8 ;
- sauvegardes et compatibilité réservées au chapitre 9.

Livrables documentés :

- `src/features/beacons/domain/beacon_profile.gd` ;
- `src/features/beacons/domain/beacon_runtime_state.gd` ;
- `src/features/beacons/application/beacon_catalog.gd` ;
- `src/features/beacons/infrastructure/beacon_catalog_loader.gd` ;
- `src/features/beacons/infrastructure/beacon_json_mapper.gd` ;
- `src/features/beacons/infrastructure/beacon_json_importer.gd` ;
- `src/core/data/stable_id.gd` ;
- `src/core/data/json_file_reader.gd` ;
- `src/core/data/dictionary_reader.gd` ;
- `src/core/config/app_config.gd` ;
- `src/core/config/app_config_loader.gd` ;
- `data/beacons/*.tres` ;
- `data/import/beacons.json` ;
- `config/default.cfg` ;
- `scenes/learning/ch07_data_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-07.md`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 15. Chapitre 8 — état détaillé

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

## 16. Chapitre 9 — état détaillé

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

## 17. Chapitre 10 — état détaillé

Fichier : `Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- sources Markdown et manifeste JSON comme autorité ;
- index Qdrant entièrement dérivé et reconstructible ;
- `intfloat/multilingual-e5-small` comme modèle pédagogique ;
- dimension `384` et distance cosinus ;
- CPU comme chemin Windows/AMD de référence ;
- fragments mesurés avec le tokenizer réel ;
- cible `420`, overlap `60`, maximum `480` tokens ;
- titres Markdown et provenance conservés ;
- `source_id` stable et `chunk_id` UUIDv5 déterministe ;
- préfixes `passage:` et `query:` obligatoires ;
- payload avec révision, hash, langue, visibilité, tags, modèle et schéma ;
- remplacement complet des points d’une source dans le parcours Solo ;
- suppression des sources obsolètes par différence avec le manifeste ;
- filtres de visibilité imposés ;
- repli lexical indépendant du modèle et de Qdrant ;
- évaluation par cas versionnés, `hit-rate@k` et MRR ;
- accélérations DirectML, WinML et MIGraphX non revendiquées ;
- communication Godot réservée au chapitre 11 ;
- HTTP, WebSocket et serveur Qdrant réservés au chapitre 12.

Livrables documentés :

- `knowledge/manifest.json` ;
- `knowledge/sources/**/*.md` ;
- `knowledge/evaluation/retrieval-cases.json` ;
- `tools/knowledge/knowledge_config.py` ;
- `tools/knowledge/knowledge_models.py` ;
- `tools/knowledge/source_loader.py` ;
- `tools/knowledge/chunker.py` ;
- `tools/knowledge/embedding_provider.py` ;
- `tools/knowledge/knowledge_index.py` ;
- `tools/knowledge/qdrant_index.py` ;
- `tools/knowledge/lexical_index.py` ;
- `tools/knowledge/retrieval_service.py` ;
- `tools/knowledge/index_knowledge.py` ;
- `tools/knowledge/search_knowledge.py` ;
- `tools/knowledge/evaluate_retrieval.py`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-10.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-10.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 18. Chapitre 11 — état détaillé

Fichier : `Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- port `LocalAiGateway` indépendant du transport ;
- processus compagnon Python local ;
- protocole JSON par lignes sur entrée et sortie standard ;
- formats requête et réponse versionnés ;
- erreurs et capacités structurées ;
- `request_id` unique par session et compteur ;
- appels non bloquants sondés depuis `_process()` ;
- tampon des lignes partielles et limite en octets ;
- stdout réservé au protocole, stderr aux journaux ;
- handshake `capabilities.describe` avant l’état prêt ;
- états `STOPPED`, `STARTING`, `READY`, `DEGRADED`, `FAILED` et `STOPPING` ;
- délais fondés sur `Time.get_ticks_msec()` ;
- tickets résolus une seule fois ;
- réponses tardives ignorées après retrait du registre ;
- annulation coopérative, sans promesse d’interruption immédiate ;
- repli déterministe au niveau de la fonctionnalité `beacons` ;
- repli limité à indisponibilité, timeout et capacité absente ;
- règles de gameplay essentielles indépendantes du service ;
- arrêt par `system.shutdown`, puis `OS.kill()` uniquement après délai ;
- export Web et plateformes non qualifiées orientés vers le repli ;
- HTTP, WebSocket, API compatibles OpenAI et files de tâches réservés au chapitre 12 ;
- durcissement production/runtime réservé au chapitre 13.

Livrables documentés :

- `src/core/ai/ai_service_config.gd` ;
- `src/core/ai/ai_service_error.gd` ;
- `src/core/ai/ai_capability.gd` ;
- `src/core/ai/ai_request.gd` ;
- `src/core/ai/ai_response.gd` ;
- `src/core/ai/ai_call_ticket.gd` ;
- `src/core/ai/ai_service_status.gd` ;
- `src/core/ai/ai_envelope_codec.gd` ;
- `src/core/ai/ai_transport.gd` ;
- `src/core/ai/local_ai_gateway.gd` ;
- `src/core/ai/stdio_companion_transport.gd` ;
- `src/core/ai/local_ai_gateway_service.gd` ;
- `src/features/beacons/application/beacon_knowledge_service.gd` ;
- `src/features/beacons/infrastructure/beacon_knowledge_fallback.gd` ;
- `src/app/ai_bootstrap.gd` ;
- `tools/ai/companion_protocol.py` ;
- `tools/ai/knowledge_service_adapter.py` ;
- `tools/ai/companion_service.py` ;
- `scenes/learning/ch11_local_ai_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-11.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-11.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 19. Chapitre 12 — état détaillé

Fichier : `Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- `LocalAiGateway` conservé comme unique port métier ;
- `HTTPRequest` pour les requêtes et réponses bornées ;
- `WebSocketPeer` pour événements, progressions et certains flux ;
- contrats HTTP versionnés et erreurs structurées ;
- limite du corps configurée avant téléchargement ;
- séparation résultat de transport, code HTTP et erreur métier ;
- tâches longues avec sept états explicites ;
- file prioritaire bornée, concurrence limitée et backpressure ;
- `429` et `Retry-After` pour la surcharge ;
- idempotence par clé et empreinte canonique du payload ;
- conflit `409` lorsqu’une clé est réutilisée avec un autre payload ;
- retries bornés avec backoff et jitter ;
- délais relatifs convertis vers une horloge monotone locale ;
- annulation coopérative et réponses tardives rejetées ;
- événements ordonnés par séquence et polling HTTP de secours ;
- adaptateur compatible OpenAI isolé du domaine ;
- compatibilité `chat/completions` qualifiée de sous-ensemble historique ;
- API Responses et SSE réservés à un schéma explicitement versionné ;
- file en mémoire qualifiée de volatile ;
- repli déterministe limité aux indisponibilités attendues ;
- durcissement production/runtime réservé au chapitre 13.

Livrables documentés :

- `src/core/ai/ai_network_config.gd` ;
- `src/core/ai/ai_network_envelope_codec.gd` ;
- `src/core/ai/http_local_ai_transport.gd` ;
- `src/core/ai/websocket_event_channel.gd` ;
- `src/core/ai/ai_task_status.gd` ;
- `src/core/ai/ai_task.gd` ;
- `src/core/ai/ai_task_event.gd` ;
- `src/core/ai/openai_compatible_mapper.gd` ;
- `src/app/ai_network_bootstrap.gd` ;
- `tools/ai_server/task_models.py` ;
- `tools/ai_server/task_queue.py` ;
- `tools/ai_server/task_worker.py` ;
- `tools/ai_server/protocol.py` ;
- `tools/ai_server/operations.py` ;
- `tools/ai_server/task_registry.py` ;
- `tools/ai_server/event_hub.py` ;
- `tools/ai_server/openai_adapter.py` ;
- `tools/ai_server/server.py` ;
- `scenes/learning/ch12_network_ai_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-12.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-12.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 20. Erreurs à ne pas reproduire

- ne pas donner une commande sans terminal ;
- ne pas donner un fichier sans éditeur et chemin ;
- ne pas présenter une sortie comme une commande ;
- ne pas revendiquer un test runtime non exécuté ;
- ne pas laisser fonction ou paramètre sans explication ;
- ne pas dupliquer une explication complète ;
- ne pas créer de couche ou manager sans besoin ;
- ne pas laisser `core` dépendre d’une fonctionnalité ;
- ne pas utiliser le registre comme Service Locator ;
- ne pas créer un Autoload par service ;
- ne pas utiliser un bus générique à dictionnaires ;
- ne pas modifier une `Resource` de conception partagée comme état runtime ;
- ne pas utiliser un nom affiché comme identifiant métier ;
- ne pas accepter un JSON sans validation de structure et de version ;
- ne pas stocker un secret dans un fichier versionné ;
- ne pas écrire une base mutable dans `res://` ;
- ne pas concaténer une valeur dynamique dans SQL ;
- ne pas modifier une migration déjà appliquée ;
- ne pas démarrer le gameplay après une migration incomplète ;
- ne pas copier une base WAL encore ouverte ;
- ne pas masquer une panne SQL comme une absence de ligne ;
- ne pas traiter le fichier SQLite comme un slot de sauvegarde complet ;
- ne pas écrire directement dans le fichier final ;
- ne pas promettre une atomicité universelle non documentée ;
- ne pas laisser une sauvegarde future tomber silencieusement sur son `.bak` ;
- ne pas écraser une sauvegarde future avec un ancien build ;
- ne pas copier un principal corrompu vers une bonne copie `.bak` ;
- ne pas appliquer une section avant la validation globale ;
- ne pas libérer le verrou avant application ou annulation ;
- ne pas utiliser les `.tres` comme sauvegarde du joueur ;
- ne pas traiter un index vectoriel comme une source canonique ;
- ne pas inclure Qdrant dans l’autorité d’une sauvegarde ;
- ne pas découper par caractères lorsque le modèle consomme des tokens ;
- ne pas tronquer silencieusement un passage ;
- ne pas omettre les préfixes E5 ;
- ne pas mélanger des dimensions de vecteurs ;
- ne pas conserver plusieurs révisions actives d’une source ;
- ne pas laisser une requête élargir sa visibilité ;
- ne pas présenter un score de similarité comme probabilité ;
- ne pas promettre l’accélération AMD sans exécution ;
- ne pas masquer toute erreur par le repli lexical ;
- ne pas versionner le stockage Qdrant dérivé ;
- ne pas bloquer la boucle principale pour attendre un service IA ;
- ne pas exposer `FileAccess` ou le transport dans les scènes de gameplay ;
- ne pas lire directement le stockage Qdrant depuis Godot ;
- ne pas construire une commande depuis une saisie utilisateur ;
- ne pas mélanger les journaux et le protocole sur stdout ;
- ne pas analyser une ligne JSON partielle ;
- ne pas laisser un tampon de protocole sans limite ;
- ne pas réutiliser un `request_id` ;
- ne pas appliquer une réponse tardive ;
- ne pas présenter un timeout comme une interruption garantie ;
- ne pas masquer une erreur de protocole par le repli ;
- ne pas rendre l’IA obligatoire pour une règle essentielle ;
- ne pas oublier l’arrêt du processus compagnon ;
- ne pas confondre processus vivant et capacité disponible ;
- ne pas coupler le port applicatif à HTTP avant le chapitre 12 ;
- ne pas utiliser `OS.kill()` avant la tentative d’arrêt coopératif ;
- ne pas placer les routes HTTP dans le gameplay ;
- ne pas utiliser WebSocket pour tous les échanges ;
- ne pas lancer plusieurs requêtes simultanées sur une même instance `HTTPRequest` ;
- ne pas confondre résultat de transport et code HTTP ;
- ne pas retenter immédiatement après `429` ;
- ne pas laisser une file de tâches sans limite ;
- ne pas confondre corrélation et idempotence ;
- ne pas accepter la même clé d’idempotence pour deux payloads différents ;
- ne pas traiter `CANCEL_REQUESTED` comme un état terminal ;
- ne pas appliquer un événement WebSocket hors séquence ;
- ne pas traiter un fragment de streaming comme résultat final ;
- ne pas laisser un schéma OpenAI-compatible devenir le modèle du domaine ;
- ne pas déclarer le service prêt lorsque ses dépendances obligatoires sont indisponibles ;
- ne pas utiliser un identifiant de tâche comme autorisation ;
- ne pas promettre une reprise après panne avec une file volatile ;
- ne pas masquer une erreur de protocole par le repli ;
- ne pas construire le PDF à chaque chapitre ;
- ne pas oublier la mise à jour de ce fichier.

## 21. État courant

- branche principale : `main` ;
- jalon : M3 — Livre II ;
- progression : 12 chapitres sur 30 ;
- chapitre 1 : version `1.3.0` ;
- chapitre 2 : version `1.5.0` ;
- chapitres 3 à 6 : version `1.1.0` ;
- chapitre 7 : version `1.1.1` ;
- chapitre 8 : version `1.0.0` ;
- chapitre 9 : version `1.0.0` ;
- chapitre 10 : version `1.0.0` ;
- chapitre 11 : version `1.0.0` ;
- chapitre 12 : version `1.0.1` ;
- Starter Kit non matérialisé ;
- licence globale à définir ;
- accessibilité PDF avancée à traiter avant publication.

## 22. Prochaine action

Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md
```

Périmètre attendu :

- modèle de menaces et frontières de confiance ;
- séparation stricte entre outils de production et services autorisés au runtime ;
- configurations distinctes développement, test et production ;
- secrets hors versionnement et hors payloads de gameplay ;
- écoute sur boucle locale par défaut et refus de l’exposition implicite ;
- authentification obligatoire dès qu’un service quitte la boucle locale ;
- TLS et certificats lorsque le réseau l’exige ;
- listes d’autorisation pour opérations, modèles et chemins ;
- moindre privilège pour processus, fichiers et réseau ;
- limites de payload, débit, concurrence et quotas ;
- rédaction des journaux et politique de conservation ;
- dépendances épinglées, inventaire, licences et SBOM ;
- packaging, signature et stratégie de mise à jour ;
- échec fermé pour la sécurité avec repli déterministe du gameplay ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.

## 23. Journal

### 2026-07-19 — version 3.13.0

- création, correction et audit statique du chapitre 12 ;
- conservation de `LocalAiGateway` comme port canonique ;
- transports HTTP et WebSocket derrière des adaptateurs ;
- contrats réseau versionnés, limites avant téléchargement et erreurs structurées ;
- tâches longues, file prioritaire bornée et backpressure ;
- idempotence, retries bornés, polling, séquences et annulation coopérative ;
- compatibilité OpenAI isolée et API Responses explicitement qualifiée ;
- progression à 12 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 13 ;
- aucun PDF construit.


### 2026-07-19 — version 3.12.0

- création et audit statique du chapitre 11 ;
- adoption d’un port applicatif indépendant du transport ;
- ajout d’un processus compagnon Python local par JSON sur stdio ;
- séparation stdout protocolaire et stderr de diagnostic ;
- requêtes et réponses versionnées avec corrélation ;
- découverte de capacités et états explicites ;
- appels non bloquants, délais monotones et réponses tardives ignorées ;
- annulation coopérative sans promesse d’interruption immédiate ;
- repli déterministe au niveau de la fonctionnalité ;
- arrêt coopératif puis forcé après délai ;
- progression à 11 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 12 ;
- aucun PDF construit.

### 2026-07-19 — version 3.11.0

- création et audit statique du chapitre 10 ;
- séparation permanente entre sources canoniques, index vectoriel dérivé et sauvegardes ;
- choix pédagogique de `multilingual-e5-small`, dimension `384`, CPU de référence ;
- découpage avec tokenizer réel, provenance et UUID déterministes ;
- Qdrant Local Mode pour l’outil Python, sans serveur ni accès Godot direct ;
- synchronisation des modifications et suppressions ;
- filtres de visibilité, langue et tags ;
- repli lexical indépendant du modèle ;
- évaluation par `hit-rate@k` et MRR ;
- progression à 10 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 11 ;
- correction de la version déclarée du protocole QA vers `1.5.0` ;
- aucun PDF construit.

### 2026-07-19 — version 3.10.0

- ajout de `REPRISE-NOUVELLE-CONVERSATION.md` comme point d’entrée stable pour une nouvelle conversation ;
- rappel que le dépôt puis `CONTINUITE-PROJET.md` prévalent sur les anciens résumés ;
- interdiction de recopier la progression et la prochaine action dans le fichier de reprise ;
- procédure de confirmation obligatoire avant toute nouvelle rédaction ;
- ajout du fichier de reprise aux chemins du workflow léger ;
- aucun PDF construit.

### 2026-07-19 — version 3.9.0

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

### 2026-07-19 — version 3.8.0

- création et audit statique du chapitre 8 ;
- choix de Godot-SQLite `4.7` sous licence MIT avec réserve Godot 4.7.1 ;
- ajout des contrats de connexion et de dépôt ;
- schéma relationnel des états et événements de balise ;
- requêtes paramétrées et transactions explicites ;
- migrations numérotées, checksums et refus des schémas futurs ;
- backup fermé seulement avant migration et restauration sans sidecars WAL ;
- contrôles `quick_check` et `foreign_key_check` ;
- validateur sémantique étendu aux libellés « Architecture corrigée » et « Flux corrigé » ;
- validations finales `29684886165` et `29684886159` réussies ;
- 56 sources, 55 identifiants uniques et 1 143 blocs sur 1 143 repérés ;
- progression à 8 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 9 ;
- PDF non construit.

### 2026-07-19 — version 3.7.0

- généralisation sémantique de la règle « erreur fautive / correction » ;
- audit rétroactif des chapitres 1 à 6 ;
- 52 cas détaillés enrichis ;
- ajout des marqueurs QA de section et d’index ;
- validation automatique renforcée ;
- aucun PDF intermédiaire construit.

### 2026-07-19 — version 3.6.0

- création et audit statique du chapitre 7 ;
- séparation données de conception, configuration, runtime et persistance ;
- adoption de Resources typées et catalogues à identifiants stables ;
- validation JSON et versionnement des formats ;
- configuration par défaut et surcharge locale avec `ConfigFile` ;
- progression à 7 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 8 ;
- PDF non construit.

### 2026-07-19 — version 3.5.0

- séparation permanente des workflows chapitre et PDF ;
- ajout de `tools/validate_chapters.py` et `tools/check_context_markers.py` ;
- validation automatique rétroactive des chapitres 5 et 6 ;
- aucun PDF produit par la validation légère.

### 2026-07-19 — version 3.4.0

- création et audit statique du chapitre 6 ;
- séparation lecture des entrées, intention, contrôleur et moteur ;
- caméra troisième personne et interaction typée ;
- progression à 6 chapitres sur 30.

### 2026-07-19 — version 3.3.0

- création et audit statique du chapitre 5 ;
- registre limité au bootstrap ;
- bus d’événements typé ;
- cycle de vie des services et politique PDF différée.

### 2026-07-18 — versions 3.0.0 à 3.2.0

- plans maîtres détaillés des Livres III à V et du Companion Pack ;
- création du chapitre 3 ;
- création du chapitre 4 et architecture feature-first.
