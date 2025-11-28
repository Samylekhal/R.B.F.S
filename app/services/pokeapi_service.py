import json
import os
import requests

from app.models.BasePokemon import BasePokemon
from app.models.Moves import Moves
from app.models.Abilities import Abilities
from app.models.Natures import Natures
from app.models.Items import Items


class PokeAPIService:
    BASE_URL = "https://pokeapi.co/api/v2/"
    LOCAL_DATA_PATH = os.path.join("R.B.F.S", "app", "data", "api", "v2")

    @staticmethod
    def _load_local_data(category: str, name_or_id: str):
        """
        Essaie de charger un fichier JSON localement avant de faire un appel API.
        """
        file_path = os.path.join(PokeAPIService.LOCAL_DATA_PATH, category, f"{name_or_id.lower()}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    @staticmethod
    def _fetch_data(category: str, name_or_id: str):
        """
        Récupère les données : d'abord localement, sinon via l'API.
        """
        # Essai en local
        data = PokeAPIService._load_local_data(category, name_or_id)
        if data is not None:
            return data

        # Sinon, appel API
        url = f"{PokeAPIService.BASE_URL}{category}/{name_or_id.lower()}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"{category.capitalize()} '{name_or_id}' introuvable ({response.status_code})")

        return response.json()

    # --------------------------------------------------------------------------
    # Pokémon
    # --------------------------------------------------------------------------
    @staticmethod
    def get_pokemon(name_or_id) -> BasePokemon:
        data = PokeAPIService._fetch_data("pokemon", str(name_or_id))
        name = data["name"]
        id = data["id"]
        weight = data["weight"]
        height = data["height"]
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        movepool = [m["move"]["name"] for m in data["moves"]]

        return BasePokemon(name, id, types, weight, height, stats, abilities, movepool)

    # --------------------------------------------------------------------------
    # Capacités (Moves)
    # --------------------------------------------------------------------------
    @staticmethod
    def get_move(name_or_id) -> Moves:
        data = PokeAPIService._fetch_data("move", str(name_or_id))
        name = data["name"]
        id = data["id"]
        damageclass = data["damage_class"]["name"]
        type_ = data["type"]["name"]
        basepower = data.get("power")
        pp = data.get("pp")
        accuracy = data.get("accuracy")
        description = next((entry["flavor_text"] for entry in data["flavor_text_entries"] if entry["language"]["name"] == "en"), "")
        return Moves(name, id, damageclass, type_, basepower, pp, accuracy, description)

    # --------------------------------------------------------------------------
    # Talents (Abilities)
    # --------------------------------------------------------------------------
    @staticmethod
    def get_ability(name_or_id) -> Abilities:
        data = PokeAPIService._fetch_data("ability", str(name_or_id))
        name = data["name"]
        id = data["id"]
        description = next((entry["flavor_text"] for entry in data["flavor_text_entries"] if entry["language"]["name"] == "en"), "")
        return Abilities(name, id, description)

    # --------------------------------------------------------------------------
    # Natures
    # --------------------------------------------------------------------------
    @staticmethod
    def get_nature(name_or_id) -> Natures:
        data = PokeAPIService._fetch_data("nature", str(name_or_id))
        name = data["name"]
        nature = Natures(name)
        nature.id = data["id"]
        return nature

    # --------------------------------------------------------------------------
    # Objets (Items)
    # --------------------------------------------------------------------------
    @staticmethod
    def get_item(name_or_id) -> Items:
        data = PokeAPIService._fetch_data("item", str(name_or_id))
        name = data["name"]
        id = data["id"]
        description = next((entry["effect"] for entry in data["effect_entries"] if entry["language"]["name"] == "en"), "")
        item_category = data["category"]["name"]
        return Items(name, id, description, item_category)

    # --------------------------------------------------------------------------
    # Compteur de données (utile pour stats ou pagination)
    # --------------------------------------------------------------------------
    @staticmethod
    def get_count_data(category):
        local_dir = os.path.join(PokeAPIService.LOCAL_DATA_PATH, category)
        if os.path.exists(local_dir):
            return len([f for f in os.listdir(local_dir) if f.endswith(".json")])

        # Sinon fallback API
        url = f"{PokeAPIService.BASE_URL}{category}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"({response.status_code})")
        return response.json()["count"]
