# Faça uma função que receba dois vetores. Retorne um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números que estão em qualquer um dos vetores. Esse vetor de retorno não deve conter números repetidos.

def funcao(vetor1, vetor2):
    vetor_uniao = []
    uniao = vetor1 + vetor2

    for i in uniao:
        if i not in vetor_uniao:
            vetor_uniao.append(i)    

    return vetor_uniao

funcao(vetor1=[1, 2, 1, 2, 3], vetor2=[1, 2, 3, 4, 5])