import random

jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

x = []

for i in range(1, jogos + 1):
    x =[]
    while len(x) < 6:
        a = random.randrange(1,60)
        if a not in x:
            x.append(a)
        
    print(f'Jogo {i}: {x}')