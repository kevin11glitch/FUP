# Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.

entrada = input()
contador = 0

for i in entrada:
    if i == "1":
        contador += 1
print(contador)