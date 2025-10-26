# Ler três valores e imprimi-los na tela em ordem crescente.

def func(x,y,z):
    maior_num = x
    menor_num = x
    
    if maior_num < y:
        maior_num = y
    if menor_num > y:
        menor_num = y
    if maior_num < z:
        maior_num = z
    if menor_num > z:
        menor_num = z
    

    if x == maior_num:
        if y == menor_num:
            return menor_num, z, maior_num
    if x == maior_num:
        if z == menor_num:
            return menor_num, y, maior_num
    if y == maior_num:
        if z == menor_num:
            return menor_num, x, maior_num
    if y == maior_num:
        if x == menor_num:
            return menor_num, z, maior_num
    if z == maior_num:
        if x == menor_num:
            return menor_num, y, maior_num
    if z == maior_num:
        if y == menor_num:
            return menor_num, x, maior_num
    
        
menor_num, num_meio, maior_num = func(int(input()), int(input()), int(input()))

print(menor_num)
print(num_meio)
print(maior_num)