salario = float(input('Informe o salário bruto do funcionário: '))
inss = (salario*0.14)
irpf = (salario*0.225)
if salario<=1320:
    inss = (salario * 0.075)

elif salario>1320 and salario<=2571.29:
    inss = (salario * 0.9)

elif salario>2571.30 and salario <=3856.94:
    inss = (salario * 0.12)

elif salario>=3856.95:
    inss = (salario * 0.14)

