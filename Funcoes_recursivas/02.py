# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro n.

def funcao(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * funcao(x-1)