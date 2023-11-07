print("Sequência até zero")

pares = 0
impares = 0
num = 1

while num  != 0:
    num = int(input("Introduza um valor"))
    if num % 2==0:
        pares = pares = 1
    else:
        impares = impares + 1

print("O numero de pares introduzidos foi", pares)
print("O numero de impares introduzidos foi", impares)