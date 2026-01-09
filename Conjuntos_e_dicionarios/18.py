"""
Faça um programa que gerencie o estoque de um mercado e:
◦ Crie e leia um vetor de 5 produtos, com os dados: código (inteiro), nome (máximo 15 letras), preço e quantidade.
◦ Leia um pedido, composto por um código de produto e a quantidade. Localize este código no vetor e, se houver quantidade suficiente para atender ao pedido integralmente, atualize o estoque e informe o usuário. Repita este processo até ler um código igual a zero. Se, por algum motivo não for possível atender ao pedido, mostre uma mensagem informando que é “Impossivel atender ao pedido, produto sem estoque suficiente” ou “Impossivel atender ao pedido, codigo nao encontrado”.
◦ A cada passo, antes de ler o código, imprima o estoque do mercado.
"""
def verificar_estoque(codigo, quantidade, estoque):
    produto_encontrado = False

    for item in estoque:
        if item['codigo'] == codigo:
            produto_encontrado = True

            if item['quantidade'] >= quantidade:
                item['quantidade'] -= quantidade

            else:
                print("Impossivel atender ao pedido, produto sem estoque suficiente")
            
            break
            
    if not produto_encontrado:
        print("Impossivel atender ao pedido, codigo nao encontrado")

estoque = []

for i in range(5):
    mercado = {}
    mercado['codigo'] = int(input())
    mercado['nome'] = input()
    mercado['preco'] = float(input())
    mercado['quantidade'] = int(input())

    estoque.append(mercado)


while True:

    for i in estoque:
        print(i)

    cod_prod = int(input())

    if cod_prod == 0:
        break

    qtd = int(input())

    verificar_estoque(cod_prod, qtd, estoque)


