# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
num = float(input())

maior = num
menor = num

for i in range(9):
    num = float(input())
   

    if num > maior:
        maior = num

    elif num < menor:
        menor = num



print(f"{menor:.2f}")
print(f"{maior:.2f}")