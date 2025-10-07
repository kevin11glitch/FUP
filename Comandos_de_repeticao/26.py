# Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n . Calcule o valor do seno desse ângulo usando a respectiva série de Taylor: sin(x) = x – x3/3! + x5/5! - … + (-1)n (x^(2n+1))/(2n+1)!.
def fatorial(y):
    fatorial = 1

    for i in range(1, y+1):
        fatorial *= i
    return fatorial

def funcao(x, n):
    seno_x = 0
    for i in range(n+1):
        termo = ((-1)**i) * (x**(2*i+1)) / fatorial(2*i+1)
        seno_x += termo
    return seno_x

funcao(1.570796327, 6)