# Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após a contagem.

game_over = True
num = 10
while game_over:
    print(num)
    if num != 0:
        num -= 1
    else:
        print("FIM!")
        game_over = False