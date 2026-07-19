---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.6.0"
lang: "fr-FR"
last-updated: "2026-07-19"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les règles QA, les erreurs corrigées et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot.

## 1. Procédure de reprise

Une nouvelle conversation doit :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. lire le plan maître du Livre ou Pack concerné ;
4. vérifier les derniers commits, branches, pull requests et workflows ;
5. ne pas recréer un chapitre, audit ou choix déjà présent ;
6. identifier le prochain chapitre ;
7. annoncer **GPT-5.6 Sol — Moyenne ou Élevée** et justifier le choix ;
8. comparer le périmètre au plan maître ;
9. rédiger, auditer et corriger ;
10. exécuter les workflows légers ;
11. mettre à jour index, roadmap, `contents.txt` et ce fichier ;
12. ne construire le PDF qu’à la fin du Livre, sauf modification directe de la chaîne PDF.

## 2. Sources maîtres

- **Livre II :** `Livre-II/index.md` et le présent fichier ;
- **Livre III :** `plans/LIVRE-III-PLAN-MAITRE.md` ;
- **Livre IV :** `plans/LIVRE-IV-PLAN-MAITRE.md` ;
- **Livre V :** `plans/LIVRE-V-PLAN-MAITRE.md` ;
- **Companion Pack :** `plans/COMPANION-PACK-PLAN-MAITRE.md`.

Les plans maîtres des Livres III à V et du Companion Pack contiennent les chapitres ou lots détaillés, leurs objectifs, livrables, dépendances, frontières et critères de validation. Aucun titre, ordre ou périmètre ne doit être modifié silencieusement.

## 3. Vision permanente

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
- les fonctions, paramètres, arguments, types, opérateurs et retours ;
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

### 5.1 Volume 0

**Terminé et audité.** Onze chapitres normatifs, assurance qualité, annexes et convention des contextes.

### 5.2 Livre I

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

### 5.3 Livre II

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
12. HTTP, WebSocket, API compatibles OpenAI et files de tâches.
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
- **Élevée** : architecture, code imbriqué, données, IA, sécurité, optimisation ou dépendances nombreuses.

Chapitres 3 à 7 : **Élevée**.

## 8. Audit obligatoire par chapitre

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
11. workflow automatique léger ;
12. rapport QA ;
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

## 9. Politique PDF et workflows

Décision utilisateur du 19 juillet 2026 :

- ne plus construire le PDF après chaque chapitre ;
- construire et inspecter le PDF à la fin de chaque Livre ;
- construire une dernière version à la fin de la collection ;
- autoriser une exception uniquement pour une modification directe de la chaîne PDF ou de la mise en page.

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.4.0`.

Workflows séparés :

- `Validate Chapters Without PDF` : structure, métadonnées, liens, doublons, repères et assertion d’absence de PDF ;
- `Validate Usage Contexts` : présence et cohérence sémantique des repères ;
- `Validate Documentation PDF` : déclenchement manuel de fin de Livre ou de collection.

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

## 11. Décisions d’architecture de `Project Asteria`

- organisation feature-first ;
- couches locales non spéculatives ;
- dépendances orientées vers le domaine et les contrats ;
- composition privilégiée ;
- `src/app` comme point de composition ;
- `core` ne dépend d’aucune fonctionnalité ;
- infrastructure derrière des contrats ;
- services construits par le bootstrap ;
- registre limité au point de composition ;
- bus d’événements typé et limité ;
- un Autoload par nécessité de durée de vie ;
- démarrage déterministe et arrêt dans l’ordre inverse ;
- actions d’entrée nommées, jamais de touches physiques dans le métier ;
- définitions canoniques séparées de l’état runtime ;
- identifiants stables séparés des noms affichés ;
- fichiers chargés et validés dans l’infrastructure ;
- repositories injectés dans les fonctionnalités ;
- configuration brute convertie en objet typé ;
- aucune mutation des Resources canoniques ;
- aucun secret dans les fichiers versionnés.

## 12. État détaillé des chapitres récents

### 12.1 Chapitre 5

Fichier : `Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md`.

Décisions principales : injection, `GameEventBus` typé, `ServiceRegistry` limité au bootstrap, cycle de vie, démarrage avec rollback et arrêt inverse.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-05.md`.

### 12.2 Chapitre 6

Fichier : `Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md`.

Décisions principales : `PlayerInputReader` → `PlayerInputFrame` → `PlayerController`, `CharacterBody3D`, caméra yaw/pitch avec `SpringArm3D`, interaction typée, remappage en mémoire et accessibilité préparée.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-06.md`.

### 12.3 Chapitre 7

Fichier : `Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions principales :

- quatre familles : conception, configuration, état runtime et persistance ;
- `BeaconCatalog` versionné et validé ;
- `DataValidationIssue` et `DataValidationReport` ;
- identifiants `StringName` stables ;
- Resources canoniques en lecture seule par convention ;
- repository Resource injecté ;
- chemins contrôlés avant chargement ;
- JSON avec diagnostics détaillés ;
- fusion récursive des objets, remplacement des tableaux ;
- `RuntimeConfiguration` typée ;
- couches default puis environnement ;
- `res://` pour les données embarquées, aucune écriture `user://` avant le chapitre 9 ;
- chargement différé sans boucle bloquante ;
- aucun secret versionné.

Livrables documentés :

- `src/core/data/data_validation_issue.gd` ;
- `src/core/data/data_validation_report.gd` ;
- `src/core/config/json_config_loader.gd` ;
- `src/core/config/runtime_configuration.gd` ;
- `src/features/beacons/data/beacon_catalog.gd` ;
- `src/features/beacons/data/beacon_catalog_validator.gd` ;
- `src/features/beacons/application/beacon_catalog_repository.gd` ;
- `src/features/beacons/infrastructure/resource_beacon_catalog_repository.gd` ;
- `data/beacons/beacon_catalog.tres` ;
- `config/defaults/runtime.json` ;
- `config/environments/studio.json` ;
- `scenes/learning/ch07_data_demo.gd` ;
- `scenes/learning/ch07_data_demo.tscn` ;
- `docs/architecture/data-contract.md`.

Omissions trouvées et corrigées pendant la seconde lecture :

- `_read_ai_services()` manquante ;
- `_read_data_paths()` manquante ;
- `_load_catalog_at(path)` appelée sans définition ;
- validation renforcée de la version, des identifiants, des URLs locales, délais et chemins.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-07.md`.

Décision : accepté sous réserves runtime, workflow final et PDF de fin de Livre.

## 13. Erreurs à ne pas reproduire

- ne pas donner une commande sans terminal ;
- ne pas donner un fichier sans éditeur et chemin ;
- ne pas présenter une sortie comme une commande ;
- ne pas revendiquer un test runtime non exécuté ;
- ne pas laisser fonction ou paramètre sans explication ;
- ne pas appeler une fonction absente de l’exemple ;
- ne pas dupliquer une explication complète ;
- ne pas créer de couche ou manager sans besoin ;
- ne pas laisser `core` dépendre d’une fonctionnalité ;
- ne pas utiliser le registre comme Service Locator ;
- ne pas créer un Autoload par service ;
- ne pas modifier une Resource canonique au runtime ;
- ne pas utiliser le nom affiché comme identifiant ;
- ne pas accepter un JSON après la seule vérification syntaxique ;
- ne pas écrire de sauvegarde dans `res://` ;
- ne pas versionner un secret ;
- ne pas bloquer en attendant un chargement différé ;
- ne pas construire le PDF à chaque chapitre ;
- ne pas oublier la mise à jour de ce fichier.

## 14. État courant

- branche principale : `main` ;
- jalon : M3 — Livre II ;
- progression : 7 chapitres sur 30 ;
- fondations : 7 chapitres sur 9 ;
- chapitre 2 : version `1.3.0` ;
- chapitres 3 à 6 : version `1.0.0` ;
- chapitre 7 : version `1.0.1` ;
- Starter Kit non matérialisé ;
- licence globale à définir ;
- accessibilité PDF avancée à traiter avant publication.

## 15. Prochaine action

Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md
```

Périmètre attendu :

- rôle et limites de SQLite ;
- choix de l’intégration Godot ;
- fichier de base sous `user://` ;
- schéma relationnel ;
- clés primaires et étrangères ;
- migrations numérotées ;
- transactions et rollback ;
- index et requêtes préparées ;
- repositories persistants ;
- import initial depuis les données de conception ;
- gestion des erreurs et corruption ;
- différences Solo/Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.

## 16. Journal

### 2026-07-19 — version 3.6.0

- création et seconde lecture du chapitre 7 ;
- séparation définition, configuration, état runtime et persistance ;
- ajout du catalogue, des diagnostics et du repository ;
- ajout du chargeur JSON et de la configuration typée ;
- correction de trois fonctions manquantes dans le premier brouillon ;
- progression à 7 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 8 ;
- aucun PDF intermédiaire.

### 2026-07-19 — version 3.5.0

- séparation permanente des workflows chapitre et PDF ;
- ajout de `tools/validate_chapters.py` et `tools/check_context_markers.py` ;
- validation automatique rétroactive des chapitres 5 et 6 ;
- aucun PDF produit par la validation légère.

### 2026-07-19 — version 3.4.0

- création et audit statique du chapitre 6 ;
- progression à 6 chapitres sur 30.

### 2026-07-19 — version 3.3.0

- création et audit statique du chapitre 5 ;
- politique PDF différée enregistrée.

### 2026-07-18 — versions 3.0.0 à 3.2.0

- plans maîtres détaillés des Livres III à V et du Companion Pack ;
- création des chapitres 3 et 4 ;
- architecture feature-first, `StatusBeacon`, `BeaconProfile`, matrice de dépendances et ADR.
