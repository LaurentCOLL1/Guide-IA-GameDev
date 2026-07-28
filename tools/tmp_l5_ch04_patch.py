#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T14:25:00+02:00"


def ensure_replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    chapter_path = ROOT / "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md"
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-04.md"

    ensure_replace(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-03-Fiches-des-logiciels-et-outils.md\n"
        "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    ensure_replace(index, 'version: "0.5.0"', 'version: "0.6.0"')
    ensure_replace(
        index,
        "- [ ] Chapitre 4 — Fiches des moteurs et backends IA.",
        "- [x] [Fiche 04 — Fiches des moteurs et backends IA](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md) — version `1.0.0`, niveau `static-review`.",
    )
    ensure_replace(
        index,
        "Progression : **3 chapitres sur 26** rédigés et audités. Les fiches 01 à 03 utilisent le profil de référence spécialisé du Livre V ; la fiche 03 normalise les logiciels et outils, leurs versions datées, formats, intégrations, alternatives, limites et sources officielles.",
        "Progression : **4 chapitres sur 26** rédigés et audités. Les fiches 01 à 04 utilisent le profil de référence spécialisé du Livre V ; la fiche 04 distingue moteurs, backends, modèles, interfaces et orchestration, puis qualifie les voies CPU et AMD.",
    )

    roadmap = ROOT / "ROADMAP.md"
    ensure_replace(
        roadmap,
        "- [x] Fiches universelles — fiche 03 des logiciels et outils rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Fiches universelles — fiche 03 des logiciels et outils rédigée et auditée au niveau `static-review`.\n"
        "- [x] Moteurs et backends IA — fiche 04 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    ensure_replace(
        roadmap,
        "**Statut M6 : en cours — 3 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 4 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    ensure_replace(plan, 'version: "1.3.0"', 'version: "1.4.0"')
    ensure_replace(
        plan,
        "> **Statut :** 3 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 4 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    ensure_replace(
        plan,
        "## Chapitre 4 — Fiches des moteurs et backends IA\n\n**Objectifs**",
        "## Chapitre 4 — Fiches des moteurs et backends IA\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    ensure_replace(continuity, 'version: "3.90.0"', 'version: "3.91.0"')
    ensure_replace(
        continuity,
        'last-updated: "2026-07-28T13:42:52+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    ensure_replace(
        continuity,
        "- progression du Livre V : 3 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 4 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    ensure_replace(
        continuity,
        "Le Livre V contient trois fiches sur 26 au niveau `static-review`. La fiche 03 normalise douze logiciels ou familles d’outils, distingue leurs rôles, versions datées, formats, intégrations, alternatives, limites et preuves, et fournit trois matrices de consultation. Les vérifications runtime, les tests de liens web depuis un navigateur, les matrices historiques de compatibilité, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 4 possédera les fiches des moteurs et backends IA, notamment Ollama, llama.cpp, LocalAI et les voies visuelles ou audio. Il devra distinguer moteur, modèle, interface et orchestration, conserver les chemins CPU/AMD et ne pas recopier les déploiements complets du Livre I ni l’intégration du Livre II.",
        "Le Livre V contient quatre fiches sur 26 au niveau `static-review`. La fiche 04 distingue moteurs, backends, modèles, interfaces et orchestration ; elle couvre Ollama, llama.cpp, LocalAI, ComfyUI et les voies CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP et audio. Les exécutions runtime, les benchmarks, les tests de liens web depuis un navigateur, les matrices historiques de compatibilité, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 5 possédera les fiches des familles de modèles de langage, tailles, quantifications, contextes, langues, licences et exigences mémoire. Il devra renvoyer aux moteurs de la fiche 04 sans confondre le modèle avec son runtime et ne présenter aucun résultat matériel sans benchmark exécuté.",
    )

    journal = f"""### {TIMESTAMP} — version 3.91.0

- création de la fiche 04 — Fiches des moteurs et backends IA ;
- ajout de treize cartes et de trois matrices compactes ;
- Ollama, llama.cpp, LocalAI, ComfyUI, CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP, faster-whisper, whisper.cpp et Piper distingués ;
- séparation moteur, backend, modèle, interface, API et orchestration explicitée ;
- voies CPU et AMD, mémoire, sécurité, formats, API et diagnostics par couches documentés ;
- métriques statiques : 363 lignes, 20 titres, 13 fiches, 3 matrices, 83 liens, 57 renvois vers les Livres I à IV et 52 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 05 — Fiches des modèles de langage, niveau Élevée ;
- aucune commande, inférence, accélération, mesure, vérification web, création d’artefact du Companion Pack ou production PDF.

"""
    ensure_replace(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T13:42:52+02:00 — version 3.90.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T13:42:52+02:00 — version 3.90.0",
    )

    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 363
    assert chapter.count("<!-- l5:card -->") == 13
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == "8b3456593905c277c269888e3000470e52835869393a27d35d3149ec07494036"
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == "ce249db94b76015b175666b99afadd52a3bb75f07a97a7c0a806e8296eba1d39"
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 83
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/", chapter)) == 57
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)", chapter)) == 52
    assert chapter.count("https://") == 9

    print("Gouvernance de la fiche 04 vérifiée ou mise à jour.")


if __name__ == "__main__":
    main()
