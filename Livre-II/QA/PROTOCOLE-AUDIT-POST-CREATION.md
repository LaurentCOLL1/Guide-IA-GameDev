---
title: "Protocole d’audit post-création des chapitres"
id: "DOC-L2-QA-POST-CREATION"
status: "complete"
version: "1.7.3"
book: "Livre II"
category: "quality-protocol"
last-verified: "2026-07-20T10:19:05+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Protocole d’audit post-création des chapitres

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Règle obligatoire

À partir du Livre II, un chapitre n’est jamais considéré comme terminé immédiatement après sa rédaction. Il doit franchir une porte d’audit distincte, recevoir ses corrections et laisser une preuve consultable.

La séquence obligatoire est :

> **[LECTURE] Processus de référence — Ne pas saisir.**

```text
annonce du chapitre et du niveau GPT-5.6 Sol conseillé
   ↓
rédaction
   ↓
audit de complétude et de périmètre
   ↓
audit des outils et contextes d’utilisation
   ↓
contrôle des doublons et seconde lecture
   ↓
vérification technique et des sources
   ↓
mise à jour index / roadmap / contents.txt / continuité
   ↓
contrôles documentaires et statiques du chapitre
   ↓
rapport d’audit
   ↓
chapitre déclaré rédigé, repéré et audité
```

La compilation Pandoc/XeLaTeX et l’inspection visuelle du PDF ne sont plus réalisées après chaque chapitre. Elles sont regroupées à la fin de chaque Livre, puis une dernière fois à la fin de la collection.

## 2. Politique de génération PDF

### 2.1 Construction différée

Le PDF complet est construit :

1. à la fin du Volume ou Livre actif ;
2. à la fin du Companion Pack lorsqu’une publication PDF est pertinente ;
3. à la fin de la collection complète.

Cette politique réduit le temps de calcul et évite de produire des artefacts intermédiaires qui deviennent rapidement obsolètes.

### 2.2 Exceptions

Une construction intermédiaire reste autorisée uniquement lorsque le lot modifie directement :

- `metadata.yaml` ;
- les scripts `build.ps1` ou `build.sh` ;
- le filtre Pandoc ;
- le moteur PDF ;
- les polices ;
- la table des matières ;
- les marges, tableaux ou règles de mise en page ;
- le workflow de publication.

L’exception et sa justification doivent être consignées dans le rapport QA.

### 2.3 Workflows permanents

Deux workflows ont des responsabilités séparées :

- `Validate Chapters Without PDF` s’exécute sur chaque pull request documentaire du Livre II et contrôle structure, métadonnées, liens, doublons et repères sans produire de PDF ;
- `Validate Documentation PDF` est réservé au déclenchement manuel de fin de Livre ou aux modifications directes de la chaîne de publication.

Le workflow léger doit contenir une assertion explicite confirmant qu’aucun fichier PDF n’a été produit.

### 2.4 Ce qui reste obligatoire par chapitre

Chaque chapitre doit encore réussir :

- l’intégrité du Markdown et du front matter ;
- la continuité des numéros et identifiants ;
- la vérification des liens locaux ;
- l’audit des repères d’utilisation ;
- le contrôle des doublons ;
- la vérification statique du code et des commandes ;
- la comparaison au plan maître ;
- la mise à jour des documents de gouvernance.

## 3. Recommandation du niveau GPT-5.6 Sol

Avant toute rédaction, la conversation doit annoncer :

- le titre exact du chapitre ;
- le niveau conseillé : **Moyenne** ou **Élevée** ;
- une justification liée au contenu réel du chapitre.

Utiliser généralement :

- **Moyenne** pour un chapitre principalement descriptif, linéaire, à faible risque technique et avec peu de dépendances ;
- **Élevée** pour architecture, code imbriqué, bases de données, IA, sécurité, optimisation, intégrations ou nombreuses frontières entre systèmes.

La recommandation est enregistrée dans le front matter :

> **[LECTURE] Exemple YAML — Ne pas créer de fichier sans chemin explicitement indiqué.**

```yaml
recommended-reasoning: "GPT-5.6 Sol — Élevée"
```

## 4. Métadonnées obligatoires

Un chapitre audité porte au minimum :

> **[LECTURE] Exemple YAML — Ne pas créer de fichier sans chemin explicitement indiqué.**

```yaml
last-verified: "AAAA-MM-JJTHH:MM:SS±HH:MM"
audit-status: "complete"
audit-date: "AAAA-MM-JJTHH:MM:SS±HH:MM"
audit-report: "Livre-II/QA/<rapport>.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"
```

Les champs `last-verified` et `audit-date` sont des chaînes ISO 8601 entre guillemets et incluent obligatoirement les secondes ainsi qu’un décalage UTC explicite. `static-review` signifie que les explications, commandes et extraits ont été relus contre les références officielles, sans prétendre qu’ils ont tous été exécutés. Le niveau devient `runtime-tested` uniquement lorsque les fichiers du projet fil rouge ont été matérialisés, exécutés et associés à des journaux conservés.

## 5. Matrice de contrôle

### Q0 — Intégrité

- [ ] Le fichier existe au chemin canonique.
- [ ] Le front matter YAML est valide.
- [ ] L’identifiant est unique et correspond au numéro du chapitre.
- [ ] L’encodage UTF-8 et les blocs Markdown sont valides.
- [ ] Les liens locaux sont résolus.
- [ ] Chaque fragment interne vise une ancre existante et la sous-section la plus précise pertinente.
- [ ] Le niveau de raisonnement conseillé est annoncé et enregistré.

### Q1 — Complétude pédagogique

- [ ] L’objectif et les prérequis sont observables.
- [ ] Les termes nouveaux sont définis avant usage.
- [ ] Le parcours convient à un débutant.
- [ ] Les fonctions, paramètres, types et opérateurs nouveaux sont expliqués.
- [ ] Les sujets exclus sont renvoyés au bon chapitre.
- [ ] Les modes Solo et Studio sont présents lorsque pertinents.
- [ ] Une checklist et un critère d’acceptation sont fournis.
- [ ] Toute section qui enseigne des erreurs, anti-patterns, pièges ou corrections fournit un exemple fautif, un exemple corrigé et leur différence pour chaque cas.
- [ ] Chaque bloc de code significatif possède une explication pédagogique proportionnée à sa longueur et à sa complexité.

#### Q1.1 — Explication obligatoire de chaque bloc de code

Un bloc de code ne peut pas être considéré comme expliqué par une simple phrase générique. L’explication doit donner au lecteur les informations nécessaires pour comprendre, adapter et diagnostiquer l’extrait.

Pour chaque bloc significatif, vérifier explicitement, selon ce que le bloc exige réellement :

1. son rôle uniquement lorsque cette formulation ajoute une information propre au code ;
2. son emplacement seulement lorsqu’il n’est pas déjà donné par la consigne `[VSC]` ou par le contexte adjacent ;
3. les entrées, paramètres, types, valeurs par défaut et dépendances qui demandent une explication ;
4. les sorties, valeurs de retour, erreurs, signaux et effets de bord ;
5. le déroulement des instructions importantes, ligne par ligne ou par groupes cohérents ;
6. les opérateurs, conversions, conditions et appels non évidents ;
7. les préconditions, invariants et postconditions protégés ;
8. le résultat attendu et la manière de le vérifier ;
9. les variantes raisonnables, limites et erreurs fréquentes pour un débutant ;
10. le lien avec l’architecture générale lorsqu’il éclaire réellement l’extrait.

Une explication peut être placée avant ou après le bloc, mais elle doit être immédiatement identifiable. Elle ne répète ni le chemin déjà affiché avant le code, ni une règle générale de syntaxe déjà présentée dans un chapitre de référence. Une rubrique `Rôle` qui reformule seulement le titre de la section est supprimée ; elle est conservée lorsqu’elle nomme un contrat, une fonction, une transformation ou une responsabilité concrète. Cette interdiction vaut pour toutes les rubriques : `Rôle`, `Pourquoi cet exemple est fautif`, `Pourquoi la correction fonctionne`, `Résultat attendu` ou toute formulation équivalente. Une explication ne peut jamais justifier un bloc en citant le titre de la section qui le contient ; elle énonce directement le fait technique, le risque ou l’invariant.

Dans une section d’erreurs, d’anti-patterns, de pièges ou de corrections, le format privilégié est plus court : `Pourquoi cet exemple est fautif` sous le contre-exemple et `Pourquoi la correction fonctionne` sous la version corrigée. Un renvoi vers une section ou un chapitre antérieur peut être placé avant le code fautif lorsqu’il évite de répéter une règle déjà établie. Ce renvoi vise la sous-section exacte qui porte la règle ; une section parente n’est acceptable qu’en l’absence de cible plus précise. Son fragment doit être vérifié. Une ancre explicite et stable est privilégiée lorsque le fragment automatique du titre peut être ambigu, fragile ou dépendre du moteur Markdown.

Hors de ces sections pédagogiques, le mot `erreur` ne sert pas de libellé générique pour tout résultat négatif. Employer :

- `Valeurs de retour` lorsqu’une fonction renvoie plusieurs formes de résultat, y compris une sentinelle ;
- `Codes de retour` lorsqu’une fonction renvoie des valeurs de l’énumération `Error` ;
- `Refus contrôlé` lorsqu’une entrée ou une opération est rejetée normalement par un contrat ;
- `Statuts à distinguer` lorsqu’il faut comparer plusieurs états métier ou résultats de recherche ;
- `Traitement du résultat` lorsque l’appelant doit consommer, journaliser ou propager la valeur renvoyée.

Le libellé `Erreur fréquente` est réservé à un véritable piège que le lecteur pourrait reproduire. S’il apparaît, il relève de Q1.2 et doit être accompagné d’un exemple fautif et d’une correction, ou être reformulé avec l’un des libellés précis ci-dessus.

### Q1.1.1 — Horodatage des vérifications et audits

À partir du chapitre 17 version `1.0.2`, et pour tout nouveau chapitre ou document d’audit, `last-verified` et `audit-date` utilisent une chaîne ISO 8601 complète et entre guillemets : date, heure, minutes, secondes et décalage UTC. Le fuseau de référence du projet est `Europe/Paris` ; l’offset enregistré suit donc l’heure légale applicable, par exemple `+01:00` ou `+02:00`.

Une heure ne doit jamais être inventée rétroactivement. Les documents historiques qui portent seulement `YYYY-MM-DD` conservent cette valeur jusqu’à leur prochaine révision réellement vérifiée. Dès qu’un chapitre ou son audit est modifié et revalidé, les deux champs sont actualisés avec l’heure effective de cette nouvelle vérification.

Le validateur impose ce format au chapitre 17 et aux chapitres suivants, ainsi qu’à leurs rapports d’audit.

**Règle de décision :** si un lecteur débutant doit deviner la fonction d’une ligne importante, d’un paramètre, d’un type, d’un retour ou d’un effet de bord, le bloc est non conforme et le chapitre ne peut pas passer l’audit.

### Q1.2 — Règle sémantique des erreurs et corrections

La règle dépend de la fonction pédagogique, jamais du titre exact. Elle couvre notamment les sections nommées :

- `Erreurs fréquentes` ;
- `Erreurs fréquentes et diagnostics` ;
- `Anti-patterns et corrections` ;
- `Éviter les anti-patterns` ;
- `Pièges`, `Mauvaises pratiques` ou toute formulation équivalente.

Une section détaillée porte le marqueur invisible suivant :

> **[LECTURE] Marqueur QA — Ne pas saisir dans un terminal.**

```html
<!-- qa:error-correction-section -->
```

Chaque sous-cas doit alors contenir :

1. un symptôme ou risque ;
2. un **exemple fautif** suivi de `Pourquoi cet exemple est fautif` ;
3. un **exemple corrigé** suivi de `Pourquoi la correction fonctionne`.

Une ligne autonome `Correction` ou `Différence` n’est pas exigée lorsque son contenu est déjà intégré à ces deux explications. Le but est d’éviter la répétition sans supprimer l’analyse de l’invariant violé puis rétabli.

Un tableau servant uniquement d’index de diagnostic peut rester compact s’il porte `<!-- qa:error-correction-index -->` et renvoie clairement vers une section détaillée conforme. Il ne peut pas remplacer les exemples détaillés.

### Q2 — Cohérence de collection

- [ ] Le chapitre couvre exactement son entrée du sommaire maître.
- [ ] Il ne duplique pas inutilement un chapitre précédent.
- [ ] Il ne consomme pas prématurément le périmètre suivant.
- [ ] Les chemins et identifiants cités sont stables.
- [ ] L’index, la roadmap, `contents.txt` et `CONTINUITE-PROJET.md` reflètent son état réel.

### Q3 — Vérification technique

- [ ] Les versions et sources sont actuelles à la date d’audit.
- [ ] Les sources principales sont officielles et épinglées lorsque possible.
- [ ] Les commandes sont relues argument par argument.
- [ ] Les exemples de code font l’objet d’une revue syntaxique statique.
- [ ] Les sorties attendues sont plausibles.
- [ ] Les limitations des tests sont déclarées.
- [ ] Les erreurs courantes disposent d’un diagnostic.

### Q4 — Outils et contextes d’utilisation

- [ ] Chaque bloc procédural possède un repère reconnu.
- [ ] Une commande indique le terminal exact : `[PS]`, `[CMD]`, `[WSL]` ou `[DCT]`.
- [ ] Un fichier à créer ou modifier indique `[VSC]` et son chemin cible.
- [ ] Une action graphique indique `[APP]` ou `[DCK]` et nomme l’application.
- [ ] Un téléchargement procédural indique `[WEB]`.
- [ ] Une sortie à comparer utilise `[SORTIE]`.
- [ ] Un exemple non exécutable utilise `[LECTURE]`.
- [ ] Le repère est cohérent avec le langage et l’action décrite.

### Q5 — Sécurité et licences

- [ ] Les privilèges sont minimaux.
- [ ] Les commandes destructives sont signalées.
- [ ] Aucun secret réel n’apparaît.
- [ ] Les obligations de licence et d’attribution sont mentionnées.
- [ ] Les addons, modèles, assets ou services tiers sont qualifiés.

### Q6 — Validation documentaire du chapitre

- [ ] Le contrôle des repères réussit.
- [ ] Le contrôle des doublons réussit.
- [ ] Les contrôles spécialisés du chapitre réussissent lorsqu’ils existent.
- [ ] L’ordre de compilation est mis à jour sans construire le PDF.
- [ ] Les réserves statiques et runtime sont consignées.
- [ ] Le rapport d’audit est complet.

### Q7 — Publication de fin de Livre

Cette porte reste **différée** jusqu’au dernier chapitre du Livre :

- [ ] la compilation Pandoc/XeLaTeX réussit ;
- [ ] le PDF est non vide et son texte est extractible ;
- [ ] la table des matières est lisible ;
- [ ] un échantillon représentatif des pages est inspecté visuellement ;
- [ ] les erreurs, réserves, exécutions et artefacts sont consignés ;
- [ ] la preuve finale ne contient pas de mesure auto-référentielle.

## 6. Décision

Un audit de chapitre se termine par une décision unique :

- **Accepté** : aucune non-conformité bloquante ou majeure ouverte ;
- **Accepté avec réserves** : le chapitre est utilisable, mais un test runtime, matériel ou PDF de fin de Livre reste à produire ;
- **Refusé** : une omission ou erreur majeure empêche de le considérer comme terminé.

La mention **rédigé, repéré et audité** signifie que les portes documentaires et statiques du chapitre ont réussi. Elle ne signifie ni que tous les exemples ont été exécutés, ni qu’un PDF intermédiaire a été construit.
