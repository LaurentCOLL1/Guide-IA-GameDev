#!/usr/bin/env python3
from pathlib import Path
import re

PATH = Path("Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md")
text = PATH.read_text(encoding="utf-8")

CASES = {
    "41.1 Utiliser le texte affiché comme identité de quête": {
        "symptom": "un renommage ou une traduction du titre change l’identité de la quête et casse les références ou sauvegardes existantes.",
        "faulty": "`title_label.text` appartient à la présentation, peut être localisé ou modifié et ne constitue donc pas une identité métier stable.",
        "corrected": "`definition.quest_id` provient de la définition validée et reste identique quels que soient la langue, le titre affiché ou la scène qui présente la quête.",
    },
    "41.2 Traiter un événement comme vérité narrative complète": {
        "symptom": "la réception d’un événement marque immédiatement la quête comme réussie sans normaliser le fait ni vérifier ses objectifs.",
        "faulty": "un événement de gameplay est une observation source, pas une décision narrative complète ; l’affectation directe contourne l’adaptateur, les conditions et l’idempotence.",
        "corrected": "l’adaptateur transforme l’événement en fait typé et identifié ; l’évaluateur de quête décide ensuite de la progression à partir de ce fait validé.",
    },
    "41.3 Évaluer une condition avec du code dynamique": {
        "symptom": "une expression stockée dans les données peut exécuter du code non autorisé et rendre la décision impossible à expliquer ou reproduire.",
        "faulty": "`eval()` laisse le contenu choisir du code exécutable hors du catalogue des conditions, sans type fermé ni motif de refus contrôlé.",
        "corrected": "le registre sélectionne uniquement un évaluateur connu pour le type de condition et retourne une décision explicite, y compris lorsqu’il refuse une condition inconnue.",
    },
    "41.4 Valider une quête avant les conséquences": {
        "symptom": "une panne entre le changement de statut et le crédit monétaire laisse une quête réussie sans récompense, ou une récompense sans réussite correspondante.",
        "faulty": "les deux mutations sont appliquées séquentiellement par des autorités différentes, sans candidat commun, reçu idempotent ni garantie de commit coordonné.",
        "corrected": "`commit_completion()` reçoit les candidats narratif et monétaire avec le même reçu, puis les applique comme un lot cohérent ou refuse l’ensemble.",
    },
    "41.5 Révéler une entrée sur une décision indéterminée": {
        "symptom": "une entrée de codex devient visible alors que les données nécessaires à la décision sont absentes ou encore indéterminées.",
        "faulty": "la condition `!= FALSE` accepte à la fois `TRUE` et `INDETERMINATE`, alors que l’indéterminé ne prouve pas que la condition est satisfaite.",
        "corrected": "la comparaison `== TRUE` réserve la révélation au seul résultat positif explicite et maintient l’entrée cachée pour `FALSE` comme pour `INDETERMINATE`.",
    },
    "41.6 Confondre connaissance et fait global": {
        "symptom": "la croyance d’un personnage devient une vérité mondiale partagée et perd sa source, sa confiance et son statut.",
        "faulty": "réduire `claim` à un booléen global supprime le détenteur, la provenance, le degré de confiance et la possibilité de contradiction.",
        "corrected": "le dépôt conserve l’affirmation complète ; la connaissance reste relative à son détenteur et peut être comparée, révisée ou contredite sans modifier les faits du monde.",
    },
    "41.7 Laisser l’IA achever un objectif": {
        "symptom": "une réponse textuelle non déterministe fixe directement la progression autoritaire d’un objectif.",
        "faulty": "la chaîne `ai_response` est une sortie consultative non fiable ; l’utiliser comme commande contourne les faits, les règles d’objectif et la reproductibilité.",
        "corrected": "`objective_evaluator` calcule la progression depuis l’objectif validé et les faits autoritaires ; une suggestion IA ne peut ni écrire ni valider ce résultat.",
    },
    "41.8 Utiliser l’heure système": {
        "symptom": "la même partie ou le même replay reçoit un tick de départ différent selon la machine et l’instant réel du chargement.",
        "faulty": "l’heure Unix appartient au temps réel et non à l’horloge logique sauvegardée ; elle ne peut donc pas être rejouée avec les mêmes entrées.",
        "corrected": "`world_clock.current_tick` appartient à la simulation, est sauvegardable et permet de retrouver le même ordre narratif après restauration ou replay.",
    },
    "41.9 Charger directement dans les dépôts actifs": {
        "symptom": "un payload invalide peut remplacer partiellement les états actifs avant que l’ensemble du document soit contrôlé.",
        "faulty": "enchaîner décodage et remplacement supprime la phase de candidat complet et ne garantit pas qu’aucune mutation n’a lieu avant la validation globale.",
        "corrected": "`prepare_restore()` construit et valide un candidat détaché ; `commit()` ne remplace les dépôts actifs qu’après la réussite de toute la préparation.",
    },
    "41.10 Persister l’index vectoriel": {
        "symptom": "la sauvegarde contient un cache volumineux qui peut devenir obsolète ou incompatible avec une nouvelle version du moteur d’indexation.",
        "faulty": "l’index vectoriel est dérivé des connaissances canoniques ; le persister duplique l’autorité et peut restaurer des vecteurs qui ne correspondent plus aux sources.",
        "corrected": "la sauvegarde conserve uniquement les enregistrements de connaissance autoritaires ; l’index vectoriel est reconstruit depuis ces données après le chargement.",
    },
}

for heading, values in CASES.items():
    pattern = re.compile(
        rf"(^###\s+{re.escape(heading)}\s*$)(.*?)(?=^###\s+41\.\d+\s+|^##\s+42\.)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise SystemExit(f"Cas introuvable : {heading}")
    body = match.group(2)
    body, count_symptom = re.subn(
        r"^\*\*Symptôme(?: ou risque)?\s*:\*\*.*$",
        f"**Symptôme :** {values['symptom']}",
        body,
        count=1,
        flags=re.MULTILINE,
    )
    body, count_faulty = re.subn(
        r"^\*\*Pourquoi cet exemple est fautif\s*:\*\*.*$",
        f"**Pourquoi cet exemple est fautif :** {values['faulty']}",
        body,
        count=1,
        flags=re.MULTILINE,
    )
    body, count_corrected = re.subn(
        r"^\*\*Pourquoi la correction fonctionne\s*:\*\*.*$",
        f"**Pourquoi la correction fonctionne :** {values['corrected']}",
        body,
        count=1,
        flags=re.MULTILINE,
    )
    if (count_symptom, count_faulty, count_corrected) != (1, 1, 1):
        raise SystemExit(
            f"Cas incomplet {heading}: symptôme={count_symptom}, "
            f"fautif={count_faulty}, corrigé={count_corrected}"
        )
    text = text[: match.start(2)] + body + text[match.end(2) :]

if "Dans le cas «" in text:
    raise SystemExit("Une formulation répétitive subsiste dans le chapitre 25")

PATH.write_text(text, encoding="utf-8")
print("Explications sémantiques spécifiques du chapitre 25 appliquées.")
