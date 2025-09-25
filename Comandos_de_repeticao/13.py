"""
O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
◦ F1 = 1
◦ F2 = 1
◦ Fn = Fn−1 + Fn−2 para n> 2
Faça uma função que receba um valor inteiro n e calcule e Fn.
"""

def funcao(n):
    f1 = 1
    f2 = 1
    y = 1
    for i in range(3, n+1):
        y = f2 + f1
        f1 = f2
        f2 = y

    return y


