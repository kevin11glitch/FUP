# Implemente a função h definida recursivamente por: h(m, n) = m + 1, se n = 1; h(m, n) = n + 1, se m = 1, h(m, n) = h(m, n − 1) + h(m − 1, n), se m > 1, n > 1.

def h(x, y):
    if y == 1:
        return x + 1
    if x == 1:
        return y + 1
    if x > 1 and y > 1:
        return h(x, y -1) + h(x - 1, y)