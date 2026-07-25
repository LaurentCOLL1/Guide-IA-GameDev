#!/usr/bin/env python3
from __future__ import annotations

import base64
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")
TODAY = NOW[:10]
BASE_COMMIT = "36cd27ea95a830192a0f66e88cf4c278c752f1dc"

CHAPTER = base64.b64decode("LS0tCnRpdGxlOiAiTGl2cmUgSVYg4oCUIENoYXBpdHJlIDEgOiDDiXF1aWxpYnJhZ2UgZXQgdMOpbMOpcsOpdHJpZSBsb2NhbGUiCmlkOiAiRE9DLUw0LUNIMDEiCnN0YXR1czogInJldmlld2VkIgp2ZXJzaW9uOiAiMS4wLjAiCmxhbmc6ICJmci1GUiIKYm9vazogIkxpdnJlIElWIgpjaGFwdGVyOiAxCmxhc3QtdmVyaWZpZWQ6ICJfX05PV19fIgphdWRpdC1zdGF0dXM6ICJjb21wbGV0ZSIKYXVkaXQtZGF0ZTogIl9fTk9XX18iCmF1ZGl0LXJlcG9ydDogIkxpdnJlLUlWL1FBL0FVRElULUNIQVBJVFJFLTAxLm1kIgphdWRpdC1sZXZlbDogInN0YXRpYy1yZXZpZXciCnJlZmVyZW5jZS1lbmdpbmU6CiAgbmFtZTogIkdvZG90IEVuZ2luZSIKICB2ZXJzaW9uOiAiNC43LjEtc3RhYmxlIgogIGVkaXRpb246ICJTdGFuZGFyZCIKICBsYW5ndWFnZTogIkdEU2NyaXB0IgpyZWZlcmVuY2UtcHJvamVjdDoKICBuYW1lOiAiUHJvamVjdCBBc3RlcmlhIgogIHJlbmRlcmVyOiAiRm9yd2FyZCsiCnVzYWdlLWNvbnRleHQtc3RhbmRhcmQ6ICJET0MtVjAtQU5OLUNPTlRFWFRFUyIKLS0tCgojIMOJcXVpbGlicmFnZSBldCB0w6lsw6ltw6l0cmllIGxvY2FsZQoKPiAqKlJlcMOocmVzIGTigJl1dGlsaXNhdGlvbiA6KiogKipbUFNdKiogUG93ZXJTaGVsbCA3LCAqKltDTURdKiogSW52aXRlIGRlIGNvbW1hbmRlcywgKipbV1NMXSoqIHRlcm1pbmFsIFdTTCwgKipbRENUXSoqIHRlcm1pbmFsIGRhbnMgdW4gY29udGVuZXVyLCAqKltEQ0tdKiogRG9ja2VyIERlc2t0b3AsICoqW1ZTQ10qKiBWaXN1YWwgU3R1ZGlvIENvZGUsICoqW1dFQl0qKiBuYXZpZ2F0ZXVyLCAqKltBUFBdKiogaW50ZXJmYWNlIGdyYXBoaXF1ZSBub21tw6llLCAqKltTT1JUSUVdKiogcsOpc3VsdGF0IMOgIGxpcmUgc2FucyBsZSBzYWlzaXIsICoqW0xFQ1RVUkVdKiogZXhlbXBsZSBvdSBzdHJ1Y3R1cmUgZGUgcsOpZsOpcmVuY2UuIFZvaXIgbGEgW2NvbnZlbnRpb24gY29tcGzDqHRlXSguLi9Wb2x1bWUtMC9hbm5leGVzL0NPTlZFTlRJT04tT1VUSUxTLUVULUNPTlRFWFRFUy5tZCkuCgo+ICoqSWRlbnRpZmlhbnQgc3RhYmxlIDoqKiBgRE9DLUw0LUNIMDFgICAKPiAqKlByaW9yaXTDqSA6KiogT2JsaWdhdG9pcmUgIAo+ICoqUGFyY291cnMgOioqIE1vZGUgU29sbyDCtyBNb2RlIFN0dWRpbyAgCj4gKipQdWJsaWMgOioqIGTDqWJ1dGFudCDDoCBhdmFuY8OpICAKPiAqKlZlcnNpb24gZGUgcsOpZsOpcmVuY2UgOioqIEdvZG90IGA0LjcuMS1zdGFibGVgLCDDqWRpdGlvbiBTdGFuZGFyZCwgR0RTY3JpcHQsIEZvcndhcmQrCgojIyAxLiBSw7RsZSBkdSBjaGFwaXRyZQoKTGVzIExpdnJlcyBJSSBldCBJSUkgb250IGNvbnN0cnVpdCBsZXMgcgjDqGdsZXMgZGUgZ2FtZXBsYXksIGxlcyBzeXN0w6htZXMgZGUgZG9ubsOpZXMsIGxlcyB0ZXN0cywgbOKAmW9ic2VydmFiaWxpdMOpIGV0IGxhIHByb2R1Y3Rpb24gZGVzIGFzc2V0cy4gQ2UgcHJlbWllciBjaGFwaXRyZSBkdSBMaXZyZSBJViBu4oCZYWpvdXRlIHBhcyB1bmUgbm91dmVsbGUgYXV0b3JpdMOpIG3DqXRpZXIuIElsIG1ldCBlbiBwbGFjZSB1bmUgbcOpdGhvZGUgcG91ciAqb2JzZXJ2ZXIqLCAqY29tcGFyZXIqIGV0ICpqdXN0aWZpZXIqIGxlcyByw6lnbGFnZXMgZHUgamV1IHNhbnMgbW9kaWZpZXIgc2lsZW5jaWV1c2VtZW50IGxlcyByw6hnbGVzIHF1aSBsZXMgcHJvZHVpc2VudC4KCkzigJHDqXF1aWxpYnJhZ2UgY29uc2lzdGUgw6AgdHJhbnNmb3JtZXIgdW5lIGludGVudGlvbiBkZSBjb25jZXB0aW9uIGVuIGh5cG90aMOoc2UgbWVzdXJhYmxlLCBwdWlzIMOgIGTDqWNpZGVyIMOgIHBhcnRpciBkZSByw6lzdWx0YXRzIHJlcHJvZHVjdGlibGVzLiBVbmUgZGlmZmljdWx0w6kgwqsgdHJvcCBmb3J0ZSDCuywgdW5lIMOpY29ub21pZSDCqyB0cm9wIGxlbnRlIMK7IG91IHVuZSBwcm9ncmVzc2lvbiDCqyB0cm9wIHJhcGlkZSDCuyBuZSBzb250IHBhcyBlbmNvcmUgZGVzIGRpYWdub3N0aWNzLiBJbCBmYXV0IHByw6ljaXNlciBsYSBwb3B1bGF0aW9uIMOpdHVkacOpZSwgbGUgc2PDqW5hcmlvLCBsZXMgdmVyc2lvbnMsIGxlcyBwYXJhbcOodHJlcywgbGEgbWVzdXJlIGV0IGxlIHNldWlsIHF1aSBkw6ljbGVuY2hlIHVuZSBkw6ljaXNpb24uCgpMYSB0w6lsw6ltw6l0cmllIGxvY2FsZSBzZXJ0IGljaSDDoCByZWN1ZWlsbGlyIGRlcyBvYnNlcnZhdGlvbnMgc3VyIHVuZSBtYWNoaW5lIGRlIGTDqXZlbG9wcGVtZW50LCBkYW5zIHVuZSBzY8OobmUgZGUgdGVzdCwgdW5lIHNpbXVsYXRpb24gZMOpdGVybWluaXN0ZSBvdSB1bmUgc2Vzc2lvbiBpbnRlcm5lIGV4cGxpY2l0ZW1lbnQgYXV0b3Jpc8OpZS4gRWxsZSBuZSBzdXBwb3NlIGF1Y3VuIHNlcnZpY2UgZGlzdGFudCwgYXVjdW4gaWRlbnRpZmlhbnQgZGUgY29tcHRlLCBhdWN1bmUgY29sbGVjdGUgY2FjaMOpZSBldCBhdWN1bmUgdHJhbnNtaXNzaW9uIGF1dG9tYXRpcXVlLgoKTGUgY2hhcGl0cmUgZG9pdCBwcm9kdWlyZSBjaW5xIGZhbWlsbGVzIGRlIGxpdnJhYmxlcyA6CgotIHVuIGNhdGFsb2d1ZSBkZSBtw6l0cmlxdWVzIHZlcnNpb25uw6kgOwotIGRlcyB0YWJsZWF1eCBk4oCZqXF1aWxpYnJhZ2UgbGlzaWJsZXMgOwotIGRlcyBzY8OpbmFyaW9zIGRlIHNpbXVsYXRpb24gcmVwcm9kdWN0aWJsZXMgOwotIGRlcyByYXBwb3J0cyBkZSBkw6ljaXNpb24gY29tcGFyYW50IHVuZSByw6lmw6lyZW5jZSBldCB1biBjYW5kaWRhdCA7Ci0gdW5lIHByb2PDqWR1cmUgZGUgbWluaW1pc2F0aW9uLCBk4oCZYW5vbnltaXNhdGlvbiBvdSBkZSBzdXBwcmVzc2lvbiBkZXMgZG9ubsOpZXMuCgojIyAyLiBSw6lzdWx0YXRzIGTigJlhcHByZW50aXNzYWdlCgrDgCBsYSBmaW4gZHUgY2hhcGl0cmUsIGxlIGxlY3RldXIgc2F1cmEgOgoKLSBkaXN0aW5ndWVyIMOpdsOpbmVtZW50IG3DqXRpZXIsIG9ic2VydmF0aW9uLCBtw6l0cmlxdWUsIGFncsOpZ2F0IGV0IGTDqWNpc2lvbiA7Ci0gZMOpZmluaXIgdW5lIG3DqXRyaXF1ZSBhdmVjIHVuZSBmaW5hbGl0w6ksIHVuZSB1bml0w6ksIGRlcyBkaW1lbnNpb25zIGF1dG9yaXPDqWVzIGV0IHVuZSBkdXLDqWUgZGUgY29uc2VydmF0aW9uIDsKLSByZXByw6lzZW50ZXIgbGVzIG1vbnRhbnRzIG1vbsOpdGFpcmVzIGVuIHVuaXTDqXMgbWluZXVyZXMgZXQgbGVzIHRhdXggZW4gcG9pbnRzIGRlIGJhc2UgOwotIGNvbnN0cnVpcmUgZGVzIHNjw6luYXJpb3MgZOKAkmVxdWlsaWJyYWdlIGF2ZWMgw6l0YXQgaW5pdGlhbCwgbGVzIGNvbW1hbmRlcywgZGVzIGdyYWluZXMgZXQgZGVzIGNyaXTDqHJlcyBk4oCZYXJyw6p0IDsKLSBjYWxjdWxlciBtb3llbm5lLCBtw6lkaWFuZSwgbWluaW11bSwgbWF4aW11bSBldCBwZXJjZW50aWxlcyBzYW5zIG1hc3F1ZXIgbGEgdGFpbGxlIGRlIGzigJHDqWNoYW50aWxsb24gOwotIGNvbXBhcmVyIHVuZSBjb25maWd1cmF0aW9uIGRlIHLDqWbDqXJlbmNlIMOgIHVuZSBjb25maWd1cmF0aW9uIGNhbmRpZGF0ZSA7Ci0gZG9jdW1lbnRlciB1bmUgZMOpY2lzaW9uLCBzZXMgbGltaXRlcyBldCBzb24gcGxhbiBkZSByZXRvdXIgYXJyacOocmUgOwotIHPDqXBhcmVyIHTDqWzDqW3DqXRyaWUgbG9jYWxlLCB0ZXN0cyBpbnRlcm5lcyBldCBkb25uw6llcyBkZSBqb3VldXJzIDsKLSByZWZ1c2VyIHRvdXRlIGNvbGxlY3RlIHF1aSBu4oCZYSBuaSBmaW5hbGl0w6kgZMOpZmluaWUsIG5pIGJhc2UsIG5pIG1pbmltaXNhdGlvbiwgbmkgcsOpdGVudGlvbi4KCiMjIDMuIE5pdmVhdSBkZSBwcmV1dmUgZXQgcsOpc2VydmVzCgpMZSBjaGFwaXRyZSBlc3QgYWNjZXB0w6kgYXUgbml2ZWF1IGBzdGF0aWMtcmV2aWV3YC4gTGVzIGNsYXNzZXMsIHNjaMOpbWFzLCBjb21tYW5kZXMgZXQgc29ydGllcyBzb250IGRlcyBtb2TDqGxlcyBww6lkYWdvZ2lxdWVzIHJlbHVzIHN0YXRpcXVlbWVudC4gSWxzIG5lIHByb3V2ZW50IHBhcyBxdWUgUHJvamVjdCBBc3RlcmlhIGEgb3DDqWN1dMOpIHVuZSBjYW1wYWduZSBk4oCZw6lxdWlsaWJyYWdlIHLDqWVsbGUuCgpBdWN1biBub21icmUgZGUgam91ZXVycywgZHVyw6llIGRlIHNlc3Npb24sIHRhdXggZGUgdmljdG9pcmUsIHByaXggbW95ZW4sIHBlcmNlbnRpbGUsIEZQUywgY2/Du3QgbWF0w6lyaWVsIG91IGdhaW4gZOKAmWVuZ2FnZW1lbnQgbuKAmWVzdCBpbnZlbnTDqS4gTGVzIHZhbGV1cnMgaWxsdXN0cmF0aXZlcyBzb250IGlkZW50aWZpw6llcyBjb21tZSB0ZWxsZXMgZXQgbmUgZGV2aWVubmVudCBqYW1haXMgZGVzIHLDqXN1bHRhdHMgZGUgcHJvZHVjdGlvbi4KCj4gKipbTEVDVFVSRV0gTml2ZWF1IGRlIHByZXV2ZSDigJQgTmUgcGFzIHNhaXNpci4qKgoKYGBgeWFtbApldmlkZW5jZV9sZXZlbDoKICBjaGFwdGVyOiBzdGF0aWNfcmV2aWV3CiAgdGVsZW1ldHJ5X3J1bnRpbWVfaW1wbGVtZW50ZWQ6IGZhbHNlCiAgc2ltdWxhdGlvbnNfZXhlY3V0ZWQ6IGZhbHNlCiAgcGxheWVyX2RhdGFfY29sbGVjdGVkOiBmYWxzZQogIHJlbW90ZV9leHBvcnRfZW5hYmxlZDogZmFsc2UKICBiYWxhbmNpbmdfZGVjaXNpb25zX2FwcGxpZWQ6IGZhbHNlCiAgcGRmX3Byb2R1Y2VkOiBmYWxzZQpgYGAKCjwhLS0gcWE6Y29kZS1leHBsYW5hdGlvbiAtLT4KCi**Explication structurée du bloc :**

- **Statut :** `static_review` signifie que les contrats sont relus sans prétendre qu’ils ont été exécutés.
- **Runtime :** les adaptateurs de collecte et les scènes de simulation ne sont pas matérialisés par ce chapitre
- **Données :** aucune donnée de joueur, identifiant de compte ou donnée personnelle n’est déclarée collectée
- **Publication :** aucun réglage n’est promu et aucun PDF intermédiaire n’est construit

## 4. Prérequis et frontières

Le lecteur doit avoir parcouru :

- le Livre II, chapitre 18 pour l’autorité du combat ;
- le Livre II, chapitre 21 pour les devises, prix, offres et transactions ;
- le Livre II, chapitre 22 pour l’horloge logique et la simulation écologique ;
- le Livre II, chapitre 27 pour les tests, graines et simulations déterministes ;
- le Livre II, chapitre 28 pour les journaux, métriques, traces et paquets de diagnostic ;
- le Livre II, chapitre 29 pour l’automatisation Python et les manifestes ;
- le Livre III, chapitre 29 pour les portes de validation et la séparation des preuves.

Ce chapitre couvre :

- le catalogue de métriques d’équilibrage ;
- les observations locales ;
- les agrégats et distributions ;
- les courbes de progression ;
- les indicateurs de combat, économie, écologie et difficulté ;
- les scénarios de simulation ;
- les comparaisons avant/après ;
- les rapports de décision ;
- la minimisation, la rétention et la purge.

Il ne couvre pas :

- la stratégie QA générale, réservée au chapitre 2 ;
- la campagne produit de tests fonctionnels, réservée au chapitre 3 ;
- la reproduction détaillée des anomalies, réservée au chapitre 4 ;
- la journalisation et les tableaux de bord d’exploitation, approfondis au chapitre 5 ;
- le profilage CPU, GPU et mémoire, traité aux chapitres 6 à 8 ;
- la redéfinition des règles de combat, d’économie, d’écologie ou de progression ;
- une consultation juridique ou une décision automatique sur la licéité d’un traitement.

> **Frontière essentielle :** l’équilibrage propose et compare des paramètres. Chaque système propriétaire reste seul autorisé à valider et appliquer ses règles. La télémétrie décrit un résultat déjà produit ; elle ne crée ni dégâts, ni monnaie, ni ressource, ni progression.

## 5. Vocabulaire opérationnel

Une **métrique** est une définition stable indiquant ce qui est mesuré, pourquoi, dans quelle unité et avec quelles dimensions.

Une **observation** est un fait élémentaire enregistré à un instant logique ou pendant une exécution : dégâts infligés, durée d’un affrontement, montant d’une transaction, palier atteint ou résultat d’un scénario.

Un **agrégat** résume plusieurs observations : compteur, somme, minimum, maximum, moyenne entière, médiane ou percentile.

Une **dimension** est une catégorie utilisée pour découper une métrique, par exemple `difficulty_profile` ou `weapon_family`. Une dimension ne doit pas contenir un identifiant individuel à forte cardinalité.

Un **scénario** décrit un état initial, une configuration, une suite de commandes, des graines et un critère d’arrêt.

Une **configuration de référence** est la version actuellement acceptée. Une **configuration candidate** est une modification soumise à comparaison.

Un **rapport de décision** relie une hypothèse, des données sourcées, une comparaison, une décision humaine et un plan de retour arrière.

La **pseudonymisation** remplace un identifiant direct par une référence contrôlée mais réversible ou recoupable. Elle ne transforme pas automatiquement les données en données anonymes.

L’**anonymisation** vise à rendre l’identification raisonnablement impossible. Elle doit être évaluée selon le contexte réel ; retirer un nom ne suffit pas.

## 6. Chaîne d’autorité

> **[LECTURE] Flux d’une décision d’équilibrage — Ne pas saisir.**

```text
système propriétaire
    ↓ événement ou résultat déjà committé
TelemetryPort
    ↓ observation minimale autorisée
agrégateur local
    ↓ agrégats + manifeste de scénario
analyse reproductible
    ↓ comparaison référence / candidat
rapport de décision
    ↓ validation humaine
propriétaire du système
    ↓ nouvelle révision de configuration ou refus
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** l’observation provient d’un résultat déjà décidé par combat, économie, écologie ou progression
- **Agrégation :** le collecteur calcule des résumés sans réinterpréter l’autorité métier
- **Décision :** une personne examine les résultats, les limites et les effets secondaires
- **Application :** seul le propriétaire du système publie une nouvelle révision de configuration
- **Retour arrière :** le rapport conserve la référence précédente afin de pouvoir restaurer le réglage

## 7. Architecture retenue

La fonctionnalité d’équilibrage reste séparée de l’observabilité générale. Elle consomme le `TelemetryPort` du Livre II, chapitre 28, ajoute un catalogue propre aux questions d’équilibrage et produit des artefacts dérivés. Elle ne duplique pas les événements de domaine.

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/balancing/
├── domain/
│   ├── balance_metric_id.gd
│   ├── balance_metric_definition.gd
│   ├── balance_observation.gd
│   ├── balance_sample.gd
│   ├── balance_summary.gd
│   ├── balance_scenario_definition.gd
│   ├── balance_comparison.gd
│   └── balance_decision_report.gd
├── application/
│   ├── balance_metric_catalog.gd
│   ├── balance_telemetry_port.gd
│   ├── balance_aggregator.gd
│   ├── balance_simulation_port.gd
│   ├── balance_analysis_service.gd
│   └── balance_report_service.gd
├── infrastructure/
│   ├── jsonl_balance_sink.gd
│   ├── csv_balance_exporter.gd
│   └── local_balance_retention.gd
└── presentation/
    └── balance_debug_panel.gd

res://data/balancing/
├── metrics/
├── scenarios/
└── profiles/

automation/balancing/
├── compare_runs.py
├── export_tables.py
└── schemas/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaine :** les définitions, observations et rapports restent indépendants des scènes
- **Application :** les services agrègent et comparent sans modifier les systèmes propriétaires
- **Infrastructure :** seuls les adaptateurs écrivent des fichiers locaux ou exportent des tableaux
- **Présentation :** le panneau de débogage lit des agrégats et ne devient pas une source de vérité
- **Automatisation :** Python consolide des artefacts reproductibles sans décider du réglage à publier

## 8. Séparer les trois contextes de données

### 8.1 Simulation locale

La simulation locale utilise des personnages, équipements, régions et transactions synthétiques. Elle peut employer des identifiants fictifs et des graines fixes. Elle est le contexte par défaut pour apprendre et comparer des réglages.

### 8.2 Test interne

Un test interne peut enregistrer les actions de membres de l’équipe ou de testeurs recrutés. Les finalités, personnes autorisées, durées de conservation et modalités d’effacement doivent être documentées avant la collecte.

### 8.3 Données de joueurs

Les données de joueurs peuvent constituer des données personnelles même sans nom visible, notamment lorsque des identifiants, adresses réseau, appareils, horaires ou comportements permettent de distinguer une personne. Ce chapitre n’active aucune collecte de ce type.

La conception doit toujours commencer par la question suivante : **la même décision peut-elle être prise avec une simulation ou un agrégat local ne contenant aucune donnée personnelle ?** Si oui, cette voie est privilégiée.

## 9. Registre des finalités et minimisation

> **[VSC] Visual Studio Code — Créer `res://data/balancing/metrics/metric-purpose-register.v1.yaml`.**

```yaml
schema_version: 1
purposes:
  combat_tuning:
    question: "Le profil standard termine-t-il le duel cible dans la fenêtre prévue ?"
    allowed_contexts: [synthetic_simulation, internal_test]
    personal_data_required: false
    retention_class: short_lived
  economy_tuning:
    question: "Combien de cycles synthétiques sont nécessaires pour acheter un équipement cible ?"
    allowed_contexts: [synthetic_simulation]
    personal_data_required: false
    retention_class: derived_only
defaults:
  remote_transfer: denied
  raw_player_identifiers: denied
  free_text: denied
  collect_when_purpose_missing: denied
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Finalité :** chaque entrée formule une question décisionnelle plutôt qu’une collecte générale
- **Contextes :** `allowed_contexts` ferme les environnements dans lesquels la métrique peut être utilisée
- **Données personnelles :** `false` impose l’arrêt si l’implémentation exige finalement une donnée personnelle
- **Valeurs par défaut :** tout transfert distant, texte libre ou collecte sans finalité est refusé
- **Rétention :** la classe indique si les observations brutes doivent être supprimées après agrégation

## 10. Concevoir un catalogue de métriques

Une métrique doit être définie avant sa première observation. Son identifiant ne dépend ni d’un libellé traduit ni d’un nom de fichier. Le catalogue précise :

- la question à laquelle elle répond ;
- le type d’agrégation ;
- l’unité ;
- les bornes acceptées ;
- les dimensions autorisées ;
- les contextes d’usage ;
- la rétention ;
- le propriétaire fonctionnel ;
- la version du schéma.

Une métrique « au cas où » est interdite. Une métrique qui n’entraîne aucune décision identifiable doit être supprimée ou reformulée.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_metric_definition.gd`.**

```gdscript
class_name BalanceMetricDefinition
extends Resource

enum Kind {
    COUNTER,
    GAUGE,
    DISTRIBUTION,
}

@export var metric_id: StringName
@export var kind: Kind
@export var unit: StringName
@export var purpose_id: StringName
@export var minimum_value: int
@export var maximum_value: int
@export var allowed_dimensions: PackedStringArray = []
@export var retention_class: StringName
@export var owner_system: StringName

func validate() -> PackedStringArray:
    var findings := PackedStringArray()
    if not StableId.is_valid(metric_id):
        findings.append("METRIC_ID_INVALID")
    if unit.is_empty():
        findings.append("METRIC_UNIT_MISSING")
    if not StableId.is_valid(purpose_id):
        findings.append("METRIC_PURPOSE_INVALID")
    if minimum_value > maximum_value:
        findings.append("METRIC_RANGE_INVALID")
    if retention_class.is_empty():
        findings.append("METRIC_RETENTION_MISSING")
    if owner_system.is_empty():
        findings.append("METRIC_OWNER_MISSING")
    return findings
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `Resource` permet de versionner les définitions de métriques comme données de conception
- **Types :** `Kind` ferme les trois familles admises ; les bornes utilisent des `int`
- **Paramètres :** les dimensions et la rétention sont déclarées dans la définition, pas au moment de l’envoi
- **Retour :** `validate()` renvoie tous les constats sous forme de codes stables
- **Effet de bord :** la validation ne modifie ni la définition ni un système de gameplay

## 11. Identifiants stables

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_metric_id.gd`.**

```gdscript
class_name BalanceMetricId
extends RefCounted

const PREFIX := "balance.metric."

static func from_slug(slug: String) -> StringName:
    var normalized := slug.strip_edges().to_lower().replace(" ", "_")
    if normalized.is_empty():
        return &""
    if not normalized.is_valid_identifier():
        return &""
    return StringName(PREFIX + normalized)

static func is_valid(value: StringName) -> bool:
    return String(value).begins_with(PREFIX) and StableId.is_valid(value)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `slug` est un nom technique stable, non un texte affiché au joueur
- **Normalisation :** les espaces deviennent des traits de soulignement et la casse est abaissée
- **Refus contrôlé :** une chaîne vide ou non compatible avec un identifiant retourne `StringName()` vide
- **Retour :** un identifiant valide porte toujours le préfixe `balance.metric.`
- **Limite :** une modification de sens crée un nouvel identifiant ou une nouvelle version, pas un renommage silencieux

## 12. Compteurs, jauges et distributions

Un **compteur** ne fait qu’augmenter dans une exécution donnée : combats terminés, achats acceptés, objectifs atteints.

Une **jauge** représente une valeur observée à un instant : stock courant, niveau du joueur, nombre de quêtes actives.

Une **distribution** conserve plusieurs valeurs afin d’étudier leur dispersion : dégâts par coup, durée d’un affrontement, revenu par cycle.

Le choix du type influence l’agrégation. Transformer une distribution en simple moyenne perd les extrêmes, la médiane et les percentiles.

## 13. Unités et représentations numériques

Les métriques doivent annoncer leur unité. `120` n’a aucun sens sans préciser s’il s’agit de points de vie, millisecondes, ticks, unités mineures ou points de base.

Les règles suivantes sont retenues :

- les montants monétaires utilisent des unités mineures entières ;
- les taux utilisent des points de base lorsque quatre décimales suffisent ;
- les durées de simulation utilisent des ticks logiques ;
- les durées réelles utilisent une unité explicitement nommée, par exemple la milliseconde ;
- les ratios calculés pour affichage peuvent utiliser un `float`, mais les données sources restent entières et le rapport indique l’arrondi.

Dans les exemples économiques français, `12,34 €` est stocké comme `1234` centimes. Le symbole affiché ne devient jamais une donnée de calcul.

> **[LECTURE] Représentation des unités — Ne pas saisir.**

```yaml
units:
  currency_cent:
    storage_type: int
    example_minor_units: 1234
    rendered_fr_FR: "12,34 €"
  basis_point:
    storage_type: int
    example_value: 750
    rendered_percent: "7,50 %"
  logical_tick:
    storage_type: int
    wall_clock_equivalence: none
  millisecond:
    storage_type: int
    clock_source: monotonic_when_measuring_duration
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Monnaie :** `1234` centimes représente `12,34 €` sans utiliser de flottant pour l’autorité économique
- **Taux :** `750` points de base représente `7,50 %`
- **Temps logique :** un tick ordonne la simulation sans promettre une durée réelle
- **Durée réelle :** une mesure en millisecondes doit préciser sa source d’horloge
- **Affichage :** la localisation intervient après les calculs et ne modifie pas les valeurs stockées

## 14. Représenter une observation

Une observation contient uniquement les champs nécessaires à la finalité. Elle ne copie pas un objet complet, une sauvegarde, un texte libre ou un identifiant de compte.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_observation.gd`.**

```gdscript
class_name BalanceObservation
extends RefCounted

var metric_id: StringName
var value: int
var logical_tick: int
var scenario_id: StringName
var run_id: StringName
var dimensions: Dictionary

func _init(
    p_metric_id: StringName,
    p_value: int,
    p_logical_tick: int,
    p_scenario_id: StringName,
    p_run_id: StringName,
    p_dimensions: Dictionary,
) -> void:
    metric_id = p_metric_id
    value = p_value
    logical_tick = p_logical_tick
    scenario_id = p_scenario_id
    run_id = p_run_id
    dimensions = p_dimensions.duplicate(true)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** le constructeur exige métrique, valeur, tick, scénario, run et dimensions
- **Types :** la valeur et le tick sont des entiers ; les identités sont des `StringName` stables
- **Copie :** `duplicate(true)` détache le dictionnaire fourni par l’appelant
- **Effet de bord :** l’objet ne publie rien et ne touche à aucun état gameplay
- **Limite :** aucune propriété de joueur, adresse réseau ou chaîne libre n’est prévue dans le contrat

## 15. Valider une observation avant collecte

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_metric_catalog.gd`.**

```gdscript
class_name BalanceMetricCatalog
extends RefCounted

var _definitions: Dictionary = {}

func register(definition: BalanceMetricDefinition) -> Error:
    var findings := definition.validate()
    if not findings.is_empty():
        return ERR_INVALID_DATA
    if _definitions.has(definition.metric_id):
        return ERR_ALREADY_EXISTS
    _definitions[definition.metric_id] = definition
    return OK

func validate_observation(observation: BalanceObservation) -> Error:
    if not _definitions.has(observation.metric_id):
        return ERR_DOES_NOT_EXIST
    var definition: BalanceMetricDefinition = _definitions[observation.metric_id]
    if observation.value < definition.minimum_value:
        return ERR_PARAMETER_RANGE_ERROR
    if observation.value > definition.maximum_value:
        return ERR_PARAMETER_RANGE_ERROR
    for key in observation.dimensions:
        if String(key) not in definition.allowed_dimensions:
            return ERR_UNAUTHORIZED
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Enregistrement :** une définition invalide ou dupliquée est refusée avant toute observation
- **Codes de retour :** `Error` distingue données invalides, doublon, absence, plage et dimension interdite
- **Bornes :** la valeur est comparée aux limites de la définition
- **Dimensions :** chaque clé doit appartenir à la liste autorisée
- **Effet de bord :** seule une définition validée est ajoutée au catalogue

## 16. Définir le port de télémétrie d’équilibrage

Le port constitue la frontière entre les systèmes producteurs et le collecteur local. Un système transmet une observation minimale après son commit. Il ne connaît ni le fichier JSONL, ni le CSV, ni le rapport final.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_telemetry_port.gd`.**

```gdscript
class_name BalanceTelemetryPort
extends RefCounted

func record(_observation: BalanceObservation) -> Error:
    return ERR_UNAVAILABLE

func flush() -> Error:
    return OK

func close() -> Error:
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** `record()` reçoit une observation déjà construite et retourne un code `Error`
- **Repli :** l’implémentation de base refuse la collecte avec `ERR_UNAVAILABLE`
- **Cycle de vie :** `flush()` et `close()` permettent aux adaptateurs de persister ou libérer leurs ressources
- **Autorité :** le port n’autorise aucune mutation gameplay
- **Appelant :** un échec de télémétrie ne doit pas annuler rétroactivement une transaction métier déjà committée

## 17. Agréger en mémoire

L’agrégateur en mémoire sert aux simulations et tests. Il conserve des sommes, comptes, minima, maxima et valeurs triables pour les distributions. Une campagne réelle doit borner le nombre de valeurs brutes ou employer des buckets.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_aggregator.gd`.**

```gdscript
class_name BalanceAggregator
extends RefCounted

var _values_by_metric: Dictionary = {}

func record(observation: BalanceObservation) -> void:
    var values: Array[int] = []
    if _values_by_metric.has(observation.metric_id):
        values = _values_by_metric[observation.metric_id]
    values.append(observation.value)
    _values_by_metric[observation.metric_id] = values

func values(metric_id: StringName) -> Array[int]:
    var stored: Array[int] = _values_by_metric.get(metric_id, [])
    return stored.duplicate()

func clear() -> void:
    _values_by_metric.clear()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Stockage :** chaque métrique pointe vers un tableau d’entiers
- **Ajout :** `append()` conserve l’ordre d’observation de la campagne
- **Retour :** `values()` fournit une copie afin que l’appelant ne modifie pas l’agrégat interne
- **Effet de bord :** `clear()` supprime uniquement les observations en mémoire
- **Limite :** cette implémentation pédagogique n’est pas adaptée à un volume non borné

## 18. Utiliser des buckets pour les distributions bornées

Un histogramme répartit les valeurs dans des intervalles définis avant la campagne. Les bornes doivent correspondre à une question de conception. Changer les buckets entre deux runs empêche une comparaison directe sans retraitement des valeurs brutes.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_histogram.gd`.**

```gdscript
class_name BalanceHistogram
extends RefCounted

var _upper_bounds: Array[int]
var _counts: Array[int]

func _init(upper_bounds: Array[int]) -> void:
    _upper_bounds = upper_bounds.duplicate()
    _upper_bounds.sort()
    _counts.resize(_upper_bounds.size() + 1)
    _counts.fill(0)

func observe(value: int) -> void:
    for index in range(_upper_bounds.size()):
        if value <= _upper_bounds[index]:
            _counts[index] += 1
            return
    _counts[_counts.size() - 1] += 1

func counts() -> Array[int]:
    return _counts.duplicate()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** `upper_bounds` contient les limites supérieures inclusives des buckets
- **Tri :** les bornes sont triées une seule fois dans le constructeur
- **Déroulement :** la première borne qui contient la valeur reçoit le compteur
- **Dernier bucket :** l’élément supplémentaire reçoit toutes les valeurs au-dessus de la dernière borne
- **Retour :** `counts()` protège l’état interne par une copie

## 19. Écrire un journal JSONL local

JSONL stocke un objet JSON par ligne. Ce format facilite l’écriture progressive et la lecture ligne par ligne. Le fichier reste un artefact de campagne locale, non une sauvegarde de partie.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/infrastructure/jsonl_balance_sink.gd`.**

```gdscript
class_name JsonlBalanceSink
extends BalanceTelemetryPort

var _file: FileAccess
var _catalog: BalanceMetricCatalog

func _init(path: String, catalog: BalanceMetricCatalog) -> void:
    _catalog = catalog
    _file = FileAccess.open(path, FileAccess.WRITE)

func record(observation: BalanceObservation) -> Error:
    if _file == null:
        return FileAccess.get_open_error()
    var validation := _catalog.validate_observation(observation)
    if validation != OK:
        return validation
    var payload := {
        "metric_id": String(observation.metric_id),
        "value": observation.value,
        "logical_tick": observation.logical_tick,
        "scenario_id": String(observation.scenario_id),
        "run_id": String(observation.run_id),
        "dimensions": observation.dimensions,
    }
    _file.store_line(JSON.stringify(payload))
    return OK

func flush() -> Error:
    if _file == null:
        return ERR_UNCONFIGURED
    _file.flush()
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ouverture :** `FileAccess.WRITE` crée ou tronque le fichier de run explicitement choisi
- **Validation :** l’observation passe par le catalogue avant sérialisation
- **Payload :** seuls les champs contractuels sont écrits
- **Retour :** les erreurs d’ouverture ou de validation sont propagées comme codes `Error`
- **Persistance :** `flush()` force l’écriture seulement lorsque la campagne en a besoin

## 20. Créer un manifeste de run

Les observations ne sont interprétables qu’avec le scénario, les versions et les paramètres qui les ont produites. Le manifeste est écrit avant l’exécution, puis complété par un statut final et les empreintes des artefacts.

> **[VSC] Visual Studio Code — Créer `res://data/balancing/scenarios/run-manifest.schema.yaml`.**

```yaml
schema_version: 1
run:
  run_id: AST-BALANCE-RUN-0001
  scenario_id: AST-BALANCE-SCENARIO-DUEL-001
  source_commit: "<git-commit>"
  engine_version: "4.7.1-stable"
  configuration_id: AST-BALANCE-PROFILE-REFERENCE-001
  seed_set: [1103, 1109, 1117, 1123]
  repetition_count: 100
  started_at_utc: null
  completed_at_utc: null
  execution_status: NOT_EXECUTED
artifacts:
  observations_jsonl:
    path: "work/runs/AST-BALANCE-RUN-0001/observations.jsonl"
    sha256: null
  summary_json:
    path: "work/runs/AST-BALANCE-RUN-0001/summary.json"
    sha256: null
privacy:
  context: synthetic_simulation
  personal_data: false
  remote_transfer: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le run, le scénario et la configuration possèdent des identifiants distincts
- **Versions :** le commit source et la version moteur rendent la campagne situable
- **Graines :** le jeu de seeds et le nombre de répétitions sont déclarés avant l’exécution
- **Artefacts :** chaque sortie recevra une empreinte après production
- **Confidentialité :** le contexte synthétique et l’absence de transfert sont explicites

## 21. Définir des profils de collecte

Le profil `synthetic_simulation` est le profil par défaut. Il ne nécessite pas de consentement de joueur puisqu’il n’utilise pas de personne réelle. Un profil `internal_test` exige une information préalable, une finalité, une durée et un mécanisme d’effacement. Aucun profil `player_production` n’est fourni dans ce chapitre.

> **[LECTURE] Profils de collecte — Ne pas saisir.**

```yaml
collection_profiles:
  synthetic_simulation:
    enabled: true
    personal_data: false
    identifiers: synthetic_only
    retention_days: 30
    raw_observations_after_summary: delete
  internal_test:
    enabled: false
    information_notice_required: true
    legal_review_required: true
    free_text: denied
    direct_identifiers: denied
    retention_days: project_policy
  player_production:
    enabled: false
    reason: not_defined_in_this_chapter
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Simulation :** seuls des identifiants synthétiques sont autorisés
- **Test interne :** le profil reste désactivé tant que les obligations et responsables ne sont pas définis
- **Texte libre :** son refus évite de recueillir des informations imprévues
- **Production :** aucune collecte joueur n’est activée par défaut
- **Rétention :** les observations brutes peuvent être supprimées après calcul des résumés

## 22. Minimiser, pseudonymiser et anonymiser

Retirer un nom ne suffit pas lorsque le reste des champs permet de reconnaître une personne. Les identifiants persistants, horaires précis, adresses réseau, caractéristiques d’appareil et séquences détaillées peuvent être recoupés.

Pour un besoin d’équilibrage, l’ordre de préférence est :

1. simulation entièrement synthétique ;
2. agrégats calculés localement sans observation individuelle conservée ;
3. échantillon interne volontaire, borné et documenté ;
4. données pseudonymisées lorsque l’objectif ne peut pas être atteint autrement ;
5. collecte de production uniquement après analyse, information, base juridique, sécurité, rétention et exercice des droits.

Ce chapitre ne déclare pas qu’un jeu de données est anonyme. Cette conclusion exige une analyse spécifique des risques de réidentification.

## 23. Définir une politique de rétention et de purge

> **[VSC] Visual Studio Code — Créer `res://data/balancing/profiles/retention-policy.v1.yaml`.**

```yaml
schema_version: 1
classes:
  derived_only:
    raw_observations: delete_after_summary
    summaries_days: 365
  short_lived:
    raw_observations_days: 30
    summaries_days: 365
  investigation_hold:
    raw_observations_days: project_policy
    approval_required: true
    reason_required: true
purge:
  allowed_roots:
    - "user://balancing/runs/"
  dry_run_required: true
  log_deletion_manifest: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classes :** chaque métrique référence une durée au lieu d’inventer sa propre politique
- **Observations brutes :** `derived_only` impose leur suppression après le résumé
- **Exception :** une conservation d’enquête exige une approbation et une raison
- **Racines :** la purge est limitée au répertoire des runs d’équilibrage
- **Preuve :** un manifeste de suppression conserve les identités et empreintes, pas les données supprimées

## 24. Construire une courbe de progression

Une courbe de progression définit le coût d’un palier ou le cumul nécessaire pour l’atteindre. Elle doit être monotone lorsque chaque niveau exige au moins autant d’expérience totale que le précédent.

L’exemple suivant emploie une progression quadratique entière :

`coût_niveau = base + croissance_linéaire × (niveau - 1) + croissance_quadratique × (niveau - 1)²`

Les coefficients sont des données de configuration. La formule ne prouve pas que la courbe est agréable ; elle rend les hypothèses calculables.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/progression_curve.gd`.**

```gdscript
class_name ProgressionCurve
extends Resource

@export_range(1, 1_000_000, 1) var base_cost: int = 100
@export_range(0, 1_000_000, 1) var linear_growth: int = 25
@export_range(0, 1_000_000, 1) var quadratic_growth: int = 5

func cost_for_level(level: int) -> int:
    if level < 1:
        return -1
    var offset := level - 1
    return (
        base_cost
        + linear_growth * offset
        + quadratic_growth * offset * offset
    )

func cumulative_cost(target_level: int) -> int:
    if target_level < 1:
        return -1
    var total := 0
    for level in range(1, target_level + 1):
        total += cost_for_level(level)
    return total
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** les trois coefficients sont des entiers exportés et bornés
- **Retour :** un niveau inférieur à `1` retourne `-1` comme sentinelle contrôlée
- **Opérateurs :** `*` applique les croissances et `+` compose le coût
- **Cumul :** `range(1, target_level + 1)` inclut le niveau cible
- **Limite :** les bornes finales doivent aussi protéger le cumul contre un dépassement adapté au projet réel

## 25. Produire un tableau de progression

> **[PS] PowerShell 7 — Exporter un tableau illustratif depuis la racine de l’outil d’automatisation — Ne pas saisir avant matérialisation.**

```powershell
.\.venv\Scripts\python.exe -m asteria_tools.balance export-progression `
  --profile "res://data/balancing/profiles/reference.tres" `
  --first-level 1 `
  --last-level 20 `
  --output "work/tables/progression-reference.csv"

if ($LASTEXITCODE -ne 0) {
  throw "L’export du tableau de progression a échoué."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interpréteur :** la commande utilise l’environnement virtuel qualifié du Livre II, chapitre 29
- **Paramètres :** le profil, le premier niveau, le dernier niveau et le chemin de sortie sont explicites
- **Code de retour :** une valeur non nulle bloque l’utilisation du tableau
- **Effet de bord :** seul le CSV dérivé sous `work/` est créé
- **Réserve :** la commande illustre le contrat et n’est pas déclarée exécutée

## 26. Mesurer le combat sans le redéfinir

Le combat conserve les commandes, cibles, chances de toucher, dégâts, états et commits. L’équilibrage peut observer :

- durée logique d’un affrontement ;
- nombre de tours ;
- dégâts infligés et reçus ;
- proportion de commandes refusées ;
- fréquence d’utilisation des familles d’actions ;
- santé restante à la fin ;
- nombre de situations où aucun choix utile n’est disponible.

Les dimensions autorisées doivent rester peu nombreuses : profil de difficulté, famille d’arme, archétype synthétique, type de scénario. Un identifiant de personnage individuel n’est pas nécessaire pour une comparaison agrégée.

> **[VSC] Visual Studio Code — Créer `res://data/balancing/metrics/combat-metrics.v1.yaml`.**

```yaml
metrics:
  - id: balance.metric.combat_turns_to_resolution
    kind: distribution
    unit: logical_turn
    range: [1, 10000]
    dimensions: [difficulty_profile, encounter_family]
    purpose: balance.purpose.combat_tuning
  - id: balance.metric.combat_damage_per_action
    kind: distribution
    unit: hit_point
    range: [0, 1000000]
    dimensions: [difficulty_profile, action_family]
    purpose: balance.purpose.combat_tuning
  - id: balance.metric.combat_command_refused
    kind: counter
    unit: occurrence
    range: [0, 1000000]
    dimensions: [reason_code, scenario_family]
    purpose: balance.purpose.combat_diagnostics
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durée :** la résolution est mesurée en tours logiques, pas en temps d’animation
- **Dégâts :** l’observation décrit le résultat autoritaire du combat
- **Refus :** `reason_code` doit provenir d’une nomenclature stable
- **Dimensions :** les familles restent de faible cardinalité
- **Bornes :** une valeur hors plage est refusée au lieu d’être tronquée silencieusement

## 27. Mesurer l’économie sans recalculer les prix

L’économie conserve devises, offres, devis, transactions et écritures. L’équilibrage peut mesurer :

- revenu synthétique par cycle ;
- dépense par catégorie ;
- nombre de cycles nécessaires pour atteindre un achat cible ;
- fréquence des refus pour fonds insuffisants ;
- dispersion des prix finaux déjà calculés par l’économie ;
- concentration d’une ressource monétaire entre profils synthétiques.

Les montants sont exprimés dans la devise du scénario et en unités mineures. Un exemple de `1299` centimes représente `12,99 €`.

> **[LECTURE] Tableau économique illustratif — Ne pas saisir.**

```csv
scenario_id,configuration_id,target_price_cent,median_cycles,p90_cycles,insufficient_funds_count
AST-ECO-SCENARIO-001,AST-BALANCE-PROFILE-REFERENCE-001,1299,8,13,21
AST-ECO-SCENARIO-001,AST-BALANCE-PROFILE-CANDIDATE-002,1299,6,10,12
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Monnaie :** `target_price_cent=1299` représente `12,99 €` dans les deux lignes
- **Comparaison :** la référence et le candidat utilisent le même scénario et le même prix cible
- **Médiane :** `median_cycles` résume le centre de la distribution
- **Percentile :** `p90_cycles` expose une queue plus lente que la médiane
- **Illustration :** ces valeurs ne proviennent pas d’une campagne exécutée et ne constituent pas une décision

## 28. Mesurer l’écologie sans produire un prix

L’écologie conserve populations, ressources, capacités et transitions. L’équilibrage peut observer :

- temps logique avant épuisement d’une réserve synthétique ;
- temps de récupération ;
- amplitude des populations ;
- fréquence des passages sous un seuil de viabilité ;
- proportion de runs qui atteignent un état stable ;
- nombre de rattrapages agrégés nécessaires.

L’équilibrage ne transforme pas une rareté en prix. Il transmet uniquement des résultats aux rapports ; l’économie reste propriétaire des prix.

## 29. Mesurer la difficulté

La difficulté n’est pas une seule valeur. Une campagne doit expliciter les dimensions retenues :

- probabilité de réussite dans un scénario contrôlé ;
- nombre de tentatives ;
- durée logique ;
- ressources consommées ;
- marge restante ;
- nombre de décisions non triviales ;
- fréquence de blocage sans option utile.

Un taux de réussite isolé ne permet pas de savoir si le scénario est intéressant, frustrant, exploitable ou trivial.

## 30. Définir un scénario d’équilibrage

> **[VSC] Visual Studio Code — Créer `res://data/balancing/scenarios/duel-standard.v1.yaml`.**

```yaml
schema_version: 1
scenario_id: AST-BALANCE-SCENARIO-DUEL-001
purpose_id: balance.purpose.combat_tuning
initial_state:
  attacker_profile: AST-CHAR-PROFILE-SCOUT-001
  defender_profile: AST-CHAR-PROFILE-GUARD-001
  distance_units: 4
configuration:
  combat_rules: AST-COMBAT-RULES-REFERENCE-001
commands:
  source: deterministic_policy
seeds:
  values: [1103, 1109, 1117, 1123]
execution:
  repetitions_per_seed: 25
  maximum_logical_turns: 200
stop_conditions:
  - one_side_defeated
  - maximum_turns_reached
required_metrics:
  - balance.metric.combat_turns_to_resolution
  - balance.metric.combat_damage_per_action
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le scénario et les profils ont des identifiants stables
- **État initial :** la distance et les deux profils sont fixés avant le run
- **Commandes :** une politique déterministe remplace une interaction humaine variable
- **Graines :** quatre seeds et vingt-cinq répétitions par seed définissent cent exécutions prévues
- **Arrêt :** la victoire ou la borne de tours évite une simulation infinie

## 31. Valider un scénario

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_scenario_definition.gd`.**

```gdscript
class_name BalanceScenarioDefinition
extends Resource

@export var scenario_id: StringName
@export var purpose_id: StringName
@export var seed_values: PackedInt64Array
@export_range(1, 100000, 1) var repetitions_per_seed: int = 1
@export_range(1, 1000000, 1) var maximum_logical_steps: int = 1

func planned_run_count() -> int:
    return seed_values.size() * repetitions_per_seed

func validate() -> PackedStringArray:
    var findings := PackedStringArray()
    if not StableId.is_valid(scenario_id):
        findings.append("SCENARIO_ID_INVALID")
    if not StableId.is_valid(purpose_id):
        findings.append("SCENARIO_PURPOSE_INVALID")
    if seed_values.is_empty():
        findings.append("SCENARIO_SEEDS_EMPTY")
    if planned_run_count() <= 0:
        findings.append("SCENARIO_RUN_COUNT_INVALID")
    return findings
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** la liste de graines, les répétitions et la borne d’étapes sont des données explicites
- **Calcul :** `planned_run_count()` multiplie le nombre de seeds par les répétitions
- **Retour :** `validate()` accumule les constats sans modifier le scénario
- **Bornes :** les annotations d’export limitent les valeurs saisies dans l’éditeur
- **Limite :** la validation complète doit aussi vérifier les profils et métriques référencés

## 32. Utiliser un générateur pseudo-aléatoire contrôlé

Chaque run possède sa propre instance de `RandomNumberGenerator`. La graine est fixée avant toute lecture de l’état interne. Une graine identique aide à reproduire une séquence dans un environnement qualifié, mais l’algorithme interne du moteur reste un détail d’implémentation : la version du moteur doit donc être manifestée.

Les graines voisines ne sont pas supposées produire des flux statistiquement indépendants. Une dérivation par hash ou un jeu de seeds revu est préférable.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_rng_factory.gd`.**

```gdscript
class_name BalanceRngFactory
extends RefCounted

static func create(scenario_id: StringName, seed_value: int) -> RandomNumberGenerator:
    if not StableId.is_valid(scenario_id):
        return null
    var rng := RandomNumberGenerator.new()
    rng.seed = hash("%s:%d" % [String(scenario_id), seed_value])
    return rng
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** l’identité du scénario et la seed externe participent à la dérivation
- **Hash :** la chaîne composée évite d’utiliser directement des graines voisines
- **Ordre :** `seed` est défini avant le premier appel aléatoire
- **Retour :** une identité invalide renvoie `null` comme refus contrôlé
- **Réserve :** le manifeste conserve aussi la version de Godot car l’algorithme interne n’est pas un contrat stable

## 33. Exécuter une simulation bornée

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_simulation_runner.gd`.**

```gdscript
class_name BalanceSimulationRunner
extends RefCounted

func run(
    scenario: BalanceScenarioDefinition,
    seed_value: int,
    repetition: int,
    simulation: BalanceSimulationPort,
    telemetry: BalanceTelemetryPort,
) -> Error:
    if repetition < 1:
        return ERR_INVALID_PARAMETER
    var findings := scenario.validate()
    if not findings.is_empty():
        return ERR_INVALID_DATA
    var rng := BalanceRngFactory.create(scenario.scenario_id, seed_value)
    if rng == null:
        return ERR_CANT_CREATE
    var start_result := simulation.start(scenario, rng, repetition)
    if start_result != OK:
        return start_result
    for logical_step in range(scenario.maximum_logical_steps):
        var step_result := simulation.step(logical_step)
        if step_result not in [OK, ERR_BUSY]:
            return step_result
        for observation in simulation.drain_observations():
            var record_result := telemetry.record(observation)
            if record_result != OK:
                return record_result
        if simulation.is_terminal():
            return OK
    return ERR_TIMEOUT
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** le scénario, la seed, la répétition, le port de simulation et la télémétrie sont injectés
- **Préconditions :** une répétition commence à `1` et le scénario doit être valide
- **Boucle :** `range(maximum_logical_steps)` borne le nombre d’étapes
- **Codes de retour :** `ERR_BUSY` représente une étape sans terminaison ; tout autre échec est propagé
- **Postcondition :** un run non terminal à la borne retourne `ERR_TIMEOUT`

## 34. Calculer des statistiques descriptives

Une moyenne peut être fortement influencée par quelques valeurs extrêmes. La médiane coupe l’échantillon en deux. Un percentile `p90` indique la valeur sous laquelle se trouvent environ 90 % des observations triées selon la convention choisie.

Le rapport doit toujours afficher le nombre d’observations. Un percentile calculé sur cinq valeurs peut être mathématiquement défini mais reste faible pour une décision générale.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_summary.gd`.**

```gdscript
class_name BalanceSummary
extends RefCounted

static func median(values: Array[int]) -> float:
    if values.is_empty():
        return NAN
    var ordered := values.duplicate()
    ordered.sort()
    var middle := int(ordered.size() / 2)
    if ordered.size() % 2 == 1:
        return float(ordered[middle])
    return (float(ordered[middle - 1]) + float(ordered[middle])) / 2.0

static func nearest_rank_percentile(values: Array[int], percentile: int) -> int:
    if values.is_empty() or percentile < 1 or percentile > 100:
        return -1
    var ordered := values.duplicate()
    ordered.sort()
    var rank := int(ceil(percentile * ordered.size() / 100.0))
    return ordered[max(rank - 1, 0)]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Médiane :** le tableau est copié puis trié afin de protéger l’entrée
- **Parité :** une taille impaire renvoie l’élément central ; une taille paire moyenne les deux centres
- **Percentile :** la méthode du rang le plus proche est nommée afin d’éviter une convention implicite
- **Retours :** un tableau vide produit `NAN` pour la médiane et `-1` pour le percentile entier
- **Limite :** le rapport doit afficher la méthode, la taille d’échantillon et l’arrondi

## 35. Conserver la taille d’échantillon et les limites

Les statistiques ne remplacent pas le protocole. Un rapport doit préciser :

- le nombre de scénarios ;
- le nombre de seeds ;
- le nombre de répétitions ;
- le nombre de runs réussis, bloqués, interrompus et expirés ;
- le nombre d’observations par métrique ;
- les valeurs manquantes ;
- les versions des configurations ;
- les exclusions ;
- les limites de généralisation.

Un résultat produit uniquement par une politique déterministe synthétique ne prouve pas la réaction d’un joueur humain.

## 36. Comparer référence et candidat

La comparaison porte sur le même scénario, les mêmes seeds, la même version de moteur et les mêmes règles hors paramètre étudié. Si plusieurs paramètres changent en même temps, le rapport ne peut pas attribuer l’effet à un seul d’entre eux.

> **[LECTURE] Contrat de comparaison — Ne pas saisir.**

```yaml
comparison:
  comparison_id: AST-BALANCE-COMP-DUEL-001
  scenario_id: AST-BALANCE-SCENARIO-DUEL-001
  baseline:
    configuration_id: AST-BALANCE-PROFILE-REFERENCE-001
    run_id: AST-BALANCE-RUN-0001
  candidate:
    configuration_id: AST-BALANCE-PROFILE-CANDIDATE-002
    run_id: AST-BALANCE-RUN-0002
  invariants:
    same_source_commit: true
    same_engine_version: true
    same_seed_set: true
    same_repetition_count: true
    changed_parameters:
      - combat.guard_reduction_basis_points
  decision_status: PENDING
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paire :** la référence et le candidat possèdent des runs distincts
- **Invariants :** versions, seeds et répétitions doivent correspondre
- **Variable étudiée :** la liste ferme les paramètres volontairement modifiés
- **Statut :** `PENDING` empêche de confondre comparaison calculée et décision prise
- **Traçabilité :** l’identifiant de comparaison relie tableaux, graphiques et rapport

## 37. Calculer des deltas sans masquer les unités

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_comparison.gd`.**

```gdscript
class_name BalanceComparison
extends RefCounted

static func absolute_delta(baseline: int, candidate: int) -> int:
    return candidate - baseline

static func relative_delta_basis_points(baseline: int, candidate: int) -> int:
    if baseline == 0:
        return 0
    return int(round((candidate - baseline) * 10000.0 / baseline))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Delta absolu :** la soustraction conserve l’unité de la métrique
- **Delta relatif :** `10000` convertit le ratio en points de base
- **Précondition :** une référence nulle empêche un pourcentage relatif significatif
- **Arrondi :** `round()` est appliqué avant la conversion en entier
- **Limite :** le rapport doit distinguer le cas `baseline == 0` d’un changement réellement nul

## 38. Rédiger un rapport de décision

Un rapport de décision n’est pas un tableau de chiffres isolé. Il doit contenir :

- la question ;
- l’hypothèse ;
- les configurations comparées ;
- les métriques principales et de garde ;
- les résultats ;
- la qualité et les limites de la preuve ;
- la décision ;
- l’auteur ;
- la date ;
- la portée ;
- le plan de déploiement ;
- le plan de retour arrière.

> **[VSC] Visual Studio Code — Créer `res://data/balancing/reports/decision-report.schema.yaml`.**

```yaml
schema_version: 1
decision:
  decision_id: AST-BALANCE-DECISION-DUEL-001
  question: "Le candidat réduit-il la durée sans augmenter les blocages ?"
  hypothesis: "Une garde légèrement réduite rapproche la médiane de la cible."
  comparison_id: AST-BALANCE-COMP-DUEL-001
  primary_metrics:
    - balance.metric.combat_turns_to_resolution
  guardrail_metrics:
    - balance.metric.combat_command_refused
  evidence_level: NOT_EXECUTED
  result_summary: null
  limitations:
    - synthetic_policy_only
    - no_human_playtest
  decision_status: PENDING
  approved_by: null
  rollback_configuration_id: AST-BALANCE-PROFILE-REFERENCE-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Question :** le rapport formule un effet attendu et un risque à surveiller
- **Métriques :** les indicateurs principaux sont séparés des garde-fous
- **Preuve :** `NOT_EXECUTED` interdit toute conclusion sur l’exemple
- **Décision :** l’approbateur reste vide tant qu’une personne n’a pas statué
- **Retour arrière :** la configuration de référence est nommée avant toute promotion

## 39. Exporter des tableaux dérivés

Les CSV, graphiques et tableaux sont dérivés des observations et manifestes. Ils doivent conserver l’identité du run, la métrique, l’unité et le nombre d’observations. Un tableau copié dans un document sans ces références devient difficile à auditer.

Les graphiques peuvent faciliter la lecture, mais ils doivent annoncer leurs axes, unités, échelles, exclusions et méthode d’agrégation. Une échelle tronquée peut exagérer une différence.

## 40. Mode Solo

En mode Solo :

- commencer par un seul scénario et trois à cinq métriques ;
- utiliser uniquement des données synthétiques ;
- conserver une configuration de référence immuable ;
- exécuter des lots courts avec seeds fixes ;
- lire médiane, extrêmes et quelques runs individuels ;
- modifier un paramètre principal à la fois ;
- écrire la décision avant de changer la configuration publiée ;
- supprimer les observations brutes après le résumé lorsque leur conservation n’est plus utile.

Le développeur Solo peut être à la fois auteur et approbateur, mais il doit séparer les moments : préparer l’hypothèse, exécuter, fermer la session, puis relire le rapport avant de décider.

## 41. Mode Studio

En mode Studio :

- le propriétaire du système formule la question et les paramètres autorisés ;
- la QA ou l’analyste prépare le scénario et vérifie les invariants ;
- l’opérateur exécute la campagne sans modifier la configuration ;
- une personne distincte relit les résultats lorsque l’organisation le permet ;
- les profils de collecte, accès, rétention et purge sont approuvés ;
- les exceptions possèdent un auteur, une durée et une justification ;
- les rapports et artefacts sont archivés selon leur classification ;
- aucune équipe produit ne reçoit des données individuelles non nécessaires.

## 42. Frontières avec les chapitres suivants

Le chapitre 2 définira la stratégie QA générale, les niveaux de test, les responsabilités et les portes qualité. Le présent chapitre lui fournit des métriques et rapports, mais ne fixe pas toute la politique QA.

Le chapitre 3 intégrera les tests fonctionnels et de régression à une campagne produit. Il pourra réutiliser les scénarios et seeds sans confondre une décision d’équilibrage avec un test de conformité.

Le chapitre 4 organisera la reproduction d’anomalies. Un run d’équilibrage peut fournir un cas reproductible, mais il ne remplace pas un rapport de bug.

Le chapitre 5 approfondira journaux, métriques, traces, rotation et tableaux de bord locaux pour l’exploitation. Le présent chapitre reste centré sur les décisions d’équilibrage.

## 43. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les cas suivants appliquent la règle sémantique complète : symptôme, exemple fautif, cause, correction et différence expliquée.

### 43.1 Collecter sans question décisionnelle

**Symptôme ou risque :** Le projet accumule des centaines de champs mais personne ne sait quel réglage ils doivent éclairer.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
telemetry:
  collect_everything: true
  fields: "*"
  retention: forever
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La collecte n’a ni finalité, ni liste fermée, ni rétention. Elle augmente les risques sans garantir une décision utile.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
telemetry:
  purpose_id: balance.purpose.combat_tuning
  metrics:
    - balance.metric.combat_turns_to_resolution
  retention_class: derived_only
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction relie une métrique précise à une finalité et impose une rétention. La différence est que chaque donnée possède désormais une utilité et une fin de vie vérifiables.

### 43.2 Utiliser une moyenne sans distribution

**Symptôme ou risque :** Quelques runs très longs sont masqués par une moyenne apparemment acceptable.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
var average := total_turns / run_count
print("Durée moyenne :", average)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le calcul ne montre ni médiane, ni minimum, ni maximum, ni taille de la queue, et peut utiliser une division entière implicite.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var summary := {
    "count": turns.size(),
    "minimum": turns.min(),
    "median": BalanceSummary.median(turns),
    "p90": BalanceSummary.nearest_rank_percentile(turns, 90),
    "maximum": turns.max(),
}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve plusieurs statistiques et le nombre d’observations. La différence est que les valeurs extrêmes et la queue de distribution deviennent visibles au lieu d’être absorbées par une seule moyenne.

### 43.3 Mélanger monnaie et flottants

**Symptôme ou risque :** Deux calculs supposés équivalents produisent des centimes divergents après plusieurs opérations.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
var target_price := 12.99
var discounted := target_price * 0.9
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les flottants binaires ne représentent pas exactement tous les décimaux monétaires et l’arrondi n’est pas contractuel.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var target_price_cent := 1299
var discount_basis_points := 1000
var discounted_cent := int((
    target_price_cent * (10000 - discount_basis_points) + 5000
) / 10000)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction stocke `12,99 €` comme `1299` centimes et le taux en points de base, avec un arrondi entier explicite. La différence est que l’unité et la règle d’arrondi sont déterministes.

### 43.4 Changer plusieurs paramètres à la fois

**Symptôme ou risque :** Le candidat paraît meilleur mais il est impossible d’identifier la cause du changement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
candidate:
  guard_reduction: 0.25
  enemy_health: 850
  reward_cent: 1800
  spawn_rate: 1.4
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Combat, économie et écologie changent simultanément ; aucune attribution causale simple n’est possible.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
candidate:
  changed_parameters:
    combat.guard_reduction_basis_points:
      baseline: 3000
      candidate: 2500
  all_other_parameters: identical_to_baseline
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction isole un paramètre et verrouille les autres. La différence est que le delta observé peut être discuté par rapport à une modification documentée.

### 43.5 Utiliser une graine dépendante de l’heure

**Symptôme ou risque :** Un échec rare ne peut pas être rejoué après la campagne.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
var rng := RandomNumberGenerator.new()
rng.randomize()
run_simulation(rng)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `randomize()` choisit une graine dépendante du temps et le run ne conserve pas l’entrée nécessaire à la reproduction.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var rng := BalanceRngFactory.create(
    scenario.scenario_id,
    manifest.seed_values[seed_index],
)
run_simulation(rng)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise une seed manifestée et dérivée avec l’identité du scénario. La différence est qu’un autre opérateur peut reconstruire le même run dans l’environnement qualifié.

### 43.6 Enregistrer un identifiant individuel comme dimension

**Symptôme ou risque :** Le nombre de séries explose et les observations peuvent distinguer des personnes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
metric: balance.metric.session_duration
dimensions:
  player_account_id: "user-8491"
  device_fingerprint: "..."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les dimensions ont une cardinalité non bornée et contiennent des identifiants qui ne sont pas nécessaires à une décision d’équilibrage agrégée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
metric: balance.metric.session_duration
dimensions:
  test_profile: "internal_beginner"
  difficulty_profile: "standard"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise des catégories fermées et documentées. La différence est que l’analyse reste agrégée et ne dépend plus d’un suivi individuel.

### 43.7 Conserver les observations brutes indéfiniment

**Symptôme ou risque :** Des fichiers anciens restent accessibles alors que seuls les résumés sont utilisés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
retention:
  raw_jsonl: forever
  summaries: forever
  purge: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La conservation n’est liée ni à une finalité ni à une durée, et aucun effacement n’est vérifiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
retention:
  class: derived_only
  raw_jsonl: delete_after_summary
  summaries_days: 365
  deletion_manifest: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction supprime les données brutes après dérivation et borne les résumés. La différence est que chaque catégorie possède une fin de vie et une preuve de purge.

### 43.8 Promouvoir automatiquement le meilleur score

**Symptôme ou risque :** Une configuration maximise la métrique principale tout en dégradant fortement un garde-fou.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
winner = max(candidates, key=lambda row: row["win_rate"])
publish(winner["configuration_id"])
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le script réduit la décision à un seul score, ignore les limites et publie sans autorité humaine ni retour arrière.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
comparison = build_comparison(candidates)
write_decision_report(
    comparison=comparison,
    status="PENDING",
    guardrails=["command_refused", "resource_consumption"],
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction produit un rapport en attente avec des garde-fous. La différence est que le calcul prépare la décision sans se substituer à l’approbation ni à la promotion contrôlée.

### 43.9 Comparer des runs non équivalents

**Symptôme ou risque :** Le candidat semble plus rapide alors qu’il a utilisé moins de répétitions et une autre version moteur.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
baseline:
  engine: "4.7.1-stable"
  repetitions: 100
candidate:
  engine: "4.8-dev"
  repetitions: 20
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Deux variables majeures diffèrent en plus du réglage étudié ; la comparaison ne respecte pas ses invariants.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
invariants:
  engine_version: "4.7.1-stable"
  source_commit: "<same-commit>"
  seed_set_sha256: "<same-sha256>"
  repetitions: 100
changed_parameters:
  - combat.guard_reduction_basis_points
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction verrouille l’environnement, les seeds et le nombre de répétitions. La différence est que le candidat ne varie que sur le paramètre annoncé.

### 43.10 Confondre corrélation et causalité

**Symptôme ou risque :** Une métrique augmente en même temps qu’un réglage et le rapport affirme que le réglage en est la cause.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```text
Après l’augmentation des récompenses, la durée de session a augmenté.
Conclusion : les récompenses causent l’augmentation.
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La simultanéité ne contrôle ni les autres changements, ni la sélection des sessions, ni les facteurs externes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```text
Observation : les deux valeurs ont évolué pendant la même période.
Décision : aucune causalité revendiquée.
Action : préparer une comparaison contrôlée avec scénario, référence,
candidat, métriques de garde et facteurs constants.
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction limite l’énoncé à l’observation puis demande une comparaison contrôlée. La différence est que le rapport sépare un signal corrélé d’une conclusion causale.

## 44. Checklist de production et d’acceptation

- [ ] question d’équilibrage formulée ;
- [ ] système propriétaire et frontière identifiés ;
- [ ] métriques définies avant la collecte ;
- [ ] unités, bornes et dimensions documentées ;
- [ ] finalité et contexte de données enregistrés ;
- [ ] données personnelles évitées lorsque la simulation suffit ;
- [ ] scénario, état initial, seeds et critères d’arrêt versionnés ;
- [ ] configuration de référence immuable ;
- [ ] configuration candidate et paramètres modifiés listés ;
- [ ] nombre de répétitions et statuts de runs consignés ;
- [ ] moyenne, médiane, percentiles et taille d’échantillon interprétés avec prudence ;
- [ ] garde-fous examinés avec la métrique principale ;
- [ ] limites et exclusions écrites ;
- [ ] rapport de décision signé ou explicitement en attente ;
- [ ] configuration de retour arrière nommée ;
- [ ] rétention et purge appliquées ;
- [ ] aucune collecte distante ou joueur activée implicitement ;
- [ ] aucune exécution runtime revendiquée sans artefact ;
- [ ] validation légère sans PDF réussie.

## 45. Références techniques officielles

Les références externes documentent les API et les principes de protection des données. Elles ne remplacent ni les contrats du dépôt, ni une analyse juridique propre au produit, ni une campagne exécutée.

- [Godot 4.7 — `RandomNumberGenerator`](https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html)
- [Godot 4.7 — Génération de nombres aléatoires](https://docs.godotengine.org/en/4.7/tutorials/math/random_number_generation.html)
- [Godot 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Godot 4.7 — `FileAccess`](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html)
- [CNIL — Minimisation](https://www.cnil.fr/fr/definition/minimisation)
- [CNIL — Minimiser les données collectées](https://www.cnil.fr/fr/minimiser-les-donnees-collectees)
- [CNIL — Chapitre II du RGPD : principes](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2)
- [Livre II — Chapitre 18 : Combat](../Livre-II/CHAPITRE-18-Combat.md)
- [Livre II — Chapitre 21 : Économie](../Livre-II/CHAPITRE-21-Economie.md)
- [Livre II — Chapitre 22 : Monde vivant et simulation écologique](../Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)
- [Livre II — Chapitre 27 : Tests unitaires, tests d’intégration et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Livre II — Chapitre 28 : Journalisation, diagnostic et reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md)
- [Livre II — Chapitre 29 : Automatisation Python et génération de données](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md)

## 46. Synthèse opérationnelle pour Project Asteria

Project Asteria retient une chaîne d’équilibrage locale et reproductible. Les systèmes de combat, d’économie, d’écologie et de progression publieront uniquement des observations minimales après leurs commits. Le catalogue fermera la finalité, l’unité, les bornes, les dimensions et la rétention de chaque métrique.

Les premières campagnes seront entièrement synthétiques. Elles utiliseront des scénarios versionnés, des graines manifestées, des configurations de référence immuables et des candidats limités à des paramètres explicitement listés. Les rapports compareront distributions, tailles d’échantillon et métriques de garde sans transformer un score en décision automatique.

Aucune donnée de joueur, transmission distante, profil de production ou collecte cachée n’est activé. Une future collecte impliquant des personnes devra faire l’objet d’une analyse distincte, d’une information appropriée, d’une base documentée, d’une minimisation, d’une rétention, d’une sécurité et de mécanismes d’exercice des droits.

Le pilote documentaire est `AST-BALANCE-SCENARIO-DUEL-001`. Il reste non matérialisé : aucune simulation, observation, agrégation, comparaison, décision, modification de configuration ou validation runtime n’est revendiquée.
").decode("utf-8").replace("__NOW__", NOW)
AUDIT = base64.b64decode("LS0tCnRpdGxlOiAiQXVkaXQgcG9zdC1jcsOpYXRpb24g4oCUIExpdnJlIElWLCBjaGFwaXRyZSAxIgppZDogIkRPQy1MNC1RQS1BVURJVC1DSDAxIgpzdGF0dXM6ICJjb21wbGV0ZSIKdmVyc2lvbjogIjEuMC4wIgpsYW5nOiAiZnItRlIiCmNoYXB0ZXItaWQ6ICJET0MtTDQtQ0gwMSIKY2hhcHRlci12ZXJzaW9uOiAiMS4wLjAiCmF1ZGl0LWRhdGU6ICJfX05PV19fIgpsYXN0LXZlcmlmaWVkOiAiX19OT1dfXyIKYXVkaXQtbGV2ZWw6ICJzdGF0aWMtcmV2aWV3Igpwcm90b2NvbDogIkxpdnJlLUlJL1FBL1BST1RPQ09MRS1BVURJVC1QT1NULUNSRUFUSU9OLm1kIgp1c2FnZS1jb250ZXh0LXN0YW5kYXJkOiAiRE9DLVYwLUFOTi1DT05URVhURVMiCi0tLQoKIyBBdWRpdCBwb3N0LWNyw6lhdGlvbiDigJQgTGl2cmUgSVYsIGNoYXBpdHJlIDEKCiMjIDEuIETDqWNpc2lvbgoKTGUgY2hhcGl0cmUgZXN0IGFjY2VwdMOpIGF1IG5pdmVhdSBgc3RhdGljLXJldmlld2AgYXZlYyByw6lzZXJ2ZXMgZGUgbWF0w6lyaWFsaXNhdGlvbiBkZSBsYSB0w6lsw6ltw6l0cmllIGxvY2FsZSwgZGVzIHNjw6luYXJpb3MsIGRlcyBzaW11bGF0aW9ucywgZGVzIGFncsOpZ2F0ZXVycywgZGVzIGV4cG9ydHMsIGRlcyByYXBwb3J0cyBkZSBkw6ljaXNpb24sIGRlcyBwb2xpdGlxdWVzIGRlIHLDqXRlbnRpb24gZXQgZGUgdG91dGUgw6l2ZW50dWVsbGUgY29sbGVjdGUgaW1wbGlxdWFudCBkZXMgcGVyc29ubmVzLgoKQXVjdW5lIHNpbXVsYXRpb24sIGNvbGxlY3RlLCBkb25uw6llIGRlIGpvdWV1ciwgZXhwb3J0IGRpc3RhbnQsIGNhbXBhZ25lIGludGVybmUsIGTDqWNpc2lvbiBk4oCZw6lxdWlsaWJyYWdlLCBtb2RpZmljYXRpb24gZGUgY29uZmlndXJhdGlvbiwgbWVzdXJlIHJ1bnRpbWUgb3UgY29uc3RydWN0aW9uIFBERiBu4oCZlc3QgcmV2ZW5kaXF1w6llLgoKIyMgMi4gUMOpcmltw6h0cmUgY29tcGFyw6kgYXUgcGxhbiBtYcOudHJlCgpMZSBjaGFwaXRyZSBjb3V2cmUgbGVzIGNpbnEgb2JqZWN0aWZzIGR1IHBsYW4gbWHDqnRyZSA6CgotIG3DqXRyaXF1ZXMgdXRpbGVzIHNhbnMgY29sbGVjdGUgZXhjZXNzaXZlIDsKLSBjb3VyYmVzIGRlIHByb2dyZXNzaW9uLCDDqWNvbm9taWUsIGNvbWJhdCBldCBkaWZmaWN1bHTDqSA7Ci0gc2ltdWxhdGlvbnMgZXQgdGFibGVhdXggZGUgY29tcGFyYWlzb24gOwotIHPDqXBhcmF0aW9uIGVudHJlIHTDqWzDqW3DqXRyaWUgbG9jYWxlLCB0ZXN0cyBpbnRlcm5lcyBldCBkb25uw6llcyBqb3VldXJzIDsKLSBjb25maWRlbnRpYWxpdMOpLCBmaW5hbGl0w6ksIG1pbmltaXNhdGlvbiwgcgjDqXRlbnRpb24gZXQgcHVyZ2UuCgpMZXMgbGl2cmFibGVzIHNvbnQgcHLDqXBhcsOpcyBzb3VzIGZvcm1lIGRlIGNvbnRyYXRzIDogY2F0YWxvZ3VlIGRlIG3DqXRyaXF1ZXMsIHRhYmxlYXV4LCBzY8OpbmFyaW9zLCBtYW5pZmVzdGVzIGRlIHJ1biwgY29tcGFyYWlzb25zLCByYXBwb3J0cyBkZSBkw6ljaXNpb24gZXQgcG9saXRpcXVlIGRlIGRvbm7DqWVzLgoKTGEgdmFsaWRhdGlvbiBwYXIgcmVwcm9kdWN0aW9uIGTigJl1bmUgZMOpY2lzaW9uIHJlc3RlIGVuIHLDqXNlcnZlIGNhciBhdWN1biBzY8OpbmFyaW8gbuKAmWVzdCBtYXTDqXJpYWxpc8OpIG5pIGV4w6ljdXTDqS4KCiMjIDMuIEZyb250acOocmVzIGNvbnRyw7Rsw6llcwoKLSBsZSBjb21iYXQgY29uc2VydmUgbOKAmWF1dG9yaXTDqSBzdXIgY29tbWFuZGVzLCBjaWJsZXMsIGTDqWfDonRzLCDDqXRhdHMgZXQgcsOpc3VsdGF0cyA7Ci0gbOKAmcOpY29ub21pZSBjb25zZXJ2ZSBkZXZpc2VzLCBwcml4LCB0cmFuc2FjdGlvbnMsIMOpY3JpdHVyZXMgZXQgdW5pdMOocyBtaW5ldXJlcyA7Ci0gbOKAmcOpY29sb2dpZSBjb25zZXJ2ZSBwb3B1bGF0aW9ucywgcmVzc291cmNlcywgdGVtcHMgbG9naXF1ZSBldCB0cmFuc2l0aW9ucyA7Ci0gbGUgTGl2cmUgSUksIGNoYXBpdHJlIDI3IGNvbnNlcnZlIGxlcyBjb250cmF0cyBkZSB0ZXN0cyBldCBzaW11bGF0aW9ucyA7Ci0gbGUgTGl2cmUgSUksIGNoYXBpdHJlIDI4IGNvbnNlcnZlIGzigJlvYnNlcnZhYmlsaXTDqSBnw6luw6lyYWxlIDsKLSBsZSBMaXZyZSBJSSwgY2hhcGl0cmUgMjkgY29uc2VydmUgbOKAmWF1dG9tYXRpc2F0aW9uIFB5dGhvbiBnw6luw6lyaXF1ZSA7Ci0gbGUgTGl2cmUgSVYsIGNoYXBpdHJlIDIgY29uc2VydmVyYSBsYSBzdHJhdMOoZ2llIGfDqW7DqXJhbGUgZGUgUUEgOwotIGxlIExpdnJlIElWLCBjaGFwaXRyZSA1IGNvbnNlcnZlcmEgbOKAmW9ic2VydmFiaWxpdMOpIGTigJlleHBsb2l0YXRpb24gOwotIGF1Y3VuZSBtw6l0cmlxdWUsIGFncsOpZ2F0aW9uIG91IGFuYWx5c2UgbmUgbW9kaWZpZSB1biDDqXRhdCBnYW1lcGxheSA7Ci0gYXVjdW5lIHNvcnRpZSBhdXRvbWF0aXF1ZSBuZSBwdWJsaWUgdW4gcsOpZ2xhZ2UuCgojIyA0LiBDb250csO0bGVzIHDDqWRhZ29naXF1ZXMKCi0gdm9jYWJ1bGFpcmUgZMOpZmluaSBhdmFudCB1c2FnZSA7Ci0gZmluYWxpdMOpcywgbcOpdHJpcXVlcywgdW5pdMOpcywgZGltZW5zaW9ucywgcgjDqXRlbnRpb24gZXQgcHJvcHJpw6l0YWlyZXMgZXhwbGlxdcOpcyA7Ci0gY29tcHRldXJzLCBqYXVnZXMsIGRpc3RyaWJ1dGlvbnMsIGhpc3RvZ3JhbW1lcywgbcOpZGlhbmUgZXQgcGVyY2VudGlsZSBkaXN0aW5ndcOpcyA7Ci0gY2VudGltZXMsIGV1cm9zLCBwb2ludHMgZGUgYmFzZSwgdGlja3MgbG9naXF1ZXMgZXQgbWlsbGlzZWNvbmRlcyBzw6lwYXLDqXMgOwotIGZvbmN0aW9ucywgcGFyYW3DqHRyZXMsIHR5cGVzLCByZXRvdXJzLCBvcMOpcmF0ZXVycyBldCBlZmZldHMgZGUgYm9yZCBleHBsaXF1w6lzIDsKLSBzY8OpbmFyaW9zLCBzZWVkcywgcsOpcMOpdGl0aW9ucywgYm9ybmVzIGV0IGNyaXTDqHJlcyBk4oCZYXJyw6p0IGRvY3VtZW50w6lzIDsKLSBjb21wYXJhaXNvbiByw6lmw6lyZW5jZS9jYW5kaWRhdCBldCBtw6l0cmlxdWVzIGRlIGdhcmRlIGV4cGxpcXXDqWVzIDsKLSBtb2RlcyBTb2xvIGV0IFN0dWRpbyBkb2N1bWVudMOpcyBlbiBNYXJrZG93biBvcmRpbmFpcmUgOwotIGRpeCBkaWFnbm9zdGljcyBzdWl2ZW50IHN5bXB0w7RtZSwgZXhlbXBsZSBmYXV0aWYsIGNhdXNlLCBjb3JyZWN0aW9uIGV0IGRpZmbDqXJlbmNlIDsKLSByw6lmw6lyZW5jZXMgdGVjaG5pcXVlcyBvZmZpY2llbGxlcyBmb3VybmllcyBzb3VzIGZvcm1lIGRlIGxpZW5zIE1hcmtkb3duIG5vbW3DqXMuCgojIyA1LiBDb250csO0bGVzIGRvY3VtZW50YWlyZXMKCi0gbGlnbmVzIDogMTcxNiA7Ci0gdGl0cmVzIDogNjAgOwotIGJsb2NzIGNvZGUgb3UgZG9ubsOpZXMgOiA0OCA7Ci0gbWFycXVldXJzIGTigJlleHBsaWNhdGlvbiA6IDQ4IDsKLSBleHBsaWNhdGlvbnMgc3RydWN0dXLDqWVzIGhvcnMgZGlhZ25vc3RpY3MgOiAyOCA7Ci0gZGlhZ25vc3RpY3MgZMOpdGFpbGzDqXMgOiAxMCA7Ci0gZXhlbXBsZXMgZmF1dGlmcyBleHBsaXF1w6lzIDogMTAgOwotIGV4ZW1wbGVzIGNvcnJpZ8OpcyBleHBsaXF1w6lzIDogMTAgOwotIHRpdHJlcyBkdXBsaXF1w6lzIDogMCA7Ci0gYmxvY3Mgc2lnbmlmaWNhdGlmcyBkdXBsaXF1w6lzIDogMCA7Ci0gcGFyYWdyYXBoZXMgbG9uZ3MgZHVwbGlxdcOpcyA6IDAgOwotIHN5bnRow6hzZSBvcMOpcmF0aW9ubmVsbGUgYFByb2plY3QgQXN0ZXJpYWAgcHLDqXNlbnRlIDsKLSByw6lmw6lyZW5jZXMgZXh0ZXJuZXMgbm9tbcOpZXMgZXQgY2xpcXVhYmxlcyA7Ci0gYWJzZW5jZSBkZSBwcm9jaGFpbmUgYWN0aW9uIGV0IGRlIHJlY29tbWFuZGF0aW9uIEdQVCBkYW5zIGxlIHRleHRlIGxlY3RldXIgOwotIFBERiBub24gcHJvZHVpdC4KCiMjIDYuIEV4YWN0aXR1ZGUgdGVjaG5pcXVlCgpMYSByZXZ1ZSBzdGF0aXF1ZSB2w6lyaWZpZSBsZXMgY29udHJhdHMgR29kb3QgYFJhbmRvbU51bWJlckdlbmVyYXRvcmAsIGBKU09OYCBldCBgRmlsZUFjY2Vzc2AsIGxlcyBjb2RlcyBgRXJyb3JgLCBsZXMgdGFibGVhdXggdHlww6lzLCBsZXMgY29waWVzIGTDqXRhY2jDqWVzLCBsZXMgYm9ybmVzIGRlIHNpbXVsYXRpb24gZXQgbGEgc8OpcGFyYXRpb24gZW50cmUgdGljayBsb2dpcXVlIGV0IGR1csOpZSByw6llbGxlLgoKTGVzIGdyYWluZXMgc29udCBtYW5pZmVzdMOpZXMgYXZlYyBsYSB2ZXJzaW9uIG1vdGV1ci4gTGUgY2hhcGl0cmUgbmUgZMOpcGVuZCBwYXMgZGUgbOKAmWFsZ29yaXRobWUgaW50ZXJuZSBkdSBnw6luw6lyYXRldXIgY29tbWUgZOKAmXVuIGNvbnRyYXQgc3RhYmxlLgoKTGVzIG1vbnRhbnRzIG1vbsOpdGFpcmVzIHJlc3RlbnQgZW4gY2VudGltZXMgZW50aWVycyBldCBsZXMgdGF1eCBlbiBwb2ludHMgZGUgYmFzZS4gTGVzIGV4ZW1wbGVzIGAxMiwzNCDigq1gIGV0IGAxMiw5OSDigq1gIHV0aWxpc2VudCByZXNwZWN0aXZlbWVudCBgMTIzNGAgZXQgYDEyOTlgIGNlbnRpbWVzLgoKTGVzIHByaW5jaXBlcyBkZSBmaW5hbGl0w6ksIG1pbmltaXNhdGlvbiwgdHJhbnNwYXJlbmNlIGV0IHLDqXRlbnRpb24gc29udCBwcsOpc2VudMOpcyBjb21tZSBleGlnZW5jZXMgZGUgY29uY2VwdGlvbiBldCBub24gY29tbWUgY29uc3VsdGF0aW9uIGp1cmlkaXF1ZS4gQXVjdW5lIGRvbm7DqWUgbuKAmWVzdCBkw6ljbGFyw6llIGFub255bWUgc2FucyBhbmFseXNlIGRlIHLDqWlkZW50aWZpY2F0aW9uLgoKIyMgNy4gw4l2b2x1dGlvbiBkZSBsYSBjaGHDrm5lIFFBIGzDqWfDqHJlCgpVbiDDqWNhcnQgcHLDqWV4aXN0YW50IGEgw6l0w6kgY29ycmlnw6kgOiBsZXMgdmFsaWRhdGV1cnMgcGVybWFuZW50cyBuZSBwYXJjb3VyYWllbnQgcXVlIGxlcyBMaXZyZXMgSSDDoCBJSUkuIExlIGxvdCDDqXRlbmQgZXhwbGljaXRlbWVudCBsZXMgY29udHLDtGxlcyBhdSBMaXZyZSBJViBkYW5zIDoKCi0gYHRvb2xzL3ZhbGlkYXRlX2NoYXB0ZXJzLnB5YCA7Ci0gYHRvb2xzL2NoZWNrX2NvZGVfZXhwbGFuYXRpb25fc3RydWN0dXJlLnB5YCA7Ci0gYHRvb2xzL2NoZWNrX2NvbnRleHRfbWFya2Vycy5weWAgOwotIGB0b29scy9hdWRpdF9jb250ZXh0ZXNfc2VtYW50aXF1ZXMucHlgLgoKQ2V0dGUgZXh0ZW5zaW9uIG5lIG1vZGlmaWUgbmkgbGUgcGxhbiBtYcOudHJlLCBuaSBs4oCZb3JkcmUgZGVzIGNoYXBpdHJlcywgbmkgY2hhw65uZSBQREYuIEVsbGUgZW1ww6pjaGUgcXXigJl1biBjaGFwaXRyZSBkdSBMaXZyZSBJViDDqWNoYXBwZSBhdXggY29udHLDtGxlcyBkb2N1bWVudGFpcmVzLgoKIyMgOC4gUsOpc2VydmVzIG91dmVydGVzCgotIGNsYXNzZXMgZXQgUmVzb3VyY2VzIG5vbiBtYXTDqXJpYWxpc8OpZXMgZGFucyBQcm9qZWN0IEFzdGVyaWEgOwotIGNhdGFsb2d1ZSBkZSBtw6l0cmlxdWVzIG5vbiBjcsOpw6kgOwotIHNjw6luYXJpb3MgZXQgcHJvZmlscyBub24gY3LDqcOpcyA7Ci0gdMOpbMOpbcOpdHJpZSBKU09OTCBub24gZXjDqWN1dMOpZSA7Ci0gc2ltdWxhdGlvbnMgZMOpdGVybWluaXN0ZXMgbm9uIGV4w6ljdXTDqWVzIDsKLSBhZ3LDqWdhdHMsIHRhYmxlYXV4IGV0IENTViBub24gcHJvZHVpdHMgOwotIGF1Y3VuZSBjb21wYXJhaXNvbiByw6lmw6lyZW5jZS9jYW5kaWRhdCByw6lhbGlzw6llIDsKLSBhdWN1biByYXBwb3J0IGRlIGTDqWNpc2lvbiBhcHByb3V2w6kgOwotIGF1Y3VuZSBwcm9jw6lkdXJlIGRlIHB1cmdlIGV4w6ljdXTDqWUgOwotIGF1Y3VuZSBjb2xsZWN0ZSBpbnRlcm5lIG91IGpvdWV1ciBhdXRvcmlzw6llIDsKLSBhdWN1bmUgYW5hbHlzZSBqdXJpZGlxdWUgcHJvcHJlIGF1IHByb2R1aXQgcsOpYWxpc8OpZSA7Ci0gYXVjdW4gdGVzdCBydW50aW1lIGV4w6ljdXTDqSA7Ci0gYXVjdW4gUERGIGNvbnN0cnVpdC4KCiMjIDkuIENvbmNsdXNpb24KCkxlIGNoYXBpdHJlIHNhdGlzZmFpdCBsZSBww6lyaW3DqHRyZSBkdSBwbGFuIG1hw650cmUgYXUgbml2ZWF1IGRvY3VtZW50YWlyZSBldCBwZXV0IGVudHJlciBkYW5zIGxhIHZhbGlkYXRpb24gbMOpZ8OocmUgc2FucyBQREYuIExhIHByZXV2ZSBmaW5hbGUgcmVzdGUgYHBlbmRpbmdgIGp1c3F14oCZ w6AgbGEgcsOpdXNzaXRlIGRlcyB3b3JrZmxvd3MgcGVybWFuZW50cyBzdXIgbGEgYnJhbmNoZSBkZSBwdWxsIHJlcXVlc3QuCg==").decode("utf-8").replace("__NOW__", NOW)

def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu une occurrence, trouvé {count}")
    return text.replace(old, new, 1)

def update(path: str, transform) -> None:
    target = ROOT / path
    original = target.read_text(encoding="utf-8")
    changed = transform(original)
    if changed == original:
        raise RuntimeError(f"Aucune modification produite pour {path}")
    target.write_text(changed, encoding="utf-8")

write("Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md", CHAPTER)
write("Livre-IV/QA/AUDIT-CHAPITRE-01.md", AUDIT)

chapter_lines = CHAPTER.splitlines()
heading_count = sum(1 for line in chapter_lines if re.match(r"^#{1,6}\s+", line))
fence_count = sum(1 for line in chapter_lines if re.match(r"^```|^~~~", line.strip())) // 2
marker_count = CHAPTER.count("<!-- qa:code-explanation -->")
structured_count = CHAPTER.count("**Explication structurée du bloc :**")
faulty_count = CHAPTER.count("**Pourquoi cet exemple est fautif :**")
corrected_count = CHAPTER.count("**Pourquoi la correction fonctionne :**")
chapter_sha = sha256(CHAPTER.encode("utf-8")).hexdigest()
audit_sha = sha256(AUDIT.encode("utf-8")).hexdigest()

proof = f"""schema-version: 1
evidence-id: DOC-L4-QA-EVIDENCE-CH01
validation-authority: permanent-workflows
status: pending
validation-date: '{TODAY}'
validated-base-commit: {BASE_COMMIT}
validated-head-commit: null
chapter:
  id: DOC-L4-CH01
  path: Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: null
  warnings: null
  chapter-lines: {len(chapter_lines)}
  chapter-headings: {heading_count}
  chapter-code-and-data-blocks: {fence_count}
  significant-code-and-data-blocks: {fence_count}
  code-explanation-markers: {marker_count}
  structured-non-error-code-explanations: {structured_count}
  detailed-error-cases: {faulty_count}
  faulty-examples-explained: {faulty_count}
  corrected-examples-explained: {corrected_count}
  duplicate-headings: 0
  duplicate-blocks: 0
  duplicate-paragraphs: 0
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  solo-studio-documented: true
  master-plan-scope-covered: true
  project-asteria-operational-summary-present: true
  clickable-technical-references: true
  metric-catalog-documented: true
  progression-economy-combat-difficulty-documented: true
  deterministic-scenarios-documented: true
  privacy-minimization-retention-documented: true
  decision-reports-documented: true
  no-gameplay-authority: true
  runtime-values-not-invented: true
  semantic-error-correction-sequence: true
  error-explanations-directly-after-markers: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: {chapter_sha}
  audit-sha256: {audit_sha}
ci:
  validate-chapters-without-pdf:
    workflow-name: Validate Chapters Without PDF
    run-id: null
    conclusion: pending
  validate-usage-contexts:
    workflow-name: Validate Chapters Without PDF
    run-id: null
    conclusion: pending
  artifact:
    id: null
    name: chapter-validation-without-pdf
    digest: null
reservations:
  - Balancing classes and Resources are not materialized.
  - Metric catalog and collection profiles are not created.
  - Deterministic scenarios are not executed.
  - JSONL telemetry and CSV exports are not produced.
  - Baseline/candidate comparisons are not performed.
  - No balancing decision is approved or applied.
  - No internal tester or player data collection is authorized.
  - No product-specific legal analysis is performed.
  - Runtime tests are not executed.
  - No PDF is built.
evidence-closure:
  commit: null
  conclusion: pending
"""
write("Livre-IV/QA/VALIDATION-FINALE-CHAPITRE-01.yaml", proof)

index = f"""---
title: "Livre IV — Finalisation, optimisation, publication et maintenance"
id: "LIV-IV-INDEX"
status: "in-progress"
version: "1.1.0"
lang: "fr-FR"
last-verified: "{NOW}"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Livre IV — Finalisation, optimisation, publication et maintenance

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

Ce livre transforme le projet jouable en produit testé, optimisé, publiable et maintenable. Le fil rouge reste `Project Asteria`.

## Chapitres

1. [Équilibrage et télémétrie locale](CHAPITRE-01-Equilibrage-et-telemetrie-locale.md)

Le chapitre 1 est présent, repéré et audité au niveau `static-review`. Les chapitres 2 à 22 restent à produire dans l’ordre du plan maître.

## Principes du Livre IV

- toute optimisation commence par une mesure et se termine par une comparaison avant/après ;
- une métrique n’obtient aucune autorité sur le système qu’elle observe ;
- les données personnelles sont évitées, minimisées, protégées et conservées pour une durée justifiée ;
- les campagnes, builds, migrations et retours arrière produisent des preuves consultables ;
- les parcours Solo et Studio partagent les mêmes invariants et diffèrent par les responsabilités ;
- les audits et preuves internes restent hors du manuel lecteur.
"""
write("Livre-IV/index.md", index)

def patch_contents(text: str) -> str:
    return replace_once(
        text,
        "Livre-IV/index.md\nLivre-V/index.md",
        "Livre-IV/index.md\nLivre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md\nLivre-V/index.md",
        "contents Livre IV",
    )
update("contents.txt", patch_contents)

def patch_roadmap(text: str) -> str:
    old = """## M5 — Livre IV : Finalisation et exploitation

- [ ] Équilibrage, QA et diagnostic.
- [ ] Optimisation et multijoueur.
- [ ] DevOps, publication et maintenance.
"""
    new = """## M5 — Livre IV : Finalisation et exploitation

- [x] Chapitre 1 — Équilibrage et télémétrie locale — rédigé et audité au niveau `static-review`.
- [ ] Équilibrage, QA et diagnostic — 1 chapitre sur 5.
- [ ] Optimisation et multijoueur.
- [ ] DevOps, publication et maintenance.
"""
    return replace_once(text, old, new, "ROADMAP M5")
update("ROADMAP.md", patch_roadmap)

def patch_validate_chapters(text: str) -> str:
    replacements = [
        ('CHAPTER_RE = re.compile(r"Livre-(I|II|III)/CHAPITRE-(\\d{2})-.+\\.md$")',
         'CHAPTER_RE = re.compile(r"Livre-(I|II|III|IV)/CHAPITRE-(\\d{2})-.+\\.md$")'),
        ('chapter_entries: dict[str, list[tuple[str, int]]] = {"I": [], "II": [], "III": []}',
         'chapter_entries: dict[str, list[tuple[str, int]]] = {"I": [], "II": [], "III": [], "IV": []}'),
        ('    actual_iii = [number for _, number in chapter_entries["III"]]\n    if actual_iii != list(range(1, len(actual_iii) + 1)):\n        errors.append(f"Les chapitres présents du Livre III doivent être continus depuis 01 ; détectés : {actual_iii}.")',
         '    actual_iii = [number for _, number in chapter_entries["III"]]\n    if actual_iii != list(range(1, len(actual_iii) + 1)):\n        errors.append(f"Les chapitres présents du Livre III doivent être continus depuis 01 ; détectés : {actual_iii}.")\n\n    actual_iv = [number for _, number in chapter_entries["IV"]]\n    if actual_iv != list(range(1, len(actual_iv) + 1)):\n        errors.append(f"Les chapitres présents du Livre IV doivent être continus depuis 01 ; détectés : {actual_iv}.")'),
        ('expected_book = {"I": "Livre I", "II": "Livre II", "III": "Livre III"}[book_code]',
         'expected_book = {"I": "Livre I", "II": "Livre II", "III": "Livre III", "IV": "Livre IV"}[book_code]'),
        ('expected_id = expected_livre_i_ids[number] if book_code == "I" else f"DOC-L{2 if book_code == \'II\' else 3}-CH{number:02d}"',
         'if book_code == "I":\n                expected_id = expected_livre_i_ids[number]\n            else:\n                book_number = {"II": 2, "III": 3, "IV": 4}[book_code]\n                expected_id = f"DOC-L{book_number}-CH{number:02d}"'),
        ('if book_code in {"II", "III"}:', 'if book_code in {"II", "III", "IV"}:'),
        ('                if book_code == "III" or number >= 17:', '                if book_code in {"III", "IV"} or number >= 17:'),
        ('                elif book_code == "III" or number >= 17:', '                elif book_code in {"III", "IV"} or number >= 17:'),
        ('if book_code == "III" and number >= 19:', 'if book_code == "IV" or (book_code == "III" and number >= 19):'),
        ('f"- Chapitres du Livre III : **{len(chapter_entries[\'III\'])}**",',
         'f"- Chapitres du Livre III : **{len(chapter_entries[\'III\'])}**",\n        f"- Chapitres du Livre IV : **{len(chapter_entries[\'IV\'])}**",'),
        ('"## Doublons par chapitre des Livres II et III", ""',
         '"## Doublons par chapitre des Livres II à IV", ""'),
    ]
    for old, new in replacements:
        text = replace_once(text, old, new, f"validate_chapters: {old[:40]}")
    return text
update("tools/validate_chapters.py", patch_validate_chapters)

def patch_code_explanations(text: str) -> str:
    text = replace_once(
        text,
        '    is_livre_iii = path.parent.name == "Livre-III"\n    if chapter is None or (not is_livre_iii and chapter < 17):',
        '    requires_four_labels = path.parent.name in {"Livre-III", "Livre-IV"}\n    if chapter is None or (path.parent.name == "Livre-II" and chapter < 17):',
        "code explanations scope",
    )
    text = replace_once(
        text,
        '        minimum = 4 if is_livre_iii or chapter in {25, 26} else 1',
        '        minimum = 4 if requires_four_labels or chapter in {25, 26} else 1',
        "code explanations minimum",
    )
    text = replace_once(
        text,
        '    for book in ("Livre-II", "Livre-III"):',
        '    for book in ("Livre-II", "Livre-III", "Livre-IV"):',
        "code explanations books",
    )
    return text
update("tools/check_code_explanation_structure.py", patch_code_explanations)

def patch_context_markers(text: str) -> str:
    text = replace_once(
        text,
        'AUDITED_CHAPTER_RE = re.compile(r"Livre-(II|III)/CHAPITRE-(\\d{2})-.+\\.md$")',
        'AUDITED_CHAPTER_RE = re.compile(r"Livre-(II|III|IV)/CHAPITRE-(\\d{2})-.+\\.md$")',
        "context regex",
    )
    text = replace_once(
        text,
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III"):',
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV"):',
        "context books",
    )
    text = replace_once(
        text,
        '        if book_code == "III" or chapter_number >= 17:',
        '        if book_code in {"III", "IV"} or chapter_number >= 17:',
        "context timestamps",
    )
    return text
update("tools/check_context_markers.py", patch_context_markers)

def patch_semantic_contexts(text: str) -> str:
    return replace_once(
        text,
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III"):',
        'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV"):',
        "semantic context books",
    )
update("tools/audit_contextes_semantiques.py", patch_semantic_contexts)

def patch_continuity(text: str) -> str:
    text = replace_once(text, 'version: "3.62.0"', 'version: "3.63.0"', "continuity version")
    text = replace_once(
        text,
        'last-updated: "2026-07-25T14:46:00+02:00"',
        f'last-updated: "{NOW}"',
        "continuity timestamp",
    )
    text = replace_once(
        text,
        "Cette règle est contrôlée automatiquement pour le Livre III à partir du chapitre 19.",
        "Cette règle est contrôlée automatiquement pour le Livre III à partir du chapitre 19 et pour tous les chapitres du Livre IV.",
        "continuity reference rule",
    )
    old_collection = """### Livres IV à V et Companion Pack

Le détail chapitre par chapitre ou pack par pack se trouve dans leurs plans maîtres. Chaque entrée y possède objectifs, livrables, dépendances, frontières et critères de validation.
"""
    new_collection = """### Livre IV

**En cours : 1 chapitre sur 22, au niveau `static-review`.**

1. Équilibrage et télémétrie locale — terminé au niveau `static-review`.

Les chapitres 2 à 22 restent à produire dans l’ordre de `plans/LIVRE-IV-PLAN-MAITRE.md`.

### Livre V et Companion Pack

Le détail chapitre par chapitre ou pack par pack se trouve dans leurs plans maîtres. Chaque entrée y possède objectifs, livrables, dépendances, frontières et critères de validation.
"""
    text = replace_once(text, old_collection, new_collection, "continuity collection")
    text = replace_once(
        text,
        "- jalon : M5 — Livre IV ;\n",
        "- jalon : M5 — Livre IV ;\n- progression du Livre IV : 1 chapitre sur 22 ;\n- chapitre 1 du Livre IV : version `1.0.0`, niveau `static-review` ;\n",
        "continuity current state",
    )
    start = text.index("## 26. Prochaine action")
    end = text.index("## 27. Journal")
    next_action = f"""## 26. Prochaine action

Le Livre IV compte un chapitre rédigé, repéré et audité sur vingt-deux. Le chapitre 1 définit le catalogue de métriques, les scénarios d’équilibrage, les comparaisons et les règles de minimisation sans collecte de joueur ni revendication runtime.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 2 définira les niveaux de test, responsabilités, portes qualité, risques et critères d’entrée ou de sortie. Il consommera les métriques et rapports du chapitre 1 sans détailler encore les tests fonctionnels du chapitre 3.

"""
    text = text[:start] + next_action + text[end:]
    journal_anchor = "## 27. Journal\n\n"
    journal_entry = f"""### {NOW} — version 3.63.0

- chapitre 1 du Livre IV créé, relu et audité au niveau `static-review` ;
- catalogue de métriques, finalités, unités, dimensions, bornes et rétention documentés ;
- courbes de progression, métriques de combat, économie, écologie et difficulté encadrées ;
- scénarios, seeds, répétitions, bornes, distributions et comparaisons référence/candidat documentés ;
- rapports de décision, garde-fous, autorité humaine et retour arrière définis ;
- séparation entre simulation synthétique, test interne et données joueurs explicitée ;
- minimisation, pseudonymisation, anonymisation prudente, rétention et purge encadrées ;
- validateurs légers étendus explicitement au Livre IV ;
- progression portée à 1 chapitre sur 22 ; prochaine action déplacée vers le chapitre 2 ;
- aucun test runtime, collecte joueur, décision appliquée ou PDF revendiqué.

"""
    text = replace_once(text, journal_anchor, journal_anchor + journal_entry, "continuity journal")
    return text
update("CONTINUITE-PROJET.md", patch_continuity)

print("Lot Livre IV chapitre 1 matérialisé.")
