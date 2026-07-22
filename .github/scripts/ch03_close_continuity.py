#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
from zoneinfo import ZoneInfo

PATH = Path("CONTINUITE-PROJET.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 motif, trouvé {count}")
    return text.replace(old, new, 1)


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    if 'version: "3.33.1"' in text:
        print("continuity_already_closed")
        return 0

    text = replace_once(text, 'version: "3.33.0"', 'version: "3.33.1"', "version continuité")
    now = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
    text, count = re.subn(
        r'last-updated: "[^"]+"',
        f'last-updated: "{now}"',
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError(f"last-updated: attendu 1 motif, trouvé {count}")

    marker = "## 27. Journal\n\n"
    entry = f"""### {now} — version 3.33.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-03.yaml` fermée avec zéro erreur bloquante et une réserve documentaire ;
- workflow permanent `Validate Chapters Without PDF` réussi au run `29949966935` sur la base `7bbab5accaf56fd6560579a08a8c9dee8bdc8f6c` et la tête documentaire `ab7fefc9422ee16a1e32b7db1e2bc933684f515d` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8541707655`, digest `395aba9d4fdde611ccddcc12a623c0cf25a36738acb3657b2619bce269a24fd7` ;
- audit des contextes réussi au run `29950382307` sur la même tête documentaire ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8541869318`, digest `cbd05e077f333c541341bd50d335ce76ac71f352018d339ba2086d94c19dbabb` ;
- empreinte SHA-256 du chapitre fermée à `71f196636f663e00b3c925ed792c3323187bf7f22db30c95c313805f5f2fd912` ;
- matérialiseur, runner de contextes, fichiers de résultat et déclencheurs temporaires supprimés avant fusion ;
- prochaine action maintenue sur le chapitre 4 — Pipeline Blender et organisation des fichiers, niveau Élevée ;
- aucune exécution ComfyUI ou Godot et aucun PDF du Livre III construits.

"""
    text = replace_once(text, marker, marker + entry, "journal")
    PATH.write_text(text, encoding="utf-8", newline="\n")
    print(f"continuity_closed version=3.33.1 timestamp={now}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
