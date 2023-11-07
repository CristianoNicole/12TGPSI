print("String com nome e apelido")

nomecompleto = str(input("Introduza o nome completo"))

primeiro = nomecompleto.split()[0]
apelido =  nomecompleto.split()[-1]

print("O primeiro nome é", primeiro,"é o apelidado é", apelido)