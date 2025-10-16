from app.services.pokeapi_service import PokeAPIService

class PokemonController:
    def __init__(self):
        self.service = PokeAPIService()

    def afficher_pokemon(self, name_or_id):
        pokemon = self.service.get_pokemon(name_or_id)
        print(pokemon)
        print("Stats :", pokemon.stats)
        print("Talents :", ", ".join(pokemon.abilities))
        print("Nombre d'attaques possibles :", len(pokemon.movepool))
        print("Sprite :", pokemon.sprites)
        return pokemon
    
    def afficher_move(self,name_or_id):
        move = self.service.get_move(name_or_id)
        print(move)
        return move
    
    def afficher_talent(self,name_or_id):
        talent = self.service.get_ability(name_or_id)
        print(talent)
        return talent
    
    def afficher_nature(self,name_or_id):
        nature = self.service.get_nature(name_or_id)
        print(nature)
        return nature
    
    def  afficher_item(self,name_or_id):
        item = self.service.get_item(name_or_id)
        print(item)
        return item