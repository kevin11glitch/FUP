# Faça um programa que armazene em um dicionário os dados de um funcionário de uma empresa, compostos de: Nome, Idade, Sexo (M/F), CPF, Data de Nascimento, Código do Setor onde trabalha (0-99), Cargo que ocupa (string de até 30 caracteres) e Salário. Os dados devem ser digitados pelo usuário, armazenados no dicionário e exibidos na tela.

funcionario = {}

funcionario['nome'] = input()
funcionario['idade'] = int(input())
funcionario['sexo'] = input()
funcionario['cpf'] = input()
funcionario['nascimento'] = input()
funcionario['setor'] = int(input())
funcionario['cargo'] = input()
funcionario['salario'] = float(input())

print(funcionario)