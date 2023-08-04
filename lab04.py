dias = int(input())     # Quantidade de dias analisados
x = 0
while x <= (dias): 
    procedimentos = []
    pares_brigas = []
    proced_anim = []
    anim_atend = []
    anim_atend_ndispo = []
    atend_n = []
    proced_num_int = []
    proced_nome = []
    proced_num_str = []
    p_b = ''
    p_a = ''
    brigas = 0
    q = 0 
    u = 0 
    z = 0 
    h = 1 
    g = 1 
    m = int(input())        # Quantidade de animais que brigaram    # 1 <= m <= 100
    for i in range(m):
        p_b += input() + ' '
    pares_brigas = p_b.split()
    p = input()     # String com os procedimentos disponíveis no dia e quantos deles estão disponíveis
    procedimentos = p.split()
    while z < (len(procedimentos) - 1):
        proced_nome.append(procedimentos[z])
        proced_num_str.append(procedimentos[z+1])
        z += 2
    for c in proced_num_str:
        proced_num_int.append(int(c))
    animais = int(input())
    for d in range(animais):
        p_a += input() + ' '     # String com o nome do animal mais o nome do procedimento
    proced_anim = p_a.split()
    while q < (len(pares_brigas) - 1):
        if pares_brigas[q] in proced_anim and pares_brigas[q+1] in proced_anim:
            brigas += 1
        q += 2
    for y in range(len(proced_anim)):
        for j in range(len(proced_nome)):
            if proced_anim[y] == proced_nome[j] and proced_num_int[j] > 0:
                anim_atend.append(proced_anim[y-1])
                proced_num_int[j] = proced_num_int[j] - 1
            elif proced_anim[y] == proced_nome[j] and proced_num_int[j] <= 0:
                anim_atend_ndispo.append(proced_anim[y-1])
    while u < (len(proced_anim)-1):
        if proced_anim[u+1] not in procedimentos:
            atend_n.append(proced_anim[u])
        u += 2
    
    print("Dia:",(x+1))
    print("Brigas:",brigas)
    if anim_atend != []:
        print("Animais atendidos:",anim_atend[0],end='')
        while h < len(anim_atend):
            print(',',anim_atend[h],end='')
            h += 1
        print()
    if anim_atend_ndispo != []:
        print("Animais não atendidos:",anim_atend_ndispo[0],end='')
        while g < len(anim_atend_ndispo):
            print(',',anim_atend_ndispo[g],end='')
            g += 1
        print()
    for t in atend_n:
        print("Animal",t,"solicitou procedimento não disponível.")
    x += 1
    print()