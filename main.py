from app.controllers.pokemon_controller import PokemonController
from app.services.constantes import MAX_NATURE

if __name__ == "__main__":
    controller = PokemonController()
    i = 1
    
    munja = controller.get_Setpokemon(292)  # Munja
    print(munja)

    munja.set_IV("attack", 10)
    munja.set_ability()
    munja.set_item("restes")
    print(munja.nature.id)

    # while i <= MAX_NATURE:
    #     controller.afficher_nature(i)
    #     i += 1


