---
title: "Audit — Livre V, fiche 25 : Licences, provenance et conformité"
id: "DOC-L5-QA-AUDIT-CH25"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 25
last-verified: "2026-07-30T00:17:00+02:00"
audit-date: "2026-07-30T00:17:00+02:00"
audit-level: "static-review"
validated-document: "Livre-V/CHAPITRE-25-Licences-provenance-et-conformite.md"
validation-profile: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 25 — Licences, provenance et conformité

## 1. Décision

**Décision : accepté au niveau `static-review`, avec réserves explicites sur toute qualification juridique, compatibilité de licences, titularité, consentement, conformité réglementaire et licence globale de collection.**

La fiche respecte le profil spécialisé du Livre V : consultation non linéaire, cartes et matrices, sources officielles datées, renvois vers les propriétaires et absence d’avis juridique ou de registre réel présenté comme validé.

## 2. Périmètre audité

L’audit couvre :

- le contrat de qualification d’un objet et d’un usage ;
- la séparation entre code, documentation, modèles, poids, datasets, assets, audio, polices, services, personnes et sorties ;
- l’identité, la version, les opérations, le périmètre, les preuves et l’expiration ;
- les identifiants SPDX, expressions et `LicenseRef` ;
- les droits, obligations, restrictions et questions bloquantes ;
- le routage vers le Volume 0 et les Livres II à IV ;
- la provenance, les transformations et les paquets de preuves ;
- les personnes, consentements, données, voix, visages et mocap ;
- les chaînes IA, services, entrées, sorties et contribution humaine ;
- la redistribution, les dépendances transitives et les analyses de compatibilité ;
- les statuts, déclarations permises et formulations interdites ;
- les notices, attributions, offres de source, SBOM et paquets de publication ;
- les vues Solo et Studio ;
- les exceptions, escalades, changements, incidents, retraits et requalifications ;
- la future décision de licence globale de la collection ;
- les sources officielles SPDX, REUSE, OSI, Creative Commons, Légifrance, CNIL et Union européenne.

L’audit ne qualifie aucun objet réel, ne choisit aucune licence et ne rend aucun avis juridique.

## 3. Métriques statiques

| Mesure | Valeur finale |
|---|---:|
| lignes du chapitre | 584 |
| titres Markdown | 34 |
| cartes `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 77 |
| renvois vers les Livres I à IV | 35 |
| liens avec fragment | 55 |
| diagrammes compacts | 9 |
| blocs clôturés | 0 |
| titres dupliqués | 0 |

## 4. Conformité au profil Livre V

| Exigence | Résultat | Observation |
|---|---|---|
| chemin canonique et identifiant stable | conforme | `DOC-L5-CH25` et chemin officiel du plan maître |
| front matter, version, date et audit | conforme | version `1.0.0`, preuve `static-review`, cadre France/UE |
| format `reference-cards` | conforme | cartes et matrices marquées |
| consultation non linéaire | conforme | index express et identifiants `LIC-*` |
| réponse rapide et limites | conforme | chaque carte substantive contient décision, porte ou limite |
| liens vers les propriétaires | conforme | Volume 0 et Livres II à IV reliés sans duplication longue |
| sources officielles datées | conforme | autorités primaires ou institutionnelles vérifiées le 30 juillet 2026 |
| séparation documentaire/juridique | conforme | aucune conclusion juridique automatisée ou personnalisée |
| absence de PDF intermédiaire | conforme | aucune chaîne PDF appelée |
| lot permanent de huit fichiers | conforme | contrôle automatisé dans le workflow de finalisation |

## 5. Couverture du plan maître

| Objectif du plan | Couverture |
|---|---|
| résumer licences du texte, code, modèles et assets | matrice A, `LIC-03`, `LIC-06` et `LIC-12` |
| documenter provenance, consentement et redistribution | `LIC-04`, `LIC-05` et `LIC-07` |
| fournir matrices et modèles de registre | matrices A à C et contrat `LIC-00` |
| signaler besoins de conseil professionnel | `LIC-10` et frontières finales |
| fournir fiches de licences | `LIC-00` à `LIC-03` |
| fournir un registre | `LIC-01`, `LIC-02` et matrice B |
| fournir des modèles d’attribution | `LIC-08` |
| fournir une checklist de publication | `LIC-08`, matrice C et renvoi vers la fiche 24 |
| ne pas constituer un avis juridique | principe, statuts, limites et réserves |
| valider par cohérence et sources officielles | `LIC-02`, `LIC-05`, `LIC-06`, `LIC-10` et `LIC-12` |

## 6. Contrats structurants vérifiés

### 6.1 Objets séparés

La fiche interdit qu’une licence de code prouve automatiquement les droits sur :

- les poids et adaptations ;
- les datasets et entrées ;
- les sorties générées ;
- les assets, polices, musiques et voix ;
- les personnes, marques et services ;
- la documentation et les captures.

### 6.2 Usage et périmètre

Chaque décision doit nommer :

- l’objet et sa version ;
- l’opération prévue ;
- le produit, le canal et la plateforme ;
- le territoire, la durée et le public ;
- les obligations et restrictions ;
- les preuves, propriétaires et approbateurs ;
- les dépendances et l’expiration.

### 6.3 Statuts honnêtes

`unknown`, `NOASSERTION`, `under_review`, `stale`, `contested` et `blocked` ne permettent aucune déclaration de publication autorisée. Les statuts `approved_*` restent bornés au périmètre réellement revu.

### 6.4 Automatisation limitée

Les outils peuvent vérifier structure, présence, versions, expressions, relations, notices et contenu d’un package. Ils ne peuvent pas :

- déterminer une titularité ;
- interpréter définitivement un contrat ;
- décider une compatibilité universelle ;
- conclure à la conformité RGPD ou AI Act ;
- remplacer l’autorité humaine ou professionnelle adaptée.

### 6.5 Licence globale non décidée

La fiche maintient explicitement le chantier de licence globale ouvert. Elle distingue texte, code, exemples, médias, Companion Pack, Project Asteria, contributions, marques et données confidentielles avant toute décision future.

## 7. Sources officielles

Les références externes ont été revues le 30 juillet 2026 :

- SPDX Specifications et SPDX License List ;
- REUSE Specification 3.3 ;
- Open Source Definition et licences approuvées OSI ;
- licences Creative Commons ;
- article L131-3 du Code de la propriété intellectuelle sur Légifrance ;
- principes de protection des données présentés par la CNIL ;
- règlement (UE) 2024/1689 sur EUR-Lex et calendrier officiel de mise en œuvre.

La fiche présente les sources réglementaires comme volatiles et exige une nouvelle vérification selon la date, le rôle et le produit.

## 8. Réserves

- aucun composant, modèle, dataset, asset, contrat, consentement ou service réel n’a été qualifié ;
- aucune compatibilité de licences n’a été décidée ;
- aucune titularité, base juridique, juridiction ou applicabilité réglementaire n’a été déterminée ;
- aucun registre de production, SBOM, notice, offre de source ou paquet de preuves n’a été créé ;
- aucune donnée personnelle, voix, image, signature, contrat ou information confidentielle n’a été traitée ;
- aucune exception, approbation, signature ou revue professionnelle n’a été émise ;
- aucune licence globale n’a été choisie ;
- aucun outil du Companion Pack et aucun PDF n’ont été produits.

## 9. Conclusion

La fiche 25 est conforme au plan maître et au protocole du Livre V au niveau `static-review`. Elle peut être intégrée comme couche de référence transversale, sous réserve que toute décision réelle s’appuie sur les textes applicables, les preuves du projet et une autorité compétente.
