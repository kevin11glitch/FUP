# Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.

salario = float(input())

novo_salario = salario + (salario * (21.37/100))

print(f"{novo_salario:.2f}")