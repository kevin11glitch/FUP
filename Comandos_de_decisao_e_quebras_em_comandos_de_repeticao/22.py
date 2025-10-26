# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com os pesos 5, 3, 2.

def funcao(x1, x2, x3, x4):
    mediaA = 0
    mediaP = 0
    if x4 == "A":
        mediaA = (x1+x2+x3) / 3
        return mediaA
    elif x4 == "P":
        mediaP = ((x1*5) + (x2*3) + (x3*2)) / (5+3+2)
        return mediaP
