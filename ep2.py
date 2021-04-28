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
    if indice == 0:
        return resultado
    else:
        if listavalores[indice] == listavalores[indice-1] or listanaipe[indice] == listanaipe[indice-1]:
                resultado.append(1)
        if indice > 2:  
            if listavalores[indice] == listavalores[indice-3] or listanaipe[indice] == listanaipe[indice-3]:
                resultado.append(3)
    return resultado

def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del(baralho[origem])
    return baralho

def possui_movimentos_possiveis(baralho):
    sim = 0
    for i in range(0,len(baralho)-1):
        movimentos = lista_movimentos_possiveis(baralho,i)
        if movimentos == []:
            sim += 0
        else:
            sim += 1
    if sim != 0:
        return True
    else:
        return False
