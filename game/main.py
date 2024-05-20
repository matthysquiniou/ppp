import pygame
from State import State
from SubState import SubState
from game import Game

from pygame.locals import *
pygame.init()
pygame.display.set_caption('PPP')

windowSize = (960, 540)
screen = pygame.display.set_mode(windowSize)
mouse = pygame.mouse
clock = pygame.time.Clock()


game = Game(windowSize)  

while game.state != State.FINISHED:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game.state = State.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            game.check_where_click(pos[0],pos[1])
        if event.type == pygame.KEYDOWN and game.sub_state in [SubState.WIN,SubState.LOSE] :
            game.check_key(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.state = State.QUIT

    screen.fill((0,0,0))
    game.draw(screen)
    clock.tick(60)


    

    
    pygame.display.update()
    