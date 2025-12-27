# Faça uma função que, dado um inteiro n, preencha uma matriz de tamanho nxn com o produto do valor da linha e da coluna de cada elemento.

def funcao(n):
    matriz_result = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(i * j)
        matriz_result.append(linha)
    
    return matriz_result

funcao(n=5)