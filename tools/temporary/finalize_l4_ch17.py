from __future__ import annotations

import base64
import gzip
import hashlib
import os
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TEMP = ROOT / "tools" / "temporary"
BRANCH = "docs/livre-iv-chapitre-17-publication-distribution"
TIMESTAMP = "2026-07-27T09:40:10+02:00"
DATE = "2026-07-27"
CHAPTER_PATH = ROOT / "Livre-IV" / "CHAPITRE-17-Publication-et-distribution.md"
AUDIT_PATH = ROOT / "Livre-IV" / "QA" / "AUDIT-CHAPITRE-17.md"
PROOF_PATH = ROOT / "Livre-IV" / "QA" / "VALIDATION-FINALE-CHAPITRE-17.yaml"

EXPECTED = {
    "CONTINUITE-PROJET.md",
    "Livre-IV/CHAPITRE-17-Publication-et-distribution.md",
    "Livre-IV/QA/AUDIT-CHAPITRE-17.md",
    "Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-17.yaml",
    "Livre-IV/index.md",
    "ROADMAP.md",
    "contents.txt",
    "plans/LIVRE-IV-PLAN-MAITRE.md",
}


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def decode_gzip_b64(path: Path) -> str:
    return gzip.decompress(base64.b64decode(path.read_text(encoding="utf-8"))).decode("utf-8")


def replace_once(text: str, old: str, new: str, name: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{name}: motif attendu exactement une fois, trouvé {count}")
    return text.replace(old, new, 1)


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def count_blocks(text: str) -> tuple[int, int, list[str]]:
    blocks = re.findall(r"```[^\n]*\n(.*?)\n```", text, re.S)
    significant = []
    for block in blocks:
        normalized = "\n".join(line.rstrip() for line in block.strip().splitlines())
        meaningful = [line for line in normalized.splitlines() if line.strip()]
        if len(meaningful) >= 4 or len(normalized) >= 180:
            significant.append(normalized)
    return len(blocks), len(significant), significant


def duplicate_paragraphs(text: str) -> int:
    paragraphs: list[str] = []
    in_fence = False
    current: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            current = []
            continue
        if in_fence or not line.strip() or line.lstrip().startswith(("#", ">", "- ", "* ", "|", "<!--")):
            if current:
                value = re.sub(r"\s+", " ", " ".join(current).strip().casefold())
                if len(value) >= 180:
                    paragraphs.append(value)
                current = []
            continue
        current.append(line.strip())
    if current:
        value = re.sub(r"\s+", " ", " ".join(current).strip().casefold())
        if len(value) >= 180:
            paragraphs.append(value)
    counts = Counter(paragraphs)
    return sum(value - 1 for value in counts.values() if value > 1)


def validate_chapter(chapter: str, audit: str) -> None:
    if not chapter.startswith("---\n"):
        raise RuntimeError("front matter absent")
    front_end = chapter.find("\n---\n", 4)
    front = yaml.safe_load(chapter[4:front_end])
    required_front = {
        "id": "DOC-L4-CH17",
        "status": "reviewed",
        "version": "1.0.0",
        "chapter": 17,
        "audit-level": "static-review",
    }
    for key, expected in required_front.items():
        if front.get(key) != expected:
            raise RuntimeError(f"front matter {key}: {front.get(key)!r} != {expected!r}")
    if "recommended-reasoning" in chapter or "Niveau GPT-5.6" in chapter or "Niveau de raisonnement conseillé" in chapter:
        raise RuntimeError("métadonnée ou recommandation de raisonnement présente")
    if re.search(r"^## .*Prochaine (?:étape|action)", chapter, re.M | re.I):
        raise RuntimeError("prochaine étape présente dans le chapitre lecteur")
    if "PDF du chapitre" in chapter or "construire le PDF" in chapter:
        raise RuntimeError("chaîne PDF présente dans le chapitre lecteur")
    if len(chapter.splitlines()) != 2435:
        raise RuntimeError(f"lignes inattendues: {len(chapter.splitlines())}")
    headings = re.findall(r"^#{1,6}\s+(.+?)\s*$", chapter, re.M)
    normalized_headings = [re.sub(r"\s+", " ", re.sub(r"[*_~`]", "", item).strip().casefold()) for item in headings]
    duplicates = [item for item, count in Counter(normalized_headings).items() if count > 1]
    if len(headings) != 95 or duplicates:
        raise RuntimeError(f"titres: total={len(headings)}, doublons={duplicates}")
    blocks_total, significant_total, significant = count_blocks(chapter)
    if blocks_total != 71 or significant_total != 67:
        raise RuntimeError(f"blocs: total={blocks_total}, significatifs={significant_total}")
    if len(set(significant)) != len(significant):
        raise RuntimeError("bloc significatif dupliqué")
    if duplicate_paragraphs(chapter):
        raise RuntimeError("paragraphe long dupliqué")
    if chapter.count("<!-- qa:code-explanation -->") != 71:
        raise RuntimeError("nombre de marqueurs d’explication inattendu")
    if chapter.count("**Explication structurée du bloc :**") != 51:
        raise RuntimeError("nombre d’explications structurées inattendu")
    if chapter.count("**Pourquoi cet exemple est fautif :**") != 10:
        raise RuntimeError("nombre d’explications fautives inattendu")
    if chapter.count("**Pourquoi la correction fonctionne :**") != 10:
        raise RuntimeError("nombre d’explications corrigées inattendu")
    if chapter.count("**Exemple fautif :**") != 10 or chapter.count("**Exemple corrigé :**") != 10:
        raise RuntimeError("nombre d’exemples diagnostic inattendu")
    markers = ("[PS]", "[CMD]", "[WSL]", "[DCT]", "[DCK]", "[VSC]", "[WEB]", "[APP]", "[SORTIE]", "[LECTURE]")
    body = chapter.split("Voir la [convention complète]", 1)[1]
    missing = [marker for marker in markers if marker not in body]
    if missing:
        raise RuntimeError(f"repères absents: {missing}")
    if not chapter.rstrip().endswith("n’est revendiquée."):
        raise RuntimeError("synthèse Asteria absente ou clôture inattendue")
    if "## 45. Synthèse opérationnelle pour `Project Asteria`" not in chapter:
        raise RuntimeError("synthèse Asteria absente")
    if "## 44. Références techniques officielles" not in chapter:
        raise RuntimeError("références techniques absentes")
    if "<!-- qa:error-correction-section -->" not in chapter:
        raise RuntimeError("marqueur de diagnostics absent")
    if "19,99 €" not in chapter or "currency: EUR" not in chapter:
        raise RuntimeError("cohérence monétaire française absente")
    if "USD" in chapter or "$19.99" in chapter:
        raise RuntimeError("devise générique non conforme")
    if not audit.startswith("---\n") or "id: \"DOC-L4-QA-AUDIT-CH17\"" not in audit:
        raise RuntimeError("audit invalide")
    if "recommended-reasoning" in audit or "Niveau GPT-5.6" in audit:
        raise RuntimeError("raisonnement présent dans l’audit")


def update_index() -> None:
    path = ROOT / "Livre-IV" / "index.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "0.17.0"', 'version: "0.18.0"', "index version")
    text = replace_once(text, 'last-updated: "2026-07-27T08:32:16+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
    text = replace_once(text, "17. Publication et distribution ;", "17. [Publication et distribution](CHAPITRE-17-Publication-et-distribution.md) — version `1.0.0`, niveau `static-review` ;", "index chapter")
    text = replace_once(text, "**16 sur 22**", "**17 sur 22**", "index progress")
    text = replace_once(text, "**chapitre 16 — Exports Godot et packaging**", "**chapitre 17 — Publication et distribution**", "index current")
    text = replace_once(text, "**chapitre 17 — Publication et distribution** ;", "**chapitre 18 — Accessibilité** ;", "index next")
    text = replace_once(text, "les chapitres 1 à 16 sont terminés", "les chapitres 1 à 17 sont terminés", "index status")
    write(path, text)


def update_roadmap() -> None:
    path = ROOT / "ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    anchor = "- [x] Chapitre 16 — Exports Godot et packaging — rédigé, repéré et audité au niveau `static-review`.\n"
    addition = anchor + "- [x] Chapitre 17 — Publication et distribution — rédigé, repéré et audité au niveau `static-review`.\n"
    text = replace_once(text, anchor, addition, "roadmap chapter")
    text = replace_once(text, "DevOps, publication et maintenance — 3 chapitres sur 9.", "DevOps, publication et maintenance — 4 chapitres sur 9.", "roadmap group")
    text = replace_once(text, "16 chapitres rédigés, repérés et audités sur 22.", "17 chapitres rédigés, repérés et audités sur 22.", "roadmap status")
    write(path, text)


def update_contents() -> None:
    path = ROOT / "contents.txt"
    text = path.read_text(encoding="utf-8")
    anchor = "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md\n"
    text = replace_once(text, anchor, anchor + "Livre-IV/CHAPITRE-17-Publication-et-distribution.md\n", "contents chapter")
    write(path, text)


def update_master_plan() -> None:
    path = ROOT / "plans" / "LIVRE-IV-PLAN-MAITRE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "1.0.16"', 'version: "1.0.17"', "plan version")
    text = replace_once(text, 'last-updated: "2026-07-27T08:32:16+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
    text = replace_once(text, "> **Statut :** en cours — 16 chapitres sur 22", "> **Statut :** en cours — 17 chapitres sur 22", "plan status")
    anchor = "Le marketing approfondi reste hors périmètre principal. Validation par dry-run de soumission et conformité documentaire."
    addition = anchor + "\n\n**État documentaire au 2026-07-27 :** chapitre rédigé, repéré et audité au niveau `static-review`. Le dossier de publication, les fiches produit, médias, canaux, clés, classifications, déclarations, soumissions, calendrier, lancement et support sont préparés sans revendiquer de compte, page, téléversement, revue, approbation, vente ou lancement public."
    text = replace_once(text, anchor, addition, "plan chapter state")
    write(path, text)


def update_continuity() -> None:
    path = ROOT / "CONTINUITE-PROJET.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "3.79.0"', 'version: "3.80.0"', "continuity version")
    text = replace_once(text, 'last-updated: "2026-07-27T08:32:16+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp")
    rules_anchor = "- ne pas supprimer une génération avant expiration, contrôle juridique et remplacement vérifié ;\n"
    publication_rules = (
        rules_anchor
        + "- ne pas reconstruire un package pendant sa soumission ou sa promotion vers une boutique ;\n"
        + "- ne pas confondre présence d’un build, envoi en revue, approbation et publication publique ;\n"
        + "- ne pas publier une affirmation de fiche produit sans preuve reliée à un build ou une fonctionnalité réelle ;\n"
        + "- ne pas réutiliser une classification d’âge ou une déclaration de confidentialité d’une autre version sans revue ;\n"
        + "- ne pas verser un secret, une clé d’accès ou un credential de boutique dans le dépôt ou un journal ;\n"
        + "- ne pas traiter un canal interne, fermé ou preview comme une sortie publique ;\n"
        + "- ne pas générer des clés d’accès sans lot, propriétaire, finalité, quantité, expiration et révocation ;\n"
        + "- ne pas figer dans la procédure des dimensions, délais ou champs de portail susceptibles d’évoluer sans registre de vérification ;\n"
        + "- ne pas annoncer une date de lancement sans portes techniques, juridiques, support et décision de retour arrière ;\n"
        + "- ne pas présenter une soumission illustrative ou un dry-run documentaire comme une revue réellement exécutée ;\n"
    )
    text = replace_once(text, rules_anchor, publication_rules, "continuity publication rules")
    text = replace_once(text, "- progression du Livre IV : 16 chapitres sur 22 ;", "- progression du Livre IV : 17 chapitres sur 22 ;", "continuity progress")
    text = replace_once(text, "- chapitre 16 du Livre IV : version `1.0.0`, niveau `static-review` ;", "- chapitre 16 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 17 du Livre IV : version `1.0.0`, niveau `static-review` ;", "continuity chapter")
    next_section = f'''## 26. Prochaine action

Les chapitres 1 à 17 du Livre IV sont terminés au niveau documentaire et statique. Les comptes de publication, fiches produit, médias, prix, classifications, déclarations de confidentialité, clés d’accès, téléversements, soumissions, revues, approbations, ventes, lancements et opérations de support de `Project Asteria` restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-18-Accessibilite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 18 du Livre IV couvrira commandes, visuel, audio, cognition et motricité, préparera remapping, sous-titres, contrastes et options de rythme, organisera scénarios avec profils et utilisateurs, documentera les limites connues et préparera une déclaration publique d’accessibilité du produit complet.

## 27. Journal

### {TIMESTAMP} — version 3.80.0

- création du chapitre 17 du Livre IV — Publication et distribution ;
- export, package, artefact, build boutique, soumission, approbation, publication et lancement distingués ;
- dossier de publication, identités produit, matrice des boutiques et registre des exigences volatiles documentés ;
- même candidat binaire, manifestes et empreintes du chapitre 16 réutilisés sans reconstruction ;
- fiches produit, affirmations, exigences système, médias, droits, textes alternatifs, tags et catégories encadrés ;
- prix candidats en euros, territoires, contrats, licences, attributions, classifications d’âge et déclarations de confidentialité préparés ;
- rôles, MFA, secrets, canaux, clés d’accès, Steam, itch.io, Google Play, App Store Connect et boutiques supplémentaires qualifiés ;
- calendrier, dry-run, reçus, go/no-go, lancement, support, métriques et procédures Solo/Studio préparés ;
- métriques statiques : 2435 lignes, 95 titres, 67 blocs significatifs, 51 explications structurées et dix diagnostics ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 18 — Accessibilité, niveau Élevée ;
- aucun compte, page boutique, média final, prix réel, classification, formulaire, clé, téléversement, soumission, revue, vente, lancement runtime ou PDF du Livre IV produit.
'''
    pattern = re.compile(r"## 26\. Prochaine action\n.*?\n## 27\. Journal\n", re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"continuity next section: {len(matches)} matches")
    text = text[:matches[0].start()] + next_section + text[matches[0].end():]
    write(path, text)


def write_proof(chapter: str, audit: str) -> None:
    proof = (TEMP / "ch17.proof.template").read_text(encoding="utf-8")
    proof = proof.replace("__CHAPTER_SHA256__", sha256(chapter))
    proof = proof.replace("__AUDIT_SHA256__", sha256(audit))
    proof = proof.replace("__RUN_ID__", os.environ.get("GITHUB_RUN_ID", "not-available"))
    write(PROOF_PATH, proof)


def cleanup() -> None:
    for path in [
        TEMP / "ch17.chapter.001.b64",
        TEMP / "ch17.audit.001.b64",
        TEMP / "ch17.proof.template",
        TEMP / "ch17.start",
        TEMP / "finalize_l4_ch17.py",
        ROOT / ".github" / "workflows" / "livre-iv-ch17-finalizer.yml",
    ]:
        path.unlink(missing_ok=True)


def verify_final_diff() -> None:
    subprocess.check_call(["git", "add", "-A"], cwd=ROOT)
    changed = set(run("git", "diff", "--cached", "--name-only", "origin/main").splitlines())
    if changed != EXPECTED:
        raise RuntimeError(f"diff final inattendu: {sorted(changed)}")


def main() -> None:
    chapter = decode_gzip_b64(TEMP / "ch17.chapter.001.b64")
    audit = decode_gzip_b64(TEMP / "ch17.audit.001.b64")
    validate_chapter(chapter, audit)
    write(CHAPTER_PATH, chapter)
    write(AUDIT_PATH, audit)
    update_index()
    update_roadmap()
    update_contents()
    update_master_plan()
    update_continuity()
    write_proof(chapter, audit)
    cleanup()
    verify_final_diff()
    print("Livre IV chapitre 17 finalisé; huit fichiers permanents prêts.")


if __name__ == "__main__":
    main()
