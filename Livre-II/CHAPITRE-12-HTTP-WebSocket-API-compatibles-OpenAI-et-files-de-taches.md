---
title: "Livre II — Chapitre 12 : HTTP, WebSocket, API compatibles OpenAI et files de tâches"
id: "DOC-L2-CH12"
status: "reviewed"
version: "1.0.2"
lang: "fr-FR"
book: "Livre II"
chapter: 12
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-12.md"
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

# HTTP, WebSocket, API compatibles OpenAI et files de tâches

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH12`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

## 1. Rôle du chapitre

Le chapitre 11 a défini un port applicatif indépendant du transport. Le jeu exprime une opération, un payload, un délai et un identifiant de corrélation. Un premier adaptateur utilise un processus compagnon local et un protocole JSON Lines sur les flux standard.

Ce chapitre ajoute les transports réseau locaux et la gestion des travaux qui ne peuvent pas être traités comme une réponse instantanée :

- HTTP pour les requêtes et réponses bornées ;
- WebSocket pour les événements, les progressions et certains flux continus ;
- une couche de traduction vers des API compatibles OpenAI ;
- une file de tâches bornée pour les opérations longues ;
- des règles de backpressure, d’idempotence, d’annulation et de reprise.

L’objectif n’est pas de rendre le gameplay dépendant d’un serveur. `LocalAiGateway` reste le contrat. Les adaptateurs HTTP et WebSocket sont remplaçables, et le repli déterministe du chapitre 11 reste disponible.

## 2. Prérequis

Le lecteur doit connaître :

- les types, fonctions, signaux et dictionnaires du chapitre 2 ;
- les nœuds et le cycle de vie du chapitre 3 ;
- les frontières de modules du chapitre 4 ;
- les services, contrats et bootstrap du chapitre 5 ;
- la configuration typée du chapitre 7 ;
- la mémoire vectorielle du chapitre 10 ;
- `LocalAiGateway`, la corrélation, les délais et le repli du chapitre 11.

Le présent chapitre reste au niveau `static-review`. Aucun serveur, socket, flux de tokens ou worker n’est exécuté dans le Starter Kit.

## 3. Périmètre et frontières

Ce chapitre définit :

- les rôles respectifs de HTTP et WebSocket ;
- un adaptateur HTTP Godot derrière `LocalAiGateway` ;
- un canal WebSocket pour événements et flux progressifs ;
- des enveloppes réseau versionnées ;
- une traduction isolée vers un sous-ensemble compatible OpenAI ;
- un modèle de tâche longue ;
- une file bornée et une politique de backpressure ;
- l’idempotence, la déduplication et les réponses tardives ;
- l’annulation distante ;
- les parcours Solo et Studio.

Il ne définit pas encore :

- l’exposition sur Internet ;
- l’authentification forte ;
- la gestion complète des secrets ;
- TLS, certificats et rotation ;
- les permissions multi-utilisateurs ;
- le sandboxing du processus ;
- la signature des exécutables ;
- la politique de publication.

Ces sujets appartiennent au chapitre 13 et aux Livres suivants.

## 4. Comparaison avec les chapitres voisins

### 4.1 Chapitre 11

Le chapitre 11 reste propriétaire :

- des objets requête, réponse, erreur et capacité ;
- du registre des appels en attente ;
- des délais monotones ;
- du repli déterministe ;
- du cycle de vie du gateway.

Le présent chapitre ajoute des adaptateurs. Il ne déplace pas les URL, en-têtes ou sockets dans les fonctionnalités de gameplay.

### 4.2 Chapitre 13

Le chapitre 13 traitera :

- séparation production/runtime ;
- secrets ;
- liste d’hôtes autorisés ;
- privilèges minimaux ;
- durcissement réseau ;
- isolation ;
- télémétrie et confidentialité ;
- politiques d’échec en production.

Ce chapitre applique seulement des limites minimales : boucle locale par défaut, validation, taille bornée et liste fermée d’opérations.

## 5. Choisir le transport

> **[LECTURE] Matrice de décision — Ne pas saisir.**

```text
Besoin                                      Transport conseillé
------------------------------------------  ----------------------------
Requête courte avec réponse unique          HTTP
Lecture de santé et capacités               HTTP
Soumission d’une tâche longue               HTTP
Consultation ponctuelle de l’état            HTTP
Progression d’une tâche                     WebSocket ou polling HTTP
Événements nombreux dans les deux sens      WebSocket
Flux de tokens ou fragments                 WebSocket
Fonctionnement sans réseau local            processus compagnon stdio
```

HTTP n’est pas « lent » par nature. WebSocket n’est pas « meilleur » par nature. Le choix dépend du cycle de vie du message.

## 6. Architecture de référence

> **[LECTURE] Architecture transportable — Ne pas saisir.**

```text
fonctionnalité Godot
        ↓
LocalAiGateway
        ↓
┌───────────────────────────────┐
│ StdioCompanionTransport       │
│ HttpLocalAiTransport          │
│ WebSocketEventChannel         │
└───────────────────────────────┘
        ↓
service local Python
        ↓
TaskQueue + workers + adaptateurs IA
```

Le canal WebSocket n’est pas un second port métier. Il alimente des événements qui restent corrélés aux requêtes et tâches du gateway.

## 7. Arborescence documentée

> **[LECTURE] Arborescence cible — Ne pas créer sans adaptation.**

```text
res://src/core/ai/
├── http_local_ai_transport.gd
├── websocket_event_channel.gd
├── ai_network_envelope_codec.gd
├── ai_task.gd
├── ai_task_status.gd
├── ai_task_event.gd
├── openai_compatible_mapper.gd
└── local_ai_network_driver.gd

res://src/app/
└── ai_network_bootstrap.gd

tools/ai_server/
├── app.py
├── protocol.py
├── task_models.py
├── task_queue.py
├── task_worker.py
├── openai_adapter.py
└── operations.py

res://scenes/learning/
└── ch12_network_ai_demo.gd
```

## 8. Configuration réseau typée

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_network_config.gd`.

```gdscript
class_name AiNetworkConfig
extends RefCounted

var base_url := "http://127.0.0.1:8765"
var websocket_url := "ws://127.0.0.1:8765/v1/events"
var request_timeout_seconds := 15.0
var max_response_bytes := 4 * 1024 * 1024
var max_in_flight := 8

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not _is_loopback_url(base_url, "http", ""):
		errors.append("base_url doit viser exactement 127.0.0.1 avec un port valide")
	if not _is_loopback_url(websocket_url, "ws", "/v1/events"):
		errors.append("websocket_url doit viser 127.0.0.1 et /v1/events")
	if request_timeout_seconds < 0.1 or request_timeout_seconds > 120.0:
		errors.append("request_timeout_seconds hors limites")
	if max_response_bytes < 1024 or max_response_bytes > 32 * 1024 * 1024:
		errors.append("max_response_bytes hors limites")
	if max_in_flight < 1 or max_in_flight > 64:
		errors.append("max_in_flight hors limites")
	return errors

func _is_loopback_url(value: String, scheme: String, path: String) -> bool:
	var prefix := scheme + "://127.0.0.1:"
	if not value.begins_with(prefix):
		return false

	var remainder := value.trim_prefix(prefix)
	var slash_index := remainder.find("/")
	var port_text := remainder
	var actual_path := ""
	if slash_index >= 0:
		port_text = remainder.left(slash_index)
		actual_path = remainder.substr(slash_index)

	if not port_text.is_valid_int():
		return false
	var port := port_text.to_int()
	return port >= 1 and port <= 65535 and actual_path == path
```

`base_url` et `websocket_url` restent des données d’infrastructure. La validation refuse les noms ressemblant à la boucle locale, comme `127.0.0.1.example.org`, et contrôle le port. `max_in_flight` limite les requêtes simultanées. Le chapitre 13 généralisera les hôtes autorisés, TLS et les politiques réseau.

## 9. Enveloppe réseau

Le contrat métier du chapitre 11 est converti vers une enveloppe réseau stable.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_network_envelope_codec.gd`.

```gdscript
class_name AiNetworkEnvelopeCodec
extends RefCounted

const REQUEST_FORMAT := "project-asteria-ai-http-request"
const RESPONSE_FORMAT := "project-asteria-ai-http-response"
const FORMAT_VERSION := 1

func encode_request(request: AiRequest) -> Dictionary:
	if request == null:
		return {}
	return {
		"format": REQUEST_FORMAT,
		"format_version": FORMAT_VERSION,
		"request_id": String(request.request_id),
		"operation": String(request.operation),
		"payload": request.payload.duplicate(true),
		"timeout_ms": int(request.timeout_seconds * 1000.0),
	}

func decode_response(
	document: Dictionary,
	expected_request_id: StringName
) -> AiResponse:
	if String(document.get("format", "")) != RESPONSE_FORMAT:
		return AiResponse.protocol_error(
			expected_request_id,
			"Format de réponse inconnu."
		)
	if int(document.get("format_version", -1)) != FORMAT_VERSION:
		return AiResponse.protocol_error(
			expected_request_id,
			"Version de réponse incompatible."
		)
	var response_id := StringName(String(document.get("request_id", "")))
	if response_id != expected_request_id:
		return AiResponse.protocol_error(
			expected_request_id,
			"Identifiant de corrélation incohérent."
		)
	return AiResponse.from_dictionary(document)
```

`encode_request()` transforme le contrat en dictionnaire JSON. `decode_response()` vérifie format, version et corrélation avant de déléguer au constructeur de réponse.

## 10. Routes HTTP de référence

> **[LECTURE] Routes locales — Ne pas saisir.**

```text
GET    /v1/health
GET    /v1/capabilities
POST   /v1/operations
POST   /v1/tasks
GET    /v1/tasks/{task_id}
DELETE /v1/tasks/{task_id}
GET    /v1/tasks/{task_id}/result
WS     /v1/events
```

`POST /v1/operations` convient aux appels courts. `POST /v1/tasks` crée une tâche longue. `DELETE` demande une annulation coopérative.

## 11. Adaptateur HTTP Godot

`HTTPRequest` est un nœud haut niveau. Une instance ne doit pas être réutilisée pour plusieurs requêtes simultanées. L’adaptateur crée donc un nœud par appel, sous une limite globale.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/http_local_ai_transport.gd`.

```gdscript
class_name HttpLocalAiTransport
extends AiTransport

signal response_received(response: AiResponse)

var _config: AiNetworkConfig
var _codec := AiNetworkEnvelopeCodec.new()
var _owner: Node
var _requests: Dictionary[StringName, HTTPRequest] = {}

func configure(owner: Node, config: AiNetworkConfig) -> void:
	_owner = owner
	_config = config

func submit(request: AiRequest) -> Error:
	if _owner == null or _config == null:
		return ERR_UNCONFIGURED
	if request == null or not request.is_valid():
		return ERR_INVALID_PARAMETER
	if _requests.size() >= _config.max_in_flight:
		return ERR_BUSY
	if _requests.has(request.request_id):
		return ERR_ALREADY_EXISTS

	var http := HTTPRequest.new()
	http.timeout = minf(
		request.timeout_seconds,
		_config.request_timeout_seconds
	)
	http.body_size_limit = _config.max_response_bytes
	http.download_file = ""
	http.use_threads = true
	_owner.add_child(http)
	_requests[request.request_id] = http
	http.request_completed.connect(
		_on_request_completed.bind(request.request_id),
		CONNECT_ONE_SHOT
	)

	var envelope := _codec.encode_request(request)
	var body := JSON.stringify(envelope)
	var headers := PackedStringArray([
		"Content-Type: application/json",
		"Accept: application/json",
	])
	var error := http.request(
		_config.base_url + "/v1/operations",
		headers,
		HTTPClient.METHOD_POST,
		body
	)
	if error != OK:
		_cleanup_request(request.request_id)
	return error
```

`HTTPRequest.new()` crée le nœud. `timeout` est exprimé en secondes et plafonné par la configuration. `body_size_limit` interrompt le téléchargement lorsque le corps décompressé dépasse la limite, au lieu d’attendre son chargement complet. `CONNECT_ONE_SHOT` déconnecte le signal après le premier appel. `bind()` ajoute `request_id` aux arguments du callback.

## 12. Lire une réponse HTTP

> **[VSC] Visual Studio Code — Ajouter :** dans `http_local_ai_transport.gd`.

```gdscript
func _on_request_completed(
	result: int,
	response_code: int,
	_headers: PackedStringArray,
	body: PackedByteArray,
	request_id: StringName
) -> void:
	_cleanup_request(request_id)

	if body.size() > _config.max_response_bytes:
		response_received.emit(
			AiResponse.failure(
				request_id,
				AiServiceError.protocol("Réponse HTTP trop volumineuse.")
			)
		)
		return

	if result == HTTPRequest.RESULT_BODY_SIZE_LIMIT_EXCEEDED:
		response_received.emit(
			AiResponse.failure(
				request_id,
				AiServiceError.protocol(
					"Réponse HTTP au-delà de la limite autorisée."
				)
			)
		)
		return

	if result != HTTPRequest.RESULT_SUCCESS:
		response_received.emit(
			AiResponse.failure(
				request_id,
				AiServiceError.unavailable(
					"Échec du transport HTTP : %d" % result,
					true
				)
			)
		)
		return

	if response_code < 200 or response_code >= 300:
		response_received.emit(
			AiResponse.failure(
				request_id,
				_map_http_error(response_code, body)
			)
		)
		return

	var json := JSON.new()
	var text := body.get_string_from_utf8()
	if json.parse(text) != OK or not json.data is Dictionary:
		response_received.emit(
			AiResponse.failure(
				request_id,
				AiServiceError.protocol("JSON HTTP invalide.")
			)
		)
		return

	response_received.emit(
		_codec.decode_response(json.data as Dictionary, request_id)
	)

func _cleanup_request(request_id: StringName) -> void:
	var http := _requests.get(request_id) as HTTPRequest
	_requests.erase(request_id)
	if http != null:
		http.queue_free()
```

`result` décrit l’état du transport. `response_code` est le code HTTP. Une réponse HTTP reçue avec `500` n’est pas un succès métier.

## 13. Mapper les codes HTTP

> **[VSC] Visual Studio Code — Ajouter :** dans `http_local_ai_transport.gd`.

```gdscript
func _map_http_error(
	response_code: int,
	body: PackedByteArray
) -> AiServiceError:
	var retryable := response_code in [408, 429, 502, 503, 504]
	var message := "Erreur HTTP %d" % response_code

	var json := JSON.new()
	if body.size() <= _config.max_response_bytes:
		var text := body.get_string_from_utf8()
		if json.parse(text) == OK and json.data is Dictionary:
			var document := json.data as Dictionary
			message = String(document.get("message", message))

	match response_code:
		400:
			return AiServiceError.invalid_request(message)
		404:
			return AiServiceError.unsupported(message)
		408:
			return AiServiceError.timeout(message)
		409:
			return AiServiceError.conflict(message)
		429:
			return AiServiceError.unavailable(message, true)
		_:
			return AiServiceError.remote(message, retryable)
```

Le code `429` indique une surcharge ou une limite. Il ne doit pas déclencher une boucle de nouvelles tentatives immédiates.

## 14. Annulation HTTP

`HTTPRequest.cancel_request()` annule l’attente locale. Le serveur peut avoir commencé le travail. Pour une opération longue, l’annulation doit cibler une ressource de tâche.

> **[VSC] Visual Studio Code — Ajouter :** dans `http_local_ai_transport.gd`.

```gdscript
func cancel(request_id: StringName) -> void:
	var http := _requests.get(request_id) as HTTPRequest
	if http == null:
		return
	http.cancel_request()
	_cleanup_request(request_id)
	response_received.emit(
		AiResponse.failure(
			request_id,
			AiServiceError.cancelled(
				"Requête HTTP annulée localement."
			)
		)
	)
```

La formulation « localement » est obligatoire : elle ne promet pas l’arrêt du serveur.

## 15. Santé et capacités

Le gateway ne doit pas considérer le service prêt après une simple connexion TCP. Il lit la santé et les capacités.

> **[LECTURE] Réponse de santé — Ne pas saisir.**

```json
{
  "status": "ready",
  "protocol_version": 1,
  "service_version": "0.1.0",
  "queue": {
    "capacity": 32,
    "pending": 2,
    "running": 1
  }
}
```

> **[LECTURE] Réponse de capacités — Ne pas saisir.**

```json
{
  "capabilities": [
    {
      "name": "knowledge.search",
      "mode": "interactive",
      "max_payload_bytes": 65536
    },
    {
      "name": "text.generate",
      "mode": "task",
      "streaming": true
    }
  ]
}
```

Une capacité doit indiquer si elle accepte une réponse directe, une tâche ou un flux.

## 16. WebSocket : rôle et cycle de vie

`WebSocketPeer` fournit un canal bidirectionnel. Le nœud pilote appelle `poll()` régulièrement. Le code doit gérer connexion, fermeture, paquets, limites et reconnexion bornée.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/websocket_event_channel.gd`.

```gdscript
class_name WebSocketEventChannel
extends Node

signal connected
signal disconnected(code: int, reason: String)
signal event_received(event: AiTaskEvent)

const MAX_PACKET_BYTES := 1024 * 1024

var _peer := WebSocketPeer.new()
var _url := ""
var _connected := false
var _stopping := false

func configure(url: String) -> void:
	_url = url

func start() -> Error:
	if _url.is_empty():
		return ERR_UNCONFIGURED
	_stopping = false
	_connected = false
	_peer = WebSocketPeer.new()
	_peer.inbound_buffer_size = MAX_PACKET_BYTES
	_peer.max_queued_packets = 128
	var error := _peer.connect_to_url(_url)
	if error != OK:
		return error
	set_process(true)
	return OK

func _process(_delta: float) -> void:
	_peer.poll()
	var state := _peer.get_ready_state()

	if state == WebSocketPeer.STATE_OPEN and not _connected:
		_connected = true
		connected.emit()

	if state == WebSocketPeer.STATE_OPEN:
		_read_packets()
	elif state == WebSocketPeer.STATE_CLOSED:
		_connected = false
		set_process(false)
		disconnected.emit(
			_peer.get_close_code(),
			_peer.get_close_reason()
		)
```

`poll()` fait progresser le protocole. `get_ready_state()` retourne l’état courant. Le chapitre ne promet pas une reconnexion automatique infinie.

## 17. Lire des événements WebSocket

> **[VSC] Visual Studio Code — Ajouter :** dans `websocket_event_channel.gd`.

```gdscript
func _read_packets() -> void:
	while _peer.get_available_packet_count() > 0:
		var packet := _peer.get_packet()
		if packet.size() > MAX_PACKET_BYTES:
			_peer.close(1009, "message too large")
			return
		if not _peer.was_string_packet():
			continue

		var text := packet.get_string_from_utf8()
		var json := JSON.new()
		if json.parse(text) != OK or not json.data is Dictionary:
			continue

		var event := AiTaskEvent.from_dictionary(
			json.data as Dictionary
		)
		if event != null:
			event_received.emit(event)

func stop() -> void:
	_stopping = true
	if _peer.get_ready_state() == WebSocketPeer.STATE_OPEN:
		_peer.close(1000, "normal shutdown")
	else:
		set_process(false)
```

Le code `1000` désigne une fermeture normale. Le code `1009` signale un message trop volumineux.

## 18. S’abonner aux tâches

Après connexion, le client envoie une liste de tâches autorisées.

> **[VSC] Visual Studio Code — Ajouter :** dans `websocket_event_channel.gd`.

```gdscript
func subscribe(task_ids: Array[StringName]) -> Error:
	if _peer.get_ready_state() != WebSocketPeer.STATE_OPEN:
		return ERR_UNAVAILABLE

	var values: Array[String] = []
	for task_id: StringName in task_ids:
		if not task_id.is_empty():
			values.append(String(task_id))

	var message := {
		"type": "subscribe",
		"format_version": 1,
		"task_ids": values,
	}
	var text := JSON.stringify(message)
	if text.to_utf8_buffer().size() > MAX_PACKET_BYTES:
		return ERR_OUT_OF_MEMORY
	return _peer.send_text(text)
```

Le serveur doit vérifier que le client peut consulter chaque tâche. La présence d’un identifiant ne constitue pas une autorisation.

## 19. Modèle d’une tâche longue

Une tâche est une ressource possédant un identifiant stable pendant sa durée de vie.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_task_status.gd`.

```gdscript
class_name AiTaskStatus
extends RefCounted

enum State {
	QUEUED,
	RUNNING,
	SUCCEEDED,
	FAILED,
	CANCEL_REQUESTED,
	CANCELLED,
	EXPIRED,
}

static func is_terminal(value: State) -> bool:
	return value in [
		State.SUCCEEDED,
		State.FAILED,
		State.CANCELLED,
		State.EXPIRED,
	]
```

Un état terminal ne doit plus revenir à `RUNNING`.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_task.gd`.

```gdscript
class_name AiTask
extends RefCounted

var task_id: StringName
var request_id: StringName
var operation: StringName
var state: AiTaskStatus.State
var progress := 0.0
var result: Dictionary[String, Variant] = {}
var error: AiServiceError
var created_at_utc := ""
var updated_at_utc := ""

func is_terminal() -> bool:
	return AiTaskStatus.is_terminal(state)
```

`progress` reste indicatif. La réussite est définie par l’état et le résultat, pas par `progress == 1.0`.

## 20. Transitions de tâche

> **[LECTURE] Graphe de transitions — Ne pas saisir.**

```text
QUEUED ───────→ RUNNING ───────→ SUCCEEDED
   │               │
   │               ├───────────→ FAILED
   │               └───────────→ CANCEL_REQUESTED ─→ CANCELLED
   └───────────────────────────→ CANCEL_REQUESTED ─→ CANCELLED

QUEUED ou RUNNING ─────────────→ EXPIRED
```

Une demande d’annulation n’est pas un état terminal. Le worker doit atteindre `CANCELLED` ou terminer avec un autre état documenté.

## 21. Soumettre une tâche

> **[LECTURE] Requête de création — Ne pas saisir.**

```json
{
  "format": "project-asteria-task-create",
  "format_version": 1,
  "request_id": "session-a-00000042",
  "idempotency_key": "session-a-00000042",
  "operation": "text.generate",
  "payload": {
    "prompt": "Rédige un résumé du codex.",
    "max_tokens": 300
  },
  "priority": 50,
  "timeout_ms": 30000
}
```

> **[LECTURE] Réponse de création — Ne pas saisir.**

```json
{
  "task_id": "task-6e2d...",
  "request_id": "session-a-00000042",
  "state": "queued",
  "status_url": "/v1/tasks/task-6e2d...",
  "result_url": "/v1/tasks/task-6e2d.../result"
}
```

Le serveur peut retourner `202 Accepted` parce que le résultat n’existe pas encore.

## 22. Idempotence et déduplication

Une `idempotency_key` permet de répéter une soumission après une perte de réponse sans créer deux tâches identiques.

Règles :

- la clé est générée par le client ;
- elle est unique dans un périmètre documenté ;
- le serveur conserve la clé pendant une durée limitée ;
- même clé et même empreinte retournent la même tâche ;
- même clé et payload différent produisent un conflit ;
- l’idempotence ne remplace pas la corrélation.

> **[LECTURE] Résultat de conflit — Ne pas saisir.**

```json
{
  "code": "idempotency_conflict",
  "message": "La clé existe avec un payload différent.",
  "retryable": false
}
```

## 23. File bornée et backpressure

Une file sans limite transforme une surcharge en consommation mémoire illimitée.

> **[VSC] Visual Studio Code — Créer :** `tools/ai_server/task_queue.py`.

```python
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from itertools import count
from typing import Any

_sequence = count()

@dataclass(order=True, slots=True)
class QueueEntry:
    priority: int
    sequence: int = field(compare=True)
    task_id: str = field(compare=False)
    operation: str = field(compare=False)
    payload: dict[str, Any] = field(compare=False)

class BoundedTaskQueue:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity doit être positif")
        self._queue: asyncio.PriorityQueue[QueueEntry] = (
            asyncio.PriorityQueue(maxsize=capacity)
        )

    def try_put(
        self,
        task_id: str,
        operation: str,
        payload: dict[str, Any],
        priority: int,
    ) -> bool:
        entry = QueueEntry(
            priority=-max(0, min(priority, 100)),
            sequence=next(_sequence),
            task_id=task_id,
            operation=operation,
            payload=dict(payload),
        )
        try:
            self._queue.put_nowait(entry)
        except asyncio.QueueFull:
            return False
        return True

    async def get(self) -> QueueEntry:
        return await self._queue.get()

    def task_done(self) -> None:
        self._queue.task_done()

    def size(self) -> int:
        return self._queue.qsize()
```

`PriorityQueue` retourne le plus petit élément. Le signe négatif transforme une priorité élevée en valeur plus petite. `sequence` conserve l’ordre entre priorités égales.

## 24. Réponse de surcharge

Lorsque la file est pleine, le serveur refuse la nouvelle tâche.

> **[LECTURE] Réponse HTTP de surcharge — Ne pas saisir.**

```text
HTTP 429 Too Many Requests
Retry-After: 2
```

> **[LECTURE] Corps structuré — Ne pas saisir.**

```json
{
  "code": "queue_full",
  "message": "La file locale est pleine.",
  "retryable": true,
  "retry_after_ms": 2000
}
```

Le client peut afficher un repli, demander confirmation ou réessayer avec un délai borné et du jitter. Il ne doit pas boucler immédiatement.

## 25. Registre de tâches en mémoire

Le chapitre utilise un registre en mémoire. Il ne promet pas la persistance après redémarrage.

> **[VSC] Visual Studio Code — Créer :** `tools/ai_server/task_models.py`.

```python
from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from time import time
from typing import Any

class TaskState(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCEL_REQUESTED = "cancel_requested"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

@dataclass(slots=True)
class TaskRecord:
    task_id: str
    request_id: str
    operation: str
    state: TaskState = TaskState.QUEUED
    progress: float = 0.0
    result: dict[str, Any] = field(default_factory=dict)
    error: dict[str, Any] = field(default_factory=dict)
    cancel_requested: bool = False
    created_at: float = field(default_factory=time)
    updated_at: float = field(default_factory=time)
```

`StrEnum` fournit des valeurs texte. `slots=True` limite les attributs accidentels. `time()` convient à un horodatage, pas à la mesure d’un délai monotone.

## 26. Worker coopératif

> **[VSC] Visual Studio Code — Créer :** `tools/ai_server/task_worker.py`.

```python
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from time import time
from typing import Any

from task_models import TaskRecord, TaskState
from task_queue import BoundedTaskQueue

OperationHandler = Callable[
    [TaskRecord, dict[str, Any]],
    Awaitable[dict[str, Any]],
]

class TaskWorker:
    def __init__(
        self,
        queue: BoundedTaskQueue,
        records: dict[str, TaskRecord],
        handlers: dict[str, OperationHandler],
    ) -> None:
        self._queue = queue
        self._records = records
        self._handlers = handlers

    async def run(self) -> None:
        while True:
            entry = await self._queue.get()
            try:
                await self._execute(entry.task_id, entry.payload)
            finally:
                self._queue.task_done()

    async def _execute(
        self,
        task_id: str,
        payload: dict[str, Any],
    ) -> None:
        record = self._records.get(task_id)
        if record is None:
            return
        if record.cancel_requested:
            record.state = TaskState.CANCELLED
            return

        handler = self._handlers.get(record.operation)
        if handler is None:
            record.state = TaskState.FAILED
            record.error = {
                "code": "unsupported_operation",
                "message": record.operation,
            }
            return

        record.state = TaskState.RUNNING
        record.updated_at = time()
        try:
            record.result = await handler(record, payload)
        except asyncio.CancelledError:
            record.state = TaskState.CANCELLED
            raise
        except Exception as exc:
            record.state = TaskState.FAILED
            record.error = {
                "code": "internal_error",
                "message": type(exc).__name__,
            }
        else:
            record.state = (
                TaskState.CANCELLED
                if record.cancel_requested
                else TaskState.SUCCEEDED
            )
        finally:
            record.updated_at = time()
```

Le worker transmet le payload copié depuis la file au handler et actualise `updated_at` à chaque fin de tentative. Le message d’erreur ne recopie pas automatiquement des données sensibles. Un handler long doit consulter `record.cancel_requested` à des points sûrs.

## 27. Événements de progression

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/ai_task_event.gd`.

```gdscript
class_name AiTaskEvent
extends RefCounted

var task_id: StringName
var sequence: int
var event_type: StringName
var state: AiTaskStatus.State
var progress: float
var payload: Dictionary[String, Variant]

static func from_dictionary(document: Dictionary) -> AiTaskEvent:
	if String(document.get("format", "")) != "project-asteria-task-event":
		return null
	if int(document.get("format_version", -1)) != 1:
		return null

	var result := AiTaskEvent.new()
	result.task_id = StringName(String(document.get("task_id", "")))
	result.sequence = int(document.get("sequence", -1))
	result.event_type = StringName(String(document.get("event", "")))
	result.progress = clampf(
		float(document.get("progress", 0.0)),
		0.0,
		1.0
	)

	match String(document.get("state", "")):
		"queued":
			result.state = AiTaskStatus.State.QUEUED
		"running":
			result.state = AiTaskStatus.State.RUNNING
		"succeeded":
			result.state = AiTaskStatus.State.SUCCEEDED
		"failed":
			result.state = AiTaskStatus.State.FAILED
		"cancel_requested":
			result.state = AiTaskStatus.State.CANCEL_REQUESTED
		"cancelled":
			result.state = AiTaskStatus.State.CANCELLED
		"expired":
			result.state = AiTaskStatus.State.EXPIRED
		_:
			return null

	var payload_value: Variant = document.get("payload", {})
	if not payload_value is Dictionary:
		return null
	result.payload = (payload_value as Dictionary).duplicate(true)
	if result.task_id.is_empty() or result.sequence < 0:
		return null
	return result
```

`sequence` permet d’ignorer un événement ancien reçu après un événement plus récent. L’état et le payload sont validés avant création de l’objet typé.

## 28. Ordonnancer les événements

> **[VSC] Visual Studio Code — Ajouter :** dans le gestionnaire de tâches Godot.

```gdscript
var _last_sequences: Dictionary[StringName, int] = {}

func accept_event(event: AiTaskEvent) -> bool:
	if event == null:
		return false
	var previous := _last_sequences.get(event.task_id, -1)
	if event.sequence <= previous:
		return false
	_last_sequences[event.task_id] = event.sequence
	return true
```

Un WebSocket conserve l’ordre dans une connexion, mais une reconnexion ou un rattrapage peut réintroduire des événements anciens. Le numéro rend la politique explicite.

## 29. Polling HTTP de secours

WebSocket est optionnel. Si le canal est absent, Godot peut interroger l’état avec un intervalle croissant et borné.

> **[LECTURE] Politique de polling — Ne pas saisir.**

```text
0 à 5 secondes       : toutes les 0,5 s
5 à 30 secondes      : toutes les 1 s
au-delà de 30 s      : toutes les 2 s
maximum               : 2 s
arrêt                 : état terminal ou délai global
```

Le polling cesse lorsque l’interface n’a plus besoin du résultat ou lorsque la tâche est terminale.

## 30. API compatibles OpenAI : principe

Une API « compatible OpenAI » reproduit une partie des chemins et schémas attendus par des clients existants. Le projet ne doit pas confondre cette compatibilité d’interface avec une dépendance métier à un fournisseur.

L’adaptateur prend un `AiRequest` interne et produit par exemple :

- `/v1/chat/completions` pour une cible de compatibilité historique ;
- `/v1/responses` lorsque le serveur local l’implémente ;
- `/v1/embeddings` ;
- `/v1/models`.

L’exemple détaillé ci-dessous cible volontairement le sous-ensemble `chat/completions`. Il ne prétend pas reproduire toute l’API OpenAI actuelle. Les intégrations directes avec la plateforme OpenAI privilégient désormais l’API Responses et diffusent notamment des événements Server-Sent Events ; le mapper local doit donc être versionné selon la cible réellement choisie.

Le port interne conserve ses propres opérations : `text.generate`, `embedding.create`, `knowledge.search`.

## 31. Mapper une requête de génération

> **[VSC] Visual Studio Code — Créer :** `res://src/core/ai/openai_compatible_mapper.gd`.

```gdscript
class_name OpenAiCompatibleMapper
extends RefCounted

func to_chat_completion(request: AiRequest) -> Dictionary:
	if request == null or request.operation != &"text.generate":
		return {}

	var prompt := String(request.payload.get("prompt", "")).strip_edges()
	if prompt.is_empty():
		return {}

	return {
		"model": String(
			request.payload.get("model", "local-default")
		),
		"messages": [
			{
				"role": "user",
				"content": prompt,
			},
		],
		"temperature": clampf(
			float(request.payload.get("temperature", 0.2)),
			0.0,
			2.0
		),
		"max_tokens": clampi(
			int(request.payload.get("max_tokens", 256)),
			1,
			4096
		),
		"stream": bool(request.payload.get("stream", false)),
	}
```

Le mapper applique des limites. Il ne transmet pas tout le payload interne.

## 32. Mapper une réponse compatible OpenAI

> **[VSC] Visual Studio Code — Ajouter :** dans `openai_compatible_mapper.gd`.

```gdscript
func from_chat_completion(
	request_id: StringName,
	document: Dictionary
) -> AiResponse:
	var choices: Variant = document.get("choices", null)
	if not choices is Array or choices.is_empty():
		return AiResponse.protocol_error(
			request_id,
			"choices absent ou vide."
		)

	var first: Variant = choices[0]
	if not first is Dictionary:
		return AiResponse.protocol_error(
			request_id,
			"Premier choix invalide."
		)

	var message: Variant = (first as Dictionary).get("message", null)
	if not message is Dictionary:
		return AiResponse.protocol_error(
			request_id,
			"Message absent."
		)

	var content := String(
		(message as Dictionary).get("content", "")
	)
	return AiResponse.success(
		request_id,
		{
			"text": content,
			"finish_reason": String(
				(first as Dictionary).get("finish_reason", "")
			),
			"usage": (
				document.get("usage", {}) as Dictionary
			).duplicate(true),
		}
	)
```

Le mapper valide chaque niveau. Une réponse HTTP `200` avec `choices` absent reste une erreur de protocole.

## 33. Streaming compatible OpenAI

Certaines API utilisent Server-Sent Events, d’autres WebSocket. Le présent chapitre choisit WebSocket pour le fil pédagogique de Godot. Chaque fragment porte :

- `request_id` ou `task_id` ;
- `sequence` ;
- `delta` ;
- `finish_reason` éventuel ;
- version du format.

> **[LECTURE] Fragment de texte — Ne pas saisir.**

```json
{
  "format": "project-asteria-text-delta",
  "format_version": 1,
  "task_id": "task-6e2d",
  "sequence": 12,
  "delta": " nord",
  "finish_reason": ""
}
```

Le client concatène uniquement les séquences acceptées. Le texte progressif n’est pas autoritaire tant que la tâche n’est pas terminale.

## 34. Reprise après déconnexion

Après reconnexion, le client :

1. relit l’état HTTP de chaque tâche non terminale ;
2. récupère le dernier numéro de séquence connu ;
3. se réabonne ;
4. accepte uniquement les événements plus récents ;
5. récupère le résultat final par HTTP.

Le chapitre ne promet pas que le serveur conserve tous les fragments. Le résultat final reste l’autorité.

## 35. Nouvelle tentative bornée

Une nouvelle tentative est permise uniquement pour une erreur déclarée `retryable`.

> **[LECTURE] Politique initiale — Ne pas saisir.**

```text
tentative 1 : délai 0,5 s + jitter
tentative 2 : délai 1,0 s + jitter
tentative 3 : délai 2,0 s + jitter
maximum     : 3 tentatives
```

Le jitter évite que plusieurs clients recommencent exactement au même instant. Une nouvelle tentative de création de tâche réutilise la même `idempotency_key`.

## 36. Priorités

Le serveur accepte une priorité bornée de `0` à `100`. Une priorité élevée ne doit pas permettre de contourner les permissions ou la capacité.

Politique Solo :

> **[LECTURE] Priorités initiales — Ne pas saisir.**

```text
80 : réponse visible attendue par le joueur
50 : génération de contenu de préparation
20 : indexation ou tâche d’arrière-plan
```

Le Studio peut appliquer des quotas par équipe et opération. La famine des faibles priorités doit être mesurée.

## 37. Expiration et délais

Trois durées sont distinctes :

- délai HTTP de transport ;
- durée maximale métier d’une tâche, transportée ici par `timeout_ms` puis convertie en échéance monotone côté serveur ;
- durée de conservation du résultat.

Une tâche `EXPIRED` peut avoir été supprimée avant lecture. Le client ne doit pas la présenter comme `FAILED` sans distinction.

## 38. Cycle de vie du serveur local

> **[LECTURE] Cycle de vie — Ne pas saisir.**

```text
démarrage
  ↓
chargement configuration
  ↓
initialisation des adaptateurs
  ↓
démarrage des workers
  ↓
ouverture HTTP
  ↓
ouverture WebSocket
  ↓
ready
  ↓
arrêt des nouvelles soumissions
  ↓
annulation ou drainage borné
  ↓
fermeture WebSocket
  ↓
fermeture HTTP
  ↓
arrêt workers
```

Le serveur ne doit pas annoncer `ready` avant que les opérations déclarées soient réellement disponibles.

## 39. Bootstrap Godot

> **[VSC] Visual Studio Code — Créer :** `res://src/app/ai_network_bootstrap.gd`.

```gdscript
class_name AiNetworkBootstrap
extends RefCounted

func build(
	parent: Node,
	config: AiNetworkConfig
) -> LocalAiGatewayService:
	var errors := config.validate()
	if not errors.is_empty():
		for message: String in errors:
			push_error(message)
		return null

	var transport := HttpLocalAiTransport.new()
	transport.configure(parent, config)

	var events := WebSocketEventChannel.new()
	events.configure(config.websocket_url)
	parent.add_child(events)

	var service := LocalAiGatewayService.new()
	service.configure(
		transport,
		BeaconKnowledgeFallback.new()
	)

	var driver := LocalAiNetworkDriver.new()
	driver.configure(service, events)
	parent.add_child(driver)
	return service
```

Le point de composition connaît les adaptateurs. Les fonctionnalités reçoivent le port.

## 40. Serveur Python : enveloppe minimale

> **[VSC] Visual Studio Code — Créer :** `tools/ai_server/protocol.py`.

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

REQUEST_FORMAT = "project-asteria-ai-http-request"
RESPONSE_FORMAT = "project-asteria-ai-http-response"
FORMAT_VERSION = 1
MAX_PAYLOAD_KEYS = 64

@dataclass(frozen=True, slots=True)
class OperationRequest:
    request_id: str
    operation: str
    payload: dict[str, Any]
    timeout_ms: int

def parse_operation_request(document: Any) -> OperationRequest:
    if not isinstance(document, dict):
        raise ValueError("La racine doit être un objet")
    if document.get("format") != REQUEST_FORMAT:
        raise ValueError("Format inconnu")
    if document.get("format_version") != FORMAT_VERSION:
        raise ValueError("Version incompatible")

    request_id = document.get("request_id")
    operation = document.get("operation")
    payload = document.get("payload")
    timeout_ms = document.get("timeout_ms")

    if not isinstance(request_id, str) or not request_id:
        raise ValueError("request_id invalide")
    if not isinstance(operation, str) or not operation:
        raise ValueError("operation invalide")
    if not isinstance(payload, dict):
        raise ValueError("payload invalide")
    if len(payload) > MAX_PAYLOAD_KEYS:
        raise ValueError("payload trop complexe")
    if not isinstance(timeout_ms, int) or isinstance(timeout_ms, bool):
        raise ValueError("timeout_ms invalide")
    if timeout_ms < 100 or timeout_ms > 120_000:
        raise ValueError("timeout_ms hors limites")

    return OperationRequest(
        request_id=request_id,
        operation=operation,
        payload=dict(payload),
        timeout_ms=timeout_ms,
    )
```

Le parseur n’exécute aucune opération. Il convertit une entrée non fiable vers un type interne.

## 41. Registre fermé des opérations

> **[VSC] Visual Studio Code — Créer :** `tools/ai_server/operations.py`.

```python
from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

Operation = Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]

class OperationRegistry:
    def __init__(self) -> None:
        self._operations: dict[str, Operation] = {}

    def register(self, name: str, operation: Operation) -> None:
        if not name or name in self._operations:
            raise ValueError(f"Opération invalide ou dupliquée : {name}")
        self._operations[name] = operation

    def get(self, name: str) -> Operation | None:
        return self._operations.get(name)

    def names(self) -> list[str]:
        return sorted(self._operations)
```

Aucun nom de fonction reçu par réseau n’est évalué dynamiquement.

## 42. Réponse directe ou tâche

Une opération possède un mode déclaré :

> **[LECTURE] Catalogue de capacités — Ne pas saisir.**

```json
{
  "knowledge.search": {
    "mode": "interactive",
    "streaming": false
  },
  "text.generate": {
    "mode": "task",
    "streaming": true
  }
}
```

Le serveur refuse une route incohérente : `text.generate` ne doit pas être exécutée par la route interactive si elle est déclarée `task`.

## 43. Repli côté client

Le client utilise le repli lorsque :

- le service est indisponible ;
- la capacité n’existe pas ;
- la file refuse la tâche ;
- le délai est dépassé pour une fonction tolérant le repli.

Il ne masque pas :

- une réponse de protocole invalide ;
- une violation d’autorisation ;
- une incohérence de version ;
- un résultat métier déclaré invalide.

Le repli doit être observable dans la réponse et l’interface.

## 44. Parcours Solo

Le parcours Solo retient :

- service sur `127.0.0.1` ;
- HTTP pour santé, capacités, appels courts et tâches ;
- WebSocket optionnel pour progression ;
- file en mémoire bornée ;
- un petit nombre de workers ;
- trois nouvelles tentatives maximum ;
- idempotence en mémoire ;
- repli déterministe ;
- aucun accès Internet requis.

## 45. Parcours Studio

Le parcours Studio ajoute :

- contrat d’API versionné ;
- schéma JSON partagé ;
- propriétaires des opérations ;
- quotas ;
- métriques de saturation ;
- tests de compatibilité ;
- tests de reconnexion ;
- tests de concurrence ;
- stratégie de migration ;
- persistance de tâches uniquement après décision d’architecture ;
- revue de confidentialité et sécurité au chapitre 13.

## 46. Erreurs fréquentes, pièges et corrections

<!-- qa:error-correction-section -->

### 46.1 Mettre les URL dans le gameplay

**Symptôme :** une fonctionnalité construit directement `/v1/tasks`.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
http.request("http://127.0.0.1:8765/v1/tasks")
```

**Correction :** appeler le port injecté.

> **[LECTURE] Architecture corrigée — Référence.**

```text
fonctionnalité → LocalAiGateway → adaptateur HTTP
```

**Différence :** le gameplay ne dépend plus de la route.

### 46.2 Utiliser WebSocket pour tout

**Symptôme :** une simple lecture de santé exige une connexion durable.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
Toute opération passe par WebSocket.
```

**Correction :** choisir selon le cycle de vie.

> **[LECTURE] Exemple corrigé — Référence.**

```text
santé et réponse unique : HTTP
progression et fragments : WebSocket
```

**Différence :** chaque transport répond à un besoin précis.

### 46.3 Réutiliser un `HTTPRequest` concurrent

**Symptôme :** la deuxième requête retourne une erreur d’occupation.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
_shared_http.request(url_a)
_shared_http.request(url_b)
```

**Correction :** utiliser une instance par appel sous une limite globale.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var http := HTTPRequest.new()
_requests[request_id] = http
```

**Différence :** les appels simultanés possèdent chacun leur état.

### 46.4 Traiter tout code HTTP comme un succès

**Symptôme :** un corps `500` est analysé comme un résultat métier.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if result == HTTPRequest.RESULT_SUCCESS:
	parse_result(body)
```

**Correction :** vérifier aussi `response_code`.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if response_code >= 200 and response_code < 300:
	parse_result(body)
```

**Différence :** succès du transport et succès HTTP sont séparés.

### 46.5 Réessayer immédiatement après `429`

**Symptôme :** le client aggrave la surcharge.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
while response_code == 429:
	send_again()
```

**Correction :** appliquer un délai borné et du jitter.

> **[LECTURE] Flux corrigé — Référence.**

```text
429 → Retry-After → attente + jitter → maximum 3 tentatives
```

**Différence :** la charge diminue au lieu d’augmenter.

### 46.6 Créer une file sans limite

**Symptôme :** la mémoire augmente tant que des tâches arrivent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
queue: list[TaskRecord] = []
queue.append(task)
```

**Correction :** utiliser une file bornée et refuser la surcharge.

> **[LECTURE] Exemple corrigé — Référence.**

```python
asyncio.PriorityQueue(maxsize=32)
```

**Différence :** la capacité est explicite et observable.

### 46.7 Confondre corrélation et idempotence

**Symptôme :** une clé de requête est réutilisée sans politique serveur.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```json
{"request_id":"same-for-ever"}
```

**Correction :** utiliser un identifiant d’appel et une clé d’idempotence au périmètre documenté.

> **[LECTURE] Exemple corrigé — Référence.**

```json
{
  "request_id":"session-a-00000042",
  "idempotency_key":"session-a-00000042"
}
```

**Différence :** corrélation et déduplication ont des responsabilités distinctes.

### 46.8 Accepter la même clé avec un autre payload

**Symptôme :** le serveur retourne une ancienne tâche pour une nouvelle demande.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
return tasks_by_key[idempotency_key]
```

**Correction :** comparer une empreinte canonique du payload.

> **[LECTURE] Flux corrigé — Référence.**

```text
même clé + même empreinte → même tâche
même clé + autre empreinte → 409
```

**Différence :** une collision ne change pas silencieusement le sens.

### 46.9 Considérer `cancel_requested` comme terminal

**Symptôme :** l’interface annonce l’arrêt alors que le worker calcule encore.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if state == CANCEL_REQUESTED:
	show_cancelled()
```

**Correction :** attendre `CANCELLED` ou un autre état terminal.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if AiTaskStatus.is_terminal(state):
	show_final_state()
```

**Différence :** une intention d’annulation n’est pas un résultat.

### 46.10 Appliquer les événements hors ordre

**Symptôme :** la progression recule après reconnexion.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
progress_bar.value = event.progress
```

**Correction :** vérifier `sequence`.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if event.sequence > last_sequence:
	progress_bar.value = event.progress
```

**Différence :** les événements anciens sont ignorés.

### 46.11 Présenter un fragment comme résultat final

**Symptôme :** un texte incomplet devient autoritaire.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
save_to_codex(streamed_text)
```

**Correction :** attendre la tâche terminale et récupérer le résultat final.

> **[LECTURE] Flux corrigé — Référence.**

```text
fragments → aperçu
SUCCEEDED → GET result → donnée finale
```

**Différence :** le flux améliore l’interface sans devenir la source d’autorité.

### 46.12 Exposer directement le schéma OpenAI au domaine

**Symptôme :** les fonctionnalités manipulent `choices[0].message`.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var text = response["choices"][0]["message"]["content"]
```

**Correction :** isoler la traduction.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var response := mapper.from_chat_completion(request_id, document)
```

**Différence :** le contrat interne reste stable si l’API externe change.

### 46.13 Faire confiance au statut `ready`

**Symptôme :** le serveur annonce prêt avant le chargement du modèle.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
ready = socket_is_open
```

**Correction :** calculer la santé depuis les dépendances nécessaires.

> **[LECTURE] Flux corrigé — Référence.**

```text
configuration valide + workers actifs + capacités chargées → ready
```

**Différence :** la santé décrit une disponibilité réelle.

### 46.14 Utiliser le WebSocket comme autorisation

**Symptôme :** connaître un `task_id` permet de s’y abonner.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
subscriptions.add(task_id)
```

**Correction :** vérifier l’autorisation avant abonnement.

> **[LECTURE] Flux corrigé — Référence.**

```text
identité → politique → tâche autorisée → abonnement
```

**Différence :** l’identifiant n’est pas un secret d’accès.

### 46.15 Promettre la persistance des tâches

**Symptôme :** la documentation affirme qu’une tâche survit au redémarrage.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
La file en mémoire garantit la reprise après panne.
```

**Correction :** déclarer la limite.

> **[LECTURE] Formulation corrigée — Référence.**

```text
Le registre du chapitre est volatil. Une persistance exigera un contrat distinct.
```

**Différence :** la capacité réelle n’est pas surévaluée.

### 46.16 Masquer une erreur de protocole par le repli

**Symptôme :** une réponse incompatible paraît être une simple indisponibilité.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if not response.is_success():
	return fallback()
```

**Correction :** limiter le repli aux familles prévues.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if response.error.code in [UNAVAILABLE, TIMEOUT]:
	return fallback()
```

**Différence :** les incompatibilités restent visibles.

## 47. Diagnostic

### 47.1 Connexion HTTP impossible

Vérifier :

- le serveur local ;
- l’adresse `127.0.0.1` ;
- le port ;
- l’état de santé ;
- le pare-feu local ;
- le délai ;
- le processus compagnon ou serveur.

### 47.2 Réponse `429`

Lire la capacité de file, `Retry-After`, le nombre de workers et les opérations longues. Ne pas augmenter aveuglément la file.

### 47.3 WebSocket connecté sans événements

Vérifier l’abonnement, les autorisations, les identifiants de tâche, le polling du peer, le type texte et les numéros de séquence.

### 47.4 Progression bloquée

Relire l’état HTTP. Le WebSocket peut être interrompu alors que la tâche continue.

### 47.5 Résultat compatible OpenAI invalide

Vérifier le mapper, `choices`, `message`, `content`, `finish_reason` et la version réellement implémentée par le serveur.

## 48. Tests préparatoires

Conserver les cas :

- santé prête et dégradée ;
- capacité absente ;
- réponse HTTP valide ;
- JSON invalide ;
- corps trop grand ;
- codes `400`, `404`, `408`, `409`, `429`, `500`, `503` ;
- délai et annulation locale ;
- création idempotente ;
- conflit d’idempotence ;
- file pleine ;
- priorité égale ;
- annulation avant et pendant exécution ;
- événement dupliqué ou hors ordre ;
- déconnexion et reconnexion WebSocket ;
- polling de secours ;
- résultat final après fragments ;
- mapper OpenAI incomplet ;
- arrêt avec tâches en cours.

## 49. Critères d’acceptation

Le lecteur peut expliquer et montrer statiquement que :

- le gameplay dépend de `LocalAiGateway`, pas des routes ;
- HTTP gère les échanges bornés ;
- WebSocket gère les événements et flux pertinents ;
- santé et capacités sont distinctes ;
- les corps et paquets sont bornés ;
- les codes HTTP sont mappés ;
- les tâches possèdent des transitions explicites ;
- la file est bornée ;
- `429` exprime la backpressure ;
- l’idempotence refuse un payload différent ;
- l’annulation est coopérative ;
- les événements utilisent une séquence ;
- le résultat final est distinct des fragments ;
- la compatibilité OpenAI reste dans un mapper ;
- le repli ne masque pas les erreurs de contrat ;
- aucune persistance de tâches non implémentée n’est revendiquée.

## 50. Checklists

### 50.1 Solo

- [ ] Valider `AiNetworkConfig`.
- [ ] Créer le codec réseau.
- [ ] Créer l’adaptateur HTTP.
- [ ] Lire santé et capacités.
- [ ] Créer le canal WebSocket optionnel.
- [ ] Définir tâche, états et événements.
- [ ] Ajouter la file bornée.
- [ ] Ajouter idempotence et annulation.
- [ ] Ajouter polling de secours.
- [ ] Isoler le mapper compatible OpenAI.
- [ ] Conserver le repli.

### 50.2 Studio

- [ ] Versionner routes et schémas.
- [ ] Définir quotas et capacités.
- [ ] Mesurer saturation et latence.
- [ ] Tester concurrence et reconnexion.
- [ ] Tester compatibilité OpenAI.
- [ ] Définir une stratégie de migration.
- [ ] Décider explicitement de la persistance.
- [ ] Préparer le durcissement du chapitre 13.

## 51. Sources techniques

Sources principales relues pour l’audit statique du 19 juillet 2026 :

- [Godot Engine 4.7 — `HTTPRequest`](https://docs.godotengine.org/en/4.7/classes/class_httprequest.html) ;
- [Godot Engine 4.7 — `HTTPClient`](https://docs.godotengine.org/en/4.7/classes/class_httpclient.html) ;
- [Godot Engine 4.7 — `WebSocketPeer`](https://docs.godotengine.org/en/4.7/classes/class_websocketpeer.html) ;
- [Godot Engine 4.7 — tutoriel WebSocket](https://docs.godotengine.org/en/4.7/tutorials/networking/websocket.html) ;
- [Godot Engine 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html) ;
- [Python 3.12 — files `asyncio`](https://docs.python.org/3.12/library/asyncio-queue.html) ;
- [Python 3.12 — `dataclasses`](https://docs.python.org/3.12/library/dataclasses.html) ;
- [Python 3.12 — `enum.StrEnum`](https://docs.python.org/3.12/library/enum.html) ;
- [OpenAI API — Responses et événements de streaming](https://platform.openai.com/docs/api-reference/responses-streaming) ;
- schéma de l’API compatible OpenAI réellement ciblée par le serveur local.

Le chapitre n’impose pas un framework serveur Python. Cette décision doit être prise au moment de matérialiser le Starter Kit, puis la documentation officielle de ce framework doit être ajoutée au rapport runtime.

## 52. Réserves de validation

Ne sont pas exécutés :

- `HTTPRequest` avec Godot 4.7.1 sous Windows 11 ;
- les codes HTTP et limites de corps ;
- `WebSocketPeer`, reconnexion et paquets ;
- les files `asyncio` et workers ;
- la backpressure ;
- l’idempotence ;
- les annulations ;
- les priorités ;
- le streaming ;
- le mapper compatible OpenAI face à un serveur réel et à une version de schéma explicitement choisie ;
- le polling de secours ;
- l’arrêt avec tâches en cours ;
- le packaging et les exports.

Aucun PDF intermédiaire n’est construit.

## 53. Résultat attendu

`Project Asteria` possède désormais une architecture documentée pour communiquer avec des services IA locaux par HTTP et WebSocket sans coupler le gameplay au réseau.

Les appels courts, tâches longues, progressions et réponses compatibles OpenAI sont séparés. La surcharge est refusée explicitement, les événements sont ordonnés, les créations peuvent être idempotentes et le repli déterministe reste disponible.

Le chapitre 13 pourra maintenant durcir cette plateforme et séparer clairement les outils de production des services autorisés au runtime.
