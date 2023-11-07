print("Introduza o numero da turma")
num = int(input("Introduza o numero de alunos"))

soma = 0

for i in range(1, num +1):
    teste= float(input("Introduza a nota do teste"))
    trab = float(input("Introduza a nota do trab"))
    soma = soma + (teste + trab)/2

    print("A média da turma é ", soma/num)