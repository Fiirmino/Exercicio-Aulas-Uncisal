#SISTEMA DE VENDAS COM DESCONTO PROGRESSIVO

valor_total = float(input('Qual o valor total da compra? R$'))

if valor_total>=100 and valor_total<200:
    desconto = valor_total*0.10
    print(f'Desconto de 10% aplicado: Novo valor --> R${valor_total-desconto:.2f}')
elif valor_total>=200 and valor_total<500:
    desconto = valor_total*0.20
    print(f'Desconto de 20% aplicado com sucesso: Novo valor --> R${valor_total-desconto:.2f}')
elif valor_total>500:
    desconto = valor_total*0.30
    print(f'Desconto de 30% aplicado com sucesso: Novo valor --> R${valor_total-desconto:.2f}')
else:
    print('Valor de compra inválido')
