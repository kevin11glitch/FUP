# Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9...
import math
def funcao(x):
    raiz = math.sqrt(x)
    if raiz == int(raiz):
        return True
    else:
        return False
    
