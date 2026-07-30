#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "Companion-Pack/Documentation-Library"
TIMESTAMP = "2026-07-30T12:34:03+02:00"
QUALIFICATION_RUN = 30535138371
ARTIFACT_ID = 8756322426
ARTIFACT_DIGEST = "sha256:7d17cbbc5897f74130ef20420c33d5f68a9d483381027b549b2f558e14806933"
FINALIZER_RUN = int(os.environ.get("GITHUB_RUN_ID", "0"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


readme = f'''---
title: "Companion Pack — Documentation Library"
id: "CP-PACK-07-DOCUMENTATION-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{TIMESTAMP}"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Documentation Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 7 fournit des patrons documentaires normalisés, des exemples fictifs remplis, des schémas et des scripts déterministes pour créer, contrôler et compiler de nouveaux documents sans dupliquer les chapitres propriétaires.

## État qualifié

| Élément | État |
|---|---|
| patrons documentaires | 13 validés |
| exemples remplis | 10 régénérés octet pour octet |
| schémas documentaires | 3 matérialisés |
| tests Python | 18 réussis |
| compilation Pandoc HTML | 9 documents réussis |
| preuve YAML générée | analysée avec PyYAML |
| validations transversales | réussies sans PDF |
| licence globale | non décidée |

## Utilisation minimale

> **[PS] PowerShell — Exécuter depuis la racine du dépôt :**

```powershell
python .\\Companion-Pack\\Documentation-Library\\scripts\\generate_document.py `
  --root .\\Companion-Pack\\Documentation-Library `
  --template templates\\chapters\\tutorial.md `
  --data examples\\data\\chapter.json `
  --output dist\\CHAPITRE-99.md
```

Le générateur refuse les tokens manquants, les valeurs inutilisées et les placeholders restants.

## Validation locale

```powershell
python .\\Companion-Pack\\Documentation-Library\\scripts\\validate_documentation_library.py

python -m unittest discover `
  -s .\\Companion-Pack\\Documentation-Library\\tests `
  -v
```

## Compilation de contrôle

```powershell
pandoc .\\dist\\CHAPITRE-99.md --from markdown --to html --standalone `
  --output .\\dist\\CHAPITRE-99.html
```

Cette compilation vérifie la portabilité structurelle. Elle ne constitue pas une inspection visuelle ou d’accessibilité.

## Qualification obtenue

Le run `{QUALIFICATION_RUN}` a validé 57 fichiers du Pack, 13 patrons, 10 exemples remplis et 18 tests Python. Les dix exemples ont été régénérés octet pour octet ; les neuf documents Markdown ont été compilés vers HTML et la preuve YAML a été analysée.

Environnement : Ubuntu 24.04, CPython `3.12.13`, PyYAML `6.0.3` et Pandoc `3.1.3`. Artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}`.

L’arbre Git est resté propre. Aucun PDF, DOCX ou EPUB n’a été produit.

## Frontières

Le Volume 0 demeure normatif. Les Livres demeurent propriétaires de leurs explications. Le Pack ne modifie aucun index ni `contents.txt` automatiquement et ne transforme jamais un exemple rempli en preuve d’un document réel.

## Réserves

La qualification ne valide aucun rendu visuel, contrôle d’accessibilité, PDF, DOCX, EPUB, publication, licence globale ou redistribution autonome.
'''
write(PACK / "README.md", readme)

manifest = json.loads(read(PACK / "manifest.json"))
manifest["status"] = "reviewed"
write(PACK / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

provenance = json.loads(read(PACK / "PROVENANCE.json"))
provenance["qualification"] = f"runtime-tested-linux-run-{QUALIFICATION_RUN}"
write(PACK / "PROVENANCE.json", json.dumps(provenance, ensure_ascii=False, indent=2))

audit = f'''---
title: "Audit — Documentation Library"
id: "CP-AUDIT-PACK-07"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "{TIMESTAMP}"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Décision

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 7 est accepté dans son périmètre Linux x86_64 pour la génération et la compilation documentaire textuelle.

## Périmètre comparé au plan maître

Le lot matérialise les templates de chapitre, front matter, rapports QA, preuves YAML, ADR, checklists, fiches outil/modèle/asset, glossaire et scripts de génération prévus. Il conserve le Volume 0 comme source normative et ne copie aucun chapitre propriétaire.

## Preuves runtime

- workflow permanent : `Validate Documentation Library` ;
- run : `{QUALIFICATION_RUN}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}` ;
- Ubuntu 24.04, Python `3.12.13`, PyYAML `6.0.3`, Pandoc `3.1.3` ;
- 57 fichiers du Pack validés ;
- 13 patrons et 13 entrées de catalogue ;
- 10 exemples remplis régénérés octet pour octet ;
- 18 tests Python réussis ;
- 9 documents Markdown compilés en HTML ;
- 1 preuve YAML analysée ;
- validations documentaires transversales réussies ;
- arbre Git propre ;
- aucun PDF, DOCX ou EPUB produit.

## Contrôle anti-doublon

- le Volume 0 reste propriétaire des règles ;
- les Livres restent propriétaires de leurs explications ;
- le Livre V reste propriétaire des fiches de référence publiées ;
- le Pack ne fournit que des structures abstraites et des exemples fictifs ;
- le générateur ne modifie aucune gouvernance automatiquement.

## Réserves

Aucun rendu visuel, contrôle d’accessibilité, PDF, DOCX, EPUB, publication, licence globale ou redistribution autonome n’est validé.
'''
write(PACK / "qa/AUDIT-DOCUMENTATION-LIBRARY.md", audit)

proof = {
    "schema-version": 1,
    "evidence-id": "QA-DOCUMENTATION-LIBRARY-PACK-07",
    "status": "complete",
    "validation-date": "2026-07-30",
    "source-branch": "feat/companion-pack-documentation-library",
    "pack": {
        "id": "CP-PACK-07-DOCUMENTATION-LIBRARY",
        "version": "1.0.0",
        "audit-level": "runtime-tested-linux",
    },
    "environment": {
        "os": "ubuntu-24.04",
        "python": "3.12.13",
        "pyyaml": "6.0.3",
        "pandoc": "3.1.3",
    },
    "results": {
        "source-files": 57,
        "templates": 13,
        "catalog-entries": 13,
        "filled-examples": 10,
        "python-tests": {"status": "success", "count": 18},
        "deterministic-generation": {"status": "success", "count": 10},
        "pandoc-html-compilation": {"status": "success", "count": 9},
        "yaml-proofs-parsed": 1,
        "clean-tree": True,
        "pdf-produced": False,
        "docx-produced": False,
        "epub-produced": False,
    },
    "ci": {
        "workflow": "Validate Documentation Library",
        "run-id": QUALIFICATION_RUN,
        "artifact-id": ARTIFACT_ID,
        "artifact-digest": ARTIFACT_DIGEST,
        "governance-finalizer-run": FINALIZER_RUN,
    },
    "reservations": [
        "No visual or accessibility inspection.",
        "No PDF, DOCX or EPUB output.",
        "No publication or autonomous redistribution.",
        "Global license undefined.",
    ],
}
import yaml
write(PACK / "qa/VALIDATION-DOCUMENTATION-LIBRARY.yaml", yaml.safe_dump(proof, sort_keys=False, allow_unicode=True))

# Companion Pack index.
path = ROOT / "Companion-Pack/index.md"
text = read(path)
text = replace_once(text, 'version: "0.7.0"', 'version: "0.8.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-30T11:20:49+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(text, '7. [ ] Documentation Library ;', '7. [x] [Documentation Library](Documentation-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec génération déterministe et Pandoc HTML ;', "index pack 7")
text = replace_once(
    text,
    'Progression : **6 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library, Database Library et ComfyUI Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 7 — Documentation Library.',
    'Progression : **7 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library, Database Library, ComfyUI Library et Documentation Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, Forward+ GPU, rendus documentaires visuels, accessibilité, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 8 — Test & Benchmark Library.',
    "index status",
)
write(path, text)

# Roadmap.
path = ROOT / "ROADMAP.md"
text = read(path)
text = replace_once(text, '**Statut M7 : actif — 6 packs validés sur 10 ; Pack 7, Documentation Library, suivant.**', '**Statut M7 : actif — 7 packs validés sur 10 ; Pack 8, Test & Benchmark Library, suivant.**', "roadmap status")
text = replace_once(text, '- [ ] Documentation Library.', '- [x] Documentation Library — version `1.0.0`, validation Linux `runtime-tested` avec génération déterministe et compilation Pandoc HTML.', "roadmap pack 7")
write(path, text)

# Reader order.
path = ROOT / "contents.txt"
text = read(path)
text = replace_once(text, 'Companion-Pack/ComfyUI-Library/README.md\n', 'Companion-Pack/ComfyUI-Library/README.md\nCompanion-Pack/Documentation-Library/README.md\n', "contents pack 7")
write(path, text)

# Master plan.
path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
text = read(path)
text = replace_once(text, 'version: "1.6.0"', 'version: "1.7.0"', "plan version")
text = replace_once(text, '> **Statut :** en cours — Pack 6 sur 10 validé', '> **Statut :** en cours — Pack 7 sur 10 validé', "plan status")
text = replace_once(text, '## Pack 7 — Documentation Library\n\n**Objectifs**', f'## Pack 7 — Documentation Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `{QUALIFICATION_RUN}` avec génération déterministe, PyYAML et compilation Pandoc HTML ; réserves rendu visuel, accessibilité, PDF, DOCX, EPUB, publication et licence globale maintenues.\n\n**Objectifs**', "plan pack 7 state")
write(path, text)

# Continuity.
path = ROOT / "CONTINUITE-PROJET.md"
text = read(path)
text = replace_once(text, 'version: "4.20.0"', 'version: "4.21.0"', "continuity version")
text = replace_once(text, 'last-updated: "2026-07-30T11:20:49+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp")
text = replace_once(text, '- progression du Companion Pack : 6 packs validés sur 10 ;', '- progression du Companion Pack : 7 packs validés sur 10 ;', "continuity progress")
text = replace_once(text, '- ComfyUI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec ComfyUI CPU sans modèle ;', '- ComfyUI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec ComfyUI CPU sans modèle ;\n- Documentation Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec génération déterministe, PyYAML et Pandoc HTML ;', "continuity pack 7 state")
text = replace_once(
    text,
    'M7 — Companion Pack est actif. Les Packs 1 à 6 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. ComfyUI Library a validé 37 fichiers, 12 tests Python, ComfyUI `v0.28.0` au commit `700821e1364eaab0e8f21c538a2131719fec57bf`, un démarrage CPU local et le workflow sans modèle `LoadImage → SaveImage`, avec sortie PNG et métadonnées. Les modèles, custom nodes tiers, profils AMD/ZLUDA, Windows graphique, performances, qualité, droits de sortie, exports et licence globale restent réservés.',
    f'M7 — Companion Pack est actif. Les Packs 1 à 7 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Documentation Library a validé 57 fichiers, 13 patrons, 10 exemples remplis, 18 tests Python, une régénération déterministe de dix documents, neuf compilations Pandoc HTML et une preuve YAML avec PyYAML. Les rendus visuels, l’accessibilité, PDF, DOCX, EPUB, publication, exports et licence globale restent réservés.',
    "continuity next summary",
)
text = replace_once(text, '```text\nCompanion-Pack/Documentation-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```', '```text\nCompanion-Pack/Test-Benchmark-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```', "continuity next path")
text = replace_once(
    text,
    'Le Pack 7 doit matérialiser une bibliothèque documentaire normalisée : templates de chapitre, front matter, rapports QA, preuves YAML, ADR, checklists, fiches outils/modèles/assets, glossaires et scripts de génération. Les templates devront être compilables, porter des identifiants conformes, inclure les repères d’utilisation, fournir des exemples remplis et documenter leur personnalisation sans dupliquer les documents propriétaires.',
    'Le Pack 8 doit matérialiser une bibliothèque de tests et benchmarks : tests GDScript, tests Python, scènes de benchmark CPU/GPU/mémoire, corpus IA, fixtures de base, scripts de lancement, formats CSV/JSON/YAML et modèles de rapports. Les tests devront rester exécutables séparément ; chaque résultat devra être horodaté, lié au matériel, documenter répétitions et variance, et exclure toute donnée non redistribuable.',
    "continuity next scope",
)
journal = f'''### {TIMESTAMP} — version 4.21.0

- matérialisation du Companion Pack, Pack 7 — Documentation Library ;
- 57 fichiers du Pack, 13 patrons, 13 entrées de catalogue, trois schémas, dix profils et dix exemples remplis créés ;
- générateur déterministe, validateur statique et 18 tests Python créés et réussis ;
- dix exemples régénérés octet pour octet ;
- neuf documents Markdown compilés vers HTML et une preuve YAML analysée ;
- Ubuntu 24.04, Python `3.12.13`, PyYAML `6.0.3` et Pandoc `3.1.3` qualifiés ;
- run `{QUALIFICATION_RUN}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- validations documentaires transversales réussies, arbre Git propre et aucun PDF, DOCX ou EPUB produit ;
- progression M7 portée à 7 packs sur 10 ;
- prochaine action : `Companion-Pack/Test-Benchmark-Library/README.md`, niveau Élevée ;
- aucun rendu visuel, contrôle d’accessibilité, PDF, DOCX, EPUB, publication, export, release, licence globale, donnée personnelle ou secret validé ou produit.

'''
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, "continuity journal")
write(path, text)

print(json.dumps({
    "status": "success",
    "qualification_run": QUALIFICATION_RUN,
    "artifact_id": ARTIFACT_ID,
    "finalizer_run": FINALIZER_RUN,
    "timestamp": TIMESTAMP,
}, ensure_ascii=False))
