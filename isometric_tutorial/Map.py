import pygame
import random
import math

class Map:
    def __init__(self,file) -> None:
        self.file = file
        
    def draw(self,display):
        size = display.get_size()

        grass_img = pygame.image.load('./images/grass.png').convert()
        grass_img.set_colorkey((0, 0, 0))

        sand_img = pygame.image.load('./images/walk.png').convert()
        sand_img.set_colorkey((0, 0, 0))

        f = open(self.file)


        map_data = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()

        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    display.blit(grass_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))

                elif tile == 2:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    display.blit(sand_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))