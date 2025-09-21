# Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.

temp_c = float(input())

temp_f = temp_c * (9/5) + 32

print(f"{temp_f:.2f}")