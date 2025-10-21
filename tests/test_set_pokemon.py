import pytest
from app.models.BasePokemon import BasePokemon
from app.models.SetPokemon import SetPokemon
from app.models.Natures import Natures
from app.models.Items import Items
from app.controllers.pokemon_controller import PokemonController
# Exemple d’un Pokémon basique pour les tests

controller = PokemonController()

@pytest.fixture
def base_munja():
    return controller.get_Basepokemon(292)

def test_base_pokemon_attributes(base_munja):
    assert base_munja.name == "shedinja"
    assert base_munja.id == 292
    assert "bug" in base_munja.types
    assert "ghost" in base_munja.types
    assert base_munja.weight == 12
    assert base_munja.height == 8
    assert base_munja.stats["hp"] == 1
    assert base_munja.stats["attack"] == 90
    assert base_munja.stats["defense"] == 45
    assert base_munja.stats["special-attack"] == 30
    assert base_munja.stats["special-defense"] == 30
    assert base_munja.stats["speed"] == 40
    assert "wonder-guard" in base_munja.abilities

@pytest.fixture
def set_munja(base_munja):
    return SetPokemon(base_munja)

def test_initialisation(set_munja):
    assert set_munja.base_pokemon.name == "shedinja"
    assert set_munja.level == 50
    assert set_munja.happiness == 255
    assert set_munja.current_hp == 1  # Shedinja HP fixe
    assert set_munja.ability == "wonder-guard"

def test_set_iv(set_munja):
    old_attack = set_munja.stats["attack"]
    assert set_munja.IV["attack"] == 31
    set_munja.set_IV(hp=0, atk=0, defense=31, spatk=0, spdef=0, spd=31)
    assert set_munja.IV["attack"] == 0
    assert set_munja.stats["attack"] < old_attack

def test_invalid_iv_value(set_munja):
    with pytest.raises(ValueError):
        set_munja.set_IV(hp=40)  # > 31 = erreur
    with pytest.raises(ValueError):
        set_munja.set_IV(atk=-5)  # < 0 = erreur
    

def test_set_moves_valid(set_munja):
    set_munja.set_moves(["griffe", "ténacité"])
    assert set_munja.moves == ["griffe", "ténacité"]

def test_set_moves_invalid(set_munja):
    with pytest.raises(ValueError):
        set_munja.set_moves(["ember"])  

def test_set_ability_valid(set_munja):
    set_munja.set_ability()
    assert set_munja.ability == "wonder-guard"

def test_set_invalid_ability(set_munja):
    with pytest.raises(ValueError):
        set_munja.set_ability("Levitation")

def test_set_nature_changes_stats(set_munja):
    old_attack = set_munja.stats["attack"]
    adamant = Natures("adamant")  
    set_munja.set_nature(adamant)
    assert set_munja.stats["attack"] != old_attack

def test_set_item(set_munja):
    item = Items()
    set_munja.set_item(item)
    assert set_munja.item == item
