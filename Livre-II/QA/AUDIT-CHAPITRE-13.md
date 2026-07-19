---
title: "Audit du Livre II — Chapitre 13"
id: "DOC-L2-QA-CH13"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 13
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH13"
chapter-version: "1.0.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 13

> **Chapitre audité :** `Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté après corrections, avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le chapitre ferme la plateforme IA locale sans déplacer dans le runtime distribué les capacités, secrets ou privilèges des outils de production.

Il contrôle notamment :

- le modèle de menaces et les frontières de confiance ;
- la séparation production, livraison, runtime et données du joueur ;
- les profils `development`, `test` et `production` ;
- les secrets hors dépôt, hors package et hors payloads métier ;
- l’écoute sur la boucle locale par défaut ;
- l’authentification et TLS dès qu’une frontière réseau s’élargit ;
- l’autorisation par défaut refusée ;
- les listes d’autorisation d’opérations, modèles et chemins ;
- le moindre privilège, les limites et les quotas ;
- la rédaction des journaux ;
- l’épinglage des dépendances, le SBOM, la provenance et la signature ;
- l’échec fermé pour la sécurité avec maintien du repli déterministe du gameplay.

## 2. Porte d’audit distincte

Le chapitre a été rédigé sur une branche dédiée, puis relu contre le protocole `DOC-L2-QA-POST-CREATION` avant sa déclaration finale.

La séquence appliquée est :

1. annonce du titre et du niveau GPT-5.6 Sol ;
2. rédaction du chapitre ;
3. audit de complétude et de périmètre ;
4. audit des repères d’utilisation ;
5. seconde lecture et contrôle des doublons ;
6. vérification technique et des sources officielles ;
7. corrections ;
8. création du présent rapport et de la preuve YAML ;
9. mise à jour de la gouvernance ;
10. validations GitHub sans PDF.

La réussite des workflows reste enregistrée séparément dans `VALIDATION-FINALE-CHAPITRE-13.yaml`.

## 3. Couverture du périmètre officiel

| Exigence | Couverture |
|---|---|
| Modèle de menaces et frontières de confiance | Complet |
| Séparation production/runtime | Complet |
| Profils développement, test et production | Complet |
| Secrets hors versionnement et gameplay | Complet |
| Boucle locale par défaut | Complet |
| Authentification hors loopback | Complet |
| TLS et certificats | Complet au niveau architectural |
| Listes d’autorisation | Complet |
| Moindre privilège | Complet |
| Limites, débit, concurrence et quotas | Complet |
| Rédaction et rétention des journaux | Complet |
| Dépendances, licences et SBOM | Complet au niveau de préparation |
| Packaging, signature et mise à jour | Complet au niveau architectural |
| Échec fermé et repli déterministe | Complet |
| Parcours Solo et Studio | Complet |
| Audit statique sans PDF | Complet |

## 4. Frontières avec les chapitres voisins

### 4.1 Chapitre 12

Le chapitre 12 reste propriétaire :

- des contrats HTTP et WebSocket ;
- des files de tâches ;
- de l’idempotence ;
- de la backpressure ;
- des événements et du polling ;
- de l’adaptation compatible OpenAI.

Le chapitre 13 applique à ces mécanismes des politiques de confiance, d’identité, d’autorisation, de limites et de publication. Il ne redéfinit pas les transports.

### 4.2 Chapitre 14

Le chapitre 14 commencera les systèmes de gameplay avec les personnages. Le chapitre 13 ne définit ni attributs de personnage, ni contrôleur, ni relations sociales, ni agents autonomes, ni combat.

## 5. Corrections issues de la première lecture

### 5.1 Saisie PowerShell du jeton

Une première formulation envisageait `Read-Host -AsSecureString` pour affecter directement une variable d’environnement. Elle aurait produit un objet `SecureString`, non une chaîne exploitable par le processus enfant.

Correction : utilisation de `Read-Host -MaskInput`, accompagnée d’une explication claire de sa limite en mémoire.

### 5.2 Faux fichier de verrouillage

Une première structure risquait de présenter des versions factices comme un vrai verrou de dépendances.

Correction : le chapitre montre uniquement la forme d’un verrou sous le repère `[LECTURE]` et précise qu’aucun faux verrou n’est créé avant le choix du framework serveur réel.

### 5.3 Mode isolé Python

L’option `-I` peut retirer le répertoire du script du chemin d’importation et rendre un module local introuvable.

Correction : la commande est réservée au paquet `asteria_ai_server` installé dans l’environnement virtuel.

### 5.4 Sources et versions

Les liens Godot sont épinglés sur la branche documentaire `4.7`. Les références Python sont épinglées sur `3.12`. Le SSDF `1.1` est qualifié de version finale publiée et le SSDF `1.2` de brouillon initial.

### 5.5 Sources immédiatement accessibles

Les seize références de la section `Sources techniques` utilisent des liens Markdown nommés et cliquables. Aucune adresse n’est présentée comme texte entre backticks.

## 6. Matrice Q0 à Q5

### Q0 — Intégrité

- [x] Chemin canonique présent.
- [x] Front matter YAML cohérent.
- [x] Identifiant `DOC-L2-CH13` unique.
- [x] Chapitre et version concordants.
- [x] Niveau de raisonnement enregistré.
- [x] Rapport d’audit distinct référencé.

### Q1 — Complétude pédagogique

- [x] Objectif, prérequis et périmètre observables.
- [x] Vocabulaire défini avant usage.
- [x] Progression du modèle de menaces vers la publication.
- [x] Modes Solo et Studio séparés.
- [x] Tests à préparer, critères d’acceptation et checklists présents.
- [x] Seize erreurs détaillées avec symptôme, exemple fautif, correction, exemple corrigé et différence.

### Q2 — Cohérence de collection

- [x] Entrée du plan maître couverte.
- [x] Responsabilités du chapitre 12 conservées.
- [x] Périmètre du chapitre 14 non consommé.
- [x] `LocalAiGateway` reste le port du gameplay.
- [x] La plateforme IA locale se termine à quatre chapitres sur quatre.

### Q3 — Vérification technique

- [x] Boucle locale et adresses non spécifiées distinguées.
- [x] Authentification et autorisation séparées.
- [x] Comparaison de jetons avec `hmac.compare_digest`.
- [x] Génération de jetons avec `secrets`.
- [x] Résolution canonique des chemins sous une racine.
- [x] TLS sûr séparé de `client_unsafe()`.
- [x] Limites de ressources explicites.
- [x] Rédaction récursive des champs sensibles.
- [x] SBOM, provenance, signature et rollback qualifiés sans prétention runtime.
- [x] Extraits Python relus syntaxiquement.
- [x] Extraits GDScript relus statiquement.

### Q4 — Outils et contextes

- [x] Chaque fichier à créer indique `[VSC]` et un chemin.
- [x] Chaque commande indique `[PS]`.
- [x] Les exemples non exécutables indiquent `[LECTURE]`.
- [x] Les résultats indiquent `[SORTIE]`.
- [x] Les blocs de données possèdent un contexte explicite.

### Q5 — Sécurité et licences

- [x] Aucun secret réel.
- [x] Aucun privilège administrateur demandé.
- [x] Les clés privées sont exclues du client.
- [x] Les modèles runtime doivent être redistribuables.
- [x] Les licences sont intégrées à l’inventaire de dépendances.
- [x] Les limites de l’audit sont déclarées.

## 7. Audit des erreurs et corrections

La section détaillée porte `<!-- qa:error-correction-section -->`.

Les seize cas contrôlés sont :

1. outils de production livrés au runtime ;
2. écoute sur toutes les interfaces ;
3. jeton stocké dans `res://` ;
4. authentification confondue avec autorisation ;
5. `task_id` utilisé comme autorisation ;
6. TLS non vérifié en production ;
7. chemin client ouvert directement ;
8. en-tête `Authorization` journalisé ;
9. `random` utilisé pour un jeton ;
10. file illimitée ;
11. TLS considéré comme permission ;
12. clé privée incluse dans le client ;
13. publication sans SBOM ;
14. hachage seul considéré comme preuve d’origine ;
15. refus de sécurité masqué par le repli ;
16. debug conservé en production.

Chaque cas contient les cinq éléments obligatoires.

## 8. Sources principales

Les références privilégiées sont officielles ou normatives :

- OWASP Cheat Sheet Series ;
- NIST SSDF et profil IA ;
- CISA pour les ressources SBOM ;
- documentation Godot 4.7 ;
- documentation Python 3.12 ;
- Microsoft Learn pour PowerShell.

Les destinations sont cliquables depuis le chapitre.

## 9. Réserves runtime

Ne sont pas revendiqués :

- exécution des scripts dans Godot 4.7.1 ;
- configuration réelle du pare-feu Windows ;
- serveur authentifié ou TLS matérialisé ;
- émission, rotation ou révocation de certificats et secrets ;
- restrictions d’un compte de service ;
- limites CPU et mémoire du processus ;
- quotas concurrents ;
- validation de rédaction sur des journaux réels ;
- détection de secrets et scan de vulnérabilités ;
- génération d’un SBOM réel ;
- attestation de provenance ;
- signature de code ;
- mise à jour et rollback ;
- packaging multi-plateforme ;
- PDF du Livre II.

## 10. Décision

Le chapitre 13 est accepté au niveau `static-review` après application des corrections recensées.

La preuve finale est enregistrée dans :

`Livre-II/QA/VALIDATION-FINALE-CHAPITRE-13.yaml`.

Le chapitre ne deviendra `runtime-tested` qu’après matérialisation du Starter Kit, exécution des contrôles de sécurité et conservation de journaux vérifiables.
