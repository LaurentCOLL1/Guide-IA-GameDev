#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T10:13:20+02:00"
CHAPTER_SHA256 = "340d10d8b03495c43272c6242ce85d8c3fad9c28cd9f35c815e9c50d03f59528"
AUDIT_SHA256 = "eb6b4d5a278b4da105746e4a8d90d8dd4a3943c01f06253fcfc720dad4f4319c"
CHUNK_SHA256 = {
    ".qa/ch10-chapter.part01.b64": "ba8469c07c31b347986846fc27972f8d996fa8ed1f880e289563706329c380aa",
    ".qa/ch10-chapter.part02.b64": "11d0af21b7d190ba13ef799576991e2ed6abffa550d3764042111e78aecf08ed",
    ".qa/ch10-chapter.part03.b64": "25bc15fb5a0e9f1f14a6cd55198d6991acf673f5d1bb88cc6348a7766ca21275",
    ".qa/ch10-chapter.part04.b64": "57d14dbbb9ddb1a6bd710f0830afabbfe4c6060f43e96ab2c258871a18088bb6",
}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: occurrence attendue 1, obtenue {count}")
    return text.replace(old, new, 1)


def write(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


payload_parts: list[str] = []
for path, expected_sha in CHUNK_SHA256.items():
    payload = Path(path).read_text(encoding="ascii").strip()
    actual_sha = hashlib.sha256(payload.encode("ascii")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(f"fragment invalide {path}: {actual_sha}")
    payload_parts.append(payload)

compressed = base64.b64decode("".join(payload_parts).encode("ascii"))
chapter = zlib.decompress(compressed).decode("utf-8")
actual_chapter_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_chapter_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_chapter_sha}")

audit = Path(".qa/ch10-audit.md").read_text(encoding="utf-8")
actual_audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()
if actual_audit_sha != AUDIT_SHA256:
    raise RuntimeError(f"empreinte audit invalide: {actual_audit_sha}")

proof = Path(".qa/ch10-proof.yaml").read_text(encoding="utf-8")

write("Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-10.md", audit)
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-10.yaml", proof)

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.10.0"', 'version: "0.11.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T08:52:20+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '10. Optimisation des scènes, scripts et systèmes de jeu ;',
    '10. [Optimisation des scènes, scripts et systèmes de jeu](CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 10",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **9 sur 22** ;', '- chapitres rédigés, repérés et audités : **10 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 9 — Chargements, streaming et gestion des ressources** ;', '- chapitre courant terminé : **chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu** ;', '- prochaine entrée du plan maître : **chapitre 11 — Architecture multijoueur** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 9 sont terminés', 'les chapitres 1 à 10 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 9 — Chargements, streaming et gestion des ressources — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 4 chapitres sur 8.',
    '- [x] Chapitre 9 — Chargements, streaming et gestion des ressources — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 5 chapitres sur 8.',
    "roadmap chapitre 10",
)
text = replace_once(text, '**Statut M5 : en cours — 9 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 10 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md\nLivre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md\nLivre-V/index.md',
    "contents chapitre 10",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.9"', 'version: "1.0.10"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T08:52:20+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 9 chapitres sur 22', '> **Statut :** en cours — 10 chapitres sur 22', "plan statut")
anchor = 'Toute optimisation doit rester justifiée par le profiler. Validation par tests fonctionnels et mesures répétées.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Le catalogue de techniques, les benchmarks, les exemples avant/après, les seuils d’activation et la checklist de revue sont préparés sans revendication de mesure ou d’amélioration runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 10")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.72.0"', 'version: "3.73.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T08:52:20+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas comparer des chargements dont build, stockage, état de cache ou profil diffèrent sans qualification ;\n'
rules_new = rules_anchor + (
    '- ne pas optimiser une scène ou un système sans profil, hypothèse et mesures répétées comparables ;\n'
    '- ne pas supposer que `set_process(false)` désactive la physique, les entrées ou tout le sous-arbre ;\n'
    '- ne pas utiliser visibilité caméra, distance ou LOD logique comme autorité gameplay implicite ;\n'
    '- ne pas laisser une file par frame, un quota ou une fréquence sans borne, équité et latence maximale ;\n'
    '- ne pas rechercher les mêmes nœuds ou groupes à chaque frame lorsqu’un registre stable est possible ;\n'
    '- ne pas créer un pool gameplay sans capacité, remise à zéro et test de réemploi ;\n'
    '- ne pas manipuler l’arbre de scène actif depuis un thread arbitraire ;\n'
    '- ne pas migrer vers une API serveur avant d’avoir mesuré et épuisé les solutions de plus haut niveau ;\n'
    '- ne pas accepter un gain CPU si fonctionnel, latence, déterminisme, mémoire, lisibilité ou testabilité se dégradent ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 10")
text = replace_once(text, '- progression du Livre IV : 9 chapitres sur 22 ;', '- progression du Livre IV : 10 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 9 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 9 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 10 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 10",
)
old_next = """Les chapitres 1 à 9 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, profils de streaming, tests de stockage et parcours prolongés, budgets qualifiés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 du Livre IV réduira les fréquences de mise à jour, appliquera pooling, activation par distance et LOD logique, découpera scènes et systèmes, puis optimisera signaux, recherches et allocations. Il restera guidé par le profiler et préservera lisibilité, testabilité et contrats fonctionnels.
"""
new_next = """Les chapitres 1 à 10 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, profils de streaming, optimisations de systèmes, seuils qualifiés, tests de stockage, parcours prolongés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-11-Architecture-multijoueur.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 11 du Livre IV comparera client-serveur, pair-à-pair et modèles hybrides, puis structurera sessions, lobby, découverte, reconnexion, autorité réseau, protocoles, versions, coûts et risques. Le chapitre 12 conservera la synchronisation, l’autorité détaillée et la prédiction.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T10:13:20+02:00 — version 3.73.0

- création du chapitre 10 du Livre IV — Optimisation des scènes, scripts et systèmes de jeu ;
- contrat de benchmark, manifeste d’environnement, budgets et échantillonnage documentés ;
- fréquences, accumulateurs, time slicing, quotas adaptatifs et priorités encadrés ;
- activation par visibilité, distance, hystérésis et LOD logique distinguée de l’autorité gameplay ;
- groupes, appels différés uniques, références mises en cache et index spatial structurés ;
- cycle de vie des signaux, coalescence, pooling borné, remise à zéro et tampons réutilisés documentés ;
- découpage de scènes, préparation en thread et porte de migration vers les API serveur encadrés ;
- exemples avant/après, seuils, porte de promotion, checklist et rollback préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 11 — Architecture multijoueur, niveau Élevée ;
- aucun benchmark, seuil qualifié, pool runtime, LOD logique, migration serveur ou gain revendiqué.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
