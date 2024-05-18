import pygame

class Tree:
    def __init__(self,player,size=(1920,1080)):
        self.social = player.social_points
        self.techno = player.technologic_points
        self.physic = player.physical_points

        self.ask = False



        self.button_pos = [(size[0]//4,size[1]//5*2),
                           (size[0]//4,size[1]//5*3),
                           (size[0]//4,size[1]//5*4),
                           (size[0]//2,size[1]//5*2),
                           (size[0]//2,size[1]//5*3),
                           (size[0]//2,size[1]//5*4),
                           (size[0]//4*3,size[1]//5*2),
                           (size[0]//4*3,size[1]//5*3),
                           (size[0]//4*3,size[1]//5*4),]
        self.button_texts = ["-","-","-","Social : "+str(self.social),"Tech : "+str(self.techno),"Physic : "+str(self.physic),"+","+","+"]

    def draw(self,display):
        if self.ask:
              pass
        else:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()
                    
            for x,pos in enumerate(self.button_pos) :
                text = smallfont.render(self.button_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))
                if pos[0] <= mouse[0] <= pos[0]+50 and pos[1] <= mouse[1] <= pos[1]+50: 
                            pygame.draw.rect(display,(255,255,255),[pos[0],pos[1],50,50])

    