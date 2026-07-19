from pathlib import Path

path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one occurrence, found {count}: {old[:80]!r}")
    text = text.replace(old, new, 1)


replace_once('version: "3.13.1"', 'version: "3.14.0"')
replace_once('**En cours : 12 chapitres sur 30.**', '**En cours : 13 chapitres sur 30.**')
replace_once(
    '13. Sécurité et séparation production/runtime de l’IA — prochain chapitre.',
    '13. Sécurité et séparation production/runtime de l’IA — terminé au niveau `static-review`.'
)
replace_once('Chapitres 3 à 12 : **Élevée**.', 'Chapitres 3 à 13 : **Élevée**.')

replace_once(
    '- le durcissement de production reste réservé au chapitre 13.\n\n## 12. Chapitre 5 — état résumé',
    '''- le durcissement de production est traité au chapitre 13.\n\n### 11.8 Sécurité et séparation production/runtime\n\n- modèle de menaces maintenu avec actifs, frontières et menaces prioritaires ;\n- quatre zones séparées : production, livraison, runtime distribué et données du joueur ;\n- capacités de production exclues du package runtime ;\n- profils `development`, `test` et `production` distincts ;\n- secrets hors dépôt, hors `res://`, hors payloads métier et hors journaux ;\n- écoute sur `127.0.0.1` par défaut, adresses non spécifiées refusées ;\n- authentification et TLS obligatoires lorsque le service quitte la boucle locale ;\n- autorisation par défaut refusée pour opérations, modèles et chemins ;\n- `task_id` et identifiants similaires ne valent jamais autorisation ;\n- chemins canoniques résolus sous des racines autorisées ;\n- processus exécuté sans privilège administrateur ni clé de publication ;\n- payloads, résultats, délais, débit, tâches et concurrence bornés ;\n- journaux rédigés, rotatifs et sans en-tête `Authorization` ;\n- dépendances épinglées et licences inventoriées ;\n- SBOM, provenance, signature et rollback préparés pour la publication ;\n- violation de sécurité refusée sans contournement par le repli ;\n- repli déterministe conservé uniquement pour les indisponibilités fonctionnelles prévues.\n\n## 12. Chapitre 5 — état résumé'''
)

chapter13 = '''## 20. Chapitre 13 — état détaillé\n\nFichier : `Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md`.\n\nNiveau : **GPT-5.6 Sol — Élevée**.\n\nDécisions enregistrées :\n\n- modèle de menaces versionné et relu lors des changements de surface ;\n- production, livraison, runtime et données du joueur séparés par des frontières explicites ;\n- outils d’indexation, diagnostics et secrets de signature absents du package runtime ;\n- profils d’environnement avec debug, journaux, administration, TLS et authentification explicites ;\n- secrets exclus du dépôt, de `res://`, des payloads métier et des journaux ;\n- `.godot/export_credentials.cfg`, fichiers `.env`, clés et certificats privés ignorés ;\n- jetons générés avec `secrets` et comparés avec `hmac.compare_digest` ;\n- boucle locale par défaut et refus des adresses non spécifiées ;\n- authentification et TLS exigés hors loopback ;\n- autorisation `deny-by-default` par identité et capacité ;\n- listes d’autorisation pour opérations, modèles, extensions et racines de chemins ;\n- résolution canonique des chemins sous une racine autorisée ;\n- `TLSOptions.client_unsafe()` exclu du profil production ;\n- moindre privilège pour fichiers, réseau, variables, temps et mémoire ;\n- limites de corps, résultat, tâches, débit et timeout ;\n- journaux structurés avec rédaction des champs sensibles ;\n- dépendances réelles épinglées sans faux fichier de verrouillage ;\n- SBOM CycloneDX ou SPDX choisi selon l’outillage réel ;\n- provenance reliant commit, outils, paramètres non secrets et hachages ;\n- signature de publication distincte d’un simple hachage ;\n- mise à jour versionnée avec vérification et rollback ;\n- échec fermé pour authentification, autorisation, signature et validation ;\n- repli déterministe réservé aux indisponibilités fonctionnelles ;\n- systèmes de gameplay réservés à partir du chapitre 14.\n\nLivrables documentés :\n\n- `docs/security/threat-model.md` ;\n- `config/ai-capabilities.yaml` ;\n- `config/ai-server-production.toml` ;\n- `config/runtime-models.yaml` ;\n- `res://src/core/security/runtime_profile.gd` ;\n- `res://src/core/security/tls_policy.gd` ;\n- `res://src/core/security/security_policy.gd` ;\n- `tools/security/secret_provider.py` ;\n- `tools/security/generate_local_token.py` ;\n- `tools/security/redaction.py` ;\n- `tools/ai_server/security_config.py` ;\n- `tools/ai_server/authentication.py` ;\n- `tools/ai_server/authorization.py` ;\n- `tools/ai_server/safe_paths.py` ;\n- `tools/ai_server/tls_context.py` ;\n- `tools/ai_server/security_limits.py`.\n\nAudit : `Livre-II/QA/AUDIT-CHAPITRE-13.md`.\n\nPreuve : `Livre-II/QA/VALIDATION-FINALE-CHAPITRE-13.yaml`.\n\nDécision : accepté avec réserves runtime et PDF de fin de Livre.\n\n'''
replace_once('## 20. Erreurs à ne pas reproduire', chapter13 + '## 21. Erreurs à ne pas reproduire')

replace_once(
    '- ne pas masquer une erreur de protocole par le repli ;\n- ne pas construire le PDF à chaque chapitre ;',
    '''- ne pas masquer une erreur de protocole par le repli ;\n- ne pas livrer les outils de production dans le runtime ;\n- ne pas écouter sur `0.0.0.0` ou `::` par défaut ;\n- ne pas stocker un jeton dans `res://` ou dans le dépôt ;\n- ne pas confondre authentification, autorisation et chiffrement ;\n- ne pas utiliser un identifiant de tâche comme permission ;\n- ne pas utiliser `TLSOptions.client_unsafe()` en production ;\n- ne pas ouvrir directement un chemin fourni par le client ;\n- ne pas journaliser `Authorization`, jetons ou payloads complets ;\n- ne pas utiliser `random` pour un jeton de sécurité ;\n- ne pas inclure une clé privée dans le package client ;\n- ne pas publier sans inventaire des dépendances et SBOM ;\n- ne pas présenter un hachage seul comme preuve d’origine ;\n- ne pas contourner un refus de sécurité par un repli ;\n- ne pas conserver le debug de développement en production ;\n- ne pas construire le PDF à chaque chapitre ;'''
)

replace_once('## 21. État courant', '## 22. État courant')
replace_once('- progression : 12 chapitres sur 30 ;', '- progression : 13 chapitres sur 30 ;')
replace_once(
    '- chapitre 12 : version `1.0.2` ;\n- Starter Kit non matérialisé ;',
    '- chapitre 12 : version `1.0.2` ;\n- chapitre 13 : version `1.0.0` ;\n- Starter Kit non matérialisé ;'
)

old_next = '''## 22. Prochaine action\n\nChapitre :\n\n> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md\n```\n\nPérimètre attendu :\n\n- modèle de menaces et frontières de confiance ;\n- séparation stricte entre outils de production et services autorisés au runtime ;\n- configurations distinctes développement, test et production ;\n- secrets hors versionnement et hors payloads de gameplay ;\n- écoute sur boucle locale par défaut et refus de l’exposition implicite ;\n- authentification obligatoire dès qu’un service quitte la boucle locale ;\n- TLS et certificats lorsque le réseau l’exige ;\n- listes d’autorisation pour opérations, modèles et chemins ;\n- moindre privilège pour processus, fichiers et réseau ;\n- limites de payload, débit, concurrence et quotas ;\n- rédaction des journaux et politique de conservation ;\n- dépendances épinglées, inventaire, licences et SBOM ;\n- packaging, signature et stratégie de mise à jour ;\n- échec fermé pour la sécurité avec repli déterministe du gameplay ;\n- parcours Solo et Studio ;\n- audit statique sans PDF intermédiaire.\n\nRecommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.'''
new_next = '''## 23. Prochaine action\n\nChapitre :\n\n> **[LECTURE] Chemin prévisionnel — Ne pas saisir.**\n\n```text\nLivre-II/CHAPITRE-14-Personnages.md\n```\n\nPérimètre attendu :\n\n- premier des douze systèmes de gameplay ;\n- identité stable d’un personnage indépendante de son nom affiché ;\n- séparation entre définition de conception, état runtime et persistance ;\n- données de base, attributs, statistiques dérivées et validation ;\n- composition de la scène de personnage et responsabilités des composants ;\n- séparation entre personnage, contrôleur, représentation visuelle et corps physique ;\n- réutilisation des entrées, caméra et interactions du chapitre 6 ;\n- création, apparition, désapparition et registre limité des personnages actifs ;\n- événements typés pour les changements importants ;\n- sérialisation vers le système de sauvegarde sans inclure les caches dérivés ;\n- frontières explicites avec relations sociales, famille, agents autonomes, combat et compétences ;\n- démonstration pédagogique, critères d’acceptation et tests à préparer ;\n- parcours Solo et Studio ;\n- audit statique sans PDF intermédiaire.\n\nRecommandation probable : **GPT-5.6 Sol — Élevée**, à annoncer et justifier avant rédaction.'''
replace_once(old_next, new_next)
replace_once('## 23. Journal', '## 24. Journal')
replace_once(
    '## 24. Journal\n\n### 2026-07-19 — version 3.13.1',
    '''## 24. Journal\n\n### 2026-07-19 — version 3.14.0\n\n- création, correction et audit statique du chapitre 13 ;\n- modèle de menaces et frontières de confiance documentés ;\n- séparation stricte entre production, livraison, runtime et données du joueur ;\n- profils développement, test et production ;\n- secrets hors dépôt et hors package ;\n- boucle locale par défaut, authentification et TLS hors loopback ;\n- autorisation par défaut refusée et listes d’autorisation ;\n- chemins canoniques, moindre privilège, limites et quotas ;\n- journaux rédigés et rétention distincte Solo/Studio ;\n- dépendances épinglées, licences, SBOM, provenance et signature préparés ;\n- échec fermé sans contournement par le repli déterministe ;\n- plateforme IA locale terminée à quatre chapitres sur quatre ;\n- progression à 13 chapitres sur 30 ;\n- prochaine action déplacée vers le chapitre 14 — Personnages ;\n- aucun PDF construit.\n\n### 2026-07-19 — version 3.13.1'''
)

path.write_text(text, encoding="utf-8")
print("CONTINUITE-PROJET.md updated for chapter 13")
