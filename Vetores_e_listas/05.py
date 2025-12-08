# Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

numeros = []
numeros_quadrado = []

for i in range(10):
    entrada = float(input())
    numeros.append(entrada)

for u in numeros:
    print(f"{u:.2f}")

for y in range(10):
    numeros_quadrado.append(numeros[y] * numeros[y])

for j in numeros_quadrado:
    print(f"{j:.2f}")


