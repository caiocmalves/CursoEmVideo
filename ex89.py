from statistics import mean


alunos = []
continuar = 's'
while continuar != 'n':
    notas = []
    alunos.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas)
    continuar = input('Quer continuar? [S/N] ')

print('=-' * 20)
print('No. NOME          MÉDIA')
print('-' * 30)

cont=0
for i in range(0, len(alunos) - 1, 2):
    print('{}   {}           {}'.format(cont, alunos[i], round(mean(alunos[i+1]),1)))
    cont += 1
    
print('-' * 30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if mostrar == 0:
        print(alunos[1])
    elif mostrar <= cont:
        print(alunos[mostrar * 2 + 1])
    elif mostrar > cont:
        continue
    elif mostrar == 999:
        break