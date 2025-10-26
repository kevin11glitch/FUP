# Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.

entrada = input()
saida = ""

for i in entrada:
    if i == "0":
        i = "1"
        saida += i
    else:
        saida += i

print(saida)