from pathlib import Path

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly 1 occurrence, found {count}")
    return text.replace(old, new, 1)

def update_index() -> None:
    path = Path("Livre-II/index.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "1.7.0"', 'version: "1.8.0"', "index version")
    text = replace_once(
        text,
        "15. Relations sociales — à rédiger",
        "15. [Relations sociales](CHAPITRE-15-Relations-sociales.md) — **rédigé, repéré et audité au niveau static-review**",
        "index chapter 15",
    )
    text = replace_once(
        text,
        "- [audit du chapitre 14](QA/AUDIT-CHAPITRE-14.md) ;",
        "- [audit du chapitre 14](QA/AUDIT-CHAPITRE-14.md) ;\n- [audit du chapitre 15](QA/AUDIT-CHAPITRE-15.md) ;",
        "index audit link",
    )
    text = replace_once(
        text,
        "Les chapitres 3 à 14 utilisent **Élevée**.",
        "Les chapitres 3 à 15 utilisent **Élevée**.",
        "index reasoning range",
    )
    old_status = (
        "Le milestone **M3 — Livre II : Développement et architecture** est en cours. "
        "**Quatorze chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. "
        "Les fondations et la plateforme IA locale sont complètes : neuf chapitres de fondation sur neuf et quatre chapitres de plateforme IA sur quatre. "
        "La partie gameplay compte désormais **un système sur douze**. "
        "Le système de personnages documente identité stable, définition de conception, état runtime, statistiques dérivées, scène composée, contrôleurs séparés, apparition, registre actif, événements et sauvegarde validée. "
        "Le chapitre 15 poursuivra avec les relations sociales sans déplacer leur état dans le personnage."
    )
    new_status = (
        "Le milestone **M3 — Livre II : Développement et architecture** est en cours. "
        "**Quinze chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. "
        "Les fondations et la plateforme IA locale sont complètes : neuf chapitres de fondation sur neuf et quatre chapitres de plateforme IA sur quatre. "
        "La partie gameplay compte désormais **deux systèmes sur douze**. "
        "Les personnages possèdent une identité et un état séparés ; les relations sociales utilisent des clés orientées, quatre axes bornés, des causes traçables, un historique limité, des vues mutuelles calculées, des événements typés et une section de sauvegarde indépendante des nœuds actifs. "
        "Le chapitre 16 poursuivra avec la famille et les générations sans déduire la parenté depuis l’affinité."
    )
    text = replace_once(text, old_status, new_status, "index status")
    path.write_text(text, encoding="utf-8")

def update_roadmap() -> None:
    path = Path("ROADMAP.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- [ ] Douze grands systèmes de jeu — 1 chapitre rédigé, repéré et audité sur 12.",
        "- [ ] Douze grands systèmes de jeu — 2 chapitres rédigés, repérés et audités sur 12.",
        "roadmap gameplay count",
    )
    text = replace_once(
        text,
        "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 14.",
        "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 15.",
        "roadmap contexts",
    )
    text = replace_once(
        text,
        "- [x] Chapitre 14 — identité stable, définition, état runtime, statistiques dérivées, scène, contrôleurs, apparition, registre actif, événements et sauvegarde — rédigé et audité au niveau `static-review`.",
        "- [x] Chapitre 14 — identité stable, définition, état runtime, statistiques dérivées, scène, contrôleurs, apparition, registre actif, événements et sauvegarde — rédigé et audité au niveau `static-review`.\n"
        "- [x] Chapitre 15 — relations orientées, axes bornés, causes, historique, vues mutuelles, requêtes, événements et sauvegarde indépendante — rédigé et audité au niveau `static-review`.",
        "roadmap chapter 15",
    )
    old_status = (
        "**Statut M3 : en cours — 14 chapitres rédigés, repérés et audités sur 30.** "
        "Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. "
        "Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. "
        "Le premier des douze systèmes de gameplay est documenté : les personnages possèdent une identité stable distincte du nom, une définition de conception, un état runtime borné, des statistiques dérivées, une scène composée, des contrôleurs séparés, un cycle apparition/disparition, un registre limité aux instances actives, des événements typés et une section de sauvegarde validée avant application. "
        "Le chapitre 15 traitera les relations sociales dans un système séparé. "
        "Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II."
    )
    new_status = (
        "**Statut M3 : en cours — 15 chapitres rédigés, repérés et audités sur 30.** "
        "Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. "
        "Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. "
        "Deux des douze systèmes de gameplay sont documentés : les personnages restent séparés de leur représentation, tandis que les relations sociales sont orientées, bornées, causales, indépendantes des scènes, interrogeables par voisinage et persistées dans une section distincte. "
        "Le chapitre 16 traitera la famille et les générations avec leurs propres invariants. "
        "Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II."
    )
    text = replace_once(text, old_status, new_status, "roadmap status")
    path.write_text(text, encoding="utf-8")

def update_contents() -> None:
    path = Path("contents.txt")
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Livre-II/CHAPITRE-14-Personnages.md",
        "Livre-II/CHAPITRE-14-Personnages.md\nLivre-II/CHAPITRE-15-Relations-sociales.md",
        "contents chapter",
    )
    text = replace_once(
        text,
        "Livre-II/QA/AUDIT-CHAPITRE-14.md\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml",
        "Livre-II/QA/AUDIT-CHAPITRE-14.md\n"
        "Livre-II/QA/AUDIT-CHAPITRE-15.md\n"
        "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml\n"
        "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml",
        "contents qa",
    )
    path.write_text(text, encoding="utf-8")

def update_continuity() -> None:
    path = Path("CONTINUITE-PROJET.md")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "3.15.0"', 'version: "3.16.0"', "continuity version")
    text = replace_once(text, "**En cours : 14 chapitres sur 30.**", "**En cours : 15 chapitres sur 30.**", "continuity chapter count top")
    text = replace_once(text, "15. Relations sociales.", "15. Relations sociales — terminé au niveau `static-review`.", "continuity collection chapter 15")
    text = replace_once(text, "Chapitres 3 à 14 : **Élevée**.", "Chapitres 3 à 15 : **Élevée**.", "continuity reasoning range")

    character_summary = """### 11.9 Personnages

- identité d’instance `chr_...` indépendante du nom affiché et distincte du `StableId` de définition ;
- `CharacterDefinition` comme `Resource` de conception validée et partagée ;
- `CharacterRuntimeState` séparé, borné et dépourvu de référence vers un nœud actif ;
- statistiques dérivées recalculées depuis la définition et les bonus autoritaires ;
- scène composée avec corps, runtime, synchronisation de transform, visuel et contrôleur séparés ;
- réutilisation de la chaîne d’intention du chapitre 6 sans lecture directe de `Input` dans le personnage ;
- initialisation avant entrée dans l’arbre et placement global après `add_child()` ;
- apparition unique par identité et disparition distincte de la suppression métier ;
- registre limité aux instances actives et injecté aux services concernés ;
- événements typés de nom, santé, endurance et état de vie ;
- snapshot strict composé d’identifiants et de valeurs sérialisables, sans nœud, ressource ou cache ;
- section de sauvegarde préparée complètement avant application ;
- relations, famille, agents, combat et compétences maintenus dans des systèmes séparés."""
    social_summary = character_summary + """

### 11.10 Relations sociales

- une relation est une perception orientée `source → cible` entre deux `CharacterId` ;
- les deux directions peuvent diverger et sont persistées séparément ;
- les vues mutuelles sont calculées et distinguent absence de relation et neutralité ;
- affinité, confiance et respect sont bornés de `-100` à `100`, peur de `0` à `100` ;
- chaque mutation exige une cause stable, un système source, un tick logique et au moins un delta ;
- les deltas sont bornés et l’historique récent est limité à `32` entrées ;
- la mutation utilise une copie profonde, une validation complète et `replace_one()` avant émission ;
- le dépôt indexe les relations sortantes sans dépendre des nœuds actifs ;
- l’existence est validée contre un index logique des personnages, y compris hors scène ;
- les événements typés transportent des copies des axes avant et après ;
- les snapshots refusent clés inconnues, conversions silencieuses, doublons et références absentes ;
- la section sociale est préparée avant application et reste indépendante de la section personnages ;
- parenté, agents, factions, réputation et narration restent dans leurs systèmes propres."""
    text = replace_once(text, character_summary, social_summary, "continuity section 11.10")

    detailed_anchor = """Audit : `Livre-II/QA/AUDIT-CHAPITRE-14.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 22. Erreurs à ne pas reproduire"""
    chapter15_detail = """Audit : `Livre-II/QA/AUDIT-CHAPITRE-14.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 22. Chapitre 15 — état détaillé

Fichier : `Livre-II/CHAPITRE-15-Relations-sociales.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- clé orientée fondée sur deux `CharacterId`, avec auto-relation refusée ;
- perceptions `A → B` et `B → A` indépendantes ;
- vues mutuelles calculées à partir des deux directions ;
- quatre axes sociaux bornés : affinité, confiance, respect et peur ;
- commandes sans effet et deltas excessifs refusés ;
- cause, provenance, contexte et tick logique obligatoires ;
- historique causal borné à `32` entrées par direction ;
- copie profonde des axes, états et enregistrements ;
- mutation atomique par candidat validé et `replace_one()` ;
- dépôt en mémoire avec index des relations sortantes ;
- requêtes renvoyant des identifiants plutôt que des nœuds ;
- validation contre un index logique incluant les personnages hors scène ;
- événements typés après remplacement réussi ;
- snapshot JSON strict, versionné et sans nœud ni vue dérivée ;
- section de sauvegarde indépendante préparée avant application ;
- famille, agents, factions, réputation et narration séparés.

Livrables documentés :

- `src/features/social/domain/social_relationship_key.gd` ;
- `src/features/social/domain/social_axes.gd` ;
- `src/features/social/domain/social_change_cause.gd` ;
- `src/features/social/domain/social_change_record.gd` ;
- `src/features/social/domain/social_relationship_state.gd` ;
- `src/features/social/application/change_social_relationship_command.gd` ;
- `src/features/social/application/social_relationship_repository.gd` ;
- `src/features/social/application/social_relationship_changed_event.gd` ;
- `src/features/social/application/social_relationship_service.gd` ;
- `src/features/social/application/social_relationship_query.gd` ;
- `src/features/social/application/mutual_social_view.gd` ;
- `src/features/characters/application/character_identity_index.gd` ;
- `src/features/social/infrastructure/in_memory_social_relationship_repository.gd` ;
- `src/features/social/infrastructure/social_relationship_snapshot_codec.gd` ;
- `src/features/social/infrastructure/social_relationship_save_section.gd` ;
- `scenes/learning/ch15_social_relationships_demo.tscn` ;
- `scenes/learning/ch15_social_relationships_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-15.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 23. Erreurs à ne pas reproduire"""
    text = replace_once(text, detailed_anchor, chapter15_detail, "continuity detailed chapter 15")

    text = replace_once(
        text,
        "- ne pas placer relations, famille, agent, combat ou compétences dans `CharacterRuntimeState` ;\n- ne pas construire le PDF à chaque chapitre ;",
        "- ne pas placer relations, famille, agent, combat ou compétences dans `CharacterRuntimeState` ;\n"
        "- ne pas stocker une relation sociale sur un nœud actif ;\n"
        "- ne pas utiliser un nom affiché comme clé de relation ;\n"
        "- ne pas forcer la symétrie entre deux perceptions ;\n"
        "- ne pas persister un booléen d’amitié contradictoire avec les axes ;\n"
        "- ne pas laisser un axe ou un delta hors bornes ;\n"
        "- ne pas accepter un changement sans cause ni provenance ;\n"
        "- ne pas utiliser l’heure système comme ordre de simulation ;\n"
        "- ne pas conserver un historique social illimité ;\n"
        "- ne pas retourner les collections internes mutables ;\n"
        "- ne pas créer toutes les paires possibles de personnages ;\n"
        "- ne pas valider une relation uniquement contre les personnages actifs ;\n"
        "- ne pas appliquer une section sociale avant validation complète ;\n"
        "- ne pas déduire la parenté depuis l’affinité ;\n"
        "- ne pas laisser une sortie IA modifier directement l’état social ;\n"
        "- ne pas construire le PDF à chaque chapitre ;",
        "continuity social errors",
    )

    text = replace_once(text, "## 23. État courant", "## 24. État courant", "continuity state heading")
    text = replace_once(text, "- progression : 14 chapitres sur 30 ;", "- progression : 15 chapitres sur 30 ;", "continuity progress")
    text = replace_once(text, "- chapitre 14 : version `1.0.0` ;", "- chapitre 14 : version `1.0.0` ;\n- chapitre 15 : version `1.0.0` ;", "continuity chapter version")

    old_next = """## 24. Prochaine action

Chapitre :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-15-Relations-sociales.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu :

- état relationnel séparé de `CharacterRuntimeState` ;
- identité d’une relation fondée sur les identifiants stables des personnages ;
- distinction explicite entre relations dirigées et relations symétriques ;
- axes bornés comme affinité, confiance, peur et respect ;
- modificateurs sociaux, causes, provenance et historique borné ;
- opérations applicatives validées pour faire évoluer une relation ;
- événements typés et requêtes de voisinage social ;
- absence de dépendance directe aux nœuds actifs ;
- sérialisation dans une section de sauvegarde indépendante ;
- validation des références de personnages et gestion des personnages absents de la scène ;
- frontières avec famille, agents autonomes, factions, réputation et narration ;
- démonstration pédagogique, critères d’acceptation et tests à préparer ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.

La recommandation **GPT-5.6 Sol — Élevée** est à annoncer et justifier avant la rédaction."""
    new_next = """## 25. Prochaine action

Chapitre :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-16-Famille-et-generations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu :

- système familial séparé des axes sociaux ;
- liens de filiation dirigés et unions ou fratries traitées selon leurs invariants réels ;
- types de liens explicites : biologique, adoption, tutelle et union ;
- identités fondées sur les `CharacterId`, sans dépendance aux nœuds actifs ;
- refus des auto-liens, doublons, cycles d’ascendance et références inconnues ;
- ancêtres, descendants, fratries et générations calculés par requêtes bornées ;
- absence de génération persistée lorsqu’elle peut être dérivée ;
- dates ou ticks de début et de fin pour les liens temporels ;
- événements typés et historique des changements familiaux ;
- sauvegarde dans une section indépendante validée contre les personnages candidats ;
- gestion des personnages décédés, absents de la scène ou archivés ;
- frontières avec relations sociales, agents, succession, politique et narration ;
- démonstration pédagogique, critères d’acceptation et tests à préparer ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.

La recommandation **GPT-5.6 Sol — Élevée** est à annoncer et justifier avant la rédaction."""
    text = replace_once(text, old_next, new_next, "continuity next action")

    text = replace_once(text, "## 25. Journal", "## 26. Journal", "continuity journal heading")
    journal_anchor = "### 2026-07-19 — version 3.15.0"
    journal_entry = """### 2026-07-19 — version 3.16.0

- création, correction et audit statique du chapitre 15 ;
- relations sociales orientées entre identifiants stables ;
- axes affinité, confiance, respect et peur bornés ;
- causes, provenance, ticks logiques et historique limité ;
- mutation atomique par copie profonde et remplacement validé ;
- requêtes et vues mutuelles indépendantes des scènes ;
- événements typés et index des relations sortantes ;
- snapshot strict et section de sauvegarde indépendante ;
- maintien de la famille, des agents, factions, réputations et récits dans leurs systèmes propres ;
- progression à 15 chapitres sur 30 et systèmes de gameplay à 2 sur 12 ;
- prochaine action déplacée vers le chapitre 16 — Famille et générations, niveau Élevée ;
- aucun PDF construit.

""" + journal_anchor
    text = replace_once(text, journal_anchor, journal_entry, "continuity journal entry")
    path.write_text(text, encoding="utf-8")

update_index()
update_roadmap()
update_contents()
update_continuity()
