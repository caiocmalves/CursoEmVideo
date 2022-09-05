n = int(input('Digite um número: '))

cont = 0
for i in range(1, n + 1):
    print(i, end=' ')
    if n % i == 0:
        cont += 1
        
print()
print('O numero {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO é primo')