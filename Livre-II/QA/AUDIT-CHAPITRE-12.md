---
title: "Audit du Livre II — Chapitre 12"
id: "DOC-L2-QA-CH12"
status: "complete"
version: "1.0.1"
book: "Livre II"
chapter: 12
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH12"
chapter-version: "1.0.2"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 12

> **Chapitre audité :** `Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté après corrections, avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le chapitre met en œuvre la frontière du chapitre 11 sans coupler le gameplay :

- aux routes HTTP ;
- au cycle de vie d’un WebSocket ;
- au schéma d’un fournisseur ;
- à une file de tâches non bornée ;
- à une disponibilité permanente du service IA.

Il vérifie également que le durcissement production/runtime reste réservé au chapitre 13.

## 2. Anomalie de processus corrigée

La première rédaction déclarait prématurément dans son front matter :

- `audit-status: complete` ;
- `audit-level: static-review` ;
- un lien vers le présent rapport, alors que celui-ci n’existait pas encore.

Cette déclaration ne constituait pas une preuve d’audit. Le chapitre n’est considéré comme audité qu’après la présente revue, ses corrections, la création de la preuve YAML et la réussite des workflows légers.

## 3. Couverture du périmètre officiel

| Exigence | Couverture |
|---|---|
| Port du chapitre 11 derrière des transports réseau | Complet |
| Choix `HTTPRequest`, `HTTPClient`, `WebSocketPeer` | Complet, avec `HTTPRequest` et `WebSocketPeer` détaillés |
| Contrats HTTP versionnés | Complet |
| En-têtes, types de contenu et codes HTTP | Complet |
| API compatibles OpenAI sans dépendance fournisseur | Complet |
| Streaming et événements | Complet au niveau architectural |
| Files de tâches bornées | Complet |
| Identifiants, états et résultats | Complet |
| Idempotence et déduplication | Complet |
| Retries bornés, backoff et jitter | Complet |
| Délais et annulation | Complet |
| Polling, notification et reprise | Complet |
| Backpressure et concurrence | Complet |
| Erreurs réseau structurées | Complet |
| Santé et capacités | Complet |
| Aucun secret réel | Complet |
| Frontière du chapitre 13 | Préservée |
| Parcours Solo et Studio | Complet |
| Audit statique sans PDF | Complet |

## 4. Frontières avec les chapitres voisins

### 4.1 Chapitre 11

Le chapitre 11 reste propriétaire :

- du port `LocalAiGateway` ;
- des contrats `AiRequest`, `AiResponse` et `AiServiceError` ;
- du repli déterministe ;
- de la corrélation et du cycle de vie générique.

Le chapitre 12 ajoute des adaptateurs. Il ne crée pas un second port métier.

### 4.2 Chapitre 13

Restent exclus :

- secrets réels ;
- authentification de production ;
- TLS et certificats de production ;
- listes d’autorisation généralisées ;
- isolation des processus ;
- signature des exécutables ;
- exposition réseau distante ;
- politiques de confidentialité et de conservation.

La boucle locale et les limites de taille sont des précautions minimales, pas un durcissement complet.

## 5. Corrections appliquées pendant l’audit

### 5.1 Nom du port applicatif

Le brouillon utilisait `LocalAiPort`, absent du chapitre 11.

Correction : toutes les références utilisent désormais le nom canonique `LocalAiGateway`.

### 5.2 Architecture transportable

Le schéma contenait deux niveaux de port successifs.

Correction : le flux devient :

> **[LECTURE] Architecture corrigée — Ne pas saisir.**

```text
fonctionnalité Godot
        ↓
LocalAiGateway
        ↓
adaptateur stdio, HTTP ou canal d’événements WebSocket
```

Le WebSocket reste un canal d’événements, pas un port métier concurrent.

### 5.3 Validation des URL locales

Le test `begins_with("http://127.0.0.1")` acceptait des chaînes ressemblantes, par exemple un nom d’hôte commençant par ces caractères.

Correction : le schéma, l’adresse exacte `127.0.0.1`, le port de `1` à `65535` et le chemin WebSocket `/v1/events` sont contrôlés séparément.

### 5.4 Limite du corps HTTP

Le brouillon comparait la taille du corps seulement après son téléchargement.

Correction : `HTTPRequest.body_size_limit` est configuré avant l’appel. Le résultat `RESULT_BODY_SIZE_LIMIT_EXCEEDED` devient une erreur de protocole explicite.

### 5.5 Délai HTTP

Le délai demandé par l’appel est désormais plafonné par `request_timeout_seconds` dans la configuration réseau.

### 5.6 Cycle de vie WebSocket

Une fermeture avant l’état `OPEN` n’émettait aucun diagnostic et laissait le polling actif.

Correction : chaque démarrage crée un nouveau `WebSocketPeer`, borne son tampon et sa file de paquets, puis traite tout état `CLOSED` en arrêtant le polling et en émettant `disconnected`.

### 5.7 Événements de tâche

Le brouillon déclarait `AiTaskEvent.state` sans le remplir et convertissait le payload sans vérifier son type.

Correction : les sept états autorisés sont mappés explicitement ; tout état inconnu ou payload non dictionnaire est refusé.

### 5.8 Worker Python

Le worker retirait un `QueueEntry`, mais appelait le handler avec `{}`. Le payload de la tâche était perdu.

Correction : `entry.payload` est transmis à `_execute()` puis au handler. `updated_at` est actualisé à la fin de chaque tentative.

### 5.9 Durée d’une tâche

Le champ d’exemple `deadline_ms` ressemblait à une horloge absolue alors que la valeur était relative.

Correction : le contrat utilise `timeout_ms`, que le serveur convertira vers une échéance monotone locale.

### 5.10 Compatibilité OpenAI

Le brouillon présentait uniquement `/v1/chat/completions` sans situer cette cible.

Correction : le chapitre précise que l’exemple est un sous-ensemble de compatibilité historique. L’API Responses, les événements SSE et le schéma réellement ciblé doivent être versionnés dans un adaptateur distinct.

### 5.11 Sources

Les références génériques ont été remplacées par des documents officiels épinglés :

- Godot Engine 4.7 pour `HTTPRequest`, `HTTPClient`, `WebSocketPeer`, le tutoriel WebSocket et `JSON` ;
- Python 3.12 pour `asyncio.Queue`, `PriorityQueue`, `dataclasses` et `StrEnum` ;
- référence officielle OpenAI pour Responses et les événements de streaming.

## 6. Vérification technique

### 6.1 Godot

La documentation officielle confirme notamment :

- une instance `HTTPRequest` traite une requête à la fois et peut retourner `ERR_BUSY` ;
- `body_size_limit` borne le corps décompressé ;
- `cancel_request()` annule la requête locale ;
- `request_completed` sépare résultat de transport et code HTTP ;
- `WebSocketPeer.connect_to_url()` est non bloquant ;
- `poll()` doit être appelé régulièrement ;
- `get_ready_state()`, `get_available_packet_count()` et `get_packet()` pilotent la lecture ;
- `send_text()` envoie une trame texte.

Les exemples GDScript ont été relus statiquement, mais Godot 4.7.1 n’a pas été exécuté.

### 6.2 Python

Les cinq modules Python complets documentés ont été extraits et compilés avec `python -m py_compile` : succès.

Les petits fragments de la section d’erreurs ne sont pas des modules autonomes et ne sont pas comptés comme compilation de fichiers.

La documentation Python confirme :

- `asyncio.Queue(maxsize>0)` bloque `put()` lorsque la capacité est atteinte ;
- `put_nowait()` lève `QueueFull` ;
- `PriorityQueue` retourne l’entrée de priorité numérique la plus basse ;
- `task_done()` doit correspondre à chaque élément retiré.

### 6.3 JSON

Les dix blocs JSON du chapitre ont été analysés avec le parseur standard Python : succès.

### 6.4 API compatibles OpenAI

Le mapper reste isolé du domaine. Il ne prétend pas garantir une compatibilité universelle : le serveur et la version de schéma devront être sélectionnés puis testés explicitement.

## 7. Contrôle documentaire

Résultats après corrections :

- 2 018 lignes ;
- 79 titres ;
- 71 blocs de code, données ou sortie ;
- 71 blocs sur 71 munis d’un repère reconnu ;
- 16 cas détaillés dans la section d’erreurs ;
- 0 titre dupliqué ;
- 0 bloc significatif dupliqué ;
- 0 long paragraphe dupliqué ;
- 1 lien Markdown local, résolu vers la convention des contextes ;
- 0 PDF produit.

## 8. Règle sémantique des erreurs et corrections

La section porte `<!-- qa:error-correction-section -->`.

Chacun des seize cas contient :

1. un symptôme ;
2. un exemple fautif ;
3. une correction ;
4. un exemple ou flux corrigé ;
5. une différence explicite.

Les thèmes couvrent transports, concurrence, codes HTTP, surcharge, idempotence, annulation, ordre des événements, streaming, traduction OpenAI, santé, autorisation, volatilité des tâches et repli.

## 9. Parcours Solo et Studio

### 9.1 Solo

Le parcours reste exploitable avec :

- boucle locale ;
- file en mémoire bornée ;
- petit nombre de workers ;
- WebSocket optionnel ;
- polling de secours ;
- idempotence volatile ;
- repli déterministe.

### 9.2 Studio

Le parcours ajoute gouvernance de schémas, quotas, métriques, campagnes de compatibilité, stratégie de migration et décision explicite sur la persistance.

## 10. Réserves runtime

Ne sont pas revendiqués :

- analyse GDScript par Godot 4.7.1 ;
- exécution de `HTTPRequest` sous Windows 11 ;
- application réelle de `body_size_limit` ;
- serveur HTTP ou WebSocket matérialisé ;
- reconnexion et messages fragmentés ;
- concurrence des workers ;
- backpressure réelle ;
- idempotence et empreinte canonique ;
- annulation distante ;
- priorités et prévention de famine ;
- expiration des tâches ;
- streaming SSE ou WebSocket ;
- compatibilité avec un serveur OpenAI-compatible réel ;
- packaging et exports ;
- durcissement du chapitre 13 ;
- PDF du Livre II.

## 11. Correction post-audit — liens des sources techniques

Une relecture utilisateur a détecté que les neuf adresses de la section 51 étaient placées entre backticks au lieu d’être exposées comme liens Markdown. Cette présentation obligeait le lecteur à copier manuellement les URL et n’était pas cohérente avec les chapitres voisins.

Correction appliquée : chaque référence possède désormais un libellé descriptif cliquable au format `[nom de la source](URL)`. Les destinations et les versions documentaires restent inchangées.

Contrôles associés :

- les neuf références web sont des liens Markdown ;
- aucun lien technique n’est laissé sous forme d’URL entre backticks dans la section 51 ;
- les intitulés permettent d’identifier la documentation avant l’ouverture ;
- la section conserve la source non déterminée du serveur local comme exigence à compléter lors de sa matérialisation.

## 12. Décision

Le chapitre 12 est accepté au niveau `static-review` après application des corrections recensées.

La preuve finale est enregistrée dans :

`Livre-II/QA/VALIDATION-FINALE-CHAPITRE-12.yaml`.

Le chapitre ne deviendra `runtime-tested` qu’après matérialisation du Starter Kit, exécution de Godot et du serveur, et conservation des journaux correspondants.
