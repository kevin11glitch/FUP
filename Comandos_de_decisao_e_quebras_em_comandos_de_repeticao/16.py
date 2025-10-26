# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

num = int(input())


if num < 0:
    maior = num
    menor = num

else:    
    maior = num
    menor = num
    while True:
        num = int(input())

        if num < 0:
            break 

        if num > maior:
            maior = num

        elif num < menor:
            menor = num

    print(maior)
    print(menor)
        