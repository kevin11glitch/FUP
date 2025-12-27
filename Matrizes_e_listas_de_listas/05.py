# Dada uma matriz e um valor numérico, crie uma função que deverá fazer uma busca desse valor na matriz e, retornar a sua localização (linha e coluna) ou os valores -1, -1, caso o valor não esteja na matriz.

def funcao(mat, num):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if num == mat[i][j]:
                return i, j
    return -1, -1



funcao(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], num=3)
