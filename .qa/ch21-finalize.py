from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path('.')
CHAPTER = ROOT / 'Livre-II/CHAPITRE-21-Economie.md'
AUDIT = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-21.md'
EVIDENCE = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-21.yaml'
CONTINUITY = ROOT / 'CONTINUITE-PROJET.md'
INDEX = ROOT / 'Livre-II/index.md'
ROADMAP = ROOT / 'ROADMAP.md'
CONTENTS = ROOT / 'contents.txt'

now = datetime.now(ZoneInfo('Europe/Paris')).isoformat(timespec='seconds')
date_only = now[:10]


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f'missing replacement {label}: {old[:120]!r}')
    return text.replace(old, new, 1)


def insert_before(text: str, anchor: str, addition: str, label: str) -> str:
    if anchor not in text:
        raise SystemExit(f'missing insertion {label}: {anchor[:120]!r}')
    return text.replace(anchor, addition + anchor, 1)


chapter = read(CHAPTER)

# Final static corrections.
chapter = replace_once(
    chapter,
    '│   ├── pricing_policy.gd\n│   ├── economy_service.gd',
    '│   ├── pricing_policy.gd\n│   ├── trade_offer_factory.gd\n│   ├── economy_service.gd',
    'architecture factory',
)
chapter = replace_once(
    chapter,
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(wallet_id):',
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(wallet_id):',
    'wallet catalog null',
)
chapter = replace_once(
    chapter,
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(posting_id):',
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(posting_id):',
    'posting catalog null',
)
chapter = replace_once(
    chapter,
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(transaction_id):',
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(transaction_id):',
    'ledger catalog null',
)
chapter = replace_once(
    chapter,
    'func validate(currency_catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(value_id):',
    'func validate(currency_catalog: CurrencyCatalog) -> Error:\n\tif currency_catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(value_id):',
    'value catalog null',
)
chapter = replace_once(
    chapter,
    '\tvar currency := currency_catalog.get_definition(currency_id)\n\tif currency == null or currency.validate() != OK:\n\t\treturn ERR_DOES_NOT_EXIST\n\tif minimum_unit_price_minor < 1:',
    '\tvar currency := currency_catalog.get_definition(currency_id)\n\tif currency == null or currency.validate() != OK:\n\t\treturn ERR_DOES_NOT_EXIST\n\tif not currency.transferable:\n\t\treturn ERR_UNAVAILABLE\n\tif minimum_unit_price_minor < 1:',
    'value transferable currency',
)
chapter = replace_once(
    chapter,
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(quote_id) or not StableId.is_valid(offer_id):',
    'func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(quote_id) or not StableId.is_valid(offer_id):',
    'quote catalog null',
)
chapter = replace_once(
    chapter,
    '\tif tax_minor > 0 and not StableId.is_valid(tax_wallet_id):\n\t\treturn ERR_INVALID_DATA\n\treturn OK',
    '\tif tax_minor > 0 and not StableId.is_valid(tax_wallet_id):\n\t\treturn ERR_INVALID_DATA\n\tif tax_minor == 0 and not tax_wallet_id.is_empty():\n\t\treturn ERR_INVALID_DATA\n\treturn OK',
    'quote tax wallet symmetry',
)
chapter = replace_once(
    chapter,
    'func validate(currency_catalog: CurrencyCatalog) -> Error:\n\tif not StableId.is_valid(offer_id):',
    'func validate(currency_catalog: CurrencyCatalog) -> Error:\n\tif currency_catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(offer_id):',
    'offer catalog null',
)
chapter = replace_once(
    chapter,
    '\tif currency_catalog.get_definition(currency_id) == null:\n\t\treturn ERR_DOES_NOT_EXIST\n\tif unit_price_minor < 1 or remaining_quantity < 0 or minimum_quantity < 1:',
    '\tvar currency := currency_catalog.get_definition(currency_id)\n\tif currency == null or currency.validate() != OK:\n\t\treturn ERR_DOES_NOT_EXIST\n\tif not currency.transferable:\n\t\treturn ERR_UNAVAILABLE\n\tif unit_price_minor < 1 or unit_price_minor > currency.maximum_balance_minor:\n\t\treturn ERR_INVALID_DATA\n\tif remaining_quantity < 0 or minimum_quantity < 1:',
    'offer currency and price bounds',
)
chapter = replace_once(
    chapter,
    '\tif quantity < 1 or expected_total_minor < 1:\n\t\treturn ERR_INVALID_DATA',
    '\tif quantity < 1 or quantity > 1000000:\n\t\treturn ERR_INVALID_DATA\n\tif expected_total_minor < 1 or expected_total_minor > MoneyMath.MAX_SAFE_INTEGER:\n\t\treturn ERR_INVALID_DATA',
    'purchase quantity total bounds',
)
chapter = replace_once(
    chapter,
    '\tif logical_tick < 0 or command_fingerprint.is_empty():\n\t\treturn ERR_INVALID_DATA\n\treturn OK\n```\n\n<!-- qa:code-explanation -->\n\n**Explication détaillée du bloc :**\n\n- La commande contient le total affiché',
    '\tif logical_tick < 0 or command_fingerprint.is_empty():\n\t\treturn ERR_INVALID_DATA\n\tif command_fingerprint.length() > 128:\n\t\treturn ERR_INVALID_DATA\n\treturn OK\n```\n\n<!-- qa:code-explanation -->\n\n**Explication détaillée du bloc :**\n\n- La commande contient le total affiché',
    'purchase fingerprint bound',
)
chapter = replace_once(
    chapter,
    '\tif amount == null or amount.validate(currency_catalog) != OK:\n\t\treturn ERR_INVALID_DATA\n\tif amount.minor_units < 1:',
    '\tif amount == null or amount.validate(currency_catalog) != OK:\n\t\treturn ERR_INVALID_DATA\n\tvar currency := currency_catalog.get_definition(amount.currency_id)\n\tif currency == null or not currency.transferable:\n\t\treturn ERR_UNAVAILABLE\n\tif amount.minor_units < 1:',
    'reward transferable',
)
chapter = replace_once(
    chapter,
    '\tif logical_tick < 0 or command_fingerprint.is_empty():\n\t\treturn ERR_INVALID_DATA\n\treturn OK\n```\n\n<!-- qa:code-explanation -->\n\n**Explication détaillée du bloc :**\n\n- Une récompense est un transfert',
    '\tif logical_tick < 0 or command_fingerprint.is_empty():\n\t\treturn ERR_INVALID_DATA\n\tif command_fingerprint.length() > 128:\n\t\treturn ERR_INVALID_DATA\n\treturn OK\n```\n\n<!-- qa:code-explanation -->\n\n**Explication détaillée du bloc :**\n\n- Une récompense est un transfert',
    'reward fingerprint bound',
)
chapter = replace_once(
    chapter,
    '\tif total_minor < 0:\n\t\treturn ERR_INVALID_DATA',
    '\tif total_minor < 0 or total_minor > MoneyMath.MAX_SAFE_INTEGER:\n\t\treturn ERR_INVALID_DATA',
    'result total bound',
)
chapter = replace_once(
    chapter,
    'func validate(\n\tcurrency_catalog: CurrencyCatalog,\n) -> Error:\n\tif not StableId.is_valid(transaction_id) or command_fingerprint.is_empty():',
    'func validate(\n\tcurrency_catalog: CurrencyCatalog,\n) -> Error:\n\tif currency_catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(transaction_id) or command_fingerprint.is_empty():',
    'candidate catalog null',
)
chapter = replace_once(
    chapter,
    '\tfor wallet_id: StringName in wallets:\n\t\tif not posted_wallets.has(wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\tfor aggregate_id: StringName in expected_revisions:',
    '\tfor wallet_id: StringName in wallets:\n\t\tif not posted_wallets.has(wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\tif not expected_revisions.has(wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\tif offer != null and not expected_revisions.has(offer.offer_id):\n\t\treturn ERR_INVALID_DATA\n\tif result.affected_wallet_ids.size() != wallets.size():\n\t\treturn ERR_INVALID_DATA\n\tfor wallet_id: StringName in result.affected_wallet_ids:\n\t\tif not wallets.has(wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\tfor aggregate_id: StringName in expected_revisions:',
    'candidate revision/result cross refs',
)
chapter = replace_once(
    chapter,
    '\tpostings.append(_posting(command, 0, buyer_candidate, -quote.total_minor))\n\tpostings.append(_posting(command, 1, seller_candidate, quote.seller_net_minor))',
    '\tpostings.append(_posting(\n\t\tcommand, 0, buyer_candidate, quote.currency_id, -quote.total_minor\n\t))\n\tpostings.append(_posting(\n\t\tcommand, 1, seller_candidate, quote.currency_id, quote.seller_net_minor\n\t))',
    'payment posting calls',
)
chapter = replace_once(
    chapter,
    '\t\tpostings.append(_posting(command, 2, tax_candidate, quote.tax_minor))',
    '\t\tpostings.append(_posting(\n\t\t\tcommand, 2, tax_candidate, quote.currency_id, quote.tax_minor\n\t\t))',
    'tax posting call',
)
chapter = replace_once(
    chapter,
    'func _posting(\n\tcommand: PurchaseCommand,\n\tindex: int,\n\twallet: WalletState,\n\tdelta: int,\n) -> EconomyPosting:\n\tvar posting := EconomyPosting.new()\n\tposting.posting_id = EconomyId.posting(command.transaction_id, index)\n\tposting.wallet_id = wallet.wallet_id\n\tposting.currency_id = _repository.get_offer(command.offer_id).currency_id',
    'func _posting(\n\tcommand: PurchaseCommand,\n\tindex: int,\n\twallet: WalletState,\n\tcurrency_id: StringName,\n\tdelta: int,\n) -> EconomyPosting:\n\tvar posting := EconomyPosting.new()\n\tposting.posting_id = EconomyId.posting(command.transaction_id, index)\n\tposting.wallet_id = wallet.wallet_id\n\tposting.currency_id = currency_id',
    'posting explicit currency',
)
chapter = replace_once(
    chapter,
    '- `_posting()` relit la devise de l’offre et enregistre le solde candidat résultant.',
    '- `_posting()` reçoit la devise déjà validée et enregistre le solde candidat résultant sans nouvelle lecture du dépôt.',
    'posting explanation',
)
chapter = replace_once(
    chapter,
    '\tvar economy_candidate := _prepare_payment(\n\t\tcommand,\n\t\tquote,\n\t\tbuyer,\n\t\tseller,\n\t\ttax_wallet,\n\t)\n\tif economy_candidate == null:\n\t\treturn {"result": _result_insufficient(command, quote)}',
    '\tif buyer.balance_for(quote.currency_id) < quote.total_minor:\n\t\treturn {"result": _result_insufficient(command, quote)}\n\tvar economy_candidate := _prepare_payment(\n\t\tcommand,\n\t\tquote,\n\t\tbuyer,\n\t\tseller,\n\t\ttax_wallet,\n\t)\n\tif economy_candidate == null:\n\t\treturn {"result": _result_internal(command, "préparation monétaire invalide")}',
    'purchase null classification',
)
chapter = replace_once(
    chapter,
    '- L’offre est décrémentée sur une copie et désactivée à quantité nulle.',
    '- L’offre est décrémentée sur une copie et désactivée dès que le reliquat devient inférieur à la quantité minimale.',
    'offer explanation',
)
chapter = replace_once(
    chapter,
    'func commit(\n\t_economy_candidate: EconomyMutationCandidate,\n\t_inventory_candidate: EconomyInventoryTradePort.PreparedTrade,\n) -> Error:',
    'func commit(\n\t_economy_candidate: EconomyMutationCandidate,\n\t_inventory_candidate: EconomyInventoryTradePort.PreparedTrade = null,\n) -> Error:',
    'nullable inventory candidate',
)
chapter = replace_once(
    chapter,
    'var _commit_port: EconomyTransactionCommitPort\n\nfunc transfer_reward(command: RewardCommand) -> EconomyResult:\n\tif command == null or command.validate(_currency_catalog) != OK:',
    '\tvar _commit_port: EconomyTransactionCommitPort\n\nfunc transfer_reward(command: RewardCommand) -> EconomyResult:\n\tif not _is_configured():\n\t\treturn _reward_internal(command, "services obligatoires indisponibles")\n\tif command == null or command.validate(_currency_catalog) != OK:',
    'reward configuration',
)
chapter = replace_once(
    chapter,
    '\tvar candidate := _prepare_reward_candidate(command, issuer, recipient)\n\tif candidate == null:\n\t\treturn _insufficient_reward(command)\n\tvar code := _commit_port.commit(candidate, null)',
    '\tif issuer.balance_for(command.amount.currency_id) < command.amount.minor_units:\n\t\treturn _insufficient_reward(command)\n\tvar candidate := _prepare_reward_candidate(command, issuer, recipient)\n\tif candidate == null:\n\t\treturn _reward_internal(command, "préparation de récompense invalide")\n\tvar code := _commit_port.commit(candidate)',
    'reward classification and optional commit arg',
)
chapter = replace_once(
    chapter,
    '\trecord.postings = [debit, credit]\n\n\tvar result := EconomyResult.new()',
    '\trecord.postings.append(debit)\n\trecord.postings.append(credit)\n\n\tvar result := EconomyResult.new()',
    'typed reward postings',
)
chapter = replace_once(
    chapter,
    '\tresult.affected_wallet_ids = [issuer.wallet_id, recipient.wallet_id]\n\tresult.affected_wallet_ids.sort()',
    '\tresult.affected_wallet_ids.append(issuer.wallet_id)\n\tresult.affected_wallet_ids.append(recipient.wallet_id)\n\tresult.affected_wallet_ids.sort()',
    'typed result wallets',
)
chapter = replace_once(
    chapter,
    'func _invalid_reward(command: RewardCommand) -> EconomyResult:\n\treturn _reward_result(EconomyResult.Status.REJECTED_INVALID_COMMAND, command, "commande invalide")',
    'func _invalid_reward(command: RewardCommand) -> EconomyResult:\n\tvar result := EconomyResult.new()\n\tresult.status = EconomyResult.Status.REJECTED_INVALID_COMMAND\n\tresult.message = "commande invalide"\n\tif command != null and StableId.is_valid(command.transaction_id):\n\t\tresult.transaction_id = command.transaction_id\n\treturn result',
    'valid invalid-reward result',
)
chapter = insert_before(
    chapter,
    'func transfer_reward(command: RewardCommand) -> EconomyResult:\n',
    'func _is_configured() -> bool:\n\treturn (\n\t\t_currency_catalog != null\n\t\tand _repository != null\n\t\tand _access != null\n\t\tand _commit_port != null\n\t)\n\n',
    'reward is configured helper',
)
chapter = replace_once(
    chapter,
    '\tvar wallet_revision: int = 0\n\tvar offer_id: StringName',
    '\tvar wallet_revision: int = 0\n\tvar seller_wallet_revision: int = 0\n\tvar tax_wallet_revision: int = 0\n\tvar offer_id: StringName',
    'agent wallet revisions',
)
chapter = replace_once(
    chapter,
    '\tvar entry_revision: int = 0\n\n\tfunc validate() -> Error:',
    '\tvar entry_revision: int = 0\n\tvar created_stack_id: StringName\n\n\tfunc validate() -> Error:',
    'agent created stack id',
)
chapter = replace_once(
    chapter,
    '\t\tif not StableId.is_valid(wallet_id) or wallet_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\tif not StableId.is_valid(offer_id)',
    '\t\tif not StableId.is_valid(wallet_id) or wallet_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\tif seller_wallet_revision < 0 or tax_wallet_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\tif not StableId.is_valid(offer_id)',
    'agent seller tax validation',
)
chapter = replace_once(
    chapter,
    '\t\tif source_container_revision < 0 or destination_container_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\treturn OK if entry_revision >= 0 else ERR_INVALID_DATA',
    '\t\tif source_container_revision < 0 or destination_container_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\tif entry_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\tif not created_stack_id.is_empty() and not StableId.is_valid(created_stack_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\treturn OK',
    'agent final validation',
)
chapter = replace_once(
    chapter,
    '- Les trois révisions d’inventaire protègent la source, la destination et l’entrée.',
    '- Les révisions du vendeur, de la trésorerie éventuelle, de la source, de la destination et de l’entrée complètent la révision du portefeuille acheteur.',
    'agent explanation',
)

# Final metadata.
chapter = replace_once(chapter, 'status: "draft"', 'status: "reviewed"', 'chapter status')
chapter = replace_once(chapter, 'version: "0.9.0"', 'version: "1.0.0"', 'chapter version')
chapter = re.sub(r'last-verified: ".*?"', f'last-verified: "{now}"', chapter, count=1)
chapter = replace_once(chapter, 'audit-status: "pending"', 'audit-status: "complete"', 'audit status')
chapter = re.sub(r'audit-date: ".*?"', f'audit-date: "{now}"', chapter, count=1)
chapter = replace_once(chapter, 'audit-level: "not-audited"', 'audit-level: "static-review"', 'audit level')
chapter = replace_once(
    chapter,
    '> **Audit post-création :** en attente — voir `Livre-II/QA/AUDIT-CHAPITRE-21.md`.',
    '> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-21.md`.',
    'reader audit status',
)
write(CHAPTER, chapter)

# Metrics and semantic gates.
lines = chapter.splitlines()
line_count = len(lines)
headings = [line.strip() for line in lines if re.match(r'^#{1,6}\s+', line)]
heading_count = len(headings)
normalized = [re.sub(r'^#{1,6}\s+', '', h).strip().lower() for h in headings]
duplicate_headings = sum(count - 1 for count in Counter(normalized).values() if count > 1)
fence_count = sum(1 for line in lines if line.startswith('```')) // 2
explanation_count = chapter.count('<!-- qa:code-explanation -->')
error_cases = len(re.findall(r'^### 41\.\d+\s+', chapter, flags=re.MULTILINE))
faulty_explained = chapter.count('**Pourquoi cet exemple est fautif :**')
corrected_explained = chapter.count('**Pourquoi la correction fonctionne :**')

if fence_count != explanation_count:
    raise SystemExit(f'unexplained blocks: fences={fence_count} explanations={explanation_count}')
if error_cases != 10 or faulty_explained != 10 or corrected_explained != 10:
    raise SystemExit(
        f'error format mismatch: cases={error_cases} faulty={faulty_explained} corrected={corrected_explained}'
    )
if duplicate_headings != 0:
    raise SystemExit(f'duplicate headings: {duplicate_headings}')
if 'Prochaine étape' in chapter or 'CHAPITRE-22-' in chapter:
    raise SystemExit('reader chapter contains next-step material')
if '## 45. Synthèse opérationnelle pour Project Asteria' not in chapter:
    raise SystemExit('missing Project Asteria synthesis')
if 'Validate Chapters Without PDF' in chapter:
    raise SystemExit('reader chapter contains QA workflow procedure')

# Audit report.
audit = f'''---
title: "Audit du Livre II — Chapitre 21"
id: "DOC-L2-QA-AUDIT-CH21"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH21"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "{now}"
last-verified: "{now}"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 21 — Économie

## 1. Porte de brouillon

Le chapitre a été matérialisé sur une branche dédiée et dans une pull request en brouillon. Une seconde lecture automatisée puis une troisième lecture statique ciblée ont corrigé les contrats avant la présente clôture `1.0.0`.

## 2. Résultats

- lignes finales : **{line_count}** ;
- titres Markdown : **{heading_count}** ;
- blocs de code ou de données : **{fence_count}** ;
- marqueurs d’explication : **{explanation_count}** ;
- cas d’erreurs détaillés : **{error_cases}** ;
- contre-exemples expliqués : **{faulty_explained}** ;
- corrections expliquées : **{corrected_explained}** ;
- doublons de titres : **{duplicate_headings}** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre couvre :

- devises immuables et unités mineures entières ;
- portefeuilles multi-devises, soldes non négatifs et révisions ;
- écritures signées et records équilibrés par devise ;
- valeurs économiques séparées des définitions d’objets ;
- multiplicateurs en points de base et arithmétique bornée ;
- création d’offres verrouillées et devis temporaires ;
- achats, taxes, ventes et récompenses monétaires ;
- idempotence avec empreinte canonique ;
- candidat économique et commit commun avec l’inventaire ;
- adaptateur d’agent, présentation, codec et restauration préparée.

Les frontières sont respectées :

- l’inventaire conserve identité, quantité, propriété et transfert des objets ;
- les relations, l’écologie et les systèmes futurs fournissent seulement des contextes bornés ;
- la politique et la justice futures pourront autoriser ou taxer sans écrire les soldes ;
- les domaines et factions futurs restent propriétaires de leur existence ;
- la présentation consomme uniquement des résultats committés ou rejoués.

## 4. Corrections issues des lectures statiques

Les lectures distinctes ont notamment :

1. séparé les révisions d’inventaire de la source, de la destination et de l’entrée ;
2. renommé le port de commit afin de couvrir achats et récompenses ;
3. supprimé les plages d’export irréalistes et conservé les bornes dans `validate()` ;
4. protégé les contrôles signés contre le cas limite de `abs()` ;
5. ajouté une fabrique d’offres qui verrouille un prix calculé ;
6. recoupé chaque écriture avec le solde candidat correspondant ;
7. exigé une révision attendue pour chaque portefeuille et offre mutés ;
8. distingué fonds insuffisants et panne de préparation ;
9. transmis explicitement la devise aux fabriques d’écritures ;
10. complété les helpers de résultats et de journal ;
11. matérialisé une récompense équilibrée et ses refus précis ;
12. vérifié la configuration avant toute lecture du service de récompense ;
13. rendu le candidat d’inventaire explicitement optionnel pour une récompense monétaire ;
14. ajouté les révisions vendeur et fiscales au contexte d’agent ;
15. borné quantités, totaux et empreintes de commandes ;
16. interdit les devises non transférables dans les offres et transferts ;
17. renforcé les validations nulles des catalogues ;
18. corrigé la désactivation d’une offre lorsque le reliquat devient inférieur au minimum.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier :

- les signatures, types, paramètres et valeurs de retour ;
- les sentinelles `null`, `{{}}`, `&""` et `-1` ;
- les codes `Error` et refus métier ;
- la plage entière JSON sûre ;
- les copies détachées de portefeuilles et records ;
- l’équilibre séparé de chaque devise ;
- les soldes finaux non négatifs ;
- les révisions des portefeuilles, offres et agrégats d’inventaire ;
- l’idempotence et les conflits d’empreinte ;
- l’absence de mutation active depuis l’interface, l’agent ou une sortie IA.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques

Les **{fence_count}** blocs possèdent chacun un marqueur `<!-- qa:code-explanation -->` et une explication proportionnée portant, selon le besoin, sur les entrées, types, paramètres, retours, effets, invariants, déroulement, résultat attendu et frontières.

Aucune rubrique ne justifie un extrait en répétant seulement le titre de sa section.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`.

Chacun des dix cas contient un symptôme ou risque, un exemple fautif expliqué, puis un exemple corrigé expliqué. Les cas couvrent les `float`, les mutations depuis l’interface, les soldes négatifs, les récompenses sans contrepartie, les totaux clients, les commits séquentiels, les prix dans les objets, les retries avec nouvelle identité, les conversions implicites et les prix issus d’une sortie IA.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les flux, contrats, résultats et contre-exemples utilisent `[LECTURE]`. Les autres repères restent déclarés dans l’en-tête sans être ajoutés artificiellement.

Le chapitre ne contient aucune procédure de workflow ou commande de validation documentaire destinée à l’équipe éditoriale.

## 9. Sources et exactitude technique

Les API et types moteur renvoient aux pages officielles Godot 4.7 concernant `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Variant`, les signaux et les entiers GDScript 64 bits.

Les dépendances internes renvoient aux chapitres 7, 8, 9, 14, 15, 17 et 20. La version de référence reste Godot `4.7.1-stable`.

## 10. Clôture éditoriale

La dernière section du chapitre est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les dictionnaires typés n’ont pas été vérifiés dans toutes les signatures ;
- les contrôles de dépassement n’ont pas été exécutés aux bornes ;
- l’atomicité runtime du commit économie-inventaire n’a pas été exécutée ;
- l’adaptateur d’autorisation n’a pas été matérialisé ;
- les taxes et contextes futurs n’ont pas été exécutés ;
- l’action d’agent n’a pas été matérialisée ;
- la scène pédagogique n’a pas été instanciée ;
- les budgets n’ont pas été mesurés ;
- le codec et une future migration n’ont pas été exécutés ;
- le replay interplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 21 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
'''
write(AUDIT, audit)

# Pending evidence, closed after successful workflow runs.
evidence = f'''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH21
status: pending
validation-date: {date_only}
validated-base-commit: c4e16559e24dc2b0f432f1bd24bd643f9520c162
validated-head-commit: pending
chapter:
  id: DOC-L2-CH21
  path: Livre-II/CHAPITRE-21-Economie.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: pending
  warnings: pending
  chapter-lines: {line_count}
  chapter-headings: {heading_count}
  chapter-code-and-data-blocks: {fence_count}
  code-explanation-markers: {explanation_count}
  detailed-error-cases: {error_cases}
  faulty-examples-explained: {faulty_explained}
  corrected-examples-explained: {corrected_explained}
  duplicate-headings: {duplicate_headings}
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  project-asteria-final-synthesis: true
  integer-minor-units: true
  balanced-postings-per-currency: true
  item-values-separated-from-inventory: true
  basis-point-pricing: true
  idempotent-transactions: true
  economy-inventory-commit-contract: true
  save-prepared-before-replacement: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    run-id: pending
    conclusion: pending
reservations:
  - Godot parser not executed.
  - Typed Dictionary signatures not runtime-verified.
  - Arithmetic bounds not runtime-tested.
  - Economy-inventory transaction commit not run.
  - Authorization adapter not materialized.
  - Future tax and pricing contexts not run.
  - Agent action not materialized.
  - Demo scene not instantiated.
  - Performance budgets not measured.
  - Save restoration not executed.
  - Cross-platform replay not verified.
  - PDF deferred until end of Livre II.
'''
write(EVIDENCE, evidence)

# Continuity.
continuity = read(CONTINUITY)
continuity = replace_once(continuity, 'version: "3.20.0"', 'version: "3.21.0"', 'continuity version')
continuity = re.sub(r'last-updated: ".*?"', f'last-updated: "{now}"', continuity, count=1)
continuity = replace_once(continuity, '**En cours : 19 chapitres sur 30.**', '**En cours : 21 chapitres sur 30.**', 'continuity early count')
continuity = replace_once(continuity, '20. Inventaire et réputation des objets.\n21. Économie.', '20. Inventaire et réputation des objets — terminé au niveau `static-review`.\n21. Économie — terminé au niveau `static-review`.', 'continuity chapter statuses')
continuity = replace_once(continuity, 'Chapitres 3 à 20 : **Élevée**.', 'Chapitres 3 à 21 : **Élevée**.', 'continuity reasoning range')

economy_architecture = '''
### 11.16 Économie

- `CurrencyDefinition` constitue une `Resource` de conception partagée et immuable ;
- tous les montants utilisent des unités mineures entières dans la plage JSON sûre ;
- les portefeuilles portent des soldes non négatifs, des révisions et des séquences d’écriture ;
- chaque transaction produit des écritures équilibrées séparément par devise ;
- les valeurs économiques sont séparées des `ItemDefinition` du chapitre 20 ;
- les multiplicateurs utilisent des points de base et un ordre déterministe ;
- une fabrique verrouille le prix unitaire lors de la création d’une offre ;
- les devis sont temporaires, bornés et recalculés avant le commit ;
- le total proposé par l’appelant sert uniquement à détecter un changement de prix ;
- récompenses et paiements débitent toujours un portefeuille explicite ;
- l’idempotence associe identité de transaction, empreinte canonique et résultat durable ;
- `EconomyTransactionCommitPort` coordonne candidat économique et candidat d’inventaire ;
- l’inventaire conserve identité, quantité, propriété et transfert des objets ;
- contextes sociaux, écologiques, politiques ou fiscaux restent derrière des ports ;
- devis, contextes, commandes, candidats, caches et présentation sont exclus de la persistance.

'''
continuity = insert_before(continuity, '## 12. Chapitre 5 — état résumé', economy_architecture, 'continuity economy architecture')
continuity = replace_once(continuity, '- ne pas oublier la mise à jour de ce fichier.', '''- ne pas utiliser de `float` comme montant monétaire autoritaire ;
- ne pas modifier un portefeuille depuis l’interface, un agent ou une sortie IA ;
- ne pas créer de récompense sans portefeuille émetteur explicite ;
- ne pas faire confiance à un prix ou un total fourni par l’appelant ;
- ne pas committer séparément paiement et transfert d’objet ;
- ne pas stocker un prix dans `ItemDefinition` ;
- ne pas changer l’identité d’un retry économique ;
- ne pas convertir implicitement deux devises ;
- ne pas oublier la mise à jour de ce fichier.''', 'continuity economy errors')
continuity = replace_once(continuity, '- progression : 20 chapitres sur 30 ;', '- progression : 21 chapitres sur 30 ;', 'continuity state count')
continuity = replace_once(continuity, '- chapitre 20 : version `1.0.0` ;', '- chapitre 20 : version `1.0.0` ;\n- chapitre 21 : version `1.0.0` ;', 'continuity chapter version')
next_action = f'''## 26. Prochaine action

Le chapitre 21 est terminé au niveau `static-review`. L’économie utilise des unités mineures entières, équilibre les écritures par devise, sépare valeurs et objets, protège les transactions par idempotence et prépare avec l’inventaire un commit multi-autorités.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : horloge et ticks du monde, régions écologiques, populations, ressources, apparitions, disparitions, régénération et simulation active ou hors écran, avec des indices structurés fournis à l’économie sans déplacer les prix, offres, soldes ou transactions hors du chapitre 21.

'''
continuity = re.sub(r'## 26\. Prochaine action\n.*?(?=## 27\. Journal)', next_action, continuity, count=1, flags=re.DOTALL)
journal = f'''### {now} — version 3.21.0

- chapitre 21 créé, relu, corrigé et audité au niveau `static-review` ;
- devises, unités mineures, portefeuilles, écritures, valeurs, offres, devis, achats, taxes, récompenses et idempotence documentés ;
- commit économie-inventaire et révisions multi-agrégats explicités ;
- paragraphes de gouvernance restés à 19 chapitres et 6 systèmes corrigés ;
- index, roadmap, `contents.txt`, audit et preuve QA mis à jour ;
- prochaine action déplacée vers le chapitre 22 — Monde vivant et simulation écologique, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
continuity = insert_before(continuity, '### 2026-07-20T17:50:09+02:00 — version 3.20.0', journal, 'continuity journal')
write(CONTINUITY, continuity)

# Book index.
index = read(INDEX)
index = replace_once(index, 'version: "1.13.0"', 'version: "1.14.0"', 'index version')
index = replace_once(index, '21. Économie — à rédiger', '21. [Économie](CHAPITRE-21-Economie.md) — **rédigé, repéré, expliqué bloc par bloc, écritures équilibrées et commit économie-inventaire préparé, clôturé par les décisions Project Asteria et audité au niveau static-review**', 'index chapter 21')
index = replace_once(index, '- [audit du chapitre 20](QA/AUDIT-CHAPITRE-20.md) ;', '- [audit du chapitre 20](QA/AUDIT-CHAPITRE-20.md) ;\n- [audit du chapitre 21](QA/AUDIT-CHAPITRE-21.md) ;', 'index audit 21')
index = replace_once(index, 'Les chapitres 3 à 20 utilisent **Élevée**.', 'Les chapitres 3 à 21 utilisent **Élevée**.', 'index reasoning range')
index = re.sub(
    r'Le milestone \*\*M3 — Livre II : Développement et architecture\*\* est en cours\..*$',
    'Le milestone **M3 — Livre II : Développement et architecture** est en cours. **Vingt et un chapitres sur trente** sont rédigés, repérés et audités au niveau documentaire et statique. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. La partie gameplay compte désormais **huit systèmes sur douze** : personnages, relations sociales, famille, agents autonomes, combat, compétences et pouvoirs, inventaire et réputation des objets, puis économie. Le chapitre 20 conserve l’autorité sur les objets et leurs transferts. Le chapitre 21 sépare devises, soldes, valeurs, offres et paiements, puis exige un commit commun avec l’inventaire. Les réserves runtime et le PDF restent différés conformément au protocole QA.',
    index,
    count=1,
    flags=re.DOTALL,
)
write(INDEX, index)

# Roadmap.
roadmap = read(ROADMAP)
roadmap = replace_once(roadmap, 'Douze grands systèmes de jeu — 7 chapitres rédigés, repérés et audités sur 12.', 'Douze grands systèmes de jeu — 8 chapitres rédigés, repérés et audités sur 12.', 'roadmap systems count')
roadmap = replace_once(roadmap, 'Convention des outils et contextes appliquée aux chapitres 1 à 20.', 'Convention des outils et contextes appliquée aux chapitres 1 à 21.', 'roadmap context range')
roadmap = replace_once(roadmap, '- [x] Chapitre 20 — définitions et instances d’objets, lots fongibles, conteneurs, transferts autorisés, équipement, durabilité, propriété, provenance, réputation et sauvegarde stricte — rédigé et audité au niveau `static-review`.', '- [x] Chapitre 20 — définitions et instances d’objets, lots fongibles, conteneurs, transferts autorisés, équipement, durabilité, propriété, provenance, réputation et sauvegarde stricte — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 21 — devises, unités mineures, portefeuilles, écritures équilibrées, prix, offres, achats, taxes, récompenses, idempotence et commit avec l’inventaire — rédigé et audité au niveau `static-review`.', 'roadmap chapter 21')
roadmap = re.sub(
    r'\*\*Statut M3 : en cours — 19 chapitres rédigés, repérés et audités sur 30\.\*\*.*?(?=\n\n## M4)',
    '**Statut M3 : en cours — 21 chapitres rédigés, repérés et audités sur 30.** Godot 4.7.1-stable, l’édition Standard, GDScript typé et Forward+ constituent la base actuelle du projet fil rouge `Project Asteria`. Les neuf chapitres de fondation et les quatre chapitres de plateforme IA locale sont complets. Huit des douze systèmes de gameplay sont documentés. Le chapitre 20 conserve l’autorité sur les objets, quantités, propriétés et transferts. Le chapitre 21 utilise des unités mineures entières, équilibre les écritures, protège l’idempotence et coordonne le paiement avec l’inventaire. Le workflow léger valide chaque chapitre sans PDF ; la publication complète reste différée à la fin du Livre II.',
    roadmap,
    count=1,
    flags=re.DOTALL,
)
write(ROADMAP, roadmap)

# Compilation order.
contents = read(CONTENTS)
contents = replace_once(contents, 'Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md\n', 'Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md\nLivre-II/CHAPITRE-21-Economie.md\n', 'contents chapter 21')
contents = replace_once(contents, 'Livre-II/QA/AUDIT-CHAPITRE-20.md\n', 'Livre-II/QA/AUDIT-CHAPITRE-20.md\nLivre-II/QA/AUDIT-CHAPITRE-21.md\n', 'contents audit 21')
contents = replace_once(contents, 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-20.yaml\n', 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-20.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-21.yaml\n', 'contents proof 21')
write(CONTENTS, contents)
