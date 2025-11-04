# Faça uma função recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. Exemplo de superfatorial: sf (4) = 1! * 2! * 3! * 4! = 288.

def f(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * f(n-1)
        
def sf(n):
    if n == 0 or n == 1:
        return 1
    else:
        return f(n) * sf(n-1)