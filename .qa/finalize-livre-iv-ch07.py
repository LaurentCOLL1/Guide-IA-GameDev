#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T03:23:02+02:00"
CHAPTER_SHA256 = "79f4ca00b5ea62e0754fa7fa71baea6d29838c216ddae46aa1814eee954d8557"

def decode_parts(paths: list[str]) -> str:
    payload = "".join(Path(path).read_text(encoding="ascii").strip() for path in paths)
    return zlib.decompress(base64.b64decode(payload.encode("ascii"))).decode("utf-8")

def decode_file(path: str) -> str:
    payload = Path(path).read_text(encoding="ascii").strip()
    return zlib.decompress(base64.b64decode(payload.encode("ascii"))).decode("utf-8")

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: occurrence attendue 1, obtenue {count}")
    return text.replace(old, new, 1)

def write(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")

chapter = decode_parts([
    ".qa/ch07-chapter.part01.b64",
    ".qa/ch07-chapter.part02.b64",
    ".qa/ch07-chapter.part03.b64",
    ".qa/ch07-chapter.part04.b64",
    ".qa/ch07-chapter.part05.b64",
])
actual_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_sha}")

write("Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-07.md", decode_file(".qa/ch07-audit.zlib.b64"))
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-07.yaml", Path(".qa/ch07-proof.yaml").read_text(encoding="utf-8"))

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.7.0"', 'version: "0.8.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T02:53:24+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '7. Profilage GPU et optimisation du rendu ;',
    '7. [Profilage GPU et optimisation du rendu](CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 7",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **6 sur 22** ;', '- chapitres rédigés, repérés et audités : **7 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 6 — Profilage CPU** ;', '- chapitre courant terminé : **chapitre 7 — Profilage GPU et optimisation du rendu** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 7 — Profilage GPU et optimisation du rendu** ;', '- prochaine entrée du plan maître : **chapitre 8 — Optimisation RAM, VRAM et allocations** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 6 sont terminés', 'les chapitres 1 à 7 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 6 — Profilage CPU — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 1 chapitre sur 8.',
    '- [x] Chapitre 6 — Profilage CPU — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 7 — Profilage GPU et optimisation du rendu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 2 chapitres sur 8.',
    "roadmap chapitre 7",
)
text = replace_once(text, '**Statut M5 : en cours — 6 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 7 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-06-Profilage-CPU.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-06-Profilage-CPU.md\nLivre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md\nLivre-V/index.md',
    "contents chapitre 7",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.6"', 'version: "1.0.7"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T02:53:24+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 6 chapitres sur 22', '> **Statut :** en cours — 7 chapitres sur 22', "plan statut")
anchor = 'La production des assets optimisés est au Livre III. Validation par stabilité des FPS et qualité visuelle documentée.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Les budgets GPU, captures, profils graphiques, rapports de coût et scènes de stress sont préparés sans revendication de mesure ou d’amélioration runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 7")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.69.0"', 'version: "3.70.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T02:53:24+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas accepter un gain de performance lorsque la suite fonctionnelle requise échoue ;\n'
rules_new = rules_anchor + (
    '- ne pas conclure à une optimisation GPU depuis le FPS, les draw calls ou les primitives seuls ;\n'
    '- ne pas comparer des campagnes GPU dont résolution, renderer, pilote, profil ou V-Sync ne sont pas qualifiés ;\n'
    '- ne pas utiliser le replay d’une capture de frame comme unique baseline temporelle native ;\n'
    '- ne pas réduire la qualité visuelle sans images comparables, revue humaine et profil de repli ;\n'
    '- ne pas fusionner une géométrie globale sans mesurer la perte de granularité du culling ;\n'
    '- ne pas attribuer un pic au coût GPU continu sans vérifier compilations de pipeline, soumission CPU et synchronisation ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 7")
text = replace_once(text, '- progression du Livre IV : 6 chapitres sur 22 ;', '- progression du Livre IV : 7 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 6 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 6 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 7 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 7",
)
old_next = """Les chapitres 1 à 6 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU, captures de profiler, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 7 du Livre IV couvrira passes de rendu, draw calls, overdraw, shaders, lumières, ombres, transparence, post-traitement, VRAM et bande passante. Il utilisera le GPU AMD de référence sans recopier les campagnes CPU du chapitre 6.
"""
new_next = """Les chapitres 1 à 7 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, captures de frame, profils graphiques, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 8 du Livre IV mesurera consommation et pics RAM/VRAM, identifiera fuites, duplications, caches excessifs et allocations temporaires, puis définira des limites par plateforme. Il reprendra les signaux mémoire du chapitre 7 sans recopier son profilage des passes de rendu.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T03:23:02+02:00 — version 3.70.0

- création du chapitre 7 du Livre IV — Profilage GPU et optimisation du rendu ;
- budget GPU, contrat de benchmark, manifeste AMD et scène de stress documentés ;
- Visual Profiler, moniteurs `Performance`, `RenderingServer` et temps GPU de viewport expliqués ;
- draw calls, primitives, passes visibles, ombres et compilations de pipeline distingués ;
- fill rate, overdraw, transparence, LOD, culling, shaders, lumières, ombres et post-traitement encadrés ;
- profils graphiques, captures AMD, inspection RenderDoc et rapport de coût par effet préparés ;
- comparaison visuelle, campagne avant/après, porte de décision et rollback documentés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 8 — Optimisation RAM, VRAM et allocations, niveau Élevée ;
- aucune scène de stress, capture, série GPU, profil qualifié ou amélioration runtime revendiquée.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
