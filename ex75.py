n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

x = (n1, n2, n3, n4)
cont = 0
posi = 0
pares = []
for i in range(0,4):
    if x[i] % 2 == 0:
        pares.append(x[i])
    
print('O valor 9 apareceu {} vezes'.format(x.count(9)))
print('O valor 3 apareceu na {}ª posição'.format(x.index(3)+1))
print('Os valores pares digitados foram {}'.format(pares))