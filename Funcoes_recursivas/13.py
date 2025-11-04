# Implemente a função A definida recursivamente por: A(m, n) = n + 1, se m = 0; A(m, n) = A(m − 1, 1), se m > 0 e n = 0; A(m, n) = A(m − 1, A(m, n − 1)) , se m > 0 e n > 0.

def A(x1, x2):
    if x1 == 0:
        return x2 + 1
    if x1 > 0 and x2 == 0:
        return A(x1-1, 1)
    if x1 > 0 and x2 > 0:
        return A(x1-1, A(x1, x2-1))
    