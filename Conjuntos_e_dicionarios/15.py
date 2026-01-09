# Faça um programa que leia um vetor com dados de 5 livros: título, autor e ano. Procure um livro por título, perguntando ao usuário qual título deseja buscar. Mostre os dados de todos os livros encontrados. O título procurado não precisa ser exato, ou seja, os livros encontrados devem ser aqueles que contêm o título buscado.

def procurar_livro(pesquisa, livros):
    tem = []

    for livro in livros:
        if pesquisa.lower() in livro['titulo'].lower():
            tem.append(livro)
    return tem


vetor = []

for i in range(5):
    livro = {}
    livro['titulo'] = input()
    livro['autor'] = input()
    livro['ano'] = int(input())

    vetor.append(livro)


palavra = input()

resultado = procurar_livro(palavra, vetor)

for i in resultado:
    print(i)