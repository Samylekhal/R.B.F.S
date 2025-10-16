"""Contient plusieurs valeurs fixes 
servant pour différentes fonctions"""
from app.controllers.pokemon_controller import PokemonController


MAX_POKE = PokemonController().get_nb_data("pokemon")
MAX_MOVE = PokemonController().get_nb_data("move")
MAX_TALENT = PokemonController().get_nb_data("ability")
MAX_NATURE = PokemonController().get_nb_data("nature")
MAX_ITEM = PokemonController().get_nb_data("item")