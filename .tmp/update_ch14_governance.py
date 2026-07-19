from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


# Livre II index
path = Path("Livre-II/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.6.0"', 'version: "1.7.0"', "index version")
text = replace_once(
    text,
    '14. Personnages — à rédiger',
    '14. [Personnages](CHAPITRE-14-Personnages.md) — **rédigé, repéré et audité au niveau static-review**',
    "index chapter 14",
)
text = replace_once(
    text,
    '- [audit du chapitre 13](QA/AUDIT-CHAPITRE-13.md) ;',
    '- [audit du chapitre 13](QA/AUDIT-CHAPITRE-13.md) ;\n- [audit du chapitre 14](QA/AUDIT-CHAPITRE-14.md) ;',
    "index audit 14",
)
text = replace_once(
    text,
    'Les chapitres 3 à 13 utilisent **Élevée**.',
    'Les chapitres 3 à 14 utilisent **Élevée**.',
    "index reasoning range",
)
old_status = (
    'Le milestone **M3 — Livre II : Développement et architecture** est en cours. '
    '**Treize chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. '
    'La première partie consacrée aux fondations Godot, à l’architecture, aux données et à la plateforme IA locale est complète : '
    'neuf chapitres de fondation sur neuf et quatre chapitres de plateforme IA sur quatre. '
    'La plateforme couvre désormais mémoire vectorielle dérivée, frontière de service locale, transports HTTP et WebSocket, '
    'tâches bornées, idempotence, backpressure, compatibilité OpenAI isolée, modèle de menaces, séparation production/runtime, '
    'secrets, autorisations, limites, journaux, SBOM, provenance, signature et échec fermé. '
    'Le chapitre 14 ouvre la partie consacrée aux douze systèmes de gameplay avec les personnages.'
)
new_status = (
    'Le milestone **M3 — Livre II : Développement et architecture** est en cours. '
    '**Quatorze chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. '
    'Les fondations et la plateforme IA locale sont complètes : neuf chapitres de fondation sur neuf et quatre chapitres de plateforme IA sur quatre. '
    'La partie gameplay compte désormais **un système sur douze**. Le système de personnages documente identité stable, définition de conception, '
    'état runtime, statistiques dérivées, scène composée, contrôleurs séparés, apparition, registre actif, événements et sauvegarde validée. '
    'Le chapitre 15 poursuivra avec les relations sociales sans déplacer leur état dans le personnage.'
)
text = replace_once(text, old_status, new_status, "index status")
path.write_text(text, encoding="utf-8")


# Roadmap
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '- [ ] Douze grands systèmes de jeu — 0 chapitre sur 12.',
    '- [ ] Douze grands systèmes de jeu — 1 chapitre rédigé, repéré et audité sur 12.',
    "roadmap gameplay count",
)
text = replace_once(
    text,
    '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 13.',
    '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 14.',
    "roadmap context range",
)
text = replace_once(
    text,
    '- [x] Chapitre 13 — modèle de menaces, séparation production/runtime, secrets, authentification, autorisation, TLS, limites, journaux, SBOM, provenance et signature — rédigé et audité au niveau `static-review`.',
    '- [x] Chapitre 13 — modèle de menaces, séparation production/runtime, secrets, authentification, autorisation, TLS, limites, journaux, SBOM, provenance et signature — rédigé et audité au niveau `static-review`.\n'
    '- [x] Chapitre 14 — identité stable, définition, état runtime, statistiques dérivées, scène, contrôleurs, apparition, registre actif, événements et sauvegarde — rédigé et audité au niveau `static-review`.',
    "roadmap chapter 14",
)
old_status = (
    '**Statut M3 : en cours — 13 chapitres rédigés, repérés et audités sur 30.** '
    'Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. '
    'La première partie est complète : neuf chapitres de fondation et quatre chapitres de plateforme IA locale. '
    'Cette plateforme possède une mémoire vectorielle reconstructible, un port indépendant du transport, un processus compagnon, HTTP et WebSocket, '
    'des tâches bornées, l’idempotence, la backpressure, des adaptateurs compatibles OpenAI isolés, un modèle de menaces, des profils d’environnement, '
    'une séparation production/runtime, des secrets hors package, des autorisations par défaut refusées, des limites, des journaux rédigés, '
    'ainsi qu’une préparation au SBOM, à la provenance et à la signature. Le CPU reste le chemin de référence sur Windows/AMD. '
    'Le chapitre 14 ouvre les douze systèmes de jeu avec les personnages. Le workflow léger valide chaque chapitre sans PDF ; '
    'la publication complète reste différée à la fin du Livre II.'
)
new_status = (
    '**Statut M3 : en cours — 14 chapitres rédigés, repérés et audités sur 30.** '
    'Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. '
    'Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. '
    'Le premier des douze systèmes de gameplay est documenté : les personnages possèdent une identité stable distincte du nom, une définition de conception, '
    'un état runtime borné, des statistiques dérivées, une scène composée, des contrôleurs séparés, un cycle apparition/disparition, '
    'un registre limité aux instances actives, des événements typés et une section de sauvegarde validée avant application. '
    'Le chapitre 15 traitera les relations sociales dans un système séparé. Le workflow léger valide chaque chapitre sans PDF ; '
    'la publication complète reste différée à la fin du Livre II.'
)
text = replace_once(text, old_status, new_status, "roadmap status")
path.write_text(text, encoding="utf-8")


# Compilation order
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    'Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md\nLivre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md',
    'Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md\n'
    'Livre-II/CHAPITRE-14-Personnages.md\n'
    'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md',
    "contents chapter 14",
)
text = replace_once(
    text,
    'Livre-II/QA/AUDIT-CHAPITRE-13.md\nLivre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md',
    'Livre-II/QA/AUDIT-CHAPITRE-13.md\n'
    'Livre-II/QA/AUDIT-CHAPITRE-14.md\n'
    'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml\n'
    'Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md',
    "contents audit 14",
)
path.write_text(text, encoding="utf-8")


# Continuity
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.14.0"', 'version: "3.15.0"', "continuity version")
text = replace_once(text, '**En cours : 13 chapitres sur 30.**', '**En cours : 14 chapitres sur 30.**', "continuity book count")
text = replace_once(
    text,
    '14. Personnages.\n15. Relations sociales.',
    '14. Personnages — terminé au niveau `static-review`.\n15. Relations sociales.',
    "continuity chapter list",
)
text = replace_once(
    text,
    'Chapitres 3 à 13 : **Élevée**.',
    'Chapitres 3 à 14 : **Élevée**.\n\n'
    'À chaque clôture de chapitre, le bloc **Prochaine action** doit contenir dans le même bloc de texte le chemin canonique et la ligne '
    '`Niveau GPT-5.6 Sol recommandé : Moyenne ou Élevée`.',
    "continuity closing rule",
)
anchor = (
    '- repli déterministe conservé uniquement pour les indisponibilités fonctionnelles prévues.\n\n'
    '## 12. Chapitre 5 — état résumé'
)
replacement = (
    '- repli déterministe conservé uniquement pour les indisponibilités fonctionnelles prévues.\n\n'
    '### 11.9 Personnages\n\n'
    '- identité d’instance `chr_...` indépendante du nom affiché et distincte du `StableId` de définition ;\n'
    '- `CharacterDefinition` comme `Resource` de conception validée et partagée ;\n'
    '- `CharacterRuntimeState` séparé, borné et dépourvu de référence vers un nœud actif ;\n'
    '- statistiques dérivées recalculées depuis la définition et les bonus autoritaires ;\n'
    '- scène composée avec corps, runtime, synchronisation de transform, visuel et contrôleur séparés ;\n'
    '- réutilisation de la chaîne d’intention du chapitre 6 sans lecture directe de `Input` dans le personnage ;\n'
    '- initialisation avant entrée dans l’arbre et placement global après `add_child()` ;\n'
    '- apparition unique par identité et disparition distincte de la suppression métier ;\n'
    '- registre limité aux instances actives et injecté aux services concernés ;\n'
    '- événements typés de nom, santé, endurance et état de vie ;\n'
    '- snapshot strict composé d’identifiants et de valeurs sérialisables, sans nœud, ressource ou cache ;\n'
    '- section de sauvegarde préparée complètement avant application ;\n'
    '- relations, famille, agents, combat et compétences maintenus dans des systèmes séparés.\n\n'
    '## 12. Chapitre 5 — état résumé'
)
text = replace_once(text, anchor, replacement, "continuity architecture 11.9")
chapter13_end = (
    'Audit : `Livre-II/QA/AUDIT-CHAPITRE-13.md`.\n\n'
    'Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-13.yaml`.\n\n'
    'Décision : accepté avec réserves runtime et PDF de fin de Livre.\n\n'
    '## 21. Erreurs à ne pas reproduire'
)
chapter14_detail = (
    'Audit : `Livre-II/QA/AUDIT-CHAPITRE-13.md`.\n\n'
    'Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-13.yaml`.\n\n'
    'Décision : accepté avec réserves runtime et PDF de fin de Livre.\n\n'
    '## 21. Chapitre 14 — état détaillé\n\n'
    'Fichier : `Livre-II/CHAPITRE-14-Personnages.md`.\n\n'
    'Niveau : **GPT-5.6 Sol — Élevée**.\n\n'
    'Décisions enregistrées :\n\n'
    '- identifiant d’instance aléatoire canonique, indépendant du nom et du chemin ;\n'
    '- espace d’identifiants distinct pour les définitions de contenu ;\n'
    '- `CharacterDefinition`, `CharacterRuntimeState` et snapshot persistant séparés ;\n'
    '- attributs de base validés et statistiques dérivées reconstructibles ;\n'
    '- bonus et valeurs courantes bornés, transforms obligatoirement finis ;\n'
    '- fabrique centralisant les invariants de création ;\n'
    '- règles fondamentales de santé et d’endurance sans anticiper le combat ;\n'
    '- signaux typés transportant l’identifiant stable ;\n'
    '- corps physique, runtime, visuel, synchronisation et contrôleur séparés ;\n'
    '- contrôleur humain réutilisé depuis le chapitre 6 et contrôleur autonome réservé au chapitre 17 ;\n'
    '- initialisation avant `add_child()` et transform global appliqué après ;\n'
    '- une seule représentation active par identité ;\n'
    '- disparition conservant l’état logique ;\n'
    '- registre actif injecté, non global et non persistant ;\n'
    '- codec strict refusant les conversions silencieuses ;\n'
    '- snapshot sans nœud, ressource, contrôleur ou statistique dérivée ;\n'
    '- section de sauvegarde validée et préparée avant mutation ;\n'
    '- systèmes sociaux, familiaux, autonomes, de combat et de compétences séparés.\n\n'
    'Livrables documentés :\n\n'
    '- `src/features/characters/domain/character_id.gd` ;\n'
    '- `src/features/characters/domain/character_definition.gd` ;\n'
    '- `src/features/characters/domain/character_statistics.gd` ;\n'
    '- `src/features/characters/domain/character_runtime_state.gd` ;\n'
    '- `src/features/characters/domain/character_rules.gd` ;\n'
    '- `src/features/characters/application/character_catalog.gd` ;\n'
    '- `src/features/characters/application/character_factory.gd` ;\n'
    '- `src/features/characters/application/character_spawner.gd` ;\n'
    '- `src/features/characters/application/active_character_registry.gd` ;\n'
    '- `src/features/characters/presentation/character_runtime.gd` ;\n'
    '- `src/features/characters/presentation/character_transform_sync.gd` ;\n'
    '- `src/features/characters/presentation/player_character.tscn` ;\n'
    '- `src/features/characters/infrastructure/character_snapshot_codec.gd` ;\n'
    '- `src/features/characters/infrastructure/character_save_section.gd` ;\n'
    '- `src/app/character_bootstrap.gd` ;\n'
    '- `data/characters/aster.tres` ;\n'
    '- `scenes/learning/ch14_characters_demo.tscn` ;\n'
    '- `scenes/learning/ch14_characters_demo.gd`.\n\n'
    'Audit : `Livre-II/QA/AUDIT-CHAPITRE-14.md`.\n\n'
    'Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-14.yaml`.\n\n'
    'Décision : accepté avec réserves runtime et PDF de fin de Livre.\n\n'
    '## 22. Erreurs à ne pas reproduire'
)
text = replace_once(text, chapter13_end, chapter14_detail, "continuity chapter 14 detail")
text = replace_once(
    text,
    '- ne pas conserver le debug de développement en production ;\n- ne pas construire le PDF à chaque chapitre ;',
    '- ne pas conserver le debug de développement en production ;\n'
    '- ne pas utiliser le nom affiché ou un index comme identité de personnage ;\n'
    '- ne pas modifier une `CharacterDefinition` partagée comme état vivant ;\n'
    '- ne pas sauvegarder un nœud, une `Resource` ou une statistique dérivée comme autorité ;\n'
    '- ne pas faire lire `Input` directement au personnage ;\n'
    '- ne pas confondre contrôleur, possession et identité ;\n'
    '- ne pas initialiser le runtime après l’entrée du nœud dans l’arbre ;\n'
    '- ne pas enregistrer deux acteurs actifs pour la même identité ;\n'
    '- ne pas traiter `queue_free()` comme une suppression métier ;\n'
    '- ne pas appliquer une section de personnages avant validation complète ;\n'
    '- ne pas placer relations, famille, agent, combat ou compétences dans `CharacterRuntimeState` ;\n'
    '- ne pas construire le PDF à chaque chapitre ;',
    "continuity error rules",
)
text = replace_once(text, '## 22. État courant', '## 23. État courant', "continuity state heading")
text = replace_once(text, '- progression : 13 chapitres sur 30 ;', '- progression : 14 chapitres sur 30 ;', "continuity state count")
text = replace_once(
    text,
    '- chapitre 13 : version `1.0.0` ;\n- Starter Kit non matérialisé ;',
    '- chapitre 13 : version `1.0.0` ;\n- chapitre 14 : version `1.0.0` ;\n- Starter Kit non matérialisé ;',
    "continuity chapter version",
)
text = replace_once(text, '## 23. Prochaine action', '## 24. Prochaine action', "continuity next heading")
old_next = '''Chapitre :

> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**

```text
Livre-II/CHAPITRE-14-Personnages.md
```

Périmètre attendu :

- premier des douze systèmes de gameplay ;
- identité stable d’un personnage indépendante de son nom affiché ;
- séparation entre définition de conception, état runtime et persistance ;
- données de base, attributs, statistiques dérivées et validation ;
- composition de la scène de personnage et responsabilités des composants ;
- séparation entre personnage, contrôleur, représentation visuelle et corps physique ;
- réutilisation des entrées, caméra et interactions du chapitre 6 ;
- création, apparition, désapparition et registre limité des personnages actifs ;
- événements typés pour les changements importants ;
- sérialisation vers le système de sauvegarde sans inclure les caches dérivés ;
- frontières explicites avec relations sociales, famille, agents autonomes, combat et compétences ;
- démonstration pédagogique, critères d’acceptation et tests à préparer ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire.

Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.'''
new_next = '''Chapitre :

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

La recommandation **GPT-5.6 Sol — Élevée** est à annoncer et justifier avant la rédaction.'''
text = replace_once(text, old_next, new_next, "continuity next chapter")
text = replace_once(text, '## 24. Journal', '## 25. Journal', "continuity journal heading")
journal_anchor = '## 25. Journal\n\n### 2026-07-19 — version 3.14.0'
journal_entry = '''## 25. Journal

### 2026-07-19 — version 3.15.0

- création, correction et audit statique du chapitre 14 ;
- ouverture des douze systèmes de gameplay avec les personnages ;
- identité stable séparée du nom et des définitions de contenu ;
- définition de conception, état runtime et snapshot persistant séparés ;
- attributs bornés et statistiques dérivées reconstructibles ;
- scène composée avec corps, runtime, visuel, synchronisation et contrôleur séparés ;
- apparition, disparition et registre limité aux instances actives ;
- événements typés et sauvegarde validée avant application ;
- maintien des relations, famille, agents, combat et compétences dans leurs chapitres propres ;
- progression à 14 chapitres sur 30 et systèmes de gameplay à 1 sur 12 ;
- règle permanente ajoutée : chaque prochaine action affiche le chemin et le niveau GPT-5.6 Sol dans le même bloc ;
- prochaine action déplacée vers le chapitre 15 — Relations sociales ;
- aucun PDF construit.

### 2026-07-19 — version 3.14.0'''
text = replace_once(text, journal_anchor, journal_entry, "continuity journal entry")
path.write_text(text, encoding="utf-8")
