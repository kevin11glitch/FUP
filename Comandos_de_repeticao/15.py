# Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! . . . 1/n!.

def funcao(n):
    n_fatorial = 1
    e = 1

    for i in range(1, n+1):
        n_fatorial *= i
        e += (1/n_fatorial)
   

    return e

