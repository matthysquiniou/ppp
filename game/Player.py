from Type import Type
from State import State
from Castle import Castle
from Ennemi import Ennemi
from EnnemiBoss import EnnemiBoss
from PlayerAttaque import PlayerAttaque
import math

class Player:

    def __init__(self,Wsize):
        self.social_points = 20
        self.physical_points = 20
        self.technologic_points = 20
        self.health_point = 1000
        self.max_health = 1000
        self.remain_points = 15
        self.level = 1
        self.castle = Castle.CASTLE_1.value
        self.x = Wsize[0]//2-95
        self.y = Wsize[1]//2-95
        self.list_of_lauched_attack = []
        self.ticks_since_last_attack = 0
        self.ticks_needed_for_attack = 60/self.castle["attack_speed"]
        self.exp = 0
    
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

    def add_exp(self,number:int):
        acc = number/self.level

        if acc +self.exp >= 100:
            self.exp = (acc+self.exp)-100

            if self.exp >= 100:
                if self.level == 99:
                    return
                self.exp = self.exp-100
                self.level_up()
            self.level_up()
        else:
            self.exp = self.exp + acc

    def take_damage(self,state: State, damage: int, enemi_type: Type):
        match state:
            case state.LVLMANAGER :
                if enemi_type == Type.TECHNO:
                    self.health_point = self.health_point - (damage*2)
                elif enemi_type == Type.PHYSIQUE:
                    self.health_point = self.health_point - (damage*0.5)
                else: 
                    self.health_point = self.health_point - damage
                    
            case state.LVLDEV :
                if enemi_type == Type.PHYSIQUE:
                    self.health_point = self.health_point - (damage*2)
                elif enemi_type == Type.MANAGE:
                    self.health_point = self.health_point - (damage*0.5)
                else: 
                    self.health_point = self.health_point - damage

            case state.LVLOUV :
                if enemi_type == Type.MANAGE:
                    self.health_point = self.health_point - (damage*2)
                elif enemi_type == Type.TECHNO:
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
        self.remain_points += 5*self.level

        self.health_point += self.max_health*20/100

        if self.health_point >= self.max_health:
            self.max_health += 50
            self.health_point = self.max_health
            

        if self.level >= self.castle["next_level_required"]:
            self.castle = self.castle["next_castle"].value
            self.ticks_needed_for_attack = 60/self.castle["attack_speed"]

    def attaque(self,game,display):
        nearest_ennemi = None
        distance_nearest = None
        if self.ticks_since_last_attack >= self.ticks_needed_for_attack:
            self.ticks_since_last_attack = 0
            for object in game.objects:
                if isinstance(object,Ennemi) or isinstance(object,EnnemiBoss):
                    if object.dead:
                        continue
                    new_distance = math.sqrt((object.x - (self.x+100))**2 + (object.y - (self.y+100))**2)
                    if nearest_ennemi == None:
                        nearest_ennemi = object 
                        distance_nearest = new_distance
                    elif new_distance < distance_nearest:
                        nearest_ennemi = object 
                        distance_nearest = new_distance
            if (nearest_ennemi != None):
                self.generate_attaque(nearest_ennemi,distance_nearest)
        else:
            self.ticks_since_last_attack = self.ticks_since_last_attack + 1
        self.draw_attaque(display,game)
    
    def generate_attaque(self,ennemi,distance):
        self.list_of_lauched_attack.append(PlayerAttaque(ennemi,self.x,self.y,distance,self.social_points,self.technologic_points,self.physical_points))

    def draw_attaque(self,display,game):
        for attaque in self.list_of_lauched_attack[:]:
            touched = attaque.draw(display,game)
            if touched:
                self.list_of_lauched_attack.remove(attaque)




