# Escreva uma função que, dada uma semente e um tamanho n, gere uma matriz quadrada de tamanho n x n com inteiros aleatórios no intervalo [1, 20]. Depois, transforme a matriz gerada numa matriz triangular inferior, ou seja, atribua zero a todos os elementos acima da diagonal principal. Retorne a matriz original e a matriz transformada. Não use nenhuma comparação.
import random

def funcao(x, n):
    matriz_aleatoria = []
    matriz_triangular = []

    random.seed(x)

    for i in range(n):
        linha = []
        linha_triang = []

        for j in range(i+1):
            num = random.randint(1, 20)
            linha.append(num)
            linha_triang.append(num)


        for j in range(i+1, n):
            num = random.randint(1, 20)
            linha.append(num)
            linha_triang.append(0)

        matriz_aleatoria.append(linha)
        matriz_triangular.append(linha_triang)



    return matriz_aleatoria, matriz_triangular

def imprimir(matriz_aleatoria, matriz_triangular):
    for i in range(len(matriz_aleatoria)):
        for j in range(len(matriz_aleatoria)):
            print(f"{matriz_aleatoria[i][j]:4}", end="")
        print()
    
    for i in range(len(matriz_triangular)):
        for j in range(len(matriz_triangular)):
            print(f"{matriz_triangular[i][j]:4}", end="")
        print()

m1, m2 = funcao(x=4, n=5)
imprimir(m1, m2)
