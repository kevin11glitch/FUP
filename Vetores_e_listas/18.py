# Faça uma função que receba dois vetores, A e B, de mesmo tamanho. Crie um novo vetor denominado C calculando C = A – B (a diferença elemento a elemento). Retorne o vetor C.

def funcao( vetorA, vetorB):
    vetorC = []
    
    for i in range(len(vetorA)):
        vetorC.append(vetorA[i] - vetorB[i])

    
    return vetorC

vetorA = [10, 9, 8, 7, 6]
vetorB = [6, 7, 8, 9, 6]

funcao(vetorA, vetorB)