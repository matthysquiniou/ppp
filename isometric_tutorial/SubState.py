from enum import Enum

class SubState(Enum):
    WAITING_WAVE = 0
    WAVE_SPAWN = 1
    WAVE = 2
    SKILL_TREE = 3
    LOSE = 4
    WIN = 5