"""
Faça um programa que seja uma agenda de compromissos e:
◦ Crie e leia um vetor de 5 estruturas de dados com: compromisso e data. A data deve ser outra estrutura de dados contendo dia, mês e ano.
◦ Leia dois inteiros M e A e mostre todos os compromissos do mês M do ano A, ordenados do menor para o maior dia.
Repita o procedimento até ler M = 0.
"""

def compromissos(mm, aaaa, vetor):
    compromissos = []

    for item in vetor:
        if item['data']['mes'] == mm and item['data']['ano'] == aaaa:
            compromissos.append(item)
    
    n = len(compromissos)

    for i in range(n):
        for j in range(0, n - i - 1):
            dia_atual = compromissos[j]['data']['dia']
            proximo_dia = compromissos[j + 1]['data']['dia']

            if dia_atual > proximo_dia:
                temp = compromissos[j]
                compromissos[j] = compromissos[j + 1]
                compromissos[j + 1] = temp

    return compromissos


vetor = []

for i in range(5):
    compromisso = {}
    data = {}

    compromisso['compromisso'] = input("Descricao: ")
    data['dia'] = int(input("Dia: "))
    data['mes'] = int(input("Mes: "))
    data['ano'] = int(input("Ano: "))
    compromisso['data'] = data
    
    vetor.append(compromisso)

    
mm = int(input())

while mm != 0:
    aaaa = int(input())

    resultado = compromissos(mm, aaaa, vetor)

    if len(resultado) == 0:
        pass
    else:
        for item in resultado:
            print(item)

    mm = int(input())