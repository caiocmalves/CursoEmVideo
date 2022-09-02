print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

x1 = float(input('Primeiro segmento: '))
x2 = float(input('Segundo segmento: '))
x3 = float(input('Terceiro segmento: '))

if x1 > abs(x2 - x3) and x1 < (x2 + x3):
    if x2 > abs(x1 - x3) and x1 < (x1 + x3):
        if x3 > abs(x2 - x1) and x3 < (x2 + x1):
            print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO podem formar triângulo!')