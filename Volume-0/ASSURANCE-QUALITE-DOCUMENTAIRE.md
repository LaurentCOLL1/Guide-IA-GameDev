---
title: "Assurance qualité documentaire"
id: "DOC-V0-QA"
status: "complete"
version: "1.1.0"
volume: "Volume 0"
category: "normative"
---

# Assurance qualité documentaire

## 1. Objet

Ce document définit le système d’assurance qualité applicable à l’ensemble du **Guide IA GameDev**, à ses annexes et au Companion Pack.

L’objectif n’est pas seulement de produire des fichiers Markdown valides. La documentation doit également être :

- correcte sur le plan technique ;
- compréhensible par le public visé ;
- reproductible sur la configuration matérielle de référence ;
- cohérente entre les volumes ;
- traçable ;
- compatible avec la chaîne Pandoc ;
- maintenable dans le temps ;
- conforme aux licences et aux règles de sécurité du projet.

Les exigences de ce document sont **obligatoires** pour toute publication officielle.

## 2. Périmètre

Le contrôle qualité couvre :

- les fichiers Markdown ;
- les métadonnées YAML ;
- les liens internes et externes ;
- les identifiants documentaires ;
- les blocs de code et commandes ;
- les images, tableaux et diagrammes ;
- les références bibliographiques ;
- les annexes et index ;
- les scripts du Companion Pack ;
- les workflows ComfyUI ;
- les projets Godot et Blender de démonstration ;
- les fichiers générés pour publication ;
- les licences, crédits et obligations de redistribution.

## 3. Principes de qualité

### 3.1 La source fait autorité

Le Markdown versionné dans Git constitue la source de vérité documentaire.

Un PDF, un site HTML ou un document bureautique généré ne doit jamais devenir une source éditée manuellement.

### 3.2 Toute affirmation vérifiable doit pouvoir être contrôlée

Une affirmation technique dépendante d’une version, d’un outil, d’un pilote ou d’un modèle doit indiquer suffisamment de contexte pour être reproduite.

Cela peut inclure :

- la version du logiciel ;
- la version du pilote ;
- le système d’exploitation ;
- le modèle matériel ;
- le commit ou tag testé ;
- le profil de configuration ;
- la date de vérification.

### 3.3 Une procédure doit produire un résultat observable

Une procédure n’est considérée comme valide que si elle contient :

1. les prérequis ;
2. les étapes ;
3. le résultat attendu ;
4. une méthode de vérification ;
5. une voie de diagnostic en cas d’échec.

### 3.4 La qualité précède la publication

Une publication ne doit pas contourner un contrôle bloquant pour respecter une date arbitraire.

## 4. Niveaux de contrôle

Le processus est divisé en six portes qualité.

| Porte | Nom | Objectif | Nature |
|---|---|---|---|
| Q0 | Intégrité du fichier | Vérifier l’existence, l’encodage et la structure minimale | Automatique |
| Q1 | Conformité Markdown | Vérifier la syntaxe et les conventions éditoriales | Automatique et manuelle |
| Q2 | Cohérence documentaire | Vérifier identifiants, liens, index et absence de doublons | Automatique et manuelle |
| Q3 | Validation technique | Vérifier les commandes, exemples, workflows et résultats | Manuelle et automatisée |
| Q4 | Conformité juridique et sécurité | Vérifier licences, crédits, données et risques | Manuelle |
| Q5 | Validation de publication | Vérifier la compilation et les livrables finaux | Automatique et manuelle |

Toutes les portes applicables doivent être franchies avant une publication officielle.

## 5. Gravité des non-conformités

### Bloquante

Une erreur bloquante interdit la publication.

Exemples :

- compilation impossible ;
- lien vers un fichier obligatoire absent ;
- commande destructive non signalée ;
- secret ou donnée personnelle présent dans le dépôt ;
- licence incompatible ou inconnue pour un élément redistribué ;
- identifiant dupliqué ;
- procédure principale manifestement non fonctionnelle.

### Majeure

Une erreur majeure doit être corrigée avant une version stable.

Exemples :

- résultat attendu manquant ;
- version technique ambiguë ;
- contradiction entre deux chapitres ;
- exemple incomplet ;
- index important non mis à jour ;
- solution de repli absente pour la configuration de référence.

### Mineure

Une erreur mineure peut être corrigée dans une révision proche si elle ne dégrade pas l’usage principal.

Exemples :

- formulation imprécise ;
- faute typographique ;
- format de tableau incohérent ;
- lien externe utile mais non essentiel indisponible.

### Suggestion

Une suggestion améliore le document sans corriger une non-conformité.

## 6. Contrôles automatiques obligatoires

## 6.1 Encodage et fichiers

Vérifier que :

- les fichiers texte utilisent UTF-8 ;
- aucun fichier temporaire ou secret n’est versionné ;
- aucun nom de fichier ne contient de caractère interdit par la convention ;
- les chemins référencés respectent la casse réelle ;
- les fichiers générés restent dans les répertoires prévus ;
- aucune ressource obligatoire n’est vide.

## 6.2 Métadonnées YAML

Pour chaque document normatif ou chapitre, vérifier la présence et la validité de :

- `title` ;
- `id` ;
- `status` ;
- `version`.

Selon le type de document, vérifier également :

- `volume` ;
- `category` ;
- les informations de compatibilité ;
- la date de dernière validation.

Un identifiant doit être unique dans l’ensemble du dépôt.

## 6.3 Structure Markdown

Vérifier que :

- un seul titre de niveau 1 existe par document ;
- les niveaux de titres ne sautent pas de niveau sans justification ;
- les blocs de code sont fermés ;
- le langage des blocs de code est déclaré lorsque pertinent ;
- les tableaux sont syntaxiquement valides ;
- les listes sont cohérentes ;
- les espaces et lignes vides suivent les conventions du projet ;
- les ancres explicitement définies sont uniques.

## 6.4 Liens et références

Vérifier :

- les liens internes relatifs ;
- les liens vers images et annexes ;
- les références aux identifiants ;
- les entrées de `contents.txt` ;
- les liens des index de volume ;
- les références vers le Companion Pack ;
- les URL externes lorsque le contrôle réseau est disponible.

Un lien externe indisponible ne doit pas supprimer l’information essentielle du guide.

## 6.5 Doublons et cohérence

Rechercher :

- les identifiants dupliqués ;
- les titres dupliqués sans justification ;
- les procédures copiées dans plusieurs chapitres ;
- les définitions concurrentes d’un même terme ;
- les conventions contradictoires ;
- les versions incompatibles mentionnées comme simultanément recommandées.

## 6.6 Validation des fichiers structurés

Lorsque présents, valider syntaxiquement :

- JSON ;
- YAML ;
- TOML ;
- XML ;
- CSV ;
- fichiers Docker Compose ;
- fichiers de configuration Godot ;
- exports de workflows ComfyUI.

Une validation syntaxique ne remplace pas un test fonctionnel.

## 6.7 Recherche de secrets

Rechercher avant publication :

- clés API ;
- jetons GitHub ;
- mots de passe ;
- clés privées ;
- chaînes de connexion ;
- adresses internes sensibles ;
- données personnelles non nécessaires.

Les exemples doivent utiliser des valeurs factices immédiatement reconnaissables.

## 7. Contrôles manuels obligatoires

## 7.1 Relecture éditoriale

Le relecteur vérifie :

- la clarté de l’objectif ;
- la progression pédagogique ;
- la définition des termes ;
- l’absence d’ambiguïté dans les actions ;
- la présence d’un résultat attendu ;
- la séparation entre Obligatoire, Recommandé et Optionnel ;
- la pertinence des parcours Solo et Studio ;
- l’absence de promesses non démontrées.

## 7.2 Relecture technique

Le relecteur technique vérifie :

- les versions citées ;
- les prérequis ;
- les chemins de fichiers ;
- les commandes ;
- les paramètres ;
- les ports réseau ;
- les formats d’entrée et de sortie ;
- les limites matérielles ;
- les messages d’erreur et solutions de diagnostic ;
- la compatibilité avec le profil AMD de référence.

## 7.3 Relecture de sécurité

Vérifier :

- les privilèges demandés ;
- les commandes destructives ;
- les services exposés sur le réseau ;
- les permissions de fichiers ;
- la manipulation de contenus non fiables ;
- les actions exécutées par les agents IA ;
- les risques de fuite de données ;
- les procédures de sauvegarde et de restauration.

## 7.4 Relecture juridique

Vérifier :

- la licence de chaque composant redistribué ;
- les obligations d’attribution ;
- les restrictions d’usage commercial ;
- les restrictions applicables aux modèles et datasets ;
- la provenance des médias ;
- le droit d’utilisation des voix et ressemblances ;
- la présence des notices obligatoires.

Une licence inconnue est traitée comme bloquante tant qu’elle n’est pas clarifiée.

## 8. Validation des exemples techniques

Chaque exemple significatif reçoit un statut :

- **Non testé** ;
- **Test partiel** ;
- **Testé** ;
- **Testé sur la configuration de référence** ;
- **Déprécié**.

Une fiche de validation doit idéalement contenir :

```yaml
validation_id: VAL-EXAMPLE-0001
document_id: DOC-EXAMPLE
environment:
  os: Windows
  gpu: AMD Radeon RX 6750 XT 12GB
  cpu: Ryzen 7 2700
  ram: 32GB
status: tested
validated_at: YYYY-MM-DD
result: pass
notes: ""
```

## 9. Validation de la chaîne Pandoc

La porte Q5 exige au minimum :

1. la lecture complète de `contents.txt` ;
2. la présence de tous les fichiers listés ;
3. une compilation sans erreur bloquante ;
4. une table des matières correcte ;
5. une numérotation cohérente ;
6. l’affichage correct des accents et symboles ;
7. l’intégration correcte des images et tableaux ;
8. l’absence de débordement majeur dans le PDF ;
9. la vérification des liens du livrable ;
10. la conservation des sources indépendamment du livrable.

Les avertissements Pandoc doivent être enregistrés et triés. Un avertissement ignoré doit être justifié.

## 10. Rapport de contrôle

Chaque campagne de contrôle peut produire un rapport suivant ce modèle :

```markdown
# Rapport QA

- Version contrôlée :
- Commit contrôlé :
- Date :
- Responsable :
- Périmètre :

## Résultats

- Bloquantes : 0
- Majeures : 0
- Mineures : 0
- Suggestions : 0

## Portes qualité

- [ ] Q0 — Intégrité
- [ ] Q1 — Markdown
- [ ] Q2 — Cohérence
- [ ] Q3 — Technique
- [ ] Q4 — Juridique et sécurité
- [ ] Q5 — Publication

## Décision

- [ ] Accepté
- [ ] Accepté avec réserves
- [ ] Refusé
```

## 11. Traitement des non-conformités

Une non-conformité doit comporter :

- un identifiant ;
- une gravité ;
- le fichier concerné ;
- une description reproductible ;
- le résultat attendu ;
- le responsable de la correction ;
- le statut ;
- la preuve de résolution.

Cycle recommandé :

```text
Détectée → Confirmée → Assignée → Corrigée → Vérifiée → Fermée
```

Une erreur récurrente doit conduire à l’ajout ou à l’amélioration d’un contrôle automatique.

## 12. Modes Solo et Studio

### Mode Solo

Le même auteur peut rédiger, tester et valider, mais il doit séparer les étapes dans le temps et utiliser les checklists.

Minimum recommandé :

- une relecture différée ;
- une compilation propre ;
- une vérification des liens ;
- un test des commandes principales ;
- un rapport QA succinct.

### Mode Studio

Les rôles sont séparés autant que possible :

- auteur ;
- relecteur éditorial ;
- relecteur technique ;
- responsable sécurité ou juridique ;
- responsable de publication.

Une modification importante doit être revue par une personne différente de son auteur.

## 13. Checklist de validation d’un document

- [ ] Métadonnées YAML présentes et valides.
- [ ] Identifiant unique.
- [ ] Objectif et périmètre explicites.
- [ ] Structure de titres valide.
- [ ] Terminologie conforme au glossaire.
- [ ] Liens internes valides.
- [ ] Sources citées lorsque nécessaires.
- [ ] Versions et environnement précisés.
- [ ] Procédures reproductibles.
- [ ] Résultats attendus indiqués.
- [ ] Diagnostic prévu pour les échecs courants.
- [ ] Code et commandes relus.
- [ ] Risques et commandes destructives signalés.
- [ ] Licences et crédits vérifiés.
- [ ] Index concernés mis à jour.
- [ ] Compilation vérifiée.
- [ ] Audit post-création réalisé et rapport enregistré.
- [ ] Métadonnées `audit-status`, `audit-date`, `audit-report` et `audit-level` présentes lorsque requises.

## 13.1 Porte obligatoire après création d’un chapitre

À partir du Livre II, la rédaction et l’audit constituent deux étapes distinctes. Un chapitre ne peut être annoncé comme terminé qu’après :

1. comparaison au sommaire maître ;
2. recherche des notions fondamentales manquantes ;
3. relecture technique des commandes et exemples ;
4. vérification des sources et versions ;
5. correction des non-conformités ;
6. mise à jour de l’index, de la roadmap et de `contents.txt` ;
7. compilation CI réussie ;
8. enregistrement d’un rapport d’audit.

Le protocole détaillé du Livre II est défini dans `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`.

## 14. Critères de clôture du Volume 0

Le milestone M1 peut être déclaré terminé lorsque :

- les onze chapitres principaux sont présents ;
- les annexes normatives initiales sont présentes ;
- tous les documents sont inscrits dans `contents.txt` selon l’ordre prévu ;
- les identifiants sont uniques ;
- les liens internes essentiels sont valides ;
- les métadonnées sont cohérentes ;
- aucun secret n’est présent ;
- aucune non-conformité bloquante n’est ouverte ;
- la compilation complète réussit ;
- le PDF produit fait l’objet d’une vérification visuelle minimale ;
- la roadmap et le changelog reflètent l’état réel.

## 15. Évolution du dispositif

Cette norme constitue le socle initial. Les contrôles automatiques seront progressivement industrialisés dans le Companion Pack.

Les futurs scripts devront au minimum pouvoir contrôler :

- les métadonnées ;
- les identifiants ;
- les liens locaux ;
- les entrées de compilation ;
- les fichiers structurés ;
- les secrets courants ;
- les licences enregistrées ;
- les erreurs de compilation Pandoc.

Toute nouvelle famille de contenu doit définir ses propres contrôles avant d’être considérée comme stable.
