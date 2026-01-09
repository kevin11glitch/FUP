# Utilizando um dicionário, faça um programa que permita a entrada de nome, endereço e telefone de 5 pessoas e os imprima em ordem alfabética.
pessoas = []

for i in range(5):
    pessoa = {}

    pessoa['nome'] = input()
    pessoa['endereco'] = input()
    pessoa['telefone'] = input()

    pessoas.append(pessoa)

n = len(pessoas)

for i in range(n):
    for j in range(0, n - i - 1):
        if pessoas[j]['nome'] > pessoas[j + 1]['nome']:
            pos_atual = pessoas[j]

            pessoas[j] = pessoas[j + 1]

            pessoas[j + 1] = pos_atual

for pessoa in pessoas:
    print(pessoa)