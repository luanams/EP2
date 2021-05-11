import random
baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'] 

random.shuffle(baralho)
jogo = True

def extrai_valor(carta):
    valor = carta [0:len(carta)-1]
    return valor
def extrai_naipe(carta):
    naipe = carta[len(carta)-1]
    return naipe

while jogo:
    for i in range(0,len(baralho)) :
        print('\n'+str(i)+ '. '+baralho[i])
    pergunta = int(input('escolha uma carta: '))
    carta = baralho[pergunta]
    def lista_movimentos_possiveis(cartas,pergunta):
        cartas = []
        if pergunta == '1' or pergunta == '2':
            cartas.append(carta - 1) 
            cartas.append(carta)
        if pergunta > '2':
            cartas.append(carta - 3)
            cartas.append(carta - 2)
            cartas.append(carta - 1)
            cartas.append(carta)
        listanaipe = []
        listavalores = []
        resultado = []
        
        for a in range(0,len(cartas)):
            naipes = extrai_naipe(cartas[a])
            valores = extrai_valor(cartas[a])
            listanaipe.append(naipes)
            listavalores.append(valores)
            
        if pergunta != 0:
            if listavalores[pergunta] == listavalores[pergunta-1] or listanaipe[pergunta] == listanaipe[pergunta-1]:
                resultado.append(1)
        if pergunta > 2:  
            if listavalores[pergunta] == listavalores[pergunta-3] or listanaipe[pergunta] == listanaipe[pergunta-3]:
                resultado.append(3)
        if resultado == [1,3]:
            print('\n'+str(i)+ '. '+(carta - 3)+(carta-1) )
            opcao = int(input('Para qual das duas gostaria de movimentar?' ))
        

        def empilha(baralho,pergunta,destino):
            if resultado == [1]:
                destino = cartas[carta-1]
            if resultado == [1,3]:
                destino = cartas[opcao]
            baralho[destino] = baralho[pergunta]
            del(baralho[pergunta])
            return baralho
        return resultado

    def possui_movimentos_possiveis(baralho):
        sim = 0
        for i in range(0,len(baralho)-1):
            movimentos = lista_movimentos_possiveis(baralho,i)
            if movimentos == []:
                sim += 0
                perdeu = str(input('você perdeu, gostaria de começar de novo? '))
                if perdeu == 'sim':
                    
                else:
                    jogo = False
            else:
                sim += 1
        if sim != 0:
            return True
        else:
            return False