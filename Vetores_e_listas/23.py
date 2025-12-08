# Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.

def primo(x):
    if x < 0:
        x = x * -1
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

vetor = []
vetor_resultado = []

for i in range(10):
    num = int(input())
    vetor.append(num)

for i in range(10):
    valor = vetor[i]
    if primo(valor):
        vetor_resultado.append(valor)
        vetor_resultado.append(i)


for num in vetor_resultado:
    print(num)

