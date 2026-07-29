---
title: "Livre V — Fiche 18 : Référence graphique et 3D"
id: "DOC-L5-CH18"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 18
last-verified: "2026-07-29T13:59:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T13:59:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-18.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "graphics-and-3d-reference"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-tools:
  blender:
    version: "5.2.0"
    channel: "Stable"
    qualification: "documentation-reviewed"
  exchange:
    format: "glTF 2.0"
    default-container: "GLB"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Référence graphique et 3D

> **Type de document :** tables techniques, cartes de convention, matrices de choix, diagrammes compacts et index de contrôles visuels.
> **Référence projet :** Blender `5.2.0` Stable, glTF 2.0 / GLB, Godot `4.7.1-stable` et rendu Forward+.
> **Principe :** une convention 3D n’est valide que si la source, la transformation, la livraison, l’import, le contexte de rendu et le niveau de preuve restent distingués.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat d’une référence 3D | [G3D-00](#g3d-00--contrat-dune-référence-graphique-et-3d) |
| trouver la source propriétaire | [Matrice A](#matrice-a--entrée-par-problème-ou-livrable) |
| contrôler unités, axes et transforms | [G3D-01](#g3d-01--unités-axes-et-transformations) |
| fixer origine, pivot, limites et sockets | [G3D-02](#g3d-02--origines-pivots-limites-et-sockets) |
| choisir un format d’échange | [Matrice B](#matrice-b--formats-et-chemins-déchange) |
| séparer source, export et intégration | [G3D-03](#g3d-03--cycle-de-vie-de-lasset-3d) |
| relire un matériau PBR | [G3D-04](#g3d-04--pbr-canaux-et-espaces-colorimétriques) |
| contrôler UV, densité et baking | [G3D-05](#g3d-05--uv-densité-de-texels-et-baking) |
| vérifier géométrie, normales et tangentes | [G3D-06](#g3d-06--géométrie-topologie-normales-et-tangentes) |
| choisir LOD, HLOD ou imposteur | [G3D-07](#g3d-07--lod-hlod-imposteurs-et-proxies) |
| relire squelette, skinning et retargeting | [G3D-08](#g3d-08--rigging-skinning-et-retargeting) |
| protéger import et réimportation | [G3D-09](#g3d-09--import-réimportation-et-personnalisations-godot) |
| encadrer les budgets et mesures | [G3D-10](#g3d-10--budgets-profils-et-mesures) |
| préparer une comparaison de pilotes | [G3D-11](#g3d-11--presets-checklists-et-comparaison-des-pilotes) |
| distinguer les niveaux de preuve | [Matrice C](#matrice-c--preuves-et-portes-de-promotion) |
| diagnostiquer un défaut visuel | [G3D-12](#g3d-12--symptômes-visuels-diagnostics-et-acceptation) |

---

<!-- l5:card -->
## G3D-00 — Contrat d’une référence graphique et 3D

| Champ | Question obligatoire |
|---|---|
| besoin | quelle décision technique ou visuelle doit être prise |
| famille | texture, matériau, maillage, rig, animation, décor ou scène intégrée |
| source | quel fichier ou chapitre possède la méthode et l’intention |
| unité | quelle grandeur est mesurée et dans quelle unité |
| repère | quels axes, origine, pivot, pose ou espace colorimétrique s’appliquent |
| format | quelle information doit traverser l’échange |
| transformation | quelle opération produit le dérivé |
| livraison | quel fichier est destiné à l’import ou à la revue |
| profil | quel usage, renderer, distance, caméra ou plateforme est visé |
| preuve | revue statique, import, capture, mesure ou acceptation humaine |
| réserve | quelle étape n’a pas été exécutée ou qualifiée |
| retrait | quel changement invalide le preset, le budget ou le résultat |

**Réponse rapide :** partir du [pipeline Blender et de ses responsabilités de fichiers](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#5-responsabilités-des-fichiers), puis rejoindre le chapitre propriétaire de la famille. La fiche décrit le vocabulaire et les portes ; elle ne remplace ni la production du Livre III ni la [validation d’un candidat individuel](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#1-rôle-du-chapitre).

**Diagramme compact :** `intention → source canonique → dérivé de travail → livraison → import → scène d’intégration → preuve → décision`.

**Limite :** une valeur chiffrée sans asset, caméra, renderer, plateforme et protocole n’est pas un budget approuvé.

---

<!-- l5:matrix -->
## Matrice A — Entrée par problème ou livrable

| Problème ou livrable | Carte | Source propriétaire |
|---|---|---|
| mauvaise taille ou rotation après import | [G3D-01](#g3d-01--unités-axes-et-transformations) | [unités et axes Blender–Godot](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#10-fixer-les-unités-et-léchelle) |
| objet qui tourne ou s’aligne mal | [G3D-02](#g3d-02--origines-pivots-limites-et-sockets) | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) |
| choix GLB, glTF séparé, `.blend`, FBX ou OBJ | [Matrice B](#matrice-b--formats-et-chemins-déchange) | [importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#2-résultats-dapprentissage) |
| matériau trop brillant, terne ou incohérent | [G3D-04](#g3d-04--pbr-canaux-et-espaces-colorimétriques) | [pipeline PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md#6-contrat-dun-matériau) |
| seams, distorsion ou bake incorrect | [G3D-05](#g3d-05--uv-densité-de-texels-et-baking) | [UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md#1-rôle-du-chapitre) |
| facettes, ombrage ou normales inversées | [G3D-06](#g3d-06--géométrie-topologie-normales-et-tangentes) | [UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md) |
| chaîne de représentations lointaines | [G3D-07](#g3d-07--lod-hlod-imposteurs-et-proxies) | [LOD et imposteurs](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md#1-rôle-du-chapitre) |
| déformation, poids ou socket instable | [G3D-08](#g3d-08--rigging-skinning-et-retargeting) | [rigging et skinning](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md#1-rôle-du-chapitre) |
| clip incompatible avec un autre rig | [G3D-08](#g3d-08--rigging-skinning-et-retargeting) | [capture et retargeting](../Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md#4-frontières-avec-les-chapitres-voisins) |
| personnalisation perdue à la réimportation | [G3D-09](#g3d-09--import-réimportation-et-personnalisations-godot) | [modèle mental de l’import](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#6-modèle-mental-de-la-chaîne-dimport) |
| budget ou performance supposée | [G3D-10](#g3d-10--budgets-profils-et-mesures) | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) |
| décision d’acceptation d’un asset | [G3D-11](#g3d-11--presets-checklists-et-comparaison-des-pilotes) | [porte qualité](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#5-pilote-de-validation-de-project-asteria) |

**Décision :** ouvrir d’abord la carte du symptôme, puis suivre le lien vers la méthode propriétaire. Un même défaut apparent peut provenir de la source, de l’échange, de l’import, du renderer ou du contexte de mesure.

---

<!-- l5:card -->
## G3D-01 — Unités, axes et transformations

| Élément | Convention `Project Asteria` | Contrôle |
|---|---|---|
| système | métrique | `Unit System = Metric` |
| échelle Blender | `1 unité = 1 mètre` | cube étalon de `1 m × 1 m × 1 m` |
| `Unit Scale` | `1.0` | ne répare jamais une géométrie mal dimensionnée |
| haut Blender | `+Z` | sol à `Z = 0` |
| avant Blender | `-Y` | asset orienté sans parent correctif |
| haut Godot | `+Y` | boîte englobante et placement contrôlés |
| avant du modèle Godot | `+Z` | conversion assurée par glTF et l’importeur |
| translation | appliquée selon pivot fonctionnel | comparer source et scène d’intégration |
| rotation | cohérente avant export | absence de parent tourné à `90°` |
| échelle objet | finie et documentée | examiner les conséquences avant application |

**Réponse rapide :** utiliser le contrat [« une unité Blender représente un mètre »](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#10-fixer-les-unités-et-léchelle) et la [correspondance des axes Blender–Godot](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#11-comprendre-les-axes-blender-et-godot). Corriger la source, pas l’affichage des unités ni un parent de compensation.

**Diagramme compact :** `Blender : Z haut, -Y avant → glTF 2.0 → Godot : Y haut, +Z avant`.

**Validation minimale :** dimensions du cube, orientation d’un marqueur avant, position du sol, transform racine et absence de scale exotique après import.

**Limite :** appliquer toutes les transformations peut modifier rigs, contraintes, hiérarchies et baking ; l’opération dépend de la famille d’asset.

---

<!-- l5:card -->
## G3D-02 — Origines, pivots, limites et sockets

| Élément | Usage | Invariant |
|---|---|---|
| origine objet | référence des transforms | stable après publication |
| pivot fonctionnel | charnière, roue, porte, outil ou placement | placé selon le mouvement attendu |
| point de sol | alignement et placement | distinct du centre géométrique si nécessaire |
| boîte englobante | culling, visibilité et contrôle de taille | couvre l’asset utile sans devenir artificiellement immense |
| socket visuel | attache d’accessoire ou effet | nom et transform versionnés |
| `BoneAttachment3D` | suivi d’un os importé | ne possède aucune autorité gameplay |
| collision guide | aide de production | séparé du mesh de rendu et du contrat gameplay |
| nom d’objet | lisibilité et mapping | ne remplace pas un identifiant stable |
| collection d’export | frontière de livraison | une unique collection `__EXPORT` qualifiée |

**Réponse rapide :** définir le pivot selon la fonction observable avant publication, puis conserver une nouvelle version si sa position change. Les conventions de noms et collections restent dans le [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#7-convention-didentifiants-noms-et-versions), tandis que les sockets squelettiques sont approfondis par le [chapitre de rigging](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md).

**Alternative :** un objet statique peut utiliser une origine simple au point de placement ; un mécanisme articulé exige plusieurs pivots ou pièces clairement séparées.

**Validation minimale :** rotation autour de l’axe attendu, placement sur un gabarit, AABB cohérente, socket testé avec un proxy et réimportation sans glissement.

**Limite :** un socket, un suffixe ou une proximité spatiale ne crée ni propriété, ni équipement, ni droit d’interaction.

---

<!-- l5:matrix -->
## Matrice B — Formats et chemins d’échange

| Format ou chemin | Usage pertinent | Préserve ou facilite | Limites principales |
|---|---|---|---|
| GLB | livraison 3D par défaut | scène glTF dans un fichier portable | moins pratique pour inspecter séparément les dépendances |
| glTF séparé | revue et diagnostic détaillés | JSON, buffers et images visibles | plusieurs fichiers à maintenir comme un lot |
| `.blend` direct | itération Solo encadrée | source ouverte depuis Blender installé | dépend d’une version Blender qualifiée ; non recommandé comme livraison Studio |
| FBX via importeur Godot | échange hérité lorsque nécessaire | certains pipelines existants | format et implémentations plus variables ; qualifier le cas réel |
| OBJ | géométrie statique simple | positions, UV et normales selon export | pas de squelette, animation ou blendshapes adaptés au personnage |
| image source sans perte | travail et archivage | précision et réédition | taille et compatibilité runtime à traiter séparément |
| texture runtime | import Godot selon profil | mipmaps et compression adaptées à l’usage | résultat dépend du profil, de la plateforme et du renderer |
| scène importée Godot | surface générée | structure dérivée de la livraison | ne pas éditer comme surface de personnalisation durable |
| scène d’intégration | composition propre au jeu | scripts, collisions, remaps et dépendances du projet | doit survivre à la réimportation |

**Réponse rapide :** retenir GLB comme livraison par défaut, glTF séparé pour l’inspection et `.blend` direct seulement comme variante Solo dépendante de Blender. La matrice complète et les profils appartiennent au [chapitre d’importation](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#2-résultats-dapprentissage).

**Décision :** choisir le format d’après les données à préserver, la portabilité, la capacité de diagnostic et l’environnement de production ; jamais d’après l’extension la plus familière.

---

<!-- l5:card -->
## G3D-03 — Cycle de vie de l’asset 3D

| État | Autorité | Peut être régénéré ? |
|---|---|---|
| référence approuvée | intention et critères visuels | non, sans nouvelle décision |
| source canonique `.blend` | construction modifiable | non depuis l’export seul |
| fichier de travail | expérimentation locale | oui ou abandonné |
| bibliothèque liée | contenu partagé gouverné | selon sa propre source |
| cache auteur | accélération locale | oui |
| export | résultat d’échange | oui depuis la source et le preset |
| livraison | candidat versionné avec manifeste | oui, mais produit une nouvelle révision |
| sidecar `<asset>.import` | configuration d’import Godot | oui, mais versionné |
| cache `.godot/imported` | dérivé moteur local | oui |
| scène importée | surface générée | oui |
| scène d’intégration | personnalisations du jeu | non depuis la livraison seule |
| preuve | captures, rapports, mesures, décisions | non sans perdre la traçabilité |

**Réponse rapide :** ne jamais confondre la source, l’export, la livraison et les surfaces générées. Le [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#5-responsabilités-des-fichiers) possède l’amont ; le [modèle mental de l’import Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#6-modèle-mental-de-la-chaîne-dimport) possède l’aval.

**Diagramme compact :** `.blend source → preset + __EXPORT → GLB livraison → .import versionné → cache .godot → scène importée → scène d’intégration`.

**Validation minimale :** chaque fichier a un statut, un propriétaire, une version, des dépendances et une procédure de reconstruction ou de restauration.

**Limite :** une livraison approuvée est immuable ; toute correction produit une nouvelle révision candidate et relance les contrôles affectés.

---

<!-- l5:card -->
## G3D-04 — PBR, canaux et espaces colorimétriques

| Canal ou donnée | Sens | Traitement de référence |
|---|---|---|
| base color | couleur de surface sans éclairage peint | sRGB |
| metallic | caractère conducteur ou diélectrique du modèle metallic-roughness | donnée linéaire |
| roughness | largeur et netteté de la réflexion | donnée linéaire |
| normal tangent | perturbation locale de la normale | donnée linéaire, convention OpenGL pour Godot |
| ambient occlusion | atténuation locale de cavités | donnée linéaire |
| height | hauteur ou déplacement candidat | donnée linéaire, usage qualifié |
| emissive | émission visuelle | couleur, avec intensité et contexte documentés |
| opacity | couverture ou transparence | choix de mode et coût à qualifier |
| transmission | passage de lumière candidat | dépend du matériau et du renderer |
| subsurface | diffusion sous la surface | réservé aux familles qui le nécessitent |
| ORM | packing occlusion–roughness–metallic | canaux et ordre explicitement vérifiés |

**Réponse rapide :** assigner un rôle unique à chaque image et distinguer les cartes de couleur des cartes de données. Le contrat complet est défini par le [pipeline PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md#6-contrat-dun-matériau), avec comparaison sous plusieurs éclairages et sans supposer une identité automatique entre Blender et Godot.

**Alternative :** `StandardMaterial3D` convient à une composition explicite de cartes ; `ORMMaterial3D` convient lorsque le packing et le profil d’import sont réellement gouvernés.

**Validation minimale :** sphère lisse, géométrie facettée, vue rasante, éclairages neutre/chaud/froid/contrasté, mipmaps, répétition, compression et captures verrouillées.

**Limite :** une texture plus grande, un shader plus complexe ou un matériau plus brillant n’est pas automatiquement plus fidèle ni plus coûteux de la même manière sur toutes les plateformes.

---

<!-- l5:card -->
## G3D-05 — UV, densité de texels et baking

| Élément | Question de contrôle |
|---|---|
| seams | suivent-ils les ruptures de forme, de matériau ou de visibilité |
| îlots | sont-ils orientés et regroupés selon l’usage |
| distorsion | le checker révèle-t-il étirement ou compression |
| densité de texels | est-elle cohérente avec la taille réelle et l’importance visuelle |
| marges | restent-elles suffisantes avec mipmaps et résolution cible |
| chevauchements | sont-ils intentionnels, documentés et compatibles avec le bake |
| triangulation | est-elle stable avant le bake final et l’export |
| high poly | porte-t-il le détail à transférer |
| low poly | préserve-t-il silhouette, shading et déformation |
| cage | couvre-t-elle les surfaces sans capturer les voisines |
| normal map | utilise-t-elle la convention tangentielle attendue |
| dilation | évite-t-elle les bords contaminés |
| comparaison | Blender et Godot montrent-ils le même sens de relief |

**Réponse rapide :** stabiliser topologie, seams, UV, tangentes et triangulation avant le bake définitif. Le déroulement propriétaire reste dans [UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md#1-rôle-du-chapitre) ; le [pipeline PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md#4-périmètre-et-frontières) reçoit ensuite les cartes qualifiées.

**Diagramme compact :** `high poly + low poly → UV et triangulation gelées → cage → bake → contrôle multi-angle → GLB → comparaison tangentielle Godot`.

**Alternative :** une géométrie simple ou un matériau tilable peut ne nécessiter aucun bake haute-vers-basse résolution ; ne pas créer une cage sans besoin observable.

**Limite :** une densité de texels unique pour toute la production ignore taille réelle, distance, caméra, fonction et plateforme.

---

<!-- l5:card -->
## G3D-06 — Géométrie, topologie, normales et tangentes

| Signal | Contrôle |
|---|---|
| silhouette | reste lisible aux distances et angles cibles |
| edge flow | accompagne déformation, courbure et contacts utiles |
| densité locale | suit les besoins de forme plutôt qu’une uniformité abstraite |
| triangles | acceptables lorsqu’ils restent contrôlés et stables |
| n-gons | exclus des zones où triangulation ou déformation devient imprévisible |
| arêtes dures | cohérentes avec seams, normales et intention de shading |
| normales | orientées, finies et cohérentes entre surfaces |
| tangentes | présentes lorsque le matériau tangent-space l’exige |
| sommets exportés | mesurés séparément des sommets Blender apparents |
| surfaces | limitées selon matériaux et passes nécessaires |
| modificateurs | appliqués ou exportés selon un contrat explicite |
| géométrie cachée | retirée seulement si aucun usage futur ou silhouette ne la requiert |

**Réponse rapide :** juger la topologie par la silhouette, la déformation, le shading et l’échange, pas par l’obligation de tout convertir en quads. Les procédures restent dans le [chapitre 17 du Livre III](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md), puis la chaîne de coût géométrique est qualifiée dans le [chapitre LOD](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md).

**Validation minimale :** vues de silhouette, affichage des normales, poses ou articulations pertinentes, triangulation contrôlée, export GLB et comparaison du mesh importé.

**Limite :** le ratio de polygones seul ne mesure ni les sommets exportés, ni les surfaces, ni les draw calls, ni l’overdraw, ni le coût d’ombre.

---

<!-- l5:card -->
## G3D-07 — LOD, HLOD, imposteurs et proxies

| Représentation | Rôle | Ne doit pas devenir |
|---|---|---|
| LOD0 | référence visuelle approuvée | cible modifiée après dérivation silencieuse |
| LOD manuel | simplification artistique contrôlée | pourcentage arbitraire universel |
| LOD automatique Godot | variante générée à inspecter | acceptation sans revue humaine |
| HLOD | regroupement lointain d’un ensemble | fusion globale détruisant le culling |
| imposteur | atlas multi-vues avec alpha et orientation | simple capture sans padding ni profondeur |
| billboard | représentation plane orientée | remplacement de proximité non qualifié |
| proxy d’ombre | silhouette d’ombre simplifiée | géométrie gameplay |
| proxy de collision | collision simplifiée gouvernée séparément | conséquence automatique du LOD visuel |
| plage de visibilité | sélection selon taille et contexte | distance unique supposée universelle |
| hystérésis | limite les oscillations de transition | cache d’un mauvais seuil |
| `lod_bias` | diagnostic et réglage global candidat | réparation d’une chaîne mal conçue |

**Réponse rapide :** dériver chaque niveau depuis un LOD0 gelé, puis comparer taille écran, silhouette, matériaux, ombres, AABB et coût réel. Les responsabilités complètes sont au [chapitre LOD](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md#1-rôle-du-chapitre).

**Diagramme compact :** `LOD0 gelé → LOD1 → LOD2 → proxy lointain → imposteur/billboard si pertinent`, avec revue et mesure à chaque étape.

**Alternative :** pour un asset rarement visible ou très simple, conserver un seul mesh peut être moins risqué qu’une chaîne de transitions et de ressources supplémentaires.

**Limite :** les fades `SELF` et `DEPENDENCIES` ne sont pas supposés équivalents entre Forward+, Mobile et Compatibility ; toute promesse dépend du renderer testé.

---

<!-- l5:card -->
## G3D-08 — Rigging, skinning et retargeting

| Élément | Contrat |
|---|---|
| squelette de déformation | hiérarchie exportée qui déforme réellement le mesh |
| rig de contrôle | mécanismes auteur non exportés sauf besoin explicite |
| rest pose | interface versionnée entre mesh, rig et animation |
| roll et axes locaux | cohérents par chaîne et fonction |
| bind | relation gelée entre mesh et squelette |
| poids | normalisés et vérifiés dans une grille de poses |
| influences | limitées selon le profil mesuré, sans nettoyage aveugle |
| correctifs | identifiés, versionnés et testés dans les poses concernées |
| `Skeleton3D` | représentation importée du squelette |
| `BoneMap` / `SkeletonProfile` | mapping fonctionnel, pas simple rapprochement de noms |
| socket osseux | attache visuelle versionnée |
| retargeting | compare hiérarchie, axes, pose de référence, proportions et contacts |
| clip baké | voie de référence pour une livraison stable |
| retargeting runtime | variante à mesurer avant adoption |

**Réponse rapide :** séparer squelette de déformation et rig de contrôle, puis valider poids et rest pose en mouvement. Le [chapitre 19](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md#1-rôle-du-chapitre) possède le rig et le skinning ; le [chapitre 21](../Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md#4-frontières-avec-les-chapitres-voisins) possède capture, mapping et retargeting.

**Diagramme compact :** `mesh approuvé → rest pose → squelette de déformation → bind et poids → poses extrêmes → GLB filtré → Skeleton3D/BoneMap → test multi-rigs`.

**Validation minimale :** pose neutre, flexions extrêmes, torsions, contacts, volume, sockets, import, mapping et au moins plusieurs morphologies lorsque la compatibilité multi-rigs est revendiquée.

**Limite :** des noms d’os identiques ne prouvent ni hiérarchie, ni axes, ni roll, ni proportions, ni compatibilité de pose.

---

<!-- l5:card -->
## G3D-09 — Import, réimportation et personnalisations Godot

| Élément | Politique |
|---|---|
| livraison | versionnée et accompagnée de son manifeste |
| `<asset>.import` | configuration versionnée |
| `.godot/imported` | cache régénérable, exclu du dépôt |
| scène importée | surface générée, non éditée comme source durable |
| scène héritée | adaptation lorsque l’héritage reste stable |
| scène de composition | enveloppe préférée pour dépendances et scripts du jeu |
| ressource externe | matériau, animation ou donnée réutilisable |
| remap matériau | relation durable entre import et ressource du projet |
| profil d’import | paramètres par famille d’asset |
| suffixe ou métadonnée | aide d’outil, jamais autorité gameplay |
| post-import | idempotent, borné, inspectable et non récursif |
| baseline | structure et preuves de la version approuvée |
| candidat | changements attendus et diff documentés |
| rollback | retour à la livraison et au preset précédents |

**Réponse rapide :** protéger les personnalisations en les plaçant hors de la scène importée. Le [chapitre d’importation](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) définit formats, profils, remaps et réimportation ; la [porte qualité](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#4-frontières-avec-les-chapitres-voisins) décide ensuite l’acceptation.

**Diagramme compact :** `livraison vN + preset → import dérivé → diff structurel → scène d’intégration inchangée ou migrée → contrôles → promotion/rollback`.

**Validation minimale :** import depuis un workspace propre, suppression du cache régénérable, réimportation, comparaison de structure, matériaux, rigs, animations, collisions, sockets et LOD.

**Limite :** un import terminé sans message bloquant ne prouve ni fidélité artistique, ni performance, ni droits, ni préservation de toutes les personnalisations.

---

<!-- l5:card -->
## G3D-10 — Budgets, profils et mesures

| Dimension | Mesure distincte |
|---|---|
| géométrie | triangles, sommets exportés, surfaces et instances |
| rendu | draw calls, passes, ombres, transparence et overdraw |
| textures | dimensions, formats, mipmaps, compression et mémoire |
| matériaux | variantes, shaders, paramètres et compilations |
| animation | os, influences, clips, pistes et fréquence d’évaluation |
| mémoire | RAM, mémoire privée, VRAM et ressources résidentes |
| temps | import, chargement, CPU, GPU et durée de frame |
| perception | taille écran, distance, FOV, résolution et importance visuelle |
| scène | AABB, culling, occlusion, lumière et caméra |
| plateforme | OS, GPU, pilote, renderer, résolution et profil graphique |
| protocole | chauffe, répétitions, baseline, parcours et tolérances |
| qualité | captures comparables, artefacts, silhouette et lisibilité |

**Réponse rapide :** traiter tout budget comme une hypothèse versionnée jusqu’à une campagne comparable. Les méthodes de mesure restent au [Livre IV, profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md), à l’[optimisation mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) et aux [chargements](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md).

**Alternative :** une porte documentaire peut exiger que les champs soient présents sans fixer de seuil universel ; chaque profil de famille ou plateforme porte ensuite ses valeurs approuvées.

**Validation minimale :** une seule variable principale modifiée, environnement enregistré, répétitions, données brutes, statistiques adaptées, captures comparables et non-régression fonctionnelle.

**Limite :** FPS, triangles, draw calls ou mémoire pris isolément ne permettent pas d’attribuer une cause ni d’accepter une optimisation.

---

<!-- l5:card -->
## G3D-11 — Presets, checklists et comparaison des pilotes

| Objet | Contenu minimal |
|---|---|
| preset auteur | version outil, unités, axes, collection, options et famille |
| preset export | format, collection, transforms, données incluses et exclusions |
| profil texture | rôle, espace colorimétrique, mipmaps, compression et plateforme |
| profil matériau | workflow, canaux, paramètres, renderer et éclairages de contrôle |
| profil mesh | famille, échelle, pivot, UV, normales, tangentes, surfaces et LOD |
| profil rig | rest pose, hiérarchie, mapping, influences, sockets et animations |
| profil import | format, remaps, collisions, LOD, animations et post-import |
| manifeste | identités, versions, dépendances, empreintes et provenance |
| checklist | critères universels plus extension de famille |
| comparaison | baseline, candidat, changements attendus, captures et mesures |
| décision | accepté, changements demandés, rejeté ou dérogation limitée |
| invalidation | source, preset, outil, renderer, plateforme ou dépendance modifiés |

**Réponse rapide :** un preset est une configuration versionnée, pas une preuve de qualité. Comparer les pilotes documentaires `AST-MAT-LAB-PBR-001`, `AST-BAKE-PILOT-RELAY-001`, `AST-LOD-PILOT-SIGNAL-TOWER-001`, `AST-RIG-PILOT-SCOUT-001`, `AST-IMPORT-PILOT-SCOUT-RELAY-001` et `AST-ASSET-GATE-SCOUT-RELAY-001` seulement après matérialisation de leurs assets et scènes.

La [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#5-pilote-de-validation-de-project-asteria) exige identité, provenance, intégrité, import Godot, contrôle technique et revue artistique. L’[importation](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#5-pilote-dintégration-de-project-asteria) fournit l’entrée intégrée.

**Checklist compacte :** identité stable ; source et livraison distinctes ; droits qualifiés ; unités et axes contrôlés ; pivot et AABB cohérents ; PBR et UV vérifiés ; LOD/rig selon la famille ; import propre ; réimportation déterministe ; captures et mesures contextualisées ; décision humaine tracée.

**Limite :** cette fiche ne contient aucun preset exécutable ni asset pilote réel ; les fichiers réutilisables restent au Companion Pack.

---

<!-- l5:matrix -->
## Matrice C — Preuves et portes de promotion

| Niveau | Preuve disponible | Autorise | N’autorise pas |
|---|---|---|---|
| `documentation-reviewed` | conventions et liens relus | publier la fiche documentaire | annoncer un asset fonctionnel |
| `source-inspected` | source ouverte et structure contrôlée | corriger la source | affirmer un export fidèle |
| `export-produced` | livraison et manifeste créés | lancer l’import | déclarer la qualité Godot |
| `import-checked` | structure, matériaux et dépendances inspectés | créer ou vérifier l’intégration | revendiquer un budget runtime |
| `reimport-checked` | baseline, diff et personnalisations préservées | promouvoir le preset d’import | accepter l’art ou les droits |
| `runtime-measured` | protocole, données et captures comparables | qualifier un profil sur les plateformes testées | généraliser aux plateformes non testées |
| `technical-approved` | blockers techniques nuls ou dérogés | ouvrir la revue artistique | déclarer la conformité artistique |
| `art-approved` | revue humaine contre bible et contexte | ouvrir la décision de publication | remplacer la revue juridique |
| `publishable` | droits, technique, art, preuves et décisions complets | publier le candidat identifié | réutiliser automatiquement la décision pour une nouvelle version |

**Décision :** le niveau le plus faible encore ouvert borne l’affirmation possible. Une absence de test signifie « non vérifié », pas « incompatible » ni « conforme ».

---

<!-- l5:card -->
## G3D-12 — Symptômes visuels, diagnostics et acceptation

| Symptôme | Vérification prioritaire | Cause possible | Source propriétaire |
|---|---|---|---|
| asset cent fois trop petit ou grand | dimensions réelles et `Unit Scale` | géométrie source incorrecte | [erreurs du pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#37-erreurs-fréquentes-et-corrections) |
| asset couché ou inversé | axes source, avant et transform racine | parent correctif ou convention incohérente | [axes Blender–Godot](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md#11-comprendre-les-axes-blender-et-godot) |
| rotation autour d’un point absurde | origine et pivot fonctionnel | pivot déplacé ou appliqué tardivement | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) |
| texture délavée ou trop sombre | espace sRGB ou données linéaires | profil de canal incorrect | [pipeline PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md#6-contrat-dun-matériau) |
| relief inversé | convention de normale et canal vert | normale DirectX utilisée comme OpenGL | [UV et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md) |
| seams visibles à distance | marges, mipmaps, dilation et tangentes | UV ou bake insuffisamment stabilisés | [UV et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md#1-rôle-du-chapitre) |
| facettes ou éclats de lumière | normales, arêtes dures et triangulation | shading incohérent | [retopologie](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md) |
| popping LOD | seuils, hystérésis, silhouette et AABB | plages mal qualifiées | [LOD et imposteurs](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md) |
| imposteur bordé ou incorrect de biais | padding, alpha, angles et orientation | atlas non qualifié | [LOD et imposteurs](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md#1-rôle-du-chapitre) |
| volume écrasé en animation | poids, influences, roll et rest pose | skinning non vérifié en poses extrêmes | [rigging](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md#1-rôle-du-chapitre) |
| pied ou main glisse après retargeting | pose de référence, proportions et contacts | mapping fondé sur les noms seuls | [retargeting](../Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md) |
| matériau revient à l’état importé | remap, ressource externe et scène d’intégration | édition directe d’une surface générée | [importation](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#6-modèle-mental-de-la-chaîne-dimport) |
| cache ou sidecar mal versionné | `.godot/` et `<asset>.import` | autorité de fichiers inversée | [importation](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md) |
| « optimisation » sans gain stable | protocole, baseline, répétitions et qualité | plusieurs variables changées | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) |
| asset « accepté » sans preuve | manifeste, captures, mesures, droits et responsables | décision réduite à « paraît bon » | [porte qualité](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md#1-rôle-du-chapitre) |

**Réponse rapide :** localiser d’abord la frontière où l’écart apparaît : source auteur, export, livraison, import, intégration, rendu ou mesure. Modifier une seule cause candidate, reconstruire le dérivé et comparer à la baseline.

**Porte d’acceptation compacte :** aucune identité inconnue ; aucune dépendance bloquée ; droits vérifiés ; transforms finis ; unités, axes, pivot et AABB conformes ; données de famille présentes ; import et réimportation contrôlés ; preuves contextualisées ; blockers techniques nuls ; revue artistique humaine ; réserves et dérogations tracées.

**Limite :** cet index oriente le diagnostic. Les exemples fautifs et corrections détaillées restent dans les sections d’erreurs des chapitres propriétaires et le catalogue transversal appartient à la fiche 20.

---

## Sources propriétaires et limites

- [Livre III, chapitre 4 — Pipeline Blender et organisation des fichiers](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)
- [Livre III, chapitre 5 — Provenance, licences et validation des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)
- [Livre III, chapitre 16 — Textures, matériaux et pipeline PBR](../Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md)
- [Livre III, chapitre 17 — UV, retopologie et baking](../Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md)
- [Livre III, chapitre 18 — LOD, imposteurs et optimisation géométrique](../Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md)
- [Livre III, chapitre 19 — Rigging et skinning](../Livre-III/CHAPITRE-19-Rigging-et-skinning.md)
- [Livre III, chapitre 20 — Animation procédurale et animation par keyframes](../Livre-III/CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md)
- [Livre III, chapitre 21 — Capture de mouvement et retargeting](../Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md)
- [Livre III, chapitre 28 — Importation et intégration dans Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md)
- [Livre III, chapitre 29 — Validation technique et artistique des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md)
- [Livre IV, chapitre 7 — Profilage GPU et optimisation du rendu](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md)
- [Livre IV, chapitre 8 — Optimisation RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md)

**Niveau de preuve de cette fiche :** `static-review`. Les décisions sont issues des contrats déjà publiés dans le dépôt. Aucun Blender, Godot, glTF, GLB, mesh, texture, matériau, UV, bake, LOD, imposteur, rig, animation, preset, sidecar, scène, import, capture, benchmark, donnée utilisateur ou asset du Companion Pack n’a été exécuté ou produit pour cette fiche.
