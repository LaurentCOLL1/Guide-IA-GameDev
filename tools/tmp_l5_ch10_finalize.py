#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md"
AUDIT = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-10.md"
PROOF = ROOT / "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-10.yaml"
INDEX = ROOT / "Livre-V/index.md"
ROADMAP = ROOT / "ROADMAP.md"
CONTENTS = ROOT / "contents.txt"
PLAN = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
TIMESTAMP = "2026-07-28T21:24:52+02:00"
BASE_COMMIT = "edb7992232b19f2aa2ec492422ac3830ca9f30ca"
BRANCH = "docs/livre-v-ch10-scripts-recettes-code"

LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>.*)$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: remplacement attendu une fois, trouvé {count}")
    return text.replace(old, new, 1)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chapter_metrics(text: str) -> dict[str, int]:
    lines = text.splitlines()
    headings = 0
    fences = 0
    inside = False
    fence_char = ""
    fence_len = 0
    for line in lines:
        stripped = line.strip()
        match = FENCE_RE.match(stripped)
        if match:
            token = match.group("fence")
            if not inside:
                inside = True
                fence_char = token[0]
                fence_len = len(token)
                fences += 1
            elif token[0] == fence_char and len(token) >= fence_len and not match.group("lang").strip():
                inside = False
            continue
        if not inside and HEADING_RE.match(line):
            headings += 1

    links = LINK_RE.findall(text)
    targets = [target.strip().split()[0].strip("<>") for _, target in links]
    source_targets = [
        target
        for target in targets
        if re.match(r"^\.\./Livre-(?:I|II|III|IV)/", target)
    ]
    fragment_targets = [target for target in source_targets if "#" in target]
    official_targets = [target for target in targets if target.startswith(("https://", "http://"))]
    return {
        "lines": len(lines),
        "headings": headings,
        "cards": text.count("<!-- l5:card -->"),
        "matrices": text.count("<!-- l5:matrix -->"),
        "links": len(links),
        "source_links": len(source_targets),
        "fragment_links": len(fragment_targets),
        "official_links": len(official_targets),
        "fenced_blocks": fences,
    }


def patch_static_snippets() -> str:
    text = read(CHAPTER)
    text = replace_once(
        text,
        'if ($nativeCode -ne 0) {\n    Write-Error "native_command_failed:$nativeCode"\n    exit $nativeCode\n}',
        'if ($nativeCode -ne 0) {\n    [Console]::Error.WriteLine("native_command_failed:$nativeCode")\n    exit $nativeCode\n}',
        "propagation du code natif PowerShell",
    )
    text = replace_once(
        text,
        'readonly bytes=$(wc -c < "$input")\nprintf \'%s\\t%s\\n\' "$input" "$bytes"',
        'bytes=$(wc -c < "$input")\nreadonly bytes\nprintf \'%s\\t%s\\n\' "$input" "$bytes"',
        "statut de la substitution Bash",
    )
    write(CHAPTER, text)
    return text


def build_audit(metrics: dict[str, int]) -> str:
    return f'''---
title: "Audit — Livre V, fiche 10 : Bibliothèque de scripts et recettes de code"
id: "DOC-L5-QA-AUDIT-CH10"
status: "complete"
version: "1.0.0"
last-verified: "{TIMESTAMP}"
lang: "fr-FR"
book: "Livre V"
chapter: 10
audit-date: "{TIMESTAMP}"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 10 : Bibliothèque de scripts et recettes de code

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V sous réserve des exécutions explicitement laissées ouvertes. Elle catalogue des recettes GDScript, Python, PowerShell et Bash, distingue squelettes statiques et composants qualifiés, et ne présente aucun bloc comme parsé, testé ou prêt pour la production.

## 2. Périmètre contrôlé

- chemin canonique : `Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md` ;
- identifiant : `DOC-L5-CH10` ;
- version : `1.0.0` ;
- format : `reference-cards` ;
- niveau de preuve : `static-review` ;
- documentations officielles de Godot, Python, PowerShell et Bash revues le 28 juillet 2026 ;
- aucune compilation PDF intermédiaire.

## 3. Métriques statiques

| Mesure | Valeur |
|---|---:|
| lignes | {metrics['lines']} |
| titres | {metrics['headings']} |
| cartes `l5:card` | {metrics['cards']} |
| matrices `l5:matrix` | {metrics['matrices']} |
| liens Markdown | {metrics['links']} |
| renvois vers les Livres I à IV | {metrics['source_links']} |
| liens profonds vers les sources propriétaires | {metrics['fragment_links']} |
| liens officiels | {metrics['official_links']} |
| blocs clôturés | {metrics['fenced_blocks']} |

## 4. Couverture du plan maître

| Exigence | Couverture |
|---|---|
| scripts courts GDScript | règle pure et contrôle `SceneTree` headless |
| scripts courts Python | CLI de staging et chargeur JSON borné |
| scripts courts PowerShell | wrapper de programme natif et propagation du code |
| scripts courts Bash | contrôle de fichier avec statuts explicites |
| contexte et paramètres | environnement, entrées, bornes et dossier courant par carte |
| sorties et erreurs | stdout, stderr, fichiers, codes et sorties partielles distingués |
| recette pédagogique et production | taxonomie de huit statuts de preuve |
| exemples d’appel | appels Godot et Python explicitement non exécutés |
| tests minimaux | douze contrôles par recette et campagne Q1 à Q12 |
| licences | source, snippet, dépendance, fixture et publication distingués |
| code complexe | maintenu hors fiche et réservé au Companion Pack |
| exécution ou statut statique | chaque bloc porte `static-skeleton` et la réserve associée |

## 5. Frontières

La fiche conserve les responsabilités suivantes :

- les tutoriels détaillés restent dans les Livres I à IV ;
- la fiche 08 conserve workflows et orchestration ;
- la fiche 09 conserve prompts et critères d’évaluation ;
- le chapitre 10 conserve les recettes courtes et leur index ;
- les chapitres 11 et 12 conserveront les références GDScript et Python ;
- le chapitre 13 conservera les formats d’échange ;
- les diagnostics transversaux resteront au chapitre 20 ;
- les campagnes et mesures resteront au chapitre 21 ;
- les compatibilités, checklists et licences resteront aux chapitres 22, 24 et 25 ;
- les fichiers exécutables réels resteront au Companion Pack.

## 6. Séparation définition et exécution

Les cartes distinguent `pedagogical`, `static-skeleton`, `syntax-checked`, `unit-tested`, `integration-tested`, `qualified`, `production` et `withdrawn`. Aucune carte n’annonce :

- un parse GDScript ou un lancement Godot ;
- une compilation, un import ou un test Python ;
- une analyse ou une exécution PowerShell ;
- un `bash -n` ou une exécution WSL ;
- un programme natif réellement appelé ;
- un workspace temporaire, une fixture ou un fichier de staging produit ;
- une compatibilité multiplateforme ou une performance mesurée.

## 7. Code et repères

Les {metrics['fenced_blocks']} blocs sont précédés d’un repère d’utilisation reconnu. Chaque recette nomme entrées, sorties, erreurs, effets et statut. Le validateur d’explication détaillée ne s’applique pas au Livre V, mais les blocs restent proportionnés et renvoient aux tutoriels propriétaires.

## 8. Sécurité et licences

Les contrôles couvrent chemins canoniques, staging, sorties partielles, programmes allowlistés, arguments séparés, secrets, réseau, privilèges, fichiers tiers, empreintes, licences des snippets et dépendances. Une petite taille de script n’est jamais assimilée à un faible rayon d’impact.

## 9. Liens et sources

Les {metrics['source_links']} renvois vers les Livres I à IV évitent de recopier les cours de langage, les tests, la sécurité et l’automatisation. Les {metrics['fragment_links']} fragments ciblent notamment la nature de GDScript, les codes PowerShell, les tests, les journaux et les frontières de workspace.

Les liens externes pointent vers les documentations officielles de Godot 4.7, Python 3.14, PowerShell 7.6 et GNU Bash revues le 28 juillet 2026. Leur présence ne constitue ni installation, ni parse, ni exécution.

## 10. Réserves ouvertes

1. aucun fichier GDScript parsé et aucun moteur Godot lancé ;
2. aucun module Python compilé, importé ou exécuté ;
3. aucun script PowerShell analysé ou exécuté ;
4. aucun script Bash vérifié et aucun WSL utilisé ;
5. aucune fixture, arborescence temporaire ou sortie de staging créée ;
6. aucun programme natif, processus enfant ou timeout testé ;
7. aucun chemin sortant, lien symbolique, secret ou injection testé ;
8. aucune dépendance installée, verrouillée ou reconstruite ;
9. aucune campagne d’idempotence, interruption, repli ou retrait réalisée ;
10. aucune mesure de durée, mémoire, portabilité ou performance produite ;
11. aucune approbation juridique ni artefact permanent du Companion Pack matérialisé ;
12. aucun PDF produit ; licence globale et balisage avancé ouverts.

## 11. Critère d’acceptation

La fiche est acceptée au niveau `static-review` lorsque les validateurs permanents confirment structure, métadonnées, liens locaux, cartes, matrices, liens profonds, repères de tous les blocs et absence de PDF. Les recettes restent `static-reviewed` jusqu’à leurs campagnes propres dans des environnements enregistrés.
'''


def build_proof(metrics: dict[str, int], chapter_sha: str, audit_sha: str) -> str:
    return f'''schema-version: 2
evidence-id: DOC-L5-QA-EVIDENCE-CH10
validation-authority: livre-v-reference-profile
status: complete
validation-date: '2026-07-28'
validated-base-commit: {BASE_COMMIT}
source-branch: {BRANCH}
chapter:
  id: DOC-L5-CH10
  path: Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md
  version: 1.0.0
  document-format: reference-cards
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 12
  chapter-lines: {metrics['lines']}
  chapter-headings: {metrics['headings']}
  reference-cards: {metrics['cards']}
  matrices: {metrics['matrices']}
  internal-links: {metrics['links']}
  source-book-links: {metrics['source_links']}
  fragment-links: {metrics['fragment_links']}
  official-links: {metrics['official_links']}
  fenced-blocks: {metrics['fenced_blocks']}
  languages-covered: 4
  gdscript-covered: true
  python-covered: true
  powershell-covered: true
  bash-covered: true
  status-taxonomy-present: true
  exit-codes-covered: true
  tests-and-fixtures-covered: true
  security-and-licenses-covered: true
  static-skeletons-only: true
  runtime-results-invented: false
  companion-pack-boundary-preserved: true
  tutorial-boundary-preserved: true
  master-plan-scope-covered: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_sha}
  audit-sha256: {audit_sha}
ci:
  permanent-validations:
    status: pending-recording-after-pr-run
reservations:
- No GDScript file was parsed and no Godot engine was launched.
- No Python module was compiled, imported or executed.
- No PowerShell script was parsed or executed.
- No Bash script was syntax-checked and no WSL session was used.
- No fixture, temporary workspace or staging output was created.
- No native command, child process or timeout was exercised.
- No path escape, symbolic link, secret or injection test was performed.
- No dependency was installed, locked or rebuilt.
- No idempotence, interruption, fallback or withdrawal campaign was performed.
- No duration, memory, portability or performance measurement was produced.
- No legal approval or permanent Companion Pack artifact was materialized.
- No PDF was produced; collection licence and advanced accessibility tagging remain open.
'''


def update_governance(metrics: dict[str, int]) -> None:
    index = read(INDEX)
    index = replace_once(index, 'version: "1.1.0"', 'version: "1.2.0"', "version index")
    index = replace_once(
        index,
        '- [ ] Chapitre 10 — Bibliothèque de scripts et recettes de code.',
        '- [x] [Fiche 10 — Bibliothèque de scripts et recettes de code](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md) — version `1.0.0`, niveau `static-review`.',
        "ligne index chapitre 10",
    )
    index = replace_once(
        index,
        'Progression : **9 chapitres sur 26** rédigés et audités. Les fiches 01 à 09 utilisent le profil de référence spécialisé du Livre V ; la fiche 09 catalogue templates, variables, instances, modèles cibles, sécurité et critères d’évaluation pour sept familles de tâches. Les appels de modèles, datasets du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
        'Progression : **10 chapitres sur 26** rédigés et audités. Les fiches 01 à 10 utilisent le profil de référence spécialisé du Livre V ; la fiche 10 catalogue recettes GDScript, Python, PowerShell et Bash, statuts de preuve, codes de sortie, tests, sécurité et licences. Les exécutions runtime, fichiers du Companion Pack, benchmarks, licence globale et formats de publication avancés restent des chantiers distincts.',
        "statut index",
    )
    write(INDEX, index)

    roadmap = read(ROADMAP)
    roadmap = replace_once(
        roadmap,
        '- [x] Bibliothèque de prompts — fiche 09 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
        '- [x] Bibliothèque de prompts — fiche 09 rédigée et auditée au niveau `static-review`.\n- [x] Bibliothèque de scripts et recettes de code — fiche 10 rédigée et auditée au niveau `static-review`.\n- [x] Arbres de décision et matrices — fiche 02 rédigée et auditée au niveau `static-review`.',
        "roadmap chapitre 10",
    )
    roadmap = replace_once(
        roadmap,
        '**Statut M6 : en cours — 9 chapitres rédigés, repérés et audités sur 26.**',
        '**Statut M6 : en cours — 10 chapitres rédigés, repérés et audités sur 26.**',
        "statut M6",
    )
    write(ROADMAP, roadmap)

    contents = read(CONTENTS)
    contents = replace_once(
        contents,
        'Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md\nCompanion-Pack/index.md',
        'Livre-V/CHAPITRE-09-Bibliotheque-de-prompts.md\nLivre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md\nCompanion-Pack/index.md',
        "ordre lecteur chapitre 10",
    )
    write(CONTENTS, contents)

    plan = read(PLAN)
    plan = replace_once(plan, 'version: "1.9.0"', 'version: "1.10.0"', "version plan")
    plan = replace_once(
        plan,
        '> **Statut :** 9 chapitres sur 26 rédigés et audités au niveau `static-review`',
        '> **Statut :** 10 chapitres sur 26 rédigés et audités au niveau `static-review`',
        "statut plan",
    )
    plan = replace_once(
        plan,
        '## Chapitre 10 — Bibliothèque de scripts et recettes de code\n\n**Objectifs**',
        '## Chapitre 10 — Bibliothèque de scripts et recettes de code\n\n**État documentaire :** rédigé en version `1.0.0`, niveau `static-review`, au format fiches de référence.\n\n**Objectifs**',
        "état documentaire chapitre 10",
    )
    write(PLAN, plan)

    continuity = read(CONTINUITY)
    continuity = replace_once(continuity, 'version: "3.96.0"', 'version: "3.97.0"', "version continuité")
    continuity = replace_once(
        continuity,
        'last-updated: "2026-07-28T19:12:00+02:00"',
        f'last-updated: "{TIMESTAMP}"',
        "date continuité",
    )
    continuity = replace_once(
        continuity,
        '- progression du Livre V : 9 chapitres sur 26 ;',
        '- progression du Livre V : 10 chapitres sur 26 ;',
        "progression continuité",
    )
    continuity = replace_once(
        continuity,
        '- chapitre 9 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
        '- chapitre 9 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- chapitre 10 du Livre V : version `1.0.0`, niveau `static-review`, format `reference-cards` ;\n- profil éditorial du Livre V',
        "état chapitre 10 continuité",
    )
    old_next = '''Le Livre V contient neuf fiches sur 26 au niveau `static-review`. La fiche 09 catalogue les prompts textuels, structurés, RAG, code, visuels, audio et narratifs, puis sépare template, instance, run, modèle cible, paramètres, sécurité et évaluation. Les appels de modèles, datasets de test, sorties réelles, mesures, approbations juridiques, artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 cataloguera des recettes courtes GDScript, Python, PowerShell et Bash avec contexte, paramètres, sorties, codes d’échec, sécurité, licences et statut d’exécution. Il devra distinguer recette pédagogique, squelette statique et composant réellement testé, sans absorber les références complètes des chapitres 11 et 12 ni matérialiser prématurément le Companion Pack.'''
    new_next = '''Le Livre V contient dix fiches sur 26 au niveau `static-review`. La fiche 10 catalogue les recettes courtes GDScript, Python, PowerShell et Bash, puis sépare squelette statique, syntaxe, tests, qualification, effets de bord, codes, sécurité et licences. Les parses et exécutions réels, fichiers du Companion Pack, benchmarks, approbations juridiques, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-11-Reference-GDScript.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 11 fournira une référence non linéaire de GDScript pour Godot 4.7.1 : syntaxe, types, fonctions, classes, annotations, collections, opérateurs et pièges versionnés. Il devra renvoyer au chapitre pédagogique du Livre II, éviter de devenir un second cours complet et ne présenter aucun exemple comme exécuté sans preuve.'''
    continuity = replace_once(continuity, old_next, new_next, "prochaine action continuité")
    journal = f'''### {TIMESTAMP} — version 3.97.0

- création de la fiche 10 — Bibliothèque de scripts et recettes de code ;
- ajout de treize cartes, trois matrices et {metrics['fenced_blocks']} blocs contrôlés ;
- recettes GDScript, Python, PowerShell et Bash cataloguées ;
- statuts pédagogique, squelette, syntaxe, tests, qualification, production et retrait séparés ;
- entrées, sorties, codes, effets de bord, sécurité, licences et douze tests de qualification documentés sans exécution inventée ;
- documentations officielles de Godot 4.7, Python 3.14, PowerShell 7.6 et Bash revues le 28 juillet 2026 ;
- métriques statiques : {metrics['lines']} lignes, {metrics['headings']} titres, {metrics['cards']} fiches, {metrics['matrices']} matrices, {metrics['links']} liens, {metrics['source_links']} renvois vers les Livres I à IV et {metrics['fragment_links']} liens profonds ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- prochaine action déplacée vers la fiche 11 — Référence GDScript, niveau Élevée ;
- aucun parseur, moteur, shell, test, fixture, processus, secret, réseau, artefact du Companion Pack, approbation juridique ou PDF produit.


'''
    continuity = replace_once(
        continuity,
        '### 2026-07-28T19:12:00+02:00 — version 3.96.0',
        journal + '### 2026-07-28T19:12:00+02:00 — version 3.96.0',
        "journal continuité",
    )
    write(CONTINUITY, continuity)


def main() -> None:
    chapter = patch_static_snippets()
    metrics = chapter_metrics(chapter)
    expected = {"cards": 13, "matrices": 3, "headings": 18, "fenced_blocks": 8}
    for key, value in expected.items():
        if metrics[key] != value:
            raise RuntimeError(f"métrique {key}: attendu {value}, obtenu {metrics[key]}")
    if metrics["source_links"] < 16 or metrics["fragment_links"] < 16:
        raise RuntimeError(f"densité de liens insuffisante: {metrics}")

    audit = build_audit(metrics)
    write(AUDIT, audit)
    chapter_sha = sha256_text(chapter)
    audit_sha = sha256_text(audit)
    write(PROOF, build_proof(metrics, chapter_sha, audit_sha))
    update_governance(metrics)

    print("Fiche 10 finalisée")
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print(f"chapter_sha256: {chapter_sha}")
    print(f"audit_sha256: {audit_sha}")


if __name__ == "__main__":
    main()
