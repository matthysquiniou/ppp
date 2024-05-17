from Objet import Objet

class Chateau(Objet):

    def __init__(self, x, y, niveau, technologie, asset_name):
        super().__init__(x, y, asset_name)
        self.niveau = niveau
        self.technologie = technologie