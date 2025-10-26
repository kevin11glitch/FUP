# O numero 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e 552 = 3025. Elaborar um algoritmo que verifique todos os números de quatro algarismos que apresentem essa propriedade. Não use operações com strings.


for i in range(1000, 10000):
    parte1 = i // 100
    parte2 = i % 100
    soma = parte1 + parte2

    if soma**2 == i:
        print(i)
