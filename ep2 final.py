import random

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

def empilha(listacartas,origem,destino):
    listacartas[destino] = listacartas[origem]
    del(listacartas[origem])
    return listacartas

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
baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'] 

random.shuffle(baralho)

jogo = True

while jogo:
    cartas = []
    for i in range(0,len(baralho)) :
        print('\n'+str(i)+ '. '+baralho[i])
    pergunta = int(input('escolha uma carta, ou 99 para finalizar: '))
    if pergunta == 99:
        jogo = False
    elif pergunta == 0 or pergunta > 51:
        print('carta invalida')
    else:    
        if pergunta == 1 or pergunta == 2:
            cartas.append(baralho[pergunta-1])
            cartas.append(baralho[pergunta])
        if pergunta > 2:
            cartas.append(baralho[pergunta-3])
            cartas.append(baralho[pergunta-2])
            cartas.append(baralho[pergunta-1])
            cartas.append(baralho[pergunta])
        movimentos = lista_movimentos_possiveis(cartas,len(cartas)-1)
        if movimentos == []:
            print('escolha outra carta')
        if movimentos == [1,3]:
            escolha = int(input('para qual das cartas gostaria de movimentar? '))
            print('\n'+str(i)+ '. '+cartas[pergunta - 3]+cartas[pergunta-1])
            if escolha == 0:
                movimento = pergunta - 3
            if escolha == 1:
                movimento = pergunta - 1
        elif movimentos == [1]:
            movimento = bpergunta - 1
        elif movimentos == [3]:
            movimento = pergunta - 3
        jogada = empilha(baralho, pergunta , movimento )
        acaba = possui_movimentos_possiveis(baralho)
        if acaba == True:
            jogo = False
    