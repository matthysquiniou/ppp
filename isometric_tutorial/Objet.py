from abc import ABC, abstractmethod

class Objet(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y