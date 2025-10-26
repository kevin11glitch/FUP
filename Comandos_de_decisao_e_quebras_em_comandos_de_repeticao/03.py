# Ler 4 números inteiros e calcular a soma dos que forem par.

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
nFinal = 0
for i in n1,n2,n3,n4:
    if i % 2 == 0:
        nFinal += i

print(nFinal)