valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N]').strip().lower()
    if continuar == 'n':
         break

print('Você digitou {} elementos.'.format(len(valores)))
print('Os valores em ordem decrescente são {}'.format(sorted(valores, reverse=True)))
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')