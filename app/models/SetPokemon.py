import BasePokemon
import Natures

class SetPokemon:
    def __init__(self, base_pokemon: BasePokemon, level):
        self.base_pokemon = base_pokemon
        self.current_hp = self.calculate_stat("hp", level)
        self.level = level
        self.nature = "hardy"  # par défaut, nature neutre
        self.IV = {
            "hp": 31,
            "attack": 31,
            "defense": 31,
            "special_attack": 31,
            "special_defense": 31,
            "speed": 31
        }
        self.EV = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0
        }
        self.moves = [None, None, None, None]
        self.ability = None
        self.item = None
        self.status = "neutre"
        self.modified_stats = {"attack": 0, "defense": 0, "special_attack": 0, "special_defense": 0, "speed": 0, "accuracy": 0, "evasion": 0}
    
    def set_nature(self, nature: Natures):
        self.nature = nature.name
        self.nature_modifier = nature.get_nature_modifier()
 
    def calculate_stat(self, stat_name, level, nature_modifier=1.0):
        base_stat = self.base_pokemon.stats[stat_name]
        iv = self.IV[stat_name]
        ev = self.EV[stat_name]
        if stat_name == "hp":
            if self.base_pokemon.id == 292:  # Munja bien sûr sinon c'est pas drôle
                return 1
            return ((2 * base_stat + iv + (ev // 4)) * level) // 100 + level + 10
        else:
            return (((2 * base_stat + iv + (ev // 4)) * level) // 100 + 5) * nature_modifier
        
    def set_IV(self, stat_name, value):
        if 0 <= value <= 31:
            self.IV[stat_name] = value
        else:
            raise ValueError("IV must be between 0 and 31")
    
    def set_EV(self, stat_name, value):
        # verifier que la somme des EV ne dépasse pas 510 et que chaque EV ne dépasse pas 252
        current_total_ev = sum(self.EV.values())
        remaining_ev = 510 - current_total_ev
        if value < 0 or value > 252 or value > remaining_ev:
            raise ValueError("Invalid EV value")
        self.EV[stat_name] = value

    
