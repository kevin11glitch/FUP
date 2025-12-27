# Faça uma função que, dada uma matriz, divida todos os elementos de cada linha pelo maior elemento em módulo daquela linha. Retorne a matriz resultado.

def funcao(mat):
    mat_result = []

    for i in range(len(mat)):
        linha = []
        maior_num = 0

        for j in range(len(mat[i])):
            valor_temp = mat[i][j]
            
            if mat[i][j] < 0:
                valor_temp = mat[i][j] * -1

            if valor_temp > maior_num:
                maior_num = valor_temp

        for k in range(len(mat[i])):
            if maior_num != 0:
                elemento = mat[i][k] / maior_num
            else:
                elemento = 0

            linha.append(elemento)

        mat_result.append(linha)
    
    return mat_result

def imprimir(mat_result):
    for i in range(len(mat_result)):
        for j in range(len(mat_result)):
            print(f"{mat_result[i][j]:.2f}", end="")

funcao(mat=[
    [-7, -7, -6, -10, -2, 6, -5, 10, -2, 0, -7, 9, -9],
    [-3, 8, -3, -3, 10, 0, 4, 1, -7, -5, -2, 9, 1],
    [2, 6, -3, 1, -1, -10, 2, 2, -5, -1, 8, 8, -7],
    [1, -8, 3, -6, -10, 3, -5, -3, -3, 9, -2, 6, 1],
    [-1, -4, -3, 0, 5, -6, -1, 1, 1, -6, 7, 7, -1],
    [5, -7, 10, 2, 6, -8, -4, -3, 4, 5, -2, 4, 2],
    [0, 10, -10, -2, 6, 4, 6, -2, 8, 8, 1, 6, 0],
    [-6, -7, 0, 2, -5, 1, -9, 3, 5, 3, -5, 9, 0],
    [-9, 1, 8, -9, 1, -4, -5, 10, -8, 3, 6, 2, 10],
    [-10, -3, -5, -5, 8, 9, -8, 8, 1, 6, -2, 9, 1],
    [-5, -1, 9, 5, 6, 10, 4, 9, 2, 4, -9, 6, 8],
    [0, 0, -5, 3, 10, 5, -4, 2, -3, -7, -8, -1, 6]
])