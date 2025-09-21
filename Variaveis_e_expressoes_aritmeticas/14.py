# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

num = int(input())

num_1 = num // 1000
num_2 = (num // 100) % 10
num_3 = (num // 10) % 10
num_4 = num % 10

print(f"{num_1}")
print(f"{num_2}")
print(f"{num_3}")
print(f"{num_4}")