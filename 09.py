# Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).

def funcao(n):
    soma = 0
    for i in range(0, (n*2), 2):
        soma += i
    return soma 

