from enum import Enum
import pygame
import sys
from Map import Map
from Ennemi import Ennemi
from Type import Type
from Rank import Rank
import time

MANAGER_BUTTON_POS = (850,400)
DEV_BUTTON_POS = (850,450)
QUIT_BUTTON_POS = (850,750)

button_pos = [MANAGER_BUTTON_POS,DEV_BUTTON_POS,QUIT_BUTTON_POS]
menu_texts = ["become manager","become dev","quit"]

class State(Enum):
    ERROR = 0
    MENU = 1
    LVLMANAGER = 2
    LVLDEV = 3
    LVL3 = 4
    FINISHED = 5
    QUIT = 6


class Game : 
    
    def __init__(self) -> None:
        self.state = State.MENU
        self.lvl = 0
        self.objects = []

    def draw(self,display):
        size = display.get_size()

        mouse = pygame.mouse.get_pos() 

        match self.state:
            case State.MENU:
                smallfont = pygame.font.SysFont('Corbel',35) 
                
                for x,pos in enumerate(button_pos) :
                    text = smallfont.render('>  '+ menu_texts[x], True , (255,255,255)) 
                    display.blit(text,(pos[0],pos[1]))
                    if pos[0] <= mouse[0] <= pos[0]+140 and pos[1] <= mouse[1] <= pos[1]+40: 
                        pygame.draw.rect(display,(255,255,255),[pos[0],pos[1],30,40]) 
               
                pass

            case State.LVLMANAGER:
                if len(self.objects)==0:
                    self.objects.append(Ennemi(150,150,Type.TECHNO,Rank.BASE))
                map = Map("./config/map.txt")
                map.draw(display)

                for i in self.objects:
                    i.draw(display)

            case State.LVLDEV:
                map = Map("./config/map.txt")
                map.draw(display)

            case State.QUIT:
                pygame.quit()
                sys.exit()


    def check_where_click(self,mouse_x,mouse_y):
        match self.state:
            case State.MENU:
                for x,pos in enumerate(button_pos) :
                    
                    if pos[0] <= mouse_x <= pos[0]+140 and pos[1] <= mouse_y <= pos[1]+40: 
                        match x:
                            case 0:
                                self.state = State.LVLMANAGER
                            case 1:
                                self.state = State.LVLDEV
                            case 2:
                                self.state = State.QUIT
            
    

   