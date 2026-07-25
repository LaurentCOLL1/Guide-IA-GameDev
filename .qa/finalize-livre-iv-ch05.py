from __future__ import annotations

import base64
import hashlib
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T01:20:53+02:00"
CHAPTER_SHA256 = "2dbdc275e62b27bf5f27ce44c38c30617b2621e4ad170e5f3e42494c9fe81bf0"

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
    ".qa/ch05-chapter.part01.b64",
    ".qa/ch05-chapter.part02.b64",
    ".qa/ch05-chapter.part03.b64",
    ".qa/ch05-chapter.part04.b64",
    ".qa/ch05-chapter.part05.b64",
])
solo_yaml = """> **[LECTURE] Répartition de référence — Ne pas saisir.**

```yaml
roles:
  runtime_owner:
    accountable_for: [event_contracts, instrumentation]
  platform_owner:
    accountable_for: [collector, rotation, purge]
  security_reviewer:
    accountable_for: [classification, redaction, export_review]
  qa_owner:
    accountable_for: [incident_simulation, evidence_queries]
  product_owner:
    accountable_for: [retention_approval, release_decision]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Runtime :** l’émetteur ne choisit pas seul la rétention.
- **Plateforme :** le collecteur possède la fiabilité technique sans interpréter les causes.
- **Sécurité :** l’export exige une revue distincte.
- **QA :** l’incident simulé valide la capacité de diagnostic.
- **Produit :** la décision de publication reste séparée du tableau de bord.
"""
solo_markdown = """La répartition recommandée est la suivante :

- **Responsable runtime :** possède les contrats d’événements et l’instrumentation ;
- **Responsable plateforme :** possède le collecteur, la rotation et la purge ;
- **Relecteur sécurité :** valide classification, expurgation et export ;
- **Responsable QA :** possède l’incident simulé et les requêtes de preuve ;
- **Responsable produit :** approuve la rétention et conserve l’autorité de décision.

Même lorsqu’une seule personne cumule ces responsabilités, elle conserve des décisions séparées et versionnées.
"""
chapter = replace_once(chapter, solo_yaml, solo_markdown, "modes Solo/Studio")
actual_sha = hashlib.sha256(chapter.encode("utf-8")).hexdigest()
if actual_sha != CHAPTER_SHA256:
    raise RuntimeError(f"empreinte chapitre invalide: {actual_sha}")

audit = decode_file(".qa/ch05-audit.zlib.b64")
audit = replace_once(audit, "- lignes : 1551 ;", "- lignes : 1537 ;", "audit lignes")
audit = replace_once(audit, "- blocs de code ou données : 69 ;", "- blocs de code ou données : 68 ;", "audit blocs")
audit = replace_once(audit, "- marqueurs d’explication structurée : 49 ;", "- marqueurs d’explication structurée : 48 ;", "audit explications")
audit_sha = hashlib.sha256(audit.encode("utf-8")).hexdigest()

proof = decode_file(".qa/ch05-proof.zlib.b64")
proof = replace_once(proof, "chapter-lines: 1551", "chapter-lines: 1537", "preuve lignes")
proof = replace_once(proof, "chapter-code-and-data-blocks: 69", "chapter-code-and-data-blocks: 68", "preuve blocs")
proof = replace_once(proof, "code-explanation-markers: 49", "code-explanation-markers: 48", "preuve explications")
proof = replace_once(proof, "chapter-sha256: a4842063e12c71c6d351f0e0d10557b644d58404785a966064fb91e463ce3a96", f"chapter-sha256: {CHAPTER_SHA256}", "preuve empreinte chapitre")
proof = replace_once(proof, "audit-sha256: ac5349f858367ebc6195d875709806b5eee9097c0ffda3d483ebad7b306c4a2f", f"audit-sha256: {audit_sha}", "preuve empreinte audit")

write("Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md", chapter)
write("Livre-IV/QA/AUDIT-CHAPITRE-05.md", audit)
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-05.yaml", proof)

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.5.0"', 'version: "0.6.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T00:30:21+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '5. Journalisation et observabilité locale ;',
    '5. [Journalisation et observabilité locale](CHAPITRE-05-Journalisation-et-observabilite-locale.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 5",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **4 sur 22** ;', '- chapitres rédigés, repérés et audités : **5 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 4 — Débogage et reproduction des anomalies** ;', '- chapitre courant terminé : **chapitre 5 — Journalisation et observabilité locale** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 5 — Journalisation et observabilité locale** ;', '- prochaine entrée du plan maître : **chapitre 6 — Profilage CPU** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 4 sont terminés', 'les chapitres 1 à 5 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 4 — Débogage et reproduction des anomalies — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Équilibrage, QA et diagnostic — 4 chapitres sur 5.',
    '- [x] Chapitre 4 — Débogage et reproduction des anomalies — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 5 — Journalisation et observabilité locale — rédigé, repéré et audité au niveau `static-review`.\n- [x] Équilibrage, QA et diagnostic — 5 chapitres sur 5.',
    "roadmap chapitre 5",
)
text = replace_once(text, '**Statut M5 : en cours — 4 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 5 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md\nLivre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md\nLivre-V/index.md',
    "contents chapitre 5",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.4"', 'version: "1.0.5"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T00:30:21+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 4 chapitres sur 22', '> **Statut :** en cours — 5 chapitres sur 22', "plan statut")
anchor = 'La journalisation ne doit pas exposer secrets ou données personnelles. Validation par diagnostic d’un incident simulé.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. La politique, le format structuré, le collecteur, le dashboard et la purge sont préparés sans revendication de collecte ou de diagnostic runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 5")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.67.0"', 'version: "3.68.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T00:30:21+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas partager une sauvegarde joueur, un dump ou des journaux bruts sans minimisation, expurgation et revue ;\n'
rules_new = rules_anchor + (
    '- ne pas journaliser un secret, une donnée personnelle ou un texte libre sans contrat explicite, minimisation et expurgation ;\n'
    '- ne pas utiliser un identifiant joueur, une corrélation, un chemin ou un texte libre comme dimension métrique ;\n'
    '- ne pas émettre un événement à chaque frame sans agrégation, échantillonnage ou limite de débit déclarée ;\n'
    '- ne pas régénérer un identifiant de corrélation dans chaque couche d’une même opération ;\n'
    '- ne pas faire tourner des journaux sans politique de rétention et procédure de purge confinée ;\n'
    '- ne pas laisser un tableau de bord ou un seuil d’observabilité modifier directement le gameplay ou une décision de publication ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 5")
text = replace_once(text, '- progression du Livre IV : 4 chapitres sur 22 ;', '- progression du Livre IV : 5 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 4 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 4 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 5 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 5",
)
old_next = """Les chapitres 1 à 4 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, archives diagnostiques, reproductions, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 5 du Livre IV définira les niveaux et catégories de journaux, la corrélation, les métriques, les traces, la rotation, la confidentialité et les tableaux de bord locaux. Il ne recopiera ni le protocole de rapport et de réduction du chapitre 4, ni les campagnes fonctionnelles du chapitre 3.
"""
new_next = """Les chapitres 1 à 5 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, journaux runtime, index locaux, dashboards, incidents simulés, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-06-Profilage-CPU.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 6 du Livre IV utilisera le profiler Godot et les outils système pour mesurer scripts, physique, navigation, IA et threads, définir des budgets CPU et comparer avant/après. Il consommera les signaux légers du chapitre 5 sans transformer la journalisation en profiler.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
journal_entry = """### 2026-07-26T01:20:53+02:00 — version 3.68.0

- création du chapitre 5 du Livre IV — Journalisation et observabilité locale ;
- niveaux, catégories, taxonomie, schéma structuré, horodatage et corrélation documentés ;
- distinction entre événements, métriques et traces établie ;
- émetteur Godot, sinks, JSONL, collecteur Python et index SQLite préparés ;
- rotation, rétention, purge, backpressure, échantillonnage, débit et déduplication encadrés ;
- confidentialité, classification, expurgation, détection de secrets et export local documentés ;
- dashboard local en lecture seule et incident simulé de stockage saturé préparés ;
- modes Solo/Studio et dix diagnostics conformes documentés ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 6 — Profilage CPU, niveau Élevée ;
- aucun journal runtime, collecteur, dashboard, incident simulé, scan de secrets ou mesure de coût revendiqué.

"""
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal_entry, "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
