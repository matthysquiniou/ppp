from enum import Enum
import pygame
import sys
from Map import Map
from Ennemi import Ennemi
from Type import Type
from Rank import Rank
import time




menu_texts = ["Become manager","Become dev","Quit"]

class State(Enum):
    ERROR = 0
    MENU = 1
    LVLMANAGER = 2
    LVLDEV = 3
    LVL3 = 4
    FINISHED = 5
    QUIT = 6


class Game : 
    
    def __init__(self,size=(1920,1080)) -> None:
        self.MANAGER_BUTTON_POS = (size[0]//2-size[0]//10,size[1]//2)
        self.DEV_BUTTON_POS = (size[0]//2-size[0]//10,size[1]//2+50)
        self.QUIT_BUTTON_POS = (size[0]//2-size[0]//10,size[1]-150)
        self.LOGO_POS = (size[0]//2-size[0]//5,100)
        self.LOGO_SIZE = (size[0]//2,size[1]//4)

        self.button_pos = [self.MANAGER_BUTTON_POS,self.DEV_BUTTON_POS,self.QUIT_BUTTON_POS,]
        self.state = State.MENU
        self.lvl = 0
        self.objects = []

    def draw(self,display):
        size = display.get_size()

        mouse = pygame.mouse.get_pos() 

        match self.state:
            case State.MENU:
                logo = pygame.image.load('./images/logo.png').convert()
                logo = pygame.transform.scale(logo,self.LOGO_SIZE)
                display.blit(logo,self.LOGO_POS)

                smallfont = pygame.font.SysFont('Corbel',35) 
                
                for x,pos in enumerate(self.button_pos) :
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

                if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                     pygame.draw.rect(display,(255,255,255),[0,0,50,50]) 

            case State.LVLDEV:



                if len(self.objects)==0:
                    self.objects.append(Ennemi(150,150,Type.TECHNO,Rank.BASE))
                map = Map("./config/map.txt")
                map.draw(display)

                for i in self.objects:
                    i.draw(display)

                if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                     pygame.draw.rect(display,(255,255,255),[0,0,50,50]) 

            case State.QUIT:
                pygame.quit()
                sys.exit()


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
                if 0 <= mouse_x <= 50 and 0 <= mouse_y <= 50:
                    
                    pass

   