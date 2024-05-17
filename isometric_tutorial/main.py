import pygame, sys, time, random
from Map import Map
from game import Game,State

from pygame.locals import *
pygame.init()
pygame.display.set_caption('PPP')


#config game
screen = pygame.display.set_mode((1920, 1080))
mouse = pygame.mouse

chateau_img = pygame.image.load('./images/image.png').convert()
chateau_img.set_colorkey((255, 255, 255))
size = chateau_img.get_size()
coeff = 0.5
chateau_img = pygame.transform.scale(chateau_img,(size[0]*coeff,size[1]*coeff))


game = Game()  

map = Map("./config/map.txt") 
map.draw(screen)
screen.blit(chateau_img,(150,150))

while game.state != State.FINISHED:
    screen.fill((0,0,0))
    match game.state:
        case State.MENU:
            
            pass
        case State.LVL1:
            
            
            pass


    #display.fill((0,0,0))
    (mouse_x, mouse_y) = mouse.get_pos()
    
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    
    pygame.display.update()
    