---
title: "Livre IV — Chapitre 16 : Exports Godot et packaging"
id: "DOC-L4-CH16"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 16
last-verified: "2026-07-27T08:32:16+02:00"
audit-status: "complete"
audit-date: "2026-07-27T08:32:16+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-16.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
reference-hardware:
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  architecture: "RDNA 2"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
  os: "Windows 11 64 bits"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Exports Godot et packaging

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 14 a défini la chaîne CI/CD, les identités de builds, les artefacts, les manifestes et la règle de promotion sans reconstruction. Le chapitre 15 a défini la conservation et la restauration de ces éléments. Le présent chapitre possède la transformation d’un projet Godot validé en livrables de plateforme : presets, filtres de ressources, dépendances, icônes, signatures, packages, manifestes de contenu, sommes de contrôle et protocole d’installation sur une machine propre.

Exporter ne signifie pas publier. Un export produit un exécutable, un bundle, une archive ou un paquet conforme à un preset. Le packaging assemble les fichiers remis à un testeur ou à une plateforme. La publication commerciale, les pages boutique, les canaux, les clés de distribution, la soumission et le lancement restent au chapitre 17. Les patches distribués et leur rollback produit restent au chapitre 20.

Le chapitre documente une architecture de production au niveau `static-review`. Aucun preset de `Project Asteria`, template d’export, SDK, certificat, signature, notarisation, package, installation ou lancement sur machine propre n’est présenté comme matérialisé ou exécuté.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer projet, import, export, build, package, artefact, release et publication ;
- installer et qualifier les templates d’export correspondant exactement à la version de Godot ;
- versionner `export_presets.cfg` sans versionner les credentials ;
- définir des identités de preset stables et une matrice plateforme/architecture/profil ;
- séparer builds debug, test et release ;
- utiliser les filtres d’inclusion et d’exclusion sans livrer de fichiers privés ;
- gérer ressources non Godot, dépendances natives, GDExtension et bibliothèques ;
- préparer icônes, identifiants d’application, versions et métadonnées ;
- exporter en ligne de commande avec propagation stricte des erreurs ;
- préparer Windows, Linux, macOS, Android, iOS et Web sans prétendre qu’un seul poste peut tout signer ;
- produire un staging fermé, un manifeste et des sommes SHA-256 ;
- distinguer signature de code, notarisation, empreinte et preuve de provenance ;
- installer et lancer un candidat sur une machine propre ;
- organiser les responsabilités Solo et Studio ;
- diagnostiquer dix erreurs fréquentes de packaging.

## 3. Niveau de preuve et réserves

### 3.1. Déclarer le niveau de preuve

> **[LECTURE] Déclarer le niveau de preuve — Adapter les booléens après exécution.**

```yaml
evidence_level:
  chapter: static_review
  export_presets_materialized: false
  official_templates_installed: false
  windows_export_executed: false
  linux_export_executed: false
  macos_export_executed: false
  android_export_executed: false
  ios_export_executed: false
  web_export_executed: false
  signing_executed: false
  notarization_executed: false
  clean_machine_install_executed: false
  clean_machine_launch_executed: false
  runtime_claimed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`chapter` :** `static_review` signifie que contrats, commandes et contrôles sont relus sans produire de binaire.
- **Booléens :** chaque plateforme et chaque opération sensible possède une preuve indépendante.
- **Signature :** une empreinte calculée ne devient ni signature de code ni notarisation.
- **Machine propre :** une archive présente dans le staging ne démontre ni installation ni lancement.
- **Limite :** aucune capacité d’export ou de distribution de `Project Asteria` n’est déduite du document seul.

## 4. Prérequis et frontières

Le lecteur doit connaître le projet Godot du Livre I, les dépendances et données persistantes du Livre II, l’importation des assets du Livre III, les tests du chapitre 3, les serveurs dédiés du chapitre 13, la CI/CD du chapitre 14 et les restaurations du chapitre 15.

Le chapitre possède :

- les presets d’export client et leurs identités ;
- les profils debug, test et release ;
- les templates, SDK et outils externes nécessaires ;
- les filtres de ressources incluses ou exclues ;
- les fichiers non-ressources explicitement autorisés ;
- les icônes, identifiants d’application et métadonnées techniques ;
- les dépendances natives livrées avec le package ;
- les contrats de signature et de notarisation ;
- les scripts d’export et de packaging ;
- le staging, le manifeste fermé et les checksums ;
- l’installation et le lancement sur machine propre comme porte runtime future.

Le chapitre ne possède pas :

- les suites et oracles de tests, traités au chapitre 3 ;
- le runtime du serveur dédié, traité au chapitre 13 ;
- l’orchestration des workflows et la promotion d’artefacts, traitées au chapitre 14 ;
- la politique de sauvegarde et de restauration, traitée au chapitre 15 ;
- les boutiques, pages, canaux, clés et soumissions, traités au chapitre 17 ;
- les patches distribués et rollbacks produit, traités au chapitre 20 ;
- l’archivage patrimonial, traité au chapitre 22.

## 5. Vocabulaire opérationnel

- **Projet :** sources et configurations ouvertes par l’éditeur Godot.
- **Import :** transformation d’un asset source en données exploitables par le moteur.
- **Template d’export :** binaire moteur optimisé utilisé pour produire un jeu exporté.
- **Preset :** configuration nommée d’une cible, stockée principalement dans `export_presets.cfg`.
- **Credential d’export :** secret de signature, mot de passe ou clé conservé hors du fichier versionné.
- **Export debug :** export utilisant un template de débogage et des capacités supplémentaires de diagnostic.
- **Export release :** export utilisant un template de release ; il ne signifie pas automatiquement « publiable ».
- **Build test :** candidat instrumenté ou marqué pour une campagne interne, distinct du debug quotidien.
- **Package :** ensemble remis à un testeur, un installateur ou une plateforme.
- **Artefact :** sortie immuable identifiée par le chapitre 14.
- **Signature de code :** opération cryptographique associant un paquet à une identité de signature.
- **Notarisation :** contrôle de plateforme distinct de la signature locale.
- **Checksum :** empreinte d’intégrité calculée sur des octets.
- **Staging :** répertoire neuf dans lequel le candidat est assemblé avant validation.
- **Machine propre :** environnement sans checkout du dépôt, cache de l’éditeur ni dépendance implicite de développement.

## 6. Distinguer export, packaging et publication

> **[LECTURE] Comparer les responsabilités — Conserver une seule autorité par étape.**

```yaml
delivery_chain:
  source:
    owner: repository
  imported_project:
    owner: godot-editor
  exported_build:
    owner: export-preset
  package:
    owner: packaging-contract
  artifact:
    owner: ci-evidence
  release_candidate:
    owner: human-gate
  commercial_publication:
    owner: chapter-17
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chaîne :** chaque état reçoit une autorité et ne se confond pas avec l’état précédent.
- **Export :** le preset choisit plateforme, architecture, ressources et options moteur.
- **Package :** le contrat ajoute structure, documentation technique, manifeste et contrôles.
- **Artefact :** la CI conserve l’identité et les octets ; elle ne prononce pas seule la publication.
- **Frontière :** la publication commerciale reste explicitement hors du chapitre.

## 7. Construire une matrice de cibles

Une cible n’est pas seulement un système d’exploitation. Elle associe plateforme, architecture, renderer, profil, extension de sortie, outil obligatoire, capacité de signature, caractère requis et environnement de validation. Une ligne non qualifiée reste `candidate` ou `blocked`.

### 7.1. Matrice initiale de `Project Asteria`

> **[VSC] Définir les cibles candidates — Adapter aux plateformes réellement supportées.**

```yaml
targets:
  - id: AST-EXPORT-WIN-X64-RELEASE
    preset: Asteria Windows x86_64 Release
    platform: windows
    architecture: x86_64
    profile: release
    required: true
    output: Asteria.exe
    signing: candidate
    clean_machine_gate: required
  - id: AST-EXPORT-LINUX-X64-RELEASE
    preset: Asteria Linux x86_64 Release
    platform: linux
    architecture: x86_64
    profile: release
    required: true
    output: Asteria.x86_64
    signing: not-defined
    clean_machine_gate: required
  - id: AST-EXPORT-WEB-SINGLE-TEST
    preset: Asteria Web Single Test
    platform: web
    architecture: wasm32
    profile: test
    required: false
    output: index.html
    hosting_contract: secure-context
    clean_machine_gate: browser-matrix
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`id` :** identifiant stable de la ligne de matrice, indépendant du nom du fichier final.
- **`preset` :** nom exact passé à l’interface ou à la ligne de commande Godot.
- **`profile` :** `release` et `test` décrivent des contrats différents, même sur une plateforme identique.
- **`required` :** une cible optionnelle n’empêche pas une version qui ne la revendique pas.
- **`clean_machine_gate` :** décrit la famille de preuve attendue, sans déclarer le test déjà exécuté.

## 8. Qualifier Godot et les templates d’export

Les templates doivent correspondre à la version exacte de l’éditeur utilisée pour l’export. Le preset peut être valide alors que le template manque, est d’une autre version ou ne couvre pas l’architecture demandée. La qualification conserve version Godot, origine, nom du fichier, taille, empreinte et date de vérification.

### 8.1. Installer depuis l’éditeur

> **[APP] Godot — Ouvrir le gestionnaire de templates.**

```text
Godot Editor
  → Editor
  → Manage Export Templates
  → vérifier la version affichée
  → sélectionner uniquement les plateformes nécessaires
  → installer
  → revenir dans Project → Export
  → vérifier l’absence d’erreur de template pour chaque preset
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** la procédure s’effectue dans l’éditeur Godot.
- **Version :** le numéro affiché doit correspondre à l’éditeur qualifié, ici `4.7.1-stable` comme référence documentaire.
- **Sélection :** installer uniquement les cibles nécessaires réduit volume et surface de maintenance.
- **Résultat :** l’absence d’erreur dans la boîte d’export est une précondition, pas une preuve de lancement du jeu.

### 8.2. Enregistrer le manifeste de l’outil

> **[VSC] Créer `docs/build/toolchain-manifest.yaml` — Ne pas inscrire de secret.**

```yaml
toolchain:
  godot:
    version: 4.7.1-stable
    binary_sha256: PLACEHOLDER_TO_REPLACE
  export_templates:
    version: 4.7.1-stable
    source: official-download
    archive_sha256: PLACEHOLDER_TO_REPLACE
  android:
    jdk_major: 17
    sdk_revision: TO_QUALIFY
  apple:
    xcode_version: TO_QUALIFY_ON_MACOS
  signing:
    identities_present: false
    secret_values_recorded: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Placeholders :** ils rendent l’incomplétude visible et bloquent une prétendue qualification.
- **Versions :** l’outil, les templates et les SDK sont des dépendances distinctes.
- **Apple :** Xcode reste à qualifier sur macOS ; une machine Windows ne fournit pas cette preuve.
- **Secrets :** le manifeste décrit la présence d’identités sans contenir certificat privé, mot de passe ou jeton.
- **Empreintes :** elles portent sur les fichiers réellement utilisés lorsqu’ils seront matérialisés.

## 9. Versionner presets et credentials correctement

Godot sépare la plupart des réglages d’export dans `export_presets.cfg` et les valeurs confidentielles dans `.godot/export_credentials.cfg`. Le premier appartient normalement au dépôt ; le second reste hors versionnement. Un clone neuf doit reconstruire les credentials par un canal secret documenté.

### 9.1. Vérifier les règles Git

> **[PS] Contrôler les fichiers d’export suivis ou ignorés.**

```powershell
$ErrorActionPreference = "Stop"

git check-ignore -v .godot/export_credentials.cfg
if ($LASTEXITCODE -ne 0) {
    throw ".godot/export_credentials.cfg doit être ignoré"
}

git ls-files --error-unmatch export_presets.cfg
if ($LASTEXITCODE -ne 0) {
    throw "export_presets.cfg doit être versionné"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`git check-ignore -v` :** affiche la règle qui exclut le fichier confidentiel.
- **`git ls-files --error-unmatch` :** exige que le preset soit déjà suivi par Git.
- **Codes de retour :** chaque invariant non satisfait provoque un arrêt explicite.
- **Limite :** l’ignorance Git ne retire pas un secret déjà committé ; il faut alors révoquer, nettoyer l’historique selon décision et renouveler le credential.

### 9.2. Contrat minimal d’un preset

> **[LECTURE] Structure pédagogique de `export_presets.cfg` — Utiliser l’interface Godot pour générer les clés réelles.**

```ini
[preset.0]

name="Asteria Windows x86_64 Release"
platform="Windows Desktop"
runnable=false
advanced_options=true
dedicated_server=false
custom_features="asteria,release,client"
export_filter="all_resources"
include_filter="config/public/*.json"
exclude_filter="tests/**,tools/**,docs/private/**"
export_path="build/staging/windows-x86_64/Asteria.exe"

[preset.0.options]

binary_format/architecture="x86_64"
binary_format/embed_pck=false
codesign/enable=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Génération :** les clés exactes doivent provenir de l’éditeur Godot qualifié ; cet extrait explique le contrat.
- **`name` :** chaîne exacte utilisée par `--export-release`.
- **`custom_features` :** marque le rôle du build sans servir d’autorisation de sécurité.
- **Filtres :** ils décrivent une liste contrôlée, mais le package final doit encore être inspecté.
- **`export_path` :** cible le staging, jamais un dossier publié.
- **Signature :** `false` exprime un candidat non signé ; il ne doit pas être confondu avec un package de distribution approuvé.

## 10. Définir l’identité du produit

Nom affiché, identifiant technique, version marketing, version de build et identifiant d’artefact sont distincts. Les identifiants de plateforme restent stables après publication ; les versions augmentent selon les règles de chaque cible.

> **[VSC] Créer `docs/build/product-identity.yaml` — Adapter après décision produit.**

```yaml
product:
  display_name: Project Asteria
  internal_id: project-asteria
  semantic_version: 0.16.0
  build_id: PLACEHOLDER_FROM_CHAPTER_14
platform_ids:
  windows:
    executable_name: Asteria
  macos:
    bundle_identifier: com.example.asteria
  android:
    package_name: com.example.asteria
  ios:
    bundle_identifier: com.example.asteria
version_codes:
  android: TO_ASSIGN_MONOTONICALLY
  apple_build: TO_ASSIGN_MONOTONICALLY
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom affiché :** il peut être localisé sans changer l’identité interne.
- **Version sémantique :** elle décrit le produit ; le build ID relie commit, run et tentative.
- **Identifiants inversés :** les valeurs `com.example...` sont des placeholders et doivent être remplacées avant toute soumission.
- **Codes monotones :** Android et Apple imposent des identifiants de build propres à leur écosystème.
- **Frontière :** la réservation commerciale et la soumission de ces identifiants relèvent du chapitre 17.

## 11. Séparer debug, test et release

`--export-debug` et `--export-release` choisissent les templates correspondants. Un profil `test` n’est pas une option native unique : c’est un preset ou un ensemble de features, paramètres et ressources explicitement défini par le projet.

> **[LECTURE] Définir les profils — Aucun profil ne doit hériter silencieusement de secrets.**

```yaml
profiles:
  debug:
    godot_template: debug
    remote_debug: allowed-local-only
    test_hooks: allowed
    telemetry: local-verbose
    signing: optional-development
  test:
    godot_template: release
    custom_features: [test, internal]
    test_hooks: selected
    telemetry: local-structured
    signing: candidate
  release:
    godot_template: release
    custom_features: [release, public]
    test_hooks: forbidden
    telemetry: minimized
    signing: required-when-platform-policy-requires
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Debug :** garde les capacités de diagnostic utiles au développement, sans être remis au public.
- **Test :** peut utiliser le template release tout en conservant des hooks internes explicitement sélectionnés.
- **Release :** exclut outils, données de test et endpoints internes.
- **Signature :** dépend de la politique de plateforme et de la cible, pas seulement du mot `release`.
- **Sécurité :** une feature de build n’est jamais une permission métier ou un secret.

## 12. Utiliser les feature tags sans déplacer l’autorité métier

Les feature tags permettent d’adapter paramètres et ressources au build exporté. Les tags personnalisés ne sont utilisés que dans le projet exporté ou le déploiement en un clic ; le test dans l’éditeur doit fournir une voie explicite. Une branche `if OS.has_feature("release")` ne doit jamais autoriser une transaction, révéler un secret ou contourner un contrôle serveur.

> **[VSC] Lire un profil de build sans autorité métier.**

```gdscript
extends RefCounted
class_name BuildProfile

enum Kind {
    EDITOR,
    DEBUG,
    TEST,
    RELEASE,
}

static func detect() -> Kind:
    if Engine.is_editor_hint():
        return Kind.EDITOR
    if OS.has_feature("release"):
        return Kind.RELEASE
    if OS.has_feature("test"):
        return Kind.TEST
    return Kind.DEBUG
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `BuildProfile` centralise une lecture descriptive du contexte.
- **Enum :** les valeurs entières nommées évitent les chaînes dispersées dans le gameplay.
- **`detect() -> Kind` :** retourne toujours un profil et n’effectue aucun effet de bord.
- **Ordre :** l’éditeur est détecté avant les features exportées ; les tags personnalisés ne sont pas supposés actifs dans l’éditeur.
- **Limite :** le résultat peut choisir une interface ou un niveau de journalisation, jamais une autorisation métier.

## 13. Gouverner les ressources incluses et exclues

Le mode « toutes les ressources » est simple mais peut inclure des scènes expérimentales ou des données inutiles. Le mode sélectionné réduit la surface, mais une dépendance oubliée peut casser le jeu. Les filtres de fichiers non-ressources sont nécessaires pour JSON, CSV ou licences chargés à l’exécution. Les fichiers et dossiers commençant par un point ne sont pas exportés par le mécanisme normal, ce qui ne dispense pas d’inspecter le package.

### 13.1. Liste fermée des familles

> **[VSC] Créer `docs/build/resource-policy.yaml` — Adapter les motifs à l’arborescence.**

```yaml
resource_policy:
  export_mode: all_resources
  include_non_resources:
    - config/public/*.json
    - data/runtime/*.csv
    - licenses/runtime/**
  exclude:
    - tests/**
    - tools/**
    - docs/private/**
    - captures/**
    - build/**
  forbidden_anywhere:
    - "*.p12"
    - "*.keystore"
    - "*.env"
    - "*secret*"
    - "*credential*"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode :** `all_resources` reste un choix explicite, compensé par exclusions et inspection.
- **Non-ressources :** seules les familles réellement lues par le runtime sont ajoutées.
- **Répertoires :** tests, outils et sorties de build ne doivent pas entrer dans le package client.
- **Motifs interdits :** ils forment un filet de sécurité, pas une détection parfaite de secrets.
- **Revue :** chaque nouveau type de fichier runtime met à jour politique, tests et manifeste.

### 13.2. Scanner le staging

> **[VSC] Créer `tools/build/scan_package.py` — Refuser les familles privées.**

```python
from __future__ import annotations

from pathlib import Path

FORBIDDEN_SUFFIXES = {".p12", ".keystore", ".pem", ".env"}
FORBIDDEN_PARTS = {"tests", "tools", "private", ".git", ".godot"}

def scan_package(root: Path) -> list[str]:
    root = root.resolve(strict=True)
    findings: list[str] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root)
        lowered = {part.lower() for part in relative.parts}
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(relative.as_posix())
        elif lowered & FORBIDDEN_PARTS:
            findings.append(relative.as_posix())
    return findings

def require_clean_package(root: Path) -> None:
    findings = scan_package(root)
    if findings:
        raise ValueError("fichiers interdits : " + ", ".join(findings))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Constantes :** ensembles de suffixes et segments de chemin permettent des recherches déterministes.
- **`scan_package` :** reçoit une racine existante et retourne une liste triée de chemins relatifs.
- **Normalisation :** les segments sont comparés en minuscules sans modifier le fichier.
- **`require_clean_package` :** lève `ValueError` si au moins un candidat interdit existe.
- **Limite :** le scan par noms ne remplace pas l’analyse de contenu, le secret scanning ni la revue humaine.

## 14. Gérer les dépendances natives et GDExtension

Un projet GDScript pur utilise principalement les templates officiels. Une extension native ajoute bibliothèques par plateforme et architecture, compatibilité d’ABI, licences, symboles et règles de chargement. Le fichier `.gdextension` associe des bibliothèques à des feature tags ; une architecture absente doit bloquer la cible plutôt que produire un package incomplet.

> **[LECTURE] Inventorier les dépendances natives — Adapter aux binaires réellement adoptés.**

```yaml
native_dependencies:
  - id: AST-NATIVE-SQLITE-001
    type: gdextension
    source: qualified-release
    license: MIT
    godot_compatibility: 4.7
    libraries:
      windows.x86_64: bin/windows/sqlite.windows.template_release.x86_64.dll
      linux.x86_64: bin/linux/libsqlite.linux.template_release.x86_64.so
      macos.universal: TO_QUALIFY
    debug_symbols:
      retention: internal
    missing_target_policy: block-export
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la dépendance possède une fiche indépendante du fichier copié.
- **Compatibilité :** la série Godot et l’architecture sont explicites.
- **Bibliothèques :** chaque clé associe plateforme, profil et architecture à un chemin.
- **Symbols :** ils peuvent être conservés comme artefacts internes sans entrer dans le package public.
- **Politique :** une cible sans binaire qualifié échoue ; aucun fallback silencieux n’est autorisé.

### 14.1. Vérifier les bibliothèques attendues

> **[WSL] Vérifier les dépendances d’un staging Linux.**

```bash
set -euo pipefail
root="${1:?racine du staging manquante}"
binary="$root/Asteria.x86_64"

test -f "$binary"
test -x "$binary"
find "$root" -maxdepth 3 -type f -printf '%P
' | LC_ALL=C sort
ldd "$binary"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** le premier argument doit désigner le staging Linux.
- **`test -f` :** exige le binaire ; `test -x` exige le bit exécutable.
- **Inventaire :** `find` limite la profondeur et trie les chemins pour une preuve stable.
- **`ldd` :** décrit les dépendances dynamiques du binaire dans l’environnement courant.
- **Limite :** un `ldd` propre sur une distribution ne prouve pas la compatibilité avec toutes les distributions ciblées.

## 15. Préparer icônes, splash et métadonnées

Les sources d’icônes restent séparées des dérivés de plateforme. Une image carrée unique ne remplace pas les variantes de tailles, zones sûres, transparence et formats demandés. Le package conserve un manifeste reliant chaque dérivé à sa source approuvée et à son outil de génération.

> **[VSC] Définir les dérivés graphiques — Adapter les tailles aux exigences vérifiées.**

```yaml
branding_assets:
  source:
    icon_master: art/branding/asteria-icon-master.svg
    splash_master: art/branding/asteria-splash-master.blend
  windows:
    icon: build-inputs/icons/asteria.ico
  macos:
    icon: build-inputs/icons/asteria.icns
  android:
    adaptive_foreground: build-inputs/icons/android/foreground.png
    adaptive_background: build-inputs/icons/android/background.png
  ios:
    asset_catalog: build-inputs/icons/ios/AppIcon.appiconset
  web:
    favicon: build-inputs/icons/web/favicon.png
  provenance_manifest: docs/build/branding-provenance.yaml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sources :** les masters modifiables restent distincts des fichiers consommés par l’export.
- **Formats :** ICO, ICNS, images adaptatives et catalogues répondent à des cibles différentes.
- **Chemins :** les entrées de build sont versionnées ou produites par un pipeline qualifié, jamais récupérées depuis un dossier personnel.
- **Provenance :** le manifeste relie droits, version source, transformation et empreinte.
- **Validation :** chaque plateforme doit être inspectée sur son environnement réel avant approbation.

## 16. Exporter Windows

Le preset Windows choisit architecture, console éventuelle, intégration du PCK, icône et signature. Un exécutable avec PCK séparé facilite l’inspection et certains patchs ; l’intégration produit un fichier unique mais change les limites et le diagnostic. Le choix doit rester stable par canal.

### 16.1. Exporter depuis PowerShell

> **[PS] Exporter un candidat Windows release vers un staging neuf.**

```powershell
param(
    [Parameter(Mandatory)] [string]$Godot,
    [Parameter(Mandatory)] [string]$ProjectRoot,
    [Parameter(Mandatory)] [string]$StagingRoot
)

$ErrorActionPreference = "Stop"
$Target = Join-Path $StagingRoot "windows-x86_64"

if (Test-Path $Target) {
    throw "le staging doit être neuf : $Target"
}

New-Item -ItemType Directory -Path $Target | Out-Null
& $Godot --headless --path $ProjectRoot `
    --export-release "Asteria Windows x86_64 Release" `
    (Join-Path $Target "Asteria.exe")

if ($LASTEXITCODE -ne 0) {
    throw "export Windows échoué avec le code $LASTEXITCODE"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** binaire Godot, projet et staging sont obligatoires et injectés.
- **Staging :** un dossier existant est refusé pour éviter les fichiers résiduels.
- **`--headless` :** permet l’export automatisé sans interface graphique.
- **`--path` :** fixe explicitement le projet ; le chemin de sortie est calculé sous la racine de staging.
- **Code de retour :** tout code non nul bloque le packaging avant manifeste.

### 16.2. Inspecter un package Windows

> **[CMD] Lister les fichiers d’un candidat Windows.**

```bat
@echo off
setlocal
set "ROOT=%~1"

if "%ROOT%"=="" exit /b 64
if not exist "%ROOT%\Asteria.exe" exit /b 66

dir /s /b "%ROOT%"
certutil -hashfile "%ROOT%\Asteria.exe" SHA256
if errorlevel 1 exit /b %errorlevel%

exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`%~1` :** retire les guillemets de l’argument racine tout en conservant les espaces dans les usages suivants.
- **Codes `64` et `66` :** distinguent argument manquant et binaire absent.
- **`dir /s /b` :** produit une liste brute de fichiers à archiver avec la preuve.
- **`certutil` :** calcule une empreinte ; il ne vérifie pas une signature de code.
- **Retour :** le script propage l’échec du calcul au processus appelant.

### 16.3. Signature Windows

La signature automatique demande un outil et un certificat qualifiés. Le certificat privé et son mot de passe restent hors du preset versionné. Un package non signé peut servir à des tests internes si le statut est explicite ; il ne doit pas être promu comme équivalent au candidat signé.

> **[LECTURE] Contrat de signature Windows — Ne jamais inscrire le secret.**

```yaml
windows_signing:
  enabled_for_public_candidate: true
  tool:
    windows: signtool
    non_windows: osslsigncode
  identity_source: protected-secret
  timestamp_service: TO_QUALIFY
  verification:
    - signature-present
    - certificate-chain-reviewed
    - file-sha256-recorded
  unsigned_internal_candidate:
    allowed: true
    promotion_to_public: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outil :** la voie dépend du système d’export et doit être qualifiée.
- **Identité :** le certificat vient d’un stockage protégé, pas du dépôt ni du PCK.
- **Horodatage :** le service doit être choisi et vérifié avant usage réel.
- **Contrôles :** signature, chaîne et empreinte constituent des preuves distinctes.
- **Promotion :** un candidat interne non signé ne devient jamais public par simple renommage.

## 17. Exporter Linux

Le package Linux doit préserver le bit exécutable, déclarer l’architecture et vérifier les bibliothèques dynamiques attendues. Une archive ZIP produite et extraite avec des outils inadaptés peut perdre des permissions ; le format et le protocole d’extraction appartiennent au contrat.

> **[WSL] Exporter Linux depuis Bash.**

```bash
set -euo pipefail
godot_bin="${1:?binaire Godot manquant}"
project_root="${2:?projet manquant}"
staging_root="${3:?staging manquant}"
target="$staging_root/linux-x86_64"

if [ -e "$target" ]; then
  echo "le staging doit être neuf : $target" >&2
  exit 73
fi

mkdir -p "$target"
"$godot_bin" --headless --path "$project_root"   --export-release "Asteria Linux x86_64 Release"   "$target/Asteria.x86_64"

test -x "$target/Asteria.x86_64"
sha256sum "$target/Asteria.x86_64"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Arguments :** trois paramètres positionnels définissent outil, projet et racine de staging.
- **`set -euo pipefail` :** arrête erreurs, variables absentes et pipelines défaillants.
- **Code `73` :** signale un staging déjà présent sans l’effacer.
- **Extension :** `.x86_64` rend l’architecture visible ; elle reste une convention de nom.
- **Postcondition :** le bit exécutable et l’empreinte sont contrôlés avant archivage.

## 18. Exporter macOS

Le bundle macOS contient exécutable, bibliothèques et données du projet. L’export en `.zip` est préférable lorsqu’il est produit hors macOS afin de préserver les permissions du bundle. La signature et la notarisation demandent des identités Apple et des outils qualifiés. Une signature ad hoc facilite certains tests locaux mais ne remplace pas une distribution signée et notariée.

> **[LECTURE] Contrat macOS — Adapter sur un hôte macOS qualifié.**

```yaml
macos_export:
  preset: Asteria macOS Universal Release
  architecture: universal
  output_from_non_macos: Asteria-macos.zip
  bundle_identifier: com.example.asteria
  signing:
    mode: candidate
    tools:
      native: xcode-codesign
      cross_platform: rcodesign
  notarization:
    required_for_public_outside_store: candidate
    credential_source: protected-secret
  clean_machine:
    target: supported-macos-device
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Architecture :** `universal` exprime le contrat Intel et Apple Silicon du template officiel, à vérifier sur la version adoptée.
- **Archive :** la sortie ZIP protège mieux la structure lorsqu’elle est générée hors macOS.
- **Bundle ID :** le placeholder doit être remplacé par une identité stable.
- **Signature et notarisation :** deux opérations séparées avec outils et credentials distincts.
- **Machine propre :** la porte exige un appareil macOS supporté, pas seulement l’examen de l’archive sous Windows.

### 18.1. Vérifier le bundle sur macOS

> **[WSL] Contrôler signature et bundle dans un terminal macOS de qualification.**

```bash
set -euo pipefail
app="${1:?bundle .app manquant}"

test -d "$app/Contents"
test -x "$app/Contents/MacOS/Asteria"
codesign --verify --deep --strict --verbose=2 "$app"
spctl --assess --type execute --verbose=2 "$app"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préconditions :** le bundle et son exécutable doivent exister avec le bit exécutable.
- **`codesign --verify` :** vérifie la cohérence de la signature présente.
- **`spctl --assess` :** interroge la politique Gatekeeper de l’hôte.
- **Codes de retour :** un refus bloque la porte macOS et conserve les sorties de diagnostic.
- **Limite :** ce bloc est documentaire tant qu’aucun hôte, certificat ni bundle réel n’est utilisé.

## 19. Exporter Android

L’environnement Android sépare JDK, SDK, templates Godot, Gradle, identifiant de package et keystore. Le keystore de debug ne doit pas signer un candidat public. Les mots de passe peuvent être injectés par variables d’environnement ou secret de CI, jamais committés.

Pour un package AAB ou l’intégration de SDK tiers, le build Gradle est activé et son projet généré devient une dépendance à maintenir. Les répertoires de ressources dont le nom commence par un underscore possèdent une règle d’inclusion particulière dans le build Gradle ; la campagne doit vérifier les fichiers réels du package.

> **[VSC] Manifeste Android candidat — Adapter après qualification.**

```yaml
android_export:
  preset: Asteria Android Release
  jdk_major: 17
  sdk_path_source: machine-configuration
  package_name: com.example.asteria
  output_formats:
    internal: apk
    store_candidate: aab
  gradle_build:
    enabled_for_aab: true
    generated_project: android/build
  signing:
    debug_keystore_public_use: forbidden
    release_keystore_source: protected-secret-file
    release_alias_source: protected-secret
    release_password_source: protected-secret
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **JDK :** la version majeure est qualifiée comme dépendance de l’export.
- **SDK :** son chemin appartient à la machine ou au runner, pas au projet.
- **Formats :** APK interne et AAB candidat répondent à des usages distincts.
- **Gradle :** son activation ajoute fichiers générés, plugins et dépendances à inventorier.
- **Keystore :** le fichier privé, alias et mot de passe restent protégés et récupérables selon le chapitre 15.

### 19.1. Vérifier l’environnement Android

> **[PS] Contrôler les outils Android sans afficher de secret.**

```powershell
$ErrorActionPreference = "Stop"

java -version
if ($LASTEXITCODE -ne 0) { throw "Java indisponible" }

& "$env:ANDROID_HOME\platform-toolsdb.exe" version
if ($LASTEXITCODE -ne 0) { throw "ADB indisponible" }

if (-not $env:GODOT_ANDROID_KEYSTORE_RELEASE_PATH) {
    throw "chemin du keystore release absent"
}

Write-Output "android-toolchain=present"
Write-Output "release-keystore-path=redacted"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outils :** Java et ADB sont invoqués pour confirmer leur présence.
- **Variable :** le chemin du keystore doit exister dans l’environnement protégé.
- **Expurgation :** la valeur réelle n’est jamais écrite dans les logs.
- **Code de retour :** une dépendance absente bloque l’export Android.
- **Limite :** la présence des outils ne prouve ni compatibilité du SDK, ni signature, ni installation sur appareil.

## 20. Exporter iOS

L’export iOS prépare un projet Xcode. La compilation, la signature et le déploiement exigent macOS avec Xcode, une équipe et un identifiant de bundle valides. Une archive générée sous un autre système ne fournit pas cette preuve. Le chapitre documente le contrat ; il ne simule pas un environnement Apple absent.

> **[LECTURE] Contrat iOS — Bloquer tant que l’hôte Apple n’est pas qualifié.**

```yaml
ios_export:
  preset: Asteria iOS Release
  export_host: macos-required
  xcode: TO_QUALIFY
  app_store_team_id: PLACEHOLDER_TO_REPLACE
  bundle_identifier: com.example.asteria
  signing_identity: protected-apple-identity
  provisioning_profile: protected-platform-file
  device_install_gate: required
  archive_validation_gate: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hôte :** `macos-required` interdit une revendication d’export iOS depuis Windows ou Linux.
- **Xcode :** la version reste un placeholder jusqu’à qualification.
- **Identités :** Team ID et bundle ID sont séparés.
- **Provisioning :** le profil est un fichier sensible géré hors dépôt.
- **Portes :** archive et installation sur appareil fournissent des preuves complémentaires.

## 21. Exporter pour le Web

L’export Web produit plusieurs fichiers servis par HTTP. Le profil monothread offre une compatibilité plus large ; le profil multithread exige un contexte sécurisé et des en-têtes d’isolation adaptés. Le jeu ne doit pas être validé en ouvrant directement `index.html` depuis le système de fichiers.

La persistance `user://` dépend du stockage navigateur et de ses politiques. Les tests couvrent navigation privée, stockage refusé, cache, service worker et mise à jour. Le chapitre 17 possédera l’hébergement et la publication ; ici, le package et son contrat de serveur sont préparés.

> **[VSC] Définir les profils Web.**

```yaml
web_profiles:
  single:
    preset: Asteria Web Single Release
    threads: false
    secure_context: recommended
    cross_origin_isolation: not-required
  threaded:
    preset: Asteria Web Threads Test
    threads: true
    secure_context: required
    response_headers:
      Cross-Origin-Opener-Policy: same-origin
      Cross-Origin-Embedder-Policy: require-corp
    third_party_embedding: constrained
  validation:
    browsers: [chromium-current, firefox-current, safari-current]
    direct_file_open: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** monothread et multithread sont des cibles distinctes.
- **En-têtes :** le profil threads déclare les deux en-têtes d’isolation attendus.
- **Intégrations :** l’isolation peut contraindre contenus tiers et iframes.
- **Navigateurs :** les noms restent des familles candidates jusqu’à qualification des versions.
- **Interdiction :** l’ouverture `file://` ne remplace pas un serveur HTTP conforme.

### 21.1. Servir localement le package

> **[WSL] Servir un staging Web pour test local.**

```bash
set -euo pipefail
root="${1:?racine web manquante}"
port="${2:-8000}"

test -f "$root/index.html"
python3 -m http.server "$port" --directory "$root"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** le premier argument doit contenir `index.html`.
- **Port :** le second argument est optionnel et vaut `8000` par défaut.
- **Serveur :** `http.server` convient à une vérification locale simple, pas à une publication de production.
- **Processus :** la commande reste au premier plan afin que l’opérateur voie les requêtes et l’arrête explicitement.
- **Limite :** elle ne fournit ni HTTPS ni les en-têtes d’isolation du profil threads.

### 21.2. Vérifier les en-têtes

> **[SORTIE] Reconnaître une réponse Web multithread conforme.**

```text
HTTP/2 200
content-type: text/html
cross-origin-opener-policy: same-origin
cross-origin-embedder-policy: require-corp
cache-control: no-cache
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `200` confirme la réponse de la ressource demandée.
- **Type :** `text/html` correspond au document principal.
- **Isolation :** les deux en-têtes sont nécessaires au contrat multithread documenté.
- **Cache :** la valeur illustrative doit être remplacée par la politique de version réellement retenue.
- **Honnêteté :** cette sortie est un exemple de lecture, pas une capture de `Project Asteria`.

## 22. Séparer le serveur dédié du client

Le chapitre 13 possède le preset serveur, le mode headless, les features et l’exploitation. Le présent chapitre peut inclure le serveur dans la matrice de packages afin de vérifier sa structure, sans redéfinir son architecture réseau ou sa sécurité.

> **[LECTURE] Référencer le package serveur sans reprendre son runtime.**

```yaml
server_package_reference:
  owner_chapter: 13
  preset: Asteria Linux Dedicated Release
  expected_outputs:
    - AsteriaServer.x86_64
    - manifest.json
  packaging_checks:
    - no-client-visual-assets
    - no-signing-private-key
    - executable-bit-present
    - configuration-external
  runtime_security_review: chapter-13
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriété :** le chapitre 13 reste l’autorité du serveur dédié.
- **Sorties :** le chapitre 16 vérifie seulement la forme du package.
- **Secrets :** aucune clé privée ne doit être incluse.
- **Configuration :** elle reste externe au binaire et adaptée à l’environnement.
- **Frontière :** ports, admission, authentification et drainage ne sont pas redéfinis.

## 23. Créer un script canonique d’export

Le workflow du chapitre 14 appelle un script versionné. Le script choisit une ligne de matrice, crée un staging neuf, lance Godot, inspecte les sorties, génère le manifeste puis quitte avec un code non nul au premier échec. Le workflow ne duplique pas cette logique.

> **[VSC] Créer `tools/build/export_target.py` — Adapter les chemins des exécutables.**

```python
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ExportTarget:
    preset: str
    output_relative: Path
    debug: bool = False

def export_target(
    godot: Path,
    project_root: Path,
    staging_root: Path,
    target: ExportTarget,
) -> Path:
    godot = godot.resolve(strict=True)
    project_root = project_root.resolve(strict=True)
    staging_root = staging_root.resolve()
    output = (staging_root / target.output_relative).resolve()

    if staging_root not in output.parents:
        raise ValueError("sortie hors staging")
    if output.exists():
        raise FileExistsError(output)

    output.parent.mkdir(parents=True, exist_ok=False)
    mode = "--export-debug" if target.debug else "--export-release"
    command = [
        str(godot),
        "--headless",
        "--path",
        str(project_root),
        mode,
        target.preset,
        str(output),
    ]
    subprocess.run(command, check=True, shell=False)
    if not output.exists():
        raise FileNotFoundError(output)
    return output
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`ExportTarget` :** dataclass immuable portant nom de preset, sortie relative et choix debug.
- **Résolution :** outil et projet doivent exister ; le staging peut être créé par la fonction.
- **Confinement :** la sortie résolue doit rester sous la racine de staging.
- **Commande :** la liste d’arguments et `shell=False` évitent une concaténation interprétée par le shell.
- **`check=True` :** transforme tout code non nul en `CalledProcessError`.
- **Retour :** la fonction renvoie le chemin produit ou lève une exception si le fichier attendu manque.

## 24. Produire un manifeste fermé de package

Le manifeste décrit les octets remis au testeur : identité du build, cible, preset, version Godot, profil, commit, liste exacte des fichiers, tailles, empreintes, statut de signature et réserves. Il est généré depuis le staging après export, jamais à partir du workspace entier.

> **[VSC] Créer `tools/build/build_package_manifest.py` — Adapter le schéma de preuve.**

```python
from __future__ import annotations

import hashlib
import json
from pathlib import Path

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def build_manifest(root: Path, metadata: dict[str, str]) -> dict[str, object]:
    root = root.resolve(strict=True)
    files: list[dict[str, object]] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        files.append({
            "path": relative,
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    if not files:
        raise ValueError("package vide")
    return {
        "schema": "asteria-package-manifest",
        "version": 1,
        "metadata": dict(sorted(metadata.items())),
        "files": files,
    }

def write_manifest(root: Path, metadata: dict[str, str], output: Path) -> None:
    manifest = build_manifest(root, metadata)
    output.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`sha256_file` :** lit les fichiers par blocs et retourne une empreinte hexadécimale.
- **`metadata` :** dictionnaire de chaînes fourni par la chaîne de build ; son ordre est canonisé.
- **Fichiers :** seuls les fichiers sous le staging sont inventoriés avec chemins relatifs.
- **Refus :** un package vide lève `ValueError`.
- **Écriture :** JSON trié et terminé par un saut de ligne facilite revue et comparaison.
- **Limite :** SHA-256 détecte une divergence par rapport à une valeur connue, mais ne prouve ni auteur ni innocuité.

### 24.1. Exemple de manifeste

> **[SORTIE] Lire un manifeste de package candidat — Valeurs illustratives.**

```json
{
  "schema": "asteria-package-manifest",
  "version": 1,
  "metadata": {
    "build_id": "0.16.0+git.0123456789ab.run.123456789.1",
    "godot": "4.7.1-stable",
    "preset": "Asteria Windows x86_64 Release",
    "profile": "release",
    "signature": "not-executed",
    "target": "windows-x86_64"
  },
  "files": [
    {
      "path": "Asteria.exe",
      "size": 12345678,
      "sha256": "PLACEHOLDER_TO_REPLACE"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** nom et version permettent au validateur de refuser un format inconnu.
- **Build ID :** relie produit, commit, run et tentative sans les confondre.
- **Preset :** conserve le nom exact utilisé pour l’export.
- **Signature :** `not-executed` interdit de déduire une signature absente.
- **Fichier :** taille et empreinte sont des exemples de structure, pas des résultats observés.

## 25. Créer des checksums externes

Un fichier de checksums externe permet de vérifier une archive avant extraction. Il doit être produit après fermeture du package et conservé avec son manifeste. Le checksum ne doit pas être recalculé puis remplacé silencieusement après promotion.

> **[PS] Calculer les empreintes finales sous PowerShell.**

```powershell
param(
    [Parameter(Mandatory)] [string]$PackageDirectory,
    [Parameter(Mandatory)] [string]$OutputFile
)

$ErrorActionPreference = "Stop"
$Files = Get-ChildItem -LiteralPath $PackageDirectory -File -Recurse |
    Sort-Object FullName

if ($Files.Count -eq 0) {
    throw "aucun fichier à hacher"
}

$Lines = foreach ($File in $Files) {
    $Hash = Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName
    $Relative = [System.IO.Path]::GetRelativePath($PackageDirectory, $File.FullName)
    "{0}  {1}" -f $Hash.Hash.ToLowerInvariant(), $Relative.Replace([char]92, "/")
}

[System.IO.File]::WriteAllLines($OutputFile, $Lines)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** répertoire et fichier de sortie sont obligatoires.
- **Tri :** `Sort-Object FullName` rend l’ordre stable pour une même arborescence.
- **`GetRelativePath` :** retire les chemins spécifiques à la machine.
- **Format :** empreinte en minuscules, deux espaces puis chemin normalisé.
- **Écriture :** le fichier est produit en une opération après calcul de toutes les lignes.
- **Postcondition :** la chaîne doit ensuite vérifier que le checksum lui-même est associé au bon build ID.

## 26. Assembler une archive sans inclure le workspace

Le packaging part du staging fermé. Il ne compresse jamais la racine du dépôt, un dossier utilisateur ou un cache global. Le nom d’archive associe produit, version, cible et profil, sans timestamp comme seule identité.

> **[WSL] Créer une archive Linux reproductible au niveau procédural.**

```bash
set -euo pipefail
staging="${1:?staging manquant}"
archive="${2:?archive manquante}"

test -d "$staging"
test ! -e "$archive"

tar   --sort=name   --owner=0   --group=0   --numeric-owner   --mtime='UTC 2026-01-01'   -czf "$archive"   -C "$staging" .

sha256sum "$archive"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Staging :** la source doit être un dossier existant ; l’archive ne doit pas exister.
- **Tri :** les entrées sont ordonnées par nom.
- **Propriétaire :** UID et GID sont normalisés dans l’archive.
- **Date :** la valeur fixe est un exemple de normalisation et doit provenir d’une politique versionnée, pas de l’horloge courante.
- **Limite :** ces options améliorent la reproductibilité procédurale sans garantir l’identité binaire de tous les outils ou formats.

### 26.1. Inspecter un conteneur de build

> **[DCK] Docker Desktop — Vérifier l’image et les montages d’un runner local.**

```text
Docker Desktop
  → Containers
  → sélectionner le conteneur d’export Linux
  → Inspect
  → relever image et digest
  → vérifier que le dépôt est monté en lecture seule
  → vérifier qu’un volume de staging séparé reçoit les sorties
  → vérifier qu’aucun socket Docker ni secret global inutile n’est monté
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** l’inspection se fait dans Docker Desktop.
- **Digest :** l’image doit être identifiée par des octets, pas uniquement par un tag mobile.
- **Montages :** les sources sont préférablement en lecture seule et les sorties dans une zone distincte.
- **Privilèges :** socket Docker, mode privilégié et secrets globaux augmentent la surface de risque.
- **Frontière :** ce conteneur peut aider Windows/Linux ; il ne remplace pas les outils et hôtes Apple exigés.

### 26.2. Vérifier dans le conteneur

> **[DCT] Inspecter le staging depuis un conteneur non privilégié.**

```bash
set -euo pipefail
test -d /workspace/staging
find /workspace/staging -type f -printf '%P	%s
' | LC_ALL=C sort
test ! -e /workspace/staging/.git
test ! -e /workspace/staging/.godot
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** `/workspace/staging` doit être le seul arbre inspecté.
- **Inventaire :** chemin relatif et taille sont triés pour la preuve.
- **Interdictions :** `.git` et `.godot` ne doivent pas apparaître dans le package.
- **Privilèges :** aucune commande ne requiert root ni accès au moteur Docker.
- **Limite :** l’absence de deux dossiers ne suffit pas ; le scan complet de politique reste obligatoire.

## 27. Gérer signature, notarisation et clés

Les secrets de signature ne sont jamais écrits dans `export_presets.cfg`, le package, les logs ou un argument visible si une interface plus sûre existe. La chaîne sépare :

1. export non signé dans un staging ;
2. vérification du contenu ;
3. signature dans un job protégé ;
4. vérification de la signature ;
5. notarisation éventuelle ;
6. nouvelle empreinte des octets finaux ;
7. promotion de ces mêmes octets.

Une signature modifie généralement les octets. L’empreinte finale est donc calculée après toutes les transformations de signature et de packaging.

> **[LECTURE] Définir la porte de signature.**

```yaml
signing_gate:
  input_manifest_verified: required
  protected_environment: required
  signer_identity: approved
  private_key_in_repository: forbidden
  private_key_in_package: forbidden
  signing_result: required
  platform_verification: required
  final_manifest_regenerated: required
  final_sha256_recorded: required
  same_bytes_promoted: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le contenu est contrôlé avant accès au signer.
- **Environnement :** seuls les jobs autorisés reçoivent l’identité de signature.
- **Interdictions :** clé privée absente du dépôt et du package.
- **Transformation :** le manifeste final est recalculé parce que la signature change les octets.
- **Promotion :** les mêmes octets vérifiés sont transmis au chapitre 17.

## 28. Valider sur une machine propre

La validation du plan maître exige une installation et un lancement sur une machine propre. Cette porte reste runtime. Elle utilise un package téléchargé depuis l’artefact identifié, jamais le workspace du développeur. La machine ne possède ni éditeur Godot, ni dépôt, ni SDK de développement nécessaire au lancement normal.

### 28.1. Fiche de campagne

> **[VSC] Créer `docs/build/clean-machine-campaign.yaml` — Adapter à la cible.**

```yaml
campaign:
  id: AST-CLEAN-WIN-X64-001
  target: windows-x86_64
  package_build_id: PLACEHOLDER_TO_REPLACE
  package_sha256: PLACEHOLDER_TO_REPLACE
  machine:
    os_version: TO_RECORD
    architecture: x86_64
    godot_editor_installed: false
    source_repository_present: false
  steps:
    - verify-package-hash
    - extract-or-install
    - launch
    - create-new-profile
    - load-representative-scene
    - save-and-reload
    - quit-cleanly
    - relaunch
    - uninstall-or-remove
  evidence:
    - command-log
    - screenshots-redacted
    - application-log
    - result-summary
  runtime_executed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** la campagne et le build possèdent des identifiants séparés.
- **Machine :** environnement et absences importantes sont enregistrés.
- **Étapes :** installation, lancement, persistance et retrait sont contrôlés séparément.
- **Preuves :** les captures et journaux sont expurgés avant partage.
- **Honnêteté :** `runtime_executed=false` maintient la campagne au statut préparé.

### 28.2. Résultat attendu

> **[SORTIE] Exemple de résumé de campagne — Ne pas saisir.**

```text
campaign=AST-CLEAN-WIN-X64-001
build_id=PLACEHOLDER_TO_REPLACE
package_hash=verified
install=not-executed
launch=not-executed
save_reload=not-executed
uninstall=not-executed
runtime_claimed=false
decision=prepared-only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hash :** `verified` illustre le statut de contrôle attendu, sans fournir une empreinte réelle.
- **Étapes :** chaque résultat runtime reste `not-executed`.
- **Décision :** `prepared-only` interdit la promotion fondée sur ce document.
- **Traçabilité :** une vraie campagne remplacera les placeholders par build, machine, date, preuves et approbateur.

## 29. Contrôler installation, lancement et retrait

Une campagne réelle vérifie au minimum :

- fichier ou installateur téléchargé depuis l’artefact prévu ;
- somme SHA-256 avant extraction ;
- signature de plateforme si requise ;
- installation ou extraction dans un chemin sans outils de développement ;
- lancement avec un profil utilisateur neuf ;
- création, lecture et réécriture d’une sauvegarde représentative ;
- fermeture propre puis relance ;
- absence de dépendance à un chemin absolu du poste de build ;
- journaux sans secret et sans erreur critique ;
- retrait ou désinstallation ;
- conservation des preuves et écarts.

Les tests produit détaillés appartiennent au chapitre 3. La campagne de ce chapitre vérifie le contrat de livraison et l’autonomie du package.

## 30. Ne pas reconstruire pendant la promotion

Le chapitre 14 a établi que la promotion réutilise les mêmes octets. Le chapitre 16 ferme ces octets après signature, packaging et manifeste. Le chapitre 17 reçoit l’identifiant et l’emplacement de l’artefact final ; il ne relance pas Godot pour produire une version « identique ».

> **[LECTURE] Décrire un reçu de promotion.**

```yaml
promotion_receipt:
  build_id: 0.16.0+git.0123456789ab.run.123456789.1
  target: windows-x86_64
  package: Project-Asteria-0.16.0-windows-x86_64.zip
  package_sha256: PLACEHOLDER_TO_REPLACE
  manifest_sha256: PLACEHOLDER_TO_REPLACE
  signing_status: not-executed
  clean_machine_status: prepared
  rebuild_during_promotion: false
  publication_owner: chapter-17
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** package et manifeste possèdent leurs propres empreintes.
- **Statuts :** signature et machine propre restent explicites, même lorsqu’ils sont incomplets.
- **Reconstruction :** `false` protège l’identité des octets.
- **Propriétaire :** le chapitre 17 prend la décision de soumission ou de canal, sans modifier le package.

## 31. Gérer les échecs et reprises

Une tentative d’export reçoit une identité distincte. Un échec conserve logs, codes de retour et staging en quarantaine selon la rétention diagnostique. Un retry recommence dans un staging neuf. Une erreur de preset, de ressource interdite, de dépendance, de signature ou d’intégrité n’est pas classée comme transitoire.

> **[LECTURE] Classer les raisons d’échec.**

```yaml
export_failures:
  transient:
    - remote-artifact-download-timeout
    - temporary-runner-storage-unavailable
  permanent_until_change:
    - preset-missing
    - export-template-version-mismatch
    - forbidden-file-detected
    - native-library-missing
    - signing-identity-invalid
    - manifest-hash-mismatch
  retry_policy:
    transient_max_attempts: 2
    permanent_automatic_retry: false
    new_staging_per_attempt: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Familles :** les raisons stables facilitent triage et métriques sans exposer de texte libre.
- **Transitoire :** seules les pannes susceptibles de disparaître sans changement de contenu sont retentées.
- **Permanent :** une correction de configuration, dépendance ou secret est nécessaire.
- **Staging :** chaque tentative reçoit une racine neuve.
- **Visibilité :** l’échec initial reste conservé même si une tentative suivante réussit.

## 32. Mode Solo et Mode Studio

### Mode Solo

Le développeur Solo limite d’abord les cibles à celles qu’il peut réellement maintenir :

- Windows x86_64 et Linux x86_64 comme premiers candidats selon son public ;
- un preset stable par cible et profil ;
- templates officiels qualifiés ;
- scripts locaux identiques à ceux appelés par la CI ;
- credentials hors dépôt ;
- staging neuf et manifeste sur chaque candidat ;
- package non signé clairement marqué pour les tests internes ;
- une machine ou VM propre par cible réellement revendiquée ;
- calendrier de requalification après mise à jour de Godot ou du SDK ;
- aucune cible Apple déclarée supportée sans hôte Apple et preuve réelle.

La réduction du nombre de plateformes est préférable à plusieurs packages non testés.

### Mode Studio

Le Studio ajoute :

- propriétaires par plateforme ;
- matrice d’architectures et canaux ;
- runners ou machines dédiés ;
- séparation build, signature et publication ;
- accès protégé aux certificats et keystores ;
- rotation et récupération des identités de signature ;
- inventaire SBOM et licences des dépendances ;
- laboratoires de machines propres ;
- campagnes par système, version et architecture ;
- revue indépendante du manifeste ;
- rétention des symboles et preuves ;
- procédures d’incident pour certificat compromis ;
- approbation humaine avant promotion vers le chapitre 17.

## 33. Critère d’acceptation documentaire

Le chapitre passe au niveau `static-review` lorsque :

1. son périmètre correspond au plan maître ;
2. export, package, artefact et publication sont distingués ;
3. templates, presets et credentials sont séparés ;
4. debug, test et release possèdent des contrats explicites ;
5. ressources, fichiers non-ressources et exclusions sont gouvernés ;
6. dépendances natives et architectures sont inventoriées ;
7. les plateformes principales possèdent préconditions et réserves ;
8. staging, manifeste, checksums et signature sont ordonnés ;
9. la validation sur machine propre est préparée sans être inventée ;
10. les diagnostics suivent la séquence sémantique complète ;
11. les références techniques sont des liens nommés ;
12. les documents de gouvernance sont mis à jour ;
13. aucun résultat d’export, de signature, d’installation ou de lancement n’est revendiqué.

La validation finale du plan maître reste une réserve runtime jusqu’à l’installation et au lancement d’un package réel sur une machine propre.

## 34. Checklist opérationnelle

Avant de déclarer un package candidat :

- version Godot et templates identifiées ;
- preset exact versionné ;
- credentials absents du dépôt ;
- identité produit et version définies ;
- architecture et profil explicites ;
- filtre de ressources relu ;
- fichiers privés interdits ;
- bibliothèques natives présentes ;
- icônes et métadonnées contrôlées ;
- staging neuf ;
- code de sortie Godot vérifié ;
- contenu du package inventorié ;
- manifeste fermé produit ;
- empreintes calculées après transformation finale ;
- signature et notarisation vérifiées si requises ;
- package testé hors du workspace ;
- machine propre enregistrée ;
- lancement, sauvegarde et relance contrôlés ;
- échecs et réserves conservés ;
- mêmes octets remis à la publication.

## 35. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 35.1 Versionner les credentials d’export

**Symptôme ou risque :** Un certificat privé ou un mot de passe apparaît dans Git et dans tous les clones.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```ini
[preset.0.options]
codesign/identity="certificates/release.p12"
codesign/password="secret123"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `export_presets.cfg` devient un conteneur de secret et le mot de passe reste récupérable dans l’historique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```ini
[preset.0.options]
codesign/enable=true
# identité et mot de passe injectés par l’environnement protégé
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le preset versionne l’intention tandis que fichier privé et mot de passe proviennent d’un canal secret séparé.

### 35.2 Exporter dans un dossier déjà utilisé

**Symptôme ou risque :** Un fichier résiduel d’une ancienne cible entre dans le nouveau package.

**Exemple fautif :**

> **[PS] Exemple fautif — Ne pas appliquer.**

```powershell
godot --headless --export-release "Windows" .\build\Asteria.exe
Compress-Archive .\build\* .\Asteria.zip -Force
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le dossier partagé n’est ni nettoyé de façon confinée ni prouvé neuf, puis tout son contenu est archivé.

**Exemple corrigé :**

> **[PS] Exemple corrigé — Adapter au projet réel.**

```powershell
$Target = ".\build\staging\windows-x86_64"
if (Test-Path $Target) { throw "staging non neuf" }
New-Item -ItemType Directory $Target | Out-Null
godot --headless --export-release "Asteria Windows x86_64 Release" "$Target\Asteria.exe"
if ($LASTEXITCODE -ne 0) { throw "export échoué" }
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** une racine dédiée est créée, l’export vise un preset exact et le code de retour bloque la suite.

### 35.3 Inclure tests, outils et documents privés

**Symptôme ou risque :** Le package client contient scripts internes, fixtures ou données confidentielles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```ini
export_filter="all_resources"
include_filter="**/*"
exclude_filter=""
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le filtre ajoute aveuglément tous les fichiers non-ressources sans exclusion ni scan.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```ini
export_filter="all_resources"
include_filter="config/public/*.json,licenses/runtime/**"
exclude_filter="tests/**,tools/**,docs/private/**,build/**"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les fichiers non-ressources sont limités aux familles runtime et les surfaces internes sont explicitement exclues.

### 35.4 Traiter un export release comme publication approuvée

**Symptôme ou risque :** Un binaire non signé et non testé est envoyé à un canal public parce que son template vaut release.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
candidate:
  godot_mode: release
  status: publishable
  clean_machine_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `release` décrit le template Godot, pas les preuves de package, signature, installation et décision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
candidate:
  godot_mode: release
  package_manifest: required
  signing_status: explicit
  clean_machine_test: required
  publication_decision: chapter-17
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le template devient une propriété parmi plusieurs portes et la décision commerciale reste dans son chapitre propriétaire.

### 35.5 Utiliser une feature tag comme autorisation

**Symptôme ou risque :** Un joueur obtient une capacité métier parce que le package porte le tag `internal`.

**Exemple fautif :**

> **[VSC] Exemple fautif — Ne pas appliquer.**

```gdscript
if OS.has_feature("internal"):
    wallet.credit(100000)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** un marqueur de build contrôlé par le client modifie directement un état économique autoritaire.

**Exemple corrigé :**

> **[VSC] Exemple corrigé — Adapter au projet réel.**

```gdscript
if OS.has_feature("internal"):
    diagnostic_panel.visible = true
# Toute mutation métier passe encore par les commandes et autorités normales.
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le tag ne change qu’une présentation diagnostique et n’acquiert aucune autorité métier.

### 35.6 Recalculer le package pendant la promotion

**Symptôme ou risque :** Les octets publiés ne correspondent plus au manifeste et aux tests du candidat.

**Exemple fautif :**

> **[WSL] Exemple fautif — Ne pas appliquer.**

```bash
godot --headless --export-release "Asteria Linux x86_64 Release" release/Asteria.x86_64
upload release/Asteria.x86_64
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la phase de publication reconstruit le binaire au lieu de réutiliser l’artefact vérifié.

**Exemple corrigé :**

> **[WSL] Exemple corrigé — Adapter au projet réel.**

```bash
verify_manifest artifact/manifest.json artifact/package/
sha256sum --check artifact/SHA256SUMS
upload artifact/Project-Asteria-linux-x86_64.tar.gz
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la promotion vérifie puis transmet les mêmes octets identifiés par le manifeste et les checksums.

### 35.7 Calculer l’empreinte avant la signature

**Symptôme ou risque :** La somme publiée diverge du fichier signé finalement distribué.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
steps:
  - sha256
  - codesign
  - upload
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la signature modifie les octets après le calcul de l’empreinte.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
steps:
  - verify-unsigned-content
  - codesign
  - verify-platform-signature
  - build-final-manifest
  - sha256-final-package
  - upload-same-bytes
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le contrôle final porte sur les octets signés et interdit toute transformation après fermeture.

### 35.8 Valider le Web avec une ouverture locale

**Symptôme ou risque :** Le jeu semble fonctionner depuis un chemin local mais échoue une fois servi avec ses contraintes réelles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```text
file:///C:/build/web/index.html
result=looks-ok
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `file://` ne reproduit ni HTTP, ni contexte sécurisé, ni en-têtes, ni politique de cache.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```text
https://localhost.example.test/asteria/
secure_context=verified
response_headers=recorded
browser_profile=recorded
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le test s’effectue via un serveur conforme et conserve contexte, en-têtes et navigateur utilisés.

### 35.9 Signer Android avec le keystore debug

**Symptôme ou risque :** Le package public dépend d’une identité de développement non gouvernée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
android:
  package: release.aab
  keystore: debug.keystore
  promotion: public
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le nom `release.aab` ne change pas l’identité cryptographique utilisée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
android:
  package: release.aab
  keystore_source: protected-release-identity
  signature_verification: required
  promotion: human-gated
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** l’identité release protégée est vérifiée et la promotion attend une porte humaine.

### 35.10 Tester uniquement sur le poste de build

**Symptôme ou risque :** Le package dépend d’un SDK, d’une DLL ou d’un chemin présent uniquement chez le développeur.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
validation:
  machine: build-workstation
  source_repository_present: true
  godot_editor_installed: true
  result: approved
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** l’environnement masque les dépendances implicites et ne représente pas une installation utilisateur.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
validation:
  machine: clean-target
  source_repository_present: false
  godot_editor_installed: false
  package_hash_verified: true
  install_launch_save_reload: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la campagne part du package fermé sur un environnement sans sources ni éditeur et contrôle le parcours représentatif.

## 36. Références techniques officielles

- [Godot 4.7 — Export](https://docs.godotengine.org/en/4.7/tutorials/export/index.html)
- [Godot — Exporting projects](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html)
- [Godot — Command line tutorial](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html)
- [Godot — Feature tags](https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html)
- [Godot 4.7 — EditorExportPreset](https://docs.godotengine.org/en/4.7/classes/class_editorexportpreset.html)
- [Godot 4.7 — Exporting for Windows](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_windows.html)
- [Godot 4.7 — Exporting for Linux](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_linux.html)
- [Godot 4.7 — Exporting for macOS](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_macos.html)
- [Godot 4.7 — Exporting for Android](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_android.html)
- [Godot 4.7 — Gradle builds for Android](https://docs.godotengine.org/en/4.7/tutorials/export/android_gradle_build.html)
- [Godot — Exporting for iOS](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_ios.html)
- [Godot — Exporting for the Web](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html)
- [Godot 4.7 — Exporting for dedicated servers](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_dedicated_servers.html)
- [Godot — Exporting packs, patches, and mods](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)
- [Android Developers — Sign your app](https://developer.android.com/studio/publish/app-signing)
- [Apple Developer — Code signing](https://developer.apple.com/support/code-signing/)
- [Apple Developer — Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)

## 37. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` maintient une matrice versionnée de cibles. Chaque ligne possède identité, preset exact, plateforme, architecture, profil, sortie attendue, dépendances, statut de signature et porte de machine propre. Godot, templates, SDK, outils de signature et dépendances natives sont qualifiés séparément. `export_presets.cfg` est versionné tandis que credentials, certificats, keystores et profils privés restent hors dépôt.

Les profils debug, test et release sont des contrats distincts. Les feature tags décrivent le build sans acquérir d’autorité métier. Les ressources suivent une politique d’inclusion et d’exclusion ; tests, outils, documents privés, caches et secrets ne sont pas livrés. Les bibliothèques natives sont inventoriées par plateforme et architecture. Icônes et métadonnées restent reliées à leurs sources et preuves.

Chaque export travaille dans un staging neuf. Le script canonique propage les codes non nuls, inspecte les sorties, refuse les fichiers interdits, génère un manifeste fermé et calcule des checksums. Les opérations de signature et de notarisation restent séparées ; les empreintes finales sont calculées sur les octets réellement signés et empaquetés. La promotion réutilise ces mêmes octets sans reconstruction.

La validation de livraison s’effectuera depuis l’artefact identifié sur une machine propre, sans dépôt ni éditeur Godot. Elle vérifiera somme, installation ou extraction, lancement, création de profil, sauvegarde, relance et retrait. Tant que presets, templates, SDK, certificats, packages et machines de qualification ne sont pas matérialisés, le chapitre reste une architecture documentaire au niveau `static-review`. Aucun export, package, signature, notarisation, installation ou lancement de `Project Asteria` n’est revendiqué.
