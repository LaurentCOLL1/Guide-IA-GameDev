---
title: "Chapitre 7 — Standards techniques"
id: "DOC-V0-CH07"
status: "complete"
version: "1.4.0"
book: "Volume 0"
chapter: 7
tags:
  - standards
  - architecture
  - code
  - reproductibilite
  - qualite
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 7 — Standards techniques

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Objectif du chapitre

Ce chapitre définit les règles techniques communes à l’ensemble du guide, au projet fil rouge et au Companion Pack. Ces règles servent de contrat entre la documentation, les scripts, les projets Godot, les scènes Blender, les workflows ComfyUI, les services Docker et les outils d’intelligence artificielle locale.

L’objectif n’est pas d’imposer une complexité inutile. Il s’agit de garantir que chaque exemple soit compréhensible, reproductible, testable, versionnable et maintenable sur la durée.

Les règles sont classées selon trois niveaux :

- **Obligatoire** : exigence à respecter dans tous les exemples officiels ;
- **Recommandé** : pratique à appliquer sauf justification documentée ;
- **Optionnel** : amélioration utile selon l’échelle du projet.

## 1. Principes directeurs

### 1.1 Une seule source de vérité

**Obligatoire.** Toute donnée importante doit posséder une source de vérité clairement identifiée.

Exemples :

- le texte du guide réside dans les fichiers Markdown ;
- l’ordre de compilation réside dans `contents.txt` ;
- les métadonnées globales résident dans `metadata.yaml` ;
- la configuration d’un service réside dans son fichier versionné ;
- les paramètres d’un workflow ComfyUI résident dans le fichier JSON exporté ;
- les réglages d’un projet Godot résident dans le projet et ses ressources versionnées.

Une information ne doit pas être maintenue manuellement dans plusieurs emplacements. Lorsqu’une duplication est nécessaire pour des raisons de publication, elle doit être générée automatiquement.

### 1.2 Reproductibilité avant commodité

**Obligatoire.** Une procédure officielle doit pouvoir être reproduite à partir d’un clone propre du dépôt et d’une liste explicite de prérequis.

Chaque procédure technique doit préciser :

1. les versions ou plages de versions testées ;
2. les dépendances requises ;
3. les commandes à exécuter ;
4. les fichiers créés ou modifiés ;
5. le résultat attendu ;
6. une méthode de vérification ;
7. une procédure de retour arrière lorsque l’opération est risquée.

### 1.3 Local d’abord

**Obligatoire pour le pipeline principal.** Les fonctions centrales du guide doivent pouvoir être exécutées localement, sans dépendance obligatoire à un service en ligne.

Une ressource distante peut être utilisée pour :

- télécharger une dépendance ;
- consulter une documentation officielle ;
- comparer une solution locale avec une solution hébergée ;
- publier une version du projet.

Elle ne doit pas devenir une dépendance cachée du fonctionnement quotidien.

### 1.4 Simplicité observable

**Recommandé.** Une solution simple, instrumentée et testable est préférable à une solution sophistiquée difficile à diagnostiquer.

Chaque composant non trivial doit exposer au minimum :

- son état ;
- ses erreurs ;
- sa version ;
- sa configuration active ;
- les chemins des fichiers qu’il lit ou écrit.

## 2. Environnement technique de référence

Le guide utilise la configuration de référence suivante :

- Windows comme système principal ;
- processeur AMD Ryzen 7 2700 ;
- 32 Go de mémoire vive ;
- carte AMD Radeon RX 6750 XT avec 12 Go de VRAM ;
- ComfyUI avec ZLUDA lorsque le workflow l’exige ;
- Docker Desktop ou moteur Docker compatible ;
- Visual Studio Code comme éditeur principal ;
- Git comme système de versionnement ;
- PowerShell comme shell principal sous Windows ;
- Bash pour les environnements Linux, WSL et CI ;
- Python pour l’automatisation ;
- Godot pour le moteur de jeu ;
- Blender pour la création et le traitement 3D.

Cette configuration est une référence de validation, pas une limitation. Lorsqu’un exemple exige davantage de mémoire, de VRAM ou de puissance CPU, cette exigence doit être signalée avant la procédure.

## 3. Gestion des versions

### 3.1 Versions explicites

**Obligatoire.** Toute dépendance critique doit être associée à une version testée.

Sont notamment concernés :

- Godot ;
- Blender ;
- Python ;
- Docker et Docker Compose ;
- ComfyUI ;
- les nœuds personnalisés ComfyUI ;
- Ollama, llama.cpp ou les serveurs LLM utilisés ;
- FFmpeg ;
- Pandoc ;
- les modèles d’IA et leurs variantes quantifiées.

Il est acceptable d’indiquer une plage compatible lorsque plusieurs versions ont été validées.

### 3.2 Verrouillage des dépendances

**Obligatoire pour les projets livrés.** Les dépendances doivent être verrouillées dès que l’outil le permet.

Exemples :

- `requirements.txt` ou fichier de verrouillage Python ;
- image Docker identifiée par version ;
- révision Git précise pour un nœud ComfyUI ;
- version précise d’un modèle ;
- version Godot enregistrée dans les métadonnées du projet.

L’étiquette `latest` ne doit pas être utilisée dans un exemple de production sans justification.

### 3.3 Politique de mise à jour

**Recommandé.** Une mise à jour de dépendance suit le cycle suivant :

1. création d’une branche dédiée ;
2. lecture des notes de version ;
3. mise à jour d’une dépendance à la fois ;
4. exécution des tests ;
5. comparaison des performances ;
6. mise à jour de la documentation ;
7. validation avant fusion.

## 4. Organisation des projets techniques

### 4.1 Séparation des responsabilités

**Obligatoire.** Le code, les données, la configuration, les ressources sources et les fichiers générés doivent être séparés.

Structure générique recommandée :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
project/
├── src/            # Code source
├── config/         # Configuration versionnée
├── data/           # Données d’entrée contrôlées
├── assets/         # Ressources utilisées par le projet
├── tools/          # Outils et scripts internes
├── tests/          # Tests automatisés
├── docs/           # Documentation du composant
├── build/          # Fichiers générés, non versionnés
└── README.md
```

La structure exacte varie selon Godot, Blender, ComfyUI ou Docker, mais la séparation conceptuelle reste obligatoire.

### 4.2 Fichiers générés

**Obligatoire.** Les fichiers pouvant être régénérés ne doivent pas être considérés comme des sources.

Ils doivent être :

- exclus par `.gitignore` lorsque leur conservation n’est pas nécessaire ;
- placés dans un dossier clairement identifié ;
- régénérés par une commande documentée ;
- nettoyables sans perte de travail manuel.

### 4.3 Chemins portables

**Obligatoire.** Les exemples officiels doivent utiliser des chemins relatifs dès que possible.

Les chemins absolus propres à une machine, comme `C:\Users\Nom\...`, ne doivent apparaître que comme exemples et doivent être remplacés par des variables ou paramètres dans les scripts réutilisables.

## 5. Conventions de nommage technique

### 5.1 Principes communs

**Obligatoire.** Un nom technique doit être :

- descriptif ;
- stable ;
- sans ambiguïté ;
- cohérent avec le langage ou l’outil ;
- dépourvu de termes temporaires comme `test2`, `final-final` ou `new`.

### 5.2 Fichiers et dossiers

**Recommandé.** Utiliser :

- `kebab-case` pour la documentation et les dossiers génériques ;
- `snake_case` pour les scripts Python ;
- les conventions natives de Godot pour les scènes, scripts et ressources ;
- des noms ASCII pour les fichiers techniques lorsque l’outil présente des limites d’encodage ;
- des noms français explicites dans la documentation et des noms anglais cohérents dans le code lorsque les bibliothèques utilisées sont anglophones.

Le mélange de langues dans un même sous-système doit être évité.

### 5.3 Variables et fonctions

**Obligatoire.** Les conventions du langage sont prioritaires :

- GDScript : `snake_case` pour variables et fonctions, `PascalCase` pour les classes ;
- Python : PEP 8 ;
- PowerShell : verbes approuvés et noms explicites ;
- Bash : variables en minuscules pour le local, majuscules pour l’environnement ;
- JSON et YAML : clés stables en `snake_case` sauf contrainte d’un format externe.

## 6. Standards de code

### 6.1 Lisibilité

**Obligatoire.** Le code pédagogique doit privilégier la lisibilité à la concision.

Sont attendus :

- des fonctions courtes ;
- une responsabilité principale par fonction ;
- des noms explicites ;
- peu d’imbrication ;
- des commentaires expliquant les décisions, non les instructions évidentes ;
- des valeurs configurables au lieu de nombres magiques.

### 6.2 Typage

**Recommandé.** Utiliser le typage disponible lorsque celui-ci améliore la détection des erreurs.

Cela concerne notamment :

- les annotations de type GDScript ;
- les annotations Python ;
- les schémas JSON ;
- les structures de données explicitement documentées.

### 6.3 Gestion des erreurs

**Obligatoire.** Une erreur ne doit pas être ignorée silencieusement.

Le code doit :

1. détecter l’échec ;
2. produire un message compréhensible ;
3. indiquer l’action ou la ressource concernée ;
4. conserver le contexte utile au diagnostic ;
5. échouer proprement lorsqu’une poursuite risquerait de corrompre des données.

### 6.4 Configuration

**Obligatoire.** Les valeurs dépendantes de l’environnement doivent être externalisées.

Exemples :

- ports réseau ;
- chemins de modèles ;
- quantité de mémoire allouée ;
- résolution de rendu ;
- niveau de journalisation ;
- adresse d’un service local.

Les valeurs par défaut doivent être sûres et adaptées à la configuration de référence.

## 7. Données et formats d’échange

### 7.1 Formats ouverts

**Recommandé.** Privilégier les formats ouverts ou largement documentés :

- JSON, YAML, CSV et SQLite pour les données ;
- glTF pour l’échange 3D ;
- PNG, EXR et formats adaptés au pipeline graphique ;
- WAV et FLAC pour les sources audio ;
- Markdown pour la documentation ;
- UTF-8 pour le texte.

### 7.2 Validation des données

**Obligatoire.** Les données reçues d’un fichier, d’un modèle d’IA, d’une interface ou d’un service doivent être validées avant utilisation.

La validation porte au minimum sur :

- le type ;
- les champs requis ;
- les plages de valeurs ;
- les chemins ;
- la taille ;
- la version du schéma lorsque le format évolue.

### 7.3 Migrations

**Recommandé.** Toute structure de données persistante doit posséder une stratégie de migration.

Une migration ne doit pas modifier irréversiblement les données sans sauvegarde préalable.

## 8. Services, conteneurs et réseau local

### 8.1 Docker Compose comme description exécutable

**Recommandé.** Les ensembles de services locaux doivent être décrits dans un fichier Docker Compose versionné.

Chaque service doit préciser :

- une image versionnée ;
- ses ports ;
- ses volumes ;
- ses variables d’environnement ;
- une politique de redémarrage adaptée ;
- un test de santé lorsque possible.

### 8.2 Exposition réseau minimale

**Obligatoire.** Un service local ne doit pas être exposé sur toutes les interfaces réseau sans nécessité explicite.

Par défaut :

- écouter sur `127.0.0.1` ;
- limiter les ports publiés ;
- ne pas intégrer de secret dans une URL ;
- documenter toute ouverture vers le réseau local.

### 8.3 Persistance

**Obligatoire.** Les données persistantes doivent être stockées dans des volumes ou dossiers clairement identifiés et sauvegardables.

La suppression d’un conteneur ne doit pas supprimer involontairement les modèles, bases, conversations ou configurations importantes.

## 9. Sécurité et secrets

### 9.1 Aucun secret dans Git

**Obligatoire.** Les mots de passe, jetons, clés privées et identifiants sensibles ne doivent jamais être enregistrés dans le dépôt.

Utiliser :

- des variables d’environnement ;
- un fichier `.env` ignoré par Git ;
- un fichier `.env.example` sans valeur sensible ;
- un gestionnaire de secrets en Mode Studio.

### 9.2 Principe du moindre privilège

**Obligatoire.** Un outil ne reçoit que les droits nécessaires à son fonctionnement.

Cela s’applique aux :

- conteneurs ;
- scripts ;
- comptes de service ;
- accès aux dossiers ;
- bases de données ;
- intégrations GitHub.

### 9.3 Entrées non fiables

**Obligatoire.** Toute sortie générée par une IA, tout fichier téléchargé et toute donnée utilisateur doivent être considérés comme non fiables avant validation.

Un modèle ne doit jamais déclencher directement une commande système destructive sans étape de contrôle explicite.

## 10. Journalisation et diagnostic

### 10.1 Niveaux de journalisation

**Recommandé.** Les composants doivent utiliser des niveaux cohérents :

- `DEBUG` : détails de diagnostic ;
- `INFO` : étapes normales importantes ;
- `WARNING` : situation anormale récupérable ;
- `ERROR` : opération échouée ;
- `CRITICAL` : arrêt ou corruption potentielle.

### 10.2 Messages exploitables

**Obligatoire.** Un message d’erreur doit répondre autant que possible aux questions suivantes :

- qu’est-ce qui a échoué ?
- où l’échec s’est-il produit ?
- quelle ressource était concernée ?
- quelle action corrective est suggérée ?

### 10.3 Données sensibles

**Obligatoire.** Les journaux ne doivent pas contenir de secrets, de données privées non nécessaires ou de contenu sensible complet lorsqu’un identifiant technique suffit.

## 11. Tests et validation

### 11.1 Pyramide de tests adaptée

**Recommandé.** Utiliser plusieurs niveaux :

- tests unitaires pour les fonctions isolées ;
- tests d’intégration pour les échanges entre composants ;
- tests de bout en bout pour les parcours critiques ;
- tests manuels documentés pour les dimensions visuelles, sonores ou ergonomiques.

### 11.2 Test minimal obligatoire

**Obligatoire pour tout exemple officiel.** Chaque composant doit posséder au moins une méthode de validation reproductible.

Exemples :

- une commande retournant un code de sortie nul ;
- une scène Godot de démonstration ;
- une image de référence ComfyUI ;
- un fichier audio témoin ;
- une requête de santé HTTP ;
- un test de schéma JSON.

### 11.3 Données de test

**Recommandé.** Les jeux de données de test doivent être petits, légaux, versionnables et dépourvus de données personnelles.

## 12. Performance et budgets

### 12.1 Mesurer avant d’optimiser

**Obligatoire.** Toute optimisation doit partir d’une mesure.

Les mesures pertinentes incluent :

- temps CPU ;
- utilisation GPU ;
- VRAM ;
- mémoire vive ;
- taille des fichiers ;
- temps de chargement ;
- images par seconde ;
- latence d’inférence ;
- temps de génération d’un asset.

### 12.2 Budgets matériels

**Recommandé.** Chaque pipeline lourd doit annoncer ses budgets indicatifs pour la configuration de référence.

Pour la RX 6750 XT 12 Go, la documentation doit distinguer :

- les réglages confortables ;
- les réglages possibles avec optimisation ;
- les réglages déconseillés ;
- les solutions de repli CPU ou mémoire partagée.

### 12.3 Dégradation contrôlée

**Recommandé.** Un système doit proposer un mode réduit plutôt que d’échouer brutalement lorsque les ressources sont insuffisantes.

Exemples :

- résolution d’image inférieure ;
- lot de génération plus petit ;
- quantification de modèle ;
- niveau de détail réduit ;
- désactivation d’effets secondaires ;
- chargement progressif.

## 13. Standards des assets

### 13.1 Traçabilité

**Obligatoire.** Chaque asset doit pouvoir être relié à :

- sa source ;
- sa licence ;
- sa version ;
- son auteur ou générateur ;
- ses paramètres de production ;
- ses transformations principales.

### 13.2 Sources et exports

**Obligatoire.** Conserver séparément :

- les fichiers sources modifiables ;
- les exports destinés au moteur ;
- les caches ;
- les aperçus ;
- les variantes générées.

### 13.3 Nommage et unités

**Obligatoire.** Les unités, axes, échelles, espaces colorimétriques et fréquences audio doivent être documentés pour éviter les conversions implicites.

## 14. Automatisation

### 14.1 Scripts idempotents

**Recommandé.** Un script de préparation ou de construction doit pouvoir être relancé sans produire un état incohérent.

### 14.2 Mode simulation

**Optionnel mais fortement recommandé pour les opérations destructives.** Ajouter un mode `--dry-run`, `-WhatIf` ou équivalent lorsque le script déplace, renomme ou supprime des fichiers.

### 14.3 Codes de sortie

**Obligatoire.** Les scripts de ligne de commande doivent retourner :

- `0` en cas de réussite ;
- une valeur non nulle en cas d’échec.

Ils doivent également écrire les erreurs sur le canal approprié.

## 15. Mode Solo et Mode Studio

### 15.1 Mode Solo

Le Mode Solo privilégie :

- une installation locale simple ;
- un nombre limité de services ;
- des scripts directement exécutables ;
- une sauvegarde locale claire ;
- une documentation concentrée dans le dépôt.

Les exigences de qualité, de sécurité et de reproductibilité restent applicables.

### 15.2 Mode Studio

Le Mode Studio ajoute notamment :

- branches protégées ;
- revue de code ;
- intégration continue ;
- gestion centralisée des secrets ;
- registre d’assets ;
- stockage partagé ;
- rôles et permissions ;
- validation automatisée des livrables ;
- suivi des performances et régressions.

Le Mode Studio étend le Mode Solo sans créer un second pipeline incompatible.

## 16. Dérogations

Une règle peut être contournée lorsqu’une contrainte technique réelle l’exige. La dérogation doit alors être :

1. explicitement signalée ;
2. justifiée ;
3. limitée au périmètre nécessaire ;
4. accompagnée de ses risques ;
5. réévaluée lors d’une mise à jour majeure.

Une habitude personnelle ou un gain de quelques secondes ne constitue pas une justification suffisante pour supprimer une garantie de sécurité ou de reproductibilité.

## 17. Checklist de conformité technique

Avant de considérer un exemple comme publiable, vérifier :

- [ ] les versions testées sont indiquées ;
- [ ] les dépendances sont explicites et verrouillées lorsque possible ;
- [ ] les chemins sont portables ;
- [ ] les fichiers générés sont séparés des sources ;
- [ ] les secrets sont exclus du dépôt ;
- [ ] les entrées externes sont validées ;
- [ ] les erreurs sont visibles et exploitables ;
- [ ] une méthode de test est fournie ;
- [ ] les ressources matérielles nécessaires sont annoncées ;
- [ ] les données persistantes sont sauvegardables ;
- [ ] les licences et provenances des assets sont traçables ;
- [ ] le parcours Solo fonctionne sans infrastructure excessive ;
- [ ] les extensions Studio restent compatibles avec le socle Solo.

## Conclusion

Les standards techniques transforment une collection de tutoriels en système de production cohérent. Ils rendent les procédures fiables, limitent les erreurs invisibles et permettent au projet fil rouge d’évoluer sans perdre sa traçabilité.

Le chapitre suivant applique la même logique aux modèles, prompts, workflows, données d’entraînement, sorties générées et services d’intelligence artificielle locale.
