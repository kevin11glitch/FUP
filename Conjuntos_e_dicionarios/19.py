"""
Defina os dicionários cujas representações gráficas são dadas na figura a seguir:
◦ Permita ao usuário entrar com dados para preencher 5 cadastros.
◦ Encontre a pessoa com maior idade entre os cadastrados
◦ Encontre as pessoas do sexo masculino
◦ Encontre as pessoas com salário maior que 1000.
◦ Imprima os dados da pessoa cuja identidade seja igual a um valor fornecido pelo usuário
"""

def maior_idade(lista_pessoas):
    maior_idade = -1
    pessoa_mais_velha = {}

    for pessoa in lista_pessoas:
        if pessoa['idade'] > maior_idade:
            maior_idade = pessoa['idade']
            pessoa_mais_velha['idade'] = pessoa
            
    
    return pessoa_mais_velha


def sexo(lista_pessoas):
    pessoa_masc = []
    for pessoa in lista_pessoas:
        if pessoa['sexo'].lower() == "masculino":
            pessoa_masc.append(pessoa)

    return pessoa_masc


def salario(lista_pessoas):
    pessoas_salario = []

    for pessoa in lista_pessoas:
        if pessoa['salario'] > 1000:
            pessoas_salario.append(pessoa)

    return pessoas_salario


def verificar_id(entrada, lista_pessoas):
    id_busca = str(entrada)

    for pessoa in lista_pessoas:
        if pessoa['identidade'] == id_busca:
            return pessoa
    return ""


lista_pessoas = []

for i in range(5):
    pessoa = {}
    endereco = {}

    pessoa['nome'] = input("Nome: ")
    endereco['rua'] = input("Rua: ")
    endereco['bairro'] = input("Bairro: ")
    endereco['cidade'] = input("Cidade: ")
    endereco['estado'] = input("Estado: ")
    endereco['cep'] = input("CEP: ")
    pessoa['endereco'] = endereco
    pessoa['salario'] = float(input("Salario: "))
    pessoa['identidade'] = input("Identidade: ")
    pessoa['cpf'] = input("CPF: ")
    pessoa['civil'] = input("Estado Civil: ")
    pessoa['telefone'] = input("Telefone: ")
    pessoa['idade'] = int(input("Idade: "))
    pessoa['sexo'] = input("Sexo: ")

    lista_pessoas.append(pessoa)

pessoa_mais_velha = maior_idade(lista_pessoas)
pessoas_sexo_masc = sexo(lista_pessoas)
pessoas_salario_1000 = salario(lista_pessoas)


print(f"Pessoa com maior idade:\n{pessoa_mais_velha['idade']}")

print(f"Pessoas do sexo masculino:")
for pessoa in pessoas_sexo_masc:
    print(pessoa)

print(f"Pessoas com salario maior que 1000:")
for pessoa in pessoas_salario_1000:
    print(pessoa)

identidade = int(input("Identidade: "))
identidade_bateu = verificar_id(identidade, lista_pessoas)

print(identidade_bateu)
