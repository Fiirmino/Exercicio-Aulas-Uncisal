salario = float(input('Informe o salário do funcionário: R$'))
if salario<=1320:
    inss = (salario*0.075)
    print(f'Desconto 7,5% INSS -R${inss:.2f}')

elif salario >=1320.01 and salario<=2571.29:
    inss = (salario*0.09)
    print(f'Desconto 9% INSS -R${inss:.2f}')
elif salario>=2571.30 and salario <=3856.94:
    inss = (salario*0.12)
    print(f'Desconto 12% INSS -R${inss:.2f}')
elif salario>=3856.95:
    inss = (salario*0.14)
    print(f'Desconto 14% INSS -R${inss:.2f}')

if salario <=2112:
    print('Isento de imposto de renda')
elif salario >=2112.01 and salario <=2826.65:
    irpf = (salario*0.075)
    print(f'Desconto de 7,5% de IRPF -R${irpf:.2f}')
    print(f'Salário líquido do funcionário R${salario-inss-irpf:.2f}')
elif salario >=2826.66 and salario <=3751.05:
    irpf = (salario*0.15)
    print(f'Desconto de 15% de IRPF -R${irpf:.2f}')
    print(f'Salário líquido do funcionário R${salario-inss-irpf:.2f}')
elif salario >=3751.06 and salario <=4664.68:
    irpf = (salario*0.225)
    print(f'Desconto de 22,5% de IRPF -R${irpf:.2f}')
    print(f'Salário líquido do funcionário R${salario-inss-irpf:.2f}')
elif salario >4664.68:
    irpf = (salario*0.275)
    print(f'Desconto de 27,5% de IRPF -R${irpf:.2f}')
    print(f'Salário líquido do funcionário R${salario-inss-irpf:.2f}')


