from __future__ import annotations

import json
import re
from pathlib import Path

TS = "2026-07-30T05:34:00+02:00"
DATE = "2026-07-30"
RUN_ID = 30511425269
HEAD = "488697292d3dd82804c80d6bbc56629b45cb6a79"
ARTIFACT_ID = 8747249256
ARTIFACT_DIGEST = "sha256:a285b4880527d0aa36bfe1f1ed67d3e950b4668601709ce5aadb04e73bd04473"
GODOT_VERSION = "4.7.1.stable.official.a13da4feb"
GODOT_ZIP_SHA256 = "c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba"
SOLO_PROJECT_SHA = "61f2286f90dbaad1375ac201eeecfff85f65eecd25967799a126e6d1cdbe2896"
STUDIO_PROJECT_SHA = "43d49d1e9b06a16f2f822217111a7d1ca49a759b7390a2f7b86adfe604dd4f57"
SOLO_MODULE_SHA = "0662f720c8880a4726fb5139ca247f692ae7b283620d32a6f46c2ac6975d471a"
STUDIO_MODULE_SHA = "6a48c5014cfffdbe8645a5959294ae90d408e6f81fba4584afa2e86da5328cf7"

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/Project-Templates"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, got {count}: {old!r}")
    return text.replace(old, new, 1)


def update_json(path: Path, callback) -> None:
    data = json.loads(read(path))
    callback(data)
    write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


readme_path = PACK / "README.md"
readme = read(readme_path)
readme = replace_once(readme, 'status: "candidate"', 'status: "reviewed"', "README status")
readme = replace_once(readme, 'version: "0.1.0"', 'version: "1.0.0"', "README version")
readme = re.sub(r'last-verified: "[^"]+"', f'last-verified: "{TS}"', readme, count=1)
readme = replace_once(
    readme,
    'validation-status: "pending-runtime"',
    'validation-status: "runtime-tested-linux"',
    "README validation status",
)
readme = replace_once(
    readme,
    "| création de projets neufs | en attente de la preuve CI |",
    f"| création de projets neufs | validée par le run `{RUN_ID}` |",
    "README fresh projects",
)
readme = replace_once(
    readme,
    "| import et tests Godot | en attente de la preuve CI |",
    f"| import et tests Godot | validés sur Linux x86_64 par le run `{RUN_ID}` |",
    "README runtime",
)
anchor = (
    "Les fichiers de gouvernance sont des **modèles de départ**. Leur présence ne prouve ni une protection de branche active, "
    "ni une revue obligatoire, ni l’application d’un CODEOWNERS par GitHub."
)
qualification = f"""{anchor}

## Qualification obtenue

Le run `{RUN_ID}` a instancié les profils Solo et Studio, créé un module en cinq couches dans chacun, initialisé leurs dépôts Git, importé les deux projets avec Godot `{GODOT_VERSION}`, exécuté les démarrages headless et Xvfb Compatibility, puis obtenu `PROJECT_TEMPLATE_TESTS: PASS` pour les deux profils. Les arbres Git sont restés propres après runtime.

La génération statique est déterministe pour des entrées identiques :

- projet Solo : `{SOLO_PROJECT_SHA}` ;
- projet Studio : `{STUDIO_PROJECT_SHA}` ;
- module Solo : `{SOLO_MODULE_SHA}` ;
- module Studio : `{STUDIO_MODULE_SHA}`.

Cette qualification ne rend pas les politiques GitHub effectives et ne constitue pas une revue visuelle du rendu Xvfb.
"""
readme = replace_once(readme, anchor, qualification.rstrip(), "README qualification")
write(readme_path, readme)

write(PACK / "VERSION", "1.0.0\n")
changelog_path = PACK / "CHANGELOG.md"
changelog = read(changelog_path)
if "## 1.0.0" not in changelog:
    changelog = replace_once(
        changelog,
        "# Journal des versions\n\n",
        f"""# Journal des versions

## 1.0.0 — {DATE}

- profils Solo et Studio instanciés dans des dossiers neufs ;
- enveloppe PowerShell validée ;
- génération déterministe confirmée pour chaque profil ;
- module en cinq couches créé et testé dans les deux projets ;
- Godot `{GODOT_VERSION}` téléchargé depuis le point d’entrée officiel ;
- imports, démarrages headless et lancements Xvfb Compatibility réussis ;
- tests GDScript réussis avec `PROJECT_TEMPLATE_TESTS: PASS` ;
- dépôts Git générés restés propres après runtime ;
- réserves protection de branche, CODEOWNERS effectif, Windows graphique, Forward+ GPU, exports et licence globale maintenues.

""",
        "CHANGELOG insertion",
    )
write(changelog_path, changelog)

update_json(PACK / "manifest.json", lambda data: data.update({"version": "1.0.0"}))
update_json(PACK / "PROVENANCE.json", lambda data: data.update({"version": "1.0.0"}))


def qualify_dependencies(data: dict) -> None:
    for item in data.get("runtime", []):
        if item.get("name") == "Godot Engine":
            item["qualification"] = {
                "platform": "linux-x86_64",
                "engine_version": GODOT_VERSION,
                "archive_sha256": GODOT_ZIP_SHA256,
                "run_id": RUN_ID,
                "status": "pass",
            }
    for item in data.get("tooling", []):
        if item.get("name") == "Python":
            item["qualification"] = {"run_id": RUN_ID, "status": "pass", "third_party_packages": []}
        elif item.get("name") == "PowerShell":
            item["qualification"] = {"run_id": RUN_ID, "status": "pass-linux-runner"}
        elif item.get("name") == "Git":
            item["qualification"] = {"run_id": RUN_ID, "status": "pass-generated-repositories"}


update_json(PACK / "DEPENDENCIES.json", qualify_dependencies)

audit_path = PACK / "qa/AUDIT-PROJECT-TEMPLATES.md"
audit = read(audit_path)
audit = replace_once(audit, 'status: "candidate"', 'status: "complete"', "audit status")
audit = replace_once(audit, 'version: "0.1.0"', 'version: "1.0.0"', "audit version")
audit = re.sub(r'last-verified: "[^"]+"', f'last-verified: "{TS}"', audit, count=1)
audit = re.sub(r'audit-date: "[^"]+"', f'audit-date: "{TS}"', audit, count=1)
audit = replace_once(audit, 'audit-level: "static-review"', 'audit-level: "runtime-tested"', "audit level")
audit = replace_once(audit, "## Décision candidate", "## Décision", "audit decision heading")
audit = replace_once(
    audit,
    "La décision finale reste suspendue à l’exécution CI avec Godot `4.7.1-stable`.",
    f"Le pack est accepté au niveau `runtime-tested` pour Linux x86_64. Le run `{RUN_ID}` a validé la génération, les deux imports, les deux démarrages headless, les deux démarrages Xvfb Compatibility, les deux suites GDScript et les arbres Git propres.",
    "audit decision",
)
if "## Résultats runtime" not in audit:
    audit += f"""

## Résultats runtime

- Godot : `{GODOT_VERSION}` ;
- archive Linux SHA-256 : `{GODOT_ZIP_SHA256}` ;
- profil Solo : import, bootstrap, Xvfb et tests réussis ;
- profil Studio : import, bootstrap, Xvfb et tests réussis ;
- module généré `inventory_demo` chargé et testé dans les deux profils ;
- arbres Git propres après import et tests ;
- run : `{RUN_ID}` ;
- commit qualifié : `{HEAD}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}`.

## Réserves maintenues

- les avertissements Xvfb relatifs à V-Sync et à l’absence de périphérique audio sur le runner ne constituent pas une revue de qualité visuelle ou audio ;
- aucune protection de branche n’est appliquée à un dépôt cible ;
- l’efficacité de CODEOWNERS n’est pas vérifiée sur un dépôt cible ;
- Windows graphique et Forward+ sur GPU réel ne sont pas exécutés ;
- aucun export, paquet de release ou licence globale n’est produit ou décidé.
"""
write(audit_path, audit)

proof = f"""schema-version: 1
evidence-id: CP-QA-PACK-02
status: complete
validation-date: '{DATE}'
source-branch: feat/companion-pack-project-templates
pack:
  id: CP-PACK-02-PROJECT-TEMPLATES
  version: 1.0.0
  entry-point: Companion-Pack/Project-Templates/README.md
  audit-level: runtime-tested
results:
  static-validation: success
  source-files: 71
  powershell-wrapper: success
  solo-instantiation: success
  studio-instantiation: success
  module-generation: success
  deterministic-generation:
    status: success
    solo-project-sha256: {SOLO_PROJECT_SHA}
    studio-project-sha256: {STUDIO_PROJECT_SHA}
    solo-module-sha256: {SOLO_MODULE_SHA}
    studio-module-sha256: {STUDIO_MODULE_SHA}
  godot-version: {GODOT_VERSION}
  godot-archive-sha256: {GODOT_ZIP_SHA256}
  solo-import: success
  studio-import: success
  solo-headless-smoke: success
  studio-headless-smoke: success
  solo-virtual-graphical-smoke:
    status: success
    display: Xvfb
    renderer: gl_compatibility
  studio-virtual-graphical-smoke:
    status: success
    display: Xvfb
    renderer: gl_compatibility
  solo-gdscript-tests: success
  studio-gdscript-tests: success
  generated-module-tests: success
  clean-tree-after-runtime: true
  runtime-tests: 8
ci:
  qualification-run:
    workflow: Validate Project Templates
    run-id: {RUN_ID}
    head-commit: {HEAD}
    conclusion: success
    artifact-id: {ARTIFACT_ID}
    artifact-digest: {ARTIFACT_DIGEST}
reservations:
  - Branch protection is not applied to a target repository.
  - CODEOWNERS effectiveness is not verified on a target repository.
  - Xvfb execution is not a visual-quality review.
  - Windows graphical execution is not executed.
  - Forward+ rendering on a real GPU is not executed.
  - Exports and release packages are not produced.
  - The global license is undefined.
"""
write(PACK / "qa/VALIDATION-PROJECT-TEMPLATES.yaml", proof)

index_path = ROOT / "Companion-Pack/index.md"
index = read(index_path)
index = replace_once(index, 'version: "0.2.0"', 'version: "0.3.0"', "index version")
index = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{TS}"', index, count=1)
index = replace_once(
    index,
    "2. [ ] Project Templates ;",
    "2. [x] [Project Templates](Project-Templates/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;",
    "index Pack 2",
)
index = replace_once(
    index,
    "Progression : **1 pack sur 10**. Le Starter Kit est matérialisé et validé dans son périmètre Linux. Les réserves Windows graphique, Forward+ GPU, exports et licence globale restent ouvertes. La prochaine action est le Pack 2 — Project Templates.",
    "Progression : **2 packs sur 10**. Le Starter Kit et Project Templates sont matérialisés et validés dans leur périmètre Linux. Les réserves Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 3 — AI Library.",
    "index status",
)
write(index_path, index)

plan_path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
plan = read(plan_path)
plan = replace_once(plan, 'version: "1.1.0"', 'version: "1.2.0"', "plan version")
plan = replace_once(plan, "> **Statut :** en cours — Pack 1 sur 10 validé", "> **Statut :** en cours — Pack 2 sur 10 validé", "plan status")
pack2_heading = "## Pack 2 — Project Templates\n\n"
pack2_state = f"**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `{RUN_ID}` ; réserves protections GitHub effectives, Windows graphique, Forward+ GPU, exports et licence globale maintenues.\n\n"
plan = replace_once(plan, pack2_heading, pack2_heading + pack2_state, "plan Pack 2 state")
write(plan_path, plan)

roadmap_path = ROOT / "ROADMAP.md"
roadmap = read(roadmap_path)
roadmap = replace_once(
    roadmap,
    "**Statut M7 : actif — 1 pack validé sur 10 ; Pack 2, Project Templates, suivant.**",
    "**Statut M7 : actif — 2 packs validés sur 10 ; Pack 3, AI Library, suivant.**",
    "roadmap status",
)
roadmap = replace_once(
    roadmap,
    "- [ ] Project Templates.",
    "- [x] Project Templates — version `1.0.0`, validation Linux `runtime-tested`.",
    "roadmap Pack 2",
)
write(roadmap_path, roadmap)

contents_path = ROOT / "contents.txt"
contents = read(contents_path)
entry = "Companion-Pack/Project-Templates/README.md"
if entry not in contents.splitlines():
    starter_entry = "Companion-Pack/Starter-Kit/README.md"
    contents = replace_once(contents, starter_entry, starter_entry + "\n" + entry, "contents Pack 2")
write(contents_path, contents)

continuity_path = ROOT / "CONTINUITE-PROJET.md"
continuity = read(continuity_path)
continuity = replace_once(continuity, 'version: "4.15.0"', 'version: "4.16.0"', "continuity version")
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{TS}"', continuity, count=1)
continuity = replace_once(
    continuity,
    "- progression du Companion Pack : 1 pack validé sur 10 ;",
    "- progression du Companion Pack : 2 packs validés sur 10 ;",
    "continuity progress",
)
continuity = replace_once(
    continuity,
    "- Starter Kit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;",
    "- Starter Kit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;\n- Project Templates : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;",
    "continuity pack state",
)
next_section = f"""## 26. Prochaine action

M7 — Companion Pack est actif. Les Packs 1 et 2 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Project Templates a généré des projets Solo et Studio, ajouté un module en cinq couches, importé les deux projets, exécuté les démarrages headless et Xvfb Compatibility, passé les tests GDScript et conservé des arbres Git propres. Les protections GitHub effectives, Windows graphique, Forward+ GPU, exports et licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/AI-Library/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 3 doit matérialiser une couche IA locale remplaçable : contrats OpenAI-compatible, clients HTTP et WebSocket, adaptateurs Ollama, llama.cpp et LocalAI, délais, reprises bornées, annulation, files, cache, mocks, filtres de sécurité et exemples Godot. Aucun service réel, secret, disponibilité fournisseur, performance ou compatibilité réseau ne devra être annoncé sans exécution et preuve.
"""
continuity = re.sub(
    r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)",
    next_section,
    continuity,
    count=1,
    flags=re.DOTALL,
)
journal_entry = f"""### {TS} — version 4.16.0

- matérialisation du Companion Pack, Pack 2 — Project Templates ;
- modèles Solo et Studio, générateur Python, enveloppe PowerShell, module en cinq couches, ADR, conventions Git, issues, PR, VS Code, style et CODEOWNERS Studio créés ;
- 71 sources textuelles du pack validées sans dépendance Python tierce ni fichier binaire ;
- générations Solo et Studio déterministes pour des entrées identiques ;
- projets neufs et modules `inventory_demo` créés, importés et testés ;
- Godot `{GODOT_VERSION}`, archive SHA-256 `{GODOT_ZIP_SHA256}` ;
- démarrages headless et Xvfb Compatibility réussis pour les deux profils ;
- tests GDScript réussis avec `PROJECT_TEMPLATE_TESTS: PASS` ;
- arbres Git générés propres après runtime ;
- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- progression M7 portée à 2 packs sur 10 ;
- prochaine action : `Companion-Pack/AI-Library/README.md`, niveau Élevée ;
- aucune protection de branche, efficacité CODEOWNERS, Windows graphique, Forward+ GPU réel, export, release, licence globale, donnée personnelle ou secret validé ou produit.

"""
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal_entry, "continuity journal")
write(continuity_path, continuity)

assert read(PACK / "VERSION").strip() == "1.0.0"
assert "Companion-Pack/AI-Library/README.md" in read(continuity_path)
assert entry in read(contents_path)
assert "2 packs validés sur 10" in read(roadmap_path)
assert "status: complete" in read(PACK / "qa/AUDIT-PROJECT-TEMPLATES.md")

print("Project Templates Pack 2 finalized.")
