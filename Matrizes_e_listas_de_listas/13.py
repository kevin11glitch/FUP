# Crie uma função que, dada uma matriz de números reais, retorne um vetor unidimensional contendo a soma dos números de cada coluna da matriz.

def funcao(mat):
    result = []
    
    for j in range(len(mat[0])):
        soma = 0

        for i in range(len(mat)):
            soma += mat[i][j]

        result.append(soma)

    print(result)

funcao(mat = [[-9, -9,  7, -10,  8], [-3, -6,  0,  -7, -5], [10, -6,  2,  10, -3], [-8,  3,  8,   4,  5], [-6,  8,  4,   8, 10]])
        

