# Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4 dígitos separados, cada um em uma variável diferente. Não utilize strings.

def funcao(x):
    num_1 = x // 1000
    num_2 = (x // 100) % 10
    num_3 = (x // 10) % 10
    num_4 = x % 10

    return num_1, num_2, num_3, num_4