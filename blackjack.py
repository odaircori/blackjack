from integrantes import participantes
import carteado
import time

while True:
    jogadorJoga = True
    casaJoga = True

    try:
        jogador
    except:
        nomeJogador = input('Por favor, qual seu nome? ')

        while True:
            try:    
                valor = float(input('Qual o valor em fichas? '))        
            except:
                print('Você precisa informar uma valor em números')
            else:
                break
        jogador = participantes.Jogador(nomeJogador, valor)
        croupie = participantes.Croupie()

        print('Bem vindo à mesa de BlackJack ', nomeJogador, ', vamos começar. Boa sorte!!!')
    else:
        continue

    finally:

        baralho = carteado.Baralho().novoBaralho()

        comecarPartida = True

        while comecarPartida:
            comecar = input('\nPosso retirar sua primeira carta?(S/N) ').upper()

            if comecar == "S":
                break
            else:
                print('Então foda-se!!!')
                jogadorJoga = False
                time.sleep(3)
                break
        
        if jogadorJoga:

            while True:
                try:
                    valorAposta = float(input('Quanto você deseja perder? Ops... Apostar: '))
                except:
                    print('Você precisa informar uma valor em números')
                else:
                    break        

            while jogadorJoga:

                jogador.pedirCarta(baralho)
                print('Sua carta é %s de %s' % (jogador.ultimaCarta["carta"], jogador.ultimaCarta["naipe"]))
                print('\nSua contagem atual é de {0}'.format(jogador.contaCartas()))

                if jogador.contaCartas() > 21:
                    print("Você estourou 21 pontos. LOOOSEERRR!!!")
                    print('\nVocê perdeu', valorAposta)
                    casaJoga = False
                    jogador.fazAposta(valorAposta)
                    jogador.novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                    break
                elif jogador.contaCartas() == 21:
                    print("Parabéns, você acertou em cheio os 21 pontos. BLACKJACK!!!")
                    casaJoga = False
                    jogador.rodadaGanha(valorAposta)
                    jogador.novaPartida = input('\nDeseja jogar novamente?(S/N)').upper()
                    casaJoga = False
                    break
                else:
                    outraCarta = input('\nDeseja outra carta?(S/N)').upper()

                if outraCarta == 'S':
                    continue
                else:
                    jogadorJoga = False
                    break

            while casaJoga:
                croupie.pedirCarta(baralho)
                print('A carta do Croupiê é %s de %s' % (croupie.ultimaCarta["carta"], croupie.ultimaCarta["naipe"]))
                print('A pontuação atual do Croupiê é {0}'.format(croupie.contaCartas()))
                time.sleep(3)

                if croupie.contaCartas() > jogador.contaCartas() and croupie.contaCartas() <= 21:
                    jogador.fazAposta(valorAposta)
                    print('A casa ganhou!')

                    novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                    break

                elif croupie.contaCartas() > 21:
                    print('A casa estourou os 21 pontos, Parabéns, você ganhou')
                    jogador.rodadaGanha(valorAposta)
                    print('Você ganhou %s. Seu valor total é %s'.format(valorAposta * 1.25, jogador.valorPraGastar))
                    jogador.novaPartida = input('Deseja jogar novamente?(S/N)').upper()
                    break
                else:
                    continue
            
        if jogador.novaPartida == "S":
            jogador.apagaMinhasCartas()
            croupie.apagaMinhasCartas()
            continue
        else:
            break