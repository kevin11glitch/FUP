# Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, se sim escreva esses valores na tela. Não utilize contadores.

vetor = []
vetor2 = []

for i in range(10):
    num = int(input())
    vetor.append(num)
    
for i in range(10):
    for j in range(i + 1, 10):
        if vetor[i] == vetor[j]:
            vetor2.append(vetor[i])

for num in vetor2:
    print(num)