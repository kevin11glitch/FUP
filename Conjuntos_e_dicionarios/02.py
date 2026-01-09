"""
Faça um programa que preencha as informações dos modelos de cinco carros (exemplos de modelos: Fusca, Gol, Vectra, etc.) juntamente com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre:
◦ O modelo de carro mais econômico;
◦ Quantos quilômetros cada um dos carros cadastrados percorre com 50 litros de combustível;
◦ Quantos litros de combustível cada um dos carros cadastrados consomem para percorrer uma distância de 1.000 quilômetros.
"""

carros = []

for i in range(5):
    carro_atual = {}
    carro_atual["modelo"] = input("")
    carro_atual["consumo"] = float(input(""))

    carros.append(carro_atual)


mais_economico = ""
maior_eficiencia = 0


for carro in carros:

    if carro["consumo"] > maior_eficiencia:
        maior_eficiencia = carro["consumo"]
        mais_economico = carro["modelo"]

print(f"Carro mais economico: {mais_economico}")

for carro in carros:
    distancia_50 = carro["consumo"] * 50
    print(f"Carro {carro['modelo']} percorre {distancia_50:.2f} kms com 50 litros")

for carro in carros:
    litros = 1000 / carro["consumo"]

    print(f"Carro {carro['modelo']} precisa de {litros:.2f} litros para percorrer 1000 kms")