# Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

def soma(x, y): #1
    soma = x + y
    return soma

def sub(x, y): #2
    sub = x - y
    return sub

def mult(x, y): #3
    mult = x * y
    return mult

def div(x, y): #4
    div = x / y
    return div

num1 = float(input())
escolha = input()
num2 = float(input())


if escolha == "+":
    print(f"{soma(num1, num2):.2f}")

elif escolha == "-":
    print(f"{sub(num1, num2):.2f}")

elif escolha == "*":
    print(f"{mult(num1, num2):.2f}")

elif escolha == "/":
    print(f"{div(num1, num2):.2f}")

else:
    print("Escolha um operador")