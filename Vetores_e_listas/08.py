# Leia um vetor com 15 posições. Somar e mostrar os números que são ímpares.

vetor = []
impares =[]
soma = 0
for i in range(15):
    num = int(input())
    vetor.append(num)
    
for num in vetor:
    if (num % 2) != 0:
        impares.append(num)

for num in impares:
    soma += num
    
print(soma)

for num in impares:
    print(num)