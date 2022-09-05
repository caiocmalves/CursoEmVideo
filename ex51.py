print('=' * 10)
print('10 TERMOS DE UMA PA')
print('=' * 10)

inicio = int(input('Primeiro termo: '))
passo = int(input('Razão: '))
seguinte = inicio

print(inicio, end=' -> ')
for i in range(0, 9):
    seguinte += passo
    print(seguinte, end=' -> ')
    
print('Acabou')