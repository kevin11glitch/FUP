# Escreva um programa que leia as coordenadas x e y de pontos no R^2 e calcule sua distância da origem (0, 0).
import math

x = float(input())
y = float(input())

distancia = ((x * x) + (y * y)) ** 0.5

print(f"{distancia:.2f}")