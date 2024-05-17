from Objet import Objet

class Ennemi(Objet):
    def __init__(self, x, y, niveau, faiblesses, resistances, defence, attaque, vie, vitesse, asset_name):
        super().__init__(x, y, asset_name)
        self.niveau = niveau
        self.faiblesses = faiblesses
        self.resistances = resistances
        self.defence = defence
        self.attaque = attaque
        self.vie = vie
        self.vitesse = vitesse