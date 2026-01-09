"""
Faça um programa que faça operações simples de números complexos:
◦ Crie e leia dois números complexos z e w, compostos por parte real e parte imaginária.
◦ Apresente a soma, subtração e produto entre z e w, nessa ordem, bem como o módulo de ambos. Cada operação deve ser feita em uma função diferente.
"""
import math
def soma(z, w):
    return z + w

def sub(z, w):
    return z - w

def prod(z, w):
    return z * w

def modulo(a):
    return abs(a)

def formatar(c):
    return {'real': c.real, 'imaginario': c.imag}


result = []

z_real = float(input())
z_imag = float(input())
z = complex(z_real, z_imag)

w_real = float(input())
w_imag = float(input())
w = complex(w_real, w_imag)

res_soma = soma(z, w)
res_sub = sub(z, w)
res_prod = prod(z, w)
res_modulo_z = modulo(z) 
res_modulo_w = modulo(w)

print(formatar(res_soma))
print(formatar(res_sub))
print(formatar(res_prod))
print(f"{res_modulo_z:.2f}")
print(f"{res_modulo_w:.2f}")




