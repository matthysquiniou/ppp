from Objet import Objet

class Ennemi(Objet):
    def __init__(self, x, y, niveau, faiblesses, resistances, defence, attaque, vie):
        super().__init__(x, y)
        self.niveau = niveau
        self.faiblesses = faiblesses
        self.resistances = resistances
        self.defence = defence
        self.attaque = attaque
        self.vie = vie