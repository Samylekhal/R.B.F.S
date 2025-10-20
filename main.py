from app.controllers.pokemon_controller import PokemonController
from app.services.constantes import MAX_NATURE
from app.models.Team import Team

if __name__ == "__main__":
    controller = PokemonController()
    i = 1
    team = Team()
    team.add_pokemon(controller.get_Setpokemon("shedinja")) 
    team.add_pokemon(controller.get_Setpokemon("pikachu"))  
    team.add_pokemon(controller.get_Setpokemon("arceus"))  

    print(team)
    # while i <= MAX_NATURE:
    #     controller.afficher_nature(i)
    #     i += 1


