# Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.
num_seg = int(input())

num_horas = num_seg // 3600
num_seg -= num_horas * 3600

num_min = num_seg // 60
num_seg -= num_min * 60
seg = num_seg


print(f"{num_horas}")
print(f"{num_min}")
print(f"{seg}")