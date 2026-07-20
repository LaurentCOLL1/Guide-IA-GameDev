from pathlib import Path
import re

FILES = {
    15: Path('Livre-II/CHAPITRE-15-Relations-sociales.md'),
    16: Path('Livre-II/CHAPITRE-16-Famille-et-generations.md'),
}


def once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1, got {count}')
    return text.replace(old, new, 1)


def anchor(text, heading, anchor_id):
    target = f'<a id="{anchor_id}"></a>\n\n{heading}'
    return text if target in text else once(text, heading, target, anchor_id)


anchors = {
    15: {
        '## 3. Périmètre et frontières': 'ch15-system-boundaries',
        '### 4.1 Une relation est dirigée': 'ch15-directed-relation',
        '### 6.1 Clé de relation': 'ch15-relationship-key',
        '## 7. Représenter les axes sociaux': 'ch15-social-axes',
        '## 9. Commander un changement social': 'ch15-change-command',
        '### 10.2 Pourquoi l’historique reste borné': 'ch15-bounded-history',
        '## 15. Service applicatif': 'ch15-social-service',
        '## 17. Requêtes de voisinage': 'ch15-neighborhood-queries',
        '## 23. Restaurer l’historique sans exposer la collection': 'ch15-history-encapsulation',
        '## 24. Encoder et décoder les axes': 'ch15-axis-codec',
        '## 27. Ordre de restauration': 'ch15-restoration-order',
    },
    16: {
        '## 3. Périmètre et frontières': 'ch16-system-boundaries',
        '### 6.1 Intervalle logique': 'ch16-logical-interval',
        '### 7.1 Modèle de lien': 'ch16-parent-link-model',
        '### 7.2 Identité métier de la filiation': 'ch16-parentage-identity',
        '### 9.1 Paire non orientée': 'ch16-canonical-pair',
        '### 11.1 Stockages internes': 'ch16-family-storage',
        '### 11.3 Cycle d’ascendance': 'ch16-ancestry-cycle',
        '### 12.1 Parents et enfants directs': 'ch16-defensive-parent-child-queries',
        '### 15.3 Orchestration': 'ch16-family-service',
        '## 19. Construction atomique du graphe candidat': 'ch16-candidate-graph',
    },
}

links15 = [
    ('> **À relire :** [§ 6. Identifier une relation dirigée](#6-identifier-une-relation-dirigee).', '> **À relire :** [§ 6.1 Clé de relation](#ch15-relationship-key).'),
    ('> **À relire :** [§ 4.1 Une relation est dirigée](#41-une-relation-est-dirigee).', '> **À relire :** [§ 4.1 Une relation est dirigée](#ch15-directed-relation).'),
    ('> **À relire :** [§ 7. Représenter les axes sociaux](#7-representer-les-axes-sociaux).', '> **À relire :** [§ 7. Représenter les axes sociaux](#ch15-social-axes).'),
    ('> **À relire :** [§ 9. Commander un changement social](#9-commander-un-changement-social).', '> **À relire :** [§ 9. Commander un changement social](#ch15-change-command).'),
    ('> **À relire :** [§ 23. Restaurer l’historique sans exposer la collection](#23-restaurer-lhistorique-sans-exposer-la-collection).', '> **À relire :** [§ 10.2 Pourquoi l’historique reste borné](#ch15-bounded-history).'),
    ('> **À relire :** [§ 12. Dépôt de relations](#12-depot-de-relations).', '> **À relire :** [§ 23. Restaurer l’historique sans exposer la collection](#ch15-history-encapsulation).'),
    ('> **À relire :** [§ 17. Requêtes de voisinage](#17-requetes-de-voisinage).', '> **À relire :** [§ 17. Requêtes de voisinage](#ch15-neighborhood-queries).'),
    ('> **À relire :** [§ 24. Encoder et décoder les axes](#24-encoder-et-decoder-les-axes).', '> **À relire :** [§ 24. Encoder et décoder les axes](#ch15-axis-codec).'),
    ('> **À relire :** [§ 27. Ordre de restauration](#27-ordre-de-restauration).', '> **À relire :** [§ 27. Ordre de restauration](#ch15-restoration-order).'),
]

links16 = [
    ('> **À relire :** [§ 7.2 Identité métier de la filiation](#72-identite-metier-de-la-filiation).', '> **À relire :** [§ 7.2 Identité métier de la filiation](#ch16-parentage-identity).'),
    ('> **À relire :** [§ 11. Graphe familial](#11-graphe-familial).', '> **À relire :** [§ 11.1 Stockages internes](#ch16-family-storage).'),
    ('> **À relire :** [§ 7. Filiation dirigée](#7-filiation-dirigee).', '> **À relire :** [§ 7.1 Modèle de lien](#ch16-parent-link-model).'),
    ('> **À relire :** [§ 18.5 Intervalles, tutelles et unions](#185-intervalles-tutelles-et-unions).', '> **À relire :** [§ 9.1 Paire non orientée](#ch16-canonical-pair).'),
    ('> **À relire :** [§ 18.4 Décodage strict d’une filiation](#184-decodage-strict-dune-filiation).', '> **À relire :** [§ 15.3 Orchestration](#ch16-family-service).'),
    ('> **À relire :** [§ 3. Périmètre et frontières](#3-perimetre-et-frontieres).', '> **À relire :** [§ 3. Périmètre et frontières](#ch16-system-boundaries).'),
]

metrics = {}
for chapter, path in FILES.items():
    text = path.read_text(encoding='utf-8')
    text = once(text, 'version: "1.2.0"', 'version: "1.2.1"', f'ch{chapter} version')
    if chapter == 15:
        text = once(text,
            '- **Pourquoi cet exemple est fautif :** l’extrait viole la règle métier rappelée dans « 6.2 Pourquoi ne pas trier les identifiants ».',
            '- **Pourquoi cet exemple est fautif :** l’extrait viole la règle métier.', 'ch15 self title')
        text = once(text,
            '- **Rôle :** ce bloc montre la forme JSON attendue par « 21.1 Forme JSON ».',
            '- **Rôle :** ce bloc décrit le document persistant d’une relation sociale : identité orientée, axes, révision, tick et historique causal.', 'ch15 JSON role')
        for old, new in links15:
            text = once(text, old, new, old)
        repeated = '> **À relire :** [§ 14. Événement social typé](#14-evenement-social-type).'
        if text.count(repeated) != 2:
            raise RuntimeError('ch15 repeated link count')
        text = text.replace(repeated, '> **À relire :** [§ 3. Périmètre et frontières](#ch15-system-boundaries).', 1)
        text = text.replace(repeated, '> **À relire :** [§ 15. Service applicatif](#ch15-social-service).', 1)
        expected_links = 11
        self_removed, roles_fixed = 2, 0
    else:
        text = once(text,
            '- **Rôle :** ce bloc montre la forme JSON attendue par « 18.1 Structure JSON ».',
            '- **Rôle :** ce bloc décrit le snapshot du graphe familial, séparé en filiations, tutelles, unions et historique.', 'ch16 JSON role')
        bad = '- **Rôle :** ce bloc illustre volontairement une normalisation incorrecte qui détruit l’ordre métier.'
        if text.count(bad) != 2:
            raise RuntimeError(f'ch16 incorrect role count: expected 2, got {text.count(bad)}')
        text = text.replace(bad,
            '- **Rôle :** ces deux requêtes reconstruisent les parents et les enfants depuis les liens autoritaires sans exposer les index internes.', 1)
        text = text.replace(bad,
            '- **Rôle :** cette requête dérive la fratrie depuis les parents partagés au lieu de la persister.', 1)
        for old, new in links16:
            text = once(text, old, new, old)
        cycle = '> **À relire :** [§ 11.3 Cycle d’ascendance](#113-cycle-dascendance).'
        logical = '> **À relire :** [§ 6.1 Intervalle logique](#61-intervalle-logique).'
        candidate = '> **À relire :** [§ 19. Construction atomique du graphe candidat](#19-construction-atomique-du-graphe-candidat).'
        if text.count(cycle) != 2 or text.count(logical) != 2 or text.count(candidate) != 2:
            raise RuntimeError('ch16 repeated link counts')
        text = text.replace(cycle, '> **À relire :** [§ 11.3 Cycle d’ascendance](#ch16-ancestry-cycle).')
        text = text.replace(logical, '> **À relire :** [§ 6.1 Intervalle logique](#ch16-logical-interval).')
        text = text.replace(candidate, '> **À relire :** [§ 12.1 Parents et enfants directs](#ch16-defensive-parent-child-queries).', 1)
        text = text.replace(candidate, '> **À relire :** [§ 19. Construction atomique du graphe candidat](#ch16-candidate-graph).', 1)
        expected_links = 12
        self_removed, roles_fixed = 1, 2

    for heading, anchor_id in anchors[chapter].items():
        text = anchor(text, heading, anchor_id)

    current = None
    reread = []
    for line_no, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^#{2,6}\s+(.+?)\s*$', line)
        if match:
            current = match.group(1)
            continue
        if current and line.lstrip().startswith('- **') and current in line:
            raise RuntimeError(f'ch{chapter}:{line_no}: self-title mention remains')
        if line.startswith('> **À relire :**'):
            reread.append((line_no, line))
    if len(reread) != expected_links:
        raise RuntimeError(f'ch{chapter}: expected {expected_links} reread links, got {len(reread)}')
    for line_no, line in reread:
        m = re.search(r'\]\(#([^)]+)\)', line)
        if not m or f'<a id="{m.group(1)}"></a>' not in text:
            raise RuntimeError(f'ch{chapter}:{line_no}: unresolved explicit anchor')
    if 'normalisation incorrecte qui détruit l’ordre métier' in text:
        raise RuntimeError(f'ch{chapter}: false role remains')

    path.write_text(text, encoding='utf-8')
    metrics[chapter] = (self_removed, roles_fixed, expected_links, len(anchors[chapter]), len(text.splitlines()))

Path('tmp_precise_section_references_metrics.txt').write_text(
    '\n'.join(
        f'chapter {chapter}: self_title_removed={m[0]}, roles_fixed={m[1]}, links_fixed={m[2]}, anchors_added={m[3]}, lines={m[4]}'
        for chapter, m in metrics.items()
    ) + '\n', encoding='utf-8')
