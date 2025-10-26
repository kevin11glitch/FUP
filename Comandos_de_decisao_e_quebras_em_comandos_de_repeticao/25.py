# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.


soma_final = 0
num_positivos = 0

while num_positivos < 10:
    num = int(input())
    if num > 0:
        soma_final += num
        num_positivos += 1

media =  soma_final / num_positivos
print(f"{media:.2f}")
    