# Faça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. Não use nenhuma funcionalidade do python que já faça isso.

entrada = input()
saida = ""

for i in entrada:

    if i == "a":
        saida = "*" + saida
    elif i == "A":
        saida = "*" + saida    

    else: 
        saida = i + saida

print(saida)