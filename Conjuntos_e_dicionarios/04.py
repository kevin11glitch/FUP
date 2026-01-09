"""
Escreva um trecho de código para fazer a criação dos novos tipos de dados conforme solicitado abaixo:
◦ Data: composto de dia, mês e ano.
◦ Horário: composto de hora, minutos e segundos.
◦ Compromisso: composto de uma data, horário e texto que descreve o compromisso.
Leia n compromissos. Crie uma função que, dadas duas datas, retorne se a primeira ocorre antes da segunda ou não. Crie outra função semelhante, mas para comparar horários. Mostre os compromissos em ordem de data e horário.
"""

def data_antes(d1, d2):
    if d1["ano"] != d2["ano"]:
        return d1["ano"] < d2["ano"]
    if d1["mes"] != d2["mes"]:
        return d1["mes"] < d2["mes"]
    return d1["dia"] < d2["dia"]

def horario_antes(h1, h2):
    if h1["hora"] != h2["hora"]:
        return h1["hora"] < h2["hora"]
    if h1["minuto"] != h2["minuto"]:
        return h1["minuto"] < h2["minuto"]
    return h1["segundo"] < h2["segundo"]

geral = []
qtd = int(input())

for i in range(qtd):
    dia = {}
    dia["dia"] = int(input("Dia: "))
    dia["mes"] = int(input("Mes: "))
    dia["ano"] = int(input("Ano: "))

    h = {}
    h["hora"] = int(input("Hora: "))
    h["minuto"] = int(input("Minuto: "))
    h["segundo"] = int(input("Segundo: "))

    descricao = input("Descricao: ")
    
    compromisso = {
        "data": dia,
        "horario": h,
        "descricao": descricao,
    }

    geral.append(compromisso)

n = len(geral)

for i in range(n):
    for j in range(0, n - i - 1):
        comp1 = geral[j]
        comp2 = geral[j+1]

        trocar = False

        if data_antes(comp2["data"], comp1["data"]):
            trocar = True
        elif (comp1["data"] == comp2["data"]) and horario_antes(comp2["horario"], comp1["horario"]):
            trocar = True
        
        if trocar:
            geral[j], geral[j+1] = geral[j+1], geral[j]


for item in geral:
    print(item)