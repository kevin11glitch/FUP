# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

numeros = []

for y in range(6):
    numeros_entrada = int(input())
    numeros.append(numeros_entrada)

for i in numeros:
    print(i)