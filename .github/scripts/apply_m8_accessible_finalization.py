#!/usr/bin/env python3
"""Apply the verified M8 accessible-PDF governance updates exactly once."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAMP = "2026-08-01T06:49:00+02:00"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: remplacement attendu une fois, trouvé {count}")
    return text.replace(old, new, 1)


def update_roadmap() -> None:
    path = ROOT / "ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    old = "- [ ] Produire un PDF balisé pour les lecteurs d’écran."
    new = (
        "- [x] Produire un PDF balisé pour les lecteurs d’écran — candidat "
        "technique de 4 214 pages, structure et métadonnées validées sous Linux, "
        "profil veraPDF PDF/UA-1 sans échec machine, réserves humaines et cinq "
        "avertissements qpdf conservés."
    )
    text = replace_once(text, old, new, "ROADMAP PDF balisé")
    path.write_text(text, encoding="utf-8")


def update_build() -> None:
    path = ROOT / "BUILD.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "2.1.0"', 'version: "2.2.0"', "BUILD version")
    text = replace_once(
        text,
        'last-updated: "2026-07-31T16:34:00+02:00"',
        f'last-updated: "{STAMP}"',
        "BUILD date",
    )
    marker = "## Reproductibilité\n"
    qualification = """## Qualification de référence

Le workflow `Build Accessible Tagged PDF`, run `30684329205`, a qualifié sous Ubuntu 24.04 un candidat de 4 214 pages et 28 766 695 octets, SHA-256 `629ed5231627b84ea1832ffea9a60a403d3818b785949dbc3c2425ddac33159b`.

veraPDF 1.30.2 a réussi le profil PDF/UA-1 avec 106 règles et 20 644 277 contrôles réussis, sans échec machine. `qpdf --check` termine avec cinq avertissements de clés `/Group` dupliquées et le statut `success-with-reservations` ; les sorties brutes restent conservées.

L’artefact final `8813427010` porte le digest `sha256:fe3f4c844b5d3e14afe2d01ca070b11d8f215aa92563c79f502d410c4d7bc861`. L’artefact de diagnostics `8813426329` porte le digest `sha256:57e86c3de2ffd3bf31a51a97417077456a30fd923029f6bd32e2e5efaf1cfde3`.

La qualification complète et ses réserves sont consignées dans `QA/AUDIT-ACCESSIBLE-PDF.md` et `QA/VALIDATION-ACCESSIBLE-PDF.yaml`. Aucun test avec lecteur d’écran réel ni aucune certification PDF/UA ne sont revendiqués.

"""
    if qualification in text:
        raise SystemExit("BUILD qualification déjà présente")
    text = replace_once(text, marker, qualification + marker, "BUILD qualification")
    path.write_text(text, encoding="utf-8")


def update_continuity() -> None:
    path = ROOT / "CONTINUITE-PROJET.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        'version: "4.26.0"',
        'version: "4.27.0"',
        "continuité version",
    )
    text = replace_once(
        text,
        'last-updated: "2026-07-30T23:04:00+02:00"',
        f'last-updated: "{STAMP}"',
        "continuité date",
    )

    old_next = """## 26. Prochaine action

M8 — Publications est actif. La chaîne commune génère désormais depuis 162 sources un PDF A4, un HTML autonome et un EPUB 3, avec manifeste SHA-256, licence éditoriale et statut explicite de build technique. La génération a été qualifiée sur Linux ; aucune release officielle n'a été créée.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Produire un PDF balisé pour les lecteurs d’écran.
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le prochain lot doit traiter la structure logique, les titres, la langue, l'ordre de lecture, les alternatives textuelles et la vérification avec des outils d'accessibilité, sans dégrader le PDF visuel existant ni revendiquer une conformité non testée.

"""
    new_next = """## 26. Prochaine action

M8 — Publications est actif. La chaîne commune PDF, HTML autonome et EPUB 3 reste qualifiée sur Linux. Un candidat PDF balisé distinct de 4 214 pages a également été qualifié au niveau `runtime-tested-linux`, avec diagnostic veraPDF PDF/UA-1 sans échec machine, inventaire de structure, inspection humaine représentative et réserves explicites. Il demeure un build technique ; aucune release officielle ni certification d'accessibilité n'a été créée.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Companion-Pack/
Publier les archives du Companion Pack.
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le prochain lot doit empaqueter les dix Packs sans modifier leur périmètre, vérifier les licences, noms stables, manifestes, sommes de contrôle, extraction propre et contenu attendu des archives. Il doit distinguer artefacts techniques, archives candidates et publication publique, sans revendiquer une release non créée.

"""
    text = replace_once(text, old_next, new_next, "continuité prochaine action")

    journal_marker = "## 27. Journal\n\n"
    journal_entry = """### 2026-08-01T06:49:00+02:00 — version 4.27.0

- chaîne séparée de PDF balisé qualifiée sous Ubuntu 24.04 à partir des 162 sources de `contents.txt` ;
- candidat de 4 214 pages, 28 766 695 octets, SHA-256 `629ed5231627b84ea1832ffea9a60a403d3818b785949dbc3c2425ddac33159b` ;
- Pandoc 3.10, LuaHBTeX 1.24.0 et TeX Live 2026 épinglé par digest ;
- `Tagged: yes`, langue `fr-FR`, `/Marked true`, arbre de structure, titre, auteur et manifeste validés ;
- veraPDF 1.30.2, profil PDF/UA-1 : 106 règles et 20 644 277 contrôles réussis, zéro échec machine ;
- inventaire indépendant : 387 347 éléments structurés, 579 tableaux, 28 926 éléments de liste, 5 figures avec alternative et 2 978 liens ;
- audit source : cinq images dans `README.md`, aucune alternative vide après exclusion des exemples de code ;
- qpdf terminé avec cinq avertissements conservés sur des clés `/Group` dupliquées ;
- inspection Poppler représentative de la couverture, du sommaire, des figures, listes, tableaux, code, liens, index, licences et fin du volume sans défaut visuel bloquant observé ;
- run accessible `30684329205`, artefact final `8813427010`, digest `sha256:fe3f4c844b5d3e14afe2d01ca070b11d8f215aa92563c79f502d410c4d7bc861` ;
- diagnostics `8813426329`, digest `sha256:57e86c3de2ffd3bf31a51a97417077456a30fd923029f6bd32e2e5efaf1cfde3` ;
- non-régression multiformat réussie au run `30684329206`, artefact `8813421114`, digest `sha256:e47f97c7a44c3fbc8ec3cccf4298769ae4d0c3f63751ddbce889f8255f77399f` ;
- audit `QA/AUDIT-ACCESSIBLE-PDF.md` fermé et preuve `QA/VALIDATION-ACCESSIBLE-PDF.yaml` ajoutée ;
- tâche M8 « produire un PDF balisé pour les lecteurs d'écran » clôturée ;
- prochaine action déplacée vers la publication des archives du Companion Pack, niveau Élevée ;
- aucun test avec lecteur d'écran réel, inspection exhaustive des 4 214 pages, certification PDF/UA, identité byte pour byte ou release publique revendiqués ;
- `contents.txt` inchangé, car aucun contenu lecteur ni ordre de compilation n'a été ajouté.

"""
    if journal_entry in text:
        raise SystemExit("entrée de journal déjà présente")
    text = replace_once(
        text,
        journal_marker,
        journal_marker + journal_entry,
        "continuité journal",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    required = [
        ROOT / "QA" / "AUDIT-ACCESSIBLE-PDF.md",
        ROOT / "QA" / "VALIDATION-ACCESSIBLE-PDF.yaml",
    ]
    missing = [path.as_posix() for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"preuves absentes : {missing}")
    update_roadmap()
    update_build()
    update_continuity()
    print("M8 accessible PDF governance updated")


if __name__ == "__main__":
    main()
