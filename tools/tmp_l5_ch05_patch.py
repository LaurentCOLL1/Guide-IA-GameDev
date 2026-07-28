#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T15:09:18+02:00"
CHAPTER_SHA = "d4d1594298d400f886e0c2e0c634a2dec9967050bc5c0e7449c95a84e5e4dcde"
AUDIT_SHA = "9cdfa20194772b1bbbe1b2e285c237781833f49083fdd0f424ae8a84e7cee315"


def ensure_replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def assemble_chapter() -> Path:
    parts = [
        ROOT / "tools/tmp_l5_ch05_part1.txt",
        ROOT / "tools/tmp_l5_ch05_part2.txt",
        ROOT / "tools/tmp_l5_ch05_part3.txt",
    ]
    text = "".join(path.read_text(encoding="utf-8") for path in parts)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != CHAPTER_SHA:
        raise RuntimeError(f"empreinte du chapitre inattendue : {digest}")
    path = ROOT / "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md"
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    chapter_path = assemble_chapter()
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-05.md"

    ensure_replace(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md\n"
        "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    ensure_replace(index, 'version: "0.6.0"', 'version: "0.7.0"')
    ensure_replace(
        index,
        "- [ ] Chapitre 5 — Fiches des modèles de langage.",
        "- [x] [Fiche 05 — Fiches des modèles de langage](CHAPITRE-05-Fiches-des-modeles-de-langage.md) — version `1.0.0`, niveau `static-review`.",
    )
    ensure_replace(
        index,
        "Progression : **4 chapitres sur 26** rédigés et audités. Les fiches 01 à 04 utilisent le profil de référence spécialisé du Livre V ; la fiche 04 distingue moteurs, backends, modèles, interfaces et orchestration, puis qualifie les voies CPU et AMD. Les campagnes runtime, les artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
        "Progression : **5 chapitres sur 26** rédigés et audités. Les fiches 01 à 05 utilisent le profil de référence spécialisé du Livre V ; la fiche 05 qualifie sept familles de modèles de langage, leurs tailles, contextes, licences, quantifications, langues et enveloppes théoriques. Les benchmarks runtime, les artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.",
    )

    roadmap = ROOT / "ROADMAP.md"
    ensure_replace(
        roadmap,
        "- [x] Moteurs et backends IA — fiche 04 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Moteurs et backends IA — fiche 04 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Modèles de langage — fiche 05 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    ensure_replace(
        roadmap,
        "**Statut M6 : en cours — 4 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 5 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    ensure_replace(plan, 'version: "1.4.0"', 'version: "1.5.0"')
    ensure_replace(
        plan,
        "> **Statut :** 4 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 5 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    ensure_replace(
        plan,
        "## Chapitre 5 — Fiches des modèles de langage\n\n**Objectifs**",
        "## Chapitre 5 — Fiches des modèles de langage\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    ensure_replace(continuity, 'version: "3.91.0"', 'version: "3.92.0"')
    ensure_replace(
        continuity,
        'last-updated: "2026-07-28T14:25:00+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    ensure_replace(
        continuity,
        "- progression du Livre V : 4 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- progression du Livre V : 5 chapitres sur 26 ;\n"
        "- chapitre 1 du Livre V : version `1.1.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 2 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 3 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 4 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 5 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )
    ensure_replace(
        continuity,
        "Le Livre V contient quatre fiches sur 26 au niveau `static-review`. La fiche 04 distingue moteurs, backends, modèles, interfaces et orchestration ; elle couvre Ollama, llama.cpp, LocalAI, ComfyUI et les voies CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP et audio. Les exécutions runtime, les benchmarks, les tests de liens web depuis un navigateur, les matrices historiques de compatibilité, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-05-Fiches-des-modeles-de-langage.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 5 possédera les fiches des familles de modèles de langage, tailles, quantifications, contextes, langues, licences et exigences mémoire. Il devra renvoyer aux moteurs de la fiche 04 sans confondre le modèle avec son runtime et ne présenter aucun résultat matériel sans benchmark exécuté.",
        "Le Livre V contient cinq fiches sur 26 au niveau `static-review`. La fiche 05 qualifie Qwen3, Gemma 4, Phi-4, Granite 4, Mistral Small 4, Llama et DeepSeek-R1, distingue modèles denses et MoE, paramètres totaux et actifs, contextes annoncés et testés, licences, quantifications et poids théoriques. Les sources officielles ont été revues le 28 juillet 2026 ; les téléchargements, inférences, benchmarks, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.\n\n"
        "Action suivante :\n\n"
        "> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n"
        "```text\n"
        "Livre-V/CHAPITRE-06-Fiches-des-modeles-visuels.md\n"
        "Niveau GPT-5.6 Sol recommandé : Élevée\n"
        "```\n\n"
        "Le chapitre 6 possédera les fiches des checkpoints, VAE, ControlNet, LoRA et upscalers visuels. Il devra qualifier provenance, licence, formats, résolution, sampler, besoins VRAM et workflow de test sans recopier les installations ComfyUI ni produire d’images prétendument validées.",
    )

    journal = f"""### {TIMESTAMP} — version 3.92.0

- création de la fiche 05 — Fiches des modèles de langage ;
- ajout de treize cartes et de trois matrices compactes ;
- Qwen3, Gemma 4, Phi-4, Granite 4, Mistral Small 4, Llama et DeepSeek-R1 qualifiés ;
- familles, checkpoints, modèles denses, MoE, paramètres totaux et actifs séparés ;
- quantifications, contextes, langues, licences, provenance, poids théoriques et protocole de huit tests documentés ;
- sources officielles des éditeurs revues en ligne le 28 juillet 2026 sans reprendre leurs performances promotionnelles ;
- métriques statiques : 379 lignes, 20 titres, 13 fiches, 3 matrices, 56 liens, 19 renvois vers les Livres I à IV et 19 liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 06 — Fiches des modèles visuels, niveau Élevée ;
- aucun modèle téléchargé, aucune inférence, mesure, approbation juridique, création d’artefact du Companion Pack ou production PDF.

"""
    ensure_replace(
        continuity,
        "## 27. Journal\n\n\n### 2026-07-28T14:25:00+02:00 — version 3.91.0",
        "## 27. Journal\n\n\n" + journal + "### 2026-07-28T14:25:00+02:00 — version 3.91.0",
    )

    chapter = chapter_path.read_text(encoding="utf-8")
    audit = audit_path.read_text(encoding="utf-8")
    assert len(chapter.splitlines()) == 379
    assert chapter.count("<!-- l5:card -->") == 13
    assert chapter.count("<!-- l5:matrix -->") == 3
    assert hashlib.sha256(chapter.encode("utf-8")).hexdigest() == CHAPTER_SHA
    assert hashlib.sha256(audit.encode("utf-8")).hexdigest() == AUDIT_SHA
    assert len(re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", chapter)) == 56
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/", chapter)) == 19
    assert len(re.findall(r"\]\(\.\./Livre-(?:I|II|III|IV)/[^)#]+#[^)]+\)", chapter)) == 19
    assert chapter.count("https://") == 13
    assert "```" not in chapter

    print("Gouvernance de la fiche 05 vérifiée ou mise à jour.")


if __name__ == "__main__":
    main()
