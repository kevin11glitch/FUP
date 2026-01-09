# Faça um programa que leia um vetor com os dados de 5 carros: marca, ano e preço. Leia um valor p e mostre as informações de todos os carros com preço menor que p. Repita este processo até que seja lido um valor p = 0.

carros = []

for i in range(5):
    carro = {}
    carro['marca'] = input()
    carro['ano'] = int(input())
    carro['preco'] = int(input())

    carros.append(carro)

valor = int(input())

while valor != 0:
    zero = False
    
    for carro in carros:
        if carro['preco'] < valor:
            print(f"{{'modelo': '{carro['marca']}', 'ano': {carro['ano']}, 'preco': {carro['preco']:.1f}}}")            
            zero = True

    if not zero:
        pass

    valor = int(input())