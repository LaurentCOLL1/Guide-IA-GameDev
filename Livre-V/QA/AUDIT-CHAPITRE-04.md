---
title: "Audit — Livre V, fiche 04"
id: "DOC-L5-QA-AUDIT-CH04"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 4
last-verified: "2026-07-28T14:25:00+02:00"
audit-date: "2026-07-28T14:25:00+02:00"
audit-level: "static-review"
audited-document: "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 04 — Fiches des moteurs et backends IA

## Décision

**Acceptée au niveau `static-review`.** La fiche respecte le profil spécialisé du Livre V : cartes directement consultables, séparation des couches, matrices compactes, renvois fréquents vers les tutoriels propriétaires et absence de déploiement complet recopié.

## Couverture du plan maître

| Exigence | Résultat |
|---|---|
| Ollama, llama.cpp et LocalAI comparés | conforme |
| backends visuels et audio couverts | ComfyUI, CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP, faster-whisper, whisper.cpp et Piper |
| API et formats précisés | présents dans chaque carte et dans la matrice B |
| accélération et mémoire précisées | variables, limites et voies CPU/AMD visibles |
| sécurité qualifiée | boucle locale, privilèges, secrets, données et exposition réseau visibles |
| moteur, modèle, interface et orchestration distingués | matrice A et carte MOTEUR-00 |
| chemins CPU et AMD documentés | CPU de référence, Vulkan, DirectML, ZLUDA et ROCm/HIP |
| exemples minimaux | commandes de version, santé et observation intégrées aux cartes sans bloc de code |
| diagnostics courants | matrice C par couches |
| déploiements complets non recopiés | conforme |
| intégration Godot non recopiée | liens vers les chapitres 11 à 13 du Livre II |

## Frontières contrôlées

- La fiche 03 conserve les applications et outils.
- La fiche 04 décrit les moteurs, backends, API d’inférence et accélérations.
- La fiche 05 conservera les familles de modèles de langage.
- Les fiches 06 et 07 conserveront les modèles visuels et audio.
- Le chapitre 21 conservera les benchmarks et résultats mesurés.
- Le chapitre 22 conservera les matrices historiques de compatibilité.
- Les déploiements complets restent dans le Livre I.
- L’intégration applicative et le durcissement restent dans le Livre II.

## Contrôles de forme

| Contrôle | Résultat |
|---|---:|
| lignes | 363 |
| titres Markdown | 20 |
| fiches `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 83 |
| renvois vers les Livres I à IV | 57 |
| liens profonds vers des sous-sections | 52 |
| liens officiels | 9 |
| blocs clôturés | 0 |
| structure « Résultats d’apprentissage » importée | absente |
| synthèse finale `Project Asteria` importée | absente |
| déploiement complet recopié | absent |

## Exactitude et qualification

Les états techniques sont repris des documents propriétaires du dépôt, principalement vérifiés entre le `2026-07-18` et le `2026-07-19`.

La fiche distingue explicitement :

- moteur et modèle ;
- backend et moteur ;
- interface et API ;
- support officiel, possibilité technique et laboratoire ;
- revue documentaire et exécution runtime ;
- disponibilité CPU et accélération AMD ;
- licence du moteur et licence du modèle ou de la voix.

Les affirmations matérielles restent conditionnelles. Aucune compatibilité AMD n’est extrapolée d’un autre GPU, d’un autre système ou d’un autre moteur.

## Liens et ancres

Les cartes renvoient aux chapitres propriétaires des Livres I et II. Les fragments ciblent des titres stables : architecture, API, accélération, validation, diagnostic, sécurité ou séparation production/runtime.

Le validateur spécialisé du Livre V doit confirmer les 52 fragments sur la branche de pull request.

Les liens web sont nommés et visent des documentations ou dépôts officiels. Leur présence ne prouve pas qu’ils resteront accessibles ; aucun contrôle navigateur n’est revendiqué dans ce lot.

## Commandes minimales

Les commandes restent intégrées dans les cellules sous forme de vérifications de version, santé ou observation :

- `ollama --version` et `ollama ps` ;
- `llama-cli.exe --version` et le healthcheck de `llama-server` ;
- `docker compose config` et `/readyz` ;
- journaux et indicateurs CPU/GPU.

Elles ne constituent pas une procédure d’installation et n’ont pas été exécutées dans ce lot.

## Diagnostic

La matrice C impose un ordre par couches : modèle, moteur, backend, API, interface, orchestration et sécurité. Elle évite de conclure à une panne de modèle lorsque l’erreur appartient à l’endpoint, au conteneur ou au backend.

## Doublons et densité

- aucun titre dupliqué ;
- aucune carte dupliquée ;
- pas de reprise longue des chapitres sources ;
- les champs communs servent la consultation et non un formulaire vide ;
- les fiches voisines conservent leurs responsabilités ;
- les données de benchmark restent absentes tant qu’elles ne sont pas exécutées.

## Réserves

- aucun moteur, modèle, workflow, conteneur, serveur ou fichier audio n’a été exécuté ;
- aucune commande minimale n’a été lancée ;
- aucun lien web n’a été ouvert depuis un navigateur ;
- aucune accélération CPU, Vulkan, DirectML, ZLUDA, ROCm ou HIP n’a été mesurée ;
- aucun débit, temps de chargement, facteur temps réel, pic RAM ou VRAM n’est revendiqué ;
- aucune licence de modèle, voix ou déploiement organisationnel n’a été approuvée ;
- aucun artefact du Companion Pack ni PDF n’a été produit ;
- la licence globale et le balisage avancé de publication restent ouverts.

## Empreinte

L’empreinte du chapitre est enregistrée dans la preuve QA finale. Toute modification ultérieure exige une nouvelle empreinte et une nouvelle validation.
