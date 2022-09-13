lista = []

for i in range(0, 5):
    lista.append(int(input('Digite um valor para a Posição {}: '.format(i))))

print('=-' * 30)
print('Você digitou os valores {}'.format(lista))
maior = 0
for i in range(0,len(lista)):
    if maior == 0:
        maior = lista[i]
    elif maior != 0 and lista[i] > maior:
        maior = lista[i]

print('O maior valor digitado foi {} nas posições '.format(maior), end='')

for i in range(0,len(lista)):
    if lista[i] == maior:
        print('{}...'.format(i), end=' ')

print()
menor = 0
for i in range(0,len(lista)):
    if menor == 0:
        menor = lista[i]
    elif menor != 0 and lista[i] < menor:
        menor = lista[i]

print('O menor valor digitado foi {} nas posições '.format(menor), end='')

for i in range(0,len(lista)):
    if lista[i] == menor:
        print('{}...'.format(i), end=' ')