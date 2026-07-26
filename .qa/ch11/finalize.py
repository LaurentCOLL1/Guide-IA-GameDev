#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = '2026-07-26T16:42:00+02:00'
CHAPTER_SHA256 = 'fd9dfda927535ecb9b286244b7989f0e422640057213f19528315e272763fda2'
AUDIT_SHA256 = 'efeda70c07aa0f85d33b0ee7243dd6a3eec4bb84228aa8985006fdfc90d9571f'
PART_SHA256 = {'.qa/ch11/chapter.part-01.b64': 'cd67c2caffbce0dec9491411e71369ca178635a5b59a2e19d36535a8fb8bec33', '.qa/ch11/chapter.part-02.b64': 'b44cca99123311f3064d89fe6bae9279ace5901043ad8a938c94042d3aa14bfd', '.qa/ch11/chapter.part-03.b64': '43e6f64ddebd7ed16a92f1cc1cea55d8afcaf62a93db3bd6f1a398f5c178ad6d', '.qa/ch11/chapter.part-04.b64': '945f4f6ab16f0f0f54681abe49b255db6e4f0f16bb799b21a41dd96464e39bad', '.qa/ch11/chapter.part-05.b64': '19ed15dcb4042bd2e59454e23e657b6bf4b879567164676ac6a8ba2c4009831b', '.qa/ch11/chapter.part-06.b64': '6d336de925daa6f4ced636e2dd18db5c25668bc5b7e14c12e35ed9bae5a640fa'}
OLD_NEXT = 'Les chapitres 1 à 10 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, profils de streaming, optimisations de systèmes, seuils qualifiés, tests de stockage, parcours prolongés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-IV/CHAPITRE-11-Architecture-multijoueur.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe chapitre 11 du Livre IV comparera client-serveur, pair-à-pair et modèles hybrides, puis structurera sessions, lobby, découverte, reconnexion, autorité réseau, protocoles, versions, coûts et risques. Le chapitre 12 conservera la synchronisation, l’autorité détaillée et la prédiction.\n'
NEW_NEXT = 'Les chapitres 1 à 11 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, benchmarks CPU/GPU, séries mémoire, profils de streaming, optimisations de systèmes, prototypes multijoueurs, tests de reprise, coûts qualifiés, tests de stockage, parcours prolongés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-IV/CHAPITRE-12-Synchronisation-autorite-et-prediction.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe chapitre 12 du Livre IV définira la réplication des états et événements, l’autorité détaillée, l’interpolation, l’extrapolation, la prédiction client, le rollback, les budgets de bande passante et les diagnostics de désynchronisation. Le chapitre 13 conservera les serveurs dédiés et la sécurité réseau.\n'
JOURNAL_ENTRY = '### 2026-07-26T16:42:00+02:00 — version 3.74.0\n\n- création du chapitre 11 du Livre IV — Architecture multijoueur ;\n- client-serveur, pair-à-pair, hybride, serveur d’écoute, serveur dédié et relais comparés ;\n- client-serveur autoritaire retenu comme défaut documenté de `Project Asteria` ;\n- identité durable, membre de session, pair, génération et ticket distingués ;\n- contrats de session, lobby, protocole, capacités et compatibilité structurés ;\n- initialisation ENet, signaux de cycle de vie, fermeture et chemin hors ligne documentés ;\n- découverte, invitation, admission et transport de jeu séparés ;\n- reconnexion par nouveau pair, ticket opaque, rotation, génération et backoff encadrée ;\n- migration d’hôte maintenue fermée jusqu’à preuve contre le double hôte ;\n- prototype, journaux, catalogue de tests, matrice de risques, coûts, ADR et rollback préparés ;\n- modes Solo/Studio et dix diagnostics conformes documentés ;\n- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;\n- prochaine action déplacée vers le chapitre 12 — Synchronisation, autorité et prédiction, niveau Élevée ;\n- aucune session, reconnexion, migration d’hôte, qualification NAT, mesure de coût ou disponibilité runtime revendiquée.\n\n'

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
for path, expected_sha in PART_SHA256.items():
    content = Path(path).read_text(encoding="ascii").strip()
    actual_sha = hashlib.sha256(content.encode("ascii")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(f"fragment invalide {path}: {actual_sha}")
    payload_parts.append(content)
compressed = base64.b64decode("".join(payload_parts).encode("ascii"))
chapter = zlib.decompress(compressed).decode("utf-8")
actual_chapter_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_chapter_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_chapter_sha}")

audit = Path(".qa/ch11/audit.md").read_text(encoding="utf-8")
actual_audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()
if actual_audit_sha != AUDIT_SHA256:
    raise RuntimeError(f"empreinte audit invalide: {actual_audit_sha}")
proof = Path(".qa/ch11/proof.yaml").read_text(encoding="utf-8")

write("Livre-IV/CHAPITRE-11-Architecture-multijoueur.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-11.md", audit)
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-11.yaml", proof)

path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.11.0"', 'version: "0.12.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T10:13:20+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(text, '11. Architecture multijoueur ;', '11. [Architecture multijoueur](CHAPITRE-11-Architecture-multijoueur.md) — version `1.0.0`, niveau `static-review` ;', "index chapitre 11")
text = replace_once(text, '- chapitres rédigés, repérés et audités : **10 sur 22** ;', '- chapitres rédigés, repérés et audités : **11 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu** ;', '- chapitre courant terminé : **chapitre 11 — Architecture multijoueur** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 11 — Architecture multijoueur** ;', '- prochaine entrée du plan maître : **chapitre 12 — Synchronisation, autorité et prédiction** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 10 sont terminés', 'les chapitres 1 à 11 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
old = '- [x] Chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 5 chapitres sur 8.'
new = '- [x] Chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 11 — Architecture multijoueur — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.\n- [ ] Optimisation et multijoueur — 6 chapitres sur 8.'
text = replace_once(text, old, new, "roadmap chapitre 11")
text = replace_once(text, '**Statut M5 : en cours — 10 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 11 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md\nLivre-V/index.md', 'Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md\nLivre-IV/CHAPITRE-11-Architecture-multijoueur.md\nLivre-V/index.md', "contents chapitre 11")
path.write_text(text, encoding="utf-8", newline="\n")

path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.10"', 'version: "1.0.11"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T10:13:20+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 10 chapitres sur 22', '> **Statut :** en cours — 11 chapitres sur 22', "plan statut")
anchor = 'Le chapitre 12 détaille synchronisation et prédiction. Validation par connexion, déconnexion et reprise contrôlées.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Le diagramme réseau, le contrat de session, le prototype de connexion, la matrice de risques et la stratégie Solo/Studio sont préparés sans revendication de serveur, session, reconnexion ou coût runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 11")
path.write_text(text, encoding="utf-8", newline="\n")

path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.73.0"', 'version: "3.74.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T10:13:20+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas accepter un gain CPU si fonctionnel, latence, déterminisme, mémoire, lisibilité ou testabilité se dégradent ;\n'
rules_new = rules_anchor + (
    '- ne pas utiliser un identifiant de pair comme identité durable, compte ou droit ;\n'
    '- ne pas interpréter le retour immédiat de `create_client()` comme une connexion effective ;\n'
    '- ne pas accepter comme vérité finale un état calculé par le client ;\n'
    '- ne pas retenter sans borne un refus permanent de version, capacité ou admission ;\n'
    '- ne pas appliquer une complétion de reconnexion dont la génération est obsolète ;\n'
    '- ne pas diffuser un ticket de jonction ou de reprise dans une annonce LAN ;\n'
    '- ne pas confondre découverte, invitation, admission et transport de jeu ;\n'
    '- ne pas promettre une migration d’hôte sans transfert d’état, époque et prévention du double hôte ;\n'
    '- ne pas rendre le chemin Solo dépendant d’un annuaire, relais ou service distant ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 11")
text = replace_once(text, '- progression du Livre IV : 10 chapitres sur 22 ;', '- progression du Livre IV : 11 chapitres sur 22 ;', "continuité progression")
text = replace_once(text, '- chapitre 10 du Livre IV : version `1.0.0`, niveau `static-review` ;', '- chapitre 10 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 11 du Livre IV : version `1.0.0`, niveau `static-review` ;', "continuité état chapitre 11")
text = replace_once(text, OLD_NEXT, NEW_NEXT, "continuité prochaine action")
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + JOURNAL_ENTRY, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")

print("Lot matérialisé et gouvernance mise à jour.")
