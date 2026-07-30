---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "4.19.0"
lang: "fr-FR"
last-updated: "2026-07-30T10:29:52+02:00"
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
- **Livre V :** `plans/LIVRE-V-PLAN-MAITRE.md` et `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` ;
- **Companion Pack :** `plans/COMPANION-PACK-PLAN-MAITRE.md`.

Aucun titre, ordre ou périmètre ne doit être modifié silencieusement.

Toute section de sources ou de références techniques présente les pages web sous forme de liens Markdown nommés et directement cliquables. Une URL brute, entre accents graves ou placée dans un bloc de code ne remplit pas cette exigence lecteur. Cette règle est contrôlée automatiquement pour le Livre III à partir du chapitre 19.

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

Tout bloc de code significatif doit recevoir une explication proportionnée à sa complexité et limitée aux informations réellement utiles : entrées et types, paramètres, valeurs de retour, effets de bord, instructions non évidentes, invariants, résultat attendu et limites pertinentes. `Rôle` est conservé seulement lorsqu’il nomme un contrat, une fonction, une transformation ou une responsabilité concrète. `Emplacement` est omis lorsque le chemin est déjà donné par le contexte adjacent. Les règles générales de syntaxe déjà expliquées ne sont pas répétées.

Chaque chapitre du Livre III doit comporter une section finale intitulée **« Synthèse opérationnelle pour Project Asteria »**. Elle doit traduire le contenu en décisions permanentes du projet fil rouge : identifiants retenus, conventions, dépendances, livrables, porte d’acceptation et réserves. Son absence est désormais une erreur QA bloquante pour les chapitres 17 et suivants.

Cette règle est une porte d’audit bloquante pour les nouveaux chapitres comme pour les corrections rétroactives. Les chapitres 15 et 16 ont été corrigés selon cette règle ; le chapitre 17 applique en plus la nomenclature précise des retours, refus et statuts.

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

**Terminé, audité transversalement et compilé : 30 chapitres sur 30.**

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
13. Sécurité et séparation production/runtime de l’IA — terminé au niveau `static-review`.

#### Partie C — Systèmes de gameplay

14. Personnages — terminé au niveau `static-review`.
15. Relations sociales — terminé au niveau `static-review`.
16. Famille et générations — terminé au niveau `static-review`.
17. Agents IA et comportements autonomes — terminé au niveau `static-review`.
18. Combat — terminé au niveau `static-review`.
19. Compétences et pouvoirs — terminé au niveau `static-review`.
20. Inventaire et réputation des objets — terminé au niveau `static-review`.
21. Économie — terminé au niveau `static-review`.
22. Monde vivant et simulation écologique — terminé au niveau `static-review`.
23. Politique, factions et justice — terminé au niveau `static-review`.
24. Construction et gestion de domaines — terminé au niveau `static-review`.
25. Narration, quêtes, codex et connaissances — terminé au niveau `static-review`.

#### Partie D — Industrialisation

26. Outils d’édition internes et pipelines de contenu — terminé au niveau `static-review`.
27. Tests unitaires, tests d’intégration et simulations — terminé au niveau `static-review`.
28. Journalisation, diagnostic et reproductibilité — terminé au niveau `static-review`.
29. Automatisation Python et génération de données — terminé au niveau `static-review`.
30. Architecture Solo et architecture Studio — terminé au niveau `static-review`.

### Livre III

**Terminé, audité transversalement et compilé : 30 chapitres sur 30.**

1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.
2. Direction artistique et bible visuelle — terminé au niveau `static-review`.
3. Références, concept art et ComfyUI — terminé au niveau `static-review`.
4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.
5. Provenance, licences et validation des assets — terminé au niveau `static-review`.
6. Création des humains — terminé au niveau `static-review`.
7. Création des humanoïdes — terminé au niveau `static-review`.
8. Création des animaux — terminé au niveau `static-review`.
9. Création des créatures — terminé au niveau `static-review`.
10. Visages, peau, yeux, cheveux et pilosité — terminé au niveau `static-review`.
11. Vêtements, armures et accessoires — terminé au niveau `static-review`.
12. Objets, équipements et armes — terminé au niveau `static-review`.
13. Architecture, bâtiments et kits modulaires — terminé au niveau `static-review`.
14. Terrains, paysages et mondes ouverts — terminé au niveau `static-review`.
15. Végétation et biomes — terminé au niveau `static-review`.
16. Textures, matériaux et pipeline PBR — terminé au niveau `static-review`.
17. UV, retopologie et baking — terminé au niveau `static-review`.
18. LOD, imposteurs et optimisation géométrique — terminé au niveau `static-review`.
19. Rigging et skinning — terminé au niveau `static-review`.
20. Animation procédurale et animation par keyframes — terminé au niveau `static-review`.
21. Capture de mouvement et retargeting — terminé au niveau `static-review`.
22. Cinématiques, caméras et mise en scène — terminé au niveau `static-review`.
23. Effets visuels, particules et simulations — terminé au niveau `static-review`.
24. Interface utilisateur — terminé au niveau `static-review`.
25. Expérience utilisateur et accessibilité visuelle — terminé au niveau `static-review`.
26. Voix, bruitages, ambiances et musique — terminé au niveau `static-review`.
27. Synchronisation labiale et animation faciale — terminé au niveau `static-review`.
28. Importation et intégration dans Godot — terminé au niveau `static-review`.
29. Validation technique et artistique des assets — terminé au niveau `static-review`.
30. Automatisation Blender, ComfyUI et production en lots — terminé au niveau `static-review`.

Les trente chapitres sont rédigés, repérés et audités. La compilation Pandoc/XeLaTeX, le préflight et l’inspection visuelle du PDF lecteur ont réussi ; le Livre III est clos avec réserves globales de collection.

### Livres IV à V et Companion Pack

Le détail chapitre par chapitre ou pack par pack se trouve dans leurs plans maîtres. Chaque entrée y possède objectifs, livrables, dépendances, frontières et critères de validation.

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

Chapitres 3 à 30 : **Élevée**.

Livre III, chapitres 1 et 2 : **Élevée**.

À chaque clôture de chapitre, la section **Prochaine action** de `CONTINUITE-PROJET.md` doit contenir dans le même bloc de texte le chemin canonique et la ligne `Niveau GPT-5.6 Sol recommandé : Moyenne ou Élevée`. Le chapitre publié ne contient ni section `Prochaine étape`, ni chemin ou niveau du chapitre suivant : ces informations restent exclusivement dans la continuité du projet.

La recommandation GPT-5.6 Sol décrit l’effort de raisonnement conseillé pour **produire** un chapitre. Elle ne décrit pas le chapitre lui-même et ne doit donc apparaître ni sous la clé `recommended-reasoning`, ni dans l’en-tête ou le corps destiné au lecteur, ni dans l’audit ou la preuve QA du document publié.

## 8. Audit par chapitre

Les explications de code des chapitres 17 et suivants conservent toute information pédagogique déjà publiée, la reclassent sous un point explicite et créent un point technique supplémentaire lorsqu’aucune rubrique standard ne convient. Les sections Solo/Studio restent en Markdown ordinaire sauf représentation littérale d’un format.

Exception obligatoire : dans une section sémantique d’erreurs, d’anti-patterns, de diagnostics ou de corrections, les marqueurs placés après les deux exemples sont suivis directement par `Pourquoi cet exemple est fautif` puis `Pourquoi la correction fonctionne`. La rubrique `Explication structurée du bloc`, les points génériques et toute répétition intermédiaire sont interdits dans ces sous-cas.

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
last-verified: "YYYY-MM-DDTHH:MM:SS±HH:MM"
audit-status: "complete"
audit-date: "YYYY-MM-DDTHH:MM:SS±HH:MM"
audit-level: "static-review"
audit-report: "Livre-II/QA/..."
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
```

## 9. Politique PDF

Décision utilisateur du 19 juillet 2026 :

- ne plus construire le PDF après chaque chapitre ;
- construire et inspecter le PDF à la fin de chaque Livre ;
- construire une dernière version à la fin de la collection ;
- autoriser une exception uniquement pour une modification directe de la chaîne PDF ou de la mise en page.
- l’ordre de compilation destiné au lecteur exclut tous les fichiers `QA/`, protocoles d’audit, audits de chapitres, preuves de validation et rapports de campagne ;
- les métadonnées et mentions visibles décrivant la phase de conception ou l’audit restent dans le dépôt, mais ne doivent pas apparaître dans le manuel PDF vendu au lecteur ;

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.9`.

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

Aucune rubrique d’explication ne justifie un bloc en citant le titre de la section courante. Elle énonce directement le fait technique, le risque ou l’invariant. Les renvois internes visent la sous-section exacte et utilisent un fragment vérifié ou une ancre explicite stable.

La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif suivi de `Pourquoi cet exemple est fautif`, puis un exemple corrigé suivi de `Pourquoi la correction fonctionne`.

Les sections détaillées portent `<!-- qa:error-correction-section -->`. Un index compact de symptômes peut porter `<!-- qa:error-correction-index -->` uniquement s’il renvoie vers des exemples détaillés conformes.

Hors d’une section pédagogique d’erreurs ou de corrections, le mot `erreur` ne sert pas de libellé générique. Employer `Valeurs de retour` pour des résultats ou sentinelles, `Codes de retour` pour les valeurs `Error`, `Refus contrôlé` pour un rejet normal par contrat, `Statuts à distinguer` pour comparer des états métier, et `Traitement du résultat` lorsque l’appelant doit consommer ou journaliser le retour. `Erreur fréquente` est réservé à un piège reproductible accompagné d’un exemple fautif et d’une correction.

À partir du chapitre 17 version `1.0.2`, `last-verified` et `audit-date` sont des chaînes ISO 8601 complètes avec heure, secondes et décalage UTC, dans le fuseau `Europe/Paris`. Une heure historique inconnue n’est jamais reconstruite : les documents antérieurs passent au format horodaté seulement lors de leur prochaine révision réellement auditée.

Les chapitres 14 à 25 se terminent par une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Les informations de pilotage éditorial et la préparation du chapitre suivant restent dans la section `Prochaine action` de ce fichier, jamais dans le chapitre destiné au lecteur.

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
- le durcissement de production est traité au chapitre 13.

### 11.8 Sécurité et séparation production/runtime

- modèle de menaces maintenu avec actifs, frontières et menaces prioritaires ;
- quatre zones séparées : production, livraison, runtime distribué et données du joueur ;
- capacités de production exclues du package runtime ;
- profils `development`, `test` et `production` distincts ;
- secrets hors dépôt, hors `res://`, hors payloads métier et hors journaux ;
- écoute sur `127.0.0.1` par défaut, adresses non spécifiées refusées ;
- authentification et TLS obligatoires lorsque le service quitte la boucle locale ;
- autorisation par défaut refusée pour opérations, modèles et chemins ;
- `task_id` et identifiants similaires ne valent jamais autorisation ;
- chemins canoniques résolus sous des racines autorisées ;
- processus exécuté sans privilège administrateur ni clé de publication ;
- payloads, résultats, délais, débit, tâches et concurrence bornés ;
- journaux rédigés, rotatifs et sans en-tête `Authorization` ;
- dépendances épinglées et licences inventoriées ;
- SBOM, provenance, signature et rollback préparés pour la publication ;
- violation de sécurité refusée sans contournement par le repli ;
- repli déterministe conservé uniquement pour les indisponibilités fonctionnelles prévues.

### 11.9 Personnages

- identité d’instance `chr_...` indépendante du nom affiché et distincte du `StableId` de définition ;
- `CharacterDefinition` comme `Resource` de conception validée et partagée ;
- `CharacterRuntimeState` séparé, borné et dépourvu de référence vers un nœud actif ;
- statistiques dérivées recalculées depuis la définition et les bonus autoritaires ;
- scène composée avec corps, runtime, synchronisation de transform, visuel et contrôleur séparés ;
- réutilisation de la chaîne d’intention du chapitre 6 sans lecture directe de `Input` dans le personnage ;
- initialisation avant entrée dans l’arbre et placement global après `add_child()` ;
- apparition unique par identité et disparition distincte de la suppression métier ;
- registre limité aux instances actives et injecté aux services concernés ;
- événements typés de nom, santé, endurance et état de vie ;
- snapshot strict composé d’identifiants et de valeurs sérialisables, sans nœud, ressource ou cache ;
- section de sauvegarde préparée complètement avant application ;
- relations, famille, agents, combat et compétences maintenus dans des systèmes séparés.

### 11.10 Relations sociales

- une relation est une perception orientée `source → cible` entre deux `CharacterId` ;
- les deux directions peuvent diverger et sont persistées séparément ;
- les vues mutuelles sont calculées et distinguent absence de relation et neutralité ;
- affinité, confiance et respect sont bornés de `-100` à `100`, peur de `0` à `100` ;
- chaque mutation exige une cause stable, un système source, un tick logique et au moins un delta ;
- les deltas sont bornés et l’historique récent est limité à `32` entrées ;
- la mutation utilise une copie profonde, une validation complète et `replace_one()` avant émission ;
- le dépôt indexe les relations sortantes sans dépendre des nœuds actifs ;
- l’existence est validée contre un index logique des personnages, y compris hors scène ;
- les événements typés transportent des copies des axes avant et après ;
- les snapshots refusent clés inconnues, conversions silencieuses, doublons et références absentes ;
- la section sociale est préparée avant application et reste indépendante de la section personnages ;
- parenté, agents, factions, réputation et narration restent dans leurs systèmes propres.

### 11.11 Famille et générations

- système familial séparé de `CharacterRuntimeState` et des axes sociaux ;
- liens fondés sur les `CharacterId` et indépendants des nœuds actifs ;
- filiation dirigée parent vers enfant avec types biologique et adoption ;
- tutelle dirigée et union par paire canonique distinctes de la filiation ;
- intervalles logiques inclusifs avec début, fin éventuelle et provenance ;
- auto-liens, doublons métier, chevauchements invalides et références inconnues refusés ;
- cycles d’ascendance détectés avant mutation avec refus conservateur en cas de dépassement du budget ;
- parcours bornés par profondeur `32` et maximum `4 096` nœuds ;
- parents, enfants, fratries, ancêtres, descendants et distance générationnelle calculés ;
- fratries, générations, caches et index secondaires exclus de la persistance ;
- personnages décédés, archivés ou absents de la scène conservés par l’index logique ;
- événements typés et historique familial borné à `256` records ;
- snapshots stricts pour filiation, tutelle, union et historique ;
- graphe candidat complet validé avant remplacement de l’état actif ;
- succession, héritage, politique, narration et décisions d’agents maintenus dans leurs systèmes propres.

### 11.12 Agents IA et comportements autonomes

- état `AgentState` séparé de `CharacterRuntimeState`, du social et de la famille ;
- faits structurés avec provenance, confiance, observation et expiration ;
- mémoire bornée à `128` faits et tableau noir à `32` clés déclarées ;
- buts durables séparés des intentions, plans et requêtes transitoires ;
- catalogue d’actions validé avec préconditions, effets, coût et exécuteur ;
- planificateur déterministe borné à `256` expansions et profondeur `8` ;
- snapshots détachés et révision du monde contrôlée avant émission ;
- ordonnanceur round-robin limité à `8` décisions par tick physique ;
- échéance conservée avec `logical_tick >= next_due_tick` lorsqu’un agent est reporté par le budget ;
- modes actif, arrière-plan et dormant sans confondre scène et existence ;
- invalidation et annulation coopérative corrélées par `request_id` ;
- RNG local restaurable réservé aux variantes métier équivalentes ;
- IA générative limitée à des suggestions filtrées par le catalogue ;
- persistance des buts et compteurs durables, sans perceptions ni plans ;
- codec strict et section préparée avant remplacement atomique ;
- combat, compétences, économie, monde vivant, politique et narration séparés.

### 11.13 Combat

- `CombatService` constitue l’autorité des commandes de combat ;
- les joueurs, agents et scénarios soumettent des commandes typées sans imposer le résultat ;
- santé, endurance et état de vie restent dans `CharacterRuntimeState` ;
- initiative, côté, garde et états temporaires restent dans `CombatantState` ;
- les côtés sont explicites et le tir allié dépend d’une règle de conception ;
- l’initiative utilise des entiers bornés et un départage lexical stable, jamais `hash()` ;
- portée logique et ligne de vue sont validées séparément ;
- les mutations sont calculées sur des copies détachées puis committées comme un lot validé ;
- l’historique candidat est écrit avant commit et les événements ne sont émis qu’après succès ;
- les commandes sont corrélées, idempotentes, bornées et ordonnées ;
- le codec de sauvegarde est strict et encode le RNG 64 bits sans perte par deux mots de 32 bits ;
- file de commandes, raycasts, caches et présentation sont exclus de la persistance ;
- compétences, objets, économie, politique et narration restent dans leurs systèmes propres.

### 11.14 Compétences et pouvoirs

- `AbilityDefinition` constitue une `Resource` de conception partagée et immuable ;
- progression et état runtime sont séparés de la définition et liés au `CharacterId` ;
- rang, expérience, charges, prochain tick de recharge et séquence d’utilisation sont persistés ;
- les coûts sont décrits par identifiants de ressources et préparés sans mutation active ;
- les ciblages sur soi, personnage, point et zone sont déclaratifs, bornés et revalidés par l’autorité propriétaire ;
- les effets sont composables, ordonnés, copiés et limités à des types explicitement autorisés ;
- dégâts et états temporaires restent sous l’autorité du combat ;
- santé et endurance restent sous les règles des personnages ;
- `AbilityMutationUnitOfWork` reçoit réservation, candidats d’effets, progression, runtime et révisions dans un même commit ;
- un effet requis absent bloque le lot avant commit ;
- un résultat partiel est une utilisation consommée et ne déclenche pas un retry gratuit ;
- les recharges utilisent des ticks logiques, jamais un `Timer` autoritaire ;
- plans, réservations, candidats, cibles dérivées, caches et présentation sont exclus de la persistance ;
- l’inventaire peut accorder une compétence sans devenir propriétaire de ses règles.

### 11.15 Inventaire et réputation des objets

- `ItemDefinition` constitue une `Resource` de conception partagée et immuable ;
- instances uniques et lots fongibles possèdent des états distincts ;
- une définition empilable exclut durabilité, équipement, compétence accordée et réputation individuelle ;
- propriété métier et garde matérielle sont séparées ;
- les conteneurs référencent des entrées par identifiants stables et la masse totale reste dérivée ;
- l’origine complète d’un lot comprend `lot_id`, cause, système source et tick logique ;
- les fusions exigent définition, origine complète et propriétaire identiques ;
- source, destination et entrée sont préparées sur des copies avec révisions séparées ;
- `InventoryAccessPort` autorise la demande sans contourner les invariants d’inventaire ;
- un objet équipé doit être déséquipé avant transfert ;
- seuls les objets uniques compatibles et non brisés peuvent être équipés ;
- les compétences accordées restent sous l’autorité du système de compétences ;
- le combat prépare une demande de durabilité sans écrire l’inventaire ;
- provenance et réputation utilisent des causes validées et des ticks logiques ;
- `InventoryMutationUnitOfWork` reçoit les candidats d’inventaire et des autorités externes avant tout événement ;
- définitions, masse dérivée, commandes, candidats, caches et présentation sont exclus de la persistance ;
- prix, monnaies, paiements, achats et ventes restent réservés au chapitre 21.


### 11.16 Économie

- `CurrencyDefinition` constitue une `Resource` de conception partagée et immuable ;
- tous les montants utilisent des unités mineures entières dans la plage JSON sûre ;
- les portefeuilles portent des soldes non négatifs, des révisions et des séquences d’écriture ;
- chaque transaction produit des écritures équilibrées séparément par devise ;
- les valeurs économiques sont séparées des `ItemDefinition` du chapitre 20 ;
- les multiplicateurs utilisent des points de base et un ordre déterministe ;
- une fabrique verrouille le prix unitaire lors de la création d’une offre ;
- les devis sont temporaires, bornés et recalculés avant le commit ;
- le total proposé par l’appelant sert uniquement à détecter un changement de prix ;
- récompenses et paiements débitent toujours un portefeuille explicite ;
- l’idempotence associe identité de transaction, empreinte canonique et résultat durable ;
- `EconomyTransactionCommitPort` coordonne candidat économique et candidat d’inventaire ;
- l’inventaire conserve identité, quantité, propriété et transfert des objets ;
- contextes sociaux, écologiques, politiques ou fiscaux restent derrière des ports ;
- devis, contextes, commandes, candidats, caches et présentation sont exclus de la persistance.

### 11.17 Monde vivant et simulation écologique

- `WorldClockState` constitue l’horloge logique globale persistée ;
- l’heure système, les `Timer` et les durées basées sur l'heure réelle ne sont jamais autoritaires ;
- les régions sont des unités logiques indépendantes des scènes ;
- définitions de régions, espèces et ressources restent des `Resource` immuables ;
- populations et réserves sont des états agrégés persistants séparés des représentations ;
- les résidus sont entiers, bornés par `ticks_per_day` et restaurés avec l’horloge ;
- les habitats et ressources alimentaires sont validés par le catalogue ;
- les calculs utilisent une arithmétique entière bornée et des points de base ;
- ressources puis populations sont simulées dans un ordre lexical déterministe ;
- les modes actif, arrière-plan et dormant contrôlent la fréquence, jamais l’existence ;
- l’ordonnanceur est round-robin et limité à quatre régions par tick physique ;
- un long intervalle produit une étape agrégée bornée, jamais un replay tick par tick ;
- matérialiser ou dématérialiser un acteur ne modifie pas la population logique ;
- les commandes causales sont révisionnées, idempotentes et committent leur résultat avec la région ;
- une récolte committe ensemble réserve écologique et candidat d’inventaire ;
- l’écologie fournit rareté, abondance et observations structurées sans calculer de prix ;
- factions, lois, territoires politiques, domaines et narration restent dans les chapitres 23 à 25 ;
- définitions, capacités dérivées, contextes, modes, nœuds, signaux, commandes et candidats sont exclus de la persistance.

### 11.18 Politique, factions et justice

- institutions, factions, rangs, fonctions et lois utilisent des identifiants stables ;
- définitions de conception et états vivants restent séparés ;
- adhésions et mandats portent statuts, ticks, causes et révisions ;
- relations sociales et liens familiaux ne créent aucun droit institutionnel implicite ;
- lois et promulgations sont versionnées et immuables après publication ;
- juridictions et périodes d’effet utilisent des références logiques et l’horloge du monde ;
- autorisations calculées distinguent `ALLOW`, `DENY`, `NOT_APPLICABLE` et `INDETERMINATE` ;
- seule une décision `ALLOW` autorise une action protégée ;
- une infraction rapportée ouvre un dossier sans établir la culpabilité ;
- preuves, faits sources, recevabilité, poids et verdicts restent distincts ;
- la chaîne de garde utilise identité, séquence, provenance et empreinte ;
- verdicts référencent lois, preuves et codes de raisonnement ;
- sanctions sont décrites par un plan puis préparées par les autorités propriétaires ;
- amendes, confiscations, restrictions et changements de domaine sont committés avec dossier, verdict et idempotence ;
- commandes, résultats et décisions durables sont révisionnés et idempotents ;
- événements sont émis uniquement après commit ;
- sorties IA restent consultatives et ne peuvent ni promulguer ni condamner ;
- définitions, droits dérivés, contextes, candidats, observations et présentation sont exclus de la persistance.

### 11.19 Construction et gestion de domaines

- domaines, parcelles, bâtiments et chantiers utilisent des identifiants stables ;
- définitions de conception et états vivants restent séparés ;
- parcelles et emplacements logiques sont indépendants des scènes ;
- les liens de tenure référencent les droits du chapitre 23 sans les recréer ;
- seule une décision politique `ALLOW` ouvre une action protégée ;
- les contraintes de site proviennent de snapshots écologiques révisionnés ;
- la capacité de parcelle est réservée à l’ouverture du chantier ;
- matériaux livrés et travail accompli restent deux dimensions distinctes ;
- progression et condition utilisent des entiers et des points de base ;
- inventaire et économie préparent leurs candidats sans céder leur autorité ;
- construction, production et entretien committent les candidats multi-autorités avec le résultat idempotent ;
- un bâtiment logique existe indépendamment de sa représentation 3D ;
- événements sont émis uniquement après commit ;
- sorties IA restent consultatives et repassent par des commandes validées ;
- définitions, décisions dérivées, candidats, scènes, observations et caches sont exclus de la persistance.

### 11.20 Narration, quêtes, codex et connaissances

- faits sources et interprétations narratives restent distincts ;
- arcs, quêtes, objectifs et codex utilisent des identifiants stables ;
- définitions de conception et états runtime restent séparés ;
- conditions évaluées par un registre fermé et explicable ;
- `INDETERMINATE` n’accorde ni succès ni visibilité ;
- événements sources traités avec identité, empreinte et reçu idempotent ;
- conséquences externes préparées par leurs autorités propriétaires ;
- achèvement et conséquences committés dans un même lot ;
- connaissances relatives à un détenteur, une source et une confiance ;
- mémoire vectorielle dérivée et exclue de l’autorité des sauvegardes ;
- IA locale consultative avec repli déterministe ;
- restauration globale préparée avant remplacement ;
- définitions, vues, caches, index et présentation exclus de la persistance.

### 11.21 Outils d’édition internes et pipelines de contenu

- scripts `@tool` isolés du runtime et gardés par le contexte éditeur ;
- cycle de vie des plugins symétrique, sans dock, inspecteur ni importeur résiduel ;
- modifications de scènes et ressources ouvertes intégrées à l’annulation de l’éditeur ;
- sources canoniques, artefacts générés et caches strictement séparés ;
- validation structurée, bornée et fondée sur des codes stables ;
- dépendances explicites, cycles refusés et ordre topologique déterministe ;
- sérialisation canonique avant calcul d’empreinte ;
- manifestes, provenance et reçus conservés avec les artefacts ;
- publication de fichiers par staging, vérification et promotion contrôlée ;
- importeurs versionnés, idempotents et sans réimportation récursive ;
- sortie IA limitée au statut de brouillon jusqu’à validation et approbation ;
- exécution headless disponible pour la validation de contenu ;
- chapitres 14 à 25 maintenus comme autorités exclusives du runtime.

### 11.45 Localisation et internationalisation

- `fr-FR` constitue la locale source documentaire ; aucune locale cible n’est annoncée avant qualification complète ;
- les balises éditoriales BCP 47 sont normalisées à la frontière Godot sans perdre la valeur d’origine ;
- les textes visibles utilisent des clés stables indépendantes de la formulation source ;
- les sauvegardes et le domaine conservent identifiants et valeurs, jamais les traductions résolues ;
- langue de texte, langue audio, région de format, écriture et direction restent des axes distincts ;
- nombres, dates, montants en `EUR` et unités restent structurés jusqu’au rendu ;
- variables, balises et contenus de joueur sont protégés pendant formatage et pseudo-localisation ;
- les pluriels et genres relèvent des règles de locale, jamais d’une condition française codée en dur ;
- les piles de polices, glyphes, shaping, segmentation, BiDi et saisie sont qualifiés par écriture et plateforme ;
- pseudo-localisation longue, RTL, captures et contrôles de débordement précèdent toute déclaration de support ;
- catalogue, glossaire, mémoire, statuts, rapports et captures sont versionnés et corrélés au build ;
- traduction, relecture linguistique, validation en contexte, accessibilité et publication restent des portes séparées ;
- les fournisseurs et services distants reçoivent uniquement des lots minimisés, approuvés et gouvernés ;
- les corrections distribuées et rollbacks restent au chapitre 20.

### 11.46 Correctifs, mises à jour et retour arrière

- les versions produit, build, contenu, sauvegarde et protocole restent distinctes ;
- les canaux interne, bêta et stable sont des politiques d’accès et de promotion ;
- le même candidat qualifié est promu sans reconstruction silencieuse ;
- chaque patch différentiel exige une base identifiée et une empreinte cible ;
- téléchargement, staging, vérification, activation, migration et observation forment des phases distinctes ;
- l’installation active n’est jamais modifiée pendant l’acquisition du package ;
- chaque sauvegarde porte un schéma explicite et reçoit une copie vérifiée avant migration ;
- les migrations publiées restent immuables et leurs chemins source-cible sont fermés ;
- interruption de diffusion, rollback binaire et restauration de données sont trois décisions différentes ;
- une migration irréversible peut interdire le retour binaire et imposer un roll-forward ;
- les plateformes sont des mécanismes de diffusion à revérifier, pas une garantie de rétrogradation ;
- notes de version, support, métriques et communication restent corrélés au build ;
- les tests couvrent plusieurs versions sources, interruptions et reprises sur copies ;
- l’archivage des builds, outils et preuves reste au chapitre 22.

### 11.47 Modding et contenu communautaire

- le support public commence par des formats déclaratifs et des assets runtime bornés ;
- chaque mod porte un identifiant namespacé, une version, une API cible, des dépendances, des capacités, des licences et des empreintes ;
- manifeste, archive, chemins, quotas et intégrité sont validés avant toute activation ;
- installation, activation, désactivation et désinstallation restent quatre opérations distinctes ;
- les PCK communautaires utilisent `replace_files = false` et une racine `res://mods/<id>/` ;
- GDScript et extensions natives sont traités comme du code exécutable, jamais comme une sandbox implicite ;
- les capacités inconnues sont refusées et réseau, processus, secrets et sauvegardes globales restent interdits par défaut ;
- dépendances, cycles, contraintes, ordre et conflits sont résolus de manière déterministe ;
- les sauvegardes enregistrent ensemble, versions, empreintes et état namespacé sans céder l’autorité globale ;
- le serveur possède le contrat de mods en multijoueur ;
- SDK, schémas, templates, validateur, mod d’exemple et politique de dépréciation évoluent ensemble ;
- plateformes UGC, licences, provenance, modération, confidentialité et support forment des portes séparées ;
- les mises à jour officielles restent au chapitre 20 et l’archivage au chapitre 22.


### 11.48 Maintenance, archivage et pérennité

- le dossier historique d’une version relie sources, dépendances, outils, builds, SBOM, licences, documentation et rapports ;
- un miroir reste une copie de disponibilité et ne remplace ni rétention indépendante ni support hors ligne ;
- chaque objet d’archive possède identité, classe de conservation, propriétaire, emplacement, checksum et test prévu ;
- les alertes de vulnérabilité sont triées par contexte avant toute mise à niveau ou acceptation ;
- les lockfiles améliorent la répétabilité sans supprimer le besoin de veille et de qualification ;
- Git bundle, objets LFS, sous-modules, releases et dépendances externes sont inventoriés séparément ;
- environnement de build, templates, SDK, images et paramètres sont capturés avec leurs droits de redistribution ;
- fixité, signature, authenticité, restauration et reconstruction restent des preuves distinctes ;
- les migrations de format préservent l’original et enregistrent outil, dérivé, validation et nouvelles empreintes ;
- comptes, domaines, certificats, clés et secrets possèdent propriété organisationnelle, récupération et succession ;
- la fin de support distingue annonce, maintenance réduite, retrait de services, données, communauté et archive finale ;
- une ouverture éventuelle du code ou des contenus exige une revue juridique, de secrets, de marques et de licences ;
- les critères runtime, de publication et de PDF du Livre IV restent ouverts après la fin de la rédaction documentaire.

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

Fichier : `Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md`.

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

## 20. Chapitre 13 — état détaillé

Fichier : `Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- modèle de menaces versionné et relu lors des changements de surface ;
- production, livraison, runtime et données du joueur séparés par des frontières explicites ;
- outils d’indexation, diagnostics et secrets de signature absents du package runtime ;
- profils d’environnement avec debug, journaux, administration, TLS et authentification explicites ;
- secrets exclus du dépôt, de `res://`, des payloads métier et des journaux ;
- `.godot/export_credentials.cfg`, fichiers `.env`, clés et certificats privés ignorés ;
- jetons générés avec `secrets` et comparés avec `hmac.compare_digest` ;
- boucle locale par défaut et refus des adresses non spécifiées ;
- authentification et TLS exigés hors loopback ;
- autorisation `deny-by-default` par identité et capacité ;
- listes d’autorisation pour opérations, modèles, extensions et racines de chemins ;
- résolution canonique des chemins sous une racine autorisée ;
- `TLSOptions.client_unsafe()` exclu du profil production ;
- moindre privilège pour fichiers, réseau, variables, temps et mémoire ;
- limites de corps, résultat, tâches, débit et timeout ;
- journaux structurés avec rédaction des champs sensibles ;
- dépendances réelles épinglées sans faux fichier de verrouillage ;
- SBOM CycloneDX ou SPDX choisi selon l’outillage réel ;
- provenance reliant commit, outils, paramètres non secrets et hachages ;
- signature de publication distincte d’un simple hachage ;
- mise à jour versionnée avec vérification et rollback ;
- échec fermé pour authentification, autorisation, signature et validation ;
- repli déterministe réservé aux indisponibilités fonctionnelles ;
- systèmes de gameplay réservés à partir du chapitre 14.

Livrables documentés :

- `docs/security/threat-model.md` ;
- `config/ai-capabilities.yaml` ;
- `config/ai-server-production.toml` ;
- `config/runtime-models.yaml` ;
- `res://src/core/security/runtime_profile.gd` ;
- `res://src/core/security/tls_policy.gd` ;
- `res://src/core/security/security_policy.gd` ;
- `tools/security/secret_provider.py` ;
- `tools/security/generate_local_token.py` ;
- `tools/security/redaction.py` ;
- `tools/ai_server/security_config.py` ;
- `tools/ai_server/authentication.py` ;
- `tools/ai_server/authorization.py` ;
- `tools/ai_server/safe_paths.py` ;
- `tools/ai_server/tls_context.py` ;
- `tools/ai_server/security_limits.py`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-13.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-13.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 21. Chapitre 14 — état détaillé

Fichier : `Livre-II/CHAPITRE-14-Personnages.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- identifiant d’instance aléatoire canonique, indépendant du nom et du chemin ;
- espace d’identifiants distinct pour les définitions de contenu ;
- `CharacterDefinition`, `CharacterRuntimeState` et snapshot persistant séparés ;
- attributs de base validés et statistiques dérivées reconstructibles ;
- bonus et valeurs courantes bornés, transforms obligatoirement finis ;
- fabrique centralisant les invariants de création ;
- règles fondamentales de santé et d’endurance sans anticiper le combat ;
- signaux typés transportant l’identifiant stable ;
- corps physique, runtime, visuel, synchronisation et contrôleur séparés ;
- contrôleur humain réutilisé depuis le chapitre 6 et contrôleur autonome réservé au chapitre 17 ;
- initialisation avant `add_child()` et transform global appliqué après ;
- une seule représentation active par identité ;
- disparition conservant l’état logique ;
- registre actif injecté, non global et non persistant ;
- codec strict refusant les conversions silencieuses ;
- snapshot sans nœud, ressource, contrôleur ou statistique dérivée ;
- section de sauvegarde validée et préparée avant mutation ;
- systèmes sociaux, familiaux, autonomes, de combat et de compétences séparés.

Livrables documentés :

- `src/features/characters/domain/character_id.gd` ;
- `src/features/characters/domain/character_definition.gd` ;
- `src/features/characters/domain/character_statistics.gd` ;
- `src/features/characters/domain/character_runtime_state.gd` ;
- `src/features/characters/domain/character_rules.gd` ;
- `src/features/characters/application/character_catalog.gd` ;
- `src/features/characters/application/character_factory.gd` ;
- `src/features/characters/application/character_spawner.gd` ;
- `src/features/characters/application/active_character_registry.gd` ;
- `src/features/characters/presentation/character_runtime.gd` ;
- `src/features/characters/presentation/character_transform_sync.gd` ;
- `src/features/characters/presentation/player_character.tscn` ;
- `src/features/characters/infrastructure/character_snapshot_codec.gd` ;
- `src/features/characters/infrastructure/character_save_section.gd` ;
- `src/app/character_bootstrap.gd` ;
- `data/characters/aster.tres` ;
- `scenes/learning/ch14_characters_demo.tscn` ;
- `scenes/learning/ch14_characters_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-14.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 22. Chapitre 15 — état détaillé

Fichier : `Livre-II/CHAPITRE-15-Relations-sociales.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- clé orientée fondée sur deux `CharacterId`, avec auto-relation refusée ;
- perceptions `A → B` et `B → A` indépendantes ;
- vues mutuelles calculées à partir des deux directions ;
- quatre axes sociaux bornés : affinité, confiance, respect et peur ;
- commandes sans effet et deltas excessifs refusés ;
- cause, provenance, contexte et tick logique obligatoires ;
- historique causal borné à `32` entrées par direction ;
- copie profonde des axes, états et enregistrements ;
- mutation atomique par candidat validé et `replace_one()` ;
- dépôt en mémoire avec index des relations sortantes ;
- requêtes renvoyant des identifiants plutôt que des nœuds ;
- validation contre un index logique incluant les personnages hors scène ;
- événements typés après remplacement réussi ;
- snapshot JSON strict, versionné et sans nœud ni vue dérivée ;
- section de sauvegarde indépendante préparée avant application ;
- famille, agents, factions, réputation et narration séparés.

Livrables documentés :

- `src/features/social/domain/social_relationship_key.gd` ;
- `src/features/social/domain/social_axes.gd` ;
- `src/features/social/domain/social_change_cause.gd` ;
- `src/features/social/domain/social_change_record.gd` ;
- `src/features/social/domain/social_relationship_state.gd` ;
- `src/features/social/application/change_social_relationship_command.gd` ;
- `src/features/social/application/social_relationship_repository.gd` ;
- `src/features/social/application/social_relationship_changed_event.gd` ;
- `src/features/social/application/social_relationship_service.gd` ;
- `src/features/social/application/social_relationship_query.gd` ;
- `src/features/social/application/mutual_social_view.gd` ;
- `src/features/characters/application/character_identity_index.gd` ;
- `src/features/social/infrastructure/in_memory_social_relationship_repository.gd` ;
- `src/features/social/infrastructure/social_relationship_snapshot_codec.gd` ;
- `src/features/social/infrastructure/social_relationship_save_section.gd` ;
- `scenes/learning/ch15_social_relationships_demo.tscn` ;
- `scenes/learning/ch15_social_relationships_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-15.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 23. Chapitre 16 — état détaillé

Fichier : `Livre-II/CHAPITRE-16-Famille-et-generations.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- `FamilyLinkId` aléatoire stable et indépendant de l’affichage ;
- filiation biologique et adoptive orientée parent vers enfant ;
- tutelle temporelle séparée de l’adoption ;
- union identifiée par une paire canonique non orientée ;
- intervalles logiques validés et fondés sur le tick de simulation ;
- index logique des personnages réutilisé depuis le chapitre 15 ;
- auto-liens et références inconnues refusés ;
- doublons métier et intervalles chevauchants refusés ;
- cycle d’ascendance recherché avant insertion ;
- dépassement du budget traité comme refus conservateur ;
- parents, enfants et fratries retournés par copies défensives ;
- ancêtres et descendants bornés par profondeur et nombre de nœuds ;
- génération représentée par une distance relative, jamais persistée comme valeur absolue ;
- personnages décédés, archivés ou hors scène conservés ;
- événements familiaux typés et historique borné ;
- snapshot strict sans index secondaire ni relation dérivée ;
- codec complet des filiations, tutelles, unions et records ;
- restauration par graphe candidat puis `replace_all_from()` validé ;
- agents, succession, héritage, politique et narration séparés.

Livrables documentés :

- `src/features/families/domain/family_link_id.gd` ;
- `src/features/families/domain/family_link_kind.gd` ;
- `src/features/families/domain/logical_interval.gd` ;
- `src/features/families/domain/parent_child_link.gd` ;
- `src/features/families/domain/guardianship_link.gd` ;
- `src/features/families/domain/character_pair.gd` ;
- `src/features/families/domain/union_link.gd` ;
- `src/features/families/domain/family_graph.gd` ;
- `src/features/families/domain/family_history_record.gd` ;
- `src/features/families/domain/family_event_log.gd` ;
- `src/features/families/application/add_parent_link_command.gd` ;
- `src/features/families/application/family_link_added_event.gd` ;
- `src/features/families/application/family_graph_service.gd` ;
- `src/features/families/application/family_graph_validator.gd` ;
- `src/features/families/infrastructure/family_snapshot_codec.gd` ;
- `src/features/families/infrastructure/family_save_section.gd` ;
- `scenes/learning/ch16_family_demo.tscn` ;
- `scenes/learning/ch16_family_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-16.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-16.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

### 11.23 Tests, intégration et simulations

- GUT 9.x constitue le framework de référence pour les scripts du projet, avec une révision compatible Godot 4.7 épinglée et sa licence MIT conservée ;
- les suites sont séparées entre tests unitaires, tests de composant, intégration, simulations et campagnes de plateforme ;
- les règles pures utilisent builders, fixtures, fakes, stubs et spies sans charger une scène inutilement ;
- un `SceneTree` réel est utilisé uniquement lorsque le cycle de vie Godot, les signaux, les frames ou la physique appartiennent au contrat ;
- horloge logique, RNG, dépôts et services externes sont injectés et contrôlés par le test ;
- fichiers, bases SQLite et workspaces utilisent des racines temporaires uniques et sont nettoyés après chaque cas ;
- chaque simulation déclare un scénario versionné, ses graines, un maximum de ticks et des invariants vérifiés pendant l’exécution ;
- snapshots, événements canoniques et empreintes permettent de comparer deux exécutions sans dépendre du rendu ;
- les golden files sont revus explicitement et ne sont jamais régénérés automatiquement par le test qui les compare ;
- les exécutions headless conservent les codes de sortie et publient les rapports JUnit et artefacts de diagnostic ;
- aucun retry automatique ne masque un test instable ; les services IA et réseaux réels restent hors des suites déterministes.

### 11.24 Journalisation, diagnostic et reproductibilité

- journaux, métriques et traces restent descriptifs et n’acquièrent aucune autorité métier ;
- les événements utilisent des identifiants stables, des sévérités explicites et une corrélation séparée de la causalité ;
- UTC décrit un instant civil, un compteur monotone mesure une durée et le tick logique ordonne la simulation ;
- secrets, jetons, clés, chaînes de connexion, prompts et réponses IA brutes sont exclus des exports ;
- métriques et traces utilisent une cardinalité bornée et des politiques d’échantillonnage conservant les événements graves ;
- le logger moteur multithread écrit dans une file protégée sans rappel récursif de la journalisation ;
- un marqueur de session non fermé indique une fin non propre possible, jamais une preuve certaine de crash ;
- les paquets de diagnostic utilisent une liste fermée, des chemins relatifs, un manifeste, des empreintes et un consentement explicite ;
- ZIP est un conteneur compressé et ne constitue ni un chiffrement ni une signature ;
- le support hors ligne reste possible sans transmission distante obligatoire.

### 11.25 Automatisation Python et génération de données

- CPython 3.14.6 constitue la cible principale provisoire du paquet `asteria-tools`, avec CPython 3.13.14 comme repli ;
- `hatchling 1.31.0` et `jsonschema 4.26.0` constituent les dépendances directes minimales de qualification ;
- toute dépendance future ajoutée, supprimée ou mise à jour dans le Starter Kit doit être qualifiée avant adoption : résolution complète, environnement vierge, roues binaires des paquets natifs, contrôle des dépendances, imports et commandes utilisés, tests concernés, verrous par plateforme et série Python, inventaire de licences, SBOM et réserves explicites pour les environnements non exécutés ;
- la compatibilité doit être vérifiée avec des roues binaires sous Windows et Linux, puis sur un WSL réel avant toute garantie spécifique à WSL ;
- les piles IA lourdes conservent des environnements Python séparés ;
- les environnements utilisent `venv`, `pyproject.toml` et des verrous séparés lorsque la plateforme l’exige ;
- `pip lock` reste expérimental et ne devient obligatoire qu’après validation dans le Starter Kit ;
- les CLI utilisent `argparse`, des codes de sortie stables et des chemins `Path` confinés ;
- configurations TOML, instances JSON, checkpoints et manifestes portent une version ;
- JSON Schema Draft 2020-12 valide les échanges sans remplacer les règles métier ;
- les générateurs utilisent des RNG locaux, des graines dérivées, des identités et des ordres stables ;
- les écritures passent par staging, validation, empreintes et promotion contrôlée ;
- les processus externes reçoivent une liste d’arguments, `shell=False`, des délais et leurs codes non nuls conservés ;
- le parallélisme est borné et les résultats sont réordonnés canoniquement ;
- une reprise exige un plan identique et des empreintes valides ;
- les nouvelles tentatives sont limitées à des erreurs transitoires cataloguées ;
- chaque lot publiable possède provenance, manifeste, SHA-256, rapport et archive vérifiée ;
- Python orchestre les chapitres 26 à 28 sans acquérir d’autorité métier.

### 11.27 Direction artistique et bible visuelle

- la bible transforme des intentions perceptuelles en règles visuelles observables et versionnées ;
- formes, silhouettes, proportions, valeurs, saturation, température, matériaux, lumière, profondeur, UI et VFX partagent une grammaire commune ;
- les signaux gameplay importants restent lisibles sans dépendre de la couleur seule ;
- les matériaux sont évalués sous plusieurs éclairages et leur usure suit des causes localisées ;
- les variations culturelles, régionales, sociales et temporelles dérivent de règles communes documentées ;
- les exemples conformes, limites et non conformes rendent les règles classables par une autre personne ;
- les exceptions sont écrites, limitées, approuvées et réévaluées ;
- toute modification influençant coûts ou priorités passe par la demande de changement du chapitre 1 ;
- la validation cible une scène Godot comparative, mais aucune exécution runtime n’est revendiquée avant matérialisation des assets pilotes.

### 11.28 Références, concept art et ComfyUI

- toute collecte commence par une question visuelle et une relation explicite avec la bible ;
- inspiration, référence, concept, source de production et asset final restent des statuts distincts ;
- chaque référence retenue possède une provenance, un contexte d’usage, des droits connus ou un état bloqué ;
- les moodboards sont annotés et produisent des décisions, pas seulement une ambiance ;
- le workflow ComfyUI JSON, les modèles, custom nodes, paramètres et runs sont versionnés séparément ;
- une seed n’est reproductible qu’avec l’environnement, le graphe et les paramètres associés ;
- les custom nodes sont traités comme du code exécutable et qualifiés avant adoption ;
- les propositions sont critiquées humainement sur l’anatomie, les matériaux, la culture et la fonction ;
- une image générée ne devient jamais directement une texture, un modèle ou un asset final ;
- les sorties destinées au partage sont séparées des sources et vérifiées pour leurs métadonnées ;
- la configuration AMD Windows de référence reste non qualifiée tant qu’aucun test réel n’est exécuté ;
- le dossier consolidé transmet règles, sources modifiables, inconnues et rapport de sélection aux chapitres de production.

### 11.29 Pipeline Blender et organisation des fichiers

- Blender `5.2.0` Stable constitue la référence documentaire ; toute mise à jour future repasse par une qualification et un asset pilote ;
- aucun add-on tiers n’est obligatoire pour le chemin de référence ; une extension future est qualifiée comme du code et une dépendance de production ;
- le fichier `.blend` reste la source canonique 3D et ne se confond ni avec les caches, ni avec les exports, ni avec les livraisons ;
- les scènes utilisent le système métrique avec une unité pour un mètre ; `Unit Scale` ne sert pas à réparer une géométrie incorrecte ;
- les assets orientés regardent vers `-Y` dans Blender et arrivent vers `+Z` dans Godot par la conversion glTF, sans parent correctif ;
- origines et pivots sont fonctionnels et ne changent pas après publication sans nouvelle version ;
- les collections distinguent géométrie, rig, sockets, guides et frontière `__EXPORT` unique ;
- Link conserve l’autorité de la bibliothèque, Append crée une copie locale, et Library Override encadre les adaptations autorisées ;
- les dépendances utilisent des chemins relatifs et une réouverture sur une autre machine fait partie de la porte runtime ;
- sources, travail, bibliothèques, caches, exports, livraisons et archives occupent des chemins distincts ;
- les versions approuvées sont immuables, les sauvegardes automatiques ne sont pas des versions publiées ;
- GLB constitue la livraison par défaut, glTF séparé répond aux besoins d’inspection, et l’import direct `.blend` reste une voie Solo dépendante de Blender ;
- tout export cite source, preset, collection, empreinte et autorité de publication ;
- le cube d’un mètre vérifie échelle, orientation, pivot, marqueurs et réimportation dans Godot ;
- aucune exécution Blender, export, import Godot, réouverture multi-poste ou mesure n’est revendiquée avant matérialisation.

### 11.30 Provenance, licences et validation des assets

- aucun fichier ne devient publiable par simple présence, achat, commande, gratuité ou génération ;
- chaque asset possède un identifiant stable, une version immuable, une fiche, un statut, des dépendances et un paquet de preuves ;
- auteur, titulaire de droits, fournisseur, acquéreur et responsable de publication restent des rôles distincts ;
- droit d’auteur, droits patrimoniaux, droit moral, droits voisins, consentement, données personnelles, image et marques ne sont pas fusionnés ;
- les licences standards utilisent un identifiant exact lorsque possible ; contrats, boutiques et consentements utilisent `LicenseRef-...` ;
- commercial, modification, redistributions, attribution, territoire, durée, sous-licence, entraînement et clonage restent séparés ;
- `unknown`, une contestation ou une dépendance non publiable bloquent la livraison ;
- les transformations sont append-only et relient entrées, outils, paramètres, sorties et empreintes ;
- les chaînes IA qualifient application, extensions, modèles, poids, datasets, entrées, workflow, sorties et sélection humaine ;
- voix, image, interprétation, scan et mocap utilisent des autorisations adaptées et un stockage restreint ;
- les contrôles automatiques vérifient la structure sans prononcer de conclusion juridique ;
- la publication exige une décision humaine et un paquet de preuves haché ;
- un retrait conserve l’historique, gèle les nouvelles livraisons et crée un remplacement versionné ;
- aucune fiche réelle, licence, contrat, consentement, revue juridique ou CI de provenance n’est revendiqué avant matérialisation.

### 11.31 LOD, imposteurs et optimisation géométrique

- `AST-LOD-PILOT-SIGNAL-TOWER-001` constitue le pilote de chaîne LOD du chapitre 18 ;
- la taille écran, le FOV, la résolution, l’échelle et l’importance gameplay restent des variables séparées ;
- triangles Blender, sommets exportés, surfaces, draw calls, mémoire et temps CPU/GPU sont mesurés distinctement ;
- le LOD0 approuvé est gelé avant dérivation et toute modification invalide les niveaux, imposteurs, captures et benchmarks concernés ;
- LOD manuel, LOD automatique Godot, HLOD, imposteur, billboard, proxy d’ombre et proxy de collision ont des responsabilités distinctes ;
- Collapse, Planar et Un-Subdivide sont choisis selon la topologie, avec silhouette et signaux visuels protégés ;
- chaque niveau possède ses normales, tangentes, triangulation, UV et matériaux qualifiés ;
- `lod_bias` sert au diagnostic et ne masque pas une chaîne mal conçue ;
- les plages de visibilité utilisent des seuils cohérents et des marges d’hystérésis ;
- les fades `SELF` et `DEPENDENCIES` ne sont considérés comme doux que sous Forward+ ;
- collisions et règles gameplay ne sont jamais commandées directement par le niveau visuel ;
- les imposteurs documentent pivot, angles, atlas, alpha, padding, normales, profondeur et ombres ;
- MultiMesh, AABB, culling et occlusion sont mesurés sans devenir une optimisation globale du jeu ;
- baseline, variantes, parcours caméra, répétitions, données brutes, captures et tableau comparatif sont requis ;
- aucune amélioration runtime, mesh, atlas, GLB, scène, capture ou mesure n’est revendiquée avant matérialisation.

### 11.32 Capture de mouvement et retargeting

- `AST-MOCAP-PILOT-SCOUT-001` constitue le pilote de capture et retargeting du chapitre 21 ;
- session, prise, clip sélectionné, animation nettoyée, retargeting et animation publiée restent des états distincts ;
- les sources brutes sont immuables et séparées des dérivés de travail, exports et ressources Godot ;
- consentement, droit à l’image, modification, usage commercial, redistribution et entraînement restent des autorisations séparées ;
- contrats, identités et données personnelles restent hors du dépôt public, avec références de preuve et statuts publiables ;
- unités, axes, sol, fréquence, calibration et pose de capture sont déclarés avant toute conversion ;
- bruit, trous, dérive, échanges d’étiquettes, root, contacts, collisions et équilibre sont diagnostiqués avant filtrage ;
- les noms d’os seuls ne suffisent pas : hiérarchie, axes, roll, pose de référence et fonctions du profil sont vérifiés ;
- les différences de proportions sont traitées par chaîne, priorités de contact et corrections artistiques, jamais par une échelle uniforme ;
- `BoneMap`, `SkeletonProfile`, profils personnalisés et options d’import Godot restent versionnés par rig ;
- le retargeting runtime avec `RetargetModifier3D` reste une variante à mesurer ; les clips bakés hors runtime constituent la voie de référence ;
- root motion, phases et événements sont revérifiés après retargeting sans acquérir d’autorité gameplay ;
- la porte exige droits traçables, contacts crédibles, rythme cohérent, stabilité sur plusieurs morphologies et import Godot contrôlé ;
- aucune session, animation, donnée personnelle, GLB, bibliothèque, scène, capture, mesure ou résultat runtime n’est revendiqué avant matérialisation.

### 11.33 Cinématiques, caméras et mise en scène

- `AST-CINE-PILOT-SCOUT-RELAY-001` constitue le pilote cinématique du chapitre 22 ;
- l’intention dramatique, les beats, le storyboard, la liste de plans, le blocage, l’animatique et la séquence Godot restent des états distincts et versionnés ;
- chaque plan possède un identifiant stable, une fonction narrative, une durée candidate, une caméra, des dépendances et un statut de revue ;
- focales, FOV, projection, composition, profondeur, hauteur, direction écran, regards et raccords sont décidés selon l’information à transmettre ;
- les trajectoires de caméra utilisent des chemins et interpolations inspectables ; le bruit éventuel reste borné, désactivable et subordonné au confort ;
- la scène cinématique dérivée référence les personnages, décors et animations approuvés sans éditer directement les imports ;
- `Camera3D`, `AnimationPlayer` et un directeur limité orchestrent la lecture visuelle sans acquérir d’autorité gameplay ;
- animations, dialogue, lumière et VFX partagent une base temporelle documentée, mais leurs assets restent produits dans leurs chapitres propriétaires ;
- l’entrée, la sortie, le saut, l’annulation et l’interruption restaurent explicitement caméra, entrées, état final et contrôle du joueur ;
- les versions de revue conservent commentaires, plans concernés, décisions, responsables et historique des reprises ;
- la porte exige lecture narrative claire, rythme maîtrisé, dépendances résolues, séquence fonctionnelle dans le build et retour gameplay contrôlé ;
- aucun storyboard, animatique, asset, scène Godot, timeline, rendu, test de build, synchronisation ou mesure runtime n’est revendiqué avant matérialisation.

### 11.34 Effets visuels, particules et simulations

- `AST-VFX-PILOT-RELAY-STORM-001` constitue le pilote VFX du chapitre 23 ;
- fonction critique, renforcement secondaire et ambiance restent des couches distinctes ;
- particules GPU, particules CPU, shaders, maillages, décalques, flipbooks et caches sont choisis selon leur contrat ;
- `ParticleProcessMaterial` décrit le mouvement tandis que le matériau de dessin décrit l’apparence ;
- collisions de particules, corps physiques gameplay et `visibility_aabb` ont des responsabilités séparées ;
- populations, durées de vie, instances, pools et saturation sont bornés ;
- transparence, couverture écran, overdraw, éclairage et turbulence sont mesurés dans les vues cibles ;
- profils `low`, `reference` et `high` conservent l’information critique ;
- simulations précalculées et caches restent reliés à leur source, version, paramètres, plage et empreinte ;
- les VFX reçoivent un événement déjà décidé et n’appliquent aucune conséquence métier ;
- la porte exige lisibilité, provenance, profils, confort et mesures runtime ;
- aucun preset, shader compilé, cache, scène Godot, benchmark ou résultat runtime n’est revendiqué avant matérialisation.

### 11.35 Interface utilisateur

- `AST-UI-PILOT-CORE-SHELL-001` constitue le pilote UI du chapitre 24 ;
- `AST-UI-THEME-CORE-001` centralise tokens, types natifs, variations sémantiques, polices, icônes et `StyleBox` ;
- ancres et offsets servent aux attaches simples, tandis que les `Container` possèdent le layout de leurs enfants ;
- tailles minimales, flags de taille et ratios d’étirement sont documentés par composant ;
- menu principal, HUD, inventaire, pause et modale partagent des composants réutilisables ;
- souris, clavier et manette utilisent des profils distincts sans changer les actions métier ;
- les actions `ui_*` restent réservées à la navigation et au focus ;
- chaque écran possède un focus initial, des voisins explicites lorsque nécessaire et une restauration après fermeture ;
- les événements GUI consommés ne déclenchent pas simultanément le gameplay ;
- ratios, zones sûres, échelle UI, textes longs, pseudo-localisation et pseudo-RTL appartiennent à la campagne de qualification ;
- modèles de vue et requêtes UI restent séparés de l’état et des transactions autoritaires ;
- la porte exige cohérence visuelle, navigation complète, adaptation, dépendances qualifiées et mesures runtime ;
- aucun thème, composant, écran, police, capture, test multi-résolution ou benchmark n’est revendiqué avant matérialisation.


### 11.36 Expérience utilisateur et accessibilité visuelle

- `AST-UX-PILOT-CORE-SHELL-001` constitue le pilote UX et accessibilité visuelle du chapitre 25 ;
- les cinq écrans de `AST-UI-PILOT-CORE-SHELL-001` sont évalués par tâches, profils et preuves séparées ;
- hiérarchie, charge cognitive, densité et divulgation progressive sont définies selon la fonction de l’information ;
- les critères WCAG 2.2 servent de références mesurables sans constituer une certification automatique du jeu ;
- contraste, taille, reflow, focus et cibles sont mesurés dans les contextes de rendu réels ;
- toute signification portée par la couleur possède un canal redondant par texte, forme, icône, motif ou position ;
- les profils de contraste, texte, couleur, mouvement et focus sont composables et n’exigent aucun diagnostic ;
- le mouvement est inventorié par fonction ; la variante réduite conserve état final, information critique et disponibilité des actions ;
- erreurs, confirmations, annulation, retour, retry et undo possèdent des contrats distincts et récupérables ;
- les tests utilisent tâches versionnées, fixtures, consentements séparés, observations brutes et interprétations révisables ;
- une personne ou un petit panel ne représente jamais tous les joueurs ; toute conclusion cite son périmètre et ses limites ;
- identités, enregistrements et données sensibles restent hors du dépôt public ;
- la porte exige preuves techniques, parcours de tâches, retests, confidentialité et mesures runtime ;
- aucun profil, mesure, participant, session, rapport, benchmark ou résultat runtime n’est revendiqué avant matérialisation.

### 11.37 Voix, bruitages, ambiances et musique

- `AST-AUDIO-PILOT-RELAY-STORM-001` constitue le pilote audio du chapitre 26 ;
- prises brutes, sources générées ou licenciées, sessions de travail, masters, exports runtime et caches importés restent des états distincts ;
- voix, SFX, ambiances, musique et UI sont classés selon fonction, spatialisation, durée, priorité et stratégie de lecture ;
- toute autorisation de voix sépare enregistrement, montage, exploitation, redistribution, entraînement et clonage ;
- fréquences, profondeur PCM, canaux, compression, loudness, crête vraie, mémoire, polyphonie et latence restent des dimensions séparées ;
- les boucles conservent points en échantillons, continuité, crossfade éventuel et métadonnées de transition ;
- les variantes utilisent plusieurs sources, des écarts bornés et une mémoire anti-répétition ;
- `AudioStreamPlayer` porte les flux non positionnels et `AudioStreamPlayer3D` les sources spatiales qualifiées ;
- les bus `Music`, `Voice`, `SFX`, `Ambience` et `UI` structurent effets, snapshots, ducking et réglages ;
- zones, réverbération, atténuation, directionnalité, Doppler et auditeur restent des responsabilités de présentation ;
- la fin d’un flux, un beat ou une analyse de spectre ne possède aucune autorité gameplay ;
- la porte exige provenance, qualité artistique, intégrité technique, loudness, crête vraie, concurrence, mémoire, latence et tests de plateforme ;
- aucun enregistrement, asset généré, master, export, bus, scène, rapport ou benchmark n’est revendiqué avant matérialisation.

### 11.38 Synchronisation labiale et animation faciale

- `AST-FACE-PILOT-RELAY-DIALOGUE-001` constitue le pilote facial du chapitre 27 ;
- la voix approuvée, la transcription, le profil linguistique, le rig facial, les timings et les courbes restent des dépendances versionnées distinctes ;
- graphèmes, phonèmes, allophones, visèmes et silences ne sont jamais confondus ;
- `AST-FACE-VISEME-SET-001` définit un jeu minimal extensible après tests par langue, personnage et distance ;
- pose neutre, mâchoire, lèvres, langue, yeux, sourcils, expressions et correctifs utilisent des canaux séparés et composables ;
- les alignements forcés et analyses automatiques restent des brouillons jusqu’à revue humaine ;
- TextGrid, lexiques, mappings et timings portent une origine temporelle liée à l’export audio runtime approuvé ;
- coarticulation, anticipation, maintien, relâchement, priorités et saturation sont versionnés par profil ;
- regard, clignements, saccades, tête et gestes soutiennent l’acting sans suivre mécaniquement chaque phonème ;
- `AnimationPlayer` conserve les animations sources et `AnimationTree` pilote les mélanges actifs avec filtres de pistes ;
- les profils `hero_close_up`, `gameplay_mid` et `crowd_low` réduisent canaux et fréquence sans changer la voix ni l’autorité narrative ;
- toute nouvelle prise ou locale invalide les timings dépendants et exige un profil linguistique qualifié ;
- la porte exige intelligibilité, acting, compatibilité du rig, droits, stabilité multi-distance et mesures runtime ;
- aucune forme, annotation, animation, scène, capture ou mesure n’est revendiquée avant matérialisation.

### 11.39 Importation et intégration dans Godot

- `AST-IMPORT-PILOT-SCOUT-RELAY-001` constitue le pilote d’import et d’intégration du chapitre 28 ;
- GLB constitue la livraison 3D par défaut ; glTF séparé, `.blend`, FBX et OBJ restent des variantes encadrées par une matrice format-usage ;
- source canonique, livraison, sidecar `.import`, cache `.godot/imported`, scène importée et scène d’intégration restent des états distincts ;
- les fichiers `<asset>.import` sont versionnés tandis que `.godot/` reste un cache régénérable exclu du dépôt ;
- `AST-IMPORT-PROFILE-STATIC-001`, `AST-IMPORT-PROFILE-CHARACTER-001` et `AST-IMPORT-PROFILE-ANIM-001` portent les profils initiaux ;
- les scènes importées sont considérées comme des surfaces générées ; héritage, composition et ressources externes protègent les personnalisations Godot ;
- `AST-MAT-REMAP-SCOUT-001` et `AST-SOCKET-PROFILE-SCOUT-001` encadrent matériaux, sockets et dépendances ;
- squelettes, skins, blendshapes, animations, collisions, LOD et métadonnées sont comparés à des manifestes versionnés ;
- les scripts `EditorScenePostImport` restent idempotents, bornés, sans réimportation récursive et sans exécution dynamique issue des métadonnées ;
- une réimportation conserve baseline, candidate, changements attendus, diff structurel et contrôle de la scène d’intégration ;
- l’import, un suffixe, un socket, une animation ou une métadonnée n’acquiert aucune autorité gameplay ;
- la porte exige import propre, réimportation déterministe, personnalisations préservées, revue artistique, droits et mesures runtime ;
- aucun asset, preset, sidecar, scène, remap, script exécuté, rapport, capture ou benchmark n’est revendiqué avant matérialisation.


### 11.40 Validation technique et artistique des assets

- `AST-ASSET-GATE-SCOUT-RELAY-001` constitue le pilote de porte qualité du chapitre 29 ;
- chaque décision vise un `asset_id`, une version candidate, une empreinte, un profil et un contexte d’usage ;
- `AST-ASSET-QA-CHECKLIST-001` compose un socle universel avec des extensions par famille ;
- les états distinguent brouillon, revue, blocages techniques ou juridiques, corrections, dérogations, acceptation et retrait ;
- propriétaire, revue technique, revue artistique, droits et publication restent des rôles séparés même en Mode Solo ;
- provenance, licence, redistribution et consentement constituent une précondition indépendante de la qualité visuelle ;
- géométrie, UV, matériaux, textures, rigs, skinning, blendshapes, animations, collisions, sockets et LOD utilisent des règles versionnées ;
- VFX, UI et audio restent validés selon les contrats de leurs chapitres propriétaires ;
- `AST-ASSET-QA-SCENE-001` regroupe des fixtures neutres d’échelle, matériaux, animation, collision, sockets et LOD ;
- les moniteurs Godot décrivent la scène complète et restent séparés des statistiques du contenu source ;
- chauffe, répétitions, baseline, tolérances, renderer, résolution et caméra sont enregistrés avec les mesures ;
- la revue artistique cite la bible, les références approuvées, le contexte et les preuves visuelles ;
- constats, sévérités, dérogations, corrections et décisions utilisent des identifiants stables et un historique append-only ;
- une correction produit toujours une nouvelle révision candidate et relance les contrôles affectés plus la non-régression ;
- une dérogation possède portée, propriétaire, justification, expiration et plan de correction ;
- un contrôle automatique sans blocker conduit à `ART_REVIEW_REQUIRED`, jamais à une acceptation artistique ;
- l’acceptation finale exige droits approuvés, blockers techniques nuls, preuves Godot complètes, revue artistique et dérogations valides ;
- le chapitre 30 recevra les contrats d’entrée, de sortie et de codes sans reprendre la décision artistique ;
- aucun asset, profil, scène, rapport, capture, mesure, revue ou benchmark n’est revendiqué avant matérialisation.

### 11.41 Serveurs dédiés et sécurité réseau

- l’export dédié Godot reste distinct du client et ne crée aucun joueur local ;
- `dedicated_server`, `--headless` et l’argument utilisateur `--server` possèdent des rôles distincts ;
- code installé, configuration, credentials, état durable, journaux et releases occupent des zones séparées ;
- l’identité système est dédiée, non privilégiée et limitée aux chemins, familles réseau et ports nécessaires ;
- le plan de données expose uniquement le port UDP ENet déclaré ; administration, sauvegardes et métriques restent séparées ;
- `SceneMultiplayer` authentifie avant admission et conserve `allow_object_decoding` désactivé pour les sources non fiables ;
- tickets, tailles, rejeux, cadences, concurrence, coût et amplification possèdent des bornes explicites ;
- liveness, readiness, admission et drainage restent quatre états distincts ;
- les journaux sont structurés et expurgés, les métriques ont une cardinalité bornée et aucun des deux n’acquiert d’autorité métier ;
- une mise à jour utilise releases immuables, compatibilité d’état, drainage, sauvegarde fermée et rollback vérifié ;
- alertes, empreintes et scans ouvrent un diagnostic sans constituer une preuve automatique de compromission ou une certification ;
- tout scan futur exige une cible isolée, une autorisation écrite et un périmètre déclaré ;
- aucun build, hôte, pare-feu, service, conteneur, campagne d’abus, scan, restauration ou exercice d’incident n’est revendiqué avant matérialisation.

### 11.42 DevOps et intégration continue

- `main` reste la branche intégrée ; les changements passent par branches courtes, pull requests et contrôles requis ;
- les scripts canoniques versionnés portent la logique, tandis que les workflows orchestrent événements, permissions, matrices et artefacts ;
- un événement non fiable ne reçoit ni secret, ni permission d’écriture, ni environnement protégé ;
- version produit, commit, run, tentative, identifiant de build et empreinte d’artefact restent des identités distinctes ;
- les actions externes sont inventoriées, qualifiées et épinglées avant adoption ;
- les matrices déclarent plateforme, rôle, caractère requis, délai et politique d’échec ;
- un cache reste reconstructible et ne remplace ni source canonique, ni artefact, ni preuve ;
- chaque build travaille dans un staging propre et confiné, puis produit manifeste fermé et empreintes ;
- construction et promotion sont séparées : la promotion réutilise les mêmes octets vérifiés au lieu de reconstruire ;
- secrets, environnements protégés et OIDC ne sont disponibles que dans des jobs explicitement autorisés ;
- délais, concurrence, annulation et retries transitoires sont bornés, et l’échec initial reste visible ;
- reproductibilité procédurale et identité binaire sont distinguées ;
- une reconstruction depuis un clone neuf est requise avant toute revendication runtime ;
- aucun workflow, build, test runtime, package, attestation, secret, runner ou déploiement n’est revendiqué avant matérialisation.

### 11.43 Sauvegardes, migrations et reprise après incident

- les actifs critiques possèdent identité stable, autorité, propriétaire, sensibilité, dépendances et ordre de restauration ;
- sauvegarde, réplication, snapshot, synchronisation, export logique et archive restent des mécanismes distincts ;
- les caches, index et données dérivées restent reconstructibles et ne deviennent pas autoritaires ;
- RPO et RTO sont des objectifs associés à un service minimal observable, jamais des garanties sans exercice ;
- chaque génération utilise un staging propre, une identité immuable, un manifeste fermé, des tailles et des empreintes ;
- une tentative échouée ou quarantinée ne remplace jamais la dernière génération vérifiée ;
- copies locales, hors site et immuables utilisent des supports, identités et domaines de panne distincts ;
- le dépôt source, les objets externes, les builds retenus, les bases, services, secrets et données joueurs sont inventoriés séparément ;
- SQLite exige une fermeture qualifiée ou un mécanisme de backup cohérent ; PostgreSQL est restauré dans une base neuve ;
- les volumes de conteneur ne sont pas assimilés aux images et suivent la cohérence de leur moteur de données ;
- la récupération de secrets, leur révocation et leur rotation restent séparées des archives de données ;
- toute restauration commence dans un environnement isolé, suit un graphe de dépendances et exécute des contrôles structurels et métier ;
- les migrations sont immuables, versionnées, préparées sur des candidats et validées avant remplacement ;
- rollback applicatif et restauration de données sont gouvernés par une matrice de compatibilité ;
- exercices, mesures RPO/RTO, écarts, actions correctives et retests conservent une preuve append-only ;
- aucun job, stockage, clé, bundle, dump, sauvegarde, restauration, migration, mesure ou exercice runtime n’est revendiqué avant matérialisation.

### 11.44 Accessibilité du produit complet

- la matrice d’accessibilité part de tâches observables et de barrières, jamais de diagnostics supposés ;
- commandes, visuel, audio, cognition, motricité et contraintes temporelles possèdent des contrôles séparés mais composables ;
- les réglages sont disponibles dès le premier démarrage, enregistrés dans des profils réversibles et séparés de l’état gameplay ;
- le remapping agit sur des actions nommées, détecte les conflits et fournit des alternatives aux maintiens, répétitions et combinaisons ;
- couleur, son, vibration, texte, icône et mouvement sont des canaux redondants ; aucun canal unique ne porte une information critique ;
- texte, contraste, focus, tailles de cible, reflow, mouvement, caméra et photosensibilité sont vérifiés sur des parcours représentatifs ;
- sous-titres, captions, mixage, indices visuels, description audio, TTS et lecteurs d’écran restent des capacités distinctes ;
- difficulté, rythme, limites temporelles, aides motrices, sauvegardes, checkpoints et récupération sont réglables sans déplacer l’autorité métier ;
- les contrôles automatiques, revues spécialisées, technologies d’assistance et sessions utilisateurs fournissent des preuves complémentaires ;
- consentement, minimisation, confidentialité, retrait et compensation encadrent toute session avec des personnes ;
- une déclaration publique cite le build, la plateforme, les fonctions vérifiées, les limites connues et les preuves datées ;
- WCAG 2.2 et les Xbox Accessibility Guidelines servent de références et d’objectifs mesurables, sans certification automatique du jeu ;
- aucune fonction, session, compatibilité périphérique, intégration de technologie d’assistance ou conformité n’est revendiquée avant matérialisation.

## 24. Erreurs à ne pas reproduire

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
- ne pas livrer les outils de production dans le runtime ;
- ne pas écouter sur `0.0.0.0` ou `::` par défaut ;
- ne pas stocker un jeton dans `res://` ou dans le dépôt ;
- ne pas confondre authentification, autorisation et chiffrement ;
- ne pas utiliser un identifiant de tâche comme permission ;
- ne pas utiliser `TLSOptions.client_unsafe()` en production ;
- ne pas ouvrir directement un chemin fourni par le client ;
- ne pas journaliser `Authorization`, jetons ou payloads complets ;
- ne pas utiliser `random` pour un jeton de sécurité ;
- ne pas inclure une clé privée dans le package client ;
- ne pas publier sans inventaire des dépendances et SBOM ;
- ne pas présenter un hachage seul comme preuve d’origine ;
- ne pas contourner un refus de sécurité par un repli ;
- ne pas conserver le debug de développement en production ;
- ne pas utiliser le nom affiché ou un index comme identité de personnage ;
- ne pas modifier une `CharacterDefinition` partagée comme état vivant ;
- ne pas sauvegarder un nœud, une `Resource` ou une statistique dérivée comme autorité ;
- ne pas faire lire `Input` directement au personnage ;
- ne pas confondre contrôleur, possession et identité ;
- ne pas initialiser le runtime après l’entrée du nœud dans l’arbre ;
- ne pas enregistrer deux acteurs actifs pour la même identité ;
- ne pas traiter `queue_free()` comme une suppression métier ;
- ne pas appliquer une section de personnages avant validation complète ;
- ne pas placer relations, famille, agent, combat ou compétences dans `CharacterRuntimeState` ;
- ne pas stocker une relation sociale sur un nœud actif ;
- ne pas utiliser un nom affiché comme clé de relation ;
- ne pas forcer la symétrie entre deux perceptions ;
- ne pas persister un booléen d’amitié contradictoire avec les axes ;
- ne pas laisser un axe ou un delta hors bornes ;
- ne pas accepter un changement sans cause ni provenance ;
- ne pas utiliser l’heure système comme ordre de simulation ;
- ne pas conserver un historique social illimité ;
- ne pas retourner les collections internes mutables ;
- ne pas créer toutes les paires possibles de personnages ;
- ne pas valider une relation uniquement contre les personnages actifs ;
- ne pas appliquer une section sociale avant validation complète ;
- ne pas déduire la parenté depuis l’affinité ;
- ne pas laisser une sortie IA modifier directement l’état social ;
- ne pas utiliser un nom affiché comme identité familiale ;
- ne pas stocker les liens familiaux sur un nœud actif ;
- ne pas déduire la filiation depuis une valeur sociale ;
- ne pas persister fratries, générations ou index secondaires ;
- ne pas insérer une filiation sans détection de cycle ;
- ne pas traiter un dépassement de parcours comme une absence de cycle ;
- ne pas orienter une union qui exige une paire canonique ;
- ne pas dater un lien avec l’heure système ;
- ne pas accepter un intervalle terminé avant son début ;
- ne pas valider une identité uniquement contre les personnages actifs ;
- ne pas retourner les collections internes du graphe ;
- ne pas charger directement dans le graphe actif ;
- ne pas laisser une sortie IA créer un lien sans commande validée ;
- ne pas mélanger filiation et succession politique ;
- ne pas insérer un bloc de code significatif sans expliquer son rôle, ses types, paramètres, retours, effets, invariants, déroulement et résultat attendu ;
- ne pas considérer une phrase générique comme une explication suffisante d’un bloc complexe ;
- ne pas démarrer un nouveau chapitre tant que les corrections pédagogiques prioritaires des chapitres précédents ne sont pas fermées ;
- ne pas construire le PDF à chaque chapitre ;
- ne pas laisser un agent, une animation ou un raycast muter directement la santé ;
- ne pas utiliser `hash()` comme départage reproductible d’initiative ;
- ne pas déduire une équipe depuis une relation sociale ou une proximité spatiale ;
- ne pas confondre portée logique et ligne de vue physique ;
- ne pas émettre un événement de combat avant le commit autoritaire ;
- ne pas modifier le dépôt actif avant validation complète des candidats ;
- ne pas conserver des références mutables dans l’historique ou la file ;
- ne pas sérialiser un entier 64 bits directement dans JSON sans représentation sûre ;
- ne pas charger directement dans les affrontements actifs ;
- ne pas persister raycasts, commandes en attente, caches ou présentation ;
- ne pas écrire directement dégâts, santé ou états depuis une définition de compétence ;
- ne pas stocker charges ou recharge dans une `Resource` de conception partagée ;
- ne pas utiliser un `Timer` ou l’heure système comme recharge autoritaire ;
- ne pas consommer un coût avant la validation et la préparation de tous les effets requis ;
- ne pas committer séparément coût, effets et état de compétence ;
- ne pas charger un script, une classe ou une méthode depuis une définition externe ;
- ne pas traiter une prévisualisation comme validation autoritaire ;
- ne pas persister plans, réservations, candidats, cibles dérivées ou caches ;
- ne pas utiliser un nom affiché comme identité de compétence ;
- ne pas modifier une `ItemDefinition` partagée comme état d’instance ;
- ne pas confondre propriété métier et garde matérielle ;
- ne pas fusionner des objets individualisés ou des lots d’origines différentes ;
- ne pas retirer une entrée de la source avant validation complète de la destination ;
- ne pas autoriser un transfert sans politique d’accès explicite ;
- ne pas transférer directement un objet encore équipé ;
- ne pas laisser le combat écrire directement la durabilité ;
- ne pas laisser l’inventaire écrire progression, charges ou recharge d’une compétence ;
- ne pas persister masse dérivée, tris, filtres ou sélection d’interface ;
- ne pas laisser une sortie IA modifier directement la réputation d’un objet ;
- ne pas retenter automatiquement une utilisation partiellement résolue ;
- ne pas placer les commandes de validation documentaire ou la procédure QA dans un chapitre destiné au lecteur ;
- ne pas placer la prochaine étape, le chemin ou le niveau du chapitre suivant dans le chapitre publié ;
- ne pas terminer un chapitre de système sans synthèse opérationnelle de `Project Asteria` ;
- ne pas utiliser de `float` comme montant monétaire autoritaire ;
- ne pas modifier un portefeuille depuis l’interface, un agent ou une sortie IA ;
- ne pas créer de récompense sans portefeuille émetteur explicite ;
- ne pas faire confiance à un prix ou un total fourni par l’appelant ;
- ne pas committer séparément paiement et transfert d’objet ;
- ne pas stocker un prix dans `ItemDefinition` ;
- ne pas changer l’identité d’un retry économique ;
- ne pas convertir implicitement deux devises ;
- ne pas utiliser l’heure système ou un `Timer` comme horloge autoritaire du monde ;
- ne pas utiliser un nombre de nœuds actifs comme population écologique ;
- ne pas laisser un résidu dépasser `ticks_per_day - 1` ;
- ne pas rejouer chaque tick manqué lors d’un rattrapage ;
- ne pas modifier une population lors d’une simple matérialisation ;
- ne pas laisser l’économie écrire une réserve écologique ou l’écologie fixer un prix ;
- ne pas réduire une réserve avant la préparation du rendement d’inventaire ;
- ne pas appliquer deux fois une mort, une naissance ou une récolte portant la même identité ;
- ne pas laisser une sortie IA remplacer directement populations, ressources ou horloge ;
- ne pas utiliser un nom affiché comme identité institutionnelle ;
- ne pas déduire une adhésion, un rang ou un droit depuis une relation sociale ;
- ne pas modifier en place une version de loi promulguée ;
- ne pas autoriser une action protégée par simple absence de règle ;
- ne pas traiter une accusation ou un rapport comme un verdict ;
- ne pas copier un objet, une transaction ou un événement comme preuve autoritaire ;
- ne pas laisser une sortie IA promulguer, juger ou condamner ;
- ne pas appliquer séparément amende, confiscation, restriction ou changement de domaine ;
- ne pas dater adhésions, mandats ou lois avec l’heure système ;
- ne pas émettre un événement politique ou judiciaire avant commit ;

- ne pas utiliser un nœud ou une scène comme autorité d’un bâtiment ;
- ne pas déduire un droit foncier depuis une relation sociale ;
- ne pas consommer matériaux ou coûts avant le commit commun ;
- ne pas confondre livraison de matériaux et travail de chantier ;
- ne pas utiliser un `float` comme progression autoritaire ;
- ne pas stocker un prix ou un solde dans un bâtiment ;
- ne pas produire les extrants séparément de la consommation des intrants ;
- ne pas dater entretien ou chantier avec le temps réel ;
- ne pas autoriser une action en absence de décision politique `ALLOW` ;
- ne pas laisser une sortie IA construire, produire ou entretenir directement ;

- ne pas utiliser un texte affiché comme identité de quête ;
- ne pas traiter un événement comme une vérité narrative complète ;
- ne pas exécuter une condition issue des données ;
- ne pas achever une quête avant la préparation de ses conséquences ;
- ne pas révéler une entrée sur une décision indéterminée ;
- ne pas confondre connaissance découverte et fait global ;
- ne pas laisser une sortie IA valider un objectif ;
- ne pas dater une quête avec le temps réel ;
- ne pas charger directement dans les dépôts narratifs actifs ;
- ne pas persister un index vectoriel dérivé ;

- ne pas écrire directement un fichier canonique depuis un bouton d’éditeur ;
- ne pas modifier une scène ouverte sans transaction d’annulation ;
- ne pas utiliser un chemin ou un libellé comme identité de contenu ;
- ne pas exécuter un nom de méthode provenant des données ;
- ne pas mélanger source canonique, artefact généré et cache ;
- ne pas calculer une empreinte depuis le temps réel ou une sérialisation instable ;
- ne pas publier un lot sans staging, vérification et promotion ;
- ne pas promouvoir automatiquement une sortie IA ;
- ne pas lancer un scan ou une réimportation pendant un import actif ;
- ne pas donner au plugin d’éditeur une autorité runtime ;

- ne pas présenter `godot --test` comme le runner des scripts GDScript du projet ;
- ne pas laisser le framework de test entrer dans les dépendances runtime ;
- ne pas utiliser l’heure système, un RNG global ou un ordre de dictionnaire comme oracle ;
- ne pas partager un fixture mutable entre deux tests ;
- ne pas lancer un serveur IA ou réseau réel dans une suite déterministe ;
- ne pas comparer un `float` par égalité stricte lorsqu’une tolérance appartient au contrat ;
- ne pas générer un golden file depuis le test qui doit le vérifier ;
- ne pas utiliser un retry automatique pour masquer un test instable ;
- ne pas oublier de borner les attentes de signaux, le nombre de ticks et les files simulées ;
- ne pas considérer une couverture élevée comme preuve de qualité ou de correction métier ;
- ne pas employer les calques `durée murale`, `temps mur`, `temps mural` ou `temps horloge` ; utiliser `durée réelle (durée de l’horloge système)` et `horloge système` selon le contexte ;

- ne pas donner aux journaux, métriques ou traces une autorité métier ;
- ne pas utiliser l’horloge système pour mesurer une durée ; utiliser un compteur monotone ;
- ne pas journaliser de mot de passe, jeton, clé, chaîne de connexion, prompt ou réponse IA brute ;
- ne pas utiliser un identifiant d’instance, un chemin ou un message libre comme label de métrique ;
- ne pas écrire directement depuis un callback `Logger` multithread ni rappeler la journalisation depuis ce callback ;
- ne pas exporter récursivement `user://` ; utiliser une liste fermée et des chemins relatifs ;
- ne pas présenter un marqueur de session comme une preuve certaine de crash ;
- ne pas présenter une archive ZIP comme chiffrée ou signée ;
- ne pas échantillonner les événements `ERROR`, `FATAL` ou de sécurité ;
- ne pas reconstruire un état autoritaire depuis un journal de diagnostic ;

- ne pas utiliser un environnement Python global pour le projet ;
- ne pas présenter `pip freeze` comme un verrou résolu ;
- ne pas traiter `pip lock` comme une interface stabilisée tant que son statut reste expérimental ;
- ne pas adopter une dépendance future du Starter Kit sans qualification explicite des versions Python, plateformes, roues natives, transitives, licences et usages réellement concernés ;
- ne pas accepter une configuration TOML ou JSON sans limite de taille et validation de version ;
- ne pas construire une commande externe par concaténation ni avec `shell=True` ;
- ne pas laisser un chemin configuré sortir du workspace autorisé ;
- ne pas utiliser le RNG global ou `hash()` pour une génération reproductible ;
- ne pas dépendre de l’ordre du système de fichiers ou de l’ordre de fin des tâches parallèles ;
- ne pas écrire directement dans les sources ou sorties publiées ; utiliser staging, validation et promotion ;
- ne pas reprendre une tâche sur la seule présence d’un fichier ; vérifier plan et empreinte ;
- ne pas retenter sans limite ni retenter une erreur de schéma, d’intégrité ou d’autorité ;
- ne pas lancer un pool non borné ni utiliser `ProcessPoolExecutor` avec des fonctions non sérialisables ;
- ne pas considérer SHA-256 comme une preuve d’auteur ou ZIP comme un chiffrement ;
- ne pas laisser l’orchestrateur Python modifier directement un état métier Godot ;

- ne pas traiter un moodboard comme une bible visuelle ;
- ne pas employer des adjectifs artistiques sans critère observable ;
- ne pas maximiser détail, saturation ou contraste sur chaque élément ;
- ne pas coder une information essentielle par la couleur seule ;
- ne pas valider un matériau sous un seul éclairage avantageux ;
- ne pas distribuer usure et salissures sans cause ;
- ne pas réduire les régions ou cultures à une recoloration aléatoire ;
- ne pas modifier la bible sans version, propriétaire et conséquences identifiées ;
- ne pas accepter une dérogation uniquement orale ;
- ne pas déclarer la direction validée dans Godot avant les assets pilotes et la scène comparative ;

- ne pas collecter des images sans question visuelle ;
- ne pas employer une référence dont la provenance ou les droits sont inconnus ;
- ne pas installer automatiquement tous les custom nodes manquants ;
- ne pas considérer une seed fixe comme une garantie d’identité ;
- ne pas modifier plusieurs variables dans une même expérience non tracée ;
- ne pas sélectionner une proposition uniquement parce qu’elle est spectaculaire ;
- ne pas présenter une image générée comme un asset final ;
- ne pas ignorer les incohérences anatomiques, matérielles ou culturelles ;
- ne pas publier une image sans contrôler les métadonnées de workflow qu’elle contient ;
- ne pas accumuler des variantes sans budget ni règle d’arrêt ;

- ne pas utiliser `Unit Scale` comme réparation d’une géométrie incorrecte ;
- ne pas ajouter un parent tourné à 90 degrés pour masquer une mauvaise convention d’axes ;
- ne pas appliquer toutes les transformations sans examiner rigs, contraintes et hiérarchies ;
- ne pas exporter une sélection manuelle lorsque la collection `__EXPORT` est le contrat ;
- ne pas versionner des chemins personnels absolus vers des textures ou bibliothèques ;
- ne pas modifier une donnée liée comme si elle était possédée localement ;
- ne pas versionner caches, temporaires ou sauvegardes automatiques comme sources ;
- ne pas écraser une version approuvée ;
- ne pas livrer uniquement un `.blend` en Studio sans GLB contrôlé et manifeste ;
- ne pas installer automatiquement un add-on inconnu ;
- ne pas déplacer le pivot après publication sans nouvelle version et validation ;

- ne pas considérer qu’un asset gratuit est libre ou redistribuable ;
- ne pas déduire l’étendue des droits d’une facture ou d’un paiement ;
- ne pas utiliser `royalty-free`, `free`, `open` ou `AI-generated` comme identifiant de licence ;
- ne pas fusionner auteur, titulaire, fournisseur et plateforme ;
- ne pas publier une sortie générée sans qualifier modèles, entrées, workflow et conditions ;
- ne pas déduire clonage vocal ou entraînement d’une autorisation générale d’enregistrement ;
- ne pas effacer un asset contesté avec ses preuves ;
- ne pas accepter un asset dont une dépendance reste bloquée ;
- ne pas stocker contrats, signatures ou données personnelles dans un dépôt public ;
- ne pas écraser une licence ancienne sans nouvelle version et requalification ;
- ne pas confondre empreinte et preuve de validité juridique ;
- ne pas laisser une décision automatique remplacer la revue humaine ;

- ne pas remplacer une référence web cliquable par une URL brute, une URL entre accents graves ou un bloc de code ;
- ne pas oublier la mise à jour de ce fichier.

- ne pas approuver un LOD sur son seul ratio de triangles ;
- ne pas utiliser une distance unique sans FOV, résolution et taille écran ;
- ne pas laisser des niveaux partager des origines ou AABB incohérentes ;
- ne pas dépendre d’un fondu Forward+ sur Mobile ou Compatibility ;
- ne pas lier directement collision ou autorité gameplay au LOD visuel ;
- ne pas créer un imposteur sans padding, contexte d’alpha et revue multi-angle ;
- ne pas comparer deux benchmarks qui changent plusieurs variables à la fois ;
- ne pas forcer une AABB immense pour masquer un défaut de culling ;
- ne pas présenter le LOD automatique comme approuvé sans inspection humaine ;

- ne pas exporter contrôleurs et mécanismes comme squelette de déformation ;
- ne pas corriger un mauvais roll par une contrainte compensatoire ;
- ne pas modifier la rest pose après bind sans nouvelle version et revalidation ;
- ne pas approuver les poids automatiques sans grille de poses ;
- ne pas limiter les influences sans nettoyage, normalisation et comparaison ;
- ne pas miroiter aveuglément une région asymétrique ;
- ne pas donner à un socket ou `BoneAttachment3D` une autorité gameplay ;
- ne pas supposer que des noms identiques suffisent au retargeting ;
- ne pas activer `override_pose` pour une simple attache visuelle ;
- ne pas valider un rig uniquement en pose neutre ;

- ne pas enregistrer chaque contrôleur à chaque image sans distinguer clés artistiques et bake ;
- ne pas utiliser l’Auto Key sans Keying Set, signal visible et revue des canaux créés ;
- ne pas accélérer une marche pour fabriquer une course ;
- ne pas mélanger des cycles sans aligner phases et contacts ;
- ne pas utiliser l’IK procédurale pour masquer un glissement présent dans la source ;
- ne pas laisser le root motion décider directement collision ou déplacement autoritaire ;
- ne pas appliquer dégâts, consommation ou progression depuis une piste de méthode ;
- ne pas éditer directement une scène importée comme surface d’intégration ;
- ne pas étiqueter un clip absolu comme couche additive sans pose de référence ;
- ne pas employer un fondu unique pour toutes les transitions ;
- ne pas valider les animations uniquement comme clips isolés ;
- ne pas supposer qu’un graphe complexe compense des poses, arcs ou contacts faibles ;

- ne pas considérer une autorisation d’enregistrement comme une autorisation générale de modification, redistribution ou entraînement ;
- ne pas stocker contrats, identités, vidéos ou signaux personnels dans le dépôt public ;
- ne pas modifier une prise brute ni écraser son empreinte ;
- ne pas traiter `free`, `royalty-free` ou un paiement comme un identifiant de licence ;
- ne pas choisir une technologie de capture sans besoin, contacts, confidentialité et coût de correction explicites ;
- ne pas confondre fréquence d’échantillonnage et FPS d’auteur ;
- ne pas supposer que la pose de capture est la rest pose du rig cible ;
- ne pas mapper deux squelettes sur les seuls noms d’os ;
- ne pas copier des composantes Euler entre axes locaux différents ;
- ne pas employer un filtre global identique sur root, pieds, mains et colonne ;
- ne pas interpoler un long trou comme s’il avait été mesuré ;
- ne pas utiliser l’IK pour masquer un glissement présent dans la source, l’échelle ou le root ;
- ne pas appliquer un ratio de taille uniforme à toutes les translations locales ;
- ne pas copier doigts ou visage sans source, synchronisation, mapping et droits compatibles ;
- ne pas traiter un import Godot terminé ou un auto-mapping comme une approbation ;
- ne pas valider un retargeting multi-rigs sur une seule morphologie ou une seule caméra ;
- ne pas laisser une piste mocap, un événement ou le root motion modifier directement le gameplay ;
- ne pas déclarer contacts, stabilité, performance ou coût runtime sans exécution et mesures réelles ;

- ne pas ajouter un plan dépourvu de fonction narrative vérifiable ;
- ne pas franchir l’axe de mise en scène sans préparation ou nouveau plan d’établissement ;
- ne pas utiliser une focale ou un FOV extrême pour masquer un mauvais placement ;
- ne pas éditer directement une scène importée comme source de la cinématique ;
- ne pas laisser une piste de méthode ou la timeline modifier directement l’état gameplay autoritaire ;
- ne pas désactiver les entrées ou la caméra de gameplay sans restauration garantie ;
- ne pas traiter un dialogue, une lumière ou un VFX placeholder comme un asset final approuvé ;
- ne pas démarrer la séquence avant que ses dépendances obligatoires soient chargées et validées ;
- ne pas valider une cinématique uniquement dans l’éditeur, sur un seul ratio d’image ou sans variante de confort ;
- ne pas déclarer rythme, synchronisation, stabilité du build ou coût runtime sans exécution et mesures réelles ;


- ne pas laisser une particule, un shader, un décalque ou un cache appliquer une règle gameplay ;
- ne pas dimensionner un effet sur `amount` seul sans considérer durée, instances et couverture d’écran ;
- ne pas empiler des quads transparents sans revue de l’overdraw en vue rapprochée ;
- ne pas supposer qu’un `PhysicsBody3D` suffit aux collisions de particules GPU ;
- ne pas conserver une `visibility_aabb` par défaut lorsque les trajectoires la dépassent ;
- ne pas augmenter `preprocess` ou `fixed_fps` sans besoin et mesure ;
- ne pas instancier sans limite des scènes VFX courtes et répétitives ;
- ne pas déclarer un profil de qualité unique valable pour toutes les plateformes ;
- ne pas accepter un cache précalculé sans source, manifeste, version et procédure de régénération ;
- ne pas promouvoir un placeholder cinématique en asset final sans provenance, confort, profils et budget ;
- ne pas laisser un bouton, un slider, une ligne de liste ou un tween modifier directement un état métier ;
- ne pas positionner manuellement un enfant dont le parent est un `Container` ;
- ne pas copier les mêmes overrides de thème dans plusieurs écrans ;
- ne pas ouvrir un écran navigable sans focus initial ;
- ne pas utiliser les actions `ui_*` comme actions gameplay ;
- ne pas valider une interface uniquement en 16:9, à l’échelle 1.0 ou hors zones sûres ;
- ne pas fixer une largeur de texte sans test de localisation, reflow ou accès au contenu complet ;
- ne pas laisser un overlay décoratif intercepter la souris ;
- ne pas fermer une modale sans restaurer une cible de focus valide ;
- ne pas empiler des transitions concurrentes ni laisser une hitbox active pendant la sortie visuelle ;

- ne pas coder une information critique par la couleur seule ;
- ne pas agrandir toute l’interface avec un simple `scale` sans reflow ni tailles minimales recalculées ;
- ne pas employer un indicateur de focus subtil, non mesuré ou confondu avec le survol ;
- ne pas accélérer uniformément toutes les animations pour fabriquer un profil de mouvement réduit ;
- ne pas afficher seulement un code interne lorsqu’une action échoue ;
- ne pas utiliser `Oui` et `Non` pour une confirmation destructive ambiguë ;
- ne pas faire disparaître automatiquement une notification critique sans historique ni récupération ;
- ne pas remplacer un scénario de tâche par une question générale de préférence ;
- ne pas publier identité, citation, enregistrement ou donnée sensible sans consentement séparé ;
- ne pas généraliser une observation ou un petit échantillon à tous les joueurs et toutes les plateformes ;

- ne pas écraser une prise brute après nettoyage ou montage ;
- ne pas déduire entraînement ou clonage vocal d’une autorisation d’enregistrement ;
- ne pas utiliser la normalisation comme remplacement du mix et de la mesure de loudness ;
- ne pas choisir une boucle sur le seul passage par zéro sans contrôler pente, spectre et modulation ;
- ne pas fabriquer toute la variation avec un pitch ou un gain aléatoire extrême ;
- ne pas utiliser sans revue un fichier stéréo comme source 3D ponctuelle ;
- ne pas laisser `finished`, un beat ou un seuil de spectre modifier une règle gameplay ;
- ne pas laisser la polyphonie, les pools ou les files audio sans borne ni priorité ;
- ne pas utiliser `royalty-free`, `free` ou un paiement comme identifiant de licence ;
- ne pas déclarer un profil audio unique valable pour toutes les plateformes sans exécution et mesures ;

- ne pas mapper directement les lettres d’un sous-titre vers des formes de bouche ;
- ne pas créer une forme distincte pour chaque phonème sans preuve de différence visible ;
- ne pas publier un alignement automatique sans revue des mots inconnus et performances atypiques ;
- ne pas utiliser des clés carrées sans anticipation, relâchement ni coarticulation ;
- ne pas piloter directement la mâchoire par l’amplitude sonore ;
- ne pas laisser une expression écraser les fermetures articulatoires ;
- ne pas laisser la fin d’une animation faciale modifier la narration ou le gameplay ;
- ne pas réutiliser des timings après remplacement temporel de la voix ;
- ne pas employer un profil facial unique pour gros plan, gameplay et foule ;
- ne pas laisser un outil automatique promouvoir seul une animation faciale en état approuvé ;

- ne pas éditer directement une scène importée comme surface de personnalisation durable ;
- ne pas imposer l’import `.blend` à une équipe ou une CI sans version de Blender qualifiée ;
- ne pas utiliser OBJ pour un personnage exigeant squelette, animation ou blendshapes ;
- ne pas laisser un post-import créer ou modifier une règle gameplay ;
- ne pas ajouter à chaque réimportation des nœuds ou suffixes sans idempotence ;
- ne pas modifier un matériau embarqué sans ressource externe ou remap durable ;
- ne pas générer une collision dynamique complexe depuis le mesh de rendu sans contrat ;
- ne pas utiliser un nom de socket comme identité d’objet ou autorité d’équipement ;
- ne pas committer `.godot/` tout en ignorant les sidecars `<asset>.import` ;
- ne pas réimporter une livraison sans baseline, changements attendus, diff et contrôle des personnalisations ;


- ne pas accepter un asset sur la seule formule « paraît bon » sans candidat, preuve et critères ;
- ne pas laisser un script promouvoir directement un résultat technique en acceptation artistique ;
- ne pas valider uniquement dans Blender sans import propre et scène d’intégration Godot ;
- ne pas appliquer un budget unique à toutes les familles, distances et plateformes ;
- ne pas conclure depuis une seule frame froide sans chauffe, répétitions ni baseline ;
- ne pas créer une dérogation sans portée, propriétaire, expiration et plan de correction ;
- ne pas modifier le candidat pendant la revue tout en conservant l’ancien rapport ;
- ne pas réduire technique, art, droits et exécution à un booléen unique ;
- ne pas créer un constat vague sans règle, preuve et procédure de reproduction ;
- ne pas accepter un asset dont la provenance, la licence ou le consentement reste incomplet ;


- ne pas exécuter un script Blender directement sur une source canonique modifiable ;
- ne pas dépendre d’une sélection interactive ou d’un contexte implicite pour un job de lot ;
- ne pas installer automatiquement un custom node ComfyUI manquant ;
- ne pas présenter une seed fixe comme preuve d’identité binaire entre environnements ;
- ne pas retenter sans limite une violation de schéma, de provenance ou d’intégrité ;
- ne pas réutiliser un checkpoint lorsque le plan ou les empreintes d’entrée ont changé ;
- ne pas lancer plusieurs jobs GPU concurrents sur une ressource qualifiée comme exclusive ;
- ne pas promouvoir un lot parce que tous les codes techniques valent zéro ;
- ne pas échantillonner uniquement les premiers fichiers produits ou triés ;
- ne pas nettoyer une racine large qui contient des sources, livraisons ou preuves non régénérables ;

- ne pas introduire dans un chapitre lecteur des instructions ou critères liés à la génération du PDF du guide ; cette chaîne appartient à la publication documentaire de fin de Livre ou de collection ;
- ne pas considérer un pipeline vert, un score unique ou un taux de couverture comme une autorité de publication ;
- ne pas enregistrer un risque critique sans propriétaire, couches de contrôle et décision résiduelle ;
- ne pas accorder une dérogation sans portée, approbateur et expiration ;
- ne pas modifier un critère après observation des résultats sans créer une nouvelle version applicable aux campagnes futures ;
- ne pas présenter une hypothèse de cause comme un fait observé dans un rapport d’anomalie ;
- ne pas interpréter `NOT_REPRODUCED` comme une preuve d’inexistence du défaut ;
- ne pas fermer automatiquement un doublon à partir d’un titre ou d’une signature ;
- ne pas fermer un défaut au seul commit du correctif sans vérification et lien de non-régression ;
- ne pas partager une sauvegarde joueur, un dump ou des journaux bruts sans minimisation, expurgation et revue ;
- ne pas journaliser un secret, une donnée personnelle ou un texte libre sans contrat explicite, minimisation et expurgation ;
- ne pas utiliser un identifiant joueur, une corrélation, un chemin ou un texte libre comme dimension métrique ;
- ne pas émettre un événement à chaque frame sans agrégation, échantillonnage ou limite de débit déclarée ;
- ne pas régénérer un identifiant de corrélation dans chaque couche d’une même opération ;
- ne pas faire tourner des journaux sans politique de rétention et procédure de purge confinée ;
- ne pas laisser un tableau de bord ou un seuil d’observabilité modifier directement le gameplay ou une décision de publication ;
- ne pas collecter une métrique sans question, finalité et politique de conservation explicites ;
- ne pas utiliser un identifiant de joueur, un texte libre ou un identifiant d’instance runtime comme dimension d’équilibrage ;
- ne pas publier un ratio sans conserver son numérateur et son dénominateur ;
- ne pas conclure depuis une moyenne seule lorsqu’une distribution ou une queue peut modifier la décision ;
- ne pas déclarer une amélioration CPU sans benchmark, environnement et contrat d’échantillonnage comparables ;
- ne pas supprimer un run de profilage valide parce que son résultat est défavorable ;
- ne pas attribuer un temps de frame élevé au CPU sans distinguer temps propre, temps inclusif, rendu et attente ;
- ne pas réduire la cadence physique ou IA sans tests fonctionnels, latence et déterminisme adaptés ;
- ne pas introduire des threads sans mesurer préparation, travail, attente, fusion et correction du résultat ;
- ne pas accepter un gain de performance lorsque la suite fonctionnelle requise échoue ;
- ne pas conclure à une optimisation GPU depuis le FPS, les draw calls ou les primitives seuls ;
- ne pas comparer des campagnes GPU dont résolution, renderer, pilote, profil ou V-Sync ne sont pas qualifiés ;
- ne pas utiliser le replay d’une capture de frame comme unique baseline temporelle native ;
- ne pas réduire la qualité visuelle sans images comparables, revue humaine et profil de repli ;
- ne pas fusionner une géométrie globale sans mesurer la perte de granularité du culling ;
- ne pas attribuer un pic au coût GPU continu sans vérifier compilations de pipeline, soumission CPU et synchronisation ;
- ne pas conclure à une fuite depuis une seule capture ou un maximum isolé ;
- ne pas comparer working set, mémoire privée, mémoire statique et VRAM comme s’ils mesuraient la même chose ;
- ne pas conserver un cache, un pool ou un registre sans capacité, poids, expiration ou échéance explicite ;
- ne pas retirer un nœud de l’arbre en supposant qu’il est libéré ;
- ne pas dupliquer profondément une ressource sans besoin de mutabilité et provenance déclarés ;
- ne pas accepter une baisse de pic si le plateau, les orphelins, la qualité ou les tests se dégradent ;
- ne pas appeler `load_threaded_get()` sur le chemin critique avant que le statut soit `THREAD_LOAD_LOADED` ;
- ne pas interroger un chargement fileté dans une boucle bloquante sans rendre la main entre les frames ;
- ne pas soumettre une file concurrente sans limite, admission, priorité ni vieillissement ;
- ne pas afficher une progression ou une estimation restante qui n’est pas soutenue par des phases et poids mesurables ;
- ne pas présenter une annulation logique comme preuve d’arrêt du travail interne déjà lancé ;
- ne pas manipuler l’arbre de scène actif depuis un thread arbitraire ;
- ne pas évincer une zone depuis la distance seule sans propriétaires, échéances et coût de rechargement ;
- ne pas comparer des chargements dont build, stockage, état de cache ou profil diffèrent sans qualification ;
- ne pas optimiser une scène ou un système sans profil, hypothèse et mesures répétées comparables ;
- ne pas supposer que `set_process(false)` désactive la physique, les entrées ou tout le sous-arbre ;
- ne pas utiliser visibilité caméra, distance ou LOD logique comme autorité gameplay implicite ;
- ne pas laisser une file par frame, un quota ou une fréquence sans borne, équité et latence maximale ;
- ne pas rechercher les mêmes nœuds ou groupes à chaque frame lorsqu’un registre stable est possible ;
- ne pas créer un pool gameplay sans capacité, remise à zéro et test de réemploi ;
- ne pas manipuler l’arbre de scène actif depuis un thread arbitraire ;
- ne pas migrer vers une API serveur avant d’avoir mesuré et épuisé les solutions de plus haut niveau ;
- ne pas accepter un gain CPU si fonctionnel, latence, déterminisme, mémoire, lisibilité ou testabilité se dégradent ;
- ne pas utiliser un identifiant de pair comme identité durable, compte ou droit ;
- ne pas interpréter le retour immédiat de `create_client()` comme une connexion effective ;
- ne pas accepter comme vérité finale un état calculé par le client ;
- ne pas retenter sans borne un refus permanent de version, capacité ou admission ;
- ne pas appliquer une complétion de reconnexion dont la génération est obsolète ;
- ne pas diffuser un ticket de jonction ou de reprise dans une annonce LAN ;
- ne pas confondre découverte, invitation, admission et transport de jeu ;
- ne pas promettre une migration d’hôte sans transfert d’état, époque et prévention du double hôte ;
- ne pas rendre le chemin Solo dépendant d’un annuaire, relais ou service distant ;
- ne pas accepter comme résultat final une position, un inventaire ou un combat calculé par le client ;
- ne pas confondre autorité réseau d’un nœud et permission métier ;
- ne pas envoyer chaque snapshot en fiable sur le même canal que les événements critiques ;
- ne pas appliquer un delta sans posséder sa base exacte ;
- ne pas utiliser une pose interpolée comme état de collision ou d’autorité ;
- ne pas extrapoler sans durée, vitesse et politique de retour bornées ;
- ne pas purger les entrées non acquittées lors d’une réconciliation ;
- ne pas synchroniser `Resource`, `RID` ou identifiants d’instance comme données portables ;
- ne pas ajouter manuellement à l’arbre le nœud retourné par `MultiplayerSpawner.spawn_function` ;
- ne pas conclure à une triche depuis une empreinte divergente sans diagnostic et resynchronisation ;
- ne pas exécuter le serveur dédié comme joueur local implicite ;
- ne pas embarquer un secret dans le dépôt, le PCK, l’image ou une ligne de commande visible ;
- ne pas exposer publiquement ports d’administration, de métriques, de base ou de debug ;
- ne pas lancer le conteneur avec `--privileged` pour contourner une permission manquante ;
- ne pas activer le décodage d’objets pour une source réseau non fiable ;
- ne pas accepter un ticket sans audience, expiration, nonce et validation de session ;
- ne pas journaliser tickets, credentials, en-têtes d’authentification ou payloads complets ;
- ne pas redémarrer avant fermeture de l’admission, drainage borné et sauvegarde contrôlée ;
- ne pas revenir à un ancien binaire sans vérifier sa compatibilité avec l’état courant ;
- ne pas présenter zéro alerte d’un scanner comme audit professionnel ou certification ;
- ne pas fournir de secret, de permission d’écriture ou d’environnement protégé à une pull request non fiable ;
- ne pas masquer un code de sortie non nul avec une continuation systématique ;
- ne pas utiliser une référence d’action mobile non qualifiée dans un workflow sensible ;
- ne pas traiter un cache comme un artefact de preuve ou une sauvegarde ;
- ne pas reconstruire un candidat pendant sa promotion ;
- ne pas publier le workspace entier lorsqu’une liste fermée d’artefacts suffit ;
- ne pas relancer un test déterministe jusqu’à obtenir artificiellement du vert ;
- ne pas afficher l’environnement complet pour diagnostiquer un secret manquant ;
- ne pas déplacer un tag de release déjà publié ;
- ne pas revendiquer une reconstruction reproductible sans clone neuf, outils qualifiés et manifestes comparables ;
- ne pas confondre synchronisation, réplication ou snapshot avec une sauvegarde indépendante ;
- ne pas sauvegarder uniquement des caches ou index dérivés ;
- ne pas écraser la dernière génération valide avec une tentative incomplète ;
- ne pas présenter un objectif RPO/RTO comme un résultat mesuré ;
- ne pas copier une base SQLite active sans mécanisme cohérent ;
- ne pas restaurer un dump ou une archive directement en production ;
- ne pas modifier une migration déjà appliquée ;
- ne pas revenir à un ancien binaire sans matrice de compatibilité des données ;
- ne pas conserver l’unique clé de déchiffrement avec l’unique archive ;
- ne pas déclarer une restauration réussie après un simple test de connexion ;
- ne pas laisser le compte de production supprimer toutes les générations ;
- ne pas supprimer une génération avant expiration, contrôle juridique et remplacement vérifié ;
- ne pas reconstruire un package pendant sa soumission ou sa promotion vers une boutique ;
- ne pas confondre présence d’un build, envoi en revue, approbation et publication publique ;
- ne pas publier une affirmation de fiche produit sans preuve reliée à un build ou une fonctionnalité réelle ;
- ne pas réutiliser une classification d’âge ou une déclaration de confidentialité d’une autre version sans revue ;
- ne pas verser un secret, une clé d’accès ou un credential de boutique dans le dépôt ou un journal ;
- ne pas traiter un canal interne, fermé ou preview comme une sortie publique ;
- ne pas générer des clés d’accès sans lot, propriétaire, finalité, quantité, expiration et révocation ;
- ne pas figer dans la procédure des dimensions, délais ou champs de portail susceptibles d’évoluer sans registre de vérification ;
- ne pas annoncer une date de lancement sans portes techniques, juridiques, support et décision de retour arrière ;
- ne pas présenter une soumission illustrative ou un dry-run documentaire comme une revue réellement exécutée ;
- ne pas traiter un préréglage d’accessibilité comme un diagnostic ou un profil figé pour une catégorie de personnes ;
- ne pas rendre une information critique dépendante de la couleur, du son, de la vibration ou du mouvement seuls ;
- ne pas cacher les réglages essentiels derrière le premier obstacle ou uniquement dans une partie déjà commencée ;
- ne pas publier une fonction d’accessibilité sans preuve liée au même build et à la même plateforme ;
- ne pas utiliser un avertissement comme remplacement de la réduction des flashs, du mouvement ou de leur revue ;
- ne pas présenter un contrôle automatique comme preuve suffisante d’accessibilité ;
- ne pas demander de diagnostic médical pour autoriser un réglage ou participer à un test ;
- ne pas persister un réglage visuel ou de navigation risqué avant prévisualisation, confirmation et restauration possible ;
- ne pas généraliser une observation ou un petit échantillon à tous les joueurs, périphériques et plateformes ;
- ne pas revendiquer une conformité WCAG, XAG, légale ou universelle à partir d’une revue statique ;
- ne pas utiliser le texte source comme identité de traduction ;
- ne pas concaténer des fragments de phrase traduisibles ;
- ne pas choisir les pluriels, genres, dates, montants ou unités avec une règle française codée en dur ;
- ne pas stocker une date, un montant ou une unité uniquement sous sa forme affichée ;
- ne pas appliquer un miroir géométrique global pour traiter une interface RTL ;
- ne pas dépendre d’une police système implicite pour masquer des glyphes absents ;
- ne pas pseudo-localiser les variables, balises ou identifiants ;
- ne pas déclarer une locale supportée après la seule traduction du catalogue ;
- ne pas envoyer un corpus, un secret ou un contenu non publié à un fournisseur sans minimisation et approbation ;
- ne pas modifier l’installation active pendant le téléchargement ou l’application d’un patch ;
- ne pas appliquer un différentiel sans vérifier l’identité exacte de la base ;
- ne pas confondre arrêt de diffusion, rollback binaire et restauration de données ;
- ne pas revenir à un binaire incapable de lire le schéma courant ;
- ne pas modifier en place une migration déjà publiée ;
- ne pas écraser la copie pré-migration lors d’un retry ;
- ne pas reconstruire un candidat pendant sa promotion entre canaux ;
- ne pas retenter indéfiniment une erreur de schéma ou d’intégrité ;
- ne pas collecter automatiquement sauvegardes brutes, secrets ou environnement complet ;
- ne pas interpréter un tableau vide comme zéro incident ;
- ne pas utiliser un nom affiché comme identité de mod ;
- ne pas monter un PCK communautaire avec remplacement global des ressources officielles ;
- ne pas charger un script ou une extension native non fiable comme une simple donnée ;
- ne pas extraire une archive avant validation de tous ses chemins, types et quotas ;
- ne pas utiliser l’ordre du système de fichiers comme ordre de chargement ;
- ne pas ignorer une capacité, dépendance, contrainte ou version inconnue ;
- ne pas résoudre silencieusement un conflit par le dernier mod chargé ;
- ne pas supprimer état ou fichiers lors d’une simple désactivation ;
- ne pas charger une sauvegarde moddée sans vérifier l’ensemble requis ;
- ne pas laisser un client imposer un mod autoritaire au serveur ;
- ne pas présenter un abonnement Workshop ou une release comme validation de sécurité ;
- ne pas présumer qu’un contenu sans licence explicite est redistribuable ;
- ne pas traiter un contrôle automatique comme décision juridique ou de modération ;
- ne pas confondre miroir synchronisé et archive indépendante ;
- ne pas archiver uniquement le code en oubliant outils, dépendances, builds, licences et documentation ;
- ne pas confondre checksum, signature, authenticité, restauration et reconstruction ;
- ne pas placer de secret, clé privée ou valeur de récupération dans Git ou une archive documentaire ;
- ne pas fermer une alerte de vulnérabilité sans contexte, preuve, propriétaire et échéance ;
- ne pas écraser un original pendant une migration de format ;
- ne pas annoncer une reconstruction après le seul clone d’un dépôt ;
- ne pas laisser un compte critique dépendre d’une personne ou d’une voie de récupération unique ;
- ne pas retirer un service sans plan de données, communication et support ;
- ne pas déclarer une archive saine sans test de restauration et, pour une release, exercice de reconstruction ;
- ne pas modifier plusieurs variables dans une même expérience sans les déclarer et justifier leur couplage ;
- ne pas utiliser le générateur pseudo-aléatoire global pour une simulation comparative ;
- ne pas présenter une graine comme preuve d’identité binaire universelle entre environnements ;
- ne pas laisser une métrique, un dashboard ou un rapport modifier directement un état gameplay ;
- ne pas confondre corrélation observée et causalité démontrée ;
- ne pas présenter une simulation comme un résultat obtenu auprès de joueurs ;
- ne pas collecter à distance ou auprès de personnes sans gouvernance, minimisation, information, base retenue, rétention et retrait adaptés ;
- ne pas traiter un message, un code, une corrélation ou une signature comme une cause unique ;
- ne pas supprimer un cache, réinstaller, migrer ou restaurer avant d’avoir préservé les preuves utiles ;
- ne pas publier un secret, un dump non revu, une sauvegarde joueur brute ou une donnée personnelle dans un dossier diagnostique ;
- ne pas fermer un défaut sur un contournement, un commit ou une CI verte sans vérification et non-régression adaptées ;
- ne pas présenter une moyenne isolée comme description suffisante d’une distribution ;
- ne pas traiter les observations d’un même run comme des répétitions indépendantes ;
- ne pas supprimer une valeur extrême ou manquante sans règle, statut et justification conservés ;
- ne pas arrêter une campagne dès que le résultat devient favorable ni changer la métrique primaire après lecture ;
- ne pas confondre support officiel, preuve locale et décision de la collection ;
- ne pas interpréter une cellule vide, non évaluée, bloquée ou obsolète comme une incompatibilité ;
- ne pas déduire lecture, écriture, import, export ou round-trip les uns des autres ;
- ne pas conserver une cellule `reference` sans preuve consultable, date et propriétaire ;
- ne pas confondre obligation, applicabilité, statut, preuve et décision d’une checklist ;
- ne pas considérer une case cochée, un nom ou une CI verte comme preuve suffisante sans artefact propriétaire ;
- ne pas masquer un item obligatoire pour faire passer une porte ;
- ne pas accepter une dérogation sans portée, propriétaire, compensation et expiration ;
- ne pas transférer automatiquement une checklist réussie vers un nouveau build, une nouvelle plateforme ou une nouvelle locale ;
- ne pas réécrire une décision historique lors d’une réouverture ;
- ne pas déduire un droit d’un prix, d’un téléchargement, d’une visibilité publique ou d’une génération ;
- ne pas étendre la licence du code aux modèles, poids, données, médias, personnes ou services ;
- ne pas utiliser `open`, `free`, `royalty-free` ou `NOASSERTION` comme autorisation de publication ;
- ne pas fusionner auteur, titulaire, fournisseur, opérateur et approbateur ;
- ne pas publier un objet dont une dépendance obligatoire reste `unknown`, `blocked`, `contested` ou `stale` ;
- ne pas exposer contrats, consentements, signatures, secrets ou données personnelles dans un registre public ;
- ne pas automatiser une conclusion de titularité, de compatibilité juridique ou de conformité réglementaire ;
- ne pas appliquer une exception au-delà de son objet, sa version, son canal, son territoire, sa durée ou son expiration ;
- ne pas annoncer une licence globale avant une décision documentée sur le texte, le code, les médias et le Companion Pack ;
- ne pas confondre identifiant d’index, libellé, chemin, titre et ancre ;
- ne pas donner à un alias, un acronyme ou une ancienne appellation une définition concurrente ;
- ne pas confondre `owner`, `prerequisite`, `validates`, `diagnoses`, `alternative`, `supersedes` et `related` ;
- ne pas déclarer un document orphelin depuis le seul nombre de liens entrants ou sortants ;
- ne pas présenter une cible `planned`, `unresolved`, `deprecated` ou `retired` comme une destination active ;
- ne pas déduire la qualité de navigation PDF, HTML ou EPUB depuis les seuls liens Markdown ;
- ne pas exposer secret, donnée personnelle, contrat ou chemin restreint dans un index public ;
- ne pas modifier les poids, critères ou seuils après lecture des scores sans créer une nouvelle version du comparatif ;
- ne pas laisser un score agrégé compenser une porte obligatoire non satisfaite ;
- ne pas imputer silencieusement une valeur aux données inconnues, bloquées, obsolètes ou non applicables ;
- ne pas présenter une préférence, une note ordinale ou une estimation comme un fait ou une mesure physique ;
- ne pas produire de recommandation absolue ni forcer un vainqueur lorsque la preuve autorise une égalité, un pilote ou une indétermination ;

## 25. État courant

- branche principale : `main` ;
- jalon : M7 — Companion Pack ;
- progression du Companion Pack : 5 packs validés sur 10 ;
- Starter Kit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;
- Project Templates : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;
- AI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec faux serveurs contrôlés ;
- Code Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;
- Database Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python `sqlite3` ;
- progression du Livre V : 26 chapitres sur 26 ;
- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 6 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 7 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 8 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 9 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 10 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 11 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 12 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 13 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 14 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 15 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 16 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 17 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 18 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 19 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 20 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 21 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 22 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 23 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 24 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 25 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- chapitre 26 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;
- profil éditorial du Livre V : fiches, matrices, recettes minimales et index ; les obligations tutoriel incompatibles sont exclues ;
- publication technique du Livre V : acceptée au niveau `static-review+pdf-inspected` ; PDF cumulatif de 4063 pages, préflight réussi et inspection Poppler/PDFium achevée ;
- progression du Livre IV : 22 chapitres sur 22 ;
- chapitre 1 du Livre IV : version `1.0.1`, niveau `static-review` ;
- chapitre 2 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 3 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 4 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 5 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 6 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 7 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 8 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 9 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 10 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 11 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 12 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 13 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 14 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 15 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 16 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 17 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 18 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 19 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 20 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 21 du Livre IV : version `1.0.0`, niveau `static-review` ;
- chapitre 22 du Livre IV : version `1.0.0`, niveau `static-review` ;
- publication technique du Livre IV : validation transversale, compilation Pandoc/XeLaTeX, préflight et inspection visuelle terminés ;
- progression du Livre III : 30 chapitres sur 30 ; publication technique terminée ;
- chapitre 1 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 2 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 3 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 4 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 5 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 6 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 7 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 8 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 9 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 10 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 11 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 12 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 13 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 14 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 15 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 16 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 17 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 18 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 19 du Livre III : version `1.0.2`, niveau `static-review` ;
- chapitre 20 du Livre III : version `1.0.2`, niveau `static-review` ;
- chapitre 21 du Livre III : version `1.0.1`, niveau `static-review` ;
- chapitre 22 du Livre III : version `1.0.1`, niveau `static-review` ;
- chapitre 23 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 24 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 25 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 26 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 27 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 28 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 29 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 30 du Livre III : version `1.0.0`, niveau `static-review` ;
- Livre II : 30 chapitres sur 30, publication technique terminée ;
- industrialisation du Livre II : 5 chapitres sur 5 ;
- chapitre 1 : version `1.3.0` ;
- chapitre 2 : version `1.5.0` ;
- chapitres 3 à 6 : version `1.1.0` ;
- chapitre 7 : version `1.1.1` ;
- chapitre 8 : version `1.0.0` ;
- chapitre 9 : version `1.0.0` ;
- chapitre 10 : version `1.0.0` ;
- chapitre 11 : version `1.0.0` ;
- chapitre 12 : version `1.0.2` ;
- chapitre 13 : version `1.0.0` ;
- chapitre 14 : version `1.0.0` ;
- chapitre 15 : version `1.2.1` ;
- chapitre 16 : version `1.2.1` ;
- chapitre 17 : version `1.0.5` ;
- chapitre 18 : version `1.0.2` ;
- chapitre 19 : version `1.0.3` ;
- chapitre 20 : version `1.0.2` ;
- chapitre 21 : version `1.0.2` ;
- chapitre 22 : version `1.0.4` ;
- chapitre 23 : version `1.0.3` ;
- chapitre 24 : version `1.0.2` ;
- chapitre 25 : version `1.0.2` ;
- chapitre 26 : version `1.0.2` ;
- chapitre 27 : version `1.0.1` ;
- chapitre 28 : version `1.0.0` ;
- chapitre 29 : version `1.0.1` ;
- chapitre 30 : version `1.0.0` ;
- Starter Kit matérialisé et validé dans le périmètre Linux ;
- licence globale à définir ;
- publication technique du Livre II acceptée après compilation et inspection PDF ;
- publication technique du Livre III acceptée après compilation et inspection PDF ;
- licence globale à décider avant publication officielle de la collection ;
- accessibilité PDF avancée et balisage à traiter avant publication officielle.

## 26. Prochaine action

M7 — Companion Pack est actif. Les Packs 1 à 5 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Database Library a validé quatre migrations ascendantes, deux repositories, quatorze tests Python, la création depuis zéro, les montées de version, la sauvegarde, la restauration et les contrôles d’intégrité avec Python `sqlite3`. Godot-SQLite, Godot, les performances, la concurrence, Windows graphique, les exports et la licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/ComfyUI-Library/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 6 doit matérialiser une bibliothèque ComfyUI reproductible : workflows JSON, manifestes YAML, listes de custom nodes, presets, scripts de lancement, modèles de dossiers, fiches de provenance, images légères de validation et checksums. Aucun modèle non redistribuable ne devra être inclus ; chaque dépendance, seed, paramètre, profil matériel, exécution et licence devra être qualifié sans inventer de résultat.
## 27. Journal

### 2026-07-30T10:29:52+02:00 — version 4.19.0

- matérialisation du Companion Pack, Pack 5 — Database Library ;
- quatre migrations SQLite ascendantes et immuables avec manifeste et empreintes SHA-256 ;
- schémas de balises, événements, documents, tags et cache dérivé créés ;
- deux repositories, fixture synthétique, scripts d’initialisation, sauvegarde, restauration et validation créés ;
- 46 fichiers sources validés sans paquet runtime tiers, addon binaire, secret, donnée personnelle ni base binaire versionnée ;
- 14 tests Python réussis avec `3.12.13` et SQLite `3.45.1` via `sqlite3` ;
- création depuis zéro, montées depuis les versions 1 à 3, refus de version future et de base étrangère validés ;
- Online Backup API, restauration par staging, `quick_check`, `foreign_key_check` et historique des migrations validés ;
- run `30526910180` du finaliseur temporaire ;
- validations documentaires légères exécutées sans PDF ;
- progression M7 portée à 5 packs sur 10 ;
- prochaine action : `Companion-Pack/ComfyUI-Library/README.md`, niveau Élevée ;
- aucun Godot-SQLite, Godot, Windows graphique, test de performance, charge, concurrence, export, release, licence globale, donnée personnelle ou secret validé ou produit.

### 2026-07-30T07:53:26+02:00 — version 4.18.0

- matérialisation du Companion Pack, Pack 4 — Code Library ;
- 18 composants enregistrés pour 9 concepts, avec ports Python et GDScript et registre d’API publique ;
- collections, validation, sérialisation canonique, services, repository mémoire, machine à états, interactions, conversions et aides de test créés ;
- politique anti-doublon appliquée ; files et cache réservés à l’AI Library, bootstrap et composition réservés aux Packs 1 et 2 ;
- 64 fichiers sources du pack validés sans paquet Python tiers, addon binaire, secret ni donnée personnelle ;
- 16 tests Python réussis ;
- import, démarrages headless et Xvfb Compatibility réussis avec Godot `4.7.1.stable.official.a13da4feb` ;
- tests GDScript réussis avec `CODE_LIBRARY_GODOT_TESTS: PASS` ;
- arbre Git propre après runtime ;
- run `30517143131`, artefact `8749316530`, digest `sha256:d7c5bc8ae40c824e0629e290c3765470132fa3141f7f2b59416c8b7310957b52` ;
- correction d’une inférence de type GDScript, durcissement de la CI contre les `SCRIPT ERROR` et arrêt explicite du runner après succès ;
- progression M7 portée à 4 packs sur 10 ;
- prochaine action : `Companion-Pack/Database-Library/README.md`, niveau Élevée ;
- aucune performance, charge, Windows graphique, Forward+ GPU réel, export, release, licence globale, donnée personnelle ou secret validé ou produit.

### 2026-07-30T06:36:00+02:00 — version 4.17.0

- matérialisation du Companion Pack, Pack 3 — AI Library ;
- contrats, sous-ensemble OpenAI-compatible, HTTP, WebSocket, adaptateurs Ollama/llama.cpp/LocalAI, délais, reprises, annulation, file, cache, sécurité et modes dégradés créés ;
- 51 fichiers sources validés sans paquet Python tiers ;
- 13 tests Python réussis contre les faux serveurs contrôlés ;
- import, démarrages headless et Xvfb Compatibility réussis avec Godot `4.7.1.stable.official.a13da4feb` ;
- tests GDScript réussis avec `AI_LIBRARY_GODOT_TESTS: PASS` ;
- arbre Git propre après runtime ;
- run `30514201037`, artefact `8748232588`, digest `sha256:c42c91c7d604a2d128e6e95f2923b46cc55397e87956d7787cd9d63a812741b7` ;
- progression M7 portée à 3 packs sur 10 ;
- prochaine action : `Companion-Pack/Code-Library/README.md`, niveau Élevée ;
- aucun service fournisseur réel, modèle, secret, réseau distant, mesure de performance, export, release ou licence globale validé ou produit.

### 2026-07-30T05:34:00+02:00 — version 4.16.0

- matérialisation du Companion Pack, Pack 2 — Project Templates ;
- modèles Solo et Studio, générateur Python, enveloppe PowerShell, module en cinq couches, ADR, conventions Git, issues, PR, VS Code, style et CODEOWNERS Studio créés ;
- 71 sources textuelles du pack validées sans dépendance Python tierce ni fichier binaire ;
- générations Solo et Studio déterministes pour des entrées identiques ;
- projets neufs et modules `inventory_demo` créés, importés et testés ;
- Godot `4.7.1.stable.official.a13da4feb`, archive SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` ;
- démarrages headless et Xvfb Compatibility réussis pour les deux profils ;
- tests GDScript réussis avec `PROJECT_TEMPLATE_TESTS: PASS` ;
- arbres Git générés propres après runtime ;
- run `30511425269`, artefact `8747249256`, digest `sha256:a285b4880527d0aa36bfe1f1ed67d3e950b4668601709ce5aadb04e73bd04473` ;
- progression M7 portée à 2 packs sur 10 ;
- prochaine action : `Companion-Pack/AI-Library/README.md`, niveau Élevée ;
- aucune protection de branche, efficacité CODEOWNERS, Windows graphique, Forward+ GPU réel, export, release, licence globale, donnée personnelle ou secret validé ou produit.

### 2026-07-30T04:19:00+02:00 — version 4.15.0

- matérialisation du Companion Pack, Pack 1 — Starter Kit ;
- projet Godot `Project Asteria` version `1.0.0`, Godot `4.7.1.stable.official.a13da4feb`, GDScript et Forward+ de référence ;
- scène de bootstrap 3D, `BootstrapReport`, profils Solo/Studio, manifestes, provenance et statut de redistribution créés ;
- validateur Python sans paquet tiers et enveloppe PowerShell exécutés avec succès ;
- import et démarrage Linux headless réussis ;
- démarrage graphique virtuel Xvfb avec Compatibility réussi, sans revendication de qualité visuelle ;
- tests GDScript réussis avec `STARTER_KIT_TESTS: PASS` ;
- clone Git neuf reproduit, importé et testé ; arbre propre après runtime ;
- trois UID Godot générés puis versionnés ;
- run `30508086899`, artefact `8746081670`, digest `sha256:5429fcc7001d4a28d7475908d8660e859b4aafd86b4febd42629b66e5310e2ed` ;
- progression M7 portée à 1 pack sur 10 ;
- prochaine action : `Companion-Pack/Project-Templates/README.md`, niveau Élevée ;
- aucun Windows graphique, Forward+ GPU réel, export, archive publiable, restauration, licence globale, donnée personnelle ou secret validé ou produit.

### 2026-07-30T03:00:00+02:00 — version 4.14.0

- clôture technique et PDF du Livre V — Encyclopédie technique et bibliothèque de référence ;
- 145 sources lecteur validées et parsables avec Pandoc ;
- deux séparateurs de la fiche 05 normalisés pour empêcher une interprétation YAML erronée ;
- dépendance Latin Modern ajoutée à la chaîne temporaire XeLaTeX ;
- PDF cumulatif final : 4063 pages A4, 10462788 octets, version 1.5, non chiffré et texte extractible ;
- empreinte PDF `008ae82f759f562178b810e87abbd08c0e00bf6dd6eba4afeb5334748feda8a3` et empreinte du texte extrait `6734cb86d214264e55b0f2ef188be73c55ccfed050c9374d43cde37ad6e58df5` ;
- `qpdf --check`, polices incorporées, 26 titres du Livre V et exclusion des contenus QA internes validés ;
- Livre V cartographié des pages 3 681 à 4 062 ; Companion Pack à partir de la page 4 063 ;
- 82 pages inspectées avec Poppler et 8 pages comparées avec PDFium, sans défaut visuel bloquant observé ;
- run final `30503741584`, artefact `8744567647`, digest `sha256:b8300a8a449b89606f9a1b80551454d17f3205bb8f1131451676fc514a4ff221` ;
- publication technique du Livre V acceptée au niveau `static-review+pdf-inspected` ;
- jalon actif déplacé vers M7 — Companion Pack ;
- prochaine action : `Companion-Pack/Starter-Kit/README.md`, niveau Élevée ;
- aucune licence globale, aucun PDF balisé, HTML, EPUB, Starter Kit, projet Godot exécutable, test runtime ou publication commerciale produit.

### 2026-07-30T01:18:00+02:00 — version 4.13.0

- création de la fiche 26 — Index croisés ;
- ajout de treize cartes, de trois matrices et de 9 diagrammes compacts ;
- identités canoniques, index alphabétiques et thématiques, facettes, synonymes, alias, anciennes appellations, relations typées, routes outils/systèmes/formats/diagnostics/licences et navigation multiformat indexés ;
- contrôles de chemins, fragments, doublons, redirections, candidats orphelins, cibles retirées et supports non testés encadrés sans suppression automatique ;
- frontières avec les fiches 01 à 25, les procédures des Livres I à IV, le Companion Pack et M8 maintenues sans duplication ;
- métriques statiques : 474 lignes, 21 titres, 13 fiches, 3 matrices, 176 liens, 46 renvois vers les Livres I à IV, 102 liens profonds et 9 diagrammes compacts ;
- progression documentaire du Livre V portée à 26 chapitres sur 26 ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la construction, le préflight et l’inspection du PDF complet du Livre V, niveau Élevée ;
- aucun moteur de recherche, générateur d’index, base d’alias, graphe de connaissances, rapport exhaustif d’orphelins, étude utilisateur, donnée personnelle, licence globale, outil du Companion Pack, PDF, HTML ou EPUB produit.

### 2026-07-30T00:17:00+02:00 — version 4.12.0

- création de la fiche 25 — Licences, provenance et conformité ;
- ajout de treize cartes, de trois matrices et de 9 diagrammes compacts ;
- objets, couches juridiques, inventaire, SPDX, droits, provenance, personnes, chaînes IA, redistribution, statuts, notices, gouvernance, escalades, incidents et licence globale indexés ;
- sources officielles SPDX, REUSE, OSI, Creative Commons, Légifrance, CNIL et Union européenne vérifiées le 30 juillet 2026 ;
- frontières avec le Volume 0, les Livres II à IV, la fiche 24, la future fiche 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 584 lignes, 34 titres, 13 fiches, 3 matrices, 77 liens, 35 renvois vers les Livres I à IV, 55 liens profonds et 9 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 26 — Index croisés, niveau Élevée ;
- aucune licence, compatibilité, titularité, conformité réglementaire, donnée personnelle, approbation, licence globale, outil du Companion Pack ou PDF produit.

### 2026-07-29T23:31:00+02:00 — version 4.11.0

- création de la fiche 24 — Checklists de production et de publication ;
- ajout de treize cartes, de trois matrices et de 9 diagrammes compacts ;
- contrat d’item, obligation, statut, phase, preuve, préparation, intégration, QA, build, publication, vues Solo/Studio, décisions, dérogations, signatures et réouverture indexés ;
- frontières avec le Volume 0, les Livres II à IV, les fiches 21 à 23, les futures fiches 25 et 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 481 lignes, 20 titres, 13 fiches, 3 matrices, 64 liens, 34 renvois vers les Livres I à IV, 64 liens profonds et 9 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 25 — Licences, provenance et conformité, niveau Élevée ;
- aucune checklist, preuve d’exécution, dérogation, signature, approbation, publication, donnée utilisateur, outil du Companion Pack ou PDF produit.

### 2026-07-29T22:44:00+02:00 — version 4.10.0

- création de la fiche 23 — Comparatifs des solutions ;
- ajout de treize cartes, de trois matrices et de 8 diagrammes compacts ;
- contrat, couches d’information, candidats, portes, critères, pondérations, données manquantes, scénarios, sources, mesures, préférences, coûts, migration, sensibilité, recommandations et maintenance indexés ;
- frontières avec les fiches 02 à 22, les procédures propriétaires des Livres I à IV, les futures fiches 24 à 26 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 460 lignes, 20 titres, 13 fiches, 3 matrices, 90 liens, 30 renvois vers les Livres I à IV, 55 liens profonds et 8 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 24 — Checklists de production et de publication, niveau Élevée ;
- aucun candidat, benchmark, score, prix, devis, coût total, étude utilisateur, pilote de migration, décision d’achat, donnée utilisateur, outil du Companion Pack ou PDF produit.

### 2026-07-29T21:13:00+02:00 — version 4.09.0

- création de la fiche 22 — Matrices de compatibilité ;
- ajout de treize cartes, de trois matrices et de 8 diagrammes compacts ;
- contrat de cellule, statuts amont et locaux, axes, sources, versions, systèmes, GPU, backends, outils, formats, API, tests, promotion, vues, migrations et historique indexés ;
- frontières avec la politique du Volume 0, les fiches 03 à 07, 13 à 14 et 18 à 21, les procédures propriétaires des Livres II à IV, la future fiche 23 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 493 lignes, 20 titres, 13 fiches, 3 matrices, 70 liens, 11 renvois vers les Livres I à IV, 51 liens profonds et 8 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 23 — Comparatifs des solutions, niveau Élevée ;
- aucun OS, GPU, pilote, backend, outil, format, import, export, API, sauvegarde, réseau, mod, matrice runtime, donnée utilisateur ou PDF produit.

### 2026-07-29T18:11:00+02:00 — version 4.08.0

- création de la fiche 21 — Benchmarks et méthodes de mesure ;
- ajout de treize cartes, de trois matrices et de 8 diagrammes compacts ;
- contrat, routage, question, environnement, scénario, warm-up, caches, répétitions, unités, données brutes, statistiques, exclusions, comparaison, rapports, preuves et maintenance indexés ;
- frontières avec l’équilibrage, la QA, l’observabilité, le diagnostic et les campagnes spécialisées des chapitres 1 à 14 du Livre IV, les fiches 18 à 20, les futures fiches 22 et 23 et le Companion Pack maintenues sans duplication ;
- métriques statiques : 462 lignes, 20 titres, 13 fiches, 3 matrices, 64 liens, 41 renvois vers les Livres I à IV, 47 liens profonds et 8 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 22 — Matrices de compatibilité, niveau Élevée ;
- aucun benchmark, warm-up, cache, run, profiler, série, statistique, comparaison, donnée utilisateur, script du Companion Pack ou PDF produit.

### 2026-07-29T16:26:00+02:00 — version 4.07.0

- création de la fiche 20 — Catalogue des erreurs et diagnostics ;
- ajout de treize cartes, de trois matrices et de 7 diagrammes compacts ;
- contrat diagnostique, routage, certitude, environnement, reproduction, preuves, messages, hypothèses, causes, contournements, corrections, index transversaux et maintenance versionnée indexés ;
- frontières avec les chapitres 2 à 20 du Livre IV, les méthodes de production du Livre III, les fiches 18 et 19, la future fiche 21, la future fiche 22 et le Companion Pack maintenues sans duplication ;
- validations documentaires légères sans PDF préparées par le workflow temporaire dédié ;
- métriques statiques : 454 lignes, 20 titres, 13 fiches, 3 matrices, 89 liens, 50 renvois vers les Livres I à IV, 80 liens profonds et 7 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 21 — Benchmarks et méthodes de mesure, niveau Élevée ;
- aucun défaut, message, log, trace, dump, reproduction, hypothèse, cause, contournement, correctif, benchmark, donnée utilisateur, outil diagnostique ou PDF produit.


### 2026-07-29T15:46:00+02:00 — version 4.06.0

- création de la fiche 19 — Référence audio ;
- ajout de treize cartes, de trois matrices et de 7 diagrammes compacts ;
- signal, niveaux, formats, cycle de vie, boucles, familles, spatialisation, bus, voix, TTS/STT, localisation, accessibilité, budgets, preuves et diagnostics audio indexés ;
- frontières avec la fiche 07, les chapitres 9 du Livre I, 5, 26 à 29 du Livre III et 18 à 19 du Livre IV maintenues sans duplication ;
- validations documentaires légères sans PDF réussies dans le run `30458855819` ;
- métriques statiques : 468 lignes, 20 titres, 13 fiches, 3 matrices, 95 liens, 49 renvois vers les Livres I à IV, 49 liens profonds et 7 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 20 — Catalogue des erreurs et diagnostics, niveau Élevée ;
- aucun outil audio, TTS, STT, fichier, encodage, écoute, import, bus, effet, boucle, mesure, donnée vocale, approbation juridique ou PDF produit.


### 2026-07-29T13:59:00+02:00 — version 4.05.0

- création de la fiche 18 — Référence graphique et 3D ;
- ajout de treize cartes, de trois matrices et de 7 diagrammes compacts ;
- unités, axes, pivots, formats, cycle de vie, PBR, UV, baking, géométrie, LOD, rigs, import, budgets, presets, preuves et diagnostics visuels indexés ;
- méthodes propriétaires des chapitres 4, 5, 16 à 21, 28 et 29 du Livre III maintenues sans duplication ;
- validations documentaires légères sans PDF réussies dans le run `30451780779` ;
- métriques statiques : 500 lignes, 19 titres, 13 fiches, 3 matrices, 91 liens, 63 renvois vers les Livres I à IV, 35 liens profonds et 7 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 19 — Référence audio, niveau Élevée ;
- aucun Blender, Godot, GLB, mesh, texture, matériau, UV, bake, LOD, rig, animation, preset, import, comparaison de pilote, benchmark, approbation juridique ou PDF produit.


### 2026-07-29T10:21:00+02:00 — version 4.04.0

- création de la fiche 17 — Patrons de gameplay ;
- ajout de treize cartes, de trois matrices et de six diagrammes compacts ;
- machines à états, variantes simples et avancées, capacités, commandes, inventaires, quêtes, simulations, matérialisation, commits multi-autorités et coutures de test indexés ;
- frontières avec les systèmes propriétaires des chapitres 14, 17 à 20, 22, 25 et 27 du Livre II maintenues sans duplication ;
- validations documentaires légères sans PDF réussies dans le run `30438299611` ;
- métriques statiques : 442 lignes, 19 titres, 13 fiches, 3 matrices, 57 liens, 33 renvois vers les Livres I à IV, 4 liens profonds et 6 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 18 — Référence graphique et 3D, niveau Élevée ;
- aucun runtime Godot, GDScript, scène, addon, base, réseau, service IA, prototype du Companion Pack, approbation juridique ou PDF produit.


### 2026-07-29T07:08:35+02:00 — version 4.03.0

- création de la fiche 16 — Patrons d’architecture ;
- ajout de treize cartes, de trois matrices et de sept diagrammes compacts ;
- frontières, dépendances, composition root, injection, composition, services, repositories, ports, adaptateurs, événements, propriété d’état, façades, stratégies et coutures de test indexés ;
- documentation Godot `4.7` et sources spécialisées sur injection, Repository et architectures événementielles relues le 29 juillet 2026 ;
- campagne temporaire de 67 contrats synthétiques réussie avec CPython `3.12.3`, sans Godot, addon, stockage, réseau ni donnée utilisateur ;
- métriques statiques : 409 lignes, 19 titres, 13 fiches, 3 matrices, 65 liens, 34 renvois vers les Livres I à IV, 21 liens profonds et 7 diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 17 — Patrons de gameplay, niveau Élevée ;
- aucun runtime Godot, GDScript, scène, addon, base, service, projet Companion Pack, approbation juridique ou PDF produit.


### 2026-07-29T06:18:10+02:00 — version 4.02.0

- création de la fiche 15 — Bases vectorielles et recherche sémantique ;
- ajout de treize cartes et de trois matrices de référence ;
- espaces vectoriels, modèles, dimensions, métriques, normalisation, fragments, métadonnées, collections, exact, ANN, filtres, cycle de vie, réindexation et évaluation indexés ;
- Qdrant `1.18.2`, Faiss `1.14.3`, Chroma `1.5.9` et Sentence Transformers `5.5.1` revus comme références documentaires ;
- campagne temporaire de 43 contrats synthétiques réussie avec CPython `3.12.3` sans réseau, modèle, backend vectoriel ni donnée utilisateur ;
- échecs préparatoires du seuil 42/43 et de l’import dynamique Python 3.12 tracés avant le run réussi ;
- métriques statiques : 424 lignes, 19 titres, 13 fiches, 3 matrices, 67 liens, 28 renvois vers les Livres I à IV et 12 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 16 — Patrons d’architecture, niveau Élevée ;
- aucun Qdrant, Faiss, Chroma, modèle, Godot, réseau, GPU, corpus réel, benchmark matériel, approbation juridique ou PDF produit.


### 2026-07-29T01:06:05+02:00 — version 4.01.0

- création de la fiche 14 — Schémas SQLite et migrations ;
- ajout de treize cartes, de trois matrices et de trois extraits SQL minimaux ;
- identité, versions, affinités, tables `STRICT`, clés, contraintes, relations, index, pragmas, transactions, migrations, sauvegardes et diagnostics indexés ;
- documentation officielle SQLite `3.53.4` revue le 29 juillet 2026 ;
- campagne temporaire de 36 bases et opérations synthétiques réussie avec Python `3.12.3`, module `sqlite3` `2.6.0` et SQLite `3.45.1` ;
- différence entre version documentaire et runtime de fixture conservée explicitement ;
- métriques statiques : 487 lignes, 18 titres, 13 fiches, 3 matrices, 47 liens, 20 renvois vers les Livres I à IV et 19 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 15 — Bases vectorielles et recherche sémantique, niveau Élevée ;
- aucun Godot, addon, export, fichier utilisateur, base de production, benchmark, approbation juridique ou PDF produit.


### 2026-07-28T23:25:14+02:00 — version 4.00.0

- création de la fiche 13 — Structures JSON et formats d’échange ;
- ajout de treize cartes et de trois matrices compactes ;
- JSON, JSONL, JSON Text Sequences, CSV, YAML, Resources, scènes et configurations Godot distingués ;
- format, schéma, sérialisation, transport, stockage, conversion, round-trip, canonicalisation et intégrité séparés ;
- profils stricts, encodages, types média, versions, limites et risques documentés ;
- documentations officielles RFC, YAML, JSON Schema, Python, PyYAML, OWASP et Godot `4.7.1-stable` revues le 28 juillet 2026 ;
- campagne temporaire de 24 fixtures locales en mémoire prévue comme porte avant commit ;
- métriques statiques : 419 lignes, 18 titres, 13 fiches, 3 matrices, 53 liens, 18 renvois vers les Livres I à IV et 18 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 14 — Schémas SQLite et migrations, niveau Élevée ;
- aucun moteur Godot, fichier utilisateur, réseau, secret, archive, convertisseur permanent, artefact du Companion Pack, approbation juridique ou PDF produit.


### 2026-07-28T22:48:26+02:00 — version 3.99.0

- création de la fiche 12 — Référence Python ;
- ajout de treize cartes et de trois matrices compactes ;
- environnements, types, collections, flux, fonctions, modules, fichiers, CLI, tests, dépendances, packaging et sécurité indexés ;
- matrice Python/GDScript ajoutée sans traduction mécanique ni déplacement d’autorité ;
- documentations officielles CPython `3.14.6`, Python 3.14 et PyPA revues le 28 juillet 2026 ;
- métriques statiques : 403 lignes, 18 titres, 13 fiches, 3 matrices, 60 liens, 21 renvois vers les Livres I à IV et 21 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 13 — Structures JSON et formats d’échange, niveau Élevée ;
- aucun interpréteur, environnement, module, test, dépendance, processus, build, artefact du Companion Pack, approbation juridique ou PDF produit.


### 2026-07-28T22:02:17+02:00 — version 3.98.0

- création de la fiche 11 — Référence GDScript ;
- ajout de treize cartes et de trois matrices compactes ;
- syntaxe, types, opérateurs, contrôle de flux, fonctions, classes, annotations, collections, signaux, ressources et diagnostics indexés ;
- aide-mémoire relié au chapitre pédagogique du Livre II sans duplication du cours ;
- documentation officielle de Godot `4.7.1-stable`, du typage, du guide de style, des exports et des avertissements revue le 28 juillet 2026 ;
- métriques statiques : 387 lignes, 18 titres, 13 fiches, 3 matrices, 68 liens, 39 renvois vers les Livres I à IV et 36 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 12 — Référence Python, niveau Élevée ;
- aucun binaire Godot, parseur, import, scène, test, migration, artefact du Companion Pack, approbation juridique ou PDF produit.


### 2026-07-28T21:24:52+02:00 — version 3.97.0

- création de la fiche 10 — Bibliothèque de scripts et recettes de code ;
- ajout de treize cartes, trois matrices et 8 blocs contrôlés ;
- recettes GDScript, Python, PowerShell et Bash cataloguées ;
- statuts pédagogique, squelette, syntaxe, tests, qualification, production et retrait séparés ;
- entrées, sorties, codes, effets de bord, sécurité, licences et douze tests de qualification documentés sans exécution inventée ;
- documentations officielles de Godot 4.7, Python 3.14, PowerShell 7.6 et Bash revues le 28 juillet 2026 ;
- métriques statiques : 528 lignes, 18 titres, 13 fiches, 3 matrices, 46 liens, 18 renvois vers les Livres I à IV et 18 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 11 — Référence GDScript, niveau Élevée ;
- aucun parseur, moteur, shell, test, fixture, processus, secret, réseau, artefact du Companion Pack, approbation juridique ou PDF produit.


### 2026-07-28T19:12:00+02:00 — version 3.96.0

- création de la fiche 09 — Bibliothèque de prompts ;
- ajout de treize cartes et de trois matrices compactes ;
- prompts textuels, structurés, RAG, code, visuels, audio et narratifs catalogués ;
- template, variante, instance, requête, réponse brute, résultat interprété et décision séparés ;
- variables, modèles cibles, paramètres, injections, outils et douze tests de qualification documentés sans résultat inventé ;
- sources officielles d’OpenAI, Google, Anthropic, Ollama et OWASP revues le 28 juillet 2026 ;
- métriques statiques : 402 lignes, 18 titres, 13 fiches, 3 matrices, 51 liens, 27 renvois propriétaires et 27 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 10 — Bibliothèque de scripts et recettes de code, niveau Élevée ;
- aucun modèle, API, outil, prompt du Companion Pack, réponse, parse, génération, mesure, secret, approbation juridique ou PDF produit.


### 2026-07-28T18:20:01+02:00 — version 3.95.0

- création de la fiche 08 — Bibliothèque de workflows ;
- ajout de treize cartes et de trois matrices compactes ;
- workflows Godot, Blender, ComfyUI, audio et documentation catalogués ;
- définition, exécution, cache, artefact, preuve, reprise, profils Solo/Studio et acceptation séparés ;
- sécurité, idempotence, retry, checkpoints, manifestes et douze tests de qualification documentés sans résultat inventé ;
- sources officielles de Godot, Blender, ComfyUI, GitHub Actions, FFmpeg et Pandoc revues le 28 juillet 2026 ;
- métriques statiques : 409 lignes, 18 titres, 13 fiches, 3 matrices, 70 liens, 36 renvois vers les Livres I à IV et 36 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 09 — Bibliothèque de prompts, niveau Élevée ;
- aucun template du Companion Pack, workflow runtime, import, export, média, build, mesure, secret, approbation juridique ou PDF produit.


### 2026-07-28T17:27:15+02:00 — version 3.94.0

- création de la fiche 07 — Fiches des modèles audio ;
- ajout de treize cartes et de trois matrices compactes ;
- Kokoro-82M, Piper, Chatterbox, Whisper, MusicGen et AudioGen qualifiés ;
- modèles, moteurs, voix, locuteurs, consentements, phonémiseurs, vocodeurs, codecs, VAD et dérivés séparés ;
- langues, licences, usages, mémoire, facteurs temps réel et protocole de douze tests documentés sans résultat inventé ;
- sources officielles des éditeurs et dépôts revues en ligne le 28 juillet 2026 sans reprendre leurs performances ou échantillons promotionnels ;
- métriques statiques : 394 lignes, 18 titres, 13 fiches, 3 matrices, 61 liens, 27 renvois vers les Livres I à IV et 27 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 08 — Bibliothèque de workflows, niveau Élevée ;
- aucun modèle, voix ou enregistrement téléchargé, aucune synthèse, transcription, génération, mesure, écoute, approbation juridique, artefact du Companion Pack ou PDF produit.

### 2026-07-28T16:17:52+02:00 — version 3.93.0

- création de la fiche 06 — Fiches des modèles visuels ;
- ajout de treize cartes et de trois matrices compactes ;
- Stable Diffusion XL/3.5, FLUX.2/FLUX.1, Qwen-Image, HunyuanImage-3.0 et HiDream-I1 qualifiés ;
- checkpoints, VAE, encodeurs, ControlNet, LoRA, upscalers et dérivés communautaires séparés ;
- licences, provenance, formats, résolutions, samplers, variables VRAM et protocole de dix tests documentés ;
- sources officielles des éditeurs, de ComfyUI et des composants revues en ligne le 28 juillet 2026 sans reprendre leurs images ou performances promotionnelles ;
- métriques statiques : 380 lignes, 18 titres, 13 fiches, 3 matrices, 65 liens, 20 renvois vers les Livres I à IV et 19 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 07 — Fiches des modèles audio, niveau Élevée ;
- aucun modèle téléchargé, workflow chargé, image générée, mesure, approbation juridique, artefact du Companion Pack ou PDF produit.

### 2026-07-28T15:09:18+02:00 — version 3.92.0

- création de la fiche 05 — Fiches des modèles de langage ;
- ajout de treize cartes et de trois matrices compactes ;
- Qwen3, Gemma 4, Phi-4, Granite 4, Mistral Small 4, Llama et DeepSeek-R1 qualifiés ;
- familles, checkpoints, modèles denses, MoE, paramètres totaux et actifs séparés ;
- quantifications, contextes, langues, licences, provenance, poids théoriques et protocole de huit tests documentés ;
- sources officielles des éditeurs revues en ligne le 28 juillet 2026 sans reprendre leurs performances promotionnelles ;
- métriques statiques : 379 lignes, 20 titres, 13 fiches, 3 matrices, 56 liens, 19 renvois vers les Livres I à IV et 19 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 06 — Fiches des modèles visuels, niveau Élevée ;
- aucun modèle téléchargé, aucune inférence, mesure, approbation juridique, création d’artefact du Companion Pack ou production PDF.

### 2026-07-28T14:25:00+02:00 — version 3.91.0

- création de la fiche 04 — Fiches des moteurs et backends IA ;
- ajout de treize cartes et de trois matrices compactes ;
- Ollama, llama.cpp, LocalAI, ComfyUI, CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP, faster-whisper, whisper.cpp et Piper distingués ;
- séparation moteur, backend, modèle, interface, API et orchestration explicitée ;
- voies CPU et AMD, mémoire, sécurité, formats, API et diagnostics par couches documentés ;
- métriques statiques : 363 lignes, 20 titres, 13 fiches, 3 matrices, 83 liens, 57 renvois vers les Livres I à IV et 52 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 05 — Fiches des modèles de langage, niveau Élevée ;
- aucune commande, inférence, accélération, mesure, vérification web, création d’artefact du Companion Pack ou production PDF.

### 2026-07-28T13:42:52+02:00 — version 3.90.0

- création de la fiche 03 — Fiches des logiciels et outils ;
- ajout de douze cartes d’outils, d’un contrat commun et de trois matrices compactes ;
- Windows Terminal, PowerShell, WinGet, Git, GitHub, VS Code, Python, Docker, Godot, Blender, ComfyUI, Open WebUI et Open Terminal référencés ;
- versions datées, formats, intégrations, alternatives, limites, commandes minimales et liens officiels enregistrés ;
- frontière préservée avec les décisions de la fiche 02 et les moteurs ou backends du chapitre 4 ;
- métriques statiques : 355 lignes, 19 titres, 13 fiches, 3 matrices, 64 liens, 28 renvois vers les Livres I à IV et 24 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 04 — Fiches des moteurs et backends IA, niveau Élevée ;
- aucune installation, commande, vérification web, exécution runtime, création d’artefact du Companion Pack ou production PDF.

### 2026-07-28T13:00:32+02:00 — version 3.89.0

- création de la fiche 02 — Arbres de décision ;
- ajout de douze arbres ou cartes décisionnelles et de trois matrices compactes ;
- chemins AMD, CPU, DirectML, ZLUDA, Windows natif, WSL, Docker et ComfyUI distingués ;
- décisions pour moteurs LLM, supports de données, transports IA, assets, diagnostic, Solo/Studio et publication ajoutées ;
- critères pondérés séparés des portes éliminatoires et situations sans solution unique documentées ;
- quatre scénarios conditionnels ajoutés sans les présenter comme benchmarks ;
- métriques statiques : 344 lignes, 19 titres, 14 fiches, 3 matrices, 63 renvois vers les Livres I à IV et 32 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 03 — Fiches des logiciels et outils, niveau Élevée ;
- aucune exécution runtime, étude lecteur, calibration des poids, création d’artefact du Companion Pack ou production PDF.

### 2026-07-28T11:28:35+02:00 — version 3.88.0

- correction de la conception éditoriale du Livre V après revue utilisateur ;
- création de `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` comme profil spécialisé ;
- clarification des règles générales conservées et des obligations tutoriel non applicables ;
- refonte de la fiche 01 en 263 lignes, 12 fiches et 2 matrices ;
- suppression des résultats d’apprentissage, commandes sans valeur de référence, dix diagnostics imposés et synthèse `Project Asteria` ;
- ajout de 167 liens vers les Livres I à IV, dont 29 liens profonds vers des sous-sections ;
- adaptation des validateurs au format `reference-cards` ;
- maintien de la prochaine action sur `Livre-V/CHAPITRE-02-Arbres-de-decision.md` ;
- aucune exécution runtime, étude lecteur, création d’artefact du Companion Pack ou production PDF.

### 2026-07-28T09:26:30+02:00 — version 3.87.0

- ouverture du Livre V — Encyclopédie technique et bibliothèque de référence ;
- création du chapitre 1 — Carte générale de la collection ;
- structure Volume 0, Livres I à V et Companion Pack cartographiée ;
- dépendances, parcours débutant, production, dépannage, Solo et Studio documentés ;
- entrées par besoin, outil et système et index initial des prérequis ajoutés ;
- fonctions, paramètres, types, retours, opérateurs, commandes et sorties expliqués ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- validateurs légers étendus explicitement au Livre V ;
- métriques statiques : 1095 lignes, 51 titres, 33 blocs clôturés et 10 diagnostics ;
- prochaine action déplacée vers le chapitre 2 — Arbres de décision, niveau Élevée ;
- aucun test runtime, étude lecteur, index interactif, artefact du Companion Pack ou PDF produit.

### 2026-07-28T07:28:40+02:00 — version 3.86.0

- clôture technique et PDF du Livre IV — Finalisation, optimisation, publication et maintenance ;
- validation transversale des 22 chapitres, audits, preuves, identifiants, liens, doublons et repères réussie ;
- trois caractères de contrôle invisibles supprimés des exemples de chemins des chapitres 16 et 18 ;
- filtre PDF corrigé pour préserver le chapitre 2 — Stratégie générale d’assurance qualité ;
- garde-fou ajouté : les 22 titres du Livre IV doivent apparaître dans le texte extrait ;
- compilation finale Pandoc/XeLaTeX réussie sur la tête `f6b2118daf23edf7595ce9d5e2b4d300c00b1d40` ;
- PDF cumulatif final : 3 672 pages A4, 9 428 292 octets, version 1.5, non chiffré et texte extractible ;
- empreinte PDF `013f8d9bf800d74b408c806f5b5ea6e291e85568b152799feb2b75152de7f9fe` ;
- `qpdf --check`, contrôle des polices incorporées et exclusion des contenus QA internes réussis ;
- 49 pages inspectées avec Poppler, 12 pages comparées avec PDFium et neuf pages de tête finale réinspectées ;
- run final `30331869053`, artefact `8677727006`, digest `sha256:0109aa765694cee0c6cc2663e83a3310485e5915517e3c0c35fcb95b43ac59ce` ;
- Livre IV accepté au niveau `static-review+pdf-inspected` avec réserves runtime, licence globale et balisage d’accessibilité ;
- jalon actif déplacé vers M6 — Livre V ;
- prochaine action : `Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md`, niveau Élevée.

### 2026-07-28T05:41:07+02:00 — version 3.85.0

- création du chapitre 22 du Livre IV — Maintenance, archivage et pérennité ;
- maintenance, archivage, sauvegarde, miroir, fixité, signature, restauration et reconstruction distingués ;
- calendrier, responsabilités, inventaire, dépendances, vulnérabilités, SBOM et décisions de mise à niveau documentés ;
- topologie de copies, Git bundle, LFS, sous-modules, releases, environnements et artefacts encadrés ;
- checksums, signatures, contrôles de fixité, restaurations isolées et reconstructions historiques préparés ;
- reproductibilité, écarts, formats durables, migrations sans écrasement et données historiques gouvernés ;
- succession, comptes, certificats, clés, fournisseurs, fin de support, ouverture éventuelle et communauté documentés ;
- procédures Solo/Studio, préflight, synthèse `Project Asteria` et dix diagnostics complets ajoutés ;
- métriques statiques provisoires : 1939 lignes, 60 titres, 48 blocs de code ou de données, 28 explications hors diagnostics et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- progression documentaire du Livre IV portée à 22 chapitres sur 22 ;
- prochaine action déplacée vers la construction, le préflight et l’inspection du PDF complet du Livre IV, niveau Élevée ;
- aucune archive, restauration, reconstruction, succession, fin de support publique, exécution runtime ou production PDF revendiquée.


### 2026-07-27T21:47:17+02:00 — version 3.84.0

- création du chapitre 21 du Livre IV — Modding et contenu communautaire ;
- mods, UGC, plugins, DLC, patches, surfaces d’extension, capacités et ensembles de mods distingués ;
- niveaux de support déclaratif, packs Godot et code exécutable encadrés ;
- manifestes, identités namespacées, versions, dépendances, capacités, licences et empreintes documentés ;
- staging, inspection d’archives, quotas, chargement runtime et PCK sans remplacement préparés ;
- scripts communautaires et extensions natives exclus du support public sans isolation démontrée ;
- dépendances, cycles, contraintes, ordre stable, conflits, fusion, mode sûr et désactivation gouvernés ;
- sauvegardes moddées, migrations, dépréciation, localisation, accessibilité et multijoueur préparés ;
- SDK, templates, mod d’exemple, validateurs, plateformes UGC, provenance, modération et support documentés ;
- métriques statiques : 1771 lignes, 66 titres, 37 blocs significatifs, 23 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 22 — Maintenance, archivage et pérennité, niveau Élevée ;
- aucun chargeur, SDK, mod, sandbox, plateforme UGC, campagne runtime, modération réelle ou PDF du Livre IV produit.

### 2026-07-27T19:11:44+02:00 — version 3.83.0

- création du chapitre 20 du Livre IV — Correctifs, mises à jour et retour arrière ;
- correctif, hotfix, mise à jour, patch différentiel, interruption, rollback et roll-forward distingués ;
- versions produit, build, contenu, sauvegarde et protocole séparées ;
- canaux interne, bêta et stable, promotion du même candidat et versions sources supportées documentés ;
- packages complets, patches différentiels, manifestes, préflight, staging, intégrité, activation et reprise préparés ;
- sauvegardes versionnées, copies pré-migration, registres immuables, réversibilité et compatibilité encadrés ;
- déploiements progressifs, observation, portes d’arrêt, interruption et population déjà exposée distingués ;
- rollback binaire, restauration de données, désactivation, hotfix et roll-forward gouvernés ;
- Steam, itch.io, Google Play, Apple, launcher, hors-ligne, sécurité, confidentialité et support documentés ;
- tests depuis plusieurs versions, injection de fautes, exercice de rollback, procédures Solo/Studio et dix diagnostics ajoutés ;
- métriques statiques : 1855 lignes, 73 titres, 64 blocs significatifs, 44 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 21 — Modding et contenu communautaire, niveau Élevée ;
- aucun package, patch, migration, canal, déploiement, interruption, rollback, hotfix, support runtime, opération de plateforme ou PDF du Livre IV produit.

### 2026-07-27T18:41:51+02:00 — version 3.82.0

- création du chapitre 19 du Livre IV — Localisation et internationalisation ;
- internationalisation, localisation, traduction, transcréation et adaptation culturelle distinguées ;
- locales, langue source, langue cible, région, écriture, direction, normalisation et politiques de repli documentées ;
- clés stables, chaînes externalisées, variables nommées, balises protégées et contenus dynamiques encadrés ;
- pluriels, genres grammaticaux, dates, heures, calendriers, nombres, montants en euros et unités préparés ;
- écritures LTR/RTL, BiDi, shaping, segmentation, saisie, glyphes, polices et fallbacks gouvernés ;
- mise en page flexible, pseudo-localisation longue et bidirectionnelle, catalogues, extraction et statuts documentés ;
- traduction, relecture linguistique, validation en contexte, glossaire, mémoire, voix, sous-titres et médias localisés préparés ;
- automatisation, captures, écritures non latines, changement de langue, persistance, sécurité et procédures Solo/Studio encadrés ;
- métriques statiques : 1325 lignes, 60 titres, 42 blocs significatifs, 23 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 20 — Correctifs, mises à jour et retour arrière, niveau Élevée ;
- aucune locale qualifiée, traduction approuvée, police, catalogue final, pseudo-localisation exécutée, relecture native, build multilingue, publication réelle, exécution runtime ou PDF du Livre IV produit.

### 2026-07-27T13:24:17+02:00 — version 3.81.0

- création du chapitre 18 du Livre IV — Accessibilité ;
- commandes, visuel, audio, cognition, motricité et temps organisés par barrières et tâches observables ;
- matrice d’accessibilité, profils composables, premier démarrage, application, restauration et migration des réglages documentés ;
- remapping, conflits, prompts, maintiens, répétitions, combinaisons, deadzones, sensibilité, inversion et alternatives numériques encadrés ;
- texte, contraste, focus, tailles de cible, reflow, mouvement, caméra, flashs et photosensibilité préparés ;
- sous-titres, captions, mixage, mono, plage dynamique, indices visuels, description audio, TTS et lecteurs d’écran distingués ;
- cognition, erreurs, récupération, aides motrices, haptique, sauvegardes, checkpoints et options de rythme documentés ;
- parcours représentatifs, profils, consentement, minimisation, revues automatiques, manuelles et spécialisées préparés ;
- registre des limites connues, déclaration publique corrélée au build, support, modes Solo/Studio et dix diagnostics ajoutés ;
- métriques statiques : 2090 lignes, 66 titres, 59 blocs significatifs, 44 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 19 — Localisation et internationalisation, niveau Élevée ;
- aucune option, intégration, session utilisateur, revue spécialisée, certification, conformité globale, déclaration publiée, exécution runtime ou PDF du Livre IV produit.

### 2026-07-27T09:40:10+02:00 — version 3.80.0

- création du chapitre 17 du Livre IV — Publication et distribution ;
- export, package, artefact, build boutique, soumission, approbation, publication et lancement distingués ;
- dossier de publication, identités produit, matrice des boutiques et registre des exigences volatiles documentés ;
- même candidat binaire, manifestes et empreintes du chapitre 16 réutilisés sans reconstruction ;
- fiches produit, affirmations, exigences système, médias, droits, textes alternatifs, tags et catégories encadrés ;
- prix candidats en euros, territoires, contrats, licences, attributions, classifications d’âge et déclarations de confidentialité préparés ;
- rôles, MFA, secrets, canaux, clés d’accès, Steam, itch.io, Google Play, App Store Connect et boutiques supplémentaires qualifiés ;
- calendrier, dry-run, reçus, go/no-go, lancement, support, métriques et procédures Solo/Studio préparés ;
- métriques statiques : 2435 lignes, 95 titres, 67 blocs significatifs, 51 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 18 — Accessibilité, niveau Élevée ;
- aucun compte, page boutique, média final, prix réel, classification, formulaire, clé, téléversement, soumission, revue, vente, lancement runtime ou PDF du Livre IV produit.

### 2026-07-27T08:32:16+02:00 — version 3.79.0

- création du chapitre 16 du Livre IV — Exports Godot et packaging ;
- export, build, package, artefact, release et publication distingués ;
- matrice de cibles, templates, presets, credentials, identités et profils debug/test/release encadrés ;
- filtres de ressources, fichiers privés, dépendances natives, GDExtension, icônes et métadonnées documentés ;
- Windows, Linux, macOS, Android, iOS, Web et référence au serveur dédié préparés avec leurs préconditions ;
- scripts canoniques, staging neuf, manifestes fermés, checksums, archives et reçus de promotion préparés ;
- signature, notarisation, empreinte finale et promotion des mêmes octets ordonnées ;
- campagne d’installation et lancement sur machine propre préparée sans exécution revendiquée ;
- métriques statiques : 2004 lignes, 73 titres, 56 blocs significatifs, 40 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 17 — Publication et distribution, niveau Élevée ;
- aucun preset, template, SDK, certificat, export, signature, package, installation, lancement runtime ou PDF du Livre IV produit.

### 2026-07-27T01:20:18+02:00 — version 3.78.0

- création du chapitre 15 du Livre IV — Sauvegardes, migrations et reprise après incident ;
- sauvegarde, réplication, snapshot, synchronisation, export logique et archive distingués ;
- inventaire des actifs, autorités, propriétaires, sensibilités et dépendances préparé ;
- objectifs RPO/RTO, services minimaux, générations, rétention et budget candidat structurés ;
- supports, identités, copies hors site ou immuables, manifestes et empreintes encadrés ;
- dépôt Git, builds retenus, données joueurs, SQLite, PostgreSQL, services et volumes couverts ;
- secrets, chiffrement, récupération de clés, jobs, métriques et runbooks préparés ;
- restauration isolée, contrôles structurels et métier, mesures et approbation humaine documentés ;
- migrations immuables, expand/contract et compatibilité application/données encadrés ;
- scénarios catastrophe, compromission, rançongiciel, rôles, exercices et écarts préparés ;
- dix diagnostics conformes et frontières avec les chapitres 8 et 9 du Livre II, puis 13, 14, 16, 20 et 22 maintenues ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 16 — Exports Godot et packaging, niveau Élevée ;
- aucune génération, sauvegarde, restauration, migration, mesure RPO/RTO, reprise runtime ou PDF du Livre IV revendiqué.

### 2026-07-26T21:42:29+02:00 — version 3.77.0

- création du chapitre 14 du Livre IV — DevOps et intégration continue ;
- intégration continue, livraison, déploiement et publication distingués ;
- branches, pull requests, tags, versions, runs, tentatives, builds et empreintes séparés ;
- scripts canoniques, workflows, permissions minimales et entrées non fiables encadrés ;
- matrices, environnements propres, caches, artefacts, manifestes et rétention structurés ;
- secrets, environnements protégés, OIDC, attestations et dépendances d’actions préparés ;
- délais, concurrence, annulation, retries bornés et reprise après échec documentés ;
- reconstruction depuis clone neuf et distinction procédurale/binaire préparées ;
- dix diagnostics conformes et frontières avec les chapitres 3, 13, 15, 16 et 17 maintenues ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 15 — Sauvegardes, migrations et reprise après incident, niveau Élevée ;
- aucun workflow de `Project Asteria`, build, test runtime, package, cache, attestation, secret, runner, déploiement ou PDF du Livre IV revendiqué.

### 2026-07-26T17:45:00+02:00 — version 3.76.0

- création du chapitre 13 du Livre IV — Serveurs dédiés et sécurité réseau ;
- export dédié, mode headless, tag de fonctionnalité et rôle serveur sans joueur local distingués ;
- configuration, credentials, état durable, journaux, releases et manifeste d’artefact séparés ;
- exposition ENet UDP, pare-feu Windows/Linux, identité systemd et conteneur non privilégié préparés ;
- liveness, readiness, admission, authentification et drainage structurés ;
- tailles, rejeux, quotas, concurrence, amplification, journaux et métriques bornés ;
- sauvegarde, restauration, promotion, mise à jour, rollback et rotation de secrets documentés ;
- matrice de durcissement, sévérités, runbook d’incident et responsabilités Solo/Studio préparés ;
- dix diagnostics conformes et frontières avec les chapitres 11, 12 et 14 maintenues ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- groupe Optimisation et multijoueur terminé à 8 chapitres sur 8 ;
- prochaine action déplacée vers le chapitre 14 — DevOps et intégration continue, niveau Élevée ;
- aucun build, hôte, service, pare-feu, conteneur, scan, attaque simulée, restauration ou résultat de durcissement revendiqué.

### 2026-07-26T17:30:00+02:00 — version 3.75.0

- création du chapitre 12 du Livre IV — Synchronisation, autorité et prédiction ;
- commandes, événements, snapshots, deltas, acquittements et séquences distingués ;
- autorité réseau séparée de l’autorité métier et validation des RPC encadrée ;
- `SceneReplicationConfig`, `MultiplayerSynchronizer` et `MultiplayerSpawner` documentés ;
- pertinence par pair, canaux, modes de transfert et idempotence structurés ;
- interpolation, extrapolation, prédiction et réconciliation préparées ;
- rollback borné, anneau d’états, RNG local et compensation historique encadrés ;
- budgets de bande passante, quantification, adaptation et portes de promotion documentés ;
- empreintes d’état, comparateur Python, captures expurgées et profils d’altération préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 13 — Serveurs dédiés et sécurité réseau, niveau Élevée ;
- aucun synchroniseur, spawner, snapshot, prédicteur, rollback, campagne réseau ou gain de bande passante revendiqué.

### 2026-07-26T16:42:00+02:00 — version 3.74.0

- création du chapitre 11 du Livre IV — Architecture multijoueur ;
- client-serveur, pair-à-pair, hybride, serveur d’écoute, serveur dédié et relais comparés ;
- client-serveur autoritaire retenu comme défaut documenté de `Project Asteria` ;
- identité durable, membre de session, pair, génération et ticket distingués ;
- contrats de session, lobby, protocole, capacités et compatibilité structurés ;
- initialisation ENet, signaux de cycle de vie, fermeture et chemin hors ligne documentés ;
- découverte, invitation, admission et transport de jeu séparés ;
- reconnexion par nouveau pair, ticket opaque, rotation, génération et backoff encadrée ;
- migration d’hôte maintenue fermée jusqu’à preuve contre le double hôte ;
- prototype, journaux, catalogue de tests, matrice de risques, coûts, ADR et rollback préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 12 — Synchronisation, autorité et prédiction, niveau Élevée ;
- aucune session, reconnexion, migration d’hôte, qualification NAT, mesure de coût ou disponibilité runtime revendiquée.

### 2026-07-26T10:13:20+02:00 — version 3.73.0

- création du chapitre 10 du Livre IV — Optimisation des scènes, scripts et systèmes de jeu ;
- contrat de benchmark, manifeste d’environnement, budgets et échantillonnage documentés ;
- fréquences, accumulateurs, time slicing, quotas adaptatifs et priorités encadrés ;
- activation par visibilité, distance, hystérésis et LOD logique distinguée de l’autorité gameplay ;
- groupes, appels différés uniques, références mises en cache et index spatial structurés ;
- cycle de vie des signaux, coalescence, pooling borné, remise à zéro et tampons réutilisés documentés ;
- découpage de scènes, préparation en thread et porte de migration vers les API serveur encadrés ;
- exemples avant/après, seuils, porte de promotion, checklist et rollback préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 11 — Architecture multijoueur, niveau Élevée ;
- aucun benchmark, seuil qualifié, pool runtime, LOD logique, migration serveur ou gain revendiqué.

### 2026-07-26T08:52:20+02:00 — version 3.72.0

- création du chapitre 9 du Livre IV — Chargements, streaming et gestion des ressources ;
- contrats de transition, budgets, manifeste de stockage et états du gestionnaire documentés ;
- chargement fileté, polling non bloquant, progression pondérée et activation différée encadrés ;
- priorités, vieillissement, admission, coalescence, annulation logique, reprises et replis documentés ;
- dépendances, modes de cache, scènes de transition et racine persistante distingués ;
- zones, chunks, hystérésis, prédiction, mémoire d’admission et éviction bornée structurés ;
- tests de stockage lent, parcours prolongé, rapport avant/après et rollback préparés ;
- progression accessible, erreurs honnêtes, sauvegarde et transfert d’état encadrés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu, niveau Élevée ;
- aucun gestionnaire runtime, profil qualifié, test de stockage, parcours prolongé ou gain revendiqué.

### 2026-07-26T08:02:49+02:00 — version 3.71.0

- création du chapitre 8 du Livre IV — Optimisation RAM, VRAM et allocations ;
- budgets souples et durs, unités, campagne cyclique et manifeste d’environnement documentés ;
- moniteurs `Performance`, appels `OS`, `RenderingServer` et vue processus Windows distingués ;
- phases, plateaux, pente, percentiles et suspicion de fuite encadrés ;
- durée de vie des nœuds, références faibles, `RefCounted`, signaux et duplications documentée ;
- caches LRU et pondérés, expiration, pools et allocations temporaires bornés ;
- textures, images CPU, ressources vidéo et sous-ressources distinguées ;
- test de longue durée, rapport avant/après, rollback et portes de qualité préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 9 — Chargements, streaming et gestion des ressources, niveau Élevée ;
- aucune campagne mémoire, série, fuite attribuée, cache qualifié ou amélioration runtime revendiquée.

### 2026-07-26T03:23:02+02:00 — version 3.70.0

- création du chapitre 7 du Livre IV — Profilage GPU et optimisation du rendu ;
- budget GPU, contrat de benchmark, manifeste AMD et scène de stress documentés ;
- Visual Profiler, moniteurs `Performance`, `RenderingServer` et temps GPU de viewport expliqués ;
- draw calls, primitives, passes visibles, ombres et compilations de pipeline distingués ;
- fill rate, overdraw, transparence, LOD, culling, shaders, lumières, ombres et post-traitement encadrés ;
- profils graphiques, captures AMD, inspection RenderDoc et rapport de coût par effet préparés ;
- comparaison visuelle, campagne avant/après, porte de décision et rollback documentés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 8 — Optimisation RAM, VRAM et allocations, niveau Élevée ;
- aucune scène de stress, capture, série GPU, profil qualifié ou amélioration runtime revendiquée.

### 2026-07-26T02:53:24+02:00 — version 3.69.0

- création du chapitre 6 du Livre IV — Profilage CPU ;
- budgets de frame, distributions, warm-up, répétitions et contrats de benchmark documentés ;
- Profiler Godot, Monitors, singleton `Performance`, moniteurs personnalisés et chronométrage borné expliqués ;
- analyse des scripts, de la physique, de la navigation, de l’IA et des tâches parallèles structurée ;
- scènes de benchmark, manifestes d’environnement, hypothèses et rapports avant/après préparés ;
- médiane, p95, p99, maximum et dépassements de budget conservés ;
- portes de régression fonctionnelle, retour arrière et approbation humaine encadrés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 7 — Profilage GPU et optimisation du rendu, niveau Élevée ;
- aucune scène de benchmark, capture, série de mesures, budget qualifié ou amélioration runtime revendiquée.

### 2026-07-26T01:20:53+02:00 — version 3.68.0

- création du chapitre 5 du Livre IV — Journalisation et observabilité locale ;
- niveaux, catégories, taxonomie, schéma structuré, horodatage et corrélation documentés ;
- distinction entre événements, métriques et traces établie ;
- émetteur Godot, sinks, JSONL, collecteur Python et index SQLite préparés ;
- rotation, rétention, purge, backpressure, échantillonnage, débit et déduplication encadrés ;
- confidentialité, classification, expurgation, détection de secrets et export local documentés ;
- dashboard local en lecture seule et incident simulé de stockage saturé préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 6 — Profilage CPU, niveau Élevée ;
- aucun journal runtime, collecteur, dashboard, incident simulé, scan de secrets ou mesure de coût revendiqué.

### 2026-07-26T00:30:21+02:00 — version 3.67.0

- création du chapitre 4 du Livre IV — Débogage et reproduction des anomalies ;
- rapports exploitables, environnements, builds, configurations, états initiaux, étapes, attendus et observés documentés ;
- archives diagnostiques, manifestes d’intégrité, expurgation, fenêtres de journaux et fixtures synthétiques encadrés ;
- reproduction indépendante humaine ou scriptée préparée ;
- réduction des étapes, états et entrées documentée sans effacer le rapport original ;
- doublons, défaut canonique, fermeture, réouverture et lien de non-régression encadrés ;
- rôles Solo/Studio et triage documentés ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 5 — Journalisation et observabilité locale, niveau Élevée ;
- aucun défaut réel, archive, reproduction, dump, mesure runtime ou donnée joueur revendiqué.

### 2026-07-26T00:16:25+02:00 — version 3.66.0

- création du chapitre 3 du Livre IV — Tests fonctionnels et tests de régression ;
- catalogue, cas, fixtures synthétiques, seeds, états contrôlés et oracles documentés ;
- suites smoke, rapide, complète et publication définies ;
- non-régression, mutation connue isolée, quarantaine et tests instables encadrés ;
- dix diagnostics conformes ;
- prochaine action déplacée vers le chapitre 4 — Débogage et reproduction des anomalies ;
- aucune campagne ou mesure runtime revendiquée.



### 2026-07-25T21:28:22+02:00 — version 3.65.0

- création du chapitre 2 du Livre IV — Stratégie générale d’assurance qualité ;
- charte QA, modèle de qualité, niveaux, familles et matrice risques/contrôles documentés ;
- prévention, détection et correction séparées ;
- portes `G0` à `G5`, critères d’entrée/sortie et statuts de décision définis ;
- rôles Solo/Studio, RACI, indépendance et calendrier encadrés ;
- environnements, baselines, sévérité, priorité, triage, stop-ship et dérogations documentés ;
- QA documentaire, technique, artistique et produit reliées ;
- accessibilité, sécurité, données assistées et récupérabilité intégrées ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 3 — Tests fonctionnels et tests de régression, niveau Élevée ;
- aucune campagne, revue spécialisée, décision de porte, mesure runtime ou publication produit revendiquée.


### 2026-07-25T20:33:18+02:00 — version 3.64.0

- correction du chapitre 1 du Livre IV en version `1.0.1` ;
- retrait des deux mentions de PDF présentes dans le texte lecteur ;
- la commande de campagne décrit désormais uniquement l’exécution de la matrice d’équilibrage ;
- la checklist d’acceptation porte désormais sur le confinement des sorties dans le workspace déclaré ;
- décision permanente enregistrée : la génération du PDF du guide appartient à la chaîne de publication documentaire et ne doit pas apparaître comme procédure ou critère métier d’un chapitre ;
- audit, preuve QA, index actif et continuité mis à jour ;
- prochaine action officielle inchangée : Livre IV, chapitre 2.


### 2026-07-25T17:49:48+02:00 — version 3.63.0

- ouverture du Livre IV et création du chapitre 1 — Équilibrage et télémétrie locale ;
- pilote `AST-BALANCE-PILOT-RELAY-EXPEDITION-001` défini sans matérialisation ;
- questions, métriques, unités, dimensions, cardinalité et rétention documentées ;
- compteurs, jauges, distributions, ratios, moyenne, médiane, percentiles et dispersion encadrés ;
- références, candidats, baselines, courbes, rapports de décision et retour arrière préparés ;
- frontières avec combat, économie, écologie, tests, observabilité et automatisation maintenues ;
- scénarios déterministes, graines locales, matrices et comparaisons appariées documentés ;
- collecte locale hors ligne par défaut, minimisation, consentement, retrait et anonymisation encadrés ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 2 — Stratégie générale d’assurance qualité, niveau Élevée ;
- aucune collecte joueur, simulation, analyse Python, décision d’équilibrage, mesure runtime ou PDF du Livre IV produite.


### 2026-07-25T14:46:00+02:00 — version 3.62.0

- validation transversale des trente chapitres, audits et preuves finales du Livre III réussie ;
- compilation du manuel lecteur avec Pandoc/XeLaTeX réussie ;
- préflight `pdfinfo`, `pdffonts`, `qpdf --check` et extraction textuelle réussis ;
- PDF A4 de 2 910 pages produit, texte extractible et polices incorporées ;
- trente ouvertures de chapitre du Livre III, trente pages intermédiaires et pages de transition finales inspectées ;
- vingt-cinq rendus de référence reproduits à l’identique avant la mise à jour de clôture ;
- audits, preuves YAML et protocoles QA confirmés absents du manuel lecteur ;
- M4 et Livre III marqués terminés ; prochaine action déplacée vers le Livre IV, chapitre 1 ;
- licence globale, balisage d’accessibilité et réserves runtime maintenus sans revendication excessive.

### 2026-07-25T09:40:18+02:00 — version 3.61.0

- chapitre 30 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-PRODUCTION-BATCH-SCOUT-RELAY-001` défini pour l’éclaireur, le module de relais et l’expérience de marquages ;
- tâches déterministes, génératives et humaines séparées par contrats explicites ;
- identités de lot, run, tâche, tentative et artefact, manifeste fermé et graphe acyclique documentés ;
- scripts Blender paramétrés, idempotents, exécutables en arrière-plan et limités aux copies isolées préparés ;
- workflows ComfyUI API, modèles, custom nodes, seeds, file locale, historique et quarantaine encadrés ;
- ressources, concurrence, exclusivité GPU, backpressure, délais, annulation et retries bornés documentés ;
- checkpoints par empreinte, reprise, staging, promotion, provenance, journaux et rapports structurés préparés ;
- échantillonnage déterministe, planches comparatives et approbation humaine indépendante imposés ;
- intégration CI, matrices, artefacts, sécurité, quotas, conservation et exemples du Companion Pack préparés ;
- progression documentaire portée à 30 chapitres sur 30 ; prochaine action déplacée vers la clôture PDF du Livre III ;
- aucun lot, script exécuté, workflow soumis, asset, checkpoint, reprise, rapport runtime, approbation artistique, benchmark ou PDF du Livre III produit.

### 2026-07-25T07:39:11+02:00 — version 3.60.0

- chapitre 29 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-ASSET-GATE-SCOUT-RELAY-001` défini pour l’éclaireur et le module de relais ;
- identité, version, empreinte, manifeste, profil et contexte d’usage séparés ;
- états, transitions, rôles, checklist universelle et extensions par famille documentés ;
- provenance, droits, dépendances, géométrie, UV, matériaux, textures, rigs, animations, collisions, sockets et LOD encadrés ;
- VFX, UI et audio reliés à leurs contrats propriétaires sans duplication ;
- scène Godot de validation, fixtures, captures, moniteurs, protocole de mesure, baseline et tolérances préparés ;
- grille artistique, références, constats, sévérités, dérogations, corrections et signatures documentés ;
- automatisation limitée au blocage technique et à la collecte, sans acceptation artistique autonome ;
- progression documentaire portée à 29 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 30 — Automatisation Blender, ComfyUI et production en lots, niveau Élevée ;
- aucun asset, profil, scène, rapport, capture, mesure runtime, revue, benchmark ou PDF du Livre III produit.


### 2026-07-25T06:23:53+02:00 — version 3.59.0

- chapitre 28 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-IMPORT-PILOT-SCOUT-RELAY-001` défini pour l’éclaireur et le module de relais ;
- GLB, glTF séparé, `.blend`, FBX, OBJ et DAE comparés par usage, capacité et dépendance ;
- source, livraison, sidecar `.import`, cache `.godot`, scène importée et scène d’intégration séparés ;
- profils statique, personnage, animation, texture et audio documentés ;
- héritage, composition, externalisation et remapping des matériaux encadrés ;
- squelettes, skins, blendshapes, animations, LOD, collisions, sockets et métadonnées contrôlés ;
- `EditorScenePostImport`, idempotence, sécurité, limites et refus de la réimportation récursive documentés ;
- baseline, diff, protection des personnalisations, campagnes propres et profils de plateforme préparés ;
- progression documentaire portée à 28 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 29 — Validation technique et artistique des assets, niveau Élevée ;
- aucun asset, preset, sidecar, scène, remap, script exécuté, rapport, capture, benchmark ou PDF du Livre III produit.

### 2026-07-24T23:50:00+02:00 — version 3.58.0

- chapitre 27 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-FACE-PILOT-RELAY-DIALOGUE-001` défini sur les voix du relais ;
- graphèmes, phonèmes, allophones, visèmes, silences et différences linguistiques séparés ;
- jeu minimal de visèmes, pose neutre, mâchoire, lèvres, langue, yeux, sourcils et correctifs documentés ;
- transcriptions, lexiques, annotation manuelle, TextGrid, alignement forcé et revue humaine encadrés ;
- mapping, coarticulation, enveloppes, mélange, interpolation, lissage et latence préparés ;
- regard, clignements, saccades, tête, gestes, émotion, asymétrie et micro-expressions documentés ;
- pistes de blend shapes, `AnimationPlayer`, `AnimationTree`, ressource de timing et driver runtime préparés ;
- profils français, anglais candidat, gros plan, gameplay et foule définis ;
- progression documentaire portée à 27 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 28 — Importation et intégration dans Godot, niveau Élevée ;
- aucun rig facial, timing, animation, scène, capture, mesure runtime, benchmark ou PDF du Livre III produit.


### 2026-07-24T22:50:00+02:00 — version 3.57.0

- chapitre 26 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-AUDIO-PILOT-RELAY-STORM-001` défini pour le relais abandonné sous l’orage ;
- voix, SFX, ambiances, musique, UI, sources, dérivés, masters et exports runtime séparés ;
- enregistrement, génération, consentement, montage, nettoyage, fades et room tone documentés ;
- formats WAV, Ogg Vorbis et MP3, fréquences, profondeur PCM, canaux, compression et import Godot encadrés ;
- loudness, BS.1770-5, crête vraie, headroom, boucles, transitions, variantes et anti-répétition préparés ;
- `AudioStreamPlayer`, `AudioStreamPlayer3D`, auditeur, atténuation, zones, bus, effets, snapshots et ducking documentés ;
- contrats d’événements, pooling, polyphonie, saturation et absence d’autorité gameplay encadrés ;
- manifestes de voix, provenance, licences, retraits, rapports et portes artistique-technique préparés ;
- progression documentaire portée à 26 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 27 — Synchronisation labiale et animation faciale, niveau Élevée ;
- aucun enregistrement, asset, master, scène Godot, mesure runtime, benchmark ou PDF du Livre III produit.

### 2026-07-24T21:47:46+02:00 — version 3.56.0

- chapitre 25 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-UX-PILOT-CORE-SHELL-001` défini sur les cinq écrans du noyau UI ;
- hiérarchie de l’information, charge cognitive, densité, regroupement et divulgation progressive documentés ;
- contrastes, tailles, typographie, reflow, perception des couleurs et codages redondants encadrés ;
- focus visible, ordre logique, taille des cibles, profils de mouvement réduit et revue des flashs préparés ;
- messages d’erreur, confirmations, annulation, retour, retry, undo et notifications persistantes séparés ;
- profils composables, brouillon, aperçu, application et migrations de réglages documentés ;
- scénarios, recrutement, consentement, confidentialité, facilitation, observations, gravité, rapport et retests préparés ;
- références WCAG utilisées comme objectifs mesurables sans certification automatique du jeu ;
- progression documentaire portée à 25 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 26 — Voix, bruitages, ambiances et musique, niveau Élevée ;
- aucun profil, mesure, participant, session, rapport, test runtime, benchmark ou PDF du Livre III produit.

### 2026-07-24T20:12:01+02:00 — version 3.55.0

- chapitre 24 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-UI-PILOT-CORE-SHELL-001` défini avec menu principal, HUD, inventaire, pause et modale ;
- design tokens, identités, arborescences, `Control`, ancres, offsets, conteneurs, tailles minimales et facteurs d’échelle documentés ;
- `Theme`, variations de type, typographie, couleurs fonctionnelles, icônes et composants réutilisables encadrés ;
- navigation souris, clavier et manette, focus initial, voisins, restauration et séparation des événements GUI documentés ;
- profils de ratios, zones sûres, échelle UI, pseudo-localisation, RTL et contenus longs préparés ;
- modèles de vue, requêtes typées, pile d’écrans, pause, dépendances, captures et budgets séparés des autorités métier ;
- décision permanente 11.34 du chapitre 23 ajoutée pour fermer l’omission de continuité VFX ;
- progression documentaire portée à 24 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 25 — Expérience utilisateur et accessibilité visuelle, niveau Élevée ;
- aucun thème, composant, écran, police, capture, test runtime, benchmark ou PDF du Livre III produit.


### 2026-07-24T19:28:11+02:00 — version 3.54.0

- chapitre 23 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-VFX-PILOT-RELAY-STORM-001` défini pour la station-relais ;
- fonction visuelle, taxonomie, architecture, identités, sources, dérivés et presets documentés ;
- `GPUParticles3D`, `CPUParticles3D`, `ParticleProcessMaterial`, shaders, draw passes, sous-émetteurs, collisions, attracteurs, turbulence, traînées et `visibility_aabb` encadrés ;
- feu, fumée, impacts, magie, météo, fluides corporels stylisés, boue, hologramme, éclipses, disque d’accrétion, poussière, buée, bulles, geyser, traces de pas et débris couverts ;
- simulations précalculées, caches Blender, flipbooks, manifestes et régénération séparés des sources canoniques ;
- pooling, durée de vie, saturation, contrat gameplay-VFX, profils de qualité, accessibilité, scène de test et budgets préparés ;
- progression documentaire portée à 23 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 24 — Interface utilisateur, niveau Élevée ;
- aucun preset, shader compilé, cache, scène, benchmark, résultat runtime ou PDF du Livre III produit.


### 2026-07-24T18:01:38+02:00 — version 3.53.1

- régression éditoriale des références techniques corrigée rétroactivement dans les chapitres 19 à 22 du Livre III ;
- sources officielles restaurées sous forme de liens Markdown nommés et directement cliquables, selon le modèle du chapitre 18 ;
- bibliographies YAML et intitulés sans URL remplacés par des listes lecteur cliquables ;
- guide de style et protocole d’audit renforcés ;
- validateur léger étendu pour bloquer les références techniques sans lien nommé ou contenant une URL brute à partir du chapitre 19 ;
- versions portées à 1.0.2 pour les chapitres 19 et 20, et à 1.0.1 pour les chapitres 21 et 22 ;
- prochaine action maintenue au chapitre 23 — Effets visuels, particules et simulations ;
- aucun asset, test runtime, benchmark ou PDF du Livre III produit.

### 2026-07-24T15:16:59+02:00 — version 3.53.0

- chapitre 22 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-CINE-PILOT-SCOUT-RELAY-001` documenté pour une courte séquence d’éclaireur au relais abandonné ;
- intention dramatique, beats, storyboard, liste de plans, blocage, animatique et base temporelle encadrés ;
- focales, FOV, projection, composition, profondeur, axes, regards, raccords et mouvements de caméra documentés ;
- architecture Godot avec scènes dérivées, `Camera3D`, `AnimationPlayer`, routeur et directeur de séquence préparée ;
- synchronisation des animations, dialogues, lumières et VFX placeholders séparée de la production de leurs assets ;
- entrée, sortie, saut, annulation, interruption, chargement et restauration du gameplay encadrés ;
- versions de revue, commentaires, ratios d’image, confort visuel, sous-titres, budgets candidats et tests de build documentés ;
- progression documentaire portée à 22 chapitres sur 30 et synthèse supérieure du Livre III alignée ;
- prochaine action déplacée vers le chapitre 23 — Effets visuels, particules et simulations, niveau Élevée ;
- aucun storyboard, animatique, asset, scène Godot, timeline, rendu, test runtime, benchmark ou PDF du Livre III produit.

### 2026-07-24T13:38:11+02:00 — version 3.52.0

- chapitre 21 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-MOCAP-PILOT-SCOUT-001` documenté pour une action locomotion-accroupissement-radio sur trois morphologies ;
- familles optique, inertielle, sans marqueur, profondeur, hybride et référence vidéo comparées ;
- consentement, droits, données personnelles, accès restreint, provenance et retraits encadrés ;
- calibration, pose de capture, slate, ingestion, empreintes et chaîne non destructive documentés ;
- bruit, trous, dérive, trajectoire root, pieds, mains, collisions, équilibre et réduction de clés encadrés ;
- mapping, hiérarchie, axes, poses de référence, proportions, corrections IK et profils personnalisés documentés ;
- Blender, `BoneMap`, `SkeletonProfile`, options d’import, `RetargetModifier3D` et `AnimationLibrary` préparés ;
- matrice multi-rigs, contrôles visuels, mesures candidates, budgets, procédures Solo et Studio et porte d’acceptation ajoutés ;
- progression documentaire portée à 21 chapitres sur 30 et ligne de progression obsolète du plan maître corrigée ;
- version réelle du chapitre 20 alignée sur `1.0.1` dans l’état courant ;
- prochaine action déplacée vers le chapitre 22 — Cinématiques, caméras et mise en scène, niveau Élevée ;
- aucune session, donnée personnelle, animation, GLB, bibliothèque, scène, benchmark, résultat runtime ou PDF du Livre III produit.


### 2026-07-24T05:30:00+02:00 — version 3.50.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-20.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 20 Finalizer Runner`, run `30074762997`, sur la tête documentaire `d633b32d99c77ae9c1407e7eca4bd3fa8c0a2359` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8589406545`, digest `5c1cf6067261e6d10f56a7522357cddcead41de1829c4046c52cfaf523107750` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8589406911`, digest `efd5b7133c64c24288c7a0ee083804dded01d8f05b0f641908c9291b6f613786` ;
- empreinte SHA-256 du chapitre : `9caa2e71f4ad8bb1ecbf3d9dfe0eaf0189bf085ecba7884f7d759c136f9567f9` ;
- empreinte SHA-256 de l’audit : `c132ed7d0950212a32e6689a13ad87ee69b4c94842cddf811d60a1bd2ad82d63` ;
- métriques finales : 2 452 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 21 — Capture de mouvement et retargeting, niveau Élevée ;
- aucune animation, bibliothèque, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-24T05:10:00+02:00 — version 3.50.0

- chapitre 20 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-ANIM-PILOT-SCOUT-001` documenté pour actions keyframes, cycles, root motion, événements, graphes et corrections procédurales ;
- pose, timing, spacing, arcs, silhouette, poids, follow-through, holds et anticipation encadrés ;
- Dope Sheet, Graph Editor, interpolation, poignées, rotations et réduction de clés documentés ;
- idle, marche, course, démarrages, arrêts, demi-tours, contacts et vitesse gameplay encadrés ;
- couches additives, masques, blend spaces, synchronisation, machine à états et OneShot préparés ;
- `AnimationPlayer`, `AnimationTree`, root motion, événements filtrés et scène pilote Godot documentés ;
- regard, visée, placement des pieds et ajustement d’interaction bornés et désactivables ;
- métriques statiques : 2 452 lignes, 76 titres, 81 blocs significatifs, 61 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 21 — Capture de mouvement et retargeting, niveau Élevée ;
- aucune animation, bibliothèque, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-24T04:30:00+02:00 — version 3.49.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-19.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 19 Finalizer Runner`, run `30063921909`, sur la tête documentaire `6a09773f263d100fc5a96c7fa6409b40651e51cb` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8585536990`, digest `d3a57dd460cb7587652d70a58c4b48e26442a54d42468a33f18eda2a973dcbc3` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8585537117`, digest `be01ed1150134c448f82fef5294ffaf01c6c854a832962ea78bfb2abb9284b78` ;
- empreinte SHA-256 du chapitre : `57b09954e53bd85507cc283e373ba5b6a66981100dac277db36041851e241e7b` ;
- empreinte SHA-256 de l’audit : `6b04f3a29668933df08e4a8ccc88c81373545baaa3297b87c92bdd6afd781c67` ;
- métriques finales : 2 255 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 20 — Animation procédurale et animation par keyframes, niveau Élevée ;
- aucun rig, poids, correctif, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-24T04:10:00+02:00 — version 3.49.0

- chapitre 19 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-RIG-PILOT-SCOUT-001` documenté pour squelette de déformation, rig de contrôle, skinning, sockets et retargeting ;
- axes, unités, rest pose, noms, hiérarchie, roll, symétrie et collections d’os encadrés ;
- IK, FK, pole targets, changements d’espace, limites, twist bones et correctifs documentés ;
- bind, poids automatiques, normalisation, influences, miroir et revues par articulation encadrés ;
- export GLB filtré, `Skeleton3D`, `BoneMap`, `SkeletonProfile`, retargeting et `BoneAttachment3D` préparés ;
- métriques statiques : 2 255 lignes, 76 titres, 81 blocs significatifs, 61 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 20 — Animation procédurale et animation par keyframes, niveau Élevée ;
- aucun rig, poids, correctif, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-24T02:55:00+02:00 — version 3.48.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-18.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 18 Finalizer Runner`, run `30058228976`, sur la tête documentaire `7c19bcd270f4b3f5e99037fda8d2750ae7127996` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8583558109`, digest `256057dbe11faa7507e33947becdfb0eff5b152103794d92c88e29d0232a28bb` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8583558353`, digest `65fc51322c2dff5a9e47eeffc3407068fa469ac74154b0ddbadd73a95866c975` ;
- empreinte SHA-256 du chapitre : `e3a68e7826741d7f09136777108c370e5678bf5c5e4707c337164b1f88092697` ;
- empreinte SHA-256 de l’audit : `7a1740697d1a8aeefad7ee2c6ca32b73aaa8d601988e223fcc3c43eaf6c935d1` ;
- métriques finales : 3 904 lignes, 76 titres, 81 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 19 — Rigging et skinning, niveau Élevée ;
- aucun mesh LOD, proxy, atlas, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-24T02:35:00+02:00 — version 3.48.0

- chapitre 18 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-LOD-PILOT-SIGNAL-TOWER-001` documenté pour LOD manuels, LOD automatique Godot, HLOD, imposteur et billboard ;
- budgets par taille écran, importance gameplay, plateforme, caméra, triangles, sommets, surfaces, mémoire et draw calls encadrés ;
- Collapse, Planar, Un-Subdivide, protections locales, silhouette, normales, tangentes, UV, matériaux et textures documentés ;
- plages de visibilité, hystérésis, fades selon renderer, `lod_bias`, proxies d’ombre et collisions simplifiées encadrés ;
- atlas multi-vues, alpha, padding, normales, profondeur, orientation et ombres d’imposteur documentés ;
- MultiMesh, AABB, culling, occlusion, scène de benchmark, métriques, captures et non-régression préparés ;
- métriques statiques : 3 904 lignes, 76 titres, 81 blocs significatifs, 61 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 19 — Rigging et skinning, niveau Élevée ;
- aucun mesh LOD, proxy, atlas, GLB, scène, capture, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T23:35:00+02:00 — version 3.47.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-17.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 17 Finalizer Runner`, run `30047507706`, sur la tête documentaire `c803916a02416ad0338ace6d4fdaf66e2595d65d` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8579697669`, digest `4586c47733f516f4988aebbae51fe725467cf1bd962a74e1116acad3fc09f847` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8579697878`, digest `16e07a6f3eb6df1ab92cfeaea4b895188b97eae790867caee70e11700a5b0130` ;
- empreinte SHA-256 du chapitre : `127d06c2bc9bbd28c606088e303ea74d447b91c57f8a906c5b8e1da046f58a2d` ;
- empreinte SHA-256 de l’audit : `35eeabea1cdd67cc858a7dcceb4abeab9f436c182fc206177f4b2511864b3d86` ;
- métriques finales : 2 890 lignes, 82 titres, 84 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 18 — LOD, imposteurs et optimisation géométrique, niveau Élevée ;
- aucun maillage, UV, cage, texture bakée, GLB, scène, capture, rapport, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T23:15:00+02:00 — version 3.47.0

- chapitre 17 du Livre III créé, relu et audité au niveau `static-review` ;
- pilote `AST-BAKE-PILOT-RELAY-001` combinant coque technique statique et sangle déformable documenté ;
- haute résolution, basse résolution, cage, conventions de nommage et collections Blender encadrées ;
- retopologie statique et déformable, silhouette, edge flow, densité locale, pôles, quads, triangles et n-gons documentés ;
- normales, arêtes dures, seams, triangulation, UV, îlots, distortion, densité de texels, packing, marges et chevauchements encadrés ;
- bake sets, correspondance par noms, images cibles, Selected to Active, cages et distances de rayon documentés ;
- normales tangentes OpenGL, AO, curvature, cartes auxiliaires, dilation, sampling, skew, géométries fines et miroir encadrés ;
- glTF, tangentes Blender–Godot, import, scène comparative, validateur structurel, captures et rapport de contrôle préparés ;
- métriques statiques : 2 890 lignes, 82 titres, 84 blocs significatifs, 64 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 18 — LOD, imposteurs et optimisation géométrique, niveau Élevée ;
- aucun maillage, UV, cage, texture bakée, GLB, scène, capture, rapport, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T21:35:00+02:00 — version 3.46.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-16.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 16 Finalizer Runner`, run `30040252690`, sur la tête documentaire `1944934b3213f986cf84422bfb6bc254cc5c4c20` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8576919800`, digest `c40b945f5592cb8bd0f948506b40822159703287d0337b55fe1cb93166597b65` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8576920326`, digest `a6a5f5a2c71966717d0a11707775ee4035a69036d93c804ec1a8a76689a41c51` ;
- empreinte SHA-256 du chapitre : `2c5d9182ff27921ee14905e5a516a73a054e3657a6d8e7394347c957044e105b` ;
- empreinte SHA-256 de l’audit : `55eb5d449c8fc79ecbda55ef66b2ed76de1c6a5fa3bf78d87efa3cf218d8d3e8` ;
- métriques finales : 1 654 lignes, 63 titres, 68 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 17 — UV, retopologie et baking, niveau Élevée ;
- aucune texture, matériau, ressource Godot, scène, capture, GLB, preset, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T21:15:00+02:00 — version 3.46.0

- chapitre 16 du Livre III créé, relu et audité au niveau `static-review` ;
- laboratoire `AST-MAT-LAB-PBR-001`, géométries de contrôle, caméras, étalons et profils d’éclairage documentés ;
- base color, metallic, roughness, normal, AO, height, emissive, opacity, transmission et subsurface encadrés ;
- sRGB, données linéaires, formats, mémoire brute, mipmaps, compression et packing ORM documentés ;
- densité de texels, matériaux maîtres, tiling, trim sheets, atlas, détails et décalcomanies encadrés ;
- Principled BSDF Blender, glTF, import Godot, `StandardMaterial3D`, `ORMMaterial3D` et samplers documentés ;
- captures comparatives, inventaire, budgets, validateur structurel et campagne de mesure préparés ;
- métriques statiques : 1 654 lignes, 63 titres, 68 blocs significatifs, 48 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 17 — UV, retopologie et baking, niveau Élevée ;
- aucune texture, matériau, ressource Godot, scène, capture, GLB, preset, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T20:38:21+02:00 — version 3.45.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-15.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 15 Finalizer Runner`, run `30034556687`, sur la tête documentaire `d90cf18dec3755309f23eaff9d62838bb6e6adea` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8574685813`, digest `417f0bcf07d8de36ab648f92f6d8e9496f48643157a32774187c6981bfd0bdff` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8574686290`, digest `1bc30e64a303926e6518666c382e0b7569327f49a40e2dbf6d73af92539741e9` ;
- empreinte SHA-256 du chapitre : `7db682e1b4c4bc85519a056b45d5ffb80b340d50a5d9c7663e38690cdcf0f85a` ;
- empreinte SHA-256 de l’audit : `a54b97367c5fc1434f369b67505dc130fec37a111e9d8602abc0afa880dab728` ;
- métriques finales : 2 236 lignes, 64 titres, 66 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 16 — Textures, matériaux et pipeline PBR, niveau Élevée ;
- aucun végétal, texture, matériau, atlas, shader, carte, `MultiMesh`, imposteur, collision, scène, GLB, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T20:23:04+02:00 — version 3.45.0

- chapitre 15 du Livre III créé, relu et audité au niveau `static-review` ;
- biome pilote `AST-VEG-BIOME-DELTA-001`, fonctions visuelles, strates et transitions documentés ;
- catalogue d’espèces, provenance, échelle, pivots, collections Blender et contrats d’export encadrés ;
- arbres, arbustes, herbes, fleurs, couvre-sols, débris, feuillage et atlas préparatoires documentés ;
- variantes de taille, saison et santé, vent hiérarchique et interaction locale préparés ;
- LOD, imposteurs, cartes de distribution, exclusions, graines et prévisualisation Geometry Nodes encadrés ;
- lots `MultiMesh`, boîtes englobantes, cycle des cellules, collisions, navigation, ombres et overdraw documentés ;
- benchmark de densité, profils de qualité, mesures CPU/GPU/mémoire et porte d’acceptation préparés ;
- métriques statiques : 2 236 lignes, 64 titres, 66 blocs significatifs, 46 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 16 — Textures, matériaux et pipeline PBR, niveau Élevée ;
- aucun végétal, texture, matériau, atlas, shader, carte, `MultiMesh`, imposteur, collision, scène, GLB, benchmark, résultat runtime ou PDF du Livre III produit.

### 2026-07-23T17:21:59+02:00 — version 3.44.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-14.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 14 Finalizer Runner`, run `30020181756`, sur la tête documentaire `5a9e20a3d861e70ca72b50110c4c9a9e2b4b2687` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8568886690`, digest `8dc797d970acc956f327f385050a99b693953767cad3c0d76d71d0eecfd83bce` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8568887308`, digest `07ca8b78a0a1a330fce1170fc96944deb96d2974387b155424b7b060759a6288` ;
- empreinte SHA-256 du chapitre : `72cfb38fac389935c3099b09b00f68d8ee416f4ad413a30f8fab21855077c01e` ;
- empreinte SHA-256 de l’audit : `35c311478ecda349ae6850dbef8ae9c65fbb3db9ab62490ab7cc8abd53f7145c` ;
- métriques finales : 2806 lignes, 74 titres, 78 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 15 — Végétation et biomes, niveau Élevée ;
- aucun terrain, heightmap, tuile, route, rivière, lac, matériau, collision, navmesh, scène, GLB, LOD, HLOD, runtime ou PDF du Livre III produits.

### 2026-07-23T16:43:43+02:00 — version 3.44.0

- chapitre 14 du Livre III créé, relu et audité au niveau `static-review` ;
- région pilote `AST-WORLD-REGION-DELTA-001`, parcours, repères, échelle, coordonnées et partition spatiale documentés ;
- heightmaps haute précision, blockout, sculpt par niveaux, érosion contrôlée et bordures partagées encadrés ;
- corridors routiers, raccords architecturaux, rivière, lac, littoral et interfaces d’eau documentés ;
- matériaux et masques limités à des contrats préparatoires, sans refaire le pipeline PBR ;
- collisions `HeightMapShape3D`, géométries spéciales et raccords de navigation bidirectionnels préparés ;
- scènes de cellules, manifestes, états de streaming, chargement en arrière-plan, hystérésis, épingles et retrait documentés ;
- LOD de tuile, HLOD de secteur, horizon, environnement global et occlusion qualifiée encadrés ;
- métriques statiques : 2806 lignes, 74 titres, 78 blocs significatifs, 58 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 15 — Végétation et biomes, niveau Élevée ;
- aucun terrain, heightmap, tuile, route, rivière, lac, matériau, collision, navmesh, scène, GLB, LOD, HLOD, runtime ou PDF du Livre III produits.

### 2026-07-23T16:22:54+02:00 — version 3.43.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-13.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 13 Finalizer Runner`, run `30015525117`, sur la tête documentaire `612bc2878246229b691d7a420e4ec3e6efd41ff7` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8566943950`, digest `5dcc0c417a79d6f058a8caabacb96b388b545be8da695a205f8b51866d385cf3` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8566944381`, digest `6783ea5316695ef04a95f16d1c3feefda48ce9e95e3c07547f95c1fb96fe5970` ;
- empreinte SHA-256 du chapitre : `fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9` ;
- empreinte SHA-256 de l’audit : `48defcdb19887a51643c87d3ad2aa02d37792c5d42409d1d9508b511d255af0e` ;
- métriques finales : 2 381 lignes, 63 titres, 69 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 14 — Terrains, paysages et mondes ouverts, niveau Élevée ;
- aucun module, bâtiment, collision, navigation, occluder, matériau, atlas, LOD, HLOD, GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T14:35:47+02:00 — version 3.43.0

- chapitre 13 du Livre III récupéré avec son empreinte originale, relu et audité au niveau `static-review` ;
- audit QA reconstruit depuis le chapitre vérifié, le plan maître et le protocole après corruption du conteneur de transport temporaire ;
- kit pilote `AST-ARCH-KIT-WAYSTATION-001`, grille, modules, connecteurs, tolérances et porte de blockout à trois bâtiments documentés ;
- murs, ouvertures, coins, transitions, sols, escaliers, toitures, intérieurs et variantes encadrés ;
- rendu, collisions, navigation et occlusion séparés ; destruction limitée à une préparation visuelle ;
- scènes modulaires, `GridMap`, `MeshLibrary`, LOD de module et HLOD de bâtiment documentés ;
- métriques statiques : 2 381 lignes, 63 titres, 69 blocs significatifs, 49 explications structurées et dix diagnostics ;
- synthèse supérieure du Livre III corrigée de 9/30 à 13/30 pour rejoindre l’état courant et les preuves ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 14 — Terrains, paysages et mondes ouverts, niveau Élevée ;
- aucun module, bâtiment, collision, navigation, occluder, matériau, atlas, LOD, HLOD, GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T14:07:25+02:00 — version 3.42.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-12.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 12 Finalizer Runner`, run `30005722322`, sur la tête documentaire `55317ee6bba9a0c98e442234632f7bb80565f45d` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8562880714`, digest `cdb144885bf89c65fa758326bac5c339e044a8678a82f3c567e5dfdf9ef2b56a` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8562881257`, digest `1b585b8b385a5acb878a45bd37bf20a67846c8852b89e3ed4bef584e9fde2932` ;
- empreinte SHA-256 du chapitre : `73905a954ffe28f11fb1e8f9350df80969829a9520cfa4bd98c2f9e620f960ac` ;
- empreinte SHA-256 de l’audit : `c8196c7ed13377c180011844cc1e269f7721328b3746d21ff708bdd39bb31856` ;
- métriques finales : 2 312 lignes, 57 titres, 61 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 13 — Architecture, bâtiments et kits modulaires, niveau Élevée ;
- aucun objet, outil, arme, pivot, socket, collision, matériau, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T13:30:28+02:00 — version 3.42.0

- chapitre 12 du Livre III créé, relu et audité au niveau `static-review` ;
- bibliothèque pilote `AST-PROP-KIT-EXPLORER-001` encadrée par cinq objets aux contraintes distinctes ;
- fonctions observables, références dimensionnelles, ergonomie, échelle et gabarits documentés ;
- axes, origines, pivots, prises, sockets de rangement, environnement et émission encadrés ;
- pièces mobiles, silhouette, blockout, topologie, ombrage et matériaux provisoires préparés ;
- interaction, physique, impact et émission séparés en profils de collision distincts ;
- états visuels, variantes, dégradation, LOD et représentations fonctionnelles documentés ;
- export GLB, scènes Godot dérivées, validateur structurel et campagnes de mesure préparés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 13 — Architecture, bâtiments et kits modulaires, niveau Élevée ;
- aucun objet, outil, arme, pivot, socket, collision, matériau, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T12:33:11+02:00 — version 3.41.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-11.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 11 Finalizer Runner`, run `29999720086`, sur la tête documentaire `61703c5c010d267e525fe138ed02ca41096cab86` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8560445995`, digest `960e88fe4a2f2b501effb7145a69217e1099f1852aa277e158af852833539298` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8560446417`, digest `5620ac27632218aa33759a1592d076d4142490dc82f2309018be6b7b3527d84c` ;
- empreinte SHA-256 du chapitre : `bcc38ce80457fc3b765d9d818f8a8d82c102bd9387d9eb11af57f94c5f8e73ee` ;
- empreinte SHA-256 de l’audit : `afc04b0d138f789788f3a16144281b8c060c1f0bb8a13bf8ce7b3d06fc722288` ;
- métriques finales : 1 975 lignes, 52 titres, 56 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 12 — Objets, équipements et armes, niveau Élevée ;
- aucun vêtement, armure, accessoire, patron, skinning, simulation, collision, masque, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T11:50:40+02:00 — version 3.41.0

- chapitre 11 du Livre III créé, relu et audité au niveau `static-review` ;
- kit pilote `AST-WEAR-KIT-WARDEN-001` encadré par catégories de comportement et cas d’usage ;
- layering, conflits, prérequis, profils morphologiques et matrice de compatibilité documentés ;
- patrons, marges de mouvement, blockout, topologie, coutures et épaisseurs encadrés ;
- transfert de poids, skinning, rigidité locale, armures et attaches préparés ;
- proxies de collision, simulation Blender, conversion et frontière runtime Godot explicités ;
- clipping, masques corporels réversibles, matériaux, variantes et LOD documentés ;
- export GLB, scène Godot dérivée, validateur structurel et campagne de performance préparés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 12 — Objets, équipements et armes, niveau Élevée ;
- aucun vêtement, armure, accessoire, patron, skinning, simulation, collision, masque, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T11:14:44+02:00 — version 3.40.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-10.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 10 Finalizer Runner`, run `29994474356`, sur la tête documentaire `5ca5d5b21395df3f45365b8885c40b78d92b3d4e` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8558361544`, digest `e853f5235aa9a5bf045ed3372ff52f07268b7779668bf0200236eb3f22a13258` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8558362006`, digest `b9d4c95525d780fcbc30fd8018223e281b9f9421dbad254232cbb976b4c4da72` ;
- empreinte SHA-256 du chapitre : `a39df80e5f6a37d9290f87464f02b5804d0193b262db3c6209560cc10e3e375c` ;
- empreinte SHA-256 de l’audit : `cf9a9fa649b59b07c7a70b1193fa1340291cbf9a18ce6b02e268bdc88e082a7e` ;
- métriques finales : 1 978 lignes, 49 titres, 52 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 11 — Vêtements, armures et accessoires, niveau Élevée ;
- aucune tête, texture, matériau, œil, dentition, solution capillaire, blendshape, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T10:56:17+02:00 — version 3.40.0

- chapitre 10 du Livre III créé, relu et audité au niveau `static-review` ;
- tête pilote `AST-CHR-FACE-PILOT-001` encadrée par un brief de gros plan et des caméras de référence ;
- provenance, consentement, diversité des références et risques de perspective documentés ;
- repères anatomiques, topologie, sculpture primaire-secondaire-tertiaire et asymétrie contrôlée encadrés ;
- profils de peau, diffusion sous-surface, œil, bouche, dents et intersections préparés ;
- cheveux, hair cards, groom, sourcils, cils, barbe, duvet, transparence et overdraw documentés ;
- formes faciales limitées aux tests de déformation, sans visèmes ni timings du chapitre 27 ;
- LOD, export GLB, scène Godot dérivée, validateur structurel et campagne de performance documentés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 11 — Vêtements, armures et accessoires, niveau Élevée ;
- aucune tête, texture, matériau, œil, dentition, solution capillaire, blendshape, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T09:48:12+02:00 — version 3.39.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-09.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validations légères sans PDF réussies dans `Chapter 9 Finalizer Runner`, run `29989288114`, sur la tête documentaire `8c97f97f8217ef2aa547aa2cc159c54dda024e12` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8556352553`, digest `44f0efe8d9f79f7e1516f3146476089e3e2d3c135f27d949432300ec515522b5` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8556352744`, digest `fa0c0a7c0de16fdb8715fbd4589bff0d28af77cd441c42ae4ea8f5d2abe62a80` ;
- empreinte SHA-256 du chapitre : `6f17a958c6b19825d86d3cdfc4c337e9ebcbc05cdf75c1115d9b71ee2333eb2f` ;
- empreinte SHA-256 de l’audit : `6d1a40d71c768a840e91c6d157c46ed906495ae724d7c139923acb5d0b4a32a2` ;
- métriques finales : 2 332 lignes, 66 titres, 45 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 10 — Visages, peau, yeux, cheveux et pilosité, niveau Élevée ;
- aucun concept final, modèle, rig, collision, socket, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T09:06:37+02:00 — version 3.39.0

- chapitre 9 du Livre III créé, relu et audité au niveau `static-review` ;
- brief fonctionnel et matrice fonction-forme-coût-limite du Veilleur des brumes documentés ;
- analogues réels, niveaux de spéculation et inconnues bloquantes séparés ;
- masses, appuis, silhouettes, vues de contrôle et blockout métrique encadrés ;
- topologie, profil de rig, sockets, proxies de collision et zones de lisibilité préparés ;
- poses d’action, enveloppes de mouvement, variantes et LOD définis sans valeurs gameplay inventées ;
- export GLB, scène Godot dérivée, validateur structurel et campagnes de mesure documentés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 10 — Visages, peau, yeux, cheveux et pilosité, niveau Élevée ;
- aucun concept final, modèle, rig, collision, socket, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T05:31:31+02:00 — version 3.38.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-08.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire et des contextes réussie au run `29977206341` sur la tête `7d07b1ffd26c80aa996e6306608ca7334415bc82` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8551861160`, digest `24b629ad09a2c02bd72d688a976715c851a59716693f962def4ac6a7c3cc0c8f` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8551861420`, digest `3637966f882e3063e619fa355738a3bf9eafc914bc6aa6bcef59dd522bdb8815` ;
- empreinte SHA-256 du chapitre : `5d58026bee2abf1c142e20b6f8b2ede9cabf681453a097f5f3153da3f4de46d2` ;
- empreinte SHA-256 de l’audit : `470c892898124408e60f930c9a78d4818b998125e05a7a642d23a67286ba7123` ;
- métriques finales : 1 929 lignes, 67 titres, 32 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 9 — Création des créatures, niveau Élevée ;
- aucun animal, rig, animation, surface, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T05:13:25+02:00 — version 3.38.0

- chapitre 8 du Livre III créé, relu et audité au niveau `static-review` ;
- pilotes quadrupède, oiseau, poisson, reptile bas et morphologie serpentine documentés ;
- références, masses, repères, appuis et calendriers de contacts encadrés ;
- bases maillées, topologies, profils de rig, skinning et influences préparés ;
- cycles de marche, course, vol, nage, repos et transitions décrits sans animation inventée ;
- pelage, plumes, écailles, variantes et représentations de livraison séparés des sources Blender ;
- LOD, densité, limites de MultiMesh, export GLB, import Godot et laboratoire de validation documentés ;
- dix erreurs fréquentes fournissent exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 9 — Création des créatures, niveau Élevée ;
- aucun modèle animal, rig, animation, surface, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T02:47:39+02:00 — version 3.37.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-07.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire et des contextes réussie au run `29970060048` sur la tête `71595cdea8f3eec006112d301bf969ea3bf5e2ac` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8549296753`, digest `09ba794a1b5de6abb9e6e7d9f2beaeb216186fa3d6b5336be4f0153cdb47b063` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8549296962`, digest `2a8d9520185a8d5a946077fb3e3df34126e3cbd4500d048dbeaab99c77b19068` ;
- empreinte SHA-256 du chapitre : `7cc7ea64b3e4f86ef16cb043ab5436e52dd95f006bbb1d11162a798f72eba2c8` ;
- empreinte SHA-256 de l’audit : `7a0961703c8038698937aab2e68325ff13fed5731854e68b35675481fdaca64c` ;
- métriques finales : 2 015 lignes, 72 titres, 39 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 8 — Création des animaux, niveau Élevée ;
- aucun humanoïde, rig, animation, équipement, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T02:42:14+02:00 — version 3.37.0

- chapitre 7 du Livre III créé, relu et audité au niveau `static-review` ;
- fiche d’espèce, registre des écarts anatomiques et classes d’impact documentés ;
- proportions, posture, centre de masse, membres, extrémités et traits secondaires encadrés ;
- silhouettes, topologie, variantes, modules et interfaces versionnées définis ;
- profils de rig, BoneMap, poses de repos, retargeting local, global et partiel documentés ;
- vêtements, armures, masques corporels, sockets et interactions qualifiés par matrice ;
- variations culturelles séparées de l’anatomie et protégées contre les inférences réductrices ;
- LOD, budgets, export GLB, import Godot, scènes de test et validateur structurel documentés ;
- dix erreurs fréquentes fournissent exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 8 — Création des animaux, niveau Élevée ;
- aucun humanoïde, rig, animation, équipement, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T01:25:59+02:00 — version 3.36.2

- correction de cohérence de la section `État courant` après la fusion du chapitre 6 ;
- progression du Livre III alignée de 5 à 6 chapitres sur 30 ;
- chapitre 6 ajouté à la liste des versions courantes en `1.0.0`, niveau `static-review` ;
- prochaine action, preuve QA, empreintes et périmètre documentaire inchangés ;
- aucun asset, runtime ou PDF produit par cette correction de gouvernance.

### 2026-07-23T01:16:33+02:00 — version 3.36.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-06.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire réussie au run `29965382843` sur la tête `12f949fcf53f53eaafb774b5d86b0d706b228191` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8547618141`, digest `51ba9423ef5f80744ac63ee8d9a0ce880c058d24fe6f81bf52f02bcf14b7dd03` ;
- validation des contextes réussie au run `29965382828` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8547616966`, digest `5b4e2105ae83c656c5bcc0e08b797c9260da1a62ffc4f212bed08121403d178a` ;
- empreinte SHA-256 du chapitre : `199af753e3c11117af44b8e8dac1911955654d734d5a64375b86af4238dcebeb` ;
- empreinte SHA-256 de l’audit : `13106867a157ad14d5ebcf2fae09263ccce2d039813a4bc856a23ace6bcbbd16` ;
- métriques finales : 1 755 lignes, 68 titres, 26 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 7 — Création des humanoïdes, niveau Élevée ;
- aucun maillage humain, rig, animation, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T01:08:11+02:00 — version 3.36.0

- chapitre 6 du Livre III créé, relu et audité au niveau `static-review` ;
- références anatomiques, proportions métriques, pose de construction et base neutre documentées ;
- topologie des épaules, coudes, hanches, genoux, mains et pieds encadrée ;
- modules, variantes morphologiques et séparation avec les données de gameplay définis ;
- préparation UV, matériaux, rig futur, export GLB et import Godot documentée ;
- budgets provisoires, profils LOD, scène de poses et protocole de mesure définis sans résultat runtime inventé ;
- dix erreurs fréquentes fournissent exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 7 — Création des humanoïdes, niveau Élevée ;
- aucun maillage humain, rig, animation, export GLB, scène Godot, runtime ou PDF du Livre III produits.

### 2026-07-23T00:26:51+02:00 — version 3.35.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-05.yaml` fermée avec zéro erreur bloquante et un avertissement documentaire ;
- validation documentaire réussie au run `29960812166` sur la tête `ea8f6a6b9c6cd66b9c3a7922d801274e2405f5e7` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8545871720`, digest `b4ae05177e0fc97a7d79cac93c7610046a84db483b0bd8a134032dad9c13083f` ;
- validation des contextes réussie au run `29961125128` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8545999556`, digest `f701349af7c1e7694d736925e30153a6419b4f32fcf1656d2f3f601b13825d84` ;
- empreinte SHA-256 du chapitre : `652cdf06964e9354e310fdbb152f9e34dff1f4062b3af313b976901d3ec9d4ec` ;
- empreinte SHA-256 de l’audit : `b2a7782ead143c01ef1fe4e040365bb1cd4cfeab982e570ea09ac75bedd3ef1f` ;
- métriques finales : 1 555 lignes, 63 titres, 26 blocs significatifs et aucun doublon ;
- prochaine action maintenue au chapitre 6 — Création des humains, niveau Élevée ;
- aucun registre réel, contrat, consentement, runtime ou PDF du Livre III produits.

### 2026-07-22T23:35:44+02:00 — version 3.35.0

- chapitre 5 du Livre III créé, relu et audité au niveau `static-review` ;
- auteurs, titulaires, licences, consentements, données personnelles, image, droits voisins et marques distingués ;
- fiches, registre, preuves, transformations, restrictions, statuts et dépendances documentés ;
- chaînes IA, voix, scans, mocap, polices, audio, marques et contenus sensibles encadrés ;
- contrôles structurels, porte humaine de publication, retrait et remplacement définis ;
- sources institutionnelles françaises, européennes et standards de licences vérifiés au 22 juillet 2026 ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 6 — Création des humains, niveau Élevée ;
- aucun registre réel, contrat, consentement, runtime ou PDF du Livre III produits.

### 2026-07-22T23:08:24+02:00 — version 3.34.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-04.yaml` fermée avec zéro erreur bloquante et une réserve documentaire ;
- validation chapitre réussie au run `29957934668` sur la tête documentaire `b760a5640c5ae8bd69c1c35aaa38a4d36bf1dec0` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8544781576`, digest `a9446929811cbf1d62d55f0ff8340e843ed7f1981d74d469c75c571c3dac1457` ;
- validation des contextes réussie au run `29957934555` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8544781110`, digest `57449276e4cb121519d26e1cf45e4b2dc9f556af64cdb6fdfb592aba893f28dd` ;
- empreinte SHA-256 du chapitre : `6d811877b5d30a3675ba00dae1950d3ad68b4529eeaddb93ab6c5c1027c90c9c` ;
- empreinte SHA-256 de l’audit : `907d1cfc1ae110990dfe12e6c64727524198727d3ece354941ce292ba15bce7b` ;
- les huit fichiers permanents du lot restent seuls dans la PR ;
- prochaine action maintenue au chapitre 5 — Provenance, licences et validation des assets, niveau Élevée ;
- aucune exécution Blender ou Godot et aucun PDF du Livre III produits.

### 2026-07-22T22:37:42+02:00 — version 3.34.0

- chapitre 4 du Livre III créé, relu et audité au niveau `static-review` ;
- Blender `5.2.0` Stable qualifié comme référence documentaire, sans add-on tiers obligatoire ;
- template, unités, axes, pivots, transformations, collections, bibliothèques liées et overrides documentés ;
- arborescence source, travail, bibliothèque, cache, export, livraison et archive définie ;
- conventions de noms, versions, sauvegardes, chemins relatifs et dépendances encadrées ;
- formats GLB, glTF séparé et import direct `.blend` comparés avec leurs limites ;
- cube d’un mètre, validateur Blender, exporteur GLB, empreintes et contrôle Godot documentés ;
- procédures Solo, Studio, réouverture multi-poste, sécurité et checklists ajoutées ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 5 — Provenance, licences et validation des assets, niveau Élevée ;
- aucune exécution Blender ou Godot et aucun PDF du Livre III construits.

### 2026-07-22T21:21:47+02:00 — version 3.33.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-03.yaml` fermée avec zéro erreur bloquante et une réserve documentaire ;
- workflow permanent `Validate Chapters Without PDF` réussi au run `29949966935` sur la base `7bbab5accaf56fd6560579a08a8c9dee8bdc8f6c` et la tête documentaire `ab7fefc9422ee16a1e32b7db1e2bc933684f515d` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8541707655`, digest `395aba9d4fdde611ccddcc12a623c0cf25a36738acb3657b2619bce269a24fd7` ;
- audit des contextes réussi au run `29950382307` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8541869318`, digest `cbd05e077f333c541341bd50d335ce76ac71f352018d339ba2086d94c19dbabb` ;
- empreinte SHA-256 du chapitre fermée à `71f196636f663e00b3c925ed792c3323187bf7f22db30c95c313805f5f2fd912` ;
- matérialiseur, runner de contextes, fichiers de résultat et déclencheurs temporaires supprimés avant fusion ;
- prochaine action maintenue sur le chapitre 4 — Pipeline Blender et organisation des fichiers, niveau Élevée ;
- aucune exécution ComfyUI ou Godot et aucun PDF du Livre III construits.

### 2026-07-22T20:42:28+02:00 — version 3.33.0

- chapitre 3 du Livre III créé, relu et audité au niveau `static-review` ;
- distinctions entre inspiration, référence, concept, source de production et asset final documentées ;
- registre de provenance, droits d’usage, quarantaine et empreintes définis ;
- moodboards annotés, planches comparatives et questions visuelles encadrés ;
- ComfyUI `0.28.0`, workflows JSON, modèles, custom nodes, seeds, paramètres et manifestes documentés ;
- sélection humaine, contrôles anatomiques, matériels, culturels et fonctionnels définis ;
- sécurité des extensions, métadonnées de partage, budgets d’itération et règle d’arrêt documentés ;
- configuration AMD Windows de référence maintenue en réserve runtime ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 4 — Pipeline Blender et organisation des fichiers, niveau Élevée ;
- aucune exécution ComfyUI ou Godot et aucun PDF du Livre III construits.

### 2026-07-22T19:53:29+02:00 — version 3.32.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-02.yaml` fermée avec zéro erreur bloquante et une réserve documentaire ;
- validation statique approuvée réussie au run `29943194826` sur la base `8f8271a407c7978cfc668aad90e073e3ef3b3713` et la tête documentaire `b05c502ee5c39451784a288ceee09669f60065cd` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8539045265`, digest `07f9309cec632d7be4490ecb7fa16d8b31f5728cd8b143215b1f87ea1b3a14dd` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8539045793`, digest `f0e67e60f1cfb8ec320d9f6d0111d0ca2b9bb68ffebda59df863c1a23cfc35a8` ;
- chapitre et audit restaurés depuis le paquet source, avec SHA-256 et CRC du chapitre concordant avec l’archive déclarée ;
- finaliseurs, archiveurs, correcteurs, runners approuvés et déclencheurs temporaires supprimés de `main` par la PR `136`, commit `8ca89d683e8f980491de418b2cc47dbdc3e80857` ;
- prochaine action maintenue sur le chapitre 3 — Références, concept art et ComfyUI, niveau Élevée ;
- aucune exécution runtime et aucun PDF du Livre III construits.

### 2026-07-22T18:10:53+02:00 — version 3.32.0

- chapitre 2 du Livre III créé, relu et audité au niveau `static-review` ;
- bible visuelle, piliers, formes, silhouettes, proportions, palettes, matériaux, lumière, profondeur, UI et VFX documentés ;
- variations culturelles, régionales, sociales et temporelles encadrées par des règles communes ;
- exemples conformes, limites et non conformes, grille de revue, dérogations et gestion des changements définis ;
- scène comparative Godot et captures documentées sans revendiquer leur exécution ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- récupération documentée du chapitre et de l’audit depuis le paquet source ;
- prochaine action déplacée vers le chapitre 3 — Références, concept art et ComfyUI, niveau Élevée ;
- aucun PDF du Livre III construit.


### 2026-07-22T13:55:05+02:00 — version 3.31.0

- ouverture du jalon M4 et du Livre III ;
- chapitre 1 créé, relu et audité au niveau `static-review` ;
- cahier des charges, matrice d’assets, budgets initiaux, calendrier, registre des risques et checklist d’acceptation documentés ;
- budgets marqués comme hypothèses révisables et aucun résultat runtime inventé ;
- outils et workflows légers étendus au Livre III ;
- index, roadmap, ordre lecteur et plan maître mis à jour ;
- prochaine action déplacée vers le chapitre 2 — Direction artistique et bible visuelle, niveau Élevée ;
- aucun PDF du Livre III construit.

### 2026-07-22T12:45:00+02:00 — version 3.30.5

- le dernier lien sémantique vers la fabrication éditoriale est retiré du manuel lecteur ;
- l’exemple Python du chapitre 29 utilise désormais `pyproject.toml` comme marqueur technique de racine ;
- le PDF lecteur doit être reconstruit et inspecté sur ce dernier état avant fusion ;
- le plan maître enrichi du Livre III reste en version `1.1.0`.

### 2026-07-22T12:34:00+02:00 — version 3.30.4

- les derniers résidus de fabrication du manuel lecteur sont retirés des chapitres 15 et 25 ;
- les critères techniques du chapitre 15 sont conservés sous une formulation destinée au lecteur ;
- les sections obsolètes `Tests à préparer`, les statuts `static-review` visibles et les références au PDF intermédiaire sont exclus du manuel ;
- le filtre PDF reconnaît les variantes résiduelles de statut éditorial ;
- le plan maître enrichi du Livre III reste en version `1.1.0` et la prochaine action demeure son chapitre 1.

### 2026-07-22T12:07:56+02:00 — version 3.30.3

- `plans/LIVRE-III-PLAN-MAITRE.md` enrichi et porté en version `1.1.0` ;
- les trente chapitres possèdent désormais intention, résultats d’apprentissage, contenu obligatoire, livrables, dépendances, variantes Solo/Studio, critères de validation et frontière ;
- le plan contient une procédure de reprise explicite pour une nouvelle conversation ;
- la règle de publication est confirmée : le manuel lecteur exclut protocoles, audits, preuves, rapports QA, continuité et documents de fabrication ;
- la prochaine action reste `Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md` après validation du PDF lecteur du Livre II.

### 2026-07-22T11:18:12+02:00 — version 3.30.2

- ordre de compilation lecteur nettoyé : protocoles, audits, preuves et rapports QA exclus du PDF ;
- mentions visibles d’audit et d’explication éditoriale retirées des en-têtes des trente chapitres du Livre II ;
- index du Livre II recentré sur le contenu du manuel, sans sections de gouvernance éditoriale ;
- pagination `plain` retenue pour éviter les en-têtes courants rognés ;
- fichiers QA conservés dans le dépôt comme preuves de conception et de validation ;
- reconstruction Pandoc/XeLaTeX et inspection visuelle du manuel lecteur requises avant le Livre III.

### 2026-07-22T10:11:47+02:00 — version 3.30.1

- validation transversale des trente chapitres du Livre II réussie ;
- audits référencés, preuves disponibles, identifiants, liens, contextes et doublons contrôlés ;
- compilation Pandoc/XeLaTeX et préflight PDF réussis ;
- cinquante et une pages de séparation parasites supprimées avec `openany` ;
- couverture, table des matières, trente ouvertures de chapitre, pages de code et pages finales inspectées ;
- rapport de validation transversal ajouté au PDF et preuve de publication conservée hors compilation ;
- M3 et Livre II marqués terminés ; prochaine action déplacée vers le Livre III, chapitre 1 ;
- licence globale, balisage d’accessibilité et réserves runtime maintenus sans revendication excessive.

### 2026-07-22T07:41:06+02:00 — version 3.30.0

- règle permanente ajoutée : toute dépendance future du Starter Kit doit être qualifiée avant adoption ;
- chapitre 30 créé, relu et audité au niveau `static-review` ;
- profils Solo et Studio consolidés autour d’un même cœur métier ;
- autorités, dépendances, composition, responsabilités, environnements, revues, CI, exports, incidents et plan de matérialisation documentés ;
- progression portée à 30 chapitres sur 30 et industrialisation à 5 chapitres sur 5 ;
- prochaine action déplacée vers la validation transversale et le PDF complet du Livre II ;
- aucun Starter Kit, test runtime, paquet exporté ou PDF revendiqué comme produit.

### 2026-07-22T07:05:00+02:00 — version 3.29.2

- chapitre 29 porté à `1.0.1` après revue de compatibilité Python ;
- CPython 3.14.6 reclassé en cible principale provisoire et CPython 3.13.14 ajouté comme repli ;
- dépendances directes mises à jour vers `hatchling 1.31.0` et `jsonschema 4.26.0` ;
- matrice Windows/Linux avec roues binaires et critères de qualification documentés ;
- WSL réel et ensemble futur des dépendances maintenus en réserve ;
- preuve QA remise en attente ; aucun PDF ni test du Starter Kit revendiqué.

### 2026-07-22T05:14:39+02:00 — version 3.29.1

- compteur supérieur du Livre II aligné sur 29 chapitres sur 30 ;
- chapitres 28 et 29 marqués terminés au niveau `static-review` dans la liste de collection ;
- plage des niveaux de production alignée sur les chapitres 3 à 29 ;
- terminologie temporelle harmonisée sur `durée réelle (durée de l’horloge système)` et `horloge système` ;
- aucune modification du chapitre 29, aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-22T04:30:00+02:00 — version 3.29.0

- chapitre 29 créé, relu et audité au niveau `static-review` ;
- CPython 3.14.6, environnements virtuels, `pyproject.toml`, verrouillage et CLI typées documentés ;
- configurations versionnées, JSON Schema, génération déterministe, graines locales et identités stables encadrés ;
- processus externes, parallélisme borné, reprise par checkpoint, staging, promotion, manifestes et archives vérifiées définis ;
- chapitres 26 à 28 orchestrés sans transfert d’autorité métier ;
- progression portée à 29 chapitres sur 30 et prochaine action déplacée vers le chapitre 30 ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-22T03:13:32+02:00 — version 3.28.0

- chapitre 28 créé, relu et audité au niveau `static-review` ;
- journaux structurés, sévérités, identifiants stables, temps UTC et monotone, corrélation et causalité documentés ;
- listes autorisées, rédaction des secrets, métriques de faible cardinalité, traces et files bornées encadrées ;
- marqueur de session, manifeste de reproduction, empreintes SHA-256, paquet ZIP, consentement et support hors ligne définis ;
- résultats du chapitre 27 consommés sans redéfinir les suites, scénarios ou golden files ;
- progression portée à 28 chapitres sur 30 et prochaine action déplacée vers le chapitre 29 ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-22T01:40:00+02:00 — version 3.27.1

- chapitres 22, 23 et 27 corrigés : les calques liés à `wall-clock time` et `wall-clock duration` sont remplacés par `durée réelle (durée de l’horloge système)` ou `horloge système` selon le contexte ;
- versions portées à `1.0.4`, `1.0.3` et `1.0.1` ; audits portés à `1.0.4`, `1.0.3` et `1.0.2` ;
- règle terminologique permanente ajoutée au validateur des chapitres ;
- preuves QA des trois chapitres remises en attente de validation ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T21:00:05+02:00 — version 3.27.0

- chapitre 27 créé, relu et audité au niveau `static-review` ;
- niveaux unitaires, composants, intégration, simulations et plateformes distingués ;
- GUT 9.x, dépendance épinglée, doubles, fixtures, builders, `SceneTree`, signaux et exécution headless documentés ;
- horloges, RNG, stockages temporaires, scénarios versionnés, graines, invariants, empreintes et golden files encadrés ;
- critères de passage, rapports JUnit et artefacts de diagnostic définis sans retry masquant les échecs ;
- progression portée à 27 chapitres sur 30 et prochaine action déplacée vers le chapitre 28 ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T19:59:30+02:00 — correction sémantique des sections d’erreurs

- chapitres 17 à 26 : sections d’erreurs restaurées depuis leur version antérieure à la restructuration générale ;
- explications fautives et corrigées replacées directement après leur marqueur, sans sous-titre structuré ni rubrique parasite ;
- formulations historiques conservées, sans perte de sens ;
- protocole et contrôle automatique renforcés pour distinguer explication générale et séquence sémantique d’erreur/correction ;
- audits et preuves QA remis en attente de validation ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T17:35:51+02:00 — reclassement fidèle des explications historiques

- chapitres 17 à 24 reconstruits depuis leurs explications présentes sur `main` ;
- libellés historiques utilisés comme autorité de classement ;
- **1760** unités conservées mot pour mot et **0** perdue ;
- aucune modification des exemples de code ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T15:28:42+02:00 — affinage qualitatif des explications restructurées

- libellés génériques supprimés des chapitres 17 à 26 ;
- explications antérieures décomposées en **2082** segments conservés mot pour mot ;
- rubriques dupliquées regroupées et catégories réattribuées selon le contenu réel ;
- **506** segments complémentaires spécifiques conservés pour les chapitres 25 et 26 ;
- contrôle permanent renforcé contre les formulations génériques et les rubriques dupliquées ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T14:38:26+02:00 — restructuration pédagogique des chapitres 17 à 26

- explications des blocs restructurées sous des rubriques explicites ;
- **1854** unités pédagogiques antérieures conservées et **0** perdue ;
- **460** points complémentaires ajoutés aux chapitres 25 et 26 ;
- sections Solo/Studio des chapitres 25 et 26 converties en Markdown ordinaire ;
- protocole et contrôle automatique renforcés ;
- audits et preuves QA préparés pour une nouvelle validation ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T12:47:15+02:00 — version 3.26.0

- chapitre 26 créé, relu, corrigé et audité au niveau `static-review` ;
- plugins d’éditeur, docks, inspecteurs, annulation, validation, importeurs et exécution headless documentés ;
- séparation source/artefact/cache, sérialisation canonique, empreintes, manifestes, provenance et reçus explicités ;
- staging, transactions de fichiers, import incrémental et IA limitée aux brouillons documentés ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 27 — Tests unitaires, tests d’intégration et simulations, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T12:24:22+02:00 — version 3.25.2

- lignes « Niveau de raisonnement conseillé » retirées des en-têtes lecteurs des chapitres du Livre II ;
- validateur renforcé pour refuser la clé YAML comme la mention visible dans un chapitre publié ;
- protocole QA clarifié : la recommandation reste exclusivement dans le processus de production ;
- prochaine action maintenue sur le chapitre 26 ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T12:15:30+02:00 — version 3.25.1

- correction de gouvernance : le niveau GPT-5.6 Sol est une donnée du processus de production, pas une métadonnée du chapitre ;
- clé `recommended-reasoning` retirée des chapitres publiés du Livre II ;
- protocole QA et validateur léger corrigés pour ne plus exiger cette clé ;
- doublon de l’audit du chapitre 24 retiré de l’index ;
- prochaine action maintenue sur le chapitre 26 ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-21T11:20:30+02:00 — version 3.25.0

- chapitre 25 créé, relu, corrigé et audité au niveau `static-review` ;
- faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex et connaissances documentés ;
- conséquences multi-autorités et idempotence explicitées ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 26 — Outils d’édition internes et pipelines de contenu, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T09:05:12+02:00 — version 3.24.0

- chapitre 24 créé, relu, corrigé et audité au niveau `static-review` ;
- domaines, parcelles, liens de tenure, bâtiments, chantiers, matériaux, production et entretien documentés ;
- droits, sites, inventaire et économie maintenus derrière des ports propriétaires ;
- commits multi-autorités, révisions et idempotence explicités ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 25 — Narration, quêtes, codex et connaissances, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T04:38:43+02:00 — version 3.23.0

- chapitre 23 créé, relu, corrigé et audité au niveau `static-review` ;
- institutions, factions, adhésions, rangs, mandats, lois, autorisations, dossiers, preuves, verdicts et sanctions documentés ;
- invariants de restauration des rangs, fonctions, institutions et sièges vacants renforcés ;
- sanctions multi-autorités et idempotence explicitées ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 24 — Construction et gestion de domaines, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.


### 2026-07-21T00:57:24+02:00 — version 3.22.2

- preuve finale `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-22.yaml` clôturée ;
- `Validate Chapters Without PDF` réussi au run `29785409352` ;
- `Validate Usage Contexts` réussi au run `29785409338` ;
- artefact `chapter-validation-without-pdf` enregistré avec l’identifiant `8478251858` et son digest SHA-256 ;
- aucune exécution runtime et aucun PDF construit.

### 2026-07-21T00:48:43+02:00 — version 3.22.1

- contrat `EcologyAccessPort` restauré dans le chapitre 22 ;
- résultats écologiques réussis rendus stricts sur `command_id` et `region_id` ;
- métriques du chapitre et de l’audit recalculées après la correction finale ;
- chapitre et audit portés en version `1.0.1` ;
- aucune exécution runtime et aucun PDF construit.

### 2026-07-21T00:29:34+02:00 — version 3.22.0

- chapitre 22 créé, relu, corrigé et audité au niveau `static-review` ;
- horloge logique, régions, espèces, ressources, populations, capacités et résidus documentés ;
- simulation active, arrière-plan, dormante et rattrapage agrégé borné explicités ;
- séparation entre existence logique et matérialisation maintenue ;
- commandes causales idempotentes et récolte coordonnée avec l’inventaire ajoutées ;
- indices écologiques fournis à l’économie sans déplacement de l’autorité des prix ;
- index, roadmap, `contents.txt`, audit et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 23 — Politique, factions et justice, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-20T21:13:06+02:00 — version 3.21.0

- chapitre 21 créé, relu, corrigé et audité au niveau `static-review` ;
- devises, unités mineures, portefeuilles, écritures, valeurs, offres, devis, achats, taxes, récompenses et idempotence documentés ;
- commit économie-inventaire et révisions multi-agrégats explicités ;
- paragraphes de gouvernance restés à 19 chapitres et 6 systèmes corrigés ;
- index, roadmap, `contents.txt`, audit et preuve QA mis à jour ;
- prochaine action déplacée vers le chapitre 22 — Monde vivant et simulation écologique, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-20T17:50:09+02:00 — version 3.20.0

- chapitre 20 créé, relu, corrigé et audité au niveau `static-review` ;
- définitions, instances, lots, conteneurs, équipement, durabilité, propriété, provenance et réputation documentés ;
- autorisation des transferts, statuts de préparation et révisions multi-agrégats explicités ;
- frontières avec combat, compétences, agents, justice future et économie maintenues ;
- index, roadmap, `contents.txt`, audit et preuve QA mis à jour ;
- prochaine action déplacée vers le chapitre 21 — Économie, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

### 2026-07-20T16:52:26+02:00 — version 3.19.1

- retrait de la section interne `Validation légère sans PDF` du chapitre 19 destiné au lecteur ;
- conservation de cette procédure dans le protocole, le rapport d’audit, la preuve QA et les workflows ;
- chapitre 19 et audit portés en version `1.0.1` ;
- règle ajoutée aux erreurs à ne pas reproduire ;
- aucune exécution runtime et aucun PDF construit.

### 2026-07-20T15:27:31+02:00 — version 3.19.0

- chapitre 19 créé, corrigé et audité au niveau `static-review` ;
- définitions, coûts, ciblages, effets composables, progression, charges et recharges documentés ;
- commit séquentiel corrigé au profit d’une unité de travail commune ;
- ports de combat, personnage, ressources et contexte séparés ;
- sauvegarde limitée aux données durables et restauration préparée ;
- index, roadmap, `contents.txt`, audit et preuve QA mis à jour ;
- prochaine action déplacée vers le chapitre 20 — Inventaire et réputation des objets, niveau Élevée ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20T14:18:58+02:00 — version 3.18.0

- chapitre 18 porté de la porte de brouillon `0.9.0` à la version auditée `1.0.0` ;
- côtés, initiative, ciblage, portée, ligne de vue, dégâts, garde et états documentés ;
- copies détachées, historique avant commit, événements après commit et sauvegarde stricte établis ;
- chapitre clôturé par les décisions `Project Asteria`, sans prochaine étape dans le texte lecteur ;
- gouvernance et ordre de compilation mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.10

- chapitre 17 porté en version `1.0.3` ;
- section `Prochaine étape` retirée du texte destiné au lecteur ;
- chemin et niveau du chapitre suivant conservés uniquement dans `CONTINUITE-PROJET.md` ;
- clôture remplacée par une synthèse opérationnelle de `Project Asteria` ;
- règle rendue obligatoire pour les chapitres de systèmes 14 à 25 ;
- protocole QA porté en version `1.7.4` ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20T10:19:05+02:00 — version 3.17.9

- nomenclature des résultats négatifs ajoutée explicitement à la continuité du projet ;
- `Valeurs de retour`, `Codes de retour`, `Refus contrôlé`, `Statuts à distinguer` et `Traitement du résultat` deviennent les libellés permanents hors sections pédagogiques d’erreurs ;
- `Erreur fréquente` reste réservé aux pièges accompagnés d’un exemple fautif et d’une correction ;
- `last-verified` et `audit-date` adoptent le format ISO 8601 horodaté avec offset à partir du chapitre 17 ;
- chapitre et audit 17 portés en version `1.0.2`, protocole QA en version `1.7.3` ;
- aucune heure rétroactive inconnue n’est inventée.

### 2026-07-20 — version 3.17.8

- chapitre 17 porté en version `1.0.1` ;
- intervalles `ACTIVE`, `BACKGROUND` et `DORMANT` explicitement reliés à `6`, `60` et `600` ticks ;
- fréquences qualifiées de nominales et dépendantes de la fréquence physique configurée ;
- six libellés ambigus remplacés par valeurs ou codes de retour, refus contrôlé, statuts à distinguer et traitement du résultat ;
- politique de tick corrigée afin de conserver une échéance reportée par le budget ;
- protocole QA porté en version `1.7.2` ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.7

- chapitre 17 porté de la porte de brouillon `0.9.0` à `1.0.0` ;
- audit distinct terminé au niveau `static-review` ;
- codec d’agent complété et section de sauvegarde sécurisée ;
- planification déterministe, budgets logiques et ordonnanceur documentés ;
- IA générative maintenue dans un rôle consultatif ;
- index, roadmap, `contents.txt`, audit et preuve mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.6

- création du brouillon `0.9.0` du chapitre 17 ;
- état `draft`, audit `pending`, niveau `not-audited` ;
- périmètre agents autonomes séparé des personnages, relations, famille et combat ;
- porte de brouillon et preuve initiale enregistrées ;
- index, roadmap et `contents.txt` mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.5

- suppression des auto-paraphrases du titre de section dans toutes les rubriques d’explication ;
- correction de deux rôles factuellement incompatibles avec les requêtes familiales présentées ;
- recâblage de 23 renvois `À relire` vers les sous-sections exactes ;
- ajout de 21 ancres explicites et stables dans les chapitres 15 et 16 ;
- protocole QA porté en version `1.7.1` ;
- chapitres et audits 15 et 16 portés en version `1.2.1` ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.4

- correction éditoriale des explications de code des chapitres 15 et 16 ;
- suppression des rubriques `Emplacement` lorsque le chemin précède déjà le bloc ;
- suppression des rappels répétés sur les annotations `:` et `->` ;
- conservation des rôles uniquement lorsqu’ils apportent une responsabilité concrète ;
- simplification des exemples fautifs et corrigés ;
- suppression des lignes autonomes `Correction` et `Différence` lorsqu’elles répètent déjà les deux justifications ;
- ajout de renvois contextuels avant certaines erreurs ;
- chapitres, audits et preuves QA portés en version `1.2.0` ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.3

- correction post-fusion de la source de vérité de continuité ;
- versions courantes des chapitres 15 et 16 corrigées de `1.0.0` vers `1.1.0` ;
- comptage final corrigé à 56 blocs expliqués pour le chapitre 15 et 67 pour le chapitre 16 ;
- aucune modification du contenu technique des chapitres ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.2

- enrichissement pédagogique systématique des blocs de code des chapitres 15 et 16 ;
- explications ajoutées pour rôle, emplacement, types, paramètres, retours, effets de bord, déroulement, invariants et résultat attendu ;
- exemples fautifs et corrigés explicités selon la porte QA Q1.1 ;
- chapitres 15 et 16 portés en version `1.1.0` ;
- audits et preuves QA mis à jour ;
- chapitre 17 débloqué après validations finales ;
- aucun PDF construit et aucun test runtime revendiqué.

### 2026-07-20 — version 3.17.1

- règle pédagogique permanente renforcée : tout bloc de code significatif doit être expliqué en détail ;
- critères obligatoires ajoutés pour rôle, emplacement, types, paramètres, retours, erreurs, effets de bord, déroulement, invariants et résultat attendu ;
- une phrase générique n’est plus acceptée comme explication d’un bloc complexe ;
- correction rétroactive des chapitres 15 et 16 déclarée prioritaire et bloquante avant le chapitre 17 ;
- protocole QA et roadmap mis à jour ;
- aucun PDF construit.

### 2026-07-19 — version 3.17.0

- création, correction et audit statique du chapitre 16 ;
- séparation permanente entre famille, personnages et relations sociales ;
- filiations biologiques ou adoptives dirigées ;
- tutelles temporelles et unions par paires canoniques ;
- cycles d’ascendance, doublons et références inconnues refusés ;
- parcours d’ancêtres et descendants bornés ;
- fratries et générations calculées plutôt que persistées ;
- personnages décédés, archivés ou hors scène conservés ;
- événements et historique familial borné ;
- snapshot strict et restauration par graphe candidat ;
- progression à 16 chapitres sur 30 et systèmes de gameplay à 3 sur 12 ;
- prochaine action déplacée vers le chapitre 17 — Agents IA et comportements autonomes, niveau Élevée ;
- aucun PDF construit.

### 2026-07-19 — version 3.16.0

- création, correction et audit statique du chapitre 15 ;
- relations sociales orientées entre identifiants stables ;
- axes affinité, confiance, respect et peur bornés ;
- causes, provenance, ticks logiques et historique limité ;
- mutation atomique par copie profonde et remplacement validé ;
- requêtes et vues mutuelles indépendantes des scènes ;
- événements typés et index des relations sortantes ;
- snapshot strict et section de sauvegarde indépendante ;
- maintien de la famille, des agents, factions, réputations et récits dans leurs systèmes propres ;
- progression à 15 chapitres sur 30 et systèmes de gameplay à 2 sur 12 ;
- prochaine action déplacée vers le chapitre 16 — Famille et générations, niveau Élevée ;
- aucun PDF construit.

### 2026-07-19 — version 3.15.0

- création, correction et audit statique du chapitre 14 ;
- ouverture des douze systèmes de gameplay avec les personnages ;
- identité stable séparée du nom et des définitions de contenu ;
- définition de conception, état runtime et snapshot persistant séparés ;
- attributs bornés et statistiques dérivées reconstructibles ;
- scène composée avec corps, runtime, visuel, synchronisation et contrôleur séparés ;
- apparition, disparition et registre limité aux instances actives ;
- événements typés et sauvegarde validée avant application ;
- maintien des relations, famille, agents, combat et compétences dans leurs chapitres propres ;
- progression à 14 chapitres sur 30 et systèmes de gameplay à 1 sur 12 ;
- règle permanente ajoutée : chaque prochaine action affiche le chemin et le niveau GPT-5.6 Sol dans le même bloc ;
- prochaine action déplacée vers le chapitre 15 — Relations sociales ;
- aucun PDF construit.

### 2026-07-19 — version 3.14.0

- création, correction et audit statique du chapitre 13 ;
- modèle de menaces et frontières de confiance documentés ;
- séparation stricte entre production, livraison, runtime et données du joueur ;
- profils développement, test et production ;
- secrets hors dépôt et hors package ;
- boucle locale par défaut, authentification et TLS hors loopback ;
- autorisation par défaut refusée et listes d’autorisation ;
- chemins canoniques, moindre privilège, limites et quotas ;
- journaux rédigés et rétention distincte Solo/Studio ;
- dépendances épinglées, licences, SBOM, provenance et signature préparés ;
- échec fermé sans contournement par le repli déterministe ;
- plateforme IA locale terminée à quatre chapitres sur quatre ;
- progression à 13 chapitres sur 30 ;
- prochaine action déplacée vers le chapitre 14 — Personnages ;
- aucun PDF construit.

### 2026-07-19 — version 3.13.1

- correction post-audit de la section 51 du chapitre 12 ;
- conversion de neuf URL techniques en liens Markdown nommés et directement cliquables ;
- mise à jour du chapitre 12 vers la version `1.0.2` et de son audit vers `1.0.1` ;
- aucun changement de périmètre, aucune exécution runtime et aucun PDF construit.

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

### 2026-07-24 — Restauration des synthèses opérationnelles Asteria

- chapitres 17 à 20 complétés par une synthèse opérationnelle propre à Project Asteria ;
- progression autoritative corrigée de 18/30 à 20/30 ;
- règle de clôture ajoutée au plan maître et à la continuité ;
- validateur permanent ajouté pour empêcher une nouvelle régression ;
- audits et preuves QA actualisés sans modifier le niveau `static-review`.
