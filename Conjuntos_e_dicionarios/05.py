"""
Crie um dicionário representando os alunos de um determinado curso. O dicionário deve conter a matrícula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova.
◦ Permita ao usuário entrar com os dados de 5 alunos.
◦ Encontre o aluno com maior nota da primeira prova.
◦ Encontre o aluno com maior média geral.
◦ Encontre o aluno com menor média geral.
◦ Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 7 para aprovação.
"""

def aprovado(media):
    for nota in alunos:
        if nota["media"] >= 7:
            print(f"Aluno {nota['nome']} esta aprovado com media {nota['media']:.2f}")
        else:
            print(f"Aluno {nota['nome']} esta reprovado com media {nota['media']:.2f}")

alunos = []
maior_nota = 0
aluno_maior_nota = ""

maior_media = 0
aluno_maior_media = ""

menor_media = 11
aluno_menor_media = ""

for i in range(5):
    info = {}

    info["matricula"] = int(input())
    info["nome"] = input()
    info["nota1"] = float(input())
    info["nota2"] = float(input())
    info["nota3"] = float(input())
    info["media"] = (info["nota1"] + info["nota2"] + info["nota3"]) / 3

    alunos.append(info)


for nota in alunos:
    if nota["nota1"] > maior_nota:
        maior_nota = nota["nota1"]
        aluno_maior_nota = nota["nome"]

    if nota["media"] > maior_media:
        maior_media = nota["media"]
        aluno_maior_media = nota["nome"]

    if nota["media"] < menor_media:
        menor_media = nota["media"]
        aluno_menor_media = nota["nome"]


print(f"Aluno {aluno_maior_nota} tem a maior nota1: {maior_nota:.2f}")
print(f"Aluno {aluno_maior_media} tem a maior media: {maior_media:.2f}")
print(f"Aluno {aluno_menor_media} tem a menor media: {menor_media:.2f}")
aprovado(info["media"])

