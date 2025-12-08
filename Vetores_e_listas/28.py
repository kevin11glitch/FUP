# Faça um programa para ler 12 inteiros DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados na ordem que forem sendo lidos, mas caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Exibir na tela o vetor final que foi digitado.


vetor = []

for i in range(12):
    num = int(input())

    while num in vetor:
        print(f"Numero {num} ja existe, escreva outro")
        num = int(input())

    vetor.append(num)

print(vetor)

