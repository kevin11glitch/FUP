"""
Faça um programa para simular uma agenda de telefones. Para cada pessoa devem-se ter os seguintes dados: Nome, E-mail, Endereço (contendo campos para Rua, número, complemento, bairro, cep, cidade, estado, país), Telefone (contendo campo para DDD e número), Data de aniversário (contendo campo para dia, mês, ano), Uma string para alguma observação especial. O programa deve:
◦ Definir uma função para inserir uma pessoa: Cria uma nova pessoa e insere os dados definidos anteriormente.
◦ Definir uma função para buscar por primeiro nome: Imprime os dados da pessoa com esse nome (se tiver mais de uma pessoa, imprime todas).
◦ Definir uma função para buscar por mês de aniversário: Imprime os dados de todas as pessoas que fazem aniversário nesse mês.
◦ Definir uma função para buscar por dia e mês de aniversário: Imprime os dados de todas as pessoas que fazem aniversário nesse dia e mês.
◦ Definir uma função para imprimir agenda com as opções:
    ▪ Imprime nome, telefone e e-mail.
    ▪ Imprime todos os dados.
◦ O programa deve ter um menu principal oferecendo as opções acima. O menu deve ser outra função. Caso a opção seja 0, o programa encerra.
"""

agenda = []

def exibir_menu():
    print("1: Inserir uma pessoa")
    print("2: Buscar por primeiro nome")
    print("3: Buscar por mes de nascimento")
    print("4: Buscar por dia e mes de nascimento")
    print("5: Imprimir agenda")
    print("0: Sair")
    
   
    return int(input("Opcao: "))


def inserir_pessoa(agenda):
    pessoa = {}
    endereco = {}
    telefone = {}
    data = {}

    pessoa['nome'] = input("Nome: ")
    pessoa['email'] = input("E-mail: ")

    endereco['rua'] = input("Rua: ")
    endereco['numero'] = int(input("Numero: "))
    endereco['complemento'] = input("Complemento: ")
    endereco['bairro'] = input("Bairro: ")
    endereco['cep'] = input("CEP: ")
    endereco['cidade'] = input("Cidade: ")
    endereco['estado'] = input("Estado: ")
    endereco['pais'] = input("Pais: ")
    pessoa['endereco'] = endereco

    telefone['ddd'] = int(input("DDD: "))
    telefone['numero'] = input("Telefone: ")
    pessoa['telefone'] = telefone

    data['dia'] = int(input("Dia do nascimento: "))
    data['mes'] = int(input("Mes do nascimento: "))
    data['ano'] = int(input("Ano do nascimento: "))
    pessoa['nascimento'] = data

    pessoa['observacao'] = input("Observacao: ")

    agenda.append(pessoa)


def buscar_nome(nome, agenda):
    encontrados = []

    for pessoa in agenda:
        primeiro_nome = ""
        nome_completo = pessoa['nome']

        for letra in nome_completo:
            if letra == " ":
                break
            primeiro_nome += letra

        tamanho_busca = len(nome)
        prefixo_nome = primeiro_nome[:tamanho_busca]

        if prefixo_nome.lower() == nome.lower():
            encontrados.append(pessoa)
    
    return encontrados


def buscar_mes(mes, agenda):
    encontrados = []

    for pessoa in agenda:
        if pessoa['nascimento']['mes'] == mes:
            encontrados.append(pessoa)

    return encontrados


def buscar_dia_mes(dia, mes, agenda):
    encontrados = []

    for pessoa in agenda:
        if pessoa['nascimento']['dia'] == dia:
            if pessoa['nascimento']['mes'] == mes:
                encontrados.append(pessoa)

    return encontrados


def imprime_agenda(opcao, agenda):
    for pessoa in agenda:
        impressao = {}
        if opcao == 1:
            impressao = {
                'nome': pessoa['nome'],
                'telefone': pessoa['telefone'],
                'email': pessoa['email']
            }
            
            print(impressao)

        if opcao == 2:
            print(pessoa)


def exibir_menu_imprimir():
    print("1: Imprimir apenas nome, telefone e email")
    print("2: Imprimir todos os dados")

    return int(input("Opcao: "))


while True:

    opcao = exibir_menu()

    if opcao == 1:
        inserir_pessoa(agenda)
    
    elif opcao == 2:
        entrada = input("Primeiro nome: ")
        encontrados = buscar_nome(entrada, agenda)
        for pessoa in encontrados:
            print(pessoa)

    elif opcao == 3:
        mes = int(input("Mes de nascimento: "))
        encontrados = buscar_mes(mes, agenda)
        for pessoa in encontrados:
            print(pessoa)
    
    elif opcao == 4:
        dia = int(input("Dia do nascimento: "))
        mes = int(input("Mes do nascimento: "))
        encontrados = buscar_dia_mes(dia, mes, agenda)
        for pessoa in encontrados:
            print(pessoa)

    elif opcao == 5:
        escolha = exibir_menu_imprimir()
        if escolha not in [1, 2]:
            print("Opcao invalida")
        else:
            pessoas = imprime_agenda(escolha, agenda)

    elif opcao == 0:
        break

    if opcao not in [0, 1, 2, 3, 4, 5]:
        print("Opcao invalida")

