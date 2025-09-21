# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321.

num = int(input())

unidades = num % 10
dezenas = (num // 10) % 10
centenas = num // 100

num_final = (unidades * 100) + (dezenas * 10) + centenas

print(f"{num_final:.2f}")