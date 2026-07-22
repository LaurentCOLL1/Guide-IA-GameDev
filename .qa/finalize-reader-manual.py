from __future__ import annotations

import base64
import hashlib
import re
import subprocess
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / ".qa"
CHUNKS = [QA / f"l3-plan-{index:02d}.b64" for index in range(4)]
PLAN = ROOT / "plans" / "LIVRE-III-PLAN-MAITRE.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
EXPECTED_SHA256 = "ac748d63b59e8e99123e2e0daf8884533fcc35a3122ec54e07a8efac88daaefb"
TIMESTAMP = "2026-07-22T12:07:56+02:00"

missing = [path.as_posix() for path in CHUNKS if not path.is_file()]
if missing:
    raise RuntimeError(f"Fragments du plan absents : {missing}")

encoded = "".join(path.read_text(encoding="ascii").strip() for path in CHUNKS)
plan_bytes = zlib.decompress(base64.b64decode(encoded))
actual_sha256 = hashlib.sha256(plan_bytes).hexdigest()
if actual_sha256 != EXPECTED_SHA256:
    raise RuntimeError(
        f"Empreinte du plan incorrecte : {actual_sha256} au lieu de {EXPECTED_SHA256}"
    )

plan_text = plan_bytes.decode("utf-8")
if plan_text.count("\n## Chapitre ") != 30:
    raise RuntimeError("Le plan enrichi ne contient pas exactement trente chapitres.")
for required in (
    'version: "1.1.0"',
    "## 1. Fonction de ce document dans une nouvelle conversation",
    "### Mode Solo",
    "### Mode Studio",
    "## 8. Critères de clôture du Livre III",
    "Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md",
):
    if required not in plan_text:
        raise RuntimeError(f"Élément obligatoire absent du plan : {required}")

PLAN.write_text(plan_text, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity, count = re.subn(
    r'^version: "3\.30\.2"$', 'version: "3.30.3"', continuity, count=1, flags=re.M
)
if count != 1:
    raise RuntimeError("La version 3.30.2 de la continuité est introuvable.")
continuity, count = re.subn(
    r'^last-updated: ".*"$', f'last-updated: "{TIMESTAMP}"', continuity, count=1, flags=re.M
)
if count != 1:
    raise RuntimeError("Le champ last-updated de la continuité est introuvable.")

anchor = "## 27. Journal\n\n"
entry = f"""### {TIMESTAMP} — version 3.30.3

- `plans/LIVRE-III-PLAN-MAITRE.md` enrichi et porté en version `1.1.0` ;
- les trente chapitres possèdent désormais intention, résultats d’apprentissage, contenu obligatoire, livrables, dépendances, variantes Solo/Studio, critères de validation et frontière ;
- le plan contient une procédure de reprise explicite pour une nouvelle conversation ;
- la règle de publication est confirmée : le manuel lecteur exclut protocoles, audits, preuves, rapports QA, continuité et documents de fabrication ;
- la prochaine action reste `Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md` après validation du PDF lecteur du Livre II.

"""
if anchor not in continuity:
    raise RuntimeError("L’ancre du journal de continuité est introuvable.")
continuity = continuity.replace(anchor, anchor + entry, 1)
CONTINUITY.write_text(continuity, encoding="utf-8")

subprocess.run(
    ["git", "add", PLAN.relative_to(ROOT).as_posix(), CONTINUITY.relative_to(ROOT).as_posix()],
    cwd=ROOT,
    check=True,
)

for path in CHUNKS + [QA / "reader-manual-rerun.txt", Path(__file__)]:
    if path.exists():
        path.unlink()

print(f"Plan Livre III écrit : {PLAN}")
print(f"SHA-256 : {actual_sha256}")
print("Continuité portée à 3.30.3.")
