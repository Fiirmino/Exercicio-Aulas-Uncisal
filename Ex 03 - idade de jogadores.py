#VERIFICADOR DE IDADE PARA JOGO (18 ANOS)


from datetime import datetime

hoje = datetime.now()
nascimento = input('\033[1:4:35:40mInsira a data de nascimento (dd/mm/aa):\033[m ')
nascimento = datetime.strptime(nascimento, '%d/%m/%Y')

if hoje.month < nascimento.month or hoje.day < nascimento.day and hoje.month == nascimento.month:

    idade = (hoje.year-nascimento.year-1)

else:
    idade = (hoje.year-nascimento.year)

if idade>=18:
    print('\033[1:37mPode jogar o jogo, bem-vindo 😉 !\033[m')
else:
    print(f'\033[1:37mInfelizmente você não pode jogar o jogo 😕 Você possui apenas {idade} anos !\033[m')







