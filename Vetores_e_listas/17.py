# Faça uma função que receba um vetor e um número inteiro x e retorne os múltiplos do número x que existem no vetor.

def funcao(vetor, x):
    mult = []

    for i in vetor:
        if i % x == 0:
            mult.append(i)
    
    return mult

vetor = [10, 9, 8, 7, 6, 6, 7, 8, 9, 6]

x = 3

funcao(vetor, x)

