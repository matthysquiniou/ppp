import pygame, sys, time, random

from game import Game,State

from pygame.locals import *
pygame.init()
pygame.display.set_caption('PPP')

windowSize = (960, 540)
#config game
screen = pygame.display.set_mode(windowSize)
mouse = pygame.mouse



game = Game(windowSize)  

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
    