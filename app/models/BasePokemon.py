class BasePokemon:
    """
    Représente les informations de base d'un Pokémon
    telles qu'elles proviennent de la PokéAPI.
    Ces données ne changent pas pendant le combat.
    """
    def __init__(self, name, id, types, stats, abilities, movepool, sprites):
        self.name = name
        self.id = id
        self.types = types              # ex: ["fire", "flying"]
        self.stats = stats              # ex: {"hp": 78, "attack": 84, ...}
        self.abilities = abilities          # ex: ["blaze", "solar-power"]
        self.movepool = movepool        # ex: ["flamethrower", "fly", "heat-wave", ...]
        self.sprites = sprites          # URL de l’image officielle

    def __str__(self):
        return f"{self.name.title()} (#{self.id}) — Types: {', '.join(self.types)}"
