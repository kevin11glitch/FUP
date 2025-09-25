# Faça um programa que leia 10 inteiros e imprima sua média.

media = 0

for i in range(1, 11):
    num = float(input())
    media += num/10

print(f"{media:.2f}")