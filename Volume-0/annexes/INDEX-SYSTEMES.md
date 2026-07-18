---
title: "Annexe — Index des systèmes"
id: "DOC-V0-ANN-INDEX-SYSTEMES"
status: "provisional"
version: "0.1.0"
---

# Index des systèmes

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](CONVENTION-OUTILS-ET-CONTEXTES.md).

Cet index réserve les identifiants des douze grands systèmes de jeu qui structureront le Livre II. Leur périmètre détaillé pourra évoluer pendant la conception, mais leurs identifiants doivent rester stables afin de préserver les références croisées.

## Catalogue initial des douze systèmes

| ID | Système | Responsabilité principale | Interfaces majeures |
|---|---|---|---|
| SYS-01 | Personnage joueur | Déplacement, états, attributs, actions et représentation du joueur | Entrées, caméra, interaction, combat, sauvegarde |
| SYS-02 | Caméra et perception | Cadrage, suivi, visée, visibilité et retours perceptifs | Joueur, environnement, interface, accessibilité |
| SYS-03 | Interaction | Détection, sélection et activation des éléments interactifs | Joueur, inventaire, monde, narration |
| SYS-04 | Inventaire et objets | Collecte, stockage, équipement, consommation et métadonnées des objets | Interaction, combat, artisanat, sauvegarde, UI |
| SYS-05 | Combat et dégâts | Attaques, défenses, collisions, dégâts, états et résolution des affrontements | Joueur, PNJ, objets, animation, audio, VFX |
| SYS-06 | IA des personnages | Perception, décision, navigation, comportements et coordination des PNJ | Monde, combat, narration, animation, audio |
| SYS-07 | Quêtes, dialogues et narration | États narratifs, objectifs, choix, dialogues et conséquences | IA, monde, sauvegarde, interface, audio |
| SYS-08 | Progression et économie | Expérience, compétences, ressources, coûts, récompenses et équilibrage | Inventaire, quêtes, combat, sauvegarde |
| SYS-09 | Monde, temps et environnement | Chargement des zones, cycle temporel, météo, événements et simulation environnementale | IA, narration, audio, sauvegarde, optimisation |
| SYS-10 | Sauvegarde et persistance | Sérialisation, migration, chargement, autosauvegarde et reprise après erreur | Tous les systèmes persistants |
| SYS-11 | Interface, UX et accessibilité | HUD, menus, retours, navigation, paramètres et options d’accessibilité | Tous les systèmes exposés au joueur |
| SYS-12 | Audio, animation et effets | Coordination des animations, sons, musique, voix, particules et retours sensoriels | Joueur, IA, combat, monde, interface |

## Contrat minimal d’un système

Chaque système du Livre II devra fournir une fiche conforme au modèle suivant :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: "SYS-XX"
name: "Nom du système"
owner: "responsable ou domaine"
status: "draft | validated | deprecated"
responsibilities:
  - "Responsabilité"
non_responsibilities:
  - "Élément explicitement hors périmètre"
inputs:
  - "Entrée"
outputs:
  - "Sortie"
dependencies:
  - "SYS-YY"
events_emitted:
  - "event_name"
events_consumed:
  - "event_name"
persistence:
  schema_version: 1
performance_budget:
  cpu_ms: "à mesurer"
  memory_mb: "à mesurer"
tests:
  - "test de référence"
```

## Règles d’architecture

- Un système possède une responsabilité principale identifiable.
- Les dépendances cycliques sont interdites ou doivent être justifiées par une décision architecturale.
- Les échanges transversaux privilégient des signaux, événements ou interfaces documentées.
- Les données sauvegardées possèdent une version de schéma.
- Les comportements critiques disposent de tests reproductibles.
- Les budgets de performance sont mesurés sur le profil matériel de référence.
- Les composants propres à l’éditeur sont séparés du runtime lorsque cela réduit les dépendances.

## Parcours Solo et Studio

### Mode Solo

- architecture lisible dans un seul dépôt ;
- configuration locale simple ;
- outils de diagnostic accessibles depuis l’éditeur ;
- dépendances externes minimales.

### Mode Studio

- propriétaires de systèmes identifiés ;
- contrats d’interface revus avant intégration ;
- scènes, ressources et données organisées pour limiter les conflits Git ;
- tests automatiques et validation des migrations ;
- documentation des décisions architecturales.

## Statut de cet index

Ce catalogue constitue une réservation normative des identifiants, pas encore la spécification complète des systèmes. Toute modification du découpage doit :

1. conserver un alias pour les identifiants remplacés ;
2. mettre à jour les références croisées ;
3. documenter la migration dans le changelog ;
4. vérifier les conséquences sur les sauvegardes et le Companion Pack.

## Checklist

- [ ] Les douze fiches détaillées existent dans le Livre II.
- [ ] Chaque dépendance entre systèmes est documentée.
- [ ] Les événements partagés possèdent un registre.
- [ ] Les schémas persistants sont versionnés.
- [ ] Les budgets de performance sont mesurés.
- [ ] Les parcours Solo et Studio sont testés.
