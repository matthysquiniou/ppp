import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('PPP')


#config game
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((900, 900))
mouse = pygame.mouse

grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))

chateau_img = pygame.image.load('image.png').convert()
chateau_img.set_colorkey((255, 255, 255))
size = chateau_img.get_size()
coeff = 0.5
chateau_img = pygame.transform.scale(chateau_img,(size[0]*coeff,size[1]*coeff))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    #display.fill((0,0,0))
    (mouse_x, mouse_y) = mouse.get_pos()

    
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
    display.blit(chateau_img,(0,0))           

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
