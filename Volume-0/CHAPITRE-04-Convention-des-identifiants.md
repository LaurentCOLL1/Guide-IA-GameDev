---
title: "Volume 0 — Chapitre 4 : Convention des identifiants"
id: "DOC-V0-CH04"
status: "complete"
version: "1.4.0"
lang: "fr-FR"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Volume 0 — Chapitre 4 : Convention des identifiants

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Objectif

Ce chapitre définit le système d’identifiants stables utilisé dans toute la collection et dans le Companion Pack.

Un identifiant permet de référencer une ressource sans dépendre :

- de son numéro de page ;
- de son emplacement physique dans le dépôt ;
- du format de publication ;
- de la version du PDF ;
- de l’ordre futur des chapitres.

Les identifiants sont conçus pour rester valides pendant toute la durée de vie du projet.

## 2. Principes généraux

Chaque ressource importante reçoit un identifiant unique, lisible et non réutilisable.

Un identifiant doit être :

- stable ;
- court ;
- explicite ;
- écrit en lettres majuscules ASCII ;
- séparé par des tirets ;
- exempt d’espace, d’accent et de ponctuation libre.

Une ressource supprimée conserve son identifiant dans le registre historique. Cet identifiant ne doit jamais être attribué à une autre ressource.

## 3. Structure générale

La forme générique est :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
<CATEGORIE>-<SOUS-CATEGORIE>-<NUMERO>
```

Exemples :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
GDS-GAME-001
PY-AUTO-014
SQL-ECO-003
WF-CFY-027
PR-IMG-042
UML-SEQ-008
CHK-BUILD-006
```

Certaines ressources documentaires utilisent une structure dédiée :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
DOC-V0-CH04
DOC-L1-CH03
DOC-L2-P2-CH11
DOC-L5-FICHE-0042
```

## 4. Identifiants documentaires

### 4.1 Volume 0

Format :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
DOC-V0-CHNN
```

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-V0-CH04
```

### 4.2 Livres I à IV

Format simple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-LN-CHNN
```

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-L1-CH03
```

Lorsque le livre est divisé en parties :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-LN-PN-CHNN
```

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-L2-P3-CH07
```

### 4.3 Livre V

Le Livre V contient principalement des fiches de référence.

Format :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-L5-<TYPE>-NNNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
DOC-L5-IA-0001
DOC-L5-WF-0012
DOC-L5-ERR-0043
```

### 4.4 Annexes

Format :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ANN-<VOLUME>-<LETTRE>
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ANN-V0-A
ANN-L4-C
```

## 5. Identifiants du Companion Pack

### 5.1 Scripts GDScript

Préfixe : `GDS`

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
GDS-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
GDS-INV-001
GDS-DLG-004
GDS-NET-012
```

### 5.2 Scripts Python

Préfixe : `PY`

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PY-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PY-AUTO-001
PY-ASSET-015
PY-BENCH-003
```

### 5.3 Scripts PowerShell, Bash et outils système

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PS-<DOMAINE>-NNN
SH-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PS-BUILD-001
SH-BACKUP-002
```

### 5.4 Structures JSON

Préfixe : `JSON`

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
JSON-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
JSON-NPC-001
JSON-QUEST-003
JSON-WORLD-008
```

### 5.5 Schémas et scripts SQL

Préfixe : `SQL`

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
SQL-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
SQL-NPC-001
SQL-ECO-004
SQL-SAVE-002
```

### 5.6 Workflows ComfyUI

Préfixe : `WF-CFY`

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-CFY-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-CFY-CHAR-001
WF-CFY-TEX-014
WF-CFY-VFX-003
```

### 5.7 Workflows généraux

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-<OUTIL>-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-BLD-RIG-002
WF-GDT-IMPORT-006
WF-OWUI-RAG-004
```

### 5.8 Prompts

Préfixe : `PR`

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PR-<TYPE>-<DOMAINE>-NNN
```

Types principaux :

- `TXT` : texte ;
- `IMG` : image ;
- `AUD` : audio ;
- `CODE` : programmation ;
- `DATA` : JSON, SQL ou données structurées.

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PR-TXT-LORE-001
PR-IMG-CHAR-018
PR-AUD-VOICE-006
PR-CODE-GDS-022
```

### 5.9 Diagrammes UML et architecture

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
UML-<TYPE>-NNN
ARCH-<DOMAINE>-NNN
```

Types UML usuels :

- `CLS` : classes ;
- `SEQ` : séquence ;
- `CMP` : composants ;
- `DEP` : déploiement ;
- `ACT` : activité ;
- `STATE` : états.

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
UML-CLS-003
UML-SEQ-011
ARCH-DOCKER-002
```

### 5.10 Checklists, tests et benchmarks

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
CHK-<DOMAINE>-NNN
TST-<TYPE>-NNN
BENCH-<DOMAINE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
CHK-ASSET-004
TST-NET-012
BENCH-CFY-003
```

### 5.11 Templates et documents

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
TMP-<TYPE>-NNN
DOC-TPL-<TYPE>-NNN
```

Exemples :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
TMP-GODOT-001
TMP-DOCKER-004
DOC-TPL-GDD-001
```

## 6. Codes de domaines normalisés

Les codes suivants sont privilégiés :

| Code | Domaine |
|---|---|
| `CHAR` | personnages |
| `NPC` | personnages non-joueurs |
| `DLG` | dialogues |
| `QUEST` | quêtes |
| `INV` | inventaire |
| `ECO` | économie |
| `REL` | relations |
| `FAM` | famille |
| `COMBAT` | combat |
| `SKILL` | compétences |
| `WORLD` | monde vivant |
| `POL` | politique |
| `BUILD` | construction et bâtiments |
| `NARR` | narration |
| `SAVE` | sauvegardes |
| `NET` | réseau et multijoueur |
| `UI` | interface utilisateur |
| `UX` | expérience utilisateur |
| `AUDIO` | audio général |
| `VOICE` | voix et TTS |
| `MUSIC` | musique |
| `VFX` | effets visuels |
| `TEX` | textures |
| `RIG` | rigging |
| `ANIM` | animation |
| `ASSET` | ressources artistiques |
| `AUTO` | automatisation |
| `BENCH` | benchmarks |
| `DOC` | documentation |

Un nouveau code ne doit être créé que lorsqu’aucun code existant ne convient.

## 7. Numérotation

Les numéros sont attribués séquentiellement dans chaque espace de noms.

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
GDS-INV-001
GDS-INV-002
GDS-INV-003
```

Les trous de numérotation sont autorisés. Ils ne doivent pas être comblés par réutilisation d’un identifiant retiré.

Trois chiffres sont utilisés pour les bibliothèques techniques ordinaires. Quatre chiffres sont autorisés pour les très grandes collections, notamment les fiches du Livre V.

## 8. Identifiant et nom de fichier

L’identifiant ne remplace pas le nom descriptif du fichier.

Exemple recommandé :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
GDS-INV-001-inventory-service.gd
```

Exemples documentaires :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
CHAPITRE-04-Convention-des-identifiants.md
FICHE-0042-Ollama.md
```

L’identifiant officiel est stocké dans les métadonnées du fichier et, lorsque pertinent, dans son en-tête.

## 9. Métadonnées minimales

Chaque document Markdown majeur utilise un en-tête YAML :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text CHAPITRE-04-Convention-des-identifiants.md FICHE-0042-Ollama.md`.

```yaml
---
title: "Titre de la ressource"
id: "DOC-V0-CH04"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
---
```

Les ressources techniques peuvent utiliser un manifeste associé :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: GDS-INV-001
name: inventory-service
version: 1.0.0
language: gdscript
status: stable
```

## 10. Statuts normalisés

Les valeurs recommandées sont :

- `planned` : ressource planifiée ;
- `draft` : première rédaction ;
- `in-review` : en relecture ;
- `complete` : rédaction terminée ;
- `stable` : ressource testée et validée ;
- `deprecated` : encore disponible, mais déconseillée ;
- `archived` : conservée uniquement pour l’historique.

## 11. Références croisées

Une référence technique cite l’identifiant et peut ajouter un lien relatif :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```markdown
Voir [DOC-V0-CH03](CHAPITRE-03-Architecture-documentaire.md).
```

Pour une ressource du Companion Pack :

> **[VSC] Visual Studio Code - Créer ou modifier :** `markdown Voir [DOC-V0-CH03](CHAPITRE-03-Architecture-documentaire.md).`.

```markdown
Utiliser `GDS-INV-001` et le schéma `SQL-INV-001`.
```

Les numéros de page ne doivent jamais constituer l’unique moyen de référence.

## 12. Registre central

Le Companion Pack comportera un registre central des identifiants.

Structure prévue :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
Companion-Pack/Knowledge-Base/identifiers/
├── registry.yaml
├── deprecated.yaml
└── aliases.yaml
```

Le registre indiquera au minimum :

- identifiant ;
- titre ;
- type ;
- chemin ;
- version ;
- statut ;
- dépendances principales.

## 13. Aliases et renommages

Lorsqu’une ressource change de nom ou de chemin, son identifiant reste inchangé.

Un alias peut être créé pour faciliter une transition, mais il ne devient pas un nouvel identifiant officiel.

Exemple :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
aliases:
  GDS-INVENTORY-001: GDS-INV-001
```

## 14. Dépréciation

Une ressource dépréciée :

1. conserve son identifiant ;
2. reçoit le statut `deprecated` ;
3. indique la ressource de remplacement ;
4. reste accessible pendant une période de transition ;
5. n’est jamais remplacée silencieusement par un contenu incompatible.

## 15. Validation automatique

À terme, un script vérifiera :

- l’unicité des identifiants ;
- la conformité de leur syntaxe ;
- l’existence des chemins référencés ;
- l’absence d’identifiants réutilisés ;
- la validité des références croisées ;
- la cohérence entre registre et métadonnées.

Ressource prévue :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
PY-DOC-001
```

## 16. Mode Solo et Mode Studio

### Mode Solo

Le développeur peut attribuer les identifiants directement, à condition de tenir le registre à jour.

### Mode Studio

L’équipe doit définir :

- une personne ou un processus responsable du registre ;
- une procédure de réservation des identifiants ;
- une validation lors des revues ;
- une règle de dépréciation commune.

## 17. Erreurs fréquentes

- créer deux identifiants pour la même ressource ;
- modifier l’identifiant lors d’un simple renommage ;
- réutiliser un identifiant supprimé ;
- employer des accents ou espaces ;
- mélanger identifiant, numéro de chapitre et numéro de page ;
- multiplier les codes de domaines synonymes ;
- référencer uniquement un chemin susceptible de changer.

## 18. Checklist de validation

- [ ] L’identifiant respecte la syntaxe de sa catégorie.
- [ ] Il est unique dans le registre.
- [ ] Le code de domaine existe ou a été approuvé.
- [ ] Le numéro n’a jamais été utilisé auparavant.
- [ ] Les métadonnées du fichier contiennent l’identifiant.
- [ ] Les références croisées utilisent l’identifiant stable.
- [ ] Tout renommage conserve l’identifiant original.
- [ ] Toute dépréciation indique un remplacement.

## 19. Références croisées

- `DOC-V0-CH01` — Vision générale du projet.
- `DOC-V0-CH02` — Les 21 règles fondamentales.
- `DOC-V0-CH03` — Architecture documentaire.
- `DOC-V0-CH05` — Conventions Markdown et Pandoc.
- `DOC-L5-INDEX` — Encyclopédie technique.

## 20. Résultat attendu

À l’issue de ce chapitre, toutes les ressources du guide peuvent être nommées et référencées de manière durable, indépendamment de leur emplacement, de leur format de publication et des futures réorganisations du dépôt.
