"""
Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
◦ 1: Média entre os números digitados
◦ 2: Diferença do maior pelo menor
◦ 3: Produto entre os números digitados
◦ 4: Divisão do primeiro pelo segundo
Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.
"""

num1 = float(input())
num2 = float(input())
num_escolha = int(input())


if num_escolha == 1:
    print(f"{((num1+num2)/2):.2f}")

elif num_escolha ==2:
    if num1 > num2:
        print(f"{(num1-num2):.2f}")
    else:
       print(f"{(num2-num1):.2f}")

elif num_escolha == 3:
    print(f"{num1 * num2:.2f}")


elif num_escolha == 4:
    if num2 == 0:
        print("Erro")
    else:
        print(f"{(num1 / num2):.2f}")
        
else:
    print("Erro")