# Ler três valores e determinar o maior entre eles.

n1 = float(input())
n2 = float(input())
n3 = float(input())


if n1 > n2 and n1 > n3:
    print(f"{n1:.2f}")

elif n2 > n3 and n2 > n1:
    print(f"{n2:.2f}")

elif n3 > n1 and n3 > n2:
    print(f"{n3:.2f}")

elif n1 == n2 and n2 == n1:
    print(f"{n1:.2f}")