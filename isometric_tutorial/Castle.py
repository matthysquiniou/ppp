from enum import Enum

class Castle(Enum):
    CASTLE_1 = {
        "next_level_required" : 3,
        "asset" : "./images/small_wood_castle.png",
        "attack_speed" : 1/3,
        "next_castle" : None
    }
    CASTLE_2 = {
        "next_level_required" : 7,
        "asset" : "./images/wood_castle.png",
        "attack_speed" : 0.5,
        "next_castle" : None
    }
    CASTLE_3 = {
        "next_level_required" : 12,
        "asset" : "./images/castle.png",
        "attack_speed" : 0.7,
        "next_castle" : None
    }
    CASTLE_4 = {
        "next_level_required" : 999999999,
        "asset" : "./images/big_castle.png",
        "attack_speed" : 0.9,
        "next_castle" : None
    }

    @classmethod
    def set_next_castle(cls):
        cls.CASTLE_1.value["next_castle"] = cls.CASTLE_2
        cls.CASTLE_2.value["next_castle"] = cls.CASTLE_3
        cls.CASTLE_3.value["next_castle"] = cls.CASTLE_4

Castle.set_next_castle()