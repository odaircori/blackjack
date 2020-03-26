import weakref

class Jogador(object):
    def __init__(self,nome):
        self.nome = nome        

    minhasCartas = []
    totalCartas = 0

    def pedirCarta(self, baralho):
        self.minhasCartas.append(baralho.pop())
        self.ultimaCarta =  self.minhasCartas[len(self.minhasCartas) -1]
        self.contaCartas()


    def contaCartas(self):
        self.totalCartas = 0
        for i in self.minhasCartas:
            if i["carta"] == "A":
                self.totalCartas+= 1
            else:
                if i["carta"] == "J":
                    self.totalCartas+= 11
                else:
                    if i["carta"] == "Q":
                        self.totalCartas+= 12
                    else:
                        if i["carta"] == "K":
                            self.totalCartas+= 13
                        else:                
                            self.totalCartas+= i["carta"]
        return self.totalCartas

    def apagaMinhasCartas(self):
        self.minhasCartas.clear()
    

class Croupie(Jogador):
    def __init__(self, nome = "Croupiê"):
        self.nome = nome

    minhasCartas = []
    totalCartas = 0
