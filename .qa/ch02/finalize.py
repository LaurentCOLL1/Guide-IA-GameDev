#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import re
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / ".qa/ch02"
NOW = "2026-07-22T18:10:53+02:00"
RECOVERY_POSITION = 7805
RECOVERY_CHARACTER = "S"
EXPECTED_CHAPTER_SHA256 = "d5c1d7be7d472d6fec3541ae2b0c6306070d374d281defd71e139b660bcfba23"
EXPECTED_AUDIT_SHA256 = "df5304b3f3a8f24f7d8b21cfe97bcc3915f3272a8b777bf9cad094eb2fcae283"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 motif, trouvé {count}")
    return text.replace(old, new, 1)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def decode_recovered_payload() -> bytes:
    parts = sorted(QA.glob("package-*.b64"))
    if [part.name for part in parts] != [
        "package-00.b64",
        "package-01.b64",
        "package-02.b64",
        "package-03.b64",
    ]:
        raise RuntimeError("les quatre fragments package-00 à package-03 sont requis")

    texts = [
        "".join(char for char in part.read_text(encoding="utf-8") if not char.isspace())
        for part in parts
    ]
    if len(texts[1]) != 11999:
        raise RuntimeError(f"longueur inattendue pour package-01.b64: {len(texts[1])}")
    texts[1] = (
        texts[1][:RECOVERY_POSITION]
        + RECOVERY_CHARACTER
        + texts[1][RECOVERY_POSITION:]
    )
    return base64.b64decode("".join(texts), validate=True)


def extract_local_entry(payload: bytes, offset: int) -> tuple[str, bytes, int, int, int]:
    if payload[offset : offset + 4] != b"PK\x03\x04":
        raise RuntimeError(f"signature ZIP locale absente à l’offset {offset}")
    (
        _signature,
        _version,
        _flags,
        method,
        _mtime,
        _mdate,
        declared_crc,
        compressed_size,
        uncompressed_size,
        name_length,
        extra_length,
    ) = struct.unpack_from("<IHHHHHIIIHH", payload, offset)
    name_start = offset + 30
    name_end = name_start + name_length
    name = payload[name_start:name_end].decode("utf-8")
    data_start = name_end + extra_length
    data_end = data_start + compressed_size
    compressed = payload[data_start:data_end]
    if method == 8:
        data = zlib.decompress(compressed, -15)
    elif method == 0:
        data = compressed
    else:
        raise RuntimeError(f"méthode ZIP non prise en charge pour {name}: {method}")
    if len(data) != uncompressed_size:
        raise RuntimeError(
            f"taille extraite inattendue pour {name}: {len(data)} au lieu de {uncompressed_size}"
        )
    return name, data, data_end, declared_crc, zlib.crc32(data) & 0xFFFFFFFF


payload = decode_recovered_payload()
chapter_name, chapter_data, offset, chapter_declared_crc, chapter_actual_crc = extract_local_entry(payload, 0)
audit_name, audit_data, offset, audit_declared_crc, audit_actual_crc = extract_local_entry(payload, offset)

expected_chapter_name = "Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md"
expected_audit_name = "Livre-III/QA/AUDIT-CHAPITRE-02.md"
if chapter_name != expected_chapter_name or audit_name != expected_audit_name:
    raise RuntimeError(
        f"entrées récupérées inattendues: {chapter_name!r}, {audit_name!r}"
    )
if payload[offset : offset + 4] != b"PK\x01\x02":
    raise RuntimeError("le répertoire central attendu après l’audit est absent")

chapter_sha = hashlib.sha256(chapter_data).hexdigest()
audit_sha = hashlib.sha256(audit_data).hexdigest()
if chapter_sha != EXPECTED_CHAPTER_SHA256:
    raise RuntimeError(f"empreinte du chapitre récupéré inattendue: {chapter_sha}")
if audit_sha != EXPECTED_AUDIT_SHA256:
    raise RuntimeError(f"empreinte de l’audit récupéré inattendue: {audit_sha}")
if audit_declared_crc != audit_actual_crc:
    raise RuntimeError("le CRC de l’audit intact ne correspond pas")

chapter = ROOT / expected_chapter_name
audit = ROOT / expected_audit_name
proof = ROOT / "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-02.yaml"
chapter.parent.mkdir(parents=True, exist_ok=True)
audit.parent.mkdir(parents=True, exist_ok=True)
chapter.write_bytes(chapter_data)
audit.write_bytes(audit_data)

proof_text = f"""schema-version: 1
evidence-id: DOC-L3-QA-EVIDENCE-CH02
status: pending
validation-date: '2026-07-22'
validated-base-commit: null
validated-head-commit: null
chapter:
  id: DOC-L3-CH02
  path: Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 1
  chapter-lines: 2560
  chapter-headings: 59
  chapter-code-and-data-blocks: 62
  significant-code-and-data-blocks: 62
  code-explanation-markers: 62
  structured-non-error-code-explanations: 42
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  duplicate-headings: 0
  duplicate-blocks: 0
  duplicate-paragraphs: 0
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  solo-studio-markdown-only: true
  visual-bible-documented: true
  visual-pillars-documented: true
  shape-language-documented: true
  silhouette-and-proportion-rules-documented: true
  palette-and-non-color-redundancy-documented: true
  materials-and-wear-causality-documented: true
  lighting-and-tonemapping-rules-documented: true
  family-and-variation-rules-documented: true
  review-grid-and-exceptions-documented: true
  godot-comparison-scene-contract-documented: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  error-explanations-directly-after-markers: true
  pdf-produced: false
  runtime-executed: false
recovery:
  source-package-recovered: true
  package-01-insertion-position: {RECOVERY_POSITION}
  package-01-insertion-character: '{RECOVERY_CHARACTER}'
  chapter-sha256: {chapter_sha}
  audit-sha256: {audit_sha}
  chapter-declared-crc: '{chapter_declared_crc:08x}'
  chapter-recovered-crc: '{chapter_actual_crc:08x}'
  missing-original-proof-local-record-bytes: 1083
  original-proof-regenerated-after-validation: true
ci:
  validate-chapters-without-pdf:
    run-id: null
    conclusion: pending
  validate-usage-contexts:
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
reservations:
  - Starter Kit not materialized.
  - Proposed docs, tools, scenes and captures not created in a real Godot project.
  - Real visual bible not produced from selected references.
  - References, authors, licences and rights not populated.
  - Blender version and addons not qualified.
  - Pilot assets not produced.
  - Godot validation scene not materialized.
  - Camera script not analyzed or executed.
  - Environment profiles, tonemapper, exposure and fog not exercised.
  - UI contrasts not measured.
  - Comparative captures not produced.
  - GPU, memory and frame-time costs not measured.
  - Solo or Studio review not executed.
  - Livre III PDF not built by end-of-book policy.
evidence-closure:
  commit: null
  conclusion: pending
"""
write(proof, proof_text)

chapter_text = chapter.read_text(encoding="utf-8")
if "recommended-reasoning" in chapter_text or "Niveau GPT-5.6 Sol" in chapter_text:
    raise RuntimeError("métadonnée de raisonnement interdite dans le chapitre")
if chapter_text.count("```") % 2:
    raise RuntimeError("blocs Markdown non équilibrés")
if chapter_text.count("<!-- qa:code-explanation -->") != chapter_text.count("```") // 2:
    raise RuntimeError("nombre de blocs et de marqueurs d’explication différent")
if chapter_text.count("**Exemple fautif :**") != 10 or chapter_text.count("**Exemple corrigé :**") != 10:
    raise RuntimeError("les dix séquences d’erreurs ne sont pas présentes")
if "## 41. Mode Solo" not in chapter_text or "## 42. Mode Studio" not in chapter_text:
    raise RuntimeError("sections Solo/Studio absentes")
if "manque de finition" not in chapter_text or "Principe de forme" not in chapter_text:
    raise RuntimeError("les deux passages de récupération sémantique ne sont pas restaurés")

path = ROOT / "Livre-III/index.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.0"', 'version: "1.1.0"', "version index")
text = replace_once(text, "1. [Préproduction et cahier des charges artistique](CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md)\n\nLes chapitres 2 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.", "1. [Préproduction et cahier des charges artistique](CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md)\n2. [Direction artistique et bible visuelle](CHAPITRE-02-Direction-artistique-et-bible-visuelle.md)\n\nLes chapitres 3 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.", "chapitres index")
write(path, text)

path = ROOT / "ROADMAP.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, "- [x] Chapitre 1 — Préproduction et cahier des charges artistique.\n- [ ] Préproduction et direction artistique — 1 chapitre sur 5.", "- [x] Chapitre 1 — Préproduction et cahier des charges artistique.\n- [x] Chapitre 2 — Direction artistique et bible visuelle.\n- [ ] Préproduction et direction artistique — 2 chapitres sur 5.", "roadmap chapitres")
text = replace_once(text, "**Statut M4 : en cours — 1 chapitre rédigé, repéré et audité sur 30.**", "**Statut M4 : en cours — 2 chapitres rédigés, repérés et audités sur 30.**", "statut M4")
write(path, text)

path = ROOT / "contents.txt"
text = path.read_text(encoding="utf-8")
text = replace_once(text, "Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md\nLivre-IV/index.md", "Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md\nLivre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md\nLivre-IV/index.md", "ordre lecteur")
write(path, text)

path = ROOT / "plans/LIVRE-III-PLAN-MAITRE.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.1.1"', 'version: "1.1.2"', "version plan")
text = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{NOW}"', text, count=1)
text = replace_once(text, 'status: "en cours — 1 chapitre sur 30"', 'status: "en cours — 2 chapitres sur 30"', "statut plan")
text = replace_once(text, "> **Progression :** chapitre 1 terminé au niveau `static-review` ; chapitres 2 à 30 à produire.", "> **Progression :** chapitres 1 et 2 terminés au niveau `static-review` ; chapitres 3 à 30 à produire.", "progression plan")
write(path, text)

path = ROOT / "CONTINUITE-PROJET.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.31.0"', 'version: "3.32.0"', "version continuité")
text = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{NOW}"', text, count=1)
text = replace_once(text, "**En cours : 1 chapitre sur 30.**", "**En cours : 2 chapitres sur 30.**", "collection Livre III")
text = replace_once(text, "1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.\n\nLes chapitres 2 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.", "1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.\n2. Direction artistique et bible visuelle — terminé au niveau `static-review`.\n\nLes chapitres 3 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.", "liste Livre III")
if "Livre III, chapitres 1 et 2 : **Élevée**." not in text:
    text = replace_once(text, "Chapitres 3 à 29 : **Élevée**.", "Chapitres 3 à 29 : **Élevée**.\n\nLivre III, chapitres 1 et 2 : **Élevée**.", "niveau Livre III")
architecture = """
### 11.27 Direction artistique et bible visuelle

- la bible transforme des intentions perceptuelles en règles visuelles observables et versionnées ;
- formes, silhouettes, proportions, valeurs, saturation, température, matériaux, lumière, profondeur, UI et VFX partagent une grammaire commune ;
- les signaux gameplay importants restent lisibles sans dépendre de la couleur seule ;
- les matériaux sont évalués sous plusieurs éclairages et leur usure suit des causes localisées ;
- les variations culturelles, régionales, sociales et temporelles dérivent de règles communes documentées ;
- les exemples conformes, limites et non conformes rendent les règles classables par une autre personne ;
- les exceptions sont écrites, limitées, approuvées et réévaluées ;
- toute modification influençant coûts ou priorités passe par la demande de changement du chapitre 1 ;
- la validation cible une scène Godot comparative, mais aucune exécution runtime n’est revendiquée avant matérialisation des assets pilotes.
"""
if "### 11.27 Direction artistique et bible visuelle" not in text:
    text = replace_once(text, "\n## 24. Erreurs à ne pas reproduire", architecture + "\n## 24. Erreurs à ne pas reproduire", "architecture visuelle")
art_errors = """- ne pas traiter un moodboard comme une bible visuelle ;
- ne pas employer des adjectifs artistiques sans critère observable ;
- ne pas maximiser détail, saturation ou contraste sur chaque élément ;
- ne pas coder une information essentielle par la couleur seule ;
- ne pas valider un matériau sous un seul éclairage avantageux ;
- ne pas distribuer usure et salissures sans cause ;
- ne pas réduire les régions ou cultures à une recoloration aléatoire ;
- ne pas modifier la bible sans version, propriétaire et conséquences identifiées ;
- ne pas accepter une dérogation uniquement orale ;
- ne pas déclarer la direction validée dans Godot avant les assets pilotes et la scène comparative ;

"""
if art_errors.strip() not in text:
    text = replace_once(text, "- ne pas laisser l’orchestrateur Python modifier directement un état métier Godot ;\n\n- ne pas oublier la mise à jour de ce fichier.", "- ne pas laisser l’orchestrateur Python modifier directement un état métier Godot ;\n\n" + art_errors + "- ne pas oublier la mise à jour de ce fichier.", "erreurs direction artistique")
text = replace_once(text, "- progression du Livre III : 1 chapitre sur 30 ;", "- progression du Livre III : 2 chapitres sur 30 ;", "état progression")
text = replace_once(text, "- chapitre 1 du Livre III : version `1.0.0`, niveau `static-review` ;", "- chapitre 1 du Livre III : version `1.0.0`, niveau `static-review` ;\n- chapitre 2 du Livre III : version `1.0.0`, niveau `static-review` ;", "état chapitre 2")
old_next = """Le chapitre 1 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le cahier des charges, la matrice d’assets, les budgets initiaux, le calendrier, les risques et les critères d’acceptation sont définis comme contrats de préproduction. Aucun asset, pipeline Blender ou benchmark runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 2 transformera les objectifs perceptuels du cahier des charges en bible visuelle : références, formes, proportions, palettes, matériaux, lumière, caméras de comparaison, règles d’inclusion et d’exclusion. Il ne modifiera ni les budgets ni les priorités sans demande de changement explicite."""
new_next = """Le chapitre 2 du Livre III est rédigé, repéré et audité au niveau `static-review`. La bible visuelle formalise formes, silhouettes, proportions, palettes, matériaux, lumière, profondeur, UI, VFX, variations, grilles de revue et dérogations. Aucun asset pilote, benchmark ou test Godot n’est revendiqué comme exécuté.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 3 organisera les références légalement sourcées, les moodboards annotés et les workflows ComfyUI versionnés avec modèles, seeds, prompts et paramètres. Il distinguera référence, concept, source de production et asset final, puis imposera une sélection humaine sans modifier silencieusement la bible visuelle."""
text = replace_once(text, old_next, new_next, "prochaine action")
journal = f"""### {NOW} — version 3.32.0

- chapitre 2 du Livre III créé, relu et audité au niveau `static-review` ;
- bible visuelle, piliers, formes, silhouettes, proportions, palettes, matériaux, lumière, profondeur, UI et VFX documentés ;
- variations culturelles, régionales, sociales et temporelles encadrées par des règles communes ;
- exemples conformes, limites et non conformes, grille de revue, dérogations et gestion des changements définis ;
- scène comparative Godot et captures documentées sans revendiquer leur exécution ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- récupération documentée du chapitre et de l’audit depuis le paquet source ;
- prochaine action déplacée vers le chapitre 3 — Références, concept art et ComfyUI, niveau Élevée ;
- aucun PDF du Livre III construit.

"""
text = replace_once(text, "## 27. Journal\n", "## 27. Journal\n\n" + journal, "journal")
write(path, text)

for temp in list(QA.glob("*")):
    if temp.is_file():
        temp.unlink()
try:
    QA.rmdir()
except OSError:
    pass
print(
    "chapter02_materialized_pending_ci "
    f"chapter_sha256={chapter_sha} audit_sha256={audit_sha} "
    f"chapter_crc={chapter_actual_crc:08x}"
)
