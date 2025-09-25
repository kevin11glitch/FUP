# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

n = int(input())

for i in range(1, (n *2 + 1), 2):
    print(i)