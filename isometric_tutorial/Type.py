from enum import Enum

class Type(Enum):
    PHYSIQUE = {
        "faiblesse" : "PHYSIQUE",
        "resistance" : "TECHNO",
        "defence" : 7,
        "attaque" : 4,
        "vie" : 130,
        "vitesse" : 3,
        "asset" : "Character 1"
    }
    MANAGE = {
        "faiblesse" : "TECHNO",
        "resistance" : "PHYSIQUE",
        "defence" : 5,
        "attaque" : 5,
        "vie" : 100,
        "vitesse" : 5,
        "asset" : "Character 2"
    }
    TECHNO = {
        "faiblesse" : "PHYSIQUE",
        "resistance" : "MANAGE",
        "defence" : 4,
        "attaque" : 8,
        "vie" : 80,
        "vitesse" : 6,
        "asset" : "Character 3"
    }