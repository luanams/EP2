def cria_baralho():
    baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'] 
    return baralho 

def extrai_valor(carta):
    valor = carta [0:len(carta)-1]
    return valor

def extrai_naipe(carta):
    naipe = carta[len(carta)-1]
    return naipe

def lista_movimentos_possiveis(baralho,indice):
    for i in range(0,len(baralho)):
        naipee = extrai_naipe(baralho[i])
        valorr = extrai_valor(baralho[i])
        if indice == '1':
            if valorr[1] == valorr[0] or naipee[1] == naipee[0]:
                return([1])
        if indice == '2':
            if valorr[2] == valorr[1] or naipee[2] == naipee[1]: 
                return([1])
            if valorr[2] == valorr[0] or naipee[2] == naipee[0]:
                return([3])
            if valorr[2] == valorr[1] or naipee[2] == naipee[1] and valorr[2] == valorr[0] or naipee[2] == naipee[0]:
                return([1,3])
        if indice == '3':
            if valorr[3] == valorr[2] or naipee[3] == naipee[2]:
                return([1])
            if valorr[3] == valorr[1] or naipee[3] == naipee[1]:
                return([3]) 
            if valorr[3] == valorr[2] or naipee[3] == naipee[2] and valorr[3] == valorr[1] or naipee[3] == naipee[1]:
                return([1,3])


print(lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'],1))