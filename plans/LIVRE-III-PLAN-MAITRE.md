---
title: "Plan maître détaillé — Livre III"
id: "DOC-PLAN-L3"
status: "active"
version: "1.1.11"
lang: "fr-FR"
last-updated: "2026-07-23T11:50:40+02:00"
book: "Livre III"
chapter-count: 30
---

# Plan maître détaillé — Livre III

> **Titre du Livre :** Production des contenus et des assets  
> **Statut :** en cours — 11 chapitres sur 30  
> **Rôle :** transformer la direction artistique en assets traçables, juridiquement documentés, optimisés et directement intégrables dans Godot.

## 1. Fonction de ce document dans une nouvelle conversation

Ce fichier est la source maître du périmètre du Livre III. Une nouvelle conversation doit le lire entièrement après `CONTINUITE-PROJET.md`, `ROADMAP.md`, `contents.txt` et le futur index du Livre III.

Le plan fixe :

- l’ordre immuable des trente chapitres ;
- l’intention pédagogique de chaque chapitre ;
- les résultats d’apprentissage attendus ;
- les contenus obligatoires ;
- les livrables permanents ;
- les dépendances avec les chapitres voisins et les Livres I et II ;
- les adaptations Solo et Studio ;
- les critères de validation ;
- les frontières qui empêchent les doublons ou les glissements de responsabilité.

Aucun titre, ordre, livrable majeur ou frontière ne doit être modifié silencieusement. Toute évolution du périmètre doit être explicitée dans la continuité du projet et validée dans le même lot que la modification de ce fichier.

## 2. Finalité pédagogique du Livre III

Le Livre III ne se limite pas à expliquer comment produire de belles images ou de beaux modèles. Il décrit une chaîne de production complète :

1. définir ce qui doit être produit ;
2. établir une direction artistique vérifiable ;
3. sourcer légalement les références et outils ;
4. créer les sources dans Blender, ComfyUI et les outils audio ;
5. préparer topologie, matériaux, rigs, animations et niveaux de détail ;
6. importer et réimporter dans Godot ;
7. mesurer les budgets ;
8. valider visuellement, techniquement et juridiquement ;
9. automatiser les tâches répétitives ;
10. conserver les sources, paramètres, preuves et possibilités de reprise.

Un asset n’est pas terminé uniquement parce qu’il paraît correct dans Blender. Il doit être identifiable, traçable, correctement dimensionné, budgété, exportable, réimportable, validé dans Godot et utilisable selon ses droits.

## 3. Règles transversales obligatoires

Chaque chapitre doit couvrir, selon son sujet :

- provenance, licence, consentement et restrictions de redistribution ;
- conventions de fichiers, dossiers, identifiants, noms et versions ;
- source canonique et distinction avec les fichiers générés ;
- budget technique mesurable ;
- configuration ou scène de validation dans Godot ;
- procédure Solo et procédure Studio ;
- contrôle visuel et contrôle technique ;
- symptômes, diagnostics et reprise après erreur ;
- livrables réutilisables dans le Companion Pack ;
- limites explicites et responsabilités laissées aux autres Livres.

Un asset ne peut pas être déclaré terminé sans :

- une source identifiable ;
- un auteur, fournisseur ou outil ;
- une licence ou un statut juridique explicite ;
- une version ;
- les paramètres significatifs de création ou de génération ;
- ses dimensions, unités et échelle ;
- ses formats source et export ;
- ses dépendances ;
- ses contraintes d’utilisation ;
- son budget ;
- une validation dans Godot.

Les exemples de commandes et de scripts respecteront les repères d’utilisation du Volume 0. Les sections d’erreurs appliqueront la règle sémantique complète : symptôme, exemple fautif, raison de l’échec, exemple corrigé et raison du fonctionnement.

## 4. Fil rouge et livrables cumulatifs

Le fil rouge reste `Project Asteria`. Le Livre III doit faire progresser un ensemble d’assets pilotes cohérents, plutôt que produire trente démonstrations sans lien.

Le parcours cumulatif comprend au minimum :

- une bible visuelle ;
- un registre de provenance ;
- un template Blender ;
- un personnage ou humanoïde pilote ;
- un animal ou une créature pilote ;
- un kit d’architecture ;
- un terrain avec végétation ;
- une bibliothèque PBR ;
- un asset retopologisé, baké et décliné en LOD ;
- un rig et une bibliothèque d’animations ;
- une séquence cinématique courte ;
- une bibliothèque VFX et audio minimale ;
- un thème UI avec profils d’accessibilité ;
- une chaîne d’import Godot ;
- une porte de validation d’asset ;
- un lot automatisé reproductible.

Les livrables adaptés seront versés au Companion Pack seulement après validation et nettoyage des données spécifiques au fil rouge.

## 5. Structure attendue de chaque futur chapitre

Chaque chapitre devra normalement contenir :

- rôle et résultat concret ;
- prérequis ;
- logiciels et fichiers à ouvrir ;
- conventions de projet ;
- procédure progressive ;
- exemples Solo et Studio ;
- intégration dans Godot ;
- budgets et mesures ;
- provenance et licences ;
- contrôles visuels ;
- contrôles techniques ;
- erreurs fréquentes et corrections ;
- livrables à conserver ;
- synthèse opérationnelle pour `Project Asteria`.

Le texte lecteur ne doit jamais contenir le protocole QA interne, les preuves de validation, la recommandation de raisonnement ou les informations de reprise de conversation.

## 6. Références de production héritées

Sauf révision explicite ultérieure :

- système principal : Windows 11 ;
- terminal : PowerShell 7 ;
- éditeur : Visual Studio Code ;
- moteur : Godot `4.7.1-stable`, édition Standard, GDScript, Forward+ ;
- DCC principal : Blender, version à qualifier au démarrage du Livre III ;
- génération visuelle : ComfyUI, modèles et extensions qualifiés par workflow ;
- matériel de mesure : Radeon RX 6750 XT 12 Go, Ryzen 7 2700 et 32 Go de RAM ;
- parcours : Mode Solo et Mode Studio ;
- projet fil rouge : `Project Asteria`.

Les versions de Blender, ComfyUI, extensions, modèles et outils audio devront être vérifiées au moment où leurs chapitres deviennent actifs. Elles ne sont pas inventées à l’avance dans ce plan.

## 7. Chapitres

> **Progression :** chapitres 1 à 11 rédigés, repérés et audités au niveau `static-review` ; chapitres 12 à 30 à produire.

## Chapitre 1 — Préproduction et cahier des charges artistique

### Intention

Transformer la vision générale du jeu en un programme de production artistique mesurable, ordonné et compatible avec les moyens réels du projet.

### Résultats d’apprentissage

- recenser les familles d’assets nécessaires au prototype, au vertical slice et à la production complète ;
- estimer quantités, priorités, niveaux de qualité, dépendances et risques ;
- fixer des budgets initiaux pour la géométrie, les textures, les matériaux, les rigs, les animations, les VFX et l’audio ;
- formuler des critères d’acceptation compréhensibles par une personne seule comme par une équipe ;

### Contenu obligatoire

- différence entre intention artistique, besoin fonctionnel et livrable de production ;
- matrice des assets avec identifiant, catégorie, propriétaire, état, priorité et dépendances ;
- niveaux de maturité : prototype, vertical slice, alpha de contenu, finition et livraison ;
- budgets par famille d’assets et stratégie de révision lorsque les mesures réelles contredisent les hypothèses ;
- calendrier, chemin critique, risques de dépendance et capacité de reprise ;
- critères de sortie mesurables pour éviter les validations purement subjectives ;

### Livrables

- cahier des charges artistique versionné ;
- matrice complète des assets ;
- budgets initiaux par famille ;
- calendrier de production et registre des risques ;
- checklist d’acceptation ;

### Dépendances et continuité

S’appuie sur la vision de Project Asteria et les contraintes matérielles et organisationnelles établies dans les Livres I et II.

### Mode Solo

Un tableau unique, peu d’états et des priorités strictes afin de réduire le coût de gestion.

### Mode Studio

Responsables par famille, jalons partagés, dépendances explicites et validation indépendante des estimations critiques.

### Critères de validation

- chaque asset prévu possède un identifiant, une priorité, un budget et un critère d’acceptation ;
- la charge totale reste cohérente avec le temps, le matériel et les compétences disponibles ;
- les risques bloquants et les actifs pilotes sont identifiés ;

### Frontière

Ne choisit pas encore le style visuel définitif ; ce choix appartient au chapitre 2.

## Chapitre 2 — Direction artistique et bible visuelle

### Intention

Définir un langage visuel cohérent et vérifiable qui guidera toutes les productions sans figer inutilement la créativité.

### Résultats d’apprentissage

- décrire formes, silhouettes, proportions, palettes, matériaux et éclairages de référence ;
- déterminer le niveau de réalisme et les écarts autorisés ;
- relier personnages, environnements, interface, VFX et audio visuel dans une même grammaire ;
- produire des exemples conformes, limites et non conformes ;

### Contenu obligatoire

- axes esthétiques et valeurs perceptuelles du projet ;
- échelles, proportions et règles de silhouette ;
- palettes principales, secondaires et fonctionnelles ;
- matériaux, lumière, contraste, profondeur et lisibilité du gameplay ;
- variations culturelles, régionales, temporelles et sociales ;
- règles de cohérence entre rendu rapproché, vue de jeu et interfaces ;
- processus de révision de la bible après test dans Godot ;

### Livrables

- bible visuelle versionnée ;
- palettes et références de matériaux ;
- planches de silhouettes et d’échelles ;
- règles d’éclairage ;
- grille de revue artistique ;

### Dépendances et continuité

Dépend du cahier des charges du chapitre 1 et encadre tous les chapitres de production suivants.

### Mode Solo

Bible courte, visuelle et directement actionnable, centrée sur les décisions irréversibles ou coûteuses.

### Mode Studio

Document partagé avec propriétaires, historique de décisions, exemples négatifs et processus formel de dérogation.

### Critères de validation

- plusieurs assets pilotes différents paraissent appartenir au même univers ;
- les règles restent lisibles dans Godot et sur le matériel de référence ;
- une autre personne peut classer un exemple comme conforme ou non avec peu d’ambiguïté ;

### Frontière

Définit la direction, mais ne produit pas encore les assets définitifs.

## Chapitre 3 — Références, concept art et ComfyUI

### Intention

Construire une chaîne de références et de concepts traçable, légale et reproductible, sans confondre proposition visuelle et asset final.

### Résultats d’apprentissage

- collecter et annoter des références avec leur provenance ;
- organiser des moodboards utiles à la production ;
- générer des concepts avec ComfyUI en conservant modèles, workflows, prompts, seeds et paramètres ;
- sélectionner humainement les propositions conformes à la bible ;

### Contenu obligatoire

- différences entre inspiration, référence, concept, source de production et asset final ;
- registre de provenance et droits d’utilisation des références ;
- organisation des moodboards, annotations et comparaisons ;
- workflow ComfyUI versionné, modèles et dépendances ;
- gestion des seeds, paramètres, variantes et reprises ;
- sélection, critique, correction et consolidation humaine ;
- détection des incohérences anatomiques, matérielles ou culturelles ;

### Livrables

- dossiers de références sourcées ;
- moodboards annotés ;
- workflows ComfyUI JSON ;
- manifestes de modèles et licences ;
- planches de concepts et rapport de sélection ;

### Dépendances et continuité

Utilise la bible visuelle du chapitre 2 et prépare les décisions de modélisation des chapitres 4 à 18.

### Mode Solo

Petit nombre de workflows stables et sélection stricte afin d’éviter l’accumulation de variantes inutiles.

### Mode Studio

Bibliothèque partagée, règles de nommage, revues de sélection et séparation entre génération, direction artistique et validation juridique.

### Critères de validation

- chaque image retenue possède une provenance et un contexte d’usage ;
- le workflow peut reproduire une famille de propositions à partir des paramètres enregistrés ;
- aucun concept n’est présenté comme asset final sans transformation et validation ;

### Frontière

Ne transforme pas directement une image générée en texture ou modèle de production.

## Chapitre 4 — Pipeline Blender et organisation des fichiers

### Intention

Installer un environnement Blender cohérent et une chaîne d’échange reproductible jusqu’à Godot.

### Résultats d’apprentissage

- configurer unités, axes, échelle, origines et collections ;
- séparer sources, bibliothèques, variantes, caches, exports et livraisons ;
- définir conventions de nommage et versions ;
- exporter un asset test correctement vers Godot ;

### Contenu obligatoire

- template Blender et préférences de projet ;
- unités métriques, orientations et conventions de pivots ;
- collections, bibliothèques liées et overrides ;
- arborescence source, travail, cache, export et archive ;
- stratégie de versions et sauvegardes ;
- formats d’échange, presets et limites ;
- test aller-retour Blender vers Godot ;

### Livrables

- template Blender ;
- conventions de collections et nommage ;
- arborescence canonique ;
- presets d’export ;
- checklist d’ouverture, contrôle et livraison ;

### Dépendances et continuité

Dépend des conventions générales du projet et sert de base à tous les chapitres de création 3D.

### Mode Solo

Un template principal et un chemin d’export court, avec peu de variantes.

### Mode Studio

Bibliothèques partagées, responsabilités de publication, versions immuables et contrôles automatiques des conventions.

### Critères de validation

- l’asset test arrive à la bonne échelle, orientation et position ;
- une réouverture sur une autre machine retrouve les dépendances attendues ;
- les sources et sorties générées sont immédiatement distinguables ;

### Frontière

Prépare l’environnement ; les techniques de modélisation spécialisées viennent ensuite.

## Chapitre 5 — Provenance, licences et validation des assets

### Intention

Garantir que chaque asset peut être retracé, utilisé et distribué selon des droits explicitement connus.

### Résultats d’apprentissage

- distinguer licence, droit d’auteur, consentement, marque et droit à l’image ;
- enregistrer source, auteur, outil, version, restrictions et transformations ;
- gérer les assets internes, achetés, libres et générés ;
- bloquer ou remplacer les éléments juridiquement incertains ;

### Contenu obligatoire

- typologie des droits et restrictions utiles à une production de jeu ;
- fiche d’asset et identifiant stable ;
- registre de provenance et chaîne de transformations ;
- licences des modèles IA, datasets, textures, polices, sons et mocap ;
- consentement pour voix, visage et interprétation ;
- procédure de retrait, remplacement et conservation de preuve ;
- contrôles automatiques minimaux et revue humaine ;

### Livrables

- registre de provenance ;
- modèle de fiche d’asset ;
- matrice des licences ;
- procédure de retrait et remplacement ;
- règles de blocage et contrôles minimaux ;

### Dépendances et continuité

S’applique à tous les chapitres du Livre III et complète les règles de sécurité documentaire du Livre II.

### Mode Solo

Fiche légère obligatoire pour chaque source externe ou générée.

### Mode Studio

Validation juridique ou responsable désigné, inventaire central et interdiction de publication sans statut explicite.

### Critères de validation

- tout asset publié peut être relié à sa source et à sa licence ;
- les restrictions de redistribution et d’usage commercial sont visibles ;
- un asset contesté peut être retiré sans perdre l’historique ;

### Frontière

Ne fournit pas d’avis juridique personnalisé.

## Chapitre 6 — Création des humains

### Intention

Produire une base humaine modulaire, crédible, animable et compatible avec les contraintes de personnalisation et de performance.

### Résultats d’apprentissage

- comprendre proportions, anatomie et variations morphologiques ;
- concevoir une topologie adaptée aux déformations ;
- préparer textures, LOD, vêtements et animations ;
- éviter stéréotypes, anomalies anatomiques et surcoûts ;

### Contenu obligatoire

- références anatomiques et proportions ;
- base neutre et variantes d’âge, taille et corpulence ;
- topologie des articulations et zones expressives ;
- séparation corps, tête, mains, pieds et éléments modulaires ;
- préparation des matériaux et textures ;
- LOD, mémoire et densité géométrique ;
- scène Godot de poses et performances ;

### Livrables

- base humaine de référence ;
- variantes morphologiques ;
- guide de proportions ;
- budgets et profils LOD ;
- scène Godot de validation ;

### Dépendances et continuité

S’appuie sur les chapitres 2 à 5 et prépare les chapitres 10, 11, 19 et 20.

### Mode Solo

Une base principale soigneusement conçue avec un nombre limité de variantes réellement utiles.

### Mode Studio

Bases validées par spécialité, bibliothèque morphologique, règles de compatibilité et contrôles multi-rigs.

### Critères de validation

- les poses extrêmes ne provoquent pas de déformation majeure ;
- les silhouettes restent lisibles à plusieurs distances ;
- la base accepte vêtements, rig et LOD sans rupture de conventions ;

### Frontière

Les visages, cheveux et vêtements sont approfondis aux chapitres 10 et 11.

## Chapitre 7 — Création des humanoïdes

### Intention

Adapter la logique de production humaine à des espèces humanoïdes distinctes sans perdre crédibilité, animation et compatibilité d’équipement.

### Résultats d’apprentissage

- modifier anatomie et proportions de manière fonctionnelle ;
- conserver ou documenter la compatibilité avec les rigs et interactions ;
- définir des modules spécifiques et variations culturelles ;
- maintenir une silhouette immédiatement reconnaissable ;

### Contenu obligatoire

- écarts anatomiques par rapport à la base humaine ;
- membres, articulations, tête, posture et locomotion ;
- profils de rig et retargeting partiel ;
- compatibilité des vêtements, armures et sockets ;
- variations culturelles sans stéréotype réducteur ;
- LOD et simplification des traits distinctifs ;
- tests de silhouette, équipement et mouvement ;

### Livrables

- bases humanoïdes ;
- règles d’adaptation anatomique ;
- profils de rig ;
- matrice de compatibilité des équipements ;
- scènes de test ;

### Dépendances et continuité

Part de la base humaine du chapitre 6 et alimente les chapitres 10, 11, 19 et 20.

### Mode Solo

Réutilisation maximale des contrats communs, avec exceptions clairement documentées.

### Mode Studio

Profils d’espèce versionnés, propriétaires des incompatibilités et batteries de tests partagées.

### Critères de validation

- l’espèce reste lisible à distance ;
- la locomotion et les interactions ne contredisent pas l’anatomie ;
- les équipements compatibles sont explicitement identifiés ;

### Frontière

Ne couvre pas les créatures réellement non humanoïdes du chapitre 9.

## Chapitre 8 — Création des animaux

### Intention

Créer des animaux crédibles et performants à partir de leur anatomie, locomotion et mode de présence dans le monde.

### Résultats d’apprentissage

- analyser les grandes familles anatomiques ;
- concevoir rigs et cycles adaptés ;
- gérer pelage, plumes, écailles, variantes et LOD ;
- préparer l’usage en groupe dans Godot ;

### Contenu obligatoire

- quadrupèdes, oiseaux, poissons, reptiles et morphologies particulières ;
- répartition des masses, articulations et contacts au sol ;
- cycles de marche, course, vol, nage et repos ;
- pelage, plumes, écailles et stratégies de rendu ;
- variantes d’âge, sexe, saison ou biome si pertinentes ;
- LOD, instancing et densité de groupe ;
- scènes de validation de locomotion et coût ;

### Livrables

- modèles animaux pilotes ;
- fiches anatomiques ;
- rigs de base ;
- cycles de locomotion ;
- budgets par distance et densité ;

### Dépendances et continuité

Utilise les fondations Blender et matériaux ; prépare l’intégration et l’animation des chapitres 19 à 21.

### Mode Solo

Quelques familles pilotes réutilisables et une priorité donnée aux animaux visibles en jeu.

### Mode Studio

Bibliothèques par famille, nomenclature de rigs, tests de foule et partage des cycles compatibles.

### Critères de validation

- contacts au sol crédibles ;
- absence de glissement évident ;
- coût acceptable pour les groupes prévus ;
- mouvement cohérent avec la morphologie ;

### Frontière

Les comportements de simulation appartiennent au Livre II.

## Chapitre 9 — Création des créatures

### Intention

Transformer une idée fantastique en organisme visuellement identifiable, riggable, animable et exploitable par le gameplay.

### Résultats d’apprentissage

- relier anatomie, habitat, capacités et silhouette ;
- anticiper collisions, attaques, points faibles et locomotion ;
- préparer rig et déformations dès le concept ;
- créer des variantes sans diluer l’identité ;

### Contenu obligatoire

- fonction narrative et gameplay de la créature ;
- anatomie spéculative cohérente ;
- silhouette primaire, secondaire et détails ;
- points de contact, locomotion et centre de masse ;
- volumes de collision, zones d’impact et sockets ;
- rig, contraintes et animations possibles ;
- variantes, LOD et lisibilité en combat ;

### Livrables

- fiches de créatures ;
- planches anatomiques ;
- modèles pilotes ;
- rigs et volumes de collision ;
- tests de lisibilité gameplay ;

### Dépendances et continuité

S’appuie sur la direction artistique, le concept art et les pipelines 3D ; prépare les chapitres 19, 20 et 23.

### Mode Solo

Priorité à une créature pilote complète avant multiplication des variantes.

### Mode Studio

Revue croisée concept-modélisation-animation-gameplay avant validation de la morphologie.

### Critères de validation

- la créature est reconnaissable rapidement ;
- le rig et les collisions sont compatibles avec ses actions prévues ;
- les variantes restent rattachées à la même identité visuelle ;

### Frontière

Crée l’asset mais pas son intelligence artificielle.

## Chapitre 10 — Visages, peau, yeux, cheveux et pilosité

### Intention

Produire les éléments de gros plan les plus sensibles au réalisme tout en maîtrisant coût, transparence et LOD.

### Résultats d’apprentissage

- construire visages et expressions crédibles ;
- créer matériaux de peau, yeux, dents et muqueuses ;
- choisir entre géométrie, hair cards, groom, textures et shaders ;
- préparer blendshapes et niveaux de détail faciaux ;

### Contenu obligatoire

- topologie du visage et zones de déformation ;
- sculpture, asymétrie et variation ;
- shader de peau et gestion des détails ;
- œil, cornée, iris, humidité et reflets ;
- dents, bouche et intersections ;
- cheveux, barbe, fourrure et transparence ;
- blendshapes, expressions de test et LOD ;

### Livrables

- tête de référence ;
- matériaux peau et yeux ;
- bibliothèque de cheveux et pilosité ;
- blendshapes ou système facial ;
- profils LOD ;

### Dépendances et continuité

Complète les bases des chapitres 6 et 7 et prépare la synchronisation labiale du chapitre 27.

### Mode Solo

Un ensemble limité de solutions robustes et réutilisables, testé sous plusieurs lumières.

### Mode Studio

Bibliothèques de shaders, normes de blendshapes, validation lookdev et profils de performance par plateforme.

### Critères de validation

- gros plans crédibles sous plusieurs éclairages ;
- absence d’artefacts majeurs de transparence ou d’intersection ;
- LOD facial stable à distance ;

### Frontière

La synchronisation labiale complète appartient au chapitre 27.

## Chapitre 11 — Vêtements, armures et accessoires

### Intention

Créer un système d’équipement visuel modulaire compatible avec morphologies, animation, collisions et niveaux de détail.

### Résultats d’apprentissage

- concevoir couches, attaches, tailles et variantes ;
- gérer skinning, simulation et collisions ;
- prévenir le clipping et documenter les incompatibilités ;
- optimiser matériaux, géométrie et LOD ;

### Contenu obligatoire

- layering et ordre des couches ;
- patrons, volumes et marges de mouvement ;
- skinning aux rigs de référence ;
- simulation de tissu et collisions simplifiées ;
- attaches, accessoires et points de fixation ;
- masquage de géométrie sous les vêtements ;
- LOD, atlas et réduction des matériaux ;

### Livrables

- kits vestimentaires ;
- règles de layering ;
- profils de skinning ;
- collisions de simulation ;
- matrice de compatibilité ;

### Dépendances et continuité

Dépend des bases humaines et humanoïdes et alimente les tests d’animation et d’intégration.

### Mode Solo

Kits limités mais combinables, avec règles de compatibilité simples.

### Mode Studio

Catalogue partagé, validation multi-morphologies et responsabilité séparée entre création, skinning et intégration.

### Critères de validation

- absence de clipping majeur dans les poses extrêmes ;
- combinaisons autorisées clairement identifiées ;
- simulation stable et coût maîtrisé ;

### Frontière

Les objets tenus et armes sont traités au chapitre 12.

## Chapitre 12 — Objets, équipements et armes

### Intention

Produire des objets cohérents avec leur usage, leur échelle et leurs interactions, sans mélanger représentation visuelle et règles métier.

### Résultats d’apprentissage

- respecter échelle, prise en main et fonction ;
- préparer pivots, sockets et collisions ;
- gérer variantes, états, dégâts visuels et usure ;
- intégrer les objets dans des scènes Godot d’équipement ;

### Contenu obligatoire

- références dimensionnelles et ergonomie ;
- pivot, origine et orientation ;
- sockets de main, dos, ceinture ou environnement ;
- collisions de prise, interaction et projectile si nécessaire ;
- états visuels, variantes et dégradation ;
- matériaux, LOD et atlas ;
- séparation entre asset, données de contenu et logique gameplay ;

### Livrables

- bibliothèque d’objets pilotes ;
- conventions de pivots et sockets ;
- collisions ;
- LOD ;
- scènes Godot d’équipement ;

### Dépendances et continuité

S’appuie sur les matériaux, le pipeline Blender et les rigs ; se connecte aux systèmes d’inventaire et combat du Livre II.

### Mode Solo

Bibliothèque priorisée par fréquence d’usage, avec conventions communes strictes.

### Mode Studio

Catégories propriétaires, validations d’échelle croisées et scènes de test automatisées.

### Critères de validation

- l’objet s’aligne correctement dans les animations ;
- les collisions correspondent à l’usage ;
- l’échelle reste cohérente avec le monde et les personnages ;

### Frontière

Les règles d’inventaire, de dégâts et de combat restent dans le Livre II.

## Chapitre 13 — Architecture, bâtiments et kits modulaires

### Intention

Créer des environnements construits assemblables, cohérents métriquement et assez variés pour éviter la répétition.

### Résultats d’apprentissage

- définir métriques, grille et snapping ;
- concevoir modules de murs, sols, toits, ouvertures et intérieurs ;
- préparer collisions, navigation, occlusion et destruction ;
- tester plusieurs bâtiments à partir du même kit ;

### Contenu obligatoire

- grille métrique et dimensions humaines ;
- catégories de modules et règles d’assemblage ;
- coins, jonctions, ouvertures et transitions ;
- intérieurs, façades et variantes ;
- pivots, snapping et contrôle des tolérances ;
- collisions, navigation et occlusion ;
- LOD, matériaux partagés et rupture de répétition ;

### Livrables

- kit modulaire ;
- grille métrique ;
- règles d’assemblage ;
- scènes de test ;
- budgets et LOD ;

### Dépendances et continuité

Utilise les conventions Blender, matériaux et objets ; alimente les terrains et la construction runtime.

### Mode Solo

Kit compact centré sur les bâtiments réellement nécessaires au vertical slice.

### Mode Studio

Bibliothèque modulaire versionnée, contrôles de compatibilité et revue architecture-environnement-technique.

### Critères de validation

- plusieurs bâtiments différents s’assemblent sans trous ni décalages ;
- collisions et navigation restent cohérentes ;
- la répétition visuelle est maîtrisée ;

### Frontière

La construction par le joueur appartient au Livre II.

## Chapitre 14 — Terrains, paysages et mondes ouverts

### Intention

Produire de grands espaces traversables et lisibles avec streaming, mémoire et continuité visuelle maîtrisés.

### Résultats d’apprentissage

- créer reliefs, routes, rivières, littoraux et plans d’eau ;
- organiser tuiles, streaming et LOD ;
- préparer collisions, navigation et transitions ;
- mesurer mémoire et temps de chargement ;

### Contenu obligatoire

- heightmaps, sculpt et érosion contrôlée ;
- échelle du monde et découpage spatial ;
- routes, rivières et raccords aux bâtiments ;
- tuiles, streaming et voisinage ;
- matériaux de terrain et mélange de couches ;
- eau, collisions et navigation ;
- benchmarks de parcours, mémoire et ruptures ;

### Livrables

- terrain pilote ;
- découpage spatial ;
- profils de streaming ;
- matériaux de terrain ;
- scène de benchmark ;

### Dépendances et continuité

Dépend de la direction artistique et des matériaux ; accueille bâtiments, végétation et biomes.

### Mode Solo

Zone pilote limitée mais complète avant extension du monde.

### Mode Studio

Découpage par régions, contrats de raccord, budgets par cellule et validation sur plusieurs machines.

### Critères de validation

- traversée sans rupture visuelle majeure ;
- streaming et mémoire dans les budgets ;
- collisions et navigation cohérentes ;

### Frontière

La simulation écologique appartient au Livre II.

## Chapitre 15 — Végétation et biomes

### Intention

Créer une bibliothèque végétale cohérente avec les biomes et capable d’atteindre de fortes densités à coût maîtrisé.

### Résultats d’apprentissage

- définir espèces, saisons, densités et distributions ;
- créer arbres, plantes, herbes et débris ;
- utiliser instancing, imposteurs, vent et interaction ;
- mesurer coût CPU/GPU et distance d’affichage ;

### Contenu obligatoire

- profil visuel et écologique d’un biome ;
- arbres, arbustes, herbes, fleurs et débris ;
- variantes de taille, saison et santé ;
- cartes et règles de distribution ;
- instancing, MultiMesh et regroupement ;
- shaders de vent et interaction locale ;
- LOD, imposteurs et benchmark de densité ;

### Livrables

- bibliothèque végétale ;
- profils de biome ;
- cartes de distribution ;
- shaders de vent ;
- benchmark de densité ;

### Dépendances et continuité

S’appuie sur terrains, matériaux et LOD ; se connecte aux données écologiques du Livre II.

### Mode Solo

Peu d’espèces bien combinées, avec densités mesurées sur le matériel de référence.

### Mode Studio

Catalogue par biome, production en lots, contrôle botanique et matrices de qualité par plateforme.

### Critères de validation

- diversité suffisante sans bruit visuel ;
- coût acceptable aux densités prévues ;
- transitions et distance d’affichage crédibles ;

### Frontière

Le système dynamique de biome appartient au Livre II.

## Chapitre 16 — Textures, matériaux et pipeline PBR

### Intention

Établir un pipeline PBR cohérent depuis la source jusqu’aux matériaux Godot.

### Résultats d’apprentissage

- comprendre albedo, normal, roughness, metallic, AO, height et emissive ;
- gérer espaces colorimétriques, compression et résolutions ;
- définir texel density et bibliothèques de matériaux ;
- valider les matériaux sous plusieurs éclairages ;

### Contenu obligatoire

- rôle et interprétation de chaque carte PBR ;
- sRGB, données linéaires et erreurs de colorimétrie ;
- résolution, mipmaps, compression et mémoire ;
- texel density et cohérence entre assets ;
- matériaux tilables, trim sheets et atlas ;
- configuration des matériaux Godot ;
- scène d’éclairage de référence et comparaison ;

### Livrables

- guide PBR ;
- presets d’export ;
- bibliothèque de matériaux ;
- profils de compression ;
- scène d’éclairage de référence ;

### Dépendances et continuité

Dépend de la bible visuelle et alimente tous les assets 3D, terrains, végétation et VFX.

### Mode Solo

Bibliothèque réduite de matériaux maîtres et profils simples par usage.

### Mode Studio

Lookdev partagé, validation colorimétrique, variantes de qualité et inventaire de textures.

### Critères de validation

- rendu cohérent sous plusieurs éclairages ;
- canaux et espaces colorimétriques correctement configurés ;
- mémoire et résolution conformes aux budgets ;

### Frontière

Les UV et le baking approfondis appartiennent au chapitre 17.

## Chapitre 17 — UV, retopologie et baking

### Intention

Transformer des modèles détaillés en assets optimisés tout en préservant la qualité visuelle.

### Résultats d’apprentissage

- produire une topologie animable et optimisée ;
- déplier les UV avec densité cohérente ;
- créer cages et baker les cartes nécessaires ;
- diagnostiquer seams, tangentes et artefacts ;

### Contenu obligatoire

- objectifs de retopologie selon asset statique ou déformable ;
- edge flow et densité locale ;
- découpe UV, îlots, marges et chevauchements autorisés ;
- cages, ray distance et noms de correspondance ;
- baking des normales, AO, curvature et autres cartes ;
- tangent space et cohérence Blender-Godot ;
- contrôle visuel et corrections ;

### Livrables

- maillage haute résolution ;
- maillage basse résolution ;
- UV et cages ;
- textures bakées ;
- rapport de contrôle ;

### Dépendances et continuité

S’appuie sur la modélisation et les matériaux ; prépare les LOD et l’intégration.

### Mode Solo

Procédure reproductible sur un asset pilote avant généralisation.

### Mode Studio

Spécialisation possible entre sculpt, retopo, UV et lookdev avec critères de passage formels.

### Critères de validation

- absence d’artefacts majeurs ;
- densité UV cohérente ;
- comparaison high/low satisfaisante sous éclairage de test ;

### Frontière

Le chapitre 18 traite la chaîne LOD après création de l’asset final.

## Chapitre 18 — LOD, imposteurs et optimisation géométrique

### Intention

Réduire le coût géométrique selon la distance sans provoquer de dégradation perceptuelle excessive.

### Résultats d’apprentissage

- définir seuils et budgets par distance ;
- produire des LOD manuels ou automatiques contrôlés ;
- créer imposteurs et billboards ;
- mesurer gains, transitions et popping ;

### Contenu obligatoire

- budget par taille écran et importance gameplay ;
- méthodes de décimation et préservation de silhouette ;
- simplification des matériaux et textures par LOD ;
- imposteurs, billboards et orientation ;
- seuils, hystérésis et transitions ;
- popping, ombres et collisions simplifiées ;
- benchmark avant/après ;

### Livrables

- chaîne LOD ;
- imposteurs ;
- profils de distance ;
- scène de benchmark ;
- tableau comparatif ;

### Dépendances et continuité

Dépend des assets finalisés et prépare les scènes de terrain, végétation et foule.

### Mode Solo

Quelques profils génériques validés sur les familles principales.

### Mode Studio

Budgets par plateforme, génération en lots contrôlée et revues visuelles automatisées par captures.

### Critères de validation

- réduction mesurée du coût ;
- silhouette acceptable aux distances prévues ;
- transitions sans popping excessif ;

### Frontière

L’optimisation globale du jeu sera traitée dans le Livre IV.

## Chapitre 19 — Rigging et skinning

### Intention

Créer des squelettes et déformations robustes, documentés et compatibles avec Godot et le retargeting.

### Résultats d’apprentissage

- construire squelettes, contrôleurs et contraintes ;
- standardiser noms et orientations d’os ;
- peindre et corriger les poids ;
- préparer accessoires, retargeting et export ;

### Contenu obligatoire

- squelette de déformation et rig de contrôle ;
- orientation, roll et hiérarchie ;
- contraintes et limites articulaires ;
- poids, influences et volumes ;
- twist bones, correctifs et poses extrêmes ;
- sockets et os accessoires ;
- export, rest pose et compatibilité Godot ;

### Livrables

- rigs de référence ;
- conventions d’os ;
- profils de skinning ;
- poses de test ;
- fichiers d’export ;

### Dépendances et continuité

S’appuie sur les personnages, animaux et créatures ; prépare animation et mocap.

### Mode Solo

Un rig de référence stable par grande famille.

### Mode Studio

Normes partagées, propriétaires de rig, tests de compatibilité et bibliothèque de poses.

### Critères de validation

- poses extrêmes sans écrasement majeur ;
- orientation et nomenclature compatibles avec le pipeline ;
- export Godot correct ;

### Frontière

La création des animations appartient au chapitre 20.

## Chapitre 20 — Animation procédurale et animation par keyframes

### Intention

Construire une bibliothèque d’animations expressive et techniquement exploitable, combinant keyframes et ajustements procéduraux.

### Résultats d’apprentissage

- créer poses, cycles, transitions et courbes ;
- organiser couches et blend trees ;
- gérer root motion, événements et boucles ;
- utiliser l’animation procédurale sans masquer les sources ;

### Contenu obligatoire

- principes de pose, timing, spacing et arcs ;
- cycles de locomotion et variations ;
- courbes, tangentes et nettoyage ;
- root motion et vitesse gameplay ;
- événements, contacts et fenêtres d’action ;
- blend trees, couches additives et masques ;
- IK, ajustements procéduraux et tests Godot ;

### Livrables

- cycles de base ;
- bibliothèque d’animations ;
- blend tree pilote ;
- profils d’export ;
- scène Godot animée ;

### Dépendances et continuité

Dépend des rigs du chapitre 19 et prépare mocap, cinématiques et synchronisation faciale.

### Mode Solo

Bibliothèque minimale couvrant les états essentiels avant variantes.

### Mode Studio

Nommage partagé, revues d’animation, versions et tests de transition automatisés.

### Critères de validation

- transitions fluides ;
- vitesse cohérente ;
- absence de glissement visible ;
- événements alignés avec l’action ;

### Frontière

La capture de mouvement est approfondie au chapitre 21.

## Chapitre 21 — Capture de mouvement et retargeting

### Intention

Transformer des données de mocap sourcées en animations dirigées, nettoyées et compatibles avec plusieurs rigs.

### Résultats d’apprentissage

- choisir des sources et vérifier leurs licences ;
- nettoyer bruit, glissements et collisions ;
- mapper et retargeter les squelettes ;
- corriger manuellement le résultat ;

### Contenu obligatoire

- types de capture et limites ;
- provenance, consentement et droits ;
- nettoyage des trajectoires et contacts ;
- mapping des os et poses de référence ;
- retargeting entre proportions différentes ;
- correction des mains, pieds et centre de masse ;
- direction artistique et intégration en bibliothèque ;

### Livrables

- sessions ou clips sourcés ;
- profils de mapping ;
- animations nettoyées ;
- rapport de corrections ;
- tests multi-rigs ;

### Dépendances et continuité

Dépend des rigs et de la bibliothèque d’animation ; peut alimenter cinématiques et gameplay.

### Mode Solo

Utilisation ciblée de clips réellement utiles, avec correction manuelle assumée.

### Mode Studio

Pipeline de capture, stockage des sources, validation des droits et revue animation séparée.

### Critères de validation

- contacts crédibles ;
- rythme cohérent ;
- retargeting stable sur plusieurs morphologies ;
- licences traçables ;

### Frontière

La mocap ne remplace pas la direction d’animation.

## Chapitre 22 — Cinématiques, caméras et mise en scène

### Intention

Transformer une intention narrative en séquence Godot lisible, révisable et intégrée au build.

### Résultats d’apprentissage

- passer du storyboard à l’animatique puis à la séquence ;
- gérer focales, cadrage, mouvements et continuité ;
- synchroniser animation, audio, lumière et VFX ;
- organiser timelines, reprises et versions ;

### Contenu obligatoire

- storyboard, liste de plans et intention dramatique ;
- focales, profondeur, composition et raccords ;
- blocage, animatique et validation du rythme ;
- caméras Godot et timelines ;
- synchronisation des animations, dialogues, lumière et effets ;
- versions, commentaires et reprises ;
- tests dans le build et transitions vers le gameplay ;

### Livrables

- storyboard ;
- animatique ;
- séquence Godot ;
- liste de plans ;
- versions de revue ;

### Dépendances et continuité

Mobilise animation, personnages, décors, audio et VFX.

### Mode Solo

Séquences courtes, priorité au récit et réutilisation des systèmes existants.

### Mode Studio

Rôles séparés mise en scène, animation, lumière, audio et validation narrative.

### Critères de validation

- lecture narrative claire ;
- rythme maîtrisé ;
- séquence fonctionnelle dans le build ;
- aucune dépendance perdue ;

### Frontière

La caméra de gameplay reste dans le Livre II.

## Chapitre 23 — Effets visuels, particules et simulations

### Intention

Créer des effets lisibles, modulaires et budgétés qui renforcent le gameplay et l’ambiance sans les masquer.

### Résultats d’apprentissage

- produire feu, fumée, impacts, magie, météo, fluides corporels, boue, hologramme, éclipse solaire, éclipse lunaire, disque d'accrétion autour d'un trou noir, poussière en suspension dans un rayon de soleil, buée sur une vitre, bulles de savon, geyser, traces de pas et débris ;
- choisir entre GPU, CPU, shader, particules ou simulation précalculée ;
- gérer collisions, pooling, LOD et lumière ;
- fixer des budgets par contexte ;

### Contenu obligatoire

- fonction visuelle et information transmise ;
- particules GPU et CPU ;
- shaders d’effets et distorsion ;
- simulations précalculées et caches ;
- collisions, pooling et durée de vie ;
- éclairage, transparence et overdraw ;
- LOD, variantes de qualité et tests multi-distance ;

### Livrables

- bibliothèque VFX ;
- presets ;
- scènes de test ;
- budgets ;
- variantes de qualité ;

### Dépendances et continuité

S’appuie sur les matériaux et peut utiliser les animations, environnements et systèmes gameplay.

### Mode Solo

Bibliothèque réduite de presets polyvalents et mesurés.

### Mode Studio

Catalogue partagé, budgets par plateforme et validation conjointe art-gameplay-performance.

### Critères de validation

- effet lisible sans masquer l’action ;
- coût dans le budget ;
- comportement stable à plusieurs distances et qualités ;

### Frontière

Ne doit jamais devenir une source de règles gameplay.

## Chapitre 24 — Interface utilisateur

### Intention

Construire un système visuel d’interface cohérent, réutilisable et adaptable aux résolutions et périphériques.

### Résultats d’apprentissage

- définir composants, thèmes, grilles et hiérarchie ;
- créer menus, HUD, inventaires et fenêtres ;
- gérer résolutions, ratios et périphériques ;
- intégrer icônes, animation et feedback ;

### Contenu obligatoire

- design system, tokens et composants ;
- grilles, marges, typographie et hiérarchie ;
- menus, HUD et panneaux complexes ;
- navigation clavier, souris et manette ;
- mise à l’échelle et différents ratios ;
- icônes, états, transitions et feedback ;
- thème Godot et tests multi-résolution ;

### Livrables

- design system UI ;
- composants réutilisables ;
- écrans pilotes ;
- thème Godot ;
- tests multi-résolution ;

### Dépendances et continuité

S’appuie sur la bible visuelle et les systèmes UI du Livre II.

### Mode Solo

Ensemble limité de composants réutilisables évitant les écrans uniques.

### Mode Studio

Bibliothèque de composants versionnée, revue design-développement et tests de régression visuelle.

### Critères de validation

- cohérence visuelle ;
- navigation complète ;
- aucun élément hors écran ;
- états interactifs compréhensibles ;

### Frontière

Les règles UX et l’accessibilité visuelle sont approfondies au chapitre 25.

## Chapitre 25 — Expérience utilisateur et accessibilité visuelle

### Intention

Rendre les interfaces et retours visuels compréhensibles, tolérants aux erreurs et adaptables aux besoins des joueurs.

### Résultats d’apprentissage

- améliorer lisibilité, compréhension et feedback ;
- gérer tailles, contrastes, daltonisme, mouvement et focus ;
- réduire la charge cognitive ;
- tester navigation, erreurs et récupération ;

### Contenu obligatoire

- hiérarchie de l’information et charge cognitive ;
- contrastes, tailles, densité et lisibilité ;
- daltonisme et codages redondants ;
- focus, navigation et ordre logique ;
- réduction ou désactivation des mouvements ;
- messages d’erreur, confirmations et annulation ;
- protocoles de test utilisateur et analyse des retours ;

### Livrables

- checklist UX ;
- profils d’accessibilité ;
- variantes de contraste ;
- scénarios de tests ;
- rapport utilisateur ;

### Dépendances et continuité

Dépend du système UI du chapitre 24 et prépare les validations globales du Livre IV.

### Mode Solo

Tests ciblés avec scénarios prioritaires et réglages simples mais effectifs.

### Mode Studio

Panel de test, critères d’acceptation, suivi des problèmes et responsabilité accessibilité identifiée.

### Critères de validation

- parcours réalisables sans ambiguïté majeure ;
- contrastes et tailles conformes aux objectifs ;
- erreurs récupérables et feedback explicite ;

### Frontière

L’accessibilité audio et des commandes sera complétée dans le Livre IV.

## Chapitre 26 — Voix, bruitages, ambiances et musique

### Intention

Organiser une chaîne audio complète, traçable et intégrée à Godot, depuis la source jusqu’au mix runtime.

### Résultats d’apprentissage

- gérer enregistrement, génération, montage et mixage ;
- maîtriser formats, loudness, boucles, spatialisation et variations ;
- documenter consentement, licences et provenance ;
- intégrer bus et événements audio dans Godot ;

### Contenu obligatoire

- typologie voix, SFX, ambiances et musique ;
- enregistrement, génération et nettoyage ;
- formats, fréquence, canaux et compression ;
- loudness, headroom et cohérence de mix ;
- boucles, variations et anti-répétition ;
- spatialisation, zones et bus Godot ;
- manifestes, consentement et tests mémoire ;

### Livrables

- bibliothèque audio ;
- manifestes de voix ;
- presets de mix ;
- scènes audio ;
- rapport de loudness ;

### Dépendances et continuité

S’appuie sur les outils installés au Livre I et alimente cinématiques, gameplay et synchronisation labiale.

### Mode Solo

Bibliothèque organisée, presets communs et contrôle d’écoute systématique.

### Mode Studio

Rôles séparés enregistrement, montage, intégration et mix, avec validation des droits.

### Critères de validation

- niveaux cohérents ;
- boucles propres ;
- transitions stables ;
- mémoire et voix simultanées dans les budgets ;

### Frontière

Les outils d’installation audio restent dans le Livre I.

## Chapitre 27 — Synchronisation labiale et animation faciale

### Intention

Synchroniser voix, bouche, yeux et gestes de manière intelligible et naturelle, avec plusieurs niveaux de qualité.

### Résultats d’apprentissage

- comprendre phonèmes, visèmes et blendshapes ;
- générer ou annoter des timings ;
- synchroniser voix, visage, regard et gestes ;
- gérer langues, performances et LOD facial ;

### Contenu obligatoire

- phonèmes, visèmes et différences linguistiques ;
- jeu minimal de formes faciales ;
- extraction ou annotation des timings ;
- courbes, coarticulation et transitions ;
- regard, clignements et gestes complémentaires ;
- profils de langue et de qualité ;
- tests gros plan, distance et foule ;

### Livrables

- jeu de visèmes ;
- pipeline de timing ;
- animation pilote ;
- profils par langue ;
- tests gros plan et distance ;

### Dépendances et continuité

Dépend des visages du chapitre 10, des rigs du chapitre 19 et de l’audio du chapitre 26.

### Mode Solo

Pipeline simple avec correction manuelle sur les dialogues importants.

### Mode Studio

Outils d’annotation, conventions multilingues, revue d’acting et profils de qualité par plateforme.

### Critères de validation

- dialogue intelligible ;
- mouvements stables et non mécaniques ;
- LOD facial cohérent ;
- résultat acceptable sur plusieurs voix ;

### Frontière

Ne remplace pas le jeu d’acteur ni la direction des performances.

## Chapitre 28 — Importation et intégration dans Godot

### Intention

Rendre l’import et la réimportation des assets reproductibles sans perdre les personnalisations réalisées dans Godot.

### Résultats d’apprentissage

- configurer les presets d’import ;
- gérer scènes importées, héritées et réimportation ;
- associer matériaux, animations, collisions et scripts ;
- automatiser les réglages répétitifs ;

### Contenu obligatoire

- formats d’échange et choix selon l’usage ;
- presets d’import par famille d’asset ;
- scènes importées et scènes d’intégration ;
- matériaux externes ou remappés ;
- animations, pistes, collisions et sockets ;
- scripts post-import et métadonnées ;
- réimportation, diff et protection des personnalisations ;

### Livrables

- presets d’import ;
- scènes d’intégration ;
- scripts post-import ;
- matrice format-usage ;
- checklist de réimport ;

### Dépendances et continuité

Consolide l’ensemble des assets produits aux chapitres précédents.

### Mode Solo

Presets simples et scènes héritées pour limiter les manipulations manuelles.

### Mode Studio

Automatisation post-import, contrats par famille et contrôle des changements lors de la réimportation.

### Critères de validation

- réimport reproductible ;
- aucune personnalisation Godot perdue ;
- matériaux, animations et collisions associés correctement ;

### Frontière

N’introduit pas de nouvelle logique métier dans les assets importés.

## Chapitre 29 — Validation technique et artistique des assets

### Intention

Créer une porte qualité répétable qui combine conformité artistique, budgets, intégrité technique et traçabilité.

### Résultats d’apprentissage

- comparer les assets à la bible visuelle et aux budgets ;
- vérifier formats, pivots, matériaux, collisions, rigs et LOD ;
- produire rapports, statuts et demandes de correction ;
- rendre le contrôle reproductible par une autre personne ou un script ;

### Contenu obligatoire

- états d’asset et responsabilités ;
- checklist universelle et extensions par famille ;
- contrôles de provenance et licence ;
- contrôles techniques automatisables ;
- revue artistique et comparaison aux références ;
- scènes Godot de validation ;
- rapport, refus, correction et acceptation finale ;

### Livrables

- checklist universelle ;
- scènes de validation ;
- rapport d’asset ;
- système de statut ;
- critères d’acceptation finale ;

### Dépendances et continuité

S’appuie sur toutes les règles des chapitres 1 à 28 et prépare l’automatisation du chapitre 30.

### Mode Solo

Checklist unique et revue personnelle différée pour réduire les biais.

### Mode Studio

Double validation artistique et technique, propriétaires, SLA de correction et tableaux de statut.

### Critères de validation

- même résultat obtenu par une autre personne ;
- tous les écarts sont documentés ;
- aucun asset accepté sans provenance, budget et test Godot ;

### Frontière

Ne remplace pas la QA du jeu complet.

## Chapitre 30 — Automatisation Blender, ComfyUI et production en lots

### Intention

Automatiser les tâches répétitives de production sans déléguer les décisions artistiques ni masquer les erreurs.

### Résultats d’apprentissage

- écrire des scripts Blender et orchestrer des files ComfyUI ;
- gérer lots, reprise, seeds, erreurs et déterminisme ;
- produire manifestes, journaux et rapports ;
- intégrer les contrôles techniques à la CI ;

### Contenu obligatoire

- sélection des tâches réellement automatisables ;
- scripts Blender idempotents et paramétrés ;
- queues ComfyUI, workflows et seeds ;
- manifestes de lot, identités et provenance ;
- reprise après échec et limites de tentatives ;
- échantillonnage, comparaison et validation humaine ;
- intégration CI, artefacts et rapports ;

### Livrables

- scripts de lots ;
- templates de manifestes ;
- workflows automatisés ;
- rapports de production ;
- exemples pour le Companion Pack ;

### Dépendances et continuité

Utilise les contrats, formats et portes qualité de tout le Livre III ainsi que l’automatisation Python du Livre II.

### Mode Solo

Scripts transparents, petits lots et contrôle manuel fréquent.

### Mode Studio

Orchestration partagée, files, artefacts, reprise, quotas et approbation indépendante des lots.

### Critères de validation

- reprise après échec démontrée ;
- traçabilité complète du lot ;
- résultats déterministes lorsque le procédé le permet ;
- échantillons validés humainement ;

### Frontière

L’automatisation ne peut jamais déclarer seule la qualité artistique.

## 8. Critères de clôture du Livre III

Le Livre III pourra être déclaré terminé lorsque :

- les trente chapitres sont rédigés, repérés et audités ;
- les explications de blocs sont proportionnées et toutes les sections d’erreurs respectent la structure sémantique ;
- un asset pilote complet traverse la chaîne concept → source → production → optimisation → validation → Godot ;
- les règles de provenance, licences et consentements sont appliquées ;
- les budgets sont mesurés sur le matériel de référence ;
- les scènes de validation et presets d’import sont reproductibles ;
- les livrables réutilisables sont versés au Companion Pack ;
- le PDF lecteur est compilé sans protocoles, audits, preuves ou rapports internes ;
- le PDF est inspecté visuellement ;
- `CONTINUITE-PROJET.md`, `ROADMAP.md`, l’index du Livre III, `contents.txt` et les preuves QA internes sont à jour.

## 9. Ordre de démarrage

La première action éditoriale du Livre III est :

`Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md`

Avant sa rédaction, une nouvelle conversation doit vérifier l’état du dépôt, confirmer que le PDF lecteur du Livre II est clos, créer l’index du Livre III s’il n’existe pas encore, puis annoncer le niveau GPT-5.6 Sol recommandé dans la continuité du projet uniquement.
