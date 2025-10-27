# Determine se um determinado ano lido é bissexto, sabendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.


ano = int(input())

if ano % 400 == 0 or (ano % 4 == 0 and not ano % 100 == 0):
    print("Bissexto")
else:
    print("Nao bissexto")