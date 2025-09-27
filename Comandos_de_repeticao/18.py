# Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.

def funcao(x):
    p_fatorial = 1
    for i in range(1, x+1):
        p_fatorial *= i

    soma = 0
    
    string_num = str(p_fatorial)

    for i in string_num:
        soma += int(i)

    return soma

