print('GERADOR PA')
print('=' * 10)

inicio = int(input('Primeiro termo: '))
passo = int(input('Razão: '))
seguinte = inicio
cont = 1
print(inicio, end=' -> ')
while cont < 10:
    seguinte += passo
    print(seguinte, end=' -> ')
    cont += 1
    
print('PAUSA')

plus = 10

while plus > 0:
    plus = int(input('Quanto termos você quer mostrar a mais? '))
    for i in range(plus):
        seguinte += passo
        print(seguinte, end=' -> ')
    print('PAUSA')