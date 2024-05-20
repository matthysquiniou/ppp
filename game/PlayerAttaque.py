import random
from Type import Type
import pygame
import math

class PlayerAttaque:
    def __init__(self,ennemi,x,y,ennemi_distance,social_points,technologic_points,physical_points):
        self.ennemi = ennemi
        self.x = x+100
        self.y = y+100
        self.direction = self.calculer_coefficients_direction(ennemi.x,ennemi.y)
        self.attaque_type = self.choose_attack_type(social_points,technologic_points,physical_points)
        self.vitesse = 50
        self.ennemi_distance = ennemi_distance
        self.distance_run = 0
        
        
        match self.attaque_type:
            case Type.MANAGE:
                self.damage = social_points
                self.item_to_render_color = (255, 0, 0)
            case Type.TECHNO:  
                self.damage = technologic_points
                self.item_to_render_color = (0, 255, 0)
            case Type.PHYSIQUE:
                self.damage = physical_points
                self.item_to_render_color = (0, 0, 255)


    def choose_attack_type(self,sp,tp,pp):
        types = [Type.MANAGE,Type.TECHNO,Type.PHYSIQUE]
        probabilites = [sp,tp,pp]
        choix = random.choices(types, weights=probabilites, k=sp+tp+pp)[0]
        return choix

    def draw(self,display,game): #TODO: rentre en colision trop tot
        self.update_distance()
        self.distance_run = self.distance_run + abs(self.direction[0]*self.vitesse*0.15) + abs(self.direction[1]*self.vitesse*0.15)
        self.x = self.x + self.direction[0]*self.vitesse*0.15
        self.y = self.y + self.direction[1]*self.vitesse*0.15
        if self.distance_run >= self.ennemi_distance:
            self.ennemi.takeDamage(self.damage,self.attaque_type,game)
            return True
        pygame.draw.circle(display, self.item_to_render_color, (self.x, self.y), math.log2(self.damage))
        return False

    def calculer_coefficients_direction(self, x2, y2):
        x1 = self.x
        y1 = self.y
        dx = x2 - x1
        dy = y2 - y1
        norm = abs(dx) + abs(dy)
        coeffX = dx / norm
        coeffY = dy / norm
        return [coeffX, coeffY]
    
    def update_distance(self):
        self.ennemi_distance = math.sqrt((self.ennemi.x - self.x) ** 2 + (self.ennemi.y - self.y) ** 2)