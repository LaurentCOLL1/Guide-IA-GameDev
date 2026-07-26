---
title: "Livre IV — Chapitre 15 : Sauvegardes, migrations et reprise après incident"
id: "DOC-L4-CH15"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 15
last-verified: "2026-07-27T01:20:18+02:00"
audit-status: "complete"
audit-date: "2026-07-27T01:20:18+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-15.md"
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

# Sauvegardes, migrations et reprise après incident

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 14 a organisé la chaîne d’intégration, les artefacts, les manifestes, les empreintes et la reconstruction depuis un clone neuf. Le présent chapitre traite une responsabilité différente : conserver les données irremplaçables, restaurer un produit cohérent après perte ou corruption, et faire évoluer les formats sans rendre les anciennes données inutilisables.

Une sauvegarde n’est pas une simple copie effectuée « au cas où ». Elle appartient à un système complet : inventaire, classification, fréquence, rétention, chiffrement, contrôle d’intégrité, ordre de restauration, test isolé, propriétaire, journal de preuve et décision de reprise. Une sauvegarde non testée reste un candidat, pas une capacité démontrée.

Le chapitre 16 possédera les presets d’export, les packages installables et les signatures de plateforme. Le chapitre 20 possédera les correctifs distribués, les mises à jour produit et leurs rollbacks. Le chapitre 22 possédera l’archivage de long terme et la pérennité de la collection. Ici, la portée est la continuité du produit et de son infrastructure : sources, configurations, builds retenus, bases, sauvegardes joueurs, services, secrets récupérables et preuves nécessaires à une restauration.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer sauvegarde, réplication, snapshot, archive, export logique et synchronisation ;
- inventorier les données critiques et leur autorité ;
- définir des objectifs RPO et RTO sans les présenter comme des garanties ;
- choisir fréquence, rétention et nombre de générations selon le risque ;
- séparer sources canoniques, données reconstructibles, secrets et preuves ;
- produire des manifestes et empreintes contrôlables ;
- sauvegarder correctement un fichier SQLite ou une base PostgreSQL ;
- protéger une sauvegarde contre suppression, altération et exposition ;
- préparer une restauration dans un environnement isolé ;
- vérifier cohérence fonctionnelle, version et dépendances après restauration ;
- organiser migrations de schéma et de format avec préflight et rollback ;
- distinguer retour arrière applicatif et restauration de données ;
- préparer des scénarios de perte, corruption, rançongiciel et erreur humaine ;
- organiser les responsabilités Solo et Studio ;
- diagnostiquer les anti-patterns les plus fréquents.

## 3. Niveau de preuve et réserves

## 3.1. Déclarer le niveau de preuve

> **[LECTURE] Déclarer le niveau de preuve — Adapter les valeurs au projet.**

```yaml
evidence_level:
  chapter: static_review
  backup_jobs_materialized: false
  isolated_restore_executed: false
  sqlite_restore_executed: false
  postgresql_restore_executed: false
  player_save_migration_executed: false
  service_recovery_executed: false
  disaster_drill_executed: false
  measured_rpo_available: false
  measured_rto_available: false
  runtime_claimed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`chapter` :** `static_review` signifie que les procédures et contrats sont relus sans exécution de reprise réelle.
- **Booléens :** chaque famille de preuve reste indépendante ; un script écrit ne prouve pas qu’une restauration aboutit.
- **RPO/RTO mesurés :** les objectifs définis plus loin ne deviennent des résultats qu’après exercices horodatés.
- **Limite :** aucune disponibilité, intégrité opérationnelle ou continuité de service n’est déduite du document seul.

## 4. Prérequis et frontières

Le lecteur doit connaître Git et GitHub du Livre I, les données persistantes et migrations SQLite du Livre II chapitre 8, les sauvegardes joueurs du Livre II chapitre 9, la journalisation du Livre IV chapitre 5, les serveurs dédiés du chapitre 13 et la chaîne DevOps du chapitre 14.

Le chapitre possède :

- l’inventaire global des données critiques ;
- les objectifs RPO, RTO et de rétention ;
- les politiques de sauvegarde de sources, bases, services et données joueurs ;
- les manifestes, empreintes, catalogues et journaux de sauvegarde ;
- l’ordre de restauration d’un environnement ;
- les migrations globales et la compatibilité de reprise ;
- les exercices de restauration et scénarios catastrophe.

Le chapitre ne possède pas :

- la sérialisation détaillée d’un slot joueur, déjà traitée au Livre II chapitre 9 ;
- les règles d’exploitation réseau du serveur, traitées au chapitre 13 ;
- l’orchestration générale CI/CD, traitée au chapitre 14 ;
- les formats de packages installables, traités au chapitre 16 ;
- la distribution initiale, traitée au chapitre 17 ;
- les patches distribués et canaux de mise à jour, traités au chapitre 20 ;
- l’archivage patrimonial de long terme, traité au chapitre 22.

## 5. Vocabulaire opérationnel

- **Sauvegarde :** copie gouvernée destinée à restaurer une donnée ou un système après perte, corruption ou erreur.
- **Restauration :** reconstruction d’un état utilisable à partir d’une sauvegarde vérifiée.
- **RPO, Recovery Point Objective :** quantité maximale de données que l’organisation accepte de perdre, exprimée comme un point dans le temps.
- **RTO, Recovery Time Objective :** durée cible entre l’interruption et le retour à un service acceptable.
- **Rétention :** durée pendant laquelle une génération de sauvegarde est conservée.
- **Génération :** sauvegarde identifiable correspondant à une date, un état et un manifeste.
- **Snapshot :** image cohérente d’un volume ou d’un système à un instant donné ; elle n’est pas automatiquement indépendante de la source.
- **Réplication :** copie continue ou différée d’un état vers un autre emplacement ; elle peut répliquer une corruption ou une suppression.
- **Export logique :** représentation des objets et données, par exemple un dump SQL, indépendante de l’agencement physique du stockage.
- **Sauvegarde physique :** copie des fichiers ou blocs nécessaires au moteur de stockage, avec ses contraintes de cohérence.
- **Archive :** conservation de long terme destinée à consultation, preuve ou pérennité, pas nécessairement à une reprise rapide.
- **PITR :** restauration à un point dans le temps à partir d’une base et d’un journal continu.
- **Migration :** transformation versionnée d’un schéma ou format vers une version plus récente.
- **Rollback :** retour contrôlé à une version applicative ou à une étape précédente ; il ne restaure pas automatiquement les données.
- **Runbook :** procédure exécutable décrivant préconditions, commandes, décisions, sorties et escalade.

## 6. Ne pas confondre les mécanismes de protection

> **[LECTURE] Comparer les mécanismes — Adapter la politique au risque.**

```yaml
protection_mechanisms:
  backup:
    independent_copy: required
    primary_goal: recovery
  replication:
    independent_copy: not_guaranteed
    primary_goal: availability
  snapshot:
    independent_copy: depends_on_backend
    primary_goal: rapid_point_in_time_view
  archive:
    independent_copy: required
    primary_goal: long_term_preservation
  synchronization:
    independent_copy: false
    primary_goal: convenience
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Indépendance :** une synchronisation ou une réplication peut propager immédiatement une suppression.
- **Snapshot :** son indépendance dépend du stockage ; un snapshot sur le même volume ne couvre pas la perte de ce volume.
- **Objectifs :** disponibilité, reprise et conservation sont des besoins différents.
- **Décision :** la politique combine plusieurs mécanismes au lieu d’en présenter un seul comme universel.

## 7. Inventorier les données critiques

L’inventaire commence avant le choix d’un outil. Pour chaque famille, il indique propriétaire, source canonique, emplacement, volume, sensibilité, fréquence de changement, dépendances, format de sauvegarde et procédure de restauration.

Les familles initiales de `Project Asteria` sont :

- dépôt Git et objets Git LFS éventuels ;
- sous-modules ou dépendances sources épinglées ;
- fichiers de conception non reconstructibles ;
- configurations d’environnement sans leurs secrets en clair ;
- secrets récupérables depuis un gestionnaire dédié ;
- bases SQLite locales ;
- base de service éventuelle ;
- sauvegardes joueurs et profils ;
- builds candidats retenus avec manifestes ;
- journaux et preuves nécessaires à un incident ;
- registres de licences, consentements et provenance ;
- documentation et runbooks ;
- états de services nécessaires à une reprise.

## 7.1. Registre minimal des actifs

> **[VSC] Créer `docs/continuity/critical-data-inventory.yaml` — Adapter les identifiants et emplacements.**

```yaml
assets:
  - id: AST-DATA-SOURCE-001
    name: depot-git-principal
    authority: canonical
    owner: engineering
    location: github-primary
    change_rate: continuous
    sensitivity: internal
    dependencies: []
    backup_method: verified-mirror-bundle
    restore_order: 10
  - id: AST-DATA-PLAYER-001
    name: sauvegardes-joueurs
    authority: canonical-runtime
    owner: game-runtime
    location: user-profile
    change_rate: frequent
    sensitivity: personal-possible
    dependencies:
      - AST-DATA-SCHEMA-001
    backup_method: versioned-export
    restore_order: 60
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`id` :** identifiant stable utilisé dans les manifestes et exercices ; le nom affiché peut évoluer.
- **`authority` :** distingue source canonique, état runtime et donnée reconstructible.
- **`dependencies` :** impose l’ordre de restauration sans le déduire du nom des fichiers.
- **`restore_order` :** entier de tri initial ; le graphe de dépendances reste prioritaire en cas de conflit.
- **Sensibilité :** `personal-possible` déclenche minimisation, chiffrement, accès limité et politique de retrait adaptée.

## 8. Classer autorité, reconstructibilité et sensibilité

Une donnée critique n’est pas forcément irremplaçable. Le classement évite de sauvegarder massivement des caches tout en oubliant une clé de signature, un registre juridique ou un fichier source unique.

> **[LECTURE] Matrice de classification — Adapter les durées et contrôles.**

```yaml
classification:
  canonical_irreplaceable:
    examples: [source-art, legal-register, player-state]
    backup_required: true
    integrity_check: strict
  canonical_recreatable_with_cost:
    examples: [build-candidate, generated-navigation]
    backup_required: risk_based
    rebuild_procedure: required
  derived_reconstructible:
    examples: [cache, vector-index, imported-cache]
    backup_required: false
    source_reference: required
  secret:
    examples: [signing-key, deployment-token]
    backup_required: dedicated-secret-recovery
    plaintext_archive: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Canonique :** l’autorité métier impose une restauration exacte ou une migration contrôlée.
- **Reconstructible :** le coût de recalcul décide si une copie est économiquement utile ; la source et la procédure restent obligatoires.
- **Caches :** ils ne deviennent pas autoritaires parce qu’ils sont volumineux ou rapides à restaurer.
- **Secrets :** leur récupération suit un mécanisme dédié avec rotation, révocation et accès séparés.

## 9. Définir RPO et RTO

RPO et RTO sont des objectifs de conception. Ils expriment ce que l’équipe cherche à atteindre et orientent fréquence, technologie, personnel et coût. Ils ne garantissent aucun résultat avant une campagne de restauration mesurée.

## 9.1. Tableau d’objectifs candidat

> **[LECTURE] Définir des objectifs candidats — Remplacer les valeurs après analyse métier.**

```yaml
recovery_objectives:
  source_repository:
    target_rpo: 24h
    target_rto: 4h
    minimum_service: clone-buildable
  player_saves:
    target_rpo: 15m
    target_rto: 2h
    minimum_service: load-and-resave
  dedicated_service_database:
    target_rpo: 5m
    target_rto: 1h
    minimum_service: read-write-without-corruption
  publication_evidence:
    target_rpo: 24h
    target_rto: 24h
    minimum_service: searchable-and-verifiable
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durées :** les valeurs sont des objectifs candidats, pas des mesures obtenues.
- **`minimum_service` :** définit un état acceptable observable plutôt qu’un vague « système revenu ».
- **Priorisation :** une base de service peut demander un RPO plus faible qu’une preuve de publication.
- **Validation :** chaque exercice conserve heure de début, point restauré, heure de service minimal et écarts à la cible.

## 9.2. Calculer la perte temporelle observée

> **[VSC] Créer `tools/continuity/measure_recovery.py` — Adapter le format des horodatages.**

```python
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RecoveryMeasure:
    incident_detected_at: datetime
    recovered_point_at: datetime
    minimum_service_at: datetime

    def observed_data_loss_seconds(self) -> float:
        delta = self.incident_detected_at - self.recovered_point_at
        return max(delta.total_seconds(), 0.0)

    def observed_recovery_seconds(self) -> float:
        delta = self.minimum_service_at - self.incident_detected_at
        return max(delta.total_seconds(), 0.0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`RecoveryMeasure` :** dataclass immuable regroupant trois instants timezone-aware fournis par le rapport d’exercice.
- **Valeurs de retour :** chaque méthode retourne un `float` en secondes afin de permettre comparaison et agrégation.
- **Soustraction :** les opérateurs `-` produisent des `timedelta`; `total_seconds()` conserve les fractions de seconde.
- **`max(..., 0.0)` :** refuse un résultat négatif sans masquer une chronologie incohérente, qui doit être signalée séparément par le validateur.
- **Limite :** ces mesures décrivent un exercice ; elles ne prédisent pas automatiquement le prochain incident.

## 10. Construire le graphe de dépendances de restauration

Une restauration globale suit les dépendances : identités et secrets récupérables, réseau isolé, stockage, bases, services, configurations, builds, données joueurs, puis observation et ouverture graduelle. L’ordre ne doit pas être improvisé pendant l’incident.

> **[LECTURE] Définir l’ordre logique de reprise — Adapter les composants.**

```yaml
restore_graph:
  secret-recovery: []
  isolated-network: []
  storage: [isolated-network]
  database: [storage, secret-recovery]
  application-config: [secret-recovery]
  application-build: [storage, application-config]
  game-service: [database, application-build]
  player-data: [database, game-service]
  observability: [game-service]
  controlled-admission: [observability, player-data]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Listes :** chaque clé dépend uniquement des composants qui doivent être disponibles avant elle.
- **Parallélisme :** les nœuds sans dépendance commune peuvent être préparés en parallèle si les responsabilités sont distinctes.
- **Admission :** les joueurs ou clients ne sont réadmis qu’après observation et contrôle des données.
- **Cycle :** un validateur doit refuser un graphe cyclique plutôt que choisir un ordre arbitraire.

## 11. Choisir les générations et la rétention

Une politique simple combine généralement plusieurs horizons : générations fréquentes pour les erreurs récentes, quotidiennes pour les incidents différés, mensuelles ou releases pour les événements découverts tardivement. Les durées dépendent du volume, de la réglementation, du coût et de la capacité réelle de restauration.

> **[LECTURE] Politique de rétention candidate — Adapter aux obligations et coûts.**

```yaml
retention_policy:
  frequent:
    interval_minutes: 15
    keep_count: 16
  daily:
    interval_hours: 24
    keep_count: 14
  weekly:
    interval_days: 7
    keep_count: 8
  release:
    trigger: approved-release
    keep_until: end-of-support-plus-review
  deletion:
    requires:
      - retention-expired
      - no-legal-hold
      - replacement-generation-verified
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Horizons :** les générations courtes couvrent l’erreur récente, les générations longues couvrent la découverte tardive.
- **`keep_count` :** entier de capacité ; la durée réelle dépend de l’intervalle et des échecs éventuels.
- **Release :** une sauvegarde liée à une version suit le support du produit, sans préjuger de l’archivage patrimonial du chapitre 22.
- **Suppression :** elle reste une opération gouvernée et ne dépend pas uniquement de l’âge du fichier.

## 11.1. Estimer un budget de stockage

> **[LECTURE] Estimation pédagogique en euros — Remplacer par les tarifs réels.**

```yaml
storage_budget_example:
  monthly_limit_eur: 40
  estimated_primary_copy_eur: 12
  estimated_offsite_copy_eur: 18
  estimated_immutable_copy_eur: 8
  reserve_eur: 2
  decision: candidate-only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Devise :** toutes les valeurs utilisent l’euro conformément au contexte français du guide.
- **Somme :** `12 + 18 + 8 + 2 = 40`; la réserve évite de consommer tout le plafond prévu.
- **Statut :** `candidate-only` interdit de présenter ces montants comme un devis ou un coût observé.
- **Limite :** le coût ne justifie pas de supprimer la seule génération restaurable ni de réduire silencieusement la rétention.

## 12. Séparer les emplacements et les identités

Plusieurs copies sur le même volume, le même compte administrateur ou le même fournisseur ne couvrent pas la même famille d’incidents. La séparation recherche au minimum des pannes indépendantes : support distinct, emplacement hors site, identité différente et copie non modifiable pendant une durée définie.

> **[LECTURE] Carte des copies — Adapter aux moyens réellement disponibles.**

```yaml
backup_copies:
  local-fast:
    medium: dedicated-volume
    identity: backup-local-writer
    mutable: true
  offsite:
    medium: remote-object-storage
    identity: backup-offsite-writer
    mutable: versioned
  immutable:
    medium: locked-object-storage
    identity: retention-admin-separated
    mutable: false-during-retention
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** le compte qui écrit la production ne doit pas pouvoir supprimer toutes les générations.
- **Copie locale :** elle accélère la reprise mais ne couvre pas sinistre du site ou compromission commune.
- **Copie immuable :** sa durée de verrouillage est définie avant écriture ; elle n’empêche pas la fuite de données si l’accès en lecture est trop large.
- **Versionnement :** il conserve des générations mais ne remplace ni validation ni restauration testée.

## 13. Produire un manifeste fermé

Chaque génération possède un identifiant, une date UTC, une source, une version de schéma, une liste fermée de fichiers, leurs tailles et leurs empreintes. Le manifeste est écrit après la copie et avant la promotion de la génération en état vérifiable.

## 13.1. Générer un manifeste en Python

> **[VSC] Créer `tools/continuity/build_backup_manifest.py` — Adapter les exclusions.**

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


def build_manifest(root: Path, generation_id: str) -> dict[str, object]:
    root = root.resolve()
    files: list[dict[str, object]] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        files.append({
            "path": relative,
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    if not files:
        raise ValueError("génération vide")
    return {
        "schema": "asteria-backup-manifest",
        "version": 1,
        "generation_id": generation_id,
        "files": files,
    }


def write_manifest(root: Path, generation_id: str, output: Path) -> None:
    value = build_manifest(root, generation_id)
    output.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`sha256_file(path) -> str` :** lit par blocs d’un mégaoctet et retourne une empreinte hexadécimale.
- **`build_manifest(...) -> dict[str, object]` :** reçoit la racine et un identifiant de génération, puis retourne une structure sérialisable.
- **Tri :** l’ordre lexical rend le manifeste stable pour une même liste de chemins.
- **Chemins :** `relative_to` exclut les chemins absolus propres à la machine.
- **Refus contrôlé :** une génération vide lève `ValueError` au lieu d’être promue.
- **Limite :** l’empreinte prouve l’intégrité relative à une valeur attendue, pas l’absence de code malveillant.

## 14. Vérifier strictement une génération

La vérification recalcule les empreintes, refuse les chemins absolus ou traversants, compare l’ensemble exact de fichiers et conserve le résultat dans un rapport distinct. Elle s’exécute lors de la création, périodiquement et avant restauration.

> **[VSC] Créer `tools/continuity/verify_backup_manifest.py` — Adapter le schéma accepté.**

```python
from __future__ import annotations

import json
from pathlib import Path

from build_backup_manifest import sha256_file


def verify_generation(root: Path, manifest_path: Path) -> None:
    root = root.resolve()
    manifest_path = manifest_path.resolve(strict=True)
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if data.get("schema") != "asteria-backup-manifest":
        raise ValueError("schéma de manifeste inconnu")
    if data.get("version") != 1:
        raise ValueError("version de manifeste non supportée")

    expected: set[str] = set()
    for entry in data.get("files", []):
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("chemin de manifeste non confiné")
        path = (root / relative).resolve()
        if root not in path.parents:
            raise ValueError("sortie de la racine de génération")
        if not path.is_file():
            raise ValueError(f"fichier manquant : {relative.as_posix()}")
        if path.stat().st_size != int(entry["size"]):
            raise ValueError(f"taille différente : {relative.as_posix()}")
        if sha256_file(path) != entry["sha256"]:
            raise ValueError(f"empreinte différente : {relative.as_posix()}")
        expected.add(relative.as_posix())

    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path != manifest_path
    }
    if actual != expected:
    raise ValueError("ensemble de fichiers différent")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    verify_generation(args.root, args.manifest)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** `root` désigne la génération extraite et `manifest_path` son manifeste de confiance.
- **Confinement :** chemins absolus, segments `..` et résolutions hors racine sont refusés.
- **Conversions :** `int(entry["size"])` normalise la taille déclarée avant comparaison.
- **Ensembles :** l’égalité finale détecte aussi un fichier supplémentaire non déclaré.
- **Valeur de retour :** la fonction retourne implicitement `None` sur succès et lève `ValueError` au premier invariant violé.
- **CLI :** les deux arguments positionnels sont convertis en `Path`, puis transmis à la même fonction que l’appel automatisé.

## 15. Sauvegarder le dépôt source

Une forge distante ne constitue pas à elle seule une sauvegarde complète. Le plan recense dépôt Git, refs, tags, branches, objets LFS, sous-modules, fichiers de configuration externes, registres de dépendances et droits nécessaires à la reconstruction.

Un `git clone` ordinaire ne capture pas les fichiers ignorés, les secrets, les réglages de forge, les artefacts expirés ni nécessairement tous les objets LFS non récupérés. La sauvegarde du dépôt reste séparée de la sauvegarde des services GitHub.

## 15.1. Créer un bundle Git vérifiable

> **[PS] Créer un bundle Git depuis la racine du dépôt — Adapter la destination.**

```powershell
param(
    [Parameter(Mandatory)]
    [string]$Destination
)

$ErrorActionPreference = "Stop"
git fsck --full
if ($LASTEXITCODE -ne 0) { throw "git fsck a échoué" }

git bundle create $Destination --all
if ($LASTEXITCODE -ne 0) { throw "création du bundle échouée" }

git bundle verify $Destination
if ($LASTEXITCODE -ne 0) { throw "bundle Git invalide" }

Get-FileHash -Algorithm SHA256 -Path $Destination
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre `Destination` :** chemin de sortie obligatoire ; son répertoire doit déjà exister et être confiné à la zone de sauvegarde.
- **`git fsck --full` :** contrôle la connectivité et la validité générale des objets avant création.
- **`git bundle create --all` :** inclut les refs locales connues ; la politique vérifie séparément LFS, sous-modules et réglages de forge.
- **Codes de retour :** `$LASTEXITCODE` bloque immédiatement chaque échec.
- **Sortie :** `Get-FileHash` fournit l’empreinte à enregistrer dans le manifeste.

## 15.2. Vérifier un bundle sous Windows CMD

> **[CMD] Vérifier un bundle Git — Adapter le chemin du fichier.**

```bat
@echo off
setlocal
set "BUNDLE=D:\AsteriaBackup\source\asteria.bundle"

git bundle verify "%BUNDLE%"
if errorlevel 1 exit /b %errorlevel%

certutil -hashfile "%BUNDLE%" SHA256
if errorlevel 1 exit /b %errorlevel%

exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`setlocal` :** limite la variable `BUNDLE` à ce script.
- **Guillemets :** ils protègent les chemins contenant des espaces.
- **`errorlevel` :** propage le code d’échec de Git ou `certutil`.
- **Résultat :** la vérification confirme le format du bundle et affiche une empreinte ; elle ne prouve pas la présence des fichiers externes au dépôt.

## 16. Sauvegarder les builds retenus

Tous les builds intermédiaires ne sont pas critiques. Les candidats approuvés, packages publiés, symboles de débogage nécessaires, manifestes, signatures et preuves doivent être reliés au commit, aux outils et au canal. Le chapitre 14 conserve leur identité ; le chapitre 15 définit combien de temps et dans combien d’emplacements ils restent restaurables.

> **[LECTURE] Registre d’un build conservé — Adapter les identifiants.**

```yaml
retained_build:
  build_id: 0.15.0+git.0123456789ab.run.123456789.1
  commit_sha: 0123456789abcdef0123456789abcdef01234567
  artifact_manifest_sha256: PLACEHOLDER_TO_REPLACE
  channel: release-candidate
  retention_class: supported-release
  restore_dependencies:
    - source-bundle
    - tool-manifest
    - export-presets
  rebuild_allowed: true
  byte_identity_required_for_promotion: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** build ID, commit et empreinte sont distincts et complémentaires.
- **Placeholder :** il bloque la promotion tant qu’une empreinte réelle n’est pas inscrite.
- **Dépendances :** la sauvegarde du binaire n’empêche pas de conserver la capacité de reconstruction.
- **`byte_identity_required_for_promotion` :** la promotion réutilise les octets vérifiés ; une restauration technique peut aussi reconstruire selon une procédure déclarée.

## 17. Sauvegarder les données joueurs sans redéfinir leur format

Le Livre II chapitre 9 possède le format de slot, les copies temporaires, la protection contre les versions futures et les migrations de sauvegarde. Ici, la politique globale ajoute :

- découverte des emplacements `user://` par plateforme ;
- consentement et information lorsque les fichiers quittent la machine ;
- chiffrement en transit et au repos lorsqu’une copie distante existe ;
- restauration dans un profil isolé avant remplacement du profil actif ;
- compatibilité avec le build de lecture ;
- rétention et suppression adaptées aux données personnelles ;
- absence d’autorité donnée aux caches ou index dérivés.

## 17.1. Copier un slot fermé vers une génération

> **[VSC] Créer `tools/continuity/copy_player_slot.py` — Exécuter uniquement après fermeture contrôlée du slot.**

```python
from __future__ import annotations

import shutil
from pathlib import Path


def copy_closed_slot(source: Path, generation_root: Path) -> Path:
    source = source.resolve(strict=True)
    generation_root = generation_root.resolve(strict=True)
    if not source.is_file():
        raise ValueError("le slot source n’est pas un fichier")
    destination = generation_root / source.name
    if destination.exists():
        raise FileExistsError(destination)
    shutil.copy2(source, destination)
    if destination.stat().st_size != source.stat().st_size:
        destination.unlink(missing_ok=True)
        raise OSError("taille différente après copie")
    return destination
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** le service de sauvegarde joueur a fermé et validé le fichier avant l’appel.
- **`resolve(strict=True)` :** exige que les deux chemins existent et normalise leurs cibles.
- **`copy2` :** copie le contenu et les métadonnées disponibles ; le manifeste calcule ensuite l’empreinte.
- **Refus :** un nom déjà présent ne doit pas être écrasé silencieusement dans une génération immuable.
- **Retour :** la fonction renvoie le `Path` de destination ou lève une exception sans promouvoir la génération.

## 18. Sauvegarder SQLite de manière cohérente

Copier un fichier SQLite actif peut produire une sauvegarde incohérente, notamment si le mode WAL utilise des sidecars encore nécessaires. Deux voies sont acceptables : fermer proprement l’application et copier un ensemble qualifié, ou utiliser l’API de sauvegarde/outil SQLite qui construit une image cohérente.

## 18.1. Utiliser la commande `.backup`

> **[WSL] Créer une sauvegarde SQLite cohérente — Adapter les chemins et vérifier l’outil.**

```bash
set -euo pipefail
source_db="${1:?base source manquante}"
backup_db="${2:?base de sauvegarde manquante}"

if [ -e "$backup_db" ]; then
  echo "la destination existe déjà" >&2
  exit 64
fi

sqlite3 "$source_db" ".timeout 5000" ".backup '$backup_db'"
sqlite3 "$backup_db" "PRAGMA quick_check;"
sha256sum "$backup_db"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres positionnels :** `${1:?...}` et `${2:?...}` refusent une valeur absente.
- **Destination :** l’existence préalable bloque l’écrasement d’une génération.
- **`.backup` :** demande à SQLite de produire une copie cohérente de la base ouverte.
- **`quick_check` :** exécute un contrôle d’intégrité rapide sur la copie, pas sur la source.
- **`sha256sum` :** fournit l’empreinte de la sauvegarde à inscrire dans son manifeste.
- **Limite :** un contrôle réussi ne prouve pas que les données métier attendues sont présentes ; la restauration doit tester les invariants applicatifs.

## 18.2. Restaurer SQLite dans un dossier isolé

> **[PS] Restaurer et contrôler une copie SQLite — Adapter les chemins.**

```powershell
param(
    [Parameter(Mandatory)] [string]$Backup,
    [Parameter(Mandatory)] [string]$RestoreDirectory
)

$ErrorActionPreference = "Stop"
$TargetRoot = [System.IO.Path]::GetFullPath($RestoreDirectory)
if (Test-Path $TargetRoot) { throw "le dossier de restauration doit être neuf" }
New-Item -ItemType Directory -Path $TargetRoot | Out-Null

$Target = Join-Path $TargetRoot "asteria-restored.sqlite3"
Copy-Item -LiteralPath $Backup -Destination $Target
sqlite3 $Target "PRAGMA quick_check; PRAGMA foreign_key_check;"
if ($LASTEXITCODE -ne 0) { throw "contrôle SQLite échoué" }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** la sauvegarde et le dossier neuf sont obligatoires.
- **Confinement :** `GetFullPath` normalise la cible ; un dossier existant est refusé pour éviter la contamination par des fichiers résiduels.
- **Contrôles :** `quick_check` examine la structure et `foreign_key_check` recherche des violations référentielles déclarées.
- **Code de retour :** un échec SQLite bloque la suite avant toute connexion de l’application.
- **Limite :** l’application doit encore ouvrir la base, lire des objets représentatifs et effectuer une écriture contrôlée.

## 19. Sauvegarder PostgreSQL par export logique

Lorsqu’un service utilise PostgreSQL, `pg_dump` produit une sauvegarde logique d’une base. Le format personnalisé permet une restauration sélective avec `pg_restore`. Les rôles globaux, tablespaces et paramètres d’instance demandent une politique distincte ; un dump d’une base ne capture pas tout le cluster.

## 19.1. Produire un dump personnalisé

> **[DCT] Terminal dans le conteneur d’administration PostgreSQL — Adapter les variables non secrètes.**

```bash
set -euo pipefail
: "${PGHOST:?PGHOST manquant}"
: "${PGDATABASE:?PGDATABASE manquant}"
: "${BACKUP_FILE:?BACKUP_FILE manquant}"

pg_dump \
  --format=custom \
  --no-owner \
  --no-privileges \
  --file="$BACKUP_FILE" \
  "$PGDATABASE"

pg_restore --list "$BACKUP_FILE" > "${BACKUP_FILE}.list"
sha256sum "$BACKUP_FILE" "${BACKUP_FILE}.list"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variables :** `PGHOST`, `PGDATABASE` et `BACKUP_FILE` doivent exister ; le mot de passe vient d’un canal secret et n’est pas imprimé.
- **`--format=custom` :** crée une archive consommable par `pg_restore`.
- **Propriété :** `--no-owner` et `--no-privileges` facilitent une restauration dans un environnement isolé avec des rôles préparés séparément.
- **Liste :** `pg_restore --list` produit un inventaire consultable sans restaurer.
- **Limite de confiance :** un dump provenant d’un superutilisateur non fiable peut contenir des commandes dangereuses ; il doit être inspecté avant exécution.

## 19.2. Restaurer dans une base neuve

> **[DCT] Terminal dans le conteneur de restauration PostgreSQL — Ne jamais viser la production.**

```bash
set -euo pipefail
: "${RESTORE_DB:?RESTORE_DB manquant}"
: "${BACKUP_FILE:?BACKUP_FILE manquant}"

createdb --template=template0 "$RESTORE_DB"
pg_restore \
  --exit-on-error \
  --no-owner \
  --no-privileges \
  --dbname="$RESTORE_DB" \
  "$BACKUP_FILE"

psql --dbname="$RESTORE_DB" --command="SELECT 1;"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base neuve :** `template0` limite les objets hérités du modèle local.
- **`--exit-on-error` :** arrête la restauration au premier échec au lieu de poursuivre avec un état partiel.
- **Propriété et privilèges :** les rôles de l’environnement cible sont appliqués par une étape gouvernée séparée.
- **Postcondition minimale :** `SELECT 1` confirme la connexion, mais pas la cohérence métier.
- **Sécurité :** l’environnement reste isolé jusqu’aux contrôles applicatifs et à la revue du contenu du dump.

## 20. Sauvegarder services et volumes de conteneur

Une image de conteneur n’est pas la sauvegarde de ses données. L’image doit être reconstructible depuis une source et un manifeste ; les volumes persistants demandent une sauvegarde cohérente propre au moteur de données. Copier aveuglément un volume monté et actif peut produire un état inutilisable.

## 20.1. Inspecter les volumes dans Docker Desktop

> **[DCK] Docker Desktop — Inspecter les volumes sans les supprimer.**

```text
Docker Desktop
  → Volumes
  → sélectionner le volume du service isolé
  → relever nom, taille, conteneurs utilisateurs et point de montage logique
  → vérifier que la procédure de sauvegarde appartient au moteur de données
  → ne pas utiliser Delete pendant l’inventaire
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** cette procédure s’effectue dans Docker Desktop, pas dans un terminal.
- **Inventaire :** le nom du volume ne suffit pas ; il faut connaître le service, le moteur et la cohérence requise.
- **Interdiction :** supprimer un volume pendant l’inventaire détruit la source au lieu de la sauvegarder.
- **Frontière :** PostgreSQL ou SQLite fournissent leurs propres mécanismes cohérents ; la copie de volume reste une option physique qualifiée séparément.

## 20.2. Lire le montage d’un conteneur

> **[DCT] Terminal dans un conteneur de diagnostic non privilégié — Adapter le chemin attendu.**

```bash
set -euo pipefail
mount | grep --fixed-strings "/var/lib/asteria"
df -h /var/lib/asteria
find /var/lib/asteria -maxdepth 1 -mindepth 1 -printf '%f\n' | sort
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`mount` :** confirme le point de montage réellement visible par le conteneur.
- **`df -h` :** renseigne support et capacité sans constituer une mesure de données sauvegardées.
- **`find` :** limite la profondeur à un niveau et affiche uniquement les noms ; aucun contenu sensible n’est copié dans les logs.
- **Privilèges :** le diagnostic s’exécute sans `--privileged` et sans accès en écriture non nécessaire.

## 21. Sauvegarder configurations et secrets

Les configurations non sensibles peuvent être versionnées. Les secrets restent dans un gestionnaire dédié et possèdent une procédure de récupération distincte : identités d’urgence, approbation, rotation, révocation et journalisation. Une archive chiffrée de secrets ne doit pas dépendre de l’unique clé stockée dans le même emplacement.

> **[LECTURE] Registre de récupération des secrets — Ne jamais inscrire les valeurs réelles.**

```yaml
secret_recovery:
  signing-key:
    owner: release-security
    storage: managed-key-service
    recovery_approvals: 2
    rotation_after_restore: required
    plaintext_backup: forbidden
  database-credential:
    owner: operations
    storage: secret-manager
    recovery_approvals: 1
    revoke_previous_after_restore: required
    plaintext_backup: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Noms logiques :** le registre décrit la capacité de récupération sans exposer de valeur.
- **Approbations :** le nombre reflète le risque ; la politique Studio peut imposer une séparation des rôles.
- **Rotation :** une restauration après compromission ne réactive pas aveuglément les anciens credentials.
- **Dépendance :** la procédure d’urgence doit rester accessible même si le dépôt principal est indisponible.

## 22. Chiffrer sans perdre la capacité de reprise

Le chiffrement protège la confidentialité, pas l’intégrité complète ni la disponibilité. La clé, son historique, sa rotation et sa récupération deviennent eux-mêmes des actifs critiques. Un fichier chiffré dont personne ne peut récupérer la clé est une perte de données.

> **[PS] Chiffrer une archive avec un outil qualifié — Exemple conceptuel à adapter.**

```powershell
param(
    [Parameter(Mandatory)] [string]$Archive,
    [Parameter(Mandatory)] [string]$Recipient
)

$ErrorActionPreference = "Stop"
age --recipient $Recipient --output "$Archive.age" $Archive
if ($LASTEXITCODE -ne 0) { throw "chiffrement échoué" }

Get-FileHash -Algorithm SHA256 -Path "$Archive.age"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Outil :** `age` n’est adopté qu’après qualification, installation, licence, version et procédure de récupération documentées.
- **`Recipient` :** identifiant public du destinataire ; aucune clé privée n’est passée sur la ligne de commande.
- **Code de retour :** un échec bloque la promotion de la génération.
- **Empreinte :** elle vise l’archive chiffrée réellement stockée.
- **Limite :** le chapitre ne revendique ni installation de l’outil ni génération d’une clé réelle.

## 23. Automatiser sans masquer l’échec

Le job de sauvegarde prépare une génération dans un staging, copie ou exporte les sources, construit le manifeste, vérifie l’ensemble, chiffre si nécessaire, transfère vers les destinations, puis marque la génération `verified`. Un échec laisse un statut explicite et ne remplace jamais la dernière génération valide.

## 23.1. Machine d’états d’une génération

> **[LECTURE] États d’une génération — Adapter les codes de raison.**

```yaml
backup_generation_state:
  allowed:
    - planned
    - collecting
    - manifesting
    - verifying
    - transferring
    - verified
    - failed
    - quarantined
    - expired
  terminal_for_attempt:
    - verified
    - failed
    - quarantined
  forbidden_transitions:
    - failed_to_verified_without_new_attempt
    - quarantined_to_verified_without_review
    - expired_to_collecting
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** collecte, vérification et transfert restent observables séparément.
- **Tentatives :** un retry reçoit une nouvelle identité plutôt que de réécrire l’échec précédent.
- **Quarantaine :** une empreinte divergente ou une source suspecte bloque l’utilisation sans supprimer la preuve.
- **Expiration :** la génération expirée n’est pas réactivée ; une nouvelle génération est créée.

## 23.2. Orchestrer une tentative en Python

> **[VSC] Créer `tools/continuity/run_backup.py` — Adapter les ports de stockage.**

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


class BackupCollector(Protocol):
    def collect(self, staging: Path) -> None: ...


class BackupPublisher(Protocol):
    def publish(self, staging: Path, generation_id: str) -> None: ...


@dataclass(frozen=True)
class BackupJob:
    generation_id: str
    staging: Path
    collector: BackupCollector
    publisher: BackupPublisher

    def run(self) -> None:
        if self.staging.exists():
            raise FileExistsError(self.staging)
        self.staging.mkdir(parents=True)
        self.collector.collect(self.staging)
        self.publisher.publish(self.staging, self.generation_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Protocols :** `BackupCollector` et `BackupPublisher` définissent des ports testables sans imposer un fournisseur.
- **`BackupJob` :** dataclass immuable regroupant identité, staging et dépendances injectées.
- **Précondition :** un staging existant est refusé afin d’éviter les restes d’une tentative précédente.
- **Effets de bord :** `mkdir`, collecte et publication écrivent sur le stockage ; leurs erreurs remontent à l’appelant.
- **Limite :** un vrai publisher doit vérifier manifeste, chiffrement, transfert et confirmation de destination avant succès.

## 24. Observer les jobs de sauvegarde

Une métrique ou un tableau de bord n’est pas la sauvegarde. Il indique fraîcheur, durée, volume, taux d’échec, dernière génération vérifiée et prochain exercice. Les dimensions restent de faible cardinalité et ne contiennent ni chemin personnel, ni identifiant joueur, ni nom libre.

> **[LECTURE] Catalogue de métriques — Adapter les familles.**

```yaml
backup_metrics:
  generation_age_seconds:
    labels: [asset_family, destination_family]
  attempt_duration_seconds:
    labels: [asset_family, conclusion]
  attempt_total:
    labels: [asset_family, conclusion, reason_family]
  bytes_written:
    labels: [asset_family, destination_family]
  restore_drill_age_seconds:
    labels: [scenario_family]
forbidden_labels:
  - player_id
  - absolute_path
  - generation_id
  - free_text_error
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fraîcheur :** l’âge de la dernière génération vérifiée est plus utile qu’un simple « dernier job lancé ».
- **Labels :** seules des familles stables deviennent dimensions ; les identifiants exacts restent dans les rapports.
- **Volume :** les octets aident à piloter rétention et coût sans autoriser une suppression automatique.
- **Autorité :** aucune métrique ne transforme une génération non restaurée en preuve de continuité.

## 25. Préparer une restauration isolée

Une restauration ne cible jamais directement la production au premier essai. Elle utilise un réseau, des identités, des chemins et une base isolés. Les sorties sont vérifiées avant toute admission de trafic ou remplacement de données actives.

## 25.1. Runbook de restauration

> **[VSC] Créer `docs/continuity/runbooks/restore-environment.md` — Adapter les propriétaires.**

```markdown
# Restauration d’un environnement Asteria

1. Ouvrir l’incident et attribuer le commandement.
2. Geler les écritures ou isoler la source compromise.
3. Choisir une génération selon heure, intégrité et compatibilité.
4. Vérifier manifeste, empreintes, rétention et chaîne de confiance.
5. Créer réseau, stockage et identités isolés.
6. Restaurer selon le graphe de dépendances.
7. Exécuter contrôles structurels et métier.
8. Mesurer point récupéré et temps de service minimal.
9. Obtenir la décision humaine de promotion.
10. Réadmettre progressivement les clients.
11. Conserver rapports, écarts et actions correctives.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gel :** empêche que de nouvelles écritures aggravent la divergence pendant le diagnostic.
- **Sélection :** la génération la plus récente n’est pas automatiquement la meilleure si elle contient la corruption.
- **Isolement :** la preuve est produite sans écraser l’environnement encore utile à l’enquête.
- **Promotion :** une personne autorisée compare les critères avant bascule.
- **Post-incident :** les écarts RPO/RTO et les corrections restent traçables.

## 25.2. Vérifier depuis l’interface GitHub

> **[APP] GitHub — Vérifier le commit et les artefacts d’une génération liée à un build.**

```text
Dépôt GitHub
  → Actions
  → run identifié dans le manifeste
  → commit et tentative
  → artefacts
  → comparer nom, taille, digest et expiration
  → ne pas télécharger depuis un run différent
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** la procédure utilise l’interface GitHub.
- **Corrélation :** run, commit et tentative doivent correspondre au manifeste de la génération.
- **Expiration :** un artefact expiré ne peut pas être présenté comme copie disponible.
- **Limite :** un artefact GitHub ne remplace pas la copie hors site ni l’archive durable.

## 25.3. Consulter la documentation officielle

> **[WEB] Navigateur — Vérifier les procédures des moteurs avant matérialisation.**

```text
1. Ouvrir la documentation officielle du moteur et de sa version.
2. Vérifier la méthode de sauvegarde cohérente.
3. Vérifier les préconditions de restauration.
4. Relever les avertissements de sécurité.
5. Enregistrer la page nommée et la date de revue dans le runbook.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la documentation officielle prévaut sur un tutoriel générique pour les options du moteur.
- **Version :** une procédure PostgreSQL ou Godot doit être vérifiée contre la version réellement déployée.
- **Sécurité :** les avertissements sur code restauré, privilèges et données non fiables sont conservés.
- **Traçabilité :** la date de revue permet de requalifier la procédure après une mise à jour.

## 26. Vérifier la restauration fonctionnelle

Une base qui s’ouvre n’est pas nécessairement utilisable. La campagne vérifie :

- versions et schémas attendus ;
- nombre et identité d’objets représentatifs ;
- contraintes référentielles ;
- lecture puis écriture contrôlée ;
- compatibilité du build ;
- absence de fichiers inattendus ;
- journaux sans erreur critique ;
- secrets renouvelés lorsque l’incident l’exige ;
- observabilité disponible ;
- réadmission graduelle.

> **[LECTURE] Porte de restauration — Adapter les oracles.**

```yaml
restore_gate:
  manifest_verified: required
  schema_supported: required
  structural_checks: passed
  representative_reads: passed
  controlled_write: passed
  application_start: passed
  critical_logs: zero
  secrets_rotated_when_required: passed
  measured_rpo_recorded: required
  measured_rto_recorded: required
  human_approval: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrôles :** structure, lecture, écriture et démarrage sont des preuves distinctes.
- **Secrets :** la rotation dépend du scénario ; elle devient obligatoire après exposition ou doute raisonnable.
- **Mesures :** même un échec conserve le RPO et le RTO observés.
- **Approbation :** la porte humaine vérifie risques résiduels et plan de retour avant promotion.

## 26.1. Reconnaître une sortie de campagne

> **[SORTIE] Exemple de résumé de restauration — Ne pas saisir.**

```text
scenario=sqlite-host-loss
generation=AST-BACKUP-20260727-001
manifest=verified
restore_environment=isolated
structural_checks=passed
representative_reads=passed
controlled_write=passed
observed_rpo_seconds=840
observed_rto_seconds=3120
production_promoted=false
runtime_claimed=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénario :** identifie la famille d’incident exercée.
- **Mesures :** `840` et `3120` sont des exemples de format, pas des résultats de `Project Asteria`.
- **Promotion :** `false` rappelle que l’environnement isolé n’a pas remplacé la production.
- **Honnêteté :** `runtime_claimed=false` empêche de présenter cette sortie illustrative comme une preuve exécutée.

## 27. Versionner les migrations

Une migration est immuable après application. Elle possède identifiant, version source, version cible, préconditions, transformation, validation, stratégie de reprise et empreinte. Une correction crée une nouvelle migration au lieu de réécrire l’historique.

> **[VSC] Créer `data/migrations/registry.yaml` — Adapter les versions réelles.**

```yaml
migrations:
  - id: AST-MIGRATION-SAVE-0009-0010
    source_version: 9
    target_version: 10
    applies_to: player-save
    reversible: false
    preflight:
      - source-schema-valid
      - identifiers-known
      - backup-generation-verified
    postflight:
      - target-schema-valid
      - semantic-invariants-valid
      - roundtrip-save-valid
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** stable et indépendant du nom de fichier.
- **Versions :** la migration accepte exactement une version source et produit une version cible.
- **`reversible` :** `false` interdit de promettre un downgrade automatique ; le retour passe par une sauvegarde antérieure compatible.
- **Préflight :** aucune mutation ne commence sans sauvegarde vérifiée et format source reconnu.
- **Postflight :** validation de structure, invariants métier et réécriture contrôlée sont séparées.

## 27.1. Préparer sans muter l’état actif

> **[VSC] Créer `tools/continuity/migrate_document.py` — Adapter les validateurs métier.**

```python
from __future__ import annotations

from copy import deepcopy
from typing import Callable

JsonObject = dict[str, object]
Validator = Callable[[JsonObject], None]
Transformer = Callable[[JsonObject], JsonObject]


def prepare_migration(
    source: JsonObject,
    expected_version: int,
    target_version: int,
    transform: Transformer,
    validate_target: Validator,
) -> JsonObject:
    if source.get("version") != expected_version:
        raise ValueError("version source inattendue")
    candidate = transform(deepcopy(source))
    candidate["version"] = target_version
    validate_target(candidate)
    return candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Alias :** `JsonObject`, `Validator` et `Transformer` rendent les contrats d’entrée explicites.
- **Paramètres :** versions source/cible et fonctions de transformation/validation sont injectées.
- **`deepcopy` :** protège le document actif contre une mutation partielle.
- **Retour :** la fonction renvoie un candidat validé ; elle n’écrit aucun fichier.
- **Refus :** une version inattendue ou un invariant cible invalide lève `ValueError` avant remplacement.

## 28. Utiliser une stratégie expand/contract pour les services

Pour une base partagée par plusieurs versions applicatives, une migration risquée peut être découpée :

1. **expand** : ajouter les nouvelles structures compatibles ;
2. déployer du code lisant ancien et nouveau format ;
3. migrer ou recalculer progressivement ;
4. vérifier adoption et cohérence ;
5. **contract** : retirer l’ancien format après la fenêtre de retour.

Cette stratégie réduit le couplage entre migration et déploiement, mais augmente temporairement la complexité. Elle ne convient pas automatiquement à un slot joueur local ; le contexte décide.

> **[LECTURE] États d’une migration de service — Adapter les portes.**

```yaml
migration_rollout:
  expand:
    old_read_supported: true
    old_write_supported: true
    new_read_supported: true
  transition:
    dual_read_check: required
    backfill: resumable
    progress_checkpointed: true
  contract:
    old_write_supported: false
    old_read_supported: false
    requires:
      - rollback-window-closed
      - restored-backup-tested
      - compatibility-matrix-approved
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Compatibilité :** les booléens rendent visible ce que chaque phase accepte.
- **Backfill :** `resumable` impose checkpoints et idempotence pour les longues transformations.
- **Contract :** la suppression de l’ancien format attend la fermeture de la fenêtre de rollback.
- **Preuve :** une sauvegarde restaurée et une matrice approuvée précèdent la destruction de compatibilité.

## 29. Distinguer rollback applicatif et restauration de données

Revenir à un ancien binaire peut échouer si la base ou les sauvegardes ont déjà migré vers un format futur. Inversement, restaurer une base ancienne sous un binaire récent peut relancer des migrations ou perdre des écritures récentes.

> **[LECTURE] Matrice de décision — Adapter les versions supportées.**

```yaml
rollback_matrix:
  app_v15_with_data_v15: supported
  app_v14_with_data_v15: forbidden
  app_v15_with_data_v14: migrate-forward-required
  app_v14_with_backup_v14: isolated-restore-candidate
  mixed_service_versions:
    status: conditional
    requires: compatibility-contract
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paires :** la compatibilité dépend du couple application/données, pas de la version applicative seule.
- **`forbidden` :** empêche un rollback qui interpréterait un schéma futur avec un ancien code.
- **Migration avant usage :** les données anciennes sont préparées et validées avant admission.
- **Services mixtes :** ils demandent un contrat explicite, généralement limité à une fenêtre de déploiement.

## 30. Préparer les scénarios catastrophe

Les exercices couvrent des causes différentes, car une seule procédure ne répond pas à tout :

- perte totale d’un poste ;
- suppression accidentelle d’un dossier ;
- corruption silencieuse découverte tardivement ;
- base SQLite active copiée incorrectement ;
- migration partiellement appliquée ;
- perte du volume d’un service ;
- compromission d’un compte administrateur ;
- suppression de sauvegardes accessibles au même compte ;
- rançongiciel chiffrant production et copies montées ;
- indisponibilité d’un fournisseur ;
- publication d’un build incompatible avec les données ;
- perte d’une clé ou d’un secret indispensable.

## 30.1. Fiche de scénario

> **[VSC] Créer `docs/continuity/scenarios/host-loss.yaml` — Adapter les acteurs et critères.**

```yaml
scenario:
  id: AST-DR-HOST-LOSS-001
  title: perte-totale-hote-service
  assumptions:
    - production-host-unavailable
    - offsite-backup-available
    - primary-credentials-revoked
  objectives:
    - restore-isolated-service
    - validate-database
    - rotate-credentials
    - measure-rpo-rto
  stop_conditions:
    - manifest-invalid
    - backup-generation-untrusted
    - unexpected-external-traffic
  evidence:
    - timeline
    - commands-redacted
    - manifests
    - test-results
    - decision-log
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hypothèses :** fixent le périmètre sans fabriquer de panne réelle.
- **Objectifs :** chaque résultat est observable et relié à une preuve.
- **Conditions d’arrêt :** empêchent de poursuivre avec une sauvegarde suspecte ou un environnement non isolé.
- **Preuves :** les commandes sont expurgées et les décisions humaines restent associées à la chronologie.

## 31. Réagir à une compromission ou un rançongiciel

Après compromission, la priorité n’est pas de reconnecter rapidement la dernière copie. Il faut isoler, préserver les preuves, choisir une génération antérieure au point de compromission, reconstruire des identités propres, révoquer les anciennes et restaurer dans un environnement contrôlé.

Une sauvegarde accessible en écriture permanente depuis la production peut être chiffrée ou supprimée par le même attaquant. Les copies déconnectées ou immuables réduisent ce risque, sans empêcher une fuite si leur contenu reste lisible par un compte compromis.

> **[LECTURE] Séquence de reprise après compromission — Adapter au plan de sécurité.**

```yaml
compromise_recovery:
  - isolate-affected-systems
  - preserve-forensic-evidence
  - revoke-compromised-identities
  - identify-clean-recovery-point
  - verify-immutable-generation
  - rebuild-isolated-environment
  - rotate-all-dependent-secrets
  - restore-and-validate
  - monitor-before-admission
  - document-residual-risk
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** la révocation et l’identification d’un point propre précèdent la réouverture.
- **Preuves :** l’environnement compromis n’est pas détruit avant décision de conservation forensique.
- **Secrets dépendants :** clés et jetons liés à l’identité compromise sont renouvelés.
- **Risque résiduel :** une restauration réussie ne prouve pas que la cause initiale est corrigée.

## 32. Organiser le commandement d’incident

Même en Mode Solo, les responsabilités doivent être nommées : décision, exécution, vérification, communication et conservation des preuves. En Studio, elles sont séparées pour éviter qu’une seule personne choisisse la sauvegarde, la restaure et approuve sa promotion sans revue.

> **[LECTURE] Rôles de reprise — Adapter à l’équipe.**

```yaml
recovery_roles:
  incident_commander:
    owns: [priorities, go-no-go, communication]
  recovery_operator:
    owns: [restore-execution, command-log]
  data_owner:
    owns: [semantic-validation, acceptable-loss]
  security_reviewer:
    owns: [isolation, credentials, compromise-risk]
  observer:
    owns: [timeline, evidence, rpo-rto-measurement]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Commandement :** tranche les priorités sans exécuter nécessairement chaque commande.
- **Propriétaire des données :** décide si la perte observée reste acceptable au regard du métier.
- **Sécurité :** vérifie isolation et identités avant réadmission.
- **Observateur :** mesure et conserve la preuve, ce qui limite les reconstructions rétrospectives imprécises.

## 33. Mode Solo et Mode Studio

### Mode Solo

Le développeur Solo privilégie une politique compréhensible et testable :

- dépôt distant plus bundle périodique hors du poste principal ;
- copie locale rapide et copie hors site chiffrée ;
- sauvegardes joueurs versionnées avant migration ;
- inventaire court mais complet ;
- calendrier mensuel de restauration d’un actif tournant ;
- secrets récupérables par une procédure hors dépôt ;
- budget de stockage en euros et alerte de dépassement ;
- runbook imprimable ou disponible hors ligne.

La simplicité est une exigence de sécurité : une procédure trop complexe pour être exercée sera probablement inutilisable pendant l’incident.

### Mode Studio

Le Studio ajoute :

- propriétaires et niveaux de criticité par actif ;
- comptes de sauvegarde séparés des comptes de production ;
- stockage hors site et immuable ;
- chiffrement et gestion de clés gouvernée ;
- catalogues centralisés et preuves append-only ;
- restaurations automatiques périodiques dans des environnements éphémères ;
- exercices multi-équipes avec observateur ;
- objectifs RPO/RTO par service ;
- revue de capacité et de coût ;
- procédures de crise, communication et escalade ;
- audit des suppressions et dérogations ;
- tests de sortie du fournisseur.

## 34. Planifier les exercices

Une politique sans exercice se dégrade silencieusement. Le calendrier varie les actifs et scénarios afin de ne pas tester toujours le même chemin heureux.

> **[LECTURE] Calendrier candidat d’exercices — Adapter aux ressources.**

```yaml
restore_drills:
  monthly:
    - one-player-save
    - one-source-bundle
  quarterly:
    - sqlite-database
    - retained-build-and-manifest
  semiannual:
    - isolated-service-environment
    - credential-recovery
  annual:
    - cross-provider-disaster-scenario
    - full-continuity-tabletop
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rotation :** les actifs changent afin de détecter des procédures oubliées.
- **Fréquences :** ce sont des candidats ; criticité et coût peuvent exiger un rythme différent.
- **Tabletop :** l’exercice sur table vérifie décisions et communication mais ne remplace pas la restauration technique.
- **Preuve :** chaque campagne produit un rapport, des mesures et des actions correctives avec propriétaire.

## 35. Gérer les écarts et actions correctives

Un exercice peut réussir tout en dépassant l’objectif. Le rapport distingue : résultat fonctionnel, RPO observé, RTO observé, écarts, cause probable, action corrective, propriétaire et échéance. Une mesure défavorable n’est jamais supprimée pour préserver un tableau vert.

> **[LECTURE] Registre d’écart — Adapter les codes et échéances.**

```yaml
recovery_gap:
  id: AST-RECOVERY-GAP-001
  scenario: AST-DR-HOST-LOSS-001
  status: open
  observed_rto_seconds: 7200
  target_rto_seconds: 3600
  gap_seconds: 3600
  reason_family: dependency-download-delay
  corrective_action: qualify-offline-tool-cache
  owner: operations
  due_date: 2026-09-01
  retest_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mesures :** cible, observation et différence restent séparées.
- **`gap_seconds` :** `7200 - 3600 = 3600`; le calcul positif rend visible le dépassement.
- **Cause :** une famille stable est utilisée ; le diagnostic détaillé reste dans le rapport.
- **Retest :** l’action n’est pas close au commit de correction, mais après nouvel exercice.

## 36. Respecter confidentialité, retrait et conservation

Les sauvegardes peuvent contenir données personnelles, communications, adresses réseau ou identifiants. La rétention doit être compatible avec la finalité, les obligations applicables, les demandes de retrait et les éventuels gels juridiques. Une suppression logique de production ne retire pas automatiquement toutes les générations historiques.

La procédure documente :

- quelles données peuvent apparaître ;
- pourquoi elles sont sauvegardées ;
- qui peut les restaurer ;
- combien de temps elles sont conservées ;
- comment une demande de suppression est propagée lorsque nécessaire ;
- comment un gel juridique suspend une purge ;
- comment les rapports sont expurgés avant partage.

## 37. Critère d’acceptation documentaire

Le chapitre passe au niveau `static-review` lorsque :

1. son périmètre correspond au plan maître ;
2. inventaire, RPO, RTO, rétention et dépendances sont explicites ;
3. sauvegarde, réplication, snapshot et archive sont distingués ;
4. sources, builds, bases, services, secrets et données joueurs sont couverts ;
5. chaque bloc significatif possède un repère et une explication ;
6. les migrations sont versionnées, préparées et validées avant mutation ;
7. les diagnostics suivent la séquence sémantique complète ;
8. les références officielles sont cliquables ;
9. les documents de gouvernance sont mis à jour ;
10. aucun PDF ni résultat runtime n’est revendiqué.

La validation finale du plan maître — restauration réelle d’un environnement isolé — reste une réserve runtime tant que sauvegardes, outils, clés, bases, services et exercices de `Project Asteria` ne sont pas matérialisés.

## 38. Checklist opérationnelle

Avant de déclarer la politique prête :

- actifs critiques inventoriés ;
- autorités et données dérivées distinguées ;
- propriétaires nommés ;
- RPO/RTO candidats approuvés ;
- générations et rétention définies ;
- au moins deux pannes indépendantes couvertes ;
- comptes de sauvegarde séparés ;
- chiffrement et récupération de clés préparés ;
- manifestes et empreintes produits ;
- bases sauvegardées par méthode cohérente ;
- ordre de restauration documenté ;
- environnement isolé disponible ;
- migrations immuables et préflight défini ;
- compatibilité application/données enregistrée ;
- exercices planifiés ;
- preuves, écarts et retests gouvernés ;
- aucune génération valide supprimée avant remplacement vérifié.

## 39. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 39.1 Confondre synchronisation et sauvegarde

**Symptôme ou risque :** Une suppression locale est immédiatement propagée à la seule copie distante.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
protection:
  folder_sync: enabled
  version_history: disabled
  independent_backup: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la synchronisation reproduit l’état courant, y compris suppression ou chiffrement, sans génération indépendante.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter à la politique réelle.**

```yaml
protection:
  folder_sync: enabled
  independent_backup: true
  version_history: enabled
  immutable_generation: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la synchronisation reste un confort tandis que générations versionnées et copie immuable fournissent des points de reprise distincts.

### 39.2 Copier une base SQLite active

**Symptôme ou risque :** Le fichier principal est copié sans les écritures encore présentes dans le WAL.

**Exemple fautif :**

> **[PS] Exemple fautif — Ne pas appliquer.**

```powershell
Copy-Item .\runtime\asteria.sqlite3 D:\Backup\asteria.sqlite3
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** une copie brute ne garantit pas une image cohérente lorsque la base est ouverte ou dépend de sidecars actifs.

**Exemple corrigé :**

> **[WSL] Exemple corrigé — Adapter les chemins.**

```bash
sqlite3 runtime/asteria.sqlite3 ".backup 'backup/asteria.sqlite3'"
sqlite3 backup/asteria.sqlite3 "PRAGMA quick_check;"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** SQLite construit la copie cohérente puis le contrôle s’exécute sur la sauvegarde produite.

### 39.3 Sauvegarder uniquement les caches

**Symptôme ou risque :** La copie volumineuse ne contient ni sources, ni manifestes, ni données autoritaires.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
backup_paths:
  - .godot/
  - .cache/
  - derived-vector-index/
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** ces chemins sont reconstructibles et ne permettent pas de recréer les sources canoniques absentes.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter l’inventaire.**

```yaml
backup_assets:
  canonical:
    - source-repository
    - source-art
    - player-state
    - legal-register
  derived:
    rebuild_only:
      - .godot/
      - derived-vector-index/
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les autorités sont protégées et les caches restent liés à une procédure de reconstruction.

### 39.4 Écraser la dernière génération valide

**Symptôme ou risque :** Une tentative incomplète remplace la seule copie restaurable.

**Exemple fautif :**

> **[PS] Exemple fautif — Ne pas appliquer.**

```powershell
Copy-Item .\staging\* D:\Backup\latest\ -Recurse -Force
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `-Force` écrase la génération précédente avant manifeste, vérification et promotion.

**Exemple corrigé :**

> **[PS] Exemple corrigé — Adapter l’identifiant.**

```powershell
$Generation = "AST-BACKUP-20260727-001"
Copy-Item .\staging "D:\Backup\generations\$Generation" -Recurse
python tools/continuity/verify_backup_manifest.py `
  "D:\Backup\generations\$Generation" `
  "D:\Backup\generations\$Generation\manifest.json"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** une nouvelle génération est créée et vérifiée sans détruire la dernière génération connue comme valide.

### 39.5 Définir RPO et RTO sans service minimal

**Symptôme ou risque :** L’équipe annonce « une heure » sans savoir ce qui doit fonctionner à cette échéance.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
rpo: low
rto: 1h
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `low` n’est pas mesurable et le RTO ne définit aucun état de service observable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter à l’actif.**

```yaml
player_service:
  target_rpo_seconds: 900
  target_rto_seconds: 3600
  minimum_service:
    - authentication-available
    - save-load-roundtrip-passed
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les objectifs sont mesurables et reliés à deux oracles fonctionnels précis.

### 39.6 Restaurer directement en production

**Symptôme ou risque :** Une sauvegarde corrompue ou incompatible écrase l’état encore analysable.

**Exemple fautif :**

> **[DCT] Exemple fautif — Ne pas appliquer.**

```bash
pg_restore --clean --dbname=asteria_production latest.dump
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la commande cible directement la production et peut supprimer des objets avant validation de l’archive.

**Exemple corrigé :**

> **[DCT] Exemple corrigé — Adapter le nom isolé.**

```bash
createdb --template=template0 asteria_restore_test
pg_restore --exit-on-error --dbname=asteria_restore_test latest.dump
psql --dbname=asteria_restore_test --command="SELECT 1;"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la restauration s’effectue dans une base neuve et isolée avant contrôles métier et décision de promotion.

### 39.7 Modifier une migration déjà appliquée

**Symptôme ou risque :** Deux environnements portant le même identifiant de migration obtiennent des transformations différentes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
migration_id: AST-MIGRATION-001
checksum: replace-in-place-after-production
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** l’historique devient ambigu et la preuve d’application ne correspond plus aux octets exécutés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Créer une nouvelle migration.**

```yaml
migrations:
  - id: AST-MIGRATION-001
    status: immutable-applied
  - id: AST-MIGRATION-002
    purpose: correct-previous-transformation
    depends_on: AST-MIGRATION-001
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la correction possède une nouvelle identité et conserve la transformation historiquement appliquée.

### 39.8 Conserver la clé avec l’unique archive chiffrée

**Symptôme ou risque :** La perte du support supprime simultanément données et moyen de déchiffrement.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
backup_drive:
  encrypted_archive: true
  private_key_location: same-drive
  second_recovery_identity: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la panne du support détruit la copie et son seul mécanisme de récupération.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter la gouvernance des clés.**

```yaml
key_recovery:
  encrypted_archive_location: offsite-backup
  private_key_location: managed-key-service
  emergency_recovery: separately-controlled
  recovery_test: scheduled
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** archive, clé privée et identité d’urgence ont des pannes et contrôles distincts, puis la récupération est exercée.

### 39.9 Déclarer une restauration réussie après `SELECT 1`

**Symptôme ou risque :** La base répond, mais les données métier, contraintes ou écritures sont inutilisables.

**Exemple fautif :**

> **[DCT] Exemple fautif — Ne pas appliquer.**

```bash
psql --dbname=asteria_restore --command="SELECT 1;"
echo "restauration réussie"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le test valide seulement la connexion et ne vérifie ni schéma, ni contenu, ni écriture applicative.

**Exemple corrigé :**

> **[DCT] Exemple corrigé — Adapter les oracles métier.**

```bash
psql --dbname=asteria_restore --file=checks/structural.sql
python tools/continuity/check_representative_records.py --database asteria_restore
python tools/continuity/run_save_load_roundtrip.py --environment isolated
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** structure, enregistrements représentatifs et aller-retour applicatif fournissent des preuves complémentaires.

### 39.10 Revenir à un ancien binaire avec des données futures

**Symptôme ou risque :** L’ancien code interprète mal le schéma migré et aggrave la corruption.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
rollback:
  application: v14
  data_schema: v15
  compatibility_check: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la compatibilité application/données est inconnue et aucun point de restauration cohérent n’est sélectionné.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter la matrice approuvée.**

```yaml
rollback:
  application: v14
  data_source: verified-backup-v14
  restore_environment: isolated
  compatibility_check: passed
  promotion: human-approved
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le binaire ancien est associé à une sauvegarde compatible, restaurée et validée avant promotion.

## 40. Références techniques officielles

- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [SQLite — Online Backup API](https://www.sqlite.org/backup.html)
- [SQLite — Write-Ahead Logging](https://www.sqlite.org/wal.html)
- [SQLite — Command Line Shell](https://www.sqlite.org/cli.html)
- [PostgreSQL — Backup and Restore](https://www.postgresql.org/docs/current/backup.html)
- [PostgreSQL — pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
- [PostgreSQL — pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html)
- [PostgreSQL — pg_verifybackup](https://www.postgresql.org/docs/current/app-pgverifybackup.html)
- [Git — git-bundle](https://git-scm.com/docs/git-bundle)
- [Git — git-fsck](https://git-scm.com/docs/git-fsck)
- [Godot 4.7 — File system and user path](https://docs.godotengine.org/en/4.7/tutorials/scripting/filesystem.html)
- [Godot — FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html)
- [Docker — Volumes](https://docs.docker.com/engine/storage/volumes/)

## 41. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` maintient un inventaire versionné des actifs critiques. Chaque actif indique autorité, propriétaire, sensibilité, dépendances, méthode de sauvegarde, rétention et ordre de restauration. Les caches, index vectoriels, imports et autres données dérivées restent reconstructibles et ne remplacent jamais sources, états joueurs, bases, registres juridiques ou preuves.

Les objectifs RPO et RTO sont définis par famille avec un service minimal observable. Ils restent des cibles jusqu’à un exercice mesuré. Chaque génération possède une identité immuable, un staging propre, un manifeste fermé, des tailles, des empreintes et un statut. Une tentative échouée ne remplace pas la dernière génération vérifiée. Les copies rapides, hors site et immuables utilisent des identités et pannes distinctes.

Le dépôt source est protégé avec ses refs, objets externes et dépendances ; les builds retenus restent reliés au commit et au manifeste. SQLite est sauvegardé après fermeture qualifiée ou par mécanisme de backup cohérent. PostgreSQL utilise des exports ou sauvegardes adaptés au besoin, restaurés dans une base neuve. Les volumes de conteneur ne sont jamais copiés aveuglément comme preuve de cohérence.

Les migrations sont immuables, versionnées et préparées sur des candidats avant remplacement. La matrice application/données décide des rollbacks. Toute restauration commence dans un environnement isolé, suit le graphe de dépendances, exécute contrôles structurels et métier, mesure RPO/RTO, puis attend une décision humaine avant réadmission.

Tant que jobs, stockages, clés, bases, services, migrations et exercices n’ont pas été matérialisés et exécutés, ce chapitre demeure une architecture documentaire relue au niveau `static-review`. Aucune génération réelle, restauration, migration, mesure RPO/RTO, reprise de service ou continuité runtime de `Project Asteria` n’est revendiquée.
