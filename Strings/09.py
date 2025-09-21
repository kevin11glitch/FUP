# Escreva um programa que recebe do usuário uma string S, um caractere C, e uma posição I e devolve o índice da primeira posição da string onde foi encontrado o caractere C. A procura deve começar a partir da posição I.

string = input()
carac = input()
posi = int(input())

indice = string.find(carac, posi)

print(indice)