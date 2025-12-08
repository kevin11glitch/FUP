# Dado um vetor de n elementos, descubra se existem segmentos iguais máximos. Dois segmentos são iguais se seus elementos são iguais, em ordem, e eles são máximos se têm o maior tamanho possível. Determine as posições de início dos segmentos, bem como o tamanho dos segmentos iguais máximos, e imprima esses valores. Por exemplo, no vetor [7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4], o segmento [5, 4, 3] se repete duas vezes, começando nas posições 2 e 6, e o segmento [5, 4] se repete três vezes, começando nas posições 2, 6, e 10, mas o segmento [5, 4, 3] é máximo por que tem maior tamanho. Os segmentos devem ter tamanho pelo menos igual a 2. Não é necessário encontrar todas as ocorrências de segmentos iguais, o programa pode terminar depois que encontrar a primeira ocorrência máxima. Por exemplo, no vetor [7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4, 3], apesar do segmento [5, 4, 3] aparecer três vezes, nas posições 2, 6 e 10, o programa deve retornar apenas que o segmento apareceu nas posições 2 e 6, e que tem tamanho 3. Faça isso em uma função.


def funcao(vetor):
    n = len(vetor)

    for tamanho in range(n-1, 1, -1):
        for i in range(n - tamanho + 1):
            for j in range(i + 1, n - tamanho + 1):
                iguais = True
                for k in range(tamanho):
                    val1 = vetor[i+k]
                    val2 = vetor[j+k]

                    if val1 != val2:
                        iguais = False
                        break

                if iguais:
                    return i, j, tamanho
    return -1, -1, -1
funcao(vetor=[7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4])