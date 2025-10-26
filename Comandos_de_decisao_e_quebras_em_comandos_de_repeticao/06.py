# Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.

def verif_nota(x):
    if x < 0:
        return -1
    if x > 10:
        return -1
    return x

media = 0
erro = 0

for i in range(3):
    num = verif_nota(float(input()))
    if(num != -1):
        media += num
    else:
        erro = 1
        print("Nota invalida")
        break

if(erro == 0):
    print(f"{(media/3):.2f}")
