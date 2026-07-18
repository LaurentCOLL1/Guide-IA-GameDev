---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.3.0"
lang: "fr-FR"
last-updated: "2026-07-19"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les erreurs corrigées, les règles QA et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot.

## 1. Procédure obligatoire lors d’une reprise

Une nouvelle conversation doit :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. lire le plan maître du Livre ou Pack actif ;
4. vérifier les derniers commits et pull requests ;
5. ne pas recréer un chapitre, audit ou choix déjà présent ;
6. identifier le prochain chapitre ;
7. annoncer **GPT-5.6 Sol — Moyenne ou Élevée** et justifier le choix ;
8. comparer le périmètre au plan maître ;
9. rédiger, auditer et corriger ;
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

**En cours : 5 chapitres sur 30.**

#### Partie A — Fondations Godot, architecture et données

1. Découvrir Godot et créer le projet fil rouge — terminé.
2. Fondamentaux de GDScript — terminé, enrichi et audité contre les doublons.
3. Scènes, nœuds, Resources et signaux — terminé au niveau `static-review`.
4. Architecture modulaire du projet — terminé au niveau `static-review`.
5. Services, gestionnaires, bus d’événements et injection de dépendances — terminé au niveau `static-review`.
6. Entrées, contrôleurs, caméras et interactions.
7. Données avec Resources, JSON et configurations.
8. SQLite, migrations et données persistantes.
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

Le détail chapitre par chapitre ou pack par pack se trouve exclusivement dans les quatre plans maîtres. Chaque entrée y possède objectifs, livrables, dépendances, frontières et critères de validation.

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

Chapitres 3, 4 et 5 : **Élevée**.

## 8. Audit par chapitre

Chaque chapitre suit :

1. rédaction ;
2. comparaison au plan maître ;
3. audit de complétude ;
4. explication détaillée du code ;
5. contrôle des doublons ;
6. vérification technique et sources officielles ;
7. contrôle des repères ;
8. correction des omissions ;
9. contrôle des frontières ;
10. mise à jour de la gouvernance ;
11. rapport QA ;
12. statut `static-review` ou `runtime-tested`.

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

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.3.0`.

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
- matrice de dépendances et ADR comme sources de vérité ;
- déplacements Godot effectués depuis le dock FileSystem ;
- services construits par le bootstrap ;
- registre limité au point de composition ;
- bus d’événements typé et limité ;
- un Autoload par nécessité de durée de vie, pas par commodité ;
- démarrage déterministe et arrêt dans l’ordre inverse.

## 12. Chapitre 5 — état détaillé

Fichier :

> **[LECTURE] Chemin de référence — Ne pas saisir.**

```text
Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md
```

Niveau : **GPT-5.6 Sol — Élevée**.

Contenu :

- vocabulaire service, manager, système, controller et repository ;
- critères `Node`, `RefCounted`, `Resource` et Autoload ;
- injection par constructeur, méthode et propriété exportée ;
- `GameEventBus` typé ;
- `ServiceRegistry` minimal ;
- contrat de cycle de vie ;
- `AppBootstrap` comme composition root ;
- démarrage et rollback ;
- arrêt en ordre inverse ;
- exercice `beacons` ;
- doubles de test préparatoires ;
- parcours Solo et Studio.

Livrables documentés :

- `src/app/app_bootstrap.gd` ;
- `src/core/events/game_event_bus.gd` ;
- `src/core/services/service_registry.gd` ;
- `src/core/services/service_lifecycle.gd` ;
- `src/features/beacons/application/beacon_activation_service.gd` ;
- `scenes/learning/ch05_services_demo.gd` ;
- `scenes/learning/ch05_services_demo.tscn` ;
- `docs/architecture/service-catalog.md`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-05.md`.

Résultats : 78 titres, 18 blocs, 18 repères, zéro doublon de titre, bloc significatif ou paragraphe long.

Décision : accepté avec réserve runtime et PDF de fin de Livre.

## 13. Erreurs à ne pas reproduire

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
- ne pas oublier de nettoyer un démarrage partiel ;
- ne pas construire le PDF à chaque chapitre ;
- ne pas oublier la mise à jour de ce fichier.

## 14. État courant

- branche principale : `main` ;
- jalon : M3 — Livre II ;
- progression : 5 chapitres sur 30 ;
- chapitre 2 : version `1.3.0` ;
- chapitre 3 : version `1.0.0` ;
- chapitre 4 : version `1.0.0` ;
- chapitre 5 : version `1.0.0` ;
- Starter Kit non matérialisé ;
- licence globale à définir ;
- accessibilité PDF avancée à traiter avant publication.

## 15. Prochaine action

Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md
```

Périmètre attendu :

- Input Map ;
- actions et événements d’entrée ;
- contrôleur joueur ;
- séparation intention/mouvement ;
- caméra 3D ;
- souris, clavier et manette ;
- interaction par raycast ou zone ;
- injection des services du chapitre 5 ;
- remappage et accessibilité ;
- différences Solo/Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.

## 16. Journal

### 2026-07-19 — version 3.3.0

- création et audit statique du chapitre 5 ;
- adoption du registre limité au bootstrap ;
- adoption du bus d’événements typé ;
- définition du cycle de vie des services ;
- Autoload `AppRuntime` distinct de la classe `AppBootstrap` ;
- progression à 5 chapitres sur 30 ;
- politique PDF différée enregistrée ;
- prochaine action déplacée vers le chapitre 6.

### 2026-07-18 — version 3.2.0

- création du chapitre 4 ;
- architecture feature-first ;
- matrice de dépendances et ADR ;
- `src/app` défini comme point de composition.

### 2026-07-18 — version 3.1.0

- création du chapitre 3 ;
- ajout de `StatusBeacon` et `BeaconProfile` ;
- règle Moyenne/Élevée avant chaque chapitre.

### 2026-07-18 — version 3.0.0

- création des plans maîtres détaillés des Livres III à V et du Companion Pack.
