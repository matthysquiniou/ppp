from enum import Enum

class TypeEnnemi(Enum):
    GOBELIN = {
        "niveau": 1,
        "faiblesses": ["feu"],
        "resistances": ["terre"],
        "defence": 10,
        "attaque": 15,
        "vie": 30,
        "vitesse": 5,
        "asset_name": "goblin.png"
    }
    ORC = {
        "niveau": 3,
        "faiblesses": ["glace"],
        "resistances": ["feu"],
        "defence": 20,
        "attaque": 25,
        "vie": 50,
        "vitesse": 3,
        "asset_name": "orc.png"
    }
    DRAGON = {
        "niveau": 5,
        "faiblesses": ["eau"],
        "resistances": ["feu", "glace"],
        "defence": 50,
        "attaque": 40,
        "vie": 100,
        "vitesse": 7,
        "asset_name": "dragon.png"
    }
