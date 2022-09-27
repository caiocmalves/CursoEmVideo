lista = []
for i in range(1, 8):
    lista.append(int(input('Digite o {}º valor: '.format(i))))

par = []
impar = []
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
        
print('=-' * 20)
print('Os valores pares digitados foram: {}'.format(sorted(par)))
print('Os valores ímpares digitados foram: {}'.format(sorted(impar)))


#######################################################################
"""num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
"""
