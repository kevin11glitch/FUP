# Faça um programa para ler uma lista de nomes dos alunos de uma turma de até 5 alunos. O programa deve solicitar ao usuário os nomes dos alunos, sempre perguntando se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuário irá indicar um nome que ele deseja verificar se está presente na lista, e o programa deve procurar pelo nome (ou parte deste nome) e, se encontrar, deve exibir na tela o nome completo e o índice do vetor onde está guardado este nome.

lista_alunos = []

for i in range(5):
    nome = input("Aluno: ")
    lista_alunos.append(nome)


    if i < 4:
        pergunta = input("Deseja inserir novo aluno? [S/N] ").upper() 
        
        if pergunta == "S":
            continue
        else:
            break
nome_pesquisar = input("Aluno para pesquisa: ")

nome_pesquisar = nome_pesquisar.upper() 

tam_busca = len(nome_pesquisar)

for i in range(len(lista_alunos)):
    aluno_original = lista_alunos[i]
    aluno_upper = aluno_original.upper() 
    tam_aluno = len(aluno_upper)
    
    encontrou = False
    
    if tam_busca <= tam_aluno:
        for j in range(tam_aluno - tam_busca + 1):
            fatia = aluno_upper[j : j + tam_busca]
            
            if fatia == nome_pesquisar:
                encontrou = True
                break 

    if encontrou:
        print(aluno_original)
        print(i)