# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem decrescente.

def funcao(x):
    if x == 0:
        print(0)
    else:
        print(x)
        funcao(x-1)