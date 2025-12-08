# Faça uma função que receba dois vetores. Retorne um vetor que seja a diferença entre os 2 vetores anteriores, ou seja, que contém os números que estão no primeiro vetor mas não no segundo vetor. Esse vetor de retorno não deve conter números repetidos.

def funcao(vetor1, vetor2):
    vetor_diferenca = []
    
    for i in vetor1:
        if i not in vetor2:
            if i not in vetor_diferenca:
                vetor_diferenca.append(i)

    return vetor_diferenca

funcao(vetor1=[1, 2, 3, 4, 5], vetor2=[1, 2, 1, 2, 3])