import pygame, sys, time, random

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

while game.state != State.FINISHED:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game.state = State.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            game.check_where_click(pos[0],pos[1])
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.state = State.QUIT

    screen.fill((0,0,0))
    game.draw(screen)


    

    
    pygame.display.update()
    