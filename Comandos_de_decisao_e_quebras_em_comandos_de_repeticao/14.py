"""
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
◦ adição (opção 1)
◦ subtração (opção 2)
◦ multiplicação (opção 3)
◦ divisão (opção 4)
◦ saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).
"""
def soma(x, y): #1
    return  x + y

def sub(x, y): #2
    return x - y

def mult(x, y): #3
    return x * y

def div(x, y): #4
    if y == 0:
        return "Erro, divisao por 0 é impossivel"
    return x / y

while True:
    escolha = int(input("1 - Adicao\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n5 - Saida\n"))

    if escolha == 5:
        break

    num1 = float(input())
    num2 = float(input())

    

    if escolha == 1:
        resultado = soma(num1, num2)
        print(f"{resultado:.2f}")
    elif escolha == 2:
        resultado = sub(num1, num2)
        print(f"{resultado:.2f}")
    elif escolha == 3:
        resultado = mult(num1, num2)
        print(f"{resultado:.2f}")
    elif escolha == 4:
        resultado = div(num1, num2)
        print(f"{resultado:.2f}")
    
            
