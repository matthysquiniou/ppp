from enum import Enum

class State(Enum):
    ERROR = 0
    MENU = 1
    LVLMANAGER = 2
    LVLDEV = 3
    LVLOUV = 4
    FINISHED = 5
    QUIT = 6