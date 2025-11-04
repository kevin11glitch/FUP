# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem crescente.

def funcao(x):
    if x == 0:
        print(0)
    else:
        funcao(x-1)
        print(x)