---
title: "Reprendre le projet dans une nouvelle conversation"
id: "DOC-PROJECT-RESTART-PROMPT"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-19"
source-of-truth: "CONTINUITE-PROJET.md"
---

# Reprendre le projet dans une nouvelle conversation

> **Rôle de ce fichier :** fournir un message de démarrage stable. Il ne contient volontairement ni progression détaillée, ni prochain chapitre figé, ni décisions techniques recopiées. Ces informations appartiennent à `CONTINUITE-PROJET.md`, qui reste l’unique source de vérité pour l’état courant.

## 1. Avant de commencer

Dans la nouvelle conversation :

1. active le connecteur GitHub ;
2. autorise l’accès au dépôt `LaurentCOLL1/Guide-IA-GameDev` ;
3. copie-colle le message de la section suivante ;
4. attends la confirmation de lecture du dépôt avant de demander la rédaction du chapitre suivant.

## 2. Message à copier-coller

> **[LECTURE] Prompt de reprise — À copier dans une nouvelle conversation.**

```text
Utilise mon dépôt GitHub LaurentCOLL1/Guide-IA-GameDev comme unique source de vérité pour reprendre le projet.

Avant toute rédaction ou modification :

1. lis entièrement CONTINUITE-PROJET.md ;
2. lis ROADMAP.md, contents.txt et l’index du Livre actif ;
3. lis le protocole QA du Livre actif ;
4. lis le plan maître du Livre ou Pack actif lorsqu’il existe ;
5. vérifie les derniers commits, branches, pull requests et workflows GitHub ;
6. lis le dernier chapitre terminé, son rapport d’audit et sa preuve QA ;
7. identifie la prochaine action indiquée dans CONTINUITE-PROJET.md ;
8. ne recrée aucun chapitre, audit, fichier ou choix déjà présent ;
9. ne modifie jamais silencieusement le plan maître, l’ordre des chapitres ou les décisions d’architecture.

Le contenu actuel du dépôt prévaut sur ce message, sur toute ancienne conversation et sur tout résumé extérieur au dépôt. En cas de différence, signale-la avant de continuer.

Avant de produire un nouveau chapitre :

- annonce le chapitre à produire ;
- recommande GPT-5.6 Sol — Moyenne ou Élevée ;
- justifie ce niveau ;
- compare le périmètre au plan maître et aux chapitres voisins ;
- confirme que le chapitre n’existe pas déjà comme document finalisé.

Pour chaque chapitre :

- rédige de manière détaillée pour un débutant ;
- explique les fonctions, paramètres, types, retours, opérateurs et résultats ;
- utilise les repères [PS], [CMD], [WSL], [DCT], [DCK], [VSC], [WEB], [APP], [SORTIE] et [LECTURE] ;
- respecte l’architecture et les décisions consignées dans CONTINUITE-PROJET.md ;
- applique la règle sémantique des erreurs : chaque cas détaillé doit montrer un symptôme, un exemple fautif, une correction, un exemple corrigé et expliquer leur différence ;
- effectue l’audit post-création ;
- vérifie les doublons, liens, repères, frontières et exactitude technique ;
- crée ou met à jour la preuve QA ;
- lance uniquement les validations légères sans PDF ;
- mets à jour l’index actif, ROADMAP.md, contents.txt et CONTINUITE-PROJET.md dans le même lot ;
- utilise une branche dédiée et une pull request avant fusion dans main ;
- ne revendique jamais un test runtime qui n’a pas été exécuté.

Ne construis pas de PDF après un chapitre. Le PDF doit être produit uniquement à la fin du Livre actif, à la fin du Companion Pack lorsque pertinent, ou à la fin de la collection, sauf modification directe de la chaîne PDF ou de la mise en page.

Commence par me présenter uniquement :

1. l’état actuel vérifié dans le dépôt ;
2. le dernier chapitre ou lot terminé ;
3. les réserves encore ouvertes ;
4. la prochaine action officielle ;
5. le niveau GPT-5.6 Sol recommandé et sa justification ;
6. les fichiers que tu as effectivement lus.

Ne rédige pas encore le nouveau chapitre avant cette confirmation.
```

## 3. Sources à lire obligatoirement

Le message précédent doit conduire à la lecture des fichiers suivants :

```text
CONTINUITE-PROJET.md
ROADMAP.md
contents.txt
<Livre-ou-Pack-actif>/index.md
<Livre-ou-Pack-actif>/QA/PROTOCOLE-AUDIT-POST-CREATION.md
<plan-maître-actif, lorsqu’il existe>
<dernier chapitre terminé>
<rapport d’audit correspondant>
<preuve QA correspondante>
```

Les chemins concrets du Livre, du chapitre, de l’audit et de la preuve doivent être déterminés depuis `CONTINUITE-PROJET.md`, pas depuis ce fichier.

## 4. Principe de non-divergence

L’ordre de priorité est :

```text
1. état actuel du dépôt GitHub
2. CONTINUITE-PROJET.md
3. plans maîtres, index, roadmap et ordre de compilation
4. rapports et preuves QA
5. message de la conversation en cours
6. anciens résumés ou anciennes conversations
```

Une nouvelle conversation doit arrêter son exécution et signaler toute contradiction entre ces niveaux avant de modifier le dépôt.

## 5. Ce fichier ne doit pas devenir une seconde source de vérité

Ne pas y recopier :

- le nombre courant de chapitres terminés ;
- le prochain chapitre ;
- les versions détaillées des documents ;
- les identifiants de workflows ;
- les décisions d’architecture propres à un chapitre ;
- les réserves runtime propres à un lot.

Ces informations changent fréquemment et restent centralisées dans `CONTINUITE-PROJET.md` et les preuves QA.

## 6. Entretien

Ce fichier ne doit être modifié que lorsque la **procédure générale de reprise** change. La progression normale du projet ne nécessite pas de le mettre à jour.
