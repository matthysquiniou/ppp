from enum import Enum
from PersonnageAction import PersonnageAction

class Action(Enum):
    PERSONNAGE = {
        PersonnageAction.WALK_FORWARD_RIGHT: 4,
        PersonnageAction.WALK_BACKWARD_LEFT: 4,
        PersonnageAction.TAKING_DAMAGE_FORWARD_RIGHT: 3,
        PersonnageAction.TAKING_DAMAGE_BACKWARD_LEFT: 3,
        PersonnageAction.POSING_FORWARD_RIGHT: 1,
        PersonnageAction.POSING_BACKWARD_LEFT: 1,
        PersonnageAction.ATTACKING_FORWARD_RIGHT: 5,
        PersonnageAction.ATTACKING_BACKWARD_LEFT: 5,
        PersonnageAction.DEAD_RIGHT: 1,
        PersonnageAction.WALK_FORWARD_LEFT: 4,
        PersonnageAction.WALK_BACKWARD_RIGHT: 4,
        PersonnageAction.TAKING_DAMAGE_FORWARD_LEFT: 3,
        PersonnageAction.TAKING_DAMAGE_BACKWARD_RIGHT: 3,
        PersonnageAction.POSING_FORWARD_LEFT: 1,
        PersonnageAction.POSING_BACKWARD_RIGHT: 1,
        PersonnageAction.ATTACKING_FORWARD_LEFT: 5,
        PersonnageAction.ATTACKING_BACKWARD_RIGHT: 5,
        PersonnageAction.DEAD_LEFT: 1,
    }