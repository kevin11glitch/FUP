"""
Crie uma função que, dados valores de m e n, retorne uma matriz de tamanho m × n, onde seus elementos são da forma: 
◦ A[i][j] = 2 * i + 7 * j - 2, se i < j;
◦ A[i][j] = 3 * i 2 − 1, se i = j;
◦ A[i][j] = 4 * i 3 − 5 * j 2 + 1, se i > j.
"""


def funcao(m, n):
    mat_result = []

    for i in range(m):
        linha = []
        for j in range(n):
            if i < j:
                elemento = 2 * i + 7 * j - 2
                linha.append(elemento)
            elif i == j:
                elemento = 3 * i**2 - 1
                linha.append(elemento)
            elif i > j:
                elemento = 4 * i**3 - 5 * j**2 + 1
                linha.append(elemento)
        mat_result.append(linha)
    
    return mat_result

def imprime(mat_result):
    for i in range(len(mat_result)):
        for j in range(len(mat_result)):
            print(f"{mat_result[i][j]}", end="")