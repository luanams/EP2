import random
baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'] 

random.shuffle(baralho)

for i in range(0,52) :
    print('\n'+str(i)+ '. '+baralho[i])
jogo = True

while jogo:
    pergunta = int(input('escolha uma carta de 0 a 51: '))
    carta = baralho[pergunta]
    def extrai_valor(carta):
        valor = carta [0:len(carta)-1]
        return valor
    def extrai_naipe(carta):
        naipe = carta[len(carta)-1]
        return naipe
    jogo = False
print(extrai_naipe(carta))
print(extrai_valor(carta))