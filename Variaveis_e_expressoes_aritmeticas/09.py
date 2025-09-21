# Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.
import math
angulo_g = float(input())

radiano = (angulo_g * math.pi)/180

print(f"{radiano:.2f}")