from .BasePokemon import BasePokemon
from .Natures import Natures
from .Items import Items

class SetPokemon:
    def __init__(self, base_pokemon: BasePokemon):
        self.base_pokemon = base_pokemon
        self.nature = Natures("hardy")  # nature par défaut

        # IV/EV doivent exister avant d'appeler calculate_stat
        self.IV = {
            "hp": 31,
            "attack": 31,
            "defense": 31,
            "special-attack": 31,
            "special-defense": 31,
            "speed": 31
        }
        self.EV = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special-attack": 0,
            "special-defense": 0,
            "speed": 0
        }

        level = 50  # niveau par défaut
        self.level = level

        # calculer le HP séparément puis les autres stats
        self.stats = {}
        self.stats["hp"] = self.calculate_stat("hp", level)
        for s in ["attack", "defense", "special-attack", "special-defense", "speed"]:
            self.stats[s] = self.calculate_stat(s, level)

        self.current_hp = self.stats["hp"]

        self.moves = [None, None, None, None]
        self.ability = None
        self.item = "aucun"
        self.status = "neutre"
        self.modified_stats = {"attack": 0, "defense": 0, "special-attack": 0, "special-defense": 0, "speed": 0, "accuracy": 0, "evasion": 0}

    
    def set_moves(self, moves: list):
        if len(moves) > 4:
            raise ValueError("A Pokémon can only have up to 4 moves")
        # fixme: vérifier que les moves sont dans le movepool du pokémon
        for move in moves:
            if move not in self.base_pokemon.movepool:
                raise ValueError(f"The move {move} is not in the movepool of {self.base_pokemon.name}")
        self.moves = moves

    def set_ability(self, ability = None):
        if  len(self.base_pokemon.abilities) == 1:
            self.ability = self.base_pokemon.abilities[0]
        elif ability in self.base_pokemon.abilities:
            self.ability = ability
        else:
            raise ValueError("Invalid ability for this Pokémon")

    def set_nature(self, nature: Natures):
        self.nature = nature
        self.nature.nature_modifier = self.nature.get_nature_modifier(nature.name)
        for stat in self.stats.keys():
            self.stats[stat] = self.calculate_stat(stat, self.level)

    def set_item(self, item: Items):
        self.item = item

    def __str__(self):
        nature_name = self.nature.name if self.nature else "Aucune"
        return f"{self.base_pokemon.name} (Niveau {self.level}) - talent: {self.ability} - objet: {self.item} - Nature: {nature_name}\nStats: {self.stats}"
        
    def calculate_stat(self, stat_name, level):
        # ne pas appliquer de modificateur de nature sur le HP
        if stat_name == "hp":
            nature_modifier = 1.0
        else:
            # sécurité : utiliser .get pour éviter KeyError si la nature n'a pas la clé
            nature_modifier = self.nature.nature_modifier.get(stat_name, 1.0) if self.nature else 1.0

        base_stat = self.base_pokemon.stats[stat_name]
        iv = self.IV.get(stat_name, 0)
        ev = self.EV.get(stat_name, 0)

        if stat_name == "hp":
            if self.base_pokemon.id == 292:  # Munja
                return 1
            return (((2 * base_stat + iv + (ev // 4)) * level) // 100 )+ level + 10
        else:
            return int(((((2 * base_stat + iv + (ev // 4)) * level) // 100) + 5) * nature_modifier)
    
    def set_IV(self, stat_name, value):
        if 0 <= value <= 31:
            self.IV[stat_name] = value
        else:
            raise ValueError("IV must be between 0 and 31")
        # recalculer la stat modifiée
        self.stats[stat_name] = self.calculate_stat(stat_name, self.level)
    
    def set_EV(self, stat_name, value):
        # verifier que la somme des EV ne dépasse pas 510 et que chaque EV ne dépasse pas 252
        current_total_ev = sum(self.EV.values())
        remaining_ev = 510 - current_total_ev
        if value < 0 or value > 252 or value > remaining_ev:
            raise ValueError("Invalid EV value")
        self.EV[stat_name] = value
        # recalculer la stat modifiée
        self.stats[stat_name] = self.calculate_stat(stat_name, self.level)

    
