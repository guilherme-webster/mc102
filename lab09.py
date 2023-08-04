from dataclasses import dataclass
 
@dataclass
class Robot:
    modo: int # 0 = escaneamento, 1 = limpando, 2 = retornar para o escaneamento, 3 = finalizar limpeza
    ult_pos_escan: list
    pos_atual: list[int]
    ult_pos_suja = list[int]
 
 
def le_linha(str):
    l = (str.split())
    return l
 
 
def le_matriz():
    n_linhas = int(input())
    m = []
    for i in range(n_linhas):
        linha = input()
        m.append(le_linha(linha))
    return m
 
 
def escreve_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha) - 1):
            print(linha[i], end=" ")
        print(linha[-1])
 
 
robo = Robot(modo = 0, ult_pos_escan = [0,0], pos_atual=[0,0])
 
 
def acha_sujeira(matriz):  # checa se ha sujeira na seguinte ordem: esquerda, cima, direita e baixo
    achou = False
    if robo.pos_atual[1] != 0 and matriz[robo.pos_atual[0]][robo.pos_atual[1]-1] == 'o':
        robo.ult_pos_suja = [robo.pos_atual[0],robo.pos_atual[1]-1]
        achou =  True
    elif robo.pos_atual[0] != 0 and matriz[robo.pos_atual[0]-1][robo.pos_atual[1]] == 'o':
        robo.ult_pos_suja = [robo.pos_atual[0] - 1,robo.pos_atual[1]]
        achou = True
    elif robo.pos_atual[1] != len(matriz[0]) - 1 and matriz[robo.pos_atual[0]][robo.pos_atual[1]+1] == 'o':
        robo.ult_pos_suja = [robo.pos_atual[0],robo.pos_atual[1] + 1]
        achou = True
    elif robo.pos_atual[0] != len(matriz) - 1 and matriz[robo.pos_atual[0]+1][robo.pos_atual[1]] == 'o':
        robo.ult_pos_suja = [robo.pos_atual[0] + 1,robo.pos_atual[1]]
        achou =  True
 
    if robo.modo == 0 or robo.modo == 1:
        if robo.ult_pos_suja == prox_pos_escan(matriz, robo.ult_pos_escan):
            robo.ult_pos_escan = robo.ult_pos_suja
 
    return achou
    
            
            
def troca_elemento_l_par(matriz):
    ac = matriz[robo.pos_atual[0]][robo.pos_atual[1]+1]
    matriz[robo.pos_atual[0]][robo.pos_atual[1]+1] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
    matriz[robo.pos_atual[0]][robo.pos_atual[1]] = ac
    robo.pos_atual[1] =  robo.pos_atual[1] + 1
 
 
def troca_elemento_l_impar(matriz):
    ac = matriz[robo.pos_atual[0]][robo.pos_atual[1]-1] 
    matriz[robo.pos_atual[0]][robo.pos_atual[1]-1] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
    matriz[robo.pos_atual[0]][robo.pos_atual[1]] = ac 
    robo.pos_atual[1] = robo.pos_atual[1] - 1
 
def escaneamento(matriz):
    prox_pos = prox_pos_escan(matriz, robo.pos_atual)
    matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
    robo.pos_atual = prox_pos.copy()
    robo.ult_pos_escan = robo.pos_atual.copy()
    matriz[robo.pos_atual[0]][robo.pos_atual[1]] = 'r'
 
 
def prox_pos_escan(matriz, p):
    if p[0] % 2 == 0:
        if p[1] != len(matriz[0]) -  1:
            return [p[0], p[1] + 1]
        else:
            return [p[0] + 1, p[1]]
    else:
        if p[1] != 0:
            return [p[0], p[1] - 1]
        else:
            return [p[0] + 1, p[1]]
 
 
def limpando(matriz):  # fazer o robo ir para a ultima pos escaneada(posicao suja)
    matriz[robo.ult_pos_suja[0]][robo.ult_pos_suja[1]] = 'r'
    matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
    robo.pos_atual = robo.ult_pos_suja.copy()
 
 
def retornar_ao_escaneamento(matriz):
    if robo.pos_atual[1] < robo.ult_pos_escan[1]:
        matriz[robo.pos_atual[0]][robo.pos_atual[1] + 1] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
        robo.pos_atual[1] = robo.pos_atual[1] + 1
    elif robo.pos_atual[0] < robo.ult_pos_escan[0]:
        matriz[robo.pos_atual[0] + 1][robo.pos_atual[1]] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
        robo.pos_atual[0] = robo.pos_atual[0] + 1
    elif robo.pos_atual[1] > robo.ult_pos_escan[1]:
        matriz[robo.pos_atual[0]][robo.pos_atual[1] - 1] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
        robo.pos_atual[1] = robo.pos_atual[1] - 1
    elif robo.pos_atual[0] > robo.ult_pos_escan[0]:
        matriz[robo.pos_atual[0] - 1][robo.pos_atual[1]] = matriz[robo.pos_atual[0]][robo.pos_atual[1]]
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
        robo.pos_atual[0] = robo.pos_atual[0] - 1
 
def finalizar_limpeza(matriz):
    while robo.pos_atual[1] < len(matriz[0]) - 1:
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = '.'
        robo.pos_atual[1] += 1
        matriz[robo.pos_atual[0]][robo.pos_atual[1]] = 'r'
        escreve_matriz(matriz)
        if robo.pos_atual[1] != len(matriz[0]) - 1:
            print()
 
            
 
matriz = le_matriz()
 
while True:
    escreve_matriz(matriz)
    print()
    if not acha_sujeira(matriz):
        if robo.ult_pos_escan == robo.pos_atual:
            robo.modo = 0
        elif robo.ult_pos_escan != robo.pos_atual:
            robo.modo = 2  
        if robo.modo == 0:
            escaneamento(matriz)
        if robo.modo == 2:
            retornar_ao_escaneamento(matriz)
        if robo.pos_atual[0] == len(matriz) - 1:
            if robo.pos_atual[0] % 2 == 0 and robo.pos_atual[1] == len(matriz[0]) - 1:
                escreve_matriz(matriz)
                break
            elif robo.pos_atual[0] % 2 != 0 and robo.pos_atual[1] == 0:
                escreve_matriz(matriz)
                print()
                finalizar_limpeza(matriz)
                break
    else:
        robo.modo = 1
        if robo.modo == 1:
            limpando(matriz)
 