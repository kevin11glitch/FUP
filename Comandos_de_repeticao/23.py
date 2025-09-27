# Faça um programa para exibir a tabuada de 1 a 9 .

n = 1

for y in range(1, 10):
    for i in range(0, 10):
        print(f"{n} + {i} = {n+i}")
    n +=1
