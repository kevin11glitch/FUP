# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

salario = float(input())
prestacao = float(input())
salario_20_por_cento = salario * (20/100)

if prestacao > salario_20_por_cento:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")
