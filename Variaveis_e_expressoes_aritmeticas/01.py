# Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como taxa de câmbio US$ 1,00 = R$5,27. Leia um valor em Dólares pelo teclado e mostre o correspondente em Reais.

CAMBIO = 5.27
dolar = float(input())
real = dolar * CAMBIO

print(f"{real:.2f}")