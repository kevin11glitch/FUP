"""
Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a saída para n = 6 seria:
     *
    ***
   *****
  *******
 *********
***********
"""

def funcao(n):
    linha = "*"
    espaco_quant = 2*n-1
    for i in range(1, 2*n, 2):
        asterisco = linha*i

        print(asterisco.center(espaco_quant))

funcao(8)