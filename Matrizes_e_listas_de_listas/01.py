# Faça uma função que, dada uma matriz, retorne quantos valores maiores que 10 ela possui.

def funcao(matriz):
    cont = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 10:
                cont += 1
                

    return cont 

funcao(matriz=[[33,58,34,37,28], [97, 33, 59, 44, 20], [25, 56, 75, 56, 21], [65, 10, 11, 9, 12]])