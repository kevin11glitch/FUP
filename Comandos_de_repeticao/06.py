# Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.

n = int(input())
soma = 0

for i in range(1, n+1):
    soma += i

print(soma)