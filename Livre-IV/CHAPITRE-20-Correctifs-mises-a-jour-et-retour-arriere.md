---
title: "Livre IV — Chapitre 20 : Correctifs, mises à jour et retour arrière"
id: "DOC-L4-CH20"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 20
last-verified: "2026-07-27T19:11:44+02:00"
audit-status: "complete"
audit-date: "2026-07-27T19:11:44+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-20.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Correctifs, mises à jour et retour arrière

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 16 possède l’export, le packaging, les manifestes et les octets fermés. Le chapitre 17 possède la publication initiale, les pages boutique, les soumissions et le lancement. Le présent chapitre possède les mises à jour après lancement : canaux, compatibilité, migration, déploiement progressif, interruption, hotfix, retour arrière et communication.

Le chapitre 15 conserve les sauvegardes indépendantes, la restauration et la reprise après incident. Le chapitre 14 conserve l’orchestration CI/CD et la promotion d’artefacts. Ici, ces capacités sont consommées pour faire évoluer une installation existante sans reconstruire silencieusement le candidat ni confondre arrêt de diffusion et restauration des utilisateurs déjà mis à jour.

Le niveau de preuve reste `static-review`. Aucun patch, migration, déploiement progressif, arrêt, hotfix, rollback, restauration de sauvegarde, mise à jour de boutique ou changement d’installation de `Project Asteria` n’est revendiqué comme exécuté.

> **[LECTURE] Carte de responsabilité — Ne pas saisir.**

```yaml
update_scope:
  packaging_owner: chapter-16
  initial_distribution_owner: chapter-17
  backup_restore_owner: chapter-15
  ci_promotion_owner: chapter-14
  update_and_rollback_owner: chapter-20
  mod_compatibility_owner: chapter-21
  archive_owner: chapter-22
evidence_level: static-review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorités :** Chaque sujet de cycle de vie possède un chapitre propriétaire unique.
- **Frontière :** Le chapitre 20 consomme packages et sauvegardes sans reprendre leur fabrication.
- **Niveau de preuve :** La carte décrit un contrat documentaire, pas une exploitation réelle.
- **Résultat attendu :** Une demande de correctif ou de retour arrière est routée sans ambiguïté.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer correctif, hotfix, mise à jour, patch différentiel, release et rollback ;
- définir des versions de produit, build, contenu, données et protocole ;
- organiser des canaux interne, bêta et stable avec des règles de promotion ;
- produire un manifeste de mise à jour lié aux mêmes octets que le package qualifié ;
- vérifier préconditions, intégrité, espace, verrouillage et capacité de reprise ;
- migrer des sauvegardes et bases avec chemins explicites et sauvegarde préalable ;
- préparer des déploiements progressifs, portes d’observation et critères d’arrêt ;
- séparer retour binaire, restauration de données et hotfix avant arrière ;
- rédiger notes de version, avis joueurs et messages de support ;
- diagnostiquer dix erreurs fréquentes de mise à jour.

## 3. Vocabulaire opérationnel

Un **correctif** modifie un défaut identifié. Un **hotfix** est un correctif urgent dont le périmètre est volontairement réduit. Une **mise à jour** est une nouvelle version distribuée à une installation existante. Un **patch** peut désigner le lot logique de changements ou un différentiel binaire ; le chapitre précise toujours lequel.

Un **déploiement progressif** expose une version à une fraction ou à une cohorte avant généralisation. Une **interruption** empêche de nouveaux utilisateurs de recevoir la version ; elle ne retire pas automatiquement la version des installations déjà mises à jour. Un **rollback binaire** remet un ancien exécutable ou package. Une **restauration de données** remet un état antérieur. Ces deux opérations ont des préconditions différentes.

Un **roll-forward** applique un nouveau correctif au-dessus de la version problématique. Il est souvent plus sûr qu’un retour binaire lorsque les données ont déjà évolué de manière irréversible.

> **[LECTURE] Glossaire de décision — Exemple de référence.**

```json
{
  "incident": "save-load-regression",
  "affected_build": "1.4.2+1842",
  "distribution_action": "halt",
  "installed_users_action": "roll_forward",
  "data_action": "no_restore_without_evidence",
  "status": "candidate"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Incident :** Le problème possède une identité recherchable.
- **Diffusion :** `halt` limite les nouvelles expositions sans prétendre désinstaller la version.
- **Installations :** `roll_forward` prépare un correctif pour les utilisateurs déjà touchés.
- **Données :** Aucune restauration n’est décidée sans preuve de corruption.
- **Statut :** `candidate` interdit de présenter cette décision comme exécutée.

## 4. Modèle mental : une mise à jour est une transaction distribuée

Une mise à jour touche plusieurs autorités : plateforme de distribution, installation locale, sauvegardes, services réseau, données persistantes, configuration, support et communication. Elles ne basculent pas toutes au même instant. La procédure doit donc tolérer des états mixtes : ancienne version encore active, nouvelle version téléchargée mais non installée, migration préparée mais non validée, ou déploiement interrompu après une exposition partielle.

Le contrat minimal suit cinq phases : **préparer**, **acquérir**, **vérifier**, **activer**, **observer**. Une sixième phase, **récupérer**, décrit la réponse aux échecs. L’activation n’est autorisée que si le package, les préconditions et la stratégie de données sont cohérents.

> **[LECTURE] Machine d’état conceptuelle d’une mise à jour.**

```yaml
states:
  - current
  - offered
  - downloading
  - verified
  - staged
  - activating
  - active_observation
  - completed
  - recovery_required
terminal_states:
  - completed
  - recovery_required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** Chaque étape rend visibles les reprises possibles.
- **Vérification :** `verified` précède toute modification de l’installation.
- **Observation :** La version active reste sous surveillance avant clôture.
- **Échec :** `recovery_required` appelle une procédure explicite au lieu d’un retry infini.

## 5. Versionner séparément produit, build, contenu, données et protocole

Une seule chaîne de version ne suffit pas à expliquer toutes les compatibilités. `Project Asteria` distingue au minimum :

- la version publique du produit, lisible dans les notes de version ;
- l’identifiant immuable du build, relié aux artefacts du chapitre 14 ;
- la version de contenu, utile lorsque des catalogues ou données évoluent ;
- la version de schéma de sauvegarde ou de base ;
- la version de protocole réseau ;
- la version minimale acceptée par les services ou sessions multijoueur.

Le format `major.minor.patch` peut servir à la version publique, mais ses règles doivent être documentées pour le projet. Il ne remplace ni l’empreinte du package ni la matrice de compatibilité.

> **[VSC] Contrat candidat `release/version-contract.yaml`.**

```yaml
product_version: 1.4.2
build_id: asteria-win64-1842
content_version: 37
save_schema: 12
network_protocol: 8
minimum_server_build: 1839
source_commit: 0123456789abcdef
status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Produit :** `product_version` sert à la communication et au support.
- **Build :** `build_id` identifie un artefact immuable.
- **Contenu :** `content_version` découple les données éditoriales du binaire.
- **Schémas :** `save_schema` et `network_protocol` portent leurs propres compatibilités.
- **Preuve :** `source_commit` relie le candidat à sa source sans remplacer le manifeste.

## 6. Définir les canaux interne, bêta et stable

Un canal est une politique d’accès et de promotion, pas un simple dossier. Le canal **interne** reçoit les candidats pour tests contrôlés. Le canal **bêta** reçoit une population consentante ou désignée. Le canal **stable** reçoit uniquement une version ayant franchi les portes techniques, données, sécurité, accessibilité, localisation, support et communication.

Chaque canal définit propriétaire, audience, durée minimale d’observation, versions sources supportées, droit d’interruption, métriques et sortie attendue. Un build est promu entre canaux sans reconstruction lorsque la plateforme le permet ; sinon, la nouvelle enveloppe doit conserver un lien d’intégrité avec les octets qualifiés.

> **[LECTURE] Topologie candidate des canaux.**

```yaml
channels:
  internal:
    audience: named_testers
    automatic_update: optional
    promotion_target: beta
  beta:
    audience: opt_in
    automatic_update: platform_managed
    promotion_target: stable
  stable:
    audience: public
    automatic_update: platform_managed
    promotion_target: null
promotion_requires:
  - identical_candidate_identity
  - passed_gates
  - named_approver
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Audience :** Chaque canal indique qui peut recevoir le build.
- **Automatisation :** La plateforme peut distribuer sans que le jeu contrôle le calendrier exact.
- **Promotion :** Le chemin est orienté et ne saute pas les portes.
- **Approbation :** Une personne ou un rôle nommé assume la décision.

## 7. Construire une stratégie de promotion

La promotion réutilise l’identité du candidat, ses manifestes, ses résultats de tests et ses réserves. Elle enregistre le canal source, le canal cible, l’approbateur, l’instant, la population visée et la condition d’arrêt. Un nouveau build corrigeant un défaut reçoit une nouvelle identité ; il ne remplace pas silencieusement l’artefact précédent.

Les métadonnées de boutique ou de launcher peuvent évoluer séparément du package. Le reçu de promotion doit donc distinguer l’identité binaire, la configuration de diffusion et la communication affichée aux joueurs.

> **[LECTURE] Reçu de promotion — Modèle documentaire.**

```json
{
  "promotion_id": "prom-2026-07-27-001",
  "build_id": "asteria-win64-1842",
  "from_channel": "beta",
  "to_channel": "stable",
  "rollout_mode": "progressive",
  "approved_by": "release-manager",
  "status": "planned"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `promotion_id` évite de confondre plusieurs décisions sur le même build.
- **Même candidat :** `build_id` reste celui déjà qualifié.
- **Canaux :** La source et la cible rendent le mouvement auditable.
- **Mode :** `progressive` prépare une exposition graduelle.
- **Statut :** `planned` ne revendique aucune promotion réelle.

## 8. Définir les versions sources supportées

Une mise à jour doit annoncer les installations depuis lesquelles elle sait évoluer. Le support peut couvrir la version immédiatement précédente, plusieurs versions mineures, une version de base longue durée ou une réinstallation complète. Chaque chemin possède un coût et un risque différents.

La matrice ne suppose jamais qu’une chaîne de patches intermédiaires existe encore. Si une installation est trop ancienne, le produit propose un package complet, une migration par étapes documentée ou une procédure de support. Le refus doit préserver les données et expliquer l’action suivante.

> **[VSC] Matrice candidate `release/update-paths.yaml`.**

```yaml
target_build: 1842
paths:
  - from_build: 1839
    package: delta-1839-1842
    save_path: 11-to-12
  - from_build: 1810
    package: full-1842
    save_path: 10-to-12
  - from_build: older
    package: unsupported
    support_action: export_saves_then_reinstall
status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** Tous les chemins convergent vers un build précis.
- **Différentiel :** Le package réduit n’est proposé que depuis une base connue.
- **Package complet :** Une version plus ancienne peut éviter une chaîne fragile de deltas.
- **Support :** L’absence de chemin automatique n’autorise pas la perte de sauvegardes.

## 9. Choisir entre package complet et patch différentiel

Le package complet simplifie la reconstruction de l’état cible mais augmente la bande passante. Le patch différentiel réduit souvent le transfert, tout en dépendant exactement d’un état source et d’un algorithme d’application. Le choix appartient au canal et à la plateforme.

Un patch différentiel ne se résume pas à une archive de fichiers modifiés. Il doit décrire la base attendue, les opérations, les suppressions, les métadonnées, l’empreinte cible et le comportement en cas de divergence. Lorsque la plateforme génère ses propres deltas, le projet conserve surtout les manifestes des builds source et cible.

> **[LECTURE] Manifeste logique d’un patch différentiel.**

```json
{
  "format": "asteria-patch-v1",
  "from_build": 1839,
  "to_build": 1842,
  "target_sha256": "candidate-target-digest",
  "operations": [
    {"op": "replace", "path": "Asteria.pck"},
    {"op": "remove", "path": "legacy/cache.index"}
  ],
  "requires_restart": true
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** La version du manifeste permet de faire évoluer le moteur de patch.
- **Base :** `from_build` empêche l’application sur une installation inconnue.
- **Cible :** L’empreinte attendue vérifie le résultat final, pas seulement le téléchargement.
- **Opérations :** Remplacements et suppressions sont explicites.
- **Redémarrage :** Le contrat n’active pas à chaud des fichiers encore ouverts.

## 10. Préserver l’identité des octets qualifiés

Le chapitre 16 produit le package fermé et son manifeste. Le chapitre 20 n’en reconstruit pas une variante pendant le déploiement. Les patches, launchers ou plateformes peuvent transformer le transport, mais l’état installé doit être corrélé au build cible qualifié.

L’empreinte d’un fichier prouve une identité de contenu, pas son auteur ni son innocuité. La signature, la provenance, les permissions de publication et les résultats de validation restent des preuves distinctes.

> **[PS] Vérification candidate d’un manifeste sous PowerShell.**

```powershell
param(
    [Parameter(Mandatory)]
    [string]$ManifestPath,
    [Parameter(Mandatory)]
    [string]$InstallRoot
)

$manifest = Get-Content -LiteralPath $ManifestPath -Raw | ConvertFrom-Json
foreach ($entry in $manifest.files) {
    $path = Join-Path $InstallRoot $entry.path
    $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
    if ($actual -ne $entry.sha256) {
        throw "Intégrité invalide : $($entry.path)"
    }
}
"integrity=ok build=$($manifest.build_id)"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** Le manifeste et la racine sont fournis explicitement.
- **Lecture :** `-Raw` conserve le document JSON complet.
- **Empreinte :** Chaque fichier est comparé à la valeur canonique en SHA-256.
- **Échec :** Une divergence bloque l’activation au lieu d’être seulement journalisée.
- **Sortie :** Le message final n’est produit qu’après toutes les vérifications.

## 11. Vérifier les préconditions avant téléchargement ou activation

Les préconditions incluent plateforme, architecture, version source, espace disponible, permissions, processus actifs, état des sauvegardes, connectivité, alimentation pour les appareils concernés et disponibilité des services nécessaires. Elles sont évaluées avant toute action destructive.

L’espace requis comprend le téléchargement, le staging, l’installation cible, une marge de travail et, lorsque la stratégie l’exige, une copie de l’état précédent. Une estimation insuffisante ne doit pas provoquer la suppression prématurée du seul build fonctionnel.

> **[LECTURE] Préflight candidat d’une installation.**

```yaml
preflight:
  expected_build: 1839
  target_build: 1842
  free_space_policy: staged_plus_previous
  require_save_backup: true
  require_game_stopped: true
  require_manifest_match: true
on_failure:
  mutate_installation: false
  preserve_download: conditional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** La version installée doit correspondre au chemin choisi.
- **Espace :** La politique réserve staging et version précédente.
- **Données :** La sauvegarde préalable est une porte lorsque le schéma évolue.
- **Verrou :** Le jeu arrêté évite de remplacer des fichiers ouverts.
- **Échec :** Le préflight n’altère pas l’installation.

## 12. Télécharger dans un staging confiné

Le téléchargement arrive dans un répertoire nouveau qui ne sert jamais de version active. Les noms temporaires, permissions et limites de taille sont contrôlés. Le client ne suit pas de chemins absolus ou de traversées issus d’un manifeste non fiable.

Chaque fragment peut posséder une empreinte de transport, mais l’autorité reste l’empreinte de l’état cible après application. Les reprises de téléchargement vérifient les plages déjà présentes avant de les réutiliser.

> **[CMD] Création candidate d’un staging Windows.**

```bat
@echo off
setlocal
set "STAGING=%LOCALAPPDATA%\Asteria\updates\1842.tmp"
if exist "%STAGING%" (
  echo staging-exists
  exit /b 20
)
mkdir "%STAGING%"
if errorlevel 1 exit /b 21
echo staging-ready
exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemin :** Le staging est borné à l’espace applicatif de l’utilisateur.
- **Existence :** Un ancien staging exige diagnostic ou reprise explicite.
- **Création :** Le code de sortie différencie la collision de l’échec de création.
- **Résultat :** Aucun fichier actif n’est modifié par cette étape.

## 13. Appliquer dans une nouvelle génération

L’application construit une génération complète à côté de la version active lorsque le stockage le permet. Les opérations sont idempotentes ou enregistrées dans un journal de reprise. Une suppression n’efface jamais un fichier de la génération active avant que la cible soit vérifiée.

La génération cible reçoit son propre manifeste, son identifiant de build et un marqueur d’état. Le pointeur d’activation ne bascule qu’après contrôles structurels et métier hors ligne.

> **[WSL] Préparation candidate d’une génération sous Linux ou WSL.**

```bash
#!/usr/bin/env bash
set -euo pipefail

root="${1:?install root required}"
target="${2:?target build required}"
staged="$root/generations/$target.staged"
active_link="$root/current"

test ! -e "$staged"
mkdir -p "$staged"
printf '%s\n' "state=staging" > "$staged/update.state"
printf '%s\n' "active_link=$active_link"
printf '%s\n' "staged=$staged"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** La racine et le build cible sont obligatoires.
- **Mode strict :** Le script s’arrête sur erreur, variable absente ou pipeline défaillant.
- **Isolation :** La génération `.staged` ne remplace pas le lien actif.
- **Marqueur :** L’état écrit permet de distinguer staging et activation.
- **Sorties :** Les chemins affichés servent au diagnostic, pas à une activation automatique.

## 14. Vérifier l’état cible avant bascule

Les contrôles portent sur manifestes, empreintes, présence des exécutables, permissions, dépendances natives, configuration minimale et capacité à lire un échantillon de données. Un lancement de fumée hors ligne peut être prévu si l’environnement le permet, mais il doit être borné et ne pas modifier les sauvegardes autoritaires.

La validation d’un package ne prouve pas la réussite de la migration des données. Les deux portes restent séparées afin de pouvoir diagnostiquer un binaire sain avec un schéma incompatible, ou l’inverse.

> **[VSC] Vérification d’intégrité candidate dans Godot.**

```gdscript
class_name InstalledFileVerifier
extends RefCounted

static func verify(path: String, expected_sha256: String) -> Dictionary:
    var actual := FileAccess.get_sha256(path)
    if actual.is_empty():
        return {"ok": false, "code": "hash_unavailable", "path": path}
    if actual != expected_sha256.to_lower():
        return {"ok": false, "code": "digest_mismatch", "path": path}
    return {"ok": true, "code": "verified", "path": path}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `RefCounted` convient à un service sans présence dans l’arbre.
- **Entrées :** Le chemin et l’empreinte attendue restent séparés.
- **Erreur de lecture :** Une empreinte vide n’est pas interprétée comme une valeur valide.
- **Comparaison :** La divergence produit un code structuré.
- **Retour :** L’appelant décide de la récupération sans exception implicite.

## 15. Activer par bascule atomique ou contrôlée

L’activation change un pointeur, un répertoire sélectionné ou un enregistrement de launcher. Elle doit être aussi courte que possible et laisser un chemin de reprise si le processus s’interrompt. Sur les plateformes gérées, cette responsabilité appartient au client de distribution ; le jeu ne réimplémente pas son installateur.

Une bascule de répertoire ne rend pas automatiquement les données compatibles. Le démarrage suivant vérifie le marqueur de build et le schéma avant de charger une sauvegarde.

> **[LECTURE] Journal d’activation — Structure candidate.**

```json
{
  "transaction_id": "upd-1842-device-local",
  "previous_build": 1839,
  "target_build": 1842,
  "stage": "activation_pending",
  "previous_generation_retained": true,
  "save_migration_pending": true
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Transaction :** L’identité locale corrèle toutes les étapes de reprise.
- **Générations :** Ancienne et nouvelle versions sont nommées.
- **Rétention :** Le build précédent n’est pas supprimé avant observation.
- **Migration :** Le statut des données reste indépendant de l’activation binaire.

## 16. Reprendre après interruption

Une coupure peut survenir pendant téléchargement, application, activation, migration ou premier lancement. Chaque phase possède un marqueur durable écrit avant l’opération risquée et mis à jour après réussite. Au redémarrage, le système lit ce marqueur au lieu de deviner depuis la présence de fichiers.

La reprise n’est pas un retry infini. Les erreurs d’intégrité, de schéma, de permission ou d’autorité demandent une intervention ou un package différent. Les erreurs transitoires de réseau peuvent être retentées avec délai et plafond.

> **[LECTURE] Table de reprise candidate.**

```yaml
recovery:
  downloading:
    action: resume_verified_ranges
  staged:
    action: reverify_then_activate
  activation_pending:
    action: inspect_active_pointer
  migration_started:
    action: restore_pre_migration_copy_or_resume_idempotent_step
  active_observation:
    action: continue_observation
max_transient_retries: 3
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Téléchargement :** Seules les plages vérifiées sont réutilisées.
- **Staging :** La cible est revalidée avant bascule.
- **Activation :** Le pointeur réel est inspecté au lieu d’être supposé.
- **Migration :** La stratégie dépend de l’idempotence et de la copie préalable.
- **Borne :** Les retries transitoires ne deviennent pas une boucle permanente.

## 17. Versionner les sauvegardes et données persistantes

Chaque sauvegarde porte un schéma explicite indépendant de la version du produit. Le chargeur ne modifie jamais l’unique copie pendant la lecture. Il prépare une nouvelle représentation, valide ses invariants puis la promeut.

Les sauvegardes futures ou inconnues sont refusées proprement. Une ancienne version du jeu ne doit pas ouvrir en écriture un format plus récent qu’elle ne comprend pas. Cette règle protège particulièrement les retours binaires.

> **[VSC] Enveloppe candidate d’une sauvegarde versionnée.**

```json
{
  "format": "asteria-save",
  "schema": 12,
  "created_by_build": 1842,
  "slot_id": "slot-01",
  "payload": {
    "world_id": "world-main",
    "player_id": "player-local"
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** L’identité du type de document précède le payload.
- **Schéma :** `schema` pilote les migrations.
- **Origine :** `created_by_build` aide au diagnostic sans devenir l’autorité du schéma.
- **Identités :** Le payload conserve des identifiants métier, pas des libellés affichés.

## 18. Concevoir un registre de migrations

Une migration est identifiée par schéma source, schéma cible, code, préconditions, effets et stratégie de reprise. Le registre forme un graphe dirigé sans saut implicite. Les chemins sont calculés avant toute mutation.

Les migrations publiées sont immuables. Une correction reçoit une nouvelle migration ou un nouveau build ; modifier en place une étape déjà exécutée rend les incidents impossibles à reproduire.

> **[VSC] Registre candidat de migrations en GDScript.**

```gdscript
class_name SaveMigrationRegistry
extends RefCounted

var _steps: Dictionary = {}

func register_step(from_schema: int, to_schema: int, callable: Callable) -> void:
    var key := "%d->%d" % [from_schema, to_schema]
    assert(not _steps.has(key))
    _steps[key] = callable

func get_step(from_schema: int, to_schema: int) -> Callable:
    var key := "%d->%d" % [from_schema, to_schema]
    return _steps.get(key, Callable())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Registre :** Le dictionnaire indexe une arête précise du graphe.
- **Immutabilité :** L’assertion refuse deux implémentations pour le même chemin.
- **Callable :** Le registre référence une transformation sans l’exécuter pendant la sélection.
- **Absence :** Un `Callable` vide rend le chemin manquant explicite à l’appelant.

## 19. Préparer une copie avant migration

La copie pré-migration est distincte des sauvegardes de continuité du chapitre 15, mais elle doit respecter les mêmes principes d’intégrité et de rétention. Elle contient la source exacte, son schéma, son empreinte, le build cible et l’identité de transaction.

La copie est créée avant la première écriture, vérifiée puis protégée contre l’écrasement par le processus de migration. Son expiration intervient seulement après observation, consentement de la politique de rétention et disponibilité d’une sauvegarde indépendante.

> **[PS] Copie pré-migration candidate sous PowerShell.**

```powershell
param(
    [Parameter(Mandatory)]
    [string]$SavePath,
    [Parameter(Mandatory)]
    [string]$BackupPath
)

if (Test-Path -LiteralPath $BackupPath) {
    throw "La copie pré-migration existe déjà."
}
Copy-Item -LiteralPath $SavePath -Destination $BackupPath
$source = (Get-FileHash -Algorithm SHA256 -LiteralPath $SavePath).Hash
$backup = (Get-FileHash -Algorithm SHA256 -LiteralPath $BackupPath).Hash
if ($source -ne $backup) {
    throw "La copie pré-migration ne correspond pas à la source."
}
"backup=verified"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Collision :** Une copie existante n’est jamais écrasée silencieusement.
- **Copie :** La source reste inchangée.
- **Double empreinte :** Source et destination sont comparées après écriture.
- **Échec :** Une divergence bloque la migration.
- **Sortie :** Le statut vérifié peut être joint au reçu de transaction.

## 20. Séparer migrations réversibles et irréversibles

Une migration réversible possède une transformation inverse qualifiée et conserve les informations nécessaires. Une migration irréversible supprime, fusionne ou transforme des données sans inverse fiable. Cette classification doit être décidée avant diffusion.

Lorsqu’une étape est irréversible, le rollback binaire ne suffit pas. Les options deviennent : conserver le nouveau schéma et publier un roll-forward compatible, restaurer une copie pré-migration en acceptant la perte des actions postérieures, ou bloquer le retour. La communication et le support doivent refléter cette réalité.

> **[LECTURE] Classification candidate des migrations.**

```yaml
migrations:
  - id: save-11-to-12
    reversible: false
    information_loss: normalized_quest_history
    rollback_strategy: restore_pre_migration_copy
    roll_forward_supported: true
  - id: config-4-to-5
    reversible: true
    inverse: config-5-to-4
    rollback_strategy: inverse_then_binary_rollback
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** Chaque étape possède un nom stable.
- **Réversibilité :** La propriété est déclarée, pas supposée.
- **Perte :** L’information non reconstructible est nommée.
- **Stratégie :** Le retour dépend de la nature des données.
- **Roll-forward :** Un correctif avant peut rester disponible malgré l’absence d’inverse.

## 21. Maintenir une matrice de compatibilité

La matrice relie client, serveur, protocole, sauvegarde, contenu et mods éventuels. Elle répond à des questions concrètes : un client ancien peut-il rejoindre un serveur nouveau ? une sauvegarde migrée peut-elle être relue par le build précédent ? un catalogue de contenu plus récent est-il toléré ?

Les réponses utilisent des états explicites : `compatible`, `read_only`, `migration_required`, `blocked`, `unknown`. `Unknown` bloque la promotion ; il ne signifie jamais compatible par défaut.

> **[LECTURE] Matrice de compatibilité simplifiée.**

```markdown
| Élément | Source | Cible | Décision |
|---|---:|---:|---|
| sauvegarde | 11 | 12 | migration_required |
| sauvegarde | 12 | 11 | blocked |
| protocole client | 8 | 8 | compatible |
| contenu | 36 | 37 | migration_required |
| mod API | 3 | 4 | unknown |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Axes :** Chaque ligne compare un contrat précis.
- **Sens :** La compatibilité de 11 vers 12 n’implique pas celle de 12 vers 11.
- **Réseau :** Une égalité de protocole reste soumise aux capacités.
- **Mods :** `unknown` réserve la décision au chapitre 21 et aux tests.

## 22. Gérer la compatibilité client-serveur

Une mise à jour multijoueur peut créer une population mixte. Le serveur annonce version minimale, version maximale, protocole et capacités. Le client refuse une session incompatible avant d’échanger un état métier. Les délais de grâce doivent être bornés et cohérents avec la sécurité.

Un serveur ne doit pas accepter un ancien client uniquement pour préserver le taux de connexion si le protocole ou les validations ont changé. À l’inverse, une incompatibilité de version publique ne suffit pas à bloquer si le protocole et les capacités sont explicitement compatibles.

> **[VSC] Contrat candidat de négociation de mise à jour.**

```json
{
  "server_build": 1842,
  "protocol": 8,
  "minimum_client_build": 1839,
  "required_capabilities": [
    "inventory_tx_v2",
    "save_schema_12"
  ],
  "maintenance_message_key": "network.update_required"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Serveur :** Le build facilite le support et la corrélation.
- **Protocole :** La compatibilité réseau possède sa propre version.
- **Minimum :** La borne est explicite et peut évoluer.
- **Capacités :** Les fonctions requises évitent une simple comparaison numérique.
- **Message :** La clé localisable appartient au chapitre 19.

## 23. Mettre à jour contenus et catalogues

Les données de jeu, traductions, tables d’équilibrage et ressources peuvent évoluer sans changer toutes les bibliothèques. Elles conservent pourtant une identité de build ou de contenu, un manifeste et un schéma. Une mise à jour de contenu suit les mêmes principes de staging et d’activation.

Les données autoritaires ne sont jamais chargées depuis un téléchargement partiel. Les caches ou index dérivés peuvent être reconstruits après activation, mais ils ne sont pas inclus dans la preuve de migration sauf nécessité explicite.

> **[LECTURE] Contrat candidat d’un lot de contenu.**

```yaml
content_bundle:
  version: 37
  compatible_product:
    minimum: 1.4.0
    maximum_exclusive: 1.5.0
  catalogs:
    gameplay: gameplay-37.json
    localization: localization-19.po
  derived_indexes:
    rebuild_after_activation: true
status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** Le lot de contenu possède une identité indépendante.
- **Plage :** La compatibilité produit est bornée.
- **Catalogues :** Gameplay et localisation sont distingués.
- **Dérivés :** Les index peuvent être reconstruits au lieu d’être promus comme sources.

## 24. Préserver accessibilité et localisation pendant la mise à jour

Les écrans de mise à jour, erreurs, reprises et notes de version doivent respecter les réglages d’accessibilité déjà disponibles et les locales annoncées. Une mise à jour ne doit pas rendre le produit inutilisable avant que le joueur puisse corriger un réglage.

Les nouvelles chaînes sont extraites, traduites et validées selon le chapitre 19. Les annonces de changements d’accessibilité sont reliées au même build et à la même plateforme que la fonction décrite. Une régression critique peut justifier l’arrêt du déploiement.

> **[LECTURE] Checklist de présentation de la mise à jour.**

```yaml
update_ui:
  keyboard_navigation: required
  screen_reader_status: platform_qualified_only
  localized_error_keys: required
  progress_has_text_equivalent: true
  cancel_or_resume_policy: documented
  high_contrast_state_preserved: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Navigation :** La procédure reste utilisable sans périphérique unique.
- **Lecteur d’écran :** Aucune compatibilité n’est généralisée sans qualification.
- **Erreurs :** Les messages utilisent des clés et non des chaînes codées en dur.
- **Progression :** Une valeur textuelle complète la représentation visuelle.
- **Réglages :** Les préférences sûres sont préservées à travers le changement.

## 25. Définir un déploiement progressif

Le déploiement progressif limite l’exposition initiale et fournit une fenêtre d’observation. La plateforme peut sélectionner aléatoirement des utilisateurs, utiliser une cohorte, un territoire ou un canal volontaire. Le projet ne suppose pas que les mêmes mécanismes existent partout.

Chaque étape indique population cible, durée minimale, signaux observés, seuils candidats et approbateur. Les pourcentages et délais sont des politiques à qualifier, non des constantes universelles. Une plateforme peut permettre l’interruption sans rétrograder les utilisateurs déjà servis.

> **[LECTURE] Plan candidat de déploiement progressif.**

```yaml
rollout:
  build_id: asteria-win64-1842
  stages:
    - name: internal
      audience: named_testers
      minimum_observation: candidate
    - name: beta
      audience: opt_in
      minimum_observation: candidate
    - name: stable_progressive
      audience: platform_cohort
      minimum_observation: candidate
  progression_requires:
    - integrity_green
    - migration_green
    - crash_signal_reviewed
    - support_ready
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Étapes :** Les populations sont décrites sans inventer de pourcentages.
- **Durées :** `candidate` réserve la qualification à la plateforme et au produit.
- **Portes :** Intégrité, données, stabilité et support sont contrôlés séparément.
- **Décision :** La progression n’est jamais automatique par simple absence d’alerte.

## 26. Observer avant d’élargir

L’observation combine crashs, échecs de démarrage, échecs de migration, intégrité, consommation de bande passante, demandes support, retours joueurs et signaux métier pertinents. Les métriques ne modifient pas directement le déploiement ; elles alimentent une décision tracée.

Les comparaisons utilisent une fenêtre, une population et une version de référence. Une baisse absolue peut refléter une population différente. Les petits échantillons et les délais de remontée sont nommés comme limites.

> **[SORTIE] Exemple de rapport à lire après une étape.**

```text
build=1842
channel=beta
exposed_installations=candidate
startup_failures=not_measured
migration_failures=not_measured
support_incidents=not_measured
decision=hold
reason=evidence_pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** Le build et le canal cadrent le rapport.
- **Population :** La valeur reste candidate tant qu’aucune plateforme n’est connectée.
- **Mesures :** `not_measured` évite d’inventer des zéros.
- **Décision :** `hold` conserve la cohorte sans élargissement.
- **Motif :** L’absence de preuve devient une raison explicite.

## 27. Définir des portes d’arrêt

Une porte d’arrêt décrit le signal, la source, la fenêtre, le responsable et l’action. Les seuils candidats doivent être qualifiés lors de campagnes ou à partir d’une base historique. Une alerte isolée peut déclencher investigation ou arrêt selon sa sévérité.

Les incidents de corruption, sécurité, paiement ou perte de données ont souvent une politique plus stricte que les régressions cosmétiques. Le chapitre ne fixe pas de seuil universel ; il impose leur provenance et leur approbation.

> **[LECTURE] Registre candidat des portes d’arrêt.**

```yaml
halt_gates:
  - id: save-corruption
    signal: confirmed_data_loss
    action: halt_and_incident
    threshold: any_confirmed_case
    owner: incident-commander
  - id: startup-regression
    signal: startup_failure_rate
    action: hold_then_review
    threshold: qualification_required
    owner: release-manager
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** Chaque porte est recherchable.
- **Signal :** La donnée attendue est nommée.
- **Action :** Arrêt immédiat et maintien ne sont pas confondus.
- **Seuil :** Les cas de perte confirmée peuvent suivre une règle stricte.
- **Propriétaire :** La décision n’est pas abandonnée à un dashboard.

## 28. Interrompre un déploiement sans promettre un rollback

Interrompre empêche l’élargissement. Sur certaines plateformes, les utilisateurs déjà servis conservent la version. La procédure identifie donc trois populations : non exposée, exposée sans incident connu, exposée avec incident. Chacune reçoit une action adaptée.

Le message public ne doit pas annoncer « retour à la version précédente » si seule la diffusion est arrêtée. Il précise que la mise à jour est suspendue, que les installations déjà mises à jour peuvent rester sur la version et qu’un correctif ou une instruction suivra.

> **[LECTURE] Décision candidate d’interruption.**

```json
{
  "build_id": "asteria-win64-1842",
  "distribution": "halt_new_exposure",
  "already_updated": "retain_and_monitor",
  "affected_users": "support_and_hotfix",
  "binary_rollback": "not_approved",
  "data_restore": "not_approved"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distribution :** L’arrêt vise les nouvelles expositions.
- **Déjà mis à jour :** Ces installations ne sont pas supposées rétrogradées.
- **Affectés :** Support et hotfix possèdent une action dédiée.
- **Rollback :** Binaire et données restent non approuvés sans analyse.

## 29. Choisir entre rollback, roll-forward et désactivation

Le **rollback** revient à une version précédente lorsque l’installation et les données sont compatibles. Le **roll-forward** publie une version corrigée au-dessus de la version problématique. La **désactivation** coupe une fonction par configuration ou capacité lorsque cette surface existe et a été conçue à l’avance.

La décision examine gravité, exposition, réversibilité des données, délai de correction, disponibilité du build précédent, compatibilité serveur et capacité de support. Une désactivation ne doit pas devenir une porte dérobée non auditée ni contourner la publication d’un correctif durable.

> **[LECTURE] Arbre de décision simplifié.**

```text
incident confirmé
├─ perte ou corruption de données ?
│  ├─ oui → arrêter, préserver preuves, évaluer restauration
│  └─ non → continuer l’analyse
├─ ancien build compatible avec données courantes ?
│  ├─ oui → rollback binaire candidat
│  └─ non → roll-forward ou désactivation candidate
└─ fonction isolable sans risque ?
   ├─ oui → désactivation bornée puis correctif
   └─ non → hotfix prioritaire
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Priorité :** La donnée est évaluée avant la vitesse de retour.
- **Compatibilité :** Le build précédent doit lire l’état courant.
- **Isolation :** Une désactivation exige une surface prévue et testée.
- **Sortie :** Chaque branche produit une option candidate, pas une exécution.

## 30. Exécuter un rollback binaire contrôlé

Le rollback binaire réutilise un build précédent conservé, vérifié et encore autorisé. La procédure confirme que ses certificats, dépendances, services et protocoles restent acceptables. Elle vérifie ensuite que les données n’ont pas franchi un schéma incompatible.

Le rollback reçoit une nouvelle décision et un reçu ; il ne déplace pas un tag historique ni ne réécrit les preuves du build précédent. L’ancienne version peut redevenir active sans devenir une nouvelle release binaire.

> **[LECTURE] Reçu candidat de rollback binaire.**

```yaml
rollback:
  incident_id: inc-2026-042
  from_build: 1842
  to_build: 1839
  save_schema_current: 11
  save_schema_supported_by_target: 11
  previous_build_integrity: verified
  approval: pending
  data_restore: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Incident :** Le retour est lié à la cause déclenchante.
- **Sens :** Source et cible sont explicites.
- **Données :** Le schéma courant est comparé à celui accepté par la cible.
- **Intégrité :** Le build retenu est revérifié.
- **Approbation :** `pending` bloque l’exécution.
- **Restauration :** Le rollback binaire n’implique pas une restauration de sauvegarde.

## 31. Restaurer des données uniquement avec une perte acceptée

Restaurer une copie pré-migration peut effacer les progrès réalisés après la mise à jour. La procédure calcule la fenêtre de perte, conserve l’état courant comme preuve, demande l’autorisation appropriée et vérifie la copie avant promotion.

Lorsque seule une partie des données est corrompue, une réparation ciblée peut être préférable à une restauration complète. Cette réparation est versionnée, testée sur copie et journalisée comme migration corrective.

> **[LECTURE] Évaluation candidate d’une restauration.**

```yaml
restore_assessment:
  current_state_preserved: true
  restore_source_verified: true
  estimated_progress_loss: unknown
  user_consent_required: true
  legal_or_support_review: pending
  decision: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préservation :** L’état incident reste disponible pour analyse.
- **Source :** La copie de restauration possède une intégrité vérifiée.
- **Perte :** `unknown` bloque l’opération.
- **Consentement :** La politique dépend du contexte et du type de données.
- **Décision :** La restauration reste bloquée tant que les impacts ne sont pas établis.

## 32. Préparer un hotfix minimal

Un hotfix réduit le nombre de changements mais ne réduit pas les contrôles essentiels. Il part d’une base identifiée, contient uniquement les corrections nécessaires, reçoit un nouveau build, repasse les tests ciblés et les portes de sécurité, puis suit un déploiement observable.

Le cherry-pick d’un commit n’est pas une preuve de minimalité. Le diff binaire, les dépendances, les migrations et les notes de version sont revus. Une correction urgente qui modifie les données peut être plus risquée qu’une release normale.

> **[VSC] Fiche candidate de hotfix.**

```yaml
hotfix:
  incident_id: inc-2026-042
  base_build: 1842
  target_build: 1843
  allowed_changes:
    - save_loader_null_guard
  data_migration: none
  targeted_tests:
    - load_schema_12_fixture
    - interrupted_write_recovery
  status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** Le hotfix indique le build réellement corrigé.
- **Liste fermée :** `allowed_changes` facilite la revue de périmètre.
- **Données :** L’absence de migration est déclarée.
- **Tests :** Les scénarios couvrent le défaut et sa reprise.
- **Statut :** Le lot n’est pas présenté comme publié.

## 33. Rédiger des notes de version utiles

Les notes de version distinguent corrections, changements visibles, impacts de sauvegarde, compatibilité, problèmes connus et actions demandées. Elles évitent les formulations vagues comme « améliorations diverses » lorsqu’un joueur doit comprendre un risque ou une incompatibilité.

Le texte public ne révèle ni secret, ni détail d’exploitation exploitable, ni donnée personnelle. Les références internes à un incident peuvent être conservées dans le dossier de release sans être publiées telles quelles.

> **[VSC] Gabarit candidat de notes de version.**

```markdown
# Version 1.4.2

## Corrections
- Correction d’un échec de chargement sur certaines sauvegardes version 11.

## Compatibilité
- Les sauvegardes restent lisibles après mise à jour.
- Le retour vers une version antérieure n’est pas recommandé après migration.

## Problèmes connus
- Aucun problème connu n’est déclaré sans revue des preuves.

## Assistance
- Utiliser le canal de support officiel et joindre l’identifiant de build.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** Les rubriques répondent aux questions du joueur.
- **Sauvegardes :** La compatibilité et les limites de retour sont visibles.
- **Prudence :** L’absence de problème connu exige une revue, pas une supposition.
- **Support :** L’identifiant de build accélère le diagnostic.

## 34. Préparer plusieurs messages de communication

La communication comprend au moins l’annonce planifiée, l’avis de mise à jour disponible, l’interruption, le hotfix, la restauration éventuelle et la clôture. Chaque message indique version, plateformes concernées, état, action joueur, risques connus et prochain point d’information.

Une date ou un délai n’est annoncé que si son propriétaire l’a approuvé. En incident, mieux vaut une fréquence de mise à jour tenue qu’une estimation de résolution non fondée.

> **[LECTURE] Matrice candidate de communication.**

```markdown
| Situation | Message principal | Action joueur |
|---|---|---|
| mise à jour planifiée | contenu et fenêtre approuvés | fermer le jeu si demandé |
| diffusion suspendue | nouvelles installations arrêtées | conserver la version actuelle |
| hotfix disponible | défaut ciblé corrigé | relancer la mise à jour |
| restauration requise | impact et perte expliqués | suivre la procédure de support |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Situations :** Les états de diffusion ne sont pas mélangés.
- **Message :** Chaque formulation décrit ce qui est réellement vrai.
- **Action :** Le joueur reçoit une consigne observable.
- **Restauration :** Une perte potentielle est expliquée avant l’action.

## 35. Organiser support et diagnostics

Le support collecte le minimum nécessaire : version, build, plateforme, étape de mise à jour, code d’erreur, présence d’une copie pré-migration et consentement aux pièces jointes. Les sauvegardes et journaux peuvent contenir des données personnelles ou narratives ; leur collecte suit une procédure de minimisation.

Le paquet de diagnostic ne contient ni jeton, ni credential de boutique, ni chemin personnel inutile. Il fournit des identifiants de corrélation et un inventaire lisible avant envoi.

> **[LECTURE] Schéma candidat d’un ticket de mise à jour.**

```json
{
  "ticket_type": "update_failure",
  "build_before": 1839,
  "build_target": 1842,
  "phase": "migration",
  "error_code": "save_invariant_failed",
  "diagnostic_bundle": "not_attached",
  "consent": "not_requested"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** Le ticket est routé vers la bonne procédure.
- **Versions :** Source et cible cadrent la reproduction.
- **Phase :** Le défaut est localisé dans la transaction.
- **Code :** Une valeur structurée évite le seul message libre.
- **Données :** Aucune pièce jointe n’est supposée collectée.

## 36. Modèle Steam : branches et promotion de builds

Steamworks permet d’associer des builds à une branche par défaut ou à des branches bêta publiques ou privées. La documentation officielle précise qu’un build téléversé n’est pas automatiquement rendu actif sur la branche par défaut : la mise en ligne du build est une décision distincte. Ce modèle illustre la séparation entre upload, association à un canal et activation.

Le chapitre ne fige pas les noms de menus ni les permissions, qui restent volatils. Le registre du chapitre 17 conserve la vérification du portail authentifié. Une branche bêta ne devient pas une preuve de compatibilité ou de qualité ; elle fournit seulement un canal de distribution.

> **[WEB] Vérification à effectuer dans Steamworks avant promotion — procédure navigateur.**

- confirmer la branche cible et son audience ;
- vérifier l’identité du build déjà qualifié ;
- prévisualiser le changement avant activation ;
- conserver le reçu et l’instant de mise en ligne ;
- ne pas supposer qu’un upload a modifié la branche par défaut.

## 37. Modèle itch.io : canaux et patches générés par butler

Le manuel officiel de `butler` décrit des pushes successifs vers un canal et la génération de patches entre builds. Le backend peut remplacer ensuite le patch initial par une version optimisée, tandis que le build est déjà disponible. Ce modèle montre que le transport différentiel peut être géré par la plateforme sans changer l’identité logique du build cible.

Une nouvelle poussée sur le même canal met à jour ce canal. Le projet doit donc réserver les canaux, vérifier la cible et éviter d’utiliser un canal public comme environnement de test improvisé. Les limites et comportements actuels sont relus avant opération réelle.

> **[LECTURE] Commande butler candidate — Exemple documentaire uniquement.**

```text
butler push build/windows studio/asteria:windows-beta --userversion 1.4.2
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** `build/windows` représente un package fermé du chapitre 16.
- **Cible :** Le projet et le canal sont explicites.
- **Version :** `--userversion` aide l’affichage sans remplacer l’identité interne.
- **Réserve :** La commande n’est pas exécutée et exige authentification, page et canal réels.

## 38. Modèle Google Play : tracks et déploiements par étapes

Google Play distingue les canaux de test et la production. Son déploiement par étapes s’applique aux mises à jour, expose un pourcentage choisi de la population et peut être interrompu. La documentation précise que les utilisateurs ayant déjà reçu la version interrompue la conservent ; l’arrêt empêche surtout de nouvelles expositions.

Cette propriété confirme l’invariant du chapitre : **halt n’est pas downgrade**. Le projet prépare donc un hotfix ou une stratégie de support pour la population déjà mise à jour. Les pourcentages, territoires et permissions sont qualifiés dans le portail au moment réel.

> **[APP] Contrôle à effectuer dans l’application Play Console avant élargissement.**

L’opérateur vérifie le track, le build, le pourcentage actuel, les pays concernés, l’historique du rollout et les signaux de release. Une interruption est consignée avec l’identité de la population déjà exposée et le plan de correction.

## 39. Modèle Apple : publication progressive d’une mise à jour

App Store Connect propose une publication progressive des mises à jour éligibles sur plusieurs jours pour les mises à jour automatiques. La documentation officielle indique qu’elle peut être suspendue et reprise, tandis qu’un utilisateur peut toujours télécharger manuellement la version disponible. La population réelle n’est donc pas équivalente au seul palier automatique.

Le projet enregistre la version, le jour de progression, les pauses, les téléchargements manuels possibles et les signaux observés. La décision d’arrêt ou de publication générale ne repose pas uniquement sur le calendrier de la plateforme.

> **[WEB] Vérification à effectuer dans App Store Connect — procédure navigateur.**

- confirmer que la version est une mise à jour éligible ;
- vérifier le statut de revue et de distribution ;
- distinguer progression automatique et téléchargement manuel ;
- enregistrer pause, reprise ou généralisation ;
- préparer un nouveau build corrigé lorsqu’un retour simple n’est pas disponible.

## 40. Modèle de launcher auto-hébergé

Un launcher propriétaire augmente fortement la surface de sécurité et de support. Il doit vérifier TLS, provenance, signature, manifestes, tailles, chemins, reprise, permissions et activation atomique. Il ne doit pas exécuter une commande fournie par le manifeste ni télécharger vers un chemin arbitraire.

La confiance initiale, la rotation des clés, la révocation et la mise à jour du launcher lui-même sont des problèmes séparés. Pour un studio sans nécessité démontrée, une plateforme gérée réduit souvent le risque opérationnel.

> **[VSC] Validation candidate d’un manifeste en Python.**

```python
from __future__ import annotations

from pathlib import Path
from typing import Any

ALLOWED_ROOT = Path("staging").resolve()

def validate_entry(entry: dict[str, Any]) -> Path:
    relative = Path(str(entry["path"]))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("unsafe path")
    resolved = (ALLOWED_ROOT / relative).resolve()
    if ALLOWED_ROOT not in resolved.parents:
        raise ValueError("path escapes staging")
    if int(entry["size"]) < 0:
        raise ValueError("invalid size")
    return resolved
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Types :** Le dictionnaire est traité comme une entrée non fiable.
- **Racine :** Tous les chemins sont confinés au staging.
- **Traversée :** Chemins absolus et segments `..` sont rejetés.
- **Résolution :** La vérification porte sur le chemin normalisé.
- **Taille :** Une valeur négative est refusée avant toute allocation.

## 41. Prévoir les installations hors ligne et les mises à jour manuelles

Une installation hors ligne reçoit un package complet ou un lot de patch accompagné de manifestes, signatures et instructions. La procédure vérifie la version source avant application et n’exécute aucun contenu depuis un support non fiable sans validation.

Le support doit expliquer comment exporter les sauvegardes, vérifier l’espace, appliquer la mise à jour et revenir à une copie connue. Une archive téléchargée ailleurs ou copiée par un tiers n’acquiert pas automatiquement la provenance attendue.

> **[DCT] Validation à reproduire dans un conteneur de test isolé.**

Le conteneur sert uniquement à vérifier un outil de patch portable sur une copie d’installation. Il ne reçoit ni secrets de boutique, ni sauvegardes personnelles, ni accès au répertoire actif de production.

## 42. Sécuriser la chaîne de mise à jour

La chaîne de mise à jour est une surface d’exécution privilégiée. Elle applique la moindre permission, sépare signature et chiffrement, protège les clés, journalise les décisions sans exposer de secrets et refuse les manifestes non reconnus.

Une empreinte SHA-256 détecte une divergence mais ne remplace pas une signature ni une chaîne de confiance. Les clés de signature hors ligne, les identités de publication et les mécanismes de révocation sont gouvernés par les chapitres 13, 14, 16 et 17 selon leur portée.

> **[DCK] Inspection à effectuer dans Docker Desktop pour une image d’outil de patch.**

L’opérateur vérifie l’image épinglée, l’utilisateur non root, les montages en lecture seule, l’absence de socket Docker, la liste des capacités et la destination de sortie. Une image de diagnostic ne reçoit jamais les credentials de publication.

## 43. Protéger confidentialité et données personnelles

Les métriques de mise à jour peuvent révéler appareil, région, compte, comportement et sauvegardes. La collecte doit être minimisée, documentée, retenue pendant une durée justifiée et accessible uniquement aux rôles nécessaires.

Le produit privilégie les compteurs agrégés et les codes structurés. Les journaux bruts, fichiers de sauvegarde et identifiants de plateforme ne sont pas téléversés automatiquement pour « améliorer le rollback ». Le consentement et la base applicable sont qualifiés par le projet réel.

> **[LECTURE] Politique candidate de minimisation.**

```yaml
update_telemetry:
  remote_collection: disabled_by_default
  required_fields:
    - build_id
    - phase
    - error_code
  prohibited_fields:
    - access_token
    - raw_save_payload
    - full_environment
  retention: qualification_required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** La collecte distante n’est pas supposée active.
- **Minimum :** Build, phase et code suffisent souvent au premier diagnostic.
- **Interdits :** Secrets, sauvegarde brute et environnement complet sont exclus.
- **Rétention :** La durée doit être qualifiée et approuvée.

## 44. Tester depuis plusieurs versions antérieures

La campagne minimale couvre la version immédiatement précédente, une version plus ancienne encore supportée, une installation propre, une mise à jour interrompue et une version non supportée. Chaque cas vérifie fichiers, sauvegardes, réglages, contenu, réseau, accessibilité et localisation concernés.

Les fixtures sont des copies anonymisées ou synthétiques. Une même sauvegarde n’est pas réutilisée mutée entre scénarios. Les tests conservent source, cible, schéma, résultat, journaux et empreintes.

> **[VSC] Matrice candidate de tests de mise à jour.**

```yaml
update_tests:
  - id: previous-to-target
    from_build: 1839
    to_build: 1842
    expected: success
  - id: older-supported-to-target
    from_build: 1810
    to_build: 1842
    expected: success_via_full_package
  - id: unsupported-source
    from_build: 1700
    to_build: 1842
    expected: safe_refusal
  - id: interrupted-migration
    from_build: 1839
    to_build: 1842
    expected: recovery_without_unique_copy_loss
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** Chaque scénario peut être rejoué.
- **Ancienne version :** Le chemin package complet est testé séparément.
- **Refus :** Une source non supportée doit préserver les données.
- **Interruption :** La reprise protège l’unique copie autoritaire.

## 45. Exécuter un exercice de rollback

Un exercice utilise un environnement isolé, un build précédent retenu, des copies de données et une procédure horodatée. Il mesure le temps réel de détection, décision, interruption, activation et validation, sans transformer ces mesures en promesses universelles.

L’exercice inclut un cas où le rollback binaire est interdit par le schéma de données. Le résultat attendu est alors un blocage contrôlé et un roll-forward, non un retour forcé.

> **[LECTURE] Scénarios candidats d’exercice.**

```markdown
| Scénario | Attente |
|---|---|
| défaut visuel sans migration | rollback binaire possible après validation |
| crash au premier lancement | interruption puis analyse du staging |
| migration irréversible réussie | rollback binaire bloqué |
| migration interrompue | reprise idempotente ou restauration de copie |
| build précédent indisponible | roll-forward et communication |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variété :** Les scénarios couvrent binaire, activation et données.
- **Blocage :** L’absence de rollback sûr est un résultat valide.
- **Reprise :** La procédure choisit entre idempotence et copie.
- **Indisponibilité :** La rétention du build précédent est elle-même testée.

## 46. Injecter des défaillances contrôlées

Les essais peuvent couper le réseau, remplir le disque de staging, verrouiller un fichier, corrompre un fragment, interrompre la migration ou rendre un service incompatible. Ils sont exécutés uniquement sur copies et environnements autorisés.

L’injection s’arrête dès qu’elle risque de toucher des données réelles, une boutique publique ou un compte non dédié. Chaque faute attend un code, un état durable et une reprise définie.

> **[LECTURE] Plan candidat d’injection de fautes.**

```yaml
fault_injection:
  - fault: network_cut_during_download
    expected_state: downloading
    recovery: resume_verified_ranges
  - fault: disk_full_during_staging
    expected_state: recovery_required
    recovery: clean_staging_preserve_active
  - fault: process_kill_during_migration
    expected_state: migration_started
    recovery: inspect_journal_then_resume_or_restore
scope: isolated_copy_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Téléchargement :** La coupure conserve les plages vérifiées.
- **Disque :** Le nettoyage ne touche pas la version active.
- **Migration :** Le journal décide de la reprise.
- **Portée :** Aucune installation réelle n’est ciblée.

## 47. Définir des métriques et objectifs candidats

Les mesures utiles incluent taux de téléchargement réussi, temps de staging, échec d’intégrité, échec de migration, démarrage après activation, demandes support et temps de décision d’incident. Elles sont segmentées par build, plateforme et canal avec une cardinalité bornée.

Les objectifs restent candidats tant qu’aucune campagne n’existe. Un tableau vide ne signifie pas zéro incident. Les métriques servent à décider et apprendre ; elles ne déclenchent pas seules une suppression de données ou un rollback.

> **[LECTURE] Catalogue candidat de métriques.**

```yaml
metrics:
  - name: update_integrity_failures_total
    labels: [build_id, platform, channel]
  - name: update_migration_failures_total
    labels: [from_schema, to_schema, error_code]
  - name: update_activation_duration_seconds
    labels: [build_id, platform]
objectives:
  qualification_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Compteurs :** Les échecs d’intégrité et de migration sont séparés.
- **Labels :** Les dimensions restent bornées et sans identifiant joueur.
- **Durée :** L’activation est mesurée indépendamment du téléchargement.
- **Objectifs :** Aucun seuil n’est présenté comme mesuré.

## 48. Construire une porte go/no-go

La décision rassemble preuve du build, chemins de mise à jour, migrations, sauvegardes, compatibilité, sécurité, plateforme, accessibilité, localisation, support, communication et rollback. Chaque réserve possède un propriétaire et une disposition.

Un `go` ne signifie pas absence de risque ; il signifie que les risques connus sont acceptés par les rôles compétents et que les procédures d’arrêt et de récupération sont prêtes. Un `no-go` préserve les artefacts et résultats pour correction.

> **[LECTURE] Dossier candidat de décision.**

```yaml
decision:
  build_id: asteria-win64-1842
  update_paths: passed_static_review
  migrations: passed_static_review
  rollback_drill: not_executed
  platform_portals: not_configured
  support: planned
  communication: draft
  outcome: no_go
  reason: runtime_evidence_missing
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Build :** La décision vise une identité précise.
- **Preuves :** La revue statique est distinguée de l’exécution.
- **Rollback :** L’exercice non exécuté reste visible.
- **Portails :** Aucune configuration n’est inventée.
- **Issue :** `no_go` est cohérent avec les réserves runtime.

## 49. Procédure Solo

En mode Solo, une personne peut cumuler développement, QA, release et support, mais elle sépare les décisions dans le temps et conserve les preuves. Le flux recommandé est : figer le candidat, préparer une copie de l’installation et des sauvegardes, tester chaque chemin supporté, documenter rollback et roll-forward, publier d’abord sur un canal limité, observer, puis élargir manuellement.

Le créateur Solo limite les plateformes et versions sources réellement supportées. Une matrice courte et prouvée vaut mieux qu’une promesse large impossible à tester. Les notes de version et la procédure de support sont préparées avant l’activation stable.

> **[LECTURE] Tableau de responsabilités Solo.**

```markdown
| Moment | Rôle porté | Preuve conservée |
|---|---|---|
| préparation | développeur | diff, manifeste, migrations |
| qualification | testeur | matrice source-cible, résultats |
| décision | release manager | go/no-go signé |
| incident | support | ticket, build, action |
| clôture | mainteneur | rapport et réserves |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** Une personne change explicitement de rôle.
- **Préparation :** Le diff ne remplace pas les tests.
- **Décision :** Le go/no-go reçoit une trace distincte.
- **Incident :** Le support ne modifie pas directement les données.
- **Clôture :** Le rapport alimente la maintenance du chapitre 22.

## 50. Procédure Studio

En Studio, les responsabilités sont réparties entre release, build, QA, données, sécurité, plateforme, support, communication et produit. Le responsable d’incident peut interrompre la diffusion, mais une restauration de données exige les propriétaires compétents.

Les environnements et credentials sont séparés. Les plateformes reçoivent le même candidat qualifié selon leurs contraintes. Les décisions de poursuite utilisent une réunion ou un mécanisme d’approbation court, documenté et disponible hors des personnes uniques.

> **[LECTURE] Matrice RACI candidate.**

```markdown
| Activité | Release | QA | Données | Support | Communication |
|---|---|---|---|---|---|
| promouvoir bêta | A | R | C | I | I |
| approuver migration | C | C | A/R | I | I |
| interrompre diffusion | A/R | C | C | I | I |
| restaurer données | C | C | A/R | C | I |
| publier incident | A | I | C | C | R |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilité :** `R` exécute et `A` assume la décision.
- **Consultation :** QA et données interviennent avant promotion.
- **Interruption :** La décision peut être rapide sans supprimer les expertises.
- **Communication :** Le message public reste coordonné avec les faits techniques.

## 51. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` utilise des identités séparées pour produit, build, contenu, sauvegarde et protocole. Les canaux interne, bêta et stable sont des politiques de promotion ; un build ne change pas d’identité pendant son passage entre canaux. Les packages fermés et manifestes viennent du chapitre 16, la publication initiale du chapitre 17, les sauvegardes indépendantes du chapitre 15 et les artefacts CI du chapitre 14.

Toute mise à jour passe par préflight, staging, vérification, activation, migration et observation. Les sauvegardes sont copiées avant migration, les étapes publiées restent immuables et les chemins source-cible sont explicitement testés. Une interruption limite les nouvelles expositions mais ne rétrograde pas les installations déjà mises à jour.

Le choix entre rollback, roll-forward, désactivation et restauration dépend de la compatibilité des données. Aucun retour binaire n’est autorisé lorsque le build cible ne sait pas lire le schéma courant. Les notes de version, messages d’incident, support, métriques et décisions restent corrélés au build.

Aucun package de patch, canal, migration, sauvegarde pré-migration, test depuis une version antérieure, déploiement progressif, interruption, rollback, hotfix, communication publique, opération de boutique, exécution runtime ou PDF du Livre IV n’est revendiqué.

## 52. Diagnostics : dix erreurs fréquentes

Chaque diagnostic suit la même séquence : symptôme, contre-exemple, explication, correction et justification. Les extraits sont conceptuels et doivent être adaptés aux outils réellement qualifiés.

### 52.1 Remplacer l’installation active pendant le téléchargement

**Symptôme :** L’installation devient inutilisable après une coupure réseau.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
download(target, install_root)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le téléchargement écrit directement dans la génération active.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
download(target, staging_root); verify(); activate()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le staging isolé permet de vérifier puis d’activer sans altérer l’ancien build.

### 52.2 Appliquer un delta à une base inconnue

**Symptôme :** Le patch réussit partiellement puis produit des fichiers incohérents.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
apply_patch(current_files, delta_1839_1842)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le patch suppose une base sans vérifier son identité.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
assert build_id == 1839; apply_patch(copy, delta); verify_target(1842)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La base et l’état cible sont vérifiés avant activation.

### 52.3 Confondre interruption et rétrogradation

**Symptôme :** Le support annonce un rollback alors que les joueurs conservent la version.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
platform.halt(); status = "rolled_back"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’arrêt de diffusion ne modifie pas les installations déjà exposées.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
platform.halt(); status = "new_exposure_stopped"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le statut décrit exactement l’effet obtenu.

### 52.4 Revenir au binaire précédent après migration irréversible

**Symptôme :** L’ancienne version refuse ou corrompt une sauvegarde récente.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
activate(build_1839)  # save schema is 12
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le build précédent ne comprend pas le schéma courant.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
block_binary_rollback(); prepare_roll_forward(build_1843)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le roll-forward conserve la compatibilité des données.

### 52.5 Modifier une migration déjà publiée

**Symptôme :** Deux installations portant le même schéma obtiennent des états différents.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
migrations["11->12"] = revised_function
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’historique d’exécution devient non reproductible.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
register("12->13", corrective_migration)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Une nouvelle étape conserve l’immutabilité des migrations publiées.

### 52.6 Écraser la copie pré-migration

**Symptôme :** La seule source de restauration disparaît lors d’un second essai.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
copy(save, "backup.save", overwrite=true)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le nom fixe et l’écrasement détruisent la génération précédente.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
create_unique_verified_backup(save, transaction_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Une identité de transaction et une empreinte protègent chaque copie.

### 52.7 Promouvoir un build reconstruit

**Symptôme :** La version stable diffère de celle testée en bêta.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
build_again(); publish(stable)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La reconstruction produit une nouvelle identité non qualifiée.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
promote(qualified_build_id, from="beta", to="stable")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La promotion conserve le candidat et ses preuves.

### 52.8 Retenter indéfiniment une erreur de schéma

**Symptôme :** Le launcher boucle et empêche toute intervention.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
while not migrate(): retry()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Une erreur déterministe ne devient pas transitoire par répétition.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
if schema_error: enter_recovery_required()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** L’état de récupération arrête la boucle et préserve les preuves.

### 52.9 Collecter la sauvegarde brute automatiquement

**Symptôme :** Des données personnelles ou narratives sont envoyées sans gouvernance.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
upload(save_file, logs, environment)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le diagnostic maximal viole la minimisation.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
collect(build_id, phase, error_code); request_consent_for_more()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le premier niveau collecte uniquement les champs nécessaires.

### 52.10 Déclarer zéro incident depuis un tableau vide

**Symptôme :** Le déploiement est élargi sans preuve de remontée fonctionnelle.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
if dashboard.count == 0: promote()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’absence de données est interprétée comme un succès.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
if telemetry_qualified and window_complete: review_then_decide()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La qualification de la collecte et une revue humaine précèdent la décision.

## 53. Checklist Solo

- [ ] séparer versions produit, build, contenu, données et protocole ;
- [ ] définir canaux, audiences et propriétaires ;
- [ ] conserver packages et manifestes des builds précédent et cible ;
- [ ] documenter chaque version source supportée ;
- [ ] créer et vérifier une copie avant migration ;
- [ ] tester package complet, delta, interruption et reprise ;
- [ ] qualifier compatibilité binaire et données avant rollback ;
- [ ] préparer hotfix, notes de version et messages d’incident ;
- [ ] observer un canal limité avant stable ;
- [ ] archiver décision, résultats, réserves et reçus.

## 54. Checklist Studio

- [ ] nommer release manager, incident commander et propriétaires de données ;
- [ ] versionner stratégies de canaux et matrices de compatibilité ;
- [ ] promouvoir le même candidat entre environnements ;
- [ ] séparer credentials, permissions et plateformes ;
- [ ] automatiser intégrité, préflight, staging et preuves ;
- [ ] exécuter la matrice depuis plusieurs versions antérieures ;
- [ ] exercer rollback, roll-forward et restauration sur copies ;
- [ ] corréler métriques, support et communication au build ;
- [ ] imposer approbation pour interruption et restauration ;
- [ ] transmettre au chapitre 22 les builds, outils et rapports à archiver.

## 55. Critères d’acceptation documentaire

Le chapitre passe au niveau documentaire lorsque les cinq objectifs et livrables du plan maître sont couverts, les frontières sont explicites, les chemins de mise à jour et de migration sont documentés, les dix diagnostics sont complets, les repères sont cohérents et aucune revendication runtime n’est inventée.

Le niveau `runtime-tested` exigerait au minimum plusieurs installations sources réelles, packages et patches matérialisés, migrations exécutées sur copies, tests d’interruption, intégrité, observation de canaux, exercice de rollback, vérification des plateformes, support et communication. Ces preuves ne sont pas produites ici.

## 56. Références techniques officielles

- [Branches bêta — documentation Steamworks](https://partner.steamgames.com/doc/store/application/branches?l=french)
- [Pushing builds — manuel officiel butler](https://itch.io/docs/butler/pushing.html)
- [Offline diffing and patching — manuel officiel butler](https://itch.io/docs/butler/offline.html)
- [Déployer les mises à jour par étapes — aide Google Play Console](https://support.google.com/googleplay/android-developer/answer/6346149?hl=fr)
- [Préparer et déployer une version — aide Google Play Console](https://support.google.com/googleplay/android-developer/answer/9859348?hl=fr)
- [Release a version update in phases — Apple Developer](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases)
- [FileAccess — documentation stable de Godot](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html)
- [DirAccess — documentation stable de Godot](https://docs.godotengine.org/en/stable/classes/class_diraccess.html)
- [File and data I/O — documentation stable de Godot](https://docs.godotengine.org/en/stable/tutorials/io/)
- [Godot release policy — documentation stable de Godot](https://docs.godotengine.org/en/stable/about/release_policy.html)

## 57. Conclusion

Une mise à jour sûre n’est pas un remplacement de fichiers, mais une transaction distribuée avec identités, préconditions, staging, vérification, migration, observation et récupération. Le canal limite l’exposition ; il ne prouve pas la qualité. Le rollback binaire ne restaure pas les données et peut être interdit après une migration irréversible.

`Project Asteria` retient donc la promotion du même candidat, des chemins source-cible explicites, une copie vérifiée avant migration, des portes d’arrêt, un roll-forward disponible et une communication factuelle. Les plateformes sont traitées comme des mécanismes de distribution à vérifier au moment réel, jamais comme une garantie de retour arrière automatique.
