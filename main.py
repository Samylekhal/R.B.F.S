from app.controllers.pokemon_controller import PokemonController


if __name__ == "__main__":
    controller = PokemonController()
    i = 1
    while i < 152:
        controller.afficher_pokemon(i)
        if i != 151:
            print("------------------------------------")
        i += 1