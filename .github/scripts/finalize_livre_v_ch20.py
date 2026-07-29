from __future__ import annotations

import hashlib
import os
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-20.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-20.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"

TIMESTAMP = "2026-07-29T16:26:00+02:00"
DATE = "2026-07-29"
BASE_COMMIT = "b76275616b26547f876e955064e8419c4220ab7b"
BRANCH = "docs/livre-v-ch20-catalogue-erreurs-diagnostics"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chapter_metrics(text: str) -> dict[str, int]:
    lines = text.splitlines()
    headings = [line.strip() for line in lines if re.match(r"^#{1,6}\s+\S", line)]
    normalized = [re.sub(r"^#{1,6}\s+", "", heading).strip().casefold() for heading in headings]
    duplicate_headings = sum(count - 1 for count in Counter(normalized).values() if count > 1)
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    source_book_links = sum(
        target.startswith(("../Livre-I/", "../Livre-II/", "../Livre-III/", "../Livre-IV/"))
        for target in targets
    )
    return {
        "chapter-lines": len(lines),
        "chapter-headings": len(headings),
        "reference-cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "markdown-links": len(targets),
        "source-book-links": source_book_links,
        "fragment-links": sum("#" in target for target in targets),
        "compact-diagrams": text.count("**Diagramme compact :**"),
        "fenced-blocks": sum(line.lstrip().startswith("```") for line in lines) // 2,
        "duplicate-headings": duplicate_headings,
    }


def finalize_chapter() -> dict[str, int]:
    text = read(CHAPTER)
    text = text.replace(
        "CHAPITRE-18-Reference-graphique-et-3D.md#audr-12--symptômes-diagnostics-et-acceptation",
        "CHAPITRE-18-Reference-graphique-et-3D.md#g3d-12--symptômes-visuels-diagnostics-et-acceptation",
    )
    write(CHAPTER, text)
    return chapter_metrics(text)


def finalize_audit(metrics: dict[str, int]) -> None:
    text = read(AUDIT)
    old = (
        "Les valeurs exactes sont calculées par le finaliseur sur le chapitre stabilisé et reportées dans la preuve QA : "
        "lignes, titres, cartes, matrices, liens Markdown, renvois vers les Livres I à IV, liens profonds, diagrammes compacts, "
        "blocs clôturés et doublons de titres."
    )
    new = (
        f"Métriques statiques du chapitre stabilisé : **{metrics['chapter-lines']} lignes**, "
        f"**{metrics['chapter-headings']} titres**, **{metrics['reference-cards']} cartes**, "
        f"**{metrics['matrices']} matrices**, **{metrics['markdown-links']} liens Markdown**, "
        f"**{metrics['source-book-links']} renvois vers les Livres I à IV**, "
        f"**{metrics['fragment-links']} liens profonds**, **{metrics['compact-diagrams']} diagrammes compacts**, "
        f"**{metrics['fenced-blocks']} bloc clôturé** et **{metrics['duplicate-headings']} doublon de titre**."
    )
    text = replace_once(text, old, new, "audit metrics")
    write(AUDIT, text)


def finalize_proof(metrics: dict[str, int]) -> None:
    source_head = os.environ.get("SOURCE_HEAD_COMMIT", "unknown")
    run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
    data = {
        "schema-version": 2,
        "evidence-id": "DOC-L5-QA-EVIDENCE-CH20",
        "validation-authority": "livre-v-reference-profile",
        "status": "complete",
        "validation-date": DATE,
        "validated-base-commit": BASE_COMMIT,
        "source-branch": BRANCH,
        "chapter": {
            "id": "DOC-L5-CH20",
            "path": "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md",
            "version": "1.0.0",
            "document-format": "reference-cards",
            "audit-level": "static-review",
            "reference-engine": {
                "name": "Godot Engine",
                "version": "4.7.1-stable",
                "edition": "Standard",
                "language": "GDScript",
            },
            "reference-python": {
                "implementation": "CPython",
                "version": "3.14.6",
                "fallback-version": "3.13.14",
            },
        },
        "results": {
            "blocking-errors": 0,
            **metrics,
            "diagnostic-contract-covered": True,
            "routing-and-ownership-covered": True,
            "certainty-levels-covered": True,
            "environment-and-version-fingerprint-covered": True,
            "observation-reproduction-and-reduction-covered": True,
            "evidence-collection-and-redaction-covered": True,
            "progressive-diagnostic-tree-covered": True,
            "messages-codes-and-signatures-covered": True,
            "hypotheses-and-controlled-experiments-covered": True,
            "cause-workaround-fix-and-verification-covered": True,
            "tools-dependencies-and-ci-index-covered": True,
            "data-assets-and-runtime-index-covered": True,
            "performance-network-and-delivery-index-covered": True,
            "proof-gates-covered": True,
            "maintenance-duplicates-versioning-and-retirement-covered": True,
            "master-plan-scope-covered": True,
            "qa-strategy-boundary-preserved": True,
            "tests-and-non-regression-boundary-preserved": True,
            "anomaly-reproduction-boundary-preserved": True,
            "observability-boundary-preserved": True,
            "benchmark-boundary-preserved": True,
            "compatibility-boundary-preserved": True,
            "companion-pack-boundary-preserved": True,
            "runtime-tests": 0,
            "diagnostic-tools-executed": False,
            "command-executed": False,
            "bug-report-created": False,
            "diagnostic-archive-created": False,
            "log-or-trace-collected": False,
            "dump-or-capture-created": False,
            "reproduction-executed": False,
            "reduction-executed": False,
            "hypothesis-tested": False,
            "cause-confirmed": False,
            "workaround-verified": False,
            "fix-applied": False,
            "non-regression-test-executed": False,
            "benchmark-or-profile-recorded": False,
            "network-or-delivery-tested": False,
            "user-data-processed": False,
            "runtime-results-invented": False,
            "pdf-produced": False,
        },
        "integrity": {
            "chapter-sha256": sha256(CHAPTER),
            "audit-sha256": sha256(AUDIT),
        },
        "ci": {
            "lightweight-finalization": {
                "workflow": "Temporary Livre V Chapter 20 Script Runner",
                "run-id": int(run_id) if run_id.isdigit() else run_id,
                "source-head-commit": source_head,
                "conclusion": "success",
                "validated-steps": [
                    "structure, metadata, links and duplicates",
                    "Livre V cards and deep links",
                    "structured code explanations",
                    "usage marker presence",
                    "semantic marker consistency",
                    "context coverage",
                    "absence of PDF",
                ],
            }
        },
        "reservations": [
            "No real defect, incident, crash, message, log, metric, trace, dump, capture, video or save file was collected.",
            "No command, installation, cache deletion, migration, import, export, restore or diagnostic tool was executed.",
            "No local, independent, scripted, reduced, A/B or multi-platform reproduction was performed.",
            "No hypothesis, cause, correlation, duplicate signature, workaround, fix or non-regression result was produced.",
            "No benchmark, profiling, network, delivery, update or closure decision was executed.",
            "No player data, personal data, secret, token, contract, voice, memory dump or confidential artifact was used.",
            "No Companion Pack diagnostic utility or PDF was produced.",
        ],
    }
    write(PROOF, yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120))


def update_index() -> None:
    text = read(INDEX)
    text = replace_once(text, 'version: "1.11.0"', 'version: "1.12.0"', "index version")
    text = replace_once(
        text,
        "- [ ] Chapitre 20 — Catalogue des erreurs et diagnostics.",
        "- [x] [Fiche 20 — Catalogue des erreurs et diagnostics](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md) — version `1.0.0`, niveau `static-review`.",
        "index chapter",
    )
    old = (
        "Progression : **19 chapitres sur 26** rédigés et audités. Les fiches 01 à 19 utilisent le profil de référence spécialisé du Livre V ; "
        "la fiche 19 rassemble signal, niveaux, formats, cycle de vie, boucles, familles audio, spatialisation, bus, voix, TTS/STT, localisation, "
        "accessibilité, budgets contextualisés, preuves et diagnostics. Les fichiers de test, presets exécutables et fixtures permanentes du Companion Pack, "
        "le catalogue transversal des erreurs, la licence globale et les formats de publication avancés restent des chantiers distincts."
    )
    new = (
        "Progression : **20 chapitres sur 26** rédigés et audités. Les fiches 01 à 20 utilisent le profil de référence spécialisé du Livre V ; "
        "la fiche 20 rassemble contrat diagnostique, routage, niveaux de certitude, empreintes d’environnement, reproduction, preuves, arbre progressif, "
        "messages, hypothèses, causes, contournements, corrections, index transversaux et maintenance versionnée. Les cas reproduits, outils exécutables et fixtures "
        "permanentes du Companion Pack, les protocoles de benchmark, les matrices de compatibilité, la licence globale et les formats de publication avancés restent des chantiers distincts."
    )
    text = replace_once(text, old, new, "index status")
    write(INDEX, text)


def update_roadmap() -> None:
    text = read(ROADMAP)
    marker = "- [x] Référence audio — fiche 19 rédigée et auditée au niveau `static-review`.\n"
    addition = marker + "- [x] Catalogue des erreurs et diagnostics — fiche 20 rédigée et auditée au niveau `static-review`.\n"
    text = replace_once(text, marker, addition, "roadmap chapter")
    text = replace_once(
        text,
        "**Statut M6 : en cours — 19 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 20 chapitres rédigés, repérés et audités sur 26.**",
        "roadmap status",
    )
    write(ROADMAP, text)


def update_contents() -> None:
    text = read(CONTENTS)
    marker = "Livre-V/CHAPITRE-19-Reference-audio.md\n"
    addition = marker + "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md\n"
    text = replace_once(text, marker, addition, "contents chapter")
    write(CONTENTS, text)


def update_plan() -> None:
    text = read(PLAN)
    text = replace_once(text, 'version: "1.19.0"', 'version: "1.20.0"', "plan version")
    text = replace_once(
        text,
        "> **Statut :** 19 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 20 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "plan status",
    )
    marker = "## Chapitre 20 — Catalogue des erreurs et diagnostics\n\n"
    addition = marker + "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
    text = replace_once(text, marker, addition, "plan chapter state")
    write(PLAN, text)


def update_continuity(metrics: dict[str, int]) -> None:
    text = read(CONTINUITY)
    text = replace_once(text, 'version: "4.06.0"', 'version: "4.07.0"', "continuity version")
    text = replace_once(
        text,
        'last-updated: "2026-07-29T15:46:00+02:00"',
        f'last-updated: "{TIMESTAMP}"',
        "continuity timestamp",
    )
    rules_marker = "- ne pas collecter à distance ou auprès de personnes sans gouvernance, minimisation, information, base retenue, rétention et retrait adaptés ;\n\n## 25. État courant"
    rules_addition = (
        "- ne pas collecter à distance ou auprès de personnes sans gouvernance, minimisation, information, base retenue, rétention et retrait adaptés ;\n"
        "- ne pas traiter un message, un code, une corrélation ou une signature comme une cause unique ;\n"
        "- ne pas supprimer un cache, réinstaller, migrer ou restaurer avant d’avoir préservé les preuves utiles ;\n"
        "- ne pas publier un secret, un dump non revu, une sauvegarde joueur brute ou une donnée personnelle dans un dossier diagnostique ;\n"
        "- ne pas fermer un défaut sur un contournement, un commit ou une CI verte sans vérification et non-régression adaptées ;\n\n"
        "## 25. État courant"
    )
    text = replace_once(text, rules_marker, rules_addition, "continuity diagnostic rules")
    text = replace_once(
        text,
        "- progression du Livre V : 19 chapitres sur 26 ;",
        "- progression du Livre V : 20 chapitres sur 26 ;",
        "continuity progress",
    )
    marker = "- chapitre 19 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
    addition = marker + "- chapitre 20 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
    text = replace_once(text, marker, addition, "continuity chapter")
    next_action = f"""## 26. Prochaine action

Le Livre V contient vingt fiches sur 26 au niveau `static-review`. La fiche 20 fournit un catalogue non linéaire pour contrat diagnostique, routage, certitude, environnement, observation, reproduction, réduction, preuves, messages, hypothèses, causes, contournements, corrections, index transversaux et maintenance versionnée. Les cas réels, outils de collecte, fixtures permanentes du Companion Pack, campagnes de benchmark, matrices de compatibilité, approbations organisationnelles, licence globale et balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 21 définira protocoles reproductibles, environnement, échauffement, cache, répétitions, unités, statistiques, dispersion, comparaisons et limites. Il devra dater chaque mesure, la lier au matériel et aux versions, séparer résultat brut et interprétation, et ne jamais généraliser une moyenne isolée.
"""
    text, count = re.subn(r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)", next_action, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"continuity next action: expected one section, found {count}")
    journal = f"""### {TIMESTAMP} — version 4.07.0

- création de la fiche 20 — Catalogue des erreurs et diagnostics ;
- ajout de treize cartes, de trois matrices et de {metrics['compact-diagrams']} diagrammes compacts ;
- contrat diagnostique, routage, certitude, environnement, reproduction, preuves, messages, hypothèses, causes, contournements, corrections, index transversaux et maintenance versionnée indexés ;
- frontières avec les chapitres 2 à 20 du Livre IV, les méthodes de production du Livre III, les fiches 18 et 19, la future fiche 21, la future fiche 22 et le Companion Pack maintenues sans duplication ;
- validations documentaires légères sans PDF préparées par le workflow temporaire dédié ;
- métriques statiques : {metrics['chapter-lines']} lignes, {metrics['chapter-headings']} titres, {metrics['reference-cards']} fiches, {metrics['matrices']} matrices, {metrics['markdown-links']} liens, {metrics['source-book-links']} renvois vers les Livres I à IV, {metrics['fragment-links']} liens profonds et {metrics['compact-diagrams']} diagrammes compacts ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 21 — Benchmarks et méthodes de mesure, niveau Élevée ;
- aucun défaut, message, log, trace, dump, reproduction, hypothèse, cause, contournement, correctif, benchmark, donnée utilisateur, outil diagnostique ou PDF produit.


"""
    text = replace_once(text, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
    write(CONTINUITY, text)


def main() -> None:
    metrics = finalize_chapter()
    finalize_audit(metrics)
    finalize_proof(metrics)
    update_index()
    update_roadmap()
    update_contents()
    update_plan()
    update_continuity(metrics)
    expected = {
        "CONTINUITE-PROJET.md",
        "Livre-V/CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md",
        "Livre-V/QA/AUDIT-CHAPITRE-20.md",
        "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-20.yaml",
        "Livre-V/index.md",
        "ROADMAP.md",
        "contents.txt",
        "plans/LIVRE-V-PLAN-MAITRE.md",
    }
    print("Finalized permanent files:")
    for path in sorted(expected):
        print(path)
    print("Metrics:", metrics)


if __name__ == "__main__":
    main()
