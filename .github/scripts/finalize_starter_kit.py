from __future__ import annotations

import json
import subprocess
from pathlib import Path

TS = "2026-07-30T04:19:00+02:00"
DATE = "2026-07-30"
RUN_ID = 30508086899
HEAD = "f310701c9ad41f0ca9a75a66a80fb75b089def03"
ARTIFACT_ID = 8746081670
ARTIFACT_DIGEST = "sha256:5429fcc7001d4a28d7475908d8660e859b4aafd86b4febd42629b66e5310e2ed"
GODOT_VERSION = "4.7.1.stable.official.a13da4feb"
GODOT_ZIP_SHA256 = "c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba"

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/Starter-Kit"
if 'status: "reviewed"' in (PACK / "README.md").read_text(encoding="utf-8"):
    print("Starter Kit already finalized.")
    raise SystemExit(0)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"Expected one {label}, found {text.count(old)}")
    return text.replace(old, new, 1)


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")

p = PACK / "README.md"
s = p.read_text(encoding="utf-8")
s = replace_once(s, 'status: "candidate"', 'status: "reviewed"', "README status")
s = replace_once(s, 'version: "0.1.0"', 'version: "1.0.0"', "README version")
s = replace_once(s, 'last-verified: "2026-07-30T03:39:00+02:00"', f'last-verified: "{TS}"', "README timestamp")
s = replace_once(s, 'validation-status: "pending-runtime"', 'validation-status: "runtime-tested-linux"', "README validation")
s = replace_once(s, '| exécution Linux headless | en attente de la preuve CI |', f'| exécution Linux headless | validée par le run `{RUN_ID}` |', "README headless row")
s = replace_once(s, '| clone neuf indépendant | non exécuté |', f'| clone neuf indépendant | validé par le run `{RUN_ID}` |', "README clone row")
s = replace_once(s, '| ouverture Windows graphique | non exécutée |', '| lancement graphique virtuel Linux | validé sous Xvfb avec Compatibility |\n| ouverture Windows graphique | non exécutée |', "README graphical row")
s = replace_once(s, 'Le processus retourne `0` et affiche `STARTER_KIT_TESTS: PASS` lorsque les invariants minimaux sont respectés.', f'Le run `{RUN_ID}` a retourné `0` et affiché `STARTER_KIT_TESTS: PASS`. Cette preuve couvre Godot Linux x86_64 en mode Compatibility, pas Forward+ sur GPU réel.', "README test result")
write(p, s)
write(PACK / "VERSION", "1.0.0\n")

p = PACK / "manifest.json"
data = json.loads(p.read_text(encoding="utf-8"))
data["version"] = "1.0.0"
data["validation_status"] = "runtime-tested-linux"
data["validation_evidence"] = "qa/VALIDATION-STARTER-KIT.yaml"
write(p, json.dumps(data, ensure_ascii=False, indent=2) + "\n")

p = PACK / "DEPENDENCIES.json"
data = json.loads(p.read_text(encoding="utf-8"))
data["pack_version"] = "1.0.0"
for dep in data["dependencies"]:
    if dep["id"] == "godot-engine":
        dep["qualification"]["linux_x86_64_headless"] = f"pass-run-{RUN_ID}"
        dep["qualification"]["linux_x86_64_virtual_graphical_compatibility"] = f"pass-run-{RUN_ID}"
    elif dep["id"] in {"python", "powershell"}:
        dep["qualification"]["linux_x86_64"] = f"pass-run-{RUN_ID}"
write(p, json.dumps(data, ensure_ascii=False, indent=2) + "\n")

p = PACK / "PROVENANCE.json"
data = json.loads(p.read_text(encoding="utf-8"))
data["version"] = "1.0.0"
data["validated_at"] = TS
write(p, json.dumps(data, ensure_ascii=False, indent=2) + "\n")

p = PACK / "godot-project/docs/environment/godot-reference.json"
data = json.loads(p.read_text(encoding="utf-8"))
data["verified"] = DATE
data["qualification"]["linux_headless"] = f"pass-run-{RUN_ID}"
data["qualification"]["linux_virtual_graphical_compatibility"] = f"pass-run-{RUN_ID}"
data["qualification"]["fresh_clone_linux"] = f"pass-run-{RUN_ID}"
write(p, json.dumps(data, ensure_ascii=False, indent=2) + "\n")

p = PACK / "CHANGELOG.md"
s = p.read_text(encoding="utf-8")
entry = f"""# Changelog — Starter Kit

## 1.0.0 — {DATE}

- validation statique Python et enveloppe PowerShell réussies ;
- Godot `{GODOT_VERSION}` téléchargé depuis le point d’entrée officiel ;
- import et démarrage headless réussis ;
- démarrage graphique virtuel Xvfb réussi avec le moteur Compatibility ;
- tests GDScript réussis ;
- clone Git neuf validé et arbre propre après import ;
- UID Godot générés puis versionnés ;
- réserves Windows graphique, Forward+ GPU, exports et licence globale maintenues.

## 0.1.0 — {DATE}
"""
s = replace_once(s, f"# Changelog — Starter Kit\n\n## 0.1.0 — {DATE}\n", entry, "changelog heading")
write(p, s)

write(PACK / "qa/AUDIT-STARTER-KIT.md", f'''---
title: "Audit — Companion Pack, Starter Kit"
id: "CP-QA-PACK-01-AUDIT"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{TS}"
audit-date: "{TS}"
audit-level: "runtime-tested"
target: "Companion-Pack/Starter-Kit"
---

# Audit du Starter Kit

## Décision

Le Starter Kit est accepté en version `1.0.0` au niveau `runtime-tested` pour le périmètre Linux x86_64 de la campagne CI. Le projet s’importe, démarre en headless, démarre sous affichage virtuel Xvfb avec le moteur Compatibility, exécute ses tests GDScript et se reproduit depuis un clone Git neuf.

## Preuves exécutées

- validateur Python sans paquet tiers : réussi ;
- enveloppe PowerShell : réussie ;
- Godot `{GODOT_VERSION}` : version vérifiée ;
- archive Godot SHA-256 `{GODOT_ZIP_SHA256}` ;
- import Linux headless : réussi ;
- démarrage headless borné : réussi ;
- démarrage graphique virtuel Xvfb avec Compatibility : réussi ;
- `BootstrapReport` valide et identifiant `CP-SK-BOOTSTRAP-001` observé ;
- tests GDScript : `STARTER_KIT_TESTS: PASS` ;
- clone Git neuf : validation statique, import et tests réussis ;
- arbre Git : propre après import, grâce aux UID versionnés et aux caches ignorés.

## Traçabilité

- workflow : `Validate Starter Kit` ;
- run : `{RUN_ID}` ;
- commit : `{HEAD}` ;
- artefact : `{ARTIFACT_ID}` ;
- digest : `{ARTIFACT_DIGEST}`.

## Réserves

- Windows graphique n’a pas été exécuté ;
- Forward+ sur GPU réel n’a pas été exécuté ;
- le lancement Xvfb utilise Compatibility et ne constitue pas une validation visuelle ;
- aucun preset d’export, paquet ou test d’installation n’est produit ;
- aucune restauration ou migration n’est exercée ;
- la licence globale reste indécise et bloque la redistribution autonome.
''')

write(PACK / "qa/VALIDATION-STARTER-KIT.yaml", f'''schema-version: 1
evidence-id: CP-QA-PACK-01
status: complete
validation-date: '{DATE}'
source-branch: feat/companion-pack-starter-kit
pack:
  id: CP-PACK-01-STARTER-KIT
  version: 1.0.0
  entry-point: Companion-Pack/Starter-Kit/README.md
  audit-level: runtime-tested
results:
  static-validation: success
  powershell-wrapper: success
  godot-download: success
  godot-version: {GODOT_VERSION}
  godot-archive-sha256: {GODOT_ZIP_SHA256}
  headless-import: success
  headless-smoke: success
  virtual-graphical-smoke:
    status: success
    display: Xvfb
    renderer: gl_compatibility
  gdscript-tests: success
  fresh-clone-validation: success
  clean-tree-after-runtime: true
  runtime-tests: 4
ci:
  workflow: Validate Starter Kit
  run-id: {RUN_ID}
  head-commit: {HEAD}
  conclusion: success
  artifact-id: {ARTIFACT_ID}
  artifact-digest: {ARTIFACT_DIGEST}
reservations:
  - Windows editor and graphical execution are not executed.
  - Forward+ rendering on a real GPU is not executed.
  - The Xvfb smoke test is not a visual-quality review.
  - Exports and release packages are not produced.
  - The global license is undefined.
''')

write(ROOT / "Companion-Pack/index.md", '''---
title: "Companion Pack — Kit de développement"
id: "CP-INDEX"
status: "active"
version: "0.2.0"
last-updated: "2026-07-30T04:19:00+02:00"
---

# Companion Pack — Kit de développement

Le Companion Pack regroupe les ressources directement réutilisables associées aux cinq livres.

## Packs

1. [x] [Starter Kit](Starter-Kit/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;
2. [ ] Project Templates ;
3. [ ] AI Library ;
4. [ ] Code Library ;
5. [ ] Database Library ;
6. [ ] ComfyUI Library ;
7. [ ] Documentation Library ;
8. [ ] Test & Benchmark Library ;
9. [ ] Production Toolkit ;
10. [ ] Knowledge Base.

## Principes

Chaque ressource reçoit un identifiant stable, une version, une licence ou un statut de redistribution, des dépendances, des exemples et des références croisées vers les chapitres concernés.

## Statut

Progression : **1 pack sur 10**. Le Starter Kit est matérialisé et validé dans son périmètre Linux. Les réserves Windows graphique, Forward+ GPU, exports et licence globale restent ouvertes. La prochaine action est le Pack 2 — Project Templates.
''')

p = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
s = p.read_text(encoding="utf-8")
s = replace_once(s, 'version: "1.0.0"', 'version: "1.1.0"', "plan version")
s = replace_once(s, 'last-updated: "2026-07-18"', f'last-updated: "{DATE}"', "plan date")
s = replace_once(s, '> **Statut :** non commencé  ', '> **Statut :** en cours — Pack 1 sur 10 validé  ', "plan status")
s = replace_once(s, '## Pack 1 — Starter Kit\n\n**Objectifs**', f'## Pack 1 — Starter Kit\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `{RUN_ID}` ; réserves Windows graphique, Forward+ GPU, exports et licence globale maintenues.\n\n**Objectifs**', "pack 1 state")
write(p, s)

p = ROOT / "ROADMAP.md"
s = p.read_text(encoding="utf-8")
s = replace_once(s, '**Statut M7 : actif — Pack 1, Starter Kit, à matérialiser.**', '**Statut M7 : actif — 1 pack validé sur 10 ; Pack 2, Project Templates, suivant.**', "roadmap M7 status")
s = replace_once(s, '- [ ] Starter Kit.', '- [x] Starter Kit — version `1.0.0`, validation Linux `runtime-tested`.', "roadmap starter")
write(p, s)

p = ROOT / "contents.txt"
s = p.read_text(encoding="utf-8")
line = "Companion-Pack/Starter-Kit/README.md"
if line not in s.splitlines():
    s = s.rstrip() + "\n" + line + "\n"
write(p, s)

p = ROOT / "CONTINUITE-PROJET.md"
s = p.read_text(encoding="utf-8")
s = replace_once(s, 'version: "4.14.0"', 'version: "4.15.0"', "continuity version")
s = replace_once(s, 'last-updated: "2026-07-30T03:00:00+02:00"', f'last-updated: "{TS}"', "continuity timestamp")
s = replace_once(s, '- jalon : M7 — Companion Pack ;', '- jalon : M7 — Companion Pack ;\n- progression du Companion Pack : 1 pack validé sur 10 ;\n- Starter Kit : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;', "continuity current state")
s = s.replace('- Starter Kit non matérialisé ;', '- Starter Kit matérialisé et validé dans le périmètre Linux ;')
start = s.index('## 26. Prochaine action')
end = s.index('## 27. Journal', start)
next_section = '''## 26. Prochaine action

M7 — Companion Pack est actif. Le Pack 1 — Starter Kit est matérialisé en version `1.0.0` et validé sur Linux x86_64 : statique, PowerShell, import headless, bootstrap, lancement Xvfb Compatibility, tests GDScript, clone neuf et arbre propre. Windows graphique, Forward+ GPU, exports et licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/Project-Templates/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 2 doit matérialiser des templates Solo et Studio, les conventions Git, les modèles d’issues et de PR, les ADR, les responsabilités, les réglages VS Code et les squelettes de modules Godot. Aucun projet dérivé, protection de branche, CODEOWNERS effectif ou test de création ne devra être annoncé sans matérialisation et preuve.
'''
s = s[:start] + next_section + s[end:]
journal = f'''## 27. Journal

### {TS} — version 4.15.0

- matérialisation du Companion Pack, Pack 1 — Starter Kit ;
- projet Godot `Project Asteria` version `1.0.0`, Godot `{GODOT_VERSION}`, GDScript et Forward+ de référence ;
- scène de bootstrap 3D, `BootstrapReport`, profils Solo/Studio, manifestes, provenance et statut de redistribution créés ;
- validateur Python sans paquet tiers et enveloppe PowerShell exécutés avec succès ;
- import et démarrage Linux headless réussis ;
- démarrage graphique virtuel Xvfb avec Compatibility réussi, sans revendication de qualité visuelle ;
- tests GDScript réussis avec `STARTER_KIT_TESTS: PASS` ;
- clone Git neuf reproduit, importé et testé ; arbre propre après runtime ;
- trois UID Godot générés puis versionnés ;
- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;
- progression M7 portée à 1 pack sur 10 ;
- prochaine action : `Companion-Pack/Project-Templates/README.md`, niveau Élevée ;
- aucun Windows graphique, Forward+ GPU réel, export, archive publiable, restauration, licence globale, donnée personnelle ou secret validé ou produit.

'''
s = s.replace('## 27. Journal\n\n', journal, 1)
write(p, s)

subprocess.run([
    "python3", str(PACK / "godot-project/tools/validate_project.py"),
    "--report", "validation-static.json",
], cwd=PACK / "godot-project", check=True)
print("Starter Kit finalization complete.")
