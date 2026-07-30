"""Backend volontairement non publiable.

Le pack n'est pas distribué comme paquet tant que la licence globale reste indécise.
"""

def build_wheel(*args, **kwargs):
    raise RuntimeError("La construction de paquet est bloquée avant décision de licence globale.")
