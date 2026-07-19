from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 occurrence, got {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


# Protocole QA.
replace_once(
    "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md",
    'version: "1.5.0"',
    'version: "1.6.0"',
    "protocol version",
)

protocol_anchor = """- [ ] Une checklist et un critère d’acceptation sont fournis.\n- [ ] Toute section qui enseigne des erreurs, anti-patterns, pièges ou corrections fournit un exemple fautif, un exemple corrigé et leur différence pour chaque cas.\n\n### Q1.1 — Règle sémantique des erreurs et corrections\n"""
protocol_replacement = """- [ ] Une checklist et un critère d’acceptation sont fournis.\n- [ ] Toute section qui enseigne des erreurs, anti-patterns, pièges ou corrections fournit un exemple fautif, un exemple corrigé et leur différence pour chaque cas.\n- [ ] Chaque bloc de code significatif possède une explication pédagogique proportionnée à sa longueur et à sa complexité.\n\n### Q1.1 — Explication obligatoire de chaque bloc de code\n\nUn bloc de code ne peut pas être considéré comme expliqué par une simple phrase générique. L’explication doit donner au lecteur les informations nécessaires pour comprendre, adapter et diagnostiquer l’extrait.\n\nPour chaque bloc significatif, vérifier explicitement :\n\n1. son rôle et la raison de sa présence ;\n2. le fichier et le chemin où le placer, ou le contexte dans lequel il est seulement lu ;\n3. les entrées, paramètres, types, valeurs par défaut et dépendances utilisées ;\n4. les sorties, valeurs de retour, erreurs, signaux et effets de bord ;\n5. le déroulement des instructions importantes, ligne par ligne ou par groupes cohérents ;\n6. les opérateurs, conversions, conditions et appels non évidents ;\n7. les préconditions, invariants et postconditions protégés ;\n8. le résultat attendu et la manière de le vérifier ;\n9. les variantes raisonnables, limites et erreurs fréquentes pour un débutant ;\n10. le lien avec le bloc précédent, le bloc suivant et l’architecture générale.\n\nUne explication peut être placée avant ou après le bloc, mais elle doit être immédiatement identifiable. Pour un exemple fautif, elle doit aussi expliquer précisément pourquoi il échoue ou devient dangereux. Pour un exemple corrigé, elle doit montrer quelle modification rétablit l’invariant.\n\n**Règle de décision :** si un lecteur débutant doit deviner la fonction d’une ligne importante, d’un paramètre, d’un type, d’un retour ou d’un effet de bord, le bloc est non conforme et le chapitre ne peut pas passer l’audit.\n\n### Q1.2 — Règle sémantique des erreurs et corrections\n"""
replace_once(
    "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md",
    protocol_anchor,
    protocol_replacement,
    "protocol code explanation rule",
)

# Continuité.
replace_once(
    "CONTINUITE-PROJET.md",
    'version: "3.17.0"',
    'version: "3.17.1"',
    "continuity version",
)

continuity_anchor = """- les erreurs et corrections ;\n- les frontières avec les chapitres voisins.\n\n## 4. Configuration de référence\n"""
continuity_replacement = """- les erreurs et corrections ;\n- les frontières avec les chapitres voisins.\n\nTout bloc de code significatif doit être expliqué avec un niveau de détail proportionné à sa complexité. L’explication couvre au minimum son rôle, son emplacement, ses entrées et types, ses paramètres, ses retours et erreurs, ses effets de bord, les instructions non évidentes, les invariants protégés, le résultat attendu et les erreurs fréquentes. Une phrase générique ne suffit pas lorsqu’un lecteur débutant doit encore deviner le fonctionnement d’une ligne importante.\n\nCette règle est une porte d’audit bloquante. Elle s’applique aux nouveaux chapitres et aux corrections rétroactives. Les chapitres 15 et 16 doivent recevoir un enrichissement pédagogique de leurs blocs de code avant le démarrage du chapitre 17.\n\n## 4. Configuration de référence\n"""
replace_once(
    "CONTINUITE-PROJET.md",
    continuity_anchor,
    continuity_replacement,
    "continuity permanent rule",
)

error_anchor = """- ne pas mélanger filiation et succession politique ;\n- ne pas construire le PDF à chaque chapitre ;\n"""
error_replacement = """- ne pas mélanger filiation et succession politique ;\n- ne pas insérer un bloc de code significatif sans expliquer son rôle, ses types, paramètres, retours, effets, invariants, déroulement et résultat attendu ;\n- ne pas considérer une phrase générique comme une explication suffisante d’un bloc complexe ;\n- ne pas démarrer un nouveau chapitre tant que les corrections pédagogiques prioritaires des chapitres précédents ne sont pas fermées ;\n- ne pas construire le PDF à chaque chapitre ;\n"""
replace_once(
    "CONTINUITE-PROJET.md",
    error_anchor,
    error_replacement,
    "continuity errors",
)

next_action_anchor = """## 26. Prochaine action\n\nChapitre :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n"""
next_action_replacement = """## 26. Prochaine action\n\nCorrection pédagogique prioritaire avant tout nouveau chapitre :\n\n> **[LECTURE] Chemins et niveau de correction — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-15-Relations-sociales.md\nLivre-II/CHAPITRE-16-Famille-et-generations.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nObjectif de la correction : reprendre chaque bloc de code significatif et ajouter les explications nécessaires sur le rôle, le chemin, les types, paramètres, retours, effets de bord, instructions non évidentes, invariants, résultat attendu et erreurs fréquentes. Les preuves QA et audits des deux chapitres seront mis à jour après cette passe.\n\nChapitre suivant, bloqué jusqu’à la fermeture de cette correction :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n"""
replace_once(
    "CONTINUITE-PROJET.md",
    next_action_anchor,
    next_action_replacement,
    "continuity next action",
)

journal_anchor = """## 27. Journal\n\n### 2026-07-19 — version 3.17.0\n"""
journal_replacement = """## 27. Journal\n\n### 2026-07-20 — version 3.17.1\n\n- règle pédagogique permanente renforcée : tout bloc de code significatif doit être expliqué en détail ;\n- critères obligatoires ajoutés pour rôle, emplacement, types, paramètres, retours, erreurs, effets de bord, déroulement, invariants et résultat attendu ;\n- une phrase générique n’est plus acceptée comme explication d’un bloc complexe ;\n- correction rétroactive des chapitres 15 et 16 déclarée prioritaire et bloquante avant le chapitre 17 ;\n- protocole QA et roadmap mis à jour ;\n- aucun PDF construit.\n\n### 2026-07-19 — version 3.17.0\n"""
replace_once(
    "CONTINUITE-PROJET.md",
    journal_anchor,
    journal_replacement,
    "continuity journal",
)

# Roadmap.
roadmap_anchor = """- [x] Chapitre 16 — filiation dirigée, adoption, tutelle, unions canoniques, cycles, générations dérivées et sauvegarde familiale — rédigé et audité au niveau `static-review`.\n- [x] Audit rétroactif des sections d’erreurs, diagnostics et anti-patterns des chapitres 1 à 6 — 52 cas avec exemples fautifs et corrigés.\n"""
roadmap_replacement = """- [x] Chapitre 16 — filiation dirigée, adoption, tutelle, unions canoniques, cycles, générations dérivées et sauvegarde familiale — rédigé et audité au niveau `static-review`.\n- [ ] Correction pédagogique du chapitre 15 — expliquer chaque bloc de code significatif avec rôle, types, paramètres, retours, effets, invariants et résultat attendu.\n- [ ] Correction pédagogique du chapitre 16 — expliquer chaque bloc de code significatif avec rôle, types, paramètres, retours, effets, invariants et résultat attendu.\n- [ ] Fermer les audits et preuves QA corrigés des chapitres 15 et 16 avant de commencer le chapitre 17.\n- [x] Audit rétroactif des sections d’erreurs, diagnostics et anti-patterns des chapitres 1 à 6 — 52 cas avec exemples fautifs et corrigés.\n"""
replace_once(
    "ROADMAP.md",
    roadmap_anchor,
    roadmap_replacement,
    "roadmap remediation tasks",
)

status_anchor = """Le chapitre 17 traitera les agents IA et comportements autonomes derrière des contrats et budgets explicites. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.\n"""
status_replacement = """Avant le chapitre 17, une correction pédagogique bloquante doit enrichir les explications des blocs de code des chapitres 15 et 16, puis fermer leurs audits et preuves QA mis à jour. Le chapitre 17 traitera ensuite les agents IA et comportements autonomes derrière des contrats et budgets explicites. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.\n"""
replace_once(
    "ROADMAP.md",
    status_anchor,
    status_replacement,
    "roadmap status gate",
)

print("Code explanation governance patch applied successfully.")
