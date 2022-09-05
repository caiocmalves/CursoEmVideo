import random
from time import sleep

computador = random.randint(0,2)

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

player = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 10)
if computador == 0:
    print('Computador jogou PEDRA') 
elif computador == 1:
    print('Computador jogou PAPEL')
elif computador == 2:
    print('Computador jogou TESOURA')

if player == 0:
    print('Player jogou PEDRA') 
elif player == 1:
    print('Player jogou PAPEL')
elif player == 2:
    print('Player jogou TESOURA')
print('-=' * 10)

if computador == player:
    print('EMPATE')
elif computador == 0 and player == 2:
    print('Computador GANHOU')
elif computador == 1 and player == 0:
    print('Computador GANHOU')
elif computador == 2 and player == 1:
    print('Computador GANHOU')
elif player == 0 and computador == 2:
    print('Computador GANHOU')
elif player == 1 and computador == 0:
    print('Computador GANHOU')
elif player == 2 and computador == 1:
    print('Computador GANHOU')
