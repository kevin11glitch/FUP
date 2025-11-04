# Faça uma função recursiva que receba um número inteiro positivo par n e imprima todos os números pares de 0 até n em ordem crescente.

def funcao(x):
    if (x % 2) != 0:
        return x
    if x == 0:
        print(0)
    else:
        funcao(x-2)
        print(x)