def cria_baralho():
    baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'] 
    return baralho 

def extrai_valor(carta):
    valor = carta [0:len(carta)-1]
    return valor

def extrai_naipe(carta):
    naipe = carta[len(carta)-1]
    return naipe

def lista_movimentos_possiveis(cartas,indice):
    listanaipe = []
    listavalores = []
    resultado = []
    for i in range(0,len(cartas)):
        naipes = extrai_naipe(cartas[i])
        valores = extrai_valor(cartas[i])
        listanaipe.append(naipes)
        listavalores.append(valores)
    if indice == 1:
        if listavalores[1] == listavalores[0] or listanaipe[1] == listanaipe[0]:
            resultado.append(1)  
    if indice == 2:
        if listavalores[2] == listavalores[1] or listanaipe[2] == listanaipe[1]: 
            resultado.append(1)
        if listavalores[2] == listavalores[0] or listanaipe[2] == listanaipe[0]:
            resultado.append(3)
    if indice == 3:
        if listavalores[3] == listavalores[2] or listanaipe[3] == listanaipe[2]:
            resultado.append(1)
        if listavalores[3] == listavalores[1] or listanaipe[3] == listanaipe[1]:
            resultado.append(3)
    return resultado
            


print(lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'],1))