# Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

n = int(input())
num = float(input())
maior = num
menor = num

for i in range(n-1):
    num = float(input())

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"{menor:.2f}")
print(f"{maior:.2f}")