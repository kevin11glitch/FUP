# Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1/1 + 1/2 + 1/3 … 1/n. Faça uma função que, dado um valor n inteiro positivo, calcule o valor de H(n).

def funcao(n):
    n_harmonico = 0

    for i in range(1, n+1):
        n_harmonico += (1/i) 

    return n_harmonico

