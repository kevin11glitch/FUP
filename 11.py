# Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.
def funcao(num):
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i 
    return fatorial

