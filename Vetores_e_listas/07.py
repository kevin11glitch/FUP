# Leia um vetor com 15 posições. Contar e escrever os valores pares desse vetor.

vetor = []
pares = []

for i in range(15):
    num = int(input())
    vetor.append(num)
    
for num in vetor:
    if num % 2 == 0:
        pares.append(num)

print(len(pares))

for p in pares:
    print(p)