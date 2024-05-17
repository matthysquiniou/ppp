import pygame, sys, time, random
from Map import Map

from pygame.locals import *
pygame.init()
pygame.display.set_caption('PPP')


#config game
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((900, 900))
mouse = pygame.mouse

# chateau_img = pygame.image.load('image.png').convert()
# chateau_img.set_colorkey((255, 255, 255))
# size = chateau_img.get_size()
# coeff = 0.5
# chateau_img = pygame.transform.scale(chateau_img,(size[0]*coeff,size[1]*coeff))

map = Map("./config/map.txt")    

while True:
    #display.fill((0,0,0))
    (mouse_x, mouse_y) = mouse.get_pos()

    map.draw(display)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(1)
