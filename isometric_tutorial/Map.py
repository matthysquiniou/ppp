import pygame
import random

class Map:
    def __init__(self,file) -> None:
        self.file = file
        
    def draw(self,display):
        size = display.get_size()

        grass_img = pygame.image.load('./images/grass.png').convert()
        grass_img.set_colorkey((0, 0, 0))

        f = open(self.file)


        map_data = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()

        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    if random.randint(0,10) == 3:
                        display.blit(grass_img, (x * 10 - y * 10,  x * 5 + y * 5))