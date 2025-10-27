# Faça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. Nessa função, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos. Caso alguma verificação não seja válida, os retornos devem ser iguais a zero.


def funcao(x):

    dia = 0
    mes = 0
    ano = 0

    if (len(x) != 10) or (x[2] != '/' or x[5] != '/'):
        return 0, 0, 0

    else:
        for i in range(len(x)):
            caractere = x[i]

            if i == 0 or i == 1:
                if ord("9") >= ord(caractere) and ord(caractere) >= ord("0"):
                    novo_caractere = ord(caractere) - ord('0')
                    dia = (dia * 10) + novo_caractere
                else:
                    return 0, 0, 0
            elif i == 3 or i == 4:
                if ord("9") >= ord(caractere) and ord(caractere) >= ord("0"):
                    novo_caractere = ord(caractere) - ord('0')
                    mes = (mes * 10) + novo_caractere
                else:
                    return 0, 0, 0
            elif i >= 6:
                if ord("9") >= ord(caractere) and ord(caractere) >= ord("0"):
                    novo_caractere = ord(caractere) - ord('0')
                    ano = (ano * 10) + novo_caractere
                else:
                    return 0, 0, 0
        return dia, mes, ano
        