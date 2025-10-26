# Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.

entrada1 = input()
entrada2 = input()

primeira_str = ""

maior_str = len(entrada1)
menor_str = 0
if len(entrada2) > len(entrada1):
    maior_str = len(entrada2)
    menor_str = len(entrada1)

else: 
    maior_str = len(entrada1)
    menor_str = len(entrada2)


for i in range(menor_str):
    letra1 = ord(entrada1[i])
    letra2 = ord(entrada2[i])
    
    if letra1 == letra2:
        
        continue

    elif letra2 < letra1:
        primeira_str = entrada2
        break

    else:
        primeira_str = entrada1
        break

if primeira_str == "":
    if menor_str == len(entrada1):
        primeira_str = entrada1
    else:
        primeira_str = entrada2

print(primeira_str)