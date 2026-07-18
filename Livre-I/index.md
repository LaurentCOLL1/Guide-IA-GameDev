---
title: "Livre I — Préparer la plateforme de développement IA"
id: "LIV-I-INDEX"
status: "complete"
version: "1.3.0"
---

# Livre I — Préparer la plateforme de développement IA

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

Ce livre couvre l’installation, la configuration, la compréhension et la validation de l’environnement local de développement et de création assistée par IA.

## Objectif

À la fin du Livre I, le lecteur doit disposer d’une plateforme locale documentée, récupérable et adaptée à la configuration de référence : AMD Radeon RX 6750 XT 12 Go, Ryzen 7 2700, 32 Go de RAM et Windows 11.

Le Livre I fournit également les bases nécessaires à un débutant complet : terminal, fichiers, Git, éditeur, Python, environnements isolés, secrets et restauration.

## Chapitres

1. [Matériel, Windows, pilotes AMD et accélération locale](CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md) — **rédigé, validé et audité**
2. [Terminal, PowerShell et outils Windows](CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md) — **rédigé, validé et audité**
3. [Git, GitHub et Visual Studio Code](CHAPITRE-03-Git-GitHub-et-VS-Code.md) — **rédigé, validé et audité**
4. [Python et environnements virtuels](CHAPITRE-04-Python-et-environnements-virtuels.md) — **rédigé, validé et audité**
5. [Docker et Docker Compose](CHAPITRE-05-Docker-et-Docker-Compose.md) — **rédigé, validé et audité**
6. [Open WebUI, Open Terminal et Vane](CHAPITRE-06-Open-WebUI-Open-Terminal-et-Vane.md) — **rédigé, validé et audité**
7. [ComfyUI et workflows graphiques](CHAPITRE-07-ComfyUI-et-workflows-graphiques.md) — **rédigé, validé et audité**
8. [LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat](CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) — **rédigé, validé et audité**
9. [Audio IA local, voix, transcription, musique et effets](CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md) — **rédigé, validé et audité**
10. [Sécurité, sauvegarde et validation de la plateforme](CHAPITRE-10-Securite-sauvegarde-et-validation-de-la-plateforme.md) — **rédigé, validé et audité**

## Audit transversal des contextes d’utilisation

Les dix chapitres appliquent désormais la convention `DOC-V0-ANN-CONTEXTES`. Chaque commande précise son terminal, chaque contenu de fichier précise l’éditeur et le chemin cible, les liens procéduraux utilisent **[WEB]**, et les sorties utilisent **[SORTIE]**.

Le rapport est disponible dans [`Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md`](../Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md). La validation est statique : les procédures nécessitant le matériel ou les services réels conservent une réserve runtime.

## Stabilité des identifiants

Les chapitres historiques Docker, Open WebUI, ComfyUI, LLM et audio ont été déplacés dans l’ordre pédagogique sans modifier leurs identifiants stables :

| Ordre actuel | Identifiant conservé | Ancien ordre |
|---:|---|---:|
| 5 | `DOC-L1-CH02` | 2 |
| 6 | `DOC-L1-CH03` | 3 |
| 7 | `DOC-L1-CH04` | 4 |
| 8 | `DOC-L1-CH05` | 5 |
| 9 | `DOC-L1-CH06` | 6 |

Les nouveaux chapitres utilisent des identifiants sémantiques afin de ne pas réattribuer un identifiant déjà publié.

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
- Les interfaces et APIs locales restent liées à l’hôte ou à un réseau interne par défaut.
- Une sauvegarde n’est validée qu’après une restauration testée.

## État de la plateforme de référence

Au 18 juillet 2026 :

- la RX 6750 XT est traitée comme une carte RDNA 2 `gfx1031` de 12 Go ;
- le parcours AMD privilégie les backends officiellement documentés, Windows ML ou DirectML lorsque l’application le permet, puis le CPU ;
- ZLUDA reste optionnel et expérimental ;
- PowerShell 7 et Windows Terminal constituent le shell et le terminal principaux ;
- Git, GitHub et VS Code forment la chaîne de versionnement et d’édition ;
- Python est isolé par application, avec `venv` ou `uv` selon le projet ;
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

## Assurance qualité

Le [rapport QA final](RAPPORT-QA-FINAL.md) remplace la validation historique à six chapitres.

Le workflow `Validate Documentation` a contrôlé :

- 37 sources déclarées ;
- les 10 chapitres du Livre I dans l’ordre 01 à 10 ;
- 36 identifiants uniques ;
- les identifiants historiques préservés après déplacement ;
- les métadonnées et liens locaux ;
- la compilation Pandoc/XeLaTeX.

La compilation a produit un PDF A4 de **396 pages**, dont le texte est extractible. Un échantillon de **82 pages** a été contrôlé visuellement sans défaut bloquant observé.

Deux réserves restent liées à la publication et non à M2 :

- la licence globale du projet doit être définie ;
- le PDF final devra être balisé pour améliorer l’accessibilité aux lecteurs d’écran.

## Statut

Le milestone **M2 — Livre I : Préparer la plateforme** est terminé sur sa structure corrigée à dix chapitres. La prochaine phase active est **M3 — Livre II : Développement et architecture**.
