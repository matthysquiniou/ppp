from Objet import Objet
from Type import Type
from Rank import Rank
from Action import Action
from PersonnageAction import PersonnageAction

class Ennemi(Objet):
    def __init__(self, x:int, y:int, type: Type, rank: Rank):
        super().__init__(x, y, "ennemi/"+type.asset+" "+rank.color+".png", 9, 5, Action.PERSONNAGE)
        self.faiblesse = type.faiblesse
        self.resistance = type.resistance
        self.defence = type.defence * rank.stat_mult
        self.attaque = type.attaque * rank.stat_mult
        self.vie = type.vie * rank.stat_mult
        self.vitesse = type.vitesse * rank.stat_mult
        self.current_sprite_index = 0
        self.frame_since_last_sprite_update = 0
        self.action = None

    def draw(self, screen): 
        oldAction = self.action
        self.action = self.chooseAction()
        animation = self.animations[self.action]
        if oldAction != self.action:
            self.current_sprite_index = 0
            self.frame_since_last_sprite_update = 6
        if self.frame_since_last_sprite_update > 5:
            self.frame_since_last_sprite_update = 0
            self.current_sprite_index = (self.current_sprite_index + 1) % len(animation)
        else:    
            self.frame_since_last_sprite_update = self.frame_since_last_sprite_update + 1

        self.updatePosition() 
        screen.blit(animation[self.current_sprite_index], (self.x,self.y))
    
    def chooseAction(self): # TODO : Gerer le choix d'action correctement 
        return PersonnageAction.WALK_FORWARD_RIGHT
    
    def updatePosition(self): # TODO : Gerer le déplacement correctement 
        self.x = self.x + 1
        self.x = self.y + 1
        return