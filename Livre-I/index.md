---
title: "Livre I — Préparer la plateforme de développement IA"
id: "LIV-I-INDEX"
status: "in-progress"
version: "0.2.0"
---

# Livre I — Préparer la plateforme de développement IA

Ce livre couvre l’installation, la configuration et la validation de l’environnement local de développement et de création assistée par IA.

## Objectif

À la fin du Livre I, le lecteur doit disposer d’une plateforme locale documentée, récupérable et adaptée à la configuration de référence : AMD Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Windows 11.

## Chapitres

1. [Matériel, Windows, pilotes AMD et accélération locale](CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) — **rédigé**
2. Docker et Docker Compose — à rédiger
3. Open WebUI, Open Terminal et Vane — à rédiger
4. ComfyUI et workflows graphiques — à rédiger
5. LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat — à rédiger
6. Audio IA local : Voicebox, synthèse vocale, transcription et génération — à rédiger

## Principes du Livre I

- Windows constitue la plateforme principale.
- Les procédures doivent conserver un chemin CPU de secours.
- Les versions de pilotes, runtimes et modèles doivent être enregistrées.
- Les composants expérimentaux restent isolés des installations stables.
- Les voies officiellement prises en charge sont distinguées des solutions communautaires.
- Le Mode Solo limite le nombre de services permanents.
- Le Mode Studio ajoute registres, versions approuvées et déploiement progressif.

## État de la compatibilité AMD de référence

Au 18 juillet 2026, la RX 6750 XT est traitée comme une carte RDNA 2 `gfx1031` de 12 Go. Le parcours principal privilégie les backends officiellement documentés, Windows ML/DirectML lorsque le format et l’application le permettent, puis le CPU. ZLUDA reste optionnel et expérimental.

## Statut

Le milestone M2 est en cours. **Un chapitre sur six** est rédigé.
