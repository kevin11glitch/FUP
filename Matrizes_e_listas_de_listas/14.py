# Faça uma função que, dadas duas matrizes A e B de mesmo tamanho, calcule e retorne a matriz C = A + B. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

def funcao(mat1, mat2):
    mat3 = []

    for i in range(len(mat1)):
        elemento = 0
        linha = []
        for j in range(len(mat1[i])):
            elemento = mat1[i][j] + mat2[i][j]
            linha.append(elemento)
        mat3.append(linha)
    return mat3

def imprimir(mat3):
    for i in range(len(mat3)):
        for j in range(len(mat3)):
            print(f"{mat3[i][j]}", end="")


funcao(mat1=[[-10,  6, -6, -7,  5],[ -7,  6, -6,  9, -8],[  6,  4,  0,  4, -6],[  8,  5, -5, -5, 10]], mat2=[[  5,  0, 10, -2,  6],[  6, -4,  0,  7, -9],[-10, -7,  7,  6, -1],[-10, -8, -6, -10, -6]])