#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T08:52:20+02:00"
CHAPTER_SHA256 = "d08db60dc4e39297a86f91b29fa4cdddd8033b005295ad46144a2230deb50c5b"


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


chapter = "".join(
    decode_file(path)
    for path in [
        ".qa/ch09-chapter.part01.zlib.b64",
        ".qa/ch09-chapter.part02.zlib.b64",
        ".qa/ch09-chapter.part03.zlib.b64",
        ".qa/ch09-chapter.part04.zlib.b64",
        ".qa/ch09-chapter.part05.zlib.b64",
    ]
)
actual_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_sha}")

write("Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-09.md", decode_file(".qa/ch09-audit.zlib.b64"))
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-09.yaml", decode_file(".qa/ch09-proof.zlib.b64"))

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.9.0"', 'version: "0.10.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T08:02:49+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '9. Chargements, streaming et gestion des ressources ;',
    '9. [Chargements, streaming et gestion des ressources](CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 9",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **8 sur 22** ;', '- chapitres rédigés, repérés et audités : **9 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 8 — Optimisation RAM, VRAM et allocations** ;', '- chapitre courant terminé : **chapitre 9 — Chargements, streaming et gestion des ressources** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 9 — Chargements, streaming et gestion des ressources** ;', '- prochaine entrée du plan maître : **chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 8 sont terminés', 'les chapitres 1 à 9 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 8 — Optimisation RAM, VRAM et allocations — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 3 chapitres sur 8.',
    '- [x] Chapitre 8 — Optimisation RAM, VRAM et allocations — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 9 — Chargements, streaming et gestion des ressources — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 4 chapitres sur 8.',
    "roadmap chapitre 9",
)
text = replace_once(text, '**Statut M5 : en cours — 8 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 9 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md\nLivre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md\nLivre-V/index.md',
    "contents chapitre 9",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.8"', 'version: "1.0.9"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T08:02:49+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 8 chapitres sur 22', '> **Statut :** en cours — 9 chapitres sur 22', "plan statut")
anchor = 'Le chapitre ne redéfinit pas le monde ouvert du Livre III. Validation par parcours prolongé sans fuite ni blocage excessif.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Le gestionnaire de chargement, les profils de streaming, les scènes de transition, les tests de stockage lent et le rapport de temps sont préparés sans revendication de mesure ou d’amélioration runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 9")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.71.0"', 'version: "3.72.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T08:02:49+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas accepter une baisse de pic si le plateau, les orphelins, la qualité ou les tests se dégradent ;\n'
rules_new = rules_anchor + (
    '- ne pas appeler `load_threaded_get()` sur le chemin critique avant que le statut soit `THREAD_LOAD_LOADED` ;\n'
    '- ne pas interroger un chargement fileté dans une boucle bloquante sans rendre la main entre les frames ;\n'
    '- ne pas soumettre une file concurrente sans limite, admission, priorité ni vieillissement ;\n'
    '- ne pas afficher une progression ou une estimation restante qui n’est pas soutenue par des phases et poids mesurables ;\n'
    '- ne pas présenter une annulation logique comme preuve d’arrêt du travail interne déjà lancé ;\n'
    '- ne pas manipuler l’arbre de scène actif depuis un thread arbitraire ;\n'
    '- ne pas évincer une zone depuis la distance seule sans propriétaires, échéances et coût de rechargement ;\n'
    '- ne pas comparer des chargements dont build, stockage, état de cache ou profil diffèrent sans qualification ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 9")
text = replace_once(text, '- progression du Livre IV : 8 chapitres sur 22 ;', '- progression du Livre IV : 9 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 8 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 8 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 9 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 9",
)
old_next = """Les chapitres 1 à 8 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, captures, profils, budgets qualifiés, tests de longue durée, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 9 du Livre IV couvrira chargement en arrière-plan, transitions, préchargement, éviction, zones, chunks, priorités, progression fiable, erreurs et annulation. Il consommera les budgets et échéances mémoire du chapitre 8 sans recopier son diagnostic de fuite.
"""
new_next = """Les chapitres 1 à 9 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, profils de streaming, tests de stockage et parcours prolongés, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 du Livre IV réduira les fréquences de mise à jour, appliquera pooling, activation par distance et LOD logique, découpera scènes et systèmes, puis optimisera signaux, recherches et allocations. Il restera guidé par le profiler et préservera lisibilité, testabilité et contrats fonctionnels.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T08:52:20+02:00 — version 3.72.0

- création du chapitre 9 du Livre IV — Chargements, streaming et gestion des ressources ;
- contrats de transition, budgets, manifeste de stockage et états du gestionnaire documentés ;
- chargement fileté, polling non bloquant, progression pondérée et activation différée encadrés ;
- priorités, vieillissement, admission, coalescence, annulation logique, reprises et replis documentés ;
- dépendances, modes de cache, scènes de transition et racine persistante distingués ;
- zones, chunks, hystérésis, prédiction, mémoire d’admission et éviction bornée structurés ;
- tests de stockage lent, parcours prolongé, rapport avant/après et rollback préparés ;
- progression accessible, erreurs honnêtes, sauvegarde et transfert d’état encadrés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu, niveau Élevée ;
- aucun gestionnaire runtime, profil qualifié, test de stockage, parcours prolongé ou gain revendiqué.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
