# Faça uma função que receba 2 números inteiros positivos e calcule o Mínimo Múltiplo Comum (MMC).
def funcao(x, y):

    if x > y:
        maior = x
        menor = y
    elif y > x:
        maior = y
        menor = x

    if x == y:
        return x
    else:
        while True:
            if not (maior % x == 0 and maior % y ==0):
                maior += 1
            else:
                return maior

funcao(7, 7)