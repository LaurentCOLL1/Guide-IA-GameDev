---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier permet de reprendre le projet dans une nouvelle conversation sans recommencer la conception. Il résume les décisions permanentes, l’état du dépôt, les erreurs corrigées et la prochaine action.

> **Règle obligatoire :** toute modification documentaire, technique, structurelle ou QA doit mettre à jour ce fichier dans le même lot de commits ou la même pull request.

## 1. Procédure obligatoire lors d’une reprise

Une nouvelle conversation doit suivre cet ordre :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. lire le plan maître détaillé du Livre ou Pack actif ;
4. vérifier les derniers commits et pull requests fusionnés ;
5. ne pas recréer un chapitre, un audit ou une décision déjà présent ;
6. comparer la prochaine action au plan maître ;
7. effectuer rédaction, audit, compilation et QA ;
8. mettre à jour ce fichier avant de déclarer le lot terminé.

## 2. Sources maîtres obligatoires

Le plan exact de la collection est réparti dans les documents suivants :

- **Livre II :** section dédiée du présent fichier et `Livre-II/index.md` ;
- **Livre III :** [`plans/LIVRE-III-PLAN-MAITRE.md`](plans/LIVRE-III-PLAN-MAITRE.md) ;
- **Livre IV :** [`plans/LIVRE-IV-PLAN-MAITRE.md`](plans/LIVRE-IV-PLAN-MAITRE.md) ;
- **Livre V :** [`plans/LIVRE-V-PLAN-MAITRE.md`](plans/LIVRE-V-PLAN-MAITRE.md) ;
- **Companion Pack :** [`plans/COMPANION-PACK-PLAN-MAITRE.md`](plans/COMPANION-PACK-PLAN-MAITRE.md).

Ces documents font partie de la gouvernance du projet. Un titre, un ordre ou un périmètre ne doit pas être modifié silencieusement. Toute modification du plan maître exige une décision explicite, une justification et une mise à jour de la roadmap.

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

**Statut : en cours — 2 chapitres sur 30 rédigés, repérés et audités.**

#### Partie A — Fondations Godot, architecture et données

1. Découvrir Godot et créer le projet fil rouge — **terminé**.
2. Fondamentaux de GDScript — **terminé, enrichi et audité contre les doublons**.
3. Scènes, nœuds, Resources et signaux.
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

Le détail des objectifs du chapitre 3 et des chapitres suivants doit être vérifié dans le plan maître avant rédaction.

### Livre III — Production des contenus et des assets

**Statut : non commencé — 30 chapitres.**

Source obligatoire : [`plans/LIVRE-III-PLAN-MAITRE.md`](plans/LIVRE-III-PLAN-MAITRE.md).

Le plan détaille pour chacun des 30 chapitres : objectifs, livrables, frontière avec les autres chapitres et critères de validation. Il couvre préproduction, direction artistique, ComfyUI, Blender, provenance, humains, humanoïdes, animaux, créatures, visages, vêtements, objets, architecture, terrains, végétation, PBR, UV, LOD, rigging, animation, mocap, cinématiques, VFX, UI, UX, audio, lip-sync, import Godot, validation et automatisation.

### Livre IV — Finalisation, optimisation, publication et maintenance

**Statut : non commencé — 22 chapitres.**

Source obligatoire : [`plans/LIVRE-IV-PLAN-MAITRE.md`](plans/LIVRE-IV-PLAN-MAITRE.md).

Le plan détaille équilibrage, QA, tests, débogage, observabilité, profilage CPU/GPU/mémoire, streaming, optimisation, multijoueur, sécurité réseau, DevOps, sauvegardes, exports, publication, accessibilité, localisation, mises à jour, modding et pérennité.

### Livre V — Encyclopédie technique et bibliothèque de référence

**Statut : non commencé — 26 chapitres.**

Source obligatoire : [`plans/LIVRE-V-PLAN-MAITRE.md`](plans/LIVRE-V-PLAN-MAITRE.md).

Le plan détaille chaque type de fiche, les arbres de décision, les bibliothèques de workflows/prompts/scripts, les références GDScript/Python/JSON/SQLite/vectorielles, les patrons, erreurs, benchmarks, matrices, comparatifs, checklists, licences et index croisés.

### Companion Pack

**Statut : non commencé — 10 packs.**

Source obligatoire : [`plans/COMPANION-PACK-PLAN-MAITRE.md`](plans/COMPANION-PACK-PLAN-MAITRE.md).

Packs :

1. Starter Kit.
2. Project Templates.
3. AI Library.
4. Code Library.
5. Database Library.
6. ComfyUI Library.
7. Documentation Library.
8. Test & Benchmark Library.
9. Production Toolkit.
10. Knowledge Base.

Le plan détaille objectifs, contenu prévu, dépendances et critères de validation de chaque pack.

## 6. Repères obligatoires d’utilisation

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

La CI contrôle la présence et la cohérence sémantique de ces repères.

## 7. Audit obligatoire après chaque chapitre

Aucun chapitre n’est terminé immédiatement après sa rédaction.

Séquence :

1. rédaction ;
2. comparaison au plan maître ;
3. audit de complétude pédagogique ;
4. contrôle des doublons ;
5. vérification technique ;
6. ajout des contextes d’utilisation ;
7. correction des omissions ;
8. contrôle des frontières avec les chapitres voisins ;
9. mise à jour de `contents.txt`, index, roadmap et continuité ;
10. compilation Pandoc/XeLaTeX ;
11. inspection du PDF ;
12. rapport QA et preuve indépendante ;
13. seulement ensuite : statut rédigé, repéré et audité.

Métadonnées minimales :

```yaml
status: "reviewed"
audit-status: "complete"
audit-date: "YYYY-MM-DD"
audit-level: "static-review"
audit-report: "chemin/du/rapport.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
```

`runtime-tested` est réservé aux exemples réellement exécutés.

## 8. Règle pédagogique pour le code

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

## 9. Audit actuel du chapitre 2 GDScript

Campagne de référence : PR n°11, commit métier `e40da615bdc922f0296ef34f51dc6e226f0782dd`.

Résultats :

- 152 titres contrôlés ;
- 57 blocs de code significatifs ;
- 22 paragraphes longs ;
- zéro doublon ;
- zéro explication pédagogique obligatoire manquante ;
- 829 blocs sur 829 repérés ;
- zéro incohérence sémantique ;
- PDF A4 de 512 pages ;
- réserve runtime maintenue.

La PR n°12 a été fermée sans fusion : son workflow temporaire n’avait pas appliqué les changements et était redondant.

## 10. Décisions techniques permanentes

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

## 11. Erreurs à ne pas reproduire

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
- Ne pas oublier la mise à jour de ce fichier.

## 12. État courant

- Branche principale : `main`.
- Jalon actif : M3 — Livre II.
- Livre II : 2 chapitres sur 30 terminés.
- Chapitre 2 : version `1.3.0`, audité contre les doublons.
- Licence globale : à définir.
- Accessibilité PDF avancée : à traiter avant publication.
- Tests runtime de `Project Asteria` : en attente du Starter Kit matérialisé.

## 13. Prochaine action

Créer puis auditer :

```text
Livre-II/CHAPITRE-03-Scenes-noeuds-resources-et-signaux.md
```

Le chapitre doit couvrir en détail :

- scène, nœud, branche et instance ;
- arbre de scène et ownership ;
- instanciation et composition ;
- `NodePath`, `$`, `%NomUnique`, `get_node()` et références typées ;
- signaux intégrés et personnalisés ;
- connexion par éditeur et par code ;
- `Callable`, `connect()`, émission et déconnexion ;
- Resources natives et personnalisées ;
- ordre d’initialisation ;
- erreurs fréquentes ;
- exercice intégré à `Project Asteria` ;
- repères d’utilisation ;
- explications ligne par ligne ;
- audit de complétude et de doublons ;
- compilation et inspection PDF.

## 14. Journal de continuité

### 2026-07-18 — version 3.0.0

- création de quatre plans maîtres détaillés séparés ;
- détail complet des 30 chapitres du Livre III ;
- détail complet des 22 chapitres du Livre IV ;
- détail complet des 26 chapitres du Livre V ;
- détail complet des 10 packs du Companion Pack ;
- ajout des objectifs, livrables, dépendances, frontières et critères de validation ;
- transformation de ce fichier en index de reprise obligatoire ;
- conservation de la prochaine action du Livre II.
