# Faça uma função que, dada uma matriz, divida todos os elementos de cada coluna pelo maior elemento daquela coluna que seja primo. Caso a coluna não possua um número primo, divida a coluna pelo menor número da coluna. Retorne a matriz resultado. Obs.: Números negativos também podem ser primos.
def primo(num, divisor=2):

    if num < 0:
        n = num * -1
    else:
        n = num

    if n < 1:
        return False
    if n == 1:
        return True
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    
    return primo(n, divisor + 1)
    

def funcao(mat):
    mat_result = []

    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[0])):
            linha.append(0)
        mat_result.append(linha)

    for j in range(len(mat[0])):
        maior_primo = 0
        menor_valor = mat[0][j]
        tem_primo = False

        for i in range(len(mat)):
            if mat[i][j] < menor_valor:
                menor_valor = mat[i][j]

            if primo(mat[i][j]):
                if tem_primo == False:
                    maior_primo = mat[i][j]
                    tem_primo = True
                else:
                    if mat[i][j] > maior_primo:
                        maior_primo = mat[i][j]

        if tem_primo:
            divisor = maior_primo
        else:
            divisor = menor_valor
        
        for i in range(len(mat)):
            if divisor != 0:
                resultado = mat[i][j] / divisor
            else:
                resultado = 0

            mat_result[i][j] = resultado
    
    return mat_result


dados=[
    [-7, -7, -6, -10, -2, 6, -5, 10, -2, 0, -7, 9, -9],
    [-3, 8, -3, -3, 10, 0, 4, 1, -7, -5, -2, 9, 1],
    [2, 6, -3, 1, -1, -10, 2, 2, -5, -1, 8, 8, -7],
    [1, -8, 3, -6, -10, 3, -5, -3, -3, 9, -2, 6, 1],
    [-1, -4, -3, 0, 5, -6, -1, 1, 1, -6, 7, 7, -1],
    [5, -7, 10, 2, 6, -8, -4, -3, 4, 5, -2, 4, 2],
    [0, 10, -10, -2, 6, 4, 6, -2, 8, 8, 1, 6, 0],
    [-6, -7, 0, 2, -5, 1, -9, 3, 5, 3, -5, 9, 0],
    [-9, 1, 8, -9, 1, -4, -5, 10, -8, 3, 6, 2, 10],
    [-10, -3, -5, -5, 8, 9, -8, 8, 1, 6, -2, 9, 1],
    [-5, -1, 9, 5, 6, 10, 4, 9, 2, 4, -9, 6, 8],
    [0, 0, -5, 3, 10, 5, -4, 2, -3, -7, -8, -1, 6]
]

resultado_final = funcao(dados)

def imprimir(mat_result):
    for i in range(len(mat_result)):
        for j in range(len(mat_result[0])):

            print(f"{mat_result[i][j]:.2f} ", end="")
        print()

imprimir(resultado_final)