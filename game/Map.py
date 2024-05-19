import pygame
import random
import math

class Map:
    def __init__(self,file,size) -> None:
        self.file = file

        self.dis = pygame.Surface(size)
        self.initMap(size)

        
        
    def draw(self,display):
        display.blit(pygame.transform.scale(self.dis, display.get_size()),(0,0))

    def initMap(self,size):
        grass_img = pygame.image.load('./images/grass.png').convert()
        grass_img.set_colorkey((0, 0, 0))

        lghsand_img = pygame.image.load('./images/sand_light.png').convert()
        lghsand_img.set_colorkey((0, 0, 0))

        sand_img = pygame.image.load('./images/sand.png').convert()
        sand_img.set_colorkey((0, 0, 0))

        water_img = pygame.image.load('./images/water.png').convert()
        water_img.set_colorkey((0, 0, 0))

        waterfish_img = pygame.image.load('./images/water_fish.png').convert()
        waterfish_img.set_colorkey((0, 0, 0))

        f = open(self.file)


        map_data = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()

        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    self.dis.blit(grass_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))

                elif tile == 2:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    self.dis.blit(sand_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))
                elif tile == 3:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    self.dis.blit(water_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))
                elif tile == 4:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    self.dis.blit(lghsand_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))
                elif tile == 5:
                    coeff_x = (x-len(row)//2)
                   
                    coeff_y = (y-len(map_data)//2)
                    
                    self.dis.blit(waterfish_img, ((size[0]//2) + coeff_x  * 10-coeff_y*10,(size[1]//2)+ coeff_y*5+coeff_x*5))