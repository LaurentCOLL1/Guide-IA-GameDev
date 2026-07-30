from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
PACK = ROOT / "Companion-Pack/Code-Library"
TIMESTAMP = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)

path = ROOT / "Companion-Pack/index.md"
text = read(path)
text = replace_once(text, 'version: "0.4.0"', 'version: "0.5.0"', "index version")
text = replace_once(text, 'last-updated: "2026-07-30T06:36:00+02:00"', f'last-updated: "{TIMESTAMP}"', "index timestamp")
text = replace_once(text, '4. [ ] Code Library ;', '4. [x] [Code Library](Code-Library/README.md) — version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;', "index pack 4")
text = replace_once(text, 'Progression : **3 packs sur 10**. Le Starter Kit, Project Templates et AI Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 4 — Code Library.', 'Progression : **4 packs sur 10**. Le Starter Kit, Project Templates, AI Library et Code Library sont matérialisés et validés dans leur périmètre Linux. Les réserves services IA réels, modèles, réseau distant, performance, Windows graphique, Forward+ GPU, protections GitHub effectives, exports et licence globale restent ouvertes. La prochaine action est le Pack 5 — Database Library.', "index status")
write(path, text)

path = ROOT / "plans/COMPANION-PACK-PLAN-MAITRE.md"
text = read(path)
text = replace_once(text, 'version: "1.3.0"', 'version: "1.4.0"', "plan version")
text = replace_once(text, '> **Statut :** en cours — Pack 3 sur 10 validé', '> **Statut :** en cours — Pack 4 sur 10 validé', "plan status")
text = replace_once(text, '## Pack 4 — Code Library\n\n**Objectifs**', '## Pack 4 — Code Library\n\n**État :** matérialisé en version `1.0.0`, validé sur Linux x86_64 par le run `30517143131` ; réserves performance, Windows graphique, Forward+ GPU, exports et licence globale maintenues.\n\n**Objectifs**', "plan pack 4 state")
write(path, text)

path = ROOT / "ROADMAP.md"
text = read(path)
text = replace_once(text, '**Statut M7 : actif — 3 packs validés sur 10 ; Pack 4, Code Library, suivant.**', '**Statut M7 : actif — 4 packs validés sur 10 ; Pack 5, Database Library, suivant.**', "roadmap status")
text = replace_once(text, '- [ ] Code Library.', '- [x] Code Library — version `1.0.0`, validation Linux `runtime-tested`.', "roadmap pack 4")
write(path, text)

path = ROOT / "contents.txt"
text = read(path)
entry = 'Companion-Pack/Code-Library/README.md\n'
if entry not in text:
    text = replace_once(text, 'Companion-Pack/AI-Library/README.md\n', 'Companion-Pack/AI-Library/README.md\n' + entry, "contents pack 4")
write(path, text)

path = ROOT / "CONTINUITE-PROJET.md"
text = read(path)
text = replace_once(text, 'version: "4.17.0"', 'version: "4.18.0"', "continuity version")
text = replace_once(text, 'last-updated: "2026-07-30T06:36:00+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp")
text = replace_once(text, '- progression du Companion Pack : 3 packs validés sur 10 ;', '- progression du Companion Pack : 4 packs validés sur 10 ;', "continuity progress")
text = replace_once(text, '- AI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec faux serveurs contrôlés ;', '- AI Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 avec faux serveurs contrôlés ;\n- Code Library : version `1.0.0`, niveau `runtime-tested` sur Linux x86_64 ;', "continuity pack 4 state")
text = replace_once(text, 'M7 — Companion Pack est actif. Les Packs 1 à 3 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. AI Library a validé ses contrats, politiques, faux serveurs HTTP/WebSocket, exemples Python et Godot, sans exécuter de service ou modèle fournisseur réel. Les performances, le réseau distant, Windows graphique, Forward+ GPU, exports et licence globale restent réservés.', 'M7 — Companion Pack est actif. Les Packs 1 à 4 sont matérialisés en version `1.0.0` et validés dans leur périmètre Linux. Code Library a validé 18 composants pour 9 concepts, leurs ports Python et GDScript, 16 tests Python, l’import Godot, les démarrages headless et Xvfb Compatibility ainsi que les tests GDScript. Les performances, Windows graphique, Forward+ GPU, exports et licence globale restent réservés.', "continuity next summary")
text = replace_once(text, '```text\nCompanion-Pack/Code-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```', '```text\nCompanion-Pack/Database-Library/README.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```', "continuity next path")
text = replace_once(text, 'Le Pack 4 doit rassembler des composants GDScript et utilitaires Python réutilisables : collections, validation, sérialisation, services et repositories, machines à états, interactions, helpers de tests, conversions et exemples. Chaque API publique devra être documentée, testée, versionnée et contrôlée contre les doublons sans imposer une architecture unique.', 'Le Pack 5 doit matérialiser une bibliothèque de données réutilisable : schémas SQLite, migrations ascendantes, repositories, données synthétiques, scripts d’initialisation, sauvegarde et restauration, validateurs et diagrammes. Aucune migration, restauration, performance, concurrence ou compatibilité de version ne devra être annoncée sans exécution et preuve.', "continuity next scope")

journal = f'''### {TIMESTAMP} — version 4.18.0

- matérialisation du Companion Pack, Pack 4 — Code Library ;
- 18 composants enregistrés pour 9 concepts, avec ports Python et GDScript et registre d’API publique ;
- collections, validation, sérialisation canonique, services, repository mémoire, machine à états, interactions, conversions et aides de test créés ;
- politique anti-doublon appliquée ; files et cache réservés à l’AI Library, bootstrap et composition réservés aux Packs 1 et 2 ;
- 64 fichiers sources du pack validés sans paquet Python tiers, addon binaire, secret ni donnée personnelle ;
- 16 tests Python réussis ;
- import, démarrages headless et Xvfb Compatibility réussis avec Godot `4.7.1.stable.official.a13da4feb` ;
- tests GDScript réussis avec `CODE_LIBRARY_GODOT_TESTS: PASS` ;
- arbre Git propre après runtime ;
- run `30517143131`, artefact `8749316530`, digest `sha256:d7c5bc8ae40c824e0629e290c3765470132fa3141f7f2b59416c8b7310957b52` ;
- correction d’une inférence de type GDScript, durcissement de la CI contre les `SCRIPT ERROR` et arrêt explicite du runner après succès ;
- progression M7 portée à 4 packs sur 10 ;
- prochaine action : `Companion-Pack/Database-Library/README.md`, niveau Élevée ;
- aucune performance, charge, Windows graphique, Forward+ GPU réel, export, release, licence globale, donnée personnelle ou secret validé ou produit.

'''
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, "continuity journal")
write(path, text)

assert (PACK / "VERSION").read_text(encoding="utf-8").strip() == "1.0.0"
assert 'validation-status: "runtime-tested-linux"' in read(PACK / "README.md")
assert 'status: complete' in read(PACK / "qa/VALIDATION-CODE-LIBRARY.yaml")
assert '4 packs sur 10' in read(ROOT / "ROADMAP.md")
assert 'Companion-Pack/Database-Library/README.md' in read(ROOT / "CONTINUITE-PROJET.md")
assert entry.strip() in read(ROOT / "contents.txt")
print(f"Code Library Pack 4 governance finalized at {TIMESTAMP}.")
