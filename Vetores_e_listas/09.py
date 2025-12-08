# Faça um programa que receba do usuário um vetor com 10 inteiros. Em seguida deverá ser mostrado na tela o maior e o menor valor desse vetor.

vetor = []


for i in range(10):
    num = int(input())
    vetor.append(num)
    
maior = vetor[0]
menor = vetor[0]

for num in vetor:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
print(maior)
print(menor)