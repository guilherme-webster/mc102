from math import floor

# M # dano max
# V # pontos de vida da maquina
# D == M − (|(cx − fx)| + |(cy − fy)|) # dano caso a flecha tenha o mesmo tipo de fraqueza da máquina, flecha indice em (fx, fy)
# D == (M − (|(cx − fx)| + |(cy − fy)|)) // 2 # dano caso o tipo de flecha n seja o da fraqueza

def list_u():
    """Cria um dicionario para uma maquina U, com seus dados"""
    dados = (input().split())    # linha com 3 ints: vida, ataq, partes
    for j in range(len(dados)):
        dados[j] = int(dados[j]) # j: 0 == P.V., 1 == P.A., 2 == PARTES
    return dados


def prop_partes(dic_maquina, dic_parte, dic_partes_aux,i): # cria um dicionario para uma maquina U, com dados das suas partes, 
    """Cria um dicionario para uma maquina U, com dados das suas partes"""
    for j in range(dic_maquina[i][2]):
        prop_parte = input().split(', ') # componente (parte do corpo), a sua fraqueza, o dano máximo e as coordenadas cx e cy
        dic_partes_aux[prop_parte[0]] = [prop_parte[1], int(prop_parte[2]), (int(prop_parte[3]), int(prop_parte[4]))]
    dic_parte[i] = dic_partes_aux
    return dic_parte


def dic_flechas_f(lista):
    """Cria um dicionário com os tipos de flechas como chaves e associa o número de flechas do respectivo tipo"""
    dic = {}
    for i in range(1, len(lista), 2):
        dic[lista[i - 1]] = int(lista[i])
    return dic

def dados_ataq(lista):
    """Cria uma lista com os dados do ataque"""
    dados_at = []
    dados_at.append(int(lista[0]))
    dados_at.append(lista[1])
    dados_at.append(lista[2])
    dados_at.append((int(lista[3]), int(lista[4])))
    return dados_at


def criticos(lista_at, dados_critico): # {m: {(x, y): int}}
    """Cria um dicionario com uma tupla (posição), como chave e associa o número de críticos acertados naquele ponto"""
    pos_at = lista_at[3]

    if pos_at in dados_critico.keys():
       dados_critico[pos_at] += 1
    else:
       dados_critico[pos_at] = 1
    return dados_critico


def ataq_func(lista_at, flech_uti, partes, maquinas, maq_derrotadas):
    """Calcula o dano e computa se a máquina morreu ou não"""
    alvo = lista_at[0]
    part_at = lista_at[1]
    flecha_at = lista_at[2]
    pos_at = lista_at[3]

    if flecha_at == partes[alvo][part_at][0] or partes[alvo][part_at][0] == 'todas':
        flech_uti[flecha_at] += 1
        dano = abs(partes[alvo][part_at][1] - (abs(partes[alvo][part_at][2][0] - pos_at[0]) + abs(partes[alvo][part_at][2][1] - pos_at[1])))
    else:
        flech_uti[flecha_at] += 1
        dano = abs(partes[alvo][part_at][1] - (abs(partes[alvo][part_at][2][0] - pos_at[0]) + abs(partes[alvo][part_at][2][1] - pos_at[1]))) // 2
    maquinas[alvo][0] -= dano

    if maquinas[alvo][0] <= 0:
        maq_derrotadas.append(lista_at[0])


def flech_uti(dicflechas):
    """Cria um dicionário para computar o número de flechas utilizadas naquele combate"""
    dic_flecha_uti = {}
    for k in dicflechas.keys():
        dic_flecha_uti[k] = 0
    return dic_flecha_uti

value = True
a_init = int(input()) # pontos de vida de Aloy
a = a_init
total_flechas = 0
flechas = input() # tipos e respectivos números de flechas
dic_flechas = dic_flechas_f(flechas.split())
flechas_n_muda = dic_flechas.copy()
for f in flechas_n_muda:
    total_flechas += flechas_n_muda[f]
n = int(input()) # número de máquinas a serem enfrentadas
maquinas_geral = {}
maquinas = {}
o = 0
combate = 0
flechas_counter = 0

while o < n and value:
    flechas_uti = flech_uti(dic_flechas)
    dados_critico = {}
    dic_parte = {}
    maq_derrotadas = []
    flechas_counter = 0
    lista_dic_criticos = []

    u = int(input()) # 1 <= U <= N, número máximo de máquinas a serem enfrentadas simultaneamente
    for i in range(u):
        dic_partes_aux = {}
        maquinas[i] = list_u() # cria um dicionario que guarda a maquina como chave e sua respectiva vida, ataque e quant. de partes
        partes = prop_partes(maquinas, dic_parte, dic_partes_aux, i) # cria um dicionario que guarda o nome da parte como chave e suas respectivas fraquezas, dano maximo e coordenadas
        maquinas_geral[i + o] = maquinas[i]
        lista_dic_criticos.append({})
    o += u

    while True:
        ataque = input().split(', ') # Aloy dispara três flechas seguidas antes de tomar o dano de todas as U máquinas
        lista_at = dados_ataq(ataque) # [0, olho, perfurante, (0, 10)], exemplo de dados de ataq
        ataq_func(lista_at, flechas_uti, partes, maquinas, maq_derrotadas)
        flechas_counter += 1
        if partes[lista_at[0]][lista_at[1]][2] == lista_at[3]:

            lista_dic_criticos[lista_at[0]] = criticos(lista_at, dados_critico)
        if flechas_counter % 3 == 0: # checar se maq morta e derrotadas estao funcionando e corrigir o problema com as flechas
            for maquinas_vivas in range(u):
                if maquinas[maquinas_vivas][0] > 0:
                    a -= maquinas[maquinas_vivas][1]

        if a > 0 and len(maq_derrotadas) == u: # checar o len(maq_derrotadas)
            print("Combate {}, vida = {}".format(combate, a_init))
            if maq_derrotadas != []:
                for d in maq_derrotadas:
                    print("Máquina {} derrotada".format(d))
            print("Vida após o combate =", a)
            print("Flechas utilizadas:")
            for k in dic_flechas:
                if flechas_uti[k] != 0:
                    print('- {}: {}/{}'.format(k, flechas_uti[k], flechas_n_muda[k]))
            if dados_critico != {}:
                print("Críticos acertados:")
                for j in range(len(lista_dic_criticos)):
                    if lista_dic_criticos[j] != {}:
                        print('Máquina {}:'.format(j))
                        for c in dados_critico.keys():
                                print('- {}: {}x'.format(c, dados_critico[c]))
            if o == n:
                print("Aloy provou seu valor e voltou para sua tribo.")
                value = False
                break
            combate += 1
            a += floor(0.5 * a_init)
            if a > a_init:
                a = a_init
            a_init = a
            break
        if a <= 0:
            print("Combate {}, vida = {}".format(combate, a_init))
            if maq_derrotadas != []:
                for d in maq_derrotadas:
                    print("Máquina {} derrotada".format(d))
            print("Vida após o combate = 0")
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            value = False
            break
        if flechas_counter == total_flechas and len(maq_derrotadas) != u:
            print("Combate {}, vida = {}".format(combate, a_init))
            if maq_derrotadas != []:
                for d in maq_derrotadas:
                    print("Máquina {} derrotada".format(d))
            print("Vida após o combate =", a)
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
            value = False
            break