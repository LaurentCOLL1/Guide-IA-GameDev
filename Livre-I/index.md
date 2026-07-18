---
title: "Livre I — Préparer la plateforme de développement IA"
id: "LIV-I-INDEX"
status: "in-progress"
version: "0.7.0"
---

# Livre I — Préparer la plateforme de développement IA

Ce livre couvre l’installation, la configuration et la validation de l’environnement local de développement et de création assistée par IA.

## Objectif

À la fin du Livre I, le lecteur doit disposer d’une plateforme locale documentée, récupérable et adaptée à la configuration de référence : AMD Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Windows 11.

## Chapitres

1. [Matériel, Windows, pilotes AMD et accélération locale](CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) — **rédigé**
2. [Docker et Docker Compose](CHAPITRE-02-Docker-et-Docker-Compose.md) — **rédigé**
3. [Open WebUI, Open Terminal et Vane](CHAPITRE-03-Open-WebUI-Open-Terminal-et-Vane.md) — **rédigé**
4. [ComfyUI et workflows graphiques](CHAPITRE-04-ComfyUI-et-workflows-graphiques.md) — **rédigé**
5. [LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat](CHAPITRE-05-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) — **rédigé**
6. [Audio IA local, voix, transcription, musique et effets](CHAPITRE-06-Audio-IA-local-voix-transcription-musique-et-effets.md) — **rédigé**

## Principes du Livre I

- Windows constitue la plateforme principale.
- Les procédures doivent conserver un chemin CPU de secours.
- Les versions de pilotes, runtimes et modèles doivent être enregistrées.
- Les composants expérimentaux restent isolés des installations stables.
- Les voies officiellement prises en charge sont distinguées des solutions communautaires.
- Le Mode Solo limite le nombre de services permanents.
- Le Mode Studio ajoute registres, versions approuvées et déploiement progressif.
- Les licences du code, des poids, des voix et des données sont contrôlées séparément.
- Les interfaces et APIs locales restent liées à l’hôte ou à un réseau interne par défaut.

## État de la plateforme de référence

Au 18 juillet 2026 :

- la RX 6750 XT est traitée comme une carte RDNA 2 `gfx1031` de 12 Go ;
- le parcours AMD privilégie les backends officiellement documentés, Windows ML ou DirectML lorsque l’application le permet, puis le CPU ;
- ZLUDA reste optionnel et expérimental ;
- Docker Desktop utilise le backend WSL 2 ;
- les services conteneurisés ne présument pas d’un accès au GPU AMD ;
- les calculs AMD lourds restent par défaut sur l’hôte Windows ;
- Open WebUI constitue l’interface centrale ;
- Open Terminal reste isolé sur un réseau Docker interne ;
- Vane est un moteur de recherche IA tiers et optionnel ;
- ComfyUI utilise une installation manuelle versionnée pour la RX 6750 XT ;
- un environnement CPU de référence reste disponible ;
- ZLUDA est limité à une installation de laboratoire séparée ;
- les modèles et workflows possèdent des manifestes et des empreintes ;
- Ollama natif Windows constitue le moteur LLM principal ;
- llama.cpp CPU et Vulkan servent de référence et de benchmark ;
- LocalAI et LibreChat restent optionnels selon le besoin d’orchestration ;
- Kokoro et Piper couvrent la synthèse légère ;
- Chatterbox et Voicebox couvrent les voix expressives avec consentement ;
- faster-whisper CPU INT8 constitue le parcours de transcription principal ;
- whisper.cpp fournit la référence autonome CPU/Vulkan ;
- AudioCraft est limité aux maquettes non commerciales avec les poids fournis.

## Validation restante

Les six chapitres sont rédigés et intégrés à `contents.txt`. Le milestone reste ouvert jusqu’à :

- la validation structurelle des métadonnées et liens ;
- la compilation Pandoc/XeLaTeX de l’ensemble mis à jour ;
- la vérification visuelle du PDF ;
- la rédaction du rapport QA du Livre I ;
- la confirmation que les avertissements de licences sont correctement bloquants avant publication.

## Statut

Le milestone M2 est en cours. **Les six chapitres sur six sont rédigés ; la validation technique et documentaire reste à effectuer.**