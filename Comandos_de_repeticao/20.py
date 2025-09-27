"""
Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. Por exemplo, a saída para n = 4 seria:
*
**
***
****
***
**
*
"""

def funcao(n):
    linha = "*"

    for i in range(1, n+1):
        print(linha*i)

    for i in range(n-1, 0, -1):
        print(linha*i)
 

