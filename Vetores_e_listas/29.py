# Faça uma função que, dado um vetor de números reais, ordene os elementos desse vetor do maior para o menor, e retorne o vetor ordenado. Não use nenhuma função de ordenação do python.

#Algorítmo Bubble-sort
def funcao(vetor):

    for i in range(len(vetor)):
        for j in range(0, len(vetor)-i-1):
            #verificação: se o numero da direita for maior que o da esquerda, então está no lugar errado
            if vetor[j] < vetor[j+1]:
                #troca de posição, número da direita vai pra esquerda e vice-versa
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor


funcao(vetor=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])