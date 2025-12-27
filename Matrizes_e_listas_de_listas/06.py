# Escreva uma função que, dadas duas matrizes de mesmo tamanho, e retorne uma terceira matriz com os maiores valores de cada posição das matrizes de entrada.
def funcao(mat1, mat2):
    mat_result = []

    for i in range(len(mat1)):
        linha = []
        for j in range(len(mat1[i])):
            
            if mat1[i][j] > mat2[i][j]:
                linha.append(mat1[i][j])
            else:
                linha.append(mat2[i][j])

        mat_result.append(linha)

    return mat_result

def imprime(mat_result):
    for i in range(len(mat_result)):
        for j in range(len(mat_result)):
            print(f"{mat_result[i][j]}", end="")