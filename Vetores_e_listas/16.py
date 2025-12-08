# Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os elementos que não aparecem repetidos.

def funcao(vetor):
    vetor2 = []
    flag = False
    for i in range(len(vetor)):
        flag = False

        for j in range(len(vetor)):
            if i != j and vetor[i] == vetor[j]:
                flag = True

        if flag == False:
            vetor2.append(vetor[i])

    return vetor2

vetor_input = [10, 9, 8, 7, 6, 6, 7, 8, 9, 6]

print(funcao(vetor_input))
