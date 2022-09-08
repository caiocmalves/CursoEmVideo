import random

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0
while True:
    n = int(input('Diga um valor: '))
    pc = random.randint(0,9)
    escolha = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    if ((n + pc) % 2) == 0 and escolha == 'P':
        print('-' * 20)
        print('Voce jogou {} e o computador {}. Total de {} DEU PAR.'.format(n,pc, n+pc))
        cont += 1
    elif ((n + pc) % 2) != 0 and escolha == 'I':
        print('-' * 20)
        print('Voce jogou {} e o computador {}. Total de {} DEU IMPAR.'.format(n,pc, n+pc))
        cont += 1
    else:
        if((n + pc) % 2) == 0:
            print('Voce jogou {} e o computador {}. Total de {} DEU PAR.'.format(n,pc, n+pc))
        elif((n + pc) % 2) != 0:
            print('Voce jogou {} e o computador {}. Total de {} DEU IMPAR.'.format(n,pc, n+pc))
        
        print('-' * 20)
        print('Voce PERDEU!')
        break
    
    print('Voce VENCEU!')
    print('Vamos jogar novamente...')
    
print('=-' * 20)
print('GAME OVER! Voce venceu {} vezes.'.format(cont))