
from WaveParameters import WaveParameters
from State import State
from EnnemiProportion import EnnemiProportion
from Ennemi import Ennemi
from Rank import Rank
from Type import Type
from EnnemiBoss import EnnemiBoss
import random
import math

class Wave:

    def __init__(self,wave_parameter:WaveParameters):
        self.spawn_ticks = 0
        self.wave_parameter = wave_parameter
        self.max_spawn_ticks =  self.wave_parameter["number_of_ticks"]
        self.ennemi_number =  self.wave_parameter["ennemi_number"]
        self.base_number =  self.wave_parameter["base_number"]
        self.strong_number =  self.wave_parameter["strong_number"]
        self.elite_number =  self.wave_parameter["elite_number"]
        self.radius_spawn = self.wave_parameter["radius_spawn"]
        self.spawn_ticks_required = (self.max_spawn_ticks/self.wave_parameter["ennemi_number"])-1
        self.remaining_ennemi = self.ennemi_number
        self.spawn_ticks_counter = 0
        self.ennemi_proportion = None
        self.ticks = 0

    def add_score(self,game):
        game.score = game.score + 180 - self.ticks/60
        self.ticks = 0

    def boss_spawn(self,game):
        rank = Rank.ELITE
        type = None
        state = game.state
        match state:
            case State.LVLMANAGER:
                type = Type.PHYSIQUE
            case State.LVLDEV:
                type = Type.MANAGE
            case State.LVLOUV:
                type = Type.TECHNO
        position_ennemi = self.choisir_position_ennemi()
        self.ennemi_number -= 1
        game.objects.append(EnnemiBoss(position_ennemi[0],position_ennemi[1],type,rank))

    def next_wave(self):
        self.wave_parameter = self.wave_parameter["next_wave"].value
        self.max_spawn_ticks = self.wave_parameter["number_of_ticks"]
        self.ennemi_number =  self.wave_parameter["ennemi_number"]
        self.base_number =  self.wave_parameter["base_number"]
        self.strong_number =  self.wave_parameter["strong_number"]
        self.elite_number =  self.wave_parameter["elite_number"]
        self.spawn_ticks_required = (self.max_spawn_ticks/self.wave_parameter["ennemi_number"])-1
        self.remaining_ennemi = self.ennemi_number

    def spawn(self, game):
        self.spawn_ticks_counter = self.spawn_ticks_counter + 1
        if self.spawn_ticks_counter >= self.spawn_ticks_required and self.ennemi_number != 0:
            self.spawn_ticks_counter = 0
            state = game.state
            match state:
                case State.LVLMANAGER:
                    self.ennemi_proportion = EnnemiProportion.LVLMANAGER.value
                case State.LVLDEV:
                    self.ennemi_proportion = EnnemiProportion.LVLDEV.value
                case State.LVLOUV:
                    self.ennemi_proportion = EnnemiProportion.LVLOUV.value
            type_ennemi = self.choisir_type_ennemi(self.ennemi_proportion)
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
    
    def choisir_position_ennemi(self,center=(480,270)):
        radius = random.randint(self.radius_spawn[0],self.radius_spawn[1])
        ligne_depart = random.randint(0,3)
        pos_depart = [150,150]
        if ligne_depart == 0:
            i = random.randint(3,5)
            pos =  math.pi/ i
            pos_depart = [int(math.cos(pos)*radius),int(math.sin(pos)*radius)]
        elif ligne_depart == 1:
            i = random.randint(3,5)
            pos =  math.pi/ i
            pos_depart = [int(math.cos(-pos)*radius),int(math.sin(-pos)*radius)]
        elif ligne_depart == 2:
            i = random.randint(4,5)
            pos =  (i-1)*math.pi/ i
            pos_depart = [int(math.cos(-pos)*radius),int(math.sin(-pos)*radius)]
        else:
            i = random.randint(4,5)
            pos =  (i-1)*math.pi/ i
            pos_depart = [int(math.cos(pos)*radius),int(math.sin(pos)*radius)]
        
        pos_depart = [center[0]+pos_depart[0],center[1]+pos_depart[1]]



        return pos_depart

