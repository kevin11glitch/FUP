# Faça uma função que receba dois vetores. Retorne um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Esse vetor de retorno não deve conter números repetidos.

def funcao(vetor1, vetor2):
    vetor_interseccao = []

    for i in range(len(vetor1)):
        valor = vetor1[i]
        flag = False
        for j in range(len(vetor2)):
            if valor == vetor2[j]:
                flag = True
                break
        if flag:
            na_lista = False
            for z in range(len(vetor_interseccao)):
                if vetor_interseccao[z] == valor:
                    na_lista = True
                    break
            if not na_lista:
                vetor_interseccao.append(valor)

    return vetor_interseccao

funcao(vetor1=[1, 2, 3, 4, 5, 1, 2], vetor2=[1, 2, 3, 4, 5])