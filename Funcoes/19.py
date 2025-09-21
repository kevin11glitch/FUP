# Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
def funcao(num):
    nota_100 = 100
    nota_50 = 50
    nota_20 = 20
    nota_10 = 10
    nota_5 = 5
    nota_2 = 2
    nota_1 = 1

    qtd_100 = num // nota_100
    num = num % nota_100

    qtd_50 = num // nota_50
    num = num % nota_50

    qtd_20 = num // nota_20
    num = num % nota_20

    qtd_10 = num // nota_10
    num = num % nota_10

    qtd_5 = num // nota_5
    num = num % nota_5

    qtd_2 = num // nota_2
    num = num % nota_2

    qtd_1 = num // nota_1
    num = num % nota_1

    return qtd_100, qtd_50, qtd_20, qtd_10, qtd_5, qtd_2, qtd_1