from Type import Type

class Player:

    def __init__(self):
        self.social_points = 0
        self.physical_points = 0
        self.technologic_points = 0

        self.healthPoint = 100
    
    def add_point(self,type:Type,number:int):
        if type == Type.PHYSIQUE:
            self.physical_points += number
        elif type == Type.TECHNO:
            self.technologic_points += number
        elif type == Type.MANAGE:
            self.social_points += number