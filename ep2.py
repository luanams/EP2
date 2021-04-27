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
    movimentos = 0 
    for i in range(0,len(baralho)-1):
        naipe = extrai_naipe(baralho[i])
        valor = extrai_valor(baralho[i])
        if indice == '0':
            resultado = []
        if indice == '1':
            if valor[1] == valor[0] or naipe[1] == naipe[0]:
                movimentos += 1
        if indice == '2':
            if valor[2] == valor[1] or naipe[2] == naipe[1]:
                movimentos += 1
            if valor[2] == valor[0] or naipe[2] == naipe[0]:
                movimentos += 3
        if indice == '3':
            if valor[3] == valor[2] or naipe[3] == naipe[2]:
                movimentos += 1
            if valor[3] == valor[1] or naipe[3] == naipe[1]:
                movimentos += 3
    if movimentos == '4':
        resultado = [1,3]
    if movimentos == '1':
        resultado = [1]
    if movimentos == '3':
        resultado = [3]
    return resultado

print(lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'],1))