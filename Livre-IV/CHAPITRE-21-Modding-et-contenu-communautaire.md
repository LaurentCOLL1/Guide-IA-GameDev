---
title: "Livre IV — Chapitre 21 : Modding et contenu communautaire"
id: "DOC-L4-CH21"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 21
last-verified: "2026-07-27T21:47:17+02:00"
audit-status: "complete"
audit-date: "2026-07-27T21:47:17+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-21.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Modding et contenu communautaire

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 20 possède les mises à jour officielles, migrations distribuées, hotfixes et retours arrière. Le chapitre 22 possédera la maintenance longue durée, l’archivage, la succession et la fin de vie. Le présent chapitre possède les **surfaces d’extension communautaires** : formats de mods, API publiques, règles de chargement, isolation, compatibilité, dépendances, licences, modération et support.

Le chapitre 16 conserve les packages officiels du jeu ; le chapitre 17 conserve les portails et la publication initiale ; le chapitre 19 conserve la localisation du produit. Ici, ces capacités sont consommées sans donner à un mod l’autorité de remplacer silencieusement les octets officiels, les sauvegardes canoniques ou les règles de sécurité.

Le niveau de preuve reste `static-review`. Aucun SDK, chargeur de mods, sandbox, atelier, dépôt communautaire, mod, conflit, migration, signalement ou test runtime de `Project Asteria` n’est revendiqué comme matérialisé ou exécuté.

> **[LECTURE] Carte de responsabilité — Ne pas saisir.**

```yaml
modding_scope:
  official_packages_owner: chapter-16
  initial_distribution_owner: chapter-17
  localization_owner: chapter-19
  official_updates_owner: chapter-20
  community_extensions_owner: chapter-21
  maintenance_archive_owner: chapter-22
evidence_level: static-review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorités :** Chaque étape du cycle de vie possède un propriétaire unique.
- **Frontière :** Un mod étend le produit sans devenir un patch officiel ni une sauvegarde indépendante.
- **Niveau de preuve :** La carte décrit une organisation documentaire, pas une intégration réalisée.
- **Résultat attendu :** Toute demande liée aux mods est routée vers le chapitre 21 sans reprendre la publication ou la maintenance.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer mod, contenu généré par les utilisateurs, plugin, DLC et patch officiel ;
- choisir des surfaces d’extension compatibles avec le niveau de risque accepté ;
- définir un manifeste, des identifiants stables et des versions d’API ;
- résoudre dépendances, conflits et ordre de chargement de manière déterministe ;
- installer, valider, activer, désactiver et diagnostiquer un mod sans modifier l’installation officielle ;
- protéger chemins, archives, quotas, sauvegardes, réseau et processus ;
- préparer SDK, templates, documentation et mod d’exemple ;
- gérer licences, provenance, redistribution, modération et support ;
- tester ensembles de mods, migrations, multijoueur et localisation ;
- diagnostiquer dix erreurs fréquentes de modding.

## 3. Vocabulaire opérationnel

Un **mod** est un lot communautaire qui utilise une surface d’extension explicitement publiée par le jeu. Un **contenu généré par les utilisateurs**, ou UGC, couvre aussi des créations qui ne modifient pas le jeu : cartes, captures, niveaux, traductions, presets ou médias. Un **plugin** exécute généralement du code dans un hôte ; il possède donc un risque supérieur à un pack de données. Un **DLC** ou un **patch officiel** est produit, signé et distribué sous l’autorité de l’éditeur : il ne devient pas un mod parce qu’il utilise un PCK.

Une **surface d’extension** est un contrat volontairement exposé : catalogue d’objets, format de quête, table de localisation, événement public ou API bornée. Une **capacité** est une permission fonctionnelle accordée à un mod. Un **namespace** est un préfixe stable qui évite les collisions. Un **ensemble de mods** est la liste ordonnée des mods actifs, avec leurs versions et empreintes.

## 4. Modèle mental : une extension est une entrée non fiable

Le modding n’est pas « charger un dossier ». Il introduit des données, assets et parfois du code produits hors de la chaîne officielle. Même un mod bien intentionné peut être incompatible, mal emballé, excessif en mémoire, destructeur pour une sauvegarde ou dépendant d’un autre mod absent.

La stratégie de `Project Asteria` part donc de trois principes :

1. **les données communautaires sont non fiables jusqu’à validation** ;
2. **les autorités métier restent dans le jeu officiel** ;
3. **l’activation est réversible tant qu’aucune migration irréversible n’a été approuvée**.

> **[LECTURE] Niveaux de support candidats — Exemple de référence.**

```yaml
support_tiers:
  tier_0:
    name: disabled
    content: none
  tier_1:
    name: declarative
    content:
      - json_catalogs
      - localized_text
      - approved_runtime_assets
  tier_2:
    name: packaged_resources
    content:
      - namespaced_pck_or_zip
    review: required
  tier_3:
    name: executable_code
    content:
      - gdscript
      - native_extensions
    public_support: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tier 0 :** Le produit fonctionne sans mod et conserve toujours ce chemin de repli.
- **Tier 1 :** Les formats déclaratifs utilisent des schémas et des opérations autorisées.
- **Tier 2 :** Les packs Godot facilitent les ressources mais exigent namespace, ordre et revue renforcée.
- **Tier 3 :** GDScript et extensions natives sont du code exécutable ; ils ne sont pas présentés comme sandboxés.
- **Résultat attendu :** Le niveau de support dépend du risque, pas de la popularité d’un format.

## 5. Choisir les surfaces d’extension

Une bonne surface expose une intention stable, pas une classe interne. Par exemple, « ajouter une définition d’objet » est plus durable que « instancier `InventoryItemNodeV3` ». Le jeu valide les données puis les transforme en commandes métier officielles.

Les surfaces candidates de `Project Asteria` sont :

- catalogues de définitions namespacées ;
- quêtes et dialogues exprimés dans une grammaire fermée ;
- tables de localisation ;
- thèmes, icônes, textures, audio et modèles chargés par des lecteurs bornés ;
- événements publics en lecture seule ;
- commandes déclaratives traduites par un adaptateur officiel.

Les surfaces exclues par défaut sont l’accès arbitraire au système de fichiers, au réseau, aux processus, aux secrets, aux objets serveur et aux dépôts de sauvegarde.

## 6. Concevoir un manifeste canonique

Le manifeste est lu avant tout autre fichier. Il porte l’identité, les versions, les dépendances, les capacités demandées, les points d’entrée, les licences et les empreintes. Il est encodé en UTF-8 et validé contre un schéma versionné.

> **[VSC] Fichier candidat `mod/manifest.json`.**

```json
{
  "schema": "asteria-mod-manifest-v1",
  "id": "org.example.relay-expansion",
  "version": "1.2.0",
  "display_name_key": "mod.relay_expansion.name",
  "game_api": "asteria-mod-api-1",
  "game_versions": {
    "minimum": "1.4.0",
    "maximum_exclusive": "2.0.0"
  },
  "dependencies": [
    {
      "id": "org.example.shared-creatures",
      "version": ">=1.1.0 <2.0.0",
      "required": true
    }
  ],
  "conflicts": [],
  "capabilities": [
    "catalog.items.read",
    "catalog.items.extend"
  ],
  "entrypoints": {
    "items": "content/items.json",
    "translations": "localization/"
  },
  "license_expression": "CC-BY-4.0",
  "content_hashes": "hashes.sha256"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** `schema` permet au validateur de refuser une structure inconnue plutôt que de deviner.
- **Identité :** `id` est stable, en minuscules et indépendant du nom affiché.
- **Compatibilité :** `game_api` et la plage de versions du jeu sont deux contrats distincts.
- **Dépendances :** Chaque dépendance porte identité, contrainte et caractère obligatoire.
- **Capacités :** La liste exprime ce que le mod demande ; elle ne vaut pas autorisation automatique.
- **Entrées :** Les chemins sont relatifs à la racine validée du mod.
- **Licence :** Une expression SPDX est un identifiant structuré, pas une vérification juridique.
- **Intégrité :** Le fichier d’empreintes relie le manifeste au contenu distribué.

### 6.1 Identifiants stables

L’identifiant ne reprend ni le titre, ni le nom du créateur, ni le chemin d’installation. Une convention de type domaine inversé réduit les collisions : `org.auteur.nom-du-mod`. Une fois publié, cet identifiant ne change pas ; une reprise de projet conserve l’identité et met à jour les auteurs ou propriétaires.

Les identifiants internes d’un mod sont eux aussi namespacés : `org.example.relay-expansion:item:signal_flare`. Le registre officiel ne retire jamais le préfixe avant de vérifier l’unicité.

### 6.2 Versionner trois contrats

Le manifeste sépare :

- la version du mod ;
- la version de l’API de modding ;
- la plage de versions du jeu.

Une nouvelle version du jeu peut conserver l’API de modding. Inversement, une API peut évoluer sans changer toutes les données du produit. Cette séparation permet une compatibilité explicite.

## 7. Valider le manifeste avant activation

> **[VSC] Script candidat `tools/modding/validate_manifest.py`.**

```python
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)+$")
ALLOWED_CAPABILITIES = {
    "catalog.items.read",
    "catalog.items.extend",
    "localization.extend",
    "assets.runtime.read",
}

def load_json(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("manifest-root-must-be-object")
    return value

def validate_manifest(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if value.get("schema") != "asteria-mod-manifest-v1":
        errors.append("unsupported-schema")
    mod_id = value.get("id")
    if not isinstance(mod_id, str) or ID_PATTERN.fullmatch(mod_id) is None:
        errors.append("invalid-mod-id")
    capabilities = value.get("capabilities", [])
    if not isinstance(capabilities, list):
        errors.append("capabilities-must-be-array")
    else:
        unknown = sorted(set(capabilities) - ALLOWED_CAPABILITIES)
        errors.extend(f"unsupported-capability:{item}" for item in unknown)
    return errors

def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_manifest.py <manifest.json>", file=sys.stderr)
        return 2
    try:
        errors = validate_manifest(load_json(Path(argv[1])))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"manifest-read-failed:{exc}", file=sys.stderr)
        return 3
    for error in errors:
        print(error)
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** Le programme exige exactement un chemin de manifeste.
- **Décodage :** `read_text(encoding="utf-8")` et `json.loads()` séparent lecture et parsing.
- **Type racine :** Un tableau ou une valeur scalaire est refusé avant l’accès aux champs.
- **Identité :** L’expression régulière accepte des segments namespacés en minuscules.
- **Capacités :** La différence d’ensembles révèle les permissions inconnues de manière déterministe.
- **Codes de retour :** `0` signifie conforme, `1` violations de contrat, `2` usage incorrect et `3` lecture impossible.
- **Limite :** Cet extrait ne remplace pas un schéma JSON complet ni la validation des versions.

## 8. Installer par staging, jamais dans l’installation active

L’installation suit quatre espaces distincts :

1. **inbox** : archive reçue mais non fiable ;
2. **staging** : contenu extrait dans un répertoire temporaire ;
3. **validated** : lot dont le manifeste, les chemins, quotas et empreintes ont été contrôlés ;
4. **active** : lien ou copie atomique vers la version choisie.

Un échec supprime le staging et conserve la version active. Une réinstallation avec la même identité et la même version doit produire la même empreinte ou être refusée.

## 9. Protéger l’extraction des archives

Une archive ZIP peut contenir `../`, un chemin absolu, un nom réservé, des liens symboliques ou un volume décompressé disproportionné. Le validateur inspecte toutes les entrées avant d’extraire le premier octet.

> **[VSC] Script candidat `tools/modding/safe_zip.py`.**

```python
from __future__ import annotations

from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZipInfo

def normalized_member(info: ZipInfo) -> PurePosixPath:
    member = PurePosixPath(info.filename)
    if member.is_absolute():
        raise ValueError("absolute-path")
    if not member.parts or any(part in {"", ".", ".."} for part in member.parts):
        raise ValueError("unsafe-relative-path")
    if ":" in member.parts[0]:
        raise ValueError("drive-qualified-path")
    return member

def inspect_archive(path: Path) -> list[PurePosixPath]:
    members: list[PurePosixPath] = []
    with ZipFile(path, "r") as archive:
        for info in archive.infolist():
            members.append(normalized_member(info))
    return members
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **PurePosixPath :** Les noms ZIP utilisent des séparateurs de type POSIX, indépendamment de l’OS hôte.
- **Chemins absolus :** Ils sont refusés avant toute résolution locale.
- **Segments :** `..`, `.` et les segments vides empêchent une extraction hors racine.
- **Lecteur :** `infolist()` inspecte les métadonnées sans appeler `extractall()`.
- **Sortie :** La fonction renvoie seulement des chemins normalisés ; l’extraction reste une étape ultérieure.
- **Limite :** Quotas, liens symboliques, doublons de casse et taille décompressée doivent être ajoutés au validateur réel.

## 10. Définir des quotas qualifiés

Les quotas empêchent un mod de saturer disque, mémoire, VRAM ou temps de chargement. Ils portent au minimum sur :

- taille de l’archive ;
- taille décompressée cumulée ;
- nombre de fichiers ;
- profondeur des chemins ;
- dimensions et formats d’images ;
- durée et canaux audio ;
- nombre de scènes, nœuds ou entrées de catalogue ;
- complexité des modèles ;
- temps de validation et d’import.

Le chapitre ne fixe pas de nombres universels. `Project Asteria` doit mesurer ses plateformes cibles et enregistrer des valeurs candidates puis qualifiées.

> **[LECTURE] Registre de quotas — Valeurs à qualifier.**

```yaml
quota_policy:
  archive_bytes:
    status: candidate
    value: null
  expanded_bytes:
    status: candidate
    value: null
  file_count:
    status: candidate
    value: null
  image_dimensions:
    status: candidate
    value: null
  validation_duration:
    status: candidate
    value: null
decision: block_when_unqualified_for_public_channel
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs nulles :** Elles indiquent qu’aucun seuil n’est inventé dans la documentation.
- **Statut :** `candidate` distingue une intention d’un budget mesuré.
- **Porte :** Un canal public reste bloqué tant que les limites critiques ne sont pas qualifiées.
- **Résultat attendu :** Les quotas sont traçables par plateforme et version du jeu.

## 11. Charger des ressources Godot sans écrasement implicite

Godot peut charger un PCK ou un ZIP supplémentaire avec `ProjectSettings.load_resource_pack()`. La documentation officielle avertit qu’un chemin identique peut remplacer une ressource déjà présente et que l’ordre de chargement compte. Pour un mod communautaire, `Project Asteria` utilise un namespace sous `res://mods/<id>/` et passe `false` à `replace_files`.

Un PCK peut contenir scripts, scènes et assets. Cette commodité ne constitue pas une sandbox. Le niveau public par défaut n’accepte que les ressources et points d’entrée autorisés par le manifeste.

> **[VSC] Script candidat `src/modding/mod_pack_loader.gd`.**

```gdscript
class_name ModPackLoader
extends RefCounted

static func mount_pack(pack_path: String, mod_id: StringName) -> Dictionary:
    if not pack_path.is_absolute_path():
        return {"ok": false, "code": "pack-path-not-absolute"}
    if String(mod_id).is_empty():
        return {"ok": false, "code": "mod-id-empty"}

    var mounted: bool = ProjectSettings.load_resource_pack(pack_path, false)
    if not mounted:
        return {"ok": false, "code": "pack-mount-failed"}

    var root: String = "res://mods/%s/" % String(mod_id)
    return {"ok": true, "code": "mounted", "root": root}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `RefCounted` suffit car le chargeur n’a ni scène ni cycle de vie propre.
- **Chemin :** L’extrait exige un chemin absolu déjà validé par l’installateur.
- **Identité :** Un identifiant vide est refusé avant le montage.
- **Remplacement :** Le second argument `false` interdit au pack de remplacer les fichiers déjà montés.
- **Retour :** Un dictionnaire structuré sépare succès, code stable et racine attendue.
- **Limite :** Le montage réussi ne prouve pas que le pack respecte réellement son namespace ; un inventaire préalable reste obligatoire.

## 12. Préférer le chargement de fichiers runtime pour les assets simples

Pour des textures, pistes audio ou modèles fournis hors éditeur, la documentation Godot propose des chargeurs runtime. Cette approche évite d’obliger les créateurs à produire un PCK, mais elle ne bénéficie pas automatiquement de toutes les fonctions de ressources importées.

Le jeu conserve une liste fermée de formats. Il décode chaque fichier dans un espace borné, applique les quotas et transforme le résultat en objet de présentation. Un asset communautaire ne reçoit pas de référence directe vers le domaine métier.

## 13. Ne pas exécuter du code communautaire par défaut

Un script GDScript chargé avec `load()` peut être instancié et exécuter la logique du processus. Une GDExtension native possède encore davantage de privilèges. Sans isolation externe démontrée, ces formats sont traités comme du code de confiance et restent hors du support public de `Project Asteria`.

Les besoins de logique sont exprimés avec une grammaire déclarative : conditions, effets et événements appartiennent à une liste fermée. Le mod fournit des données ; l’adaptateur officiel exécute les opérations autorisées.

> **[LECTURE] Grammaire d’effet communautaire — Exemple conceptuel.**

```json
{
  "effect_id": "org.example.relay-expansion:effect:restore_signal",
  "trigger": "quest.objective.completed",
  "conditions": [
    {
      "op": "flag_equals",
      "flag": "relay.powered",
      "value": true
    }
  ],
  "actions": [
    {
      "op": "grant_item",
      "item_id": "asteria.core:item:signal_token",
      "quantity": 1
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** L’effet communautaire est namespacé.
- **Déclencheur :** Il vise un événement public documenté, pas un signal interne arbitraire.
- **Conditions :** `op` sélectionne une opération officielle et validée.
- **Actions :** Le mod demande une commande ; le service métier conserve l’autorité de l’accepter.
- **Quantité :** La valeur reste une donnée contrôlée par les règles du jeu.
- **Résultat attendu :** Aucun nom de méthode, chemin de script ou expression exécutable n’est fourni par le mod.

## 14. Publier une API minimale et versionnée

Une API de modding est une surface de compatibilité publique. Elle ne doit pas exposer toutes les classes internes. Elle publie :

- types de données stables ;
- événements documentés ;
- commandes déclaratives ;
- codes de refus ;
- limites et quotas ;
- politique de dépréciation ;
- exemples et tests de contrat.

Une API retirée sans préavis brise l’écosystème. Une API conservée indéfiniment peut bloquer l’architecture. Le contrat prévoit donc des versions majeures, une période de dépréciation et un diagnostic explicite.

## 15. Définir les capacités et l’autorisation

Le manifeste demande des capacités. Le validateur décide si elles existent, si le canal les autorise et si l’utilisateur doit consentir. Une capacité inconnue est refusée ; elle n’est jamais ignorée silencieusement.

> **[VSC] Script candidat `src/modding/mod_capability_policy.gd`.**

```gdscript
class_name ModCapabilityPolicy
extends RefCounted

const PUBLIC_CAPABILITIES: Dictionary = {
    &"catalog.items.read": true,
    &"catalog.items.extend": true,
    &"localization.extend": true,
    &"assets.runtime.read": true,
}

static func evaluate(requested: Array[StringName]) -> Dictionary:
    var denied: Array[StringName] = []
    for capability: StringName in requested:
        if not PUBLIC_CAPABILITIES.has(capability):
            denied.append(capability)
    denied.sort()
    return {
        "allowed": denied.is_empty(),
        "denied": denied,
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Allowlist :** Le dictionnaire contient uniquement les capacités publiques reconnues.
- **Entrée typée :** `Array[StringName]` évite les valeurs hétérogènes.
- **Refus fermé :** Toute capacité absente est ajoutée à `denied`.
- **Tri :** L’ordre stable rend les rapports reproductibles.
- **Retour :** `allowed` résume la décision tandis que `denied` conserve le diagnostic.
- **Limite :** La politique réelle devra aussi dépendre du canal, de la plateforme et du consentement.

## 16. Interdire les chemins, réseau et processus arbitraires

Les mods publics n’obtiennent pas :

- `OS.execute()` ou équivalent ;
- sockets ou requêtes réseau libres ;
- lecture de l’environnement ;
- accès aux secrets ou identifiants de plateforme ;
- écriture hors d’un répertoire de données namespacé ;
- chargement de bibliothèques natives ;
- accès direct aux sauvegardes globales.

Un besoin réel est transformé en service étroit. Par exemple, une ressource distante passe par un catalogue officiel, une allowlist d’hôtes, une politique de cache et un consentement explicite. Ce service n’est pas fourni dans la première version candidate.

## 17. Organiser le répertoire d’un mod

> **[LECTURE] Arborescence de template — Exemple de référence.**

```text
org.example.relay-expansion/
├── manifest.json
├── hashes.sha256
├── README.md
├── LICENSES/
│   ├── content.txt
│   └── third-party-notices.md
├── content/
│   ├── items.json
│   ├── quests.json
│   └── dialogue.json
├── localization/
│   ├── fr-FR.csv
│   └── en-GB.csv
├── assets/
│   ├── textures/
│   └── audio/
└── tests/
    └── expected-validation.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** Le dossier reprend l’identifiant stable du manifeste.
- **Intégrité :** `hashes.sha256` couvre les fichiers distribués.
- **Licences :** Les droits du mod et des dépendances tierces sont séparés.
- **Contenu :** Les catalogues déclaratifs restent distincts des assets.
- **Localisation :** Les locales utilisent les conventions du chapitre 19.
- **Tests :** Le créateur peut fournir les résultats attendus sans prétendre qu’ils ont été exécutés par le jeu.

## 18. Découvrir les mods de manière déterministe

La découverte lit uniquement les racines configurées. Elle ignore les fichiers cachés, liens inattendus et dossiers sans manifeste. Les candidats sont d’abord triés par identifiant, puis validés. L’ordre du système de fichiers ne devient jamais l’ordre de chargement.

Le répertoire `user://mods/` est une convention candidate. Sur une plateforme gérée, un adaptateur peut fournir une autre racine, mais il produit le même modèle de candidat.

## 19. Résoudre les dépendances comme un graphe

Chaque dépendance obligatoire doit exister et satisfaire sa contrainte. Les cycles sont refusés. Les dépendances optionnelles sont enregistrées mais ne rendent pas l’ensemble invalide lorsqu’elles manquent. Un ordre topologique place les dépendances avant leurs consommateurs.

> **[LECTURE] Résultat de résolution — Exemple de référence.**

```yaml
mod_set:
  requested:
    - org.example.relay-expansion@1.2.0
  resolved:
    - org.example.shared-creatures@1.4.1
    - org.example.relay-expansion@1.2.0
  optional_missing:
    - org.example.photo-mode-bridge
  conflicts: []
  cycles: []
  decision: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Demandé :** La sélection de l’utilisateur est distinguée de la fermeture des dépendances.
- **Résolu :** L’ordre place la bibliothèque avant le mod consommateur.
- **Optionnel :** Une absence est visible sans bloquer automatiquement.
- **Conflits et cycles :** Des listes séparées évitent de réduire toutes les causes à un message générique.
- **Décision :** `candidate` interdit de confondre calcul documentaire et activation réelle.

## 20. Gérer les contraintes de versions

Une contrainte n’est pas interprétée par une comparaison lexicographique. `1.10.0` est supérieur à `1.9.0` malgré l’ordre des chaînes. Le SDK doit adopter une grammaire documentée et un parseur unique. Le manifeste conserve la contrainte source et le résolveur produit une décision détaillée.

Les versions flottantes comme `latest` sont interdites dans un ensemble reproductible. Un atelier peut télécharger une version plus récente, mais l’activation enregistre la version exacte et son empreinte.

## 21. Calculer un ordre de chargement stable

L’ordre final combine :

1. dépendances obligatoires ;
2. contraintes explicites `load_after` ou `load_before` si elles ne créent pas de cycle ;
3. priorité de canal éventuellement qualifiée ;
4. identifiant du mod comme départage déterministe.

Le nombre de téléchargements, la date locale et l’ordre d’énumération des dossiers ne participent pas au calcul.

## 22. Détecter les conflits avant le chargement

Un conflit apparaît lorsqu’au moins deux mods revendiquent la même identité de contenu, un chemin exclusif, une capacité incompatible ou une modification non fusionnable. Le système produit un rapport, puis applique une politique explicite : blocage, choix utilisateur, règle de priorité publiée ou fusion déterministe.

Le silence n’est pas une résolution. Une victoire « du dernier chargé » sans explication rend les sauvegardes et rapports non reproductibles.

> **[VSC] Format candidat `reports/mod-conflicts.json`.**

```json
{
  "schema": "asteria-mod-conflicts-v1",
  "mod_set_id": "candidate-set-2026-07-27",
  "conflicts": [
    {
      "code": "duplicate-content-id",
      "resource_id": "asteria.core:item:signal_token",
      "claimants": [
        "org.example.relay-expansion@1.2.0",
        "org.example.signal-overhaul@2.0.1"
      ],
      "resolution": "blocked"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** Le rapport peut évoluer sans casser les outils consommateurs.
- **Ensemble :** `mod_set_id` relie le conflit à une sélection précise.
- **Code :** Le diagnostic est stable et traduisible.
- **Ressource :** L’identité contestée est explicitement nommée.
- **Réclamants :** Les versions exactes permettent de reproduire le cas.
- **Résolution :** `blocked` évite une priorité implicite.

## 23. Fusionner seulement les données conçues pour l’être

Une fusion est possible si le format définit :

- une clé d’identité ;
- des champs remplaçables ou appendables ;
- une règle d’ordre ;
- un comportement pour les valeurs absentes ;
- une stratégie de conflit ;
- une validation après fusion.

Les scènes, scripts ou ressources opaques ne sont pas fusionnés par heuristique. Pour les catalogues, le registre officiel peut accepter l’ajout d’entrées namespacées et refuser la modification d’une entrée `asteria.core`.

## 24. Installer, activer, désactiver et désinstaller

**Installer** place une version validée dans le stockage. **Activer** l’ajoute à l’ensemble de mods du profil. **Désactiver** la retire de l’ensemble sans effacer son état. **Désinstaller** retire les fichiers après vérification des profils et sauvegardes qui y font référence.

Ces opérations sont distinctes. La désactivation doit rester possible après un échec de chargement, avec un démarrage en mode sûr.

## 25. Préparer un mode sûr

Le jeu conserve le dernier ensemble connu comme démarrable. Après un crash précoce ou un échec de validation, il propose :

- démarrage sans mods ;
- retour au dernier ensemble connu ;
- désactivation du dernier mod activé ;
- export d’un rapport expurgé ;
- ouverture du dossier de mods.

Le mode sûr ne détruit ni fichiers ni données communautaires sans action explicite.

## 26. Intégrer les sauvegardes sans compromettre l’état canonique

Chaque sauvegarde enregistre :

- l’ensemble de mods actif ;
- versions et empreintes ;
- version de l’API de modding ;
- namespaces d’état communautaire ;
- dépendances requises pour charger ;
- migrations de mod déjà appliquées.

Le jeu officiel conserve l’autorité de la structure globale. Un mod écrit uniquement dans son namespace. Une absence de mod produit un diagnostic et un mode dégradé lorsque le contrat le permet ; elle ne provoque pas une suppression automatique.

> **[LECTURE] Enveloppe de sauvegarde moddée — Exemple conceptuel.**

```json
{
  "save_schema": 8,
  "game_build": "1.5.0+1904",
  "mod_api": "asteria-mod-api-1",
  "mod_set": [
    {
      "id": "org.example.relay-expansion",
      "version": "1.2.0",
      "sha256": "candidate"
    }
  ],
  "mod_state": {
    "org.example.relay-expansion": {
      "schema": 2,
      "payload": {
        "relay_restored": true
      }
    }
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma global :** Il reste sous l’autorité du jeu officiel.
- **Build et API :** Ils facilitent le diagnostic de compatibilité.
- **Ensemble :** Chaque mod porte version et empreinte attendue.
- **Namespace :** `mod_state` sépare les données des créateurs.
- **Schéma local :** Le mod versionne son propre payload sans modifier la racine.
- **Empreinte candidate :** L’exemple ne prétend pas fournir un hash réel.

## 27. Migrer l’état d’un mod

Une migration de mod suit les règles du chapitre 20 : chemins source-cible fermés, scripts immuables après publication, copie préalable et reprise. Le chargeur officiel orchestre la transaction ; le mod ne reçoit pas l’accès brut au fichier de sauvegarde.

Une migration irréversible peut bloquer le retour à une ancienne version du mod. Cette contrainte apparaît avant activation et dans le rapport de compatibilité.

## 28. Déprécier une API sans casser silencieusement

Une dépréciation documente :

- symbole ou format concerné ;
- première version marquée ;
- remplacement ;
- dernière version garantie ;
- diagnostic émis ;
- exemples de migration.

Le jeu peut conserver un adaptateur temporaire. Lorsqu’il est retiré, le chargeur refuse le mod avec un code précis au lieu de laisser une erreur tardive.

## 29. Intégrer localisation et accessibilité

Un mod ne remplace pas les clés officielles. Ses clés sont namespacées et ses catalogues passent par les contrôles du chapitre 19 : variables, pluriels, écritures, polices et pseudo-localisation.

La politique communautaire demande également :

- texte alternatif pour les aperçus lorsque la plateforme le permet ;
- sous-titres ou transcription pour les contenus audio critiques ;
- absence d’information portée uniquement par la couleur ;
- avertissements et options pour mouvement ou flashs ;
- navigation et commandes compatibles avec les réglages du jeu.

Ces exigences ne transforment pas un contrôle automatique en certification.

## 30. Encadrer le multijoueur

Le serveur ou l’hôte autoritaire décide de l’ensemble de mods autorisé. Les clients transmettent l’identité, la version et l’empreinte de leur ensemble ; un écart produit refus, téléchargement guidé ou mode spectateur selon la politique.

Les mods cosmétiques clients doivent être séparés des contenus qui affectent collisions, économie, IA, quêtes ou sauvegardes. Un mod local ne peut pas envoyer une nouvelle commande métier au serveur simplement parce qu’il est actif sur le client.

> **[LECTURE] Poignée d’ensemble de mods — Exemple conceptuel.**

```yaml
session_mod_contract:
  authority: server
  required_set_hash: candidate
  required_mods:
    - id: org.example.relay-expansion
      version: 1.2.0
      sha256: candidate
  client_only_capabilities:
    - ui.theme.extend
  mismatch_policy: refuse_with_report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorité :** Le serveur possède le contrat de session.
- **Empreinte :** Le hash de l’ensemble représente ordre, versions et contenus.
- **Mods requis :** Les versions exactes sont comparées, pas seulement les noms.
- **Capacités client :** Seules les extensions explicitement cosmétiques peuvent diverger.
- **Refus :** Le rapport permet de corriger l’écart sans l’interpréter automatiquement comme une triche.

## 31. Produire un identifiant reproductible d’ensemble

L’identifiant de l’ensemble est calculé depuis une sérialisation canonique contenant :

- version de l’API ;
- liste triée selon l’ordre de chargement ;
- identifiant, version et empreinte de chaque mod ;
- capacités accordées ;
- options de compatibilité pertinentes.

Le nom de profil, le chemin local, la date et le nom d’utilisateur sont exclus. Deux installations équivalentes produisent le même identifiant.

## 32. Concevoir le SDK et les templates

Le SDK candidat comprend :

- schéma du manifeste ;
- schémas de contenu ;
- template minimal ;
- mod d’exemple ;
- validateur en ligne de commande ;
- documentation des API ;
- fixtures de tests ;
- changelog et politique de dépréciation ;
- registre des licences ;
- guide de publication.

Le SDK est versionné indépendamment du jeu mais déclare les versions d’API qu’il cible. Aucun SDK n’est matérialisé dans ce chapitre.

## 33. Fournir un mod d’exemple pédagogique

Le mod d’exemple doit être petit, lisible et entièrement redistribuable. Il démontre :

- une entrée de catalogue namespacée ;
- une traduction ;
- un asset léger ;
- une dépendance optionnelle ;
- un test de validation ;
- une désactivation sans perte de sauvegarde.

Il ne doit pas être une copie du contenu de production ni nécessiter des secrets de plateforme.

## 34. Préparer les commandes de validation

> **[PS] Validation candidate sous PowerShell — Ne pas présenter comme exécutée.**

```powershell
$ErrorActionPreference = "Stop"

$Manifest = "mods\org.example.relay-expansion\manifest.json"
python tools\modding\validate_manifest.py $Manifest
if ($LASTEXITCODE -ne 0) {
    throw "Validation du manifeste refusée."
}

python tools\modding\validate_package.py `
    "mods\org.example.relay-expansion.zip"
if ($LASTEXITCODE -ne 0) {
    throw "Validation du package refusée."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Arrêt strict :** Une erreur PowerShell interrompt la procédure.
- **Manifeste :** Le premier contrôle vérifie identité, schéma et capacités.
- **Package :** Le second contrôle inspecte archive, chemins, quotas et empreintes.
- **Codes de retour :** Chaque outil doit documenter ses statuts.
- **Réserve :** Les chemins et scripts sont candidats ; aucun fichier n’est déclaré présent.

> **[CMD] Vérification candidate depuis l’invite Windows.**

```bat
@echo off
python tools\modding\validate_manifest.py mods\sample\manifest.json
if errorlevel 1 exit /b 1

python tools\modding\validate_package.py mods\sample.zip
if errorlevel 1 exit /b 1

echo validation-candidate-ok
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Écho :** `@echo off` réduit le bruit sans masquer les codes de retour.
- **Arrêt :** `if errorlevel 1` propage tout refus du validateur.
- **Séquence :** Le manifeste précède l’inspection du package.
- **Sortie :** Le message final n’apparaît que si les deux contrôles réussissent.
- **Réserve :** Cette commande illustre le contrat et n’a pas été exécutée.

> **[WSL] Validation candidate sous Linux ou WSL.**

```bash
set -euo pipefail

python3 tools/modding/validate_manifest.py \
  mods/org.example.relay-expansion/manifest.json

python3 tools/modding/validate_package.py \
  mods/org.example.relay-expansion.zip

printf '%s\n' 'validation-candidate-ok'
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Options shell :** `-euo pipefail` bloque erreur, variable absente et pipeline défaillant.
- **Arguments :** Les chemins sont passés comme paramètres, jamais concaténés dans une commande évaluée.
- **Ordre :** Le package n’est contrôlé qu’après le manifeste.
- **Sortie :** Le résultat final est lisible par une CI légère.
- **Réserve :** Aucun package réel n’est validé par ce chapitre.

> **[DCK] Profil Docker Desktop candidat — À matérialiser séparément.**

```yaml
services:
  mod-validator:
    image: project-asteria/mod-validator:candidate
    network_mode: none
    read_only: true
    volumes:
      - ./candidate-mod:/input:ro
      - ./validation-report:/output
    command:
      - /app/validate
      - --input=/input
      - --report=/output/report.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Image :** Le tag `candidate` indique qu’aucune image qualifiée n’est publiée.
- **Réseau :** `none` interdit les téléchargements pendant la validation.
- **Système :** `read_only` limite les écritures dans le conteneur.
- **Volumes :** Le mod est monté en lecture seule et le rapport dans une sortie distincte.
- **Commande :** Les arguments sont transmis comme liste.
- **Limite :** Une image de conteneur n’est pas une sandbox suffisante sans qualification du runtime et de l’hôte.

> **[DCT] Commande candidate dans le conteneur de validation.**

```bash
/app/validate \
  --input=/input \
  --report=/output/report.json \
  --policy=/app/policies/public-mods-v1.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `/input` correspond au volume communautaire en lecture seule.
- **Rapport :** La sortie est séparée du contenu analysé.
- **Politique :** Le fichier versionné porte formats, capacités et quotas.
- **Arguments :** Aucune expansion shell issue du manifeste n’est exécutée.
- **Réserve :** Le binaire et la politique ne sont pas matérialisés.

> **[SORTIE] Rapport attendu — À lire sans le saisir.**

```json
{
  "schema": "asteria-mod-validation-report-v1",
  "mod_id": "org.example.relay-expansion",
  "version": "1.2.0",
  "decision": "candidate",
  "blocking_errors": [],
  "warnings": [
    "quota-values-not-qualified"
  ],
  "granted_capabilities": [
    "catalog.items.read",
    "catalog.items.extend"
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** Le rapport est corrélé à la version contrôlée.
- **Décision :** `candidate` ne vaut pas activation.
- **Blocages :** Les erreurs empêchant l’installation sont séparées des avertissements.
- **Avertissement :** Les quotas non qualifiés restent visibles.
- **Capacités :** Le rapport enregistre celles qui seraient accordées.
- **Résultat attendu :** Le support peut diagnostiquer sans recevoir le contenu complet.

## 35. Intégrer une interface graphique sans contourner les portes

L’interface d’installation affiche :

- identité et version ;
- source et provenance ;
- capacités demandées ;
- dépendances et conflits ;
- compatibilité ;
- licences ;
- taille et quotas ;
- résultat de validation ;
- conséquences sur les sauvegardes ;
- bouton d’activation distinct de l’installation.

Elle n’exécute pas directement l’archive. Elle appelle les mêmes services que la CLI.

> **[APP] Parcours candidat dans l’application `Project Asteria Mod Manager`.**

```text
1. Sélectionner un package local ou un élément de plateforme.
2. Lire le manifeste sans extraire.
3. Afficher source, identité, version, licences et capacités.
4. Inspecter l’archive et vérifier les empreintes.
5. Résoudre dépendances et conflits.
6. Installer dans le staging.
7. Produire un rapport.
8. Demander séparément l’activation.
9. Proposer un redémarrage ou rechargement contrôlé.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** Sélection, validation, installation et activation sont quatre décisions.
- **Information :** Les droits et capacités sont visibles avant l’écriture.
- **Conflits :** Ils sont résolus avant l’activation.
- **Rapport :** Une preuve locale est produite même si l’utilisateur annule.
- **Redémarrage :** Il dépend des ressources déjà préchargées et du contrat de l’API.

## 36. Adapter les plateformes communautaires

Une plateforme comme Steam Workshop fournit stockage, pages, abonnements et API UGC, mais le jeu reste responsable du format, du chargement, des conflits et de la sécurité. Un abonnement n’est pas une validation.

Un canal manuel, GitHub Releases ou un dépôt communautaire produit le même objet interne : source, identifiant externe, version, chemin local, manifeste et empreinte. Le chapitre 17 conserve les opérations de publication et les exigences volatiles des portails.

> **[WEB] Registre de sources communautaires — Exemple à vérifier sur les portails officiels.**

```yaml
sources:
  local:
    adapter: filesystem
    validation_required: true
  steam_workshop:
    adapter: platform_ugc
    external_id_required: true
    validation_required: true
  github_release:
    adapter: release_asset
    immutable_reference_required: true
    validation_required: true
  itch_distribution:
    adapter: channel_or_download
    validation_required: true
platform_requirements:
  status: volatile
  owner: chapter-17-register
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Adaptateurs :** Chaque source est transformée en candidat local commun.
- **Identité externe :** Elle complète l’identifiant du mod sans le remplacer.
- **Référence immuable :** Un asset doit être lié à une version ou empreinte précise.
- **Validation :** La provenance de plateforme ne dispense jamais des contrôles locaux.
- **Volatilité :** Les règles de portail restent dans le registre du chapitre 17.

## 37. Licences, provenance et redistribution

Le manifeste distingue :

- licence du code ;
- licence des assets ;
- dépendances tierces ;
- autorisations particulières ;
- obligations d’attribution ;
- droit de redistribution sur l’atelier ou le dépôt choisi.

Une expression SPDX aide à décrire une licence logicielle. Les licences Creative Commons peuvent convenir à certains contenus, selon leurs conditions. Aucun identifiant ne prouve que l’auteur possède effectivement les droits. La revue vérifie provenance, titulaires, dépendances et restrictions.

Les contenus sans licence explicite ne sont pas présumés redistribuables. Les contrats, données personnelles et preuves sensibles restent hors du dépôt public.

## 38. Politique communautaire et modération

La politique candidate décrit :

- catégories autorisées et interdites ;
- contenu illégal, haineux, harcelant ou trompeur ;
- malware, exfiltration et contournement de sécurité ;
- usurpation, marques et fausse affiliation ;
- droits d’auteur et procédures de signalement ;
- données personnelles et consentement ;
- contenus sexuels, violence et impact sur la classification ;
- transparence des médias synthétiques lorsque pertinente ;
- sanctions, retrait, appel et conservation minimale des preuves.

Le chapitre ne fournit pas de conseil juridique et ne prétend pas remplacer les règles de chaque plateforme ou territoire.

## 39. Modération technique et modération éditoriale

La modération technique vérifie format, malware connu, chemins, capacités, quotas et compatibilité. La modération éditoriale examine contenu, droits, classification et politique communautaire. Un résultat vert dans une dimension ne remplace pas l’autre.

Les contrôles automatiques produisent des signaux. Une décision de retrait ou de sanction garde une revue humaine, une trace et un mécanisme d’appel adapté.

## 40. Confidentialité et rapports de support

Un rapport de modding contient seulement :

- version du jeu et de l’API ;
- OS et renderer lorsque nécessaires ;
- liste des mods, versions et empreintes ;
- codes de validation ;
- ordre de chargement ;
- conflits ;
- extraits de journaux bornés et expurgés.

Il exclut sauvegardes brutes, noms réels, identifiants de compte, tokens, chemins personnels complets et contenu privé sauf consentement explicite et procédure sécurisée.

## 41. Support et responsabilité

Trois niveaux de support sont distingués :

- **officiel** : API, SDK, validateur et mod d’exemple ;
- **communautaire** : aide entre créateurs, sans garantie de l’éditeur ;
- **non pris en charge** : code natif, modification des binaires, contournement des validations.

Le support demande d’abord de reproduire sans mods, puis avec l’ensemble exact. Il ne conclut pas que « le mod est responsable » sans réduction du cas.

## 42. Tests du chargeur et du validateur

La campagne candidate couvre :

- manifeste valide minimal ;
- schéma inconnu ;
- identifiant invalide ;
- dépendance manquante ;
- cycle ;
- conflit ;
- archive avec traversée de chemin ;
- doublon de casse ;
- empreinte divergente ;
- capacité inconnue ;
- quota dépassé ;
- ressource non supportée ;
- sauvegarde avec mod absent ;
- migration de mod interrompue ;
- ensemble multijoueur divergent ;
- localisation incomplète ;
- activation, désactivation et mode sûr.

Aucun de ces scénarios n’est revendiqué comme exécuté.

> **[LECTURE] Matrice de tests candidate.**

```yaml
test_matrix:
  - id: manifest-minimal-valid
    expected: accepted-candidate
  - id: dependency-cycle
    expected: blocked
  - id: zip-path-traversal
    expected: blocked
  - id: unknown-capability
    expected: blocked
  - id: save-required-mod-missing
    expected: degraded-or-blocked-by-contract
  - id: multiplayer-set-mismatch
    expected: refused-with-report
runtime_execution: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** Chaque scénario est recherchable et réutilisable.
- **Oracles :** Les résultats attendus sont des codes métier, pas des phrases libres.
- **Sauvegarde :** Le comportement dépend du contrat du mod et reste explicite.
- **Multijoueur :** L’écart produit un refus diagnostiqué.
- **Preuve :** `runtime_execution: false` conserve le niveau `static-review`.

## 43. Tests de conflits combinatoires

Tester toutes les combinaisons devient rapidement impossible. La sélection combine :

- mods officiels d’exemple ;
- mods les plus dépendus ;
- paires déclarées incompatibles ;
- mêmes surfaces d’extension ;
- mêmes identités de contenu ;
- versions anciennes encore supportées ;
- ensembles issus de rapports réels ;
- génération par paires et triples bornés.

Le rapport conserve la sélection et sa justification. Une absence de conflit dans l’échantillon ne prouve pas la compatibilité universelle.

## 44. Performance et budgets

Le chargeur mesure séparément découverte, validation, montage, parsing, fusion et activation. Les budgets sont définis par plateforme et taille de lot. Les mods ne sont pas autorisés à masquer un dépassement par un écran de chargement indéfini.

Les assets communautaires utilisent les mêmes profils de qualité et limites que les assets officiels lorsque possible. Un mod peut être désactivé pour dépassement de budget sans être qualifié de malveillant.

## 45. Observabilité locale

Les événements candidats comprennent :

- `mod.discovered` ;
- `mod.validation.failed` ;
- `mod.installed` ;
- `mod.activation.blocked` ;
- `mod.dependency.missing` ;
- `mod.conflict.detected` ;
- `mod.safe_mode.started` ;
- `mod.save.compatibility.failed`.

Chaque événement porte identités stables et corrélation, sans journaliser le contenu complet.

## 46. Procédure Solo

En mode Solo :

1. définir le niveau de support ;
2. publier une seule surface déclarative ;
3. créer manifeste et schéma ;
4. écrire un validateur local ;
5. produire un template et un mod minimal ;
6. tester installation, désactivation et conflit sur copies ;
7. documenter limites et support ;
8. ouvrir progressivement d’autres surfaces seulement après preuves.

La priorité est la réversibilité. Un créateur seul ne doit pas maintenir simultanément scripts arbitraires, atelier, sandbox, modération et migrations complexes.

## 47. Procédure Studio

En mode Studio, les responsabilités sont séparées :

- architecture de l’API ;
- sécurité et menace ;
- outils et SDK ;
- validation de contenu ;
- compatibilité et migrations ;
- plateforme UGC ;
- juridique et licences ;
- trust and safety ;
- support ;
- QA et performance.

Chaque version de l’API possède un propriétaire, une matrice de compatibilité, un calendrier de dépréciation et un plan de réponse aux incidents.

## 48. Dix diagnostics détaillés

### 48.1 Utiliser le nom affiché comme identité

**Symptôme ou risque :** Une traduction ou un renommage crée un second mod et casse dépendances et sauvegardes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{
  "id": "Extension du relais",
  "version": "1.2.0"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** L’identité contient espaces, accents et texte éditorial.
- **Conséquence :** Le même contenu peut recevoir plusieurs identités selon la langue.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{
  "id": "org.example.relay-expansion",
  "display_name_key": "mod.relay_expansion.name",
  "version": "1.2.0"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** L’identifiant technique reste stable.
- **Présentation :** Le nom affiché est localisable sans modifier les références.

### 48.2 Monter un PCK avec remplacement global

**Symptôme ou risque :** Un mod peut masquer une scène ou un script officiel portant le même chemin.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
var ok := ProjectSettings.load_resource_pack(pack_path, true)
var scene := load("res://main.tscn")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** `true` autorise le pack à remplacer les fichiers déjà montés.
- **Conséquence :** Le chemin officiel peut résoudre vers une ressource communautaire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```gdscript
var ok := ProjectSettings.load_resource_pack(pack_path, false)
var scene := load("res://mods/org.example.relay-expansion/main.tscn")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Le pack ne remplace pas les ressources existantes.
- **Namespace :** Le point d’entrée reste sous la racine réservée au mod.

### 48.3 Charger un script communautaire comme une donnée

**Symptôme ou risque :** Le script s’exécute dans le processus du jeu sans isolation démontrée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
var script := load(user_selected_path)
var instance := script.new()
instance.run()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** Un chemin non fiable devient du code exécutable.
- **Conséquence :** Le script peut utiliser les capacités accessibles au processus.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{
  "op": "grant_item",
  "item_id": "asteria.core:item:signal_token",
  "quantity": 1
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Le mod demande une opération appartenant à une allowlist.
- **Autorité :** Le service officiel valide et applique la commande.

### 48.4 Extraire une archive sans inspecter ses chemins

**Symptôme ou risque :** Une entrée `../` peut écrire hors du dossier de staging.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```python
with ZipFile(package, "r") as archive:
    archive.extractall(active_mod_directory)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** L’extraction précède la validation des membres.
- **Conséquence :** Des chemins malveillants peuvent viser des fichiers voisins.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```python
members = inspect_archive(package)
staging = create_isolated_staging()
extract_validated_members(package, members, staging)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Tous les chemins sont inspectés avant écriture.
- **Staging :** L’installation active reste inchangée tant que le lot n’est pas validé.

### 48.5 Utiliser l’ordre du système de fichiers

**Symptôme ou risque :** Deux machines chargent les mêmes mods dans un ordre différent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```python
for directory in mods_root.iterdir():
    load_mod(directory)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** `iterdir()` ne constitue pas un contrat d’ordre portable.
- **Conséquence :** Les priorités et conflits deviennent non reproductibles.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```python
candidates = discover_and_validate(mods_root)
resolved = resolve_dependency_graph(candidates)
for mod in stable_load_order(resolved):
    load_mod(mod)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Dépendances et départage stable déterminent l’ordre.
- **Diagnostic :** Les cycles et conflits sont refusés avant chargement.

### 48.6 Oublier l’ensemble de mods dans la sauvegarde

**Symptôme ou risque :** La partie paraît chargeable mais perd des définitions ou interprète mal l’état communautaire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{
  "save_schema": 8,
  "world": {"relay_restored": true}
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** La sauvegarde ne dit pas quelles extensions ont produit l’état.
- **Conséquence :** L’absence d’un mod est découverte trop tard.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{
  "save_schema": 8,
  "mod_api": "asteria-mod-api-1",
  "mod_set": [
    {"id": "org.example.relay-expansion", "version": "1.2.0"}
  ],
  "mod_state": {
    "org.example.relay-expansion": {"schema": 2}
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Le chargeur connaît l’API, les versions et namespaces requis.
- **Dégradation :** Le contrat peut décider de bloquer ou de charger en mode limité.

### 48.7 Déclarer une compatibilité illimitée

**Symptôme ou risque :** Une mise à jour majeure du jeu active un mod conçu pour une API ancienne.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{
  "game_versions": "*",
  "game_api": "any"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** Aucun contrat n’encadre les versions acceptées.
- **Conséquence :** Une incompatibilité devient une erreur runtime tardive.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```json
{
  "game_versions": {
    "minimum": "1.4.0",
    "maximum_exclusive": "2.0.0"
  },
  "game_api": "asteria-mod-api-1"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** La plage du jeu et la version d’API sont explicites.
- **Refus précoce :** Le chargeur peut bloquer avant l’accès aux contenus.

### 48.8 Accorder des capacités inconnues par défaut

**Symptôme ou risque :** Une faute de frappe ou une nouvelle permission contourne la politique.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
for capability in requested:
    if not policy.has(capability):
        continue
    grant(capability)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** L’inconnu est ignoré au lieu d’être refusé.
- **Conséquence :** Le manifeste peut sembler accepté sans respecter son intention.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```gdscript
for capability in requested:
    if not policy.has(capability):
        denied.append(capability)
if not denied.is_empty():
    return {"allowed": false, "denied": denied}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Toute capacité inconnue bloque la décision.
- **Diagnostic :** La liste refusée permet une correction précise.

### 48.9 Redistribuer des assets sans preuve de droits

**Symptôme ou risque :** Un package mélange créations originales et fichiers tiers sans licences ni attributions.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
mod:
  id: org.example.relay-expansion
  license: free
  third_party_assets: unknown
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** `free` n’est pas une licence et les titulaires sont inconnus.
- **Conséquence :** La plateforme et les utilisateurs ne connaissent pas les droits accordés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
mod:
  id: org.example.relay-expansion
  code_license_expression: MIT
  content_license_expression: CC-BY-4.0
  third_party_notices: LICENSES/third-party-notices.md
  provenance_register: LICENSES/content.txt
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Code, contenus et dépendances sont distingués.
- **Réserve :** Les identifiants structurent la déclaration mais ne prouvent pas la titularité.

### 48.10 Supprimer l’état lors d’une désactivation

**Symptôme ou risque :** Un test temporaire détruit des données communautaires et rend le retour impossible.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func disable_mod(mod_id: StringName) -> void:
    active_mods.erase(mod_id)
    save.mod_state.erase(mod_id)
    delete_mod_files(mod_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant violé :** Désactivation, suppression d’état et désinstallation sont fusionnées.
- **Conséquence :** Une opération réversible devient destructive.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```gdscript
func disable_mod(mod_id: StringName) -> Dictionary:
    active_mods.erase(mod_id)
    return {
        "disabled": true,
        "state_preserved": save.mod_state.has(mod_id),
        "files_preserved": true,
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariant restauré :** Seule la sélection active change.
- **Réversibilité :** État et fichiers restent disponibles pour réactivation ou export.

## 49. Checklist d’acceptation documentaire

- [ ] Le niveau de support public est explicite.
- [ ] Les surfaces d’extension sont bornées et versionnées.
- [ ] Le manifeste possède identité, compatibilité, dépendances, capacités, licences et empreintes.
- [ ] Les archives sont inspectées avant extraction.
- [ ] Les quotas critiques sont qualifiés avant ouverture publique.
- [ ] Les PCK sont namespacés et ne remplacent pas les ressources officielles.
- [ ] Aucun code communautaire n’est présenté comme sandboxé sans preuve.
- [ ] Les dépendances, cycles, conflits et ordres sont déterministes.
- [ ] Installation, activation, désactivation et désinstallation sont distinctes.
- [ ] Les sauvegardes enregistrent l’ensemble de mods et préservent les namespaces.
- [ ] Le multijoueur compare versions et empreintes sous autorité serveur.
- [ ] Le SDK, les templates et le mod d’exemple sont versionnés.
- [ ] Licences, provenance, modération, confidentialité et support sont documentés.
- [ ] Les campagnes d’installation, désactivation et conflit conservent des preuves.
- [ ] Les limites et réserves runtime sont publiques.

## 50. Critère de passage

Le chapitre peut être accepté au niveau `static-review` lorsque le contrat couvre les cinq objectifs et livrables du plan maître, que chaque bloc est expliqué, que les dix diagnostics sont complets, que les références officielles sont cliquables, que les frontières avec les chapitres voisins sont maintenues et qu’aucun test ou service communautaire n’est présenté comme exécuté.

Le passage à `runtime-tested` exigerait au minimum un chargeur matérialisé, un manifeste et un SDK versionnés, un mod d’exemple redistribuable, des quotas qualifiés, des campagnes d’installation/désactivation/conflit, des tests de sauvegarde et multijoueur, des rapports conservés et une politique communautaire réellement publiée.

## 51. Références officielles

- [Godot — Exporting packs, patches, and mods](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)
- [Godot — Runtime file loading and saving](https://docs.godotengine.org/en/stable/tutorials/io/runtime_file_loading_and_saving.html)
- [Godot — ProjectSettings](https://docs.godotengine.org/en/stable/classes/class_projectsettings.html)
- [Godot — PCKPacker](https://docs.godotengine.org/en/stable/classes/class_pckpacker.html)
- [Godot — ZIPReader](https://docs.godotengine.org/en/stable/classes/class_zipreader.html)
- [Godot — FileAccess](https://docs.godotengine.org/en/stable/classes/class_fileaccess.html)
- [Godot — DirAccess](https://docs.godotengine.org/en/stable/classes/class_diraccess.html)
- [Godot — JSON](https://docs.godotengine.org/en/stable/classes/class_json.html)
- [Godot — GDScript resource](https://docs.godotengine.org/en/stable/classes/class_gdscript.html)
- [Steamworks — Steam Workshop](https://partner.steamgames.com/doc/features/workshop)
- [Steamworks — Steam Workshop Implementation Guide](https://partner.steamgames.com/doc/features/workshop/implementation)
- [Steamworks — ISteamUGC](https://partner.steamgames.com/doc/api/isteamugc)
- [itch.io — Butler manual](https://itch.io/docs/butler/)
- [GitHub Docs — About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Python — `zipfile`](https://docs.python.org/3/library/zipfile.html)
- [SPDX — Specifications](https://spdx.dev/use/specifications/)
- [SPDX — Handling license information](https://spdx.dev/learn/handling-license-info/)
- [Creative Commons — Licensing considerations](https://creativecommons.org/share-your-work/licensing-considerations/version4/)

## 52. Réserves explicites

- aucun chargeur, gestionnaire, SDK, template, mod d’exemple ou schéma final n’est matérialisé ;
- aucun PCK, ZIP, asset runtime ou script communautaire n’est chargé ;
- aucune sandbox de code n’est revendiquée ;
- aucun quota n’est qualifié ;
- aucune plateforme Workshop, UGC ou dépôt communautaire n’est configuré ;
- aucune installation, activation, désactivation, désinstallation ou migration n’est exécutée ;
- aucune sauvegarde moddée ou session multijoueur n’est testée ;
- aucune licence, provenance, modération ou procédure de signalement n’est juridiquement validée ;
- aucun support communautaire ou rapport utilisateur n’est traité ;
- aucun PDF du Livre IV n’est produit.

## 53. Synthèse opérationnelle de Project Asteria

`Project Asteria` retient un modèle de modding progressif. Le premier niveau public accepte des catalogues déclaratifs, traductions et assets runtime dans des formats fermés. Chaque mod possède un identifiant namespacé, un manifeste versionné, une plage de compatibilité, des dépendances, des capacités, des licences et des empreintes.

L’installation utilise inbox, staging, validation puis activation. Les archives sont inspectées avant extraction. Les PCK éventuels restent sous `res://mods/<id>/` et sont montés sans remplacement des ressources officielles. Les scripts GDScript et extensions natives ne sont pas présentés comme sandboxés et restent hors du support public par défaut.

Le résolveur produit un ordre déterministe, refuse cycles et conflits non résolus, et calcule une empreinte de l’ensemble. Les sauvegardes enregistrent versions, empreintes et état namespacé sans donner au mod l’autorité sur la structure globale. En multijoueur, le serveur possède le contrat de mods.

Le SDK candidat regroupe schémas, validateur, template, mod d’exemple, tests et politique de dépréciation. Licences, provenance, modération, confidentialité et support forment des portes séparées. Aucun de ces composants n’est présenté comme matérialisé avant validation runtime et publication réelle.
