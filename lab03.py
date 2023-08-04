j = int(input())  # 2 <= x <= 20
i = 0
u = 0
o = 0
p = 0
t = 0
q = 0
jogadores = []
pontuacao = []
pontuacao_vencedor = 0
vencedor = 0
ji = input()  # 1 <= ji <= 200
numeros = ji.split()
lr = input()
intervalos = lr.split()

while t < j:
    jogadores.append(t+1)
    t += 1
while i < len(numeros):
    numeros[i] = int(numeros[i])
    i += 1
while u < len(intervalos):
    intervalos[u] = int(intervalos[u])
    u += 1

while o < j:
    if j % 2 == 0:
        if o < j/2:
            pontuacao.append((intervalos[q+1] - intervalos[q]) * numeros[o])
        else:
            pontuacao.append((intervalos[q+1] - intervalos[q]) + numeros[o])
    else:
        if o < j/2 and o < j/2 + 1:
            pontuacao.append((intervalos[q+1] - intervalos[q]) * numeros[o])
        else:
            pontuacao.append((intervalos[q+1] - intervalos[q]) + numeros[o])
    o += 1
    q += 2

while p < j:
    if pontuacao[p] > pontuacao_vencedor:
        vencedor = jogadores[p]
        pontuacao_vencedor = pontuacao[p]
    elif pontuacao[p] == pontuacao_vencedor:
        vencedor = 0
    p += 1

if vencedor == 0:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print("O jogador número",vencedor,"vai receber o melhor bolo da cidade pois venceu com", pontuacao_vencedor,"ponto(s)!")
