---
title: "Livre II — Chapitre 28 : Journalisation, diagnostic et reproductibilité"
id: "DOC-L2-CH28"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 28
last-verified: "2026-07-22T03:02:36+02:00"
audit-status: "complete"
audit-date: "2026-07-22T03:02:36+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-28.md"
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

# Journalisation, diagnostic et reproductibilité

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH28`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-28.md`.  
> **Explications de code :** structurées bloc par bloc ; les sections d’erreurs conservent la séquence directe symptôme, exemple fautif, explication, exemple corrigé et explication de la correction.

## 1. Rôle du chapitre

Un système observable ne se contente pas d’imprimer des phrases. Il produit des événements structurés, des métriques bornées, des traces corrélées et des artefacts de diagnostic qui permettent de répondre à quatre questions :

- que s’est-il passé ;
- dans quel ordre causal ;
- avec quel état et quelle version ;
- comment reproduire le problème sans exposer de secret ni de donnée personnelle inutile.

Le chapitre construit une chaîne locale et déterministe pour `Project Asteria`. Elle fonctionne hors ligne, n’impose aucun service distant au runtime et peut ensuite alimenter un collecteur externe par un adaptateur facultatif.

## 2. Prérequis et frontières

Le lecteur doit connaître les identifiants stables, commandes, résultats, événements de domaine, horloges logiques, sauvegardes, pipelines de contenu et campagnes de tests des chapitres précédents.

Le chapitre 27 reste l’autorité des suites, fixtures, scénarios, graines et critères de passage. Le présent chapitre consomme leurs sorties et ajoute les preuves nécessaires au diagnostic. Le chapitre 29 automatisera la collecte, l’analyse et la génération de données en Python. Le chapitre 30 décidera l’organisation complète des parcours Solo et Studio.

Les journaux n’ont aucune autorité métier. Ils décrivent un événement déjà décidé par son système propriétaire. Une ligne de journal ne remplace ni une écriture de dépôt, ni un événement de domaine, ni une preuve juridique du chapitre 23, ni une sauvegarde.

## 3. Définitions opérationnelles

### 3.1 Journal

Un journal est une suite ordonnée d’enregistrements. Chaque enregistrement possède un nom d’événement stable, une sévérité, un instant d’observation, un contexte et un résultat.

### 3.2 Diagnostic

Un diagnostic relie plusieurs observations afin d’expliquer une panne, un refus, une lenteur ou une divergence. Il peut inclure journaux, métriques, traces, manifestes, empreintes et informations de version.

### 3.3 Reproductibilité

La reproductibilité consiste à fournir les entrées, versions, graines, commandes et artefacts minimaux permettant de rejouer un comportement observé. Elle n’exige pas de copier toutes les données de la partie.

### 3.4 Corrélation et causalité

La corrélation regroupe les événements d’une même opération. La causalité indique quel événement ou quelle commande a provoqué le suivant. Deux événements corrélés ne sont pas nécessairement dans une relation parent-enfant.

## 4. Portfolio des signaux

> **[LECTURE] Carte des signaux — Ne pas saisir.**

```text
Événement métier accepté
        │
        ├── journal structuré : ce qui s’est produit
        ├── métrique : quantité ou distribution agrégée
        ├── trace : chemin et durée d’une opération
        └── artefact : preuve persistante pour le diagnostic
                     │
                     ├── manifeste de reproduction
                     ├── extraits de journaux
                     ├── résultats de tests
                     ├── empreintes
                     └── archive de support
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les quatre signaux sont complémentaires ; aucun ne remplace les autres.
- **Frontières d’autorité :** L’événement métier précède l’observation. La télémétrie n’autorise ni ne rejoue une mutation.
- **Résultat attendu :** Une enquête peut partir d’un journal, retrouver la trace, lire les métriques puis ouvrir un paquet de reproduction.

## 5. Arborescence de référence

> **[LECTURE] Dossiers de diagnostic — Ne pas saisir.**

```text
src/shared/observability/
├── domain/
│   ├── telemetry_event.gd
│   ├── telemetry_severity.gd
│   └── telemetry_policy.gd
├── application/
│   ├── telemetry_port.gd
│   ├── metric_registry.gd
│   ├── trace_recorder.gd
│   └── diagnostic_package_service.gd
└── infrastructure/
    ├── jsonl_telemetry_sink.gd
    ├── threaded_engine_logger.gd
    ├── diagnostic_manifest_codec.gd
    └── zip_diagnostic_writer.gd
config/observability/
├── event-catalog.v1.json
└── redaction-policy.v1.json
user://diagnostics/
├── sessions/
├── packages/
└── pending/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** Le domaine définit les valeurs, l’application les contrats et l’infrastructure les écritures concrètes.
- **Dépendances et ports utilisés :** Les systèmes de gameplay dépendent uniquement de `TelemetryPort`.
- **Effets de bord :** Seuls les adaptateurs d’infrastructure écrivent sous `user://diagnostics`.
- **Limites et réserves :** Les dossiers `user://` sont créés au runtime et ne sont jamais ajoutés au dépôt Git.

## 6. Activer la journalisation native de Godot

Godot peut écrire les sorties et erreurs dans `user://logs/godot.log`, avec rotation. Le projet conserve cette voie native pour les messages du moteur et ajoute un journal JSONL distinct pour les événements structurés.

> **[VSC] Extrait de `project.godot` — Ne pas saisir dans un terminal.**

```ini
[application]

run/flush_stdout_on_print=false

[debug]

file_logging/enable_file_logging=true
file_logging/log_path="user://logs/godot.log"
file_logging/max_log_files=5
settings/gdscript/always_track_call_stacks=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** La rotation conserve cinq fichiers ; le suivi permanent des piles en release reste désactivé par défaut.
- **Effets de bord :** Les sorties du moteur et les appels `print`, `push_warning` ou `push_error` alimentent le fichier natif.
- **Limites et réserves :** `flush_stdout_on_print` améliore la persistance en cas d’arrêt brutal mais peut coûter cher lorsque le volume est élevé.
- **Résultat attendu :** Le journal du moteur reste disponible même si le journal structuré de l’application est incomplet.

## 7. Catégories de sortie Godot

> **[LECTURE] Usage des sorties natives — Ne pas saisir.**

```text
print_verbose()  diagnostic détaillé activé explicitement
print()          information de développement ponctuelle
push_warning()   situation anormale mais récupérable
push_error()     échec qui demande une correction
printerr()       sortie stderr de bas niveau
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** La liste sépare verbosité, information, avertissement et échec.
- **Frontières d’autorité :** Ces sorties servent au moteur et au développement ; le contrat applicatif utilise en plus un événement structuré.
- **Limites et réserves :** Une chaîne localisée ou destinée au joueur ne devient jamais un identifiant d’événement.

## 8. Niveaux de sévérité

Le projet adopte six niveaux compatibles avec la progression usuelle `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL`. La valeur numérique facilite les comparaisons et les filtres.

> **[VSC] Fichier `telemetry_severity.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetrySeverity
extends RefCounted

enum Value {
    TRACE = 1,
    DEBUG = 5,
    INFO = 9,
    WARN = 13,
    ERROR = 17,
    FATAL = 21,
}

static func name_of(value: Value) -> StringName:
    match value:
        Value.TRACE:
            return &"TRACE"
        Value.DEBUG:
            return &"DEBUG"
        Value.INFO:
            return &"INFO"
        Value.WARN:
            return &"WARN"
        Value.ERROR:
            return &"ERROR"
        Value.FATAL:
            return &"FATAL"
        _:
            return &"UNSPECIFIED"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Les valeurs numériques suivent les débuts de plages du modèle de journaux OpenTelemetry.
- **Valeur de retour ou code d’échec :** `name_of()` transforme l’énumération en nom stable destiné à la sérialisation.
- **Invariants protégés :** Une sévérité plus grande représente toujours une situation plus grave.
- **Limites et réserves :** Le projet n’implémente pas pour autant un SDK OpenTelemetry complet.

## 9. Politique de sévérité

> **[LECTURE] Décision de niveau — Ne pas saisir.**

```text
TRACE  étapes internes très fines, désactivées par défaut
DEBUG  données nécessaires au développement ou à un diagnostic ciblé
INFO   transition normale importante pour l’exploitation
WARN   repli, refus inhabituel ou dégradation récupérable
ERROR  opération échouée, état cohérent mais action non accomplie
FATAL  arrêt imminent, corruption détectée ou impossibilité de continuer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Chaque niveau décrit l’effet opérationnel plutôt que l’émotion du message.
- **Invariants protégés :** Un refus métier prévu n’est pas automatiquement une erreur ; il devient `INFO` ou `WARN` selon son intérêt opérationnel.
- **Résultat attendu :** Deux équipes classent un même événement de manière cohérente.

## 10. Catalogue des événements stables

Les noms d’événement sont versionnés. Une phrase libre peut changer ; `save.snapshot.write_failed` reste stable.

> **[VSC] Fichier `config/observability/event-catalog.v1.json` — Ne pas saisir dans un terminal.**

```json
{
  "schema_version": 1,
  "events": {
    "application.session.started": {
      "default_severity": "INFO",
      "allowed_attributes": [
        "build_id",
        "platform",
        "renderer"
      ]
    },
    "save.snapshot.write_failed": {
      "default_severity": "ERROR",
      "allowed_attributes": [
        "slot_id",
        "reason_id",
        "error_code"
      ]
    },
    "simulation.invariant.violated": {
      "default_severity": "ERROR",
      "allowed_attributes": [
        "scenario_id",
        "invariant_id",
        "logical_tick"
      ]
    }
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Chaque événement définit sa sévérité par défaut et la liste fermée de ses attributs.
- **Sécurité et confidentialité :** Une clé non autorisée est rejetée avant écriture, ce qui réduit les fuites accidentelles.
- **Invariants protégés :** Le nom d’événement n’inclut ni identifiant d’instance, ni message, ni valeur dynamique.
- **Limites et réserves :** Toute évolution incompatible du catalogue exige une nouvelle version de schéma.

## 11. Schéma d’un enregistrement

> **[LECTURE] Enregistrement JSONL canonique — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "event_name": "save.snapshot.write_failed",
  "severity_number": 17,
  "severity_text": "ERROR",
  "occurred_at_utc": "2026-07-22T00:41:12Z",
  "observed_monotonic_us": 8421199,
  "run_id": "7d5938f38bfb4fb6a1eb180a42433179",
  "correlation_id": "487e1a9d8a7d421b82db7793fd107bf0",
  "causation_id": "cmd.save.0194",
  "logical_tick": 412,
  "system_id": "save",
  "status": "failed",
  "reason_id": "save.reason.disk_full",
  "attributes": {
    "slot_id": "slot.1",
    "error_code": 19
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les champs communs restent au premier niveau ; les détails propres à l’événement restent sous `attributes`.
- **Paramètres et types importants :** L’instant UTC décrit l’occurrence ; le compteur monotone permet de mesurer un ordre local et des durées.
- **Invariants protégés :** `event_name`, `system_id`, `status` et `reason_id` sont des identifiants stables.
- **Limites et réserves :** Le journal ne contient pas le chemin absolu du profil utilisateur ni le contenu complet de la sauvegarde.

## 12. Contexte de télémétrie

> **[VSC] Fichier `telemetry_context.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryContext
extends RefCounted

var run_id: String
var correlation_id: String
var causation_id: StringName
var logical_tick: int = -1

func child(
    child_correlation_id: String = correlation_id,
    child_causation_id: StringName = causation_id
) -> TelemetryContext:
    var value := TelemetryContext.new()
    value.run_id = run_id
    value.correlation_id = child_correlation_id
    value.causation_id = child_causation_id
    value.logical_tick = logical_tick
    return value
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Le contexte transporte les identifiants nécessaires sans dépendre d’un nœud de scène.
- **Paramètres et types importants :** Un tick négatif signifie qu’aucun tick logique n’appartient à l’opération.
- **Valeur de retour ou code d’échec :** `child()` crée une copie détachée et conserve le `run_id`.
- **Invariants protégés :** Une sous-opération ne modifie jamais le contexte de son parent.

## 13. Fabriquer des identifiants opaques

Les identifiants de corrélation ne doivent contenir ni nom de joueur, ni adresse, ni chemin. Ils utilisent des octets aléatoires cryptographiquement sûrs.

> **[VSC] Fichier `telemetry_id_factory.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryIdFactory
extends RefCounted

var _crypto := Crypto.new()

func new_128_bit_id() -> String:
    return _crypto.generate_random_bytes(16).hex_encode()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Seize octets produisent un identifiant hexadécimal de 128 bits.
- **Sécurité et confidentialité :** La valeur est opaque et ne révèle aucune donnée métier.
- **Effets de bord :** Chaque appel consulte le générateur cryptographique du système.
- **Limites et réserves :** Ces identifiants ne servent pas au gameplay pseudo-aléatoire déterministe.

## 14. Temps UTC et compteur monotone

L’horloge système sert à dater un événement pour une personne. Le compteur monotone sert à mesurer une durée dans le processus. Aucun des deux ne remplace le tick logique.

> **[VSC] Aide `telemetry_clock.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryClock
extends RefCounted

static func utc_now() -> String:
    return Time.get_datetime_string_from_system(true) + "Z"

static func monotonic_us() -> int:
    return Time.get_ticks_usec()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur de retour ou code d’échec :** `utc_now()` produit une date ISO 8601 en UTC ; `monotonic_us()` renvoie les microsecondes depuis le démarrage du moteur.
- **Invariants protégés :** Les durées utilisent uniquement le compteur monotone, qui ne recule pas.
- **Limites et réserves :** L’horloge système peut être corrigée par l’utilisateur ou le système d’exploitation ; elle ne décide donc jamais d’une règle métier.

## 15. Valeur d’événement typée

> **[VSC] Fichier `telemetry_event.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryEvent
extends RefCounted

var event_name: StringName
var severity: TelemetrySeverity.Value
var system_id: StringName
var status: StringName
var reason_id: StringName
var context: TelemetryContext
var attributes: Dictionary = {}

func validate() -> PackedStringArray:
    var errors := PackedStringArray()
    if event_name == &"":
        errors.append("empty_event_name")
    if system_id == &"":
        errors.append("empty_system_id")
    if context == null:
        errors.append("missing_context")
    return errors
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** L’objet sépare identité, sévérité, résultat, contexte et attributs.
- **Valeur de retour ou code d’échec :** `validate()` renvoie plusieurs diagnostics au lieu d’un booléen muet.
- **Invariants protégés :** Aucun événement n’est accepté sans nom, système propriétaire et contexte.
- **Limites et réserves :** La validation du catalogue et des attributs est réalisée ensuite par la politique.

## 16. Port applicatif

> **[VSC] Fichier `telemetry_port.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryPort
extends RefCounted

func emit(event_value: TelemetryEvent) -> Error:
    push_error("TelemetryPort.emit() must be implemented.")
    return ERR_UNAVAILABLE

func flush() -> Error:
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Les systèmes applicatifs dépendent du port, jamais d’un fichier JSONL ou d’un service distant.
- **Codes de retour :** `ERR_UNAVAILABLE` indique qu’aucun adaptateur n’est installé.
- **Effets de bord :** L’implémentation peut écrire, mettre en file ou ignorer selon la configuration.
- **Limites et réserves :** Le port ne doit pas lever une exception métier lorsqu’un journal secondaire échoue.

## 17. Politique de minimisation

Le projet utilise une liste autorisée par événement, puis une rédaction défensive pour les clés sensibles connues.

> **[VSC] Fichier `telemetry_policy.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryPolicy
extends RefCounted

const SENSITIVE_KEYS := {
    "password": true,
    "token": true,
    "access_token": true,
    "refresh_token": true,
    "authorization": true,
    "cookie": true,
    "connection_string": true,
    "encryption_key": true,
}

var _catalog: Dictionary

func _init(catalog: Dictionary) -> void:
    _catalog = catalog.duplicate(true)

func filter_attributes(
    event_name: StringName,
    source: Dictionary
) -> Dictionary:
    var definition: Dictionary = _catalog["events"].get(
        String(event_name),
        {}
    )
    var allowed: Array = definition.get(
        "allowed_attributes",
        []
    )
    var filtered := {}
    for key in allowed:
        if SENSITIVE_KEYS.has(String(key).to_lower()):
            filtered[key] = "[REDACTED]"
        elif source.has(key):
            filtered[key] = _sanitize_value(source[key])
    return filtered
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sécurité et confidentialité :** Seules les clés déclarées dans le catalogue peuvent sortir du système.
- **Déroulement ou instructions importantes :** La clé sensible est masquée avant toute sérialisation ; les autres valeurs passent par une normalisation.
- **Invariants protégés :** Une donnée inconnue ne devient jamais journalisable par défaut.
- **Limites et réserves :** Une rédaction par nom de clé ne suffit pas seule ; la liste autorisée reste le contrôle principal.

## 18. Nettoyer les chaînes

> **[VSC] Suite de `telemetry_policy.gd` — Ne pas saisir dans Godot.**

```gdscript
const MAX_TEXT_LENGTH := 512

func _sanitize_value(value: Variant) -> Variant:
    if value is String:
        var text := value as String
        text = text.replace("\r", " ")
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        return text.left(MAX_TEXT_LENGTH)
    if value is StringName:
        return String(value)
    if value is int or value is float or value is bool:
        return value
    return "[UNSUPPORTED]"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Opérateurs et conversions non évidents :** Les retours à la ligne sont remplacés afin qu’un enregistrement reste sur une seule ligne JSONL.
- **Paramètres et types importants :** La longueur maximale borne l’espace disque et la taille d’un paquet.
- **Valeur de retour ou code d’échec :** Les types non approuvés deviennent une sentinelle explicite.
- **Sécurité et confidentialité :** Les objets, nœuds et ressources ne sont jamais sérialisés implicitement.

## 19. Construire l’enregistrement

> **[VSC] Fichier `telemetry_record_builder.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetryRecordBuilder
extends RefCounted

var _policy: TelemetryPolicy

func build(event_value: TelemetryEvent) -> Dictionary:
    return {
        "schema_version": 1,
        "event_name": String(event_value.event_name),
        "severity_number": int(event_value.severity),
        "severity_text": TelemetrySeverity.name_of(
            event_value.severity
        ),
        "occurred_at_utc": TelemetryClock.utc_now(),
        "observed_monotonic_us": TelemetryClock.monotonic_us(),
        "run_id": event_value.context.run_id,
        "correlation_id": event_value.context.correlation_id,
        "causation_id": String(event_value.context.causation_id),
        "logical_tick": event_value.context.logical_tick,
        "system_id": String(event_value.system_id),
        "status": String(event_value.status),
        "reason_id": String(event_value.reason_id),
        "attributes": _policy.filter_attributes(
            event_value.event_name,
            event_value.attributes
        ),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Le builder rassemble les champs communs et délègue la minimisation à la politique.
- **Paramètres et types importants :** Les `StringName` sont convertis en chaînes sérialisables.
- **Invariants protégés :** Tous les événements utilisent le même schéma et le même vocabulaire temporel.
- **Limites et réserves :** Le dictionnaire doit encore être validé par le codec avant écriture.

## 20. Écrire en JSONL

Un fichier JSONL contient un objet JSON par ligne. Une ligne incomplète peut être ignorée sans invalider les lignes précédentes.

> **[VSC] Fichier `jsonl_telemetry_sink.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name JsonlTelemetrySink
extends TelemetryPort

const ROOT := "user://diagnostics/sessions"
const FLUSH_EVERY := 32

var _builder: TelemetryRecordBuilder
var _file: FileAccess
var _pending_since_flush := 0

func open(run_id: String) -> Error:
    var absolute := ProjectSettings.globalize_path(ROOT)
    var make_error := DirAccess.make_dir_recursive_absolute(absolute)
    if make_error != OK:
        return make_error

    var path := "%s/%s.jsonl" % [ROOT, run_id]
    if FileAccess.file_exists(path):
        _file = FileAccess.open(path, FileAccess.READ_WRITE)
        _file.seek_end()
    else:
        _file = FileAccess.open(path, FileAccess.WRITE_READ)
    return FileAccess.get_open_error()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le dossier est créé, le fichier existant est ouvert sans troncature, puis le curseur est placé à la fin.
- **Codes de retour :** L’erreur de création du dossier ou d’ouverture est propagée à l’appelant.
- **Effets de bord :** Un fichier par `run_id` isole les sessions.
- **Limites et réserves :** Le sink est utilisé sur le thread principal ; le logger moteur multithread passe par une file séparée.

## 21. Émettre et vider

> **[VSC] Suite de `jsonl_telemetry_sink.gd` — Ne pas saisir dans Godot.**

```gdscript
func emit(event_value: TelemetryEvent) -> Error:
    var validation := event_value.validate()
    if not validation.is_empty():
        return ERR_INVALID_DATA
    if _file == null:
        return ERR_UNCONFIGURED

    var record := _builder.build(event_value)
    var line := JSON.stringify(record)
    if not _file.store_line(line):
        return ERR_CANT_WRITE

    _pending_since_flush += 1
    if (
        event_value.severity >= TelemetrySeverity.Value.ERROR
        or _pending_since_flush >= FLUSH_EVERY
    ):
        return flush()
    return OK

func flush() -> Error:
    if _file == null:
        return ERR_UNCONFIGURED
    _file.flush()
    _pending_since_flush = 0
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Codes de retour :** Les données invalides, l’absence de configuration et l’échec d’écriture sont distingués.
- **Déroulement ou instructions importantes :** Les événements graves forcent immédiatement un `flush`; les autres sont regroupés par lot.
- **Effets de bord :** `flush()` demande au système de fichiers de pousser les données en attente.
- **Limites et réserves :** Un `flush` ne garantit pas la survie à toutes les pannes matérielles ; il réduit seulement la fenêtre de perte.

## 22. Rotation et rétention

Le journal structuré applique une limite par fichier, un nombre maximal de sessions et une durée de rétention. La suppression se fait au démarrage ou lors d’une maintenance, jamais dans la méthode `emit()`.

> **[LECTURE] Politique de rétention — Ne pas saisir.**

```text
taille maximale d’un fichier     16 MiB
fichiers de session conservés    10
paquets de diagnostic locaux     5
rétention par défaut             14 jours
événements ERROR et FATAL        jamais échantillonnés
suppression                      avant ouverture d’une nouvelle session
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les limites portent sur taille, quantité et durée.
- **Invariants protégés :** La journalisation ne peut pas remplir le disque sans borne.
- **Limites et réserves :** Une politique Studio peut adapter les valeurs selon le produit et les obligations légales.

## 23. Capturer les messages du moteur

Godot 4.7 permet d’enregistrer un `Logger` personnalisé. Ses méthodes peuvent être appelées depuis plusieurs threads ; elles ne doivent ni imprimer ni écrire directement dans un fichier partagé sans synchronisation.

> **[VSC] Fichier `threaded_engine_logger.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name ThreadedEngineLogger
extends Logger

var _mutex := Mutex.new()
var _pending: Array[Dictionary] = []

func _log_message(message: String, error: bool) -> void:
    var record := {
        "kind": "engine_message",
        "stderr": error,
        "message": message.left(512),
    }
    _mutex.lock()
    _pending.append(record)
    _mutex.unlock()

func drain() -> Array[Dictionary]:
    _mutex.lock()
    var result := _pending.duplicate(true)
    _pending.clear()
    _mutex.unlock()
    return result

func pending_count() -> int:
    _mutex.lock()
    var result := _pending.size()
    _mutex.unlock()
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Les callbacks se contentent d’enfiler ; `drain()` transfère les données au thread principal.
- **Sécurité des threads :** Le mutex protège le tableau pendant la copie et la remise à zéro.
- **Effets de bord :** Aucun appel à `print`, `push_error` ou au sink n’a lieu depuis le logger, ce qui évite la récursion.
- **Limites et réserves :** La file doit recevoir une capacité maximale afin qu’un flot moteur anormal ne consomme pas toute la mémoire.

## 24. Capturer les erreurs du moteur

> **[VSC] Suite de `threaded_engine_logger.gd` — Ne pas saisir dans Godot.**

```gdscript
func _log_error(
    function: String,
    file: String,
    line: int,
    code: String,
    rationale: String,
    editor_notify: bool,
    error_type: int,
    script_backtraces: Array[ScriptBacktrace]
) -> void:
    var record := {
        "kind": "engine_error",
        "function": function,
        "file": file,
        "line": line,
        "code": code.left(256),
        "rationale": rationale.left(512),
        "error_type": error_type,
        "backtraces": _format_backtraces(script_backtraces),
    }
    _mutex.lock()
    _pending.append(record)
    _mutex.unlock()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Le moteur fournit emplacement, code, justification, type et piles de scripts.
- **Sécurité et confidentialité :** Les textes sont bornés ; les variables locales ne sont pas capturées.
- **Effets de bord :** L’enregistrement reste en mémoire jusqu’au drainage.
- **Limites et réserves :** Les piles utiles en release demandent une option de suivi qui consomme de la mémoire.

## 25. Enregistrer et retirer le logger

> **[VSC] Autoload `observability_service.gd` — Ne pas saisir dans Godot.**

```gdscript
extends Node

var _engine_logger := ThreadedEngineLogger.new()
var _sink: JsonlTelemetrySink

func _ready() -> void:
    OS.add_logger(_engine_logger)

func _process(_delta: float) -> void:
    for record in _engine_logger.drain():
        _consume_engine_record(record)

func _exit_tree() -> void:
    OS.remove_logger(_engine_logger)
    if _sink != null:
        _sink.flush()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le logger est enregistré au démarrage, vidé chaque frame et retiré avant destruction.
- **Effets de bord :** Les callbacks moteur sont transformés sur le thread principal.
- **Invariants protégés :** Un logger détruit n’est jamais laissé enregistré dans `OS`.
- **Limites et réserves :** L’ordre d’initialisation de l’Autoload doit précéder les systèmes qui émettent des événements applicatifs.

## 26. Piles d’appels et variables

Une pile d’appels aide à localiser une panne. Les variables locales peuvent contenir secrets, données personnelles et références d’objets ; elles ne sont donc pas capturées par défaut.

> **[VSC] Projection sûre d’une pile — Ne pas saisir dans Godot.**

```gdscript
func _format_backtraces(
    values: Array[ScriptBacktrace]
) -> Array[Dictionary]:
    var result: Array[Dictionary] = []
    for value in values:
        var frames: Array[Dictionary] = []
        for index in range(value.get_frame_count()):
            frames.append({
                "file": value.get_frame_file(index),
                "function": value.get_frame_function(index),
                "line": value.get_frame_line(index),
            })
        result.append({
            "language": value.get_language_name(),
            "frames": frames,
        })
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Chaque langage possède sa liste ordonnée de frames.
- **Sécurité et confidentialité :** Seuls fichier, fonction et ligne sont conservés.
- **Limites et réserves :** Les chemins doivent être localisés sous `res://` ou réduits avant export afin de ne pas révéler un chemin utilisateur absolu.

## 27. Journaliser une commande et son résultat

> **[VSC] Instrumentation d’un service de sauvegarde — Ne pas saisir.**

```gdscript
func save(command: SaveCommand) -> SaveResult:
    var context := _telemetry_context_for(command.command_id)
    _telemetry.emit(
        TelemetryEvents.save_requested(command, context)
    )

    var result := _save_core(command)

    _telemetry.emit(
        TelemetryEvents.save_completed(command, result, context)
    )
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Un événement précède l’opération et un autre décrit son résultat.
- **Frontières d’autorité :** `_save_core()` reste l’unique lieu qui décide et écrit la sauvegarde.
- **Invariants protégés :** Les deux événements partagent la même corrélation.
- **Limites et réserves :** Le snapshot complet n’est jamais ajouté aux attributs.

## 28. Corrélation entre systèmes

Une transaction multi-autorités propage le même `correlation_id`. Chaque commande ou événement conserve son `causation_id`.

> **[LECTURE] Chaîne causale — Ne pas saisir.**

```text
cmd.trade.104
  correlation_id = 48ab...
        │
        ├── economy.quote.prepared
        │     causation_id = cmd.trade.104
        ├── inventory.transfer.prepared
        │     causation_id = cmd.trade.104
        └── trade.commit.completed
              causation_id = receipt.trade.104
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** La corrélation relie le lot ; la causalité relie chaque enfant à sa cause immédiate.
- **Invariants protégés :** Une enquête peut distinguer deux opérations simultanées portant sur les mêmes objets.
- **Limites et réserves :** L’ordre visuel d’un fichier ne suffit pas à établir la causalité lorsque plusieurs threads ou processus participent.

## 29. Trace et span

Une trace décrit le chemin d’une opération. Un span possède un début monotone, une fin, un statut et éventuellement un parent.

> **[VSC] Fichier `trace_span.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TraceSpan
extends RefCounted

var trace_id: String
var span_id: String
var parent_span_id: String
var operation_name: StringName
var started_us: int
var ended_us: int = -1
var status: StringName = &"unset"

func finish(result_status: StringName) -> void:
    if ended_us >= 0:
        return
    status = result_status
    ended_us = Time.get_ticks_usec()

func duration_us() -> int:
    if ended_us < 0:
        return -1
    return ended_us - started_us
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Les identifiants sont opaques ; les noms d’opération sont stables.
- **Déroulement ou instructions importantes :** `finish()` est idempotente et fixe une seule fin.
- **Valeur de retour ou code d’échec :** Une durée négative indique un span non terminé.
- **Invariants protégés :** La durée utilise le compteur monotone et ne dépend pas d’une correction de l’horloge système.

## 30. Recorder de traces borné

> **[VSC] Fichier `trace_recorder.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name TraceRecorder
extends RefCounted

const MAX_COMPLETED_SPANS := 2048

var _completed: Array[Dictionary] = []

func record_completed(span: TraceSpan) -> void:
    _completed.append({
        "trace_id": span.trace_id,
        "span_id": span.span_id,
        "parent_span_id": span.parent_span_id,
        "operation_name": String(span.operation_name),
        "duration_us": span.duration_us(),
        "status": String(span.status),
    })
    if _completed.size() > MAX_COMPLETED_SPANS:
        _completed.pop_front()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Le recorder conserve une projection détachée plutôt que les objets actifs.
- **Effets de bord :** Le plus ancien span est supprimé lorsque la capacité est dépassée.
- **Invariants protégés :** La mémoire utilisée par les traces reste bornée.
- **Limites et réserves :** Un export Studio peut vider périodiquement la file avant la perte des anciens spans.

## 31. Propager un contexte vers un service local

À une frontière HTTP, le projet peut utiliser `traceparent` lorsqu’un service est compatible W3C. Sinon, un en-tête interne de corrélation suffit, sans inventer une conformité complète.

> **[VSC] Construction des en-têtes — Ne pas saisir dans Godot.**

```gdscript
func build_headers(context: TelemetryContext) -> PackedStringArray:
    return PackedStringArray([
        "Content-Type: application/json",
        "X-Asteria-Run-Id: %s" % context.run_id,
        "X-Asteria-Correlation-Id: %s"
            % context.correlation_id,
        "X-Asteria-Causation-Id: %s"
            % String(context.causation_id),
    ])
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les trois en-têtes transmettent session, corrélation et cause.
- **Sécurité et confidentialité :** Les valeurs sont opaques et ne contiennent aucune donnée de joueur.
- **Limites et réserves :** Ces en-têtes privés ne sont pas une implémentation de `traceparent`; un adaptateur dédié devra valider le format W3C.

## 32. Registre de métriques

Les métriques agrègent. Elles ne conservent pas une ligne par personnage, quête ou objet.

> **[VSC] Fichier `metric_registry.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name MetricRegistry
extends RefCounted

var _counters: Dictionary = {}
var _gauges: Dictionary = {}

func increment(
    metric_name: StringName,
    labels: Dictionary = {},
    amount: int = 1
) -> void:
    var key := _series_key(metric_name, labels)
    _counters[key] = int(_counters.get(key, 0)) + amount

func set_gauge(
    metric_name: StringName,
    labels: Dictionary,
    value: int
) -> void:
    _gauges[_series_key(metric_name, labels)] = value

func snapshot() -> Dictionary:
    return {
        "counters": _counters.duplicate(true),
        "gauges": _gauges.duplicate(true),
    }

func _series_key(
    metric_name: StringName,
    labels: Dictionary
) -> String:
    return "%s|%s" % [
        String(metric_name),
        JSON.stringify(CanonicalValue.normalize(labels)),
    ]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Les compteurs progressent ; les jauges représentent une valeur courante ; les labels sont normalisés avant de former la clé de série.
- **Valeur de retour ou code d’échec :** `snapshot()` produit une copie détachée.
- **Invariants protégés :** Deux dictionnaires de labels équivalents produisent la même clé canonique et le registre ne publie pas ses dictionnaires internes.
- **Limites et réserves :** Les distributions de durée exigent un histogramme borné, ajouté séparément.

## 33. Histogramme de durée

> **[VSC] Histogramme à limites fixes — Ne pas saisir dans Godot.**

```gdscript
class_name FixedHistogram
extends RefCounted

var _bounds_us := PackedInt64Array([
    1000,
    5000,
    10000,
    50000,
    100000,
    500000,
    1000000,
])
var _counts := PackedInt64Array()

func _init() -> void:
    _counts.resize(_bounds_us.size() + 1)

func observe(value_us: int) -> void:
    for index in range(_bounds_us.size()):
        if value_us <= _bounds_us[index]:
            _counts[index] += 1
            return
    _counts[_counts.size() - 1] += 1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les sept limites produisent huit buckets, dont le dernier reçoit les valeurs supérieures.
- **Paramètres et types importants :** Les durées sont des entiers en microsecondes.
- **Invariants protégés :** Le nombre de séries reste constant quelle que soit la quantité d’observations.
- **Limites et réserves :** Les bornes doivent être choisies selon le contrat de l’opération, pas selon une mesure unique.

## 34. Budget de cardinalité

> **[LECTURE] Attributs autorisés pour les métriques — Ne pas saisir.**

```text
autorisé :
  platform = Windows | Linux | macOS
  build_channel = dev | qa | release
  result = success | rejected | failed
  system = save | economy | ecology

interdit :
  character_id
  item_instance_id
  quest_id dynamique
  chemin de fichier
  message d’erreur libre
  correlation_id
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Les attributs autorisés possèdent un petit ensemble fermé de valeurs.
- **Invariants protégés :** Le nombre de séries ne croît pas avec le nombre d’entités ou de sessions.
- **Limites et réserves :** Les identifiants détaillés restent dans les journaux et traces ciblées, pas dans les métriques.

## 35. Échantillonnage

Le projet n’échantillonne jamais les événements `ERROR`, `FATAL`, les violations de sécurité ni les changements de configuration. Les traces réussies et les événements `DEBUG` peuvent être réduits.

> **[VSC] Politique d’échantillonnage — Ne pas saisir dans Godot.**

```gdscript
class_name TelemetrySamplingPolicy
extends RefCounted

func keep(
    severity: TelemetrySeverity.Value,
    event_name: StringName,
    stable_hash: int
) -> bool:
    if severity >= TelemetrySeverity.Value.ERROR:
        return true
    if String(event_name).begins_with("security."):
        return true
    if severity <= TelemetrySeverity.Value.DEBUG:
        return posmod(stable_hash, 100) < 10
    return true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Les événements graves sont conservés ; les événements détaillés utilisent un seuil de dix pour cent.
- **Paramètres et types importants :** Le hash doit provenir d’une clé stable de l’opération afin que deux décisions identiques donnent le même échantillonnage.
- **Invariants protégés :** Un incident grave n’est jamais masqué par une réduction de volume.
- **Limites et réserves :** Le `hash()` natif ne sert pas à la sécurité ; il ne décide ici que d’un échantillonnage.

## 36. État de santé

> **[VSC] Snapshot de santé applicative — Ne pas saisir dans Godot.**

```gdscript
func build_health_snapshot() -> Dictionary:
    return {
        "schema_version": 1,
        "observed_at_utc": TelemetryClock.utc_now(),
        "logical_tick": _world_clock.now_tick(),
        "active_characters": _character_registry.count(),
        "pending_events": _event_queue.size(),
        "pending_ai_requests": _ai_gateway.pending_count(),
        "save_state": String(_save_service.health_status()),
        "telemetry_queue_depth": _engine_logger.pending_count(),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Le snapshot réunit des compteurs déjà possédés par leurs systèmes.
- **Frontières d’autorité :** Le service d’observabilité lit des ports de santé ; il ne modifie aucun registre.
- **Limites et réserves :** Les valeurs détaillées des personnages, requêtes ou événements ne sont pas copiées.

## 37. Marqueur de session

Un marqueur persistant permet de détecter un arrêt non propre au démarrage suivant. Il ne prouve pas la cause du crash.

> **[VSC] Fichier `session_marker.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name SessionMarker
extends RefCounted

const PATH := "user://diagnostics/pending/session.json"

func open(run_id: String, build_id: String) -> Error:
    var root := ProjectSettings.globalize_path(
        "user://diagnostics/pending"
    )
    var make_error := DirAccess.make_dir_recursive_absolute(root)
    if make_error != OK:
        return make_error

    var file := FileAccess.open(PATH, FileAccess.WRITE)
    if file == null:
        return FileAccess.get_open_error()
    file.store_string(JSON.stringify({
        "run_id": run_id,
        "build_id": build_id,
        "started_at_utc": TelemetryClock.utc_now(),
    }))
    file.flush()
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** Le marqueur est créé et vidé sur disque avant le chargement de la partie.
- **Codes de retour :** Les erreurs de dossier et de fichier sont distinguées.
- **Invariants protégés :** Un seul marqueur représente la session active.
- **Limites et réserves :** Une coupure électrique, un arrêt forcé ou un crash produisent le même signal : marqueur resté présent.

## 38. Fermer proprement la session

> **[VSC] Suite de `session_marker.gd` — Ne pas saisir dans Godot.**

```gdscript
func close_cleanly() -> Error:
    if not FileAccess.file_exists(PATH):
        return OK
    return DirAccess.remove_absolute(
        ProjectSettings.globalize_path(PATH)
    )

func has_unclean_previous_session() -> bool:
    return FileAccess.file_exists(PATH)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Codes de retour :** L’absence du marqueur est un succès idempotent.
- **Effets de bord :** Seule une fermeture contrôlée supprime le fichier.
- **Résultat attendu :** Au démarrage, la présence du fichier déclenche une proposition de paquet de diagnostic.
- **Limites et réserves :** Le diagnostic doit encore consulter le journal natif et les derniers enregistrements pour comprendre l’arrêt.

## 39. Manifeste de reproduction

> **[LECTURE] Manifeste minimal — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "package_id": "diag.20260722.001",
  "created_at_utc": "2026-07-22T00:45:10Z",
  "build": {
    "project_version": "0.28.0-dev",
    "git_commit": "abcdef0123456789",
    "godot_version": "4.7.1-stable",
    "renderer": "Forward+"
  },
  "scenario": {
    "scenario_id": "sim.ecology.small_valley",
    "seed": 42,
    "initial_snapshot_digest": "sha256:...",
    "last_logical_tick": 720
  },
  "files": [
    {
      "path": "logs/session.jsonl",
      "size_bytes": 18421,
      "sha256": "..."
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Le manifeste distingue identité du paquet, build, scénario et inventaire des fichiers.
- **Invariants protégés :** Les fichiers sont référencés par chemin relatif, taille et empreinte.
- **Sécurité et confidentialité :** Aucun chemin absolu, nom de compte système ou contenu de sauvegarde n’apparaît.
- **Limites et réserves :** Une graine n’est incluse que lorsqu’elle appartient réellement au scénario.

## 40. Informations d’environnement minimales

> **[VSC] Projection d’environnement — Ne pas saisir dans Godot.**

```gdscript
func safe_environment() -> Dictionary:
    var engine := Engine.get_version_info()
    return {
        "platform": OS.get_name(),
        "godot_version": engine.get("string", "unknown"),
        "project_version": ProjectSettings.get_setting(
            "application/config/version",
            "unknown"
        ),
        "display_server": DisplayServer.get_name(),
        "renderer": RenderingServer.get_video_adapter_name(),
        "locale_language": OS.get_locale_language(),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** La projection contient uniquement les caractéristiques utiles à la compatibilité.
- **Sécurité et confidentialité :** Elle exclut nom de machine, nom de compte, adresse IP, identifiant matériel et chemins personnels.
- **Limites et réserves :** Le nom de l’adaptateur vidéo peut être considéré comme une information technique sensible ; l’interface d’export doit permettre de le retirer.

## 41. Inventorier et hacher les fichiers

> **[VSC] Fichier `diagnostic_file_entry.gd` — Ne pas saisir dans Godot.**

```gdscript
static func from_path(
    package_root: String,
    relative_path: String
) -> Dictionary:
    var full_path := package_root.path_join(relative_path)
    var size := FileAccess.get_size(full_path)
    var digest := FileAccess.get_sha256(full_path)
    if size < 0 or digest.is_empty():
        return {}
    return {
        "path": relative_path,
        "size_bytes": size,
        "sha256": digest,
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur de retour ou code d’échec :** Un dictionnaire vide signale un fichier illisible.
- **Sécurité et confidentialité :** Le manifeste conserve seulement le chemin relatif.
- **Invariants protégés :** Taille et SHA-256 permettent de détecter une modification ou une archive incomplète.
- **Limites et réserves :** Une empreinte prouve l’intégrité du contenu reçu, pas l’identité de son auteur.

## 42. Créer une archive ZIP

> **[VSC] Fichier `zip_diagnostic_writer.gd` — Ne pas saisir dans Godot.**

```gdscript
class_name ZipDiagnosticWriter
extends RefCounted

func write(
    output_path: String,
    files: Dictionary
) -> Error:
    var writer := ZIPPacker.new()
    var open_error := writer.open(output_path)
    if open_error != OK:
        return open_error

    for relative_path in files.keys():
        var start_error := writer.start_file(relative_path)
        if start_error != OK:
            writer.close()
            return start_error
        var bytes := FileAccess.get_file_as_bytes(
            files[relative_path]
        )
        var write_error := writer.write_file(bytes)
        if write_error != OK:
            writer.close()
            return write_error
        writer.close_file()

    return writer.close()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** L’archive est ouverte, chaque fichier est démarré, écrit puis fermé.
- **Codes de retour :** La première erreur stoppe la création et ferme le writer.
- **Sécurité et confidentialité :** Les noms internes proviennent d’une liste contrôlée, pas d’un chemin fourni librement.
- **Limites et réserves :** Le ZIP n’apporte ni chiffrement ni signature ; ces besoins exigent une couche distincte.

## 43. Contenu autorisé d’un paquet

> **[LECTURE] Liste fermée — Ne pas saisir.**

```text
manifest.json
logs/session.jsonl
logs/godot.log
tests/junit-summary.json
tests/first-failing-seed.json
traces/recent-spans.json
metrics/final-snapshot.json
config/effective-observability.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** Chaque entrée possède une responsabilité claire.
- **Sécurité et confidentialité :** Une sauvegarde complète, un prompt, une réponse IA brute, un jeton ou un fichier arbitraire sont exclus.
- **Invariants protégés :** Le service ne parcourt jamais récursivement tout `user://`.
- **Limites et réserves :** Un nouvel artefact exige une modification relue de la liste autorisée.

## 44. Consentement et aperçu

Le paquet reste local jusqu’à une action explicite. L’utilisateur voit la liste des fichiers, leur taille, les catégories de données et les champs retirés.

> **[LECTURE] Flux d’export — Ne pas saisir.**

```text
incident détecté
    ↓
préparer un paquet local
    ↓
afficher le manifeste et les catégories
    ↓
permettre de retirer les éléments optionnels
    ↓
obtenir le consentement explicite
    ↓
exporter vers un chemin choisi
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** La préparation précède le consentement, mais aucun envoi réseau n’est effectué.
- **Sécurité et confidentialité :** Les éléments optionnels, comme l’adaptateur vidéo, peuvent être exclus.
- **Invariants protégés :** Le support hors ligne reste possible par copie manuelle de l’archive.
- **Limites et réserves :** La politique juridique et l’écran final dépendent du produit publié.

## 45. Valider un paquet avant export

> **[VSC] Validation du manifeste — Ne pas saisir dans Godot.**

```gdscript
func validate_package(
    root: String,
    manifest: Dictionary
) -> PackedStringArray:
    var errors := PackedStringArray()
    for entry in manifest.get("files", []):
        var relative_path := String(entry.get("path", ""))
        if relative_path.is_empty() or relative_path.is_absolute_path():
            errors.append("invalid_relative_path")
            continue
        var full_path := root.path_join(relative_path)
        if not FileAccess.file_exists(full_path):
            errors.append("missing_file:%s" % relative_path)
            continue
        if FileAccess.get_sha256(full_path) != entry.get(
            "sha256",
            ""
        ):
            errors.append("digest_mismatch:%s" % relative_path)
    return errors
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le chemin est validé avant l’accès, puis l’existence et l’empreinte sont contrôlées.
- **Valeur de retour ou code d’échec :** Toutes les anomalies sont retournées dans un tableau.
- **Sécurité et confidentialité :** Un chemin absolu est refusé.
- **Invariants protégés :** L’archive n’est créée que depuis les fichiers annoncés par le manifeste.

## 46. Relier les résultats du chapitre 27

Une campagne échouée peut créer un paquet qui contient le résumé JUnit, la première graine défaillante, le scénario et les derniers journaux corrélés. Le paquet n’exécute pas les tests et ne met pas à jour un golden file.

> **[VSC] Construction d’une demande de paquet — Ne pas saisir.**

```gdscript
var request := DiagnosticPackageRequest.new()
request.reason_id = &"tests.simulation.failed"
request.correlation_id = result.correlation_id
request.allowed_files = PackedStringArray([
    result.junit_summary_path,
    result.first_failing_seed_path,
    result.canonical_diff_path,
    telemetry.current_session_path(),
])
var package_result := diagnostic_service.prepare(request)
assert_eq(
    package_result.status,
    DiagnosticPackageResult.Status.PREPARED
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** La demande indique la raison, la corrélation et une liste fermée de fichiers.
- **Frontières d’autorité :** Le service prépare l’archive ; il ne modifie aucun résultat de test.
- **Valeur de retour ou code d’échec :** Le statut `PREPARED` précède tout export.
- **Limites et réserves :** Les chemins fournis doivent appartenir aux racines de test et de diagnostic autorisées.

## 47. Tester la rédaction des secrets

> **[VSC] Test unitaire de politique — Ne pas saisir.**

```gdscript
func test_sensitive_fields_are_redacted() -> void:
    var policy := TelemetryPolicyFixture.create()
    var filtered := policy.filter_attributes(
        &"ai.request.failed",
        {
            "request_id": "req.1",
            "access_token": "secret-value",
            "prompt": "private text",
        }
    )

    assert_eq(filtered["request_id"], "req.1")
    assert_eq(filtered.get("access_token"), null)
    assert_eq(filtered.get("prompt"), null)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Le catalogue du fixture autorise uniquement `request_id`.
- **Invariants protégés :** Le jeton et le prompt ne sont pas seulement masqués ; ils sont absents du résultat.
- **Limites et réserves :** Un second test doit couvrir une clé sensible explicitement autorisée et vérifier la sentinelle `[REDACTED]`.

## 48. Tester la corrélation

> **[VSC] Test de chaîne causale — Ne pas saisir.**

```gdscript
func test_trade_events_share_correlation() -> void:
    var context := TelemetryContextFixture.create()
    var events := TradeTelemetryFixture.run(context)

    assert_eq(events.size(), 3)
    for event_value in events:
        assert_eq(
            event_value.context.correlation_id,
            context.correlation_id
        )
    assert_eq(
        events[2].context.causation_id,
        &"receipt.trade.104"
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le test vérifie le lot commun puis la cause spécifique du dernier événement.
- **Invariants protégés :** Une opération ne perd pas son identifiant lorsqu’elle traverse plusieurs systèmes.
- **Limites et réserves :** Le test ne suppose pas que les événements occupent des lignes adjacentes dans le fichier final.

## 49. Tester l’intégrité d’un paquet

> **[VSC] Test d’intégration sur une racine temporaire — Ne pas saisir.**

```gdscript
func test_package_manifest_detects_modified_file() -> void:
    var workspace := DiagnosticWorkspace.new()
    workspace.write_log("session.jsonl", "{\"ok\":true}\n")
    var manifest := workspace.build_manifest()

    workspace.write_log("session.jsonl", "{\"ok\":false}\n")

    var errors := DiagnosticPackageValidator.new().validate_package(
        workspace.root,
        manifest
    )
    assert_has(
        errors,
        "digest_mismatch:logs/session.jsonl"
    )
    workspace.cleanup()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le manifeste est calculé, le fichier est modifié, puis la validation compare l’empreinte.
- **Invariants protégés :** Une modification après préparation est détectée avant export.
- **Effets de bord :** Le workspace écrit uniquement sous une racine temporaire et la supprime.
- **Limites et réserves :** La signature d’un paquet par une clé de studio n’est pas couverte par ce test.

## 50. Tester la détection d’un arrêt non propre

> **[VSC] Test du marqueur de session — Ne pas saisir.**

```gdscript
func test_existing_marker_reports_unclean_session() -> void:
    var marker := SessionMarkerFixture.create()
    assert_eq(marker.open("run.1", "build.28"), OK)

    var restarted := SessionMarker.new()
    assert_true(restarted.has_unclean_previous_session())

    assert_eq(restarted.close_cleanly(), OK)
    assert_false(restarted.has_unclean_previous_session())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déroulement ou instructions importantes :** Le fixture simule un redémarrage en créant une nouvelle instance sur le même chemin.
- **Invariants protégés :** La détection est persistante et la fermeture est idempotente.
- **Limites et réserves :** Le test ne provoque pas un crash réel ; il vérifie seulement le protocole de marqueur.

## 51. Mode Solo

Le parcours Solo conserve :

- le journal natif Godot avec rotation ;
- un sink JSONL local ;
- un catalogue d’événements unique ;
- une politique de rédaction fermée ;
- un registre de métriques en mémoire ;
- un buffer de traces borné ;
- un marqueur de session ;
- un bouton d’export manuel d’un paquet ZIP.

Aucun serveur, collecteur ou compte distant n’est requis. Les événements `DEBUG` sont désactivés en release sauf activation temporaire par une configuration locale.

## 52. Mode Studio

Le parcours Studio ajoute :

- des propriétaires de catalogues par domaine ;
- une revue de confidentialité et de rétention ;
- des dashboards et alertes hors du runtime ;
- un collecteur facultatif derrière un port ;
- une propagation W3C aux frontières compatibles ;
- des budgets de volume et cardinalité par build ;
- une signature ou une chaîne de provenance pour les paquets internes ;
- une procédure de symbolisation des crashs pour les builds disposant des symboles correspondants ;
- des accès journalisés aux archives de support.

Le Studio ne contourne pas le consentement ni la minimisation. Une plateforme distante reçoit uniquement les champs approuvés.

## 53. Contrat commun Solo et Studio

Les deux parcours exigent :

- des noms d’événements stables ;
- des identifiants opaques ;
- des durées monotones ;
- une corrélation propagée ;
- une causalité explicite ;
- des attributs sur liste autorisée ;
- des volumes bornés ;
- des paquets validés avant export ;
- aucune dépendance réseau pour diagnostiquer localement ;
- aucune autorité métier accordée à la télémétrie.

## 54. Frontières avec les chapitres précédents

- architecture : le port d’observabilité respecte l’injection de dépendances ;
- sauvegarde : le journal ne copie pas le snapshot ;
- IA locale : prompts, réponses et jetons sont exclus par défaut ;
- sécurité : secrets, accès et rétention suivent les règles du chapitre 13 ;
- gameplay : chaque système conserve ses identités et raisons ;
- outils de contenu : les reçus et empreintes peuvent entrer dans un paquet ;
- tests : les résultats et graines sont consommés sans être régénérés.

## 55. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants montrent des pratiques qui rendent les journaux inutilisables, dangereux ou impossibles à reproduire.

### 55.1 Journaliser uniquement une phrase libre

**Symptôme :** Une recherche doit deviner toutes les variantes de formulation.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
print("La sauvegarde a encore échoué pour le slot 1")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La phrase mélange type d’événement, résultat et identifiant ; elle ne possède aucun nom stable ni raison exploitable.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
telemetry.emit(
    TelemetryEvents.save_failed(
        &"slot.1",
        &"save.reason.disk_full",
        context
    )
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le constructeur applique un nom d’événement, une raison, une sévérité et un contexte versionnés.

### 55.2 Inclure un secret dans les attributs

**Symptôme :** Un paquet de support contient un jeton réutilisable.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
telemetry.info(&"ai.request.started", {
    "authorization": "Bearer " + access_token,
})
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le journal devient un second stockage de secret et peut transmettre le jeton dans une archive ou un collecteur.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
telemetry.info(&"ai.request.started", {
    "request_id": request.request_id,
    "provider_id": adapter.provider_id,
})
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les identifiants opaques permettent la corrélation sans exposer l’authentification.

### 55.3 Utiliser l’horloge système pour une durée

**Symptôme :** Une durée devient négative après une correction de l’heure.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var started := Time.get_unix_time_from_system()
run_operation()
var elapsed := Time.get_unix_time_from_system() - started
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’horloge système peut avancer ou reculer indépendamment de l’opération.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var started_us := Time.get_ticks_usec()
run_operation()
var elapsed_us := Time.get_ticks_usec() - started_us
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le compteur monotone ne recule pas et mesure uniquement le temps écoulé dans le processus.

### 55.4 Utiliser l’identifiant d’une entité comme label de métrique

**Symptôme :** Le nombre de séries augmente avec chaque personnage.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
metrics.increment(
    &"character_action_total",
    {"character_id": character.character_id}
)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Chaque identifiant crée une nouvelle combinaison de labels et une cardinalité sans borne.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
metrics.increment(
    &"character_action_total",
    {"action_type": String(command.action_type)}
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** `action_type` appartient à un ensemble fermé et garde le nombre de séries prévisible.

### 55.5 Écrire depuis le callback multithread du Logger

**Symptôme :** Des lignes sont entrelacées ou le processus se bloque.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
func _log_message(message: String, error: bool) -> void:
    file.store_line(message)
    print("captured: ", message)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le fichier n’est pas synchronisé et `print()` peut rappeler le logger, créant une récursion.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func _log_message(message: String, error: bool) -> void:
    _mutex.lock()
    _pending.append({"message": message, "error": error})
    _mutex.unlock()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le callback ne fait qu’enfiler sous mutex ; le thread principal effectue ensuite la sérialisation et l’écriture.

### 55.6 Exporter tout `user://`

**Symptôme :** Le paquet contient sauvegardes, préférences et fichiers sans rapport.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
for path in scan_recursive("user://"):
    package.add_file(path)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le parcours récursif collecte des données non prévues et rend impossible un consentement informé.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
for path in request.allowed_files:
    package.add_checked_file(path)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La demande contient une liste fermée et chaque chemin est validé contre une racine autorisée.

### 55.7 Considérer un marqueur comme preuve de crash

**Symptôme :** Un arrêt forcé est présenté comme une panne certaine.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
if FileAccess.file_exists(marker_path):
    report.reason_id = &"application.crashed"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le marqueur peut rester après une coupure, un kill du processus ou un défaut de nettoyage.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
if FileAccess.file_exists(marker_path):
    report.reason_id = &"application.previous_exit_unclean"
    report.confidence = &"unknown"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le diagnostic décrit seulement le fait observé et conserve l’incertitude sur la cause.

### 55.8 Capturer toutes les variables d’une pile

**Symptôme :** Un diagnostic retient des objets et expose des données privées.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var traces := Engine.capture_script_backtraces(true)
package.add_variant("backtraces", traces)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les variables peuvent contenir secrets, états complets et références qui empêchent la libération des objets.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var traces := Engine.capture_script_backtraces(false)
package.add_json(
    "backtraces.json",
    SafeBacktraceProjection.build(traces)
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La capture exclut les variables et la projection ne conserve que langage, fichier, fonction et ligne.

### 55.9 Échantillonner les erreurs graves

**Symptôme :** Certains crashs ou échecs critiques n’apparaissent jamais.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
if randi() % 100 < 10:
    telemetry.emit(fatal_event)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La décision aléatoire supprime neuf événements graves sur dix et n’est pas reproductible.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
if fatal_event.severity >= TelemetrySeverity.Value.ERROR:
    telemetry.emit(fatal_event)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les niveaux graves passent toujours ; l’échantillonnage reste réservé aux signaux détaillés et réussis.

### 55.10 Confondre journal et état autoritaire

**Symptôme :** Le chargement reconstruit une partie depuis les lignes de journal.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
for line in telemetry_log:
    world.apply_event(JSON.parse_string(line))
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le journal peut être échantillonné, incomplet, rédigé ou supprimé selon la rétention ; il n’est pas un event store.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var restore_result := save_service.load(slot_id)
telemetry.emit(
    TelemetryEvents.restore_completed(
        restore_result,
        context
    )
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La sauvegarde restaure l’état autoritaire ; le journal observe le résultat sans participer au chargement.

## 56. Checklist d’acceptation

Avant d’accepter la chaîne de diagnostic :

- chaque événement possède un nom stable et un propriétaire ;
- la sévérité décrit l’effet opérationnel ;
- les timestamps UTC et monotones sont distingués ;
- le tick logique n’est pas remplacé par l’horloge système ;
- corrélation et causalité sont propagées ;
- les attributs sont sur liste autorisée ;
- secrets, prompts, réponses brutes et données personnelles inutiles sont absents ;
- les chaînes et tailles sont bornées ;
- journaux, métriques et traces ont des budgets ;
- le logger moteur est thread-safe et non récursif ;
- les marqueurs décrivent un arrêt non propre sans inventer sa cause ;
- le paquet contient une liste fermée de fichiers ;
- chaque fichier possède taille et SHA-256 ;
- le consentement précède tout export ;
- le support hors ligne fonctionne ;
- les résultats du chapitre 27 restent immuables ;
- aucun PDF ni test runtime non réalisé n’est revendiqué.

## 57. Critères de passage

Le chapitre peut passer lorsque :

- le schéma JSONL et le catalogue sont cohérents ;
- les exemples de code ne journalisent aucun secret ;
- les durées utilisent un compteur monotone ;
- la file du logger et les buffers sont bornés ;
- les paquets refusent les chemins absolus ;
- les empreintes sont vérifiées avant export ;
- les dix erreurs possèdent un contre-exemple, une correction et leurs explications directes ;
- les modes Solo et Studio respectent la même politique de minimisation ;
- les réserves sur crashs, symboles et collecte distante sont explicites.

## 58. Références techniques officielles

- [Godot 4.7 — journalisation](https://docs.godotengine.org/en/4.7/tutorials/scripting/logging.html) ;
- [Godot 4.7 — `ProjectSettings`](https://docs.godotengine.org/en/4.7/classes/class_projectsettings.html) ;
- [Godot 4.7 — `Logger`](https://docs.godotengine.org/en/4.7/classes/class_logger.html) ;
- [Godot 4.7 — panneau Output](https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/output_panel.html) ;
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html) ;
- [Godot 4.7 — `FileAccess`](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html) ;
- [Godot 4.7 — `Crypto`](https://docs.godotengine.org/en/4.7/classes/class_crypto.html) ;
- [Godot 4.7 — `Engine`](https://docs.godotengine.org/en/4.7/classes/class_engine.html) ;
- [Godot 4.7 — `ScriptBacktrace`](https://docs.godotengine.org/en/4.7/classes/class_scriptbacktrace.html) ;
- [Godot 4.7 — `HashingContext`](https://docs.godotengine.org/en/4.7/classes/class_hashingcontext.html) ;
- [Godot 4.7 — `ZIPPacker`](https://docs.godotengine.org/en/4.7/classes/class_zippacker.html) ;
- [OpenTelemetry — modèle de données des journaux](https://opentelemetry.io/docs/specs/otel/logs/data-model/) ;
- [W3C — Trace Context](https://www.w3.org/TR/trace-context/) ;
- [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

La revue documentaire confirme les API et contrats cités pour Godot 4.7. Elle ne constitue ni une matérialisation du Starter Kit, ni une exécution de Godot, ni une collecte de crash native avec symboles.

## 59. Décisions retenues pour Project Asteria

`Project Asteria` adopte deux voies complémentaires : le journal natif de Godot pour les sorties du moteur et un journal JSONL applicatif pour les événements structurés. Le port d’observabilité reste une dépendance périphérique ; son échec ne transforme pas une opération métier acceptée en refus.

Chaque enregistrement possède un nom stable, une sévérité numérique et textuelle, un instant UTC, un compteur monotone, un `run_id`, une corrélation, une cause, un système propriétaire et un résultat. Le tick logique reste l’autorité de la simulation. Les durées n’utilisent jamais l’horloge système.

Les attributs sont admis par catalogue, nettoyés et bornés. Les secrets, jetons, mots de passe, chaînes de connexion, clés, prompts, réponses IA brutes, chemins personnels et données complètes de sauvegarde sont exclus. Les métriques utilisent des dimensions de faible cardinalité ; les traces et files sont bornées ; les événements graves ne sont pas échantillonnés.

Après un arrêt non propre ou une campagne échouée, le projet peut préparer localement un paquet contenant manifeste, journaux, résultats, traces, métriques et empreintes. Le paquet est validé avant export, reste utilisable hors ligne et n’est transmis qu’après consentement explicite. Les crashs natifs, symboles de débogage, collecteurs distants et signatures de studio demeurent des capacités optionnelles à matérialiser et tester ultérieurement.
