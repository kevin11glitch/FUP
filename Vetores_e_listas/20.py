# Faça um programa que leia um vetor de 100 posições para números reais e, depois, um código inteiro. Se o código for 0, finalize o programa; se o código for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código seja diferente de 1 e 2 escreva uma mensagem informando que o código é inválido. O programa sempre deve pedir outro código, e terminar somente quando o código for 0.

vetor = []
for i in range(100):
    num = float(input(""))
    vetor.append(num)


while True:
    entrada = int(input(""))

    if entrada == 0:
        break
    if entrada == 1:
        for i in vetor:
            print(i)
    if entrada == 2:
        numeros_invertidos = vetor[::-1]
        for i in numeros_invertidos:
            print(i)
    if (entrada != 1) and (entrada != 2):
        print("Codigo invalido")
