import random

print("Lista de 20 valores com soma Pares ou Impares")

lista = [random.radint(0,100) for _ in range(20)]

pares = 0
impares = 0

for valor in lista:
    if valor % 2 == 0:
        pares = pares + valor 
    else:
        impares = impares + valor 
    
print("Lista de Valores")
print(lista)

print("Soma dos Pares é", pares)
print("Soma dos Impares é",impares)
