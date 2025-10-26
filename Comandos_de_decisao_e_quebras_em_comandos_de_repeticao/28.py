# Faça um algoritmo que leia um número inteiro e imprima seus divisores.

num = int(input())

for i in range(1, num+1):    
    if (num % i) == 0:
        print(i)
    False
