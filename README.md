# 12TGPSI
Nunca olhes para baixo olha sempre em frente sempre em frente

from datetime import datetime

print("Idade")

datanasc = input("Introduza a data de nascimento (YYYY-MM-DD): ")
datanasc = datetime.strptime(datanasc, '%Y-%m-%d')

dataatual = datetime.now()

diferenca = dataatual - datanasc

anos = diferenca.days // 365

print("Idade =", anos, "anos")
