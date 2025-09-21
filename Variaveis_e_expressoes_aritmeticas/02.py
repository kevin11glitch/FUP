# Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.
lado01 = float(input())
lado02 = float(input())

area = lado01 * lado02
perimetro = 2 * (lado01 + lado02)

print(f"{area:.2f}")
print(f"{perimetro:.2f}")