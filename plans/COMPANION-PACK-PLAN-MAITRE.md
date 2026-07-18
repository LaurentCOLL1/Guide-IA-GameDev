---
title: "Plan maître détaillé — Companion Pack"
id: "DOC-PLAN-COMPANION"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
pack-count: 10
---

# Plan maître détaillé — Companion Pack

> **Statut :** non commencé  
> **Rôle :** fournir les fichiers réellement réutilisables produits ou validés pendant les cinq Livres.

## Règles transversales du Companion Pack

Chaque ressource doit posséder :

- un README ;
- une licence ou un statut de redistribution ;
- une provenance ;
- une version ;
- des prérequis ;
- une procédure d’installation ou d’utilisation ;
- un exemple minimal ;
- des tests ou une validation statique clairement annoncée ;
- une procédure de désinstallation, restauration ou nettoyage lorsque pertinente.

Aucun secret, poids de modèle non redistribuable, donnée personnelle, voix sans consentement ou asset tiers incompatible ne doit être inclus. Les fichiers binaires lourds doivent être distribués comme artefacts ou releases avec sommes de contrôle.

## Pack 1 — Starter Kit

**Objectifs**

- fournir un projet Godot minimal fonctionnel ;
- matérialiser `Project Asteria` ;
- intégrer scène de bootstrap, structure canonique et configuration Git ;
- inclure profils d’environnement et tests minimaux ;
- permettre de reproduire les chapitres du Livre II.

**Contenu prévu**

- projet Godot de référence ;
- `project.godot` ;
- scène principale ;
- `BootstrapReport` ;
- dossiers `src`, `tests`, `assets`, `data`, `docs` et `tools` ;
- `.gitignore`, `.gitattributes`, README et licence ;
- scripts de validation headless.

**Dépendances**

Livre II, chapitres 1 à 9.

**Critères de validation**

- ouverture sans erreur dans la version Godot de référence ;
- lancement graphique et headless ;
- clone neuf reproductible ;
- aucun fichier importé inutilement versionné ;
- tests minimaux réussis.

## Pack 2 — Project Templates

**Objectifs**

- fournir des modèles de projet Solo et Studio ;
- formaliser modules, dossiers et responsabilités ;
- accélérer création de nouveaux projets ou fonctionnalités ;
- intégrer gouvernance et outils d’éditeur.

**Contenu prévu**

- templates Solo/Studio ;
- conventions de branches ;
- modèles d’issues et pull requests ;
- ADR ;
- CODEOWNERS ou équivalent ;
- paramètres VS Code ;
- configurations de lint et formatage ;
- modèles de module Godot.

**Dépendances**

Livre II, chapitres 4, 5, 26 et 30 ; Volume 0.

**Critères de validation**

- création d’un projet neuf à partir de chaque template ;
- chemins et noms cohérents ;
- aucune dépendance cachée ;
- documentation Solo/Studio distincte.

## Pack 3 — AI Library

**Objectifs**

- fournir une couche réutilisable de communication avec les services IA locaux ;
- isoler fournisseurs, transport et logique de jeu ;
- gérer erreurs, files, cache et tests ;
- éviter le couplage direct à un moteur unique.

**Contenu prévu**

- clients HTTP et WebSocket ;
- contrats OpenAI-compatible ;
- adaptateurs Ollama, llama.cpp/serveur et LocalAI ;
- gestion des timeouts, retries et annulation ;
- files de tâches ;
- cache ;
- mocks et faux serveurs ;
- filtres de sécurité ;
- exemples Godot.

**Dépendances**

Livre II, chapitres 10 à 13.

**Critères de validation**

- tests sans service réel via mocks ;
- tests optionnels contre services locaux ;
- secrets absents du dépôt ;
- comportement dégradé documenté ;
- fournisseurs interchangeables.

## Pack 4 — Code Library

**Objectifs**

- rassembler composants GDScript et utilitaires Python réutilisables ;
- fournir patrons testés sans imposer une architecture unique ;
- éviter la duplication entre chapitres ;
- documenter chaque API et ses limites.

**Contenu prévu**

- utilitaires de collections, validation et sérialisation ;
- services et repositories de référence ;
- machines à états ;
- composants d’interaction ;
- helpers de tests ;
- scripts Python de conversion et génération ;
- exemples d’intégration.

**Dépendances**

Livre II et Livre V.

**Critères de validation**

- documentation de chaque fonction publique ;
- paramètres et retours expliqués ;
- tests unitaires ;
- exemples minimaux ;
- contrôle anti-doublon ;
- compatibilité de version indiquée.

## Pack 5 — Database Library

**Objectifs**

- fournir schémas et migrations réutilisables ;
- démontrer sauvegarde, contenu, cache et indexation ;
- simplifier tests et restauration ;
- séparer données d’exemple et données réelles.

**Contenu prévu**

- schémas SQLite ;
- migrations ;
- repositories ;
- données synthétiques ;
- scripts d’initialisation ;
- sauvegarde/restauration ;
- validateurs ;
- diagrammes.

**Dépendances**

Livre II, chapitres 7 à 10 et systèmes de gameplay concernés.

**Critères de validation**

- base créée depuis zéro ;
- migrations ascendantes testées ;
- restauration testée ;
- requêtes préparées ;
- aucune donnée personnelle incluse.

## Pack 6 — ComfyUI Library

**Objectifs**

- distribuer les workflows visuels reproductibles du guide ;
- séparer workflows, modèles et résultats ;
- documenter dépendances, licences et mémoire ;
- fournir variantes CPU, AMD et qualité.

**Contenu prévu**

- workflows JSON ;
- manifestes YAML ;
- listes de custom nodes ;
- presets ;
- scripts de lancement ;
- modèles de dossiers ;
- fiches de provenance ;
- images de validation légères ;
- checksums.

**Dépendances**

Livre I, chapitre 7 ; Livre III, chapitres 3 et 30.

**Critères de validation**

- import sans nœud manquant ou liste exacte des dépendances ;
- exécution sur profil documenté ;
- modèles non redistribuables exclus ;
- seeds et paramètres enregistrés ;
- licence de chaque composant connue.

## Pack 7 — Documentation Library

**Objectifs**

- fournir les modèles documentaires normalisés ;
- faciliter rédaction, audit et publication ;
- conserver cohérence entre Livres et Companion Pack ;
- automatiser création de nouveaux documents.

**Contenu prévu**

- templates de chapitre ;
- front matter ;
- rapports QA ;
- preuves YAML ;
- ADR ;
- checklists ;
- fiches outils/modèles/assets ;
- glossaires ;
- scripts de génération.

**Dépendances**

Volume 0 et tous les Livres.

**Critères de validation**

- templates compilables ;
- identifiants conformes ;
- repères d’utilisation présents ;
- exemples remplis ;
- documentation de personnalisation.

## Pack 8 — Test & Benchmark Library

**Objectifs**

- centraliser suites de tests et scènes de mesure ;
- fournir fixtures et seeds reproductibles ;
- comparer matériel, versions et réglages ;
- normaliser rapports.

**Contenu prévu**

- tests GDScript ;
- tests Python ;
- scènes de benchmark CPU/GPU/mémoire ;
- corpus IA ;
- fixtures de base ;
- scripts de lancement ;
- formats CSV/JSON/YAML ;
- modèles de rapports.

**Dépendances**

Livre II, chapitre 27 ; Livre IV, chapitres 2 à 10 ; Livre V, chapitre 21.

**Critères de validation**

- tests exécutables séparément ;
- résultats horodatés et liés au matériel ;
- répétitions et variance documentées ;
- absence de données non redistribuables.

## Pack 9 — Production Toolkit

**Objectifs**

- automatiser production, conversion et validation des assets ;
- réduire tâches manuelles répétitives ;
- conserver provenance et rapports ;
- gérer lots et reprise après échec.

**Contenu prévu**

- scripts Blender ;
- convertisseurs de textures et audio ;
- validateurs d’assets ;
- générateurs de catalogues ;
- outils de renommage ;
- pipelines de lots ;
- scripts d’import Godot ;
- packaging.

**Dépendances**

Livre III, notamment chapitres 4, 16 à 18, 28 à 30 ; Livre IV, chapitre 14.

**Critères de validation**

- mode dry-run ;
- journaux et codes de sortie ;
- reprise après erreur ;
- fichiers sources préservés ;
- tests sur jeux d’assets synthétiques.

## Pack 10 — Knowledge Base

**Objectifs**

- fournir un corpus exemple pour lore, codex et RAG ;
- démontrer versionnement, métadonnées et indexation ;
- séparer vérité canonique, rumeurs et mémoire des personnages ;
- permettre tests d’embeddings et recherche.

**Contenu prévu**

- lore synthétique de `Project Asteria` ;
- codex ;
- documents RAG ;
- schémas de métadonnées ;
- corpus de test ;
- scripts de découpage ;
- index reproductibles ;
- outils de suppression/réindexation.

**Dépendances**

Livre II, chapitres 10, 15 à 17 et 25 ; Livre V, chapitre 15.

**Critères de validation**

- droits de redistribution clairs ;
- corpus synthétique ou autorisé ;
- index recréable depuis les sources ;
- tests de recherche ;
- suppression complète d’un document vérifiée.

## Organisation de dépôt prévue

```text
Companion-Pack/
├── Starter-Kit/
├── Project-Templates/
├── AI-Library/
├── Code-Library/
├── Database-Library/
├── ComfyUI-Library/
├── Documentation-Library/
├── Test-Benchmark-Library/
├── Production-Toolkit/
└── Knowledge-Base/
```

Chaque pack possède son propre `README.md`, son changelog, ses licences, ses tests et sa version.

## Critères de clôture du Companion Pack

- les dix packs existent et sont documentés ;
- leurs dépendances sont explicites ;
- chaque exemple minimal est vérifié ;
- les tests peuvent être lancés séparément ;
- les licences et provenances sont complètes ;
- les gros fichiers sont distribués de manière contrôlée ;
- les archives de publication sont reproductibles ;
- les liens entre chapitres et ressources sont valides ;
- `CONTINUITE-PROJET.md` et la roadmap reflètent les versions publiées.
