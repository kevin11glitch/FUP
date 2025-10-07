# Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

string = input()
string_final = ""

for i in string:
    valor_string = ord(i)
    
    ascii_novo = valor_string + 1

    string_final += chr(ascii_novo)

print(string_final)
