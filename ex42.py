x1 = float(input('Primeiro segmento: '))
x2 = float(input('Segundo segmento: '))
x3 = float(input('Terceiro segmento: '))

if (x1 > abs(x2 - x3) and x1 < (x2 + x3)) or (x2 > abs(x1 - x3) and x1 < (x1 + x3)) or (x3 > abs(x2 - x1) and x3 < (x2 + x1)):
    if x1 == x2 and x2 == x3:
        print('Os segmentos acima PODEM formar um triangulo EQUILATERO')
    elif x1 == x2 or x1 == x3 or x2 == x3:
        print('Os segmentos acima PODEM formar um triangulo ISOSCELES')
    else:
        print('Os segmentos acima PODEM formar um triangulo ESCALENO')
    
else:
    print('Os segmentos acima NÃO podem formar triângulo!')