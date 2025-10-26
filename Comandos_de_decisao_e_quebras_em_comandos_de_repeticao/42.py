# Ler uma frase e contar quantos caracteres são brancos. Não use nenhuma funcionalidade do python que já faça isso.

entrada = input()
contador = 0

for i in entrada:
    if i == " ":
        contador += 1
print(contador)