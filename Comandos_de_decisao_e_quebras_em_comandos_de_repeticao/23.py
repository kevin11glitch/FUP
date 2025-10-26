# Faça um programa que escreva na tela, de 1 até 100 usando o while.
game_over = True
number = 1
while game_over:
    print(number)
    if number <= 99:
        number += 1
    else:
        game_over = False