---
title: "Livre II — Chapitre 13 : Sécurité et séparation entre production et runtime de l’IA"
id: "DOC-L2-CH13"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 13
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-13.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Sécurité et séparation entre production et runtime de l’IA

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH13`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

## 1. Rôle du chapitre

Les chapitres 10 à 12 ont ajouté la mémoire vectorielle, `LocalAiGateway`, un processus compagnon, HTTP, WebSocket et des files de tâches. Le présent chapitre ferme la plateforme IA locale avant le début des systèmes de gameplay.

Il empêche de confondre :

- outil de production et capacité runtime ;
- disponibilité locale et confiance ;
- identité et permission ;
- TLS et autorisation ;
- secret injecté et secret protégé ;
- journal utile et copie de données sensibles ;
- artefact exporté et artefact authentique ;
- échec fonctionnel et échec de sécurité.

À la fin du chapitre, le lecteur doit savoir :

- maintenir un modèle de menaces ;
- dessiner les frontières de confiance ;
- séparer production, pipeline de livraison et runtime ;
- définir les profils `development`, `test` et `production` ;
- garder les secrets hors dépôt et hors package ;
- écouter sur la boucle locale par défaut ;
- exiger authentification et TLS lorsqu’une frontière réseau s’élargit ;
- autoriser explicitement opérations, modèles et chemins ;
- appliquer le moindre privilège ;
- borner payloads, files, temps et résultats ;
- rédiger les journaux ;
- épingler les dépendances et produire un SBOM ;
- prévoir provenance, signature et rollback ;
- échouer de manière fermée pour la sécurité sans supprimer le repli déterministe du gameplay.

## 2. Prérequis

Le lecteur doit connaître :

- l’architecture modulaire du chapitre 4 ;
- l’injection du chapitre 5 ;
- les configurations du chapitre 7 ;
- les sauvegardes du chapitre 9 ;
- la mémoire vectorielle du chapitre 10 ;
- le port, les capacités et les erreurs du chapitre 11 ;
- HTTP, WebSocket, idempotence et backpressure du chapitre 12 ;
- Python et PowerShell du Livre I.

Ce chapitre ne construit pas un service Internet public, une PKI d’entreprise, un système anti-triche ou une conformité réglementaire universelle.

## 3. Périmètre

Ce chapitre définit :

- modèle de menaces et zones de confiance ;
- séparation production/runtime ;
- profils d’environnement ;
- classification des données ;
- secrets, authentification et autorisation ;
- TLS, allowlists et chemins sûrs ;
- moindre privilège, limites et quotas ;
- journaux, rédaction et rétention ;
- dépendances, SBOM, provenance, packaging et signature ;
- échec fermé et repli déterministe ;
- parcours Solo et Studio.

Il ne définit pas les permissions des personnages, le multijoueur, l’anti-triche, la modération ou l’exploitation d’un service public.

> **Principe essentiel :** le runtime doit rester sûr même si un joueur inspecte ses fichiers, modifie sa configuration locale ou appelle directement le service IA local.

## 4. Vocabulaire

- **Actif :** élément à protéger : secret, build, modèle, corpus, journal ou capacité coûteuse.
- **Menace :** événement indésirable : divulgation, altération, usurpation, déni de service ou exécution non autorisée.
- **Frontière de confiance :** passage où identité, intégrité et permissions doivent être revérifiées.
- **Surface d’attaque :** entrées, protocoles, fichiers, dépendances et opérations atteignables.
- **Authentification :** vérifier qui présente la demande.
- **Autorisation :** décider si cette identité peut effectuer l’opération.
- **Secret :** donnée dont la divulgation donne un pouvoir.
- **Rédaction :** suppression ou remplacement d’une donnée sensible avant journalisation.
- **SBOM :** inventaire structuré des composants logiciels.
- **Provenance :** description de la fabrication d’un artefact.

## 5. Modèle de menaces

Le modèle répond à quatre questions :

1. que construisons-nous ;
2. que peut-il mal se passer ;
3. que faisons-nous pour le prévenir ou le limiter ;
4. avons-nous suffisamment vérifié le résultat.

> **[VSC] Visual Studio Code — Créer `docs/security/threat-model.md` :**

```markdown
# Modèle de menaces — Project Asteria

## Système
- jeu Godot exporté ;
- LocalAiGateway ;
- service IA local ;
- données et modèles runtime ;
- outils de production séparés.

## Actifs
- intégrité du gameplay ;
- secrets de build ;
- modèles autorisés ;
- corpus internes ;
- journaux de sécurité ;
- artefacts publiés.

## Frontières
- joueur → jeu ;
- jeu → service IA ;
- service → fichiers ;
- pipeline → artefact ;
- équipe → dépôt et secrets.

## Menaces prioritaires
- opération non autorisée ;
- exposition réseau involontaire ;
- fuite de secret ;
- traversal de chemin ;
- saturation ;
- journal sensible ;
- dépendance compromise ;
- mise à jour non authentique.
```

Une nouvelle route, un nouveau modèle ou une nouvelle cible d’export impose la relecture du document.

## 6. Zones de confiance

> **[LECTURE] Architecture de confiance — Ne pas saisir.**

```text
ZONE A — PRODUCTION
indexation, génération, conversion, entraînement, build
                ↓ frontière forte
ZONE B — LIVRAISON
verrous, tests, SBOM, provenance, signature
                ↓ frontière d’artefact
ZONE C — RUNTIME DISTRIBUÉ
jeu + capacités IA minimales et redistribuables
                ↓ frontière locale
ZONE D — DONNÉES DU JOUEUR
sauvegardes, configuration, entrées et caches non fiables
```

Le runtime ne reçoit jamais automatiquement les permissions de la production.

## 7. Séparation production/runtime

La production peut contenir des indexeurs, générateurs, diagnostics, modèles non redistribuables, corpus internes et secrets de signature.

Le runtime contient seulement :

- opérations nécessaires au jeu ;
- modèles redistribuables ;
- données destinées à la livraison ;
- limites de ressources ;
- journaux minimaux ;
- repli déterministe.

> **[VSC] Visual Studio Code — Créer `config/ai-capabilities.yaml` :**

```yaml
schema_version: 1
profiles:
  development:
    operations:
      - knowledge.search
      - text.generate
      - embedding.create
      - corpus.reindex
      - diagnostics.dump
  test:
    operations:
      - knowledge.search
      - text.generate
  production:
    operations:
      - knowledge.search
      - text.generate
```

`corpus.reindex` et `diagnostics.dump` restent hors production sauf décision explicite et auditée.

## 8. Profils d’environnement

| Propriété | Development | Test | Production |
|---|---:|---:|---:|
| écoute | loopback | réseau de test possible | loopback par défaut |
| données | contrôlées | fixtures | distribuables |
| logs | détaillés et rédigés | bornés | minimaux et rédigés |
| administration | locale | limitée | refusée |
| secrets | hors dépôt | injectés | injectés et rotatifs |
| certificat non vérifié | test ciblé | interdit par défaut | interdit |
| debug | autorisé | limité | désactivé |

> **[VSC] Visual Studio Code — Créer `res://src/core/security/runtime_profile.gd` :**

```gdscript
class_name RuntimeProfile
extends RefCounted

enum Kind { DEVELOPMENT, TEST, PRODUCTION }

var kind: Kind
var allow_admin_operations: bool
var require_tls: bool
var require_service_authentication: bool
var log_payloads: bool

static func production_local() -> RuntimeProfile:
	var profile := RuntimeProfile.new()
	profile.kind = Kind.PRODUCTION
	profile.allow_admin_operations = false
	profile.require_tls = false
	profile.require_service_authentication = false
	profile.log_payloads = false
	return profile
```

Ce profil est valide uniquement avec une écoute strictement locale. Une adresse distante impose TLS et authentification.

## 9. Classification des données

| Classe | Exemples | Règle |
|---|---|---|
| Public | versions, documentation | journalisable |
| Interne | chemins de build, métriques | accès limité |
| Sensible | prompts, extraits de sauvegarde | minimiser et rédiger |
| Secret | jetons, mots de passe, clés privées | ne jamais journaliser ni versionner |
| Dérivé | embeddings, caches, index | reconstructible et borné |

Un embedding ou un journal dérivé n’est pas automatiquement public.

## 10. Secrets

Un secret :

- ne figure jamais dans le dépôt ;
- ne figure jamais dans `res://` ;
- ne traverse pas un payload de gameplay ;
- n’est pas retourné par les diagnostics ;
- n’est pas copié dans les journaux ;
- possède un propriétaire, une portée, une durée de vie et une procédure de révocation.

Godot sépare `export_presets.cfg` de `.godot/export_credentials.cfg`. Le second contient des informations confidentielles et reste hors versionnement.

> **[VSC] Visual Studio Code — Vérifier `.gitignore` :**

```gitignore
.godot/export_credentials.cfg
.env
.env.*
!.env.example
secrets/
*.key
*.pem
```

> **[PS] PowerShell 7 — Injecter un jeton dans le processus courant :**

```powershell
$env:ASTERIA_AI_SERVICE_TOKEN = Read-Host "Jeton du service IA" -MaskInput
```

`-MaskInput` masque la saisie mais retourne une chaîne. Elle reste en mémoire et ne doit pas être affichée ou écrite dans un fichier.

> **[VSC] Visual Studio Code — Créer `tools/security/secret_provider.py` :**

```python
from __future__ import annotations

import os

class SecretConfigurationError(RuntimeError):
    pass

def require_secret(name: str) -> str:
    value = os.environ.get(name, "")
    if not value:
        raise SecretConfigurationError(f"Secret absent: {name}")
    if len(value) < 24:
        raise SecretConfigurationError(f"Secret trop court: {name}")
    return value
```

Une variable d’environnement réduit le risque de commit accidentel. Elle ne remplace pas un coffre de secrets.

## 11. Jetons

Python utilise `secrets`, pas `random`, pour un jeton de sécurité.

> **[VSC] Visual Studio Code — Créer `tools/security/generate_local_token.py` :**

```python
from __future__ import annotations

import secrets

def generate_token() -> str:
    return secrets.token_urlsafe(32)

if __name__ == "__main__":
    print(generate_token())
```

> **[PS] PowerShell 7 — Générer un jeton local :**

```powershell
python tools/security/generate_local_token.py
```

> **[SORTIE] Forme indicative — Ne pas réutiliser :**

```text
<jeton aléatoire généré localement>
```

## 12. Exposition réseau

Le parcours Solo écoute sur `127.0.0.1`. `0.0.0.0` et `::` sont refusés, car ils exposent toutes les interfaces disponibles.

> **[VSC] Visual Studio Code — Créer `config/ai-server-production.toml` :**

```toml
host = "127.0.0.1"
port = 8765
allow_remote = false
require_authentication = false
require_tls = false
```

> **[VSC] Visual Studio Code — Créer `tools/ai_server/security_config.py` :**

```python
from __future__ import annotations

from dataclasses import dataclass
from ipaddress import ip_address

class SecurityConfigError(ValueError):
    pass

@dataclass(frozen=True)
class ServerSecurityConfig:
    host: str
    allow_remote: bool
    require_authentication: bool
    require_tls: bool

    def validate(self) -> None:
        address = ip_address(self.host)
        if address.is_unspecified:
            raise SecurityConfigError("Toutes les interfaces sont interdites.")
        if not address.is_loopback and not self.allow_remote:
            raise SecurityConfigError("Une adresse distante exige allow_remote=true.")
        if not address.is_loopback:
            if not self.require_authentication:
                raise SecurityConfigError("Authentification distante obligatoire.")
            if not self.require_tls:
                raise SecurityConfigError("TLS distant obligatoire.")
```

## 13. Authentification et autorisation

L’authentification devient obligatoire hors boucle locale, sur une machine partagée ou dès qu’une politique Studio l’exige.

> **[LECTURE] Requête authentifiée — Ne pas saisir.**

```http
POST /v1/operations HTTP/1.1
Host: ai.internal.example
Authorization: Bearer <jeton>
Content-Type: application/json
```

Le jeton ne figure ni dans l’URL ni dans le corps métier.

> **[VSC] Visual Studio Code — Créer `tools/ai_server/authentication.py` :**

```python
from __future__ import annotations

import hmac

def bearer_token_is_valid(provided: str, expected: str) -> bool:
    if not provided or not expected:
        return False
    return hmac.compare_digest(provided.encode(), expected.encode())
```

Une identité authentifiée ne reçoit pas toutes les opérations.

> **[VSC] Visual Studio Code — Créer `tools/ai_server/authorization.py` :**

```python
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class ServicePrincipal:
    principal_id: str
    allowed_operations: frozenset[str]

def authorize_operation(principal: ServicePrincipal, operation: str) -> None:
    if operation not in principal.allowed_operations:
        raise PermissionError(
            f"Opération refusée pour {principal.principal_id}: {operation}"
        )
```

La politique suit **deny-by-default** : une opération absente est refusée.

## 14. Listes d’autorisation

Les listes d’autorisation couvrent :

- opérations ;
- modèles ;
- types de fichiers ;
- racines de chemins ;
- capacités de diagnostic ;
- origines réseau lorsque nécessaire.

> **[VSC] Visual Studio Code — Créer `config/runtime-models.yaml` :**

```yaml
schema_version: 1
models:
  - id: asteria-dialogue-small
    purpose: text.generate
    redistributable: true
  - id: multilingual-e5-small
    purpose: embedding.create
    redistributable: true
```

Un chemin reçu du réseau n’est jamais ouvert directement.

> **[VSC] Visual Studio Code — Créer `tools/ai_server/safe_paths.py` :**

```python
from __future__ import annotations

from pathlib import Path

class UnsafePathError(ValueError):
    pass

def resolve_under(root: Path, relative: str) -> Path:
    if Path(relative).is_absolute():
        raise UnsafePathError("Chemin absolu interdit.")
    resolved_root = root.resolve(strict=True)
    candidate = (resolved_root / relative).resolve(strict=False)
    if candidate != resolved_root and resolved_root not in candidate.parents:
        raise UnsafePathError("Le chemin sort de la racine autorisée.")
    return candidate
```

## 15. TLS

- boucle locale contrôlée : HTTP peut rester acceptable ;
- adresse distante : TLS obligatoire ;
- certificat non vérifié : test ciblé seulement, jamais en production.

> **[VSC] Visual Studio Code — Créer `res://src/core/security/tls_policy.gd` :**

```gdscript
class_name TlsPolicy
extends RefCounted

static func create_client_options(
	trusted_chain: X509Certificate = null,
	common_name_override: String = ""
) -> TLSOptions:
	return TLSOptions.client(trusted_chain, common_name_override)
```

`TLSOptions.client_unsafe()` est exclu du profil production.

> **[VSC] Visual Studio Code — Créer `tools/ai_server/tls_context.py` :**

```python
from __future__ import annotations

import ssl
from pathlib import Path

def create_server_context(cert: Path, key: Path) -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=str(cert), keyfile=str(key))
    return context
```

La clé privée reste sur le service et n’est jamais livrée au client.

## 16. Moindre privilège

Le processus IA reçoit seulement :

- dossiers nécessaires ;
- variables nécessaires ;
- opérations nécessaires ;
- accès réseau nécessaire ;
- mémoire et temps nécessaires ;
- aucun droit administrateur ;
- aucune clé de publication.

> **[LECTURE] Arborescence de privilèges — Ne pas créer sans adaptation.**

```text
runtime/
├── models/       lecture seule
├── knowledge/    lecture seule
└── cache/        lecture/écriture bornée
logs/             écriture limitée
production-tools/ absent du package runtime
```

Après installation du serveur comme paquet dans son environnement virtuel :

> **[PS] PowerShell 7 — Lancer le paquet en mode isolé :**

```powershell
.\.venv\Scripts\python.exe -I -m asteria_ai_server
```

Le mode isolé ne remplace pas la validation des imports et dépendances.

## 17. Limites et validation

Les limites du chapitre 12 deviennent des contrôles de sécurité :

- corps HTTP ;
- paquet WebSocket ;
- file et workers ;
- tâches par identité ;
- débit ;
- délai ;
- taille de résultat ;
- budget mémoire et génération.

> **[VSC] Visual Studio Code — Créer `tools/ai_server/security_limits.py` :**

```python
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class SecurityLimits:
    max_body_bytes: int = 1_048_576
    max_result_bytes: int = 2_097_152
    max_tasks_per_principal: int = 8
    max_requests_per_minute: int = 120
    max_timeout_ms: int = 30_000

    def validate(self) -> None:
        if self.max_body_bytes <= 0:
            raise ValueError("max_body_bytes doit être positif.")
        if self.max_tasks_per_principal <= 0:
            raise ValueError("max_tasks_per_principal doit être positif.")
```

La validation porte sur type, champs, longueur, plage, encodage, opération, identité, état et taille après décodage.

## 18. Journaux et rédaction

Journaliser : démarrage, arrêt, profil, refus d’authentification, refus d’autorisation, quotas, erreurs de validation, versions et vérifications de signature.

Ne jamais journaliser : jetons, mots de passe, clés privées, en-tête `Authorization`, payload complet, sauvegarde complète ou contenu arbitraire.

> **[VSC] Visual Studio Code — Créer `tools/security/redaction.py` :**

```python
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

REDACTED = "<redacted>"
SENSITIVE_KEYS = frozenset({
    "authorization", "token", "password", "secret", "api_key", "private_key"
})

def redact_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, item in value.items():
        if key.casefold() in SENSITIVE_KEYS:
            output[key] = REDACTED
        elif isinstance(item, Mapping):
            output[key] = redact_mapping(item)
        else:
            output[key] = item
    return output
```

Le Mode Solo utilise rotation par taille et rétention courte. Le Studio ajoute stockage séparé, accès par rôle, intégrité, politique de conservation et procédure d’incident.

## 19. Dépendances, SBOM et provenance

Une dépendance flottante empêche de reproduire le build. Les dépendances réelles possèdent :

- version exacte ;
- empreinte lorsque l’outil le permet ;
- origine connue ;
- licence inventoriée ;
- suivi des vulnérabilités ;
- mise à jour contrôlée.

> **[LECTURE] Forme d’un verrou — Ne pas installer :**

```text
package-a==X.Y.Z --hash=sha256:<empreinte>
package-b==A.B.C --hash=sha256:<empreinte>
```

Le chapitre n’impose pas encore de framework serveur et ne crée pas de faux verrou.

Un SBOM décrit au minimum composants, versions, identifiants, relations, outil de génération et date.

> **[LECTURE] Exemple SBOM simplifié — Ne pas publier tel quel.**

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "version": 1,
  "metadata": {
    "component": {
      "type": "application",
      "name": "Project Asteria",
      "version": "0.1.0"
    }
  },
  "components": []
}
```

CycloneDX et SPDX restent deux options ; le pipeline choisira selon les outils réels.

La provenance relie commit, outils, dépendances, paramètres non secrets, environnement de build et hachages des artefacts.

## 20. Packaging, signature et mise à jour

Le package runtime exclut :

- `.git` et environnements virtuels ;
- corpus et outils de production ;
- notebooks et caches inutiles ;
- journaux de développement ;
- secrets et clés privées ;
- routes d’administration inutilisées.

Une signature authentifie l’origine et l’intégrité ; elle ne garantit pas l’absence de vulnérabilité.

Le pipeline :

1. construit dans un environnement contrôlé ;
2. calcule les hachages ;
3. produit SBOM et provenance ;
4. signe l’artefact ;
5. publie signature et métadonnées ;
6. vérifie avant diffusion.

> **[PS] PowerShell 7 — Calculer un hachage :**

```powershell
Get-FileHash .\dist\ProjectAsteria.exe -Algorithm SHA256
```

> **[SORTIE] Forme attendue :**

```text
Algorithm Hash                                                             Path
--------- ----                                                             ----
SHA256    <64 caractères hexadécimaux>                                      ProjectAsteria.exe
```

Un hachage publié sur le même canal compromis que l’artefact n’authentifie pas l’origine.

Une mise à jour sûre possède un canal identifié, un manifeste versionné, une signature, une protection contre le rollback involontaire, une stratégie de reprise et une séparation des données utilisateur.

## 21. Échec fermé et repli

> **[LECTURE] Matrice de décision — Ne pas saisir.**

```text
service indisponible
    → repli déterministe autorisé

jeton invalide ou opération interdite
    → opération refusée
    → aucun contournement

signature invalide
    → mise à jour refusée
    → conserver la dernière version valide

payload invalide
    → demande refusée
    → ne pas deviner l’intention
```

Le repli ne transforme jamais une violation de sécurité en réussite.

## 22. Politique injectée dans Godot

> **[VSC] Visual Studio Code — Créer `res://src/core/security/security_policy.gd` :**

```gdscript
class_name SecurityPolicy
extends RefCounted

var allowed_operations: Dictionary
var allowed_model_ids: Dictionary

func _init(operations: Array[String], model_ids: Array[String]) -> void:
	allowed_operations = {}
	allowed_model_ids = {}
	for operation in operations:
		allowed_operations[operation] = true
	for model_id in model_ids:
		allowed_model_ids[model_id] = true

func allows_operation(operation: String) -> bool:
	return allowed_operations.has(operation)

func allows_model(model_id: String) -> bool:
	return allowed_model_ids.has(model_id)
```

La politique est injectée dans l’adaptateur. Le gameplay continue de dépendre de `LocalAiGateway`.

## 23. Erreurs structurées

| Code | Sens | Retry |
|---|---|---:|
| `authentication_required` | identité absente | non |
| `authentication_failed` | preuve refusée | non |
| `operation_forbidden` | capacité refusée | non |
| `model_forbidden` | modèle refusé | non |
| `unsafe_path` | chemin hors racine | non |
| `payload_too_large` | limite dépassée | après réduction |
| `rate_limited` | quota temporaire | oui, borné |
| `security_configuration_invalid` | profil incohérent | non |
| `signature_invalid` | artefact non authentique | non |

La route de santé ne révèle ni chemins, variables, secrets, stack traces, comptes ou configuration détaillée.

## 24. Mode Solo

Le Mode Solo choisit :

- `127.0.0.1` ;
- aucune exposition distante ;
- aucune clé fournisseur dans le jeu ;
- modèles redistribuables seulement ;
- opérations runtime minimales ;
- files et payloads bornés ;
- journaux courts et rédigés ;
- dépendances épinglées ;
- SBOM et signature à la publication ;
- repli déterministe.

## 25. Mode Studio

Le Studio ajoute :

- responsables nommés ;
- modèle de menaces revu ;
- coffre, rotation et révocation ;
- identités de service ;
- autorisations par rôle et capacité ;
- TLS géré et segmentation réseau ;
- quotas par identité ;
- journaux centralisés avec rétention ;
- analyse de dépendances ;
- SBOM et provenance automatisés ;
- signature protégée ;
- procédure de vulnérabilité et d’incident ;
- séparation des rôles de développement et de publication.

## 26. Tests à préparer

Le Starter Kit devra vérifier :

- refus de `0.0.0.0` sans opt-in ;
- TLS et authentification hors loopback ;
- opération ou modèle refusé ;
- traversal `../` et chemin absolu ;
- payload, quota ou concurrence dépassés ;
- jeton absent ou invalide ;
- rédaction des secrets ;
- absence de secrets dans le package ;
- SBOM produit ;
- signature valide et invalide ;
- rollback ;
- repli après indisponibilité.

## 27. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 27.1 Livrer les outils de production

**Symptôme :** le runtime expose `corpus.reindex` et `diagnostics.dump`.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
runtime = [knowledge.search, corpus.reindex, diagnostics.dump]
```

**Correction :** publier une liste minimale.

> **[LECTURE] Exemple corrigé — Référence.**

```text
runtime = [knowledge.search]
```

**Différence :** le runtime ne reçoit plus les capacités de production.

### 27.2 Écouter sur toutes les interfaces

**Symptôme :** un service local devient joignable depuis le réseau.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```toml
host = "0.0.0.0"
```

**Correction :** utiliser la boucle locale.

> **[LECTURE] Exemple corrigé — Référence.**

```toml
host = "127.0.0.1"
```

**Différence :** l’exposition distante n’est plus implicite.

### 27.3 Stocker un jeton dans `res://`

**Symptôme :** le secret est distribué avec le jeu.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
const SERVICE_TOKEN := "secret-production"
```

**Correction :** injecter hors dépôt.

> **[LECTURE] Exemple corrigé — Référence.**

```text
ASTERIA_AI_SERVICE_TOKEN=<injecté par l’environnement>
```

**Différence :** le secret n’est plus intégré au package.

### 27.4 Confondre authentification et autorisation

**Symptôme :** tout jeton valide appelle toute opération.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
if token_is_valid:
    run_any_operation(operation)
```

**Correction :** vérifier la capacité.

> **[LECTURE] Exemple corrigé — Référence.**

```python
if token_is_valid:
    authorize_operation(principal, operation)
```

**Différence :** une identité valide reste limitée.

### 27.5 Utiliser `task_id` comme autorisation

**Symptôme :** connaître l’identifiant permet de lire le résultat.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
def read_task(task_id: str):
    return registry.get(task_id)
```

**Correction :** vérifier le propriétaire.

> **[LECTURE] Exemple corrigé — Référence.**

```python
def read_task(task_id: str, principal):
    record = registry.get(task_id)
    authorize_task_read(principal, record)
    return record
```

**Différence :** l’identifiant localise sans accorder l’accès.

### 27.6 Désactiver TLS en production

**Symptôme :** le certificat n’est pas authentifié.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var options := TLSOptions.client_unsafe()
```

**Correction :** utiliser la validation normale.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var options := TLSOptions.client()
```

**Différence :** le certificat et le nom attendu sont vérifiés.

### 27.7 Ouvrir un chemin client

**Symptôme :** `../../secret.txt` sort de la racine.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
def unsafe_read(root, relative):
    return (root / relative).read_text()
```

**Correction :** résoudre sous la racine.

> **[LECTURE] Exemple corrigé — Référence.**

```python
def safe_read(root, relative):
    return resolve_under(root, relative).read_text()
```

**Différence :** le chemin canonique reste autorisé.

### 27.8 Journaliser Authorization

**Symptôme :** les jetons apparaissent dans les logs.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
logger.info("headers=%r", request.headers)
```

**Correction :** rédiger les champs sensibles.

> **[LECTURE] Exemple corrigé — Référence.**

```python
logger.info("headers=%r", redact_mapping(request.headers))
```

**Différence :** le diagnostic reste utile sans secret.

### 27.9 Utiliser `random` pour un jeton

**Symptôme :** le générateur est destiné à la simulation.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
token = str(random.random())
```

**Correction :** utiliser `secrets`.

> **[LECTURE] Exemple corrigé — Référence.**

```python
token = secrets.token_urlsafe(32)
```

**Différence :** la source d’aléa convient à la sécurité.

### 27.10 Laisser une file illimitée

**Symptôme :** la mémoire croît sans borne.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
queue = asyncio.Queue()
```

**Correction :** imposer une capacité.

> **[LECTURE] Exemple corrigé — Référence.**

```python
queue = asyncio.Queue(maxsize=128)
```

**Différence :** la surcharge est refusée.

### 27.11 Considérer TLS comme une autorisation

**Symptôme :** canal chiffré signifie opération permise.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
TLS actif → opération autorisée
```

**Correction :** séparer canal, identité et permission.

> **[LECTURE] Exemple corrigé — Référence.**

```text
TLS valide + identité valide + capacité autorisée → opération possible
```

**Différence :** le chiffrement ne remplace pas le contrôle d’accès.

### 27.12 Inclure une clé privée

**Symptôme :** tous les joueurs reçoivent la clé serveur.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
res://certificates/server-private.key
```

**Correction :** garder la clé sur le service.

> **[LECTURE] Exemple corrigé — Référence.**

```text
service-host:/secure/keys/server-private.key
```

**Différence :** le client ne possède plus le secret serveur.

### 27.13 Publier sans SBOM

**Symptôme :** l’équipe ignore les versions distribuées.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
pip install package-a package-b
```

**Correction :** verrouiller et inventorier.

> **[LECTURE] Exemple corrigé — Référence.**

```text
fichier verrouillé + SBOM du build
```

**Différence :** le contenu devient traçable.

### 27.14 Faire confiance à un hachage seul

**Symptôme :** artefact et hachage sont remplacés ensemble.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
game.exe + game.exe.sha256 sur le même canal
```

**Correction :** vérifier une signature de publication.

> **[LECTURE] Exemple corrigé — Référence.**

```text
artefact + signature + identité de publication vérifiée
```

**Différence :** l’intégrité est liée à une origine.

### 27.15 Masquer un refus par le repli

**Symptôme :** un jeton invalide déclenche une route non protégée.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
authentication_failed → appeler sans jeton
```

**Correction :** fermer l’opération.

> **[LECTURE] Exemple corrigé — Référence.**

```text
authentication_failed → refuser et journaliser un code rédigé
```

**Différence :** le repli ne contourne pas la sécurité.

### 27.16 Garder le debug de production

**Symptôme :** chemins et stack traces sont exposés.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```toml
profile = "production"
debug = true
```

**Correction :** désactiver le debug.

> **[LECTURE] Exemple corrigé — Référence.**

```toml
profile = "production"
debug = false
```

**Différence :** le client reçoit un diagnostic borné.

## 28. Critères d’acceptation

Le lecteur peut montrer statiquement que :

- les outils de production ne sont pas livrés ;
- le runtime possède un profil dédié ;
- les secrets restent hors dépôt et package ;
- l’écoute est locale par défaut ;
- une adresse distante exige authentification et TLS ;
- l’autorisation suit deny-by-default ;
- opérations, modèles et chemins sont autorisés explicitement ;
- privilèges, payloads, files, temps et résultats sont bornés ;
- les journaux sont rédigés ;
- dépendances, SBOM et provenance sont prévus ;
- les artefacts de publication sont signés ;
- une violation échoue fermée ;
- le gameplay conserve un repli déterministe.

## 29. Checklist Solo

- [ ] Maintenir le modèle de menaces.
- [ ] Écouter sur `127.0.0.1`.
- [ ] Refuser `0.0.0.0`.
- [ ] Exclure outils de production et secrets.
- [ ] Autoriser seulement opérations et modèles runtime.
- [ ] Valider les chemins.
- [ ] Borner requêtes et tâches.
- [ ] Rédiger et faire tourner les journaux.
- [ ] Épingler les dépendances.
- [ ] Générer un SBOM et signer le build public.
- [ ] Conserver le repli déterministe.

## 30. Checklist Studio

- [ ] Nommer les responsables.
- [ ] Revoir le modèle de menaces.
- [ ] Utiliser coffre, rotation et révocation.
- [ ] Définir identités et autorisations.
- [ ] Gérer TLS, certificats et segmentation.
- [ ] Définir quotas par identité.
- [ ] Centraliser les événements avec rétention.
- [ ] Scanner les dépendances.
- [ ] Produire SBOM et provenance à chaque build.
- [ ] Protéger les clés de signature.
- [ ] Tester vérification et rollback.
- [ ] Maintenir une procédure d’incident.

## 31. Sources techniques

Sources principales relues pour l’audit statique du 19 juillet 2026 :

- [OWASP — Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) ;
- [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) ;
- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) ;
- [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) ;
- [OWASP — WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html) ;
- [NIST — SSDF SP 800-218 version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) ;
- [NIST — SSDF version 1.2, brouillon initial](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) ;
- [NIST — SP 800-218A pour l’IA](https://csrc.nist.gov/pubs/sp/800/218/a/final) ;
- [CISA — Bibliothèque SBOM](https://www.cisa.gov/topics/cyber-threats-and-advisories/sbom/sbomresourceslibrary) ;
- [Godot Engine 4.7 — Exporting projects](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_projects.html) ;
- [Godot Engine 4.7 — Command line tutorial](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html) ;
- [Godot Engine 4.7 — TLSOptions](https://docs.godotengine.org/en/4.7/classes/class_tlsoptions.html) ;
- [Python 3.12 — `secrets`](https://docs.python.org/3.12/library/secrets.html) ;
- [Python 3.12 — `ssl`](https://docs.python.org/3.12/library/ssl.html) ;
- [Python 3.12 — Security Considerations](https://docs.python.org/3.12/library/security_warnings.html) ;
- [Microsoft Learn — `Read-Host` et `-MaskInput`](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/read-host?view=powershell-7.5).

La version finale publiée du SSDF reste `1.1` à la date d’audit. La version `1.2` est citée comme brouillon.

## 32. Réserves de validation

Ne sont pas exécutés :

- scripts GDScript dans Godot ;
- écoute et pare-feu Windows ;
- authentification, TLS et certificats ;
- rotation des secrets ;
- restrictions du compte de service ;
- limites mémoire et CPU ;
- quotas concurrents ;
- rédaction sur des logs réels ;
- détection de secrets et scan de vulnérabilités ;
- génération d’un SBOM réel ;
- provenance attestée ;
- signature de code ;
- mise à jour et rollback ;
- packaging multi-plateforme.

Aucun PDF intermédiaire n’est construit.

## 33. Résultat attendu

`Project Asteria` possède désormais une plateforme IA locale documentée de bout en bout : mémoire dérivée, port applicatif, transports, files bornées, frontières de confiance, secrets, autorisations, limites, journaux, dépendances, SBOM, signature et échec fermé.

Le chapitre 14 peut commencer les systèmes de gameplay sur une plateforme dont les responsabilités et limites de sécurité sont explicites.
