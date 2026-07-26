from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T02:53:24+02:00"
CHAPTER_SHA256 = "dc745431b86024af23332bfb05cbf79985201cdcc58182640936df5ba7d796c8"

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
    ".qa/ch06-chapter.part01.b64",
    ".qa/ch06-chapter.part02.b64",
    ".qa/ch06-chapter.part03.b64",
    ".qa/ch06-chapter.part04.b64",
    ".qa/ch06-chapter.part05.b64",
])
actual_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_sha}")

write("Livre-IV/CHAPITRE-06-Profilage-CPU.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-06.md", decode_file(".qa/ch06-audit.zlib.b64"))
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-06.yaml", decode_file(".qa/ch06-proof.zlib.b64"))

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.6.0"', 'version: "0.7.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T01:20:53+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '6. Profilage CPU ;',
    '6. [Profilage CPU](CHAPITRE-06-Profilage-CPU.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 6",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **5 sur 22** ;', '- chapitres rédigés, repérés et audités : **6 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 5 — Journalisation et observabilité locale** ;', '- chapitre courant terminé : **chapitre 6 — Profilage CPU** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 6 — Profilage CPU** ;', '- prochaine entrée du plan maître : **chapitre 7 — Profilage GPU et optimisation du rendu** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 5 sont terminés', 'les chapitres 1 à 6 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 5 — Journalisation et observabilité locale — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur.',
    '- [x] Chapitre 5 — Journalisation et observabilité locale — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 6 — Profilage CPU — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 1 chapitre sur 8.',
    "roadmap chapitre 6",
)
text = replace_once(text, '**Statut M5 : en cours — 5 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 6 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md\nLivre-IV/CHAPITRE-06-Profilage-CPU.md\nLivre-V/index.md',
    "contents chapitre 6",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.5"', 'version: "1.0.6"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T01:20:53+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 5 chapitres sur 22', '> **Statut :** en cours — 6 chapitres sur 22', "plan statut")
anchor = 'Le chapitre 7 couvre le GPU. Validation par amélioration mesurée sans modification fonctionnelle indésirable.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Les scènes de benchmark, captures, budgets CPU et rapports avant/après sont préparés sans revendication de mesure ou d’amélioration runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 6")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.68.0"', 'version: "3.69.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T01:20:53+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas conclure depuis une moyenne seule lorsqu’une distribution ou une queue peut modifier la décision ;\n'
rules_new = rules_anchor + (
    '- ne pas déclarer une amélioration CPU sans benchmark, environnement et contrat d’échantillonnage comparables ;\n'
    '- ne pas supprimer un run de profilage valide parce que son résultat est défavorable ;\n'
    '- ne pas attribuer un temps de frame élevé au CPU sans distinguer temps propre, temps inclusif, rendu et attente ;\n'
    '- ne pas réduire la cadence physique ou IA sans tests fonctionnels, latence et déterminisme adaptés ;\n'
    '- ne pas introduire des threads sans mesurer préparation, travail, attente, fusion et correction du résultat ;\n'
    '- ne pas accepter un gain de performance lorsque la suite fonctionnelle requise échoue ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 6")
text = replace_once(text, '- progression du Livre IV : 5 chapitres sur 22 ;', '- progression du Livre IV : 6 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 5 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 5 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 6 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 6",
)
old_next = """Les chapitres 1 à 5 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, index locaux, dashboards, incidents simulés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-06-Profilage-CPU.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 6 du Livre IV utilisera le profiler Godot et les outils système pour mesurer scripts, physique, navigation, IA et threads, définir des budgets CPU et comparer avant/après. Il consommera les signaux légers du chapitre 5 sans transformer la journalisation en profiler.
"""
new_next = """Les chapitres 1 à 6 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU, captures de profiler, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 7 du Livre IV couvrira passes de rendu, draw calls, overdraw, shaders, lumières, ombres, transparence, post-traitement, VRAM et bande passante. Il utilisera le GPU AMD de référence sans recopier les campagnes CPU du chapitre 6.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T02:53:24+02:00 — version 3.69.0

- création du chapitre 6 du Livre IV — Profilage CPU ;
- budgets de frame, distributions, warm-up, répétitions et contrats de benchmark documentés ;
- Profiler Godot, Monitors, singleton `Performance`, moniteurs personnalisés et chronométrage borné expliqués ;
- analyse des scripts, de la physique, de la navigation, de l’IA et des tâches parallèles structurée ;
- scènes de benchmark, manifestes d’environnement, hypothèses et rapports avant/après préparés ;
- médiane, p95, p99, maximum et dépassements de budget conservés ;
- portes de régression fonctionnelle, retour arrière et approbation humaine encadrés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 7 — Profilage GPU et optimisation du rendu, niveau Élevée ;
- aucune scène de benchmark, capture, série de mesures, budget qualifié ou amélioration runtime revendiquée.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
