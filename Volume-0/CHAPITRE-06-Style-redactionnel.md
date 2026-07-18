---
title: "Chapitre 6 — Style rédactionnel"
id: "DOC-V0-CH06"
status: "draft"
version: "0.1.0"
---

# Chapitre 6 — Style rédactionnel

Ce chapitre définit la voix, le niveau de détail et les règles de présentation applicables à l’ensemble du guide. Son objectif est de garantir une documentation claire, cohérente, pédagogique et exploitable aussi bien par une personne seule que par une équipe de production.

## 1. Objectifs du style rédactionnel

Le style du guide doit permettre de :

- comprendre une notion sans connaissances préalables inutiles ;
- reproduire une procédure sans interprétation ambiguë ;
- distinguer rapidement les décisions obligatoires des recommandations ;
- retrouver une information grâce à une structure stable ;
- passer progressivement d’une explication simple à une compréhension technique approfondie ;
- conserver une cohérence éditoriale entre tous les volumes.

## 2. Public visé

Le texte doit rester accessible à trois profils simultanément :

1. **Débutant** : découvre le développement de jeux, les outils IA ou les pipelines 3D.
2. **Intermédiaire** : maîtrise déjà certains outils mais souhaite construire un pipeline complet.
3. **Avancé** : recherche une référence structurée, des conventions, des critères de validation et des pistes d’industrialisation.

Une section ne doit jamais supposer une expertise non introduite auparavant. Lorsqu’un prérequis est nécessaire, il doit être expliqué ou référencé explicitement.

## 3. Ton général

Le ton est :

- professionnel ;
- direct ;
- calme ;
- précis ;
- pédagogique ;
- orienté vers l’action.

Le guide évite le ton publicitaire, les superlatifs non justifiés et les promesses absolues. Une technologie est décrite avec ses avantages, ses limites, ses coûts et ses risques.

## 4. Principe « expliquer, montrer, vérifier »

Chaque procédure importante suit autant que possible cette séquence :

1. **Expliquer** : présenter le but, le contexte et les prérequis.
2. **Montrer** : fournir les étapes, commandes, captures, extraits de code ou exemples.
3. **Vérifier** : indiquer le résultat attendu et les contrôles à effectuer.

Lorsque la procédure peut échouer, une section de diagnostic doit indiquer les symptômes probables, les causes et les actions correctives.

## 5. Progression pédagogique

Les explications suivent l’ordre suivant :

1. finalité ;
2. vocabulaire ;
3. architecture ou principe ;
4. procédure minimale ;
5. validation ;
6. variantes ;
7. optimisation ;
8. dépannage ;
9. références croisées.

Une section avancée ne doit pas interrompre une procédure de base. Elle est placée après la réussite du parcours minimal ou dans un encadré clairement identifié.

## 6. Longueur des phrases et paragraphes

Les phrases doivent exprimer une idée principale. Les formulations très longues sont divisées lorsque cela améliore la compréhension.

Un paragraphe doit généralement développer une seule idée. Les blocs compacts sont évités, en particulier dans les procédures et les chapitres destinés aux débutants.

Les listes sont utilisées lorsque l’ordre, la comparaison ou l’exhaustivité apporte une vraie valeur. Elles ne remplacent pas systématiquement les explications rédigées.

## 7. Vocabulaire technique

Lors de sa première apparition, un terme spécialisé doit être :

- défini simplement ;
- accompagné de son terme anglais lorsqu’il est couramment utilisé dans les outils ;
- employé ensuite de manière constante.

Exemple :

> Une **carte de normales** (*normal map*) simule de petits reliefs sans ajouter de géométrie au maillage.

Les synonymes sont évités lorsqu’ils risquent de désigner des concepts différents. Le glossaire du Livre V constitue la référence terminologique centrale.

## 8. Tutoiement, vouvoiement et formulations impersonnelles

Le guide privilégie les formulations directes et impersonnelles :

- « Ouvrez le terminal. »
- « Vérifiez que le service est actif. »
- « Le fichier doit contenir… »

Le tutoiement conversationnel et le vouvoiement éditorial ne doivent pas être mélangés dans une même procédure.

## 9. Degrés de nécessité

Chaque outil, étape ou configuration importante est classé avec l’un des niveaux suivants :

- **Obligatoire** : indispensable pour suivre le pipeline principal.
- **Recommandé** : améliore fortement la fiabilité, la qualité ou la productivité.
- **Optionnel** : utile dans certains contextes, mais non requis pour terminer le projet fil rouge.

Le niveau doit apparaître avant la décision concernée, et non après plusieurs paragraphes d’explication.

## 10. Différenciation Solo et Studio

Lorsqu’une pratique change selon l’échelle de production, deux sous-sections sont utilisées :

### Mode Solo

Décrit la solution la plus simple à maintenir pour une seule personne, avec un coût opérationnel réduit.

### Mode Studio

Décrit les besoins de collaboration, revue, sécurité, automatisation, responsabilité et traçabilité.

Les deux parcours doivent rester compatibles avec la même architecture générale du projet.

## 11. Rédaction des procédures

Une procédure doit inclure :

- son objectif ;
- ses prérequis ;
- le niveau de nécessité ;
- les étapes numérotées ;
- les commandes exactes ;
- le résultat attendu ;
- une méthode de vérification ;
- les erreurs fréquentes ;
- l’étape suivante.

Une étape numérotée ne doit pas contenir plusieurs actions indépendantes si leur séparation facilite le diagnostic.

## 12. Commandes et code

Le texte qui précède un bloc de code indique :

- l’outil ou le terminal concerné ;
- le dossier de travail ;
- les variables à adapter ;
- les privilèges requis ;
- l’effet attendu.

Les extraits incomplets sont signalés comme tels. Les ellipses ne doivent jamais masquer une partie nécessaire au fonctionnement de l’exemple.

Les secrets, mots de passe, jetons et clés API ne sont jamais placés dans les exemples. Des valeurs factices explicites sont utilisées.

## 13. Résultats attendus

Toute opération importante comporte un contrôle visible ou mesurable. Exemples :

- un service répond sur une adresse locale ;
- une commande retourne une version ;
- un projet Godot démarre sans erreur ;
- un workflow ComfyUI produit une image ;
- un test automatisé passe ;
- une scène respecte un budget de performance.

La mention « cela devrait fonctionner » est insuffisante sans critère de validation.

## 14. Incertitude et dépendance aux versions

Lorsqu’un comportement dépend d’une version, d’un pilote ou d’un matériel, le texte doit préciser :

- la version testée ;
- la date de vérification lorsque nécessaire ;
- la configuration de référence ;
- les variations connues ;
- la procédure de repli.

Une hypothèse doit être présentée comme une hypothèse. Une information non vérifiée ne doit pas être formulée comme un fait établi.

## 15. Comparaisons d’outils

Une comparaison doit reposer sur des critères explicites, par exemple :

- licence ;
- fonctionnement local ;
- prise en charge AMD ;
- consommation mémoire ;
- maturité ;
- facilité d’installation ;
- intégration au pipeline ;
- automatisation ;
- maintenance ;
- qualité des résultats.

Le choix principal du guide doit être justifié. Les alternatives restent présentées de manière loyale, sans transformer le chapitre en catalogue.

## 16. Avertissements et sécurité

Les avertissements sont placés avant l’action risquée. Ils indiquent précisément :

- le risque ;
- les conditions dans lesquelles il apparaît ;
- les conséquences possibles ;
- la mesure de prévention ;
- la méthode de restauration.

Les formulations alarmistes sans instruction pratique sont évitées.

## 17. Contenus destinés aux adultes

Les thèmes adultes sont décrits sous l’angle de la conception de systèmes, de la narration, de la sécurité, du consentement, de la classification, de la conformité, de l’accessibilité et de la modération.

Le guide évite les descriptions graphiques inutiles. Il privilégie les abstractions techniques, les paramètres de simulation, les transitions d’état, les contraintes de production et les contrôles destinés aux utilisateurs adultes.

## 18. Citations et sources

Une affirmation technique importante doit pouvoir être reliée à une source primaire lorsque cela est pertinent :

- documentation officielle ;
- dépôt du projet ;
- norme ;
- publication scientifique ;
- licence ;
- note de version.

Les liens doivent être accompagnés d’une courte indication de leur utilité. Une source obsolète ne doit pas être présentée comme l’état actuel d’un outil.

## 19. Références croisées

Une référence croisée doit mentionner l’identifiant stable et, lorsque cela améliore la lecture, le titre de la section.

Exemple :

> Voir `DOC-V0-CH04`, « Convention des identifiants ».

Le texte ne doit pas reproduire une longue explication déjà maintenue dans un autre chapitre. Il en résume uniquement le point nécessaire puis renvoie vers la source canonique.

## 20. Exemples et projet fil rouge

Les exemples principaux doivent utiliser le même projet fil rouge afin de montrer la continuité du pipeline. Un exemple isolé est acceptable lorsqu’il simplifie une notion, mais il doit être clairement identifié comme démonstration autonome.

Les noms de fichiers, scènes, classes, tables et assets restent cohérents entre les volumes.

## 21. Règles typographiques

Le guide applique notamment les conventions suivantes :

- espace avant les signes doubles en français lorsque le moteur de rendu le permet ;
- guillemets français pour les citations éditoriales ;
- code en chasse fixe pour les commandes, chemins, identifiants et noms techniques ;
- noms de logiciels écrits selon leur graphie officielle ;
- unités séparées de leur valeur par une espace ;
- dates non ambiguës ;
- acronymes développés à leur première occurrence.

## 22. Formulations à éviter

Sont notamment évitées :

- « il suffit de » lorsque l’opération comporte des prérequis ;
- « évidemment » et « simplement » lorsqu’ils minimisent une difficulté réelle ;
- « toujours » et « jamais » sans justification ;
- les promesses de performance sans mesure ;
- les jugements vagues comme « meilleur », « rapide » ou « léger » sans critère ;
- les instructions imprécises comme « configurez correctement ».

## 23. Structure recommandée d’une section technique

Une section technique complète peut utiliser le modèle suivant :

1. objectif ;
2. niveau de nécessité ;
3. prérequis ;
4. principe ;
5. procédure ;
6. résultat attendu ;
7. validation ;
8. dépannage ;
9. mode Solo ;
10. mode Studio ;
11. références.

Tous les éléments ne sont pas obligatoires dans les sections courtes, mais leur ordre doit rester stable lorsqu’ils sont présents.

## 24. Relecture éditoriale

Avant validation, un chapitre doit être relu selon quatre axes :

### Clarté

- Les termes sont-ils définis ?
- Les phrases sont-elles compréhensibles ?
- Les prérequis sont-ils visibles ?

### Reproductibilité

- Les commandes sont-elles complètes ?
- Les chemins sont-ils cohérents ?
- Le résultat attendu est-il vérifiable ?

### Cohérence

- Les identifiants sont-ils corrects ?
- Les noms correspondent-ils aux autres volumes ?
- Les références croisées pointent-elles vers une source canonique ?

### Maintenance

- Les versions sont-elles indiquées lorsque nécessaire ?
- Les informations temporaires sont-elles identifiables ?
- Les alternatives sont-elles séparées du parcours principal ?

## 25. Checklist de validation

Avant de considérer un chapitre comme rédigé :

- [ ] le public et les prérequis sont identifiables ;
- [ ] les termes nouveaux sont définis ;
- [ ] les niveaux Obligatoire, Recommandé et Optionnel sont utilisés correctement ;
- [ ] les procédures comportent un résultat attendu ;
- [ ] les commandes et extraits sont reproductibles ;
- [ ] les limites et risques sont explicites ;
- [ ] les parcours Solo et Studio sont distingués lorsque nécessaire ;
- [ ] les références croisées utilisent des identifiants stables ;
- [ ] les affirmations dépendantes d’une version sont contextualisées ;
- [ ] le chapitre respecte les conventions de `DOC-V0-CH05`.

## Conclusion

Le style rédactionnel du guide ne vise pas uniquement l’élégance. Il constitue un mécanisme de qualité, de reproductibilité et de maintenance. Une documentation claire réduit les erreurs, facilite le diagnostic et permet aux mêmes procédures d’être utilisées par un débutant, un développeur expérimenté ou une équipe complète.