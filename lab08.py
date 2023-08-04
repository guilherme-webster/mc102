def acha_cat_nota(categoria_simples, l_dados):
    lista_cat = []
    for i1 in l_dados:
        if categoria_simples in i1:
            lista_cat.append(i1[2:])  # acha o par filme nota para uma dada categoria simples
    return lista_cat


def num_aval(l_cat):
    c = 0
    d = {}
    for p1 in l_cat:
        d[p1[0]] = 0
    for p2 in l_cat:
        d[p2[0]] += 1
    return d


def acha_media(l_c):
    d_filme_soma = {}
    d_filme_counter = {}
    d_filme_media = {}
    for p3 in l_c:
        d_filme_soma[p3[0]] = 0
        d_filme_counter[p3[0]] = 0
    for p4 in l_c:
        d_filme_soma[p4[0]] += int(p4[1])
        d_filme_counter[p4[0]] += 1   
    for p5 in l_c:
        d_filme_media[p5[0]] = (d_filme_soma[p5[0]] / d_filme_counter[p5[0]])
    return d_filme_media


def acha_maior(categoria_simples, l_dados):
    """Dado um dicionário com os filmes e suas médias referentes a uma dada categoria, acha-se que filme tem a maior média"""
    par_filme_nota = acha_cat_nota(categoria_simples, l_dados)
    par_filme_media = acha_media(par_filme_nota)
    chave = list(par_filme_media)
    vencedor = chave[0]
    for k1 in par_filme_media.keys():
        if par_filme_media[k1] > par_filme_media[vencedor]:
            vencedor = k1
        elif par_filme_media[k1] == par_filme_media[vencedor]:
            avaliacoes = num_aval(par_filme_nota)
            if avaliacoes[k1] > avaliacoes[vencedor]:
                vencedor = k1
    lista_filme_media = [vencedor, par_filme_media[vencedor]]
    return lista_filme_media
    

def acha_vencedor_cat(categoria, dados):
    lista_filme_media_vencedor = acha_maior(categoria, dados)
    return(lista_filme_media_vencedor[0])


def acha_vencedor_cat2(categoria, dados):
    lista_filme_media_vencedor = acha_maior(categoria, dados)
    return lista_filme_media_vencedor


def filme_vence_n(d):
    vence_n = {}
    vence_media = {}
    vence_n_media = {}
    for p6 in d.values():
        vence_n[p6[0]] = 0
        vence_media[p6[0]] = 0
    for k2 in d.keys():
        vence_n[d[k2][0]] += 1
        vence_media[d[k2][0]] = d[k2][1]
    for o in vence_n.keys():
        vence_n_media[o] = [vence_n[o], vence_media[o]]
    return vence_n_media


def acha_pior_filme(d):
    chave = list(d)
    vencedor = chave[0]
    for k3 in d.keys():
        if d[k3][0] > d[vencedor][0]:
            vencedor = k3
        elif d[k3][0] == d[vencedor][0]:
            if d[k3][1] > d[vencedor][1]:
                vencedor = k3
    return vencedor


def acha_lista_avaliados(l_film, l_dad):
    lista_a = []
    for m in l_film:
        for n in l_dad:
            if m in n[2] and m not in lista_a:
                lista_a.append(m)
    return lista_a


def acha_n_merecia(l_film, l_dad):
    filmes_n_avaliados = l_film.copy()
    lista_avaliados = acha_lista_avaliados(lista_filmes, lista_dados)
    for i2 in lista_avaliados:
        if i2 in filmes_n_avaliados:
            filmes_n_avaliados.remove(i2)
    if filmes_n_avaliados == []:
        print('- sem ganhadores')
    else:
        resultado = (filmes_n_avaliados)
        if len(filmes_n_avaliados) > 1:
            for j1 in resultado[:len(resultado)-1]:
                print('-',j1, end=', ')
                print(resultado[-1])
        else:
            print('-',filmes_n_avaliados[0])

f = int(input())  # quantidade de filmes indicados 
lista_filmes = []
lista_dados = []
lista_dados_sem_escopo = []
lista_categorias_simples = ['filme que causou mais bocejos', 'filme que foi mais pausado', 'filme que mais revirou olhos', 'filme que não gerou discussão nas redes sociais', 'enredo mais sem noção']
d_cat_ven_med = {}


for i3 in range(f):
    filme = input()  # f linhas cada uma com um filme
    lista_filmes.append(filme)

q = int(input())  # número de 1 a 10

for p8 in range(q):
    dados = input()  # q linhas cada uma com os seguintes dados: avaliador, nome da categoria, nome do filme, nota
    lista_dados.append(dados.split(', '))


print('#### abacaxi de ouro ####')
print()
print('categorias simples')
for c1 in lista_categorias_simples:
    print('categoria:', c1)
    print('-',acha_vencedor_cat(c1, lista_dados))
    d_cat_ven_med[c1] = acha_vencedor_cat2(c1, lista_dados)
print()
print('categorias especiais')
print('prêmio pior filme do ano')
print('-',acha_pior_filme(filme_vence_n(d_cat_ven_med)))
print('prêmio não merecia estar aqui')
acha_n_merecia(lista_filmes, lista_dados)
