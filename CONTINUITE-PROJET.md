---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "3.36.2"
lang: "fr-FR"
last-updated: "2026-07-23T01:25:59+02:00"
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

Tout bloc de code significatif doit recevoir une explication proportionnée à sa complexité et limitée aux informations réellement utiles : entrées et types, paramètres, valeurs de retour, effets de bord, instructions non évidentes, invariants, résultat attendu et limites pertinentes. `Rôle` est conservé seulement lorsqu’il nomme un contrat, une fonction, une transformation ou une responsabilité concrète. `Emplacement` est omis lorsque le chemin est déjà donné par le contexte adjacent. Les règles générales de syntaxe déjà expliquées ne sont pas répétées.

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

**En cours : 6 chapitres sur 30.**

1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.
2. Direction artistique et bible visuelle — terminé au niveau `static-review`.
3. Références, concept art et ComfyUI — terminé au niveau `static-review`.
4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.
5. Provenance, licences et validation des assets — terminé au niveau `static-review`.
6. Création des humains — terminé au niveau `static-review`.

Les chapitres 7 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.

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

Chapitres 3 à 29 : **Élevée**.

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

Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.8`.

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

- ne pas oublier la mise à jour de ce fichier.

## 25. État courant

- branche principale : `main` ;
- jalon : M4 — Livre III ;
- progression du Livre III : 6 chapitres sur 30 ;
- chapitre 1 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 2 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 3 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 4 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 5 du Livre III : version `1.0.0`, niveau `static-review` ;
- chapitre 6 du Livre III : version `1.0.0`, niveau `static-review` ;
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
- Starter Kit non matérialisé ;
- licence globale à définir ;
- publication technique du Livre II acceptée après compilation et inspection PDF ;
- licence globale à décider avant publication officielle de la collection ;
- accessibilité PDF avancée et balisage à traiter avant publication officielle.

## 26. Prochaine action

Le chapitre 6 du Livre III est rédigé, repéré et audité au niveau `static-review`. La base humaine documentaire couvre références anatomiques, proportions, topologie de déformation, modules, variantes morphologiques, préparation UV et matériaux, budgets LOD et scène Godot de validation. Aucun maillage, rig, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-07-Creation-des-humanoides.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 7 adaptera le contrat de la base humaine à des espèces humanoïdes distinctes, en documentant les écarts anatomiques, profils de rig, compatibilités d’équipement, variations culturelles et tests de silhouette sans produire les créatures non humanoïdes du chapitre 9.

## 27. Journal

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
