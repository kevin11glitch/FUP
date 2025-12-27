# Crie uma função que, dada uma matriz, retorne o maior valor e a sua localização (linha e coluna).


def funcao(mat):
    linha = 0
    coluna = 0
    maior_valor = mat[0][0]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > maior_valor:
                maior_valor = mat[i][j]      
                linha = i
                coluna = j

    return maior_valor, linha, coluna


funcao(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
