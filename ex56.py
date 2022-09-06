media = 0
maior = 0
nomeMaior = ''
mulherAte20 = 0

for i in range(0, 4):
    print('----- {}ª PESSOA -----'.format(i + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    media += idade
    if sexo == 'M' and maior == 0:
        maior = idade
        nomeMaior = nome
    elif sexo == 'M' and idade > maior:
        maior = idade
        nomeMaior = nome
    if sexo == 'F' and idade < 20:
        mulherAte20 += 1
        
print('A média de idade do grupo é de {} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomeMaior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulherAte20))