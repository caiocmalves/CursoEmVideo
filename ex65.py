n = 0
continuar = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
        
media = soma / cont
print()
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

