# Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de seus divisores positivos diferentes de n. Construa um programa que verifica se um dado número é perfeito. Ex: 6 é perfeito, pois 1 + 2 + 3 = 6.


num = int(input())
soma_div = 0

for i in range(1, num):
    if num % i == 0:
        soma_div += i

if soma_div == num:
    print("Perfeito")
else:
    print("Nao perfeito")


