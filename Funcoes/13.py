"""
Faça uma função que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
Calcule e retorne a quantia ganha por cada um dos ganhadores.
"""
def funcao(premio):
    ganhador1 = premio * (46/100)
    ganhador2 = premio * (32/100)
    ganhador3 = premio - ganhador1 - ganhador2

    return ganhador1, ganhador2, ganhador3
