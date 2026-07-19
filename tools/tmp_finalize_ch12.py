from pathlib import Path
import base64
import zlib

def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"Motif absent dans {path}: {old[:120]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


parts = sorted(Path("tools/tmp_ch12_parts").glob("part-*.txt"))
encoded = "".join(part.read_text(encoding="ascii") for part in parts)
Path("Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md").write_bytes(
    zlib.decompress(base64.b64decode(encoded))
)

replace_once("CONTINUITE-PROJET.md", 'version: "3.12.0"', 'version: "3.13.0"')
replace_once("CONTINUITE-PROJET.md", "**En cours : 11 chapitres sur 30.**", "**En cours : 12 chapitres sur 30.**")
replace_once(
    "CONTINUITE-PROJET.md",
    "12. HTTP, WebSocket, API compatibles OpenAI et files de tâches — prochain chapitre.\n13. Sécurité et séparation production/runtime de l’IA.",
    "12. HTTP, WebSocket, API compatibles OpenAI et files de tâches — terminé au niveau `static-review`.\n13. Sécurité et séparation production/runtime de l’IA — prochain chapitre.",
)
replace_once("CONTINUITE-PROJET.md", "Chapitres 3 à 11 : **Élevée**.", "Chapitres 3 à 12 : **Élevée**.")
replace_once(
    "CONTINUITE-PROJET.md",
    "- HTTP, WebSocket, API compatibles OpenAI et files de tâches restent réservés au chapitre 12 ;\n- secrets, isolation, signature et durcissement de production restent réservés au chapitre 13.",
    "- les adaptateurs réseau du chapitre 12 restent derrière `LocalAiGateway` ;\n- secrets, isolation, signature et durcissement de production restent réservés au chapitre 13.",
)

anchor = """## 12. Chapitre 5 — état résumé"""
network_section = """### 11.7 Transports réseau et files de tâches

- `LocalAiGateway` reste le port applicatif canonique ;
- HTTP sert aux échanges bornés et WebSocket aux événements, progressions et flux sélectionnés ;
- les enveloppes HTTP sont versionnées et distinguent résultat de transport, code HTTP et erreur métier ;
- `HTTPRequest.body_size_limit` est configuré avant téléchargement ;
- WebSocket est sondé sans bloquer, avec tampons et files de paquets bornés ;
- les événements de tâche portent une séquence croissante et l’état HTTP final reste l’autorité ;
- les tâches utilisent `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCEL_REQUESTED`, `CANCELLED` et `EXPIRED` ;
- la file prioritaire est bornée et la surcharge produit `429` avec `Retry-After` ;
- une clé d’idempotence est liée à une empreinte canonique du payload et un conflit produit `409` ;
- les retries sont bornés avec backoff exponentiel et jitter ;
- `timeout_ms` est une durée relative convertie en échéance monotone locale ;
- le polling HTTP reste disponible lorsque WebSocket est absent ;
- la compatibilité OpenAI est isolée dans un adaptateur versionné ;
- l’exemple `chat/completions` constitue un sous-ensemble historique et l’API Responses peut être ciblée séparément ;
- la file en mémoire est volatile et ne promet aucune reprise après panne ;
- le repli déterministe masque seulement les indisponibilités prévues ;
- le durcissement de production reste réservé au chapitre 13.

## 12. Chapitre 5 — état résumé"""
replace_once("CONTINUITE-PROJET.md", anchor, network_section)

chapter12_section = """## 19. Chapitre 12 — état détaillé

Fichier : `Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md`.

Niveau : **GPT-5.6 Sol — Élevée**.

Décisions enregistrées :

- `LocalAiGateway` conservé comme unique port métier ;
- `HTTPRequest` pour les requêtes et réponses bornées ;
- `WebSocketPeer` pour événements, progressions et certains flux ;
- contrats HTTP versionnés et erreurs structurées ;
- limite du corps configurée avant téléchargement ;
- séparation résultat de transport, code HTTP et erreur métier ;
- tâches longues avec sept états explicites ;
- file prioritaire bornée, concurrence limitée et backpressure ;
- `429` et `Retry-After` pour la surcharge ;
- idempotence par clé et empreinte canonique du payload ;
- conflit `409` lorsqu’une clé est réutilisée avec un autre payload ;
- retries bornés avec backoff et jitter ;
- délais relatifs convertis vers une horloge monotone locale ;
- annulation coopérative et réponses tardives rejetées ;
- événements ordonnés par séquence et polling HTTP de secours ;
- adaptateur compatible OpenAI isolé du domaine ;
- compatibilité `chat/completions` qualifiée de sous-ensemble historique ;
- API Responses et SSE réservés à un schéma explicitement versionné ;
- file en mémoire qualifiée de volatile ;
- repli déterministe limité aux indisponibilités attendues ;
- durcissement production/runtime réservé au chapitre 13.

Livrables documentés :

- `src/core/ai/ai_network_config.gd` ;
- `src/core/ai/ai_network_envelope_codec.gd` ;
- `src/core/ai/http_local_ai_transport.gd` ;
- `src/core/ai/websocket_event_channel.gd` ;
- `src/core/ai/ai_task_status.gd` ;
- `src/core/ai/ai_task.gd` ;
- `src/core/ai/ai_task_event.gd` ;
- `src/core/ai/openai_compatible_mapper.gd` ;
- `src/app/ai_network_bootstrap.gd` ;
- `tools/ai_server/task_models.py` ;
- `tools/ai_server/task_queue.py` ;
- `tools/ai_server/task_worker.py` ;
- `tools/ai_server/protocol.py` ;
- `tools/ai_server/operations.py` ;
- `tools/ai_server/task_registry.py` ;
- `tools/ai_server/event_hub.py` ;
- `tools/ai_server/openai_adapter.py` ;
- `tools/ai_server/server.py` ;
- `scenes/learning/ch12_network_ai_demo.gd`.

Audit : `Livre-II/QA/AUDIT-CHAPITRE-12.md`.

Preuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-12.yaml`.

Décision : accepté avec réserves runtime et PDF de fin de Livre.

## 20. Erreurs à ne pas reproduire"""
replace_once("CONTINUITE-PROJET.md", "## 19. Erreurs à ne pas reproduire", chapter12_section)

replace_once(
    "CONTINUITE-PROJET.md",
    "- ne pas coupler le port applicatif à HTTP avant le chapitre 12 ;\n- ne pas utiliser `OS.kill()` avant la tentative d’arrêt coopératif ;",
    "- ne pas coupler le port applicatif à HTTP avant le chapitre 12 ;\n- ne pas utiliser `OS.kill()` avant la tentative d’arrêt coopératif ;\n- ne pas placer les routes HTTP dans le gameplay ;\n- ne pas utiliser WebSocket pour tous les échanges ;\n- ne pas lancer plusieurs requêtes simultanées sur une même instance `HTTPRequest` ;\n- ne pas confondre résultat de transport et code HTTP ;\n- ne pas retenter immédiatement après `429` ;\n- ne pas laisser une file de tâches sans limite ;\n- ne pas confondre corrélation et idempotence ;\n- ne pas accepter la même clé d’idempotence pour deux payloads différents ;\n- ne pas traiter `CANCEL_REQUESTED` comme un état terminal ;\n- ne pas appliquer un événement WebSocket hors séquence ;\n- ne pas traiter un fragment de streaming comme résultat final ;\n- ne pas laisser un schéma OpenAI-compatible devenir le modèle du domaine ;\n- ne pas déclarer le service prêt lorsque ses dépendances obligatoires sont indisponibles ;\n- ne pas utiliser un identifiant de tâche comme autorisation ;\n- ne pas promettre une reprise après panne avec une file volatile ;\n- ne pas masquer une erreur de protocole par le repli ;",
)
replace_once("CONTINUITE-PROJET.md", "## 20. État courant", "## 21. État courant")
replace_once("CONTINUITE-PROJET.md", "- progression : 11 chapitres sur 30 ;", "- progression : 12 chapitres sur 30 ;")
replace_once(
    "CONTINUITE-PROJET.md",
    "- chapitre 11 : version `1.0.0` ;",
    "- chapitre 11 : version `1.0.0` ;\n- chapitre 12 : version `1.0.1` ;",
)
replace_once("CONTINUITE-PROJET.md", "## 21. Prochaine action", "## 22. Prochaine action")
replace_once(
    "CONTINUITE-PROJET.md",
    "Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md",
    "Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md",
)
old_scope = """- mise en œuvre du port du chapitre 11 avec des transports réseau ;
- choix entre `HTTPRequest`, `HTTPClient` et `WebSocketPeer` ;
- contrats HTTP versionnés, en-têtes, types de contenu et codes de statut ;
- API compatibles OpenAI sans dépendance directe à un fournisseur ;
- streaming de réponses et événements ;
- files de tâches locales ou serveur ;
- identifiants de tâches, états et résultats ;
- idempotence, retries bornés et backoff ;
- délais et annulation à travers le transport ;
- polling, notification et reprise ;
- backpressure et limites de concurrence ;
- erreurs réseau structurées ;
- découverte de santé et de capacités ;
- aucun secret réel dans les exemples ;
- durcissement production/runtime réservé au chapitre 13 ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire."""
new_scope = """- modèle de menaces et frontières de confiance ;
- séparation stricte entre outils de production et services autorisés au runtime ;
- configurations distinctes développement, test et production ;
- secrets hors versionnement et hors payloads de gameplay ;
- écoute sur boucle locale par défaut et refus de l’exposition implicite ;
- authentification obligatoire dès qu’un service quitte la boucle locale ;
- TLS et certificats lorsque le réseau l’exige ;
- listes d’autorisation pour opérations, modèles et chemins ;
- moindre privilège pour processus, fichiers et réseau ;
- limites de payload, débit, concurrence et quotas ;
- rédaction des journaux et politique de conservation ;
- dépendances épinglées, inventaire, licences et SBOM ;
- packaging, signature et stratégie de mise à jour ;
- échec fermé pour la sécurité avec repli déterministe du gameplay ;
- parcours Solo et Studio ;
- audit statique sans PDF intermédiaire."""
replace_once("CONTINUITE-PROJET.md", old_scope, new_scope)
replace_once(
    "CONTINUITE-PROJET.md",
    "Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.\n\n## 22. Journal",
    "Recommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.\n\n## 23. Journal\n\n### 2026-07-19 — version 3.13.0\n\n- création, correction et audit statique du chapitre 12 ;\n- conservation de `LocalAiGateway` comme port canonique ;\n- transports HTTP et WebSocket derrière des adaptateurs ;\n- contrats réseau versionnés, limites avant téléchargement et erreurs structurées ;\n- tâches longues, file prioritaire bornée et backpressure ;\n- idempotence, retries bornés, polling, séquences et annulation coopérative ;\n- compatibilité OpenAI isolée et API Responses explicitement qualifiée ;\n- progression à 12 chapitres sur 30 ;\n- prochaine action déplacée vers le chapitre 13 ;\n- aucun PDF construit.\n",
)
