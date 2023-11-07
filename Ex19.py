print("String e Conta vogais")

texto = input("Introduza uma palavra")

vogais = "AEIOU/aeiou"

cont = 0

for letra in texto:
    if letra in vogais:
        cont = cont + 1

print("A palavra contem",cont,"vogais")