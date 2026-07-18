---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "2.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier résume les décisions, l’historique, l’état du dépôt, les règles permanentes, le plan maître complet de la collection et la prochaine action. Il doit permettre de reprendre le projet dans une nouvelle conversation sans recommencer la conception depuis zéro.

> **Règle obligatoire :** toute modification fonctionnelle, documentaire, structurelle, éditoriale, technique ou QA du projet doit mettre à jour ce fichier dans le même lot de commits ou la même pull request.

## 1. Mode d’emploi lors d’une reprise

Lorsqu’une nouvelle conversation commence :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. vérifier les derniers commits et pull requests fusionnés ;
4. ne pas recréer un chapitre, une décision ou un audit déjà présent ;
5. comparer la prochaine action au **plan maître détaillé** du présent fichier ;
6. continuer depuis la section **Prochaine action** ;
7. actualiser ce fichier avant de déclarer le nouveau lot terminé.

Ce document est un résumé opérationnel exhaustif de la conversation. Il ne reproduit pas mot pour mot tous les dialogues, mais conserve les informations, décisions, contraintes, plans et erreurs corrigées nécessaires pour poursuivre le travail fidèlement.

## 2. Demande et vision du projet

Laurent Collin souhaite produire un guide français très complet permettant à un débutant de concevoir et développer un jeu vidéo 3D réaliste avec :

- Godot et GDScript ;
- Blender ;
- Python, JSON, SQLite et mémoire vectorielle ;
- IA locale pour les textes, images, voix, sons et musiques ;
- outils gratuits, locaux et majoritairement open source ;
- procédures reproductibles et adaptées à une station Windows avec GPU AMD ;
- deux parcours : développeur Solo et équipe/Studio ;
- un projet fil rouge nommé `Project Asteria` ;
- une collection comprenant un Volume 0, cinq Livres et un Companion Pack.

Le guide ne doit pas seulement donner des commandes ou du code. Il doit expliquer clairement :

- quel programme ouvrir ;
- où créer ou modifier un fichier ;
- où exécuter une commande ;
- ce que signifie chaque élément important du code ;
- le résultat attendu ;
- comment vérifier et corriger les erreurs ;
- comment les choix du chapitre s’intègrent dans l’architecture générale ;
- quelles parties sont obligatoires, recommandées ou optionnelles ;
- quelles différences existent entre le parcours Solo et le parcours Studio.

## 3. Configuration matérielle de référence

- Système : Windows.
- GPU : AMD Radeon RX 6750 XT, 12 Go de VRAM, architecture RDNA2.
- CPU : AMD Ryzen 7 2700, 8 cœurs, 3,2 GHz.
- RAM : 32 Go.
- ComfyUI : installation Windows avec voie ZLUDA expérimentale lorsque pertinente.
- Docker Desktop : utilisé pour les services CPU et les interfaces ; les charges GPU AMD restent principalement natives sur Windows.
- Éditeur principal : Visual Studio Code.
- Terminal Windows principal : PowerShell 7.

## 4. Architecture générale de la collection

### Volume 0 — Fondation documentaire

Terminé et audité. Il contient :

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

Annexes et QA importantes :

- `Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md` ;
- `Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md` ;
- `Volume-0/QA/VALIDATION-FINALE-V0-L1.yaml`.

### Livre I — Préparer la plateforme de développement IA

Terminé, corrigé, repéré et audité avec dix chapitres :

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

Décision historique importante : le Livre I avait d’abord été condensé en six chapitres. Après vérification du plan initial, quatre chapitres de fondation ont été ajoutés. Les cinq chapitres historiques déplacés ont conservé leurs identifiants stables grâce aux métadonnées de migration.

## 5. Plan maître détaillé — Livre II

**Titre : Développement du jeu et plateforme IA**  
**Statut : en cours**  
**Total prévu : 30 chapitres**

Le Livre II construit le projet exécutable `Project Asteria`. Il ne doit pas devenir une simple encyclopédie de GDScript : chaque chapitre doit produire une partie utilisable du projet fil rouge.

### Partie A — Fondations Godot, architecture et données

#### Chapitre 1 — Découvrir Godot et créer le projet fil rouge

Objectifs :

- installer et identifier la version de référence de Godot ;
- comprendre le Project Manager, le renderer et les éditions Standard/.NET ;
- créer le dépôt et la structure initiale de `Project Asteria` ;
- créer une première scène exécutable ;
- valider l’exécution graphique et headless ;
- établir les premiers fichiers Git, README et référence d’environnement.

État : **rédigé, repéré et audité**.

#### Chapitre 2 — Fondamentaux de GDScript

Objectifs :

- expliquer syntaxe, indentation, types, variables, constantes et expressions ;
- détailler tableaux, dictionnaires, conditions, boucles et fonctions ;
- expliquer paramètres, arguments, retours, portée, classes et annotations ;
- expliquer chaque symbole important à sa première apparition ;
- produire et tester statiquement `BootstrapReport` ;
- contrôler les doublons pédagogiques.

État : **rédigé, repéré, enrichi et audité**, version actuelle `1.3.0`.

#### Chapitre 3 — Scènes, nœuds, Resources et signaux

Objectifs :

- distinguer scène, nœud, branche et instance ;
- comprendre l’arbre de scène et la propriété des nœuds ;
- instancier, réutiliser et composer des scènes ;
- utiliser `NodePath`, `$`, `%NomUnique`, `get_node()` et références typées ;
- expliquer les signaux intégrés et personnalisés ;
- connecter un signal dans l’éditeur et dans le code ;
- utiliser `Callable`, `emit()`, `connect()` et déconnexion ;
- introduire les Resources natives et personnalisées ;
- expliquer l’ordre d’initialisation, `_enter_tree()`, `_ready()` et sortie de l’arbre ;
- produire un exercice intégré à `Project Asteria`.

Frontière : ne pas définir encore l’architecture globale des services ; elle appartient aux chapitres 4 et 5.

#### Chapitre 4 — Architecture modulaire du projet

Objectifs :

- définir les couches et dossiers du projet ;
- séparer domaine, présentation, données, infrastructure et outils ;
- organiser les fonctionnalités par modules ;
- définir les dépendances autorisées ;
- expliquer composition, interfaces implicites et contrats ;
- éviter les singletons omniprésents et les scènes monolithiques ;
- créer un diagramme d’architecture de `Project Asteria` ;
- établir les conventions de nommage, ownership et frontières.

Livrables : arborescence canonique, ADR initiales, règles d’import et matrice des dépendances.

#### Chapitre 5 — Services, gestionnaires, bus d’événements et injection de dépendances

Objectifs :

- distinguer service, manager, repository, controller et système ;
- expliquer Autoload et ses risques ;
- créer un registre de services minimal ;
- injecter les dépendances plutôt que les rechercher globalement ;
- définir un bus d’événements limité et typé ;
- gérer initialisation, arrêt, erreurs et tests ;
- proposer variantes Solo et Studio.

Frontière : les signaux locaux restent au chapitre 3 ; ce chapitre traite l’échelle application.

#### Chapitre 6 — Entrées, contrôleurs, caméras et interactions

Objectifs :

- configurer l’Input Map ;
- distinguer actions, événements, périphériques et remappage ;
- créer contrôleur clavier/souris/manette ;
- séparer intention du joueur et mouvement ;
- créer caméra 3D, rig, rotation, zoom et collisions ;
- mettre en place raycasts, zones et interactions contextuelles ;
- gérer focus UI, accessibilité et rebinding ;
- tester les entrées sans dépendre du matériel exact.

#### Chapitre 7 — Données avec Resources, JSON et configurations

Objectifs :

- choisir entre constantes, Resources, JSON et scènes ;
- créer des Resources personnalisées éditables ;
- sérialiser et valider JSON ;
- définir schémas, valeurs par défaut et migrations simples ;
- séparer données de conception et état runtime ;
- organiser catalogues, identifiants et localisation ;
- gérer erreurs, provenance et versionnement.

#### Chapitre 8 — SQLite, migrations et données persistantes

Objectifs :

- expliquer base relationnelle, table, clé, index et transaction ;
- intégrer SQLite à Godot avec une solution vérifiée ;
- concevoir schémas et conventions ;
- créer migrations versionnées ;
- gérer requêtes préparées, transactions et sauvegardes ;
- séparer base de contenu, sauvegarde et cache ;
- fournir procédures de restauration et tests.

#### Chapitre 9 — Sauvegardes, chargements et compatibilité des versions

Objectifs :

- définir ce qui doit être sauvegardé ;
- choisir entre JSON, Resources binaires et SQLite ;
- créer slots, autosave, métadonnées et captures ;
- garantir atomicité, validation et reprise après corruption ;
- migrer les anciennes sauvegardes ;
- gérer déterminisme, références et identifiants stables ;
- tester compatibilité ascendante et retour arrière.

### Partie B — Plateforme IA locale intégrée au jeu

#### Chapitre 10 — Mémoire vectorielle, connaissances et recherche sémantique

Objectifs :

- expliquer embeddings, vecteurs, distance et recherche ;
- choisir une base vectorielle locale ;
- découper, indexer et versionner les connaissances ;
- séparer mémoire de jeu, lore, historique et documents ;
- filtrer par métadonnées ;
- mesurer rappel, précision et coût ;
- gérer suppression, réindexation et confidentialité.

#### Chapitre 11 — Communication Godot avec les services IA locaux

Objectifs :

- utiliser `HTTPRequest` et clients réseau ;
- envoyer et recevoir JSON ;
- gérer délais, annulation, retries et erreurs ;
- protéger les secrets ;
- connecter Ollama, Open WebUI ou passerelles compatibles ;
- créer une couche d’abstraction IA indépendante d’un fournisseur ;
- journaliser requêtes, réponses et latences.

#### Chapitre 12 — HTTP, WebSocket, API OpenAI-compatible et files de tâches

Objectifs :

- choisir HTTP synchrone, streaming ou WebSocket ;
- expliquer SSE et tokens diffusés progressivement ;
- créer files de tâches et priorités ;
- éviter de bloquer la boucle principale ;
- gérer concurrence, quotas, cache et reprise ;
- fournir contrats OpenAI-compatible ;
- tester avec services simulés.

#### Chapitre 13 — Sécurité et séparation production/runtime de l’IA

Objectifs :

- distinguer IA de production d’assets et IA embarquée ;
- définir sandbox, permissions et validation des sorties ;
- prévenir injection de prompt et données non fiables ;
- limiter réseau, fichiers et commandes ;
- traiter données personnelles, voix et journaux ;
- définir modes hors ligne et dégradés ;
- créer une matrice de menace et un plan d’incident.

### Partie C — Les douze grands systèmes de gameplay

Chaque système doit être modulaire, testable, sérialisable, observable et compatible avec les autres systèmes sans dépendances circulaires.

#### Chapitre 14 — Personnages

- identité, apparence, attributs, besoins et état ;
- composants, données et représentation en scène ;
- création, destruction, pooling et persistance ;
- avatars joueur et non-joueur ;
- blessures, mortalité et transformations.

#### Chapitre 15 — Relations sociales

- relations directionnelles ;
- affinité, confiance, peur, dette et mémoire ;
- événements sociaux et propagation ;
- dialogues et conséquences ;
- visualisation, sauvegarde et équilibrage.

#### Chapitre 16 — Famille et générations

- parenté, unions, descendance et foyers ;
- âge, naissance, héritage et décès ;
- généalogie et identifiants durables ;
- transmission de traits et biens ;
- simulation hors écran.

#### Chapitre 17 — Agents IA et comportements autonomes

- machines à états, behavior trees, utility AI et planification ;
- perception, mémoire, objectifs et actions ;
- navigation et évitement ;
- budgets de simulation et LOD comportemental ;
- intégration optionnelle des LLM sans dépendance critique.

#### Chapitre 18 — Combat

- modèle de dégâts, défense et résistances ;
- ciblage, portée, hitboxes et projectiles ;
- temps réel, pause tactique et tours éventuels ;
- effets, statuts et contrôle de foule ;
- journal de combat, IA et tests déterministes.

#### Chapitre 19 — Compétences et pouvoirs

- définition data-driven ;
- coûts, cooldowns, conditions et effets ;
- progression, arbres et synergies ;
- ciblage et prévisualisation ;
- validation et équilibrage automatisé.

#### Chapitre 20 — Inventaire et réputation des objets

- piles, emplacements, poids, conteneurs et équipements ;
- objets uniques, durabilité et provenance ;
- réputation, histoire et propriété ;
- transactions atomiques ;
- sauvegarde et UI.

#### Chapitre 21 — Économie

- monnaies, prix, offre et demande ;
- production, consommation et marchés ;
- métiers, salaires, taxes et commerce ;
- prévention des boucles infinies ;
- télémétrie et équilibrage.

#### Chapitre 22 — Monde vivant et simulation écologique

- temps, météo, saisons et cycles ;
- populations, ressources et chaînes alimentaires ;
- croissance, régénération et catastrophes ;
- simulation active et hors écran ;
- déterminisme, performances et sauvegarde.

#### Chapitre 23 — Politique, factions et justice

- factions, rangs, idéologies et territoires ;
- lois, crimes, preuves et sanctions ;
- élections, nominations et conflits ;
- diplomatie, réputation et guerre ;
- événements émergents et auditabilité.

#### Chapitre 24 — Construction et gestion de domaines

- placement, grille, terrain et validation ;
- bâtiments modulaires et ressources ;
- propriété, zones, travailleurs et production ;
- sauvegarde, destruction et amélioration ;
- outils d’édition et performances.

#### Chapitre 25 — Narration, quêtes, codex et connaissances

- événements, conditions et conséquences ;
- quêtes data-driven et graphes ;
- journal, objectifs et récompenses ;
- codex, lore, découverte et contradictions ;
- narration procédurale et assistance IA contrôlée.

### Partie D — Industrialisation du projet

#### Chapitre 26 — Outils d’édition internes et pipelines de contenu

- plugins Godot et outils `@tool` ;
- inspecteurs personnalisés ;
- import, validation et génération en lots ;
- formulaires de données ;
- sécurité des outils d’éditeur.

#### Chapitre 27 — Tests unitaires, tests d’intégration et simulations

- stratégie de test ;
- tests de fonctions, scènes, données et systèmes ;
- doublures, fixtures et seeds ;
- simulations accélérées ;
- couverture utile et non cosmétique.

#### Chapitre 28 — Journalisation, diagnostic et reproductibilité

- niveaux de logs et catégories ;
- traces structurées ;
- rapports de crash ;
- captures d’état ;
- identifiants de session, version et seed ;
- procédures de reproduction.

#### Chapitre 29 — Automatisation Python et génération de données

- rôle de Python hors runtime Godot ;
- scripts de conversion, génération et validation ;
- CLI, arguments et fichiers de configuration ;
- intégration CI ;
- déterminisme et provenance ;
- limites entre Python et GDScript.

#### Chapitre 30 — Architecture Solo et architecture Studio

- comparaison des deux parcours ;
- responsabilités, branches et revues ;
- gestion des assets et données ;
- environnements, CI/CD et permissions ;
- montée en charge du projet ;
- checklist de fin du Livre II.

## 6. Plan maître détaillé — Livre III

**Titre : Production des contenus et des assets**  
**Statut : non commencé**  
**Total prévu : 30 chapitres**

Le Livre III transforme la direction artistique en assets utilisables. Chaque chapitre doit inclure provenance, licences, conventions de fichiers, budgets techniques, import Godot et validation.

1. **Préproduction et cahier des charges artistique** — objectifs, contraintes, références, budgets, calendrier et critères d’acceptation.
2. **Direction artistique et bible visuelle** — formes, couleurs, matériaux, lumière, réalisme, cohérence et variantes.
3. **Références, concept art et ComfyUI** — collecte légale, moodboards, workflows, seeds, métadonnées et sélection humaine.
4. **Pipeline Blender et organisation des fichiers** — unités, axes, collections, nommage, versions, liens et exports.
5. **Provenance, licences et validation des assets** — sources, consentements, restrictions, empreintes et registre.
6. **Création des humains** — proportions, anatomie, diversité, modularité et optimisation.
7. **Création des humanoïdes** — adaptations anatomiques, silhouettes et compatibilité des rigs.
8. **Création des animaux** — anatomie, locomotion, pelage/plumes et variantes.
9. **Création des créatures** — conception crédible, besoins de gameplay, rig et lisibilité.
10. **Visages, peau, yeux, cheveux et pilosité** — shaders, textures, groom, expressions et performances.
11. **Vêtements, armures et accessoires** — couches, simulation, clipping, variantes et modularité.
12. **Objets, équipements et armes** — échelle, prise en main, états, collisions et LOD.
13. **Architecture, bâtiments et kits modulaires** — métriques, snapping, modularité, intérieurs et destruction.
14. **Terrains, paysages et mondes ouverts** — heightmaps, streaming, routes, eau et optimisation.
15. **Végétation et biomes** — espèces, distribution, saisons, imposteurs et interactions.
16. **Textures, matériaux et pipeline PBR** — maps, espaces colorimétriques, texel density et bibliothèques.
17. **UV, retopologie et baking** — topologie, dépliage, cages, normales et contrôle qualité.
18. **LOD, imposteurs et optimisation géométrique** — seuils, transitions, budgets et mesure.
19. **Rigging et skinning** — squelettes, contraintes, poids, déformations et nomenclature.
20. **Animation procédurale et animation par keyframes** — poses, courbes, blend trees et couches.
21. **Capture de mouvement et retargeting** — nettoyage, mapping, licences et correction manuelle.
22. **Cinématiques, caméras et mise en scène** — storyboard, timelines, focales, montage et export.
23. **Effets visuels, particules et simulations** — feu, fumée, magie, météo, collisions et budgets.
24. **Interface utilisateur** — composants, thèmes, icônes, responsive et intégration.
25. **Expérience utilisateur et accessibilité visuelle** — lisibilité, daltonisme, tailles, feedback et navigation.
26. **Voix, bruitages, ambiances et musique** — enregistrement, génération, montage, mixage, licences et intégration.
27. **Synchronisation labiale et animation faciale** — phonèmes, blendshapes, audio et performances.
28. **Importation et intégration dans Godot** — presets, matériaux, animations, collisions et scènes importées.
29. **Validation technique et artistique des assets** — checklists, tests, comparaison à la bible et revue.
30. **Automatisation Blender, ComfyUI et production en lots** — scripts, queues, manifestes, reproductibilité et reprise.

## 7. Plan maître détaillé — Livre IV

**Titre : Finalisation, optimisation, publication et maintenance**  
**Statut : non commencé**  
**Total prévu : 22 chapitres**

1. **Équilibrage et télémétrie locale** — métriques, simulations, courbes, confidentialité et décisions.
2. **Stratégie générale d’assurance qualité** — niveaux de test, responsabilités, critères et calendrier.
3. **Tests fonctionnels et tests de régression** — cas, suites, automatisation et non-régression.
4. **Débogage et reproduction des anomalies** — rapports, étapes, environnements et priorisation.
5. **Journalisation et observabilité locale** — logs, métriques, traces et tableaux de bord.
6. **Profilage CPU** — profiler Godot, scripts, physique, threads et budgets.
7. **Profilage GPU et optimisation du rendu** — passes, shaders, overdraw, lumière et VRAM.
8. **Optimisation RAM, VRAM et allocations** — ressources, caches, fuites et fragmentation.
9. **Chargements, streaming et gestion des ressources** — préchargement, arrière-plan, transitions et monde ouvert.
10. **Optimisation des scènes, scripts et systèmes de jeu** — fréquences, LOD logique, pooling et découpage.
11. **Architecture multijoueur** — modèle réseau, sessions, lobby et topologie.
12. **Synchronisation, autorité et prédiction** — réplication, interpolation, rollback et triche.
13. **Serveurs dédiés et sécurité réseau** — déploiement, durcissement, supervision et incidents.
14. **DevOps et intégration continue** — builds, tests, artefacts, versions et secrets.
15. **Sauvegardes, migrations et reprise après incident** — données joueurs, serveurs et procédures.
16. **Exports Godot et packaging** — presets, signatures, dépendances et formats.
17. **Publication et distribution** — boutiques, pages, builds, conformité et lancement.
18. **Accessibilité** — moteur, commandes, audio, visuel, cognition et tests utilisateurs.
19. **Localisation et internationalisation** — chaînes, pluriels, formats, polices, voix et QA linguistique.
20. **Correctifs, mises à jour et retour arrière** — patching, compatibilité, canaux et rollback.
21. **Modding et contenu communautaire** — API, sandbox, formats, licences et modération.
22. **Maintenance, archivage et pérennité** — dépendances, sources, reproductibilité, conservation et succession.

## 8. Plan maître détaillé — Livre V

**Titre : Encyclopédie technique et bibliothèque de référence**  
**Statut : non commencé**  
**Total prévu : 26 chapitres**

Le Livre V est non linéaire. Il consolide les connaissances sans dupliquer les tutoriels complets des Livres I à IV.

1. Carte générale de la collection.
2. Arbres de décision.
3. Fiches des logiciels et outils.
4. Fiches des moteurs et backends IA.
5. Fiches des modèles de langage.
6. Fiches des modèles visuels.
7. Fiches des modèles audio.
8. Bibliothèque de workflows.
9. Bibliothèque de prompts.
10. Bibliothèque de scripts et recettes de code.
11. Référence GDScript.
12. Référence Python.
13. Structures JSON et formats d’échange.
14. Schémas SQLite et migrations.
15. Bases vectorielles et recherche sémantique.
16. Patrons d’architecture.
17. Patrons de gameplay.
18. Référence graphique et 3D.
19. Référence audio.
20. Catalogue des erreurs et diagnostics.
21. Benchmarks et méthodes de mesure.
22. Matrices de compatibilité.
23. Comparatifs des solutions.
24. Checklists de production et de publication.
25. Licences, provenance et conformité.
26. Index croisés.

Chaque fiche doit inclure : identifiant, objectif, prérequis, version vérifiée, statut de licence, compatibilité matérielle, procédure minimale, erreurs fréquentes, alternatives, sources et date de révision.

## 9. Plan maître détaillé — Companion Pack

**Statut : non commencé**  
**Organisation prévue : 10 packs**

### Pack 1 — Starter Kit

Projet Godot minimal fonctionnel, structure canonique, scène de bootstrap, configuration Git, profils d’environnement et exemple de test.

### Pack 2 — Project Templates

Modèles Solo et Studio, modules, conventions de dossiers, ADR, issues, pull requests et configurations d’éditeur.

### Pack 3 — AI Library

Clients HTTP/WebSocket, contrats OpenAI-compatible, adaptateurs Ollama/LocalAI, files de tâches, cache, mocks et protections.

### Pack 4 — Code Library

Composants GDScript réutilisables, utilitaires Python, patrons, exemples documentés et tests.

### Pack 5 — Database Library

Schémas SQLite, migrations, repositories, données d’exemple, scripts de sauvegarde et validation.

### Pack 6 — ComfyUI Library

Workflows JSON, manifestes, presets, modèles de dossiers, scripts de lancement et fiches de provenance.

### Pack 7 — Documentation Library

Templates Markdown, front matter, rapports QA, ADR, checklists, glossaires et modèles de fiches.

### Pack 8 — Test & Benchmark Library

Suites de tests, fixtures, seeds, scènes de benchmark, scripts de mesure et formats de rapport.

### Pack 9 — Production Toolkit

Scripts Blender, convertisseurs, validateurs d’assets, générateurs de catalogues, outils de lots et packaging.

### Pack 10 — Knowledge Base

Lore, exemples de codex, corpus de test, documents RAG, métadonnées, embeddings reproductibles et outils d’indexation.

Règles du Companion Pack :

- chaque ressource doit être directement réutilisable ;
- chaque fichier doit avoir licence, provenance et version ;
- chaque outil doit avoir un README et un exemple minimal ;
- les packs doivent être testés séparément du guide ;
- aucun secret ni modèle tiers non redistribuable ne doit être inclus ;
- les versions binaires lourdes doivent être publiées comme artefacts ou releases, pas intégrées sans contrôle au dépôt principal.

## 10. Système obligatoire des contextes d’utilisation

Chaque bloc de commande, code, configuration, sortie ou structure doit indiquer le programme et l’action à effectuer.

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

Forme attendue :

```text
[CODE] Outil - Action : chemin, cible ou précision utile
```

La CI contrôle la présence et la cohérence sémantique de ces repères.

## 11. Règle permanente d’audit après création

Aucun chapitre ne doit être déclaré terminé immédiatement après sa rédaction.

Séquence obligatoire :

1. rédaction ;
2. comparaison au plan maître ;
3. audit de complétude pédagogique ;
4. contrôle des doublons ;
5. vérification technique des commandes et exemples ;
6. ajout des contextes d’utilisation ;
7. correction des omissions ;
8. vérification des frontières avec les chapitres voisins ;
9. mise à jour de `contents.txt`, de l’index, de `ROADMAP.md` et du présent fichier ;
10. compilation Pandoc/XeLaTeX ;
11. inspection du PDF ;
12. rapport QA et preuve indépendante ;
13. seulement ensuite : chapitre déclaré rédigé, repéré et audité.

Métadonnées minimales :

```yaml
status: "reviewed"
audit-status: "complete"
audit-date: "YYYY-MM-DD"
audit-level: "static-review"
audit-report: "chemin/du/rapport.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
```

Le niveau `runtime-tested` ne doit être utilisé qu’après exécution réelle des exemples dans un projet matérialisé.

## 12. Règle pédagogique pour le code

Lors de la première apparition d’une syntaxe ou d’un concept, expliquer :

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
- résultat concret ;
- erreurs fréquentes ;
- variante plus explicite pour débutant lorsque la forme compacte masque le fonctionnement.

Les rappels pédagogiques sont autorisés lorsqu’un nouvel exemple combine les concepts différemment. Les duplications intégrales involontaires de titres, paragraphes longs ou blocs significatifs sont interdites.

## 13. Audit actuel du chapitre 2 GDScript

Dernière campagne fusionnée : PR n°11.

- commit de référence : `e40da615bdc922f0296ef34f51dc6e226f0782dd` ;
- 152 titres contrôlés ;
- 57 blocs de code significatifs contrôlés ;
- 22 paragraphes longs contrôlés ;
- zéro titre dupliqué ;
- zéro bloc significatif dupliqué ;
- zéro paragraphe long dupliqué ;
- zéro explication pédagogique obligatoire manquante ;
- 829 blocs sur 829 repérés ;
- zéro incohérence sémantique ;
- PDF A4 1.5 de 512 pages ;
- réserve runtime maintenue jusqu’à la matérialisation de `Project Asteria`.

La PR n°12 a été fermée sans fusion, car son mécanisme temporaire n’avait pas appliqué les changements et était redondant après la fusion de la PR n°11.

## 14. QA, compilation et preuves

- Markdown = source unique ;
- compilation avec Pandoc et XeLaTeX ;
- vérification structurelle, métadonnées, identifiants et liens ;
- extraction du texte du PDF ;
- contrôle des polices et caractéristiques techniques ;
- inspection visuelle d’un échantillon de pages ;
- preuves finales externalisées en YAML pour éviter l’auto-référence des rapports compilés ;
- aucun rapport ne doit revendiquer une exécution runtime qui n’a pas eu lieu.

## 15. Décisions techniques importantes

### Windows et AMD

- guide local-first et Windows-first ;
- chemins GPU AMD expérimentaux isolés ;
- CPU toujours disponible comme référence ;
- Docker Desktop non présenté comme solution GPU AMD universelle.

### ComfyUI

- installation manuelle de référence ;
- CPU obligatoire comme secours ;
- ZLUDA laboratoire expérimental ;
- DirectML solution dégradée ;
- workflows, manifestes, modèles, licences et empreintes versionnés.

### LLM locaux

- Ollama natif Windows pour le parcours simple ;
- llama.cpp CPU/Vulkan comme moteur de référence ;
- LocalAI passerelle optionnelle ;
- LibreChat interface alternative ;
- services liés à `127.0.0.1` sauf sécurisation explicite.

### Audio local

- Kokoro et Piper pour les voix légères ;
- Chatterbox pour voix expressive et clonage autorisé ;
- faster-whisper et whisper.cpp pour transcription ;
- AudioCraft réservé aux usages compatibles avec les licences ;
- aucun clonage vocal sans consentement.

## 16. Historique condensé des jalons

- M0 : infrastructure documentaire terminée.
- M1 : Volume 0 terminé et audité.
- M2 : Livre I terminé à dix chapitres après réouverture.
- Audit transversal Volume 0/Livre I : contextes appliqués et validés.
- M3 : Livre II en cours.
- Chapitre 1 : rédigé, repéré et audité.
- Chapitre 2 : rédigé, repéré, enrichi et audité contre les doublons.

Pull requests importantes :

- PR 3 : restauration du Livre I complet ;
- PR 5 : audit initial des chapitres 1 et 2 ;
- PR 6 et 7 : audit Volume 0/Livre I ;
- PR 8 : repères Livre II ;
- PR 10 : explications GDScript ligne par ligne ;
- PR 11 : audit anti-doublon et fonctions ;
- PR 12 : fermée sans fusion.

## 17. Erreurs à ne pas reproduire

- Ne pas déclarer un Livre complet uniquement parce que ses grands domaines sont couverts.
- Ne pas condenser des fondations de débutant en simples prérequis.
- Ne pas donner une commande sans préciser le terminal.
- Ne pas donner un contenu de fichier sans préciser l’éditeur et le chemin.
- Ne pas présenter une sortie comme une commande.
- Ne pas affirmer qu’un exemple a été exécuté lorsqu’il a seulement été relu.
- Ne pas conserver de workflows temporaires dans `main`.
- Ne pas publier des mesures intermédiaires comme preuve finale.
- Ne pas laisser une fonction, un paramètre, un opérateur ou un type sans explication suffisante.
- Ne pas dupliquer intégralement une explication déjà donnée.
- Ne pas modifier le plan maître sans décision explicite et journalisée.
- Ne pas oublier de mettre à jour ce fichier.

## 18. État courant du dépôt

- Branche principale : `main`.
- Jalon actif : M3 — Livre II.
- Livre II : 2 chapitres sur 30 rédigés, repérés et audités.
- Chapitre 2 : version `1.3.0`.
- Dernier commit métier important : `e40da615bdc922f0296ef34f51dc6e226f0782dd`.
- Licence globale : à définir.
- Accessibilité PDF avancée : à traiter avant publication.
- Tests runtime de `Project Asteria` : en attente du projet exécutable matérialisé.

## 19. Prochaine action

Créer puis auditer :

```text
Livre-II/CHAPITRE-03-Scenes-noeuds-resources-et-signaux.md
```

Le chapitre doit suivre exactement la fiche du chapitre 3 dans le plan maître du Livre II et inclure : repères, explications ligne par ligne, exercice fil rouge, contrôle des doublons, audit, compilation et inspection PDF.

## 20. Journal des mises à jour de continuité

### 2026-07-18 — version 2.0.0

- ajout du plan détaillé des 30 chapitres du Livre II ;
- ajout du plan détaillé des 30 chapitres du Livre III ;
- ajout du plan détaillé des 22 chapitres du Livre IV ;
- ajout du plan détaillé des 26 chapitres du Livre V ;
- ajout des dix packs du Companion Pack ;
- ajout des objectifs, frontières, livrables et règles de chaque partie ;
- renforcement des instructions de reprise et de gouvernance.

### 2026-07-18 — version 1.0.0

- création du document de continuité ;
- reprise de la vision, du matériel, de l’architecture et des jalons ;
- enregistrement des règles d’audit et de contextes ;
- enregistrement de l’état des Livres I et II ;
- enregistrement de l’audit anti-doublon du chapitre 2 ;
- définition de la prochaine action.
