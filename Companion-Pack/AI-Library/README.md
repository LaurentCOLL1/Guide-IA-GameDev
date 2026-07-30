---
title: "Companion Pack — AI Library"
id: "CP-PACK-03-AI-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T06:36:00+02:00"
validation-status: "runtime-tested-linux"
validation-report: "Companion-Pack/AI-Library/qa/AUDIT-AI-LIBRARY.md"
redistribution-status: "pending-global-license"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
---

# AI Library

Le Pack 3 matérialise une couche IA locale remplaçable pour `Project Asteria`. Le jeu dépend de contrats stables ; les fournisseurs, transports et politiques restent injectés à la périphérie.

## État du lot

| Élément | État |
|---|---|
| contrats de requête, réponse, erreur et capacité | matérialisés |
| client HTTP JSON | matérialisé |
| client WebSocket texte | matérialisé |
| sous-ensemble OpenAI-compatible | matérialisé |
| adaptateurs Ollama, llama.cpp server et LocalAI | matérialisés |
| délais et reprises bornées | matérialisés |
| annulation coopérative | matérialisée |
| file bornée et backpressure | matérialisées |
| cache TTL/LRU en mémoire | matérialisé |
| faux serveurs HTTP et WebSocket | matérialisés |
| filtres de sécurité d’entrée et rédaction | matérialisés |
| exemple Godot | matérialisé |
| qualification Python et mocks | validée par le run `30514201037` |
| import, lancements et tests Godot | validés sur Linux x86_64 par le run `30514201037` |
| service fournisseur réel | non exécuté |
| modèle réel | non téléchargé |
| performance | non mesurée |
| licence globale | non décidée |

La qualification obligatoire utilise uniquement les faux serveurs inclus, liés à `127.0.0.1`. Les tests optionnels contre un service local réel sont séparés et ne sont jamais exécutés sans action explicite.

## Qualification obtenue

Le run `30514201037` a validé 51 fichiers sources, 13 tests Python, les faux serveurs HTTP et WebSocket sur boucle locale, l’import Godot, les lancements headless et Xvfb Compatibility, puis les tests GDScript avec `AI_LIBRARY_GODOT_TESTS: PASS`. L’arbre Git est resté propre après runtime.

Godot qualifié : `4.7.1.stable.official.a13da4feb`. Archive Linux SHA-256 : `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.

Cette qualification ne couvre aucun service fournisseur réel, aucun modèle, aucune performance, aucune qualité de sortie et aucune exposition réseau distante.

## Architecture

```text
fonctionnalité Godot ou Python
        ↓
contrat AiRequest / AiResponse
        ↓
AiClient
 ├── SafetyPolicy
 ├── TTLCache
 ├── RetryPolicy
 └── CancellationToken
        ↓
OpenAICompatibleAdapter
        ↓
HttpJsonTransport
        ↓
Ollama | llama.cpp server | LocalAI | faux serveur
```

Le WebSocket est un canal d’événements corrélé. Il ne devient pas un second port métier.

## Sous-ensemble commun

Le pack qualifie un sous-ensemble volontairement étroit :

- `GET /v1/models` ;
- `POST /v1/chat/completions` sans streaming HTTP ;
- messages texte `system`, `user`, `assistant` ;
- erreurs HTTP bornées ;
- événements WebSocket JSON textuels corrélés.

Les extensions fournisseur restent hors du contrat commun. Une compatibilité annoncée par un fournisseur ne garantit pas que toutes les options OpenAI soient identiques.

## Exécuter les tests Python

Depuis la racine du dépôt :

```powershell
$env:PYTHONPATH = "Companion-Pack/AI-Library/src"
python -m unittest discover `
  -s Companion-Pack/AI-Library/tests `
  -v
```

Aucun paquet Python tiers n’est requis.

## Démarrer les faux serveurs

```powershell
$env:PYTHONPATH = "Companion-Pack/AI-Library/src"
python -m asteria_ai.mock_server `
  --http-port 8765 `
  --ws-port 8766
```

Les réponses portent le marqueur `mock-provider`. Elles ne proviennent d’aucun modèle.

## Exemple Python

```python
from asteria_ai import (
    AiClient,
    AiClientConfig,
    AiMessage,
    AiRequest,
    ProviderKind,
)

config = AiClientConfig.for_provider(
    ProviderKind.OLLAMA,
    base_url="http://127.0.0.1:8765",
)
client = AiClient(config)
response = client.chat(
    AiRequest.chat(
        request_id="demo-001",
        model="mock-model",
        messages=[AiMessage(role="user", content="Bonjour")],
    )
)
print(response.text)
```

Dans la qualification, l’URL ci-dessus vise le faux serveur. Le choix `OLLAMA` ne prouve pas qu’Ollama est installé ou disponible.

## Exemple Godot

Le dossier `godot-example/` contient :

- une configuration réseau limitée à la boucle locale ;
- un mapper OpenAI-compatible ;
- un client HTTP avec `HTTPRequest` ;
- un canal WebSocket avec `WebSocketPeer` ;
- une scène de bootstrap ;
- un test headless contre les faux serveurs.

## Comportement dégradé

Le pack ne fabrique jamais une fausse réponse générative lorsque le service est absent. L’appelant reçoit une erreur typée et décide d’un repli local déterministe. Voir [DEGRADED-MODE.md](docs/DEGRADED-MODE.md).

## Sécurité

- boucle locale par défaut ;
- hôtes distants refusés par défaut ;
- taille, temps, file et nombre de reprises bornés ;
- opérations autorisées par liste fermée ;
- secrets lus uniquement depuis une variable d’environnement explicitement nommée ;
- valeurs d’authentification exclues des journaux et rapports ;
- aucune donnée personnelle, aucun secret et aucun payload utilisateur réel dans les fixtures.

Voir [SECURITY.md](docs/SECURITY.md).

## Fournisseurs

| Fournisseur | URL locale indicative | Contrat utilisé |
|---|---|---|
| Ollama | `http://127.0.0.1:11434` | sous-ensemble OpenAI-compatible |
| llama.cpp server | `http://127.0.0.1:8080` | sous-ensemble OpenAI-compatible |
| LocalAI | `http://127.0.0.1:8080` | sous-ensemble OpenAI-compatible |

Ces valeurs sont des défauts documentaires. Elles ne constituent ni une découverte de service, ni une preuve de compatibilité d’une version donnée.

## Sources officielles de contrat

- Ollama, compatibilité OpenAI : <https://docs.ollama.com/api/openai-compatibility>
- llama.cpp server : <https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md>
- LocalAI, présentation : <https://localai.io/docs/overview/index.html>
- Godot `HTTPRequest` : <https://docs.godotengine.org/en/4.7/classes/class_httprequest.html>
- Godot `WebSocketPeer` : <https://docs.godotengine.org/en/4.7/classes/class_websocketpeer.html>

## Nettoyage

Les tests n’écrivent que dans les dossiers temporaires du système et dans `dist/` en CI. Pour arrêter les faux serveurs, interrompre le processus. Aucun daemon ni service système n’est installé.

## Limites

Ce pack ne qualifie pas :

- un modèle, poids, tokenizer ou template de conversation réel ;
- la fidélité complète à une API fournisseur ;
- TLS, authentification distante ou exposition Internet ;
- le streaming SSE ;
- les outils, fonctions, multimodalité ou embeddings fournisseur ;
- la qualité des réponses ;
- les performances, la concurrence réelle ou la consommation mémoire ;
- Windows graphique, Forward+ sur GPU réel ou un export Godot ;
- une licence globale ou une archive redistribuable.
