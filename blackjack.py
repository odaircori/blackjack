import random
from integrantes import participantes
from baralho import naipes
from baralho import cartas

class Baralho(cartas.Cartas):
    def __init__(self):
        self.baralho = []

    def novoBaralho(self):
        for n in naipes.Naipes().naipes:
            for c in cartas.Cartas().cartas:
                carta = {"naipe": n, "carta": c}
                self.baralho.append(carta)
        
        return random.sample(self.baralho, len(self.baralho))

#########################################################################

while True:
    jogadorJoga = True
    casaJoga = True

    nomeJogador = input('Por favor, qual seu nome? ')

    jogador = participantes.Jogador(nomeJogador)
    croupie = participantes.Croupie()
    baralho = Baralho().novoBaralho()

    novaPartida = "N"

    print('Bem vindo à mesa de BlackJack ', nomeJogador, ', vamos começar. Boa sorte!!!')

    comecarPartida = True

    while comecarPartida:
        comecar = input('Posso retirar sua primeira carta?(S/N) ').upper()

        if comecar == "S":
            break
        else:
            print('Então foda-se!!!')
            jogadorJoga = False
            break
    
    if jogadorJoga:

        while jogadorJoga:

            jogador.pedirCarta(baralho)
            print('Sua carta é %s de %s' % (jogador.ultimaCarta["carta"], jogador.ultimaCarta["naipe"]))
            print('Sua contagem atual é de {0}'.format(jogador.contaCartas()))

            if jogador.contaCartas() > 21:
                print("Você estourou 21 pontos. LOOOSEERRR!!!")
                casaJoga = False
                novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                break
            elif jogador.contaCartas() == 21:
                print("Parabéns, você acertou em cheio os 21 pontos. BLACKJACK!!!")
                casaJoga = False
                novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                casaJoga = False
                break
            else:
                outraCarta = input('Deseja outra carta?(S/N)').upper()

            if outraCarta == 'S':
                continue
            else:
                jogadorJoga = False
                break

        while casaJoga:
            croupie.pedirCarta(baralho)
            print('A carta do Croupiê é %s de %s' % (croupie.ultimaCarta["carta"], croupie.ultimaCarta["naipe"]))
            print('A pontuação atual do Croupiê é {0}'.format(croupie.contaCartas()))

            if croupie.contaCartas() > jogador.contaCartas() and croupie.contaCartas() <= 21:
                print('A casa ganhou!')

                novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                break

            elif croupie.contaCartas() > 21:
                print('A casa estourou os 21 pontos, Parabéns, você ganhou')
                novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                break
            else:
                continue
        
    if novaPartida == "S":
        jogador.apagaMinhasCartas()
        croupie.apagaMinhasCartas()
        continue
    else:
        break