nome = []
peso =[]
maior = 0
menor = 0

while True:
    nome.append(input('Nome: '))
    peso.append(float(input('Peso: ')))
    
    if maior == 0 or peso[-1] > maior:
        maior = peso[-1]
    if menor == 0 or peso[-1] < menor:
        menor = peso[-1] 
           
    continuar = input('Quer continuar? [S/N]').strip().lower()
    if continuar == 'n':
        break

print('=-' * 20)


print('Ao todo você cadastrou {} pessoas.'.format(len(nome)))
print('O maior peso foi de {} Kg. Peso de'.format(maior), end=' ')
for i in range(0, len(nome)):
    if peso[i] == maior:
        print(nome[i], end=' ...')
print()
print('O menor peso foi de {} Kg. Peso de'.format(menor), end=' ')
for i in range(0, len(nome)):
    if peso[i] == menor:
        print(nome[i], end=' ...')
