# Faça uma função que leia duas matrizes A e B de tamanhos p × q e q × r, respectivamente. Calcule e retorne a matriz C = A * B. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.


def funcao(mat1, mat2):
    mat3 = []

    for i in range(len(mat1)):
        
        linha = []
        for j in range(len(mat2[0])):
            elemento = 0
            for k in range(len(mat1[0])):
                elemento += mat1[i][k] * mat2[k][j]
            linha.append(elemento)
        mat3.append(linha)

    return mat3


def imprimir(mat3):
    for i in range(len(mat3)):
        for j in range(len(mat3)):
            print(f"{mat3[i][j]}", end="")

funcao(mat1=[
    [ 0,  5, -10, -4,  6],
    [ 1,  9, -10, -3, -4],
    [ 3, -2,  -6,  5, -9],
    [-9, -8, -10, -7,  4],
    [ 6, -3,  -4, -7,  8]
], mat2=[
    [ 4, -8, -9,  6,  0],
    [-5, -8, -7,  1,  3],
    [ 8,  9, -1,  0, -1],
    [ 3, -3,  8, -8, -7],
    [-6,  3, -1, -9,  8]
])