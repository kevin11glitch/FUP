# Faça um programa que preencha um vetor de tamanho 100, com os 100 primeiros naturais que não são múltiplos de 7 ou que terminam com 7.

vetor = []
num = 1

while len(vetor) < 100:
    if (num % 7 == 0) or (num % 10 == 7) or(num % 100 == 7):
        pass
    else:
        vetor.append(num)
    num += 1
print(vetor)