from abc import ABC, abstractmethod
import pygame
from generate_animation import generate_animation
from Action import Action

class Objet(ABC):
    ASSET_PATH = "../images/"
    def __init__(self, x:int, y:int, asset_name, rows: int = None, cols: int = None, actions: Action = None):
        self.x = x
        self.y = y
        if rows and cols:
            self.animations = generate_animation(self.ASSET_PATH+asset_name, rows, cols, actions)
        else:
            self.animations = None
    def draw(self, screen): #TODO : gérer les animations / actions si il y en a (faire une "ia" pour les actions des ennemis)
        img_objet = pygame.image.load(self.asset).convert_alpha()
        screen.blit(img_objet, (self.x,self.y))