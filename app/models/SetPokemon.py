from .BasePokemon import BasePokemon
from .Natures import Natures
from .Items import Items
from .Moves import Moves

class SetPokemon:
    def __init__(self, base_pokemon: BasePokemon):
        self.base_pokemon = base_pokemon
        self.nature = Natures()
        self.IV = {"hp": 31,"attack": 31,"defense": 31,"special-attack": 31,"special-defense": 31,"speed": 31}
        self.EV = {"hp": 0,"attack": 0,"defense": 0,"special-attack": 0,"special-defense": 0,"speed": 0}
        self.level = self.set_level()
        self.happiness = self.set_happiness()
        self.stats = {}
        self.stats["hp"] = self.calculate_stat("hp", self.level)
        for s in ["attack", "defense", "special-attack", "special-defense", "speed"]:
            self.stats[s] = self.calculate_stat(s, self.level)

        self.current_hp = self.stats["hp"]

        self.moves = [None, None, None, None]
        self.ability = self.set_ability()
        self.item = None

        # statut et modificateurs de stats en combat
        self.status = "neutre"
        self.modified_stats = {"attack": 0, "defense": 0, "special-attack": 0, "special-defense": 0, "speed": 0, "accuracy": 0, "evasion": 0}

    def set_happiness(self, happiness=255):
        if happiness < 0 or happiness > 255:
            raise ValueError("Happiness must be between 0 and 255")
        self.happiness = happiness
        return happiness

    def set_level(self, level=50):
        if level < 1 or level > 100:
            raise ValueError("Level must be between 1 and 100")
        self.level = level
        return level

    def set_moves(self, moves: list[Moves]):
        if len(moves) > 4:
            raise ValueError("A Pokémon can only have up to 4 moves")
        # fixme: vérifier que les moves sont dans le movepool du pokémon
        for move in moves:
            if move not in self.base_pokemon.movepool or move is None:
                move = "<vide>"
        self.moves = moves
        return moves

    def set_ability(self, ability = None):
        if  len(self.base_pokemon.abilities) == 1 or ability is None:
            self.ability = self.base_pokemon.abilities[0]
        elif ability in self.base_pokemon.abilities:
            self.ability = ability
        else:
            raise ValueError("Invalid ability for this Pokémon")
        return self.ability

    def set_nature(self, nature: Natures = None):
        if nature is None:
            nature = Natures()  # ✅ crée une instance neuve
        self.nature = nature
        self.nature.nature_modifier = self.nature.get_nature_modifier(nature.name)
        for stat in self.stats.keys():
            self.stats[stat] = self.calculate_stat(stat, self.level)
        return self.nature

    def set_item(self, item : Items = None):
        if item is None:
            item = Items()
        self.item = item
        return item
      
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
    
    def set_IV(self, hp=31, atk=31, defense=31, spatk=31, spdef=31, spd=31):
        for iv in [hp, atk, defense, spatk, spdef, spd]:
            if iv < 0 or iv > 31:
                raise ValueError("Each IV must be between 0 and 31")
        self.IV["hp"] = hp
        self.IV["attack"] = atk
        self.IV["defense"] = defense
        self.IV["special-attack"] = spatk
        self.IV["special-defense"] = spdef
        self.IV["speed"] = spd
        # recalculer toutes les stats modifiées
        for stat in self.stats.keys():
            self.stats[stat] = self.calculate_stat(stat, self.level)
    
    def set_EV(self, hp=0, atk=0, defense=0, spatk=0, spdef=0, spd=0):
        # vérifier que la somme des EV ne dépasse pas 510 et que chaque EV est entre 0 et 252
        total_ev = hp + atk + defense + spatk + spdef + spd
        if total_ev > 510:
            raise ValueError("Total EVs cannot exceed 510")
        for ev in [hp, atk, defense, spatk, spdef, spd]:
            if ev < 0 or ev > 252:
                raise ValueError("Each EV must be between 0 and 252")
        self.EV["hp"] = hp
        self.EV["attack"] = atk
        self.EV["defense"] = defense
        self.EV["special-attack"] = spatk
        self.EV["special-defense"] = spdef
        self.EV["speed"] = spd
        # recalculer toutes les stats modifiées
        for stat in self.stats.keys():
            self.stats[stat] = self.calculate_stat(stat, self.level)
    
    def __str__(self):
        nature_name = self.nature.name if self.nature else "Aucune"
        return f"{self.base_pokemon.name} (Niveau {self.level}) - talent: {self.ability} - objet: {self.item.name} - Nature: {nature_name}\nStats: {self.stats}\nMoves: {[str(move) if move else '<vide>' for move in self.moves]}\nIVs: {self.IV}\nEVs: {self.EV}"
  