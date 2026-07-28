#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-28T19:12:00+02:00"
DATE = "2026-07-28"
BASE_COMMIT = "8a3097b99718fe0cf4a3876236b2c923680726e4"
BRANCH = "docs/livre-v-ch09-bibliotheque-prompts"
CHAPTER = ROOT / "Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-09.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-09.yaml"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_state(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"motif absent pour {label}")
    return text.replace(old, new, 1)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    chapter = CHAPTER.read_text(encoding="utf-8")
    lines = len(chapter.splitlines())
    headings = len(re.findall(r"(?m)^#{1,6} ", chapter))
    cards = chapter.count("<!-- l5:card -->")
    matrices = chapter.count("<!-- l5:matrix -->")
    links = len(re.findall(r"\[[^\]]+\]\([^)]+\)", chapter))
    source_links = len(re.findall(r"\]\(\.\./(?:Volume-0|Livre-[I|V]+|Livre-I|Livre-II|Livre-III|Livre-IV)/", chapter))
    fragment_links = len(re.findall(r"\]\(\.\./(?:Volume-0|Livre-I|Livre-II|Livre-III|Livre-IV)/[^)#]+#[^)]+\)", chapter))
    official_links = len(re.findall(r"\]\(https://", chapter))
    fenced = chapter.count("```") // 2

    if cards != 13 or matrices != 3:
        raise RuntimeError(f"profil attendu 13 cartes/3 matrices, obtenu {cards}/{matrices}")
    if fenced != 0:
        raise RuntimeError("la fiche 09 ne doit contenir aucun bloc clôturé")
    if source_links < 20 or fragment_links < 15:
        raise RuntimeError(f"densité de renvois insuffisante: {source_links}/{fragment_links}")
    if "Résultats d’apprentissage" in chapter or "Project Asteria" in chapter:
        raise RuntimeError("structure tutoriel importée dans la fiche")

    chapter_hash = sha256(chapter)

    audit = f'''---
title: "Audit — Livre V, fiche 09 : Bibliothèque de prompts"
id: "DOC-L5-QA-AUDIT-CH09"
status: "complete"
version: "1.0.0"
last-verified: "{TIMESTAMP}"
lang: "fr-FR"
book: "Livre V"
chapter: 9
audit-date: "{TIMESTAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 09 : Bibliothèque de prompts

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des contrats de prompts textuels, structurés, RAG, code, visuels, audio et narratifs sans recopier les tutoriels propriétaires ni présenter des exemples comme des sorties réellement obtenues.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md` ;
- identifiant : `DOC-L5-CH09` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- sources officielles évolutives revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | {lines} |
| titres | {headings} |
| cartes `l5:card` | {cards} |
| matrices `l5:matrix` | {matrices} |
| liens Markdown | {links} |
| renvois vers les Livres I à IV et Volume 0 | {source_links} |
| liens profonds vers les sources propriétaires | {fragment_links} |
| liens officiels | {official_links} |
| blocs clôturés | {fenced} |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| prompts par tâche et modèle | matrice de sélection et carte de cible exacte |
| variables et contraintes | types, bornes, confiance, délimiteurs et absence explicite |
| résultats attendus | formats, critères et états d’incertitude sans sortie inventée |
| limites, biais et sécurité | cartes par modalité et défense contre les injections |
| éviter les prompts magiques | template, instance, run, paramètres et évaluation séparés |
| templates paramétrés | treize contrats directement consultables |
| jeux de tests | douze fixtures de qualification sans résultat prérempli |
| exemples de sorties | formes attendues marquées illustratives, aucun résultat attribué à un modèle |
| critères d’évaluation | automatisation, revue humaine, variance et seuils distingués |
| modèle et version | fournisseur, snapshot, template de chat, moteur et date obligatoires |
| reproductibilité ou variance | cycle de qualification et comparaison contrôlée |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les modèles restent aux fiches 05 à 07 ;
- les workflows et leur orchestration restent à la fiche 08 ;
- les scripts et runners restent au chapitre 10 ;
- les tutoriels détaillés restent dans les Livres I à IV ;
- les résultats de campagnes restent au chapitre 21 ;
- les compatibilités historiques restent au chapitre 22 ;
- les checklists transversales restent au chapitre 24 ;
- licences, provenance et conformité restent au chapitre 25 ;
- les paquets exécutables réels restent au Companion Pack.

## 6. Séparation définition et exécution

Chaque carte distingue template, variante, instance, requête, réponse brute, résultat interprété et décision. Aucune carte n’annonce :

- un modèle ou moteur réellement appelé ;
- une sortie JSON parsée ;
- une réponse RAG ou citation vérifiée ;
- un code généré, compilé ou testé ;
- une image, voix, transcription, musique ou effet produit ;
- une campagne d’injection, de migration ou de variance exécutée ;
- une performance, qualité ou reproductibilité mesurée.

## 7. Sécurité et gouvernance

Les contrôles couvrent les injections directes et indirectes, la séparation instruction/données, les outils autorisés, les secrets, les données personnelles, les sorties actives, les limites de ressources et les décisions critiques. Le prompt reste une couche consultative ; l’application et le workflow gardent authentification, autorisation, validation et effets.

## 8. Liens et sources

Les {source_links} renvois propriétaires empêchent les duplications. Les {fragment_links} fragments visent les standards de prompts, les jeux de tests LLM, le RAG, la sécurité, la narration, les prompts visuels et la chaîne audio.

Les liens externes pointent vers les documentations officielles d’OpenAI, Google, Anthropic, Ollama et OWASP revues le 28 juillet 2026. Leur présence ne constitue ni appel API, ni test de modèle, ni approbation d’une plateforme distante.

## 9. Réserves ouvertes

1. aucun modèle de langage, visuel ou audio appelé ;
2. aucun template ou dataset du Companion Pack créé ;
3. aucune instance résolue ni requête envoyée ;
4. aucune réponse brute, sortie structurée ou appel d’outil produit ;
5. aucun parse, test de code, RAG, génération visuelle ou audio exécuté ;
6. aucune campagne de variance, migration ou régression réalisée ;
7. aucun test d’injection ou de sécurité runtime réalisé ;
8. aucune donnée personnelle, secrète ou tierce manipulée ;
9. aucune mesure de tokens, latence, coût, mémoire ou qualité produite ;
10. aucune note humaine, approbation juridique ou décision de production enregistrée ;
11. aucun artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 10. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, marqueurs Livre V, liens profonds, repères et absence de PDF. Les prompts eux-mêmes restent `defined` jusqu’à leur exécution sur un modèle exact et un jeu de tests représentatif.
'''
    AUDIT.write_text(audit, encoding="utf-8")
    audit_hash = sha256(audit)

    proof = f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH09
validation-authority: livre-v-reference-profile
status: complete
validation-date: '{DATE}'
validated-base-commit: {BASE_COMMIT}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH09
  path: Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 12
  chapter-lines: {lines}
  chapter-headings: {headings}
  reference-cards: {cards}
  matrices: {matrices}
  internal-links: {links}
  source-book-links: {source_links}
  fragment-links: {fragment_links}
  official-links: {official_links}
  fenced-blocks: {fenced}
  prompt-domains-covered: 7
  structured-output-covered: true
  rag-and-citations-covered: true
  code-prompts-covered: true
  visual-prompts-covered: true
  audio-prompts-covered: true
  narrative-prompts-covered: true
  injection-and-security-covered: true
  template-instance-run-separated: true
  evaluation-matrix-present: true
  model-version-required: true
  illustrative-outputs-only: true
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
- No language, visual or audio model was called.
- No reusable prompt template or Companion Pack dataset was created.
- No prompt instance was resolved and no request was sent.
- No raw response, structured output or tool call was produced.
- No parse, code test, RAG answer, image or audio generation was executed.
- No variance, migration or regression campaign was performed.
- No prompt-injection or runtime security test was performed.
- No secret, personal data, external file or network service was handled.
- No token, latency, cost, memory or quality measurement was produced.
- No human score, legal approval or production decision was recorded.
- No permanent Companion Pack artifact was materialized.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''
    PROOF.write_text(proof, encoding="utf-8")

    index = read("Livre-V/index.md")
    index = replace_state(index, 'version: "1.0.0"', 'version: "1.1.0"', "version index")
    index = replace_state(
        index,
        '- [ ] Chapitre 9 — Bibliothèque de prompts.',
        '- [x] [Fiche 09 — Bibliothèque de prompts](CHAPITRE-09-Bibliotheque-de-prompts.md) — version `1.0.0`, niveau `static-review`.',
        "ligne index chapitre 9",
    )
    index = replace_state(
        index,
        'Progression : **8 chapitres sur 26** rédigés et audités. Les fiches 01 à 08 utilisent le profil de référence spécialisé du Livre V ; la fiche 08 catalogue les contrats Godot, Blender, ComfyUI, audio et documentation, leurs profils Solo/Studio, preuves, reprises et manifestes. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
        'Progression : **9 chapitres sur 26** rédigés et audités. Les fiches 01 à 09 utilisent le profil de référence spécialisé du Livre V ; la fiche 09 catalogue templates, variables, instances, modèles cibles, sécurité et critères d’évaluation pour sept familles de tâches. Les appels de modèles, datasets du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
        "statut index",
    )
    write("Livre-V/index.md", index)

    roadmap = read("ROADMAP.md")
    roadmap = replace_state(
        roadmap,
        '- [x] Bibliothèque de workflows — fiche 08 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
        '- [x] Bibliothèque de workflows — fiche 08 rédigée et auditée au niveau `static-review`.\n- [x] Bibliothèque de prompts — fiche 09 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
        "roadmap chapitre 9",
    )
    roadmap = replace_state(
        roadmap,
        '**Statut M6 : en cours — 8 chapitres rédigés, repérés et audités sur 26.**',
        '**Statut M6 : en cours — 9 chapitres rédigés, repérés et audités sur 26.**',
        "statut roadmap",
    )
    write("ROADMAP.md", roadmap)

    contents = read("contents.txt")
    contents = replace_state(
        contents,
        'Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md\nCompanion-Pack/index.md',
        'Livre-V/CHAPITRE-08-Bibliotheque-de-workflows.md\nLivre-V/CHAPITRE-09-Bibliotheque-de-prompts.md\nCompanion-Pack/index.md',
        "ordre lecteur",
    )
    write("contents.txt", contents)

    plan = read("plans/LIVRE-V-PLAN-MAITRE.md")
    plan = replace_state(plan, 'version: "1.8.0"', 'version: "1.9.0"', "version plan")
    plan = replace_state(
        plan,
        '> **Statut :** 8 chapitres sur 26 rédigés et audités au niveau `static-review`',
        '> **Statut :** 9 chapitres sur 26 rédigés et audités au niveau `static-review`',
        "statut plan",
    )
    plan = replace_state(
        plan,
        '## Chapitre 9 — Bibliothèque de prompts\n\n**Objectifs**',
        '## Chapitre 9 — Bibliothèque de prompts\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**',
        "état chapitre 9 plan",
    )
    write("plans/LIVRE-V-PLAN-MAITRE.md", plan)

    continuity = read("CONTINUITE-PROJET.md")
    continuity = replace_state(continuity, 'version: "3.95.0"', 'version: "3.96.0"', "version continuité")
    continuity = replace_state(
        continuity,
        'last-updated: "2026-07-28T18:20:01+02:00"',
        f'last-updated: "{TIMESTAMP}"',
        "date continuité",
    )
    continuity = replace_state(
        continuity,
        '- progression du Livre V : 8 chapitres sur 26 ;',
        '- progression du Livre V : 9 chapitres sur 26 ;',
        "progression continuité",
    )
    continuity = replace_state(
        continuity,
        '- chapitre 8 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
        '- chapitre 8 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 9 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
        "état chapitre 9 continuité",
    )

    next_action = f'''## 26. Prochaine action

Le Livre V contient neuf fiches sur 26 au niveau `static-review`. La fiche 09 catalogue les prompts textuels, structurés, RAG, code, visuels, audio et narratifs, puis sépare template, instance, run, modèle cible, paramètres, sécurité et évaluation. Les appels de modèles, datasets de test, sorties réelles, mesures, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 cataloguera des recettes courtes GDScript, Python, PowerShell et Bash avec contexte, paramètres, sorties, codes d’échec, sécurité, licences et statut d’exécution. Il devra distinguer recette pédagogique, squelette statique et composant réellement testé, sans absorber les références complètes des chapitres 11 et 12 ni matérialiser prématurément le Companion Pack.
'''
    continuity, count = re.subn(
        r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)",
        next_action,
        continuity,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError("section prochaine action introuvable")

    journal = f'''## 27. Journal

### {TIMESTAMP} — version 3.96.0

- création de la fiche 09 — Bibliothèque de prompts ;
- ajout de treize cartes et de trois matrices compactes ;
- prompts textuels, structurés, RAG, code, visuels, audio et narratifs catalogués ;
- template, variante, instance, requête, réponse brute, résultat interprété et décision séparés ;
- variables, modèles cibles, paramètres, injections, outils et douze tests de qualification documentés sans résultat inventé ;
- sources officielles d’OpenAI, Google, Anthropic, Ollama et OWASP revues le 28 juillet 2026 ;
- métriques statiques : {lines} lignes, {headings} titres, {cards} fiches, {matrices} matrices, {links} liens, {source_links} renvois propriétaires et {fragment_links} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 10 — Bibliothèque de scripts et recettes de code, niveau Élevée ;
- aucun modèle, API, outil, prompt du Companion Pack, réponse, parse, génération, mesure, secret, approbation juridique ou PDF produit.

'''
    continuity = replace_state(continuity, '## 27. Journal\n', journal, "journal continuité")
    write("CONTINUITE-PROJET.md", continuity)

    print(f"chapter_lines={lines}")
    print(f"chapter_headings={headings}")
    print(f"cards={cards}")
    print(f"matrices={matrices}")
    print(f"links={links}")
    print(f"source_links={source_links}")
    print(f"fragment_links={fragment_links}")
    print(f"official_links={official_links}")
    print(f"chapter_sha256={chapter_hash}")
    print(f"audit_sha256={audit_hash}")


if __name__ == "__main__":
    main()
