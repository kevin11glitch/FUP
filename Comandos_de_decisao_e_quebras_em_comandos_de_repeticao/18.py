# Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.
def funcao(x):
    dia = str(int(x[:2]))
    mes_num = int(x[3:5])
    ano = str(int(x[6:]))
    mes = "dezembro"

    if mes_num == 1:
        mes = "janeiro"
    elif mes_num == 2:
        mes = "fevereiro"
    elif mes_num == 3:
        mes = "marco"
    elif mes_num == 4:
        mes = "abril"
    if mes_num == 5:
        mes = "maio"
    elif mes_num == 6:
        mes = "junho"
    elif mes_num == 7:
        mes = "julho"
    elif mes_num == 8:
        mes = "agosto"
    if mes_num == 9:
        mes = "setembro"
    elif mes_num == 10:
        mes = "outubro"
    elif mes_num == 11:
        mes = "novembro"

    return f"{dia} de {mes} de {ano}"
