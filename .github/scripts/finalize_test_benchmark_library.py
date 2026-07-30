#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "Companion-Pack" / "Test-Benchmark-Library"
QUALIFICATION_RUN = "30540336088"
ARTIFACT_ID = "8758417029"
ARTIFACT_DIGEST = "sha256:4c4aeeea49e3d9b1d7124bb2da119e0d4994d14250e1c9959754cf980cf18d42"
FINALIZER_RUN = os.environ.get("GITHUB_RUN_ID", "unknown")
STAMP = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
DATE = STAMP[:10]


def read(path: str | Path) -> str:
    return (ROOT / path).read_text(encoding="utf-8") if isinstance(path, str) else path.read_text(encoding="utf-8")


def write(path: str | Path, content: str) -> None:
    target = ROOT / path if isinstance(path, str) else path
    target.write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    content = read(path)
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one occurrence in {path}, found {count}: {old[:80]!r}")
    write(path, content.replace(old, new, 1))


def replace_between(path: str, start: str, end: str, replacement: str) -> None:
    content = read(path)
    start_index = content.index(start)
    end_index = content.index(end, start_index)
    write(path, content[:start_index] + replacement + content[end_index:])


README = f'''---
title: "Companion Pack — Test & Benchmark Library"
id: "CP-PACK-08-TEST-BENCHMARK-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{STAMP}"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Test & Benchmark Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 8 centralise des tests fonctionnels, des charges synthétiques et des formats de mesure reproductibles. Il sépare explicitement la preuve d’exécution, la mesure locale et toute comparaison de performance.

## État qualifié

| Élément | État |
|---|---|
| fichiers du Pack | 73 validés |
| contrats versionnés | 6 |
| tests Python | 25 réussis |
| suite GDScript | réussie |
| benchmarks Python | CPU, mémoire et corpus exécutés séparément |
| scènes Godot | CPU, mémoire et proxy de rendu exécutés séparément |
| résultats de campagne | 6 résultats horodatés et validés |
| formats | JSON, CSV, YAML-compatible et Markdown |
| arbre Git | propre après suppression des artefacts runtime |

## Exécution Python séparée

> **[PS] PowerShell — Exécuter depuis la racine du dépôt :**

```powershell
$env:PYTHONPATH = ".\\Companion-Pack\\Test-Benchmark-Library\\python\\src"
python .\\Companion-Pack\\Test-Benchmark-Library\\scripts\\run_python_suite.py `
  --benchmark cpu `
  --output-dir .\\dist\\bench-cpu
```

Remplacer `cpu` par `memory`, `corpus` ou `all`.

## Tests Python

```powershell
$env:PYTHONPATH = ".\\Companion-Pack\\Test-Benchmark-Library\\python\\src"
python -m unittest discover `
  -s .\\Companion-Pack\\Test-Benchmark-Library\\python\\tests `
  -v
```

## Scènes Godot

Chaque scène s’exécute indépendamment :

```text
res://scenes/cpu_benchmark.tscn
res://scenes/memory_benchmark.tscn
res://scenes/render_proxy_benchmark.tscn
```

## Qualification obtenue

Le run `{QUALIFICATION_RUN}` a validé les 73 fichiers du Pack, 25 tests Python, la suite GDScript, trois benchmarks Python et trois scènes Godot exécutés séparément. Il a produit six résultats avec horodatage UTC, seed, paramètres, observations brutes, statistiques de dispersion et empreinte d’environnement.

Environnement : Ubuntu 24.04, CPython `3.12.13` et Godot `4.7.1.stable.official.a13da4feb`. Le proxy de rendu a utilisé Xvfb, `gl_compatibility` et Mesa llvmpipe ; il qualifie le protocole graphique virtuel, pas un GPU physique.

Artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}`. Le finaliseur de gouvernance a été exécuté par le run `{FINALIZER_RUN}`.

## Interprétation

Une mesure est liée au contrat, au commit, à la seed, au scénario, aux versions et à l’empreinte matérielle. Les résultats du runner hébergé prouvent que le protocole s’exécute ; ils ne décrivent pas les performances générales d’un PC, d’un GPU ou du projet final.

## Réserves

La qualification ne valide aucun Windows, GPU physique, Forward+, pilote AMD/ZLUDA, mobile, console, charge longue, performance produit, modèle IA réel, export, publication, release, licence globale ou redistribution autonome.
'''
write(PACK / "README.md", README)

manifest_path = PACK / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["status"] = "reviewed"
manifest["validation"] = "runtime-tested-linux"
manifest["qualified_run"] = int(QUALIFICATION_RUN)
manifest["artifact_id"] = int(ARTIFACT_ID)
manifest["artifact_digest"] = ARTIFACT_DIGEST
manifest["qualified_environment"] = {
    "os": "ubuntu-24.04",
    "python": "3.12.13",
    "godot": "4.7.1.stable.official.a13da4feb",
    "render_proxy": "xvfb-gl-compatibility-mesa-llvmpipe",
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

AUDIT = f'''---
title: "Audit — Test & Benchmark Library"
id: "CP-AUDIT-PACK-08"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "{STAMP}"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Décision

Le Pack 8 est accepté dans son périmètre Linux x86_64 pour les tests et mesures synthétiques reproductibles.

## Périmètre validé

- 73 fichiers du Pack et 6 contrats versionnés ;
- 25 tests Python et une suite GDScript ;
- trois benchmarks Python exécutés séparément ;
- trois scènes Godot exécutées séparément ;
- six résultats horodatés avec seeds, paramètres, observations brutes, variance, écart-type, coefficient de variation, p95 et p99 ;
- portes de comparaison compatibles et incompatibles ;
- campagne JSON, CSV et Markdown ;
- fixtures et corpus entièrement synthétiques ;
- arbre Git propre et absence de donnée privée détectée.

## Preuves runtime

- workflow permanent : `Validate Test Benchmark Library` ;
- run : `{QUALIFICATION_RUN}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}` ;
- Ubuntu 24.04, Python `3.12.13`, Godot `4.7.1.stable.official.a13da4feb` ;
- archive Godot vérifiée par SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` ;
- Xvfb, renderer `gl_compatibility`, Mesa llvmpipe pour le proxy de rendu ;
- finaliseur de gouvernance : run `{FINALIZER_RUN}`.

## Décision de comparabilité

Les temps observés ne sont pas promus comme références universelles. Une comparaison automatique est refusée lorsque le contrat, la charge, la seed, l’implémentation, l’unité ou l’empreinte d’environnement diffère.

## Réserves

Aucun Windows, GPU physique, Forward+, pilote AMD/ZLUDA, mobile, console, charge longue, performance produit, modèle IA réel, export, publication, release, licence globale ou redistribution autonome n’est validé.
'''
write(PACK / "qa" / "AUDIT-TEST-BENCHMARK-LIBRARY.md", AUDIT)

PROOF = f'''schema-version: 1
evidence-id: QA-TEST-BENCHMARK-LIBRARY-PACK-08
status: complete
validation-date: '{DATE}'
source-branch: feat/companion-pack-test-benchmark-library
pack:
  id: CP-PACK-08-TEST-BENCHMARK-LIBRARY
  version: 1.0.0
  audit-level: runtime-tested-linux
environment:
  os: ubuntu-24.04
  python: 3.12.13
  godot: 4.7.1.stable.official.a13da4feb
  render-proxy: xvfb-gl-compatibility-mesa-llvmpipe
results:
  source-files: 73
  contracts: 6
  catalog-entries: 12
  python-tests:
    status: success
    count: 25
  gdscript-tests: success
  python-benchmarks:
    status: success
    count: 3
  godot-scenes:
    status: success
    count: 3
  campaign-results:
    status: success
    count: 6
  formats:
    - json
    - csv
    - yaml-compatible
    - markdown
  clean-tree: true
  private-fields-detected: false
  physical-gpu-qualified: false
ci:
  workflow: Validate Test Benchmark Library
  run-id: {QUALIFICATION_RUN}
  artifact-id: {ARTIFACT_ID}
  artifact-digest: {ARTIFACT_DIGEST}
  governance-finalizer-run: {FINALIZER_RUN}
reservations:
  - No universal performance claim.
  - No Windows or physical GPU qualification.
  - No Forward+, AMD/ZLUDA, mobile or console qualification.
  - No long-duration or product-performance campaign.
  - Global license undefined.
'''
write(PACK / "qa" / "VALIDATION-TEST-BENCHMARK-LIBRARY.yaml", PROOF)

replace_once("Companion-Pack/index.md", 'version: "0.8.0"', 'version: "0.9.0"')
replace_once("Companion-Pack/index.md", 'last-updated: "2026-07-30T12:34:03+02:00"', f'last-updated: "{STAMP}"')
replace_once("Companion-Pack/index.md", '8. [ ] Test & Benchmark Library ;', '8. [x] [Test & Benchmark Library](Test-Benchmark-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Godot et proxy de rendu Xvfb ;')
replace_once("Companion-Pack/index.md", 'Progression : **7 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library, Database Library, ComfyUI Library et Documentation Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, rendus documentaires visuels, accessibilité, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 8 — Test & Benchmark Library.', 'Progression : **8 packs sur 10**. Les Packs 1 à 8 sont matérialisés et validés dans leur périmètre Linux. Les mesures du Test & Benchmark Library restent synthétiques et liées à leurs environnements ; aucun classement matériel universel ni GPU physique n’est qualifié. Les réserves services IA réels, modèles, réseau distant, performance produit, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, accessibilité, exports et licence globale restent ouvertes. La prochaine action est le Pack 9 — Production Toolkit.')

replace_once("ROADMAP.md", '**Statut M7 : actif — 7 packs validés sur 10 ; Pack 8, Test & Benchmark Library, suivant.**', '**Statut M7 : actif — 8 packs validés sur 10 ; Pack 9, Production Toolkit, suivant.**')
replace_once("ROADMAP.md", '- [ ] Test & Benchmark Library.', '- [x] Test & Benchmark Library — version `1.0.0`, validation Linux `runtime-tested` avec Python, Godot et proxy Xvfb borné.')

replace_once("plans/COMPANION-PACK-PLAN-MAITRE.md", 'version: "1.7.0"', 'version: "1.8.0"')
replace_once("plans/COMPANION-PACK-PLAN-MAITRE.md", '> **Statut :** en cours — Pack 7 sur 10 validé', '> **Statut :** en cours — Pack 8 sur 10 validé')
replace_once("plans/COMPANION-PACK-PLAN-MAITRE.md", '## Pack 8 — Test & Benchmark Library\n\n**Objectifs**', '## Pack 8 — Test & Benchmark Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `30540336088` avec Python, Godot et proxy de rendu Xvfb ; réserves GPU physique, Windows, performance produit, charges longues, exports et licence globale maintenues.\n\n**Objectifs**')

contents = read("contents.txt")
entry = "Companion-Pack/Test-Benchmark-Library/README.md\n"
if entry not in contents:
    if not contents.endswith("\n"):
        contents += "\n"
    contents += entry
    write("contents.txt", contents)

replace_once("CONTINUITE-PROJET.md", 'version: "4.21.0"', 'version: "4.22.0"')
replace_once("CONTINUITE-PROJET.md", 'last-updated: "2026-07-30T12:34:03+02:00"', f'last-updated: "{STAMP}"')
replace_once("CONTINUITE-PROJET.md", '- progression du Companion Pack : 7 packs validés sur 10 ;', '- progression du Companion Pack : 8 packs validés sur 10 ;')
replace_once("CONTINUITE-PROJET.md", '- Documentation Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec génération déterministe, PyYAML et Pandoc HTML ;', '- Documentation Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec génération déterministe, PyYAML et Pandoc HTML ;\n- Test & Benchmark Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Godot et proxy de rendu Xvfb borné ;')

NEXT = '''## 26. Prochaine action

M7 — Companion Pack est actif. Les Packs 1 à 8 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Test & Benchmark Library a validé 73 fichiers, 6 contrats, 25 tests Python, une suite GDScript, trois benchmarks Python, trois scènes Godot et six résultats de campagne avec répétitions, variance, seeds et empreintes d’environnement. Les temps du runner ne sont pas des références universelles ; Windows, GPU physique, Forward+, AMD/ZLUDA, mobile, console, charges longues, performance produit, exports et licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/Production-Toolkit/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 9 doit matérialiser un outillage de production : scripts Blender, convertisseurs de textures et audio, validateurs d’assets, générateurs de catalogues, outils de renommage, pipelines de lots, scripts d’import Godot et packaging. Les outils devront proposer un mode dry-run, des journaux et codes de sortie, la reprise après erreur, préserver les sources et être testés sur des assets synthétiques.
'''
replace_between("CONTINUITE-PROJET.md", "## 26. Prochaine action\n", "## 27. Journal\n", NEXT)

JOURNAL = f'''## 27. Journal

### {STAMP} — version 4.22.0

- matérialisation du Companion Pack, Pack 8 — Test & Benchmark Library ;
- 73 fichiers du Pack, six contrats, douze entrées de catalogue, fixtures, seeds et corpus synthétique créés ;
- 25 tests Python et suite GDScript réussis ;
- trois benchmarks Python et trois scènes Godot exécutés séparément ;
- six résultats horodatés avec observations brutes, variance, écart-type, coefficient de variation, p95, p99 et empreinte d’environnement ;
- portes `comparable` et `not-comparable` validées ;
- campagne JSON, CSV et Markdown produite ;
- Ubuntu 24.04, Python `3.12.13` et Godot `4.7.1.stable.official.a13da4feb` qualifiés ;
- proxy de rendu Xvfb en `gl_compatibility` avec Mesa llvmpipe, sans revendication GPU physique ;
- run `{QUALIFICATION_RUN}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- arbre Git propre, aucun champ privé détecté et aucune donnée non redistribuable incluse ;
- progression M7 portée à 8 packs sur 10 ;
- prochaine action : `Companion-Pack/Production-Toolkit/README.md`, niveau Élevée ;
- aucun Windows, GPU physique, Forward+, AMD/ZLUDA, mobile, console, charge longue, performance produit, modèle IA réel, export, release ou licence globale validé ou produit.

'''
replace_once("CONTINUITE-PROJET.md", "## 27. Journal\n\n", JOURNAL)

print(json.dumps({
    "status": "success",
    "timestamp": STAMP,
    "qualification_run": QUALIFICATION_RUN,
    "artifact_id": ARTIFACT_ID,
    "finalizer_run": FINALIZER_RUN,
}, ensure_ascii=False, sort_keys=True))
