---
title: "Livre IV — Chapitre 22 : Maintenance, archivage et pérennité"
id: "DOC-L4-CH22"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 22
last-verified: "2026-07-28T05:41:07+02:00"
audit-status: "complete"
audit-date: "2026-07-28T05:41:07+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-22.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Maintenance, archivage et pérennité

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 20 possède les correctifs, mises à jour, migrations distribuées et retours arrière d’une version encore supportée. Le chapitre 21 possède les surfaces d’extension et la gouvernance des contenus communautaires. Le présent chapitre traite ce qui permet au produit, à ses preuves et à son savoir-faire de **survivre au temps** : maintenance planifiée, surveillance des dépendances, archives vérifiables, reconstruction historique, succession et fin de support.

Une archive n’est pas une sauvegarde active, et une sauvegarde n’est pas une preuve de reconstruction. Le chapitre 15 protège la continuité opérationnelle des données courantes ; ici, on conserve aussi les sources, les outils, les chaînes de build, les artefacts, les documents, les licences, les décisions et les moyens de vérifier leur intégrité.

Le niveau de preuve reste `static-review`. Aucun dépôt miroir, support hors ligne, coffre de secrets, SBOM, archive, restauration, reconstruction historique, migration de format ou plan de fin de vie de `Project Asteria` n’est revendiqué comme matérialisé ou exécuté.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- définir un calendrier de maintenance et des responsabilités explicites ;
- inventorier dépendances, outils, services, formats, comptes et artefacts ;
- trier une vulnérabilité sans confondre alerte et décision de mise à niveau ;
- produire un manifeste d’archive corrélé à une version ;
- distinguer copie, sauvegarde, archive, miroir et dépôt de conservation ;
- utiliser checksums et signatures sans leur attribuer une durée de confiance infinie ;
- préparer une reconstruction historique reproductible ;
- qualifier les écarts lorsqu’un résultat bit-à-bit identique est impossible ;
- organiser succession, transfert d’autorité et récupération des comptes ;
- planifier fin de support, retrait, ouverture éventuelle et communication publique.

## 3. Vocabulaire opérationnel

La **maintenance** regroupe les activités planifiées qui conservent un produit supportable : inventaire, revue des dépendances, correction, qualification, documentation et exercices de reprise. L’**archivage** organise une conservation à long terme avec métadonnées, fixité, accès contrôlé et politique de rétention. La **pérennité** est la capacité à comprendre, reconstruire, exploiter ou migrer un système malgré le renouvellement des personnes, outils et plateformes.

Une **copie** duplique des octets. Une **sauvegarde** vise une restauration opérationnelle. Une **archive** ajoute contexte, durée, intégrité, règles d’accès et preuve de conservation. Un **miroir** réplique une source pour la disponibilité ; il peut reproduire une suppression ou une corruption. Une **reconstruction historique** tente de recréer une version passée à partir de sources, dépendances, outils et paramètres archivés.

La **fixité** signifie que les octets vérifiés sont identiques à ceux enregistrés lors du scellement. Elle ne prouve ni authenticité juridique, ni absence de logiciel malveillant, ni validité éternelle d’un algorithme cryptographique. La **reproductibilité** vise un résultat équivalent à partir d’entrées déclarées ; l’identité bit-à-bit est un niveau plus exigeant qui doit être annoncé séparément.

## 4. Modèle mental : conserver un système, pas seulement un ZIP

Un produit durable est un graphe de dépendances. Le code dépend d’un moteur, de plugins, de compilateurs, de SDK, de scripts, de certificats, de services et de connaissances humaines. Le build dépend aussi de variables d’environnement, d’horodatages, de l’ordre des fichiers, des outils de compression et parfois d’un service externe disparu.

L’unité d’archive de `Project Asteria` est donc un **dossier de version** qui relie :

- sources et historique Git ;
- dépendances directes et transitives ;
- outils et environnements ;
- données de conception ;
- artefacts de build ;
- documentation et décisions ;
- licences et provenance ;
- rapports QA ;
- manifestes, checksums et signatures ;
- procédures de reconstruction et de restauration.

## 5. Définir les niveaux de conservation

Trois niveaux évitent de promettre la même durée pour tout :

1. **Opérationnel** : nécessaire pour maintenir une version supportée.
2. **Historique** : nécessaire pour comprendre et reconstruire une version publiée.
3. **Patrimonial** : sélection destinée à rester lisible même lorsque l’environnement d’origine n’est plus exploitable.

Chaque objet reçoit un propriétaire, une durée, un niveau, un emplacement primaire, au moins une copie indépendante et un test de restauration. Les secrets actifs ne sont jamais placés dans un dossier patrimonial en clair.

> **[LECTURE] Matrice de conservation candidate — Ne pas saisir.**

```yaml
retention_classes:
  operational:
    review_interval_days: 30
    restore_test_interval_days: 90
  historical:
    review_interval_days: 180
    reconstruction_test_interval_days: 365
  heritage:
    review_interval_days: 365
    preferred_formats:
      - text/markdown
      - application/json
      - text/csv
      - image/png
      - audio/flac
evidence_level: static-review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Niveaux :** Les durées servent de paramètres candidats, pas de valeurs déjà qualifiées.
- **Formats :** Les formats lisibles complètent les originaux ; ils ne les remplacent pas silencieusement.
- **Tests :** La présence d’une copie ne vaut pas restauration ou reconstruction réussie.
- **Résultat attendu :** Chaque classe possède un objectif de conservation et une vérification distincte.

## 6. Établir les responsabilités

En Solo, une même personne peut remplir plusieurs rôles, mais les responsabilités restent nommées. En Studio, le propriétaire technique, le responsable sécurité, le responsable juridique, l’administrateur des comptes et le dépositaire des archives ne doivent pas devenir une seule autorité implicite.

La matrice minimale désigne :

- qui maintient l’inventaire ;
- qui accepte ou refuse une mise à niveau ;
- qui scelle une archive ;
- qui peut restaurer ;
- qui détient les moyens de récupération ;
- qui valide une communication de fin de support ;
- qui peut décider d’une ouverture du code ou des contenus.

> **[VSC] Créer le registre de responsabilités : `docs/maintenance/ownership.yaml`.**

```yaml
roles:
  product_owner:
    owns:
      - support_policy
      - end_of_support_decision
  technical_custodian:
    owns:
      - source_archives
      - build_reconstruction
  security_custodian:
    owns:
      - vulnerability_triage
      - signing_key_rotation
  records_custodian:
    owns:
      - retention_schedule
      - fixity_reports
  succession_contact:
    owns:
      - recovery_inventory
      - transfer_drills
approvals:
  archive_release:
    requires:
      - technical_custodian
      - records_custodian
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôles :** Les fonctions sont séparées des noms de personnes pour faciliter la succession.
- **Autorité :** Une archive historique exige au moins validation technique et conservation.
- **Évolution :** Les titulaires réels sont référencés dans un registre d’accès distinct.
- **Résultat attendu :** Une absence ou un départ ne rend pas l’autorité introuvable.

## 7. Construire l’inventaire de maintenance

L’inventaire est la carte des choses qui peuvent devenir obsolètes. Il couvre au minimum :

- moteur Godot et templates d’export ;
- addons, bibliothèques, packages Python et images de conteneur ;
- SDK de plateformes et outils de signature ;
- pilotes, systèmes d’exploitation et GPU de référence ;
- services hébergés, domaines, DNS, courriels et comptes de portails ;
- certificats, clés et dates d’expiration ;
- formats de données, bases, sauvegardes et catalogues ;
- builds publiés, symboles, journaux et notes de version ;
- documentations, ADR, licences et registres de provenance.

Un inventaire utile enregistre une identité stable, une version observée, une source officielle, un propriétaire, une criticité, une politique de mise à jour et une date de prochaine revue.

> **[VSC] Créer l’inventaire : `docs/maintenance/inventory.yaml`.**

```yaml
inventory:
  - id: tool.godot
    kind: engine
    version: 4.7.1-stable
    source: official
    criticality: critical
    owner_role: technical_custodian
    update_policy: qualified_change_only
    next_review: 2026-08-31
  - id: artifact.windows.x86_64
    kind: release_build
    version: 1.4.0
    retention_class: historical
    checksum_manifest: manifests/asteria-1.4.0.sha256
  - id: service.community_portal
    kind: hosted_service
    exit_plan: docs/maintenance/community-export.md
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** Les identifiants restent stables lorsque le nom commercial change.
- **Criticité :** La priorité de revue dépend de l’impact, pas seulement de la nouveauté.
- **Sortie :** Chaque service hébergé possède un plan d’export ou une réserve explicite.
- **Résultat attendu :** Une revue peut lister les éléments échus ou sans propriétaire.

## 8. Verrouiller les dépendances sans geler le risque

Un lockfile rend une résolution répétable ; il ne rend pas la version sûre pour toujours. La politique sépare :

- **détection** d’une nouvelle version ou vulnérabilité ;
- **analyse** de l’exposition réelle ;
- **décision** de conserver, mettre à niveau, remplacer ou isoler ;
- **qualification** du candidat ;
- **promotion** via le chapitre 20 ;
- **archivage** des preuves et composants utilisés.

Les dépendances transitives, scripts d’installation, images de conteneur et outils de build doivent apparaître dans l’inventaire ou le SBOM. Une dépendance téléchargée uniquement pendant le build reste une dépendance de reconstruction.

> **[PS] PowerShell 7 — Recenser les fichiers de dépendances candidats depuis la racine du dépôt.**

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$patterns = @(
    "pyproject.toml",
    "poetry.lock",
    "requirements*.txt",
    "package-lock.json",
    "Dockerfile*",
    "compose*.yaml",
    "*.gdextension"
)

$files = foreach ($pattern in $patterns) {
    Get-ChildItem -Path . -Filter $pattern -File -Recurse -ErrorAction SilentlyContinue
}

$files |
    Sort-Object FullName -Unique |
    Select-Object FullName, Length, LastWriteTimeUtc |
    ConvertTo-Json -Depth 3 |
    Set-Content -Path "build/maintenance/dependency-files.json" -Encoding utf8
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** Les motifs couvrent manifestes, locks, images et extensions natives.
- **Traitement :** Le tri et l’unicité rendent le rapport stable pour un même arbre.
- **Effet de bord :** Le rapport est écrit sous `build/maintenance/`, jamais dans les sources canoniques.
- **Limite :** La découverte de fichiers ne remplace pas l’analyse des dépendances transitives.

## 9. Surveiller les vulnérabilités

Une alerte de vulnérabilité est un signal à instruire. Elle ne prouve pas que le composant est chargé, accessible ou exploitable dans le contexte du jeu. Inversement, l’absence d’alerte ne prouve pas l’absence de risque.

Le triage enregistre :

- identifiant de l’avis ;
- composant et versions concernées ;
- présence dans le build, l’outil de production ou un service ;
- surface exposée ;
- exploitabilité connue ;
- mesure compensatoire ;
- version corrigée disponible ;
- décision, propriétaire et échéance ;
- preuves de qualification.

Les alertes GitHub Dependabot peuvent compléter la veille, mais elles dépendent des écosystèmes reconnus et des manifestes soumis au graphe de dépendances. Les avis du fournisseur, les bases de vulnérabilités et les bulletins des plateformes restent nécessaires.

> **[WEB] GitHub — Ouvrir `Security` puis examiner les alertes Dependabot du dépôt candidat.**

```text
1. Ouvrir le dépôt autorisé.
2. Choisir Security.
3. Ouvrir Dependabot alerts.
4. Filtrer par manifeste, sévérité et état.
5. Copier l’identifiant de l’avis dans le registre de triage.
6. Ne fermer l’alerte qu’avec une justification et une preuve corrélée.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Accès :** Les droits et fonctionnalités disponibles dépendent du dépôt et de son offre.
- **Corrélation :** L’identifiant GHSA ou CVE est repris dans le registre interne.
- **Décision :** La fermeture d’une alerte ne constitue pas à elle seule une acceptation produit.
- **Résultat attendu :** Chaque alerte ouverte ou rejetée possède une justification traçable.

> **[VSC] Créer un dossier de triage : `docs/security/vulnerability-triage.yaml`.**

```yaml
advisory: GHSA-xxxx-yyyy-zzzz
component: example-package
detected_version: 1.2.3
contexts:
  production_tooling: true
  shipped_runtime: false
exposure: not_confirmed
decision: investigate
owner_role: security_custodian
evidence:
  - build/maintenance/sbom-1.4.0.json
  - reports/security/GHSA-xxxx-yyyy-zzzz.md
next_review: 2026-08-05
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** Production et runtime sont évalués séparément.
- **Statut :** `not_confirmed` évite de transformer une hypothèse en conclusion.
- **Preuves :** Le dossier référence SBOM, analyse et rapports sans les recopier.
- **Résultat attendu :** La décision reste révisable lorsqu’une nouvelle preuve apparaît.

## 10. Produire et conserver un SBOM

Un **Software Bill of Materials** décrit les composants logiciels d’un produit et leurs relations. SPDX et CycloneDX fournissent des formats structurés ; le projet choisit un profil, une version et un validateur, puis les conserve avec chaque build qualifié.

Le SBOM n’est pas une liste de licences suffisante, ni une preuve de provenance complète. Il doit être corrélé au commit, au build, à la plateforme et à la méthode de génération. Les dépendances de production et celles distribuées au joueur sont distinguées.

> **[LECTURE] Extrait CycloneDX candidat — Structure de référence.**

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.7",
  "serialNumber": "urn:uuid:11111111-2222-4333-8444-555555555555",
  "version": 1,
  "metadata": {
    "component": {
      "type": "application",
      "name": "Project Asteria",
      "version": "1.4.0"
    }
  },
  "components": [
    {
      "type": "framework",
      "name": "Godot Engine",
      "version": "4.7.1-stable"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** La version de spécification est explicite et doit être validée par l’outil choisi.
- **Corrélation :** Le composant racine porte la version du produit archivé.
- **Étendue :** Cet extrait pédagogique ne représente pas les dépendances transitives réelles.
- **Résultat attendu :** Le SBOM complet peut être comparé entre deux versions et enrichi par le triage.

## 11. Gouverner le calendrier de maintenance

Le calendrier combine plusieurs cadences :

- veille de sécurité fréquente ;
- revue mensuelle des dépendances critiques ;
- revue trimestrielle des comptes, certificats et services ;
- test périodique de restauration ;
- exercice annuel de reconstruction historique ;
- revue de pérennité avant toute fin de support.

Une cadence ne doit pas être choisie uniquement parce qu’elle est ronde. Elle dépend du délai acceptable de détection, de la criticité, de la volatilité du fournisseur et de la capacité réelle de l’équipe.

> **[VSC] Créer le calendrier : `docs/maintenance/calendar.yaml`.**

```yaml
tasks:
  - id: security.advisory_review
    cadence: weekly
    owner_role: security_custodian
    evidence_path: reports/security/
  - id: archive.fixity_check
    cadence: quarterly
    owner_role: records_custodian
    evidence_path: reports/archive/fixity/
  - id: historical.reconstruction_drill
    cadence: yearly
    owner_role: technical_custodian
    evidence_path: reports/reconstruction/
gates:
  missed_twice:
    action: escalate_and_replan
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cadence :** Les chaînes sont des politiques à traduire dans l’outil de planification réel.
- **Preuve :** Chaque tâche définit l’emplacement de son rapport.
- **Escalade :** Deux échéances manquées déclenchent une décision, pas un silence.
- **Résultat attendu :** Le calendrier révèle les activités sans propriétaire ou sans preuve.

## 12. Décider d’une mise à niveau

La mise à niveau n’est pas automatique. Une matrice examine :

- urgence de sécurité ;
- compatibilité des formats et API ;
- disponibilité des outils de build ;
- coût de migration ;
- couverture de tests ;
- support du fournisseur ;
- possibilité de retour arrière ;
- effet sur les archives historiques.

Le chapitre 20 prend ensuite en charge le package, la migration, le déploiement et le rollback. Le chapitre 22 conserve l’ancien environnement, la décision et les preuves nécessaires pour comprendre la transition.

> **[LECTURE] Matrice de décision — Exemple de référence.**

```yaml
candidate_change:
  component: tool.godot
  from: 4.7.1-stable
  to: next-qualified-version
  drivers:
    security: review_required
    platform_support: review_required
  gates:
    source_import_compatibility: pending
    export_templates_available: pending
    save_compatibility: pending
    rollback_plan: pending
  decision: not_authorized
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs :** Les statuts évitent de transformer une version hypothétique en recommandation.
- **Portes :** Import, exports, sauvegardes et retour arrière sont évalués séparément.
- **Autorité :** `not_authorized` reste la valeur par défaut tant que les portes sont ouvertes.
- **Résultat attendu :** La promotion n’a lieu qu’après qualification et décision explicite.

## 13. Concevoir la topologie d’archives

Une politique de type « plusieurs copies, plusieurs supports, une copie hors site » est un point de départ, pas une preuve. Le projet définit :

- l’objet primaire ;
- les copies indépendantes ;
- la séparation des identifiants et droits ;
- l’emplacement hors ligne ou immuable ;
- la fréquence de synchronisation ;
- la détection des suppressions ;
- le chiffrement et la récupération des clés ;
- les tests de restauration.

Un miroir synchronisé en permanence n’est pas une copie indépendante contre une suppression logique. Une archive immuable sans clé de déchiffrement récupérable est également inutilisable.

> **[LECTURE] Topologie candidate — Ne pas appliquer sans qualification.**

```yaml
archive_topology:
  primary:
    medium: managed_repository
    mutable: true
  secondary:
    medium: encrypted_object_storage
    object_lock: candidate
    separate_credentials: true
  offline:
    medium: encrypted_removable_storage
    connected_only_during_rotation: true
  geographic_separation: required
  restore_test: required
  deletion_detection: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Indépendance :** Les identifiants et droits du secondaire ne dépendent pas du primaire.
- **Hors ligne :** Le support amovible n’est connecté que pendant une procédure contrôlée.
- **Sécurité :** Le chiffrement exige un plan distinct de récupération des clés.
- **Résultat attendu :** Une suppression, compromission ou panne unique ne détruit pas toutes les copies.

## 14. Archiver l’historique Git avec `git bundle`

Un bundle Git peut transporter des références et objets d’un dépôt dans un fichier vérifiable. Il complète un miroir distant, notamment pour un transfert hors réseau. Avant archivage, le projet vérifie le bundle et enregistre les références incluses.

Un bundle ne contient pas automatiquement les sous-modules, fichiers LFS externes, releases, issues, secrets de CI ou artefacts de plateforme. Chacun possède une procédure séparée.

> **[WSL] Terminal WSL — Créer et vérifier un bundle complet dans un répertoire de staging.**

```bash
set -euo pipefail

version="1.4.0"
staging="build/archive/${version}"
mkdir -p "${staging}"

git status --porcelain=v1
git bundle create "${staging}/asteria-${version}.bundle" --all
git bundle verify "${staging}/asteria-${version}.bundle"
git bundle list-heads "${staging}/asteria-${version}.bundle"   > "${staging}/asteria-${version}.refs.txt"

sha256sum   "${staging}/asteria-${version}.bundle"   "${staging}/asteria-${version}.refs.txt"   > "${staging}/asteria-${version}.sha256
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** Le statut est inspecté avant de sceller une version ; les modifications locales sont traitées explicitement.
- **Bundle :** `--all` inclut les références locales disponibles, pas les systèmes externes.
- **Vérification :** `git bundle verify` contrôle la cohérence Git avant copie.
- **Résultat attendu :** Le staging contient bundle, liste de références et manifeste SHA-256.

> **[CMD] Invite de commandes Windows — Vérifier un bundle déjà copié.**

```bat
@echo off
setlocal
set BUNDLE=E:\Asteria-Archive\1.4.0\asteria-1.4.0.bundle

git bundle verify "%BUNDLE%"
if errorlevel 1 exit /b 1

git bundle list-heads "%BUNDLE%"
if errorlevel 1 exit /b 1

echo bundle-verifie
exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** La syntaxe utilise `cmd.exe`, pas PowerShell.
- **Code de retour :** `errorlevel 1` arrête la procédure lorsqu’une commande Git échoue.
- **Lecture :** La liste des têtes doit être comparée au manifeste de la version.
- **Résultat attendu :** Le message final n’apparaît qu’après les deux contrôles réussis.

## 15. Conserver les fichiers Git LFS, sous-modules et releases

Les références Git peuvent pointer vers des objets absents du bundle principal. La procédure inventorie :

- fichiers suivis par Git LFS et objets effectivement récupérés ;
- URL et commit de chaque sous-module ;
- archives de releases et checksums ;
- symboles de débogage ;
- notes de version ;
- métadonnées de publication exportables ;
- licences et sources correspondantes.

L’archive enregistre la méthode de récupération. Un lien vers un service tiers n’est pas une conservation.

## 16. Capturer l’environnement de build

Un environnement reconstructible décrit au minimum :

- système et architecture ;
- version du moteur et templates d’export ;
- plugins et extensions ;
- versions Python et outils ;
- images et digests de conteneur ;
- variables non secrètes ;
- paramètres d’export ;
- ordre des étapes ;
- entrées téléchargées et leurs checksums.

Les installateurs propriétaires ou SDK dont la redistribution est interdite sont référencés par identité, version, empreinte et procédure d’acquisition légitime. L’archive ne contourne jamais une licence.

> **[VSC] Décrire l’environnement : `archive/build-environment.yaml`.**

```yaml
environment:
  os:
    family: windows
    version: 11
    architecture: x86_64
  engine:
    name: Godot Engine
    version: 4.7.1-stable
    export_templates_checksum: pending-materialization
  python:
    version: pending-capture
    lockfile: tools/poetry.lock
  containers:
    - image: project-asteria/archive-tools
      digest: pending-materialization
  secrets:
    included: false
  source_date_epoch:
    policy: derive_from_release_commit
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Versions :** Les valeurs inconnues restent explicitement en attente au lieu d’être inventées.
- **Digests :** Une image de conteneur est archivée par digest et, si permis, par export.
- **Secrets :** Le fichier confirme leur exclusion sans indiquer leur valeur.
- **Résultat attendu :** Une personne distincte sait quelles entrées acquérir avant reconstruction.

## 17. Conteneuriser les outils auxiliaires sans promettre l’éternité

Un conteneur facilite la répétition d’outils de vérification, mais dépend encore d’un runtime, d’une architecture, d’une image de base et d’un registre. L’archive conserve Dockerfile, digest, SBOM, licences et, lorsque permis, une exportation de l’image.

> **[VSC] Créer `archive-tools.compose.yaml` dans Visual Studio Code.**

```yaml
services:
  archive-tools:
    image: project-asteria/archive-tools@sha256:pending-digest
    network_mode: none
    read_only: true
    volumes:
      - ./archive-candidate:/input:ro
      - ./reports:/output
    command:
      - python
      - /app/verify_archive.py
      - --input=/input
      - --report=/output/report.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Image :** Le digest doit être remplacé par une valeur réellement produite et archivée.
- **Réseau :** La vérification de fixité n’a pas besoin de télécharger des dépendances.
- **Volumes :** L’archive candidate est en lecture seule et le rapport séparé.
- **Limite :** Le conteneur ne remplace pas l’archivage du runtime et de l’image.

> **[DCK] Docker Desktop — Vérification graphique candidate.**

Dans Docker Desktop, ouvrir **Images**, retrouver l’image par digest, vérifier son architecture et exporter les métadonnées autorisées. Ouvrir ensuite **Containers** uniquement pour inspecter une exécution de test déjà autorisée. Ne pas considérer l’état « vert » de l’interface comme une preuve de reconstruction ; le rapport conservé reste l’autorité documentaire.

> **[DCT] Terminal dans le conteneur — Vérifier le dossier monté sans réseau.**

```bash
python /app/verify_archive.py   --input=/input   --manifest=/input/archive-manifest.json   --report=/output/archive-verification.json

test -s /output/archive-verification.json
printf '%s
' 'archive-verification-report-created'
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** Le dossier `/input` est monté en lecture seule.
- **Manifest :** Le vérificateur compare les objets attendus aux octets présents.
- **Sortie :** Le rapport est écrit dans un volume distinct.
- **Réserve :** Le binaire et l’image ne sont pas matérialisés par ce chapitre.

## 18. Sceller les artefacts et leur manifeste

Chaque build historique reçoit un manifeste qui relie :

- version produit et identifiant de build ;
- commit et état des sous-modules ;
- plateforme et architecture ;
- artefacts et tailles ;
- checksums ;
- SBOM et provenance ;
- environnement de build ;
- rapport QA ;
- date de scellement ;
- autorité de validation.

Le manifeste est lui-même inclus dans une enveloppe de checksums. Une signature éventuelle est enregistrée avec son certificat, sa chaîne, sa politique et les informations nécessaires à une validation future.

> **[LECTURE] Manifeste d’archive de version — Structure de référence.**

```json
{
  "schema": "asteria-archive-manifest-v1",
  "product_version": "1.4.0",
  "build_id": "candidate-not-materialized",
  "source": {
    "commit": "pending-materialization",
    "bundle": "asteria-1.4.0.bundle"
  },
  "artifacts": [
    {
      "path": "builds/windows/ProjectAsteria.exe",
      "size": null,
      "sha256": "pending-materialization"
    }
  ],
  "sbom": "sbom/cyclonedx-1.7.json",
  "build_environment": "build-environment.yaml",
  "qa_report": "reports/release-qualification.md",
  "sealed_at": null,
  "proof_level": "static-review"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** Le format est versionné pour permettre une migration future.
- **Valeurs nulles :** Les octets non produits restent `null` ou en attente.
- **Corrélation :** Sources, artefacts, SBOM, environnement et QA partagent la même version.
- **Résultat attendu :** Le manifeste devient le point d’entrée d’une restauration ou reconstruction.

## 19. Calculer et vérifier les checksums

SHA-256 est adapté à la détection courante de modifications d’octets, mais la politique doit permettre une migration vers un autre algorithme. Le manifeste stocke le nom de l’algorithme, le chemin normalisé et la valeur. Les chemins sont relatifs à la racine de l’archive pour rester portables.

> **[PS] PowerShell 7 — Générer un manifeste SHA-256 portable.**

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = (Resolve-Path "build/archive/1.4.0").Path
$rows = Get-ChildItem -Path $root -File -Recurse |
    Where-Object { $_.Name -ne "checksums.sha256.json" } |
    Sort-Object FullName |
    ForEach-Object {
        [pscustomobject]@{
            algorithm = "sha256"
            path = $_.FullName.Substring($root.Length + 1).Replace("\", "/")
            size = $_.Length
            digest = (Get-FileHash -Path $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
        }
    }

$rows |
    ConvertTo-Json -Depth 4 |
    Set-Content -Path (Join-Path $root "checksums.sha256.json") -Encoding utf8
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** Les chemins sont calculés relativement au dossier scellé.
- **Ordre :** Le tri produit une sortie stable pour un même ensemble de fichiers.
- **Digest :** La casse est normalisée sans modifier la valeur cryptographique.
- **Limite :** Le manifeste doit ensuite être copié et protégé avec le reste du dossier.

## 20. Distinguer checksum et signature

Un checksum détecte un changement par comparaison avec une valeur de référence. Une signature associe une preuve cryptographique à une clé, mais sa valeur dépend de la protection de la clé, de l’algorithme, du certificat, de l’horodatage et de la politique de validation.

La conservation inclut :

- signature et checksum ;
- certificat ou clé publique ;
- chaîne et politique de confiance ;
- date de signature ;
- statut de révocation disponible au moment du scellement ;
- procédure de validation hors ligne ;
- plan de migration cryptographique.

Les clés privées actives sont conservées dans un système dédié et ne sont pas placées dans l’archive de diffusion.

## 21. Exécuter des contrôles de fixité périodiques

La fixité est vérifiée sur chaque copie, sans « réparer » automatiquement une divergence. Une divergence déclenche :

1. gel de l’objet concerné ;
2. comparaison avec les autres copies ;
3. qualification de la cause ;
4. choix d’une source saine ;
5. restauration contrôlée ;
6. nouveau scellement et rapport.

> **[VSC] Créer `tools/archive/verify_manifest.py`.**

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

def verify(root: Path, manifest_path: Path) -> list[dict[str, object]]:
    rows = json.loads(manifest_path.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []

    for row in rows:
        relative = Path(str(row["path"]))
        candidate = (root / relative).resolve()
        if root.resolve() not in candidate.parents:
            raise ValueError(f"path escapes archive root: {relative}")

        actual = sha256_file(candidate) if candidate.is_file() else None
        results.append(
            {
                "path": relative.as_posix(),
                "expected": row["digest"],
                "actual": actual,
                "ok": actual == row["digest"],
            }
        )
    return results
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** La fonction reçoit une racine et un manifeste JSON déjà sélectionnés.
- **Sécurité :** La résolution refuse un chemin qui sort de la racine d’archive.
- **Retour :** La liste conserve attendu, observé et décision par fichier.
- **Limite :** Le script ne choisit jamais automatiquement quelle copie est correcte.

> **[WSL] Terminal WSL — Lancer la vérification candidate et conserver le rapport.**

```bash
set -euo pipefail

python3 tools/archive/verify_archive.py   --root "build/archive/1.4.0"   --manifest "build/archive/1.4.0/checksums.sha256.json"   --report "reports/archive/fixity/1.4.0-$(date -u +%Y%m%dT%H%M%SZ).json"

test -s reports/archive/fixity/*.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Arguments :** Racine, manifeste et rapport sont passés explicitement.
- **Horodatage :** Le nom UTC facilite le tri sans définir à lui seul l’autorité temporelle.
- **Code de retour :** Le script doit échouer si un objet manque ou diverge.
- **Résultat attendu :** Un rapport immuable est ajouté au registre de fixité.

## 22. Tester la restauration

Une restauration est un exercice isolé. Elle n’écrase jamais l’environnement actif. Le scénario définit :

- archive et copie sélectionnées ;
- identité de l’opérateur ;
- environnement vierge ;
- étapes ;
- résultats attendus ;
- objets restaurés ;
- écarts ;
- durée observée ;
- décision de conformité.

Les durées RTO et pertes RPO ne sont annoncées qu’après mesures répétées dans un contexte représentatif.

## 23. Reconstruire une version historique

La reconstruction commence par le manifeste, pas par des souvenirs. Elle suit :

1. créer un environnement isolé ;
2. restaurer le bundle et ses dépendances externes ;
3. vérifier les checksums ;
4. récupérer les outils autorisés ;
5. appliquer les paramètres archivés ;
6. reconstruire sans accès réseau lorsque cela est possible ;
7. comparer les artefacts ;
8. qualifier les écarts ;
9. conserver le rapport et les journaux.

> **[WSL] Terminal WSL — Restaurer un dépôt depuis un bundle dans un dossier neuf.**

```bash
set -euo pipefail

bundle="/archive/1.4.0/asteria-1.4.0.bundle"
target="/tmp/asteria-reconstruction-1.4.0"

test ! -e "${target}"
git clone "${bundle}" "${target}"
cd "${target}"
git fsck --full
git show --no-patch --format='%H %cI' HEAD
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Isolation :** La cible doit être absente avant le clone.
- **Transport :** `git clone` accepte un bundle approprié comme source.
- **Intégrité Git :** `git fsck --full` contrôle les objets restaurés.
- **Résultat attendu :** Le commit observé est comparé au manifeste historique.

## 24. Mesurer la reproductibilité

Trois résultats sont distingués :

- **identique** : mêmes octets et mêmes digests ;
- **fonctionnellement équivalent** : différences expliquées sans impact sur le comportement accepté ;
- **non reproductible** : dépendance, outil, entrée ou procédure manque, ou l’écart reste inexpliqué.

Les sources d’écart fréquentes sont les horodatages, chemins absolus, ordre d’archive, identifiants aléatoires, métadonnées de signature, compression, locale, fuseau horaire et versions de bibliothèque.

> **[SORTIE] Rapport attendu d’une reconstruction — À lire sans le saisir.**

```json
{
  "schema": "asteria-reconstruction-report-v1",
  "version": "1.4.0",
  "source_commit_match": true,
  "environment_complete": false,
  "artifact_comparison": "not_executed",
  "missing_inputs": [
    "qualified-export-template-archive"
  ],
  "decision": "incomplete",
  "runtime_executed": false
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État :** `incomplete` reflète l’absence d’une entrée sans inventer un résultat.
- **Comparaison :** Le champ reste `not_executed` tant qu’aucun artefact n’est produit.
- **Réserve :** Le rapport pédagogique ne constitue pas une reconstruction réelle.
- **Résultat attendu :** Chaque échec est attribué à une entrée ou un écart concret.

## 25. Rendre les builds plus reproductibles

Les améliorations possibles comprennent :

- dépendances épinglées ;
- sources téléchargées par checksum ;
- ordre de fichiers stable ;
- locale et fuseau explicites ;
- chemins de travail contrôlés ;
- graine explicite lorsque l’outil en utilise une ;
- horodatage dérivé du commit lorsqu’autorisé ;
- réseau désactivé après acquisition des entrées ;
- journaux de versions ;
- séparation entre signature et contenu reproductible.

Ces règles sont appliquées uniquement lorsqu’elles ne contredisent pas les exigences des plateformes ou des signatures.

## 26. Préserver les formats de données

Le projet conserve l’original et, lorsqu’utile, une représentation ouverte et documentée. Les formats de conservation privilégiés sont structurés, versionnés et validables.

Exemples :

- Markdown et texte UTF-8 pour la documentation ;
- JSON ou CSV avec schéma pour les données tabulaires ;
- PNG ou TIFF pour des images de référence sans perte selon le besoin ;
- FLAC ou WAV pour les masters audio ;
- glTF pour un échange 3D documenté, tout en conservant les sources Blender ;
- SQLite avec schéma, migrations et export logique ;
- PDF/A seulement après qualification de la chaîne concernée.

Le choix final dépend des licences, de la fidélité, des métadonnées et de la capacité de validation.

## 27. Migrer un format sans effacer l’original

Une migration de préservation :

1. conserve l’original en lecture seule ;
2. décrit l’outil et sa version ;
3. produit dans un dossier distinct ;
4. vérifie structure et fidélité ;
5. relie source et dérivé ;
6. calcule de nouvelles empreintes ;
7. conserve le rapport.

> **[LECTURE] Registre de migration de format — Structure de référence.**

```yaml
migration:
  source:
    path: assets/source/relay_master.blend
    sha256: pending-materialization
  derivative:
    path: archive/open-formats/relay_master.glb
    sha256: pending-materialization
  tool:
    name: Blender
    version: pending-capture
  validation:
    geometry: not_executed
    materials: not_executed
    animation: not_applicable
  source_preserved: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Traçabilité :** Source et dérivé possèdent des identités et empreintes séparées.
- **Outil :** La version réelle est capturée au moment de l’opération.
- **Validation :** Chaque dimension reste non exécutée tant qu’elle n’est pas mesurée.
- **Résultat attendu :** Le dérivé améliore l’accès sans devenir l’unique original.

## 28. Archiver bases, sauvegardes et données vivantes

Le chapitre 15 possède la sauvegarde et la reprise opérationnelles. Pour la conservation historique, le chapitre 22 ajoute :

- schéma de base et migrations ;
- dictionnaire de données ;
- export logique minimal ;
- exemples anonymisés ou synthétiques ;
- procédure d’ouverture ;
- contraintes de version ;
- checksums ;
- politique de confidentialité et de suppression.

Les données personnelles, télémétries et contenus utilisateurs ne sont pas archivés « au cas où ». Leur conservation dépend d’une finalité, d’une base légale, d’une durée et de droits d’accès explicites.

## 29. Conserver la documentation et les décisions

Une version historique doit être compréhensible sans l’équipe d’origine. Le dossier conserve :

- README de reconstruction ;
- architecture et ADR ;
- conventions de données ;
- plans de test ;
- procédures de release et de support ;
- inventaires de licences ;
- limites connues ;
- journal des décisions de fin de support ;
- glossaire des termes propriétaires.

Les liens externes importants sont accompagnés d’une référence, d’une date de consultation et, si la licence l’autorise, d’une copie ou d’un export.

## 30. Préparer la succession

La succession protège le projet contre l’indisponibilité d’une personne ou d’une organisation. Le dossier distingue :

- autorité juridique ;
- propriété des comptes ;
- droits sur le code et les contenus ;
- administrateurs de dépôt ;
- contacts de plateformes ;
- récupération des domaines et courriels ;
- coffre de secrets ;
- clés de signature ;
- contrats et licences ;
- procédure d’urgence.

Le transfert de secrets n’est jamais documenté par leur valeur. Le dossier indique où ils sont conservés, qui peut lancer une récupération, quelles approbations sont nécessaires et comment révoquer l’ancien accès.

> **[LECTURE] Dossier de succession — Structure de référence.**

```yaml
succession:
  trigger_events:
    - planned_departure
    - prolonged_unavailability
    - organization_transfer
  authorities:
    repository_admins: external-access-register
    domain_recovery: external-access-register
    signing_keys: dedicated-key-custody
  required_drills:
    - recover_read_access
    - restore_repository_from_archive
    - rotate_one_nonproduction_secret
  secrets_in_document: false
  last_drill: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déclencheurs :** Le plan couvre départ planifié et indisponibilité imprévue.
- **Références :** Les registres sensibles restent externes à la documentation lecteur.
- **Exercice :** Les capacités sont testées sur des accès non production avant urgence.
- **Résultat attendu :** Le projet peut transférer l’autorité sans divulguer de secret.

## 31. Inventorier les comptes et voies de récupération

Le registre des comptes contient fournisseur, finalité, propriétaire organisationnel, administrateurs, MFA, contacts de récupération, méthode d’export, procédure de transfert et date de revue. Les comptes personnels utilisés provisoirement sont signalés comme dette de gouvernance.

> **[APP] Gestionnaire de mots de passe d’équipe — Revue graphique candidate.**

```text
1. Ouvrir le coffre autorisé.
2. Filtrer les éléments du projet Asteria.
3. Vérifier propriétaire, administrateurs et contacts de récupération.
4. Confirmer que le MFA possède une voie de récupération indépendante.
5. Consigner uniquement le résultat de la revue dans le registre.
6. Ne jamais copier les secrets dans le rapport documentaire.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** Le gestionnaire réel doit être nommé et qualifié par l’organisation.
- **Séparation :** Le rapport contient statuts et responsables, jamais les valeurs secrètes.
- **Récupération :** Une voie de récupération est testée selon une procédure contrôlée.
- **Résultat attendu :** Aucun compte critique ne dépend d’une seule personne ou adresse.

## 32. Gérer certificats, domaines et clés de signature

Les échéances sont suivies avant expiration. Le registre enregistre :

- identifiant de la clé ou du certificat ;
- usage ;
- propriétaire ;
- système de conservation ;
- date d’expiration ;
- politique de rotation ;
- révocation ;
- effet sur les builds historiques ;
- procédure d’urgence.

Une clé historique révoquée n’annule pas automatiquement la valeur documentaire des checksums et rapports conservés ; la politique décrit ce qui reste vérifiable et par quel mécanisme.

## 33. Prévoir la disparition d’un fournisseur

Pour chaque service critique, le projet prépare :

- export des données ;
- format et fréquence de l’export ;
- alternative ou mode dégradé ;
- délai de récupération ;
- dépendances contractuelles ;
- procédure de retrait des secrets ;
- mise à jour de la documentation et du client.

Les portails de distribution peuvent empêcher de republier exactement un ancien build. L’archive conserve les octets et preuves autorisés, mais ne promet pas un droit de remise en ligne absent.

## 34. Définir les phases de fin de support

Une fin de support contrôlée distingue :

1. **annonce** avec date et périmètre ;
2. **maintenance réduite** avec types de correctifs acceptés ;
3. **fin des mises à jour** ;
4. **retrait éventuel** de certains services ;
5. **conservation** des téléchargements et documentations permis ;
6. **archivage final** ;
7. **succession ou ouverture éventuelle**.

Les sauvegardes, services en ligne, comptes joueurs, contenus communautaires et outils de modding possèdent des conséquences différentes. Le chapitre ne suppose pas qu’un jeu hors ligne devient automatiquement autonome.

> **[LECTURE] Plan de fin de support — Exemple de référence.**

```yaml
end_of_support:
  product: Project Asteria
  decision_status: not_decided
  notice_period: pending-policy
  phases:
    - announcement
    - reduced_maintenance
    - update_end
    - service_retirement
    - final_archive
  player_data:
    export_available: not_assessed
    deletion_schedule: not_assessed
  community_content:
    export_and_moderation_plan: not_assessed
  public_statement: not_published
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Décision :** Le statut empêche de présenter cet exemple comme une annonce réelle.
- **Données :** Export et suppression sont évalués séparément.
- **Communauté :** La conservation ne supprime pas les obligations de modération et de droits.
- **Résultat attendu :** Chaque phase peut être préparée et communiquée sans date inventée.

## 35. Communiquer la fin de support

La communication publique précise :

- produit et versions concernés ;
- dates absolues ;
- services affectés ;
- conséquences sur installation, sauvegardes et multijoueur ;
- disponibilité des téléchargements ;
- export ou suppression des données ;
- support résiduel ;
- statut des mods et contenus communautaires ;
- canaux officiels ;
- corrections possibles du calendrier.

Une annonce ne promet pas une ouverture du code ou la gratuité d’assets tant que les droits ne sont pas vérifiés.

## 36. Évaluer une ouverture éventuelle

Ouvrir un dépôt ou publier des sources exige une revue distincte :

- droits sur le code, assets, voix, polices et données ;
- secrets et historique Git ;
- dépendances redistribuables ;
- marques et contenus sous contrat ;
- données personnelles ;
- documentation de build ;
- licence choisie ;
- gouvernance future ;
- politique de sécurité.

L’ouverture est une décision juridique et produit. Elle n’est pas une étape automatique de fin de vie.

## 37. Préserver le modding et les contenus communautaires

Le chapitre 21 possède la politique communautaire active. Lors de la pérennité, le projet conserve :

- versions d’API et schémas ;
- SDK et exemples redistribuables ;
- manifests et validateurs ;
- documentation de compatibilité ;
- outils d’export autorisés ;
- politique de conservation des contenus ;
- décisions de modération et voies de recours selon leur durée légitime.

Une archive communautaire ne permet pas de republier des contenus tiers sans droits.

## 38. Gérer un incident d’archive

Un incident d’archive peut être une copie manquante, une divergence de checksum, une clé perdue, un support illisible, un compte inaccessible ou une procédure de restauration obsolète.

Le traitement conserve :

- heure de détection ;
- objet et copie concernés ;
- portée ;
- actions de confinement ;
- sources saines candidates ;
- preuve de restauration ;
- décision de nouveau scellement ;
- mesures préventives.

Le rapport ne réécrit jamais l’ancien manifeste pour masquer l’incident.

## 39. Procédure Solo

En Solo :

1. maintenir un inventaire unique ;
2. automatiser la création des manifestes ;
3. conserver au moins une copie indépendante et une copie hors ligne ;
4. tester une restauration dans un dossier neuf ;
5. documenter les comptes sans stocker les secrets dans Git ;
6. désigner un contact de succession ;
7. conserver les licences et sources des dépendances ;
8. planifier une reconstruction annuelle réaliste ;
9. annoncer honnêtement les réserves non testées.

La simplicité est préférable à une architecture d’archivage impossible à maintenir.

## 40. Procédure Studio

En Studio, séparer :

- propriétaire produit ;
- maintenance technique ;
- sécurité ;
- release engineering ;
- gestion des archives ;
- juridique et licences ;
- gestion des comptes ;
- support et communication ;
- trust and safety pour les contenus communautaires.

Chaque archive publiée possède une revue croisée, un journal d’accès, une politique de rétention, une preuve de fixité et un scénario de reconstruction attribué.

## 41. Arborescence candidate de `Project Asteria`

> **[LECTURE] Arborescence de conservation — Ne pas créer automatiquement.**

```text
archive/
├── releases/
│   └── 1.4.0/
│       ├── archive-manifest.json
│       ├── source/
│       ├── build-environment/
│       ├── builds/
│       ├── sbom/
│       ├── licenses/
│       ├── documentation/
│       ├── reports/
│       └── checksums/
├── tools/
├── format-migrations/
└── succession/
    └── README-NO-SECRETS.md
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** Chaque release historique possède un dossier autonome.
- **Séparation :** Sources, environnement, builds, preuves et droits restent distingués.
- **Secrets :** Le dossier de succession ne contient que les procédures et références.
- **Résultat attendu :** Une personne commence par le manifeste et trouve toutes les catégories attendues.

## 42. Automatiser un préflight d’archive

Le préflight vérifie la structure et les métadonnées avant copie. Il ne remplace ni l’ouverture réelle des fichiers, ni la restauration, ni la reconstruction.

> **[VSC] Créer `tools/archive/preflight_archive.py`.**

```python
from __future__ import annotations

import json
from pathlib import Path

REQUIRED = {
    "archive-manifest.json",
    "source",
    "build-environment",
    "builds",
    "sbom",
    "licenses",
    "documentation",
    "reports",
    "checksums",
}

def preflight(root: Path) -> dict[str, object]:
    present = {path.name for path in root.iterdir()}
    missing = sorted(REQUIRED - present)
    manifest_path = root / "archive-manifest.json"
    manifest = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path.is_file()
        else None
    )
    return {
        "root": root.as_posix(),
        "missing": missing,
        "manifest_loaded": manifest is not None,
        "candidate": not missing and manifest is not None,
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Constante :** La liste requise décrit la structure minimale du dossier de version.
- **Entrée :** La fonction reçoit un dossier déjà sélectionné.
- **Retour :** Le dictionnaire distingue éléments manquants et manifeste lisible.
- **Limite :** Le statut `candidate` ne prouve ni fixité ni reconstructibilité.

> **[PS] PowerShell 7 — Lancer le préflight sans modifier l’archive.**

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

python tools/archive/run_preflight.py `
    --root "build/archive/1.4.0" `
    --report "reports/archive/preflight-1.4.0.json"

if ($LASTEXITCODE -ne 0) {
    throw "Archive preflight failed with code $LASTEXITCODE"
}

Get-Content "reports/archive/preflight-1.4.0.json" -Raw
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Arguments :** Racine et rapport sont fournis comme paramètres explicites.
- **Code de sortie :** PowerShell transforme l’échec Python en arrêt contrôlé.
- **Effet de bord :** Seul le rapport est créé hors de l’archive candidate.
- **Résultat attendu :** Le JSON final est lu et conservé pour la revue.

## 43. Dossier opérationnel de `Project Asteria`

Pour le projet fil rouge, le lot de conservation candidat comprend :

- `docs/maintenance/ownership.yaml` ;
- `docs/maintenance/inventory.yaml` ;
- `docs/maintenance/calendar.yaml` ;
- `docs/security/vulnerability-triage.yaml` ;
- `archive/releases/<version>/archive-manifest.json` ;
- bundle Git, références et checksums ;
- environnement de build ;
- SBOM et licences ;
- builds autorisés et symboles ;
- rapports QA et reconstruction ;
- procédure de succession sans secrets ;
- plan de fin de support non publié tant qu’il n’est pas décidé.

Aucun de ces fichiers n’est matérialisé par le présent chapitre. Ils constituent une architecture documentaire à adapter, vérifier et tester.

## 44. Limites connues

Le niveau `static-review` laisse ouvertes les questions suivantes :

- capacité et coût réels des supports ;
- temps de restauration ;
- durée de conservation des clés ;
- disponibilité future des SDK propriétaires ;
- reproductibilité des exports et signatures ;
- droits de redistribution des outils et assets ;
- conservation des données joueurs ;
- transfert effectif des comptes ;
- ouverture éventuelle du code ;
- validation d’un format patrimonial ;
- accessibilité du PDF final du Livre IV ;
- licence globale de la collection.

## 45. Dix diagnostics détaillés

<!-- qa:error-correction-section -->

### 45.1 Confondre miroir et archive

**Symptôme ou risque :** La suppression d’une branche est répliquée sur toutes les destinations synchronisées.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
copies:
  primary: repository-a
  secondary: mirror-of-repository-a
retention: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** Le secondaire reproduit l’état courant sans rétention indépendante.
- **Conséquence :** Une suppression logique peut devenir définitive sur les deux emplacements.
- **Cause :** La réplication est prise à tort pour une conservation historique.
- **Refus attendu :** Aucune topologie n’est acceptée sans version immuable ou copie hors ligne.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
copies:
  primary: repository-a
  historical:
    medium: versioned-object-storage
    separate_credentials: true
  offline:
    medium: encrypted-removable-storage
restore_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Une copie historique et une copie hors ligne sont indépendantes du miroir.
- **Contrôle :** Des identifiants séparés limitent la compromission commune.
- **Limite :** Le chiffrement exige une récupération de clé réellement testée.
- **Résultat attendu :** La perte du primaire ne détruit pas toutes les générations.

### 45.2 Archiver seulement le code source

**Symptôme ou risque :** La version ne peut pas être reconstruite car les templates d’export et dépendances ont disparu.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```text
archive-1.4.0/
└── source.zip
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** Le code est séparé de ses outils, dépendances et preuves.
- **Conséquence :** La reconstruction dépend de téléchargements ou souvenirs non garantis.
- **Cause :** Le dépôt est confondu avec le système complet.
- **Refus attendu :** Une archive historique sans manifeste d’environnement reste incomplète.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```text
archive-1.4.0/
├── archive-manifest.json
├── source/
├── build-environment/
├── dependencies/
├── builds/
├── licenses/
└── reports/
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Les entrées nécessaires sont reliées au même dossier de version.
- **Traçabilité :** Le manifeste corrèle sources, outils, artefacts et droits.
- **Limite :** Les éléments non redistribuables restent référencés avec une procédure légitime.
- **Résultat attendu :** L’absence d’une entrée devient visible avant l’exercice de reconstruction.

### 45.3 Considérer un checksum comme une signature

**Symptôme ou risque :** Un attaquant remplace à la fois le fichier et le manifeste stockés au même endroit.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{"file":"build.zip","sha256":"value-next-to-file","authenticity":"guaranteed"}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** La valeur de référence n’est pas protégée indépendamment.
- **Conséquence :** Une modification coordonnée peut rester cohérente avec le faux manifeste.
- **Cause :** Fixité et authenticité sont fusionnées.
- **Refus attendu :** Le manifeste n’annonce aucune authenticité sans politique de confiance.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{"file":"build.zip","sha256":"measured-value","manifest_copy":"independent-location","signature_status":"not_materialized"}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Le checksum prouve seulement la comparaison d’octets.
- **Indépendance :** Une copie de référence distincte réduit le risque de remplacement coordonné.
- **Limite :** La signature reste non matérialisée et nécessite sa propre chaîne de confiance.
- **Résultat attendu :** Le rapport distingue fixité vérifiée et authenticité non établie.

### 45.4 Conserver des secrets dans l’archive Git

**Symptôme ou risque :** Une clé privée devient lisible par toutes les personnes ayant accès à l’historique.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
succession:
  signing_private_key: |
    -----BEGIN PRIVATE KEY-----
    secret
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** La documentation contient une valeur secrète durable dans l’historique.
- **Conséquence :** La révocation n’efface pas les copies déjà clonées.
- **Cause :** Le besoin de succession est confondu avec la duplication du secret.
- **Refus attendu :** Toute valeur secrète bloque le scellement documentaire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
succession:
  signing_key_location: dedicated-key-custody
  recovery_authority: security-custodian
  required_approvals: 2
  private_key_in_document: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Le document décrit la récupération sans contenir la clé.
- **Autorité :** Le transfert exige des rôles et approbations.
- **Limite :** Le coffre et la procédure doivent être testés séparément.
- **Résultat attendu :** La succession reste possible sans exposition du secret.

### 45.5 Fermer une alerte sans justification

**Symptôme ou risque :** Le même risque réapparaît et personne ne sait pourquoi il avait été accepté.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
advisory: GHSA-xxxx-yyyy-zzzz
state: dismissed
reason: false-positive
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** Le libellé ne contient ni contexte, ni preuve, ni échéance.
- **Conséquence :** La décision ne peut pas être réévaluée lors d’un changement d’usage.
- **Cause :** L’état de l’outil remplace le dossier de triage.
- **Refus attendu :** Une fermeture sans propriétaire et preuve reste non conforme.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
advisory: GHSA-xxxx-yyyy-zzzz
state: accepted_with_review
contexts:
  shipped_runtime: false
evidence: reports/security/advisory-analysis.md
owner_role: security_custodian
next_review: 2026-08-05
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Contexte, preuve, propriétaire et revue sont explicites.
- **Révision :** La décision peut changer si le composant entre dans le runtime.
- **Limite :** La date est un exemple documentaire, pas un engagement réel.
- **Résultat attendu :** Le registre explique et réouvre la décision au bon moment.

### 45.6 Écraser l’original pendant une migration de format

**Symptôme ou risque :** Une conversion imparfaite détruit la seule source haute fidélité.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```python
converted = convert(source)
source.write_bytes(converted)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** La sortie remplace l’original avant validation.
- **Conséquence :** Les données perdues ne peuvent plus être récupérées.
- **Cause :** Migration et remplacement sont exécutés comme une seule opération.
- **Refus attendu :** Une conversion ne peut écrire dans le chemin source.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```python
target = migration_root / source.name
converted = convert(source)
target.write_bytes(converted)
validate_derivative(source, target)
record_relationship(source, target)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Le dérivé est écrit dans un espace distinct.
- **Validation :** La fidélité est vérifiée avant toute promotion.
- **Traçabilité :** La relation entre original et dérivé est enregistrée.
- **Résultat attendu :** L’original reste disponible pour une migration future.

### 45.7 Annoncer une reconstruction réussie après un clone

**Symptôme ou risque :** Le dépôt est présent mais aucun outil, export ou artefact n’a été vérifié.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{"repository_cloned":true,"reconstruction":"success"}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** La présence des sources est assimilée à un build reconstruit.
- **Conséquence :** Les dépendances et différences d’artefacts restent inconnues.
- **Cause :** Restauration du dépôt et reconstruction du produit sont fusionnées.
- **Refus attendu :** Le statut `success` exige un artefact et une comparaison qualifiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{"repository_cloned":true,"build_executed":false,"artifact_comparison":"not_executed","decision":"incomplete"}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Chaque étape possède son propre statut.
- **Honnêteté :** Les actions non exécutées restent explicites.
- **Limite :** Un build fonctionnellement équivalent exige des critères publiés.
- **Résultat attendu :** Le rapport indique précisément ce qui manque.

### 45.8 Dépendre d’un compte personnel unique

**Symptôme ou risque :** Le départ d’une personne bloque domaine, dépôt et portail de distribution.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
critical_account:
  owner: personal-email@example.invalid
  recovery: same-person
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** Propriété et récupération reposent sur la même personne.
- **Conséquence :** Une indisponibilité individuelle devient une perte d’autorité.
- **Cause :** La commodité initiale est restée une architecture permanente.
- **Refus attendu :** Un compte critique sans propriété organisationnelle est signalé.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
critical_account:
  owner: organization
  admins:
    - role: primary-admin
    - role: recovery-admin
  recovery_channel: independent-organizational-contact
  last_review: null
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Propriété, administration et récupération sont séparées.
- **Succession :** Les rôles peuvent changer sans modifier l’identité du compte.
- **Limite :** Les contacts réels restent dans un registre d’accès protégé.
- **Résultat attendu :** La récupération ne dépend pas du titulaire principal.

### 45.9 Supprimer un service sans plan de données

**Symptôme ou risque :** Les joueurs perdent accès à leurs données et le support ne peut expliquer les délais.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
service_retirement:
  date: tomorrow
  export: none
  deletion: immediate
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** Retrait, export, conservation et suppression ne sont pas gouvernés.
- **Conséquence :** Les droits et attentes des utilisateurs ne peuvent pas être respectés.
- **Cause :** La coupure technique est prise pour une fin de support complète.
- **Refus attendu :** Aucun retrait public n’est autorisé sans plan de données et communication.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
service_retirement:
  decision_status: not_decided
  notice_period: pending-policy
  export_assessment: required
  deletion_schedule: required
  support_statement: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Chaque décision reste séparée et en attente d’une politique.
- **Communication :** Le support public précède la coupure effective.
- **Limite :** Les obligations réelles nécessitent une revue juridique et produit.
- **Résultat attendu :** Le calendrier n’est publié qu’après fermeture des portes.

### 45.10 Déclarer une archive saine sans restauration

**Symptôme ou risque :** Les checksums passent, mais la clé de déchiffrement ou le logiciel d’ouverture manque.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
archive:
  checksum_match: true
  restore_test: never
  decision: healthy
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

**Explication structurée du bloc :**

- **Invariant violé :** La fixité est assimilée à l’utilisabilité.
- **Conséquence :** L’échec n’apparaît qu’au moment de l’incident.
- **Cause :** Le contrôle d’octets remplace l’exercice de restauration.
- **Refus attendu :** Une archive non restaurée reste seulement fixité-vérifiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
archive:
  checksum_match: true
  restore_test:
    status: not_executed
    required_environment: documented
  decision: fixity_verified_only
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

**Explication structurée du bloc :**

- **Invariant restauré :** Fixité et restauration possèdent des statuts distincts.
- **Préparation :** L’environnement requis est documenté avant l’exercice.
- **Limite :** La santé complète exige une restauration et, pour une release, une reconstruction.
- **Résultat attendu :** Le rapport ne surévalue pas la preuve disponible.

## 46. Checklist d’acceptation documentaire

- [ ] Le calendrier de maintenance possède rôles, cadences et preuves.
- [ ] L’inventaire couvre dépendances, outils, comptes, formats, services et clés.
- [ ] Les alertes de vulnérabilité sont triées avec contexte et justification.
- [ ] Un SBOM versionné est corrélé à chaque build qualifié.
- [ ] La topologie d’archives comprend des copies réellement indépendantes.
- [ ] Les bundles, objets LFS, sous-modules, releases et dépendances externes sont couverts.
- [ ] Sources, environnement, builds, licences, documentation et QA sont reliés par manifeste.
- [ ] Checksums, signatures, fixité et authenticité sont distingués.
- [ ] Une restauration isolée et une reconstruction historique possèdent des procédures séparées.
- [ ] Les écarts de reproductibilité sont qualifiés.
- [ ] Les formats sources et dérivés restent liés sans écrasement.
- [ ] Les comptes critiques et secrets possèdent un plan de succession.
- [ ] La disparition d’un fournisseur possède un plan de sortie.
- [ ] La fin de support couvre données, services, sauvegardes et communauté.
- [ ] Les réserves runtime, juridiques, de licence et PDF sont publiques.

## 47. Critère de passage

Le chapitre peut être accepté au niveau `static-review` lorsque les cinq objectifs et livrables du plan maître sont couverts, que chaque bloc significatif possède une explication structurée, que les dix diagnostics sont complets, que les références officielles sont cliquables, que les frontières des chapitres 14, 15, 16, 20 et 21 restent explicites et qu’aucune archive ou reconstruction n’est présentée comme exécutée.

Le passage à `runtime-tested` exigerait au minimum une archive scellée, plusieurs copies indépendantes, un test de restauration, une reconstruction historique dans un environnement vierge, une comparaison d’artefacts, un exercice de succession limité, des rapports conservés et une décision formelle sur les écarts.

## 48. Références officielles

- [Git — Documentation de `git bundle`](https://git-scm.com/docs/git-bundle)
- [Git — Documentation de `git clone`](https://git-scm.com/docs/git-clone)
- [GitHub — Alertes Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts)
- [GitHub — Graphe de dépendances et soumission des dépendances](https://docs.github.com/en/rest/dependency-graph/dependency-submission)
- [SPDX — Spécifications officielles](https://spdx.dev/use/specifications/)
- [CycloneDX — Vue d’ensemble de la spécification](https://cyclonedx.org/specification/overview/)
- [CycloneDX — Référence JSON](https://cyclonedx.org/docs/1.7/json/)
- [SLSA — Spécification](https://slsa.dev/spec/)
- [Sigstore — Documentation](https://docs.sigstore.dev/)
- [NIST — Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
- [CISA — Software Bill of Materials](https://www.cisa.gov/sbom)
- [Library of Congress — Sustainability of Digital Formats](https://www.loc.gov/preservation/digital/formats/)
- [Godot — Licence et conformité](https://docs.godotengine.org/en/stable/about/complying_with_licenses.html)
- [Godot — Exporter des packs, patches et mods](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)

Les pages, versions de spécification, fonctionnalités de plateformes et exigences juridiques sont volatiles. Elles doivent être revérifiées au moment d’une implémentation, d’une archive ou d’une publication réelle.

## 49. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` adopte les décisions documentaires suivantes :

- le dossier de version relie sources, outils, dépendances, builds, SBOM, licences, documentation et QA ;
- un miroir ne remplace ni l’historique immuable ni la copie hors ligne ;
- le bundle Git est accompagné de ses références, checksums et inventaires externes ;
- les dépendances et outils de build sont épinglés et archivés selon leurs droits ;
- les vulnérabilités sont triées par contexte avant décision ;
- fixité, signature, authenticité, restauration et reconstruction restent cinq preuves distinctes ;
- l’original est conservé lors de toute migration de format ;
- les secrets sont exclus des archives documentaires ;
- comptes, domaines, certificats et clés possèdent des propriétaires et voies de récupération ;
- la succession et la fin de support sont préparées avant l’urgence ;
- l’ouverture éventuelle du code ou des contenus exige une revue de droits séparée ;
- la fin de support ne devient publique qu’après fermeture des portes produit, sécurité, données, juridique et communication.

La porte d’acceptation demeure documentaire. Les archives, outils, SBOM, copies, restaurations, reconstructions, migrations, transferts d’autorité, revues juridiques et communications restent à matérialiser et à exécuter.
