---
title: "Audit — Companion Pack Pack 3 AI Library"
id: "CP-AUDIT-PACK-03"
status: "candidate"
version: "0.1.0"
audit-level: "candidate"
audit-date: "2026-07-30T05:55:00+02:00"
---

# Audit — AI Library

## Décision candidate

Le pack matérialise les composants prévus. La décision `runtime-tested` reste interdite avant exécution du workflow permanent.

## Portes prévues

- validation statique sans paquet tiers ;
- tests unitaires Python ;
- faux serveur HTTP ;
- faux serveur WebSocket ;
- reprises bornées et cache ;
- annulation avant transport ;
- interchangeabilité des trois adaptateurs ;
- import Godot ;
- bootstrap headless et Xvfb ;
- tests GDScript contre les faux serveurs ;
- arbre Git propre après runtime ;
- absence de secret et de PDF.

## Réserves

- aucun service Ollama, llama.cpp ou LocalAI réel ;
- aucun modèle ou poids ;
- aucune mesure de latence, débit, mémoire ou qualité ;
- aucun TLS ou réseau distant ;
- aucun streaming SSE ;
- aucun export Godot ;
- aucune licence globale.
