def buscabinaria(lista, rank):
    """Procura o primeiro elemento de um dado rank (letra/número) na lista e devolve seu índice"""
    rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    e = 0
    d = len(lista) - 1
    while e <= d:
        m = (e + d) // 2
        str = lista[m][:-1]
        if lista[m][:-1] == rank:
            return m
        if rank_order[str] > rank_order[rank]:
            e = m + 1
        else:
            d = m - 1
    return None

def sort_cartas(cartas):
    """Ordena as cartas"""
    rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    naipe_order = {'O': 1, 'E': 2, 'C': 3, 'P': 4}
    
    def card_key(carta):
        rank = carta[:-1]
        naipe = carta[-1]
        return (rank_order[rank], naipe_order[naipe])
    
    n = len(cartas)
    for i in range(n):
        for j in range(0, n-i-1):
            if card_key(cartas[j]) < card_key(cartas[j+1]):
                cartas[j], cartas[j+1] = cartas[j+1], cartas[j]
    
    return cartas


def find_prox_jogador(jogador_atual, n):
    """Seta o próximo jogador"""
    if jogador_atual == n:
        prox_jogador = 1
    else:
        prox_jogador = jogador_atual + 1

    return prox_jogador


def jogada(dic_maos, pilha_prov, atual_jogador, idx):
    """Realiza os passos de uma jogada"""
    pilha_prov.append(dic_maos[atual_jogador][idx])
    pilha_prov = sort_cartas(pilha_prov)
    pilha_prov.reverse()
    dic_maos[atual_jogador].pop(idx)


def find_novo_rank(mao, menor_rank, blefou):
    """Procura o novo rank, caso o jogador não tenha cartas do rank atual e seta se ele blefa ou não"""
    rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    menor = mao[-1][:-1]
    idx = len(mao) - 1

    while True:
        if rank_order[mao[idx][:-1]] >= rank_order[menor_rank]:
            blefou = False
            return [mao[idx][:-1], blefou]
    
        if idx == 0:
            blefou = True
            return [menor, blefou]
        
        idx -= 1


def print_jogadores(dic_maos):
    """Printa os jogadores"""
    for jogador in range(1, j + 1):
        print("Jogador {}".format(jogador))
        print("Mão:", end=(''))
        if dic_maos[jogador] != []:
            for carta in dic_maos[jogador][:-1]:
                print(' {}'.format(carta), end='')
            print(' {}'.format(dic_maos[jogador][-1]))
        else:
            print()

def print_pilha(pilha):
    """Printa a pilha"""
    print("Pilha:", end='')
    if pilha != []:
        for carta in pilha[:-1]:
            print(' {}'.format(carta), end='')
        print(' {}'.format(pilha[-1]))
    else:
        print()


j = int(input()) # j jogadores
dic_maos = {}
for jogador in range(j):
    cartas = input().split(', ') # mão inicial do j'ésimo jogador
    dic_maos[jogador + 1] = sort_cartas(cartas)
n = int(input()) # quantas jogadas serão efetuadas até o primeiro duvido
prox_jogador = 2
atual_jogador = 1
ganhou = False

while not ganhou:
    duvido = False
    blefou = False
    pilha = []
    pilha_prov = []
    counter = 0
    menor_rank = (dic_maos[atual_jogador][-1][:-1])

    print_jogadores(dic_maos)
    print_pilha(pilha)

    while not duvido:
        cartas_jogadas = 0
        for _ in range(len(dic_maos[atual_jogador])): # itera sobre a lista, de modo que a função buscabinaria vá retornando cartas do rank
            idx = buscabinaria(dic_maos[atual_jogador], menor_rank)
            if idx != None:
                jogada(dic_maos, pilha_prov, atual_jogador, idx)
                cartas_jogadas += 1
            else:
                if cartas_jogadas == 0: # analisa se não teve jogada porque acabaram cartas daquele rank ou se elas nem exisitiam na mao do jogador
                    lista_rank_blefou = find_novo_rank(dic_maos[atual_jogador], menor_rank, blefou)
                    rank_prov = lista_rank_blefou[0]
                    blefou = lista_rank_blefou[1]
                    if not blefou:
                        menor_rank = rank_prov
                        for _ in range(len(dic_maos[atual_jogador])):
                            idx = buscabinaria(dic_maos[atual_jogador], menor_rank)
                            if idx != None:
                                jogada(dic_maos, pilha_prov, atual_jogador, idx)
                                cartas_jogadas += 1
                    else:
                        novo_menor_rank = rank_prov
                        for _ in range(len(dic_maos[atual_jogador])):
                            idx = buscabinaria(dic_maos[atual_jogador], novo_menor_rank)
                            if idx != None:
                                jogada(dic_maos, pilha_prov, atual_jogador, idx)
                                cartas_jogadas += 1

        pilha += pilha_prov
        pilha_prov = []

        print("[Jogador {}] {} carta(s) {}".format(atual_jogador, cartas_jogadas, menor_rank)) 
        print_pilha(pilha)

        counter += 1
        prox_jogador = find_prox_jogador(atual_jogador, j)
        if counter == n:
            duvido = True
            if blefou:
                dic_maos[atual_jogador] += pilha
                dic_maos[atual_jogador] = sort_cartas(dic_maos[atual_jogador])
            else:
                dic_maos[prox_jogador] += pilha
                dic_maos[prox_jogador] = sort_cartas(dic_maos[prox_jogador])
            pilha = []
            print("Jogador {} duvidou.".format(prox_jogador))

        if dic_maos[atual_jogador] == []:
            if duvido == True:
                print_jogadores(dic_maos)
                print_pilha(pilha)
            print("Jogador {} é o vencedor!".format(atual_jogador))
            ganhou = True
            break

        atual_jogador = prox_jogador
