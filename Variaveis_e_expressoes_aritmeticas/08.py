# Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.

vel_kmh = float(input())

convert = vel_kmh/3.6

print(f"{convert:.2f}")