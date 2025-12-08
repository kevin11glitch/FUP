# Faça um função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso. Exemplo: Data: 01/01/2000 , imprimir: 1 de janeiro de 2000.

def funcao(x):
    mes = ["", "janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    dia_x = x[0:2]
    dia_int = int(dia_x)
    mes_x = x[3:5]
    mes_int = int(mes_x)
    ano_x = x[6:10]


    return f"{dia_int} de {mes[mes_int]} de {ano_x}"


x = input("")
y = funcao(x)

print(y)