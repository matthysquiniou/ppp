from enum import Enum
from Type import Type
from Rank import Rank

class TypeEnnemi(Enum):
    PHYSICAL_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
    }
    PHYSICAL_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
    }
    PHYSICAL_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
    }
    MANAGE_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
    }
    MANAGE_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
    }
    MANAGE_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
    }
    TECHNO_BASE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.BASE,
    }
    TECHNO_STRONG = {
        "type": Type.PHYSIQUE,
        "rank": Rank.STRONG,
    }
    TECHNO_ELITE = {
        "type": Type.PHYSIQUE,
        "rank": Rank.ELITE,
    }