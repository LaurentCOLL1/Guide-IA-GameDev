---
title: "Chapitre 9 — Politique de compatibilité"
id: "DOC-V0-CH09"
status: "draft"
version: "0.5.0"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 9 — Politique de compatibilité

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Objectif du chapitre

Ce chapitre définit les règles qui permettent au guide, au projet fil rouge et au Companion Pack de rester utilisables malgré l’évolution du matériel, des systèmes d’exploitation, des moteurs, des bibliothèques et des modèles d’intelligence artificielle.

La compatibilité n’est pas considérée comme un état binaire. Elle est décrite, testée, documentée et limitée par des profils clairement identifiés.

> **Niveau : Obligatoire**  
> Toute procédure technique doit indiquer son environnement cible, ses dépendances, ses limites connues et une solution de repli lorsqu’elle existe.

## 1. Principes généraux

La politique de compatibilité repose sur huit principes :

1. définir un environnement de référence stable ;
2. distinguer les environnements supportés des environnements seulement possibles ;
3. verrouiller les dépendances critiques ;
4. documenter les écarts entre plateformes ;
5. privilégier les formats ouverts et durables ;
6. fournir des solutions de repli ;
7. tester les migrations avant adoption ;
8. ne jamais promettre une compatibilité non vérifiée.

Une procédure qui fonctionne uniquement sur la machine de son auteur n’est pas considérée comme reproductible.

## 2. Niveaux de compatibilité

Chaque outil, workflow, script ou asset reçoit un niveau de compatibilité.

### 2.1 Niveau C0 — Non évalué

L’élément n’a pas encore été testé dans le cadre du guide.

Conséquences :

- aucune garantie ;
- usage exploratoire uniquement ;
- mention explicite `C0` dans la fiche associée.

### 2.2 Niveau C1 — Expérimental

L’élément fonctionne dans au moins un cas réel, mais son comportement peut varier.

Exigences minimales :

- environnement testé indiqué ;
- limites connues listées ;
- procédure de retour arrière fournie.

### 2.3 Niveau C2 — Supporté

L’élément est validé sur l’environnement de référence du guide.

Exigences :

- installation reproduite ;
- exemple fonctionnel ;
- erreurs principales documentées ;
- test de non-régression disponible lorsque cela est pertinent.

### 2.4 Niveau C3 — Recommandé

L’élément est stable, maintenable et adapté au projet fil rouge.

Exigences supplémentaires :

- performances mesurées ;
- solution de repli validée ;
- dépendances verrouillées ;
- maintenance prévisible.

### 2.5 Niveau C4 — Référence

L’élément constitue la voie principale du guide.

Une solution C4 doit être :

- locale ou utilisable localement ;
- gratuite pour le parcours principal ;
- documentée pas à pas ;
- compatible avec la configuration AMD de référence ;
- intégrée au Companion Pack lorsque cela est possible.

## 3. Environnement matériel de référence

La configuration de référence du guide est :

- processeur : AMD Ryzen 7 2700 ;
- mémoire vive : 32 Go ;
- carte graphique : AMD Radeon RX 6750 XT ;
- mémoire vidéo : 12 Go ;
- stockage recommandé : SSD avec espace libre dédié aux modèles et caches.

Cette configuration ne représente pas le minimum absolu. Elle sert de base de mesure commune.

### 3.1 Profils matériels

Le guide distingue quatre profils.

| Profil | Description | Usage visé |
|---|---|---|
| H1 | CPU seul ou GPU non pris en charge | tests, scripts, petits modèles |
| H2 | GPU avec 6 à 8 Go de VRAM | workflows légers |
| H3 | GPU avec 10 à 12 Go de VRAM | profil de référence |
| H4 | GPU avec plus de 16 Go de VRAM | génération avancée et lots importants |

Toute procédure sensible à la VRAM doit préciser :

- le profil minimum ;
- la résolution testée ;
- la précision numérique utilisée ;
- le mécanisme d’offload éventuel ;
- le temps d’exécution observé.

## 4. Systèmes d’exploitation

### 4.1 Windows

Windows constitue la plateforme principale du parcours de référence, notamment pour :

- la configuration AMD ;
- ComfyUI avec couche de compatibilité adaptée ;
- Docker Desktop ou solution équivalente ;
- Blender, Godot, Git et Visual Studio Code ;
- les scripts PowerShell du Companion Pack.

Les chemins Windows doivent être écrits de manière robuste et ne pas supposer une lettre de disque particulière.

### 4.2 Linux

Linux est une plateforme supportée lorsque les outils concernés disposent d’une procédure reproductible.

Les différences à documenter concernent notamment :

- les pilotes GPU ;
- les permissions de fichiers ;
- les chemins ;
- les scripts shell ;
- les groupes Docker ;
- les bibliothèques système.

### 4.3 macOS

macOS est considéré comme une plateforme complémentaire.

Il peut convenir pour :

- la rédaction ;
- Git ;
- Godot ;
- Blender ;
- certains modèles locaux ;
- la compilation documentaire.

Il ne constitue pas la cible de référence pour les procédures AMD, ZLUDA ou DirectML.

### 4.4 WSL

WSL peut être utilisé pour les outils de ligne de commande et certains services, mais il ne doit pas être présenté comme transparent.

Une procédure WSL doit préciser :

- la distribution utilisée ;
- l’emplacement des fichiers ;
- le partage réseau ;
- l’accès GPU éventuel ;
- les différences de permissions ;
- les coûts de performance liés aux échanges de fichiers.

## 5. Politique de versions

### 5.1 Versions exactes pour les dépendances critiques

Les dépendances critiques doivent être verrouillées par :

- un fichier de contraintes Python ;
- un fichier `requirements.txt` ou équivalent ;
- une image Docker identifiée ;
- un commit Git ;
- un hash de modèle ;
- une version de workflow ;
- un fichier de verrouillage lorsque l’écosystème le permet.

### 5.2 Plages de versions

Une plage de versions n’est acceptable que si elle a été testée.

Exemple de formulation correcte :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Validé avec la version de référence et la version majeure suivante.
Les versions antérieures ne sont pas prises en charge.
```

Exemple incorrect :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Fonctionne avec toutes les versions récentes.
```

### 5.3 Politique de mise à jour

Une mise à jour majeure n’est intégrée au guide qu’après :

1. installation dans un environnement isolé ;
2. exécution des exemples de référence ;
3. comparaison des performances ;
4. vérification des formats de fichiers ;
5. vérification des licences ;
6. mise à jour des captures et commandes ;
7. rédaction d’une note de migration.

## 6. Matrice de compatibilité

Le Companion Pack contiendra une matrice centrale indiquant au minimum :

| Élément | Version | OS | Matériel | Niveau | Dernier test | Remarques |
|---|---|---|---|---|---|---|
| Godot | verrouillée | Windows/Linux/macOS | CPU/GPU standard | C4 | date | moteur principal |
| Blender | verrouillée | Windows/Linux/macOS | GPU recommandé | C4 | date | création 3D |
| ComfyUI | commit identifié | Windows/Linux | GPU | C4/C2 | date | image principale |
| Open WebUI | image identifiée | Windows/Linux/macOS | CPU/GPU | C4 | date | interface IA centrale |
| Ollama | version identifiée | selon plateforme | CPU/GPU | C3 | date | exécution LLM |

La matrice ne remplace pas les fiches détaillées. Elle permet une lecture rapide de l’état du projet.

## 7. Compatibilité des moteurs et outils

### 7.1 Godot

Le guide privilégie une version majeure stable de Godot.

Toute scène, ressource ou extension doit préciser :

- la version minimale ;
- la version testée ;
- la compatibilité avec le rendu utilisé ;
- les dépendances natives ;
- les différences entre éditeur et export.

Les API expérimentales ne doivent pas devenir une dépendance centrale sans solution de repli.

### 7.2 Blender

Les fichiers Blender doivent être accompagnés de :

- la version de création ;
- la version minimale d’ouverture ;
- la liste des extensions nécessaires ;
- les paramètres d’export ;
- les textures externes ;
- les unités et conventions d’axes.

Les Geometry Nodes, scripts Python et extensions doivent être testés séparément.

### 7.3 ComfyUI

Un workflow ComfyUI doit enregistrer :

- le fichier JSON ;
- la version ou le commit de ComfyUI ;
- la liste des nœuds personnalisés ;
- la version de chaque nœud critique ;
- les modèles utilisés ;
- les seeds et paramètres principaux ;
- le profil VRAM ;
- une image de référence.

Un workflow dépendant d’un nœud abandonné doit être migré ou marqué comme déprécié.

### 7.4 Open WebUI et services IA

Les intégrations entre Open WebUI, Ollama, llama.cpp, LocalAI ou d’autres services doivent documenter :

- le protocole utilisé ;
- l’adresse locale ;
- les ports ;
- les variables d’environnement ;
- l’authentification ;
- les formats de requêtes ;
- les limites de contexte ;
- le comportement en cas d’indisponibilité.

## 8. Compatibilité GPU

### 8.1 Principe

Le guide ne suppose jamais que CUDA est disponible.

Les procédures principales doivent prioriser les voies compatibles avec le matériel AMD de référence.

### 8.2 Couches d’exécution

Selon l’outil, les voies possibles peuvent inclure :

- exécution CPU ;
- DirectML ;
- Vulkan ;
- ROCm lorsque la plateforme le permet ;
- ZLUDA lorsqu’elle est compatible avec le workflow concerné ;
- backend spécifique au logiciel.

Chaque voie doit être décrite séparément. Une commande CUDA ne doit pas être présentée comme universelle.

### 8.3 Solutions de repli

Une procédure GPU doit proposer, selon le cas :

- réduction de résolution ;
- batch de taille 1 ;
- précision réduite ;
- attention découpée ;
- offload CPU ;
- modèle quantifié ;
- tuilage ;
- exécution CPU pour validation fonctionnelle.

## 9. Formats de fichiers

### 9.1 Formats privilégiés

Le guide privilégie les formats ouverts, documentés et largement supportés.

| Domaine | Formats recommandés |
|---|---|
| Documentation | Markdown, YAML, JSON |
| Modèles 3D | glTF/GLB, OBJ selon besoin |
| Images | PNG, WebP, EXR selon usage |
| Textures | PNG, EXR, formats GPU documentés |
| Audio | WAV pour les sources, OGG pour le jeu |
| Données | JSON, CSV, SQLite |
| Diagrammes | Mermaid, SVG |
| Archives | ZIP ou TAR documenté |

### 9.2 Formats propriétaires

Un format propriétaire peut être conservé comme source de travail, mais une exportation durable doit être fournie lorsque cela est possible.

Exemple :

- source Blender en `.blend` ;
- version d’échange en `.glb` ;
- textures séparées ;
- fiche d’export.

## 10. Compatibilité des données et sauvegardes

Les données persistantes doivent être versionnées par un numéro de schéma.

Toute modification incompatible impose :

- une migration ;
- une sauvegarde préalable ;
- un test sur copie ;
- une possibilité de restauration ;
- une note de changement.

Les sauvegardes de jeu, bases SQLite, profils utilisateur et configurations ne doivent pas être modifiés silencieusement.

## 11. Compatibilité réseau et multijoueur

Les protocoles réseau doivent intégrer un identifiant de version.

En cas d’incompatibilité, le système doit :

- refuser proprement la connexion ;
- afficher la cause ;
- indiquer les versions attendues ;
- éviter toute corruption de données.

La compatibilité réseau doit être testée indépendamment de la compatibilité des sauvegardes.

## 12. Compatibilité des modèles IA

Un modèle IA n’est pas défini uniquement par son nom.

Sa fiche doit inclure :

- l’architecture ;
- le format ;
- la quantification ;
- la taille ;
- le hash ;
- la licence ;
- le tokenizer ou encodeur associé ;
- le contexte maximal testé ;
- le backend ;
- le profil mémoire ;
- les usages autorisés.

Deux fichiers portant un nom voisin peuvent produire des résultats différents. Le hash constitue donc la référence technique prioritaire.

## 13. Compatibilité des workflows IA

Un workflow doit séparer :

- les paramètres fonctionnels ;
- les paramètres de qualité ;
- les paramètres dépendants du matériel ;
- les paramètres expérimentaux.

Les variantes doivent être nommées explicitement, par exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-IMG-001-H2-LOWVRAM
WF-IMG-001-H3-REFERENCE
WF-IMG-001-H4-HIGHQUALITY
```

## 14. Dépréciation

Un composant devient déprécié lorsqu’il :

- n’est plus maintenu ;
- dépend d’une API supprimée ;
- présente un risque de sécurité ;
- possède une alternative plus stable ;
- ne peut plus être reproduit.

La dépréciation suit quatre étapes :

1. marquage dans la documentation ;
2. maintien temporaire d’une procédure de migration ;
3. retrait du parcours principal ;
4. archivage dans une section historique.

Un identifiant déprécié n’est jamais réattribué.

## 15. Politique de rupture

Une rupture de compatibilité doit être annoncée dans :

- `CHANGELOG.md` ;
- la fiche concernée ;
- la matrice de compatibilité ;
- la note de migration ;
- la version du guide.

Les changements incompatibles entraînent une augmentation de version majeure pour l’élément concerné.

## 16. Tests de compatibilité

Les contrôles minimaux comprennent :

- démarrage de l’outil ;
- ouverture des fichiers de référence ;
- exécution d’un exemple ;
- export du résultat ;
- comparaison des journaux ;
- mesure mémoire ;
- validation des chemins ;
- test d’erreur contrôlée ;
- test de restauration.

Les résultats doivent être datés et associés à l’environnement utilisé.

## 17. Parcours Solo

En Mode Solo, la politique privilégie :

- une configuration principale ;
- peu de variantes ;
- des mises à jour manuelles et contrôlées ;
- des sauvegardes simples ;
- une matrice réduite aux outils réellement utilisés.

Le développeur solo ne doit pas maintenir artificiellement des plateformes qu’il ne peut pas tester.

## 18. Parcours Studio

En Mode Studio, la compatibilité implique en plus :

- plusieurs postes ;
- des environnements reproductibles ;
- une matrice centralisée ;
- des tests automatisés ;
- des responsabilités définies ;
- une politique de mise à jour ;
- des périodes de support ;
- des procédures de migration et de retour arrière.

## 19. Fiche universelle de compatibilité

Chaque composant important peut utiliser la structure suivante :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: TOOL-EXAMPLE-001
version_testee: "x.y.z"
niveau: C3
os:
  - Windows
materiel:
  profil_minimum: H2
  profil_recommande: H3
dependances: []
formats_entree: []
formats_sortie: []
limitations: []
solution_repli: ""
dernier_test: "AAAA-MM-JJ"
```

## 20. Checklist de validation

Avant de déclarer un élément compatible, vérifier :

- [ ] l’environnement de test est identifié ;
- [ ] la version exacte est enregistrée ;
- [ ] le niveau C0 à C4 est attribué ;
- [ ] le profil matériel est indiqué ;
- [ ] les dépendances sont listées ;
- [ ] les formats d’entrée et de sortie sont connus ;
- [ ] les limites sont documentées ;
- [ ] une solution de repli existe ou son absence est signalée ;
- [ ] le test principal est reproductible ;
- [ ] les données peuvent être sauvegardées et restaurées ;
- [ ] les incompatibilités sont visibles dans le changelog ;
- [ ] la date du dernier test est enregistrée.

## 21. Résultat attendu

À l’issue de ce chapitre, chaque outil, modèle, workflow, script et format du projet doit pouvoir être situé dans une matrice claire : environnement cible, version testée, niveau de support, limitations et solution de repli.

Cette discipline évite que le guide devienne une collection de recettes fragiles. Elle transforme la compatibilité en propriété mesurable et maintenable du projet.
