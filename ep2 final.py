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
    def lista_movimentos_possiveis(cartas,pergunta):
        if pergunta == 1 or pergunta == 2:
            cartas = [baralho[pergunta],baralho[pergunta-1]]
        if pergunta > 2:
            cartas = [baralho[pergunta],baralho[pergunta-1],baralho[pergunta-3]]
        listanaipe = []
        listavalores = []
        resultado = []
        for i in range(0,len(cartas)):
            naipes = extrai_naipe(cartas[i])
            valores = extrai_valor(cartas[i])
            listanaipe.append(naipes)
            listavalores.append(valores)
        if pergunta == 0:
            jogo == False
        else:
            if listavalores[pergunta] == listavalores[pergunta-1] or listanaipe[pergunta] == listanaipe[pergunta-1]:
                resultado.append(1)
            else:
            if pergunta > 2:  
                if listavalores[pergunta] == listavalores[pergunta-3] or listanaipe[pergunta] == listanaipe[pergunta-3]:
                    resultado.append(3)
        return resultado