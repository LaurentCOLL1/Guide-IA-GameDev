---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.7.0"
lang: "fr-FR"
last-updated: "2026-07-19"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les règles QA, les erreurs à ne pas reproduire et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot.

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
11. ne construire le PDF qu’à la fin du Livre, sauf modification directe de la chaîne PDF.

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

**En cours : 7 chapitres sur 30.**

#### Partie A — Fondations Godot, architecture et données

1. Découvrir Godot et créer le projet fil rouge — terminé.
2. Fondamentaux de GDScript — terminé, enrichi et audité contre les doublons.
3. Scènes, nœuds, Resources et signaux — terminé au niveau `static-review`.
4. Architecture modulaire du projet — terminé au niveau `static-review`.
5. Services, gestionnaires, bus d’événements et injection de dépendances — terminé au niveau `static-review`.
6. Entrées, contrôleurs, caméras et interactions — terminé au niveau `static-review`.
7. Données avec Resources, JSON et configurations — terminé au niveau `static-review`.
8. SQLite, migrations et données persistantes — prochain chapitre.
9. Sauvegardes, chargements et compatibilité des versions.

#### Partie B — Plateforme IA locale

10. Mémoire vectorielle, connaissances et recherche sémantique.
11. Communication Godot avec les services IA locaux.
12. HTTP, WebSocket, API OpenAI-compatible et files de tâches.
13. Sécurité et séparation production/runtime de l’IA.

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

Chapitres 3 à 7 : **Élevée**.

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
12. workflow `Validate Chapters Without PDF` ;
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

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.4.0`.

Deux workflows sont séparés :

- `Validate Chapters Without PDF` : validation automatique légère à chaque chapitre ;
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

La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif, une correction, un exemple corrigé et l’explication de leur différence. Le titre peut être « Erreurs fréquentes », « Erreurs fréquentes et diagnostics », « Anti-patterns et corrections », « Éviter les anti-patterns » ou toute formulation équivalente.

Les sections détaillées portent `<!-- qa:error-correction-section -->`. Un index compact de symptômes peut porter `<!-- qa:error-correction-index -->` uniquement s’il renvoie vers des exemples détaillés conformes.

## 11. Décisions d’architecture de `Project Asteria`

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
- démarrage déterministe et arrêt dans l’ordre inverse ;
- touches physiques absentes du code métier ;
- données de conception séparées de l’état runtime ;
- `Resource` partagées considérées comme immuables pendant le gameplay ;
- identifiants métier stables indépendants des noms affichés et des chemins ;
- JSON validé puis converti vers des types du domaine ;
- configuration mappée vers `AppConfig` avant injection ;
- SQLite réservé au chapitre 8 et sauvegardes au chapitre 9.

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

## 15. Erreurs à ne pas reproduire

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
- ne pas introduire SQLite avant le chapitre 8 ;
- ne pas utiliser les `.tres` comme sauvegarde du joueur ;
- ne pas construire le PDF à chaque chapitre ;
- ne pas oublier la mise à jour de ce fichier.

## 16. État courant

- branche principale : `main` ;
- jalon : M3 — Livre II ;
- progression : 7 chapitres sur 30 ;
- chapitre 2 : version `1.3.0` ;
- chapitres 3 à 7 : version `1.0.0` ;
- Starter Kit non matérialisé ;
- licence globale à définir ;
- accessibilité PDF avancée à traiter avant publication.

## 17. Prochaine action

Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md
```

Périmètre attendu :

- rôle de SQLite dans `Project Asteria` ;
- choix d’une intégration Godot compatible avec la plateforme de référence ;
- schéma relationnel et types SQLite ;
- clés primaires et étrangères ;
- contraintes et index ;
- transactions ;
- requêtes paramétrées ;
- repository derrière un contrat ;
- migrations numérotées et table de version ;
- rollback et sauvegarde avant migration ;
- séparation données de conception, base persistante et sauvegarde ;
- diagnostic et intégrité ;
- différences Solo/Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.

## 18. Journal

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
