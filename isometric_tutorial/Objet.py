from abc import ABC, abstractmethod
import pygame

class Objet(ABC):
    ASSET_PATH = "../images/"
    def __init__(self, x, y, ASSET_NAME):
        self.x = x
        self.y = y
        self.asset = self.ASSET_PATH+ASSET_NAME

    def draw(self, display):
        img_objet = pygame.image.load(self.asset).convert_alpha()
        display.blit(img_objet, (self.x,self.y))