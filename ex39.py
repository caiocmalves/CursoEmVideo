from datetime import datetime

ano = int(input('Ano de nascimento: '))
year = datetime.today().strftime("%Y")

if ano < (2022-18):
    print('Você já deveria ter se alistado há {} anos.'.format((2022-18) - ano))
else:
    print('Ainda faltam {} anos para o alistamento.'.format(ano - (2022-18)))
    print('Seu alistamento será em {}.'.format(ano + 18))
    