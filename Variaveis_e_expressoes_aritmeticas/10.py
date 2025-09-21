# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.

valorA = int(input())
valorB = int(input())
valorC = int(input())

soma_dos_quad = (valorA**2) + (valorB**2) + (valorC**2)
soma = valorA + valorB + valorC
quad = soma ** 2

print(f"{soma_dos_quad:.2f}")
print(f"{quad:.2f}")