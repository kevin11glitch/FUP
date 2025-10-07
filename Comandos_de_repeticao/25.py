# Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + … + (n2 + 1)/(n + 3)

def funcao(n):
    
    s = 0

    for i in range(1, n+1):
        
        termo = (i**2 +1)/ (i+3)
        s += termo

    return s

