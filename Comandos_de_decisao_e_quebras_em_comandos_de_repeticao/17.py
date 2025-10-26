# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
import math

while True:
    num = float(input())

    if num <= 0:
        break 
    quadrado = num ** 2
    cubo = num ** 3
    sqrt = math.sqrt(num)

    print(f"{quadrado:.2f}")
    print(f"{cubo:.2f}")
    print(f"{sqrt:.2f}") 


        

 

