#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "Companion-Pack" / "Production-Toolkit"
QUALIFICATION_RUN = "30544978391"
ARTIFACT_ID = "8760345537"
ARTIFACT_DIGEST = "sha256:d48f12b2aff00e76dc82e06072deb994863dff43fcce7758faa762c914841359"
QUALIFICATION_HEAD = "7edc117b63b596be57d91a6ff2338a29e8d970dc"
FINALIZER_RUN = os.environ.get("GITHUB_RUN_ID", "unknown")
STAMP = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
DATE = STAMP[:10]


def read(path: str | Path) -> str:
    target = ROOT / path if isinstance(path, str) else path
    return target.read_text(encoding="utf-8")


def write(path: str | Path, content: str) -> None:
    target = ROOT / path if isinstance(path, str) else path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    content = read(path)
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one occurrence in {path}, found {count}: {old[:100]!r}")
    write(path, content.replace(old, new, 1))


README = f'''---
title: "Companion Pack — Production Toolkit"
id: "CP-PACK-09-PRODUCTION-TOOLKIT"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{STAMP}"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Production Toolkit

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[VSC]** Visual Studio Code, **[APP]** application graphique, **[SORTIE]** résultat à contrôler et **[LECTURE]** contenu à étudier.

Le Pack 9 fournit des outils non destructifs pour produire, convertir, valider, cataloguer, renommer et empaqueter des assets. Il sépare les sources, le workspace et les sorties, et rend chaque opération mutante explicite.

## État qualifié

| Élément | État |
|---|---|
| fichiers du Pack | 28 validés |
| familles d’outils | 9 |
| tests Python | 29 réussis |
| dry-run | sorties métier absentes |
| conversions | PPM vers PNG et WAV stéréo vers PCM mono |
| reprise | échec injecté puis checkpoint repris |
| packaging | deux ZIP de SHA-256 identique |
| Blender | OBJ synthétique exporté en GLB |
| Godot | GLB importé et instancié |
| sources | empreintes SHA-256 inchangées |

## Principes d’exploitation

- `--dry-run` décrit les opérations sans créer les sorties métier ;
- les commandes émettent des journaux JSON structurés et des codes de sortie stables ;
- les sources sont lues, jamais modifiées ;
- l’écrasement est refusé par défaut ;
- les traitements par lots utilisent un checkpoint lié à l’empreinte du plan ;
- les archives ZIP utilisent un ordre, une date et des permissions déterministes ;
- les fixtures sont synthétiques.

## Exemple

```powershell
$env:PYTHONPATH = ".\\Companion-Pack\\Production-Toolkit\\python\\src"
python .\\Companion-Pack\\Production-Toolkit\\scripts\\toolkit_cli.py generate `
  --output .\\dist\\production-fixtures
python .\\Companion-Pack\\Production-Toolkit\\scripts\\toolkit_cli.py batch `
  --plan .\\Companion-Pack\\Production-Toolkit\\fixtures\\plans\\pipeline.json `
  --source-root .\\Companion-Pack\\Production-Toolkit\\fixtures `
  --workspace .\\dist\\production-workspace `
  --dry-run
```

## Qualification obtenue

Le run `{QUALIFICATION_RUN}` a validé 28 fichiers, 29 tests Python, le dry-run de toutes les familles mutantes, trois assets convertis ou validés, un échec injecté suivi d’une reprise complète, deux archives déterministes, l’export OBJ vers GLB et l’import Godot.

Environnement : Ubuntu 24.04, CPython `3.12.13`, Blender `4.0.2`, NumPy `1.26.4` dans Blender et Godot `4.7.1.stable.official.a13da4feb`.

Artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}`. Finaliseur de gouvernance : run `{FINALIZER_RUN}`.

## Interprétation

La qualification démontre les contrats fonctionnels sur des assets synthétiques. Elle ne mesure ni la qualité artistique, ni la qualité audio perceptuelle, ni les performances générales d’un poste de production.

## Réserves

Aucun format propriétaire, bake complexe, compression GPU, rendu artistique, export de jeu, Windows, macOS, GPU physique, mobile, console, publication, release, licence globale ou redistribution autonome n’est validé.
'''
write(PACK / "README.md", README)

manifest_path = PACK / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest.update({
    "status": "reviewed",
    "validation": "runtime-tested-linux",
    "qualified_run": int(QUALIFICATION_RUN),
    "artifact_id": int(ARTIFACT_ID),
    "artifact_digest": ARTIFACT_DIGEST,
    "qualified_environment": {
        "os": "ubuntu-24.04",
        "python": "3.12.13",
        "blender": "4.0.2",
        "blender_numpy": "1.26.4",
        "godot": "4.7.1.stable.official.a13da4feb",
    },
})
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

AUDIT = f'''---
title: "Audit — Production Toolkit"
id: "CP-AUDIT-PACK-09"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "{STAMP}"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Décision

Le Pack 9 est accepté dans son périmètre Linux x86_64 pour des traitements non destructifs sur assets synthétiques.

## Périmètre validé

- 28 fichiers et neuf familles d’outils ;
- 29 tests Python ;
- dry-run sans création de sortie métier ;
- journaux JSON et codes de sortie ;
- conversions PPM vers PNG et WAV stéréo vers PCM mono ;
- validation OBJ, PNG et WAV ;
- renommage par copie avec collisions résolues ;
- catalogue JSON et CSV ;
- échec injecté, checkpoint partiel et reprise complète ;
- deux archives ZIP déterministes ;
- Blender OBJ vers GLB ;
- Godot : import et instanciation du GLB ;
- SHA-256 des sources inchangés ;
- arbre Git propre et aucune donnée privée détectée.

## Preuves runtime

- workflow : `Validate Production Toolkit` ;
- run : `{QUALIFICATION_RUN}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}` ;
- Ubuntu 24.04 ;
- Python `3.12.13` ;
- Blender `4.0.2`, NumPy `1.26.4` ;
- Godot `4.7.1.stable.official.a13da4feb` ;
- finaliseur de gouvernance : run `{FINALIZER_RUN}`.

## Réserves

Aucun format propriétaire, bake complexe, compression GPU, rendu artistique, qualité perceptuelle, export de jeu, Windows, macOS, GPU physique, mobile, console, publication, release, licence globale ou redistribution autonome n’est qualifié.
'''
write(PACK / "qa" / "AUDIT-PRODUCTION-TOOLKIT.md", AUDIT)

PROOF = f'''schema-version: 1
evidence-id: QA-PRODUCTION-TOOLKIT-PACK-09
status: complete
validation-date: '{DATE}'
source-branch: feat/companion-pack-production-toolkit
pack:
  id: CP-PACK-09-PRODUCTION-TOOLKIT
  version: 1.0.0
  audit-level: runtime-tested-linux
environment:
  os: ubuntu-24.04
  python: 3.12.13
  blender: 4.0.2
  blender-numpy: 1.26.4
  godot: 4.7.1.stable.official.a13da4feb
results:
  source-files: 28
  catalog-entries: 9
  python-tests:
    status: success
    count: 29
  dry-run: success
  failure-injected: true
  resume-status: complete
  validated-assets: 3
  deterministic-package: true
  blender-glb: success
  godot-import: success
  source-preserved: true
  clean-tree: true
  private-fields-detected: false
  fixtures: synthetic
ci:
  workflow: Validate Production Toolkit
  run-id: {QUALIFICATION_RUN}
  artifact-id: {ARTIFACT_ID}
  artifact-digest: {ARTIFACT_DIGEST}
  governance-finalizer-run: {FINALIZER_RUN}
reservations:
  - No proprietary format or artistic-quality qualification.
  - No complex bake, GPU compression or perceptual-audio qualification.
  - No game export, Windows, macOS, mobile or console qualification.
  - Global license undefined.
'''
write(PACK / "qa" / "VALIDATION-PRODUCTION-TOOLKIT.yaml", PROOF)

replace_once("Companion-Pack/index.md", 'version: "0.9.0"', 'version: "0.10.0"')
replace_once("Companion-Pack/index.md", 'last-updated: "2026-07-30T14:03:39+02:00"', f'last-updated: "{STAMP}"')
replace_once(
    "Companion-Pack/index.md",
    "9. [ ] Production Toolkit ;",
    "9. [x] [Production Toolkit](Production-Toolkit/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Blender et import Godot ;",
)
replace_once(
    "Companion-Pack/index.md",
    "Progression : **8 packs sur 10**. Les Packs 1 à 8 sont matérialisés et validés dans leur périmètre Linux. Les mesures du Test & Benchmark Library restent synthétiques et liées à leurs environnements ; aucun classement matériel universel ni GPU physique n’est qualifié. Les réserves services IA réels, modèles, réseau distant, performance produit, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, accessibilité, exports et licence globale restent ouvertes. La prochaine action est le Pack 9 — Production Toolkit.",
    "Progression : **9 packs sur 10**. Les Packs 1 à 9 sont matérialisés et validés dans leur périmètre Linux. Production Toolkit qualifie des traitements non destructifs sur assets synthétiques avec Python, Blender et Godot ; les formats propriétaires, la qualité artistique, les exports de jeu et les plateformes non Linux restent réservés. Les réserves services IA réels, modèles, réseau distant, performance produit, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, accessibilité, exports et licence globale restent ouvertes. La prochaine action est le Pack 10 — Knowledge Base.",
)

replace_once(
    "ROADMAP.md",
    "**Statut M7 : actif — 8 packs validés sur 10 ; Pack 9, Production Toolkit, suivant.**",
    "**Statut M7 : actif — 9 packs validés sur 10 ; Pack 10, Knowledge Base, suivant.**",
)
replace_once(
    "ROADMAP.md",
    "- [ ] Production Toolkit.",
    "- [x] Production Toolkit — version `1.0.0`, validation Linux `runtime-tested` avec Python, Blender et import Godot.",
)

replace_once("plans/COMPANION-PACK-PLAN-MAITRE.md", 'version: "1.8.0"', 'version: "1.9.0"')
replace_once(
    "plans/COMPANION-PACK-PLAN-MAITRE.md",
    "> **Statut :** en cours — Pack 8 sur 10 validé",
    "> **Statut :** en cours — Pack 9 sur 10 validé",
)
replace_once(
    "plans/COMPANION-PACK-PLAN-MAITRE.md",
    "## Pack 9 — Production Toolkit\n\n**Objectifs**",
    "## Pack 9 — Production Toolkit\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `30544978391` avec Python, Blender et import Godot ; réserves formats propriétaires, qualité artistique, exports de jeu, plateformes non Linux et licence globale maintenues.\n\n**Objectifs**",
)

contents = read("contents.txt")
entry = "Companion-Pack/Production-Toolkit/README.md\n"
if entry not in contents:
    if not contents.endswith("\n"):
        contents += "\n"
    contents += entry
    write("contents.txt", contents)

replace_once("CONTINUITE-PROJET.md", 'version: "4.22.0"', 'version: "4.23.0"')
replace_once("CONTINUITE-PROJET.md", 'last-updated: "2026-07-30T14:03:39+02:00"', f'last-updated: "{STAMP}"')
replace_once(
    "CONTINUITE-PROJET.md",
    "- progression du Companion Pack : 8 packs validés sur 10 ;",
    "- progression du Companion Pack : 9 packs validés sur 10 ;",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- Test & Benchmark Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Godot et proxy de rendu Xvfb borné ;",
    "- Test & Benchmark Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Godot et proxy de rendu Xvfb borné ;\n- Production Toolkit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python, Blender et import Godot ;",
)

continuity = read("CONTINUITE-PROJET.md")
start = continuity.index("## 26. Prochaine action")
end = continuity.index("## 27. Journal", start)
next_action = '''## 26. Prochaine action

M7 — Companion Pack est actif. Les Packs 1 à 9 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Production Toolkit a validé 28 fichiers, neuf familles, 29 tests Python, le dry-run, les codes de sortie, l’échec injecté et la reprise, les conversions synthétiques, deux ZIP déterministes, Blender OBJ vers GLB, l’import Godot et la préservation des sources. Les formats propriétaires, la qualité artistique, les bakes complexes, la compression GPU, les exports de jeu, les plateformes non Linux et la licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/Knowledge-Base/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 10 doit matérialiser une base de connaissances synthétique : lore, codex, documents RAG, schémas de métadonnées, corpus de test, scripts de découpage, index reproductibles et outils de suppression/réindexation. Les droits devront être clairs, le corpus synthétique ou autorisé, l’index recréable depuis les sources, les tests de recherche exécutés et la suppression complète d’un document vérifiée.

'''
continuity = continuity[:start] + next_action + continuity[end:]
write("CONTINUITE-PROJET.md", continuity)

journal_entry = f'''### {STAMP} — version 4.23.0

- matérialisation du Companion Pack, Pack 9 — Production Toolkit ;
- 28 fichiers du Pack et neuf familles d’outils créés ;
- 29 tests Python réussis ;
- dry-run sans sortie métier, journaux JSON et codes de sortie validés ;
- conversions PPM vers PNG et WAV stéréo vers PCM mono validées ;
- validation OBJ, PNG et WAV, renommage par copie et catalogue JSON/CSV validés ;
- échec injecté, checkpoint partiel et reprise complète validés ;
- deux archives ZIP de SHA-256 identique produites ;
- Blender `4.0.2` avec NumPy `1.26.4` : OBJ synthétique exporté en GLB ;
- Godot `4.7.1.stable.official.a13da4feb` : GLB importé et instancié ;
- empreintes SHA-256 des sources inchangées ;
- run `{QUALIFICATION_RUN}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- arbre Git propre, aucune donnée privée ou asset tiers inclus ;
- progression M7 portée à 9 packs sur 10 ;
- prochaine action : `Companion-Pack/Knowledge-Base/README.md`, niveau Élevée ;
- aucun format propriétaire, rendu artistique, bake complexe, compression GPU, export de jeu, Windows, macOS, mobile, console, publication, release ou licence globale validé ou produit.

'''
replace_once("CONTINUITE-PROJET.md", "## 27. Journal\n\n", "## 27. Journal\n\n" + journal_entry)

checksums = {}
for path in sorted(PACK.rglob("*")):
    if path.is_file() and path.name != "checksums.json":
        checksums[path.relative_to(PACK).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
write(PACK / "checksums.json", json.dumps({"algorithm": "sha256", "files": checksums, "schema_version": 1}, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

print(json.dumps({
    "status": "success",
    "stamp": STAMP,
    "qualification_run": QUALIFICATION_RUN,
    "artifact_id": ARTIFACT_ID,
    "finalizer_run": FINALIZER_RUN,
    "pack_files": len([p for p in PACK.rglob("*") if p.is_file()]),
}, sort_keys=True))
