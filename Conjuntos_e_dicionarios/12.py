# Faça um programa que leia os dados de 10 alunos (Nome, matricula, Média Final), armazenando em um vetor. Uma vez lidos os dados, divida estes dados em 2 novos vetores, o vetor dos aprovados e o vetor dos reprovados, considerando a média mínima para a aprovação como sendo 5.0. Exibir na tela os dados do vetor de aprovados, seguido dos dados do vetor de reprovados.

alunos = []
aprovados = []
reprovados = []

for i in range(10):
    aluno = {}

    aluno['nome'] = input()

    aluno['matricula'] = int(input())
    aluno['media'] = float(input())

    alunos.append(aluno)

for aluno in alunos:
    if aluno['media'] >= 5:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

for aluno in aprovados:
    print(aluno)

for aluno in reprovados:
    print(aluno)
