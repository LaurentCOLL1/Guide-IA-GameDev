---
title: "Audit du Livre II — Chapitre 11"
id: "DOC-L2-QA-CH11"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 11
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH11"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 11

> **Chapitre audité :** `Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le chapitre introduit une communication locale entre Godot et les outils IA sans confondre :

- port applicatif ;
- transport ;
- processus compagnon ;
- service de connaissance ;
- index Qdrant ;
- fonction de gameplay ;
- repli déterministe.

Il vérifie aussi que les détails HTTP, WebSocket, API compatibles OpenAI et files de tâches restent réservés au chapitre 12.

## 2. Couverture du périmètre officiel

| Exigence | Couverture |
|---|---|
| Frontière de service Godot / IA locale | Complet |
| Contrats de requête, réponse, erreur et capacité | Complet |
| Port applicatif indépendant de HTTP | Complet |
| Adaptateur local ou processus compagnon | Complet |
| Disponibilité facultative | Complet |
| Découverte des capacités | Complet |
| Appels asynchrones | Complet |
| Boucle principale non bloquée | Complet |
| Délais | Complet |
| Annulation coopérative | Complet |
| Erreurs structurées | Complet |
| Corrélation | Complet |
| Repli déterministe | Complet |
| Aucune lecture directe de Qdrant par Godot | Complet |
| Frontière HTTP / WebSocket | Préservée |
| Cycle de vie et arrêt contrôlé | Complet |
| Parcours Solo | Complet |
| Parcours Studio | Complet |
| Audit statique sans PDF | Complet |

## 3. Frontières avec les chapitres voisins

### 3.1 Chapitre 5

Le chapitre 11 réutilise :

- point de composition ;
- injection de dépendances ;
- service avec cycle de vie ;
- démarrage déterministe ;
- arrêt dans l’ordre inverse.

Il n’introduit ni Service Locator, ni Autoload par service.

### 3.2 Chapitre 7

`AiServiceConfig` prolonge la configuration typée. Les chemins et délais sont validés avant injection.

Aucun secret n’est ajouté au fichier de configuration versionné.

### 3.3 Chapitre 10

Le chapitre 10 reste propriétaire :

- du corpus ;
- du modèle ;
- du tokenizer ;
- des embeddings ;
- de Qdrant ;
- du repli lexical ;
- de l’évaluation.

Le chapitre 11 expose seulement une opération `knowledge.search` et un adaptateur Python. Godot ne lit jamais le stockage Qdrant.

### 3.4 Chapitre 12

Le chapitre 11 ne fournit aucun tutoriel détaillé sur :

- `HTTPRequest` ;
- `HTTPClient` ;
- `WebSocketPeer` ;
- streaming ;
- API compatibles OpenAI ;
- file de tâches ;
- workers ;
- backpressure ;
- retries réseau.

Le transport stdio prépare le remplacement d’adaptateur sans consommer ce périmètre.

### 3.5 Chapitre 13

Les limites de taille, listes fermées d’opérations et chemins fiables constituent des précautions minimales.

Le durcissement de production, les secrets, l’isolation, la signature des exécutables et les politiques réseau restent réservés au chapitre 13.

## 4. Architecture vérifiée

### 4.1 Direction des dépendances

Le flux est :

> **[LECTURE] Dépendances relues — Ne pas saisir.**

```text
fonctionnalité
    ↓
LocalAiGateway
    ↓
LocalAiGatewayService
    ↓
AiTransport
    ↓
StdioCompanionTransport
```

Le port ne dépend pas du transport concret.

### 4.2 Processus compagnon

Le processus Python :

- reçoit un objet JSON par ligne ;
- valide format et version ;
- distribue l’opération sur une liste fermée ;
- écrit une réponse par ligne ;
- réserve stdout au protocole ;
- écrit les journaux sur stderr ;
- fournit un handshake ;
- accepte une demande d’arrêt.

### 4.3 Repli

Le repli appartient à `beacons`, pas au gateway générique.

Il utilise un catalogue injecté et produit `retrieval_mode="deterministic_fallback"`.

## 5. Revue du protocole

### 5.1 Version

Les deux formats sont distincts :

- `project-asteria-ai-request` ;
- `project-asteria-ai-response`.

La version courante vaut `1`.

### 5.2 Corrélation

Chaque requête reçoit un identifiant combinant :

- préfixe aléatoire de session ;
- compteur croissant sur huit chiffres.

La réponse doit reprendre exactement cet identifiant.

### 5.3 Statuts

Une réponse vaut :

- `ok` avec `result` ;
- `error` avec un objet structuré.

Une valeur inconnue devient une erreur de protocole.

### 5.4 Erreurs

Les familles internes sont :

- `UNAVAILABLE` ;
- `TIMEOUT` ;
- `CANCELLED` ;
- `INVALID_REQUEST` ;
- `UNSUPPORTED_CAPABILITY` ;
- `PROTOCOL_ERROR` ;
- `INTERNAL_ERROR`.

Le code externe reste conservé pour le diagnostic.

### 5.5 Taille

Le chapitre borne :

- la ligne sortante ;
- le tampon entrant ;
- la longueur de la requête de connaissance ;
- le nombre de résultats ;
- le nombre de clés du payload ;
- la durée maximale acceptée côté Python.

## 6. Revue du transport Godot

### 6.1 Lancement

La signature relue est :

> **[LECTURE] Appel de référence — Ne pas exécuter depuis le rapport.**

```gdscript
OS.execute_with_pipe(path, arguments, false)
```

Le dictionnaire de retour est lu avec :

- `stdio` ;
- `stderr` ;
- `pid`.

### 6.2 Mode non bloquant

Le transport n’appelle pas une exécution bloquante.

Il sonde les flux depuis `_process()`.

### 6.3 Lecture

La revue vérifie :

- `get_length()` pour les octets disponibles ;
- `get_buffer()` pour une lecture bornée ;
- tampon de caractères incomplets ;
- séparation sur `\n` ;
- suppression optionnelle de `\r` ;
- absence d’analyse d’une ligne partielle.

### 6.4 Écriture

La revue vérifie :

- taille UTF-8 ;
- `store_line()` ;
- `flush()` ;
- `get_error()` ;
- aucun assemblage de commande shell.

### 6.5 Processus

La revue vérifie :

- `is_process_running()` ;
- `get_process_exit_code()` après arrêt ;
- `kill()` en dernier recours ;
- fermeture des `FileAccess` ;
- nettoyage des références ;
- état d’arrêt explicite.

## 7. Revue de l’orchestrateur

### 7.1 Handshake

Le gateway commence en `STARTING`.

Il demande `capabilities.describe` et passe :

- à `READY` si toutes les capacités déclarées sont disponibles ;
- à `DEGRADED` si une capacité est indisponible ou mal formée ;
- à `FAILED` si le handshake échoue.

### 7.2 Tickets

Chaque appel possède :

- un identifiant ;
- une opération ;
- une échéance monotone ;
- un état ;
- un signal de réussite ;
- un signal d’échec.

Un ticket ne peut être résolu qu’une fois.

### 7.3 Délais

Les échéances utilisent `Time.get_ticks_msec()`.

Une expiration :

1. retire le ticket ;
2. émet `TIMEOUT` ;
3. envoie `system.cancel`.

### 7.4 Réponses tardives

Une réponse qui ne possède plus de ticket :

- est journalisée ;
- est ignorée ;
- n’est jamais appliquée au gameplay.

### 7.5 Annulation

L’annulation locale retire le ticket avant d’envoyer la demande distante.

Le chapitre indique explicitement que le compagnon séquentiel ne peut pas interrompre immédiatement une bibliothèque bloquante.

### 7.6 Arrêt

Le gateway :

1. passe à `STOPPING` ;
2. envoie `system.shutdown` ;
3. rejette les tickets encore ouverts ;
4. attend la sortie ;
5. force l’arrêt uniquement après le délai.

## 8. Revue du compagnon Python

### 8.1 Syntaxe

Les cinq blocs Python du chapitre ont fait l’objet d’une compilation syntaxique locale.

Cette compilation ne charge ni Godot, ni le service de connaissance, ni les dépendances du chapitre 10.

### 8.2 Lecture

La boucle utilise `sys.stdin.readline()` dans une condition `while application.running`.

Cette forme permet de quitter après `system.shutdown` sans attendre une ligne supplémentaire.

### 8.3 JSON

La sérialisation utilise :

- `ensure_ascii=False` ;
- séparateurs compacts ;
- `allow_nan=False` ;
- `flush=True`.

### 8.4 Distribution

Les handlers sont enregistrés dans un dictionnaire fermé.

Une opération inconnue produit `unsupported_capability`.

### 8.5 Exception inattendue

Une exception inconnue :

- est détaillée seulement sur stderr ;
- retourne une erreur publique générique ;
- ne divulgue pas automatiquement une trace dans le protocole.

## 9. Découverte des capacités

Le résultat décrit :

- nom du service ;
- version de protocole ;
- opérations ;
- version par opération ;
- disponibilité ;
- limites.

Le chapitre distingue correctement :

- processus vivant ;
- service prêt ;
- capacité particulière disponible.

## 10. Revue de la fonctionnalité `beacons`

### 10.1 Façade métier

`BeaconKnowledgeService` centralise :

- nettoyage de la question ;
- payload ;
- langue ;
- tag ;
- limite ;
- validation du résultat ;
- politique de repli.

### 10.2 Repli ciblé

Le repli est autorisé pour :

- indisponibilité ;
- timeout ;
- capacité absente.

Il ne masque pas :

- requête invalide ;
- erreur de protocole ;
- erreur interne.

### 10.3 Autorité du gameplay

Le service IA fournit une recherche ou une explication.

Il ne décide pas de l’ouverture effective de la porte ni d’une règle durable de progression.

## 11. Revue des fonctions, paramètres, types et retours

Le chapitre explique notamment :

- `AiServiceConfig._init()` et `validate()` ;
- `AiServiceError.is_failure()` et `unavailable()` ;
- `AiCapability.supports()` ;
- `AiRequest.validate()` ;
- `AiResponse.is_ok()` ;
- `AiCallTicket.resolve()`, `reject()` et `mark_cancelled()` ;
- `AiServiceStatus.set_state()` ;
- `AiEnvelopeCodec.encode_request()` et `decode_response()` ;
- `AiTransport` ;
- `StdioCompanionTransport.configure()`, `start()`, `send_line()`, `_process()` et `stop()` ;
- `LocalAiGateway` ;
- génération de `request_id` ;
- `LocalAiGatewayService.start_service()`, `request()`, `cancel()`, `supports()` et `shutdown_service()` ;
- parseur Python ;
- adaptateur de connaissance ;
- distribution du compagnon ;
- façade des balises ;
- repli déterministe ;
- bootstrap ;
- arrêt de l’application.

Les paramètres, valeurs par défaut, opérateurs et résultats sont expliqués au voisinage de leur première apparition.

## 12. Règle sémantique des erreurs

La section `Erreurs fréquentes, pièges et corrections` porte :

> **[LECTURE] Marqueur QA — Ne pas saisir.**

```html
<!-- qa:error-correction-section -->
```

Elle contient seize cas détaillés. Chacun fournit :

- un symptôme ;
- un exemple fautif ;
- une correction ;
- un exemple corrigé ou un flux équivalent ;
- une différence explicite.

## 13. Non-conformités détectées et corrigées

| N° | Risque initial | Correction |
|---:|---|---|
| 1 | Boucle Python attendant une ligne après `shutdown` | Boucle `while` vérifiant l’état avant `readline()` |
| 2 | `stop(false)` fermant les handles d’un processus vivant | Nettoyage seulement après sortie ou arrêt forcé |
| 3 | Détails d’erreur supposés dictionnaire | Validation du type avant copie |
| 4 | État `READY` malgré capacité indisponible | Passage à `DEGRADED` |
| 5 | Processus conservé après échec du handshake | Arrêt forcé ciblé |
| 6 | Ligne partielle analysée comme JSON | Tampon et séparation explicite |
| 7 | Réponse tardive appliquée | Registre vérifié avant résolution |
| 8 | Timeout présenté comme kill | Annulation coopérative documentée |
| 9 | Repli global | Liste fermée d’erreurs techniques |
| 10 | Gameplay dépendant du service | Autorité déterministe conservée |
| 11 | stdout utilisé pour les logs | stderr réservé aux diagnostics |
| 12 | Chemin de commande contrôlé par une saisie | Configuration fiable et arguments séparés |
| 13 | Processus supposé arrêté avec Godot | Cycle d’arrêt explicite |
| 14 | État du processus confondu avec une capacité | Handshake versionné |
| 15 | Port dépendant de HTTP | Opérations indépendantes du transport |
| 16 | Tampon illimité | Limite en octets avant accumulation |

## 14. Contrôle des doublons

La revue locale du chapitre détecte :

- aucun titre dupliqué ;
- aucun bloc significatif dupliqué ;
- aucun paragraphe long dupliqué.

Le workflow permanent doit confirmer la mesure sur l’ensemble du dépôt.

## 15. Repères d’utilisation

Le chapitre utilise :

- `[VSC]` pour les fichiers ;
- `[LECTURE]` pour les structures et exemples ;
- `[SORTIE]` pour le résultat illustratif.

Les repères restants figurent dans la légende sans être employés artificiellement.

Tous les blocs clôturés possèdent un repère immédiatement identifiable.

## 16. Réserves runtime

Ne sont pas exécutés :

- parsing GDScript ;
- chargement du projet Godot ;
- `OS.execute_with_pipe()` ;
- démarrage de Python sous Windows ;
- flux non bloquants ;
- fragmentation des messages ;
- limites de tampon ;
- corrélation simultanée ;
- handshake ;
- timeout ;
- annulation ;
- réponse tardive ;
- crash ;
- arrêt normal ;
- arrêt forcé ;
- adaptation du `RetrievalService` ;
- repli des balises ;
- export Windows ;
- Web ;
- mobile ;
- packaging du runtime.

## 17. PDF

Conformément à la politique du projet :

- aucun PDF intermédiaire n’est construit ;
- la compilation et l’inspection restent différées jusqu’à la fin du Livre II.

## 18. Sources officielles vérifiées

La revue statique s’appuie sur :

- [Godot 4.7 — OS](https://docs.godotengine.org/en/4.7/classes/class_os.html) ;
- [Godot 4.7 — FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html) ;
- [Godot 4.7 — JSON](https://docs.godotengine.org/en/4.7/classes/class_json.html) ;
- [Godot 4.7 — Time](https://docs.godotengine.org/en/4.7/classes/class_time.html) ;
- [Godot 4.7 — ProjectSettings](https://docs.godotengine.org/en/4.7/classes/class_projectsettings.html) ;
- [Godot 4.7 — Signals](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html) ;
- [Python 3 — `json`](https://docs.python.org/3/library/json.html) ;
- [Python 3 — `sys`](https://docs.python.org/3/library/sys.html) ;
- [Python 3 — `dataclasses`](https://docs.python.org/3/library/dataclasses.html) ;
- [Python 3 — `typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol).

## 19. Décision

**Accepté avec réserves runtime et PDF de fin de Livre.**

Le chapitre peut être déclaré **rédigé, repéré et audité au niveau `static-review`** après réussite des workflows légers :

- `Validate Chapters Without PDF` ;
- `Validate Usage Contexts`.

Cette décision ne revendique aucune exécution de Godot, de Python, du processus compagnon, du transport ou du service de connaissance.
