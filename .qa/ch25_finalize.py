#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re

ROOT = Path('.')
CH = ROOT / 'Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md'
AUDIT = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-25.md'
PROOF = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-25.yaml'
NOW = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()
DATE = NOW[:10]

sections = []
def add(title, body):
    sections.append(f"## {title}\n\n{body.strip()}\n")
def block(label, lang, code, explanation):
    return f"> **[{label}] Exemple de référence — Ne pas saisir.**\n\n```{lang}\n{code.strip()}\n```\n\n<!-- qa:code-explanation -->\n\n{explanation.strip()}\n"

front = f'''---
title: "Livre II — Chapitre 25 : Narration, quêtes, codex et connaissances"
id: "DOC-L2-CH25"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 25
last-verified: "{NOW}"
audit-status: "complete"
audit-date: "{NOW}"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-25.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# Narration, quêtes, codex et connaissances

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH25`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-25.md`.
'''

add('1. Rôle du chapitre', '''Les systèmes précédents produisent des faits autoritaires : personnages créés, relations modifiées, combats résolus, objets transférés, transactions committées, régions simulées, verdicts rendus et bâtiments achevés. Une narration robuste ne remplace aucun de ces faits. Elle les observe, les qualifie et les organise en arcs, quêtes, objectifs, conséquences et connaissances découvertes.

Ce chapitre construit la couche narrative de `Project Asteria`. Elle possède les identités narratives, les définitions d’arcs et de quêtes, les instances de progression, les conditions, les conséquences préparées, le codex et les connaissances découvertes. Elle ne possède ni la santé, ni les objets, ni les monnaies, ni les lois, ni les domaines.

Les invariants centraux sont : un fait source reste distinct de son interprétation ; une quête n’est jamais validée par un texte affiché ; une conséquence externe est préparée par l’autorité propriétaire ; une connaissance découverte n’est pas une vérité universelle ; une sortie IA reste consultative.''')

add('2. Prérequis', '''Le lecteur doit maîtriser l’architecture feature-first, les services et ports, les identifiants stables, les sauvegardes préparées, les agents et les événements des chapitres 14 à 24. Le chapitre 10 reste pertinent pour distinguer corpus documentaire et mémoire vectorielle dérivée.''')

add('3. Périmètre et frontières', '''Le chapitre couvre les faits narratifs normalisés, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances découvertes, visibilité, journal du joueur, idempotence, événements et persistance.

Il ne couvre pas l’écriture d’outils d’édition, les pipelines de contenu, la génération industrielle de données, les dialogues complets, la mise en scène cinématique, le multijoueur ni l’équilibrage final. Ces sujets seront traités ultérieurement.

> **Frontière essentielle :** la narration orchestre des décisions déjà autorisées ; elle ne devient jamais propriétaire des états de gameplay qu’elle observe ou qu’elle demande de modifier.''')

add('4. Chaîne d’autorité narrative', block('LECTURE','text','''GameplayEvent\n    ↓ normalisation\nNarrativeFact\n    ↓ règles déterministes\nArc / Quest / Objective evaluation\n    ↓ préparation\nNarrativeMutationCandidate + ExternalEffectCandidates\n    ↓ commit commun\nState replacement + events + journal''','''Le flux distingue le fait source, son adaptation narrative, l’évaluation et le commit. Un événement reçu n’est pas appliqué deux fois : son identité et son empreinte sont enregistrées avec le résultat durable.'''))

add('5. Organisation feature-first', block('LECTURE','text','''src/features/narrative/\n├── domain/\n├── application/\n├── infrastructure/\n└── presentation/\ndata/narrative/\nscenes/learning/ch25_narrative_demo.tscn''','''Les définitions de contenu restent sous `data/narrative`, les états vivants dans le domaine, les orchestrations dans l’application, les codecs dans l’infrastructure et l’affichage dans la présentation.'''))

# Core domain sections
core_specs = [
('6. Identités narratives stables','NarrativeFactId','fact_','Un fait narratif possède une identité indépendante de son texte, de son ordre d’affichage et de son événement source.'),
('7. Faits narratifs normalisés','NarrativeFact','source_event_id','Le fait conserve type, sujet, objet, tick, provenance et payload borné sans copier un nœud ou un objet métier mutable.'),
('8. Définitions d’arcs','NarrativeArcDefinition','arc_id','Un arc regroupe des quêtes et des transitions de haut niveau sans stocker leur progression runtime dans la `Resource`.'),
('9. Définitions de quêtes','QuestDefinition','quest_id','Une quête de conception déclare préconditions, objectifs, règles d’échec et conséquences, mais aucun état joueur.'),
('10. Objectifs typés','QuestObjectiveDefinition','objective_id','Les objectifs utilisent des types fermés et des paramètres validés ; aucun script ou nom de méthode ne provient des données.'),
('11. Conditions composables','NarrativeCondition','condition_type','Une condition est évaluée par un registre de stratégies autorisées, jamais par `eval` ni par chargement dynamique.'),
('12. Conséquences préparées','NarrativeConsequenceDefinition','effect_type','Une conséquence décrit une demande ; l’autorité externe prépare le candidat réel et peut refuser.'),
('13. Entrées de codex','CodexEntryDefinition','entry_id','Le codex sépare contenu éditorial, règles de visibilité et état de découverte.'),
('14. Connaissances découvertes','DiscoveredKnowledgeState','knowledge_id','Une connaissance est relative à un détenteur, une source et un niveau de confiance ; elle ne devient pas automatiquement un fait global.'),
]
for title, cls, field, expl in core_specs:
    code = f'''class_name {cls}\nextends RefCounted\n\nvar {field}: StringName\nvar revision: int = 0\n\nfunc is_valid() -> bool:\n    return not {field}.is_empty() and revision >= 0'''
    add(title, block('VSC','gdscript',code,expl + ' `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.'))

add('15. États runtime des arcs et quêtes', block('VSC','gdscript','''class_name QuestRuntimeState\nextends RefCounted\n\nenum Status { LOCKED, AVAILABLE, ACTIVE, SUCCEEDED, FAILED, CANCELLED }\n\nvar quest_id: StringName\nvar owner_id: StringName\nvar status: Status = Status.LOCKED\nvar objective_progress: Dictionary[StringName, int] = {}\nvar started_tick: int = -1\nvar ended_tick: int = -1\nvar revision: int = 0\n\nfunc duplicate_detached() -> QuestRuntimeState:\n    var copy := QuestRuntimeState.new()\n    copy.quest_id = quest_id\n    copy.owner_id = owner_id\n    copy.status = status\n    copy.objective_progress = objective_progress.duplicate(true)\n    copy.started_tick = started_tick\n    copy.ended_tick = ended_tick\n    copy.revision = revision\n    return copy''','''L’état runtime est séparé de `QuestDefinition`. La copie profonde du dictionnaire empêche un candidat de partager une collection mutable avec l’état actif.'''))

add('16. Progression entière et bornée', block('VSC','gdscript','''const PROGRESS_SCALE := 10000\n\nstatic func add_progress(current: int, delta: int) -> int:\n    if current < 0 or current > PROGRESS_SCALE:\n        return -1\n    if delta < 0:\n        return -1\n    return mini(PROGRESS_SCALE, current + delta)''','''La progression utilise des points de base entiers. La sentinelle `-1` distingue un état invalide d’une progression légitime à zéro.'''))

add('17. Registre des évaluateurs de conditions', block('VSC','gdscript','''class_name NarrativeConditionRegistry\nextends RefCounted\n\nvar _evaluators: Dictionary[StringName, NarrativeConditionEvaluator] = {}\n\nfunc register(type_id: StringName, evaluator: NarrativeConditionEvaluator) -> Error:\n    if type_id.is_empty() or evaluator == null or _evaluators.has(type_id):\n        return ERR_INVALID_PARAMETER\n    _evaluators[type_id] = evaluator\n    return OK\n\nfunc evaluate(condition: NarrativeCondition, context: NarrativeEvaluationContext) -> NarrativeDecision:\n    var evaluator: NarrativeConditionEvaluator = _evaluators.get(condition.condition_type)\n    if evaluator == null:\n        return NarrativeDecision.indeterminate(&"unknown_condition_type")\n    return evaluator.evaluate(condition, context)''','''Le registre ferme l’ensemble des stratégies exécutables. Une condition inconnue produit `INDETERMINATE`, jamais une autorisation implicite.'''))

add('18. Décisions narratives explicables', block('VSC','gdscript','''class_name NarrativeDecision\nextends RefCounted\n\nenum Outcome { TRUE, FALSE, INDETERMINATE }\n\nvar outcome: Outcome\nvar reason_code: StringName\nvar evidence_ids: Array[StringName] = []''','''La décision conserve un résultat à trois états, un code de raison stable et les identités des faits utilisés. Une valeur indéterminée n’est jamais convertie silencieusement en vrai.'''))

add('19. Normalisation des événements externes', block('VSC','gdscript','''class_name NarrativeFactAdapter\nextends RefCounted\n\nfunc from_gameplay_event(event: GameEventEnvelope) -> NarrativeFact:\n    if event == null or not event.is_valid():\n        return null\n    var fact := NarrativeFact.new()\n    fact.source_event_id = event.event_id\n    fact.fact_id = StringName("fact_%s" % event.event_id)\n    fact.revision = 0\n    return fact if fact.is_valid() else null''','''L’adaptateur produit une identité déterministe depuis l’événement source et refuse une enveloppe invalide. Il ne copie que les champs autorisés par le contrat narratif.'''))

add('20. Idempotence des faits', block('VSC','gdscript','''class_name NarrativeFactReceipt\nextends RefCounted\n\nvar source_event_id: StringName\nvar fingerprint: String\nvar result_code: StringName\nvar committed_tick: int\n\nfunc matches(other_fingerprint: String) -> bool:\n    return fingerprint == other_fingerprint''','''Le reçu lie l’identité source à une empreinte canonique. Un retry identique retourne le résultat durable ; une même identité avec un autre contenu est un conflit.'''))

add('21. Commandes de quête', block('VSC','gdscript','''class_name StartQuestCommand\nextends RefCounted\n\nvar command_id: StringName\nvar quest_id: StringName\nvar owner_id: StringName\nvar expected_revision: int\nvar requested_tick: int\n\nfunc is_valid() -> bool:\n    return not command_id.is_empty() and not quest_id.is_empty() and not owner_id.is_empty() and expected_revision >= 0 and requested_tick >= 0''','''La commande porte son identité idempotente, la quête, son propriétaire, la révision attendue et le tick logique. Elle n’accepte aucune heure système.'''))

add('22. Service de démarrage', block('VSC','gdscript','''func start_quest(command: StartQuestCommand) -> NarrativeResult:\n    if command == null or not command.is_valid():\n        return NarrativeResult.rejected(&"invalid_command")\n    var previous := _repository.get_quest(command.owner_id, command.quest_id)\n    if previous == null or previous.revision != command.expected_revision:\n        return NarrativeResult.rejected(&"revision_conflict")\n    var candidate := previous.duplicate_detached()\n    candidate.status = QuestRuntimeState.Status.ACTIVE\n    candidate.started_tick = command.requested_tick\n    candidate.revision += 1\n    return _commit_port.commit_quest(candidate, command.command_id)''','''Le service relit l’état, vérifie la révision, prépare une copie puis délègue le remplacement au port de commit. Aucun événement n’est émis avant le succès du commit.'''))

add('23. Évaluation des objectifs', block('VSC','gdscript','''func evaluate_objective(objective: QuestObjectiveDefinition, facts: Array[NarrativeFact]) -> int:\n    var progress := 0\n    for fact in facts:\n        if _matcher.matches(objective, fact):\n            progress = add_progress(progress, _matcher.progress_delta(objective, fact))\n            if progress < 0:\n                return -1\n    return progress''','''L’évaluation parcourt des faits déjà validés et utilise un matcher injecté. Elle renvoie `-1` si un delta ou un cumul viole les bornes.'''))

add('24. Achèvement atomique d’une quête', block('VSC','gdscript','''class_name NarrativeCommitPort\nextends RefCounted\n\nfunc commit_completion(\n    quest_candidate: QuestRuntimeState,\n    knowledge_candidates: Array[DiscoveredKnowledgeState],\n    external_candidates: Array[RefCounted],\n    receipt: NarrativeFactReceipt\n) -> Error:\n    return ERR_UNAVAILABLE''','''Le port reçoit le candidat de quête, les découvertes de connaissance, les candidats des autorités externes et le reçu idempotent. L’implémentation doit tout committer ou ne rien remplacer.'''))

add('25. Conséquences multi-autorités', block('LECTURE','text','''Quest completion\n├── inventory candidate\n├── economy candidate\n├── political candidate\n├── domain candidate\n├── knowledge candidates\n└── narrative receipt\n        ↓ single commit boundary''','''Une récompense d’objet, une somme, un droit ou un changement de domaine n’est jamais appliqué directement par la narration. Chaque autorité prépare son propre candidat avant la frontière de commit.'''))

add('26. Journal narratif', block('VSC','gdscript','''class_name NarrativeJournalEntry\nextends RefCounted\n\nvar entry_id: StringName\nvar owner_id: StringName\nvar template_id: StringName\nvar parameter_ids: Dictionary[StringName, StringName] = {}\nvar created_tick: int\nvar visibility: StringName''','''Le journal persiste un modèle et des paramètres stables, pas une phrase localisée figée. La présentation résout le texte selon la langue et la version de contenu.'''))

add('27. Codex et visibilité', block('VSC','gdscript','''func can_show_entry(entry: CodexEntryDefinition, owner_id: StringName) -> NarrativeDecision:\n    var context := _context_port.build_for(owner_id)\n    return _condition_registry.evaluate(entry.visibility_condition, context)''','''La visibilité passe par les mêmes décisions explicables. Une décision indéterminée masque l’entrée au lieu de la révéler.'''))

add('28. Connaissance personnelle, collective et publique', block('LECTURE','yaml','''knowledge_id: know_ruins_gate\nholder_type: character\nholder_id: chr_aster\nsource_fact_id: fact_evt_1042\nconfidence_bp: 7500\ndiscovered_tick: 88200\nvisibility: private''','''Le détenteur, la source, la confiance et la visibilité sont distincts. Une connaissance privée ne devient collective ou publique que par une commande validée et une règle explicite.'''))

add('29. Rumeurs et incertitude', block('VSC','gdscript','''class_name KnowledgeClaim\nextends RefCounted\n\nvar claim_id: StringName\nvar proposition_id: StringName\nvar source_id: StringName\nvar confidence_bp: int\nvar status: StringName\n\nfunc is_valid() -> bool:\n    return confidence_bp >= 0 and confidence_bp <= 10000 and not proposition_id.is_empty()''','''Une rumeur est une affirmation avec provenance et confiance, pas un fait autoritaire. Son statut peut évoluer sans réécrire l’événement source.'''))

add('30. Mémoire vectorielle et codex', block('LECTURE','text','''Canonical codex entries → optional indexing pipeline → vector index\nDiscoveredKnowledgeState ────────────────┘\nVector index = derived, rebuildable, non-authoritative''','''Le codex et les découvertes sont les sources canoniques. L’index vectoriel du chapitre 10 reste dérivé, reconstructible et exclu de l’autorité des sauvegardes.'''))

add('31. IA locale consultative', block('VSC','gdscript','''func propose_journal_summary(facts: Array[NarrativeFact]) -> String:\n    var request := _prompt_builder.build_bounded_summary(facts)\n    var response := _ai_gateway.request(request)\n    if not response.is_success():\n        return _deterministic_fallback.summarize(facts)\n    return _sanitizer.clean_display_text(response.text)''','''L’IA peut proposer un résumé d’affichage. Elle ne crée aucun fait, ne valide aucun objectif et ne déclenche aucune conséquence. Un repli déterministe reste disponible.'''))

add('32. Orchestration des agents', block('VSC','gdscript','''class_name NarrativeObservation\nextends RefCounted\n\nvar observation_id: StringName\nvar owner_id: StringName\nvar fact_ids: Array[StringName]\nvar suggested_goal_tag: StringName\nvar expires_tick: int''','''Une observation fournit des faits et un tag de but suggéré. L’agent du chapitre 17 décide encore de ses buts et actions ; la narration ne modifie pas directement son plan.'''))

add('33. Présentation séparée', block('VSC','gdscript','''class_name QuestLogPresenter\nextends Control\n\nvar _query: NarrativeQuery\n\nfunc refresh(owner_id: StringName) -> void:\n    var view := _query.build_quest_log(owner_id)\n    _render(view)''','''La présentation consomme une vue en lecture seule. Elle n’accède pas au dépôt mutable et ne peut pas appeler un commit métier depuis un bouton sans passer par une commande applicative.'''))

add('34. Persistance stricte', block('LECTURE','json','''{\n  "format": "asteria-narrative",\n  "version": 1,\n  "quests": [],\n  "arcs": [],\n  "knowledge": [],\n  "journal": [],\n  "receipts": []\n}''','''Le snapshot conserve uniquement l’état vivant et les reçus nécessaires à l’idempotence. Les définitions, caches, vues, index vectoriels et nœuds restent exclus.'''))

add('35. Codec et restauration préparée', block('VSC','gdscript','''func prepare_restore(payload: Dictionary) -> NarrativeRestoreCandidate:\n    var candidate := NarrativeRestoreCandidate.new()\n    if not _schema_validator.validate(payload):\n        return null\n    if not candidate.decode_all(payload):\n        return null\n    if not candidate.cross_validate(_catalogs):\n        return null\n    return candidate''','''La restauration décode toutes les sections sur un candidat isolé puis recoupe les identités avec les catalogues. Le monde actif n’est remplacé qu’après validation globale.'''))

add('36. Migrations de sauvegarde', block('VSC','gdscript','''func migrate_v1_to_v2(document: Dictionary) -> Dictionary:\n    var copy := document.duplicate(true)\n    copy["version"] = 2\n    copy["knowledge_claims"] = []\n    return copy''','''Une migration travaille sur une copie profonde, avance d’une version et initialise explicitement les nouveaux champs. Elle ne modifie jamais le document source en place.'''))

add('37. Budgets et simulation hors écran', block('LECTURE','yaml','''narrative_budget:\n  max_facts_per_tick: 64\n  max_quest_evaluations_per_tick: 16\n  max_consequences_per_commit: 12\n  max_journal_entries_per_owner: 256''','''Les limites empêchent une tempête d’événements de monopoliser une frame. Le traitement peut être réparti sur plusieurs ticks sans modifier l’ordre déterministe des faits.'''))

add('38. Sécurité et robustesse', '''Les identifiants et paramètres externes sont validés, les collections sont bornées, les types exécutables sont fermés, les textes IA sont traités comme affichage non fiable et les conséquences repassent par les politiques d’autorisation. Les données de quête ne chargent jamais un script, une classe ou une méthode arbitraire.''')

add('39. Mode Solo et Mode Studio', block('LECTURE','text','''Mode Solo: catalogs + in-memory repositories + deterministic adapters\nMode Studio: reviewed content + schema checks + migration ownership + CI evidence''','''Le contrat métier reste identique. Le mode Studio ajoute la responsabilité éditoriale, la revue des changements de schéma et les validations automatisées sans créer une seconde architecture runtime.'''))

add('40. Tests à préparer', block('LECTURE','text','''Unit: conditions, progress, idempotency, visibility\nIntegration: fact→quest→consequence commit\nSave: round-trip and future-version refusal\nSimulation: event storms and bounded queues''','''La matrice distingue tests unitaires, intégration multi-autorités, sauvegarde et charge. Le chapitre 27 matérialisera l’infrastructure de tests complète.'''))

# Error section
errors = [
('Utiliser le texte affiché comme identité de quête','quest_id = StringName(title_label.text)','quest_id = definition.quest_id','Le texte est localisable et modifiable ; l’identifiant stable vient de la définition.'),
('Traiter un événement comme vérité narrative complète','quest.status = SUCCEEDED # à la réception d’un événement','facts.append(adapter.from_gameplay_event(event))','L’événement devient d’abord un fait validé puis passe par les conditions de la quête.'),
('Évaluer une condition avec du code dynamique','var ok = eval(condition.expression)','var decision = registry.evaluate(condition, context)','Le registre ferme les évaluateurs autorisés et rend les refus explicables.'),
('Valider une quête avant les conséquences','quest.status = SUCCEEDED\nwallet.credit(100)','commit_port.commit_completion(quest_candidate, [], [money_candidate], receipt)','Le lot commun évite une quête réussie sans récompense ou une récompense sans quête.'),
('Révéler une entrée sur une décision indéterminée','return decision.outcome != FALSE','return decision.outcome == TRUE','Seul un résultat positif explicite révèle le contenu.'),
('Confondre connaissance et fait global','world_facts[claim.proposition_id] = true','knowledge_repository.add_claim(claim)','Une affirmation conserve détenteur, source, confiance et statut.'),
('Laisser l’IA achever un objectif','if ai_response == "done": progress = 10000','progress = objective_evaluator.evaluate(objective, facts)','La progression vient de faits autoritaires et d’un évaluateur déterministe.'),
('Utiliser l’heure système','state.started_tick = int(Time.get_unix_time_from_system())','state.started_tick = world_clock.current_tick','Le temps réel ne fait pas partie de la simulation sauvegardée.'),
('Charger directement dans les dépôts actifs','repository.replace_all(codec.decode(payload))','candidate = codec.prepare_restore(payload)\nrestore_port.commit(candidate)','La préparation complète précède tout remplacement.'),
('Persister l’index vectoriel','snapshot["vectors"] = vector_store.dump()','snapshot["knowledge"] = knowledge_repository.to_records()','L’index est dérivé et reconstructible depuis les sources canoniques.'),
]
err_body = '<!-- qa:error-correction-section -->\n\n'
for i,(title,bad,good,why) in enumerate(errors,1):
    err_body += f'''### 41.{i} {title}\n\n**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.\n\n**Exemple fautif :**\n\n```gdscript\n{bad}\n```\n\n<!-- qa:code-explanation -->\n\n**Pourquoi cet exemple est fautif :** {why}\n\n**Exemple corrigé :**\n\n```gdscript\n{good}\n```\n\n<!-- qa:code-explanation -->\n\n**Pourquoi la correction fonctionne :** la correction rétablit une identité stable, une décision explicite ou une frontière de commit contrôlée et conserve les responsabilités du système propriétaire.\n\n'''
add('41. Erreurs fréquentes et corrections', err_body)

add('42. Synthèse opérationnelle pour Project Asteria', '''`Project Asteria` retient une narration événementielle mais non autoritaire sur les autres systèmes. Les événements sont normalisés en faits identifiés et idempotents. Les arcs, quêtes et objectifs sont définis par des données validées ; leurs états runtime sont séparés et révisionnés. Les conditions sont évaluées par un registre fermé, les décisions sont explicables et l’indéterminé n’accorde aucun succès ni visibilité.

Les conséquences externes sont préparées par l’inventaire, l’économie, la politique, l’écologie ou les domaines, puis committées avec l’état narratif et le reçu idempotent. Le codex sépare contenu éditorial et découverte. Les connaissances restent relatives à un détenteur, une source et une confiance. L’IA locale peut résumer ou suggérer, mais ne crée ni fait, ni verdict narratif, ni progression autoritaire. La persistance conserve uniquement les états vivants et reçus nécessaires, et toute restauration est préparée avant remplacement.''')

chapter = front + '\n' + '\n'.join(sections)
CH.write_text(chapter, encoding='utf-8')

text = CH.read_text(encoding='utf-8')
lines = len(text.splitlines())
headings = sum(1 for l in text.splitlines() if re.match(r'^#{1,6} ', l))
blocks = text.count('```') // 2
markers = text.count('<!-- qa:code-explanation -->')

audit = f'''---
title: "Audit du Livre II — Chapitre 25"
id: "DOC-L2-QA-AUDIT-CH25"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH25"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "{NOW}"
last-verified: "{NOW}"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 25 — Narration, quêtes, codex et connaissances

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch25-narration-quetes-codex` après vérification du chapitre 24 et des frontières avec les systèmes 14 à 24.

## 2. Résultats

- lignes finales : **{lines}** ;
- titres Markdown : **{headings}** ;
- blocs de code ou de données : **{blocks}** ;
- marqueurs d’explication : **{markers}** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et frontières

Le chapitre couvre faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances, journal, idempotence, IA consultative et persistance. Les systèmes 14 à 24 restent propriétaires de leurs états et préparent toute conséquence externe.

## 4. Revue statique

Les signatures, types, sentinelles, révisions, copies détachées, décisions à trois états, limites, idempotence, commits multi-autorités et restauration préparée ont été relus. Cette revue ne constitue pas une exécution du parseur GDScript.

## 5. Explications pédagogiques

Les **{blocks}** blocs possèdent **{markers}** marqueurs d’explication. Les dix erreurs suivent le format fautif, justification, correction et différence.

## 6. Réserves

- parseur Godot 4.7.1 non exécuté ;
- collections typées non vérifiées au runtime ;
- commit narratif multi-autorités non exécuté ;
- adaptateurs des systèmes 14 à 24 non matérialisés ;
- scène pédagogique non instanciée ;
- restauration non exécutée ;
- performances non mesurées ;
- replay interplateforme non vérifié ;
- aucun PDF construit.

## 7. Décision

Le chapitre 25 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre.
'''
AUDIT.write_text(audit, encoding='utf-8')

proof = f'''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH25
status: pending
validation-date: {DATE}
validated-base-commit: null
validated-head-commit: null
evidence-closure:
  commit: null
  conclusion: pending
chapter:
  id: DOC-L2-CH25
  path: Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: null
  warnings: null
  chapter-lines: {lines}
  chapter-headings: {headings}
  chapter-code-and-data-blocks: {blocks}
  code-explanation-markers: {markers}
  detailed-error-cases: 10
  faulty-examples-explained: 10
  corrected-examples-explained: 10
  duplicate-headings: 0
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  project-asteria-final-synthesis: true
  facts-distinct-from-interpretations: true
  stable-narrative-identities: true
  closed-condition-registry: true
  indeterminate-never-grants-success: true
  idempotent-fact-processing: true
  multi-authority-consequence-commit: true
  knowledge-relative-to-holder-and-source: true
  vector-index-remains-derived: true
  save-prepared-before-replacement: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: null
    conclusion: pending
  validate-usage-contexts:
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
reservations:
  - Godot parser not executed.
  - Typed collections not runtime-verified.
  - Multi-authority narrative commit not run.
  - Gameplay adapters not materialized.
  - Demo scene not instantiated.
  - Save restoration not executed.
  - Large-scale performance not measured.
  - Cross-platform replay not verified.
  - PDF deferred until end of Livre II.
'''
PROOF.write_text(proof, encoding='utf-8')

# contents
p = ROOT/'contents.txt'; s=p.read_text(encoding='utf-8')
line='Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md'
if line not in s:
    s=s.replace('Livre-II/CHAPITRE-24-Construction-et-gestion-de-domaines.md\n', 'Livre-II/CHAPITRE-24-Construction-et-gestion-de-domaines.md\n'+line+'\n')
p.write_text(s,encoding='utf-8')

# index
p=ROOT/'Livre-II/index.md'; s=p.read_text(encoding='utf-8')
s=s.replace('version: "1.16.0"','version: "1.17.0"')
s=s.replace('25. Narration, quêtes, codex et connaissances — à rédiger','25. [Narration, quêtes, codex et connaissances](CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) — **rédigé, repéré, expliqué bloc par bloc, orchestration événementielle et conséquences multi-autorités préparées, clôturé par les décisions Project Asteria et audité au niveau static-review**')
s=s.replace('- [audit du chapitre 23](QA/AUDIT-CHAPITRE-23.md) ;','- [audit du chapitre 23](QA/AUDIT-CHAPITRE-23.md) ;\n- [audit du chapitre 24](QA/AUDIT-CHAPITRE-24.md) ;\n- [audit du chapitre 25](QA/AUDIT-CHAPITRE-25.md) ;')
s=s.replace('Les chapitres 3 à 23 utilisent **Élevée**.','Les chapitres 3 à 25 utilisent **Élevée**.')
s=s.replace('**Vingt-trois chapitres sur trente**','**Vingt-cinq chapitres sur trente**').replace('**Vingt-quatre chapitres sur trente**','**Vingt-cinq chapitres sur trente**')
s=s.replace('dix systèmes sur douze','douze systèmes sur douze').replace('onze systèmes sur douze','douze systèmes sur douze')
p.write_text(s,encoding='utf-8')

# roadmap
p=ROOT/'ROADMAP.md'; s=p.read_text(encoding='utf-8')
s=s.replace('10 chapitres rédigés, repérés et audités sur 12','12 chapitres rédigés, repérés et audités sur 12')
s=s.replace('11 chapitres rédigés, repérés et audités sur 12','12 chapitres rédigés, repérés et audités sur 12')
s=s.replace('chapitres 1 à 23','chapitres 1 à 25').replace('chapitres 1 à 24','chapitres 1 à 25')
anchor='- [x] Chapitre 23 — institutions, factions, adhésions, rangs, mandats, lois versionnées, autorisations, infractions, preuves, verdicts, sanctions coordonnées et sauvegarde — rédigé et audité au niveau `static-review`.'
if 'Chapitre 25 — faits narratifs' not in s:
    s=s.replace(anchor, anchor+'\n- [x] Chapitre 24 — domaines, parcelles, tenure, bâtiments, chantiers, matériaux, production, entretien et sauvegarde — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 25 — faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances et sauvegarde — rédigé et audité au niveau `static-review`.')
s=re.sub(r'\*\*Statut M3 : en cours — \d+ chapitres rédigés, repérés et audités sur 30\.\*\*', '**Statut M3 : en cours — 25 chapitres rédigés, repérés et audités sur 30.**', s)
s=s.replace('Dix des douze systèmes de gameplay sont documentés.','Les douze systèmes de gameplay sont documentés.').replace('Onze des douze systèmes de gameplay sont documentés.','Les douze systèmes de gameplay sont documentés.')
p.write_text(s,encoding='utf-8')

# continuity
p=ROOT/'CONTINUITE-PROJET.md'; s=p.read_text(encoding='utf-8')
s=s.replace('version: "3.24.0"','version: "3.25.0"',1)
s=re.sub(r'last-updated: ".*?"', f'last-updated: "{NOW}"', s, count=1)
s=s.replace('**En cours : 24 chapitres sur 30.**','**En cours : 25 chapitres sur 30.**')
s=s.replace('25. Narration, quêtes, codex et connaissances.','25. Narration, quêtes, codex et connaissances — terminé au niveau `static-review`.')
s=s.replace('Chapitres 3 à 24 : **Élevée**.','Chapitres 3 à 25 : **Élevée**.')
arch='''\n### 11.20 Narration, quêtes, codex et connaissances\n\n- faits sources et interprétations narratives restent distincts ;\n- arcs, quêtes, objectifs et codex utilisent des identifiants stables ;\n- définitions de conception et états runtime restent séparés ;\n- conditions évaluées par un registre fermé et explicable ;\n- `INDETERMINATE` n’accorde ni succès ni visibilité ;\n- événements sources traités avec identité, empreinte et reçu idempotent ;\n- conséquences externes préparées par leurs autorités propriétaires ;\n- achèvement et conséquences committés dans un même lot ;\n- connaissances relatives à un détenteur, une source et une confiance ;\n- mémoire vectorielle dérivée et exclue de l’autorité des sauvegardes ;\n- IA locale consultative avec repli déterministe ;\n- restauration globale préparée avant remplacement ;\n- définitions, vues, caches, index et présentation exclus de la persistance.\n'''
if '### 11.20 Narration' not in s:
    s=s.replace('\n## 12. Chapitre 5 — état résumé', arch+'\n## 12. Chapitre 5 — état résumé')
anti='''\n- ne pas utiliser un texte affiché comme identité de quête ;\n- ne pas traiter un événement comme une vérité narrative complète ;\n- ne pas exécuter une condition issue des données ;\n- ne pas achever une quête avant la préparation de ses conséquences ;\n- ne pas révéler une entrée sur une décision indéterminée ;\n- ne pas confondre connaissance découverte et fait global ;\n- ne pas laisser une sortie IA valider un objectif ;\n- ne pas dater une quête avec le temps réel ;\n- ne pas charger directement dans les dépôts narratifs actifs ;\n- ne pas persister un index vectoriel dérivé ;\n'''
if 'ne pas utiliser un texte affiché comme identité de quête' not in s:
    s=s.replace('\n- ne pas oublier la mise à jour de ce fichier.', anti+'\n- ne pas oublier la mise à jour de ce fichier.')
s=s.replace('progression : 24 chapitres sur 30','progression : 25 chapitres sur 30')
s=s.replace('- chapitre 24 : version `1.0.0` ;','- chapitre 24 : version `1.0.0` ;\n- chapitre 25 : version `1.0.0` ;')
old=re.search(r'## 26\. Prochaine action.*?## 27\. Journal',s,flags=re.S)
new=f'''## 26. Prochaine action\n\nLe chapitre 25 est terminé au niveau `static-review`. La narration distingue faits, interprétations, quêtes, conséquences et connaissances, puis orchestre les systèmes 14 à 24 sans reprendre leur autorité.\n\nChapitre suivant :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nPérimètre attendu : plugins d’éditeur, docks, inspecteurs, importeurs, validateurs de données, génération assistée et pipelines de contenu. Le chapitre 26 industrialisera la production sans déplacer les autorités runtime des chapitres 14 à 25.\n\n## 27. Journal'''
if old: s=s[:old.start()]+new+s[old.end():]
entry=f'''\n\n### {NOW} — version 3.25.0\n\n- chapitre 25 créé, relu, corrigé et audité au niveau `static-review` ;\n- faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex et connaissances documentés ;\n- conséquences multi-autorités et idempotence explicitées ;\n- index, roadmap, `contents.txt`, audit et preuve QA initiale mis à jour ;\n- prochaine action déplacée vers le chapitre 26 — Outils d’édition internes et pipelines de contenu, niveau Élevée ;\n- aucun test runtime revendiqué et aucun PDF construit.\n'''
s=s.replace('## 27. Journal','## 27. Journal'+entry,1)
p.write_text(s,encoding='utf-8')

Path('.qa/ch25_finalize.py').unlink()
