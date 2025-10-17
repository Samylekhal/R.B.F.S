import requests
from app.models.BasePokemon import BasePokemon
from app.models.Moves import Moves
from app.models.Abilities import Abilities
from app.models.Natures import Natures
from app.models.Items import Items

class PokeAPIService:
    BASE_URL = "https://pokeapi.co/api/v2/"

    @staticmethod
    def get_pokemon(name_or_id) -> BasePokemon:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{"pokemon/"}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Pokémon '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        weight = data["weight"]
        height = data["height"]
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        movepool = [m["move"]["name"] for m in data["moves"]]

        return BasePokemon(name, id, types, weight, height, stats, abilities, movepool)
    
    # get_moves  | Base power, PP, accurancy, description  
    
    @staticmethod
    def get_move(name_or_id) -> Moves:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{"move/"}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Capacité '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        damageclass = data["damage_class"]["name"]
        type = data["type"]["name"]
        Basepower = data["power"]
        PP = data["pp"]
        accuracy = data["accuracy"]
        description = data["flavor_text_entries"][0]["flavor_text"]

        return Moves(name,id,damageclass,type,Basepower,PP,accuracy,description)
    
    # get_abilities | Name, description
    @staticmethod
    def get_ability(name_or_id) -> Abilities:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{"ability/"}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Talent '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        description = data["flavor_text_entries"][1]["flavor_text"]

        return Abilities(name,id,description)
    
    # get_nature
    @staticmethod
    def get_nature(name_or_id) -> Natures:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{"nature/"}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Nature '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        INCstat = (data["increased_stat"]["name"] if data["increased_stat"] else "null")
        DECstat = (data["decreased_stat"]["name"] if data["decreased_stat"] else "null")


        return Natures(name,id,INCstat,DECstat)

    # get_item
    @staticmethod
    def get_item(name_or_id) -> Items:
        name_or_id = str(name_or_id)
        url = f"{PokeAPIService.BASE_URL}{"item/"}{name_or_id.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Item '{name_or_id}' introuvable ({response.status_code})")

        data = response.json()

        name = data["name"]
        id = data["id"]
        description = data["effect_entries"][0]["effect"]
        item_category = data["category"]["name"]

        return Items(name,id, description,item_category)
    
    @staticmethod
    def get_count_data(category):
        url = f"{PokeAPIService.BASE_URL}{category}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"({response.status_code})")

        data = response.json()
        return data["count"]
    

