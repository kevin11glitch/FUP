# Faça uma função que, dada uma matriz quadrada, calcule a soma dos elementos que estão abaixo da diagonal principal. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso. Para fazer a soma, utilize apenas comandos de repetição e não utilize expressões relacionais (comparações).


def funcao(mat):
    soma = 0

    for i in range(1, len(mat)):
        for j in range(0, i):
            soma += mat[i][j]
    return soma
"""
[-5   8  -3    6]
[-7   6   7   10]
[2    1  -8   -6]
[-1   8  -10  -7]

"""
funcao(mat=[[-5, 8, -3, 6], [-7, 6, 7, 10], [2, 1, -8, -6], [-1, 8, -10, -7]])