
print('\033[4:30:47mSIMULADOR DE ENTREGAS ON-LINE\033[m')
print('')

km = int(input('\033[1:30:47mInforme a distância a ser percorrida em (Km):\033[m'))
if km <= 500:
    print(f'\033[1mO melhor transporte para percorrer {km} Km é o transporte terrestre!!!')
else:
    print('\033[1m transporte aéreo é o mais recomendado')