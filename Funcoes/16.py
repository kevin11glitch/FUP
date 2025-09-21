# Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas, minutos e segundos.

def funcao(seg):
    num_horas = seg // 3600
    seg -= num_horas * 3600

    num_min = seg // 60
    seg -= num_min * 60
    num_seg = seg

    return num_horas, num_min, num_seg

