#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
NOW = "2026-07-21T12:47:15+02:00"

index_path = ROOT / "Livre-II/index.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace('version: "1.17.1"', 'version: "1.18.0"', 1)
index = index.replace(
    "26. Outils d’édition internes et pipelines de contenu — à rédiger",
    "26. [Outils d’édition internes et pipelines de contenu](CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md) — **rédigé, repéré, expliqué bloc par bloc, pipelines déterministes et transactions staged documentés, audité au niveau static-review**",
    1,
)
index = index.replace(
    "- [audit du chapitre 25](QA/AUDIT-CHAPITRE-25.md) ;",
    "- [audit du chapitre 25](QA/AUDIT-CHAPITRE-25.md) ;\n- [audit du chapitre 26](QA/AUDIT-CHAPITRE-26.md) ;",
    1,
)
index = index.replace("Les chapitres 3 à 25 ont utilisé **Élevée**.", "Les chapitres 3 à 26 ont utilisé **Élevée**.", 1)
index = index.replace(
    "Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-cinq chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. Les **douze systèmes sur douze** de la partie gameplay sont documentés. Le chapitre 25 distingue faits narratifs, interprétations, quêtes, conséquences, codex et connaissances, tout en laissant les systèmes 14 à 24 propriétaires de leurs états. Les réserves runtime et le PDF restent différés conformément au protocole QA.",
    "Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt-six chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation, les quatre chapitres de plateforme IA locale et les douze systèmes de gameplay sont complets. La partie industrialisation compte **un chapitre sur cinq** : outils d’édition, validation, import, provenance et pipelines de contenu. Les réserves runtime et le PDF restent différés conformément au protocole QA.",
    1,
)
index_path.write_text(index, encoding="utf-8")

roadmap_path = ROOT / "ROADMAP.md"
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = roadmap.replace("- [ ] Industrialisation du projet — 0 chapitre sur 5.", "- [ ] Industrialisation du projet — 1 chapitre rédigé, repéré et audité sur 5.", 1)
roadmap = roadmap.replace("- [x] Convention des outils et contextes appliquée aux chapitres 1 à 25.", "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 26.", 1)
roadmap = roadmap.replace(
    "- [x] Chapitre 25 — faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances et sauvegarde — rédigé et audité au niveau `static-review`.",
    "- [x] Chapitre 25 — faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances et sauvegarde — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 26 — plugins d’éditeur, docks, inspecteurs, validation, importeurs, provenance, staging et pipelines de contenu — rédigé et audité au niveau `static-review`.",
    1,
)
roadmap = roadmap.replace(
    "**Statut M3 : en cours — 25 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. Les douze systèmes de gameplay sont documentés. Le chapitre 25 distingue faits, interprétations, quêtes, conséquences et connaissances, puis coordonne les systèmes 14 à 24 par des ports et des commits multi-autorités. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.",
    "**Statut M3 : en cours — 26 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. Les fondations, la plateforme IA locale et les douze systèmes de gameplay sont documentés. Le premier chapitre d’industrialisation établit plugins, validation, importeurs, provenance et transactions staged sans transférer les autorités runtime. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.",
    1,
)
roadmap_path.write_text(roadmap, encoding="utf-8")

contents_path = ROOT / "contents.txt"
contents = contents_path.read_text(encoding="utf-8")
for anchor, entry in [
    ("Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md", "Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md"),
    ("Livre-II/QA/AUDIT-CHAPITRE-25.md", "Livre-II/QA/AUDIT-CHAPITRE-26.md"),
    ("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-25.yaml", "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-26.yaml"),
]:
    if entry not in contents:
        contents = contents.replace(anchor + "\n", anchor + "\n" + entry + "\n", 1)
contents_path.write_text(contents, encoding="utf-8")

cont_path = ROOT / "CONTINUITE-PROJET.md"
cont = cont_path.read_text(encoding="utf-8")
cont = cont.replace('version: "3.25.2"', 'version: "3.26.0"', 1)
cont = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{NOW}"', cont, count=1)
cont = cont.replace("**En cours : 25 chapitres sur 30.**", "**En cours : 26 chapitres sur 30.**", 1)
cont = cont.replace("26. Outils d’édition internes et pipelines de contenu.", "26. Outils d’édition internes et pipelines de contenu — terminé au niveau `static-review`.", 1)
cont = cont.replace("Chapitres 3 à 25 : **Élevée**.", "Chapitres 3 à 26 : **Élevée**.", 1)
cont = cont.replace("Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.4`.", "Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.6`.", 1)

arch_anchor = """### 11.20 Narration, quêtes, codex et connaissances

- faits sources et interprétations narratives restent distincts ;
- arcs, quêtes, objectifs et codex utilisent des identifiants stables ;
- définitions de conception et états runtime restent séparés ;
- conditions évaluées par un registre fermé et explicable ;
- `INDETERMINATE` n’accorde ni succès ni visibilité ;
- événements sources traités avec identité, empreinte et reçu idempotent ;
- conséquences externes préparées par leurs autorités propriétaires ;
- achèvement et conséquences committés dans un même lot ;
- connaissances relatives à un détenteur, une source et une confiance ;
- mémoire vectorielle dérivée et exclue de l’autorité des sauvegardes ;
- IA locale consultative avec repli déterministe ;
- restauration globale préparée avant remplacement ;
- définitions, vues, caches, index et présentation exclus de la persistance.
"""
arch_add = arch_anchor + """
### 11.21 Outils d’édition internes et pipelines de contenu

- scripts `@tool` isolés du runtime et gardés par le contexte éditeur ;
- cycle de vie des plugins symétrique, sans dock, inspecteur ni importeur résiduel ;
- modifications de scènes et ressources ouvertes intégrées à l’annulation de l’éditeur ;
- sources canoniques, artefacts générés et caches strictement séparés ;
- validation structurée, bornée et fondée sur des codes stables ;
- dépendances explicites, cycles refusés et ordre topologique déterministe ;
- sérialisation canonique avant calcul d’empreinte ;
- manifestes, provenance et reçus conservés avec les artefacts ;
- publication de fichiers par staging, vérification et promotion contrôlée ;
- importeurs versionnés, idempotents et sans réimportation récursive ;
- sortie IA limitée au statut de brouillon jusqu’à validation et approbation ;
- exécution headless disponible pour la validation de contenu ;
- chapitres 14 à 25 maintenus comme autorités exclusives du runtime.
"""
cont = cont.replace(arch_anchor, arch_add, 1)

cont = cont.replace(
    "- ne pas persister un index vectoriel dérivé ;\n\n- ne pas oublier la mise à jour de ce fichier.",
    """- ne pas persister un index vectoriel dérivé ;

- ne pas écrire directement un fichier canonique depuis un bouton d’éditeur ;
- ne pas modifier une scène ouverte sans transaction d’annulation ;
- ne pas utiliser un chemin ou un libellé comme identité de contenu ;
- ne pas exécuter un nom de méthode provenant des données ;
- ne pas mélanger source canonique, artefact généré et cache ;
- ne pas calculer une empreinte depuis le temps réel ou une sérialisation instable ;
- ne pas publier un lot sans staging, vérification et promotion ;
- ne pas promouvoir automatiquement une sortie IA ;
- ne pas lancer un scan ou une réimportation pendant un import actif ;
- ne pas donner au plugin d’éditeur une autorité runtime ;

- ne pas oublier la mise à jour de ce fichier.""",
    1,
)
cont = cont.replace("- progression : 25 chapitres sur 30 ;", "- progression : 26 chapitres sur 30 ;", 1)
cont = cont.replace("- chapitre 25 : version `1.0.0` ;", "- chapitre 25 : version `1.0.0` ;\n- chapitre 26 : version `1.0.0` ;", 1)

old_next = """## 26. Prochaine action

Le chapitre 25 est terminé au niveau `static-review`. La narration distingue faits, interprétations, quêtes, conséquences et connaissances, puis orchestre les systèmes 14 à 24 sans reprendre leur autorité.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : plugins d’éditeur, docks, inspecteurs, importeurs, validateurs de données, génération assistée et pipelines de contenu. Le chapitre 26 industrialisera la production sans déplacer les autorités runtime des chapitres 14 à 25.
"""
new_next = """## 26. Prochaine action

Le chapitre 26 est terminé au niveau `static-review`. Les outils d’édition séparent sources, artefacts et caches, enregistrent provenance et reçus, puis publient par transactions staged sans déplacer les autorités runtime.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : tests unitaires, tests d’intégration, doubles de test, fixtures, simulations déterministes, campagnes de non-régression et critères de passage. Le chapitre 27 vérifiera les contrats des chapitres 1 à 26 sans confondre tests, diagnostics et pipelines de génération.
"""
cont = cont.replace(old_next, new_next, 1)

cont = cont.replace(
    "## 27. Journal\n",
    f"""## 27. Journal

### {NOW} — version 3.26.0

- chapitre 26 créé, relu, corrigé et audité au niveau `static-review` ;
- plugins d’éditeur, docks, inspecteurs, annulation, validation, importeurs et exécution headless documentés ;
- séparation source/artefact/cache, sérialisation canonique, empreintes, manifestes, provenance et reçus explicités ;
- staging, transactions de fichiers, import incrémental et IA limitée aux brouillons documentés ;
- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;
- prochaine action déplacée vers le chapitre 27 — Tests unitaires, tests d’intégration et simulations, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.
""",
    1,
)
cont_path.write_text(cont, encoding="utf-8")

for path in [
    ROOT / "Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md",
    ROOT / "Livre-II/QA/AUDIT-CHAPITRE-26.md",
    ROOT / "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-26.yaml",
]:
    text = path.read_text(encoding="utf-8")
    if "recommended-reasoning" in text or "Niveau de raisonnement conseillé" in text:
        raise SystemExit(f"Process metadata leaked into {path}")

Path(".qa/ch26_finalize.py").unlink()
