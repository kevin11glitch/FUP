# Faça uma função que gere uma matriz m × n de inteiros aleatórios (gerados a partir de uma semente), e calcule um vetor contendo, nos elementos pares, a média dos elementos das linhas pares da matriz e, nos elementos ímpares, a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. Retorne a matriz e o vetor. A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como parâmetros para a função.
import random
def funcao(m, n, seed, x, y):
    matriz = []
    vetor = []
    random.seed(seed)

    for i in range(m):
        linha = []
        for j in range(n):
            num = random.randint(x, y)
            linha.append(num)
        matriz.append(linha)

        if i % 2 == 0:
            soma = 0
            for num in linha:
                soma += num
            media = soma / n
            vetor.append(media)

        else:
            qtd = 0
            for num in linha:
                if num < 0 and num % 3 == 0:
                    qtd += 1
            vetor.append(qtd)

    return matriz, vetor


def imprimir(matriz, vetor):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(f"{matriz[i][j]:4}", end="")
        print()
    

    print(f"{vetor}")


m1, m2 = funcao(m=4, n=4, seed=0, x=-20, y=20)
imprimir(m1, m2)
