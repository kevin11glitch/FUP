# Crie um programa que lê 10 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.

numeros = []

for y in range(10):
    numeros_entrada = int(input())
    numeros.append(numeros_entrada)

numeros_invertidos = numeros[::-1]

for i in numeros_invertidos:
    print(i)