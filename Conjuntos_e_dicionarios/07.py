# Faça um programa que realize a leitura dos seguintes dados relativos a um conjunto de alunos: Matricula, Nome, Código da Disciplina, Nota1 e Nota2. O tamanho da turma deve ser dado pelo usuário. Após ler todos os dados digitados, e depois de armazená-los em um vetor de dicionários, exiba na tela a listagem final dos alunos com as suas respectivas médias finais (use uma média ponderada: Nota1 com peso=1.0 e Nota2 com peso=2.0). Para cada aluno, inclua a média no dicionário.
def media(nota1, nota2):
    media = ((nota1 * 1) + (nota2 * 2)) / 3
    return media

alunos = []

qtd = int(input())


for i in range(qtd):
    aluno = {}
    aluno['matricula'] = int(input())
    aluno['nome'] = input()
    aluno['codigo'] = input()
    aluno['nota1'] = float(input())
    aluno['nota2'] = float(input())
    aluno['media'] = media(aluno['nota1'], aluno['nota2'])

    alunos.append(aluno)

for aluno in alunos:
    print(aluno)