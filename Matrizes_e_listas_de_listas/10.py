# Faça uma função que, dada uma matriz quadrada, calcule a soma dos elementos que estão na diagonal principal. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso. Para fazer a soma, utilize apenas um comando de repetição e não utilize expressões relacionais (comparações).

def funcao(mat):
    soma  = 0

    for i in range(0, len(mat)):
        for j in range(i, i+1):
            soma += mat[i][j]
    return soma

"""
[-5   8  -3    6]
[-7   6   7   10]
[2    1  -8   -6]
[-1   8  -10  -7]

"""
funcao(mat=[[-5, 8, -3, 6], [-7, 6, 7, 10], [2, 1, -8, -6], [-1, 8, -10, -7]])