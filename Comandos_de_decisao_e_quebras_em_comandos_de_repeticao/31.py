"""
Faça um programa que receba dois números. Calcule e mostre:
◦ A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
◦ A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados)
"""

num1 = int(input())
num2 = int(input())

soma_pares = 0
mult_pares = 1

inicio = 0
fim = 0

if num2 > num1:
    inicio = num1
    fim = num2
else:
    inicio = num2
    fim = num1

for i in range(inicio, fim+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        mult_pares *= i

print(soma_pares)
print(mult_pares)
