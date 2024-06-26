from Objet import Objet
from Type import Type
from Rank import Rank
from Action import Action
from PersonnageAction import PersonnageAction
import math
import pygame

class EnnemiBoss(Objet):


    def __init__(self, x:int, y:int, type: Type, rank: Rank):
        super().__init__(x, y, "ennemi/"+type.value["asset"]+rank.value["color"]+".png", 9, 5, Action.PERSONNAGE.value)
        self.faiblesse = type.value["faiblesse"]
        self.resistance = type.value["resistance"]
        self.defence = type.value["defence"] * rank.value["stat_mult"] * 10
        self.attaque = type.value["attaque"]  * rank.value["stat_mult"] * 10
        self.vie = type.value["vie"]  * rank.value["stat_mult"] * 100
        self.max_vie = type.value["vie"]  * rank.value["stat_mult"] * 10
        self.vitesse = type.value["vitesse"] * 0.5
        self.current_sprite_index = 0
        self.frame_since_last_sprite_update = 0
        self.action = None
        self.type = type
        self.rank = rank.value
        self.nb_attacks = 0
        self.direction = self.calculer_coefficients_direction(x,y)
        self.animation_damage = False
        self.dead = False
        self.number_ticks_since_dead = 0
        
    def draw(self, screen): 
        if self.dead:
            self.number_ticks_since_dead = self.number_ticks_since_dead + 1
        oldAction = self.action
        self.chooseAction()
        animation = self.animations[self.action]
        if oldAction != self.action:
            self.current_sprite_index = 0
            self.frame_since_last_sprite_update = 21
        if self.frame_since_last_sprite_update > 20:
            self.frame_since_last_sprite_update = 0
            index_before = self.current_sprite_index
            self.current_sprite_index = (self.current_sprite_index + 1) % len(animation)
            if index_before > self.current_sprite_index and self.action in [PersonnageAction.ATTACKING_FORWARD_LEFT,PersonnageAction.ATTACKING_BACKWARD_LEFT,PersonnageAction.ATTACKING_FORWARD_RIGHT,PersonnageAction.ATTACKING_BACKWARD_RIGHT]:
                self.nb_attacks = self.nb_attacks + 1
            if index_before > self.current_sprite_index and self.action in [PersonnageAction.TAKING_DAMAGE_FORWARD_LEFT,PersonnageAction.TAKING_DAMAGE_BACKWARD_RIGHT,PersonnageAction.TAKING_DAMAGE_BACKWARD_LEFT,PersonnageAction.TAKING_DAMAGE_FORWARD_RIGHT]:
                self.animation_damage = False
        else:    
            self.frame_since_last_sprite_update = self.frame_since_last_sprite_update + 1
        if self.action in [PersonnageAction.WALK_BACKWARD_LEFT,PersonnageAction.WALK_BACKWARD_RIGHT,PersonnageAction.WALK_FORWARD_LEFT,PersonnageAction.WALK_FORWARD_RIGHT,PersonnageAction.TAKING_DAMAGE_FORWARD_LEFT,PersonnageAction.TAKING_DAMAGE_BACKWARD_RIGHT,PersonnageAction.TAKING_DAMAGE_BACKWARD_LEFT,PersonnageAction.TAKING_DAMAGE_FORWARD_RIGHT]: 
            self.updatePosition() 
        current_sprite = animation[self.current_sprite_index]
        sprite_width, sprite_height = current_sprite.get_width(), current_sprite.get_height()
        resized_sprite = pygame.transform.scale(current_sprite, (sprite_width * 4, sprite_height * 4))
        screen.blit(resized_sprite, (self.x,self.y))
        self.drawHealthbar(screen)
    
    def drawHealthbar(self,screen):
        pygame.draw.rect(screen,(0,0,0),[self.x-52,self.y,233,12])
        pygame.draw.rect(screen,(255,255,255),[self.x-50,self.y+2,229,8])
        pygame.draw.rect(screen,(255,41,41),[self.x-50,self.y+2,self.vie*(23/self.max_vie),8]) 

    def chooseAction(self):
        x2 = 480
        y2 = 270
        distance = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)

        actions = {
            (True, lambda x: True, lambda x: True, True, lambda x: True): PersonnageAction.DEAD_LEFT,
            (False, lambda x: True, lambda x: True, True, lambda x: True): PersonnageAction.DEAD_RIGHT,
            (True, True, lambda x: True, False, True): PersonnageAction.TAKING_DAMAGE_FORWARD_LEFT,
            (False, False, lambda x: True, False, True): PersonnageAction.TAKING_DAMAGE_BACKWARD_RIGHT,
            (True, False, lambda x: True, False, True): PersonnageAction.TAKING_DAMAGE_BACKWARD_LEFT,
            (False, True, lambda x: True, False, True): PersonnageAction.TAKING_DAMAGE_FORWARD_RIGHT,
            (True, True, True, False, False): PersonnageAction.ATTACKING_FORWARD_LEFT,
            (True, False, True, False, False): PersonnageAction.ATTACKING_BACKWARD_LEFT,
            (False, True, True, False, False): PersonnageAction.ATTACKING_FORWARD_RIGHT,
            (False, False, True, False, False): PersonnageAction.ATTACKING_BACKWARD_RIGHT,
            (True, True, False, False, False): PersonnageAction.WALK_FORWARD_LEFT,
            (True, False, False, False, False): PersonnageAction.WALK_BACKWARD_LEFT,
            (False, True, False, False, False): PersonnageAction.WALK_FORWARD_RIGHT,
            (False, False, False, False, False): PersonnageAction.WALK_BACKWARD_RIGHT,
        }

        direction_x = self.direction[0] <= 0
        direction_y = self.direction[1] > 0
        is_near = distance < 100

        for (left, forward, near, dead, damage), action in actions.items():
            if (
                left == direction_x and
                (callable(forward) and forward(direction_y) or forward == direction_y) and
                (callable(near) and near(is_near) or near == is_near) and
                dead == self.dead and
                (callable(damage) and damage(self.animation_damage) or damage == self.animation_damage)
            ):
                self.action = action
                return
    
    def updatePosition(self):
        self.x = self.x + self.direction[0]*self.vitesse*0.15
        self.y = self.y + self.direction[1]*self.vitesse*0.15
    
    def calculer_coefficients_direction(self, x1, y1):
        x2 = 480
        y2 = 270
        dx = x2 - x1
        dy = y2 - y1
        norm = abs(dx) + abs(dy)
        coeffX = dx / norm
        coeffY = dy / norm
        return [coeffX, coeffY]
    
    def takeDamage(self,damage,type,game):
        if self.faiblesse == type:
            self.vie = self.vie - max(0,((damage * 2) - self.defence))
        elif self.resistance == type:
            self.vie = self.vie - max(0,((damage * 0.5) - self.defence))
        else:
            self.vie = self.vie - max(0,((damage) - self.defence))
        self.animation_damage = True
        if self.vie <= 0 and not self.dead:
            self.dead = True
            game.wave.remaining_ennemi = game.wave.remaining_ennemi - 1
            game.score = game.score + 1000