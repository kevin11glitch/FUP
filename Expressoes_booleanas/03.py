# Faça um programa que receba uma palavra e um caractere (vogal ou consoante) e imprima quantas vogais (a, e, i, o, u) possui essa palavra. Substitua todas as vogais da palavra dada pelo caractere dado, e imprima a nova palavra.

entrada = input()
caractere = input()
qtd_vogal = 0
palavra_nova = ""

for letra in entrada:
    if letra in "aeiou" or letra in "AEIOU":
        qtd_vogal += 1
        letra = caractere

    palavra_nova += letra
    

print(qtd_vogal)
print(palavra_nova)
    