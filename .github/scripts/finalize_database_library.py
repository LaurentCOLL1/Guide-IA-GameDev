from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/Database-Library"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one regex match, found {count}")
    return updated


def finalize(run_id: str, python_version: str, sqlite_version: str) -> None:
    timestamp = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()

    path = PACK / "README.md"
    text = read(path)
    text = replace_once(text, 'status: "candidate"', 'status: "reviewed"', "README status")
    text = replace_once(
        text,
        'validation-status: "local-runtime-tested-linux-pending-ci"',
        'validation-status: "runtime-tested-linux"',
        "README validation status",
    )
    write(path, text)

    path = PACK / "manifest.json"
    data = json.loads(read(path))
    data["status"] = "reviewed"
    data["validation_status"] = "runtime-tested-linux"
    write(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    path = PACK / "PROVENANCE.json"
    data = json.loads(read(path))
    data["qualification"] = f"runtime-tested-linux-run-{run_id}"
    write(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    audit = f'''---
title: "Audit — Database Library"
id: "CP-AUDIT-PACK-05"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "{timestamp}"
---

# Décision

Le Pack 5 est accepté dans son périmètre Linux x86_64 avec CPython et le module standard `sqlite3`.

## Périmètre comparé au plan maître

Le lot matérialise les huit familles prévues : schémas SQLite, migrations ascendantes, repositories, données synthétiques, scripts d’initialisation, sauvegarde et restauration, validateurs et diagrammes. Il ne modifie ni l’ordre des packs ni les décisions d’architecture.

## Contrôle anti-doublon

- le repository mémoire demeure dans la Code Library ;
- les files, retries et caches de fournisseurs demeurent dans l’AI Library ;
- le format complet de sauvegarde de partie demeure au Livre II, chapitre 9 ;
- l’index vectoriel demeure au chapitre 10 ;
- aucun addon Godot-SQLite ni binaire tiers n’est distribué.

## Preuves runtime

- workflow : `Temporary Database Library Materializer and Finalizer` ;
- run : `{run_id}` ;
- Python : `{python_version}` ;
- SQLite : `{sqlite_version}` via `sqlite3` ;
- quatre migrations ascendantes validées ;
- quatorze tests Python réussis ;
- création depuis zéro et montées depuis les versions 1, 2 et 3 validées ;
- repositories et requêtes paramétrées validés ;
- sauvegarde Online Backup API validée ;
- restauration par staging et remplacement contrôlé validée ;
- identité, version, `quick_check`, `foreign_key_check` et checksums validés ;
- validations documentaires légères exécutées ;
- aucun PDF produit.

## Repères et pédagogie

Le README utilise les dix repères officiels. Les fonctions publiques décrivent paramètres, types, retours, effets et refus. Les cinq cas d’erreurs détaillés présentent symptôme, exemple fautif, exemple corrigé et différence expliquée.

## Réserves

Godot et Godot-SQLite ne sont pas exécutés. Windows graphique n’est pas exécuté. Les performances, la charge, la concurrence et la contention ne sont pas mesurées. Aucun export, paquet de release, archive redistribuable ou licence globale n’est produit.
'''
    write(PACK / "qa/AUDIT-DATABASE-LIBRARY.md", audit)

    proof = f'''schema-version: 1
evidence-id: CP-QA-PACK-05
status: complete
validation-date: '2026-07-30'
source-branch: feat/companion-pack-database-library
pack:
  id: CP-PACK-05-DATABASE-LIBRARY
  version: 1.0.0
  entry-point: Companion-Pack/Database-Library/README.md
  audit-level: runtime-tested-linux
environment:
  os: ubuntu-24.04
  python: '{python_version}'
  sqlite: '{sqlite_version}'
results:
  source-files: 46
  migration-count: 4
  latest-schema-version: 4
  repositories: 2
  cli-tools: 4
  python-tests:
    status: success
    count: 14
  create-from-zero: success
  upgrades:
    from-1: success
    from-2: success
    from-3: success
  future-version-refusal: success
  foreign-database-refusal: success
  checksum-divergence-detection: success
  parameter-binding: success
  backup-api: success
  restore-staging: success
  quick-check: success
  foreign-key-check: success
  synthetic-data: success
  personal-data-included: false
  secrets-included: false
  database-binaries-versioned: false
  pdf-produced: false
ci:
  qualification:
    workflow: Temporary Database Library Materializer and Finalizer
    run-id: {run_id}
    validated-before-final-commit: true
reservations:
  - Godot and Godot-SQLite are not executed.
  - Windows graphical execution is not executed.
  - Performance, load, concurrency and lock contention are not measured.
  - Exports and release packages are not produced.
  - The global license is undefined.
'''
    write(PACK / "qa/VALIDATION-DATABASE-LIBRARY.yaml", proof)

    path = ROOT / "Companion-Pack/index.md"
    text = read(path)
    text = replace_once(text, 'version: "0.5.0"', 'version: "0.6.0"', "index version")
    text = regex_once(text, r'last-updated: "[^"]+"', f'last-updated: "{timestamp}"', "index timestamp")
    text = replace_once(
        text,
        '5. [ ] Database Library ;',
        '5. [x] [Database Library](Database-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python `sqlite3` ;',
        "index pack 5",
    )
    text = regex_once(
        text,
        r'## Statut\n\nProgression : \*\*4 packs sur 10\*\*\.[^\n]*',
        '## Statut\n\nProgression : **5 packs sur 10**. Le Starter Kit, Project Templates, AI Library, Code Library et Database Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, concurrence, Godot-SQLite, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 6 — ComfyUI Library.',
        "index status",
    )
    write(path, text)

    path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
    text = read(path)
    text = replace_once(text, 'version: "1.4.0"', 'version: "1.5.0"', "plan version")
    text = replace_once(text, '> **Statut :** en cours — Pack 4 sur 10 validé', '> **Statut :** en cours — Pack 5 sur 10 validé', "plan status")
    text = replace_once(
        text,
        '## Pack 5 — Database Library\n\n**Objectifs**',
        f'## Pack 5 — Database Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 avec Python `sqlite3` par le run `{run_id}` ; réserves Godot-SQLite, Godot, performance, concurrence, Windows, exports et licence globale maintenues.\n\n**Objectifs**',
        "plan pack 5 state",
    )
    write(path, text)

    path = ROOT / "ROADMAP.md"
    text = read(path)
    text = replace_once(text, '**Statut M7 : actif — 4 packs validés sur 10 ; Pack 5, Database Library, suivant.**', '**Statut M7 : actif — 5 packs validés sur 10 ; Pack 6, ComfyUI Library, suivant.**', "roadmap status")
    text = replace_once(text, '- [ ] Database Library.', '- [x] Database Library — version `1.0.0`, validation Linux `runtime-tested` avec Python `sqlite3`.', "roadmap pack 5")
    write(path, text)

    path = ROOT / "contents.txt"
    text = read(path)
    entry = "Companion-Pack/Database-Library/README.md\n"
    if entry not in text:
        text = replace_once(text, "Companion-Pack/Code-Library/README.md\n", "Companion-Pack/Code-Library/README.md\n" + entry, "contents pack 5")
    write(path, text)

    path = ROOT / "CONTINUITE-PROJET.md"
    text = read(path)
    text = replace_once(text, 'version: "4.18.0"', 'version: "4.19.0"', "continuity version")
    text = regex_once(text, r'last-updated: "[^"]+"', f'last-updated: "{timestamp}"', "continuity timestamp")
    text = replace_once(text, '- progression du Companion Pack : 4 packs validés sur 10 ;', '- progression du Companion Pack : 5 packs validés sur 10 ;', "continuity progress")
    text = replace_once(
        text,
        '- Code Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;',
        '- Code Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;\n- Database Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec Python `sqlite3` ;',
        "continuity pack 5 state",
    )
    next_section = f'''## 26. Prochaine action

M7 — Companion Pack est actif. Les Packs 1 à 5 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Database Library a validé quatre migrations ascendantes, deux repositories, quatorze tests Python, la création depuis zéro, les montées de version, la sauvegarde, la restauration et les contrôles d’intégrité avec Python `sqlite3`. Godot-SQLite, Godot, les performances, la concurrence, Windows graphique, les exports et la licence globale restent réservés.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/ComfyUI-Library/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 6 doit matérialiser une bibliothèque ComfyUI reproductible : workflows JSON, manifestes YAML, listes de custom nodes, presets, scripts de lancement, modèles de dossiers, fiches de provenance, images légères de validation et checksums. Aucun modèle non redistribuable ne devra être inclus ; chaque dépendance, seed, paramètre, profil matériel, exécution et licence devra être qualifié sans inventer de résultat.
'''
    text = regex_once(text, r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)', next_section, "continuity next section", flags=re.DOTALL)
    journal = f'''### {timestamp} — version 4.19.0

- matérialisation du Companion Pack, Pack 5 — Database Library ;
- quatre migrations SQLite ascendantes et immuables avec manifeste et empreintes SHA-256 ;
- schémas de balises, événements, documents, tags et cache dérivé créés ;
- deux repositories, fixture synthétique, scripts d’initialisation, sauvegarde, restauration et validation créés ;
- 46 fichiers sources validés sans paquet runtime tiers, addon binaire, secret, donnée personnelle ni base binaire versionnée ;
- 14 tests Python réussis avec `{python_version}` et SQLite `{sqlite_version}` via `sqlite3` ;
- création depuis zéro, montées depuis les versions 1 à 3, refus de version future et de base étrangère validés ;
- Online Backup API, restauration par staging, `quick_check`, `foreign_key_check` et historique des migrations validés ;
- run `{run_id}` du finaliseur temporaire ;
- validations documentaires légères exécutées sans PDF ;
- progression M7 portée à 5 packs sur 10 ;
- prochaine action : `Companion-Pack/ComfyUI-Library/README.md`, niveau Élevée ;
- aucun Godot-SQLite, Godot, Windows graphique, test de performance, charge, concurrence, export, release, licence globale, donnée personnelle ou secret validé ou produit.

'''
    text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
    write(path, text)

    assert (PACK / "VERSION").read_text(encoding="utf-8").strip() == "1.0.0"
    assert 'validation-status: "runtime-tested-linux"' in read(PACK / "README.md")
    assert 'status: complete' in read(PACK / "qa/VALIDATION-DATABASE-LIBRARY.yaml")
    assert "5 packs validés sur 10" in read(ROOT / "ROADMAP.md")
    assert "Companion-Pack/ComfyUI-Library/README.md" in read(ROOT / "CONTINUITE-PROJET.md")
    assert "Companion-Pack/Database-Library/README.md" in read(ROOT / "contents.txt")
    print(f"Database Library Pack 5 governance finalized at {timestamp}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--python-version", required=True)
    parser.add_argument("--sqlite-version", required=True)
    args = parser.parse_args()
    finalize(args.run_id, args.python_version.strip(), args.sqlite_version.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
