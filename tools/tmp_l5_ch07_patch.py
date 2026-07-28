#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T17:27:15+02:00"
CHAPTER_SHA256 = "84d0c56cf793038c5456cd4fa13cd512646a7aa71bd1b4b059ebc433b5a6665d"
AUDIT_SHA256 = "430db11dfcbdfa852f9422853e7a8dc07bbe6822ba52238d679fdc4a627ff6d4"


def ensure_replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    chapter_path = ROOT / "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md"
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-07.md"

    ensure_replace(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md\n"
        "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    ensure_replace(index, 'version: "0.8.0"', 'version: "0.9.0"')
    ensure_replace(
        index,
        "- [ ] Chapitre 7 — Fiches des modèles audio.",
        "- [x] [Fiche 07 — Fiches des modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md) — version `1.0.0`, niveau `static-review`.",
    )
    ensure_replace(
        index,
        "Progression : **6 chapitres sur 26** rédigés et audités. Les fiches 01 à 06 utilisent le profil de référence spécialisé du Livre V ; la fiche 06 qualifie cinq familles visuelles, leurs composants, licences, formats, compatibilités et protocoles de test. Les générations, benchmarks runtime, artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
        "Progression : **7 chapitres sur 26** rédigés et audités. Les fiches 01 à 07 utilisent le profil de référence spécialisé du Livre V ; la fiche 07 qualifie six familles audio, leurs voix, composants, langues, licences, consentements et protocoles de test. Les générations, transcriptions, benchmarks runtime, artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    )

    roadmap = ROOT / "ROADMAP.md"
    ensure_replace(
        roadmap,
        "- [x] Modèles visuels — fiche 06 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Modèles visuels — fiche 06 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Modèles audio — fiche 07 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    ensure_replace(
        roadmap,
        "**Statut M6 : en cours — 6 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 7 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    ensure_replace(plan, 'version: "1.6.0"', 'version: "1.7.0"')
    ensure_replace(
        plan,
        "> **Statut :** 6 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 7 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    ensure_replace(
        plan,
        "## Chapitre 7 — Fiches des modèles audio\n\n**Objectifs**",
        "## Chapitre 7 — Fiches des modèles audio\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    ensure_replace(continuity, 'version: "3.93.0"', 'version: "3.94.0"')
    ensure_replace(
        continuity,
        'last-updated: "2026-07-28T16:17:52+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    ensure_replace(
        continuity,
        "- progression du Livre V : 6 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 6 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 7 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 6 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 7 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    ensure_replace(
        continuity,
        "Le Livre V contient six fiches sur 26 au niveau `static-review`. La fiche 06 qualifie Stable Diffusion XL/3.5, FLUX.2/FLUX.1, Qwen-Image, HunyuanImage-3.0 et HiDream-I1, puis sépare VAE, encodeurs, ControlNet, LoRA, upscalers et dérivés communautaires. Les sources officielles ont été revues le 28 juillet 2026 ; les téléchargements, workflows, images, mesures matérielles, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 7 possédera les fiches des modèles audio pour TTS, STT, musique et effets. Il devra distinguer modèle, voix, moteur et consentement, préciser langues, licences, vitesse, mémoire et qualité, et ne présenter aucun clonage ou résultat audio sans exécution et droits vérifiés.",
        "Le Livre V contient sept fiches sur 26 au niveau `static-review`. La fiche 07 qualifie Kokoro-82M, Piper, Chatterbox, Whisper, MusicGen et AudioGen, puis sépare modèles, moteurs, voix, phonémiseurs, vocodeurs, codecs, VAD, langues, licences et consentements. Les sources officielles ont été revues le 28 juillet 2026 ; les téléchargements, synthèses, transcriptions, échantillons, mesures matérielles, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 8 cataloguera les workflows Godot, Blender, ComfyUI, audio et documentation avec leurs entrées, sorties, dépendances, variantes et niveaux de preuve. Il devra renvoyer vers les tutoriels propriétaires, distinguer définition et exécution, et ne déclarer aucun workflow reproductible sans test enregistré.",
    )

    journal = f"""### {TIMESTAMP} — version 3.94.0

- création de la fiche 07 — Fiches des modèles audio ;
- ajout de treize cartes et de trois matrices compactes ;
- Kokoro-82M, Piper, Chatterbox, Whisper, MusicGen et AudioGen qualifiés ;
- modèles, moteurs, voix, locuteurs, consentements, phonémiseurs, vocodeurs, codecs, VAD et dérivés séparés ;
- langues, licences, usages, mémoire, facteurs temps réel et protocole de douze tests documentés sans résultat inventé ;
- sources officielles des éditeurs et dépôts revues en ligne le 28 juillet 2026 sans reprendre leurs performances ou échantillons promotionnels ;
- métriques statiques : 394 lignes, 18 titres, 13 fiches, 3 matrices, 61 liens, 27 renvois vers les Livres I à IV et 27 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 08 — Bibliothèque de workflows, niveau Élevée ;
- aucun modèle, voix ou enregistrement téléchargé, aucune synthèse, transcription, génération, mesure, écoute, approbation juridique, artefact du Companion Pack ou PDF produit.

"""
    ensure_replace(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T16:17:52+02:00 — version 3.93.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T16:17:52+02:00 — version 3.93.0",
    )

    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 394
    assert chapter.count("<!-- l5:card -->") == 13
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == CHAPTER_SHA256
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == AUDIT_SHA256
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 61
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/", chapter)) == 27
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)", chapter)) == 27
    assert chapter.count("https://") == 14

    print("Fiche 07 et gouvernance vérifiées ; empreintes conformes.")


if __name__ == "__main__":
    main()
