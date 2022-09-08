
homens = 0
mais18 = 0
mulherAte20 = 0

while True:
    print('------------------------------')
    print('   CADASTRE UMA PESSOA')
    print('------------------------------')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').lower().strip()[0]
    if sexo == 'm':
        homens += 1
    if idade > 18:
        mais18 += 1
    if sexo == 'f' and idade < 20:
        mulherAte20 += 1
    print('------------------------------')
    continuar = input('Quer continuar? [S/N] ').lower().strip()[0]
    if continuar == 'n':
        break

print('Total de pessoas com mais de 18 anos: {}'.format(mais18))
print('Ao todo temos {} homens cadastrados.'.format(homens))
print('E temos {} mulheres com menos de 20 anos.'.format(mulherAte20))