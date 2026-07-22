---
title: "Livre I — Préparer la plateforme de développement IA"
id: "LIV-I-INDEX"
status: "complete"
version: "1.4.0"
---

# Livre I — Préparer la plateforme de développement IA

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

Ce livre couvre l’installation, la configuration, la compréhension et la validation pratique de l’environnement local de développement et de création assistée par IA.

## Objectif

À la fin du Livre I, le lecteur doit disposer d’une plateforme locale documentée, récupérable et adaptée à la configuration de référence : AMD Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Windows 11.

Le Livre I fournit également les bases nécessaires à un débutant complet : terminal, fichiers, Git, éditeur, Python, environnements isolés, secrets et restauration.

## Chapitres

1. [Matériel, Windows, pilotes AMD et accélération locale](CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md)
2. [Terminal, PowerShell et outils Windows](CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md)
3. [Git, GitHub et Visual Studio Code](CHAPITRE-03-Git-GitHub-et-VS-Code.md)
4. [Python et environnements virtuels](CHAPITRE-04-Python-et-environnements-virtuels.md)
5. [Docker et Docker Compose](CHAPITRE-05-Docker-et-Docker-Compose.md)
6. [Open WebUI, Open Terminal et Vane](CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md)
7. [ComfyUI et workflows graphiques](CHAPITRE-07-ComfyUI-et-workflows-graphiques.md)
8. [LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat](CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md)
9. [Audio IA local, voix, transcription, musique et effets](CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md)
10. [Sécurité, sauvegarde et validation de la plateforme](CHAPITRE-10-Securite-sauvegarde-et-validation-de-la-plateforme.md)

## Principes du Livre I

- Windows constitue la plateforme principale.
- Les commandes sont expliquées avant d’être utilisées.
- Les procédures conservent un chemin CPU de secours.
- Les versions de pilotes, runtimes et modèles sont enregistrées.
- Les composants expérimentaux restent isolés des installations stables.
- Les voies officiellement prises en charge sont distinguées des solutions communautaires.
- Git versionne les sources, mais ne remplace pas les sauvegardes des données uniques.
- Chaque application Python possède un environnement isolé et reconstructible.
- Le Mode Solo limite le nombre de services permanents.
- Le Mode Studio ajoute registres, versions approuvées et déploiement progressif.
- Les licences du code, des poids, des voix et des données sont contrôlées séparément.
- Les interfaces et API locales restent liées à l’hôte ou à un réseau interne par défaut.
- Une sauvegarde n’est validée qu’après une restauration testée.

## Plateforme de référence

- RX 6750 XT, architecture RDNA 2 et 12 Go de VRAM ;
- PowerShell 7 et Windows Terminal ;
- Git, GitHub et Visual Studio Code ;
- environnements Python isolés ;
- Docker Desktop avec WSL 2 ;
- Open WebUI comme interface centrale ;
- ComfyUI installé et versionné séparément ;
- Ollama natif Windows comme moteur LLM principal ;
- chemins CPU et solutions de repli conservés lorsque l’accélération AMD n’est pas qualifiée.
