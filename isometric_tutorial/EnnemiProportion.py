from enum import Enum
from Type import Type

class EnnemiProportion(Enum):
    LVLMANAGER = {
        Type.PHYSIQUE:0.85,
        Type.MANAGE:0.10,
        Type.TECHNO:0.05
    }