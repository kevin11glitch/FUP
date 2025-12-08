# Faça um programa que preencha um vetor com 12 números reais aleatórios (uniformemente distribuídos no intervalo [-10, 10]), mostre esses números, e calcule a quantidade de números negativos e a soma dos números positivos desse vetor. A entrada para o programa é a semente dos números aleatórios.

import random
vetor = []
contador = 0
soma = 0

random.seed(int(input()))

for i in range(12):
    num = random.uniform(-10,10)
    vetor.append(num)

for num in vetor:
    if num < 0:
        contador += 1
    if num > 0:
        soma += num

print(contador)
print(f"{soma:.2f}")