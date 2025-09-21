# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça uma função que receba quanto cada apostador investiu e o valor do prêmio, e retorne quanto cada um ganharia do prêmio com base no valor investido.

def funcao(amigo1, amigo2, amigo3, premio):
    valor_investimento = amigo1 + amigo2 + amigo3

    divisao_amigos = premio / valor_investimento

    ganhador1 = divisao_amigos * amigo1
    ganhador2 = divisao_amigos * amigo2
    ganhador3 = divisao_amigos * amigo3

    return ganhador1, ganhador2, ganhador3

