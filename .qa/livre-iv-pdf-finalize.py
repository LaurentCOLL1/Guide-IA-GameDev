from pathlib import Path
import subprocess

TS = "2026-07-28T07:28:40+02:00"
DATE = "2026-07-28"
READER_HEAD = "f6b2118daf23edf7595ce9d5e2b4d300c00b1d40"
FINAL_RUN = 30331869053
FINAL_ARTIFACT = 8677727006
FINAL_DIGEST = "sha256:0109aa765694cee0c6cc2663e83a3310485e5915517e3c0c35fcb95b43ac59ce"
PDF_SHA = "013f8d9bf800d74b408c806f5b5ea6e291e85568b152799feb2b75152de7f9fe"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


roadmap_path = Path("ROADMAP.md")
roadmap = read(str(roadmap_path))
roadmap = replace_once(
    roadmap,
    "**Statut M5 : rédaction documentaire terminée — 22 chapitres rédigés, repérés et audités sur 22.** La construction, le préflight et l’inspection du PDF complet, ainsi que les réserves runtime, de licence et d’accessibilité, restent à traiter avant publication technique.",
    "**Statut M5 : terminé — 22 chapitres rédigés, repérés et audités sur 22.** La validation documentaire transversale, la compilation Pandoc/XeLaTeX, le préflight structurel et l’inspection visuelle du PDF cumulatif sont réussis. Les réserves runtime, de licence globale et de balisage avancé d’accessibilité PDF restent des chantiers distincts de collection.",
    "ROADMAP M5 status",
)
roadmap = replace_once(
    roadmap,
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre II.\n",
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre II.\n"
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre III.\n"
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre IV.\n",
    "ROADMAP M8 publications",
)
write(roadmap_path, roadmap)

plan_path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
plan = read(str(plan_path))
plan = replace_once(plan, 'status: "active"', 'status: "complete"', "plan status")
plan = replace_once(plan, 'version: "1.0.22"', 'version: "1.0.23"', "plan version")
plan = replace_once(
    plan,
    'last-updated: "2026-07-28T05:41:07+02:00"',
    f'last-updated: "{TS}"',
    "plan timestamp",
)
plan = replace_once(
    plan,
    "> **Statut :** rédaction documentaire terminée — 22 chapitres sur 22  ",
    "> **Statut :** terminé — 22 chapitres validés et PDF inspecté  ",
    "plan display status",
)
closure_note = f"""## Clôture documentaire et PDF

**État au {DATE} :** les 22 chapitres sont rédigés, repérés et audités ; la validation documentaire transversale, la compilation Pandoc/XeLaTeX, le préflight structurel et l’inspection visuelle représentative du PDF cumulatif sont réussis. La preuve permanente est `Livre-IV/QA/VALIDATION-PUBLICATION-LIVRE-IV.yaml` et le rapport est `Livre-IV/QA/CLOTURE-LIVRE-IV.md`.

Les critères qui exigent un build de jeu exporté, des campagnes runtime, des mesures de performance, des installations, des restaurations, des mises à jour ou des rollbacks exécutés restent des réserves produit. Ils ne sont pas présentés comme satisfaits par la clôture documentaire et PDF.

"""
plan = replace_once(
    plan,
    "## Critères de clôture du Livre IV",
    closure_note + "## Critères de clôture du Livre IV",
    "plan closure insertion",
)
write(plan_path, plan)

continuity_path = Path("CONTINUITE-PROJET.md")
continuity = read(str(continuity_path))
continuity = replace_once(
    continuity, 'version: "3.85.0"', 'version: "3.86.0"', "continuity version"
)
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-28T05:41:07+02:00"',
    f'last-updated: "{TS}"',
    "continuity timestamp",
)
continuity = replace_once(
    continuity,
    "- jalon : M5 — Livre IV ;",
    "- jalon : M6 — Livre V ;",
    "continuity milestone",
)
continuity = replace_once(
    continuity,
    "- chapitre 22 du Livre IV : version `1.0.0`, niveau `static-review` ;\n",
    "- chapitre 22 du Livre IV : version `1.0.0`, niveau `static-review` ;\n"
    "- publication technique du Livre IV : validation transversale, compilation Pandoc/XeLaTeX, préflight et inspection visuelle terminés ;\n",
    "continuity Livre IV publication",
)
old_next = """Les 22 chapitres du Livre IV sont terminés au niveau documentaire et statique. Les archives, SBOM, copies indépendantes, restaurations, reconstructions, transferts de comptes, exercices de succession, décisions de fin de support et validations runtime de `Project Asteria` restent non matérialisés. La licence globale de la collection et l’accessibilité avancée des PDF restent ouvertes.

Action suivante :

> **[LECTURE] Lot de fin de Livre et niveau prévisionnel — Ne pas saisir.**

```text
Livre IV — construire, préflighter et inspecter le PDF complet
Niveau GPT-5.6 Sol recommandé : Élevée
```

Cette action doit compiler l’ordre lecteur de `contents.txt`, exclure les fichiers QA, contrôler structure et liens, inspecter le PDF complet et enregistrer les réserves d’accessibilité et de licence sans inventer de conformité."""
new_next = """Le Livre IV est terminé au niveau de publication technique documentaire : 22 chapitres sur 22, validation transversale, compilation Pandoc/XeLaTeX, préflight et inspection visuelle réussis. Les exécutions runtime, la licence globale de la collection et le balisage avancé des PDF restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 1 du Livre V construira la carte générale de la collection, les dépendances entre Volume 0, Livres I à V et Companion Pack, les parcours Solo/Studio, les entrées par besoin et l’index des prérequis, sans résumer ni dupliquer tous les tutoriels."""
continuity = replace_once(
    continuity, old_next, new_next, "continuity next action"
)
journal = f"""### {TS} — version 3.86.0

- clôture technique et PDF du Livre IV — Finalisation, optimisation, publication et maintenance ;
- validation transversale des 22 chapitres, audits, preuves, identifiants, liens, doublons et repères réussie ;
- trois caractères de contrôle invisibles supprimés des exemples de chemins des chapitres 16 et 18 ;
- filtre PDF corrigé pour préserver le chapitre 2 — Stratégie générale d’assurance qualité ;
- garde-fou ajouté : les 22 titres du Livre IV doivent apparaître dans le texte extrait ;
- compilation finale Pandoc/XeLaTeX réussie sur la tête `{READER_HEAD}` ;
- PDF cumulatif final : 3 672 pages A4, 9 428 292 octets, version 1.5, non chiffré et texte extractible ;
- empreinte PDF `{PDF_SHA}` ;
- `qpdf --check`, contrôle des polices incorporées et exclusion des contenus QA internes réussis ;
- 49 pages inspectées avec Poppler, 12 pages comparées avec PDFium et neuf pages de tête finale réinspectées ;
- run final `{FINAL_RUN}`, artefact `{FINAL_ARTIFACT}`, digest `{FINAL_DIGEST}` ;
- Livre IV accepté au niveau `static-review+pdf-inspected` avec réserves runtime, licence globale et balisage d’accessibilité ;
- jalon actif déplacé vers M6 — Livre V ;
- prochaine action : `Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md`, niveau Élevée.

"""
continuity = replace_once(
    continuity,
    "### 2026-07-28T05:41:07+02:00 — version 3.85.0",
    journal + "### 2026-07-28T05:41:07+02:00 — version 3.85.0",
    "continuity journal",
)
write(continuity_path, continuity)

for temporary in [
    Path(".github/workflows/livre-iv-pdf-finalizer.yml"),
    Path(".qa/livre-iv-pdf-finalize.py"),
    Path(".qa/livre-iv-pdf-finalize-v2.trigger"),
]:
    temporary.unlink(missing_ok=True)

bad = []
for raw in subprocess.check_output(["git", "ls-files", "-z"]).split(b"\0"):
    if not raw:
        continue
    path = Path(raw.decode("utf-8", "surrogateescape"))
    if not path.exists():
        continue
    data = path.read_bytes()
    if b"\0" in data:
        continue
    for byte in data:
        if byte in (*range(0, 9), 11, 12, *range(14, 32), 127):
            bad.append(str(path))
            break
if bad:
    raise RuntimeError("Forbidden control characters remain: " + ", ".join(sorted(bad)))

expected = {
    "CONTINUITE-PROJET.md",
    "Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md",
    "Livre-IV/CHAPITRE-18-Accessibilite.md",
    "Livre-IV/QA/CLOTURE-LIVRE-IV.md",
    "Livre-IV/QA/VALIDATION-PUBLICATION-LIVRE-IV.yaml",
    "Livre-IV/index.md",
    "ROADMAP.md",
    "filters/pdf-normalize.lua",
    "plans/LIVRE-IV-PLAN-MAITRE.md",
}
tracked = set(
    subprocess.check_output(["git", "diff", "--name-only", "origin/main"])
    .decode()
    .splitlines()
)
untracked = set(
    subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"])
    .decode()
    .splitlines()
)
actual = tracked | untracked
if actual != expected:
    raise RuntimeError(
        f"Unexpected final diff. expected={sorted(expected)} actual={sorted(actual)}"
    )

print("Permanent closure lot materialized with exactly nine files.")
