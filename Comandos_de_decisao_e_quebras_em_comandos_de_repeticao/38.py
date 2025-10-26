# Crie uma função que diga se duas strings são iguais ou não, analisando caractere a caractere.


def funcao(x1, x2):

    if len(x1) != len(x2):
        return False
    
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            return False
        
    return True

    

funcao("teste", "kk")