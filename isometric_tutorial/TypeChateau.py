from enum import Enum

class TypeChateau(Enum):
    FORTERESSE = {
        "niveau": 1,
        "technologie": ["catapulte", "muraille"],
        "asset_name": "forteresse.png"
    }
    CITADELLE = {
        "niveau": 3,
        "technologie": ["tourelle", "pont-levis"],
        "asset_name": "citadelle.png"
    }
    CHATEAU_FORT = {
        "niveau": 5,
        "technologie": ["canon", "fossé"],
        "asset_name": "chateau_fort.png"
    }