from enum import Enum

class PersonnageAction(Enum):
    WALK_FORWARD_RIGHT = 1
    WALK_BACKWARD_LEFT = 2
    TAKING_DAMAGE_FORWARD_RIGHT = 3
    TAKING_DAMAGE_BACKWARD_LEFT = 4
    POSING_FORWARD_RIGHT = 5
    POSING_BACKWARD_LEFT = 6
    ATTACKING_FORWARD_RIGHT = 7
    ATTACKING_BACKWARD_LEFT = 8
    DEAD_RIGHT = 9
    WALK_FORWARD_LEFT = 10
    WALK_BACKWARD_RIGHT = 11
    TAKING_DAMAGE_FORWARD_LEFT = 12
    TAKING_DAMAGE_BACKWARD_RIGHT = 13
    POSING_FORWARD_LEFT = 14
    POSING_BACKWARD_RIGHT = 15
    ATTACKING_FORWARD_LEFT = 16
    ATTACKING_BACKWARD_RIGHT = 17
    DEAD_LEFT = 18