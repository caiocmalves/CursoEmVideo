from datetime import datetime

nascimento = int(input('Ano de nascimento: '))

anoAtual = datetime.today().strftime("%Y")

idade = int(anoAtual) - nascimento

if idade <= 9:
    print('Sua categoria é mirim')
elif idade <= 14:
    print('Sua categoria é infantil')
elif idade <= 19:
    print('Sua catergoria é júnior')
elif idade <= 25:
    print('Sua catergoria é senior')
else:
    print('Sua catergoria é master')