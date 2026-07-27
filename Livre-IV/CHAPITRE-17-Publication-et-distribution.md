---
title: "Livre IV — Chapitre 17 : Publication et distribution"
id: "DOC-L4-CH17"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 17
last-verified: "2026-07-27T09:40:10+02:00"
audit-status: "complete"
audit-date: "2026-07-27T09:40:10+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-17.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Publication et distribution

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 16 possède les presets, exports, signatures, packages, manifestes et octets fermés. Le présent chapitre possède la préparation d’une présence de distribution, la corrélation entre produit et build candidat, les informations remises aux plateformes, la revue, le lancement initial et l’organisation du support.

Publier ne signifie ni exporter ni corriger un produit déjà distribué. Les fonctions d’accessibilité du produit complet restent au chapitre 18, la localisation au chapitre 19, les correctifs et retours arrière au chapitre 20, et l’archivage de fin de vie au chapitre 22.

Le niveau de preuve reste `static-review`. Aucun compte, page boutique, prix réel, formulaire, classification, téléversement, soumission, approbation, vente ou lancement public de `Project Asteria` n’est revendiqué.

### 1.1 Contrat contrôlé

> **[LECTURE] Contrôle 01 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-01
version: 1
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-01` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[VSC] Contrôle 02 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-02
version: 2
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-02` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer build candidat, artefact, canal, offre, fiche produit, soumission, approbation et publication ;
- préparer des descriptions, médias et déclarations reliés à des preuves ;
- organiser Steam, Epic Games Store, itch.io, Google Play, Apple App Store et distribution directe sans figer les portails ;
- gouverner prix candidats, territoires, classifications, confidentialité, clés, canaux, revue et support ;
- exécuter un dry-run documentaire sans téléverser ni publier ;
- diagnostiquer dix erreurs fréquentes de publication.

### 2.1 Contrat contrôlé

> **[PS] Contrôle 03 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-03
version: 3
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-03` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[CMD] Contrôle 04 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-04
version: 1
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-04` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 3. Niveau de preuve et réserves

Cette section définit le contrat de publication associé à « niveau de preuve et réserves ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 01.

### 3.1 Contrat contrôlé

> **[WSL] Contrôle 05 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-05
version: 2
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-05` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[DCT] Contrôle 06 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-06
version: 3
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-06` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 4. Prérequis et frontières

Cette section définit le contrat de publication associé à « prérequis et frontières ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 02.

### 4.1 Contrat contrôlé

> **[DCK] Contrôle 07 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-07
version: 1
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-07` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[WEB] Contrôle 08 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-08
version: 2
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-08` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 5. Vocabulaire opérationnel

Cette section définit le contrat de publication associé à « vocabulaire opérationnel ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 03.

### 5.1 Contrat contrôlé

> **[APP] Contrôle 09 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-09
version: 3
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-09` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[SORTIE] Contrôle 10 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-10
version: 1
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-10` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 6. Séparer export, distribution et publication

Cette section définit le contrat de publication associé à « séparer export, distribution et publication ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 04.

### 6.1 Contrat contrôlé

> **[LECTURE] Contrôle 11 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-11
version: 2
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-11` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[VSC] Contrôle 12 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-12
version: 3
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-12` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 7. Construire le dossier de publication

Cette section définit le contrat de publication associé à « construire le dossier de publication ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 05.

### 7.1 Contrat contrôlé

> **[PS] Contrôle 13 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-13
version: 1
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-13` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[CMD] Contrôle 14 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-14
version: 2
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-14` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 8. Établir la source de vérité produit

Cette section définit le contrat de publication associé à « établir la source de vérité produit ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 06.

### 8.1 Contrat contrôlé

> **[WSL] Contrôle 15 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-15
version: 3
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-15` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[DCT] Contrôle 16 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-16
version: 1
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-16` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 9. Définir la matrice des canaux

Cette section définit le contrat de publication associé à « définir la matrice des canaux ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 07.

### 9.1 Contrat contrôlé

> **[DCK] Contrôle 17 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-17
version: 2
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-17` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[WEB] Contrôle 18 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-18
version: 3
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-18` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 10. Gouverner les identités de boutique

Cette section définit le contrat de publication associé à « gouverner les identités de boutique ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 08.

### 10.1 Contrat contrôlé

> **[APP] Contrôle 19 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-19
version: 1
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-19` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[SORTIE] Contrôle 20 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-20
version: 2
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-20` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 11. Préparer les descriptions produit

Cette section définit le contrat de publication associé à « préparer les descriptions produit ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 09.

### 11.1 Contrat contrôlé

> **[LECTURE] Contrôle 21 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-21
version: 3
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-21` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[VSC] Contrôle 22 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-22
version: 1
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-22` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 12. Relier les affirmations aux preuves

Cette section définit le contrat de publication associé à « relier les affirmations aux preuves ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 10.

### 12.1 Contrat contrôlé

> **[PS] Contrôle 23 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-23
version: 2
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-23` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[CMD] Contrôle 24 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-24
version: 3
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-24` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 13. Préparer capsules, captures et bandes-annonces

Cette section définit le contrat de publication associé à « préparer capsules, captures et bandes-annonces ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 11.

### 13.1 Contrat contrôlé

> **[WSL] Contrôle 25 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-25
version: 1
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-25` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[DCT] Contrôle 26 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-26
version: 2
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-26` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 14. Documenter les exigences de médias

Cette section définit le contrat de publication associé à « documenter les exigences de médias ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 12.

### 14.1 Contrat contrôlé

> **[DCK] Contrôle 27 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-27
version: 3
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-27` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[WEB] Contrôle 28 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-28
version: 1
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-28` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 15. Définir les métadonnées techniques

Cette section définit le contrat de publication associé à « définir les métadonnées techniques ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 13.

### 15.1 Contrat contrôlé

> **[APP] Contrôle 29 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-29
version: 2
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-29` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[SORTIE] Contrôle 30 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-30
version: 3
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-30` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 16. Préparer les classifications d’âge

Cette section définit le contrat de publication associé à « préparer les classifications d’âge ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 14.

### 16.1 Contrat contrôlé

> **[LECTURE] Contrôle 31 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-31
version: 1
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-31` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.

> **[VSC] Contrôle 32 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-32
version: 2
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-32` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 17. Préparer confidentialité et données

Cette section définit le contrat de publication associé à « préparer confidentialité et données ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 15.

### 17.1 Contrat contrôlé

> **[PS] Contrôle 33 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-33
version: 3
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-33` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 18. Définir le prix candidat

Cette section définit le contrat de publication associé à « définir le prix candidat ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 16.

### 18.1 Contrat contrôlé

> **[CMD] Contrôle 34 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-34
version: 1
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-34` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 19. Gérer territoires, taxes et devises

Cette section définit le contrat de publication associé à « gérer territoires, taxes et devises ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 17.

### 19.1 Contrat contrôlé

> **[WSL] Contrôle 35 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-35
version: 2
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-35` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 20. Préparer Steam

Cette section définit le contrat de publication associé à « préparer steam ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 18.

### 20.1 Contrat contrôlé

> **[DCT] Contrôle 36 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-36
version: 3
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-36` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 21. Préparer Epic Games Store

Cette section définit le contrat de publication associé à « préparer epic games store ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 19.

### 21.1 Contrat contrôlé

> **[DCK] Contrôle 37 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-37
version: 1
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-37` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 22. Préparer itch.io

Cette section définit le contrat de publication associé à « préparer itch.io ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 20.

### 22.1 Contrat contrôlé

> **[WEB] Contrôle 38 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-38
version: 2
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-38` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 23. Préparer Google Play

Cette section définit le contrat de publication associé à « préparer google play ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 21.

### 23.1 Contrat contrôlé

> **[APP] Contrôle 39 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-39
version: 3
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-39` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 24. Préparer Apple App Store

Cette section définit le contrat de publication associé à « préparer apple app store ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 22.

### 24.1 Contrat contrôlé

> **[SORTIE] Contrôle 40 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-40
version: 1
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-40` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 25. Préparer les canaux directs

Cette section définit le contrat de publication associé à « préparer les canaux directs ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 23.

### 25.1 Contrat contrôlé

> **[LECTURE] Contrôle 41 — Adapter aux données réellement approuvées.**

```bash
schema: asteria-publication-41
version: 2
owner: role-6
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-41` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 26. Gérer clés, codes et accès

Cette section définit le contrat de publication associé à « gérer clés, codes et accès ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 24.

### 26.1 Contrat contrôlé

> **[VSC] Contrôle 42 — Adapter aux données réellement approuvées.**

```text
schema: asteria-publication-42
version: 3
owner: role-7
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-42` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 27. Séparer canaux internes, fermés et publics

Cette section définit le contrat de publication associé à « séparer canaux internes, fermés et publics ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 25.

### 27.1 Contrat contrôlé

> **[PS] Contrôle 43 — Adapter aux données réellement approuvées.**

```yaml
schema: asteria-publication-43
version: 1
owner: role-1
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-43` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 28. Préparer les builds candidats

Cette section définit le contrat de publication associé à « préparer les builds candidats ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 26.

### 28.1 Contrat contrôlé

> **[CMD] Contrôle 44 — Adapter aux données réellement approuvées.**

```json
schema: asteria-publication-44
version: 2
owner: role-2
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-44` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 29. Construire les notes de version

Cette section définit le contrat de publication associé à « construire les notes de version ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 27.

### 29.1 Contrat contrôlé

> **[WSL] Contrôle 45 — Adapter aux données réellement approuvées.**

```markdown
schema: asteria-publication-45
version: 3
owner: role-3
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-45` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 30. Planifier le calendrier de lancement

Cette section définit le contrat de publication associé à « planifier le calendrier de lancement ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 28.

### 30.1 Contrat contrôlé

> **[DCT] Contrôle 46 — Adapter aux données réellement approuvées.**

```powershell
schema: asteria-publication-46
version: 1
owner: role-4
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-46` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 31. Préparer la revue de conformité

Cette section définit le contrat de publication associé à « préparer la revue de conformité ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 29.

### 31.1 Contrat contrôlé

> **[DCK] Contrôle 47 — Adapter aux données réellement approuvées.**

```bat
schema: asteria-publication-47
version: 2
owner: role-5
status: candidate
evidence_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-47` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 32. Exécuter un dry-run de soumission

Cette section définit le contrat de publication associé à « exécuter un dry-run de soumission ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 30.

### 32.1 Contrat contrôlé

> **[WEB] Contrôle 48 — Adapter aux données réellement approuvées.**

```bash
control=48
result=candidate
runtime_claimed=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-48` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 33. Gérer les retours de revue

Cette section définit le contrat de publication associé à « gérer les retours de revue ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 31.

### 33.1 Contrat contrôlé

> **[APP] Contrôle 49 — Adapter aux données réellement approuvées.**

```text
control=49
result=candidate
runtime_claimed=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-49` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 34. Préparer le lancement initial

Cette section définit le contrat de publication associé à « préparer le lancement initial ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 32.

### 34.1 Contrat contrôlé

> **[SORTIE] Contrôle 50 — Adapter aux données réellement approuvées.**

```yaml
control=50
result=candidate
runtime_claimed=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-50` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 35. Préparer le support de lancement

Cette section définit le contrat de publication associé à « préparer le support de lancement ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 33.

### 35.1 Contrat contrôlé

> **[LECTURE] Contrôle 51 — Adapter aux données réellement approuvées.**

```json
control=51
result=candidate
runtime_claimed=false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `asteria-publication-51` distingue le contrat des noms d’interface.
- **Statut :** `candidate` interdit de présenter l’exemple comme une configuration active.
- **Propriétaire :** le rôle désigné prépare la donnée ; l’approbateur reste séparé lorsque le risque le justifie.
- **Preuve :** `evidence_required` relie la déclaration à un document, un média ou un build vérifiable.
- **Résultat attendu :** le contrôle produit une décision traçable sans publier automatiquement.


## 36. Observer sans confondre métrique et décision

Cette section définit le contrat de publication associé à « observer sans confondre métrique et décision ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 34.

### 36.1 Contrat contrôlé


## 37. Préparer communication et incidents

Cette section définit le contrat de publication associé à « préparer communication et incidents ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 35.

### 37.1 Contrat contrôlé


## 38. Organiser les responsabilités

Cette section définit le contrat de publication associé à « organiser les responsabilités ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 36.

### 38.1 Contrat contrôlé


## 39. Mode Solo et Mode Studio

Cette section définit le contrat de publication associé à « mode solo et mode studio ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 37.

### 39.1 Contrat contrôlé


## 40. Critère d’acceptation documentaire

Cette section définit le contrat de publication associé à « critère d’acceptation documentaire ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 38.

## 41. Checklist opérationnelle

Cette section définit le contrat de publication associé à « checklist opérationnelle ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 39.

## 42. Statuts, retours et preuves

Cette section définit le contrat de publication associé à « statuts, retours et preuves ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 40.

## 43. Diagnostics et corrections

<!-- qa:error-correction-section -->
Cette section définit le contrat de publication associé à « diagnostics et corrections ». La procédure privilégie des identifiants stables, des preuves nommées et des décisions humaines réversibles.

Les valeurs et statuts présentés sont des candidats documentaires. Ils ne deviennent des faits de production qu’après vérification dans le portail, corrélation avec les octets qualifiés et conservation d’un reçu pour le contrôle éditorial 41.
### 43.1 Reconstruire le package pendant la soumission

**Symptôme ou risque :** Le build envoyé ne correspond plus au manifeste approuvé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
submission:
  source: rebuilt-after-review
  same_bytes: false
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
submission:
  source: approved-artifact
  same_bytes: true
  digest_verified: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.2 Confondre build présent et produit publié

**Symptôme ou risque :** L’équipe annonce une sortie alors que le portail indique seulement un téléversement.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
build_uploaded: true
review_submitted: false
public_release: assumed
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
build_uploaded: true
review_submitted: false
public_release: false
status_label: uploaded-only
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.3 Publier une affirmation non démontrée

**Symptôme ou risque :** La fiche promet une fonctionnalité absente du candidat.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
claim: seamless-offline-coop
evidence: none
publish: true
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
claim: offline-single-player
evidence: test-report-042
publish: candidate
review_required: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.4 Versionner un credential de boutique

**Symptôme ou risque :** Un jeton de publication est enregistré dans le dépôt.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
credential_source: repository
token: plaintext-placeholder
logging: enabled
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
credential_source: protected-secret
token: omitted
logging: redacted
rotation: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.5 Réutiliser une classification obsolète

**Symptôme ou risque :** La version publiée contient un contenu différent de la version évaluée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
rating_source_version: 14
release_content_version: 17
review: skipped
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
rating_source_version: 17
release_content_version: 17
review: completed
receipt: retained
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.6 Traiter un canal fermé comme public

**Symptôme ou risque :** Les testeurs internes sont comptés comme lancement commercial.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
channel: closed-test
audience: allowlist
public_launch: true
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
channel: closed-test
audience: allowlist
public_launch: false
external_visibility: restricted
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.7 Générer des clés sans gouvernance

**Symptôme ou risque :** Des clés sont créées sans lot ni révocation.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
key_batch: none
quantity: unlimited
owner: unknown
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
key_batch: AST-KEY-2026-001
quantity: 100
owner: release-ops
purpose: press-review
revocation: available
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.8 Figer des exigences de portail

**Symptôme ou risque :** Une capture ancienne devient la seule procédure.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
requirements_source: screenshot
verified_at: unknown
portal_check: skipped
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
requirements_source: official-docs
verified_at: 2026-07-27
portal_check: required
change_log: retained
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.9 Déployer un prix pédagogique

**Symptôme ou risque :** Le montant d’exemple est traité comme décision commerciale.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
display_price: 19,99 €
currency: EUR
approval: assumed
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
display_price: 19,99 €
currency: EUR
status: candidate-only
approval: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

### 43.10 Clore un rejet sans nouvelle tentative

**Symptôme ou risque :** La même identité de soumission masque la correction.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
submission_id: AST-SUB-001
result: rejected
retry_overwrites: true
runtime_claimed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le contrat perd la corrélation entre état réel, preuve et décision publiée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au portail réel.**

```yaml
submission_id: AST-SUB-002
depends_on: AST-SUB-001
result: candidate
retry_overwrites: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les états, identités et preuves sont séparés avant toute décision publique.

































































































































































































































































































































































































































































































































































































































## 44. Références techniques officielles

- [Steamworks — Store Presence](https://partner.steamgames.com/doc/store)
- [Steamworks — Review Process](https://partner.steamgames.com/doc/store/Review_Process)
- [Steamworks — Graphical Assets](https://partner.steamgames.com/doc/store/assets)
- [Epic Games Store — Publishing Tools Workflow](https://dev.epicgames.com/docs/epic-games-store/publishing-tools/publishing-process/publishing-workflow)
- [Epic Games Store — Release Management](https://dev.epicgames.com/docs/epic-games-store/publishing-tools/publishing-process/release-management)
- [itch.io — Your first project page](https://itch.io/docs/creators/getting-started)
- [itch.io — Uploading HTML5 games](https://itch.io/docs/creators/html5)
- [Google Play Console — Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152)
- [Google Play Console — Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348)
- [Apple Developer — App Store Connect Help](https://developer.apple.com/help/app-store-connect/)
- [IARC — International Age Rating Coalition](https://www.globalratings.com/)

Les dimensions, délais, champs et règles de portail sont revérifiés contre la documentation officielle au moment de la matérialisation. Le chapitre conserve des contrats stables plutôt qu’une capture figée d’une interface susceptible d’évoluer.

## 45. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` adopte un dossier de publication versionné qui relie chaque affirmation, média, classification, déclaration et note de version à une preuve ou à un build candidat identifié.

Les plateformes et canaux sont décrits dans une matrice de distribution. Chaque entrée possède propriétaire, identité externe, territoires, profil de build, statut de revue, politique de clés, support et procédure d’arrêt. Les credentials restent hors dépôt et hors journaux.

Le prix pédagogique candidat utilise `19,99 €` et `currency: EUR`; il ne constitue ni décision commerciale ni tarif observé. Les taxes, arrondis, territoires et devises sont vérifiés dans les portails réels avant toute activation.

La soumission utilise exactement les octets qualifiés au chapitre 16. Présence d’un build, envoi en revue, approbation et publication publique restent quatre états distincts. Un rejet conserve son rapport et produit une nouvelle tentative identifiée.

Tant que comptes, pages, médias, classifications, formulaires, clés, téléversements, revues et support n’ont pas été matérialisés, aucune publication ou distribution publique de `Project Asteria` n’est revendiquée.
