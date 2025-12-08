# Faça uma função que receba dois vetores de mesmo tamanho e calcule outro vetor contendo, nas posições pares o valores do primeiro vetor e nas posições ímpares os valores do segundo vetor.

def funcao(vetorA, vetorB):
    vetorC = []

    for i in range(len(vetorA)):
            vetorC.append(vetorA[i])
            vetorC.append(vetorB[i])
        
    return vetorC


funcao(vetorA = [1, 2, 3, 4, 5], vetorB = [6, 7, 8, 9, 10])