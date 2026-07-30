---
title: "Clôture technique et PDF — Livre V"
id: "DOC-L5-QA-CLOSURE"
status: "in-progress"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-30T02:04:00+02:00"
audit-level: "static-review+pdf-inspection-pending"
target-book: "Livre V"
---

# Clôture technique et PDF — Livre V

## 1. Décision préparatoire

La couverture documentaire du Livre V est complète : 26 fiches sur 26 sont rédigées et auditées au niveau `static-review`. La présente campagne doit encore compiler le PDF cumulatif, exécuter le préflight structurel, vérifier la présence des 26 fiches dans le texte extrait et inspecter visuellement un échantillon représentatif avec deux moteurs de rendu.

Aucune décision de clôture technique n’est rendue avant la réussite documentée de ces contrôles.

## 2. Périmètre

- `Livre-V/index.md` et les 26 fiches inscrites dans `contents.txt` ;
- audits et preuves QA de fiches, qui doivent rester exclus du PDF lecteur ;
- validation documentaire transversale et contrôle des liens profonds du Livre V ;
- chaîne `build.sh` → Pandoc → XeLaTeX → PDF cumulatif ;
- préflight `qpdf`, `pdfinfo`, `pdffonts` et extraction textuelle ;
- cartographie des pages d’ouverture et inspection visuelle représentative ;
- transition de M6 vers M7 uniquement après réussite de la porte PDF.

## 3. Réserves permanentes

La campagne ne constitue ni une validation runtime, ni une décision de licence globale, ni une publication commerciale. Les formats HTML/EPUB, le balisage avancé d’accessibilité et les outils exécutables du Companion Pack restent des chantiers séparés.

## 4. État

**Candidat PDF final déclenché avec cartographie séquentielle des pages réelles du Livre V.**
