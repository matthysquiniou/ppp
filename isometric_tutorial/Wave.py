
from WaveParameters import WaveParameters
from State import State
from EnnemiProportion import EnnemiProportion
from Ennemi import Ennemi
from Rank import Rank
import random

class Wave:

    def __init__(self,wave_parameter:WaveParameters):
        self.spawn_ticks = 0
        self.wave_parameter = wave_parameter
        self.max_spawn_ticks =  self.wave_parameter["number_of_ticks"]
        self.ennemi_number =  self.wave_parameter["ennemi_number"]
        self.base_number =  self.wave_parameter["base_number"]
        self.strong_number =  self.wave_parameter["strong_number"]
        self.elite_number =  self.wave_parameter["elite_number"]
        self.spawn_ticks_required = (self.max_spawn_ticks/self.wave_parameter["ennemi_number"])-1
        self.spawn_ticks_counter = 0


    def next_wave(self):
        self.wave_parameter = self.wave_parameter["next_wave"].value
        self.max_spawn_ticks = self.wave_parameter["number_of_ticks"]
        self.ennemi_number =  self.wave_parameter["ennemi_number"]
        self.base_number =  self.wave_parameter["base_number"]
        self.strong_number =  self.wave_parameter["strong_number"]
        self.elite_number =  self.wave_parameter["elite_number"]

    def spawn(self, game):
        self.spawn_ticks_counter = self.spawn_ticks_counter + 1
        if self.spawn_ticks_counter >= self.spawn_ticks_required and self.ennemi_number != 0:
            self.spawn_ticks_counter = 0
            state = game.state
            match state:
                case State.LVLMANAGER:#TODO : gerer les autres states
                    ennemi_proportion = EnnemiProportion.LVLMANAGER.value
                    type_ennemi = self.choisir_type_ennemi(ennemi_proportion)
                    rank_ennemi = self.choisir_rank_ennemi()
                    position_ennemi = self.choisir_position_ennemi()
                    game.objects.append(Ennemi(position_ennemi[0],position_ennemi[1],type_ennemi,rank_ennemi))
        
    def choisir_type_ennemi(self,proportion):
        types = list(proportion.keys())
        probabilites = list(proportion.values())
        choix = random.choices(types, weights=probabilites, k=1)[0]
        return choix

    def choisir_rank_ennemi(self):
        ranks = []
        if self.base_number > 0:
            ranks.extend([Rank.BASE] * self.base_number)
        if self.strong_number > 0:
            ranks.extend([Rank.STRONG] * self.strong_number)
        if self.elite_number > 0:
            ranks.extend([Rank.ELITE] * self.elite_number)
        choix = random.choice(ranks)
        if choix == Rank.BASE:
            self.base_number -= 1
        elif choix == Rank.STRONG:
            self.strong_number -= 1
        elif choix == Rank.ELITE:
            self.elite_number -= 1
        self.ennemi_number -= 1

        return choix
    
    def choisir_position_ennemi(self):#TODO
        return [150,150]

