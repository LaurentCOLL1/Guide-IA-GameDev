---
title: "Protocole d’audit post-création des chapitres"
id: "DOC-L2-QA-POST-CREATION"
status: "complete"
version: "1.0.0"
book: "Livre II"
category: "quality-protocol"
last-verified: "2026-07-18"
---

# Protocole d’audit post-création des chapitres

## 1. Règle obligatoire

À partir du Livre II, un chapitre n’est pas considéré comme terminé immédiatement après sa rédaction.

Il doit franchir une porte d’audit post-création distincte comprenant :

1. la comparaison avec le sommaire maître ;
2. la vérification du périmètre annoncé ;
3. la recherche des notions fondamentales manquantes ;
4. la vérification des versions et des sources officielles ;
5. la relecture des commandes et exemples de code ;
6. le contrôle des frontières avec les chapitres précédents et suivants ;
7. le contrôle des métadonnées, liens, index, roadmap et `contents.txt` ;
8. la compilation Pandoc/XeLaTeX ;
9. l’inspection technique du PDF ;
10. la rédaction d’une preuve d’audit.

Un chapitre audité porte les métadonnées suivantes :

```yaml
audit-status: "complete"
audit-date: "AAAA-MM-JJ"
audit-report: "Livre-II/QA/<rapport>.md"
audit-level: "static-review"
```

`audit-level: static-review` signifie que le contenu, les commandes et le code ont été relus contre les références officielles, mais que les extraits n’ont pas nécessairement été exécutés sur une copie matérialisée de `Project Asteria`.

Lorsque les fichiers exécutables existent dans le Companion Pack ou dans le dépôt du projet fil rouge, le niveau peut devenir :

```yaml
audit-level: "runtime-tested"
```

## 2. Matrice de contrôle

### Q0 — Intégrité

- [ ] Le fichier existe au chemin canonique.
- [ ] Le front matter YAML est valide.
- [ ] L’identifiant est unique.
- [ ] Le numéro du chapitre correspond au nom de fichier.
- [ ] L’encodage et les blocs Markdown sont valides.

### Q1 — Complétude pédagogique

- [ ] L’objectif est observable.
- [ ] Les prérequis sont indiqués.
- [ ] Les termes nouveaux sont définis.
- [ ] Le parcours convient à un débutant.
- [ ] Les sujets exclus sont annoncés et renvoyés au bon chapitre.
- [ ] Les modes Solo et Studio sont présents lorsque pertinents.
- [ ] Une checklist et un critère d’acceptation sont fournis.

### Q2 — Cohérence de collection

- [ ] Le chapitre couvre exactement son entrée du sommaire maître.
- [ ] Il ne duplique pas inutilement un chapitre précédent.
- [ ] Il ne consomme pas prématurément le périmètre d’un chapitre suivant.
- [ ] Les identifiants et chemins cités sont stables.
- [ ] L’index, la roadmap et `contents.txt` reflètent son état réel.

### Q3 — Vérification technique

- [ ] Les versions sont actuelles à la date d’audit.
- [ ] Les sources principales sont officielles et épinglées à la version lorsque possible.
- [ ] Les commandes ont été relues argument par argument.
- [ ] Les exemples de code ont été relus syntaxiquement.
- [ ] Les sorties attendues sont plausibles et cohérentes.
- [ ] Les limitations du test sont déclarées.
- [ ] Un diagnostic est prévu pour les erreurs courantes.

### Q4 — Sécurité et licences

- [ ] Les privilèges sont minimaux.
- [ ] Les commandes destructives sont signalées.
- [ ] Aucun secret réel n’apparaît.
- [ ] Les obligations de licence et d’attribution sont mentionnées.
- [ ] Les addons, modèles, assets ou services tiers sont qualifiés.

### Q5 — Publication

- [ ] La CI structurelle réussit.
- [ ] La compilation Pandoc/XeLaTeX réussit.
- [ ] Le PDF est non vide et son texte est extractible.
- [ ] Les erreurs ou réserves sont consignées dans le rapport d’audit.

## 3. Décision

Un audit se termine par une décision unique :

- **Accepté** : aucune non-conformité bloquante ou majeure ouverte ;
- **Accepté avec réserves** : le chapitre est utilisable, mais un test runtime ou matériel reste à produire ;
- **Refusé** : une omission ou erreur majeure empêche de le considérer comme terminé.

## 4. Règle pour les prochains chapitres

La séquence obligatoire devient :

```text
rédaction
   ↓
audit de complétude
   ↓
corrections
   ↓
vérification technique
   ↓
mise à jour index / roadmap / contents
   ↓
compilation CI
   ↓
rapport d’audit
   ↓
chapitre déclaré audité
```

La CI du dépôt vérifie la présence de `audit-status`, `audit-date` et `audit-report` pour chaque chapitre du Livre II déclaré dans `contents.txt`.