from enum import Enum
class Action(Enum):
    PERSONNAGE = {
        "walk_forward_right" : 4,
        "walk_backward_left" : 4,
        "taking_damage_forward_right" : 3,
        "taking_damage_backward_left" : 3,
        "posing_forward_right": 1,
        "posing_backward_left": 1,
        "attacking_forward_right": 5,
        "attacking_backward_left": 5,
        "dead_right" : 1,
        "walk_forward_left" : 4,
        "walk_backward_right" : 4,
        "taking_damage_forward_left" : 3,
        "taking_damage_backward_right" : 3,
        "posing_forward_left": 1,
        "posing_backward_right": 1,
        "attacking_forward_left": 5,
        "attacking_backward_right": 5,
        "dead_left" : 1,
    }
