---
title: "Livre II — Chapitre 1 : Découvrir Godot et créer le projet fil rouge"
id: "DOC-L2-CH01"
status: "reviewed"
version: "1.3.0"
lang: "fr-FR"
book: "Livre II"
chapter: 1
last-verified: "2026-07-18"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Livre-II/QA/AUDIT-CHAPITRES-01-02.md"
supplemental-audit: "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-platform:
  os: "Windows 11 64 bits"
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Découvrir Godot et créer le projet fil rouge

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH01`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** installer une version stable et reproductible de Godot, créer le projet fil rouge 3D, comprendre les notions de nœud et de scène, exécuter une première scène et enregistrer une base saine dans Git.  
> **Audit post-création :** terminé — voir `Livre-II/QA/AUDIT-CHAPITRES-01-02.md`.

## 1. Rôle de ce chapitre

Le Livre I a préparé la plateforme locale. Le Livre II transforme cette plateforme en projet de jeu.

Ce premier chapitre ne cherche pas encore à construire un contrôleur complet, un inventaire ou un agent autonome. Il établit le socle sur lequel tous les systèmes suivants seront développés :

- une version précise de Godot ;
- un projet Godot identifiable ;
- une arborescence de fichiers durable ;
- une scène principale exécutable ;
- un premier script GDScript minimal ;
- une configuration Git propre ;
- un test graphique et un test sans interface ;
- une méthode de mise à jour réversible.

La règle principale est :

> Le projet fil rouge doit rester exécutable après chaque chapitre. Une nouvelle fonctionnalité ne doit pas rendre impossible le lancement de la base minimale.

## 2. Le projet fil rouge

### 2.1 Finalité

Le projet fil rouge est un jeu 3D réaliste et modulaire servant de support à toute la collection.

Il doit progressivement démontrer :

- un monde 3D explorable ;
- un personnage contrôlable ;
- des personnages non joueurs et agents autonomes ;
- des relations sociales ;
- des familles et générations ;
- du combat et des compétences ;
- un inventaire et une économie ;
- une simulation du monde vivant ;
- des factions, une politique et une justice ;
- de la construction et de la gestion ;
- des quêtes, une narration et un codex ;
- des sauvegardes locales ;
- une connexion facultative à des services IA locaux.

Le projet n’essaie pas de construire tous ces systèmes en même temps. Chaque chapitre ajoute une couche testable.

### 2.2 Nom de travail

Le nom technique utilisé dans les exemples est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Project Asteria
```

Le dossier local recommandé est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\projects\project-asteria
```

Le nom est provisoire. Le chemin et les identifiants techniques doivent rester stables même si le titre commercial change.

### 2.3 Référentiel principal

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Guide-IA-GameDev        documentation et Companion Pack
Project-Asteria         code, données et assets du jeu
```

Le guide et le projet de jeu peuvent vivre dans deux dépôts séparés. Le Companion Pack fournit les ressources réutilisables, mais le projet fil rouge possède son propre historique Git.

## 3. Version de Godot retenue

### 3.1 Version de référence

La version retenue pour ce chapitre est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Godot Engine 4.7.1-stable
```

Cette version a été publiée le 14 juillet 2026 comme première version de maintenance de la branche 4.7.

Le guide n’utilise pas comme référence :

- une version `dev` ;
- une version `beta` ;
- une version `rc` ;
- la branche `master` ;
- une compilation communautaire non documentée.

Une version de développement peut être testée dans une copie du projet, jamais comme unique environnement de travail.

### 3.2 Édition Standard ou .NET

Godot fournit notamment :

- une édition **Standard**, pour GDScript et les extensions natives ;
- une édition **.NET**, pour les projets utilisant C#.

Le parcours principal retient :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Godot Standard + GDScript
```

Motifs :

- GDScript est profondément intégré à l’éditeur ;
- la chaîne comporte moins de dépendances ;
- les exemples sont plus simples pour un débutant ;
- le temps d’itération est court ;
- le projet ne dépend pas du SDK .NET pour démarrer.

L’édition .NET sera présentée comme alternative lorsque C# apporte une valeur particulière. Elle n’est pas installée par défaut dans ce chapitre.

### 3.3 Politique de version

Pour chaque projet Godot, créer le fichier `docs/environment/godot-reference.yaml` et y enregistrer :

> **[VSC] Visual Studio Code - Créer :** `docs/environment/godot-reference.yaml` à la racine du projet.

```yaml
engine: Godot
version: 4.7.1-stable
edition: standard
language: GDScript
renderer: forward_plus
platform: windows-x86_64
verified: 2026-07-18
```

Avant une mise à jour :

1. fermer l’éditeur ;
2. vérifier que Git ne contient aucune modification inconnue ;
3. créer une branche de migration ;
4. sauvegarder les données non versionnées ;
5. lire les notes de migration ;
6. ouvrir une copie du projet ;
7. exécuter les tests ;
8. seulement ensuite, adopter la nouvelle version.

## 4. Compatibilité avec la configuration de référence

La configuration principale dépasse les recommandations d’édition d’un projet 3D simple :

| Composant | Configuration du guide | Utilisation prévue |
|---|---|---|
| CPU | Ryzen 7 2700, 8 cœurs / 16 threads | scripts, import, physique, compilation de shaders |
| GPU | Radeon RX 6750 XT, 12 Go | rendu 3D Forward+, édition et profilage |
| RAM | 32 Go | Godot, Blender, outils IA et services locaux |
| Système | Windows 11 64 bits | éditeur et exports Windows |
| API graphique | Vulkan ou Direct3D 12 selon le pilote | RenderingDevice de Godot |

Cette configuration ne dispense pas de créer des profils graphiques plus légers. Un jeu destiné à être distribué doit être testé sur du matériel inférieur à la station de développement.

## 5. Choisir le moteur de rendu

Godot 4 propose trois méthodes principales.

### 5.1 Forward+

**Choix principal du projet.**

Forward+ vise les ordinateurs récents et fournit le plus grand ensemble de fonctions de rendu avancées. Il convient au projet réaliste de référence et à la RX 6750 XT.

Utilisations prévues :

- éclairage 3D avancé ;
- nombreuses lumières locales ;
- effets de post-traitement ;
- environnements détaillés ;
- fonctionnalités modernes basées sur le RenderingDevice.

### 5.2 Mobile

**Profil secondaire.**

Le moteur Mobile peut être utilisé pour :

- des scènes moins coûteuses ;
- des tests de scalabilité ;
- des cibles mobiles ;
- certains profils desktop faibles.

Le passage entre Forward+ et Mobile demande généralement moins d’adaptation qu’un passage vers Compatibility.

### 5.3 Compatibility

**Profil de secours et cible ancienne.**

Compatibility vise :

- les GPU anciens ;
- les systèmes sans Vulkan, Direct3D 12 ou Metal compatible ;
- le Web ;
- les machines de test à très faible capacité.

Il ne fournit pas toutes les fonctions visuelles disponibles dans Forward+.

### 5.4 Décision du projet

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Édition principale       Forward+
Profil léger             Mobile
Profil ancien / Web      Compatibility
```

Le moteur de rendu n’est pas une option cosmétique. Il affecte les matériaux, les effets et la stratégie d’optimisation. Toute fonctionnalité graphique indispensable doit être inscrite dans une matrice de compatibilité.

## 6. Télécharger Godot

### 6.1 Source obligatoire

Télécharger Godot depuis :

- la page officielle de téléchargement ;
- ou l’archive officielle des versions.

Ne pas utiliser comme source principale :

- un site de téléchargement générique ;
- une archive republiée sans empreinte ;
- un paquet joint à une vidéo ;
- un exécutable modifié dont le code source et les changements ne sont pas documentés.

### 6.2 Organisation des versions

Créer :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\apps\godot\
├── 4.7.1-standard\
│   ├── Godot_v4.7.1-stable_win64.exe
│   └── SOURCE.txt
└── archives\
    └── Godot_v4.7.1-stable_win64.zip
```

Le fichier `SOURCE.txt` peut contenir :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Produit : Godot Engine Standard
Version : 4.7.1-stable
Plateforme : Windows x86_64
Date de récupération : 2026-07-18
Source : archive officielle Godot
Archive : Godot_v4.7.1-stable_win64.zip
SHA-256 : À renseigner depuis le fichier téléchargé
```

### 6.3 Calculer l’empreinte

Dans PowerShell :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-FileHash `
  "C:\IA-GameDev\apps\godot\archives\Godot_v4.7.1-stable_win64.zip" `
  -Algorithm SHA256
```

Conserver l’empreinte dans l’inventaire logiciel du poste.

### 6.4 Extraire

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Expand-Archive `
  -Path "C:\IA-GameDev\apps\godot\archives\Godot_v4.7.1-stable_win64.zip" `
  -DestinationPath "C:\IA-GameDev\apps\godot\4.7.1-standard" `
  -Force
```

Godot peut être utilisé comme application portable. L’éditeur n’a pas besoin d’un programme d’installation traditionnel pour ce parcours.

### 6.5 Vérifier la version

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$Godot = "C:\IA-GameDev\apps\godot\4.7.1-standard\Godot_v4.7.1-stable_win64.exe"
& $Godot --version
```

Résultat attendu : une version commençant par :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
4.7.1.stable
```

Enregistrer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\logs\godot | Out-Null
& $Godot --version |
  Out-File C:\IA-GameDev\logs\godot\version.txt -Encoding utf8
```

### 6.6 Licence et attribution

Godot Engine est distribué sous licence MIT. Le jeu peut utiliser une licence différente, y compris commerciale ou propriétaire, mais la distribution du binaire Godot exige de conserver la notice de copyright et le texte de licence du moteur.

Préparer dès le démarrage :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
docs/licenses/
├── GODOT-LICENSE.txt
└── THIRD-PARTY-NOTICES.md
```

Les composants tiers inclus dans Godot possèdent également leurs propres notices. La publication finale devra fournir un accès à ces informations dans les crédits, la documentation ou les fichiers accompagnant le jeu.

## 7. Rendre la commande accessible

### 7.1 Variable de session

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$env:GODOT_EXE = "C:\IA-GameDev\apps\godot\4.7.1-standard\Godot_v4.7.1-stable_win64.exe"
& $env:GODOT_EXE --version
```

### 7.2 Variable utilisateur persistante

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
[Environment]::SetEnvironmentVariable(
    "GODOT_EXE",
    "C:\IA-GameDev\apps\godot\4.7.1-standard\Godot_v4.7.1-stable_win64.exe",
    "User"
)
```

Ouvrir un nouveau terminal avant de tester :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --version
```

Le guide utilise `$env:GODOT_EXE` afin de ne pas dépendre d’un alias ambigu ou d’une autre version présente dans le `PATH`.

## 8. Créer le dépôt du projet

### 8.1 Créer le dossier

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\projects\project-asteria | Out-Null
Set-Location C:\IA-GameDev\projects\project-asteria
```

Le dossier doit être vide avant la création du projet.

### 8.2 Initialiser Git

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git init
git branch -M main
```

Créer `.gitignore` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitignore` à la racine du projet.

```gitignore
# Cache et imports générés par Godot 4
.godot/
*.translation

# Fichiers temporaires
*.tmp
*.temp

# Journaux locaux
logs/

# Exports et builds locaux
builds/
dist/

# Fichiers système
Thumbs.db
.DS_Store

# Paramètres VS Code strictement locaux
.vscode/*.local.json
```

Créer également `.gitattributes` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitattributes` à la racine du projet.

```gitattributes
# Normaliser les fichiers texte du projet en LF.
* text=auto eol=lf

*.gd text eol=lf
*.tscn text eol=lf
*.tres text eol=lf
*.godot text eol=lf
*.json text eol=lf
*.md text eol=lf
```

Lorsque l’option Git est choisie dans le Project Manager, Godot crée normalement `.gitignore` et `.gitattributes`. Les deux fichiers doivent être relus et versionnés. Sous Windows, cette normalisation évite les changements artificiels dus aux conversions CRLF/LF.

Pour un dépôt existant qui ne possède pas ces fichiers, utiliser **Project > Version Control > Generate Version Control Metadata**, puis examiner le diff avant commit.

### 8.3 README initial

Créer `README.md` :

> **[VSC] Visual Studio Code - Créer :** `README.md` à la racine du projet.

```markdown
# Project Asteria

Projet fil rouge du Guide IA GameDev.

## Moteur

- Godot 4.7.1-stable
- édition Standard
- GDScript
- Forward+

## Démarrage

Ouvrir `project.godot` dans la version de Godot indiquée ci-dessus.
```

## 9. Créer le projet dans le Project Manager

### 9.1 Ouvrir le gestionnaire

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --editor --path C:\IA-GameDev\projects\project-asteria
```

> **[APP] Godot Project Manager - Interface :** ouvrir le gestionnaire de projets et effectuer l’action décrite.

Lorsque le dossier ne contient pas encore `project.godot`, ouvrir directement l’exécutable puis utiliser le Project Manager.

### 9.2 Paramètres de création

Dans **Create New Project** :

> **[APP] Godot Project Manager - Configurer :** renseigner les paramètres ci-dessous dans **Create New Project**.

```text
Project Name       Project Asteria
Project Path       C:\IA-GameDev\projects\project-asteria
Renderer           Forward+
Version Control    Git
```

> **[APP] Godot Project Manager - Créer :** valider la création du projet avec les paramètres précédents.

Laisser le projet créer le fichier `project.godot`.

### 9.3 Vérifier les fichiers initiaux

Après ouverture :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-ChildItem -Force C:\IA-GameDev\projects\project-asteria
```

Éléments attendus :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer cette liste avec les fichiers réellement créés.

```text
.git\
.gitattributes
.gitignore
.godot\
icon.svg
icon.svg.import
project.godot
README.md
```

Le dossier `.godot` est généré. Il ne doit pas être versionné.

Les fichiers sources comme `icon.svg` sont versionnés. Les fichiers `.import` associés peuvent exister à côté de certaines sources selon le type de ressource et la version ; la source originale reste indispensable.

## 10. Comprendre `res://` et `user://`

### 10.1 `res://`

`res://` représente la racine du projet, c’est-à-dire le dossier contenant `project.godot`.

Exemples :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
res://project.godot
res://scenes/main/main.tscn
res://scripts/bootstrap.gd
```

Les ressources du jeu sont chargées depuis `res://`.

### 10.2 `user://`

`user://` représente un emplacement inscriptible propre à l’utilisateur et au système.

Il servira notamment à stocker :

- les sauvegardes ;
- les paramètres utilisateur ;
- les journaux du jeu ;
- les caches runtime ;
- les captures créées par le joueur.

Le contenu de `user://` n’appartient pas au dépôt Git du projet.

### 10.3 Règle de séparation

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
res://     contenu livré avec le jeu
user://    données créées ou modifiées pendant l’exécution
```

Ne pas écrire les sauvegardes dans `res://`.

## 11. Découvrir l’éditeur

### 11.1 Zones principales

L’éditeur comprend notamment :

- le dock **Scene**, qui affiche l’arbre des nœuds ;
- le dock **FileSystem**, qui affiche les ressources de `res://` ;
- l’**Inspector**, qui modifie les propriétés du nœud ou de la ressource sélectionnée ;
- la vue **3D** ;
- la vue **2D** ;
- l’éditeur **Script** ;
- l’éditeur **AssetLib** ;
- les panneaux inférieurs **Output**, **Debugger**, **Audio** et **Animation**.

### 11.2 Disposition de travail

Pour ce chapitre :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Scene       à gauche
3D          au centre
Inspector   à droite
FileSystem  en bas à gauche
Output      en bas
```

Ne pas masquer le panneau Output pendant l’apprentissage. Les erreurs et les messages du premier script y apparaissent.

### 11.3 Sauvegarde

Raccourcis utiles :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Ctrl+S       sauvegarder la scène courante
Ctrl+Shift+S sauvegarder sous
F6           exécuter la scène courante
F5           exécuter le projet depuis la scène principale
F8           arrêter l’exécution
```

## 12. Nœuds, scènes et arbre de scène

### 12.1 Nœud

Un nœud est une unité fonctionnelle.

Exemples :

| Nœud | Rôle |
|---|---|
| `Node` | logique générale |
| `Node3D` | transformation et parent 3D |
| `MeshInstance3D` | affichage d’une géométrie |
| `Camera3D` | point de vue |
| `DirectionalLight3D` | lumière directionnelle |
| `StaticBody3D` | corps physique immobile |
| `CharacterBody3D` | personnage contrôlé par script |
| `Control` | interface utilisateur |
| `AudioStreamPlayer` | lecture audio |

Un nœud possède :

- un nom ;
- un type ;
- des propriétés ;
- un parent éventuel ;
- des enfants éventuels ;
- des méthodes et signaux ;
- éventuellement un script.

### 12.2 Scène

Une scène est un arbre de nœuds sauvegardé dans un fichier `.tscn` ou `.scn`.

Une scène :

- possède un seul nœud racine ;
- peut être instanciée plusieurs fois ;
- peut servir de composant réutilisable ;
- peut être la scène principale du projet.

### 12.3 Composition

Le projet privilégie la composition :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Player.tscn
├── CharacterBody3D
├── CollisionShape3D
├── MeshInstance3D
├── CameraRig
└── InteractionDetector
```

La scène `Player.tscn` peut ensuite être instanciée dans plusieurs niveaux sans dupliquer sa structure interne.

### 12.4 Ressource

Une ressource représente des données réutilisables :

- matériau ;
- maillage ;
- texture ;
- son ;
- animation ;
- courbe ;
- ressource personnalisée ;
- scène empaquetée.

Le Livre II utilisera les Resources pour éviter de coder en dur les données de gameplay.

## 13. Arborescence cible du projet

Créer les dossiers suivants :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$folders = @(
    "assets\shared",
    "src\core",
    "src\features\bootstrap",
    "src\features\player",
    "src\features\world",
    "src\features\ui",
    "data",
    "localization",
    "tests",
    "tools",
    "docs",
    "logs"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force $folder | Out-Null
}
```

Créer un fichier vide :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType File -Force docs\.gdignore | Out-Null
```

Le fichier `.gdignore` empêche Godot d’importer le contenu du dossier concerné. Les ressources placées sous ce dossier ne doivent donc pas être chargées avec `load()` ou `preload()`.

### 13.1 Structure de départ

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
project-asteria/
├── project.godot
├── README.md
├── .gitignore
├── assets/
│   └── shared/
├── src/
│   ├── core/
│   └── features/
│       ├── bootstrap/
│       ├── player/
│       ├── world/
│       └── ui/
├── data/
├── localization/
├── tests/
├── tools/
├── docs/
│   └── .gdignore
└── logs/
```

### 13.2 Organisation par fonctionnalité

Le projet regroupe autant que possible les ressources proches de la fonctionnalité qui les utilise :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
src/features/player/
├── player.tscn
├── player.gd
├── player_input.gd
├── player_camera.tscn
├── materials/
├── audio/
└── tests/
```

Cette organisation limite les dossiers globaux gigantesques comme `scripts/`, `scenes/` ou `textures/` qui finissent par mélanger des systèmes sans rapport.

### 13.3 Ressources réellement partagées

`assets/shared/` est réservé aux ressources utilisées par plusieurs fonctionnalités :

- matériaux communs ;
- icônes génériques ;
- sons d’interface partagés ;
- shaders communs ;
- polices ;
- maillages de débogage.

Une ressource utilisée par un seul système reste près de ce système.

## 14. Créer la scène principale

### 14.1 Nœud racine

Dans l’éditeur :

1. choisir **3D Scene** ;
2. renommer le nœud racine `Main` ;
3. sauvegarder la scène sous :

> **[APP] Godot - Enregistrer :** sauvegarder la scène sous le chemin ci-dessous.

```text
res://src/features/bootstrap/main.tscn
```

Le nœud racine est un `Node3D`.

### 14.2 Ajouter l’environnement

Ajouter comme enfants de `Main` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
WorldEnvironment
DirectionalLight3D
```

> **[APP] Godot - Inspector :** créer et affecter la ressource décrite.

Créer une nouvelle ressource `Environment` dans la propriété **Environment** de `WorldEnvironment`.

Réglages simples :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Background Mode     Color
Background Color    bleu-gris sombre
Ambient Light       activée à faible intensité
```

Ces valeurs servent uniquement au test initial. La direction artistique sera traitée dans le Livre III.

### 14.3 Ajouter une lumière

Pour `DirectionalLight3D` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Nom                 Sun
Rotation Degrees    X = -50, Y = -30, Z = 0
Shadows             Enabled
```

### 14.4 Ajouter un sol

Créer cette structure :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Ground (StaticBody3D)
├── MeshInstance3D
└── CollisionShape3D
```

Pour `MeshInstance3D` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Mesh    PlaneMesh
Size    20 × 20
```

Pour `CollisionShape3D` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Shape       BoxShape3D
Size        X = 20, Y = 0.2, Z = 20
Position    Y = -0.1
```

La collision correspond approximativement au plan visible.

### 14.5 Ajouter un marqueur visuel

Ajouter à `Main` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Marker (MeshInstance3D)
```

Réglages :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Mesh        BoxMesh
Size        X = 1, Y = 2, Z = 1
Position    X = 0, Y = 1, Z = 0
```

> **[APP] Godot - Inspector :** créer le matériau et régler sa couleur.

Créer un `StandardMaterial3D` et lui attribuer une couleur facilement visible.

### 14.6 Ajouter la caméra

Ajouter :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
CameraRig (Node3D)
└── Camera3D
```

Réglages de `Camera3D` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Position            X = 0, Y = 4, Z = 8
Rotation Degrees    X = -20, Y = 0, Z = 0
Current             activé
```

La caméra regarde dans la direction négative de l’axe Z. Depuis `Z = 8`, elle voit l’origine.

### 14.7 Ajouter une indication à l’écran

Ajouter :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
HUD (CanvasLayer)
└── MarginContainer
    └── Label
```

Texte du `Label` :

> **[APP] Godot - Créer ou configurer :** utiliser l’arbre de scène et l’Inspector avec les valeurs ci-dessous.

```text
Project Asteria — Bootstrap OK
```

> **[APP] Godot - Interface :** régler les ancres et marges dans l’éditeur 2D.

Utiliser les ancres et marges pour placer le texte en haut à gauche sans coder une position absolue dépendante de la résolution.

## 15. Ajouter le premier script

### 15.1 Créer le fichier

Attacher un script à `Main` :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
res://src/features/bootstrap/main.gd
```

Contenu :

> **[VSC] Visual Studio Code - Créer :** `res://src/features/bootstrap/main.gd`.

```gdscript
extends Node3D

const VALIDATION_ID: StringName = &"DOC-L2-CH01"
const ROTATION_SPEED: float = 0.5

@onready var marker: MeshInstance3D = $Marker


func _ready() -> void:
    print("%s : scène principale prête." % VALIDATION_ID)


func _process(delta: float) -> void:
    marker.rotate_y(ROTATION_SPEED * delta)
```

### 15.2 Ce que fait le script

- `extends Node3D` indique le type de nœud étendu ;
- les constantes nomment des valeurs stables ;
- `@onready` récupère le nœud `Marker` lorsque la scène est prête ;
- `_ready()` écrit une preuve dans le panneau Output ;
- `_process()` fait tourner le marqueur à chaque image ;
- `delta` rend la rotation indépendante du nombre d’images par seconde.

Le chapitre suivant expliquera la syntaxe GDScript en détail.

### 15.3 Nommage

Le projet utilise :

| Élément | Convention | Exemple |
|---|---|---|
| Fichier GDScript | `snake_case.gd` | `main.gd` |
| Scène | `snake_case.tscn` | `main.tscn` |
| Classe | `PascalCase` | `PlayerController` |
| Variable | `snake_case` | `rotation_speed` |
| Constante | `UPPER_SNAKE_CASE` | `ROTATION_SPEED` |
| Nœud dans l’éditeur | `PascalCase` lisible | `CameraRig` |
| Signal | passé ou événement explicite | `health_changed` |

## 16. Définir la scène principale

Dans l’éditeur :

> **[APP] Godot - Configurer :** utiliser **Project Settings > Application > Run > Main Scene** avec la valeur ci-dessous.

```text
Project
└── Project Settings
    └── Application
        └── Run
            └── Main Scene
```

Sélectionner :

> **[APP] Godot - Configurer :** utiliser **Project Settings > Application > Run > Main Scene** avec la valeur ci-dessous.

```text
res://src/features/bootstrap/main.tscn
```

Une autre méthode consiste à appuyer sur `F5` lors du premier lancement et à choisir la scène courante comme scène principale.

## 17. Exécuter et observer

### 17.1 Scène courante

Appuyer sur :

> **[APP] Godot - Exécuter :** utiliser le raccourci ci-dessous pour lancer la scène courante.

```text
F6
```

Godot exécute uniquement la scène ouverte.

### 17.2 Projet complet

Appuyer sur :

> **[APP] Godot - Exécuter :** utiliser le raccourci ci-dessous pour lancer le projet complet.

```text
F5
```

Godot exécute la scène principale définie dans les paramètres du projet.

### 17.3 Résultat attendu

La fenêtre doit afficher :

- un sol ;
- un marqueur vertical ;
- un éclairage ;
- le texte `Project Asteria — Bootstrap OK` ;
- une rotation lente du marqueur.

Le panneau Output doit contenir :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec le panneau **Output** de Godot.

```text
DOC-L2-CH01 : scène principale prête.
```

### 17.4 Arrêter

> **[APP] Godot - Arrêter :** utiliser le raccourci ci-dessous pour arrêter l’exécution.

```text
F8
```

Vérifier qu’aucune erreur rouge n’apparaît dans Output ou Debugger.

## 18. Tester depuis PowerShell

### 18.1 Import sans interface

Depuis la racine du projet :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --headless --path . --import
```

Cette commande demande à l’éditeur d’importer les ressources puis de quitter.

### 18.2 Test de démarrage

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force .\logs | Out-Null

& $env:GODOT_EXE `
  --headless `
  --path . `
  --quit-after 5 `
  --log-file .\logs\bootstrap-smoke.log

if ($LASTEXITCODE -ne 0) {
    throw "Le test Godot a échoué avec le code $LASTEXITCODE."
}
```

`--quit-after 5` signifie cinq itérations de la boucle principale, et non cinq secondes. Ce nombre laisse la scène entrer dans `_ready()` tout en conservant un test très court.

Lire le journal :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Content .\logs\bootstrap-smoke.log
```

Rechercher :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
DOC-L2-CH01 : scène principale prête.
```

Le mode headless valide le chargement du projet et des scripts. Il ne remplace pas le contrôle visuel du rendu Forward+.

### 18.3 Journal détaillé

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE `
  --verbose `
  --headless `
  --path . `
  --quit-after 5 `
  --log-file .\logs\bootstrap-verbose.log
```

Le journal détaillé est utile pour identifier :

- la version du moteur ;
- le pilote utilisé ;
- les ressources chargées ;
- les erreurs de script ;
- les avertissements d’import.

## 19. Premier commit

### 19.1 Vérifier l’état

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git status --short
git diff --check
```

Le dossier `.godot/` ne doit pas apparaître.

### 19.2 Ajouter les sources

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git add .gitattributes .gitignore README.md project.godot icon.svg src docs data localization tests tools
```

Vérifier la sélection :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git diff --cached --stat
git diff --cached
```

### 19.3 Créer le commit

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git commit -m "feat(project): initialize Godot project bootstrap"
```

### 19.4 Étiqueter le point de départ

Après validation :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git tag -a bootstrap-godot-4.7.1 -m "Base Godot 4.7.1 validée"
```

Le tag permet de retrouver la base avant l’ajout des systèmes de gameplay.

## 20. Fichiers à versionner ou ignorer

| Élément | Versionner | Motif |
|---|---|---|
| `project.godot` | oui | configuration du projet |
| fichiers `.tscn` | oui | scènes textuelles |
| fichiers `.gd` | oui | code source |
| textures et modèles sources | oui ou LFS | sources nécessaires |
| fichiers `.tres` | oui | ressources textuelles |
| `.godot/` | non | cache et données générées |
| `user://` | non | données propres à l’utilisateur |
| logs runtime | non par défaut | bruit et données locales |
| builds exportés | non par défaut | livrables générés |
| secrets | jamais | sécurité |

Les gros fichiers binaires peuvent nécessiter Git LFS. Cette décision doit être prise avant l’accumulation d’un historique volumineux.

## 21. Ce qu’il ne faut pas modifier manuellement

Éviter de modifier à la main :

- les fichiers du dossier `.godot/` ;
- les caches d’import ;
- les UID sans comprendre leur rôle ;
- une scène `.tscn` pendant qu’elle est ouverte et modifiée dans l’éditeur ;
- `project.godot` simultanément dans plusieurs branches sans revue du conflit.

Les scènes et ressources textuelles peuvent être relues dans Git, mais les modifications doivent normalement être produites par l’éditeur ou par un outil contrôlé.

## 22. UID et chemins de ressources

Godot utilise des chemins `res://` et des identifiants de ressources.

Lorsqu’un fichier est déplacé depuis le dock FileSystem de l’éditeur, Godot peut mettre à jour les références connues. Un déplacement effectué directement dans l’Explorateur Windows peut laisser des références cassées.

Règle :

> Déplacer ou renommer les scènes et ressources depuis le dock FileSystem de Godot, puis vérifier le diff Git et relancer le projet.

Pour les opérations en lot :

1. créer une branche ;
2. fermer les scènes concernées ;
3. effectuer le déplacement ;
4. laisser Godot réimporter ;
5. rechercher les erreurs de chargement ;
6. exécuter les tests ;
7. examiner les modifications de chemins.

## 23. Gestion des addons

Le dossier standard des extensions est :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
res://addons/
```

Aucun addon tiers n’est nécessaire dans ce chapitre.

Avant d’installer un addon :

- vérifier le dépôt source ;
- vérifier la licence ;
- vérifier la version de Godot prise en charge ;
- lire le code ou la documentation de sécurité ;
- tester dans une branche ;
- enregistrer la version ou le commit ;
- éviter les mises à jour automatiques non contrôlées.

Une extension d’éditeur peut exécuter du code avec les permissions de l’utilisateur. Elle ne doit pas être traitée comme une simple image ou un asset passif.

## 24. Paramètres de l’éditeur et paramètres du projet

### 24.1 Editor Settings

Les paramètres d’éditeur concernent le poste de travail :

- thème ;
- raccourcis ;
- éditeur de code externe ;
- comportement de l’interface ;
- chemins vers certains outils.

Ils ne définissent pas le comportement final du jeu.

### 24.2 Project Settings

Les paramètres du projet concernent le jeu :

- scène principale ;
- moteur de rendu ;
- résolution ;
- actions d’entrée ;
- couches physiques ;
- autoloads ;
- internationalisation ;
- paramètres d’export.

Les modifications importantes de Project Settings doivent être incluses dans le même commit que le code qui les utilise.

## 25. Qualité de la scène de bootstrap

La scène de bootstrap n’est pas un niveau final. Elle doit rester :

- légère ;
- rapide à charger ;
- sans asset externe obligatoire ;
- sans plugin ;
- sans service réseau ;
- utilisable pour diagnostiquer le moteur ;
- compatible avec un test headless ;
- facile à comparer visuellement.

Elle servira ensuite à charger les services globaux et la première scène de jeu.

## 26. Mode Solo

Le Mode Solo applique :

- un seul dépôt de jeu ;
- Godot Standard uniquement ;
- Forward+ comme profil principal ;
- une scène de bootstrap minimale ;
- des commits petits et fréquents ;
- aucun addon tant qu’une fonctionnalité native suffit ;
- une sauvegarde locale plus une copie externe ;
- un seul environnement stable et une copie de test pour les migrations.

Le développeur solo doit pouvoir reconstruire le poste à partir du README, du dépôt et de l’inventaire logiciel.

## 27. Mode Studio

Le Mode Studio ajoute :

- une version de Godot approuvée ;
- un registre des addons ;
- un dépôt partagé et protégé ;
- des branches et pull requests ;
- Git LFS configuré avant les gros assets ;
- des conventions de verrouillage pour les fichiers binaires ;
- un script de validation headless ;
- des machines de test avec plusieurs profils graphiques ;
- une procédure de migration d’éditeur ;
- une personne responsable de l’intégration du projet Godot.

Un studio ne doit pas laisser chaque membre adopter une version différente de l’éditeur sans validation.

## 28. Erreurs fréquentes

<!-- qa:error-correction-section -->

Chaque cas associe désormais une situation fautive, une correction observable et l’explication de la différence.

### 28.1 Le projet n’apparaît pas dans le Project Manager

**Symptôme ou risque :** le mauvais dossier est importé et `project.godot` se trouve un niveau plus bas.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
C:\IA-GameDev\projects\project-asteria\project-asteria\project.godot
```

**Correction :** importer le dossier qui contient directement `project.godot` et vérifier son existence avant l’ouverture.

> **[PS] PowerShell 7 — Exemple corrigé depuis le dossier supposé du projet.**

```powershell
Set-Location C:\IA-GameDev\projects\project-asteria
Test-Path .\project.godot
```

**Différence :** le premier exemple montre une extraction imbriquée ; le second vérifie la racine exacte attendue par Godot.

### 28.2 L’éditeur utilise une autre version

**Symptôme ou risque :** un double-clic ouvre le projet avec l’association Windows, qui peut viser une version non approuvée.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Double-cliquer sur project.godot sans vérifier l’exécutable associé.
```

**Correction :** lancer explicitement l’exécutable de référence et contrôler sa version.

> **[PS] PowerShell 7 — Exemple corrigé avec l’exécutable approuvé.**

```powershell
$env:GODOT_EXE = 'C:\IA-GameDev\apps\godot\4.7.1-standard\Godot_v4.7.1-stable_win64.exe'
& $env:GODOT_EXE --version
& $env:GODOT_EXE --editor --path .
```

**Différence :** le lancement explicite rend la version reproductible, alors que l’association de fichiers reste implicite.

### 28.3 Écran vide au lancement

**Symptôme ou risque :** la scène principale ne contient aucune caméra active ou la caméra ne regarde pas le marqueur.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Main
└── Marker
```

**Correction :** utiliser une scène minimale qui contient une caméra active, une lumière et le marqueur visible.

> **[LECTURE] Structure corrigée à reproduire dans Godot.**

```text
Main
├── Camera3D (Current = On)
├── DirectionalLight3D
└── Marker
```

**Différence :** la scène corrigée fournit les éléments indispensables au rendu ; la scène fautive ne définit aucun point de vue.

### 28.4 La scène courante fonctionne, mais pas le projet

**Symptôme ou risque :** `F6` valide une scène isolée alors que `F5` lance une autre scène principale ou aucune scène.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
F6 → res://scenes/learning/bootstrap_test.tscn
F5 → scène principale absente
```

**Correction :** définir `main.tscn` comme scène principale et vérifier aussi le lancement du projet.

> **[APP] Godot — Exemple corrigé dans Project > Project Settings > Run.**

```text
Main Scene = res://src/features/bootstrap/main.tscn
F5 → main.tscn
```

**Différence :** le test corrigé valide le vrai point d’entrée du jeu, pas seulement une scène ouverte dans l’éditeur.

### 28.5 Le script ne trouve pas `Marker`

**Symptôme ou risque :** le chemin suppose un enfant direct alors que le nœud a été renommé ou déplacé.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
@onready var marker: MeshInstance3D = $Marker
```

**Correction :** aligner l’arbre et le chemin, ou rendre la dépendance explicite avec un nœud exporté.

> **[VSC] Visual Studio Code — Exemple corrigé avec une dépendance assignée dans l’Inspector.**

```gdscript
@export_node_path('MeshInstance3D') var marker_path: NodePath
@onready var marker := get_node(marker_path) as MeshInstance3D
```

**Différence :** le chemin fautif est caché dans le script ; la version corrigée expose le chemin et permet sa vérification dans l’Inspector.

### 28.6 Le rendu Forward+ ne démarre pas

**Symptôme ou risque :** le projet est relancé sans journal et plusieurs paramètres sont modifiés simultanément.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Changer le pilote, le renderer et la scène en même temps, puis relancer sans --verbose.
```

**Correction :** isoler le moteur de rendu avec un journal, puis tester un seul profil de secours à la fois.

> **[PS] PowerShell 7 — Exemple corrigé de diagnostic contrôlé.**

```powershell
& $env:GODOT_EXE --verbose --editor --path . --rendering-method mobile --log-file .\logs\mobile-test.log
```

**Différence :** le diagnostic corrigé conserve une trace et ne change qu’une variable, ce qui permet d’identifier la couche fautive.

### 28.7 Git suit `.godot/`

**Symptôme ou risque :** le cache a été ajouté à l’index avant la création ou la correction de `.gitignore`.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```powershell
git add .
git commit -m 'chore: add every generated file'
```

**Correction :** ignorer le dossier et le retirer seulement de l’index Git, sans supprimer le cache local.

> **[PS] PowerShell 7 — Exemple corrigé depuis la racine du projet.**

```powershell
Add-Content .gitignore '/.godot/'
git rm -r --cached .godot
git add .gitignore
git commit -m 'chore(git): stop tracking Godot cache'
```

**Différence :** `--cached` cesse le suivi tout en conservant les fichiers sur le poste ; l’exemple fautif versionne des données régénérables.

### 28.8 Déplacement de fichier cassant une scène

**Symptôme ou risque :** une scène ou Resource est déplacée dans l’Explorateur Windows sans mise à jour des références Godot.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Explorateur Windows : déplacer status_beacon.tscn vers un autre dossier pendant que Godot est fermé.
```

**Correction :** effectuer le déplacement depuis le dock FileSystem, puis rechercher les anciens chemins et relancer l’import.

> **[APP] Godot — Exemple corrigé à exécuter depuis le dock FileSystem.**

```text
FileSystem : Move To…
Puis vérifier Output, les scènes dépendantes et git diff.
```

**Différence :** Godot peut mettre à jour les références connues lors du déplacement corrigé ; l’Explorateur ne connaît pas ces dépendances.

## 29. Diagnostic par couches

### Couche 1 — Exécutable

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --version
```

### Couche 2 — Projet

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Test-Path .\project.godot
```

### Couche 3 — Import

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --headless --path . --import
```

### Couche 4 — Scripts

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
& $env:GODOT_EXE --headless --path . --quit-after 5
```

### Couche 5 — Rendu

> **[APP] Godot - Exécuter :** lancer la scène et vérifier visuellement le résultat.

Lancer l’éditeur, exécuter la scène et vérifier caméra, lumière et moteur de rendu.

### Couche 6 — Versionnement

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git status --short
git diff --check
```

### Couche 7 — Régression

Revenir temporairement au tag `bootstrap-godot-4.7.1` dans une copie de travail et comparer le comportement.

## 30. Validation du chapitre

### 30.1 Checklist obligatoire

- [ ] Godot 4.7.1-stable Standard est extrait dans un dossier versionné par numéro.
- [ ] La source et l’empreinte de l’archive sont enregistrées.
- [ ] `$env:GODOT_EXE` pointe vers la bonne version.
- [ ] Le projet `Project Asteria` existe.
- [ ] Le renderer principal est Forward+.
- [ ] Git ignore `.godot/` et `*.translation`.
- [ ] `.gitattributes` normalise les fichiers texte en LF.
- [ ] L’arborescence de base est créée.
- [ ] `docs/.gdignore` existe.
- [ ] La scène `main.tscn` possède caméra, lumière, sol et marqueur.
- [ ] Le script `main.gd` est attaché.
- [ ] `F6` exécute la scène courante.
- [ ] `F5` exécute la scène principale.
- [ ] Le marqueur tourne.
- [ ] Le message `DOC-L2-CH01` apparaît dans Output.
- [ ] Le test headless termine avec un code de sortie nul.
- [ ] Le premier commit Git est créé.
- [ ] Le tag de bootstrap est créé après validation.
- [ ] Aucun addon tiers n’est requis.
- [ ] La licence MIT de Godot et les notices tierces sont enregistrées pour la future distribution.

### 30.2 Critère d’acceptation

Le chapitre est validé lorsque :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Godot --version         → 4.7.1 stable
ouverture du projet     → succès
import headless         → succès
exécution F5            → scène visible
Output                  → DOC-L2-CH01 présent
rotation du marqueur    → visible
Git                     → dépôt propre après commit
cache .godot            → non suivi
```

## 31. Preuves à conserver

Créer :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\logs\project-asteria\chapter-01\
```

Y conserver :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
godot-version.txt
bootstrap-smoke.log
bootstrap-verbose.log
git-status.txt
project-tree.txt
validation-notes.md
screenshot-bootstrap.png
```

Exemple :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$dest = "C:\IA-GameDev\logs\project-asteria\chapter-01"
New-Item -ItemType Directory -Force $dest | Out-Null

& $env:GODOT_EXE --version |
  Out-File "$dest\godot-version.txt" -Encoding utf8

git status --short |
  Out-File "$dest\git-status.txt" -Encoding utf8

Get-ChildItem -Recurse -File |
  Where-Object FullName -NotMatch "\\.godot\\" |
  Select-Object FullName |
  Out-File "$dest\project-tree.txt" -Encoding utf8
```

Les captures et journaux peuvent contenir des chemins utilisateur. Les nettoyer avant partage public.

## 32. Décisions retenues

| Décision | Statut |
|---|---|
| Godot 4.7.1-stable comme référence | retenu |
| Godot 4.8-dev pour le parcours principal | écarté |
| Édition Standard | retenu |
| C# obligatoire | écarté |
| GDScript comme langage principal | retenu |
| Forward+ comme renderer principal | retenu |
| Mobile comme profil secondaire | retenu |
| Compatibility comme profil ancien/Web | retenu |
| Organisation par fonctionnalité | retenu |
| Dossier global unique pour tous les scripts | écarté |
| `.godot/` versionné | interdit |
| Addon tiers obligatoire au démarrage | écarté |
| Test visuel et test headless | obligatoires |
| Mise à jour directe sans branche | interdite |

## 33. Sources officielles vérifiées

- [Godot 4.7.1 — version de maintenance](https://godotengine.org/article/maintenance-release-godot-4-7-1/)
- [Archive officielle des versions Godot](https://godotengine.org/download/archive/)
- [Documentation Godot 4.7](https://docs.godotengine.org/en/4.7/)
- [Configuration système requise](https://docs.godotengine.org/en/4.7/about/system_requirements.html)
- [Concepts principaux de Godot](https://docs.godotengine.org/en/4.7/getting_started/introduction/key_concepts_overview.html)
- [Nœuds et scènes](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/nodes_and_scenes.html)
- [Organisation du projet](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html)
- [Systèmes de contrôle de version](https://docs.godotengine.org/en/4.7/tutorials/best_practices/version_control_systems.html)
- [Architecture interne du rendu](https://docs.godotengine.org/en/4.7/engine_details/architecture/internal_rendering_architecture.html)
- [Conformité à la licence Godot](https://docs.godotengine.org/en/4.7/about/complying_with_licenses.html)
- [Tutoriel de ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Introduction à la 3D](https://docs.godotengine.org/en/4.7/tutorials/3d/introduction_to_3d.html)
- [Premier jeu 3D](https://docs.godotengine.org/en/4.7/getting_started/first_3d_game/)

## 34. Résumé

Le projet fil rouge possède maintenant une base contrôlée :

- Godot 4.7.1-stable Standard ;
- GDScript ;
- Forward+ ;
- une arborescence organisée par fonctionnalité ;
- une scène principale 3D ;
- un script minimal ;
- une validation graphique et headless ;
- des métadonnées Git complètes avec `.gitignore` et `.gitattributes` ;
- une stratégie d’attribution pour la licence MIT de Godot ;
- un premier commit et un tag de référence.

Le chapitre suivant explique GDScript de manière progressive : variables, types, fonctions, conditions, boucles, classes, ressources et erreurs courantes.
