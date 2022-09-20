valores = []
valor = 0
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
        
    continuar = input('Quer continuar? [S/N]').strip().lower()
    if continuar == 'n':
         break

print('A lista completa é {}'.format(valores))
print('A lista de pares é {}'.format(par))
print('A lista de ímpares é {}'.format(impar))