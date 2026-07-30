# Architecture de l’AI Library

## Frontières

1. Le domaine formule une intention.
2. `AiRequest` représente le contrat.
3. `AiClient` applique sécurité, cache, reprise et annulation.
4. `OpenAICompatibleAdapter` traduit le contrat vers le sous-ensemble réseau.
5. `HttpJsonTransport` transporte des octets.
6. Le fournisseur ou le faux serveur traite la requête.

La logique de jeu ne connaît ni URL, ni en-tête, ni nom de fournisseur.

## Fournisseurs interchangeables

Les adaptateurs Ollama, llama.cpp server et LocalAI utilisent le même mapper conservateur. Ils ne promettent pas une identité complète des extensions, erreurs, métadonnées, templates ou capacités.

## WebSocket

Le canal WebSocket transporte des événements JSON textuels :

```json
{
  "event": "task.progress",
  "request_id": "demo-001",
  "sequence": 1,
  "payload": {"progress": 0.5}
}
```

Une trame sans `request_id` ou avec un objet JSON invalide est refusée.

## Cache

Le cache est :

- en mémoire ;
- borné par nombre d’entrées ;
- expiré par horloge monotone ;
- indexé par empreinte canonique de requête ;
- jamais présenté comme une persistance.

## File

La file est bornée et ordonnée par priorité puis séquence d’arrivée. Une saturation produit `QueueFullError` au lieu d’une croissance silencieuse.

## Reprises

Une reprise est autorisée seulement pour les statuts explicitement transitoires. Les délais et le nombre de tentatives restent bornés. Une requête annulée n’est pas rejouée.
