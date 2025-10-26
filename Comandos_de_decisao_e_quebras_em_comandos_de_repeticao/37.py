# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.
import math
def simplificar(x1, x2):

    maiorfator = math.gcd(x1, x2)

    x1 = x1 // maiorfator
    x2 = x2 // maiorfator
    return x1, x2

