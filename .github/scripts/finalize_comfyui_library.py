from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/ComfyUI-Library"
TIMESTAMP = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
DATE = TIMESTAMP[:10]
RUN_ID = "30529642016"
ARTIFACT_ID = "8754176422"
ARTIFACT_DIGEST = "sha256:19be52a44ab295a747cb4ed7655268058d27494572e83709455004bf5be145af"
COMFYUI_COMMIT = "700821e1364eaab0e8f21c538a2131719fec57bf"
PYTHON_VERSION = "3.12.13"
TORCH_VERSION = "2.13.0+cu130"
OUTPUT_SHA256 = "868bc37be44cf32ae8cac9e55106bd2d16dc9161f6bea4e391e9c146e7603388"
OUTPUT_SIZE = 1565


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def dump_json(path: Path, value: dict) -> None:
    write(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


# Pack README.
path = PACK / "README.md"
text = read(path)
text = replace_once(text, 'status: "candidate"', 'status: "reviewed"', "README status")
text = replace_once(text, 'validation-status: "candidate-runtime"', 'validation-status: "runtime-tested-linux"', "README validation")
text = replace_once(text, 'lang: "fr-FR"\n', f'lang: "fr-FR"\nlast-verified: "{TIMESTAMP}"\n', "README timestamp")
text = replace_once(text, '| Élément | État candidat |', '| Élément | État qualifié |', "README state heading")
text = replace_once(text, '| workflow de validation sans modèle | matérialisé |', f'| workflow de validation sans modèle | exécuté sur CPU par le run `{RUN_ID}` |', "README runtime row")
text = replace_once(text, '| manifeste ComfyUI | tag `v0.28.0`, commit à enregistrer pendant la qualification |', f'| manifeste ComfyUI | tag `v0.28.0`, commit `{COMFYUI_COMMIT}` |', "README commit row")
text = replace_once(text, '| qualification ComfyUI | à exécuter en CI |', f'| qualification ComfyUI | validée sur Linux x86_64 par le run `{RUN_ID}` |', "README qualification row")
text = replace_once(
    text,
    '## 10. Réserves\n\nLe candidat ne valide encore aucun modèle réel, aucune génération text-to-image, aucun custom node tiers, aucun profil AMD, aucune performance, aucune qualité artistique, aucun droit d’exploitation de sortie et aucune redistribution autonome.',
    f'''## 10. Qualification obtenue

Le run `{RUN_ID}` a validé 37 fichiers du Pack et 12 tests Python, puis a cloné ComfyUI `v0.28.0` au commit `{COMFYUI_COMMIT}`. L’environnement utilisait CPython `{PYTHON_VERSION}` et Torch `{TORCH_VERSION}` sur Ubuntu 24.04.

Le workflow `WF-COMFY-0001` a réellement exécuté `LoadImage → SaveImage` sans modèle ni custom node tiers. La sortie PNG contient les métadonnées `prompt` et `workflow`, mesure `{OUTPUT_SIZE}` octets et possède l’empreinte `{OUTPUT_SHA256}`.

Artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}`. L’arbre Git est resté propre et aucun PDF n’a été produit.

## 11. Réserves

La qualification ne valide aucun modèle réel, aucune génération text-to-image, aucun custom node tiers, aucun profil AMD, aucune performance, aucune qualité artistique, aucun droit d’exploitation de sortie et aucune redistribution autonome.''',
    "README qualification section",
)
write(path, text)

# Pack metadata.
path = PACK / "manifest.json"
data = load_json(path)
data["status"] = "reviewed"
data["qualification"] = {
    "level": "runtime-tested-linux",
    "run_id": int(RUN_ID),
    "artifact_id": int(ARTIFACT_ID),
}
dump_json(path, data)

path = PACK / "PROVENANCE.json"
data = load_json(path)
data["qualification"] = f"runtime-tested-linux-run-{RUN_ID}"
dump_json(path, data)

path = PACK / "DEPENDENCIES.json"
data = load_json(path)
for dependency in data["runtime_dependencies"]:
    if dependency["id"] == "comfyui":
        dependency["qualification"] = f"pass-run-{RUN_ID}"
dump_json(path, data)

path = PACK / "manifests/comfyui.yaml"
data = load_json(path)
data["comfyui"]["commit"] = COMFYUI_COMMIT
data["runtime_qualification"] = {
    "status": "success",
    "profile": "PROFILE-COMFY-CPU-001",
    "run_id": int(RUN_ID),
    "python": PYTHON_VERSION,
    "torch": TORCH_VERSION,
    "models_loaded": 0,
    "custom_nodes_loaded": 0,
}
dump_json(path, data)

path = PACK / "manifests/workflows/WF-COMFY-0001.yaml"
data = load_json(path)
data["comfyui"]["commit"] = COMFYUI_COMMIT
data["backend"]["executed"] = True
data["backend"]["run_id"] = int(RUN_ID)
data["actual_output"] = {
    "format": "png",
    "size_bytes": OUTPUT_SIZE,
    "sha256": OUTPUT_SHA256,
    "metadata": ["prompt", "workflow"],
}
data["verified_date"] = DATE
dump_json(path, data)

# Recalculate all declared permanent checksums after final metadata updates.
path = PACK / "checksums.json"
data = load_json(path)
for relative in sorted(data["files"]):
    target = PACK / relative
    data["files"][relative] = hashlib.sha256(target.read_bytes()).hexdigest()
dump_json(path, data)

# Permanent audit and QA proof.
write(
    PACK / "qa/AUDIT-COMFYUI-LIBRARY.md",
    f'''---
title: "Audit — ComfyUI Library"
id: "CP-AUDIT-PACK-06"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "{TIMESTAMP}"
---

# Décision

Le Pack 6 est accepté dans son périmètre Linux x86_64 avec ComfyUI `v0.28.0`, CPython `{PYTHON_VERSION}` et le profil CPU sans modèle.

## Périmètre comparé au plan maître

Le lot matérialise les workflows JSON, manifestes, listes de custom nodes, presets, scripts de lancement, modèles de dossiers, provenance, image légère et checksums prévus. Il ne modifie ni l’ordre des Packs ni les frontières des chapitres propriétaires.

## Contrôle anti-doublon

- la sélection de concepts reste au Livre III, chapitre 3 ;
- l’orchestration de lots reste au Livre III, chapitre 30 ;
- les files et caches de fournisseurs restent dans l’AI Library ;
- les benchmarks comparatifs restent réservés au Pack 8 ;
- aucun modèle ou custom node tiers n’est distribué.

## Preuves runtime

- workflow permanent : `Validate ComfyUI Library` ;
- run : `{RUN_ID}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}` ;
- ComfyUI : `v0.28.0`, commit `{COMFYUI_COMMIT}` ;
- Python : `{PYTHON_VERSION}` ;
- Torch : `{TORCH_VERSION}` ;
- 37 fichiers du Pack validés ;
- 12 tests Python réussis ;
- workflow `LoadImage → SaveImage` exécuté sans modèle ;
- base SQLite interne créée dans le workspace runtime ;
- PNG de `{OUTPUT_SIZE}` octets, SHA-256 `{OUTPUT_SHA256}` ;
- métadonnées `prompt` et `workflow` validées ;
- aucun modèle, custom node tiers ou PDF produit ;
- arbre Git propre après runtime.

## Réserves

Le workflow text-to-image, les modèles réels, les custom nodes tiers, le profil AMD/ZLUDA, Windows graphique, les performances, la qualité artistique, les droits d’exploitation des sorties, les exports, les releases et la licence globale ne sont pas validés.
''',
)

qa = {
    "schema-version": 1,
    "evidence-id": "CP-QA-PACK-06",
    "status": "complete",
    "validation-date": DATE,
    "source-branch": "feat/companion-pack-comfyui-library",
    "pack": {
        "id": "CP-PACK-06-COMFYUI-LIBRARY",
        "version": "1.0.0",
        "entry-point": "Companion-Pack/ComfyUI-Library/README.md",
        "audit-level": "runtime-tested-linux",
    },
    "environment": {
        "os": "ubuntu-24.04",
        "python": PYTHON_VERSION,
        "torch": TORCH_VERSION,
        "comfyui_tag": "v0.28.0",
        "comfyui_commit": COMFYUI_COMMIT,
    },
    "results": {
        "source-files": 37,
        "workflow-count": 2,
        "runtime-workflows": 1,
        "template-workflows": 1,
        "profiles": 3,
        "python-tests": {"status": "success", "count": 12},
        "comfyui-runtime": "success",
        "required-nodes": ["LoadImage", "SaveImage"],
        "models-included": False,
        "models-loaded": 0,
        "custom-node-code-included": False,
        "custom-nodes-loaded": 0,
        "database-created": True,
        "output": {
            "format": "png",
            "size-bytes": OUTPUT_SIZE,
            "sha256": OUTPUT_SHA256,
            "metadata": ["prompt", "workflow"],
        },
        "clean-tree": True,
        "pdf-produced": False,
    },
    "ci": {
        "workflow": "Validate ComfyUI Library",
        "run-id": int(RUN_ID),
        "artifact-id": int(ARTIFACT_ID),
        "artifact-digest": ARTIFACT_DIGEST,
    },
    "reservations": [
        "No model or text-to-image execution.",
        "No third-party custom node execution.",
        "No AMD, ZLUDA or Windows graphical execution.",
        "No performance or artistic quality measurement.",
        "No output-rights qualification.",
        "Global license undefined.",
    ],
}
dump_json(PACK / "qa/VALIDATION-COMFYUI-LIBRARY.yaml", qa)

# Index.
path = ROOT / "Companion-Pack/index.md"
text = read(path)
text = replace_once(text, 'version: "0.6.0"', 'version: "0.7.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-30T10:29:52+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(text, '6. [ ] ComfyUI Library ;', '6. [x] [ComfyUI Library](ComfyUI-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec ComfyUI CPU sans modèle ;', "index pack 6")
text = replace_once(
    text,
    'Progression : **5 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library et Database Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 6 — ComfyUI Library.',
    'Progression : **6 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library, Database Library et ComfyUI Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 7 — Documentation Library.',
    "index status",
)
write(path, text)

# Master plan.
path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
text = read(path)
text = replace_once(text, 'version: "1.5.0"', 'version: "1.6.0"', "plan version")
text = replace_once(text, '> **Statut :** en cours — Pack 5 sur 10 validé', '> **Statut :** en cours — Pack 6 sur 10 validé', "plan status")
text = replace_once(
    text,
    '## Pack 6 — ComfyUI Library\n\n**Objectifs**',
    f'## Pack 6 — ComfyUI Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `{RUN_ID}` avec ComfyUI CPU sans modèle ; réserves modèles, custom nodes tiers, AMD/ZLUDA, Windows graphique, performance, qualité, droits de sortie, exports et licence globale maintenues.\n\n**Objectifs**',
    "plan pack 6 state",
)
write(path, text)

# Roadmap.
path = ROOT / "ROADMAP.md"
text = read(path)
text = replace_once(text, '**Statut M7 : actif — 5 packs validés sur 10 ; Pack 6, ComfyUI Library, suivant.**', '**Statut M7 : actif — 6 packs validés sur 10 ; Pack 7, Documentation Library, suivant.**', "roadmap status")
text = replace_once(text, '- [ ] ComfyUI Library.', '- [x] ComfyUI Library — version `1.0.0`, validation Linux `runtime-tested` avec ComfyUI CPU sans modèle.', "roadmap pack 6")
write(path, text)

# Reader order.
path = ROOT / "contents.txt"
text = read(path)
entry = 'Companion-Pack/ComfyUI-Library/README.md\n'
if entry not in text:
    text = replace_once(text, 'Companion-Pack/Database-Library/README.md\n', 'Companion-Pack/Database-Library/README.md\n' + entry, "contents pack 6")
write(path, text)

# Continuity.
path = ROOT / "CONTINUITE-PROJET.md"
text = read(path)
text = replace_once(text, 'version: "4.19.0"', 'version: "4.20.0"', "continuity version")
text = replace_once(text, 'last-updated: "2026-07-30T10:29:52+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp")
text = replace_once(text, '- progression du Companion Pack : 5 packs validés sur 10 ;', '- progression du Companion Pack : 6 packs validés sur 10 ;', "continuity progress")
text = replace_once(text, '- Database Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python `sqlite3` ;', '- Database Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python `sqlite3` ;\n- ComfyUI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec ComfyUI CPU sans modèle ;', "continuity pack 6 state")
text = replace_once(
    text,
    'M7 — Companion Pack est actif. Les Packs 1 à 5 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Database Library a validé quatre migrations ascendantes, deux repositories, quatorze tests Python, la création depuis zéro, les montées de version, la sauvegarde, la restauration et les contrôles d’intégrité avec Python `sqlite3`. Godot-SQLite, Godot, les performances, la concurrence, Windows graphique, les exports et la licence globale restent réservés.',
    f'M7 — Companion Pack est actif. Les Packs 1 à 6 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. ComfyUI Library a validé 37 fichiers, 12 tests Python, ComfyUI `v0.28.0` au commit `{COMFYUI_COMMIT}`, un démarrage CPU local et le workflow sans modèle `LoadImage → SaveImage`, avec sortie PNG et métadonnées. Les modèles, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, performances, qualité, droits de sortie, exports et licence globale restent réservés.',
    "continuity next summary",
)
text = replace_once(text, 'Companion-Pack/ComfyUI-Library/README.md', 'Companion-Pack/Documentation-Library/README.md', "continuity next path")
text = replace_once(
    text,
    'Le Pack 6 doit matérialiser une bibliothèque ComfyUI reproductible : workflows JSON, manifestes YAML, listes de custom nodes, presets, scripts de lancement, modèles de dossiers, fiches de provenance, images légères de validation et checksums. Aucun modèle non redistribuable ne devra être inclus ; chaque dépendance, seed, paramètre, profil matériel, exécution et licence devra être qualifié sans inventer de résultat.',
    'Le Pack 7 doit matérialiser une bibliothèque documentaire normalisée : templates de chapitre, front matter, rapports QA, preuves YAML, ADR, checklists, fiches outils/modèles/assets, glossaires et scripts de génération. Les templates devront être compilables, porter des identifiants conformes, inclure les repères d’utilisation, fournir des exemples remplis et documenter leur personnalisation sans dupliquer les documents propriétaires.',
    "continuity next scope",
)
journal = f'''### {TIMESTAMP} — version 4.20.0

- matérialisation du Companion Pack, Pack 6 — ComfyUI Library ;
- 37 fichiers du Pack, deux workflows, trois profils, manifestes, provenance, scripts, image SVG et checksums créés ;
- 12 tests Python réussis ;
- ComfyUI `v0.28.0` au commit `{COMFYUI_COMMIT}`, Python `{PYTHON_VERSION}` et Torch `{TORCH_VERSION}` qualifiés sur Ubuntu 24.04 ;
- workflow `WF-COMFY-0001` exécuté en CPU sur `127.0.0.1` sans modèle ni custom node tiers ;
- base SQLite interne créée explicitement dans le workspace runtime ;
- sortie PNG de {OUTPUT_SIZE} octets avec métadonnées `prompt` et `workflow`, SHA-256 `{OUTPUT_SHA256}` ;
- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- arbre Git propre et validations documentaires légères exécutées sans PDF ;
- progression M7 portée à 6 packs sur 10 ;
- prochaine action : `Companion-Pack/Documentation-Library/README.md`, niveau Élevée ;
- aucun modèle réel, text-to-image, custom node tiers, AMD/ZLUDA, Windows graphique, performance, qualité, droit de sortie, export, release, licence globale, donnée personnelle ou secret validé ou produit.

'''
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, "continuity journal")
write(path, text)

# Final assertions.
assert (PACK / "VERSION").read_text(encoding="utf-8").strip() == "1.0.0"
assert 'validation-status: "runtime-tested-linux"' in read(PACK / "README.md")
assert load_json(PACK / "qa/VALIDATION-COMFYUI-LIBRARY.yaml")["status"] == "complete"
assert "6 packs validés sur 10" in read(ROOT / "ROADMAP.md")
assert "Companion-Pack/Documentation-Library/README.md" in read(ROOT / "CONTINUITE-PROJET.md")
assert entry.strip() in read(ROOT / "contents.txt")
print(f"ComfyUI Library Pack 6 finalized at {TIMESTAMP}.")
