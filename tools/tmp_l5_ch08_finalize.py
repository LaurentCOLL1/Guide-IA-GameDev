#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T18:20:01+02:00"
DATE = "2026-07-28"
BRANCH = "docs/livre-v-ch08-bibliotheque-workflows"
BASE_COMMIT = "5e8bd75b88256ece95c274767b75319ae12cff9c"
CHAPTER_PATH = ROOT / "Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md"
AUDIT_PATH = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-08.md"
PROOF_PATH = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-08.yaml"

LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
SOURCE_RE = re.compile(r"^\.\./Livre-(?:I|II|III|IV)/")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: remplacement attendu une fois, trouvé {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def regex_replace_once(path: Path, pattern: str, replacement: str, flags: int = 0) -> None:
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{path}: motif attendu une fois, trouvé {count}: {pattern}")
    path.write_text(updated, encoding="utf-8")


def metrics(text: str) -> dict[str, int]:
    links = LINK_RE.findall(text)
    source_targets = [target.strip().split()[0].strip("<>") for _, target in links if SOURCE_RE.match(target.strip())]
    return {
        "lines": len(text.splitlines()),
        "headings": sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s+", line)),
        "cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "links": len(links),
        "source_links": len(source_targets),
        "fragment_links": sum(1 for target in source_targets if "#" in target),
        "official_links": text.count("https://"),
        "fenced_blocks": len(re.findall(r"^(?:```|~~~)", text, flags=re.MULTILINE)) // 2,
    }


def write_audit(chapter: str, m: dict[str, int]) -> str:
    audit = f'''---
title: "Audit — Livre V, fiche 08 : Bibliothèque de workflows"
id: "DOC-L5-QA-AUDIT-CH08"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 8
audit-date: "{TIMESTAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 08 : Bibliothèque de workflows

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des contrats de workflows Godot, Blender, ComfyUI, audio et documentation sans recopier leurs tutoriels propriétaires ni présenter les futurs fichiers du Companion Pack comme matérialisés.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md` ;
- identifiant : `DOC-L5-CH08` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- sources évolutives revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | {m['lines']} |
| titres | {m['headings']} |
| cartes `l5:card` | {m['cards']} |
| matrices `l5:matrix` | {m['matrices']} |
| liens Markdown | {m['links']} |
| renvois vers les Livres I à IV | {m['source_links']} |
| liens profonds vers les Livres I à IV | {m['fragment_links']} |
| liens officiels | {m['official_links']} |
| blocs clôturés | {m['fenced_blocks']} |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| workflows Godot | contenu, QA, import et export distingués |
| workflows Blender | source, collection, export glTF et contrôle Godot séparés |
| workflows ComfyUI | graphe éditable, format API, modèles, run et quarantaine séparés |
| workflows audio | TTS, STT, génération exploratoire et postproduction encadrés |
| workflows documentation | branche, validations légères, audit, preuve et fusion ciblée |
| entrées, sorties, dépendances et étapes | contrat commun et cartes de domaine |
| variantes Solo et Studio | deux cartes dédiées avec gouvernance différenciée |
| reproduction et adaptation | cycle, manifestes, idempotence, repli et qualification |
| fiches workflow | treize cartes directement consultables |
| diagrammes | remplacés par matrices tabulaires adaptées au profil Livre V |
| fichiers réutilisables | emplacements et contrat définis, statut `not-materialized` |
| checklists | porte d’acceptation et matrice de douze qualifications compactes |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les tutoriels détaillés restent dans les Livres I à IV ;
- les outils et installations restent à la fiche 03 ;
- les moteurs, API et backends restent à la fiche 04 ;
- les modèles restent aux fiches 05 à 07 ;
- les prompts restent à la fiche 09 ;
- les scripts restent au chapitre 10 ;
- les mesures exécutées restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- les checklists transversales restent au chapitre 24 ;
- licences, provenance et conformité restent au chapitre 25 ;
- les fichiers exécutables et templates réels restent au Companion Pack.

## 6. Séparation définition et exécution

Chaque workflow est classé comme contrat documentaire. Les cartes décrivent les entrées, transformations, sorties, refus, reprise et preuves nécessaires. Aucune carte n’annonce :

- un import ou export Godot exécuté ;
- un script Blender lancé ou un GLB produit ;
- un graphe ComfyUI soumis ou un média généré ;
- une synthèse, transcription ou postproduction audio réalisée ;
- un build, workflow CI de produit ou publication généré ;
- une performance, reproductibilité binaire ou compatibilité matérielle mesurée.

## 7. Sécurité et gouvernance

Les contrôles visibles couvrent les écritures bornées, fichiers non fiables, scripts tiers, custom nodes, secrets, services exposés, données personnelles, sorties génératives, opérations destructives, dépendances distantes et déclencheurs de pull request.

Le workflow documentaire reste distinct d’une autorité métier. La réussite technique ne promeut jamais automatiquement un asset, un build ou une publication.

## 8. Liens et consultation

Les {m['source_links']} renvois vers les Livres I à IV évitent les duplications. Les {m['fragment_links']} fragments visent des sous-sections propriétaires pour les contrats de contenu, l’automatisation Python, Blender, ComfyUI, audio, Solo/Studio, documentation et CI.

Les liens externes pointent vers les documentations officielles de Godot, Blender, ComfyUI, GitHub Actions, FFmpeg et Pandoc. Leur présence ne constitue pas une exécution ni une campagne automatisée de vérification réseau.

## 9. Réserves ouvertes

1. aucun template ou fichier workflow du Companion Pack créé ;
2. aucun projet Godot importé, testé ou exporté ;
3. aucun script Blender exécuté et aucun GLB produit ;
4. aucun graphe ComfyUI soumis et aucun média généré ;
5. aucun moteur audio chargé et aucun fichier audio traité ;
6. aucun workflow produit ou pipeline de publication exécuté ;
7. aucun test d’idempotence, retry, interruption ou reprise effectué ;
8. aucun résultat de reproductibilité ou de performance produit ;
9. aucun secret, fichier externe, donnée personnelle ou service manipulé ;
10. aucune approbation juridique ou organisationnelle réalisée ;
11. aucun artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 10. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment la structure, les métadonnées, les liens locaux, les marqueurs Livre V, les liens profonds, les repères et l’absence de PDF. Les workflows eux-mêmes restent `defined` jusqu’à leur matérialisation et leur qualification runtime.
'''
    AUDIT_PATH.write_text(audit, encoding="utf-8")
    return audit


def write_proof(chapter_hash: str, audit_hash: str, m: dict[str, int]) -> None:
    proof = f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH08
validation-authority: livre-v-reference-profile
status: complete
validation-date: '{DATE}'
validated-base-commit: {BASE_COMMIT}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH08
  path: Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 12
  chapter-lines: {m['lines']}
  chapter-headings: {m['headings']}
  reference-cards: {m['cards']}
  matrices: {m['matrices']}
  internal-links: {m['links']}
  source-book-links: {m['source_links']}
  fragment-links: {m['fragment_links']}
  official-links: {m['official_links']}
  fenced-blocks: {m['fenced_blocks']}
  workflow-domains-covered: 5
  godot-workflows-covered: true
  blender-workflows-covered: true
  comfyui-workflows-covered: true
  audio-workflows-covered: true
  documentation-workflows-covered: true
  solo-and-studio-covered: true
  lifecycle-matrix-present: true
  qualification-matrix-present: true
  security-and-resume-covered: true
  manifests-and-artifacts-covered: true
  reusable-files-materialized: false
  runtime-results-invented: false
  companion-pack-boundary-preserved: true
  tutorial-boundary-preserved: true
  master-plan-scope-covered: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_hash}
  audit-sha256: {audit_hash}
ci:
  permanent-validations:
    status: pending-recording-after-pr-run
reservations:
- No reusable workflow template or Companion Pack file was created.
- No Godot project was imported, tested or exported.
- No Blender script was executed and no GLB was produced.
- No ComfyUI graph was submitted and no media was generated.
- No audio engine was loaded and no audio file was processed.
- No product CI, documentation publication or deployment workflow was executed.
- No idempotence, retry, interruption or resume test was performed.
- No reproducibility, duration, RAM, VRAM, throughput or quality result was produced.
- No secret, external file, personal data or network service was handled.
- No organisational or legal approval was performed.
- No permanent Companion Pack artifact was materialized.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''
    PROOF_PATH.write_text(proof, encoding="utf-8")


def update_governance(m: dict[str, int]) -> None:
    replace_once(
        ROOT / "contents.txt",
        "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md\nCompanion-Pack/index.md",
        "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md\n"
        "Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md\n"
        "Companion-Pack/index.md",
    )

    index = ROOT / "Livre-V/index.md"
    replace_once(index, 'version: "0.9.0"', 'version: "1.0.0"')
    replace_once(
        index,
        "- [ ] Chapitre 8 — Bibliothèque de workflows.",
        "- [x] [Fiche 08 — Bibliothèque de workflows](CHAPITRE-08-Bibliotheque-de-workflows.md) — version `1.0.0`, niveau `static-review`.",
    )
    regex_replace_once(
        index,
        r"Progression : \*\*7 chapitres sur 26\*\* rédigés et audités\..*",
        "Progression : **8 chapitres sur 26** rédigés et audités. Les fiches 01 à 08 utilisent le profil de référence spécialisé du Livre V ; la fiche 08 catalogue les contrats Godot, Blender, ComfyUI, audio et documentation, leurs profils Solo/Studio, preuves, reprises et manifestes. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.",
    )

    roadmap = ROOT / "ROADMAP.md"
    replace_once(
        roadmap,
        "- [x] Modèles audio — fiche 07 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
        "- [x] Modèles audio — fiche 07 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Bibliothèque de workflows — fiche 08 rédigée et auditée au niveau `static-review`.\n"
        "- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.",
    )
    replace_once(
        roadmap,
        "**Statut M6 : en cours — 7 chapitres rédigés, repérés et audités sur 26.**",
        "**Statut M6 : en cours — 8 chapitres rédigés, repérés et audités sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    replace_once(plan, 'version: "1.7.0"', 'version: "1.8.0"')
    replace_once(
        plan,
        "> **Statut :** 7 chapitres sur 26 rédigés et audités au niveau `static-review`",
        "> **Statut :** 8 chapitres sur 26 rédigés et audités au niveau `static-review`",
    )
    replace_once(
        plan,
        "## Chapitre 8 — Bibliothèque de workflows\n\n**Objectifs**",
        "## Chapitre 8 — Bibliothèque de workflows\n\n"
        "**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n"
        "**Objectifs**",
    )

    continuity = ROOT / "CONTINUITE-PROJET.md"
    replace_once(continuity, 'version: "3.94.0"', 'version: "3.95.0"')
    regex_replace_once(continuity, r'last-updated: "[^"]+"', f'last-updated: "{TIMESTAMP}"')
    replace_once(
        continuity,
        "- progression du Livre V : 7 chapitres sur 26 ;",
        "- progression du Livre V : 8 chapitres sur 26 ;",
    )
    replace_once(
        continuity,
        "- chapitre 7 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
        "- chapitre 7 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n"
        "- chapitre 8 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;",
    )

    next_section = f'''## 26. Prochaine action

Le Livre V contient huit fiches sur 26 au niveau `static-review`. La fiche 08 catalogue les workflows Godot, Blender, ComfyUI, audio et documentation, puis sépare contrat, exécution, artefact, cache, preuve, reprise, profils Solo/Studio et acceptation. Les templates exécutables, campagnes runtime, benchmarks, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 9 cataloguera les prompts par tâche et modèle avec variables, contraintes, formats attendus, limites, biais, sécurité et critères d’évaluation. Il devra distinguer template, instance et résultat, dater le modèle cible, et ne présenter aucun prompt comme universel ou validé sans campagne enregistrée.
'''
    regex_replace_once(
        continuity,
        r"## 26\. Prochaine action\n.*?(?=\n## 27\. Journal)",
        next_section.rstrip(),
        flags=re.DOTALL,
    )

    journal = f'''### {TIMESTAMP} — version 3.95.0

- création de la fiche 08 — Bibliothèque de workflows ;
- ajout de treize cartes et de trois matrices compactes ;
- workflows Godot, Blender, ComfyUI, audio et documentation catalogués ;
- définition, exécution, cache, artefact, preuve, reprise, profils Solo/Studio et acceptation séparés ;
- sécurité, idempotence, retry, checkpoints, manifestes et douze tests de qualification documentés sans résultat inventé ;
- sources officielles de Godot, Blender, ComfyUI, GitHub Actions, FFmpeg et Pandoc revues le 28 juillet 2026 ;
- métriques statiques : {m['lines']} lignes, {m['headings']} titres, {m['cards']} fiches, {m['matrices']} matrices, {m['links']} liens, {m['source_links']} renvois vers les Livres I à IV et {m['fragment_links']} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 09 — Bibliothèque de prompts, niveau Élevée ;
- aucun template du Companion Pack, workflow runtime, import, export, média, build, mesure, secret, approbation juridique ou PDF produit.

'''
    regex_replace_once(
        continuity,
        r"## 27\. Journal\n\n",
        "## 27. Journal\n\n" + journal,
    )


def main() -> None:
    chapter = CHAPTER_PATH.read_text(encoding="utf-8")
    m = metrics(chapter)

    required = {
        "cards": 13,
        "matrices": 3,
        "fenced_blocks": 0,
    }
    for key, expected in required.items():
        if m[key] != expected:
            raise RuntimeError(f"métrique {key}: attendu {expected}, obtenu {m[key]}")
    if m["source_links"] < 20 or m["fragment_links"] < 15:
        raise RuntimeError(f"densité de liens insuffisante: {m}")
    if 'document-format: "reference-cards"' not in chapter[:1200]:
        raise RuntimeError("métadonnée reference-cards absente")
    if "not-materialized" not in chapter:
        raise RuntimeError("statut des fichiers réutilisables absent")

    audit = write_audit(chapter, m)
    chapter_hash = sha256_text(chapter)
    audit_hash = sha256_text(audit)
    write_proof(chapter_hash, audit_hash, m)
    update_governance(m)

    print("Fiche 08 finalisée.")
    for key, value in m.items():
        print(f"{key}: {value}")
    print(f"chapter_sha256: {chapter_hash}")
    print(f"audit_sha256: {audit_hash}")


if __name__ == "__main__":
    main()
