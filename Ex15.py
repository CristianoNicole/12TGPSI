print("A média da turma")
num = int(input("Introduza o quantidades do alunos"))

soma = 0
posteste= 0
negteste = 0
postrab = 0
negtrab = 0

for i in range(1, num +1):
    teste = float(input("Introduza a nota do teste"))
    trab = float(input("Introduza a nota do trabalho"))
    soma = soma +(teste + trab)/2

if teste >= 9.5:
    posteste = posteste + 1
else:
    negteste = negteste + 1

if trab >= 9.5:
    postrab = postrab + 1
else:
    negtrab = negtrab + 1

print("A média da turma é", soma/num)

print("O Numero de positivas no teste são", posteste)
print("O Numero de negativas no teste são", negteste)
print("O Numero de positivas no trabalho são", postrab)
print("O Numero de negativas no tetrabalhoste são", negteste) 