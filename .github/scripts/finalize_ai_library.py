from __future__ import annotations

from pathlib import Path
import json

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/AI-Library"
TIMESTAMP = "2026-07-30T06:36:00+02:00"
RUN_ID = 30514201037
HEAD_COMMIT = "79aa29be43f508461e7a5499489bc7a8b65cf1d4"
ARTIFACT_ID = 8748232588
ARTIFACT_DIGEST = "sha256:c42c91c7d604a2d128e6e95f2923b46cc55397e87956d7787cd9d63a812741b7"
GODOT_SHA = "c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


write(PACK / "VERSION", "1.0.0\n")

readme_path = PACK / "README.md"
readme = read(readme_path)
for old, new, label in [
    ('status: "candidate"', 'status: "reviewed"', "README status"),
    ('version: "0.1.0"', 'version: "1.0.0"', "README version"),
    ('last-verified: "2026-07-30T05:55:00+02:00"', f'last-verified: "{TIMESTAMP}"', "README timestamp"),
    ('validation-status: "candidate"', 'validation-status: "runtime-tested-linux"', "README validation"),
    ('## État candidat', '## État du lot', "README heading"),
]:
    readme = replace_once(readme, old, new, label)
readme = replace_once(
    readme,
    '| exemple Godot | matérialisé |\n| service fournisseur réel | non exécuté |',
    f'| exemple Godot | matérialisé |\n| qualification Python et mocks | validée par le run `{RUN_ID}` |\n| import, lancements et tests Godot | validés sur Linux x86_64 par le run `{RUN_ID}` |\n| service fournisseur réel | non exécuté |',
    "README qualification rows",
)
qualification = f'''## Qualification obtenue\n\nLe run `{RUN_ID}` a validé 51 fichiers sources, 13 tests Python, les faux serveurs HTTP et WebSocket sur boucle locale, l’import Godot, les lancements headless et Xvfb Compatibility, puis les tests GDScript avec `AI_LIBRARY_GODOT_TESTS: PASS`. L’arbre Git est resté propre après runtime.\n\nGodot qualifié : `4.7.1.stable.official.a13da4feb`. Archive Linux SHA-256 : `{GODOT_SHA}`.\n\nCette qualification ne couvre aucun service fournisseur réel, aucun modèle, aucune performance, aucune qualité de sortie et aucune exposition réseau distante.\n\n'''
readme = replace_once(readme, "## Architecture\n", qualification + "## Architecture\n", "README qualification section")
write(readme_path, readme)

changelog_path = PACK / "CHANGELOG.md"
changelog = read(changelog_path)
entry = f'''## 1.0.0 — 2026-07-30\n\n- validation statique de 51 fichiers sans dépendance Python tierce ;\n- 13 tests Python réussis ;\n- faux serveurs HTTP et WebSocket qualifiés sur `127.0.0.1` ;\n- import, démarrages headless et Xvfb Compatibility réussis avec Godot `4.7.1-stable` ;\n- tests GDScript réussis avec `AI_LIBRARY_GODOT_TESTS: PASS` ;\n- arbre Git propre après runtime ;\n- réserves sur services réels, modèles, performances, réseau distant, exports et licence globale maintenues.\n\n'''
changelog = replace_once(changelog, "# Journal des versions\n\n", "# Journal des versions\n\n" + entry, "CHANGELOG entry")
write(changelog_path, changelog)

manifest_path = PACK / "manifest.json"
manifest = json.loads(read(manifest_path))
manifest["version"] = "1.0.0"
manifest["status"] = "reviewed"
write(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

dependencies_path = PACK / "DEPENDENCIES.json"
dependencies = json.loads(read(dependencies_path))
dependencies["pack_version"] = "1.0.0"
for dependency in dependencies["dependencies"]:
    if dependency["id"] == "python-standard-library":
        dependency["qualification"] = f"tests-pass-run-{RUN_ID}"
    elif dependency["id"] == "godot-engine":
        dependency["qualification"] = f"linux-runtime-pass-run-{RUN_ID}"
write(dependencies_path, json.dumps(dependencies, ensure_ascii=False, indent=2) + "\n")

audit = f'''---\ntitle: "Audit — Companion Pack Pack 3 AI Library"\nid: "CP-AUDIT-PACK-03"\nstatus: "complete"\nversion: "1.0.0"\naudit-level: "runtime-tested"\naudit-date: "{TIMESTAMP}"\n---\n\n# Audit — AI Library\n\n## Décision\n\nLe Pack 3 est accepté au niveau `runtime-tested` pour Linux x86_64 dans le périmètre des faux serveurs contrôlés. Aucun service fournisseur réel, modèle ou réseau distant n'est qualifié.\n\n## Portes exécutées\n\n- validation statique de 51 fichiers sans paquet Python tiers ;\n- 13 tests unitaires et d'intégration Python réussis ;\n- faux serveur HTTP et sous-ensemble OpenAI-compatible validés ;\n- faux serveur WebSocket et corrélation validés ;\n- reprises bornées, cache, annulation, file et backpressure testés ;\n- adaptateurs Ollama, llama.cpp server et LocalAI vérifiés sur leur contrat commun, sans service réel ;\n- import Godot réussi ;\n- bootstrap headless et Xvfb Compatibility réussi ;\n- tests GDScript contre les faux serveurs réussis ;\n- arbre Git propre après runtime ;\n- absence de secret, donnée personnelle, binaire tiers et PDF contrôlée.\n\n## Preuve principale\n\n- workflow : `Validate AI Library` ;\n- run : `{RUN_ID}` ;\n- commit : `{HEAD_COMMIT}` ;\n- artefact : `{ARTIFACT_ID}` ;\n- digest : `{ARTIFACT_DIGEST}`.\n\n## Réserves\n\n- aucun service Ollama, llama.cpp ou LocalAI réel ;\n- aucun modèle, poids, tokenizer ou template réel ;\n- aucune mesure de latence, débit, mémoire ou qualité ;\n- aucun TLS, authentification distante ou exposition Internet ;\n- aucun streaming SSE, outil, fonction, embedding ou multimodalité fournisseur ;\n- aucune exécution Windows graphique ou Forward+ sur GPU réel ;\n- aucun export ou paquet de release ;\n- aucune licence globale.\n'''
write(PACK / "qa/AUDIT-AI-LIBRARY.md", audit)

validation = f'''schema-version: 1\nevidence-id: CP-QA-PACK-03\nstatus: complete\nvalidation-date: '2026-07-30'\nsource-branch: feat/companion-pack-ai-library\npack:\n  id: CP-PACK-03-AI-LIBRARY\n  version: 1.0.0\n  entry-point: Companion-Pack/AI-Library/README.md\n  audit-level: runtime-tested\nresults:\n  source-files: 51\n  third-party-python-dependencies: 0\n  static-validation: success\n  python-tests:\n    status: success\n    count: 13\n  http-mock-integration: success\n  websocket-mock-integration: success\n  provider-adapters: success-common-contract-only\n  bounded-retry-cache-cancellation-queue: success\n  godot-version: 4.7.1.stable.official.a13da4feb\n  godot-archive-sha256: {GODOT_SHA}\n  godot-import: success\n  godot-headless-smoke: success\n  godot-xvfb-smoke:\n    status: success\n    renderer: gl_compatibility\n    display: Xvfb\n  godot-tests: success\n  clean-tree-after-runtime: true\n  document-validation: pending-permanent-run\n  runtime-tests: 14\nci:\n  qualification-run:\n    workflow: Validate AI Library\n    run-id: {RUN_ID}\n    head-commit: {HEAD_COMMIT}\n    conclusion: success\n    artifact-id: {ARTIFACT_ID}\n    artifact-digest: {ARTIFACT_DIGEST}\nreservations:\n  - Real Ollama, llama.cpp and LocalAI services are not executed.\n  - No model or model weights are downloaded.\n  - Performance and output quality are not measured.\n  - Remote networking, TLS and authentication are not qualified.\n  - SSE streaming, tools and multimodal features are not qualified.\n  - Windows graphical execution and real-GPU Forward+ are not executed.\n  - Exports and release packages are not produced.\n  - The global license is undefined.\n'''
write(PACK / "qa/VALIDATION-AI-LIBRARY.yaml", validation)

index_path = ROOT / "Companion-Pack/index.md"
index = read(index_path)
for old, new, label in [
    ('version: "0.3.0"', 'version: "0.4.0"', "index version"),
    ('last-updated: "2026-07-30T05:34:00+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp"),
    ('3. [ ] AI Library ;', '3. [x] [AI Library](AI-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;', "index pack"),
    ('Progression : **2 packs sur 10**. Le Starter Kit et Project Templates sont matérialisés et validés dans leur périmètre Linux. Les réserves Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 3 — AI Library.', 'Progression : **3 packs sur 10**. Le Starter Kit, Project Templates et AI Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 4 — Code Library.', "index status"),
]:
    index = replace_once(index, old, new, label)
write(index_path, index)

plan_path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
plan = read(plan_path)
plan = replace_once(plan, 'version: "1.2.0"', 'version: "1.3.0"', "plan version")
plan = replace_once(plan, '> **Statut :** en cours — Pack 2 sur 10 validé', '> **Statut :** en cours — Pack 3 sur 10 validé', "plan status")
plan = replace_once(
    plan,
    '## Pack 3 — AI Library\n\n**Objectifs**',
    f'## Pack 3 — AI Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `{RUN_ID}` avec faux serveurs contrôlés ; réserves services réels, modèles, performances, réseau distant, exports et licence globale maintenues.\n\n**Objectifs**',
    "plan Pack 3 state",
)
write(plan_path, plan)

roadmap_path = ROOT / "ROADMAP.md"
roadmap = read(roadmap_path)
roadmap = replace_once(roadmap, '**Statut M7 : actif — 2 packs validés sur 10 ; Pack 3, AI Library, suivant.**', '**Statut M7 : actif — 3 packs validés sur 10 ; Pack 4, Code Library, suivant.**', "roadmap status")
roadmap = replace_once(roadmap, '- [ ] AI Library.', '- [x] AI Library — version `1.0.0`, validation Linux `runtime-tested` avec faux serveurs.', "roadmap AI")
write(roadmap_path, roadmap)

contents_path = ROOT / "contents.txt"
contents = read(contents_path)
entry_path = "Companion-Pack/AI-Library/README.md"
if entry_path not in contents.splitlines():
    if not contents.endswith("\n"):
        contents += "\n"
    contents += entry_path + "\n"
write(contents_path, contents)

continuity_path = ROOT / "CONTINUITE-PROJET.md"
continuity = read(continuity_path)
for old, new, label in [
    ('version: "4.16.0"', 'version: "4.17.0"', "continuity version"),
    ('last-updated: "2026-07-30T05:34:00+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp"),
    ('- progression du Companion Pack : 2 packs validés sur 10 ;', '- progression du Companion Pack : 3 packs validés sur 10 ;', "continuity progress"),
    ('- Project Templates : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;', '- Project Templates : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;\n- AI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec faux serveurs contrôlés ;', "continuity pack state"),
]:
    continuity = replace_once(continuity, old, new, label)
old_next = '''M7 — Companion Pack est actif. Les Packs 1 et 2 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Project Templates a généré des projets Solo et Studio, ajouté un module en cinq couches, importé les deux projets, exécuté les démarrages headless et Xvfb Compatibility, passé les tests GDScript et conservé des arbres Git propres. Les protections GitHub effectives, Windows graphique, Forward+ GPU, exports et licence globale restent réservés.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nCompanion-Pack/AI-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe Pack 3 doit matérialiser une couche IA locale remplaçable : contrats OpenAI-compatible, clients HTTP et WebSocket, adaptateurs Ollama, llama.cpp et LocalAI, délais, reprises bornées, annulation, files, cache, mocks, filtres de sécurité et exemples Godot. Aucun service réel, secret, disponibilité fournisseur, performance ou compatibilité réseau ne devra être annoncé sans exécution et preuve.\n'''
new_next = '''M7 — Companion Pack est actif. Les Packs 1 à 3 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. AI Library a validé ses contrats, politiques, faux serveurs HTTP/WebSocket, exemples Python et Godot, sans exécuter de service ou modèle fournisseur réel. Les performances, le réseau distant, Windows graphique, Forward+ GPU, exports et licence globale restent réservés.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nCompanion-Pack/Code-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe Pack 4 doit rassembler des composants GDScript et utilitaires Python réutilisables : collections, validation, sérialisation, services et repositories, machines à états, interactions, helpers de tests, conversions et exemples. Chaque API publique devra être documentée, testée, versionnée et contrôlée contre les doublons sans imposer une architecture unique.\n'''
continuity = replace_once(continuity, old_next, new_next, "continuity next action")
journal = f'''### {TIMESTAMP} — version 4.17.0\n\n- matérialisation du Companion Pack, Pack 3 — AI Library ;\n- contrats, sous-ensemble OpenAI-compatible, HTTP, WebSocket, adaptateurs Ollama/llama.cpp/LocalAI, délais, reprises, annulation, file, cache, sécurité et modes dégradés créés ;\n- 51 fichiers sources validés sans paquet Python tiers ;\n- 13 tests Python réussis contre les faux serveurs contrôlés ;\n- import, démarrages headless et Xvfb Compatibility réussis avec Godot `4.7.1.stable.official.a13da4feb` ;\n- tests GDScript réussis avec `AI_LIBRARY_GODOT_TESTS: PASS` ;\n- arbre Git propre après runtime ;\n- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{ARTIFACT_DIGEST}` ;\n- progression M7 portée à 3 packs sur 10 ;\n- prochaine action : `Companion-Pack/Code-Library/README.md`, niveau Élevée ;\n- aucun service fournisseur réel, modèle, secret, réseau distant, mesure de performance, export, release ou licence globale validé ou produit.\n\n'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write(continuity_path, continuity)

assert read(PACK / "VERSION").strip() == "1.0.0"
assert 'status: "complete"' in read(PACK / "qa/AUDIT-AI-LIBRARY.md")
assert "Companion-Pack/Code-Library/README.md" in read(continuity_path)
assert entry_path in read(contents_path)
assert "3 packs validés sur 10" in read(roadmap_path)
print("AI Library Pack 3 finalized.")
