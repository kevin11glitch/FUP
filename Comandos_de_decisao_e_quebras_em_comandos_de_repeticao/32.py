# Faça um algoritmo que, dados dois números inteiros, seja capaz de obter o quociente inteiro da divisão entre o maior e o menor deles. Não use a operação de divisão (/), nem a operação de divisão inteira (//) e nem a operação de resto da divisão inteira (%).

num1 = int(input())
num2 = int(input())

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

contador = 0
if menor == 0:
    print("Divisao impossivel")

else:
    while maior >= menor:
        maior -= menor
        contador += 1

print(contador)
