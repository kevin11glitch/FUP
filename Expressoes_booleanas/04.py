# Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

num = int(input())

if num % 3 == 0 and num % 5 == 0:
    print(False)

elif num % 3 == 0 or num % 5 == 0:
    print(True)

else:
    print(False)