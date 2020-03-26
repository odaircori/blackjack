import random
from baralho import cartas
from baralho import naipes

class Baralho(cartas.Cartas):
    def __init__(self):
        self.baralho = []

    def novoBaralho(self):
        for n in naipes.Naipes().naipes:
            for c in cartas.Cartas().cartas:
                carta = {"naipe": n, "carta": c}
                self.baralho.append(carta)
        
        return random.sample(self.baralho, len(self.baralho))