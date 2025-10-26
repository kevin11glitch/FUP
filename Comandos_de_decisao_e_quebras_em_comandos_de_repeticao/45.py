"""
O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente uma função que faça uso desse Código de César, entre com uma string e a quantidade de posições e retorne a string codificada. Exemplo:
String: A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO
Nova string com 3 posições: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
Observação: caso a letra codificada passe da letra Z, ela deve voltar para o início do alfabeto.
"""


def funcao(str, num):
    saida = ""

    for i in str:
        if 'A' <= i <= "Z":
            cod_i = ord(i)
            num_letra = cod_i - ord('A')
            posicao_i = (num_letra + num) % 26
            novo_cod_i = posicao_i + ord('A')
            saida = saida + chr(novo_cod_i)

        elif 'a' <= i <= "z":
            cod_i = ord(i)
            num_letra = cod_i - ord('A')
            posicao_i = (num_letra + num) % 26
            novo_cod_i = posicao_i + ord('A')
            saida = saida + chr(novo_cod_i)

        else:
            saida = saida + i
    return saida

entrada = input()
num_posicoes = int(input())

funcao
