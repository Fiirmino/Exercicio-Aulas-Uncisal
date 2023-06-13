num = int(input('Informe um número'))
primo = 1
for x in range (2,num):
    if (num % x == 0):
        primo = 0
if (primo ==1):
    print('o numero é primo')
else:
    print('o numero não é primo')