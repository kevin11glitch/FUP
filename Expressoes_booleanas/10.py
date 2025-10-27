# Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).

def funcao(x, y):
    resto = 0
    if x > y:
        maior = x
        menor = y
        
    else:
        maior = y
        menor = x

    while True:
        if (maior % menor) == 0:
            return menor
        else:
            resto = maior % menor
            maior = menor
            menor = resto