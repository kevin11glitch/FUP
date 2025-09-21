# Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real. 

entrada = int(input())
valor = entrada
qtd_notas = 0

nota_100 = 100
nota_50 = 50
nota_20 = 20
nota_10 = 10
nota_5 = 5
nota_2 = 2
nota_1 = 1

qtd_100 = entrada // nota_100
entrada = entrada % nota_100

qtd_50 = entrada // nota_50
entrada = entrada % nota_50

qtd_20 = entrada // nota_20
entrada = entrada % nota_20

qtd_10 = entrada // nota_10
entrada = entrada % nota_10

qtd_5 = entrada // nota_5
entrada = entrada % nota_5

qtd_2 = entrada // nota_2
entrada = entrada % nota_2

qtd_1 = entrada // nota_1
entrada = entrada % nota_1

qtd_notas = qtd_100 + qtd_50 + qtd_20 + qtd_10 + qtd_5 + qtd_2 + qtd_1

print(int(qtd_100))
print(int(qtd_50))
print(int(qtd_20))
print(int(qtd_10))
print(int(qtd_5))
print(int(qtd_2))
print(int(qtd_1))
