from app.controllers.pokemon_controller import PokemonController
from app.services.constantes import MAX_NATURE

if __name__ == "__main__":
    controller = PokemonController()
    i = 1
    
    while i < MAX_NATURE + 1:
        controller.afficher_nature(i)
        i += 1

    # controller.afficher_move(i)

    # controller.afficher_talent(i)

    # controller.afficher_nature(i)

    # controller.afficher_item(1)

