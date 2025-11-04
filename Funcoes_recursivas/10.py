# Escreva uma função recursiva que calcule a sequência dada por: F(1) = 1; F(2) = 2; e F(n) = 2*F(n − 1) + 3*F(n − 2).

def funcao(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
        
    if x > 2:
        return 2 * funcao(x - 1) + 3 * funcao(x - 2)