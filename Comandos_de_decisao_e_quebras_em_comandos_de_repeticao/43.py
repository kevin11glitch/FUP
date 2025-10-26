# Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.
nome = input()
idade = int(input())

maior_idade = idade
menor_idade = idade

nome_mais_velho = nome
nome_mais_novo = nome

while True:
    nome = input()
    idade = int(input())

    if idade < 0:
        break
    
    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

    if idade < menor_idade:
        menor_idade = idade
        nome_mais_novo = nome

print(nome_mais_novo)
print(menor_idade)  
print(nome_mais_velho)
print(maior_idade)

        