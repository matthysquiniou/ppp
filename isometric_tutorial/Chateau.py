from Objet import Objet

class Chateau(Objet):
    def __init__(self, x, y, niveau, technologie):
        super().__init__(x, y)
        self.niveau = niveau
        self.technologie = technologie