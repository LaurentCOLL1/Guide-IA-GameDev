---
title: "Plan maître détaillé — Livre V"
id: "DOC-PLAN-L5"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
book: "Livre V"
chapter-count: 26
---

# Plan maître détaillé — Livre V

> **Titre du Livre :** Encyclopédie technique et bibliothèque de référence  
> **Statut :** non commencé  
> **Rôle :** fournir une référence non linéaire, stable et directement consultable sans dupliquer les tutoriels complets des Livres I à IV.

## Règles transversales du Livre V

Chaque fiche doit inclure : identifiant, objectif, public, prérequis, version vérifiée, date, licence, compatibilité matérielle, procédure minimale, erreurs fréquentes, alternatives, sources et liens vers les tutoriels complets. Les fiches doivent privilégier tableaux, décisions et exemples minimaux plutôt que longues procédures répétées.

## Chapitre 1 — Carte générale de la collection

**Objectifs**

- représenter la structure Volume 0, Livres I à V et Companion Pack ;
- montrer dépendances et parcours Solo/Studio ;
- permettre une entrée par besoin, outil ou système ;
- identifier prérequis et ordre conseillé.

**Livrables**

- carte de navigation ;
- matrice Livre/compétence ;
- parcours débutant, production et dépannage ;
- index des prérequis.

**Frontière et validation**

Ne résume pas tout le contenu. Validation par capacité à retrouver rapidement le bon chapitre à partir d’un besoin concret.

## Chapitre 2 — Arbres de décision

**Objectifs**

- guider les choix d’outils, formats, moteurs et pipelines ;
- expliciter critères, contraintes et conséquences ;
- fournir chemins AMD, CPU, Solo et Studio ;
- signaler situations où aucune solution unique n’existe.

**Livrables**

- arbres décisionnels ;
- critères pondérés ;
- exemples de décisions ;
- renvois vers les chapitres sources.

**Frontière et validation**

Les arbres ne doivent pas masquer les compromis. Validation avec plusieurs scénarios matériels et organisationnels.

## Chapitre 3 — Fiches des logiciels et outils

**Objectifs**

- documenter Godot, Blender, VS Code, Git, Docker, ComfyUI et outils associés ;
- préciser rôle, installation minimale, formats et intégrations ;
- indiquer alternatives et limites ;
- conserver versions et dates de vérification.

**Livrables**

- fiche normalisée par outil ;
- tableau de compatibilité ;
- commandes minimales repérées ;
- liens officiels.

**Frontière et validation**

Les installations détaillées restent dans les Livres I à IV. Validation par exactitude et absence de liens morts.

## Chapitre 4 — Fiches des moteurs et backends IA

**Objectifs**

- comparer Ollama, llama.cpp, LocalAI et backends visuels/audio ;
- préciser API, formats, accélération, mémoire et sécurité ;
- distinguer moteur, modèle, interface et orchestration ;
- documenter chemins CPU/AMD.

**Livrables**

- fiches moteurs ;
- matrice API/accélération ;
- exemples minimaux ;
- diagnostics courants.

**Frontière et validation**

Les déploiements complets restent dans le Livre I et l’intégration dans le Livre II.

## Chapitre 5 — Fiches des modèles de langage

**Objectifs**

- enregistrer familles, tailles, quantifications et contextes ;
- préciser licence, usage, langues et exigences mémoire ;
- proposer tests reproductibles ;
- distinguer recommandation générale et résultat matériel spécifique.

**Livrables**

- fiches modèles ;
- benchmarks ;
- prompts de test ;
- matrice de sélection.

**Frontière et validation**

Aucun modèle n’est présenté comme meilleur universellement. Validation par sources, licence et mesures datées.

## Chapitre 6 — Fiches des modèles visuels

**Objectifs**

- documenter checkpoints, VAEs, ControlNet, LoRA et upscalers ;
- préciser licence, provenance, format et besoins VRAM ;
- enregistrer résolution, sampler et workflow de test ;
- signaler contenus ou usages restreints.

**Livrables**

- fiches modèles ;
- manifestes ;
- images de test ;
- matrice compatibilité ComfyUI.

**Frontière et validation**

La création artistique reste au Livre III. Validation par workflow reproductible et empreinte du fichier.

## Chapitre 7 — Fiches des modèles audio

**Objectifs**

- documenter TTS, STT, musique et effets ;
- préciser langues, voix, licences et consentements ;
- mesurer vitesse, mémoire et qualité ;
- distinguer voix synthétique et clonage.

**Livrables**

- fiches modèles ;
- échantillons autorisés ;
- benchmarks ;
- formulaires de provenance/consentement.

**Frontière et validation**

Aucun clonage vocal sans consentement explicite. Validation par licence et traçabilité.

## Chapitre 8 — Bibliothèque de workflows

**Objectifs**

- cataloguer workflows Godot, Blender, ComfyUI, audio et documentation ;
- indiquer entrées, sorties, dépendances et étapes ;
- fournir versions Solo/Studio ;
- permettre reproduction et adaptation.

**Livrables**

- fiches workflow ;
- diagrammes ;
- fichiers réutilisables ;
- checklists.

**Frontière et validation**

Les tutoriels restent dans leurs Livres. Validation par exécution du workflow minimal.

## Chapitre 9 — Bibliothèque de prompts

**Objectifs**

- organiser prompts par tâche et modèle ;
- enregistrer variables, contraintes et résultats attendus ;
- documenter limites, biais et sécurité ;
- éviter prompts magiques non expliqués.

**Livrables**

- templates paramétrés ;
- jeux de tests ;
- exemples de sorties ;
- critères d’évaluation.

**Frontière et validation**

Chaque prompt doit indiquer modèle et version. Validation par résultats reproductibles ou variance documentée.

## Chapitre 10 — Bibliothèque de scripts et recettes de code

**Objectifs**

- fournir scripts courts GDScript, Python, PowerShell et Bash ;
- expliquer contexte, paramètres, sorties et erreurs ;
- distinguer recette pédagogique et composant de production ;
- inclure tests minimaux.

**Livrables**

- recettes versionnées ;
- exemples d’appel ;
- tests ;
- licences.

**Frontière et validation**

Le code complexe appartient au Companion Pack. Validation par exécution ou statut statique explicite.

## Chapitre 11 — Référence GDScript

**Objectifs**

- résumer syntaxe, types, fonctions, classes, annotations et collections ;
- fournir index des opérateurs et fonctions courantes ;
- relier chaque notion au chapitre pédagogique ;
- documenter pièges et versions.

**Livrables**

- aide-mémoire ;
- tables de syntaxe ;
- exemples minimaux ;
- index alphabétique.

**Frontière et validation**

Ne remplace pas le chapitre d’apprentissage. Validation contre la documentation officielle de la version de référence.

## Chapitre 12 — Référence Python

**Objectifs**

- couvrir environnements, types, fonctions, fichiers, CLI et tests ;
- cibler automatisation et outils du guide ;
- documenter dépendances et packaging ;
- fournir correspondances avec GDScript.

**Livrables**

- aide-mémoire ;
- recettes ;
- conventions ;
- matrice Python/GDScript.

**Frontière et validation**

Ne devient pas un cours Python général. Validation par scripts du Companion Pack.

## Chapitre 13 — Structures JSON et formats d’échange

**Objectifs**

- documenter JSON, JSONL, CSV, YAML et formats Godot ;
- définir encodage, schémas, version et validation ;
- préciser avantages, limites et sécurité ;
- proposer structures canoniques.

**Livrables**

- fiches formats ;
- schémas ;
- exemples valides/invalides ;
- convertisseurs.

**Frontière et validation**

Les usages détaillés restent aux Livres I et II. Validation avec validateurs automatiques.

## Chapitre 14 — Schémas SQLite et migrations

**Objectifs**

- cataloguer types, clés, contraintes et index ;
- fournir modèles de migrations ;
- documenter transactions, sauvegarde et restauration ;
- proposer schémas de référence du projet.

**Livrables**

- DDL ;
- migrations ;
- diagrammes ;
- requêtes de diagnostic.

**Frontière et validation**

Le tutoriel d’intégration est au Livre II. Validation par création et migration d’une base de test.

## Chapitre 15 — Bases vectorielles et recherche sémantique

**Objectifs**

- référencer concepts, métriques et solutions locales ;
- comparer index, stockage, filtres et embeddings ;
- fournir paramètres et diagnostics ;
- documenter suppression et réindexation.

**Livrables**

- fiches solutions ;
- matrice de choix ;
- jeux de benchmark ;
- schémas de métadonnées.

**Frontière et validation**

L’intégration complète est au Livre II. Validation avec corpus reproductible.

## Chapitre 16 — Patrons d’architecture

**Objectifs**

- documenter composition, services, repositories, événements et états ;
- préciser problème, contexte, solution et conséquences ;
- fournir anti-patterns ;
- relier au projet Asteria.

**Livrables**

- fiches patrons ;
- diagrammes ;
- exemples ;
- matrice d’usage.

**Frontière et validation**

Ne prescrit pas un patron unique. Validation par exemples testables et limites explicites.

## Chapitre 17 — Patrons de gameplay

**Objectifs**

- cataloguer machines à états, capacités, inventaire, quêtes et simulation ;
- séparer données, règles et présentation ;
- documenter extensibilité et tests ;
- fournir variantes simples et avancées.

**Livrables**

- fiches patrons ;
- diagrammes ;
- exemples ;
- checklists.

**Frontière et validation**

Les systèmes complets restent au Livre II. Validation par petit prototype.

## Chapitre 18 — Référence graphique et 3D

**Objectifs**

- rassembler unités, axes, formats, PBR, UV, LOD et rigs ;
- fournir budgets et conventions ;
- documenter import/export ;
- indexer erreurs visuelles fréquentes.

**Livrables**

- tables techniques ;
- presets ;
- schémas ;
- checklists.

**Frontière et validation**

Les méthodes de production restent au Livre III. Validation par comparaison aux assets pilotes.

## Chapitre 19 — Référence audio

**Objectifs**

- rassembler formats, fréquences, loudness, boucles et spatialisation ;
- référencer TTS/STT et licences ;
- documenter bus et intégration Godot ;
- fournir diagnostics.

**Livrables**

- tables ;
- presets ;
- exemples ;
- checklists.

**Frontière et validation**

La production audio reste au Livre III. Validation par fichiers de test et mesures.

## Chapitre 20 — Catalogue des erreurs et diagnostics

**Objectifs**

- classer erreurs par outil, symptôme et cause ;
- fournir procédure de diagnostic progressive ;
- distinguer cause confirmée et hypothèse ;
- enregistrer solutions et versions concernées.

**Livrables**

- fiches d’erreurs ;
- arbres de diagnostic ;
- commandes de collecte ;
- index des messages.

**Frontière et validation**

Ne promet pas qu’un message possède une cause unique. Validation par cas reproduits ou source officielle.

## Chapitre 21 — Benchmarks et méthodes de mesure

**Objectifs**

- définir protocoles reproductibles ;
- contrôler versions, température, cache et répétitions ;
- calculer moyenne, dispersion et limites ;
- comparer sans conclusions abusives.

**Livrables**

- protocoles ;
- scripts ;
- formats de résultats ;
- exemples analysés.

**Frontière et validation**

Les chiffres doivent être datés et liés au matériel. Validation par répétition indépendante.

## Chapitre 22 — Matrices de compatibilité

**Objectifs**

- croiser OS, GPU, versions, formats et outils ;
- distinguer support officiel, expérimental et non vérifié ;
- enregistrer date et source ;
- faciliter choix et diagnostic.

**Livrables**

- matrices versionnées ;
- légendes ;
- liens de preuve ;
- historique de changements.

**Frontière et validation**

L’absence de test ne signifie pas incompatibilité. Validation par source officielle ou test documenté.

## Chapitre 23 — Comparatifs des solutions

**Objectifs**

- comparer outils selon critères explicites ;
- séparer faits, mesures et préférence ;
- proposer choix par scénario ;
- documenter coûts de migration.

**Livrables**

- tableaux comparatifs ;
- scénarios ;
- pondérations ;
- recommandations conditionnelles.

**Frontière et validation**

Aucune recommandation absolue. Validation par critères reproductibles et sources diverses.

## Chapitre 24 — Checklists de production et de publication

**Objectifs**

- centraliser contrôles par phase ;
- distinguer obligatoire, recommandé et optionnel ;
- fournir versions Solo/Studio ;
- permettre signature et preuve.

**Livrables**

- checklists ;
- formulaires ;
- modèles de revue ;
- critères de sortie.

**Frontière et validation**

Les checklists renvoient aux procédures détaillées. Validation par utilisation sur un lot réel.

## Chapitre 25 — Licences, provenance et conformité

**Objectifs**

- résumer licences du texte, code, modèles et assets ;
- documenter provenance, consentement et redistribution ;
- fournir matrices et modèles de registre ;
- signaler besoins de conseil professionnel.

**Livrables**

- fiches de licences ;
- registre ;
- modèles d’attribution ;
- checklist de publication.

**Frontière et validation**

Ne constitue pas un avis juridique. Validation par cohérence des registres et sources officielles.

## Chapitre 26 — Index croisés

**Objectifs**

- indexer outils, systèmes, formats, erreurs, licences et concepts ;
- relier synonymes et anciennes appellations ;
- fournir navigation PDF/HTML ;
- détecter références orphelines.

**Livrables**

- index alphabétiques et thématiques ;
- liens croisés ;
- tables de synonymes ;
- rapport d’intégrité.

**Frontière et validation**

Ce chapitre clôt l’encyclopédie. Validation par recherche de scénarios connus et contrôle automatique des liens.

## Critères de clôture du Livre V

- les 26 chapitres sont rédigés, repérés et audités ;
- aucune fiche ne duplique intégralement un tutoriel ;
- versions, licences et dates sont présentes ;
- les index et liens croisés sont complets ;
- les matrices distinguent testé, officiel, expérimental et inconnu ;
- les exemples minimaux et fichiers associés sont validés ;
- le PDF/HTML permet une navigation non linéaire efficace.
