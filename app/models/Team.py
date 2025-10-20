from app.models.SetPokemon import SetPokemon

class Team:
    def __init__(self):
        self.pokemons = []

    def add_pokemon(self, set_pokemon: SetPokemon):
        if len(self.pokemons) < 6:
            self.pokemons.append(set_pokemon)
        else:
            raise Exception("A team can only have 6 Pokémons.")

    def remove_pokemon(self, index):
        self.pokemons.pop(index)

    def __str__(self):
        team_str = "TEAM:\n"
        for pokemon in self.pokemons:
            team_str += str(pokemon) + "\n---------------------------- \n"
        return team_str
