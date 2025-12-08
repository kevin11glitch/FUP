# Faça um vetor de tamanho 70 preenchido com o seguinte valor: (i + 5*i) % (i + 1) , sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.
vetor = []

for i in range(70):
    num = (i + 5*i) % (i +1)
    vetor.append(num)

print(vetor)