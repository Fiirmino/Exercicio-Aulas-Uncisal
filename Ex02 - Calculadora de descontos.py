print('\033[1:30:47mCALCULE SEU DESCONTO !\033[m')


preco_original = float(input('\033[1:4mInforme o preço do produto: R$'))
desconto = float(input('\033[1:4mInforme o percentual de desconto em %: '))
valor_final = preco_original-(preco_original*(desconto/100))
print (f'\033[30:47mO valor final da compra será R${valor_final:.2f}\033[m')