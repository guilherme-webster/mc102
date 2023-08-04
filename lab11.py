from dataclasses import dataclass

@dataclass 
class Personagem: 
    vida: int
    dano: int
    pos_init: tuple
    pos_atual: list
    pos_saida: tuple

    def anda_p_l_impar(matriz, self):
        ac = matriz[self.pos_atual[0]][self.pos_atual[1] + 1]
        matriz[self.pos_atual[0]][self.pos_atual[1] + 1] = matriz[self.pos_atual[0]][self.pos_atual[1]]
        matriz[self.pos_atual[0]][self.pos_atual[1]] = '.'
        self.pos_atual[1] = self.pos_atual[1] + 1


    def anda_p_l_par(matriz, self):
        ac = matriz[self.pos_atual[0]][self.pos_atual[1] - 1]  
        matriz[self.pos_atual[0]][self.pos_atual[1] - 1] = matriz[self.pos_atual[0]][self.pos_atual[1]]
        matriz[self.pos_atual[0]][self.pos_atual[1]] = '.' # ou seria '.'?
        self.pos_atual[1] = self.pos_atual[1] - 1



@dataclass
class Monstro:
    id: int
    vida: int
    dano: int
    tipo: str # U, D, L, R 
    pos_init: tuple
    pos_atual: list


@dataclass
class Objeto:
    tipo: str
    pos: tuple
    stts: int
   

def acha_dados_p():
    str = input().split()
    dado1 = int(str[0])
    dado2 = int(str[1])
    return [dado1, dado2]

def acha_pos():
    pos_p = list(input())
    return (int(pos_p[0]), int(pos_p[2]))

def cria_monstro(n, dic_monstro): 
    info_monstro = input().split() # ['100', '5', 'U', '1,0']
    vida_monstro = int(info_monstro[0])
    ataq_monstro = int(info_monstro[1])
    tipo_monstro = info_monstro[2]
    pos_monstro_aux = list(info_monstro[3])
    pos_monstro_init = (int(pos_monstro_aux[0]), int(pos_monstro_aux[2]))
    # monstro = Monstro(id = n, vida = vida_monstro, dano = ataq_monstro, tipo = tipo_monstro, pos_init = pos_monstro, pos_atual = list(pos_monstro))
    dic_monstro[n] = [vida_monstro, ataq_monstro, tipo_monstro, pos_monstro_init, list(pos_monstro_init)]


def info_obj_func(n): 
    dic_objetos_func = {}
    for objeto in range(n):
        info_obj= input().split() # ['joia', 'd', '1,2', '-1']
        nome_obj = info_obj[0]
        tipo_obj = info_obj[1]
        pos_obj_aux = list(info_obj[2])
        pos_obj = (int(pos_obj_aux[0]), int(pos_obj_aux[2]))
        stts_obj = int(info_obj[3])
        dic_objetos_func[nome_obj] = [tipo_obj, pos_obj, stts_obj]
    return dic_objetos_func


def constroi_matriz(n,m, matriz, pos_p,dic_monstros, dic_objs, pos_saida):
    if matriz == []:
        for l in range(n):
            linha = []
            for c in range(m):
                linha.append('.')
            matriz.append(linha)
    matriz[pos_p[0]][pos_p[1]] = 'P'
    for k in dic_monstros.keys():
        matriz[dic_monstros[k][3][0]][dic_monstros[k][3][1]] = dic_monstros[k][2]
    for o in dic_objs.keys():
        matriz[dic_objs[o][1][0]][dic_objs[o][1][1]] = dic_objs[o][0]
    matriz[pos_saida[0]][pos_saida[1]] = '*'
    
    return matriz


def escreve_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha) - 1):
            print(linha[i], end=" ")
        print(linha[-1])


def escreve_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha) - 1):
            print(linha[i], end=" ")
        print(linha[-1])        


def anda_p_l_impar(matriz, self):
        ac = matriz[self.pos_atual[0]][self.pos_atual[1] + 1]
        matriz[self.pos_atual[0]][self.pos_atual[1] + 1] = matriz[self.pos_atual[0]][self.pos_atual[1]]
        matriz[self.pos_atual[0]][self.pos_atual[1]] = '.'
        self.pos_atual[1] = self.pos_atual[1] + 1


def anda_p_l_par(matriz, self):
    ac = matriz[self.pos_atual[0]][self.pos_atual[1] - 1]  
    matriz[self.pos_atual[0]][self.pos_atual[1] - 1] = matriz[self.pos_atual[0]][self.pos_atual[1]]
    matriz[self.pos_atual[0]][self.pos_atual[1]] = '.' # ou seria '.'?
    self.pos_atual[1] = self.pos_atual[1] - 1

def p_desce(matriz, self):
    ac = matriz[self.pos_atual[0] + 1][self.pos_atual[1]]
    matriz[self.pos_atual[0] + 1][self.pos_atual[1]] = matriz[self.pos_atual[0]][self.pos_atual[1]]
    matriz[self.pos_atual[0]][self.pos_atual[1]] = '.'
    self.pos_atual[0] = self.pos_atual[0] + 1


def p_sobe(matriz, self):
    ac = matriz[self.pos_atual[0] - 1][self.pos_atual[1]]
    matriz[self.pos_atual[0] - 1][self.pos_atual[1]] = matriz[self.pos_atual[0]][self.pos_atual[1]]
    matriz[self.pos_atual[0]][self.pos_atual[1]] = '.'
    self.pos_atual[0] = self.pos_atual[0] - 1


lista_vida_dano = acha_dados_p()
vp = int(lista_vida_dano[0]) # vida inicial
dp = int(lista_vida_dano[1]) # dano inicial

lista_dimensao_mapa = acha_dados_p()
n_linhas = (lista_dimensao_mapa[0]) # n linhas
m_colunas = (lista_dimensao_mapa[1]) # m colunas

pos_p_init = acha_pos() # pos_p_init[0] == ix e pos_p_init[1] == iy (pos inicial da personagem)
pos_f_p = acha_pos() # saída da masmorra

p = Personagem(vida = vp, dano = dp, pos_init = pos_p_init, pos_atual = list(pos_p_init), pos_saida = pos_f_p)

n_monstros = int(input()) # numero de monstros no mapa
# lista_monstros = []
dic_monstro = {}
for i in range(n_monstros):
    cria_monstro(i, dic_monstro)
    # monstro.{i} = dic_monstro[1]
    # lista_monstros.append(m)

n_objetos = int(input())
lista_objetos = []
dic_objetos = info_obj_func(n_objetos)
# for objeto in dic_objetos.keys():
#     objeto = Objeto(tipo = dic_objetos[objeto][0], pos = dic_objetos[objeto][1], stts = dic_objetos[objeto[2]])
#     lista_objetos.append(objeto)

desceu_tudo = False
matriz = constroi_matriz(n_linhas, m_colunas, [], p.pos_atual, dic_monstro, dic_objetos, pos_f_p)
while not desceu_tudo:
    escreve_matriz(matriz)
    p_desce(matriz, p)
    if p.pos_atual[0] == n_linhas - 1:
        desceu_tudo = True

while p.pos_atual != list(p.pos_saida):
    escreve_matriz(matriz)
    if (p.pos_atual[0] % 2) == 0:
        if p.pos_atual[1] - 1 >= 0:
            anda_p_l_par(matriz, p)
        else:
            if p.pos_atual[0] != 0:
                p_sobe(matriz, p)
            else:
                break
    else:
        if p.pos_atual[1] + 1 <= m_colunas - 1:
            anda_p_l_impar(matriz, p)
        else:
            if p.pos_atual[0] != 0:
                p_sobe(matriz, p)
            else:
                break
escreve_matriz(matriz)
