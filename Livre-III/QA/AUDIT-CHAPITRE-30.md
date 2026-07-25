---
title: "Audit post-création — Livre III, chapitre 30"
id: "DOC-L3-QA-AUDIT-CH30"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L3-CH30"
chapter-version: "1.0.0"
audit-date: "2026-07-25T09:40:18+02:00"
last-verified: "2026-07-25T09:40:18+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 30

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation du pilote de lot, des scripts Blender, des workflows ComfyUI API, de l’orchestrateur Python, des profils de ressources, des checkpoints, de la CI artistique, des revues humaines et du PDF de fin de Livre.

Aucun lot, source copiée, export GLB, workflow exécuté, image générée, import Godot, checkpoint, reprise, rapport runtime, artefact CI, approbation artistique, benchmark ou PDF n’est revendiqué comme produit ou exécuté.

## 2. Périmètre comparé au plan maître

Le chapitre couvre la sélection des tâches automatisables, les scripts Blender idempotents et paramétrés, les files ComfyUI, workflows et seeds, les manifestes de lots, identités, provenance, reprise après échec, limites de tentatives, échantillonnage, validation humaine, intégration CI, artefacts et rapports.

Les livrables prévus sont préparés comme contrats : `AST-ART-BATCH-PLAN-001`, `AST-ART-BATCH-PROFILES-001`, jobs Blender, manifeste ComfyUI, runner borné, checkpoint vérifié, rapport de lot, planche comparative, workflow CI et exemples du Companion Pack. Leur matérialisation reste en réserve.

## 3. Frontières contrôlées

- le chapitre 3 conserve workflows, modèles, custom nodes, seeds et décisions de concept ;
- le chapitre 4 conserve sources Blender, collections d’export et conventions de livraison ;
- le chapitre 28 conserve les profils d’import et de réimportation Godot ;
- le chapitre 29 conserve la porte qualité d’un candidat individuel et la décision finale ;
- le Livre II, chapitre 29 conserve les primitives Python génériques ;
- le chapitre 30 conserve le plan de lot, l’ordonnancement, la reprise, les quotas, l’échantillonnage et la CI ;
- aucun script, job, workflow, événement ou statut de lot n’applique une règle gameplay ;
- aucune réussite automatique ne devient une approbation artistique.

## 4. Contrôles pédagogiques

- identité de lot, run, tâche, tentative et artefact séparées ;
- classification déterministe, générative et humaine documentée ;
- manifeste fermé, graphe acyclique, machine d’états, préconditions et postconditions définis ;
- idempotence, copie isolée, lancement Blender en arrière-plan et contexte `bpy.ops` encadrés ;
- rapports Blender, profils GLB et postconditions d’export documentés ;
- workflow ComfyUI API, file locale, suivi, seeds, modèles, custom nodes et quarantaine encadrés ;
- classes de ressources, concurrence, exclusivité GPU, backpressure, délais et annulation expliqués ;
- retries bornés, taxonomie des échecs, checkpoints et reprise par empreintes documentés ;
- staging, promotion, provenance, JSON canonique, journaux et rapports structurés ;
- échantillonnage, planche comparative et approbation humaine indépendante documentés ;
- CI, matrice, artefacts, secrets, réseau, quotas, conservation et Companion Pack préparés ;
- modes Solo et Studio documentés en Markdown ordinaire ;
- fonctions, paramètres, types, retours et effets de bord explicités ;
- chaque bloc significatif possède un repère et une explication structurée ;
- dix diagnostics suivent symptôme, exemple fautif, raison, correction et raison ;
- sources officielles fournies sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 2426 ;
- titres : 71 ;
- blocs code ou données : 77 ;
- marqueurs d’explication : 77 ;
- explications structurées hors diagnostics : 57 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- absence de prochaine action et de recommandation GPT dans le texte lecteur ;
- PDF non produit.

## 6. Exactitude technique

La revue statique s’appuie sur la documentation Blender pour l’ordre des arguments, `--background`, `--python`, `--python-exit-code`, le séparateur `--`, les accès `bpy.data`, les opérateurs et l’export glTF.

La documentation ComfyUI confirme le graphe de workflow, la soumission locale à `/prompt`, l’identité `prompt_id`, la file, l’historique, l’interruption et les messages WebSocket. Le chapitre distingue la réussite d’exécution de la sélection artistique.

La documentation GitHub Actions confirme les matrices, la concurrence et les artefacts. La documentation Godot 4.7 conserve l’import et les scripts headless. Les primitives Python suivent les contrats du Livre II pour `subprocess`, `concurrent.futures`, JSON canonique, SHA-256, checkpoint et staging.

Les capacités, délais, tailles, budgets, taux d’échec, temps d’exécution et performances restent des champs de profils ou des réserves en attente de mesure.

## 7. Réserves ouvertes

- pilote `AST-PRODUCTION-BATCH-SCOUT-RELAY-001` non matérialisé ;
- aucun plan, schéma, profil ou runner réel créé ;
- aucun script Blender exécuté en arrière-plan ;
- aucun workflow ComfyUI API soumis ni suivi ;
- aucun modèle ou custom node qualifié par le chapitre 30 ;
- aucune sortie générative placée en quarantaine réelle ;
- aucun import ou contrôle Godot de lot exécuté ;
- aucune concurrence, backpressure, annulation ou retry testé ;
- aucun checkpoint, incident ni reprise démontré ;
- aucun staging ou mécanisme de promotion exécuté ;
- aucun rapport, journal, manifeste ou artefact runtime produit ;
- aucun échantillon ni approbation humaine réalisé ;
- aucune CI artistique ou matrice de runners exécutée ;
- exemples du Companion Pack non matérialisés ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III différé à la clôture de fin de Livre.

## 8. Conclusion

Le chapitre satisfait le plan maître et peut entrer dans la validation légère sans PDF. La preuve finale restera `pending` jusqu’à la réussite des workflows permanents sur la branche documentaire. La clôture du Livre III et sa compilation PDF constituent une étape distincte après fusion du chapitre.
