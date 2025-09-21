""" 
Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

valor = float(input())
gndr1 = valor * (46/100)
gndr2 = valor * (32/100)
gndr3 = valor - gndr1 - gndr2

print(f"{gndr1:.2f}")
print(f"{gndr2:.2f}")
print(f"{gndr3:.2f}")


