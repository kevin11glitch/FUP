"""
Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Exemplos:
           ovo
           arara
           Socorram-me, subi no onibus em Marrocos.
           Anotaram a data da maratona
"""

entrada = input()
frase_limpa = ""

verificacao = ""


for i in entrada:
    if i >= "a":
        if i <= "z":
            frase_limpa = frase_limpa + i

    if i >= "A":
        if i <= "Z":
            num_letra = ord(i)
            distancia = ord('a') - ord('A')
            novo_num_letra = num_letra + distancia
            num_letra_minusculo = chr(novo_num_letra)

            frase_limpa = frase_limpa + num_letra_minusculo

for j in frase_limpa:
    verificacao = j + verificacao
    
if frase_limpa == verificacao:
    print(True)
else:
    print(False)
            