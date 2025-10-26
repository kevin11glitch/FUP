# Faça uma função que retorne o maior fator primo de um número.

def funcao(x):
    maior_fator_primo = 0
    divisor = 2

    if x == 1:
        maior_fator_primo = x

    while x > 1:
        if x % divisor == 0:
            maior_fator_primo = divisor
            x = x // divisor
        else:
            divisor += 1

    return maior_fator_primo



                

