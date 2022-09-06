frase = input('Digite uma frase qualquer: ').lower().strip()

inverso = ''

for i in range(len(frase) - 1, -1, -1):
    inverso += frase[i]
    
print('O inverso de {} é {}'.format(frase, inverso))

if inverso == frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')


































"""
frase = input('Digite uma frase qualquer: ').lower().strip()
esarf = []
novo = []


for i in frase:
    esarf.append(i)

novo = esarf[::-1]
novafrase = ''
for i in range(0, len(novo)):
    novafrase += novo[i]

print('O inverso de {} é {}'.format(frase, novafrase))

if novafrase == frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
"""