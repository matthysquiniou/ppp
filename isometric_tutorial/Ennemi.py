from Objet import Objet
from Type import Type
from Rank import Rank
from Action import Action

class Ennemi(Objet):
    def __init__(self, x:int, y:int, type: Type, rank: Rank, asset_name: str):
        super().__init__(x, y, "ennemi/"+type.asset+" "+rank.color+".png", 9, 5, Action.PERSONNAGE)
        self.faiblesse = type.faiblesse
        self.resistance = type.resistance
        self.defence = type.defence * rank.stat_mult
        self.attaque = type.attaque * rank.stat_mult
        self.vie = type.vie * rank.stat_mult
        self.vitesse = type.vitesse * rank.stat_mult
