# Digite um nome e imprima quantas letras diferentes tem esse nome.

nome = input()
contador = 0
lista = []

for i in nome:
    if i == " " or i == "-":
            continue
    existe = False
    for j in lista:
        
        if i == j:
            existe = True
            break
    if not existe:
        contador += 1
        lista.append(i)

print(contador)