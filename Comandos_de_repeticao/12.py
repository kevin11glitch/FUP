# Escreva uma função que receba n e k tais que n ≥ k ≥ 0 e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)

def funcao(n, k):
    n_fatorial = 1
    k_fatorial = 1
    nk_fatorial = 1
    for i in range(1, n+1):
        n_fatorial *= i 
    for j in range(1, k+1):
        k_fatorial *= j 
    
    for y in range(1, (n-k)+1):
        nk_fatorial *= y

    coeficiente = n_fatorial/(k_fatorial * nk_fatorial)

    return coeficiente
    
