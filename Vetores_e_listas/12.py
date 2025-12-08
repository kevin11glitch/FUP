# Faça uma uma função que receba um vetor com a nota de 15 alunos e e retorne tanto a média geral quanto o desvio padrão (populacional).

def funcao(notas):
    soma = 0
    soma_quadrados = 0

    for num in notas:
        soma += num
        
    if len(notas) == 0:
        return "0.00", "0.00"
        
    media = soma/len(notas)
    
    for i in notas:
        diferenca = (i - media)**2
        soma_quadrados += diferenca 
        
    desvio_padrao = (soma_quadrados / len(notas))**0.5
    
    return media, desvio_padrao