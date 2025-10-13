from app.services.pokeapi_service import PokeAPIService

class PokemonController:
    def __init__(self):
        self.service = PokeAPIService()

    def afficher_pokemon(self, name_or_id):
        pokemon = self.service.get_pokemon(name_or_id)
        print(pokemon)
        print("Stats :", pokemon.stats)
        print("Talents :", ", ".join(pokemon.talents))
        print("Nombre d'attaques possibles :", len(pokemon.movepool))
        print("Sprite :", pokemon.sprites)
        return pokemon
