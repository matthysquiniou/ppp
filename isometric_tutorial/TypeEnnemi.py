from enum import Enum
from Type import Type
from Rank import Rank
class TypeEnnemi(Enum):
    PHYSICAL_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
        "asset_name": "ennemi/Character 1.png"
    }
    PHYSICAL_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
        "asset_name": "ennemi/Character 1 color 3.png"
    }
    PHYSICAL_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
        "asset_name": "ennemi/Character 1 color 2.png"
    }
    MANAGE_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
        "asset_name": "ennemi/Character 2.png"
    }
    MANAGE_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
        "asset_name": "ennemi/Character 2 color 3.png"
    }
    MANAGE_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
        "asset_name": "ennemi/Character 2 color 2.png"
    }
    TECHNO_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
        "asset_name": "ennemi/Character 3.png"
    }
    TECHNO_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
        "asset_name": "ennemi/Character 3 color 3.png"
    }
    TECHNO_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
        "asset_name": "ennemi/Character 3 color 2.png"
    }