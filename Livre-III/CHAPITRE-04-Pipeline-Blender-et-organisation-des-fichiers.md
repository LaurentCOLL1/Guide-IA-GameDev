---
title: "Livre III — Chapitre 4 : Pipeline Blender et organisation des fichiers"
id: "DOC-L3-CH04"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 4
last-verified: "2026-07-22T22:37:42+02:00"
audit-status: "complete"
audit-date: "2026-07-22T22:37:42+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-04.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
reference-tools:
  blender:
    version: "5.2.0"
    channel: "Stable"
    qualification: "documentation-reviewed"
  exchange:
    format: "glTF 2.0"
    default-container: "GLB"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Pipeline Blender et organisation des fichiers

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH04`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Blender `5.2.0` Stable, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Les trois premiers chapitres ont défini le besoin artistique, la bible visuelle et la chaîne de références et de concepts. Le présent chapitre installe la **colonne vertébrale des fichiers 3D** : environnement Blender, unités, axes, origines, collections, bibliothèques, versions, sauvegardes, exports et contrôle d’arrivée dans Godot.

Le résultat attendu n’est pas encore un personnage, un décor ou un objet définitif. Il s’agit d’un environnement reproductible dans lequel un asset test peut être ouvert, contrôlé, exporté, importé dans Godot puis repris sur une autre machine sans ambiguïté entre la source, le travail intermédiaire, le cache, l’export et la livraison.

> **[LECTURE] Chaîne de production couverte — Ne pas saisir.**

```text
Concept retenu et contraintes de la bible
    ↓
Source Blender canonique
    ↓
Fichier de travail versionné
    ↓
Collection d’export explicite
    ↓
Validation statique Blender
    ↓
Export glTF 2.0 / GLB
    ↓
Import et contrôle dans Godot
    ↓
Rapport de livraison et empreinte
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** la chaîne sépare les états du fichier et place une porte de contrôle avant et après l’échange.
- **Déroulement :** le concept guide la source modifiable ; seule la collection d’export devient un fichier d’échange ; Godot valide ensuite le résultat transformé.
- **Invariant :** aucun export généré ne remplace la source Blender canonique.
- **Résultat attendu :** une personne peut identifier l’autorité de chaque fichier et reproduire le passage Blender vers Godot.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- qualifier une version de Blender et ses extensions avant adoption ;
- configurer les unités métriques, l’échelle, l’orientation et les origines ;
- distinguer scène de travail, bibliothèque liée, variante, cache, export et livraison ;
- créer une arborescence stable et des conventions de nommage ;
- choisir entre GLB, glTF séparé et import direct de fichier `.blend` ;
- produire un asset test d’un mètre et contrôler sa position, son orientation et ses dépendances dans Godot ;
- appliquer un parcours Solo réduit ou un parcours Studio avec publication immuable ;
- diagnostiquer les ruptures de chemin, d’échelle, de pivot et de version.

## 3. Niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Les procédures, paramètres, scripts et formats ont été relus contre les documentations officielles, mais aucun template Blender réel, aucune bibliothèque partagée, aucun asset test, aucun export GLB et aucune scène Godot ne sont revendiqués comme exécutés.

Blender `5.2.0` Stable constitue la version documentaire de référence au 22 juillet 2026. Le projet n’impose aucun add-on tiers : l’importateur-exportateur glTF 2.0 fourni avec Blender couvre le chemin de référence. Toute extension future devra être qualifiée séparément par version, source, licence, permissions, compatibilité, maintenance et procédure de retrait.

Aucune mesure de temps d’export, de taille de fichier, de mémoire, de GPU ou de réimport n’est inventée. Ces valeurs seront consignées seulement après exécution sur la machine de référence et sur des assets pilotes réels.

## 4. Qualifier la chaîne d’outils

La chaîne minimale est :

- Windows 11 ;
- Blender `5.2.0` Stable téléchargé depuis `blender.org` ;
- export glTF 2.0 fourni avec Blender ;
- Godot `4.7.1-stable`, édition Standard, rendu Forward+ ;
- PowerShell 7 pour les contrôles et empreintes ;
- Visual Studio Code pour les manifestes et scripts ;
- Git et Git LFS selon les décisions de stockage du projet.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/TOOLCHAIN.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
qualified_on: "2026-07-22"
platform:
  os: "Windows 11"
tools:
  blender:
    version: "5.2.0"
    channel: "Stable"
    source: "https://www.blender.org/download/"
    qualification: "documentation-reviewed"
  godot:
    version: "4.7.1-stable"
    edition: "Standard"
    renderer: "Forward+"
exchange:
  specification: "glTF 2.0"
  default_container: "GLB"
  direct_blend_import:
    allowed_for: "solo_iteration_only"
third_party_addons: []
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `qualification` décrit le niveau de preuve ; `runtime_status` interdit de confondre revue documentaire et exécution.
- **Dépendances :** l’export de référence ne dépend d’aucun add-on tiers ajouté au projet.
- **Frontière :** le manifeste qualifie les outils, pas les assets ni leurs licences, qui restent traités par leur registre propre.
- **Résultat attendu :** une reprise peut identifier exactement les versions prévues et les réserves encore ouvertes.

## 5. Responsabilités des fichiers

Le pipeline distingue six familles :

1. **source canonique** : fichier `.blend` modifiable qui porte la construction de l’asset ;
2. **travail** : copie ou branche de travail susceptible d’être abandonnée ;
3. **bibliothèque** : contenu partagé lié ou ajouté à plusieurs sources ;
4. **cache** : données reconstruisibles, temporaires ou propres à une machine ;
5. **export** : résultat généré pour l’échange technique ;
6. **livraison** : export approuvé, accompagné de son manifeste et de son empreinte.

Un même fichier ne doit pas cumuler silencieusement plusieurs autorités. Un `.glb` placé dans un dossier de livraison n’est pas une source à modifier. Un `.blend` de travail ne devient pas une version publiée parce qu’il porte un nom proche de la version finale.

## 6. Arborescence canonique

L’arborescence suivante sépare les éléments versionnés, les données locales et les sorties publiées :

> **[LECTURE] Arborescence de référence — Ne pas saisir.**

```text
ProjectAsteria/
├── art/
│   └── blender/
│       ├── templates/
│       │   └── ASTERIA-BLENDER-TEMPLATE.blend
│       ├── sources/
│       │   ├── characters/
│       │   ├── creatures/
│       │   ├── props/
│       │   └── environments/
│       ├── libraries/
│       │   ├── materials/
│       │   ├── rigs/
│       │   └── shared/
│       ├── work/
│       ├── cache/
│       ├── exports/
│       │   ├── glb/
│       │   └── gltf/
│       ├── delivery/
│       ├── archive/
│       ├── manifests/
│       ├── presets/
│       └── tests/
│           └── roundtrip/
└── game/
    └── assets/
        └── imported/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** l’arbre rend immédiatement visibles les sources, les sorties générées, les publications et les caches.
- **Autorité :** `sources/` porte l’autorité de création ; `delivery/` porte l’autorité de distribution interne ; `cache/` reste supprimable.
- **Dépendances :** les bibliothèques partagées résident sous une racine stable pour permettre des chemins relatifs.
- **Résultat attendu :** une seconde machine retrouve la même topologie sans dépendre du profil Windows d’un artiste.

> **[PS] PowerShell 7 — Créer les dossiers depuis la racine de `ProjectAsteria`.**

```powershell
$paths = @(
  "art/blender/templates",
  "art/blender/sources/characters",
  "art/blender/sources/creatures",
  "art/blender/sources/props",
  "art/blender/sources/environments",
  "art/blender/libraries/materials",
  "art/blender/libraries/rigs",
  "art/blender/libraries/shared",
  "art/blender/work",
  "art/blender/cache",
  "art/blender/exports/glb",
  "art/blender/exports/gltf",
  "art/blender/delivery",
  "art/blender/archive",
  "art/blender/manifests",
  "art/blender/presets",
  "art/blender/tests/roundtrip",
  "game/assets/imported"
)
$paths | ForEach-Object {
  New-Item -ItemType Directory -Path $_ -Force | Out-Null
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `$paths` est une liste de chemins relatifs à la racine courante.
- **Instruction importante :** `New-Item -Force` crée les dossiers absents sans supprimer leur contenu lorsqu’ils existent déjà.
- **Effet de bord :** la commande modifie uniquement l’arborescence ; elle ne crée ni asset ni manifeste.
- **Résultat attendu :** toutes les racines du pipeline existent avec les mêmes noms sur chaque poste.

## 7. Convention d’identifiants, noms et versions

Un identifiant stable ne dépend ni du nom d’affichage ni du chemin du fichier. La convention de `Project Asteria` utilise :

- `AST-CHR-...` pour un personnage ;
- `AST-CRT-...` pour une créature ;
- `AST-PRP-...` pour un objet ;
- `AST-ENV-...` pour un environnement ;
- `AST-MAT-...` pour un matériau partagé ;
- `AST-RIG-...` pour un rig publié.

Les noms de fichiers emploient des segments ASCII, des tirets, une version à trois chiffres et un suffixe d’état. Exemple : `AST-PRP-BEACON-001-v003-source.blend`.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/NAMING-CONVENTIONS.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id_pattern: '^AST-(CHR|CRT|PRP|ENV|MAT|RIG)-[A-Z0-9]+-[0-9]{3}$'
file_pattern: '^[A-Z0-9-]+-v[0-9]{3}-(source|work|export|delivery)\.[a-z0-9]+$'
collection_suffixes:
  geometry: "__GEO"
  rig: "__RIG"
  sockets: "__SOCKETS"
  collision_guides: "__COLLISION_GUIDES"
  guides: "__GUIDES"
  export: "__EXPORT"
immutable_states:
  - "delivery"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** les motifs sont des expressions régulières ; les suffixes sont des chaînes contractuelles.
- **Invariant :** un fichier `delivery` est immuable ; une correction produit une nouvelle version.
- **Effet de bord :** un validateur peut refuser un nom non conforme avant export ou publication.
- **Résultat attendu :** les fichiers restent triables et reconnaissables sans ouvrir Blender.

## 8. Installer Blender sans mélanger les profils

> **[WEB] Navigateur — Télécharger Blender `5.2.0` Stable depuis le site officiel.**

Le parcours de référence utilise une distribution officielle. Une installation portable peut isoler les préférences du projet, mais le choix doit être commun à l’équipe. Copier aveuglément un profil utilisateur complet est déconseillé : il peut introduire des extensions, raccourcis et chemins non qualifiés.

> **[APP] Blender — Ouvrir `Edit > Preferences` et vérifier les extensions actives.**

La liste attendue ne contient aucun add-on tiers obligatoire. Si une extension devient nécessaire, elle reçoit une entrée de qualification avant d’être activée sur le profil de production.

> **[PS] PowerShell 7 — Enregistrer le chemin de Blender pour la session courante.**

```powershell
$env:ASTERIA_BLENDER_EXE = "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"
if (-not (Test-Path $env:ASTERIA_BLENDER_EXE)) {
  throw "Blender introuvable au chemin qualifié."
}
& $env:ASTERIA_BLENDER_EXE --version
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la variable d’environnement contient le chemin absolu local de l’exécutable, jamais un chemin enregistré dans un asset.
- **Refus contrôlé :** `throw` arrête la procédure si l’exécutable n’existe pas.
- **Effet de bord :** la variable vaut pour le processus PowerShell courant et ses processus enfants.
- **Résultat attendu :** la sortie affiche une version commençant par `Blender 5.2`.

## 9. Construire le template Blender

> **[APP] Blender — Créer un fichier vide depuis `File > New > General`.**

Le template doit contenir seulement les décisions transversales : unités, scène de contrôle, collections racines, conventions d’affichage et métadonnées du projet. Il ne doit pas embarquer un personnage, un rig, une texture externe ou une préférence personnelle.

Créer les collections suivantes :

- `AST-TEMPLATE__GEO` ;
- `AST-TEMPLATE__RIG` ;
- `AST-TEMPLATE__SOCKETS` ;
- `AST-TEMPLATE__COLLISION_GUIDES` ;
- `AST-TEMPLATE__GUIDES` ;
- `AST-TEMPLATE__EXPORT`.

Enregistrer le fichier sous `art/blender/templates/ASTERIA-BLENDER-TEMPLATE.blend`. La fonction `File > Defaults > Save Startup File` modifie le profil Blender global ; elle n’est pas le mécanisme canonique du projet. Le projet distribue le fichier template explicitement.

## 10. Fixer les unités et l’échelle

> **[APP] Blender — Ouvrir `Scene Properties > Units`.**

Configurer :

- `Unit System` : `Metric` ;
- `Unit Scale` : `1.000000` ;
- `Length` : `Meters` ;
- `Rotation` : `Degrees` ;
- gravité : conserver une valeur cohérente avec l’échelle choisie lorsque la simulation sera abordée.

Dans ce pipeline, **une unité Blender représente un mètre**. Le champ `Unit Scale` influence surtout l’affichage et ne doit pas servir à réparer une géométrie créée cent fois trop petite. Une erreur d’échelle se corrige dans la source et se vérifie avec un objet étalon.

> **[LECTURE] Contrat d’échelle — Ne pas saisir.**

```text
1 unité Blender = 1 mètre
Cube de contrôle = 1 m × 1 m × 1 m
Sol de contrôle = Z = 0 dans Blender
Hauteur de contrôle = Z = 1 dans Blender
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** l’étalon transforme une convention abstraite en mesures vérifiables.
- **Invariant :** le fichier source ne compense pas une erreur de dimensions par une échelle globale exotique.
- **Frontière :** les budgets de taille propres aux personnages, bâtiments ou terrains seront définis dans leurs chapitres spécialisés.
- **Résultat attendu :** le cube importé dans Godot possède une boîte englobante d’environ un mètre sur chaque axe.

## 11. Comprendre les axes Blender et Godot

Blender travaille avec `Z` vers le haut. Godot utilise `Y` vers le haut. glTF transporte la scène selon sa propre convention et les importateurs effectuent la conversion attendue. Le pipeline ne demande donc pas de faire pivoter manuellement tous les objets ou d’ajouter un parent tourné à 90 degrés.

Pour un asset orienté, la convention Godot considère `+Z` comme l’avant du modèle. Dans Blender, cela correspond à `-Y` comme avant et `+Y` comme arrière.

> **[LECTURE] Correspondance d’orientation — Ne pas saisir.**

```text
Blender : Z haut, -Y avant, +X droite visuelle de la scène
Godot  : Y haut, +Z avant du modèle
Échange : conversion assurée par glTF et l’importeur
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement :** l’artiste construit dans la convention Blender prévue ; l’exporteur glTF encode les transformations ; Godot reconstruit la scène en `Y-up`.
- **Invariant :** aucune rotation corrective arbitraire n’est ajoutée au root pour masquer une orientation incorrecte.
- **Résultat attendu :** le marqueur d’avant placé vers `-Y` dans Blender pointe vers `+Z` après import dans Godot.
- **Limite :** les terrains sans avant intrinsèque utilisent plutôt les directions cardinales documentées.

## 12. Placer les origines et pivots fonctionnels

L’origine sert au placement, à la rotation, au snapping, aux sockets et à l’animation. Elle est choisie selon la fonction de l’asset :

- objet posé : centre de la zone de contact au sol ;
- porte : axe de charnière ;
- roue : centre de rotation ;
- projectile : centre physique ou point de référence documenté ;
- bâtiment modulaire : coin ou point de grille défini par le kit ;
- personnage : origine de la racine selon le contrat du rig.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/PIVOT-POLICY.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
policies:
  static_prop:
    origin: "ground_contact_center"
    ground_plane_blender: "Z=0"
  hinged_object:
    origin: "hinge_axis"
  modular_piece:
    origin: "declared_grid_anchor"
  character:
    origin: "rig_contract"
required_markers:
  - "SOCKET_ORIGIN"
  - "SOCKET_FRONT"
  - "SOCKET_TOP"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs :** chaque famille associe une fonction à un emplacement d’origine ; les marqueurs rendent le contrôle visuel explicite.
- **Invariant :** un pivot n’est pas déplacé après publication sans nouvelle version et revue des scènes consommatrices.
- **Effet de bord :** les scripts de validation peuvent vérifier l’existence des marqueurs sans déduire leur intention depuis le nom du mesh.
- **Résultat attendu :** l’asset s’aligne et pivote correctement dès son instanciation dans Godot.

## 13. Appliquer les transformations avec discernement

Avant un export statique, une échelle objet différente de `(1, 1, 1)` mérite une revue. Appliquer rotation et échelle peut être approprié pour une géométrie statique, mais n’est jamais une commande universelle. Sur un rig, une animation, une hiérarchie contrainte ou une variante liée, l’application aveugle peut modifier les relations et les poses.

La checklist demande :

- vérifier les dimensions réelles ;
- vérifier l’échelle objet ;
- vérifier les modificateurs et contraintes ;
- vérifier les enfants et armatures ;
- appliquer seulement la transformation prévue ;
- réexaminer le résultat avant sauvegarde et export.

## 14. Organiser les collections et la frontière d’export

Chaque source possède une collection racine portant l’identifiant stable de l’asset. Les sous-collections utilisent les suffixes définis dans le manifeste. Une seule collection `__EXPORT` constitue la frontière technique.

> **[LECTURE] Hiérarchie d’un asset test — Ne pas saisir.**

```text
AST-PRP-TESTCUBE-001
├── AST-PRP-TESTCUBE-001__GEO
│   └── MSH_AST_PRP_TESTCUBE_001
├── AST-PRP-TESTCUBE-001__SOCKETS
│   ├── SOCKET_ORIGIN
│   ├── SOCKET_FRONT
│   └── SOCKET_TOP
├── AST-PRP-TESTCUBE-001__GUIDES
│   └── GUIDE_SCALE_1M
└── AST-PRP-TESTCUBE-001__EXPORT
    ├── MSH_AST_PRP_TESTCUBE_001
    ├── SOCKET_ORIGIN
    ├── SOCKET_FRONT
    └── SOCKET_TOP
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** les collections de travail classent les responsabilités ; `__EXPORT` rend la sélection de livraison déterministe.
- **Dépendances :** un même objet peut être visible dans plusieurs collections Blender, mais le script d’export doit dédupliquer les objets.
- **Invariant :** guides, caméras de travail et références ne passent pas dans l’export sauf décision explicite.
- **Résultat attendu :** l’export ne dépend ni de la sélection courante ni de l’état visuel accidentel de l’interface.

## 15. Utiliser Append, Link et Library Overrides

`Append` copie les données dans le fichier courant. La copie devient locale et ne reçoit plus automatiquement les corrections de la source. `Link` conserve une référence vers une bibliothèque externe ; les modifications de la bibliothèque sont visibles lors du rechargement. Les données liées sont normalement non modifiables localement.

Les `Library Overrides` permettent des modifications locales contrôlées sur des données liées tout en conservant la relation avec la bibliothèque. Ils ne remplacent pas une stratégie de publication : une bibliothèque partagée doit posséder un propriétaire, une version, un statut et une procédure de mise à jour.

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/LIBRARY-REGISTER.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
libraries:
  - id: "AST-LIB-MATERIALS-001"
    path: "../libraries/materials/AST-LIB-MATERIALS-001-v001-delivery.blend"
    version: "1.0.0"
    mode: "link"
    owner: "art-pipeline"
    immutable: true
    override_policy: "declared_properties_only"
    status: "planned"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemin :** le chemin relatif est interprété depuis le fichier consommateur ou selon la convention documentée du projet.
- **Mode :** `link` préserve la relation ; `append` serait choisi pour une copie volontairement indépendante.
- **Invariant :** une bibliothèque marquée `immutable` n’est pas réécrite ; une correction crée une nouvelle version.
- **Résultat attendu :** les dépendances partagées peuvent être localisées, auditées et remplacées sans recherche manuelle.

## 16. Préférer les chemins relatifs portables

Les images, bibliothèques et caches nécessaires à la source doivent rester sous une racine de projet connue ou être décrits dans un manifeste. Les chemins tels que `C:\Users\Nom\Desktop\texture.png` ne sont pas portables et peuvent révéler des informations locales.

> **[APP] Blender — Utiliser `File > External Data > Make All Paths Relative` après avoir rangé les dépendances sous la racine du projet.**

Le passage en chemins relatifs n’autorise pas à publier une texture externe. Les droits et la redistribution restent contrôlés séparément.

> **[PS] PowerShell 7 — Repérer des chemins absolus suspects dans les manifestes texte.**

```powershell
$patterns = @(
  '[A-Za-z]:\\Users\\',
  '/home/[^/]+/',
  '\\\\[^\\]+\\'
)
Get-ChildItem "art/blender/manifests" -File -Recurse |
  Select-String -Pattern $patterns |
  ForEach-Object {
    "{0}:{1}: {2}" -f $_.Path, $_.LineNumber, $_.Line.Trim()
  }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** les trois motifs recherchent des profils Windows, des dossiers personnels Unix et des chemins réseau UNC.
- **Sortie :** chaque correspondance affiche le fichier, la ligne et le texte concerné ; l’absence de sortie signifie seulement qu’aucun motif n’a été trouvé.
- **Limite :** ce contrôle ne lit pas les données binaires d’un fichier `.blend` et ne prouve pas que toutes les dépendances sont portables.
- **Résultat attendu :** les chemins manifestement propres à une machine sont corrigés avant livraison.

## 17. Sauvegardes, récupération et fichiers temporaires

Blender peut conserver des versions de sauvegarde et des fichiers de récupération. Ces mécanismes réduisent le risque de perte locale, mais ne remplacent ni Git, ni une sauvegarde externe, ni une version publiée.

Conserver :

- les sources approuvées dans le système de versionnement choisi ;
- les sauvegardes automatiques dans une zone locale ou protégée ;
- les archives de jalon sous forme immuable ;
- les caches comme données reconstruisibles ;
- les fichiers `.blend1`, `.blend2` et assimilés hors de la livraison.

> **[VSC] Visual Studio Code — Ajouter aux règles d’exclusion adaptées au dépôt — Ne pas saisir.**

```gitignore
art/blender/cache/
art/blender/work/local/
*.blend1
*.blend2
*.blend@
*.autosave
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** les motifs écartent des caches et sauvegardes locales susceptibles de créer du bruit ou de révéler un état non approuvé.
- **Limite :** ignorer un fichier ne le sauvegarde pas ; une politique externe doit protéger les sources de travail importantes.
- **Frontière :** Git LFS, quotas, rétention et stockage distant relèvent de la stratégie de dépôt et de publication du projet.
- **Résultat attendu :** la livraison ne contient pas de sauvegarde locale confondue avec une source officielle.

## 18. Stratégie de versions

Le suffixe `vNNN` représente une révision publiée du fichier, pas chaque sauvegarde clavier. Les étapes recommandées sont :

- travail courant sous une branche ou un dossier `work/` ;
- source candidate avec identifiant et version ;
- revue ;
- export et contrôle Godot ;
- promotion immuable dans `delivery/` ;
- correction par `v002`, jamais par remplacement silencieux de `v001`.

En Mode Studio, la version publiée est en lecture seule pour les consommateurs. En Mode Solo, la même règle s’applique aux jalons importants, avec moins d’états intermédiaires.

## 19. Choisir le format d’échange

Godot recommande glTF 2.0 et accepte `.gltf` ou `.glb`. Le pipeline retient :

- **GLB** par défaut pour une livraison compacte en un fichier ;
- **glTF séparé** lorsque la description JSON, les données binaires et les textures doivent être inspectées ou gérées séparément ;
- **import direct `.blend`** pour une itération Solo courte, car Godot appelle Blender et convertit d’abord vers glTF ;
- **FBX** seulement pour une dépendance externe justifiée ;
- **OBJ** pour une géométrie statique très simple, en acceptant ses limitations ;
- **DAE/COLLADA** non retenu comme chemin principal.

> **[LECTURE] Matrice de décision — Ne pas saisir.**

```text
GLB          : livraison par défaut, fichier unique
.gltf séparé : revue du JSON ou textures externes
.blend direct: itération locale, Blender requis sur le poste Godot
FBX          : exception d’interopérabilité documentée
OBJ          : géométrie simple sans rig, animation ni PBR complet
DAE          : non retenu pour le pipeline principal
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Critère :** le choix dépend de l’usage, de l’inspectabilité et des dépendances, pas d’une préférence personnelle.
- **Invariant :** le format d’échange ne devient jamais la source canonique lorsqu’une source Blender existe.
- **Risque :** l’import direct `.blend` impose Blender sur les postes qui importent le projet et n’est pas disponible partout.
- **Résultat attendu :** chaque exception au GLB possède une justification enregistrée.

## 20. Définir le preset GLB de référence

Le preset décrit l’intention du projet sans prétendre remplacer le fichier de réglages propre à la version de Blender. Les options sont revérifiées dans l’interface avant export et dans le script lorsque l’automatisation est utilisée.

> **[VSC] Visual Studio Code — Créer : `art/blender/presets/EXPORT-GLB-GODOT.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
id: "AST-EXPORT-GLB-GODOT-001"
blender_version: "5.2.0"
format: "GLB"
selection_source: "unique_collection_suffix___EXPORT"
include:
  meshes: true
  empties: true
  materials: true
  custom_properties: true
exclude:
  cameras: true
  punctual_lights: true
  guides: true
transform_policy:
  unit_scale: 1.0
  manual_axis_parent: false
post_export:
  - "sha256"
  - "godot_import"
  - "roundtrip_report"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** la collection unique `__EXPORT` constitue l’entrée, ce qui évite une exportation dépendante de la sélection courante.
- **Inclusions :** les empties servent de marqueurs ou sockets ; les propriétés personnalisées sont autorisées seulement si leur usage est documenté.
- **Invariant :** `manual_axis_parent: false` interdit un parent de correction ajouté uniquement pour l’échange.
- **Résultat attendu :** l’export peut être comparé au contrat même si l’interface Blender évolue.

## 21. Fabriquer l’asset test d’un mètre

> **[APP] Blender — Ouvrir le template puis créer `AST-PRP-TESTCUBE-001`.**

Procédure :

1. ajouter un cube ;
2. régler ses dimensions à `1 m × 1 m × 1 m` ;
3. placer sa base sur `Z = 0` ;
4. placer son origine au centre du contact au sol ;
5. orienter le marqueur `SOCKET_FRONT` vers `-Y` ;
6. placer `SOCKET_TOP` à `Z = 1` ;
7. déplacer le mesh et les marqueurs dans `__EXPORT` ;
8. sauvegarder sous `art/blender/sources/props/AST-PRP-TESTCUBE-001-v001-source.blend`.

Le cube ne cherche pas à être artistique. Il mesure la chaîne : unité, base, avant, pivot, hiérarchie, nommage et présence des marqueurs.

## 22. Exporter manuellement le GLB

> **[APP] Blender — Choisir `File > Export > glTF 2.0`, format `glTF Binary (.glb)`.**

Exporter uniquement la collection contractuelle vers :

`art/blender/exports/glb/AST-PRP-TESTCUBE-001-v001-export.glb`

Contrôler avant validation :

- aucun guide ou objet de référence non prévu ;
- un seul mesh test ;
- les trois marqueurs ;
- dimensions et origine correctes ;
- matériaux sans double face accidentelle ;
- absence de caméra et de lumière de travail ;
- fichier non vide.

> **[PS] PowerShell 7 — Calculer l’empreinte de l’export.**

```powershell
$export = "art/blender/exports/glb/AST-PRP-TESTCUBE-001-v001-export.glb"
if (-not (Test-Path $export)) {
  throw "Export GLB absent."
}
$hash = Get-FileHash -Algorithm SHA256 -Path $export
$hash | Format-List Algorithm, Hash, Path
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** le fichier exporté doit exister au chemin attendu.
- **Sortie :** `Get-FileHash` renvoie l’algorithme, l’empreinte hexadécimale et le chemin.
- **Invariant :** le manifeste de livraison référence l’empreinte du fichier effectivement contrôlé.
- **Résultat attendu :** une copie ultérieure peut être comparée sans se fier uniquement au nom de fichier.

## 23. Importer et contrôler dans Godot

> **[APP] Explorateur de fichiers — Copier le GLB vers `game/assets/imported/test/`.**

> **[APP] Godot — Ouvrir `Project Asteria`, attendre l’import puis examiner le dock Import et les réglages avancés.**

Godot transforme le glTF en scène importée et applique ses options d’import. Le test vérifie :

- racine à la position attendue ;
- base du cube sur le sol ;
- dimensions proches de `1 × 1 × 1` ;
- marqueur avant vers `+Z` ;
- marqueur supérieur à un mètre ;
- aucun nœud de guide, caméra ou lumière non prévu ;
- matériau et culling cohérents ;
- réimport stable après modification du fichier source.

Le fichier importé généré par Godot n’est pas modifié directement. Les changements pérennes passent par la source Blender, le preset d’export ou les réglages d’import suivis par le projet.

## 24. Automatiser un contrôle Godot borné

Le script suivant contrôle seulement le cube pilote. Il ne remplace pas l’inspection visuelle ni les validations spécialisées des futurs assets.

> **[VSC] Visual Studio Code — Créer : `game/tools/validate_roundtrip_asset.gd` — Ne pas saisir.**

```gdscript
extends SceneTree

const EXPECTED_SIZE := Vector3.ONE
const SIZE_TOLERANCE := 0.01
const REQUIRED_MARKERS := [
    "SOCKET_ORIGIN",
    "SOCKET_FRONT",
    "SOCKET_TOP",
]

func _initialize() -> void:
    var path := "res://assets/imported/test/AST-PRP-TESTCUBE-001-v001-export.glb"
    var packed := load(path) as PackedScene
    if packed == null:
        push_error("Impossible de charger l'asset test : %s" % path)
        quit(2)
        return

    var root := packed.instantiate()
    var mesh_instance := _find_first_mesh(root)
    if mesh_instance == null or mesh_instance.mesh == null:
        push_error("MeshInstance3D absent.")
        root.free()
        quit(3)
        return

    var size := mesh_instance.mesh.get_aabb().size
    if not size.is_equal_approx(EXPECTED_SIZE) and size.distance_to(EXPECTED_SIZE) > SIZE_TOLERANCE:
        push_error("Dimensions inattendues : %s" % size)
        root.free()
        quit(4)
        return

    for marker_name in REQUIRED_MARKERS:
        if root.find_child(marker_name, true, false) == null:
            push_error("Marqueur absent : %s" % marker_name)
            root.free()
            quit(5)
            return

    print("Asset test chargé, dimensions et marqueurs conformes.")
    root.free()
    quit(0)

func _find_first_mesh(node: Node) -> MeshInstance3D:
    if node is MeshInstance3D:
        return node as MeshInstance3D
    for child in node.get_children():
        var found := _find_first_mesh(child)
        if found != null:
            return found
    return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées et types :** `path` désigne la ressource importée ; `PackedScene` représente la scène chargeable ; `Vector3.ONE` encode `(1, 1, 1)`.
- **Codes de retour :** `2` signale le chargement, `3` le mesh, `4` les dimensions, `5` un marqueur ; `0` signifie que ces contrôles bornés réussissent.
- **Déroulement :** le script charge, instancie hors arbre, cherche le premier mesh, compare sa boîte locale, puis vérifie les marqueurs récursivement.
- **Effets de bord :** les diagnostics sont écrits sur la sortie ; l’instance est libérée avant la fin.
- **Limites :** la boîte locale ne prouve ni le placement global, ni l’orientation du marqueur avant, ni le rendu du matériau ; ces points restent inspectés dans la scène de test.

> **[PS] PowerShell 7 — Exécuter le contrôle Godot depuis `game/`.**

```powershell
& "C:\Tools\Godot\Godot_v4.7.1-stable_win64.exe" `
  --headless `
  --path . `
  --script res://tools/validate_roundtrip_asset.gd
if ($LASTEXITCODE -ne 0) {
  throw "Validation Godot refusée avec le code $LASTEXITCODE."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `--headless` évite l’interface, `--path .` sélectionne le projet courant et `--script` lance le contrôleur.
- **Valeur de retour :** `$LASTEXITCODE` reçoit le code produit par `quit()`.
- **Refus contrôlé :** tout code non nul arrête la chaîne avant publication.
- **Résultat attendu :** la sortie confirme le chargement, les dimensions et les marqueurs du cube pilote.

## 25. Définir le test aller-retour

Le test aller-retour ne promet pas une identité bit à bit. Il mesure la conservation des propriétés utiles après les transformations :

1. création ou export d’un bloc simple dans Godot lorsque nécessaire ;
2. export glTF depuis Godot ;
3. import dans Blender ;
4. modification contrôlée ;
5. export GLB ;
6. réimport dans Godot ;
7. comparaison de dimensions, origine, orientation, hiérarchie et matériau supporté.

Godot documente des limites d’export glTF, notamment pour les particules, les `ShaderMaterial` et les scènes 2D. Un aller-retour ne doit donc pas être présenté comme une conversion universelle sans perte.

> **[VSC] Visual Studio Code — Créer : `art/blender/tests/roundtrip/ROUNDTRIP-REPORT.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: "AST-PRP-TESTCUBE-001"
source_version: "v001"
blender_version: "5.2.0"
godot_version: "4.7.1-stable"
checks:
  dimensions_m: "pending"
  ground_contact: "pending"
  front_direction: "pending"
  marker_presence: "pending"
  hierarchy: "pending"
  material_culling: "pending"
artifacts:
  source_blend_sha256: null
  exported_glb_sha256: null
runtime_status: "not_executed"
decision: "pending"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statuts :** `pending` et `not_executed` empêchent de transformer le modèle de rapport en preuve d’exécution.
- **Empreintes :** les deux SHA-256 relient la source testée à l’export contrôlé.
- **Décision :** la promotion vers `accepted` intervient uniquement après les contrôles et la conservation des preuves.
- **Résultat attendu :** l’asset test peut être requalifié après une mise à jour de Blender, Godot ou du preset.

## 26. Décrire la livraison

> **[VSC] Visual Studio Code — Créer : `art/blender/manifests/AST-PRP-TESTCUBE-001-v001-delivery.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: "AST-PRP-TESTCUBE-001"
version: "v001"
status: "candidate"
source:
  path: "../sources/props/AST-PRP-TESTCUBE-001-v001-source.blend"
  sha256: null
export:
  path: "../exports/glb/AST-PRP-TESTCUBE-001-v001-export.glb"
  format: "GLB"
  preset: "AST-EXPORT-GLB-GODOT-001"
  sha256: null
dependencies: []
rights_status: "internal_test_asset"
validation:
  blender_static: "not_executed"
  godot_import: "not_executed"
  visual_review: "not_executed"
publication:
  immutable_after_acceptance: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Relations :** le manifeste relie une source, un export, un preset et leurs empreintes.
- **Statuts :** `candidate` et `not_executed` maintiennent la livraison hors publication tant que les portes restent ouvertes.
- **Dépendances :** une liste vide est explicite pour le cube test ; un asset réel devra déclarer bibliothèques, textures et autres sources.
- **Invariant :** après acceptation, le lot est immuable et toute correction crée une nouvelle version.

## 27. Valider statiquement une scène Blender

Le script suivant contrôle les conventions minimales d’une source ouverte. Il ne modifie pas le fichier.

> **[VSC] Visual Studio Code — Créer : `art/blender/scripts/validate_scene.py` — Ne pas saisir.**

```python
from __future__ import annotations

import sys
from pathlib import Path

import bpy

EXPECTED_SCALE = 1.0
EXPORT_SUFFIX = "__EXPORT"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []
    source_path = Path(bpy.data.filepath)
    if not source_path.name:
        errors.append("Le fichier Blender n'est pas enregistré.")

    scene = bpy.context.scene
    if scene.unit_settings.system != "METRIC":
        errors.append("Le système d'unités doit être METRIC.")
    if abs(scene.unit_settings.scale_length - EXPECTED_SCALE) > 1e-9:
        errors.append("Unit Scale doit être 1.0.")

    export_collections = [
        collection
        for collection in bpy.data.collections
        if collection.name.endswith(EXPORT_SUFFIX)
    ]
    if len(export_collections) != 1:
        errors.append("Une collection __EXPORT unique est requise.")

    for obj in bpy.data.objects:
        if obj.type == "MESH" and any(abs(value - 1.0) > 1e-6 for value in obj.scale):
            errors.append(f"Échelle non appliquée à examiner : {obj.name} = {tuple(obj.scale)}")

    for image in bpy.data.images:
        if image.source == "FILE" and image.filepath and not image.filepath.startswith("//"):
            errors.append(f"Image avec chemin non relatif : {image.name}")

    for library in bpy.data.libraries:
        if library.filepath and not library.filepath.startswith("//"):
            errors.append(f"Bibliothèque avec chemin non relatif : {library.filepath}")

    for error in errors:
        fail(error)
    if errors:
        return 1

    print("Validation statique Blender réussie.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** le script lit le fichier ouvert via `bpy.data` et la scène active via `bpy.context.scene`.
- **Fonctions :** `main()` accumule les non-conformités ; `fail()` les écrit sur stderr sans altérer la scène.
- **Tolérances :** les comparaisons numériques évitent une égalité flottante stricte ; elles ne remplacent pas la tolérance métier de chaque asset.
- **Refus contrôlé :** le code `1` indique au pipeline qu’au moins un contrôle a échoué.
- **Limites :** une échelle non appliquée est signalée pour examen, car certains rigs et hiérarchies peuvent exiger une décision spécialisée plutôt qu’une correction automatique.

> **[PS] PowerShell 7 — Lancer la validation sur la source du cube.**

```powershell
$source = "art/blender/sources/props/AST-PRP-TESTCUBE-001-v001-source.blend"
$validator = "art/blender/scripts/validate_scene.py"
& $env:ASTERIA_BLENDER_EXE --background $source --python $validator
if ($LASTEXITCODE -ne 0) {
  throw "La source Blender ne franchit pas la porte statique."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `--background` ouvre le fichier sans interface et `--python` exécute le validateur dans Blender.
- **Valeur de retour :** Blender propage la fin du script au processus ; PowerShell lit le résultat dans `$LASTEXITCODE`.
- **Effet de bord :** le fichier est ouvert en lecture par la procédure, mais le script ne sauvegarde aucune modification.
- **Résultat attendu :** la chaîne s’arrête avant export lorsqu’une convention minimale est violée.

## 28. Exporter de façon bornée par script

Le script d’export refuse une collection ambiguë et sélectionne récursivement son contenu. Il écrit un GLB au chemin reçu après `--`.

> **[VSC] Visual Studio Code — Créer : `art/blender/scripts/export_glb.py` — Ne pas saisir.**

```python
from __future__ import annotations

import sys
from pathlib import Path

import bpy

EXPORT_SUFFIX = "__EXPORT"


def recursive_objects(collection: bpy.types.Collection) -> set[bpy.types.Object]:
    objects = set(collection.objects)
    for child in collection.children:
        objects.update(recursive_objects(child))
    return objects


def main() -> int:
    argv = sys.argv
    if "--" not in argv or len(argv[argv.index("--") + 1 :]) != 1:
        print("Usage: export_glb.py -- <output.glb>", file=sys.stderr)
        return 2

    output = Path(argv[argv.index("--") + 1]).resolve()
    if output.suffix.lower() != ".glb":
        print("La sortie doit porter l'extension .glb.", file=sys.stderr)
        return 3

    candidates = [
        collection
        for collection in bpy.data.collections
        if collection.name.endswith(EXPORT_SUFFIX)
    ]
    if len(candidates) != 1:
        print("Une collection __EXPORT unique est requise.", file=sys.stderr)
        return 4

    bpy.ops.object.select_all(action="DESELECT")
    for obj in recursive_objects(candidates[0]):
        obj.select_set(True)

    output.parent.mkdir(parents=True, exist_ok=True)
    result = bpy.ops.export_scene.gltf(
        filepath=str(output),
        export_format="GLB",
        use_selection=True,
        export_cameras=False,
        export_lights=False,
        export_extras=True,
    )
    if "FINISHED" not in result:
        print(f"Export refusé : {result}", file=sys.stderr)
        return 5

    print(f"GLB écrit : {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** un unique chemin `.glb` suit le séparateur `--`, ce qui distingue les arguments Blender de ceux du script.
- **Fonction récursive :** `recursive_objects()` retourne un ensemble afin d’éviter les doublons lorsqu’un objet appartient à plusieurs collections.
- **Codes de retour :** `2` concerne les arguments, `3` l’extension, `4` la frontière d’export et `5` l’opérateur Blender.
- **Effets de bord :** la sélection Blender est remplacée, le dossier de sortie est créé et le GLB est écrit.
- **Limite :** les options d’animation, de rig et de compression ne sont pas activées ici ; elles seront qualifiées dans les chapitres spécialisés.

> **[PS] PowerShell 7 — Valider puis exporter le cube test.**

```powershell
$source = "art/blender/sources/props/AST-PRP-TESTCUBE-001-v001-source.blend"
$validator = "art/blender/scripts/validate_scene.py"
$exporter = "art/blender/scripts/export_glb.py"
$output = "art/blender/exports/glb/AST-PRP-TESTCUBE-001-v001-export.glb"

& $env:ASTERIA_BLENDER_EXE --background $source --python $validator
if ($LASTEXITCODE -ne 0) { throw "Validation Blender refusée." }

& $env:ASTERIA_BLENDER_EXE --background $source --python $exporter -- $output
if ($LASTEXITCODE -ne 0) { throw "Export GLB refusé." }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** le validateur s’exécute avant l’exporteur ; un refus empêche de générer un nouveau candidat.
- **Arguments :** les quatre variables rendent les chemins visibles et modifiables sans changer la logique de contrôle.
- **Postcondition :** un code nul indique qu’un fichier a été écrit, pas qu’il a réussi l’import Godot ou la revue visuelle.
- **Résultat attendu :** le GLB candidat est produit seulement depuis une source qui franchit les règles statiques du chapitre.

## 29. Checklist d’ouverture

À chaque ouverture d’une source :

- confirmer le chemin, l’identifiant et la version ;
- vérifier Blender et les extensions actives ;
- lire les avertissements de bibliothèques manquantes ;
- vérifier les chemins relatifs et textures absentes ;
- vérifier `Metric`, `Unit Scale = 1` et les dimensions étalon ;
- confirmer la collection racine et l’unique `__EXPORT` ;
- contrôler les overrides et dépendances liées ;
- ne pas sauvegarder immédiatement un fichier migré ou partiellement relocalisé ;
- créer une copie de travail avant une conversion irréversible.

## 30. Checklist avant export

Avant de générer un candidat :

- source enregistrée au chemin canonique ;
- version et identifiant conformes ;
- dimensions et origine contrôlées ;
- orientation `-Y` avant dans Blender pour un asset orienté ;
- transformations examinées ;
- dépendances résolues ;
- collection `__EXPORT` unique ;
- aucun guide, caméra ou lumière non prévu ;
- matériaux et backface culling revus ;
- script statique réussi ;
- sortie écrite dans `exports/`, jamais par-dessus la source.

## 31. Checklist de livraison

Une livraison candidate contient :

- source Blender et empreinte ;
- export GLB ou exception documentée ;
- preset d’export ;
- manifeste des dépendances ;
- statut des droits ;
- rapport Blender ;
- rapport d’import Godot ;
- capture ou scène de revue visuelle lorsque matérialisée ;
- décision et réserves ;
- numéro de version immuable après acceptation.

## 32. Parcours Mode Solo

Le parcours Solo conserve un seul template principal, une source par asset, une collection d’export, un GLB candidat et un rapport de contrôle. L’import direct `.blend` peut accélérer une expérimentation locale, à condition que :

- Blender soit disponible sur le poste ;
- la conversion implicite vers glTF soit comprise ;
- la livraison finale reste explicite ;
- le fichier `.blend` direct ne masque pas les dépendances ;
- le test GLB soit réalisé avant un jalon important.

Le nombre de variantes est limité. Une copie `work/` peut être supprimée après promotion, mais la source de jalon et son export validé sont conservés.

## 33. Parcours Mode Studio

Le parcours Studio ajoute :

- propriétaires par bibliothèque ;
- versions publiées en lecture seule ;
- catalogue central de dépendances ;
- séparation entre branche de travail et canal de livraison ;
- qualification des extensions sur un profil contrôlé ;
- contrôles automatisés des noms, chemins et collections ;
- revue indépendante du preset et de l’import ;
- procédure de migration lors d’un changement de Blender ;
- possibilité de revenir à une publication antérieure.

Les `Library Overrides` sont suivis comme des écarts locaux. Une équipe ne doit pas construire une chaîne d’overrides récursifs sans propriétaire ni test de resynchronisation.

## 34. Mesures à consigner lors de l’exécution

Pour chaque asset pilote réel, enregistrer :

- version de Blender et Godot ;
- durée d’ouverture, validation, export et import ;
- taille de la source et de l’export ;
- nombre d’objets, meshes, matériaux, textures et animations ;
- dépendances absentes ou relocalisées ;
- écart de dimensions ;
- orientation et pivot ;
- avertissements de l’importeur ;
- durée du réimport ;
- décision et corrections.

Ces mesures ne deviennent des budgets qu’après plusieurs cas représentatifs. Le cube test valide la chaîne, pas les performances d’un personnage, d’un bâtiment ou d’un environnement complet.

## 35. Provenance, licences et extensions

Blender et l’exporteur glTF possèdent leurs licences propres. Chaque add-on tiers, bibliothèque `.blend`, texture, police, HDRI ou référence externe reçoit une provenance et un statut d’usage. Le fait qu’un fichier s’ouvre dans Blender ne prouve ni un droit commercial ni une autorisation de redistribution.

Le chapitre 5 approfondira la fiche d’asset, les licences, la chaîne de transformations, les preuves et la procédure de retrait. Le présent chapitre exige seulement qu’une dépendance inconnue reste bloquée et ne soit pas intégrée silencieusement au template.

## 36. Sécurité du pipeline

Un fichier `.blend` et un add-on peuvent contenir ou déclencher du code Python. Les règles minimales sont :

- ne pas activer automatiquement les scripts d’un fichier non qualifié ;
- ouvrir les sources inconnues dans un environnement isolé ;
- vérifier la provenance et l’empreinte avant adoption ;
- ne pas installer une extension uniquement parce qu’un fichier l’exige ;
- limiter les droits du processus Blender ;
- exclure secrets, jetons et chemins personnels des propriétés et manifestes ;
- conserver une procédure de retrait de l’extension ;
- réexaminer les extensions après une mise à jour majeure.

## 37. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 37.1 Modifier `Unit Scale` pour réparer une géométrie minuscule

**Symptôme :** le cube paraît correct dans l’interface, mais les simulations, mesures ou imports restent incohérents.

**Exemple fautif**

> **[LECTURE] Réglage fautif — Ne pas saisir.**

```text
Unit System = Metric
Unit Scale = 0.01
Cube dimensions affichées = 1 m
Géométrie réelle laissée cent fois trop petite
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `Unit Scale` modifie l’affichage des unités et ne corrige pas automatiquement le comportement interne ni la géométrie source.

**Réglage corrigé**

> **[LECTURE] Réglage corrigé — Ne pas saisir.**

```text
Unit System = Metric
Unit Scale = 1.0
Cube dimensions réelles = 1 m × 1 m × 1 m
Contrôle après import dans Godot
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les dimensions de la source portent directement l’échelle prévue et peuvent être comparées au même étalon dans Godot.

### 37.2 Ajouter une rotation de 90 degrés au root

**Symptôme :** l’asset semble droit dans une scène, mais ses enfants, sockets ou animations utilisent une base différente.

**Exemple fautif**

> **[LECTURE] Hiérarchie fautive — Ne pas saisir.**

```text
ROOT_CORRECTION rotation X = 90°
└── Asset construit sans convention d'avant
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le parent masque une incompréhension des axes et propage une transformation corrective à toute la hiérarchie.

**Hiérarchie corrigée**

> **[LECTURE] Hiérarchie corrigée — Ne pas saisir.**

```text
Asset Blender : Z haut, -Y avant
Export glTF : conversion normale
Asset Godot : Y haut, +Z avant du modèle
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque outil utilise sa convention documentée et la conversion est laissée au format et aux importeurs prévus.

### 37.3 Appliquer toutes les transformations sans revue

**Symptôme :** le mesh statique semble corrigé, mais le rig, les contraintes ou les poses changent.

**Exemple fautif**

> **[LECTURE] Action fautive — Ne pas saisir.**

```text
Sélectionner toute la scène
Ctrl+A > All Transforms
Sauvegarder immédiatement
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la commande ne distingue pas géométrie statique, armature, hiérarchie contrainte ou instance liée.

**Action corrigée**

> **[LECTURE] Action corrigée — Ne pas saisir.**

```text
Examiner les objets concernés
Créer une copie de travail
Appliquer seulement rotation ou échelle justifiée
Recontrôler dimensions, contraintes et poses
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la transformation devient une décision bornée et réversible plutôt qu’une opération globale aveugle.

### 37.4 Mettre guides, sources et export dans une collection unique

**Symptôme :** le GLB contient une caméra, un plan de référence ou une géométrie de contrôle.

**Exemple fautif**

> **[LECTURE] Collection fautive — Ne pas saisir.**

```text
Collection
├── mesh final
├── image de référence
├── caméra de travail
└── guide d'échelle
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la sélection d’export dépend de la visibilité ou de la mémoire de l’opérateur.

**Collection corrigée**

> **[LECTURE] Collection corrigée — Ne pas saisir.**

```text
ASSET__GEO
ASSET__GUIDES
ASSET__SOCKETS
ASSET__EXPORT
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une frontière explicite fournit une entrée déterministe au validateur et à l’exporteur.

### 37.5 Conserver des chemins personnels absolus

**Symptôme :** le fichier fonctionne sur le poste de l’auteur et perd ses textures ou bibliothèques ailleurs.

**Exemple fautif**

> **[LECTURE] Chemin fautif — Ne pas saisir.**

```text
C:\Users\Laurent\Desktop\final_texture.png
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le chemin dépend d’un profil local, révèle une information personnelle et ne correspond pas à la racine du projet.

**Chemin corrigé**

> **[LECTURE] Chemin corrigé — Ne pas saisir.**

```text
//../../shared/textures/AST-MAT-STONE-001/albedo.png
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la dépendance se résout relativement à une arborescence partagée et reste identifiable dans le manifeste.

### 37.6 Écraser la source avec un export

**Symptôme :** une correction devient impossible ou le fichier livré est pris pour la source de création.

**Exemple fautif**

> **[LECTURE] Organisation fautive — Ne pas saisir.**

```text
asset/final.glb
asset/final.blend
Les deux fichiers sont modifiés et renommés selon les besoins.
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les noms ne portent ni identifiant, ni version, ni état, et aucune autorité n’est définie.

**Organisation corrigée**

> **[LECTURE] Organisation corrigée — Ne pas saisir.**

```text
sources/props/AST-PRP-BEACON-001-v003-source.blend
exports/glb/AST-PRP-BEACON-001-v003-export.glb
delivery/AST-PRP-BEACON-001-v003-delivery.yaml
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les chemins et suffixes distinguent source, résultat généré et décision de publication.

### 37.7 Exporter les objets visibles ou sélectionnés à la main

**Symptôme :** deux exports de la même source ne contiennent pas les mêmes objets.

**Exemple fautif**

> **[LECTURE] Procédure fautive — Ne pas saisir.**

```text
Masquer quelques objets
Sélectionner ce qui semble utile
Exporter la sélection
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la sortie dépend d’un état d’interface non enregistré comme contrat.

**Procédure corrigée**

> **[LECTURE] Procédure corrigée — Ne pas saisir.**

```text
Valider une collection __EXPORT unique
Sélectionner récursivement son contenu par script
Exporter avec le preset versionné
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la composition de l’export provient d’une structure persistante et contrôlable.

### 37.8 Utiliser `.blend` direct comme livraison Studio universelle

**Symptôme :** certains postes ne réimportent pas le projet ou utilisent une autre version de Blender.

**Exemple fautif**

> **[LECTURE] Contrat fautif — Ne pas saisir.**

```text
Livraison = fichier .blend uniquement
Blender installé et configuré supposé partout
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’import direct exige Blender, ajoute une conversion implicite et n’est pas disponible dans tous les environnements Godot.

**Contrat corrigé**

> **[LECTURE] Contrat corrigé — Ne pas saisir.**

```text
Source = .blend versionné
Livraison = GLB contrôlé
Import .blend direct = option locale d'itération Solo
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la source reste modifiable tandis que la livraison possède une dépendance plus faible et un résultat explicitement validé.

### 37.9 Installer automatiquement un add-on inconnu

**Symptôme :** l’ouverture d’un fichier conduit à exécuter du code non revu ou à rendre le projet dépendant d’une extension abandonnée.

**Exemple fautif**

> **[LECTURE] Décision fautive — Ne pas saisir.**

```text
Extension manquante détectée
Télécharger le premier dépôt trouvé
Activer l'extension sur le profil principal
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune source, version, licence, permission, compatibilité ou procédure de retrait n’est vérifiée.

**Décision corrigée**

> **[LECTURE] Décision corrigée — Ne pas saisir.**

```text
Bloquer la dépendance
Qualifier source, version, licence et maintenance
Tester dans un profil isolé
Adopter seulement après décision enregistrée
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’extension est traitée comme du code exécutable et une dépendance de production, pas comme une commodité invisible.

### 37.10 Remplacer une version publiée

**Symptôme :** deux machines possèdent un fichier nommé `v001` mais avec des contenus différents.

**Exemple fautif**

> **[LECTURE] Historique fautif — Ne pas saisir.**

```text
Corriger AST-PRP-BEACON-001-v001-delivery.glb
Écraser le fichier existant
Conserver le même manifeste et la même version
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le nom et l’historique ne permettent plus de relier une scène à l’export réellement utilisé.

**Historique corrigé**

> **[LECTURE] Historique corrigé — Ne pas saisir.**

```text
Conserver v001 avec son empreinte
Créer v002-source.blend
Produire v002-export.glb
Valider puis publier v002-delivery.yaml
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque contenu publié conserve une identité stable, une empreinte et une trajectoire de remplacement explicite.

## 38. Porte d’acceptation du pipeline

Le pipeline du chapitre est accepté lorsque :

- Blender et Godot sont qualifiés par version ;
- le template s’ouvre sans dépendance inconnue ;
- unités, axes et conventions de pivot sont documentés ;
- l’arborescence sépare sources, travail, cache, export, livraison et archive ;
- les noms et versions passent le contrôle ;
- une collection `__EXPORT` unique est utilisée ;
- l’asset test arrive à la bonne échelle, orientation et position ;
- les marqueurs attendus sont présents ;
- une seconde machine retrouve les bibliothèques et textures attendues ;
- l’export possède une empreinte et un manifeste ;
- les réserves runtime sont enregistrées ;
- aucune technique de modélisation spécialisée n’est revendiquée comme couverte.

## 39. Livrables à conserver

Les livrables permanents du chapitre sont :

- `ASTERIA-BLENDER-TEMPLATE.blend` lorsqu’il sera matérialisé ;
- conventions de collections et de nommage ;
- arborescence canonique ;
- manifeste de chaîne d’outils ;
- politique de pivots ;
- registre de bibliothèques ;
- preset d’export GLB ;
- scripts de validation et d’export proposés ;
- checklist d’ouverture, de contrôle et de livraison ;
- asset test et rapport aller-retour lorsqu’ils seront exécutés.

## 40. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient Blender `5.2.0` Stable comme référence documentaire et n’impose aucun add-on tiers. Les scènes utilisent le système métrique avec une unité pour un mètre. Les assets orientés regardent vers `-Y` dans Blender afin d’arriver vers `+Z` dans Godot via glTF, sans parent de rotation correctif.

Chaque asset possède une source Blender canonique, une collection d’export explicite, un identifiant stable et une version. Les bibliothèques partagées utilisent `Link` et, lorsque nécessaire, des `Library Overrides` encadrés ; `Append` crée une copie volontairement locale. Les chemins portables sont relatifs à la racine du projet.

Le GLB constitue la livraison par défaut. Le glTF séparé reste disponible pour l’inspection et les textures externes. L’import direct `.blend` est limité à l’itération locale, car il dépend de Blender et convertit lui-même vers glTF. Une livraison Studio demeure explicite, immuable et contrôlée.

Le cube d’un mètre constitue l’asset pilote de la chaîne. À ce stade, sa création, son export, son import Godot, les scripts proposés et l’ouverture sur une seconde machine restent des réserves runtime. Le chapitre prépare l’environnement ; les techniques spécialisées de modélisation, topologie, matériaux, rig, animation et optimisation restent dans les chapitres suivants.

## 41. Références officielles vérifiées

- [Blender — versions officielles](https://www.blender.org/download/releases/)
- [Blender Manual — unités de scène](https://docs.blender.org/manual/en/latest/scene_layout/scene/properties.html#units)
- [Blender Manual — Link et Append](https://docs.blender.org/manual/en/latest/files/linked_libraries/link_append.html)
- [Blender Manual — Library Overrides](https://docs.blender.org/manual/en/latest/files/linked_libraries/library_overrides.html)
- [Blender Manual — glTF 2.0](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html)
- [Godot 4.7 — formats 3D disponibles](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)
- [Godot — conventions d’export des modèles](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html)
- [Godot 4.7 — export de scènes 3D](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/exporting_3d_scenes.html)
- [Godot — configuration d’import](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html)
