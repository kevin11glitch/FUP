# Faça um programa para ler a nota de 15 alunos e armazene em um vetor, calcule e imprima a média geral.

notas = []
soma = 0
media = 0
for i in range(15):
    num = float(input())
    notas.append(num)

for num in notas:
    soma += num

media = soma/len(notas)

print(f"{media:.2f}")