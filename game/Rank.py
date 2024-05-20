from enum import Enum

class Rank(Enum):
    BASE = {
        "stat_mult" : 1,
        "score" : 10,
        "color" : ""
    }
    STRONG = {
        "stat_mult" : 1.5,
        "score" : 25,
        "color" : " 2"
    }
    ELITE = {
        "stat_mult" : 2,
        "score" : 40,
        "color" : " 3"
    }