"""
Faça um programa que controla o consumo de energia dos eletrodomésticos de uma casa e:
◦ Crie e leia 5 eletrodomésticos que contêm nome (máximo 15 letras), potência (real, em kW) e tempo ativo por dia (real, em horas).
◦ Leia um tempo t (em dias), calcule e mostre o consumo total (em kWh) na casa e o consumo relativo de cada eletrodoméstico (consumo/consumo total) nesse período de tempo. Apresente este último dado em porcentagem.
"""
def total(eletrodomesticos, tempo):
    consumo_total = 0

    for i in range(len(eletrodomesticos)):
        potencia = eletrodomesticos[i]['potencia']
        t_diario = eletrodomesticos[i]['tempo']

        consumo_ind = potencia * t_diario * tempo

        eletrodomesticos[i]['consumo_final'] = consumo_ind

        consumo_total += consumo_ind

    print(f"{consumo_total:.2f}")

    for eletro in eletrodomesticos:
        if consumo_total > 0:
            porcentagem = (eletro['consumo_final'] / consumo_total) * 100
        else:
            porcentagem = 0
        
        print(f"{eletro['nome']}: {porcentagem:.2f}")

eletrodomesticos = []

for i in range(5):
    eletro = {}

    eletro['nome'] = input()
    eletro['potencia'] = float(input())
    eletro['tempo'] = float(input())

    eletrodomesticos.append(eletro)


tempo = int(input())

resultado = total(eletrodomesticos, tempo)


