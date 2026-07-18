---
title: "Rapport QA final du Volume 0"
id: "DOC-V0-QA-FINAL"
status: "complete"
version: "1.0.0"
volume: "Volume 0"
category: "quality-report"
validation-date: "2026-07-18"
---

# Rapport QA final du Volume 0

## 1. Décision

**Validation réussie.** Le contenu normatif du Volume 0, ses annexes initiales et la chaîne de construction documentaire satisfont les contrôles définis pour le milestone M1.

Le Volume 0 peut être considéré comme **terminé**. Cette décision ne vaut pas autorisation de publication officielle de la collection complète : la licence globale du projet doit encore être définie avant toute distribution publique versionnée.

## 2. Exécution de référence

| Élément | Valeur |
|---|---|
| Workflow | `Validate Volume 0` |
| Exécution | `29635317000` |
| Résultat | `success` |
| Branche de contrôle | `qa/validate-volume0` |
| Commit contrôlé | `21f422559d4b90971363280414d0b54b4b679258` |
| Date | 18 juillet 2026 |

Toutes les étapes du workflow ont réussi :

- installation de la chaîne documentaire ;
- contrôle structurel ;
- compilation Pandoc et XeLaTeX ;
- inspection technique du PDF ;
- publication des artefacts de validation.

## 3. Résultats du contrôle structurel

| Mesure | Résultat |
|---|---:|
| Sources déclarées dans `contents.txt` | 27 |
| Identifiants uniques détectés | 26 |
| Erreurs bloquantes | 0 |
| Avertissements | 1 |

Le validateur accepte les champs d’identification `id` et l’alias historique `identifier`. Aucun doublon d’identifiant, lien local cassé, fichier source absent, front matter invalide ou marqueur de conflit Git n’a été détecté.

## 4. Avertissement restant

La métadonnée globale de licence contient encore la valeur :

```yaml
license: "À définir avant publication"
```

Cet avertissement n’empêche pas la clôture du milestone documentaire M1. Il reste toutefois **bloquant pour une publication officielle** ou une redistribution accompagnée d’une version stable.

## 5. Résultats de compilation

| Propriété | Résultat |
|---|---|
| Format | PDF 1.5 |
| Taille de page | A4 |
| Nombre de pages | 214 |
| Taille du fichier | 583 761 octets |
| Moteur | XeLaTeX via Pandoc |
| Producteur | `xdvipdfmx` |
| Titre PDF | Guide réaliste de création de jeux vidéo 3D avec IA locale |
| Auteur | Laurent Collin |
| Chiffrement | aucun |
| JavaScript embarqué | aucun |

Le texte a été extrait avec succès par `pdftotext`, ce qui confirme que le livrable n’est pas une simple image et que son contenu principal reste sélectionnable et indexable.

## 6. Corrections appliquées pendant la validation

La validation a permis de corriger ou renforcer les éléments suivants :

1. prise en charge de l’alias historique `identifier` du chapitre 1 ;
2. installation de `lmodern`, nécessaire à la compilation LaTeX ;
3. installation de `librsvg2-bin` pour convertir les ressources SVG ;
4. conservation du journal Pandoc dans les artefacts ;
5. ajout du filtre `filters/pdf-normalize.lua` ;
6. restauration forcée du titre et de l’auteur globaux du PDF ;
7. suppression, dans le livrable PDF, de trois pictogrammes absents des polices DejaVu ;
8. alignement des scripts `build.sh` et `build.ps1`.

## 7. Contrôle visuel

Un échantillon représentatif a été rendu en images aux pages suivantes :

```text
1 à 5, 50, 100, 150, 200 et 214
```

Les vérifications réalisées n’ont révélé aucun :

- texte rogné ;
- chevauchement majeur ;
- carré noir ou glyphe manquant visible ;
- défaut de rotation ;
- changement de format de page ;
- titre de couverture incorrect ;
- tableau manifestement illisible dans l’échantillon.

La table des matières, les pages de texte courant, les blocs de code et les tableaux examinés restent lisibles.

## 8. Artefacts produits

L’artefact GitHub Actions `volume-0-validation` contient :

```text
Guide-IA-GameDev.pdf
Guide-IA-GameDev.txt
QA-Volume-0.md
PANDOC-BUILD.log
PDF-INFO.txt
```

Les artefacts de cette exécution sont conservés pendant quatorze jours par le workflow. Le PDF n’est pas versionné dans Git : il reste un livrable généré à partir des sources Markdown.

## 9. Critères de clôture M1

- [x] Onze chapitres principaux rédigés.
- [x] Sept annexes normatives initiales créées.
- [x] Référentiel d’assurance qualité créé.
- [x] Sources déclarées présentes.
- [x] Métadonnées analysables.
- [x] Identifiants sans doublon.
- [x] Liens Markdown locaux valides.
- [x] Compilation Pandoc réussie.
- [x] PDF A4 généré.
- [x] Texte du PDF extractible.
- [x] Métadonnées PDF globales corrigées.
- [x] Contrôle visuel d’un échantillon réparti dans le document.
- [x] Chaîne Windows et Unix alignée.
- [ ] Licence globale définie avant publication officielle.

## 10. Conclusion

Le milestone **M1 — Volume 0 : Fondation documentaire** est clôturé. La prochaine phase active est **M2 — Livre I : Préparer la plateforme**, en commençant par le matériel, Windows, les pilotes AMD et les voies d’accélération compatibles.
