def str_lista(s):
    """Dada uma string, tranforma-a em uma lista
"""
    l = []
    for i1 in (s):
        l.append(i1)
    return(l)

def lista_str(l):
    """Dada uma lista, transforma-a em uma string
    """
    s = ''
    for d in l:
        s += d
    return s

def transpor_genoma(g, i, j, k):
    """Transpor o genoma atual considerando os índices i, j, k, isto é, trocar a
posição da subsequência iniciada em i e terminada em j com a subsequência iniciada
em j + 1 e terminada em k.
"""
    try:
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for m1 in range(i, j+1):
            l1.append(g[m1])
        for p in range(j+1, k+1):
            l2.append(g[p])
        for m2 in range(0,i):
            l3.append(g[m2])
        for m3 in range(k+1,len(g)):
            l4.append(g[m3])
        return l3 + l2 + l1 + l4
    except IndexError:
        if i > len(g) or j > len(g):
            return g
        elif k > len(g):
            k = len(g)
            l1 = []
            l2 = []
            l3 = []
            for m1 in range(i, j+1):
                l1.append(g[m1])
            for p in range(j+1, len(g)):
                l2.append(g[p])
            for m2 in range(0,i):
                l3.append(g[m2])
            l4 = []
            return l3 + l2 + l1 + l4

def combina_genoma(g,y,i):
    """Combinar o genoma atual com um novo genoma informado, inserindo esse
na i-ésima posição do atual.
"""
    l1 = []
    l2 = []
    for n in range(0,i):
        l1.append(g[n])
    for a in range(i,len(g)):
        l2.append(g[a])
    l1 += y
    l1 += l2
    g = l1
    return g
    

def concatena_genoma(l,s):
    """Adicionar ao final do genoma atual um novo genoma informado.
"""
    g = l + s
    return g

def remove_genoma(g,i,j):
    """Remover a subsequência [i, j] do genoma atual considerando dois índices i e j
informados.
"""
    try:
        l1 = []
        l2 = []
        for c in range(0,i):
            l1.append(g[c])
        for a in range(j+1,len(g)):
            l2.append(g[a])
        l1 += l2
        g = l1
        return g
    except IndexError:
        if i > len(g):
            pass

def busca_genoma(g,b):
    """Dado um genoma de busca, exibir na tela o número de vezes em que ele
ocorre no genoma atual.
"""
    print(g.count(b))

def busca_bidirecional(g,b):
    """Dado um genoma de interesse, buscar quantas vezes ele ocorre
no genoma atual ou em sua reversão. O genoma atual não deve sofrer alterações.
"""
    l = str_lista(b)
    l = reverte_genoma(l, 0, len(l)-1)
    l = lista_str(l)
    print(g.count(b) + g.count(l))

def reverte_genoma(g, i, j):
    """Dado os índices i e j, reverter a subsequência [i, j] (de i até j, inclusive) do
genoma atual.
"""
    try:
        l = []
        for q in range(j, i-1,-1):
            l.append(g[q])
        return combina_genoma(remove_genoma(g,i,j),l,i)
    except IndexError:
        if i > len(g):
            return g
        elif j > len(g):
            q = 0
            l = []
        for q in range(len(g)-1, i-1,-1):
            l.append(g[q])
        return combina_genoma(remove_genoma(g,i,j),l,i)

def transpor_e_reverter_genoma(g, i, j, k):
   """Transpor o genoma considerando os índices i, j, k e, em seguida,
o reverter considerando os índices i e k.
"""
   m = (transpor_genoma(g,i,j,k))
   g = reverte_genoma(m,i,k)
   return g

def mostrar(g):
    """Dado um genoma, printa ele na tela
"""
    print(g)

str_genoma = input()
list_genoma = str_lista(str_genoma)

while True:
    comando = input()
    comando_dados = comando.split()
    if comando_dados[0] == 'reverter':
        i = int(comando_dados[1])
        j = int(comando_dados[2])
        novo_genoma = reverte_genoma(list_genoma,i,j)
        list_genoma = novo_genoma
    elif comando_dados[0] == 'transpor':
        i = int(comando_dados[1])
        j = int(comando_dados[2])
        k = int(comando_dados[3])
        novo_genoma = transpor_genoma(list_genoma,i,j,k)
        list_genoma = novo_genoma
    elif comando_dados[0] == 'combinar':
        y = comando_dados[1]
        i = int(comando_dados[2])
        novo_genoma = combina_genoma(list_genoma,str_lista(y),i)
        list_genoma = novo_genoma
    elif comando_dados[0] == 'concatenar':
        y = comando_dados[1]
        novo_genoma = concatena_genoma(list_genoma,str_lista(y))
        list_genoma = novo_genoma
    elif comando_dados[0] == 'remover':
        i = int(comando_dados[1])
        j = int(comando_dados[2])
        novo_genoma = remove_genoma(list_genoma,i,j)
        list_genoma = novo_genoma
    elif comando_dados[0] == 'transpor_e_reverter':
        i = int(comando_dados[1])
        j = int(comando_dados[2])
        k = int(comando_dados[3])
        novo_genoma = transpor_e_reverter_genoma(list_genoma,i,j,k)
        list_genoma = novo_genoma
    elif comando_dados[0] == 'buscar':
        y = comando_dados[1]
        busca_genoma(lista_str(list_genoma),y)
    elif comando_dados[0] == 'buscar_bidirecional':
        y = comando_dados[1]
        busca_bidirecional(lista_str(list_genoma),y)
    elif comando_dados[0] == 'mostrar':
        mostrar(lista_str(list_genoma))
    elif comando_dados[0] == 'sair':
        break
