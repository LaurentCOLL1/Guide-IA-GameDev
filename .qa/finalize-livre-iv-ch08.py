#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

TIMESTAMP = "2026-07-26T08:02:49+02:00"
SOURCE_CHAPTER_SHA256 = "ece7a115c66d3c18efeb79e6f8c4ba0b337858265559b2bff172d8b6e2e7d4ed"
FINAL_CHAPTER_SHA256 = "0662f5fa87f56fc818d995f518df8be397a011c0aed53b5f69354c289fdedd4c"

def read_parts(paths: list[str]) -> str:
    return "".join(Path(path).read_text(encoding="utf-8") for path in paths)

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: occurrence attendue 1, obtenue {count}")
    return text.replace(old, new, 1)

def write(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")

chapter = read_parts([
    ".qa/ch08-chapter.part01.md",
    ".qa/ch08-chapter.part02.md",
    ".qa/ch08-chapter.part03.md",
    ".qa/ch08-chapter.part04.md",
])
source_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if source_sha != SOURCE_CHAPTER_SHA256:
    raise RuntimeError(f"empreinte source invalide: {source_sha}")
chapter = replace_once(
    chapter,
    "## 40. Diagnostics et anti-patterns\n\n### 40.1 Conclure depuis une seule capture",
    "## 40. Diagnostics et anti-patterns\n<!-- qa:error-correction-section -->\n\n### 40.1 Conclure depuis une seule capture",
    "qualification diagnostics",
)
final_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if final_sha != FINAL_CHAPTER_SHA256:
    raise RuntimeError(f"empreinte finale invalide: {final_sha}")

write("Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-08.md", Path(".qa/ch08-audit.md").read_text(encoding="utf-8"))
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-08.yaml", Path(".qa/ch08-proof.yaml").read_text(encoding="utf-8"))

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.8.0"', 'version: "0.9.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T03:23:02+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '8. Optimisation RAM, VRAM et allocations ;',
    '8. [Optimisation RAM, VRAM et allocations](CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 8",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **7 sur 22** ;', '- chapitres rédigés, repérés et audités : **8 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 7 — Profilage GPU et optimisation du rendu** ;', '- chapitre courant terminé : **chapitre 8 — Optimisation RAM, VRAM et allocations** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 8 — Optimisation RAM, VRAM et allocations** ;', '- prochaine entrée du plan maître : **chapitre 9 — Chargements, streaming et gestion des ressources** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 7 sont terminés', 'les chapitres 1 à 8 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 7 — Profilage GPU et optimisation du rendu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 2 chapitres sur 8.',
    '- [x] Chapitre 7 — Profilage GPU et optimisation du rendu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 8 — Optimisation RAM, VRAM et allocations — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 3 chapitres sur 8.',
    "roadmap chapitre 8",
)
text = replace_once(text, '**Statut M5 : en cours — 7 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 8 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md\nLivre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md\nLivre-V/index.md',
    "contents chapitre 8",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.7"', 'version: "1.0.8"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T03:23:02+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 7 chapitres sur 22', '> **Statut :** en cours — 8 chapitres sur 22', "plan statut")
anchor = 'Le chapitre 9 traite le streaming. Validation par réduction mesurée des pics et absence de régression.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Les budgets mémoire, rapports d’allocations, stratégies de cache, tests de longue durée et procédures de diagnostic sont préparés sans revendication de mesure ou d’amélioration runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 8")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.70.0"', 'version: "3.71.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T03:23:02+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas attribuer un pic au coût GPU continu sans vérifier compilations de pipeline, soumission CPU et synchronisation ;\n'
rules_new = rules_anchor + (
    '- ne pas conclure à une fuite depuis une seule capture ou un maximum isolé ;\n'
    '- ne pas comparer working set, mémoire privée, mémoire statique et VRAM comme s’ils mesuraient la même chose ;\n'
    '- ne pas conserver un cache, un pool ou un registre sans capacité, poids, expiration ou échéance explicite ;\n'
    '- ne pas retirer un nœud de l’arbre en supposant qu’il est libéré ;\n'
    '- ne pas dupliquer profondément une ressource sans besoin de mutabilité et provenance déclarés ;\n'
    '- ne pas accepter une baisse de pic si le plateau, les orphelins, la qualité ou les tests se dégradent ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 8")
text = replace_once(text, '- progression du Livre IV : 7 chapitres sur 22 ;', '- progression du Livre IV : 8 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 7 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 7 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 8 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 8",
)
old_next = """Les chapitres 1 à 7 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, captures de frame, profils graphiques, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 8 du Livre IV mesurera consommation et pics RAM/VRAM, identifiera fuites, duplications, caches excessifs et allocations temporaires, puis définira des limites par plateforme. Il reprendra les signaux mémoire du chapitre 7 sans recopier son profilage des passes de rendu.
"""
new_next = """Les chapitres 1 à 8 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, captures, profils, budgets qualifiés, tests de longue durée, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 9 du Livre IV couvrira chargement en arrière-plan, transitions, préchargement, éviction, zones, chunks, priorités, progression fiable, erreurs et annulation. Il consommera les budgets et échéances mémoire du chapitre 8 sans recopier son diagnostic de fuite.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T08:02:49+02:00 — version 3.71.0

- création du chapitre 8 du Livre IV — Optimisation RAM, VRAM et allocations ;
- budgets souples et durs, unités, campagne cyclique et manifeste d’environnement documentés ;
- moniteurs `Performance`, appels `OS`, `RenderingServer` et vue processus Windows distingués ;
- phases, plateaux, pente, percentiles et suspicion de fuite encadrés ;
- durée de vie des nœuds, références faibles, `RefCounted`, signaux et duplications documentée ;
- caches LRU et pondérés, expiration, pools et allocations temporaires bornés ;
- textures, images CPU, ressources vidéo et sous-ressources distinguées ;
- test de longue durée, rapport avant/après, rollback et portes de qualité préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 9 — Chargements, streaming et gestion des ressources, niveau Élevée ;
- aucune campagne mémoire, série, fuite attribuée, cache qualifié ou amélioration runtime revendiquée.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
