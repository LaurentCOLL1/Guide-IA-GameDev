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
    if 'version: "3.32.1"' in text:
        print("continuity_already_closed")
        return 0

    text = replace_once(
        text,
        'version: "3.32.0"',
        'version: "3.32.1"',
        "version continuité",
    )

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
    entry = f"""### {now} — version 3.32.1

- preuve finale `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-02.yaml` fermée avec zéro erreur bloquante et une réserve documentaire ;
- validation statique approuvée réussie au run `29943194826` sur la base `8f8271a407c7978cfc668aad90e073e3ef3b3713` et la tête documentaire `b05c502ee5c39451784a288ceee09669f60065cd` ;
- artefact `chapter-validation-without-pdf` enregistré sous l’identifiant `8539045265`, digest `07f9309cec632d7be4490ecb7fa16d8b31f5728cd8b143215b1f87ea1b3a14dd` ;
- artefact `usage-context-audit` enregistré sous l’identifiant `8539045793`, digest `f0e67e60f1cfb8ec320d9f6d0111d0ca2b9bb68ffebda59df863c1a23cfc35a8` ;
- chapitre et audit restaurés depuis le paquet source, avec SHA-256 et CRC du chapitre concordant avec l’archive déclarée ;
- finaliseurs, archiveurs, correcteurs, runners approuvés et déclencheurs temporaires supprimés de `main` par la PR `136`, commit `8ca89d683e8f980491de418b2cc47dbdc3e80857` ;
- prochaine action maintenue sur le chapitre 3 — Références, concept art et ComfyUI, niveau Élevée ;
- aucune exécution runtime et aucun PDF du Livre III construits.

"""
    text = replace_once(text, marker, marker + entry, "journal")
    PATH.write_text(text, encoding="utf-8", newline="\n")
    print(f"continuity_closed version=3.32.1 timestamp={now}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
