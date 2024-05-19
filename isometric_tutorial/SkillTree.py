import pygame
from Type import Type
import random

QUESTIONS = {
    "SOCIAL" : [("La vie c'est cool", True)],
    "TECHNO" : [("Le python est un langage interpreté", True)],
    "PHYSIC" : [("Courber le dos pour supporter une charge lourde", False)]
}


class Tree:
    def __init__(self,player,size=(1920,1080)):
        self.social = player.social_points
        self.techno = player.technologic_points
        self.physic = player.physical_points

        self.player = player
        self.player_remain_pos = (size[0]//3,size[1]//6)

        self.ask = False
        self.question = ""
        self.question_index = 0
        self.question_pos = (size[0]//5,size[1]//2)
        self.question_thema = ""

        self.buttons_ask_pos = [(0,0),
                                (size[0]//4,size[1]//5*4),
                                (size[0]//4*3,size[1]//5*4)]
        
        self.buttons_ask_texts = ["back",
                                  "Vrai",
                                  "Faux"]


        self.button_pos = [(0,0),
                           (size[0]//3,size[1]//5*2),
                           (size[0]//3,size[1]//5*3),
                           (size[0]//3,size[1]//5*4),
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

            text = smallfont.render(self.question, True , (255,255,255)) 
            display.blit(text,(self.question_pos))


            for x,pos in enumerate(self.buttons_ask_pos) :
                if pos[0] <= mouse[0] <= pos[0]+50 and pos[1] <= mouse[1] <= pos[1]+50: 
                    pygame.draw.rect(display,(150,150,150),[pos[0],pos[1],50,50])
                text = smallfont.render(self.buttons_ask_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))

        else:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()

            text = smallfont.render("Points restants : " +str(self.player.remain_points), True , (255,255,255)) 
            display.blit(text,(self.player_remain_pos))
                    
            for x,pos in enumerate(self.button_pos) :
                if self.button_texts[x] == "+" or self.button_texts[x] == "-" or self.button_texts[x] == "back":
                    if pos[0] <= mouse[0] <= pos[0]+50 and pos[1] <= mouse[1] <= pos[1]+50: 
                                pygame.draw.rect(display,(150,150,150),[pos[0],pos[1],50,50])
                text = smallfont.render(self.button_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))
                

    def check_click(self,x,y):
        if self.ask:
            for index,pos in enumerate(self.buttons_ask_pos):
                if pos[0] <= x <= pos[0] + 50 and  pos[1] <= y <= pos[1]+50:
                    
                    if self.question_thema == "SOCIAL":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["SOCIAL"][self.question_index][1]:
                            self.player.add_point(Type.MANAGE,1)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["SOCIAL"][self.question_index][1]:
                            self.player.add_point(Type.MANAGE,1)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -1
                    elif self.question_thema == "TECHNO":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["TECHNO"][self.question_index][1]:
                            self.player.add_point(Type.TECHNO,1)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["TECHNO"][self.question_index][1]:
                            self.player.add_point(Type.TECHNO,1)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -1
                    elif self.question_thema == "TECHNO":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["PHYSIC"][self.question_index][1]:
                            self.player.add_point(Type.PHYSIQUE,1)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["PHYSIC"][self.question_index][1]:
                            self.player.add_point(Type.PHYSIQUE,1)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -1
                    

                    self.update_player()
                    self.ask = False
                    break
        else:
            
            for index,pos in enumerate(self.button_pos):
                
                if pos[0] <= x <= pos[0] + 50 and  pos[1] <= y <= pos[1] +50:
                    
                    if self.button_texts[index] == "-":
                        if (index %3 == 1 and self.social == 0) or (index %3 == 2 and self.techno == 0) or (index %3 == 0 and self.physic == 0):
                            continue   
                        else :
                            self.player.delete_point( (Type.MANAGE if index %3 == 1 
                                                    else Type.TECHNO if index %3 == 2 
                                                    else Type.PHYSIQUE) ,1)
                            

                    elif self.button_texts[index] == "+":
                        if self.player.remain_points > 0 :
                            self.ask = True
                            if index % 3 == 1:
                                self.question_thema = "SOCIAL"
                                ques = QUESTIONS["SOCIAL"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["SOCIAL"][self.question_index][0]
                            elif index % 3 == 2:
                                self.question_thema = "TECHNO"
                                ques = QUESTIONS["TECHNO"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["TECHNO"][self.question_index][0]
                            else:
                                self.question_thema = "PHYSIC"
                                ques = QUESTIONS["PHYSIC"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["PHYSIC"][self.question_index][0]


    def update_player(self):
        self.social = self.player.social_points
        self.techno = self.player.technologic_points
        self.physic = self.player.physical_points

        self.button_texts[4] = "Social : "+str(self.social)
        self.button_texts[5] = "Tech : "+str(self.techno)
        self.button_texts[6] = "Physic : "+str(self.physic)