"""
Dados três valores inteiros, A , B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, verificar se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos:
◦ O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
◦ Chama-se equilátero o triângulo que tem três lados iguais.
◦ Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
◦ Recebe o nome de escaleno o triângulo que tem três lados diferentes.
"""

a = int(input())
b = int(input())
c = int(input())

if a > b + c or c > b + a or b > a + c:
    print("Nao triangulo")

elif a == b and b == c:
    print("Triangulo equilatero")

elif (a == b and c != a and c != b) or (b == c and a != b and a != c) or (a == c and b != a and b != c):
    print("Triangulo isosceles")

elif a != b and b != c:
    print("Triangulo escaleno")