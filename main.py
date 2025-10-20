from app.controllers.pokemon_controller import PokemonController
from app.services.constantes import MAX_NATURE

if __name__ == "__main__":
    controller = PokemonController()
    i = 1
    
    munja = controller.get_Setpokemon(292)  # Munja
    munja.set_IV()
    munja.set_item()
    print(munja)
    # while i <= MAX_NATURE:
    #     controller.afficher_nature(i)
    #     i += 1


