# Escreva uma função recursiva SomaSerie(i,j,k). Esta função devolve a soma da série de valores no intervalo [i,j], com incremento k.

def SomaSerie(i, j, k):
    if i > j:
      return 0
    else:
      return i + SomaSerie(i + k, j, k)