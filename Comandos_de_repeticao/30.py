# Faça um programa que receba uma palavra e a imprima de trás-para-frente.

palavra = input()
ultimo_indice = len(palavra) - 1
palavra_invertida = ""

for letra in range(ultimo_indice, -1, -1):
    palavra_invertida =palavra_invertida + palavra[letra]

print(palavra_invertida)