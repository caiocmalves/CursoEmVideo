x1 = float(input('Primeira nota: '))
x2 = float(input('Segunda nota: '))

media = (x1+x2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(x1,x2, media))

if media >= 7:
    print('O aluno está aprovado')
elif media < 7 and media >= 5.0:
    print('O aluno está de recuperação')
else:
    print('o Aluno está reprovado')