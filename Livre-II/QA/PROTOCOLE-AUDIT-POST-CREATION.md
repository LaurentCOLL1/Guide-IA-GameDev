---
title: "Protocole d’audit post-création des chapitres"
id: "DOC-L2-QA-POST-CREATION"
status: "complete"
version: "1.1.0"
book: "Livre II"
category: "quality-protocol"
last-verified: "2026-07-18"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Protocole d’audit post-création des chapitres

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Règle obligatoire

À partir du Livre II, un chapitre n’est jamais considéré comme terminé immédiatement après sa rédaction. Il doit franchir une porte d’audit distincte, recevoir ses corrections, réussir les validations automatiques et laisser une preuve consultable.

La séquence obligatoire est :

> **[LECTURE] Processus de référence - Ne pas saisir.**

```text
rédaction
   ↓
audit de complétude et de périmètre
   ↓
audit des outils et contextes d’utilisation
   ↓
corrections et seconde lecture
   ↓
vérification technique et des sources
   ↓
mise à jour index / roadmap / contents.txt
   ↓
CI structurelle, contextuelle et PDF
   ↓
rapport et preuve externe
   ↓
chapitre déclaré rédigé, repéré et audité
```

## 2. Métadonnées obligatoires

Un chapitre audité porte au minimum :

> **[LECTURE] Exemple YAML - Ne pas créer de fichier sans chemin explicitement indiqué.**

```yaml
audit-status: "complete"
audit-date: "AAAA-MM-JJ"
audit-report: "Livre-II/QA/<rapport>.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
```

`static-review` signifie que les explications, commandes et extraits ont été relus contre les références officielles, sans prétendre qu’ils ont tous été exécutés. Le niveau devient `runtime-tested` uniquement lorsque les fichiers du projet fil rouge ont été matérialisés, exécutés et associés à des journaux conservés.

## 3. Matrice de contrôle

### Q0 — Intégrité

- [ ] Le fichier existe au chemin canonique.
- [ ] Le front matter YAML est valide.
- [ ] L’identifiant est unique et correspond au numéro du chapitre.
- [ ] L’encodage UTF-8 et les blocs Markdown sont valides.
- [ ] Les liens locaux sont résolus.

### Q1 — Complétude pédagogique

- [ ] L’objectif et les prérequis sont observables.
- [ ] Les termes nouveaux sont définis avant usage.
- [ ] Le parcours convient à un débutant.
- [ ] Les sujets exclus sont renvoyés au bon chapitre.
- [ ] Les modes Solo et Studio sont présents lorsque pertinents.
- [ ] Une checklist et un critère d’acceptation sont fournis.

### Q2 — Cohérence de collection

- [ ] Le chapitre couvre exactement son entrée du sommaire maître.
- [ ] Il ne duplique pas inutilement un chapitre précédent.
- [ ] Il ne consomme pas prématurément le périmètre suivant.
- [ ] Les chemins et identifiants cités sont stables.
- [ ] L’index, la roadmap et `contents.txt` reflètent son état réel.

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

### Q6 — Publication

- [ ] `Validate Usage Contexts` réussit.
- [ ] `Validate Documentation` réussit.
- [ ] La compilation Pandoc/XeLaTeX réussit.
- [ ] Le PDF est non vide et son texte est extractible.
- [ ] Un échantillon des pages modifiées est inspecté visuellement.
- [ ] Les erreurs, réserves, exécutions et artefacts sont consignés.

## 4. Décision

Un audit se termine par une décision unique :

- **Accepté** : aucune non-conformité bloquante ou majeure ouverte ;
- **Accepté avec réserves** : le chapitre est utilisable, mais un test runtime ou matériel reste à produire ;
- **Refusé** : une omission ou erreur majeure empêche de le considérer comme terminé.

La mention **rédigé, repéré et audité** signifie que les portes documentaires et statiques ont réussi. Elle ne signifie pas automatiquement que tous les exemples ont été exécutés sur la station de référence.
