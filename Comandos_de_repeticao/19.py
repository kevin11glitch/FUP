"""
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).
!
!!
!!!
!!!!
!!!!!
"""

def funcao(x):
    for i in range(1, x+1):
        exclamacao = "!"* i
        print(exclamacao)
