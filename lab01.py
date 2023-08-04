escolha_sheila = input()   #Solicita-se as entradas para as escolhas de Sheila e Reginaldo
escolha_reginaldo = input()

if escolha_sheila == escolha_reginaldo:   #Seta as condições de empate
    print("empate")

if escolha_sheila == "tesoura" and escolha_reginaldo == "papel":   #Seta todas as possibilidades para vitória de Sheila, o que implica em "Interestelar" como saída e escreve tal saída
    print("Interestelar")
if escolha_sheila == "papel" and escolha_reginaldo == "pedra":
    print("Interestelar")
if escolha_sheila == "pedra" and escolha_reginaldo == "lagarto":
    print("Interestelar")
if escolha_sheila == "lagarto" and escolha_reginaldo == "spock":
    print("Interestelar")
if escolha_sheila == "spock" and escolha_reginaldo == "tesoura":
    print("Interestelar")
if escolha_sheila == "tesoura" and escolha_reginaldo == "lagarto":
    print("Interestelar")
if escolha_sheila == "lagarto" and escolha_reginaldo == "papel":
    print("Interestelar")
if escolha_sheila == "papel" and escolha_reginaldo == "spock":
    print("Interestelar")
if escolha_sheila == "spock" and escolha_reginaldo == "pedra":
    print("Interestelar")
if escolha_sheila == "pedra" and escolha_reginaldo == "tesoura":
    print("Interestelar")

if escolha_reginaldo == "tesoura" and escolha_sheila == "papel":   #Seta todas as possibilidades para vitória de Reginaldo, o que implica em "Jornada nas Estrelas" como saída e escreve tal saída
    print("Jornada nas Estrelas")
if escolha_reginaldo == "papel" and escolha_sheila == "pedra":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "pedra" and escolha_sheila == "lagarto":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "lagarto" and escolha_sheila == "spock":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "spock" and escolha_sheila == "tesoura":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "tesoura" and escolha_sheila == "lagarto":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "lagarto" and escolha_sheila == "papel":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "papel" and escolha_sheila == "spock":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "spock" and escolha_sheila == "pedra":
    print("Jornada nas Estrelas")
if escolha_reginaldo == "pedra" and escolha_sheila == "tesoura":
    print("Jornada nas Estrelas")
