from enum import Enum

class State(Enum):
    ERROR = 0
    MENU = 1
    LVLMANAGER = 2
    LVLDEV = 3
    LVL3 = 4
    FINISHED = 5
    QUIT = 6