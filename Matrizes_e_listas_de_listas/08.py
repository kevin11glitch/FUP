# Faça uma função que, dada uma matriz quadrada, calcule a soma dos elementos que estão acima da diagonal principal. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso. Para fazer a soma, utilize apenas comandos de repetição e não utilize expressões relacionais (comparações).

def funcao(mat):
    soma = 0

    for i in range(len(mat)):
        for j in range(i+1, len(mat)):
            soma += mat[i][j]
    return soma