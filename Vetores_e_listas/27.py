# Faça uma função que receba um vetor posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. No final, retorne o vetor compacto.

def funcao(vetor):
    vetor_compacto = []

    for i in vetor:
        if i != 0:
            vetor_compacto.append(i)
            
    return vetor_compacto

funcao(vetor=[1, 0, 2, 0, 0, 3, 0, 4, 5, 5])