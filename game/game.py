import time
import pygame
import sys

from Map import Map
from Ennemi import Ennemi
from Type import Type
from Rank import Rank
from SkillTree import Tree
from Player import Player
from State import State
from SubState import SubState
from Wave import Wave
from WaveParameters import WaveParameters



menu_texts = ["Become manager","Become dev","Quit"]


class Game : 
    
    def __init__(self,size=(1920,1080)) -> None:
        self.MANAGER_BUTTON_POS = (size[0]//2-size[0]//10,size[1]//2)
        self.DEV_BUTTON_POS = (size[0]//2-size[0]//10,size[1]//2+50)
        self.QUIT_BUTTON_POS = (size[0]//2-size[0]//10,size[1]-150)
        self.LOGO_POS = (size[0]//2-size[0]//5,100)
        self.LOGO_SIZE = (size[0]//2,size[1]//4)

        self.Wsize = size
        self.player = Player(self.Wsize)

        self.tree = Tree(self.player,self.Wsize)

        self.button_pos = [self.MANAGER_BUTTON_POS,self.DEV_BUTTON_POS,self.QUIT_BUTTON_POS,]
        self.state = State.MENU
        self.wave = Wave(WaveParameters.WAVE_1.value)
        self.lvl = 0
        self.objects = []
        self.sub_state = SubState.WAITING_WAVE
        self.sub_state_save = SubState.WAITING_WAVE

        self.map = Map("./config/map.txt",size)

    def reset(self):
        self.player = Player(self.Wsize)

        self.tree = Tree(self.player,self.Wsize)
        self.state = State.MENU
        self.wave = Wave(WaveParameters.WAVE_1.value)
        self.lvl = 0
        self.objects = []
        self.sub_state = SubState.WAITING_WAVE
        self.sub_state_save = SubState.WAITING_WAVE

    def waiting_wave(self,display,mouse):
        self.put_basic_elemnts(display,mouse)

        if 0 <= mouse[0] <= 150 and 50 <= mouse[1] <= 100:
            pygame.draw.rect(display,(255,255,255),[0,50,150,50]) 
        next_wave_image = pygame.image.load('./images/next_wave.png').convert_alpha()
        next_wave_image = pygame.transform.scale(next_wave_image,(150,50))
        display.blit(next_wave_image,(0,50))

    def menu(self,mouse,display):
        logo = pygame.image.load('./images/logo.png').convert()
        logo = pygame.transform.scale(logo,self.LOGO_SIZE)
        display.blit(logo,self.LOGO_POS)

        smallfont = pygame.font.SysFont('Corbel',35) 
                
        for x,pos in enumerate(self.button_pos) :
            if pos[0] <= mouse[0] <= pos[0]+140 and pos[1] <= mouse[1] <= pos[1]+40: 
                pygame.draw.rect(display,(150,150,150),[pos[0],pos[1],30,40]) 
            text = smallfont.render('>  '+ menu_texts[x], True , (255,255,255)) 
            display.blit(text,(pos[0],pos[1]))
        pass

    def wave_commun(self,mouse,display):
        self.put_basic_elemnts(display,mouse)
        self.player.attaque(self,display)
        wavefont = pygame.font.SysFont('Corbel',20,True) 
        text = wavefont.render('Wave '+str(self.wave.wave_parameter["wave_number"]), True , (0,0,0)) 
        display.blit(text,(15,65))
        for object in self.objects:
            if isinstance(object, Ennemi):
                nb_attacks = object.nb_attacks
                object.draw(display)
                if nb_attacks < object.nb_attacks:
                    self.player.take_damage(self.state,object.attaque,object.type)
                if object.number_ticks_since_dead > 180:
                    self.objects.remove(object)
            else:
                object.draw(display)
        if self.player.health_point <= 0:
            self.sub_state = SubState.LOSE

    def wave_spawn(self):
        self.wave.spawn(self)
        if self.wave.spawn_ticks > self.wave.max_spawn_ticks:
            self.sub_state = SubState.WAVE
            self.wave.spawn_ticks = 0
        self.wave.spawn_ticks = self.wave.spawn_ticks + 1
    
    def wave_en_cours(self):
        have_ennemi = False
        for object in self.objects:
            if isinstance(object, Ennemi):
                have_ennemi = True
        if not have_ennemi:
            if self.wave.wave_parameter["next_wave"] == None:
                self.sub_state = SubState.WIN
            else:
                self.sub_state = SubState.WAITING_WAVE
                self.wave.next_wave()

    def level(self,display,mouse):
        match self.sub_state:

            case SubState.WAITING_WAVE:
                self.waiting_wave(display,mouse)

            case SubState.WAVE_SPAWN:
                self.wave_commun(mouse,display)       
                self.wave_spawn()                 

            case SubState.WAVE:
                self.wave_commun(mouse,display)
                self.wave_en_cours()
                            
            case SubState.SKILL_TREE:
                self.tree.draw(display)

            case SubState.WIN:
                self.afficher_ecran_fin("Bien joué, vous avez gagné",display,0,mouse)# remplacer 0 par un score

            case SubState.LOSE:
                self.afficher_ecran_fin("Dommage, vous avez perdu",display,0,mouse)# remplacer 0 par un score

    def draw(self,display):
        mouse = pygame.mouse.get_pos() 

        match self.state:

            case State.MENU:
                self.menu(mouse,display)

            case State.LVLMANAGER:
                self.level(display,mouse)

            case State.LVLDEV:
                self.level(display,mouse)

            case State.QUIT:
                pygame.quit()
                sys.exit()

    def afficher_ecran_fin(self, text, display, score,mouse):
        finfont = pygame.font.SysFont('Corbel',20,True) 
        text1 = finfont.render(text, True , (255,255,255)) 
        display.blit(text1,((display.get_width()//2)-100,(display.get_height()//2)-50))
        text2 = finfont.render("Score : "+str(score), True , (255,255,255)) 
        display.blit(text2,((display.get_width()//2)-25,(display.get_height()//2)))
        text3 = finfont.render("Retour au menu", True , (255,255,255)) 
        display.blit(text3,((0,0)))
        if 0 <= mouse[0] <= 140 and 0 <= mouse[1] <= 20:
            pygame.draw.rect(display,(150,150,150),[0,0,140,20]) 

    def check_where_click(self,mouse_x,mouse_y):
        match self.state:
            case State.MENU:
                for x,pos in enumerate(self.button_pos):
                    if pos[0] <= mouse_x <= pos[0]+140 and pos[1] <= mouse_y <= pos[1]+40: 
                        match x:
                            case 0:
                                self.state = State.LVLMANAGER
                            case 1:
                                self.state = State.LVLDEV
                            case 2:
                                self.state = State.QUIT
            case State.LVLMANAGER:
                if self.sub_state == SubState.SKILL_TREE:
                    self.tree.check_click(mouse_x,mouse_y)
                if 0 <= mouse_x <= 50 and 0 <= mouse_y <= 50:
                    if self.sub_state in [SubState.WAITING_WAVE,SubState.WAVE_SPAWN,SubState.WAVE]:
                        self.sub_state_save = self.sub_state
                        self.sub_state = SubState.SKILL_TREE
                    elif self.sub_state == SubState.SKILL_TREE:
                         self.sub_state = self.sub_state_save
                    pass
                if 0 <= mouse_x <= 150 and 50 <= mouse_y <= 100:
                    if self.sub_state == SubState.WAITING_WAVE:
                        self.sub_state = SubState.WAVE_SPAWN
                if 0 <= mouse_x <= 140 and 0 <= mouse_y <= 20:
                    if self.sub_state in [SubState.WIN,SubState.LOSE]:
                        self.reset()
            case State.LVLDEV:
                if 0 <= mouse_x <= 50 and 0 <= mouse_y <= 50:
                    if self.sub_state in [SubState.WAITING_WAVE,SubState.WAVE_SPAWN,SubState.WAVE]:
                        self.sub_state_save = self.sub_state
                        self.sub_state = SubState.SKILL_TREE
                    elif self.sub_state == SubState.SKILL_TREE:
                         self.sub_state = self.sub_state_save
                    pass

    def put_basic_elemnts(self,display : pygame.display,mouse):
        
        self.map.draw(display)
        if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
            pygame.draw.rect(display,(255,255,255),[0,0,50,50]) 
        
        
        logo = pygame.image.load('./images/idea.png').convert_alpha()
        logo = pygame.transform.scale(logo,(50,50))
        display.blit(logo,(0,0))

        health_bar_px = self.player.health_point*(152/self.player.max_health)
        pygame.draw.rect(display,(255,41,41),[(display.get_width()/2)-63,18,health_bar_px,21])
        exp_bar_px = self.player.exp*(152/100)
        pygame.draw.rect(display,(41,41,255),[(display.get_width()/2)-63,18,exp_bar_px,5])  #152px full health
        health_bar = pygame.image.load('./images/health_bar.png').convert_alpha()
        health_bar = pygame.transform.scale(health_bar,(200,50))
        display.blit(health_bar,((display.get_width()/2)-100,0))

        castle_img = pygame.image.load(self.player.castle["asset"]).convert_alpha()
        castle_img.set_colorkey((0, 0, 0))
        castle_img = pygame.transform.scale(castle_img,(200,200))
        display.blit(castle_img,(self.Wsize[0]//2-95,self.Wsize[1]//2-95))

        levelfont = pygame.font.SysFont('Corbel',20,True) 
        text = levelfont.render('Niveau '+str(self.player.level), True , (0,0,0)) 
        display.blit(text,((display.get_width()/2)-180,18))

        wavefont = pygame.font.SysFont('Corbel',20,True) 
        if self.sub_state == SubState.WAITING_WAVE:
            text = wavefont.render('Ennemis prochaine wave :'+str(self.wave.ennemi_number), True , (0,0,0)) 
            display.blit(text,(15,115))
        else:
            text = wavefont.render('Ennemis restant :'+str(self.wave.remaining_ennemi), True , (0,0,0)) 
            display.blit(text,(15,115))

   