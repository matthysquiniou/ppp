from enum import Enum

class Rank(Enum):
    BASE = {
        "stat_mult" : 1,
        "color" : ""
    }
    STRONG = {
        "stat_mult" : 1.5,
        "color" : "2"

    }
    ELITE = {
        "stat_mult" : 2,
        "color" : "3"
    }