from enum import Enum

class Type(Enum):
    PHYSIQUE = {
        "faiblesse" : "MANAGE",
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
        "vie" : 110,
        "vitesse" : 4,
        "asset" : "Character 2"
    }
    TECHNO = {
        "faiblesse" : "PHYSIQUE",
        "resistance" : "MANAGE",
        "defence" : 4,
        "attaque" : 8,
        "vie" : 90,
        "vitesse" : 4,
        "asset" : "Character 3"
    }