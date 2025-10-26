# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

num = int(input())
contador = 0

if num < 2:
    print("Nao primo")

else:
    for i in range(1, num+1):
        if (num % i) == 0:
            contador += 1
        
    if contador == 2:
        print("Primo")
    else:
        print("Nao primo")