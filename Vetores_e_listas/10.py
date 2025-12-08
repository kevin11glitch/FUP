# Leia um vetor de 20 inteiros e atribua 0 para todos os elementos que possuírem valores negativos.

vetor = []

for i in range(20):
    num = int(input())
    vetor.append(num)

for num in vetor:
    if num < 0:
        num = 0
        
    print(num)