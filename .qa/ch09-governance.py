from __future__ import annotations

import base64
import gzip
import json
from pathlib import Path
import re

TIMESTAMP = "2026-07-23T09:06:37+02:00"


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Remplacement attendu une fois dans {path}, trouvé {count} : {old[:80]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def regex_once(path: str, pattern: str, replacement: str, flags: int = 0) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Substitution attendue une fois dans {path}, trouvée {count} : {pattern}")
    target.write_text(updated, encoding="utf-8")


parts = sorted(Path(".qa").glob("ch09-package-*.b64"))
if not parts:
    raise RuntimeError("Fragments du paquet chapitre 9 absents.")
payload = "".join(part.read_text(encoding="ascii").strip() for part in parts)
files = json.loads(gzip.decompress(base64.b64decode(payload)).decode("utf-8"))
for relative_path, content in files.items():
    destination = Path(relative_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise RuntimeError(f"Le fichier existe déjà : {relative_path}")
    destination.write_text(content, encoding="utf-8")

for part in parts:
    part.unlink()

replace_once("Livre-III/index.md", 'version: "1.7.0"', 'version: "1.8.0"')
replace_once(
    "Livre-III/index.md",
    "8. [Création des animaux](CHAPITRE-08-Creation-des-animaux.md)\n\nLes chapitres 9 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "8. [Création des animaux](CHAPITRE-08-Creation-des-animaux.md)\n9. [Création des créatures](CHAPITRE-09-Creation-des-creatures.md)\n\nLes chapitres 10 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
)

replace_once(
    "ROADMAP.md",
    "- [x] Chapitre 8 — Création des animaux.\n- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "- [x] Chapitre 8 — Création des animaux.\n- [x] Chapitre 9 — Création des créatures.\n- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
)
replace_once(
    "ROADMAP.md",
    "**Statut M4 : en cours — 8 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 9 chapitres rédigés, repérés et audités sur 30.**",
)

replace_once(
    "contents.txt",
    "Livre-III/CHAPITRE-08-Creation-des-animaux.md\nLivre-IV/index.md",
    "Livre-III/CHAPITRE-08-Creation-des-animaux.md\nLivre-III/CHAPITRE-09-Creation-des-creatures.md\nLivre-IV/index.md",
)

replace_once("plans/LIVRE-III-PLAN-MAITRE.md", 'version: "1.1.8"', 'version: "1.1.9"')
regex_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    r'last-updated: "[^"]+"',
    f'last-updated: "{TIMESTAMP}"',
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Statut :** en cours — 8 chapitres sur 30  ",
    "> **Statut :** en cours — 9 chapitres sur 30  ",
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Progression :** chapitres 1 à 8 rédigés, repérés et audités au niveau `static-review` ; chapitres 9 à 30 à produire.",
    "> **Progression :** chapitres 1 à 9 rédigés, repérés et audités au niveau `static-review` ; chapitres 10 à 30 à produire.",
)

replace_once("CONTINUITE-PROJET.md", 'version: "3.38.1"', 'version: "3.39.0"')
regex_once(
    "CONTINUITE-PROJET.md",
    r'last-updated: "[^"]+"',
    f'last-updated: "{TIMESTAMP}"',
)
replace_once(
    "CONTINUITE-PROJET.md",
    "**En cours : 8 chapitres sur 30.**",
    "**En cours : 9 chapitres sur 30.**",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "8. Création des animaux — terminé au niveau `static-review`.\n\nLes chapitres 9 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "8. Création des animaux — terminé au niveau `static-review`.\n9. Création des créatures — terminé au niveau `static-review`.\n\nLes chapitres 10 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- progression du Livre III : 8 chapitres sur 30 ;",
    "- progression du Livre III : 9 chapitres sur 30 ;",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- chapitre 8 du Livre III : version `1.0.0`, niveau `static-review` ;\n- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "- chapitre 8 du Livre III : version `1.0.0`, niveau `static-review` ;\n- chapitre 9 du Livre III : version `1.0.0`, niveau `static-review` ;\n- Livre II : 30 chapitres sur 30, publication technique terminée ;",
)

continuity = Path("CONTINUITE-PROJET.md").read_text(encoding="utf-8")
new_next = """## 26. Prochaine action

Le chapitre 9 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système de création des créatures couvre brief fonctionnel, analogues qualifiés, niveaux de spéculation, masses, appuis, silhouettes, blockout métrique, anatomie inventée, topologie, profil de rig, sockets, proxies de collision, zones de lisibilité, poses d’action, variantes, LOD, export GLB et scène Godot de validation. Aucun concept final, modèle, rig, collision, socket, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 approfondira le lookdev de gros plan des visages, de la peau, des yeux, des cheveux et de la pilosité, sans refaire les contrats anatomiques, de rig ou de collision du chapitre 9 ni anticiper l’animation faciale complète du chapitre 27.
"""
updated, count = re.subn(
    r"## 26\. Prochaine action\n.*?(?=\n## 27\. Journal)",
    new_next.rstrip() + "\n",
    continuity,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("Section Prochaine action introuvable ou ambiguë.")
continuity = updated
journal_marker = "## 27. Journal\n\n"
journal = f"""### {TIMESTAMP} — version 3.39.0

- chapitre 9 du Livre III créé, relu et audité au niveau `static-review` ;
- brief fonctionnel et matrice fonction-forme-coût-limite du Veilleur des brumes documentés ;
- analogues réels, niveaux de spéculation et inconnues bloquantes séparés ;
- masses, appuis, silhouettes, vues de contrôle et blockout métrique encadrés ;
- topologie, profil de rig, sockets, proxies de collision et zones de lisibilité préparés ;
- poses d’action, enveloppes de mouvement, variantes et LOD définis sans valeurs gameplay inventées ;
- export GLB, scène Godot dérivée, validateur structurel et campagnes de mesure documentés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 10 — Visages, peau, yeux, cheveux et pilosité, niveau Élevée ;
- aucun concept final, modèle, rig, collision, socket, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
if journal_marker not in continuity:
    raise RuntimeError("Journal de continuité introuvable.")
continuity = continuity.replace(journal_marker, journal_marker + journal, 1)
Path("CONTINUITE-PROJET.md").write_text(continuity, encoding="utf-8")
