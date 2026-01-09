# Considerando o dicionário com chaves “x”, “y” e “z” para representar um vetor tridimensional, implemente uma função que calcule a soma de dois vetores, e um programa que peça valores para o usuário, use essa função, e mostre o resultado.

def soma(vetor1, vetor2):
    result = {}

    result["x"] = vetor1["x"] + vetor2["x"]
    result["y"] = vetor1["y"] + vetor2["y"]
    result["z"] = vetor1["z"] + vetor2["z"]

    return result

vetor1 = {}
vetor2 = {}

vetor1["x"] = float(input())
vetor1["y"] = float(input())
vetor1["z"] = float(input())

vetor2["x"] = float(input())
vetor2["y"] = float(input())
vetor2["z"] = float(input())

result_soma = soma(vetor1, vetor2)

print(result_soma)

