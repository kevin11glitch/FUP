# Crie uma função que, dado um número n, retorne uma matriz n×n. Preencha com 1 a diagonal principal e com 0 os demais elementos. Use comandos de repetição, mas não use operadores relacionais (comparações).


def function(n):
    matriz_result = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz_result.append(linha)

    
    for i in range(n):
        matriz_result[i][i] = 1
    
    return matriz_result


function(n=5)