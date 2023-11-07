import random 

print("Jogo Advinha Número em 3 Tentativas")

numero = random.randint(1,5)
tentativas = 3
    
print("Tenta adivinhar o numero em 3 tentativas")

for tentativas in range(tentativas):
    palpite = int(input("Qual o palpite"))

    if palpite == numero:
        print("Ganhou")
        break
    else:
        if palpite < numero:
            print("O Palpite é Maior")
        else:
            print("O Palpite é Menor")