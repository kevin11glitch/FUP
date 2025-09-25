# Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido.

def funcao(n):
    soma = 0

    for i in range(1, n+1):
        soma += i
    return soma


