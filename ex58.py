import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palite? '))

secreto = random.randint(0,10)

while secreto != palpite:
    if palpite < secreto:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
    elif palpite > secreto:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
else:
    print("PARABÉNS! Você me ganhou.")



