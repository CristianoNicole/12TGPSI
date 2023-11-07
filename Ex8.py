print("Média e aprovação")
teste= float (input("Introduza a nota do teste"))
trab= float (input("Introduza a nota do trabalho"))

med = teste*0.60 + trab * 0.40

if med >= 9.5:
    print("A média é", "está aprovado")
else:
    print("A média é", "está reprovado")