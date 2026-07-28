#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T13:00:32+02:00"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def validate_materialized(chapter_path: Path, audit_path: Path) -> None:
    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 344
    assert chapter.count("<!-- l5:card -->") == 14
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == "4d5f74e19435cc657e80d9853926eaf67f9827490b88be36c3611e51f7e652fd"
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == "96cab2c0c23bce9812a4229833527e5a4e19db16c63e0f3b803633a5b957ef53"
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 80

    required = {
        ROOT / "contents.txt": "Livre-V/CHAPITRE-02-Arbres-de-decision.md",
        ROOT / "Livre-V/index.md": "Progression : **2 chapitres sur 26**",
        ROOT / "ROADMAP.md": "**Statut M6 : en cours — 2 chapitres rédigés, repérés et audités sur 26.**",
        ROOT / "plans/LIVRE-V-PLAN-MAITRE.md": 'version: "1.2.0"',
        ROOT / "CONTINUITE-PROJET.md": 'version: "3.89.0"',
    }
    for path, marker in required.items():
        if marker not in path.read_text(encoding="utf-8"):
            raise RuntimeError(f"{path}: état final absent : {marker}")


def main() -> None:
    chapter_path = ROOT / "Livre-V/CHAPITRE-02-Arbres-de-decision.md"
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-02.md"
    continuity = ROOT / "CONTINUITE-PROJET.md"

    if 'version: "3.89.0"' in continuity.read_text(encoding="utf-8")[:500]:
        validate_materialized(chapter_path, audit_path)
        print("Gouvernance de la fiche 02 déjà matérialisée et vérifiée.")
        return

    replace_once(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md\n"
        "Livre-V/CHAPITRE-02-Arbres-de-decision.md\n"
        "Companion-Pack/index.md",
    )

    replace_once(ROOT / "Livre-V/index.md", 'version: "0.3.0"', 'version: "0.4.0"')
    replace_once(
        ROOT / "Livre-V/index.md",
        "- [ ] Chapitre 2 — Arbres de décision.",
        "- [x] [Fiche 02 — Arbres de décision](CHAPITRE-02-Arbres-de-decision.md) — version `1.0.0`, niveau `static-review`.",
    )
    replace_once(
        ROOT / "Livre-V/index.md",
        "Progression : **1 chapitre sur 26** rédigé et audité. La fiche 01 utilise désormais le profil de référence spécialisé du Livre V.",
        "Progression : **2 chapitres sur 26** rédigés et audités. Les fiches 01 et 02 utilisent le profil de référence spécialisé du Livre V ; la fiche 02 fournit les arbres, critères pondérés et scénarios AMD/CPU/Solo/Studio.",
    )

    replace_once(
        ROOT / "ROADMAP.md",
        "- [ ] Arbres de décision et matrices.",
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    replace_once(
        ROOT / "ROADMAP.md",
        "**Statut M6 : en cours — 1 chapitre rédigé, repéré et audité sur 26.**",
        "**Statut M6 : en cours — 2 chapitres rédigés, repérés et audités sur 26.**",
    )

    replace_once(ROOT / "plans/LIVRE-V-PLAN-MAITRE.md", 'version: "1.1.0"', 'version: "1.2.0"')
    replace_once(
        ROOT / "plans/LIVRE-V-PLAN-MAITRE.md",
        "> **Statut :** 1 chapitre sur 26 rédigé et audité au niveau `static-review`",
        "> **Statut :** 2 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    replace_once(
        ROOT / "plans/LIVRE-V-PLAN-MAITRE.md",
        "## Chapitre 2 — Arbres de décision\n\n**Objectifs**",
        "## Chapitre 2 — Arbres de décision\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    replace_once(continuity, 'version: "3.88.0"', 'version: "3.89.0"')
    replace_once(
        continuity,
        'last-updated: "2026-07-28T11:28:35+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(
        continuity,
        "- progression du Livre V : 1 chapitre sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 2 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    replace_once(
        continuity,
        "Le Livre V est ouvert avec une fiche sur 26 au niveau `static-review`. La fiche 01 a été corrigée pour adopter le profil propre au Livre V : consultation non linéaire, cartes, matrices, liens fréquents vers les Livres I à IV et absence de structure tutoriel héritée. Les tests de recherche avec lecteurs, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-02-Arbres-de-decision.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 2 possédera les arbres de choix, critères, contraintes, conséquences, variantes AMD/CPU et parcours Solo/Studio. Il suivra le protocole des fiches du Livre V, utilisera des matrices compactes et renverra fréquemment vers les sous-sections propriétaires sans recopier les tutoriels.",
        "Le Livre V contient deux fiches sur 26 au niveau `static-review`. La fiche 02 transforme les routes générales de la fiche 01 en décisions conditionnelles : portes éliminatoires, critères pondérés, chemins AMD/CPU, variantes Solo/Studio, replis et niveaux de preuve. Les études de décision avec lecteurs ou équipes, les benchmarks runtime, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 3 possédera les fiches normalisées de Godot, Blender, VS Code, Git, Docker, ComfyUI et outils associés. Il devra conserver versions, dates, compatibilités, alternatives, limites et liens officiels sans recopier leurs installations détaillées.",
    )
    journal = f"""### {TIMESTAMP} — version 3.89.0

- création de la fiche 02 — Arbres de décision ;
- ajout de douze arbres ou cartes décisionnelles et de trois matrices compactes ;
- chemins AMD, CPU, DirectML, ZLUDA, Windows natif, WSL, Docker et ComfyUI distingués ;
- décisions pour moteurs LLM, supports de données, transports IA, assets, diagnostic, Solo/Studio et publication ajoutées ;
- critères pondérés séparés des portes éliminatoires et situations sans solution unique documentées ;
- quatre scénarios conditionnels ajoutés sans les présenter comme benchmarks ;
- métriques statiques : 344 lignes, 19 titres, 14 fiches, 3 matrices, 63 renvois vers les Livres I à IV et 32 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 03 — Fiches des logiciels et outils, niveau Élevée ;
- aucune exécution runtime, étude lecteur, calibration des poids, création d’artefact du Companion Pack ou production PDF.

"""
    replace_once(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T11:28:35+02:00 — version 3.88.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T11:28:35+02:00 — version 3.88.0",
    )

    validate_materialized(chapter_path, audit_path)
    print("Gouvernance de la fiche 02 mise à jour.")


if __name__ == "__main__":
    main()
