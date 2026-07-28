#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T13:42:52+02:00"


def ensure_replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    chapter_path = ROOT / "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md"
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-03.md"

    ensure_replace(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-02-Arbres-de-decision.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-02-Arbres-de-decision.md\n"
        "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    ensure_replace(index, 'version: "0.4.0"', 'version: "0.5.0"')
    ensure_replace(
        index,
        "- [ ] Chapitre 3 — Fiches des logiciels et outils.",
        "- [x] [Fiche 03 — Fiches des logiciels et outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md) — version `1.0.0`, niveau `static-review`.",
    )
    ensure_replace(
        index,
        "Progression : **2 chapitres sur 26** rédigés et audités. Les fiches 01 et 02 utilisent le profil de référence spécialisé du Livre V ; la fiche 02 fournit les arbres, critères pondérés et scénarios AMD/CPU/Solo/Studio.",
        "Progression : **3 chapitres sur 26** rédigés et audités. Les fiches 01 à 03 utilisent le profil de référence spécialisé du Livre V ; la fiche 03 normalise les logiciels et outils, leurs versions datées, formats, intégrations, alternatives, limites et sources officielles.",
    )

    roadmap = ROOT / "ROADMAP.md"
    ensure_replace(
        roadmap,
        "- [ ] Fiches universelles.",
        "- [x] Fiches universelles — fiche 03 des logiciels et outils rédigée et auditée au niveau `static-review`.",
    )
    ensure_replace(
        roadmap,
        "**Statut M6 : en cours — 2 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 3 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    ensure_replace(plan, 'version: "1.2.0"', 'version: "1.3.0"')
    ensure_replace(
        plan,
        "> **Statut :** 2 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 3 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    ensure_replace(
        plan,
        "## Chapitre 3 — Fiches des logiciels et outils\n\n**Objectifs**",
        "## Chapitre 3 — Fiches des logiciels et outils\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    ensure_replace(continuity, 'version: "3.89.0"', 'version: "3.90.0"')
    ensure_replace(
        continuity,
        'last-updated: "2026-07-28T13:00:32+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    ensure_replace(
        continuity,
        "- progression du Livre V : 2 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 3 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    ensure_replace(
        continuity,
        "Le Livre V contient deux fiches sur 26 au niveau `static-review`. La fiche 02 transforme les routes générales de la fiche 01 en décisions conditionnelles : portes éliminatoires, critères pondérés, chemins AMD/CPU, variantes Solo/Studio, replis et niveaux de preuve. Les études de décision avec lecteurs ou équipes, les benchmarks runtime, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 3 possédera les fiches normalisées de Godot, Blender, VS Code, Git, Docker, ComfyUI et outils associés. Il devra conserver versions, dates, compatibilités, alternatives, limites et liens officiels sans recopier leurs installations détaillées.",
        "Le Livre V contient trois fiches sur 26 au niveau `static-review`. La fiche 03 normalise douze logiciels ou familles d’outils, distingue leurs rôles, versions datées, formats, intégrations, alternatives, limites et preuves, et fournit trois matrices de consultation. Les vérifications runtime, les tests de liens web depuis un navigateur, les matrices historiques de compatibilité, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 4 possédera les fiches des moteurs et backends IA, notamment Ollama, llama.cpp, LocalAI et les voies visuelles ou audio. Il devra distinguer moteur, modèle, interface et orchestration, conserver les chemins CPU/AMD et ne pas recopier les déploiements complets du Livre I ni l’intégration du Livre II.",
    )

    journal = f"""### {TIMESTAMP} — version 3.90.0

- création de la fiche 03 — Fiches des logiciels et outils ;
- ajout de douze cartes d’outils, d’un contrat commun et de trois matrices compactes ;
- Windows Terminal, PowerShell, WinGet, Git, GitHub, VS Code, Python, Docker, Godot, Blender, ComfyUI, Open WebUI et Open Terminal référencés ;
- versions datées, formats, intégrations, alternatives, limites, commandes minimales et liens officiels enregistrés ;
- frontière préservée avec les décisions de la fiche 02 et les moteurs ou backends du chapitre 4 ;
- métriques statiques : 355 lignes, 19 titres, 13 fiches, 3 matrices, 64 liens, 28 renvois vers les Livres I à IV et 24 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 04 — Fiches des moteurs et backends IA, niveau Élevée ;
- aucune installation, commande, vérification web, exécution runtime, création d’artefact du Companion Pack ou production PDF.

"""
    ensure_replace(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T13:00:32+02:00 — version 3.89.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T13:00:32+02:00 — version 3.89.0",
    )

    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 355
    assert chapter.count("<!-- l5:card -->") == 13
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == "7bed4a7f95ccd68fb29a3c85aec957eea9483f3bdc23ceae51e5ee06a27de896"
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == "4abbaf6a189e6d6f084f88353bd0a849c95fd1e93616fda1ac8bd2f111e7c87c"
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 64
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/", chapter)) == 28
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)", chapter)) == 24
    assert chapter.count("https://") == 18

    print("Gouvernance de la fiche 03 vérifiée ou mise à jour.")


if __name__ == "__main__":
    main()
