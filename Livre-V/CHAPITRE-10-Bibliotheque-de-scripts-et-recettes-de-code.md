---
title: "Livre V — Fiche 10 : Bibliothèque de scripts et recettes de code"
id: "DOC-L5-CH10"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 10
last-verified: "2026-07-28T21:24:52+02:00"
audit-status: "complete"
audit-date: "2026-07-28T21:24:52+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-10.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "cross-language-code-recipe-library"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Bibliothèque de scripts et recettes de code

> **Type de document :** cartes de recettes, squelettes statiques, matrices de preuve et portes d’acceptation.
> **Lecture :** choisir l’effet recherché, vérifier le langage et l’environnement, puis lire entrées, sorties, erreurs, tests et statut d’exécution.
> **Principe :** un extrait relu n’est ni un composant testé, ni une commande sûre dans tous les contextes, ni un artefact prêt pour la production.
>
> **Repères d’utilisation :** **[VSC]** fichier à créer ou adapter dans Visual Studio Code, **[PS]** commande PowerShell 7 sur Windows, **[WSL]** commande Bash dans WSL, **[LECTURE]** structure à lire sans l’exécuter. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer une recette | [CODE-00](#code-00--contrat-dune-recette) |
| choisir un langage | [Matrice A](#matrice-a--sélection-par-effet) |
| lire le statut de preuve | [CODE-01](#code-01--statut-et-niveau-de-preuve) |
| définir paramètres et erreurs | [CODE-02](#code-02--interface-et-codes-de-sortie) |
| valider une valeur en GDScript | [CODE-03](#code-03--gdscript-règle-pure) |
| exécuter un contrôle Godot headless | [CODE-04](#code-04--gdscript-en-ligne-de-commande) |
| écrire une CLI Python bornée | [CODE-05](#code-05--python-cli-et-staging) |
| charger un JSON avec limites | [CODE-06](#code-06--python-json-borné) |
| propager un code natif en PowerShell | [CODE-07](#code-07--powershell-et-programme-natif) |
| écrire un contrôle Bash minimal | [CODE-08](#code-08--bash-strict-et-portable) |
| borner chemins et processus | [CODE-09](#code-09--frontières-deffets) |
| définir tests et fixtures | [CODE-10](#code-10--tests-et-fixtures) |
| qualifier sécurité et licence | [CODE-11](#code-11--sécurité-dépendances-et-licences) |
| suivre le cycle d’une recette | [Matrice B](#matrice-b--cycle-de-preuve) |
| préparer une campagne | [Matrice C](#matrice-c--qualification-minimale) |
| publier un paquet | [CODE-12](#code-12--paquet-et-acceptation) |

---

<!-- l5:card -->
## CODE-00 — Contrat d’une recette

| Champ | Règle |
|---|---|
| identité | identifiant stable, version, propriétaire, langage, dépôt et chemin canonique |
| effet | transformation unique et observable, formulée sans promesse vague |
| statut | `pedagogical`, `static-skeleton`, `syntax-checked`, `tested` ou `qualified` |
| environnement | OS, shell ou moteur, version, architecture, encodage et dossier courant |
| entrées | paramètres, fichiers, variables d’environnement, formats, droits et limites |
| sorties | stdout, stderr, fichiers, objets, événements, rapport et code de sortie |
| effets de bord | créations, remplacements, suppressions, réseau, processus et état runtime |
| erreurs | conditions, codes stables, messages diagnostiques et politique de reprise |
| déterminisme | ordre, locale, horloge, graine, tri, concurrence et dépendances |
| sécurité | frontières de chemins, secrets, données non fiables, privilèges et commandes natives |
| tests | cas nominal, refus, limites, répétition, nettoyage et repli |
| licence | auteur, source, licence du snippet, dépendances et obligations de redistribution |
| preuve | commit, environnement, commande, rapports, artefacts, revue et réserves |
| retrait | appelants, remplaçant, migration, date et conservation des preuves |

**Réponse rapide :** une recette est une petite interface exécutable ou adaptable. Elle reprend la définition d’une [automatisation répétable](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#31-automatisation), mais reste distincte du [workflow qui l’orchestre](CHAPITRE-08-Bibliotheque-de-workflows.md#workflow-00--contrat-dun-workflow) et du [prompt qui décrit une demande IA](CHAPITRE-09-Bibliotheque-de-prompts.md#prompt-00--contrat-dun-prompt).

---

<!-- l5:matrix -->
## Matrice A — Sélection par effet

| Effet recherché | Langage de départ | Carte | Source propriétaire | Repli |
|---|---|---|---|---|
| règle proche du domaine Godot | GDScript typé | CODE-03 | [nature de GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#2-nature-de-gdscript) | fonction pure dans le système propriétaire |
| outil court utilisant l’API Godot | GDScript `SceneTree` | CODE-04 | [script Godot en ligne de commande](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html#running-a-script) | outil d’éditeur ou contrôle manuel |
| transformation de fichiers, schémas ou lots | Python | CODE-05 et 06 | [architecture cible de l’automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#4-architecture-cible) | opération manuelle bornée |
| orchestration Windows et programmes natifs | PowerShell | CODE-07 | [code de sortie PowerShell](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#93-code-de-sortie) | appel direct documenté |
| contrôle Linux, WSL ou conteneur | Bash | CODE-08 | [séparer Windows et WSL](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#12-séparer-windows-et-wsl) | Python portable |
| test d’un invariant | framework du langage | CODE-10 | [définitions des tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md#4-définitions-opérationnelles) | vérification manuelle enregistrée |
| coordination de plusieurs recettes | workflow, pas nouveau script monolithique | fiche 08 | [cycle d’un workflow](CHAPITRE-08-Bibliotheque-de-workflows.md#matrice-b--cycle-dun-workflow) | étapes indépendantes |

**Décision :** choisir le langage qui possède déjà l’autorité et les bibliothèques nécessaires. Une ressemblance syntaxique ne justifie pas de traduire mécaniquement GDScript en Python, ni PowerShell en Bash.

---

<!-- l5:card -->
## CODE-01 — Statut et niveau de preuve

| Statut | Ce qui existe | Allégation autorisée | Allégation interdite |
|---|---|---|---|
| `pedagogical` | extrait destiné à expliquer une idée | structure lisible | exécution ou intégration |
| `static-skeleton` | code complet relu sans run | interface et intention | syntaxe confirmée |
| `syntax-checked` | parseur, compilateur ou shell a accepté le fichier | syntaxe dans l’environnement enregistré | comportement correct |
| `unit-tested` | règles isolées exercées avec fixtures | cas couverts par la suite | intégration réelle |
| `integration-tested` | fichiers, moteur ou processus réels mobilisés | scénario et environnement testés | portabilité générale |
| `qualified` | campagne minimale, sécurité et repli passés | périmètre exact de qualification | production universelle |
| `production` | composant promu, observé et maintenu | usage approuvé dans son périmètre | absence future de défaut |
| `withdrawn` | usage bloqué et remplaçant documenté | historique consultable | nouvel appel |

Une recette de cette fiche reste `static-skeleton`. Les états supérieurs exigent la conservation des commandes, versions, codes de sortie, journaux et artefacts, conformément aux [définitions de reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md#33-reproductibilité).

---

<!-- l5:card -->
## CODE-02 — Interface et codes de sortie

| Élément | Contrat minimal |
|---|---|
| aide | décrit syntaxe, paramètres obligatoires, valeurs autorisées et exemples non destructifs |
| entrée standard | utilisée seulement si le format, l’encodage et la taille sont bornés |
| sortie standard | résultat machine ou information nominale ; aucun secret |
| erreur standard | diagnostic actionnable, identifiant stable et contexte minimal |
| code `0` | opération terminée selon le contrat |
| code `2` | arguments ou usage invalides |
| code `3` | entrée absente ou invalide |
| code `4` | dépendance, environnement ou permission indisponible |
| code `5` | échec de traitement sans sortie promouvable |
| codes natifs | conservés lorsqu’ils ont une signification utile et documentée |
| exceptions | traduites à la frontière CLI ; jamais avalées silencieusement |
| sortie partielle | reste en staging et porte un statut d’échec explicite |

Python considère `0` comme succès et un code non nul comme terminaison anormale ; les conventions détaillées restent dépendantes de l’outil. PowerShell expose le code d’un programme natif dans `$LASTEXITCODE`, tandis que Bash ne propage l’échec d’un pipeline complet que si `pipefail` est activé. Les références officielles sont [Python `sys.exit`](https://docs.python.org/3.14/library/sys.html#sys.exit), [variables automatiques PowerShell](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_automatic_variables?view=powershell-7.6) et [pipelines Bash](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).

---

<!-- l5:card -->
## CODE-03 — GDScript : règle pure

| Champ | Valeur |
|---|---|
| besoin | valider une chaîne obligatoire sans dépendre d’un nœud, d’une scène ou d’un fichier |
| entrées | `value: String`, `field_name: StringName` |
| sortie | dictionnaire fermé contenant `ok`, puis `value` ou `code` et `field` |
| erreurs | valeur vide après `strip_edges()` |
| effets | aucun |
| statut | `static-skeleton`, non parsé et non exécuté dans cette fiche |

> **[VSC] GDScript — Exemple statique à adapter dans un fichier `.gd` ; ne pas présenter comme testé.**

```gdscript
class_name RequiredText
extends RefCounted

static func validate(value: String, field_name: StringName) -> Dictionary:
	var cleaned := value.strip_edges()
	if cleaned.is_empty():
		return {
			"ok": false,
			"code": &"missing_value",
			"field": field_name,
		}
	return {"ok": true, "value": cleaned}
```

**Adaptation :** remplacer le dictionnaire par un type de résultat propriétaire lorsque le système en possède un. La recette ne lève pas d’exception, car GDScript ne fournit pas le mécanisme général de Python ; voir la [distinction GDScript/Python](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#2-nature-de-gdscript) et la règle selon laquelle [un fichier GDScript est une classe](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#3-un-fichier-gdscript-est-une-classe).

**Test minimal à matérialiser :** chaîne normale, espaces seuls, caractères accentués et nom de champ vide volontairement refusé par le contrat appelant.

---

<!-- l5:card -->
## CODE-04 — GDScript en ligne de commande

| Champ | Valeur |
|---|---|
| besoin | vérifier l’existence d’une entrée Godot sans ouvrir une scène |
| précondition | script hérité de `SceneTree`, projet et binaire exacts enregistrés |
| sortie | `input_found` sur stdout ou identifiant d’erreur sur stderr |
| codes | `0` trouvé, `2` usage invalide, `3` entrée absente |
| effets | lecture du chemin uniquement |
| statut | `static-skeleton`, aucun binaire Godot appelé |

> **[VSC] GDScript — Squelette statique `tools/check_input.gd` ; adapter les chemins et tests avant exécution.**

```gdscript
extends SceneTree

const EXIT_USAGE := 2
const EXIT_INVALID_INPUT := 3

func _init() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() != 1:
		printerr("usage: check_input.gd -- <resource-path>")
		quit(EXIT_USAGE)
		return

	var input_path := args[0]
	if not FileAccess.file_exists(input_path):
		printerr("input_not_found")
		quit(EXIT_INVALID_INPUT)
		return

	print("input_found")
	quit(0)
```

> **[PS] PowerShell 7 — Exemple d’appel à lire ; aucun projet n’a été lancé pour cette fiche.**

```powershell
godot --headless --path . -s tools/check_input.gd -- res://data/example.json
if ($LASTEXITCODE -ne 0) {
    throw "Contrôle Godot échoué : $LASTEXITCODE"
}
```

La documentation officielle confirme qu’un script lancé avec `-s` doit hériter de `SceneTree` ou `MainLoop`. La syntaxe exacte de GDScript reste au chapitre 11 ; les campagnes automatisées et leurs workspaces restent au [chapitre d’automatisation Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#3-définitions-opérationnelles).

---

<!-- l5:card -->
## CODE-05 — Python : CLI et staging

| Champ | Valeur |
|---|---|
| besoin | copier un texte autorisé vers un chemin de staging explicite |
| entrées | source existante et `--output` obligatoire |
| sorties | fichier UTF-8, aide CLI et code de sortie |
| refus | source absente, sortie identique à la source ou parent non autorisé par l’appelant |
| effets | création des parents et écriture du fichier de staging |
| statut | `static-skeleton`, non exécuté |

> **[VSC] Python — Squelette statique `tools/copy_text.py` ; borner la racine de sortie avant usage réel.**

```python
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not args.source.is_file():
        parser.error(f"source absente : {args.source}")
    if args.source.resolve() == args.output.resolve():
        parser.error("la sortie doit être distincte de la source")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    text = args.source.read_text(encoding="utf-8")
    args.output.write_text(text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

> **[PS] PowerShell 7 — Exemple d’appel à lire ; la commande n’a pas été exécutée dans cette fiche.**

```powershell
py -3.14 .\tools\copy_text.py .\inputs\note.txt `
    --output .\work\staging\note.txt
```

`argparse` est le module recommandé de la bibliothèque standard pour les CLI ; `parser.error()` produit une aide et termine avec un code d’usage. L’environnement, le verrou et la cible CPython restent au [chapitre 29](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#6-créer-un-environnement-virtuel-sous-windows). Voir aussi le [tutoriel officiel `argparse`](https://docs.python.org/3.14/howto/argparse.html).

---

<!-- l5:card -->
## CODE-06 — Python : JSON borné

| Champ | Valeur |
|---|---|
| besoin | charger un objet JSON UTF-8 sans accepter un fichier arbitrairement grand |
| entrées | `Path` et limite d’octets positive |
| sortie | `dict[str, object]` |
| erreurs | fichier absent, taille excessive, JSON invalide ou racine non objet |
| effets | lecture seule |
| statut | `static-skeleton`, non testé |

> **[VSC] Python — Fonction statique à adapter avec le schéma du chapitre 13.**

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json_object(path: Path, max_bytes: int = 1_048_576) -> dict[str, Any]:
    if max_bytes <= 0:
        raise ValueError("max_bytes doit être positif")
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.stat().st_size > max_bytes:
        raise ValueError("input_too_large")

    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError("root_must_be_object")
    return value
```

**Limite :** cette fonction ne valide ni schéma, ni licence, ni contenu métier. La validation structurelle appartient au futur chapitre 13 ; les sorties hors workspace et la publication appartiennent à la [chaîne d’automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#4-architecture-cible).

---

<!-- l5:card -->
## CODE-07 — PowerShell et programme natif

| Champ | Valeur |
|---|---|
| besoin | lancer un exécutable autorisé et propager son code sans le transformer en succès |
| entrées | chemin ou nom approuvé, tableau d’arguments non secret |
| sortie | flux natifs et code du programme |
| erreurs | exécutable absent, permission refusée ou code non nul |
| effets | ceux du programme appelé ; ils doivent être documentés séparément |
| statut | `static-skeleton`, non exécuté |

> **[VSC] PowerShell 7 — Squelette statique `Invoke-CheckedNative.ps1` ; ne pas alimenter depuis une entrée non fiable.**

```powershell
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string] $Executable,

    [string[]] $ArgumentList = @()
)

$ErrorActionPreference = "Stop"
& $Executable @ArgumentList
$nativeCode = $LASTEXITCODE

if ($nativeCode -ne 0) {
    Write-Error "native_command_failed:$nativeCode"
    exit $nativeCode
}

exit 0
```

**Sécurité :** une allowlist du programme et des sous-commandes précède l’appel lorsque les paramètres proviennent d’une interface ou d’un fichier. Les commandes doivent être inspectées selon la section [Inspecter avant d’exécuter](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#82-inspecter-avant-dexécuter). PowerShell 7.6 LTS est documenté le 28 juillet 2026, mais cette recette n’a pas été qualifiée sur cette version ; voir le [cycle de support officiel](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle?view=powershell-7.6).

---

<!-- l5:card -->
## CODE-08 — Bash strict et portable

| Champ | Valeur |
|---|---|
| besoin | vérifier un fichier dans WSL ou Linux et produire une ligne tabulée |
| entrées | chemin reçu comme premier argument |
| sortie | chemin et taille sur stdout |
| codes | `0` trouvé, `2` argument absent, `3` fichier absent |
| effets | lecture seule |
| portabilité | Bash requis ; aucun utilitaire GNU spécifique au-delà de `wc` |
| statut | `static-skeleton`, non exécuté dans WSL |

> **[WSL] Bash — Squelette statique `check-file.sh` ; lancer uniquement dans l’environnement déclaré.**

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

if (($# != 1)); then
    printf '%s\n' 'usage: check-file.sh <path>' >&2
    exit 2
fi

readonly input=$1
if [[ ! -f "$input" ]]; then
    printf '%s\n' 'input_not_found' >&2
    exit 3
fi

readonly bytes=$(wc -c < "$input")
printf '%s\t%s\n' "$input" "$bytes"
```

`set -e` possède des exceptions selon la position de la commande ; `pipefail` change le statut d’un pipeline mais ne remplace pas les tests explicites. La référence normative est le [builtin `set` de Bash](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html). Le guide conserve la séparation entre exécutables Windows et WSL décrite dans le [chapitre terminal](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#12-séparer-windows-et-wsl).

---

<!-- l5:card -->
## CODE-09 — Frontières d’effets

| Risque | Contrôle minimal | Preuve attendue |
|---|---|---|
| chemin absolu propre à une machine | racine fournie ou découverte depuis le dépôt | chemin résolu et portable |
| remontée `..` ou lien symbolique | résolution canonique et vérification sous la racine autorisée | refus avant écriture |
| remplacement d’une source | staging, empreinte, diff et promotion séparée | même artefact promu |
| fichier partiel | écriture temporaire puis remplacement atomique si le système le permet | aucun candidat incomplet |
| processus enfant | exécutable allowlisté, arguments séparés, timeout et code conservé | commande résolue et journaux |
| shell implicite | appel sans concaténation de chaîne ; shell explicite seulement si requis | absence d’interprétation inattendue |
| secret | référence injectée au runtime, jamais valeur copiée dans arguments ou logs | scan et rédaction |
| réseau | désactivé par défaut ; hôte, protocole et timeout explicites | destination et décision |
| privilège | session utilisateur et moindre privilège | identité et permissions |
| nettoyage | supprimer seulement les temporaires identifiés du run | manifeste des chemins |

Les règles de [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime) et de [sorties hors workspace](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#17-interdire-les-sorties-hors-du-workspace) prévalent. Un script court peut avoir un rayon d’impact supérieur à sa taille.

---

<!-- l5:card -->
## CODE-10 — Tests et fixtures

| Test | Fixture minimale | Oracle | Statut de cette fiche |
|---|---|---|---|
| syntaxe GDScript | fichier isolé et projet minimal | parse sans erreur | non exécuté |
| fonction pure GDScript | chaînes normales et invalides | résultat fermé attendu | non exécuté |
| script Godot CLI | ressource présente puis absente | codes `0` et `3` | non exécuté |
| syntaxe Python | module sans dépendance tierce | compilation ou import | non exécuté |
| CLI Python | source UTF-8 temporaire | fichier de staging identique | non exécuté |
| JSON Python | objet, tableau, JSON cassé et fichier trop grand | valeur ou exception exacte | non exécuté |
| parse PowerShell | fichier `.ps1` sans exécution | aucune erreur d’analyse | non exécuté |
| commande native | programme témoin succès puis échec | code propagé | non exécuté |
| syntaxe Bash | fichier isolé | `bash -n` sans erreur | non exécuté |
| Bash nominal et refus | fichier temporaire puis chemin absent | codes `0` et `3` | non exécuté |
| idempotence | même entrée et même staging nettoyé | même résultat ou refus défini | non exécuté |
| sécurité | chemins sortants, arguments hostiles et secret factice | refus sans fuite ni effet | non exécuté |

Un test précise une entrée, une observation et une règle stable ; il ne se réduit pas à l’absence d’exception. Le [portfolio des tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md#3-portfolio-de-tests) détermine quand une recette doit passer d’un test pur à une intégration réelle. Les frameworks, plugins et fixtures seront versionnés lors de la matérialisation du Companion Pack.

---

<!-- l5:card -->
## CODE-11 — Sécurité, dépendances et licences

| Objet | Exigence |
|---|---|
| auteur du snippet | identité du projet ou source externe précise |
| licence du fichier | en-tête ou fichier de licence compatible avec la collection |
| dépendance standard | version minimale et comportement utilisé |
| dépendance tierce | dépôt, version ou commit, licence, intégrité et retrait |
| code copié | provenance, modifications et obligations conservées |
| commande téléchargée | fichier séparé, inspection et empreinte avant exécution |
| modèle ou service | licence indépendante du script client |
| fixture | petite, synthétique, autorisée et sans donnée personnelle réelle |
| secret factice | valeur manifestement non valide et impossible à confondre avec un secret actif |
| logs | arguments sensibles rédigés, rétention et accès bornés |
| contribution IA | revue humaine, tests et provenance selon la politique du projet |
| publication | validation juridique organisationnelle lorsque nécessaire |

Une empreinte prouve l’identité des octets, pas leur sûreté ni leurs droits ; voir [Calculer une empreinte](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#102-calculer-une-empreinte). Les licences transversales seront consolidées au chapitre 25. Les exemples de cette fiche sont rédigés pour le guide et restent soumis à la future licence globale de la collection.

---

<!-- l5:matrix -->
## Matrice B — Cycle de preuve

| État | Porte | Artefact autorisé | Passage interdit |
|---|---|---|---|
| `draft` | but, langage et propriétaire identifiés | note ou prototype local | diffusion comme recette |
| `static-reviewed` | interface, risques, liens et licence relus | snippet versionné | annoncer une syntaxe confirmée |
| `syntax-checked` | parseur exact et code de sortie conservés | rapport de syntaxe | annoncer le comportement |
| `unit-tested` | cas nominaux, refus et limites passés | rapport et fixtures | annoncer l’intégration |
| `integration-tested` | moteur, fichiers ou processus réels testés | artefacts de staging | annoncer la portabilité générale |
| `qualified` | campagne C, sécurité, repli et environnement vierge | paquet candidat | modifier le candidat après revue |
| `accepted` | revue métier, technique et licence terminée | même paquet immuable | étendre le périmètre sans test |
| `production` | promotion, observabilité et rollback prêts | composant distribué | perdre les sources et preuves |
| `withdrawn` | appelants connus et migration décidée | historique et remplaçant | nouvel usage |

La progression suit la séparation entre définition, exécution et preuve du [cycle des workflows](CHAPITRE-08-Bibliotheque-de-workflows.md#matrice-b--cycle-dun-workflow). Un statut ne se déduit jamais du nom du fichier ou d’un commentaire `tested`.

---

<!-- l5:matrix -->
## Matrice C — Qualification minimale

| Test | Entrée fixe | Observation | Preuve attendue | État ici |
|---|---|---|---|---|
| Q1 — lecture | recette et sources | interface sans ambiguïté | revue et liens valides | relu |
| Q2 — syntaxe | fichier isolé | parseur ou shell exact | version, commande et code | non exécuté |
| Q3 — aide | aucun argument ou `--help` | usage et paramètres | stdout/stderr et code | non exécuté |
| Q4 — nominal | fixture autorisée | sortie complète | empreinte et comparaison | non exécuté |
| Q5 — argument invalide | valeur hors contrat | refus avant effet | code stable et diagnostic | non exécuté |
| Q6 — entrée absente | chemin inexistant | aucun candidat produit | code et staging inspecté | non exécuté |
| Q7 — limite | taille, longueur ou nombre maximal | succès à la borne, refus au-delà | fixtures et résultats | non exécuté |
| Q8 — répétition | même entrée deux fois | résultat identique ou politique déclarée | comparaison et effets | non exécuté |
| Q9 — interruption | arrêt au point contrôlé | temporaire nettoyé ou conservé selon règle | inventaire du workspace | non exécuté |
| Q10 — sécurité | chemin sortant, injection et secret factice | refus sans fuite | logs rédigés et diff | non exécuté |
| Q11 — environnement vierge | dépendances verrouillées | installation puis tests | versions et rapports | non exécuté |
| Q12 — repli et retrait | dépendance absente ou version bloquée | alternative ou arrêt explicite | décision et migration | non exécuté |

Les résultats mesurés appartiendront au chapitre 21 et les compatibilités historiques au chapitre 22. Cette matrice décrit la campagne nécessaire pour élever une recette au-delà de `static-reviewed`.

---

<!-- l5:card -->
## CODE-12 — Paquet et acceptation

| Élément | Exigence |
|---|---|
| fiche | but, statut, langage, environnement, entrées, sorties, erreurs et liens propriétaires |
| source | fichier lisible, encodage, fins de ligne, version et empreinte |
| appel | exemple minimal sans secret et avec dossier courant explicite |
| configuration | valeurs non sensibles, limites et ordre de résolution |
| dépendances | versions ou commits, licences, intégrité et alternatives |
| tests | fixtures, oracles, commandes et codes de sortie |
| sécurité | frontières de chemins, processus, réseau, secrets et privilèges |
| preuve | environnement, run, rapports, artefacts, digests et réserves |
| portabilité | plateformes réellement testées et différences connues |
| maintenance | propriétaire, appelants, compatibilité, retrait et migration |
| Companion Pack | chemin prévu et statut `not-materialized` tant que le fichier n’existe pas |
| décision | `static-reviewed`, `qualified`, `accepted`, `blocked`, `superseded` ou `withdrawn` |

**Porte minimale :** une recette relue sans parseur reste `static-reviewed`. Un paquet devient `qualified` seulement après syntaxe, cas nominal, refus, limites, répétition, interruption, sécurité, environnement vierge et repli enregistrés.

**Frontières :**

- les tutoriels complets restent dans les Livres I à IV ;
- le chapitre 10 possède les recettes courtes et leur index ;
- le chapitre 11 possédera la référence GDScript ;
- le chapitre 12 possédera la référence Python ;
- le chapitre 13 possédera les formats d’échange ;
- la fiche 08 possède l’orchestration des workflows ;
- la fiche 09 possède les prompts et leurs critères ;
- le chapitre 20 possédera le catalogue transversal des diagnostics ;
- le chapitre 21 possédera les campagnes exécutées et mesures ;
- le chapitre 24 possédera les checklists transversales ;
- le chapitre 25 possédera licences, provenance et conformité ;
- les fichiers réutilisables réels appartiendront au Companion Pack après matérialisation.

**Niveau de preuve :** `static-review`. Les blocs GDScript, Python, PowerShell et Bash ont été relus comme squelettes, mais aucun parseur, moteur, shell, test, fichier de fixture, processus natif, workspace, secret, réseau, approbation juridique ou PDF n’a été exécuté ou produit pour cette fiche.
