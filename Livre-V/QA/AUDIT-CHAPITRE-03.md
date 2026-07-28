---
title: "Audit — Livre V, fiche 03"
id: "DOC-L5-QA-AUDIT-CH03"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 3
audit-date: "2026-07-28T13:42:52+02:00"
audit-level: "static-review"
audited-document: "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 03 — Fiches des logiciels et outils

## Décision

**Acceptée au niveau `static-review`.** La fiche respecte le profil spécialisé du Livre V : cartes directement consultables, matrices en premier, renvois fréquents vers les tutoriels propriétaires et absence de reprise des installations complètes.

## Couverture du plan maître

| Exigence | Résultat |
|---|---|
| Godot, Blender, VS Code, Git, Docker et ComfyUI documentés | conforme |
| outils associés utiles à la collection | Windows Terminal, PowerShell, WinGet, GitHub, Python, Open WebUI et Open Terminal ajoutés |
| rôle et installation minimale | présents dans chaque carte |
| formats et intégrations | présents dans chaque carte et dans la matrice B |
| alternatives et limites | présentes dans chaque carte |
| versions et dates | références datées ou règle explicite d’enregistrer la version réellement installée |
| tableau de compatibilité | matrice A présente |
| commandes minimales repérées | matrice C présente avec contexte `[PS]` |
| liens officiels | présents pour chaque outil ou famille |
| installations détaillées non recopiées | conforme |

## Frontières contrôlées

- La fiche 02 conserve les arbres de décision et pondérations.
- La fiche 03 décrit les applications et outils.
- Le chapitre 4 conserve les moteurs et backends IA.
- Les chapitres 5 à 7 conservent les modèles.
- Le chapitre 22 conservera les matrices de compatibilité versionnées.
- Le chapitre 23 conservera les comparatifs détaillés et coûts de migration.
- Les procédures complètes restent dans les Livres I à IV.

## Contrôles de forme

| Contrôle | Résultat |
|---|---:|
| lignes | 355 |
| titres Markdown | 19 |
| fiches `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 64 |
| renvois vers les Livres I à IV | 28 |
| liens profonds vers des sous-sections | 24 |
| blocs clôturés | 0 |
| structure « Résultats d’apprentissage » importée | absente |
| synthèse finale `Project Asteria` importée | absente |
| procédure d’installation complète recopiée | absente |

## Exactitude et qualification

Les versions citées proviennent des documents propriétaires du dépôt :

- PowerShell 7 et Windows Terminal, vérifiés le `2026-07-18` ;
- Git for Windows `2.55.0`, version observée le `2026-07-18` ;
- CPython `3.14.6` et repli `3.13.14`, état du `2026-07-18` ;
- Docker Desktop avec WSL 2, état du `2026-07-18` ;
- Godot `4.7.1-stable`, état du `2026-07-18` ;
- Blender `5.2.0` Stable, revue du `2026-07-22` ;
- ComfyUI `v0.28.0`, état du `2026-07-18`.

La fiche distingue explicitement une référence datée d’une dernière version, un support officiel d’une possibilité technique, et une revue documentaire d’une exécution runtime.

## Liens et ancres

Les cartes renvoient aux chapitres propriétaires des Livres I à IV. Les fragments ciblent des titres stables : rôle, installation, version, matrice de décision, sécurité ou niveau de preuve. Le validateur spécialisé du Livre V doit vérifier leur résolution sur la branche de PR.

Les liens web sont nommés et visent les documentations ou dépôts officiels des outils. Leur présence ne constitue pas une preuve d’accessibilité future ; le contrôle des liens morts reste une obligation de maintenance.

## Commandes minimales

La matrice C utilise uniquement des commandes de version, d’état ou d’identification. Elle n’installe, ne met à jour et ne supprime rien. Les paramètres fictifs `<installation>` et `<image>` sont signalés comme valeurs à remplacer.

Aucun bloc de code n’est nécessaire : les commandes tiennent dans les cellules et leur résultat attendu est décrit à côté.

## Doublons et densité

- aucun titre dupliqué ;
- aucune carte dupliquée ;
- pas de reprise longue des chapitres sources ;
- les cartes utilisent un contrat commun sans répéter son explication ;
- les différences entre outil, service, interface, moteur et source canonique restent visibles.

## Réserves

- aucune installation ou mise à jour n’a été exécutée ;
- aucune commande de la matrice C n’a été lancée ;
- aucun lien web n’a été testé depuis un navigateur dans ce lot ;
- aucune compatibilité matérielle n’a été mesurée ;
- aucun workflow ComfyUI, projet Godot, fichier Blender ou conteneur n’a été exécuté ;
- aucune licence organisationnelle Docker Desktop n’a été déterminée ;
- aucun artefact du Companion Pack ni PDF n’a été produit ;
- la licence globale et le balisage avancé de publication restent ouverts.

## Empreinte

L’empreinte du chapitre est enregistrée dans la preuve QA finale. Toute modification ultérieure exige une nouvelle empreinte et une nouvelle validation.
