import requests
from app.models.BasePokemon import BasePokemon

class PokeAPIService:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    @staticmethod
    def get_pokemon(name_or_id) -> BasePokemon:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Pokémon '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        talents = [a["ability"]["name"] for a in data["abilities"]]
        movepool = [m["move"]["name"] for m in data["moves"]]
        sprites = data["sprites"]["front_default"]

        return BasePokemon(name, id, types, stats, talents, movepool, sprites)
