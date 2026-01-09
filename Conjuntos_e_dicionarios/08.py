"""
Faça um programa que converta coordenadas polares para cartesianas:
◦ Crie e leia um ponto em coordenada polar, composto por raio (r) e ângulo (a) em radianos.
◦ Crie outro ponto, agora em coordenada cartesiana, composto por x e y, sabendo que x = r * cos(a) e y = r * sin(a).
No programa principal, leia um ponto em coordenada polar, mostre esse ponto, e mostre as coordenadas do ponto convertido para o plano cartesiano. A conversão deve ser feita em uma função.
"""
import math
coord_polar = {}
coord_cartesiana = {}

coord_polar['r'] = float(input())
coord_polar['a'] = float(input())

coord_cartesiana['x'] = coord_polar['r'] * math.cos(coord_polar['a'])
coord_cartesiana['y'] = coord_polar['r'] * math.sin(coord_polar['a'])

print(coord_polar)
print(coord_cartesiana)

