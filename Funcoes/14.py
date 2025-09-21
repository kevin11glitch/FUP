# Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999). Retorne outro número formado pelos dígitos invertidos do número lido. Exemplo: Entrada = 123, Saída = 321. Não utilize strings.

def funcao(x):
    unidade = x % 10
    dezena = (x // 10) % 10
    centena = x // 100

    novo_x = (unidade * 100) + (dezena * 10) + centena
    return novo_x

