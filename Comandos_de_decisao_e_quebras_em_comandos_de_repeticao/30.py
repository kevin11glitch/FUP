# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

qtd_num = int(input())
num = int(input())
contador = 1
maior = num

for i in range(1, qtd_num):
    num = int(input())

    if num > maior:
        maior = num
        contador = 1
    elif num == maior:
        contador += 1
    
print(maior)
print(contador)
