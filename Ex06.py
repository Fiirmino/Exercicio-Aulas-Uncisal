#SISTEMA DE APROVAÇÃO DE EMPRÉSTIMO

idade = int(input('Qual a idade do cliente ?'))
salario_mensal = float(input('Insira o valor do seu salário mensal: R$'))
emprestimo = float(input('Valor solicitado R$'))

if salario_mensal>=2000 and emprestimo<=10*salario_mensal and idade>=18 and idade<=65:
    print('Empréstimo aprovado !!!')
else:
    print('Empréstimo negado pela política de crédito')