# Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.

entrada = input()
sem_vogais = ""

for i in entrada:
    if i in 'aeiou' or i in "AEIOU":
        continue

    sem_vogais += i 

print(sem_vogais)
