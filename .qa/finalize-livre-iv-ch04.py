from __future__ import annotations

import base64
import zlib
from pathlib import Path

TIMESTAMP = "2026-07-26T00:30:21+02:00"

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

write("Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md", decode_file(".qa/ch04-chapter.zlib.b64"))
write("Livre-IV/QA/AUDIT-CHAPITRE-04.md", decode_file(".qa/ch04-audit.zlib.b64"))
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-04.yaml", decode_file(".qa/ch04-proof.zlib.b64"))

# Index du Livre IV
path = Path("Livre-IV/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "0.4.0"', 'version: "0.5.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-26T00:16:25+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(
    text,
    '4. Débogage et reproduction des anomalies ;',
    '4. [Débogage et reproduction des anomalies](CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md) — version `1.0.0`, niveau `static-review` ;',
    "index chapitre 4",
)
text = replace_once(text, '- chapitres rédigés, repérés et audités : **3 sur 22** ;', '- chapitres rédigés, repérés et audités : **4 sur 22** ;', "index progression")
text = replace_once(text, '- chapitre courant terminé : **chapitre 3 — Tests fonctionnels et tests de régression** ;', '- chapitre courant terminé : **chapitre 4 — Débogage et reproduction des anomalies** ;', "index chapitre courant")
text = replace_once(text, '- prochaine entrée du plan maître : **chapitre 4 — Débogage et reproduction des anomalies** ;', '- prochaine entrée du plan maître : **chapitre 5 — Journalisation et observabilité locale** ;', "index prochaine entrée")
text = replace_once(text, 'les chapitres 1 à 3 sont terminés', 'les chapitres 1 à 4 sont terminés', "index statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [x] Chapitre 3 — Tests fonctionnels et tests de régression — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Équilibrage, QA et diagnostic — 3 chapitres sur 5.',
    '- [x] Chapitre 3 — Tests fonctionnels et tests de régression — rédigé, repéré et audité au niveau `static-review`.\n- [x] Chapitre 4 — Débogage et reproduction des anomalies — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Équilibrage, QA et diagnostic — 4 chapitres sur 5.',
    "roadmap chapitre 4",
)
text = replace_once(text, '**Statut M5 : en cours — 3 chapitres rédigés, repérés et audités sur 22.**', '**Statut M5 : en cours — 4 chapitres rédigés, repérés et audités sur 22.**', "roadmap statut")
path.write_text(text, encoding="utf-8", newline="\n")

# Ordre lecteur
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md\nLivre-V/index.md',
    'Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md\nLivre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md\nLivre-V/index.md',
    "contents chapitre 4",
)
path.write_text(text, encoding="utf-8", newline="\n")

# Plan maître
path = Path("plans/LIVRE-IV-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.0.3"', 'version: "1.0.4"', "plan version")
text = replace_once(text, 'last-updated: "2026-07-26T00:16:25+02:00"', f'last-updated: "{TIMESTAMP}"', "plan timestamp")
text = replace_once(text, '> **Statut :** en cours — 3 chapitres sur 22', '> **Statut :** en cours — 4 chapitres sur 22', "plan statut")
anchor = 'Le chapitre 5 traite la collecte systématique des données. Validation par reproduction indépendante par une seconde personne ou un script.\n'
addition = anchor + '\n**État documentaire au 2026-07-26 :** chapitre rédigé, repéré et audité au niveau `static-review`. Les rapports, archives, reproductions et réductions sont préparés sans revendication d’exécution runtime.\n'
text = replace_once(text, anchor, addition, "plan état chapitre 4")
path.write_text(text, encoding="utf-8", newline="\n")

# Continuité
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.66.0"', 'version: "3.67.0"', "continuité version")
text = replace_once(text, 'last-updated: "2026-07-26T00:16:25+02:00"', f'last-updated: "{TIMESTAMP}"', "continuité timestamp")
rules_anchor = '- ne pas modifier un critère après observation des résultats sans créer une nouvelle version applicable aux campagnes futures ;\n'
rules_new = rules_anchor + (
    '- ne pas présenter une hypothèse de cause comme un fait observé dans un rapport d’anomalie ;\n'
    '- ne pas interpréter `NOT_REPRODUCED` comme une preuve d’inexistence du défaut ;\n'
    '- ne pas fermer automatiquement un doublon à partir d’un titre ou d’une signature ;\n'
    '- ne pas fermer un défaut au seul commit du correctif sans vérification et lien de non-régression ;\n'
    '- ne pas partager une sauvegarde joueur, un dump ou des journaux bruts sans minimisation, expurgation et revue ;\n'
)
text = replace_once(text, rules_anchor, rules_new, "continuité règles chapitre 4")
text = replace_once(text, '- progression du Livre IV : 3 chapitres sur 22 ;', '- progression du Livre IV : 4 chapitres sur 22 ;', "continuité progression")
text = replace_once(
    text,
    '- chapitre 3 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    '- chapitre 3 du Livre IV : version `1.0.0`, niveau `static-review` ;\n- chapitre 4 du Livre IV : version `1.0.0`, niveau `static-review` ;',
    "continuité état chapitre 4",
)
old_next = """Les chapitres 1 à 3 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 4 du Livre IV détaillera les rapports exploitables, la reproduction, la réduction des anomalies et la gestion des doublons sans redéfinir les campagnes du chapitre 3.
"""
new_next = """Les chapitres 1 à 4 du Livre IV sont terminés au niveau documentaire et statique. Les métriques, campagnes, registres de risques, portes, anomalies, archives diagnostiques, reproductions, revues spécialisées, playtests et décisions réelles restent non matérialisés. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 5 du Livre IV définira les niveaux et catégories de journaux, la corrélation, les métriques, les traces, la rotation, la confidentialité et les tableaux de bord locaux. Il ne recopiera ni le protocole de rapport et de réduction du chapitre 4, ni les campagnes fonctionnelles du chapitre 3.
"""
text = replace_once(text, old_next, new_next, "continuité prochaine action")
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n### 2026-07-26T00:30:21+02:00 — version 3.67.0\n\n- création du chapitre 4 du Livre IV — Débogage et reproduction des anomalies ;\n- rapports exploitables, environnements, builds, configurations, états initiaux, étapes, attendus et observés documentés ;\n- archives diagnostiques, manifestes d’intégrité, expurgation, fenêtres de journaux et fixtures synthétiques encadrés ;\n- reproduction indépendante humaine ou scriptée préparée ;\n- réduction des étapes, états et entrées documentée sans effacer le rapport original ;\n- doublons, défaut canonique, fermeture, réouverture et lien de non-régression encadrés ;\n- rôles Solo/Studio et triage documentés ;\n- dix diagnostics conformes à la séquence sémantique erreur/correction ;\n- index, roadmap, ordre lecteur, plan maître, audit, preuve et continuité mis à jour ;\n- prochaine action déplacée vers le chapitre 5 — Journalisation et observabilité locale, niveau Élevée ;\n- aucun défaut réel, archive, reproduction, dump, mesure runtime ou donnée joueur revendiqué.\n\n', "continuité journal")
path.write_text(text, encoding="utf-8", newline="\n")
