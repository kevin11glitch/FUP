# Construa um dicionário com as seguintes informações de alunos: nome, número de matrícula e curso. Leia do usuário a informação de n alunos, armazene em um vetor e imprima os dados na tela.

dicionario = []

qtd = int(input(""))

for i in range(qtd):
    info = {}
    info["nome"] = input("")
    info["matricula"] = int(input(""))
    info["curso"] = input("")

    dicionario.append(info)

for info in dicionario:
    print(info)