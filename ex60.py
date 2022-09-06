f = int(input('Digite um número para calcular seu fatorial: '))

calculo = f
print('Calculando {}! = {}'.format(f, f), end=' ')
for i in range(f - 1, 0, -1):
    print('x {}'.format(i), end=' ')
    calculo *= i
print('= {}'.format(calculo)) 
