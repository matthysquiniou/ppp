import pygame
from Type import Type



class Tree:
    def __init__(self,player,size=(1920,1080)):
        self.social = player.social_points
        self.techno = player.technologic_points
        self.physic = player.physical_points

        self.player = player

        self.ask = False
        self.question = ""

        self.buttons_ask_pos = [(0,0),
                                (size[0]//4,size[1]//5*4),
                                (size[0]//4*3,size[1]//5*4)]


        self.button_pos = [(0,0),
                           (size[0]//4,size[1]//5*2),
                           (size[0]//4,size[1]//5*3),
                           (size[0]//4,size[1]//5*4),
                           (size[0]//2,size[1]//5*2),
                           (size[0]//2,size[1]//5*3),
                           (size[0]//2,size[1]//5*4),
                           (size[0]//4*3,size[1]//5*2),
                           (size[0]//4*3,size[1]//5*3),
                           (size[0]//4*3,size[1]//5*4),]
        


        self.button_texts = ["back",
                             "-",
                             "-",
                             "-",
                             "Social : "+str(self.social),
                             "Tech : "+str(self.techno),
                             "Physic : "+str(self.physic),
                             "+",
                             "+",
                             "+"]

    def draw(self,display):
        if self.ask:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()
        else:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()
                    
            for x,pos in enumerate(self.button_pos) :
                text = smallfont.render(self.button_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))
                if text == "+" or text == "-" or text == "back":
                    if pos[0] <= mouse[0] <= pos[0]+50 and pos[1] <= mouse[1] <= pos[1]+50: 
                                pygame.draw.rect(display,(255,255,255),[pos[0],pos[1],50,50])

    def check_click(self,x,y):
        if self.ask:
            pass
        else:
            for index,pos in enumerate(self.button_pos):
                if pos[0] <= x <= pos[0] + 50 and  pos[1] <= y <= pos[1]:
                    if self.button_texts[index] == "-":
                        if (index %3 == 1 and self.social == 0) or (index %3 == 2 and self.techno == 0) or (index %3 == 0 and self.physic == 0):
                            continue   
                        else :
                            self.player.delete_point( (Type.MANAGE if index %3 == 1 
                                                    else Type.TECHNO if index %3 == 2 
                                                    else Type.PHYSIQUE) ,1)
                    elif self.button_texts[index] == "+":
                        self.ask = True
                        if index % 3 == 1:
                            pass