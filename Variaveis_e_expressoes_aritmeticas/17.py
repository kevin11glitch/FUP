# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

amigo1 = float(input())
amigo2 = float(input())
amigo3 = float(input())
premio = float(input())

valor_investimento = amigo1 + amigo2 + amigo3

divisao_amigos = premio / valor_investimento

ganhador1 = divisao_amigos * amigo1
ganhador2 = divisao_amigos * amigo2
ganhador3 = divisao_amigos * amigo3

print(f"{ganhador1:.2f}")
print(f"{ganhador2:.2f}")
print(f"{ganhador3:.2f}")
