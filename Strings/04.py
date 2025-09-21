# Escreva um programa que recebe uma string S e inteiros não-negativos I e J e imprima o segmento S[I...J].

entrada = str(input())

inteiro1 = int(input())
inteiro2 = int(input())

string = entrada[(inteiro1-1):inteiro2]
print(string)