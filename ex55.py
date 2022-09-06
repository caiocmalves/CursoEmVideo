maior = 0
menor = 0
for i in range(0,5):
    peso = float(input('Pesoa da {}ª pessoa: '.format(i + 1)))
    if maior == 0:
        maior = peso
    elif peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso

print('O maior peso lido foi de {} Kg'.format(maior))
print('O menor peso lido foi de {} Kg'.format(menor))