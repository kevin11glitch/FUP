# Faça um programa que receba dois números inteiros e imprima o maior deles, se por acaso os dois números forem iguais, imprima a mensagem “Numeros iguais”.

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print(n1)
elif n1 == n2:
    print("Numeros iguais")
else:
    print(n2)