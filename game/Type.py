from enum import Enum

class Type(Enum):
    PHYSIQUE = {
        "faiblesse" : None,
        "resistance" : None,
        "defence" : 7,
        "attaque" : 4,
        "vie" : 130,
        "vitesse" : 3,
        "asset" : "Character 1"
    }
    MANAGE = {
        "faiblesse" : None,
        "resistance" : None,
        "defence" : 5,
        "attaque" : 5,
        "vie" : 110,
        "vitesse" : 4,
        "asset" : "Character 2"
    }
    TECHNO = {
        "faiblesse" : None,
        "resistance" : None,
        "defence" : 4,
        "attaque" : 8,
        "vie" : 90,
        "vitesse" : 4,
        "asset" : "Character 3"
    }

    @classmethod
    def set_weakness_res(cls):
        cls.PHYSIQUE.value["faiblesse"] = cls.MANAGE
        cls.PHYSIQUE.value["resistance"] = cls.TECHNO
        cls.MANAGE.value["faiblesse"] = cls.TECHNO
        cls.MANAGE.value["resistance"] = cls.PHYSIQUE
        cls.TECHNO.value["faiblesse"] = cls.PHYSIQUE
        cls.TECHNO.value["resistance"] = cls.MANAGE

Type.set_weakness_res()