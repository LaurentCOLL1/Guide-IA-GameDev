---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.1.0"
lang: "fr-FR"
last-updated: "2026-07-18"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les erreurs corrigées, les règles QA et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot de commits ou la même pull request.

## 1. Procédure obligatoire lors d’une reprise

Une nouvelle conversation doit suivre cet ordre :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. lire le plan maître détaillé du Livre ou Pack actif ;
4. vérifier les derniers commits et pull requests fusionnés ;
5. ne pas recréer un chapitre, un audit ou une décision déjà présent ;
6. identifier le prochain chapitre ;
7. annoncer le niveau GPT-5.6 Sol conseillé : **Moyenne** ou **Élevée** ;
8. justifier cette recommandation avant toute rédaction ;
9. comparer le chapitre au plan maître ;
10. effectuer rédaction, audit, compilation et QA ;
11. mettre à jour ce fichier avant de déclarer le lot terminé.

## 2. Sources maîtres obligatoires

Le plan exact de la collection est réparti dans les documents suivants :

- **Livre II :** section dédiée du présent fichier et `Livre-II/index.md` ;
- **Livre III :** [`plans/LIVRE-III-PLAN-MAITRE.md`](plans/LIVRE-III-PLAN-MAITRE.md) ;
- **Livre IV :** [`plans/LIVRE-IV-PLAN-MAITRE.md`](plans/LIVRE-IV-PLAN-MAITRE.md) ;
- **Livre V :** [`plans/LIVRE-V-PLAN-MAITRE.md`](plans/LIVRE-V-PLAN-MAITRE.md) ;
- **Companion Pack :** [`plans/COMPANION-PACK-PLAN-MAITRE.md`](plans/COMPANION-PACK-PLAN-MAITRE.md).

Un titre, un ordre ou un périmètre ne doit pas être modifié silencieusement. Toute modification du plan maître exige une décision explicite, une justification et une mise à jour de la roadmap.

## 3. Vision du projet

Laurent Collin souhaite produire un guide français très complet permettant à un débutant de concevoir et développer un jeu vidéo 3D réaliste avec :

- Godot et GDScript ;
- Blender ;
- Python, JSON, SQLite et mémoire vectorielle ;
- IA locale pour textes, images, voix, sons et musiques ;
- outils gratuits, locaux et majoritairement open source ;
- procédures adaptées à Windows et à un GPU AMD ;
- parcours Solo et Studio ;
- projet fil rouge `Project Asteria` ;
- Volume 0, cinq Livres et Companion Pack.

Le guide doit toujours expliquer :

- quel programme ouvrir ;
- où exécuter une commande ;
- où créer ou modifier un fichier ;
- la signification des fonctions, paramètres, types, opérateurs et valeurs ;
- le résultat attendu ;
- la procédure de vérification et de correction ;
- les dépendances avec les chapitres voisins ;
- le niveau Obligatoire, Recommandé ou Optionnel ;
- les différences Solo/Studio.

## 4. Configuration matérielle de référence

- Système : Windows.
- GPU : AMD Radeon RX 6750 XT, 12 Go de VRAM, RDNA2.
- CPU : AMD Ryzen 7 2700, 8 cœurs, 3,2 GHz.
- RAM : 32 Go.
- Éditeur : Visual Studio Code.
- Terminal principal : PowerShell 7.
- ComfyUI : natif Windows, ZLUDA expérimental lorsque pertinent.
- Docker Desktop : services CPU et interfaces ; charges GPU AMD principalement natives.

## 5. État de la collection

### Volume 0 — Fondation documentaire

**Statut : terminé et audité.**

Chapitres :

1. Vision générale du projet.
2. Les 21 règles fondamentales.
3. Architecture documentaire.
4. Convention des identifiants.
5. Conventions Markdown et Pandoc.
6. Style rédactionnel.
7. Standards techniques.
8. Standards IA.
9. Politique de compatibilité.
10. Production, validation et publication.
11. Glossaire, bibliographie et index.

Documents importants :

- `Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md` ;
- `Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md` ;
- `Volume-0/QA/VALIDATION-FINALE-V0-L1.yaml`.

### Livre I — Préparer la plateforme de développement IA

**Statut : terminé, repéré et audité.**

1. Matériel, Windows, pilotes AMD et accélération locale.
2. Terminal, PowerShell et outils Windows.
3. Git, GitHub et Visual Studio Code.
4. Python et environnements virtuels.
5. Docker et Docker Compose.
6. Open WebUI, Open Terminal et Vane.
7. ComfyUI et workflows graphiques.
8. LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat.
9. Audio IA local : voix, transcription, musique et effets.
10. Sécurité, sauvegarde et validation de la plateforme.

Décision historique : le Livre I avait été condensé en six chapitres. Quatre chapitres de fondation ont été ajoutés après audit. Les identifiants historiques déplacés ont été conservés.

### Livre II — Développement du jeu et plateforme IA

**Statut : en cours — 3 chapitres sur 30 rédigés, repérés et audités au niveau documentaire et statique.**

#### Partie A — Fondations Godot, architecture et données

1. Découvrir Godot et créer le projet fil rouge — **terminé**.
2. Fondamentaux de GDScript — **terminé, enrichi et audité contre les doublons**.
3. Scènes, nœuds, Resources et signaux — **terminé au niveau static-review**.
4. Architecture modulaire du projet.
5. Services, gestionnaires, bus d’événements et injection de dépendances.
6. Entrées, contrôleurs, caméras et interactions.
7. Données avec Resources, JSON et configurations.
8. SQLite, migrations et données persistantes.
9. Sauvegardes, chargements et compatibilité des versions.

#### Partie B — Plateforme IA locale intégrée au jeu

10. Mémoire vectorielle, connaissances et recherche sémantique.
11. Communication Godot avec les services IA locaux.
12. HTTP, WebSocket, API OpenAI-compatible et files de tâches.
13. Sécurité et séparation production/runtime de l’IA.

#### Partie C — Douze grands systèmes de gameplay

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

### Chapitre 3 — état détaillé

Fichier :

```text
Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md
```

Niveau recommandé annoncé avant rédaction : **GPT-5.6 Sol — Élevée**.

Le chapitre couvre :

- nœuds, scènes, instances, branches et `SceneTree` ;
- parent et propriété `owner` ;
- composition et `PackedScene.instantiate()` ;
- `NodePath`, `get_node()`, `$`, `%NomUnique` et `get_node_or_null()` ;
- références typées et `@onready` ;
- `_init()`, `_enter_tree()`, `_ready()` et `_exit_tree()` ;
- signaux intégrés et personnalisés ;
- `Callable`, `connect()`, `emit()`, `is_connected()` et `disconnect()` ;
- Resources personnalisées, partage et `resource_local_to_scene` ;
- exercice `StatusBeacon` et `BeaconProfile` ;
- validation graphique et headless ;
- diagnostics, modes Solo/Studio et critères d’acceptation.

Frontières conservées :

- architecture modulaire au chapitre 4 ;
- services globaux et bus d’événements au chapitre 5 ;
- interactions complètes au chapitre 6 ;
- stratégie des données au chapitre 7.

Rapport : `Livre-II/QA/AUDIT-CHAPITRE-03.md`.

Réserve : les fichiers de l’exercice ne sont pas encore matérialisés dans le Starter Kit ; le statut reste `static-review` jusqu’aux tests runtime.

### Livre III — Production des contenus et des assets

**Statut : non commencé — 30 chapitres.**

Source obligatoire : [`plans/LIVRE-III-PLAN-MAITRE.md`](plans/LIVRE-III-PLAN-MAITRE.md).

### Livre IV — Finalisation, optimisation, publication et maintenance

**Statut : non commencé — 22 chapitres.**

Source obligatoire : [`plans/LIVRE-IV-PLAN-MAITRE.md`](plans/LIVRE-IV-PLAN-MAITRE.md).

### Livre V — Encyclopédie technique et bibliothèque de référence

**Statut : non commencé — 26 chapitres.**

Source obligatoire : [`plans/LIVRE-V-PLAN-MAITRE.md`](plans/LIVRE-V-PLAN-MAITRE.md).

### Companion Pack

**Statut : non commencé — 10 packs.**

Source obligatoire : [`plans/COMPANION-PACK-PLAN-MAITRE.md`](plans/COMPANION-PACK-PLAN-MAITRE.md).

Packs : Starter Kit, Project Templates, AI Library, Code Library, Database Library, ComfyUI Library, Documentation Library, Test & Benchmark Library, Production Toolkit et Knowledge Base.

## 6. Règle du niveau GPT-5.6 Sol

Avant chaque nouveau chapitre, indiquer :

```text
Chapitre à produire : …
Niveau GPT-5.6 Sol recommandé : Moyenne / Élevée
Justification : …
```

Choisir généralement :

- **Moyenne** pour un chapitre descriptif, linéaire, avec peu de code ou de dépendances ;
- **Élevée** pour architecture, code imbriqué, données, IA, sécurité, optimisation, intégrations ou nombreuses frontières.

Enregistrer la recommandation dans le chapitre :

```yaml
recommended-reasoning: "GPT-5.6 Sol — Élevée"
```

## 7. Repères obligatoires d’utilisation

| Repère | Contexte |
|---|---|
| `[PS]` | PowerShell 7 sur Windows |
| `[CMD]` | Invite de commandes Windows |
| `[WSL]` | Terminal WSL/Bash |
| `[DCT]` | Terminal dans un conteneur Docker |
| `[DCK]` | Interface Docker Desktop |
| `[VSC]` | Visual Studio Code |
| `[WEB]` | Navigateur internet |
| `[APP]` | Interface graphique du logiciel nommé |
| `[SORTIE]` | Résultat à lire, ne pas saisir |
| `[LECTURE]` | Exemple ou structure de référence |

Forme obligatoire :

```text
[CODE] Outil - Action : chemin, cible ou précision utile
```

## 8. Audit obligatoire après chaque chapitre

Aucun chapitre n’est terminé immédiatement après sa rédaction.

Séquence :

1. recommandation du niveau GPT-5.6 Sol ;
2. rédaction ;
3. comparaison au plan maître ;
4. audit de complétude pédagogique ;
5. contrôle des doublons ;
6. vérification technique ;
7. ajout des contextes d’utilisation ;
8. correction des omissions ;
9. contrôle des frontières avec les chapitres voisins ;
10. mise à jour de `contents.txt`, index, roadmap et continuité ;
11. compilation Pandoc/XeLaTeX ;
12. inspection du PDF ;
13. rapport QA et preuve indépendante ;
14. seulement ensuite : statut rédigé, repéré et audité.

Métadonnées minimales :

```yaml
status: "reviewed"
audit-status: "complete"
audit-date: "YYYY-MM-DD"
audit-level: "static-review"
audit-report: "chemin/du/rapport.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"
```

`runtime-tested` est réservé aux exemples réellement exécutés.

## 9. Règle pédagogique pour le code

Lors de la première apparition d’un concept, expliquer :

- mot-clé ;
- nom de variable ou fonction ;
- type ;
- opérateur ;
- paramètre et argument ;
- valeur par défaut ;
- valeur et type de retour ;
- portée ;
- accès par index ou clé ;
- appel de méthode ;
- résultat concret.

Les rappels courts sont autorisés. Les duplications intégrales involontaires de titres, paragraphes longs et blocs significatifs sont interdites.

## 10. Audits importants

### Chapitre 2 GDScript

Campagne de référence : PR n°11, commit métier `e40da615bdc922f0296ef34f51dc6e226f0782dd`.

Résultats enregistrés : 152 titres, 57 blocs significatifs et 22 paragraphes longs contrôlés ; zéro doublon et zéro explication obligatoire manquante.

### Chapitre 3

Audit : `Livre-II/QA/AUDIT-CHAPITRE-03.md`.

Points contrôlés : périmètre, cycle de vie, ownership, références de nœuds, instanciation, Resources, signaux, Callables, contextes, doublons et commandes headless.

Décision avant CI : accepté avec réserve CI et runtime. La preuve finale doit être complétée après les workflows.

## 11. Décisions techniques permanentes

### Windows et AMD

- Windows-first pour la configuration de référence.
- CPU toujours disponible comme voie de diagnostic.
- ZLUDA et autres voies expérimentales isolées et qualifiées.
- Docker Desktop n’est pas présenté comme solution GPU AMD universelle.

### ComfyUI

- installation manuelle de référence ;
- CPU comme voie de secours ;
- ZLUDA comme laboratoire expérimental ;
- workflows, modèles, licences, versions et empreintes enregistrés.

### LLM locaux

- Ollama natif Windows pour le parcours simple ;
- llama.cpp CPU/Vulkan pour référence et mesures ;
- LocalAI optionnel ;
- LibreChat comme interface alternative ;
- services liés à `127.0.0.1` par défaut.

### Audio

- Kokoro et Piper pour les voix légères ;
- Chatterbox pour voix expressive et clonage autorisé ;
- faster-whisper et whisper.cpp pour transcription ;
- AudioCraft limité aux usages compatibles avec les licences ;
- aucun clonage sans consentement.

## 12. Erreurs à ne pas reproduire

- Ne pas déclarer un Livre complet uniquement parce que ses grands domaines sont couverts.
- Ne pas condenser les fondations débutantes en simples prérequis.
- Ne pas donner une commande sans terminal.
- Ne pas donner un contenu de fichier sans éditeur et chemin.
- Ne pas présenter une sortie comme une commande.
- Ne pas revendiquer une exécution runtime non réalisée.
- Ne pas conserver de workflow temporaire dans `main`.
- Ne pas publier des mesures intermédiaires comme preuves finales.
- Ne pas laisser fonction, paramètre, opérateur ou type sans explication suffisante.
- Ne pas dupliquer une explication complète ; utiliser rappel et renvoi.
- Ne pas modifier le plan maître sans décision explicite.
- Ne pas oublier l’annonce Moyenne/Élevée avant un chapitre.
- Ne pas oublier la mise à jour de ce fichier.

## 13. État courant

- Branche principale cible : `main`.
- Jalon actif : M3 — Livre II.
- Livre II : 3 chapitres sur 30 rédigés, repérés et audités statiquement.
- Chapitre 2 : version `1.3.0`, audité contre les doublons.
- Chapitre 3 : version `1.0.0`, recommandation Élevée, audit statique créé.
- Licence globale : à définir.
- Accessibilité PDF avancée : à traiter avant publication.
- Tests runtime de `Project Asteria` : en attente du Starter Kit matérialisé.

## 14. Prochaine action

Avant toute rédaction, annoncer le niveau conseillé pour :

```text
Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md
```

Le chapitre 4 devra notamment :

- définir les couches et dossiers du projet ;
- séparer domaine, présentation, données, infrastructure et outils ;
- organiser les fonctionnalités par modules ;
- définir les dépendances autorisées ;
- expliquer composition, contrats et interfaces implicites ;
- éviter scènes monolithiques et singletons omniprésents ;
- produire l’arborescence canonique ;
- produire une matrice des dépendances ;
- créer les premières ADR ;
- proposer variantes Solo et Studio ;
- réutiliser les scènes, Resources et signaux du chapitre 3 sans les dupliquer ;
- réussir audit, contextes, doublons, compilation et inspection PDF.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier au début de la prochaine conversation ou du prochain lot.

## 15. Journal de continuité

### 2026-07-18 — version 3.1.0

- création et audit statique du chapitre 3 ;
- ajout de `StatusBeacon` et `BeaconProfile` comme exercice documentaire ;
- ajout de la règle obligatoire Moyenne/Élevée avant chaque chapitre ;
- passage du Livre II à 3 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 4.

### 2026-07-18 — version 3.0.0

- création des quatre plans maîtres détaillés séparés ;
- transformation du fichier en index de reprise obligatoire.
