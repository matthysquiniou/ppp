from enum import Enum

class State(Enum):
    ERROR = 0
    MENU = 1
    LVL1 = 2
    LVL2 = 3
    LVL3 = 4
    FINISHED = 5
    QUIT = 6


class Game : 
    
    def __init__(self) -> None:
        self.state = State.MENU

   