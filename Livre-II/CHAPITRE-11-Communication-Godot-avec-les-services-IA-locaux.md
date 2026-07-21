---
title: "Livre II — Chapitre 11 : Communication Godot avec les services IA locaux"
id: "DOC-L2-CH11"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 11
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-11.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Communication Godot avec les services IA locaux

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH11`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-11.md`.

## 1. Rôle du chapitre

Le chapitre 10 a construit une chaîne locale de connaissances en Python : sources canoniques, découpage, embeddings, index Qdrant dérivé, repli lexical et évaluation. Cette chaîne reste volontairement extérieure aux scènes Godot.

Le présent chapitre ajoute une **frontière de service** entre le jeu et les outils IA locaux. Godot ne charge pas `sentence-transformers`, ne manipule pas Qdrant et ne connaît pas la structure interne du modèle. Il formule une demande métier versionnée, reçoit une réponse typée et reste capable de poursuivre lorsque le service est absent.

À la fin du chapitre, le lecteur doit savoir :

- distinguer port applicatif, transport, processus compagnon et fonctionnalité de repli ;
- définir des contrats de requête, réponse, erreur et capacité ;
- démarrer un processus Python local sans bloquer la boucle principale ;
- échanger des messages JSON délimités par des sauts de ligne ;
- corréler chaque réponse avec sa requête ;
- découvrir les capacités disponibles avant de les utiliser ;
- appliquer des délais avec une horloge monotone ;
- demander une annulation coopérative ;
- arrêter proprement le processus compagnon ;
- conserver un chemin déterministe lorsque l’IA locale est indisponible ;
- préserver les frontières des chapitres 12 et 13.

## 2. Prérequis

Le lecteur doit connaître :

- les fonctions, signaux, dictionnaires et types du chapitre 2 ;
- les nœuds et le cycle de vie du chapitre 3 ;
- les frontières feature-first du chapitre 4 ;
- les contrats, services, bootstrap et injection du chapitre 5 ;
- la configuration typée du chapitre 7 ;
- le contrat de mémoire vectorielle du chapitre 10 ;
- l’environnement Python local du Livre I.

Le chapitre ne demande pas Docker. Il réutilise le processus Python local et le repli lexical du chapitre 10.

## 3. Périmètre et frontières

Ce chapitre définit :

- un port `LocalAiGateway` indépendant du transport ;
- un protocole JSON versionné ;
- un transport local par entrée et sortie standard ;
- un processus compagnon Python ;
- la découverte de capacités ;
- les appels asynchrones ;
- les délais, corrélations et annulations ;
- le cycle de vie et l’arrêt contrôlé ;
- un repli déterministe au niveau de la fonctionnalité.

Il ne définit pas encore :

- les routes HTTP ;
- les connexions WebSocket ;
- les API compatibles OpenAI ;
- le streaming de tokens ;
- les files persistantes de tâches ;
- les stratégies de backpressure et de reprise distribuée ;
- les secrets, politiques réseau et durcissement de production.

Ces sujets appartiennent respectivement aux chapitres 12 et 13.

> **Frontière essentielle :** le port applicatif décrit ce que le jeu demande. Il ne décrit pas comment le message voyage.

## 4. Comparaison avec les chapitres voisins

### 4.1 Chapitre 10

Le chapitre 10 reste propriétaire :

- des sources canoniques ;
- du découpage ;
- des embeddings ;
- de Qdrant ;
- du repli lexical ;
- des métriques de récupération.

Le chapitre 11 ne recopie pas ces algorithmes. Il les place derrière une opération comme `knowledge.search`.

### 4.2 Chapitre 12

Le chapitre 12 choisira et détaillera des transports réseau :

- `HTTPRequest` ;
- `HTTPClient` ;
- `WebSocketPeer` ;
- API compatibles OpenAI ;
- files de tâches ;
- retries et backpressure.

Le présent chapitre emploie uniquement un processus compagnon local avec JSON par lignes.

### 4.3 Chapitre 13

Le chapitre 13 traitera :

- isolation production/runtime ;
- secrets ;
- listes d’autorisation ;
- distribution des exécutables ;
- politiques de réseau ;
- sandboxing ;
- mises à jour et signatures.

Le présent chapitre applique déjà des limites minimales, sans prétendre constituer ce durcissement final.

## 5. Vocabulaire

### 5.1 Port applicatif

Un **port applicatif** est un contrat utilisé par le code du jeu. Il expose des opérations métier sans dépendre de Python, de Qdrant, de HTTP ou d’un format de socket.

### 5.2 Adaptateur

Un **adaptateur** relie un port à une technologie concrète. Ici, `StdioCompanionTransport` relie Godot aux flux standard d’un processus Python.

### 5.3 Processus compagnon

Un **processus compagnon** est un programme local démarré à côté du jeu. Il possède son propre runtime, ses dépendances et son cycle de vie.

### 5.4 Corrélation

La **corrélation** associe une réponse à la requête qui l’a produite grâce à un `request_id` unique.

### 5.5 Capacité

Une **capacité** décrit une opération réellement disponible, sa version et ses limites. Le jeu ne doit pas supposer qu’un service possède toutes les fonctions possibles.

### 5.6 Délai

Un **délai**, ou *timeout*, est la durée maximale accordée par l’appelant. Il ne signifie pas nécessairement que le travail distant s’arrête instantanément.

### 5.7 Annulation coopérative

Une annulation est **coopérative** lorsque le service reçoit une demande d’arrêt et la vérifie à des points sûrs. Elle n’est pas une garantie d’interruption immédiate d’une bibliothèque native.

### 5.8 Repli déterministe

Un **repli déterministe** produit le même résultat pour les mêmes données locales. Il ne tente pas d’imiter une réponse générative indisponible.

## 6. Architecture de référence

> **[LECTURE] Architecture logique — Ne pas saisir.**

```text
fonctionnalité Godot
        ↓
port LocalAiGateway
        ↓
orchestrateur de requêtes
        ↓
transport local abstrait
        ↓
StdioCompanionTransport
        ↓
processus Python compagnon
        ↓
adaptateurs IA locaux
        ↓
RetrievalService du chapitre 10
```

Le domaine ne dépend pas du transport. Le transport ne décide pas du repli métier. Le processus Python ne modifie pas directement les scènes Godot.

## 7. Flux d’un appel

> **[LECTURE] Séquence de référence — Ne pas saisir.**

```text
Godot crée une requête typée
        ↓
le gateway attribue request_id et deadline locale
        ↓
le transport sérialise une ligne JSON
        ↓
le compagnon valide et distribue l’opération
        ↓
le service local produit un résultat ou une erreur
        ↓
une réponse JSON reprend le même request_id
        ↓
le gateway résout le ticket correspondant
        ↓
la fonctionnalité accepte le résultat ou applique son repli
```

Chaque couche refuse les données qu’elle ne comprend pas. Une réponse sans corrélation valide n’est jamais appliquée au gameplay.

## 8. États du service

Le service suit un cycle de vie explicite :

> **[LECTURE] États autorisés — Ne pas saisir.**

```text
STOPPED
   ↓ start()
STARTING
   ↓ capacités validées
READY
   ↘ capacité partielle
   DEGRADED
   ↘ panne
   FAILED
   ↓ shutdown()
STOPPING
   ↓ processus terminé
STOPPED
```

`READY` signifie que les capacités obligatoires sont disponibles. `DEGRADED` signifie que le processus répond, mais qu’une partie des capacités manque. `FAILED` conserve un diagnostic.

## 9. Protocole JSON par lignes

Le transport utilise un objet JSON par ligne. Le saut de ligne clôt le message.

### 9.1 Requête

> **[LECTURE] Enveloppe de requête — Ne pas saisir.**

```json
{
  "format": "project-asteria-ai-request",
  "format_version": 1,
  "request_id": "ai-00000001",
  "operation": "knowledge.search",
  "timeout_ms": 2500,
  "payload": {
    "query": "Comment ouvrir la porte nord ?",
    "allowed_visibility": ["internal"],
    "language": "fr",
    "required_tags": ["beacon"],
    "limit": 5
  }
}
```

`timeout_ms` est une durée relative. Il ne transporte pas une valeur d’horloge absolue, car les horloges monotones de Godot et du processus Python ne partagent pas la même origine.

### 9.2 Réponse réussie

> **[LECTURE] Enveloppe de réussite — Ne pas saisir.**

```json
{
  "format": "project-asteria-ai-response",
  "format_version": 1,
  "request_id": "ai-00000001",
  "status": "ok",
  "result": {
    "retrieval_mode": "vector",
    "hits": []
  }
}
```

### 9.3 Réponse en erreur

> **[LECTURE] Enveloppe d’erreur — Ne pas saisir.**

```json
{
  "format": "project-asteria-ai-response",
  "format_version": 1,
  "request_id": "ai-00000001",
  "status": "error",
  "error": {
    "code": "unsupported_capability",
    "message": "L’opération knowledge.search est indisponible.",
    "retryable": false,
    "details": {}
  }
}
```

Le champ `status` vaut seulement `ok` ou `error`. Une erreur est une donnée structurée, pas une phrase libre analysée par le gameplay.

## 10. Arborescence

> **[VSC] Visual Studio Code — Créer les dossiers et fichiers suivants :**

```text
ProjectAsteria/
├── src/
│   ├── core/ai/
│   │   ├── ai_service_error.gd
│   │   ├── ai_capability.gd
│   │   ├── ai_request.gd
│   │   ├── ai_response.gd
│   │   ├── ai_call_ticket.gd
│   │   ├── ai_service_status.gd
│   │   ├── ai_envelope_codec.gd
│   │   ├── ai_transport.gd
│   │   ├── local_ai_gateway.gd
│   │   ├── stdio_companion_transport.gd
│   │   └── local_ai_gateway_service.gd
│   ├── features/beacons/
│   │   ├── application/beacon_knowledge_service.gd
│   │   └── infrastructure/beacon_knowledge_fallback.gd
│   └── app/ai_bootstrap.gd
├── tools/ai/
│   ├── companion_protocol.py
│   ├── knowledge_service_adapter.py
│   └── companion_service.py
└── scenes/learning/ch11_local_ai_demo.gd
```

`core/ai` contient les contrats génériques. La fonctionnalité `beacons` choisit son repli. `src/app` compose les dépendances. `tools/ai` reste extérieur au runtime GDScript.

## 11. Configuration de la frontière IA

Le chapitre 7 a introduit `AppConfig`. Le présent chapitre ajoute une section typée, sans stocker de secret.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_service_config.gd`.

```gdscript
class_name AiServiceConfig
extends RefCounted

var enabled: bool
var python_executable: String
var companion_script: String
var startup_timeout_ms: int
var request_timeout_ms: int
var shutdown_timeout_ms: int
var max_message_bytes: int

func _init(
	enabled_value: bool,
	python_executable_value: String,
	companion_script_value: String,
	startup_timeout_value: int = 5000,
	request_timeout_value: int = 2500,
	shutdown_timeout_value: int = 1500,
	max_message_bytes_value: int = 1048576
) -> void:
	enabled = enabled_value
	python_executable = python_executable_value
	companion_script = companion_script_value
	startup_timeout_ms = startup_timeout_value
	request_timeout_ms = request_timeout_value
	shutdown_timeout_ms = shutdown_timeout_value
	max_message_bytes = max_message_bytes_value

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if startup_timeout_ms < 100:
		errors.append("startup_timeout_ms doit être supérieur ou égal à 100.")
	if request_timeout_ms < 100:
		errors.append("request_timeout_ms doit être supérieur ou égal à 100.")
	if shutdown_timeout_ms < 100:
		errors.append("shutdown_timeout_ms doit être supérieur ou égal à 100.")
	if max_message_bytes < 1024 or max_message_bytes > 16 * 1024 * 1024:
		errors.append("max_message_bytes doit rester entre 1 Kio et 16 Mio.")
	if enabled and python_executable.strip_edges().is_empty():
		errors.append("python_executable est obligatoire lorsque le service est activé.")
	if enabled and companion_script.strip_edges().is_empty():
		errors.append("companion_script est obligatoire lorsque le service est activé.")
	return errors
```

### 11.1 Explication

`enabled` permet de désactiver explicitement le service. Les deux chemins sont fournis par une configuration fiable, jamais par une saisie du joueur.

`_init()` reçoit sept paramètres obligatoires ou dotés d’une valeur par défaut. Chaque `*_value` est un argument concret affecté à un champ.

`validate()` retourne `PackedStringArray`. Un tableau vide signifie que le contrat est valide. L’opérateur `or` refuse les tailles hors intervalle. `16 * 1024 * 1024` calcule seize mébioctets.

Les chemins `res://` doivent être convertis avec `ProjectSettings.globalize_path()` avant le lancement du processus.

## 12. Erreur structurée

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_service_error.gd`.

```gdscript
class_name AiServiceError
extends RefCounted

enum Kind {
	NONE,
	UNAVAILABLE,
	TIMEOUT,
	CANCELLED,
	INVALID_REQUEST,
	UNSUPPORTED_CAPABILITY,
	PROTOCOL_ERROR,
	INTERNAL_ERROR,
}

var kind: Kind
var code: StringName
var message: String
var retryable: bool
var details: Dictionary

func _init(
	kind_value: Kind = Kind.NONE,
	code_value: StringName = &"",
	message_value: String = "",
	retryable_value: bool = false,
	details_value: Dictionary = {}
) -> void:
	kind = kind_value
	code = code_value
	message = message_value
	retryable = retryable_value
	details = details_value.duplicate(true)

func is_failure() -> bool:
	return kind != Kind.NONE

static func unavailable(message_value: String) -> AiServiceError:
	return AiServiceError.new(
		Kind.UNAVAILABLE,
		&"unavailable",
		message_value,
		true
	)
```

### 12.1 Explication

`enum Kind` associe un nom stable à chaque famille d’erreur. `code` conserve le code fourni par le protocole. `message` est destiné au diagnostic, pas à une logique conditionnelle.

`details_value.duplicate(true)` crée une copie profonde. L’appelant ne peut donc pas modifier silencieusement les détails déjà enregistrés.

`is_failure()` retourne un booléen. L’opérateur `!=` vérifie que le type n’est pas `NONE`.

`unavailable()` est une fonction statique de construction. Elle retourne un nouvel objet `AiServiceError`.

## 13. Capacité déclarée

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_capability.gd`.

```gdscript
class_name AiCapability
extends RefCounted

var operation: StringName
var version: int
var available: bool
var limits: Dictionary

func _init(
	operation_value: StringName,
	version_value: int,
	available_value: bool,
	limits_value: Dictionary = {}
) -> void:
	operation = operation_value
	version = version_value
	available = available_value
	limits = limits_value.duplicate(true)

func supports(minimum_version: int = 1) -> bool:
	return available and version >= minimum_version
```

`operation` identifie une action, par exemple `knowledge.search`. `version` permet une évolution explicite. `supports()` retourne `true` seulement si la capacité est disponible et assez récente.

## 14. Requête typée

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_request.gd`.

```gdscript
class_name AiRequest
extends RefCounted

var request_id: StringName
var operation: StringName
var payload: Dictionary
var timeout_ms: int

func _init(
	request_id_value: StringName,
	operation_value: StringName,
	payload_value: Dictionary,
	timeout_ms_value: int
) -> void:
	request_id = request_id_value
	operation = operation_value
	payload = payload_value.duplicate(true)
	timeout_ms = timeout_ms_value

func validate(max_payload_keys: int = 64) -> PackedStringArray:
	var errors := PackedStringArray()
	if request_id.is_empty():
		errors.append("request_id est vide.")
	if operation.is_empty():
		errors.append("operation est vide.")
	if timeout_ms < 100:
		errors.append("timeout_ms doit être supérieur ou égal à 100.")
	if payload.size() > max_payload_keys:
		errors.append("Le payload contient trop de clés.")
	return errors
```

`payload` reste un dictionnaire à cette frontière générique. Chaque opération possède ensuite son propre validateur métier. Le gameplay ne doit pas construire ce dictionnaire partout ; un service de fonctionnalité le centralise.

## 15. Réponse typée

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_response.gd`.

```gdscript
class_name AiResponse
extends RefCounted

var request_id: StringName
var result: Dictionary
var error: AiServiceError

func _init(
	request_id_value: StringName,
	result_value: Dictionary = {},
	error_value: AiServiceError = null
) -> void:
	request_id = request_id_value
	result = result_value.duplicate(true)
	error = error_value

func is_ok() -> bool:
	return error == null or not error.is_failure()
```

`result` contient le résultat validé de l’opération. `error` vaut `null` en cas de succès. `is_ok()` combine une vérification de nullité et l’état de l’erreur.

## 16. Ticket d’appel asynchrone

Un ticket représente une opération en cours. Il permet à la fonctionnalité de s’abonner à la réussite, à l’échec ou à l’annulation.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_call_ticket.gd`.

```gdscript
class_name AiCallTicket
extends RefCounted

signal completed(response: AiResponse)
signal failed(error: AiServiceError)

enum State {
	PENDING,
	COMPLETED,
	FAILED,
	CANCELLED,
}

var request_id: StringName
var state := State.PENDING
var deadline_msec: int
var operation: StringName

func _init(
	request_id_value: StringName,
	operation_value: StringName,
	deadline_msec_value: int
) -> void:
	request_id = request_id_value
	operation = operation_value
	deadline_msec = deadline_msec_value

func resolve(response: AiResponse) -> void:
	if state != State.PENDING:
		return
	state = State.COMPLETED
	completed.emit(response)

func reject(error: AiServiceError) -> void:
	if state != State.PENDING:
		return
	state = State.FAILED
	failed.emit(error)

func mark_cancelled(error: AiServiceError) -> void:
	if state != State.PENDING:
		return
	state = State.CANCELLED
	failed.emit(error)
```

`signal completed(response: AiResponse)` annonce le type transmis. `deadline_msec` est calculé avec l’horloge monotone de Godot. Les trois méthodes refusent une seconde résolution.

Le ticket ne supprime pas lui-même la requête du gateway. Cette responsabilité appartient à l’orchestrateur, qui possède le registre des appels.

## 17. État du service

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_service_status.gd`.

```gdscript
class_name AiServiceStatus
extends RefCounted

enum State {
	STOPPED,
	STARTING,
	READY,
	DEGRADED,
	FAILED,
	STOPPING,
}

var state := State.STOPPED
var message := ""
var changed_at_msec := 0

func set_state(next_state: State, next_message: String = "") -> void:
	state = next_state
	message = next_message
	changed_at_msec = Time.get_ticks_msec()
```

`Time.get_ticks_msec()` fournit une valeur monotone adaptée à la mesure d’une durée. Elle ne doit pas être enregistrée comme date civile.

## 18. Codec du protocole

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_envelope_codec.gd`.

```gdscript
class_name AiEnvelopeCodec
extends RefCounted

const REQUEST_FORMAT := "project-asteria-ai-request"
const RESPONSE_FORMAT := "project-asteria-ai-response"
const FORMAT_VERSION := 1

static func encode_request(request: AiRequest) -> String:
	var errors := request.validate()
	if not errors.is_empty():
		return ""

	var envelope := {
		"format": REQUEST_FORMAT,
		"format_version": FORMAT_VERSION,
		"request_id": String(request.request_id),
		"operation": String(request.operation),
		"timeout_ms": request.timeout_ms,
		"payload": request.payload,
	}
	return JSON.stringify(envelope, "", false, true)

static func decode_response(line: String) -> AiResponse:
	var json := JSON.new()
	var parse_error := json.parse(line)
	if parse_error != OK:
		return AiResponse.new(
			&"",
			{},
			AiServiceError.new(
				AiServiceError.Kind.PROTOCOL_ERROR,
				&"invalid_json",
				"JSON invalide à la ligne %d : %s"
				% [json.get_error_line(), json.get_error_message()]
			)
		)

	if not json.data is Dictionary:
		return _protocol_failure(&"", "La réponse doit être un objet.")

	var envelope := json.data as Dictionary
	var request_id := StringName(String(envelope.get("request_id", "")))
	if String(envelope.get("format", "")) != RESPONSE_FORMAT:
		return _protocol_failure(request_id, "Format de réponse inconnu.")
	if int(envelope.get("format_version", -1)) != FORMAT_VERSION:
		return _protocol_failure(request_id, "Version de réponse incompatible.")

	var status := String(envelope.get("status", ""))
	if status == "ok":
		if not envelope.get("result", null) is Dictionary:
			return _protocol_failure(request_id, "result doit être un objet.")
		return AiResponse.new(request_id, envelope["result"] as Dictionary)

	if status != "error":
		return _protocol_failure(request_id, "status doit valoir ok ou error.")
	if not envelope.get("error", null) is Dictionary:
		return _protocol_failure(request_id, "error doit être un objet.")

	return AiResponse.new(
		request_id,
		{},
		_decode_error(envelope["error"] as Dictionary)
	)

static func _decode_error(data: Dictionary) -> AiServiceError:
	var code := StringName(String(data.get("code", "internal_error")))
	var details_value: Variant = data.get("details", {})
	var details := (
		details_value as Dictionary
		if details_value is Dictionary
		else {}
	)
	return AiServiceError.new(
		_kind_from_code(code),
		code,
		String(data.get("message", "Erreur sans message.")),
		bool(data.get("retryable", false)),
		details
	)

static func _kind_from_code(code: StringName) -> AiServiceError.Kind:
	match code:
		&"unavailable":
			return AiServiceError.Kind.UNAVAILABLE
		&"timeout":
			return AiServiceError.Kind.TIMEOUT
		&"cancelled":
			return AiServiceError.Kind.CANCELLED
		&"invalid_request":
			return AiServiceError.Kind.INVALID_REQUEST
		&"unsupported_capability":
			return AiServiceError.Kind.UNSUPPORTED_CAPABILITY
		&"protocol_error":
			return AiServiceError.Kind.PROTOCOL_ERROR
		_:
			return AiServiceError.Kind.INTERNAL_ERROR

static func _protocol_failure(
	request_id: StringName,
	message: String
) -> AiResponse:
	return AiResponse.new(
		request_id,
		{},
		AiServiceError.new(
			AiServiceError.Kind.PROTOCOL_ERROR,
			&"protocol_error",
			message
		)
	)
```

### 18.1 Explication

`encode_request()` retourne une chaîne vide si la requête est invalide. Une implémentation plus riche peut retourner un résultat discriminé ; le chapitre conserve ici une forme lisible.

`JSON.stringify()` reçoit quatre arguments : la valeur, l’indentation vide, le tri des clés désactivé et la précision complète activée. Le saut de ligne est ajouté par le transport, pas par le codec.

`decode_response()` retourne toujours `AiResponse`. Une erreur de protocole devient une réponse en échec, ce qui évite un type de retour ambigu.

`match` associe les codes externes à l’énumération interne. Un code inconnu devient `INTERNAL_ERROR` et reste visible dans `code`.

## 19. Port du transport

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_transport.gd`.

```gdscript
class_name AiTransport
extends Node

signal line_received(line: String)
signal transport_failed(error: AiServiceError)
signal transport_stopped(exit_code: int)

func start() -> Error:
	return ERR_UNAVAILABLE

func send_line(_line: String) -> Error:
	return ERR_UNAVAILABLE

func stop(_force: bool = false) -> void:
	pass

func is_running() -> bool:
	return false
```

Ce contrat ne mentionne ni `FileAccess`, ni PID, ni HTTP. Un futur transport du chapitre 12 pourra respecter la même responsabilité générale sans modifier le port applicatif.

## 20. Transport par processus compagnon

`OS.execute_with_pipe()` démarre un processus et expose ses flux. Le mode non bloquant permet à Godot de continuer à rendre les images.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/stdio_companion_transport.gd`.

```gdscript
class_name StdioCompanionTransport
extends AiTransport

var _python_path: String
var _script_path: String
var _max_message_bytes: int

var _stdio: FileAccess
var _stderr: FileAccess
var _pid := -1
var _read_buffer := ""
var _stopping := false

func configure(
	python_path: String,
	script_path: String,
	max_message_bytes: int
) -> void:
	_python_path = python_path
	_script_path = script_path
	_max_message_bytes = max_message_bytes

func start() -> Error:
	if is_running():
		return ERR_ALREADY_IN_USE
	if _python_path.is_empty() or _script_path.is_empty():
		return ERR_INVALID_PARAMETER

	var result := OS.execute_with_pipe(
		_python_path,
		PackedStringArray([_script_path]),
		false
	)
	if result.is_empty():
		return ERR_CANT_FORK

	_stdio = result.get("stdio") as FileAccess
	_stderr = result.get("stderr") as FileAccess
	_pid = int(result.get("pid", -1))
	if _stdio == null or _stderr == null or _pid <= 0:
		_cleanup_handles()
		return ERR_CANT_FORK

	_stopping = false
	set_process(true)
	return OK

func send_line(line: String) -> Error:
	if not is_running() or _stdio == null:
		return ERR_UNAVAILABLE
	var encoded_size := line.to_utf8_buffer().size()
	if encoded_size < 1 or encoded_size > _max_message_bytes:
		return ERR_INVALID_PARAMETER
	if not _stdio.store_line(line):
		return _stdio.get_error()
	_stdio.flush()
	var stream_error := _stdio.get_error()
	return OK if stream_error == OK else stream_error

func _process(_delta: float) -> void:
	_read_stdout()
	_read_stderr()
	_check_process()

func _read_stdout() -> void:
	if _stdio == null:
		return
	var available := _stdio.get_length()
	if available <= 0:
		return
	if _read_buffer.to_utf8_buffer().size() + available > _max_message_bytes:
		_fail_protocol("Le tampon stdout dépasse la limite.")
		return

	var bytes := _stdio.get_buffer(available)
	if _stdio.get_error() != OK:
		_fail_transport("Lecture stdout impossible.")
		return
	_read_buffer += bytes.get_string_from_utf8()

	while true:
		var newline := _read_buffer.find("\n")
		if newline < 0:
			break
		var line := _read_buffer.substr(0, newline).trim_suffix("\r")
		_read_buffer = _read_buffer.substr(newline + 1)
		if not line.is_empty():
			line_received.emit(line)

func _read_stderr() -> void:
	if _stderr == null:
		return
	var available := _stderr.get_length()
	if available <= 0:
		return
	var text := _stderr.get_buffer(available).get_string_from_utf8()
	if _stderr.get_error() != OK:
		_fail_transport("Lecture stderr impossible.")
		return
	for line: String in text.split("\n", false):
		if not line.strip_edges().is_empty():
			push_warning("[AI companion] %s" % line.strip_edges())

func _check_process() -> void:
	if _pid <= 0 or OS.is_process_running(_pid):
		return
	var exit_code := OS.get_process_exit_code(_pid)
	_cleanup_handles()
	transport_stopped.emit(exit_code)
	if not _stopping and exit_code != 0:
		transport_failed.emit(
			AiServiceError.unavailable(
				"Le processus compagnon s’est arrêté avec le code %d."
				% exit_code
			)
		)

func stop(force: bool = false) -> void:
	_stopping = true
	if force and _pid > 0 and OS.is_process_running(_pid):
		OS.kill(_pid)
	if force or not is_running():
		_cleanup_handles()

func is_running() -> bool:
	return _pid > 0 and OS.is_process_running(_pid)

func _fail_protocol(message: String) -> void:
	transport_failed.emit(
		AiServiceError.new(
			AiServiceError.Kind.PROTOCOL_ERROR,
			&"protocol_error",
			message
		)
	)
	stop(true)

func _fail_transport(message: String) -> void:
	transport_failed.emit(AiServiceError.unavailable(message))
	stop(true)

func _cleanup_handles() -> void:
	set_process(false)
	if _stdio != null:
		_stdio.close()
	if _stderr != null:
		_stderr.close()
	_stdio = null
	_stderr = null
	_pid = -1
	_read_buffer = ""
```

### 20.1 Paramètres de lancement

`OS.execute_with_pipe(path, arguments, blocking)` reçoit :

- `path` : chemin de l’exécutable ;
- `arguments` : `PackedStringArray` sans concaténation de commande shell ;
- `blocking` : `false` pour conserver une boucle Godot réactive.

Le dictionnaire de retour fournit `stdio`, `stderr` et `pid`.

### 20.2 Lecture non bloquante

`get_length()` sur un flux indique le nombre d’octets actuellement disponibles. `get_buffer(available)` lit seulement ces octets.

Le code conserve les caractères incomplets dans `_read_buffer`. Une ligne n’est émise qu’après réception de `\n`.

### 20.3 Limites

La limite s’applique au message sortant et au tampon entrant. Un service qui envoie une ligne sans fin provoque une erreur de protocole et l’arrêt du processus.

### 20.4 Sortie d’erreur

`stdout` est réservé au protocole. `stderr` reçoit les journaux humains. Mélanger les deux rendrait le flux JSON impossible à analyser.

### 20.5 Arrêt

La documentation Godot précise que le processus ne se termine pas automatiquement avec le jeu. Le bootstrap doit donc demander un arrêt au compagnon, puis utiliser `OS.kill()` seulement comme dernier recours.

## 21. Port applicatif

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/local_ai_gateway.gd`.

```gdscript
class_name LocalAiGateway
extends Node

signal status_changed(status: AiServiceStatus)

func start_service() -> Error:
	return ERR_UNAVAILABLE

func request(
	_operation: StringName,
	_payload: Dictionary,
	_timeout_ms: int = -1
) -> AiCallTicket:
	return null

func cancel(_request_id: StringName) -> Error:
	return ERR_UNAVAILABLE

func supports(_operation: StringName, _minimum_version: int = 1) -> bool:
	return false

func shutdown_service() -> void:
	pass

func current_status() -> AiServiceStatus:
	return AiServiceStatus.new()
```

Le port expose des opérations génériques parce que plusieurs fonctionnalités partageront le même compagnon. Les services de fonctionnalités construisent ensuite des méthodes plus explicites.

## 22. Générer les identifiants de corrélation

Un identifiant doit être unique pendant la vie du processus et lisible dans les diagnostics.

> **[VSC] Visual Studio Code — Ajouter :** dans `local_ai_gateway_service.gd`.

```gdscript
var _request_sequence := 0
var _session_prefix := ""

func _initialize_request_ids() -> void:
	var random := Crypto.new().generate_random_bytes(8).hex_encode()
	_session_prefix = "ai-%s" % random
	_request_sequence = 0

func _next_request_id() -> StringName:
	_request_sequence += 1
	return StringName(
		"%s-%08d" % [_session_prefix, _request_sequence]
	)
```

`Crypto.generate_random_bytes(8)` retourne huit octets aléatoires. `hex_encode()` les transforme en texte. Le compteur `%08d` est complété avec des zéros.

L’identifiant n’est pas un secret. Il sert uniquement à la corrélation et au diagnostic.

## 23. Orchestrateur du gateway

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/local_ai_gateway_service.gd`.

```gdscript
class_name LocalAiGatewayService
extends LocalAiGateway

const CAPABILITIES_OPERATION := &"capabilities.describe"
const CANCEL_OPERATION := &"system.cancel"
const SHUTDOWN_OPERATION := &"system.shutdown"

var _transport: AiTransport
var _config: AiServiceConfig
var _status := AiServiceStatus.new()
var _pending: Dictionary[StringName, AiCallTicket] = {}
var _capabilities: Dictionary[StringName, AiCapability] = {}
var _request_sequence := 0
var _session_prefix := ""

func configure(
	transport: AiTransport,
	config: AiServiceConfig
) -> void:
	_transport = transport
	_config = config

func start_service() -> Error:
	if _transport == null or _config == null:
		return ERR_UNCONFIGURED
	if not _config.validate().is_empty():
		return ERR_INVALID_DATA
	if not _config.enabled:
		_set_status(AiServiceStatus.State.DEGRADED, "Service désactivé.")
		return OK

	_initialize_request_ids()
	_connect_transport()
	_set_status(AiServiceStatus.State.STARTING, "Démarrage du compagnon.")
	var start_error := _transport.start()
	if start_error != OK:
		_set_status(AiServiceStatus.State.FAILED, error_string(start_error))
		return start_error

	set_process(true)
	var ticket := request(
		CAPABILITIES_OPERATION,
		{},
		_config.startup_timeout_ms
	)
	if ticket == null:
		_set_status(AiServiceStatus.State.FAILED, "Handshake impossible.")
		return ERR_CANT_CREATE
	ticket.completed.connect(_on_capabilities_completed)
	ticket.failed.connect(_on_capabilities_failed)
	return OK

func request(
	operation: StringName,
	payload: Dictionary,
	timeout_ms: int = -1
) -> AiCallTicket:
	if _transport == null or not _transport.is_running():
		return null
	if operation != CAPABILITIES_OPERATION and not supports(operation):
		return null

	var effective_timeout := (
		_config.request_timeout_ms if timeout_ms < 0 else timeout_ms
	)
	var request_id := _next_request_id()
	var request_value := AiRequest.new(
		request_id,
		operation,
		payload,
		effective_timeout
	)
	var line := AiEnvelopeCodec.encode_request(request_value)
	if line.is_empty():
		return null

	var deadline := Time.get_ticks_msec() + effective_timeout
	var ticket := AiCallTicket.new(request_id, operation, deadline)
	_pending[request_id] = ticket

	var send_error := _transport.send_line(line)
	if send_error != OK:
		_pending.erase(request_id)
		ticket.reject(AiServiceError.unavailable(error_string(send_error)))
	return ticket

func cancel(request_id: StringName) -> Error:
	if not _pending.has(request_id):
		return ERR_DOES_NOT_EXIST
	var ticket := _pending[request_id]
	_pending.erase(request_id)
	ticket.mark_cancelled(
		AiServiceError.new(
			AiServiceError.Kind.CANCELLED,
			&"cancelled",
			"Requête annulée par l’appelant."
		)
	)
	return _send_control(
		CANCEL_OPERATION,
		{"target_request_id": String(request_id)}
	)

func supports(operation: StringName, minimum_version: int = 1) -> bool:
	if operation == CAPABILITIES_OPERATION:
		return true
	if not _capabilities.has(operation):
		return false
	return _capabilities[operation].supports(minimum_version)

func shutdown_service() -> void:
	if _transport == null:
		return
	_set_status(AiServiceStatus.State.STOPPING, "Arrêt demandé.")
	if _transport.is_running():
		_send_control(SHUTDOWN_OPERATION, {})
	for request_id: StringName in _pending.keys():
		var ticket := _pending[request_id]
		ticket.reject(AiServiceError.unavailable("Service en cours d’arrêt."))
	_pending.clear()

func force_stop() -> void:
	if _transport != null:
		_transport.stop(true)
	_set_status(AiServiceStatus.State.STOPPED, "Arrêt forcé.")

func current_status() -> AiServiceStatus:
	return _status

func _process(_delta: float) -> void:
	var now := Time.get_ticks_msec()
	for request_id: StringName in _pending.keys():
		var ticket := _pending[request_id]
		if now < ticket.deadline_msec:
			continue
		_pending.erase(request_id)
		ticket.reject(
			AiServiceError.new(
				AiServiceError.Kind.TIMEOUT,
				&"timeout",
				"Délai dépassé pour %s." % ticket.operation,
				true
			)
		)
		_send_control(
			CANCEL_OPERATION,
			{"target_request_id": String(request_id)}
		)

func _connect_transport() -> void:
	if not _transport.line_received.is_connected(_on_line_received):
		_transport.line_received.connect(_on_line_received)
	if not _transport.transport_failed.is_connected(_on_transport_failed):
		_transport.transport_failed.connect(_on_transport_failed)
	if not _transport.transport_stopped.is_connected(_on_transport_stopped):
		_transport.transport_stopped.connect(_on_transport_stopped)

func _on_line_received(line: String) -> void:
	var response := AiEnvelopeCodec.decode_response(line)
	if response.request_id.is_empty():
		_on_transport_failed(
			response.error
			if response.error != null
			else AiServiceError.unavailable("Réponse sans request_id.")
		)
		return
	if not _pending.has(response.request_id):
		push_warning(
			"Réponse tardive ou inconnue : %s" % response.request_id
		)
		return

	var ticket := _pending[response.request_id]
	_pending.erase(response.request_id)
	if response.is_ok():
		ticket.resolve(response)
	else:
		ticket.reject(response.error)

func _on_transport_failed(error: AiServiceError) -> void:
	for request_id: StringName in _pending.keys():
		_pending[request_id].reject(error)
	_pending.clear()
	_set_status(AiServiceStatus.State.FAILED, error.message)

func _on_transport_stopped(exit_code: int) -> void:
	set_process(false)
	var state := (
		AiServiceStatus.State.STOPPED
		if _status.state == AiServiceStatus.State.STOPPING
		else AiServiceStatus.State.FAILED
	)
	_set_status(state, "Processus terminé : %d." % exit_code)

func _send_control(operation: StringName, payload: Dictionary) -> Error:
	if _transport == null or not _transport.is_running():
		return ERR_UNAVAILABLE
	var request_value := AiRequest.new(
		_next_request_id(),
		operation,
		payload,
		_config.shutdown_timeout_ms
	)
	var line := AiEnvelopeCodec.encode_request(request_value)
	return (
		ERR_INVALID_DATA
		if line.is_empty()
		else _transport.send_line(line)
	)

func _on_capabilities_completed(response: AiResponse) -> void:
	var load_errors := _load_capabilities(response.result)
	var unavailable := PackedStringArray()
	for operation: StringName in _capabilities.keys():
		if not _capabilities[operation].available:
			unavailable.append(String(operation))

	if not load_errors.is_empty():
		_set_status(
			AiServiceStatus.State.DEGRADED,
			"; ".join(load_errors)
		)
	elif not unavailable.is_empty():
		_set_status(
			AiServiceStatus.State.DEGRADED,
			"Capacités indisponibles : %s" % ", ".join(unavailable)
		)
	else:
		_set_status(AiServiceStatus.State.READY, "Capacités validées.")

func _on_capabilities_failed(error: AiServiceError) -> void:
	_set_status(AiServiceStatus.State.FAILED, error.message)
	if _transport != null and _transport.is_running():
		_transport.stop(true)

func _load_capabilities(result: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()
	if not result.get("operations", null) is Array:
		errors.append("operations doit être un tableau.")
		return errors

	_capabilities.clear()
	for value: Variant in result["operations"]:
		if not value is Dictionary:
			errors.append("Une capacité n’est pas un objet.")
			continue
		var data := value as Dictionary
		var operation := StringName(String(data.get("name", "")))
		var version := int(data.get("version", 0))
		var available := bool(data.get("available", false))
		if operation.is_empty() or version < 1:
			errors.append("Capacité invalide.")
			continue
		_capabilities[operation] = AiCapability.new(
			operation,
			version,
			available,
			data.get("limits", {}) as Dictionary
		)
	return errors

func _set_status(
	state: AiServiceStatus.State,
	message: String
) -> void:
	_status.set_state(state, message)
	status_changed.emit(_status)

func _initialize_request_ids() -> void:
	var random := Crypto.new().generate_random_bytes(8).hex_encode()
	_session_prefix = "ai-%s" % random
	_request_sequence = 0

func _next_request_id() -> StringName:
	_request_sequence += 1
	return StringName(
		"%s-%08d" % [_session_prefix, _request_sequence]
	)
```

### 23.1 Responsabilités

`start_service()` valide la configuration, démarre le transport et lance immédiatement un handshake de capacités.

`request()` retourne `AiCallTicket` ou `null` si le service ne peut pas accepter la demande. Une fonctionnalité doit traiter ce cas sans bloquer.

`_pending` associe un `StringName` à un ticket. L’accès `_pending[request_id]` retrouve l’appel exact.

`_process()` compare l’horloge monotone au délai de chaque ticket. Une expiration retire le ticket avant d’émettre l’erreur, ce qui empêche une réponse tardive de le résoudre ensuite.

### 23.2 Limite du contrôle d’arrêt

`shutdown_service()` envoie une demande mais ne force pas immédiatement le processus. Le bootstrap doit accorder `shutdown_timeout_ms`, puis appeler `force_stop()` si le processus reste actif.

### 23.3 Réponse tardive

Une réponse reçue après délai ou annulation est ignorée avec un avertissement. Elle ne doit jamais être appliquée à un nouveau ticket.

## 24. Protocole Python

Le compagnon doit valider les mêmes formats sans importer Godot.

> **[VSC] Visual Studio Code — Créer :** `tools/ai/companion_protocol.py`.

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

REQUEST_FORMAT = "project-asteria-ai-request"
RESPONSE_FORMAT = "project-asteria-ai-response"
FORMAT_VERSION = 1
MAX_MESSAGE_CHARS = 1_048_576


@dataclass(frozen=True, slots=True)
class ProtocolRequest:
    request_id: str
    operation: str
    timeout_ms: int
    payload: dict[str, Any]


class ProtocolError(ValueError):
    def __init__(
        self,
        code: str,
        message: str,
        *,
        retryable: bool = False,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.retryable = retryable
        self.details = details or {}


def require_text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ProtocolError("invalid_request", f"{key} doit être une chaîne non vide.")
    return value.strip()


def parse_request(data: Any) -> ProtocolRequest:
    if not isinstance(data, dict):
        raise ProtocolError("protocol_error", "La requête doit être un objet.")
    if data.get("format") != REQUEST_FORMAT:
        raise ProtocolError("protocol_error", "Format de requête inconnu.")
    if data.get("format_version") != FORMAT_VERSION:
        raise ProtocolError("protocol_error", "Version de protocole incompatible.")

    request_id = require_text(data, "request_id")
    operation = require_text(data, "operation")
    timeout_ms = data.get("timeout_ms")
    if not isinstance(timeout_ms, int) or not 100 <= timeout_ms <= 300_000:
        raise ProtocolError("invalid_request", "timeout_ms est invalide.")

    payload = data.get("payload")
    if not isinstance(payload, dict):
        raise ProtocolError("invalid_request", "payload doit être un objet.")
    if len(payload) > 64:
        raise ProtocolError("invalid_request", "payload contient trop de clés.")

    return ProtocolRequest(request_id, operation, timeout_ms, dict(payload))


def ok_response(request_id: str, result: dict[str, Any]) -> dict[str, Any]:
    return {
        "format": RESPONSE_FORMAT,
        "format_version": FORMAT_VERSION,
        "request_id": request_id,
        "status": "ok",
        "result": result,
    }


def error_response(
    request_id: str,
    error: ProtocolError,
) -> dict[str, Any]:
    return {
        "format": RESPONSE_FORMAT,
        "format_version": FORMAT_VERSION,
        "request_id": request_id,
        "status": "error",
        "error": {
            "code": error.code,
            "message": str(error),
            "retryable": error.retryable,
            "details": error.details,
        },
    }
```

### 24.1 Explication

`ProtocolRequest` est une dataclass immuable. `Any` apparaît uniquement avant validation.

`ProtocolError` ajoute un code stable, un indicateur `retryable` et des détails. `super().__init__(message)` initialise le message standard de `ValueError`.

`parse_request()` transforme une valeur JSON non fiable en objet typé. Le retour n’est produit qu’après validation complète.

## 25. Port Python vers la connaissance

Le compagnon dépend d’un port minimal. L’implémentation réelle adapte `RetrievalService` du chapitre 10 sans en recopier les responsabilités.

> **[VSC] Visual Studio Code — Créer :** `tools/ai/knowledge_service_adapter.py`.

```python
from __future__ import annotations

from typing import Any, Protocol


class KnowledgeSearchPort(Protocol):
    def search(
        self,
        query: str,
        allowed_visibility: set[str],
        language: str | None,
        required_tags: set[str],
        limit: int,
    ) -> list[Any]: ...


class KnowledgeServiceAdapter:
    def __init__(self, retrieval: KnowledgeSearchPort) -> None:
        self._retrieval = retrieval

    def search(self, payload: dict[str, Any]) -> dict[str, Any]:
        query = payload.get("query")
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query doit être une chaîne non vide.")
        if len(query) > 2_000:
            raise ValueError("query dépasse 2 000 caractères.")

        visibility_value = payload.get("allowed_visibility")
        if not isinstance(visibility_value, list) or not visibility_value:
            raise ValueError("allowed_visibility doit être un tableau non vide.")
        allowed_visibility = {
            value
            for value in visibility_value
            if isinstance(value, str) and value in {"public", "internal", "restricted"}
        }
        if len(allowed_visibility) != len(visibility_value):
            raise ValueError("Une visibilité est invalide.")

        language = payload.get("language")
        if language is not None and not isinstance(language, str):
            raise ValueError("language doit être une chaîne ou null.")

        tags_value = payload.get("required_tags", [])
        if not isinstance(tags_value, list):
            raise ValueError("required_tags doit être un tableau.")
        required_tags = {
            value.strip().lower()
            for value in tags_value
            if isinstance(value, str) and value.strip()
        }
        if len(required_tags) != len(tags_value):
            raise ValueError("Un tag est invalide.")

        limit = payload.get("limit", 5)
        if not isinstance(limit, int) or not 1 <= limit <= 20:
            raise ValueError("limit doit rester entre 1 et 20.")

        hits = self._retrieval.search(
            query.strip(),
            allowed_visibility,
            language,
            required_tags,
            limit,
        )
        return {
            "retrieval_mode": hits[0].retrieval_mode if hits else "none",
            "hits": [
                {
                    "chunk_id": hit.chunk_id,
                    "source_id": hit.source_id,
                    "source_path": hit.source_path,
                    "text": hit.text,
                    "score": hit.score,
                    "metadata": hit.metadata,
                }
                for hit in hits
            ],
        }
```

### 25.1 Explication

`KnowledgeSearchPort` décrit la méthode déjà fournie par le service de récupération du chapitre 10.

L’adaptateur valide chaque champ du payload. Il transforme ensuite les objets `KnowledgeHit` en dictionnaires JSON simples.

La visibilité reçue doit déjà provenir de la politique Godot. Cette validation empêche seulement des valeurs inconnues ; le durcissement d’identité et d’autorisation appartient au chapitre 13.

## 26. Processus compagnon

> **[VSC] Visual Studio Code — Créer :** `tools/ai/companion_service.py`.

```python
from __future__ import annotations

import json
import sys
from collections.abc import Callable
from typing import Any

from companion_protocol import (
    MAX_MESSAGE_CHARS,
    ProtocolError,
    ProtocolRequest,
    error_response,
    ok_response,
    parse_request,
)


class CompanionApplication:
    def __init__(self, knowledge_adapter: Any | None) -> None:
        self._knowledge = knowledge_adapter
        self._running = True
        self._cancelled: set[str] = set()
        self._handlers: dict[str, Callable[[ProtocolRequest], dict[str, Any]]] = {
            "capabilities.describe": self._describe_capabilities,
            "health.check": self._health_check,
            "knowledge.search": self._knowledge_search,
            "system.cancel": self._cancel,
            "system.shutdown": self._shutdown,
        }

    @property
    def running(self) -> bool:
        return self._running

    def dispatch(self, request: ProtocolRequest) -> dict[str, Any]:
        handler = self._handlers.get(request.operation)
        if handler is None:
            raise ProtocolError(
                "unsupported_capability",
                f"Opération inconnue : {request.operation}",
            )
        if request.request_id in self._cancelled:
            raise ProtocolError("cancelled", "Requête annulée.")
        result = handler(request)
        if request.request_id in self._cancelled:
            raise ProtocolError("cancelled", "Requête annulée.")
        return result

    def _describe_capabilities(
        self,
        _request: ProtocolRequest,
    ) -> dict[str, Any]:
        knowledge_available = self._knowledge is not None
        return {
            "service": "project-asteria-ai-companion",
            "protocol_version": 1,
            "operations": [
                {
                    "name": "health.check",
                    "version": 1,
                    "available": True,
                    "limits": {},
                },
                {
                    "name": "knowledge.search",
                    "version": 1,
                    "available": knowledge_available,
                    "limits": {
                        "max_query_chars": 2000,
                        "max_results": 20,
                    },
                },
            ],
        }

    def _health_check(self, _request: ProtocolRequest) -> dict[str, Any]:
        return {"status": "ready"}

    def _knowledge_search(self, request: ProtocolRequest) -> dict[str, Any]:
        if self._knowledge is None:
            raise ProtocolError(
                "unavailable",
                "Le service de connaissance n’est pas initialisé.",
                retryable=True,
            )
        try:
            return self._knowledge.search(request.payload)
        except ValueError as exc:
            raise ProtocolError("invalid_request", str(exc)) from exc
        except (OSError, RuntimeError) as exc:
            raise ProtocolError(
                "unavailable",
                str(exc),
                retryable=True,
            ) from exc

    def _cancel(self, request: ProtocolRequest) -> dict[str, Any]:
        target = request.payload.get("target_request_id")
        if not isinstance(target, str) or not target:
            raise ProtocolError(
                "invalid_request",
                "target_request_id est obligatoire.",
            )
        self._cancelled.add(target)
        return {"cancelled_request_id": target}

    def _shutdown(self, _request: ProtocolRequest) -> dict[str, Any]:
        self._running = False
        return {"accepted": True}


def write_message(value: dict[str, Any]) -> None:
    text = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    )
    print(text, flush=True)


def run(application: CompanionApplication) -> int:
    while application.running:
        raw_line = sys.stdin.readline()
        if raw_line == "":
            break
        line = raw_line.rstrip("\r\n")
        if not line:
            continue

        request_id = ""
        try:
            if len(line) > MAX_MESSAGE_CHARS:
                raise ProtocolError("protocol_error", "Message trop volumineux.")
            decoded = json.loads(line)
            if isinstance(decoded, dict):
                raw_id = decoded.get("request_id")
                request_id = raw_id if isinstance(raw_id, str) else ""
            request = parse_request(decoded)
            request_id = request.request_id
            result = application.dispatch(request)
            write_message(ok_response(request.request_id, result))
        except ProtocolError as exc:
            write_message(error_response(request_id, exc))
        except json.JSONDecodeError as exc:
            write_message(error_response(
                request_id,
                ProtocolError(
                    "protocol_error",
                    f"JSON invalide : {exc.msg}",
                ),
            ))
        except Exception as exc:
            print(
                f"Erreur interne non gérée : {type(exc).__name__}: {exc}",
                file=sys.stderr,
                flush=True,
            )
            write_message(error_response(
                request_id,
                ProtocolError(
                    "internal_error",
                    "Erreur interne du compagnon.",
                    retryable=False,
                ),
            ))
    return 0


def build_application() -> CompanionApplication:
    # Le Starter Kit injectera ici le RetrievalService du chapitre 10.
    return CompanionApplication(knowledge_adapter=None)


if __name__ == "__main__":
    raise SystemExit(run(build_application()))
```

### 26.1 Entrée et sortie

`for raw_line in sys.stdin` lit une ligne à la fois. `rstrip("\r\n")` retire uniquement les fins de ligne.

`write_message()` utilise `allow_nan=False`. Les valeurs non JSON comme `NaN` provoquent donc une erreur au lieu de contaminer le protocole.

`print(..., flush=True)` rend immédiatement la réponse disponible pour Godot.

### 26.2 Journaux

Les erreurs humaines utilisent `file=sys.stderr`. Aucune ligne de journal ne doit être écrite sur stdout.

### 26.3 Distribution

`_handlers` associe une chaîne d’opération à une fonction. `Callable[[ProtocolRequest], dict[str, Any]]` décrit son paramètre et son retour.

### 26.4 Annulation coopérative

Le compagnon séquentiel peut vérifier l’annulation avant et après un handler. Il ne peut pas lire une nouvelle ligne pendant une opération Python bloquante.

La vraie file de tâches, les workers et l’annulation d’un job en cours appartiennent au chapitre 12. Le présent contrat prépare cette évolution sans la simuler.

## 27. Découverte des capacités

Le gateway ne passe à `READY` qu’après une réponse valide à `capabilities.describe`.

Une capacité doit fournir :

- `name` ;
- `version` ;
- `available` ;
- `limits`.

La disponibilité globale du processus ne suffit pas. Un compagnon peut répondre à `health.check` tout en déclarant `knowledge.search` indisponible parce que le modèle n’est pas présent.

> **[LECTURE] Exemple de capacité partielle — Ne pas saisir.**

```json
{
  "name": "knowledge.search",
  "version": 1,
  "available": false,
  "limits": {
    "max_query_chars": 2000,
    "max_results": 20
  }
}
```

Le jeu peut alors activer son repli sans traiter cette situation comme un crash.

## 28. Délai et horloge monotone

Le délai local est calculé ainsi :

> **[LECTURE] Calcul de durée — Ne pas saisir.**

```gdscript
var deadline_msec := Time.get_ticks_msec() + timeout_ms
```

`Time.get_ticks_msec()` augmente de manière monotone. Une modification de l’horloge système ne raccourcit ni n’allonge artificiellement le délai.

Le gateway retire le ticket à expiration, émet `TIMEOUT`, puis envoie une annulation coopérative. Une réponse tardive reste diagnostiquée mais ignorée.

## 29. Service de fonctionnalité

Le gameplay ne doit pas appeler `knowledge.search` avec des dictionnaires dispersés. Une façade de fonctionnalité traduit une intention métier.

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/application/beacon_knowledge_service.gd`.

```gdscript
class_name BeaconKnowledgeService
extends RefCounted

signal answer_ready(answer: Dictionary)
signal answer_failed(error: AiServiceError)

var _gateway: LocalAiGateway
var _fallback: BeaconKnowledgeFallback

func configure(
	gateway: LocalAiGateway,
	fallback: BeaconKnowledgeFallback
) -> void:
	_gateway = gateway
	_fallback = fallback

func ask_about_beacon(
	query: String,
	allowed_visibility: PackedStringArray
) -> void:
	var clean_query := query.strip_edges()
	if clean_query.is_empty():
		answer_failed.emit(
			AiServiceError.new(
				AiServiceError.Kind.INVALID_REQUEST,
				&"invalid_request",
				"La question est vide."
			)
		)
		return

	if (
		_gateway == null
		or not _gateway.supports(&"knowledge.search")
	):
		answer_ready.emit(_fallback.answer(clean_query))
		return

	var payload := {
		"query": clean_query,
		"allowed_visibility": Array(allowed_visibility),
		"language": "fr",
		"required_tags": ["beacon"],
		"limit": 5,
	}
	var ticket := _gateway.request(&"knowledge.search", payload)
	if ticket == null:
		answer_ready.emit(_fallback.answer(clean_query))
		return

	ticket.completed.connect(_on_completed)
	ticket.failed.connect(
		func(error: AiServiceError) -> void:
			if _can_fallback(error):
				answer_ready.emit(_fallback.answer(clean_query))
			else:
				answer_failed.emit(error)
	)

func _on_completed(response: AiResponse) -> void:
	var validation_errors := _validate_result(response.result)
	if not validation_errors.is_empty():
		answer_failed.emit(
			AiServiceError.new(
				AiServiceError.Kind.PROTOCOL_ERROR,
				&"invalid_result",
				"; ".join(validation_errors)
			)
		)
		return
	answer_ready.emit(response.result)

func _can_fallback(error: AiServiceError) -> bool:
	return error.kind in [
		AiServiceError.Kind.UNAVAILABLE,
		AiServiceError.Kind.TIMEOUT,
		AiServiceError.Kind.UNSUPPORTED_CAPABILITY,
	]

func _validate_result(result: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()
	if not result.get("retrieval_mode", null) is String:
		errors.append("retrieval_mode doit être une chaîne.")
	if not result.get("hits", null) is Array:
		errors.append("hits doit être un tableau.")
	return errors
```

### 29.1 Explication

`ask_about_beacon()` retourne `void` parce que le résultat arrive plus tard par signal.

`allowed_visibility` est fourni par une politique en amont. Le service ne l’obtient jamais d’un texte libre du joueur.

La lambda passée à `ticket.failed.connect()` capture `clean_query`. Elle applique le repli seulement pour trois erreurs techniques prévues.

Une erreur `INVALID_REQUEST`, `PROTOCOL_ERROR` ou `INTERNAL_ERROR` n’est pas masquée par le repli.

## 30. Repli des balises

Le repli utilise des données validées du projet. Il ne fabrique pas une réponse pseudo-intelligente.

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/infrastructure/beacon_knowledge_fallback.gd`.

```gdscript
class_name BeaconKnowledgeFallback
extends RefCounted

var _catalog: Dictionary[StringName, Dictionary]

func configure(
	catalog: Dictionary[StringName, Dictionary]
) -> void:
	_catalog = catalog.duplicate(true)

func answer(query: String) -> Dictionary:
	var terms := query.to_lower().split(" ", false)
	var matches: Array[Dictionary] = []

	for beacon_id: StringName in _catalog.keys():
		var entry := _catalog[beacon_id]
		var searchable := (
			String(entry.get("title", ""))
			+ " "
			+ String(entry.get("summary", ""))
		).to_lower()
		var score := 0
		for term: String in terms:
			if term.length() >= 3 and searchable.contains(term):
				score += 1
		if score > 0:
			matches.append({
				"source_id": String(beacon_id),
				"title": String(entry.get("title", "")),
				"text": String(entry.get("summary", "")),
				"score": float(score),
			})

	matches.sort_custom(
		func(a: Dictionary, b: Dictionary) -> bool:
			if float(a["score"]) == float(b["score"]):
				return String(a["source_id"]) < String(b["source_id"])
			return float(a["score"]) > float(b["score"])
	)

	return {
		"retrieval_mode": "deterministic_fallback",
		"hits": matches.slice(0, 5),
	}
```

### 30.1 Explication

Le repli reçoit un catalogue injecté. Il n’accède pas à Qdrant et ne démarre aucun modèle.

`split(" ", false)` produit les termes non vides. Les termes de moins de trois caractères sont ignorés pour limiter les correspondances triviales.

`sort_custom()` classe par score décroissant puis par identifiant. Ce second critère garantit un ordre stable.

`slice(0, 5)` limite le résultat à cinq entrées.

## 31. Bootstrap

Le bootstrap construit les objets dans l’ordre de dépendance.

> **[VSC] Visual Studio Code — Créer :** `res://src/app/ai_bootstrap.gd`.

```gdscript
class_name AiBootstrap
extends RefCounted

func build_gateway(config: AiServiceConfig) -> LocalAiGatewayService:
	var transport := StdioCompanionTransport.new()
	transport.configure(
		ProjectSettings.globalize_path(config.python_executable),
		ProjectSettings.globalize_path(config.companion_script),
		config.max_message_bytes
	)

	var gateway := LocalAiGatewayService.new()
	gateway.configure(transport, config)
	gateway.add_child(transport)
	return gateway

func build_beacon_service(
	gateway: LocalAiGateway,
	beacon_catalog: Dictionary[StringName, Dictionary]
) -> BeaconKnowledgeService:
	var fallback := BeaconKnowledgeFallback.new()
	fallback.configure(beacon_catalog)

	var service := BeaconKnowledgeService.new()
	service.configure(gateway, fallback)
	return service
```

### 31.1 Explication

`build_gateway()` retourne un service configuré, mais ne le démarre pas. Le point de composition décide quand l’ajouter à l’arbre et appeler `start_service()`.

`ProjectSettings.globalize_path()` transforme un chemin Godot en chemin utilisable par le système d’exploitation.

Le transport devient enfant du gateway pour recevoir `_process()`. Le gateway doit lui-même être ajouté à l’arbre principal par le bootstrap d’application.

Aucune scène de gameplay ne construit l’exécutable Python ou le transport.

## 32. Démarrage et arrêt dans l’application

> **[VSC] Visual Studio Code — Ajouter :** dans le bootstrap principal de l’application.

```gdscript
var _ai_gateway: LocalAiGatewayService
var _shutdown_deadline_msec := -1

func start_ai(config: AiServiceConfig) -> Error:
	_ai_gateway = AiBootstrap.new().build_gateway(config)
	add_child(_ai_gateway)
	return _ai_gateway.start_service()

func begin_ai_shutdown(config: AiServiceConfig) -> void:
	if _ai_gateway == null:
		return
	_ai_gateway.shutdown_service()
	_shutdown_deadline_msec = (
		Time.get_ticks_msec() + config.shutdown_timeout_ms
	)

func poll_ai_shutdown() -> bool:
	if _ai_gateway == null:
		return true
	if (
		_ai_gateway.current_status().state
		== AiServiceStatus.State.STOPPED
	):
		return true
	if (
		_shutdown_deadline_msec >= 0
		and Time.get_ticks_msec() >= _shutdown_deadline_msec
	):
		_ai_gateway.force_stop()
		return true
	return false
```

`begin_ai_shutdown()` lance un arrêt coopératif. `poll_ai_shutdown()` retourne `true` lorsque le processus est terminé ou a dû être forcé.

L’arrêt général du chapitre 5 doit appeler les services dans l’ordre inverse du démarrage.

## 33. Scène de démonstration

> **[VSC] Visual Studio Code — Créer :** `res://scenes/learning/ch11_local_ai_demo.gd`.

```gdscript
class_name Chapter11LocalAiDemo
extends Node

var _knowledge: BeaconKnowledgeService

func configure(service: BeaconKnowledgeService) -> void:
	_knowledge = service

func _ready() -> void:
	if _knowledge == null:
		push_error("BeaconKnowledgeService absent.")
		return

	_knowledge.answer_ready.connect(_on_answer_ready)
	_knowledge.answer_failed.connect(_on_answer_failed)
	_knowledge.ask_about_beacon(
		"Comment ouvrir la porte nord ?",
		PackedStringArray(["internal"])
	)

func _on_answer_ready(answer: Dictionary) -> void:
	var mode := String(answer.get("retrieval_mode", "unknown"))
	var hits := answer.get("hits", []) as Array
	print("Mode de récupération : %s" % mode)
	print("Nombre de résultats : %d" % hits.size())

func _on_answer_failed(error: AiServiceError) -> void:
	push_error(
		"Recherche impossible [%s] : %s"
		% [error.code, error.message]
	)
```

### 33.1 Résultat attendu

Lorsque le compagnon et la capacité sont disponibles, `retrieval_mode` vaut `vector` ou `lexical` selon le service du chapitre 10.

Lorsque le compagnon est absent ou dépasse son délai, la fonctionnalité retourne `deterministic_fallback`.

> **[SORTIE] Godot — Exemple documentaire :**

```text
Mode de récupération : deterministic_fallback
Nombre de résultats : 1
```

Cette sortie est illustrative. La scène, le compagnon et l’environnement n’ont pas été exécutés pendant l’audit.

## 34. Disponibilité selon la plateforme

### 34.1 Windows, Linux et macOS

Le processus compagnon est une option valide lorsque l’export cible permet de lancer un exécutable local et que les fichiers nécessaires sont distribués.

### 34.2 Web

Un export Web ne doit pas dépendre de `OS.execute_with_pipe()`. Le bootstrap désactive le compagnon et injecte le repli déterministe.

### 34.3 Mobile

Le chapitre ne qualifie pas la distribution d’un runtime Python sur mobile. Le chemin de référence y reste désactivé jusqu’à une décision d’architecture et des essais réels.

### 34.4 Éditeur

Dans l’éditeur, les chemins peuvent pointer vers l’environnement local du développeur. Un export final ne doit pas supposer que cet environnement existe sur la machine du joueur.

## 35. Confidentialité et limites minimales

Le transport local ne rend pas automatiquement le système sûr.

Règles du chapitre :

- chemins d’exécutables issus de la configuration de confiance ;
- aucun assemblage de commande shell ;
- aucun argument fourni directement par le joueur ;
- taille maximale des messages ;
- format et version obligatoires ;
- opérations sur liste fermée ;
- stdout réservé au protocole ;
- résultats validés avant usage ;
- visibilités calculées par la politique du jeu ;
- aucun secret dans les messages par défaut ;
- aucun accès direct de Godot au dossier Qdrant ;
- arrêt explicite du processus.

L’authentification réseau, les secrets et le sandboxing restent au chapitre 13.

## 36. Diagnostic

### 36.1 Le processus ne démarre pas

Vérifier :

- `enabled` ;
- le chemin globalisé de Python ;
- le chemin globalisé du script ;
- les permissions d’exécution ;
- l’existence de l’environnement ;
- le code d’erreur retourné par `start_service()`.

### 36.2 Le service reste en `STARTING`

Le handshake `capabilities.describe` n’a pas répondu. Vérifier :

- que stdout contient uniquement du JSON ;
- que chaque réponse se termine par `\n` ;
- que le compagnon appelle `flush=True` ;
- que le `request_id` est recopié ;
- que le délai de démarrage est suffisant.

### 36.3 Réponse inconnue

Une réponse inconnue peut être :

- tardive après un timeout ;
- tardive après annulation ;
- dupliquée ;
- corrélée avec un identifiant erroné.

Elle doit être journalisée puis ignorée.

### 36.4 Tampon trop volumineux

Le compagnon a envoyé une ligne trop longue ou sans séparateur. Arrêter le transport et corriger le protocole. Ne pas augmenter la limite sans analyser le payload.

### 36.5 Processus orphelin

Vérifier que l’arrêt de l’application appelle `shutdown_service()`, attend le délai, puis utilise `force_stop()` si nécessaire.

### 36.6 Repli jamais utilisé

Contrôler que la fonctionnalité accepte les erreurs `UNAVAILABLE`, `TIMEOUT` et `UNSUPPORTED_CAPABILITY`, sans intercepter les erreurs de contrat.

## 37. Erreurs fréquentes, pièges et corrections

<!-- qa:error-correction-section -->

### 37.1 Bloquer la boucle principale avec un processus synchrone

**Symptôme :** l’image se fige pendant le chargement du modèle ou la recherche.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
OS.execute(python_path, arguments, output, true)
```

**Correction :** utiliser un processus avec flux non bloquants et le sonder depuis `_process()`.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var pipes := OS.execute_with_pipe(python_path, arguments, false)
```

**Différence :** le jeu continue à traiter les images et les entrées pendant que le compagnon travaille.

### 37.2 Exposer le transport dans le gameplay

**Symptôme :** une scène construit des lignes JSON et dépend de `FileAccess`.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
stdio.store_line(JSON.stringify({"operation": "knowledge.search"}))
```

**Correction :** appeler un service de fonctionnalité derrière `LocalAiGateway`.

> **[LECTURE] Architecture corrigée — Référence.**

```text
scène → BeaconKnowledgeService → LocalAiGateway → transport
```

**Différence :** la scène exprime une intention métier et reste indépendante de la technologie de communication.

### 37.3 Lire directement le stockage Qdrant depuis Godot

**Symptôme :** le jeu dépend de fichiers internes dont le format peut changer.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var file := FileAccess.open("var/knowledge/qdrant/collection.bin", FileAccess.READ)
```

**Correction :** interroger le port applicatif.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var ticket := gateway.request(&"knowledge.search", payload)
```

**Différence :** l’index reste encapsulé et reconstructible derrière le service du chapitre 10.

### 37.4 Lancer une commande construite depuis une saisie

**Symptôme :** le joueur peut modifier le chemin ou ajouter des arguments.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var command := user_text + " " + script_path
OS.execute(command, PackedStringArray())
```

**Correction :** utiliser un exécutable et une liste d’arguments issus de la configuration fiable.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
OS.execute_with_pipe(
	configured_python,
	PackedStringArray([configured_script]),
	false
)
```

**Différence :** aucun shell ni texte contrôlé par le joueur ne construit la commande.

### 37.5 Écrire des journaux sur stdout

**Symptôme :** Godot tente d’analyser `Model loaded` comme du JSON.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
print("Model loaded")
print(json.dumps(response))
```

**Correction :** réserver stdout au protocole et envoyer les journaux sur stderr.

> **[LECTURE] Exemple corrigé — Référence.**

```python
print("Model loaded", file=sys.stderr, flush=True)
print(json.dumps(response), flush=True)
```

**Différence :** chaque ligne stdout reste une enveloppe JSON interprétable.

### 37.6 Lire une ligne incomplète comme un message complet

**Symptôme :** les gros messages provoquent des erreurs JSON intermittentes.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var text := stdio.get_buffer(stdio.get_length()).get_string_from_utf8()
decode_response(text)
```

**Correction :** accumuler les octets et émettre seulement les lignes terminées.

> **[LECTURE] Flux corrigé — Référence.**

```text
octets disponibles → tampon → recherche de "\n" → ligne complète
```

**Différence :** une lecture partielle reste en attente au lieu d’être analysée prématurément.

### 37.7 Laisser le tampon grandir sans limite

**Symptôme :** un compagnon défectueux consomme toute la mémoire.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
read_buffer += incoming_text
```

**Correction :** vérifier la taille cumulée avant l’ajout.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if read_buffer.to_utf8_buffer().size() + incoming_bytes > max_message_bytes:
	stop_transport()
```

**Différence :** une ligne absente ou excessive devient une erreur bornée.

### 37.8 Réutiliser un identifiant de corrélation

**Symptôme :** une réponse résout le mauvais ticket.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var request_id := &"knowledge-search"
```

**Correction :** combiner un préfixe de session et un compteur monotone.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var request_id := StringName("%s-%08d" % [session_prefix, sequence])
```

**Différence :** deux requêtes simultanées ne partagent jamais la même clé dans `_pending`.

### 37.9 Appliquer une réponse tardive

**Symptôme :** un résultat annulé modifie l’interface plusieurs secondes plus tard.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ticket.resolve(response)
```

**Correction :** vérifier que le `request_id` est encore présent dans le registre.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if pending.has(response.request_id):
	pending[response.request_id].resolve(response)
```

**Différence :** un timeout ou une annulation retire l’autorité de la réponse tardive.

### 37.10 Présenter le timeout comme une interruption garantie

**Symptôme :** la documentation affirme que le modèle s’arrête à la milliseconde exacte.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Après 2 500 ms, le calcul Python est forcément interrompu.
```

**Correction :** distinguer abandon local et annulation coopérative.

> **[LECTURE] Formulation corrigée — Référence.**

```text
Godot abandonne l’attente à 2 500 ms et envoie une demande d’annulation.
Le service peut terminer plus tard si l’opération n’est pas interruptible.
```

**Différence :** le contrat réel ne promet pas une propriété impossible à garantir pour toute bibliothèque.

### 37.11 Masquer toutes les erreurs par le repli

**Symptôme :** une réponse de protocole corrompue devient silencieusement un résultat local.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ticket.failed.connect(func(_error): use_fallback())
```

**Correction :** limiter le repli aux indisponibilités prévues.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if error.kind in [
	AiServiceError.Kind.UNAVAILABLE,
	AiServiceError.Kind.TIMEOUT,
	AiServiceError.Kind.UNSUPPORTED_CAPABILITY,
]:
	use_fallback()
else:
	report_error(error)
```

**Différence :** les erreurs de contrat et de programmation restent visibles.

### 37.12 Rendre l’IA obligatoire pour une fonction essentielle

**Symptôme :** une porte de quête ne peut plus s’ouvrir lorsque Python est absent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if not ai_gateway.supports(&"knowledge.search"):
	return ERR_CANT_ACQUIRE_RESOURCE
```

**Correction :** conserver l’autorité du gameplay et utiliser l’IA comme enrichissement.

> **[LECTURE] Architecture corrigée — Référence.**

```text
règle de gameplay déterministe → décision
service IA facultatif → explication, recherche ou confort
```

**Différence :** la progression du jeu ne dépend pas d’un service auxiliaire.

### 37.13 Oublier d’arrêter le processus compagnon

**Symptôme :** `python.exe` reste actif après la fermeture du jeu.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func _exit_tree() -> void:
	pass
```

**Correction :** demander l’arrêt, attendre un délai puis forcer si nécessaire.

> **[LECTURE] Flux corrigé — Référence.**

```text
system.shutdown → délai monotone → sortie normale
                               ↘ OS.kill() en dernier recours
```

**Différence :** le cycle de vie du processus suit celui de l’application.

### 37.14 Supposer les capacités sans handshake

**Symptôme :** le jeu appelle `knowledge.search` alors que le modèle est absent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var service_ready := transport.is_running()
```

**Correction :** valider `capabilities.describe` avant le passage à `READY`.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if capability_registry.supports(&"knowledge.search"):
	start_search()
else:
	use_fallback()
```

**Différence :** un processus vivant n’est plus confondu avec une capacité opérationnelle.

### 37.15 Coupler le port applicatif à HTTP

**Symptôme :** toutes les fonctionnalités dépendent déjà d’URL et de codes de statut.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func post_json(url: String, body: Dictionary) -> HTTPRequest:
	return HTTPRequest.new()
```

**Correction :** garder un port exprimé en opérations et résultats métier.

> **[LECTURE] Architecture corrigée — Référence.**

```text
LocalAiGateway.request(operation, payload)
       ↓
adaptateur stdio aujourd’hui
adaptateur HTTP ou WebSocket au chapitre 12
```

**Différence :** le transport futur peut changer sans réécrire les services de fonctionnalités.

### 37.16 Confondre arrêt coopératif et kill immédiat

**Symptôme :** le processus est tué avant d’avoir fermé ses ressources.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
OS.kill(pid)
```

**Correction :** réserver le kill à l’expiration du délai d’arrêt.

> **[LECTURE] Flux corrigé — Référence.**

```text
demande system.shutdown → attendre process exit
                         → kill seulement après timeout
```

**Différence :** le compagnon reçoit d’abord la possibilité de libérer proprement ses ressources.

## 38. Parcours Solo

Le parcours Solo retient :

- un seul processus compagnon ;
- transport JSON par lignes sur stdio ;
- un handshake de capacités ;
- une limite de message ;
- un timeout par requête ;
- un repli déterministe par fonctionnalité ;
- un arrêt coopératif puis forcé ;
- aucun serveur réseau obligatoire.

Le développeur peut désactiver le service dans `AppConfig` et vérifier que toutes les fonctions essentielles restent utilisables.

## 39. Parcours Studio

Le parcours Studio ajoute :

- propriétaire du protocole ;
- registre des opérations et versions ;
- matrice plateforme × capacité ;
- journal de corrélation ;
- tests de messages fragmentés ;
- tests de réponses tardives ;
- tests de crash du compagnon ;
- politique de timeout par opération ;
- budget de taille ;
- packaging reproductible ;
- suivi des processus orphelins ;
- procédure de rollback du compagnon ;
- préparation des transports du chapitre 12 ;
- revue sécurité du chapitre 13.

## 40. Critères d’acceptation

Le chapitre est compris lorsque le lecteur peut montrer que :

- Godot ne lit pas Qdrant directement ;
- le port applicatif ne dépend pas de HTTP ;
- chaque requête possède un identifiant unique ;
- chaque réponse reprend le même identifiant ;
- les messages sont versionnés ;
- stdout ne contient que le protocole ;
- stderr contient les journaux ;
- les lectures partielles sont mises en tampon ;
- la taille des messages est bornée ;
- le handshake précède l’état `READY` ;
- les délais utilisent `Time.get_ticks_msec()` ;
- une réponse tardive est ignorée ;
- l’annulation est décrite comme coopérative ;
- le repli ne masque pas les erreurs de contrat ;
- le processus est arrêté explicitement ;
- le gameplay essentiel reste déterministe ;
- aucun test runtime non exécuté n’est revendiqué.

## 41. Checklist Solo

- [ ] Ajouter `AiServiceConfig`.
- [ ] Créer les objets requête, réponse, erreur et capacité.
- [ ] Créer `AiCallTicket`.
- [ ] Ajouter le codec versionné.
- [ ] Créer le port `AiTransport`.
- [ ] Créer le transport stdio non bloquant.
- [ ] Créer le port `LocalAiGateway`.
- [ ] Ajouter le registre de corrélation.
- [ ] Ajouter le handshake de capacités.
- [ ] Ajouter les délais monotones.
- [ ] Ajouter l’annulation coopérative.
- [ ] Créer le compagnon Python.
- [ ] Injecter le repli de la fonctionnalité.
- [ ] Ajouter l’arrêt contrôlé.
- [ ] Vérifier le mode service désactivé.

## 42. Checklist Studio

- [ ] Versionner le protocole et chaque opération.
- [ ] Définir les limites par capacité.
- [ ] Conserver des fixtures de requêtes et réponses.
- [ ] Tester les fragments de lignes.
- [ ] Tester les messages trop volumineux.
- [ ] Tester les timeouts et réponses tardives.
- [ ] Tester le crash du processus.
- [ ] Tester l’arrêt normal et forcé.
- [ ] Qualifier les plateformes.
- [ ] Inventorier le runtime Python et ses licences.
- [ ] Préparer le packaging reproductible.
- [ ] Définir la migration vers HTTP ou WebSocket.
- [ ] Préparer la revue sécurité de production.

## 43. Sources techniques

Sources principales vérifiées le 19 juillet 2026 :

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

Points vérifiés :

- `OS.execute_with_pipe()` et son mode non bloquant ;
- clés `stdio`, `stderr` et `pid` ;
- nécessité d’arrêter explicitement le processus ;
- `OS.is_process_running()`, `OS.get_process_exit_code()` et `OS.kill()` ;
- lecture disponible par `FileAccess.get_length()` ;
- lecture binaire avec `get_buffer()` ;
- écriture avec `store_line()` et `flush()` ;
- horloge monotone `Time.get_ticks_msec()` ;
- analyse et sérialisation JSON ;
- lecture ligne par ligne de `sys.stdin` ;
- séparation stdout/stderr ;
- sérialisation JSON avec refus de `NaN`.

## 44. Réserves de validation

Le chapitre reste au niveau `static-review`.

Ne sont pas exécutés :

- création des scripts GDScript dans un projet Godot ;
- compilation GDScript dans Godot 4.7.1 ;
- démarrage réel de Python avec `OS.execute_with_pipe()` ;
- lecture non bloquante sous Windows 11 ;
- fragmentation réelle des lignes ;
- limites de tampon ;
- handshake de capacités ;
- corrélation de requêtes simultanées ;
- timeout monotone ;
- réponse tardive ;
- annulation coopérative ;
- arrêt normal ;
- arrêt forcé ;
- crash du compagnon ;
- chargement du `RetrievalService` du chapitre 10 ;
- repli de la fonctionnalité ;
- export Windows ;
- comportement Web et mobile ;
- packaging du runtime Python.

Les extraits Python ont seulement fait l’objet d’une compilation syntaxique. Les extraits GDScript ont fait l’objet d’une revue statique, sans exécution par Godot.

Aucun PDF intermédiaire n’est construit.

## 45. Résultat attendu

`Project Asteria` possède désormais une frontière locale entre Godot et ses services IA :

- contrats versionnés ;
- capacités découvertes ;
- processus compagnon ;
- transport non bloquant ;
- corrélation ;
- délais ;
- annulation coopérative ;
- erreurs structurées ;
- repli déterministe ;
- arrêt contrôlé.

Le chapitre 12 pourra remplacer ou compléter le transport stdio par HTTP, WebSocket, API compatibles OpenAI et files de tâches sans déplacer les responsabilités métier dans les scènes.
