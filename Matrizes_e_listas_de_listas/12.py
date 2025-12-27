# Faça uma função que, dada uma matriz, calcule e retorne a sua transposta. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

def funcao(mat):
    mat_result = []

    for i in range(len(mat[0])):
        linha = []
        for j in range(len(mat)):
            linha.append(mat[j][i])

        mat_result.append(linha)

    return mat_result

def imprimir(mat_result):
    for i in range(len(mat_result)):
        for j in range(len(mat_result)):
            print(f"{mat_result[i][j]}", end="")
"""
Matriz normal:
[-5   8  -3    6]
[-7   6   7   10]
[2    1  -8   -6]
[-1   8  -10  -7]

Matris transposta:
[-5  -7   2   1]
[ 8   6   1   8]
[-3   7  -8 -10]
[ 6  10  -6  -7]
"""




funcao(mat=[[-5, 8, -3, 6], [-7, 6, 7, 10], [2, 1, -8, -6], [-1, 8, -10, -7]])