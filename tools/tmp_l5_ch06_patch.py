#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T16:17:52+02:00"
CHAPTER_SHA256 = "e630b7b2f09a98affc45b9590b78d76e53ad894a35b9bb5932513bd204d95014"
AUDIT_SHA256 = "a0b17f9afd1264ea6065fd27ddd17ff14568fe7bae2eb4d3e090440a68a43a7a"


def ensure_replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def assemble_chapter() -> Path:
    chapter_path = ROOT / "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md"
    parts = [
        ROOT / "tools/tmp_l5_ch06_part1.txt",
        ROOT / "tools/tmp_l5_ch06_part2.txt",
        ROOT / "tools/tmp_l5_ch06_part3.txt",
    ]
    assembled = "".join(path.read_text(encoding="utf-8") for path in parts)
    if chapter_path.exists():
        current = chapter_path.read_text(encoding="utf-8")
        if current != assembled:
            raise RuntimeError("Le chapitre 06 existant diffère des fragments contrôlés.")
    else:
        chapter_path.write_text(assembled, encoding="utf-8")
    return chapter_path


def main() -> None:
    chapter_path = assemble_chapter()
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-06.md"

    ensure_replace(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md\n"
        "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    ensure_replace(index, 'version: "0.7.0"', 'version: "0.8.0"')
    ensure_replace(
        index,
        "- [ ] Chapitre 6 — Fiches des modèles visuels.",
        "- [x] [Fiche 06 — Fiches des modèles visuels](CHAPITRE-06-Fiches-des-modeles-visuels.md) — version `1.0.0`, niveau `static-review`.",
    )
    ensure_replace(
        index,
        "Progression : **5 chapitres sur 26** rédigés et audités. Les fiches 01 à 05 utilisent le profil de référence spécialisé du Livre V ; la fiche 05 qualifie sept familles de modèles de langage, leurs tailles, contextes, licences, quantifications, langues et enveloppes théoriques. Les benchmarks runtime, les artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
        "Progression : **6 chapitres sur 26** rédigés et audités. Les fiches 01 à 06 utilisent le profil de référence spécialisé du Livre V ; la fiche 06 qualifie cinq familles visuelles, leurs composants, licences, formats, compatibilités et protocoles de test. Les générations, benchmarks runtime, artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    )

    roadmap = ROOT / "ROADMAP.md"
    ensure_replace(
        roadmap,
        "- [x] Modèles de langage — fiche 05 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Modèles de langage — fiche 05 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Modèles visuels — fiche 06 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    ensure_replace(
        roadmap,
        "**Statut M6 : en cours — 5 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 6 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    ensure_replace(plan, 'version: "1.5.0"', 'version: "1.6.0"')
    ensure_replace(
        plan,
        "> **Statut :** 5 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 6 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    ensure_replace(
        plan,
        "## Chapitre 6 — Fiches des modèles visuels\n\n**Objectifs**",
        "## Chapitre 6 — Fiches des modèles visuels\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    ensure_replace(continuity, 'version: "3.92.0"', 'version: "3.93.0"')
    ensure_replace(
        continuity,
        'last-updated: "2026-07-28T15:09:18+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    ensure_replace(
        continuity,
        "- progression du Livre V : 5 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 6 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 6 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    ensure_replace(
        continuity,
        "Le Livre V contient cinq fiches sur 26 au niveau `static-review`. La fiche 05 qualifie Qwen3, Gemma 4, Phi-4, Granite 4, Mistral Small 4, Llama et DeepSeek-R1, distingue modèles denses et MoE, paramètres totaux et actifs, contextes annoncés et testés, licences, quantifications et poids théoriques. Les sources officielles ont été revues le 28 juillet 2026 ; les téléchargements, inférences, benchmarks, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 6 possédera les fiches des checkpoints, VAE, ControlNet, LoRA et upscalers visuels. Il devra qualifier provenance, licence, formats, résolution, sampler, besoins VRAM et workflow de test sans recopier les installations ComfyUI ni produire d’images prétendument validées.",
        "Le Livre V contient six fiches sur 26 au niveau `static-review`. La fiche 06 qualifie Stable Diffusion XL/3.5, FLUX.2/FLUX.1, Qwen-Image, HunyuanImage-3.0 et HiDream-I1, puis sépare VAE, encodeurs, ControlNet, LoRA, upscalers et dérivés communautaires. Les sources officielles ont été revues le 28 juillet 2026 ; les téléchargements, workflows, images, mesures matérielles, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 7 possédera les fiches des modèles audio pour TTS, STT, musique et effets. Il devra distinguer modèle, voix, moteur et consentement, préciser langues, licences, vitesse, mémoire et qualité, et ne présenter aucun clonage ou résultat audio sans exécution et droits vérifiés.",
    )

    journal = f"""### {TIMESTAMP} — version 3.93.0

- création de la fiche 06 — Fiches des modèles visuels ;
- ajout de treize cartes et de trois matrices compactes ;
- Stable Diffusion XL/3.5, FLUX.2/FLUX.1, Qwen-Image, HunyuanImage-3.0 et HiDream-I1 qualifiés ;
- checkpoints, VAE, encodeurs, ControlNet, LoRA, upscalers et dérivés communautaires séparés ;
- licences, provenance, formats, résolutions, samplers, variables VRAM et protocole de dix tests documentés ;
- sources officielles des éditeurs, de ComfyUI et des composants revues en ligne le 28 juillet 2026 sans reprendre leurs images ou performances promotionnelles ;
- métriques statiques : 380 lignes, 18 titres, 13 fiches, 3 matrices, 65 liens, 20 renvois vers les Livres I à IV et 19 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 07 — Fiches des modèles audio, niveau Élevée ;
- aucun modèle téléchargé, workflow chargé, image générée, mesure, approbation juridique, artefact du Companion Pack ou PDF produit.

"""
    ensure_replace(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T15:09:18+02:00 — version 3.92.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T15:09:18+02:00 — version 3.92.0",
    )

    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 380
    assert chapter.count("<!-- l5:card -->") == 13
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == CHAPTER_SHA256
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == AUDIT_SHA256
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 65
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/", chapter)) == 20
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)", chapter)) == 19
    assert chapter.count("https://") == 23

    print("Fiche 06 assemblée, gouvernance vérifiée et empreintes conformes.")


if __name__ == "__main__":
    main()
