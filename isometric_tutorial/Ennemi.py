from Objet import Objet
from Type import Type
from Rank import Rank
from Action import Action
from PersonnageAction import PersonnageAction
import math

class Ennemi(Objet):


    def __init__(self, x:int, y:int, type: Type, rank: Rank):
        super().__init__(x, y, "ennemi/"+type.value["asset"]+rank.value["color"]+".png", 9, 5, Action.PERSONNAGE.value)
        self.faiblesse = type.value["faiblesse"]
        self.resistance = type.value["resistance"]
        self.defence = type.value["defence"] * rank.value["stat_mult"]
        self.attaque = type.value["attaque"]  * rank.value["stat_mult"]
        self.vie = type.value["vie"]  * rank.value["stat_mult"]
        self.vitesse = type.value["vitesse"]
        self.current_sprite_index = 0
        self.frame_since_last_sprite_update = 0
        self.action = None
        self.type = type
        self.nb_attacks = 0
        self.direction = self.calculer_coefficients_direction(x,y)
        
    def draw(self, screen): 
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
        else:    
            self.frame_since_last_sprite_update = self.frame_since_last_sprite_update + 1
        if self.action in [PersonnageAction.WALK_BACKWARD_LEFT,PersonnageAction.WALK_BACKWARD_RIGHT,PersonnageAction.WALK_FORWARD_LEFT,PersonnageAction.WALK_FORWARD_RIGHT]: 
            self.updatePosition() 
        screen.blit(animation[self.current_sprite_index], (self.x,self.y))

    # TODO : Gerer le choix d'action correctement (dead et prendre dmg)
    def chooseAction(self): 
        x2 = 480
        y2 = 270
        distance = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)

        actions = {
            (True,  True,  True):  PersonnageAction.ATTACKING_FORWARD_LEFT,
            (True,  False, True):  PersonnageAction.ATTACKING_BACKWARD_LEFT,
            (False, True,  True):  PersonnageAction.ATTACKING_FORWARD_RIGHT,
            (False, False, True):  PersonnageAction.ATTACKING_BACKWARD_RIGHT,
            (True,  True,  False): PersonnageAction.WALK_FORWARD_LEFT,
            (True,  False, False): PersonnageAction.WALK_BACKWARD_LEFT,
            (False, True,  False): PersonnageAction.WALK_FORWARD_RIGHT,
            (False, False, False): PersonnageAction.WALK_BACKWARD_RIGHT,
        }

        direction_x = self.direction[0] <= 0
        direction_y = self.direction[1] > 0
        is_near = distance < 100

        self.action = actions[(direction_x, direction_y, is_near)]
    
    def updatePosition(self):
        self.x = self.x + self.direction[0]*self.vitesse*0.1
        self.y = self.y + self.direction[1]*self.vitesse*0.1
    
    def calculer_coefficients_direction(self, x1, y1):
        x2 = 480
        y2 = 270
        dx = x2 - x1
        dy = y2 - y1
        norm = abs(dx) + abs(dy)
        coeffX = dx / norm
        coeffY = dy / norm
        return [coeffX, coeffY]