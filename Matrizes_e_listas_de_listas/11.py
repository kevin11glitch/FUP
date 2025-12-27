# Faça uma função que, dada uma matriz quadrada, calcule a soma dos elementos que estão na diagonal secundária. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso. Para fazer a soma, utilize apenas comandos de repetição e não utilize expressões relacionais (comparações).

def funcao(mat):
    soma  = 0

    for linha in range(0, len(mat)):
        col = len(mat) - 1 - linha
        soma += mat[linha][col]

    return soma

"""
[-5   8  -3    6]
[-7   6   7   10]
[2    1  -8   -6]
[-1   8  -10  -7]

"""

funcao(mat=[[-5, 8, -3, 6], [-7, 6, 7, 10], [2, 1, -8, -6], [-1, 8, -10, -7]])