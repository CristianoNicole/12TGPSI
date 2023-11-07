print("Quantas vogais e consoantes")

frase = input("Digite uma frase")

vogais = 0
consoantes = 0

for letra in frase:
    if letra.isalpha():
        if letra.lower() in 'aeiou':
            vogais = vogais + 1
    else:
        consoantes=consoantes + 1

print("vogais tem", vogais, "e consoantes tem", consoantes)



    