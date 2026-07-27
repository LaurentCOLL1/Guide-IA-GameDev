#!/usr/bin/env python3
from __future__ import annotations

import base64
import gzip
import hashlib
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TIMESTAMP = "2026-07-27T08:32:16+02:00"
BRANCH = "docs/livre-iv-chapitre-16-exports-godot-packaging"
BASE_COMMIT = "4649385c3c0a213158b192d00275e0a6a636aee9"
def read_chunks(prefix: str) -> str:
    paths = sorted((ROOT / "tools/temporary").glob(prefix + ".*.b64"))
    if not paths:
        raise RuntimeError(f"aucun fragment pour {prefix}")
    return "".join(path.read_text(encoding="ascii").strip() for path in paths)

CHAPTER_B64 = read_chunks("ch16.chapter")
AUDIT_B64 = read_chunks("ch16.audit")
PROOF_TEMPLATE = (ROOT / "tools/temporary/ch16.proof.template").read_text(encoding="utf-8")

EXPECTED_PERMANENT = {
    "CONTINUITE-PROJET.md",
    "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md",
    "Livre-IV/QA/AUDIT-CHAPITRE-16.md",
    "Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-16.yaml",
    "Livre-IV/index.md",
    "ROADMAP.md",
    "contents.txt",
    "plans/LIVRE-IV-PLAN-MAITRE.md",
}

def decode_text(value: str) -> str:
    return gzip.decompress(base64.b64decode(value)).decode("utf-8")

def write_text(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")

def read_text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

def replace_once(relative: str, old: str, new: str) -> None:
    text = read_text(relative)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: remplacement attendu une fois, obtenu {count} pour {old!r}")
    write_text(relative, text.replace(old, new, 1))

def regex_replace_once(relative: str, pattern: str, replacement: str) -> None:
    text = read_text(relative)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{relative}: remplacement regex attendu une fois, obtenu {count}")
    write_text(relative, updated)

def sha256_text(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()

def validate_chapter(text: str) -> None:
    required = [
        "[PS]", "[CMD]", "[WSL]", "[DCT]", "[DCK]",
        "[VSC]", "[WEB]", "[APP]", "[SORTIE]", "[LECTURE]",
    ]
    for marker in required:
        if marker not in text:
            raise RuntimeError(f"repère absent: {marker}")
    if "recommended-reasoning" in text or "Niveau GPT" in text:
        raise RuntimeError("métadonnée de raisonnement interdite dans le chapitre")
    if "prochaine action" in text.lower() or "prochaine étape" in text.lower():
        raise RuntimeError("prochaine action interdite dans le chapitre lecteur")
    if "PDF" in text:
        raise RuntimeError("mention de chaîne éditoriale interdite dans le chapitre lecteur")
    if text.count("<!-- qa:code-explanation -->") != 60:
        raise RuntimeError("nombre inattendu de marqueurs d’explication")
    if text.count("**Pourquoi cet exemple est fautif :**") != 10:
        raise RuntimeError("dix explications fautives requises")
    if text.count("**Pourquoi la correction fonctionne :**") != 10:
        raise RuntimeError("dix explications corrigées requises")
    headings = [line.strip() for line in text.splitlines() if re.match(r"^#{1,6} ", line)]
    if len(headings) != len(set(headings)):
        raise RuntimeError("titre dupliqué")
    blocks = re.findall(r"```\w*\n(.*?)\n```", text, flags=re.S)
    normalized = [re.sub(r"\s+", " ", block.strip()) for block in blocks if len(block.splitlines()) >= 2]
    if len(normalized) != len(set(normalized)):
        raise RuntimeError("bloc significatif dupliqué")
    if "## 37. Synthèse opérationnelle pour `Project Asteria`" not in text:
        raise RuntimeError("synthèse Asteria absente")

def update_index() -> None:
    replace_once("Livre-IV/index.md", 'version: "0.16.0"', 'version: "0.17.0"')
    replace_once("Livre-IV/index.md", 'last-updated: "2026-07-27T01:20:18+02:00"', f'last-updated: "{TIMESTAMP}"')
    replace_once(
        "Livre-IV/index.md",
        "16. Exports Godot et packaging ;",
        "16. [Exports Godot et packaging](CHAPITRE-16-Exports-Godot-et-packaging.md) — version `1.0.0`, niveau `static-review` ;",
    )
    replace_once("Livre-IV/index.md", "**15 sur 22**", "**16 sur 22**")
    replace_once(
        "Livre-IV/index.md",
        "**chapitre 15 — Sauvegardes, migrations et reprise après incident**",
        "**chapitre 16 — Exports Godot et packaging**",
    )
    replace_once(
        "Livre-IV/index.md",
        "**chapitre 16 — Exports Godot et packaging** ;\n- construction PDF",
        "**chapitre 17 — Publication et distribution** ;\n- construction PDF",
    )
    replace_once(
        "Livre-IV/index.md",
        "les chapitres 1 à 15 sont terminés",
        "les chapitres 1 à 16 sont terminés",
    )

def update_roadmap() -> None:
    replace_once(
        "ROADMAP.md",
        "- [x] Chapitre 15 — Sauvegardes, migrations et reprise après incident — rédigé, repéré et audité au niveau `static-review`.\n",
        "- [x] Chapitre 15 — Sauvegardes, migrations et reprise après incident — rédigé, repéré et audité au niveau `static-review`.\n"
        "- [x] Chapitre 16 — Exports Godot et packaging — rédigé, repéré et audité au niveau `static-review`.\n",
    )
    replace_once(
        "ROADMAP.md",
        "- [ ] DevOps, publication et maintenance — 2 chapitres sur 9.",
        "- [ ] DevOps, publication et maintenance — 3 chapitres sur 9.",
    )
    replace_once(
        "ROADMAP.md",
        "**Statut M5 : en cours — 15 chapitres rédigés, repérés et audités sur 22.**",
        "**Statut M5 : en cours — 16 chapitres rédigés, repérés et audités sur 22.**",
    )

def update_contents() -> None:
    replace_once(
        "contents.txt",
        "Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md\nLivre-V/index.md",
        "Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md\n"
        "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md\n"
        "Livre-V/index.md",
    )

def update_master_plan() -> None:
    replace_once("plans/LIVRE-IV-PLAN-MAITRE.md", 'version: "1.0.15"', 'version: "1.0.16"')
    replace_once(
        "plans/LIVRE-IV-PLAN-MAITRE.md",
        'last-updated: "2026-07-27T01:20:18+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(
        "plans/LIVRE-IV-PLAN-MAITRE.md",
        "> **Statut :** en cours — 15 chapitres sur 22",
        "> **Statut :** en cours — 16 chapitres sur 22",
    )
    replace_once(
        "plans/LIVRE-IV-PLAN-MAITRE.md",
        "La publication commerciale est au chapitre 17. Validation par installation et lancement sur machine propre.\n\n## Chapitre 17",
        "La publication commerciale est au chapitre 17. Validation par installation et lancement sur machine propre.\n\n"
        "**État documentaire au 2026-07-27 :** chapitre rédigé, repéré et audité au niveau `static-review`. "
        "Presets, filtres, dépendances, icônes, signatures, packages, manifestes, checksums et campagne sur machine propre sont préparés sans revendiquer d’export, de signature, d’installation ou de lancement.\n\n"
        "## Chapitre 17",
    )

def update_continuity() -> None:
    replace_once("CONTINUITE-PROJET.md", 'version: "3.78.0"', 'version: "3.79.0"')
    replace_once(
        "CONTINUITE-PROJET.md",
        'last-updated: "2026-07-27T01:20:18+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(
        "CONTINUITE-PROJET.md",
        "- progression du Livre IV : 15 chapitres sur 22 ;",
        "- progression du Livre IV : 16 chapitres sur 22 ;",
    )
    replace_once(
        "CONTINUITE-PROJET.md",
        "- chapitre 15 du Livre IV : version `1.0.0`, niveau `static-review` ;\n",
        "- chapitre 15 du Livre IV : version `1.0.0`, niveau `static-review` ;\n"
        "- chapitre 16 du Livre IV : version `1.0.0`, niveau `static-review` ;\n",
    )
    next_section = f"""## 26. Prochaine action

Les chapitres 1 à 16 du Livre IV sont terminés au niveau documentaire et statique. Les presets, templates, SDK, dépendances natives, identités produit, credentials, signatures, notarisation, packages et campagnes sur machines propres de `Project Asteria` restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-17-Publication-et-distribution.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 17 du Livre IV préparera pages, médias, descriptions et exigences de publication, organisera boutiques, canaux et clés, vérifiera licences et conformité, planifiera lancement et support, puis préparera builds candidats, notes de version et dry-run de soumission.

"""
    regex_replace_once(
        "CONTINUITE-PROJET.md",
        r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)",
        next_section,
    )
    journal = f"""### {TIMESTAMP} — version 3.79.0

- création du chapitre 16 du Livre IV — Exports Godot et packaging ;
- export, build, package, artefact, release et publication distingués ;
- matrice de cibles, templates, presets, credentials, identités et profils debug/test/release encadrés ;
- filtres de ressources, fichiers privés, dépendances natives, GDExtension, icônes et métadonnées documentés ;
- Windows, Linux, macOS, Android, iOS, Web et référence au serveur dédié préparés avec leurs préconditions ;
- scripts canoniques, staging neuf, manifestes fermés, checksums, archives et reçus de promotion préparés ;
- signature, notarisation, empreinte finale et promotion des mêmes octets ordonnées ;
- campagne d’installation et lancement sur machine propre préparée sans exécution revendiquée ;
- métriques statiques : 2004 lignes, 73 titres, 56 blocs significatifs, 40 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 17 — Publication et distribution, niveau Élevée ;
- aucun preset, template, SDK, certificat, export, signature, package, installation, lancement runtime ou PDF du Livre IV produit.

"""
    replace_once(
        "CONTINUITE-PROJET.md",
        "## 27. Journal\n\n",
        "## 27. Journal\n\n" + journal,
    )

def main() -> None:
    chapter = decode_text(CHAPTER_B64)
    audit = decode_text(AUDIT_B64)
    validate_chapter(chapter)

    write_text("Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md", chapter)
    write_text("Livre-IV/QA/AUDIT-CHAPITRE-16.md", audit)

    update_index()
    update_roadmap()
    update_contents()
    update_master_plan()
    update_continuity()

    proof = (
        PROOF_TEMPLATE
        .replace("__CHAPTER_SHA256__", sha256_text("Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md"))
        .replace("__AUDIT_SHA256__", sha256_text("Livre-IV/QA/AUDIT-CHAPITRE-16.md"))
        .replace("__RUN_ID__", os.environ.get("GITHUB_RUN_ID", "unknown"))
    )
    write_text("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-16.yaml", proof)

    temporary_paths = [
        ROOT / "tools/temporary/finalize_l4_ch16.py",
        ROOT / ".github/workflows/livre-iv-ch16-finalizer.yml",
        ROOT / "tools/temporary/ch16.proof.template",
    ]
    temporary_paths.extend((ROOT / "tools/temporary").glob("ch16.chapter.*.b64"))
    temporary_paths.extend((ROOT / "tools/temporary").glob("ch16.audit.*.b64"))
    for temporary in temporary_paths:
        temporary.unlink(missing_ok=True)

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    changed = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "origin/main"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    if set(changed) != EXPECTED_PERMANENT:
        raise RuntimeError(f"diff permanent inattendu: {changed}")

if __name__ == "__main__":
    main()
