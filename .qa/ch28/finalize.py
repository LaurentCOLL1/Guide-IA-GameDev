#!/usr/bin/env python3
from pathlib import Path

STAMP = "2026-07-22T03:13:32+02:00"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


index_path = Path("Livre-II/index.md")
index = index_path.read_text(encoding="utf-8")
index = replace_once(index, 'version: "1.19.0"', 'version: "1.20.0"', "index version")
index = replace_once(
    index,
    "28. Journalisation, diagnostic et reproductibilité — à rédiger",
    "28. [Journalisation, diagnostic et reproductibilité](CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) — **rédigé, repéré, expliqué bloc par bloc, journaux structurés, métriques, traces et paquets de reproduction documentés, audité au niveau static-review**",
    "index chapter 28",
)
index = replace_once(
    index,
    "- [audit du chapitre 27](QA/AUDIT-CHAPITRE-27.md) ;",
    "- [audit du chapitre 27](QA/AUDIT-CHAPITRE-27.md) ;\n- [audit du chapitre 28](QA/AUDIT-CHAPITRE-28.md) ;",
    "index audit 28",
)
index = replace_once(
    index,
    "Les chapitres 3 à 27 ont utilisé **Élevée**.",
    "Les chapitres 3 à 28 ont utilisé **Élevée**.",
    "index reasoning range",
)
index = replace_once(
    index,
    "Les chapitres 17 à 27 utilisent désormais des explications structurées",
    "Les chapitres 17 à 28 utilisent désormais des explications structurées",
    "index explanation range",
)
index_path.write_text(index, encoding="utf-8")

roadmap_path = Path("ROADMAP.md")
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = replace_once(
    roadmap,
    "- [ ] Industrialisation du projet — 2 chapitres rédigés, repérés et audités sur 5.",
    "- [ ] Industrialisation du projet — 3 chapitres rédigés, repérés et audités sur 5.",
    "roadmap industrialization",
)
roadmap = replace_once(
    roadmap,
    "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 27.",
    "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 28.",
    "roadmap contexts",
)
roadmap = replace_once(
    roadmap,
    "- [x] Chapitre 27 — tests unitaires, intégration, doubles, fixtures, simulations déterministes, non-régression et critères de passage — rédigé et audité au niveau `static-review`.",
    "- [x] Chapitre 27 — tests unitaires, intégration, doubles, fixtures, simulations déterministes, non-régression et critères de passage — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 28 — journalisation structurée, sévérité, corrélation, causalité, métriques, traces, rédaction, paquets de diagnostic et support hors ligne — rédigé et audité au niveau `static-review`.",
    "roadmap chapter 28",
)
roadmap = replace_once(
    roadmap,
    "**Statut M3 : en cours — 27 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle de `Project Asteria`. Les fondations, la plateforme IA locale et les douze systèmes de gameplay sont documentés. Les deux premiers chapitres d’industrialisation couvrent les pipelines de contenu puis une stratégie de tests unitaires, d’intégration et de simulations déterministes avec GUT, doubles, fixtures, scénarios versionnés et critères de passage. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.",
    "**Statut M3 : en cours — 28 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle de `Project Asteria`. Les fondations, la plateforme IA locale et les douze systèmes de gameplay sont documentés. Les trois premiers chapitres d’industrialisation couvrent les pipelines de contenu, les tests déterministes, puis la journalisation structurée, les métriques, les traces et les paquets de reproduction minimisés. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.",
    "roadmap status",
)
roadmap_path.write_text(roadmap, encoding="utf-8")

contents_path = Path("contents.txt")
contents = contents_path.read_text(encoding="utf-8")
contents = replace_once(
    contents,
    "Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md\n",
    "Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md\nLivre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md\n",
    "contents chapter 28",
)
contents = replace_once(
    contents,
    "Livre-II/QA/AUDIT-CHAPITRE-27.md\n",
    "Livre-II/QA/AUDIT-CHAPITRE-27.md\nLivre-II/QA/AUDIT-CHAPITRE-28.md\n",
    "contents audit 28",
)
contents = replace_once(
    contents,
    "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml\n",
    "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-27.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-28.yaml\n",
    "contents proof 28",
)
contents_path.write_text(contents, encoding="utf-8")

continuity_path = Path("CONTINUITE-PROJET.md")
continuity = continuity_path.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.27.1"', 'version: "3.28.0"', "continuity version")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-22T01:40:00+02:00"',
    f'last-updated: "{STAMP}"',
    "continuity timestamp",
)
continuity = replace_once(
    continuity,
    "- ne pas employer les calques `temps mur`, `temps mural` ou `temps horloge` ; utiliser `temps basé sur l'horloge système` ;",
    "- ne pas employer les calques `temps mur`, `temps mural` ou `temps horloge` ; utiliser `temps basé sur l'horloge système` ;\n\n- ne pas donner aux journaux, métriques ou traces une autorité métier ;\n- ne pas utiliser l’horloge système pour mesurer une durée ; utiliser un compteur monotone ;\n- ne pas journaliser de mot de passe, jeton, clé, chaîne de connexion, prompt ou réponse IA brute ;\n- ne pas utiliser un identifiant d’instance, un chemin ou un message libre comme label de métrique ;\n- ne pas écrire directement depuis un callback `Logger` multithread ni rappeler la journalisation depuis ce callback ;\n- ne pas exporter récursivement `user://` ; utiliser une liste fermée et des chemins relatifs ;\n- ne pas présenter un marqueur de session comme une preuve certaine de crash ;\n- ne pas présenter une archive ZIP comme chiffrée ou signée ;\n- ne pas échantillonner les événements `ERROR`, `FATAL` ou de sécurité ;\n- ne pas reconstruire un état autoritaire depuis un journal de diagnostic ;",
    "continuity chapter 28 rules",
)
continuity = replace_once(
    continuity,
    "- progression : 27 chapitres sur 30 ;",
    "- progression : 28 chapitres sur 30 ;",
    "continuity progress",
)
continuity = replace_once(
    continuity,
    "- industrialisation : 2 chapitres sur 5 ;",
    "- industrialisation : 3 chapitres sur 5 ;",
    "continuity industrialization",
)
continuity = replace_once(
    continuity,
    "- chapitre 27 : version `1.0.1` ;",
    "- chapitre 27 : version `1.0.1` ;\n- chapitre 28 : version `1.0.0` ;",
    "continuity chapter version",
)
old_next = '''Le chapitre 27 est terminé au niveau `static-review`. La stratégie de tests sépare unités, composants, intégrations, simulations et campagnes de plateforme ; elle contrôle les dépendances, le temps, l’aléatoire, les stockages temporaires, les scénarios et les critères de passage sans revendiquer une exécution runtime non réalisée.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : journalisation structurée, niveaux de sévérité, identifiants d’événements stables, corrélation et causalité, rédaction des secrets, métriques, traces, paquets de diagnostic, manifestes de reproduction, collecte après crash et support hors ligne. Le chapitre 28 exploitera les sorties des tests sans redéfinir leurs suites, fixtures ou scénarios.'''
new_next = '''Le chapitre 28 est terminé au niveau `static-review`. La chaîne d’observabilité distingue journaux, métriques, traces et artefacts ; elle encadre sévérité, temps UTC et monotone, corrélation, causalité, minimisation, rétention, intégrité, consentement et support hors ligne sans revendiquer une exécution runtime non réalisée.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : environnement Python du projet, scripts et CLI typés, configurations versionnées, orchestration des validations et simulations, génération déterministe de données, validation de schémas, parallélisme borné, reprise sur erreur, manifestes, empreintes et artefacts reproductibles. Le chapitre 29 automatisera les contrats des chapitres 26 à 28 sans transférer d’autorité métier aux scripts.'''
continuity = replace_once(continuity, old_next, new_next, "continuity next action")
journal = f'''### {STAMP} — version 3.28.0

- chapitre 28 créé, relu et audité au niveau `static-review` ;
- journaux structurés, sévérités, identifiants stables, temps UTC et monotone, corrélation et causalité documentés ;
- listes autorisées, rédaction des secrets, métriques de faible cardinalité, traces et files bornées encadrées ;
- marqueur de session, manifeste de reproduction, empreintes SHA-256, paquet ZIP, consentement et support hors ligne définis ;
- résultats du chapitre 27 consommés sans redéfinir les suites, scénarios ou golden files ;
- progression portée à 28 chapitres sur 30 et prochaine action déplacée vers le chapitre 29 ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
continuity = replace_once(
    continuity,
    "## 27. Journal\n\n",
    "## 27. Journal\n\n" + journal,
    "continuity journal",
)
continuity_path.write_text(continuity, encoding="utf-8")

print("Chapter 28 governance finalized.")
