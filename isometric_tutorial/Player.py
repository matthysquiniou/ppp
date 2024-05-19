from Type import Type
from State import State
from SkillTree import Tree
from Castle import Castle
class Player:

    def __init__(self):
        self.social_points = 0
        self.physical_points = 0
        self.technologic_points = 0
        self.health_point = 1000
        self.max_health = 1000
        self.remain_points = 3
        self.level = 1
        self.castle = Castle.CASTLE_1.value
    
    def add_point(self,type:Type,number:int):
        if type == Type.PHYSIQUE:
            self.physical_points += number
            self.remain_points -= number
        elif type == Type.TECHNO:
            self.technologic_points += number
            self.remain_points -= number
        elif type == Type.MANAGE:
            self.social_points += number
            self.remain_points -= number

    def take_damage(self,state: State, damage: int, enemi_type: Type):
        match state: #TODO: gérer les autres level
            case state.LVLMANAGER :
                if enemi_type == Type.TECHNO:
                    self.health_point = self.health_point - (damage*2)
                elif enemi_type == Type.PHYSIQUE:
                    self.health_point = self.health_point - (damage*0.5)
                else: 
                    self.health_point = self.health_point - damage

    def delete_point(self,type:Type,number:int):
        if type == Type.PHYSIQUE:
            self.physical_points -= number
            self.remain_points += number
        elif type == Type.TECHNO:
            self.technologic_points -= number
            self.remain_points += number
        elif type == Type.MANAGE:
            self.social_points -= number
            self.remain_points += number

    def level_up(self):
        self.level = self.level + 1
        if self.level >= self.castle["next_level_required"]:
            self.castle = self.castle["next_castle"].value