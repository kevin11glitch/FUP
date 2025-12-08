# Faça uma função que receba um vetor com as notas de vários alunos, e retorne a média geral, o desvio padrão (populacional), e quantos alunos estão com nota menor que 7.0.

def funcao(notas):
    soma = 0
    soma_quadrados = 0
    menor_sete = 0
    for num in notas:
        soma += num
        
    if len(notas) == 0:
        return "0.00", "0.00"
        
    media = soma/len(notas)
    
    for i in notas:
        diferenca = (i - media)**2
        soma_quadrados += diferenca 
        
        if i < 7:
            menor_sete += 1
        
    desvio_padrao = (soma_quadrados / len(notas))**0.5
    
    return media, desvio_padrao, menor_sete