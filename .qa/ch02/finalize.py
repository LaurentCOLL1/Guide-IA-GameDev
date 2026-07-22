#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import multiprocessing
import os
import re
import shutil
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / ".qa/ch02"
EXPECTED = "2e9761edfadd9f7dfe93b9653ba5fde0238cb8b769e1448c8cfe81a5c76bc465"
NOW = "2026-07-22T18:10:53+02:00"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 motif, trouvé {count}")
    return text.replace(old, new, 1)


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def recover_range(
    body: str,
    padding: str,
    start: int,
    stop: int,
    expected: str,
) -> tuple[int, str, bytes] | None:
    for position in range(start, stop):
        prefix = body[:position]
        suffix = body[position:]
        for char in BASE64_ALPHABET:
            candidate = prefix + char + suffix + padding
            payload = base64.b64decode(candidate, validate=True)
            if hashlib.sha256(payload).hexdigest() == expected:
                return position, char, payload
    return None


def decode_verified_package() -> bytes:
    parts = sorted(QA.glob("package-*.b64"))
    if not parts:
        raise RuntimeError("aucun fragment package-*.b64")

    texts = ["".join(char for char in part.read_text(encoding="utf-8") if not char.isspace()) for part in parts]
    encoded = "".join(texts)
    try:
        payload = base64.b64decode(encoded, validate=True)
    except ValueError as initial_error:
        suspect_indexes = [
            index
            for index, (part, text) in enumerate(zip(parts, texts))
            if part.name == "package-01.b64" and len(text) == 11999
        ]
        if len(suspect_indexes) != 1:
            raise RuntimeError(f"paquet Base64 invalide sans fragment récupérable: {initial_error}") from initial_error

        suspect_index = suspect_indexes[0]
        body = encoded.rstrip("=")
        padding = encoded[len(body):]
        if len(body) % 4 != 1 or padding != "==":
            raise RuntimeError(
                f"forme Base64 inattendue pour récupération: body_mod4={len(body) % 4}, padding={padding!r}"
            ) from initial_error

        global_start = sum(len(text) for text in texts[:suspect_index])
        position_count = len(texts[suspect_index]) + 1
        worker_count = min(4, os.cpu_count() or 1, position_count)
        chunk_size = (position_count + worker_count - 1) // worker_count
        ranges: list[tuple[int, int]] = []
        for worker_index in range(worker_count):
            start = global_start + worker_index * chunk_size
            stop = min(global_start + position_count, start + chunk_size)
            if start < stop:
                ranges.append((start, stop))

        context = multiprocessing.get_context("fork")
        matches: list[tuple[int, str, bytes]] = []
        with ProcessPoolExecutor(max_workers=len(ranges), mp_context=context) as executor:
            futures = [
                executor.submit(recover_range, body, padding, start, stop, EXPECTED)
                for start, stop in ranges
            ]
            for future in futures:
                result = future.result()
                if result is not None:
                    matches.append(result)

        if len(matches) != 1:
            raise RuntimeError(f"récupération Base64 non concluante: {len(matches)} correspondance(s)") from initial_error

        position, char, payload = matches[0]
        local_position = position - global_start
        print(
            "package_recovered "
            f"file=package-01.b64 local_position={local_position} char={char!r} sha256={EXPECTED}"
        )

    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED:
        raise RuntimeError(f"empreinte du paquet inattendue: {digest}")
    return payload


payload = decode_verified_package()
archive = QA / "chapter-02.zip"
archive.write_bytes(payload)
with zipfile.ZipFile(archive) as zf:
    bad = zf.testzip()
    if bad:
        raise RuntimeError(f"entrée ZIP corrompue: {bad}")
    zf.extractall(ROOT)

chapter = ROOT / "Livre-III/CHAPITRE-02-Direction-artistique-et-bible-visuelle.md"
audit = ROOT / "Livre-III/QA/AUDIT-CHAPITRE-02.md"
proof = ROOT / "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-02.yaml"
for path in (chapter, audit, proof):
    if not path.exists():
        raise RuntimeError(f"fichier extrait absent: {path}")
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
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA initiale et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 3 — Références, concept art et ComfyUI, niveau Élevée ;
- aucun PDF du Livre III construit.

"""
text = replace_once(text, "## 27. Journal\n", "## 27. Journal\n\n" + journal, "journal")
write(path, text)

for temp in QA.glob("*"):
    if temp.is_file():
        temp.unlink()
try:
    QA.rmdir()
except OSError:
    pass
print("chapter02_finalized")
